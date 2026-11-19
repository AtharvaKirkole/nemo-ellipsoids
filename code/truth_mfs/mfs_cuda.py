"""Fused CUDA kernels for the MFS off-diagonal Oseen operator, fp64:

    W_p = sum_{q in partners(p)} G(b_p, s_q) S_q / (8 pi),   G_ij = I / r + r r^T / r^3,   r = b_i - s_j

for every target particle p at once, WITHOUT forming G in memory: each block builds its Oseen tile in shared memory and
multiplies it immediately.  Memory use is the inputs and the output only, for any number of particles.

  mma   R > 8 columns (full grand matrices): fp64 tensor cores, WMMA m8n8k4 (sm_80+: A100, H100, H200).  A block owns
        32 target nodes (96 rows) x 32 columns; 4 warps, one 8-column slice each, 12 accumulator fragments per warp;
        per k-chunk it builds the 96 x 24 Oseen tile (32 nodes x 8 sources) and a 24 x 32 tile of S in shared memory.
  fma   R <= 8 (one load per solve: dynamics): one thread per target node, sources streamed through shared memory in
        tiles of 128, all R columns in registers (templated R in {1, 2, 4, 8}).

partners(p) is a CSR list (ptr, idx) of global particle indices: FastMFS passes the NEAR pairs and sends far pairs
through its skeletons.  Layouts are BatchedMFS's: S (3M, LD), W (3N, LD), column q*R + r; nodes b (P, N, 3) and sources
s (P, M, 3) already in the lab frame (rotations applied by the caller).

Compiled on first use with torch.utils.cpp_extension.load_inline (needs nvcc and ninja).  available() reports whether it
built; FastMFS(kernel="cuda") uses it.  tests/test_mfs_cuda.py checks it entry by entry against the torch operator.
"""
from __future__ import annotations

import os
from typing import Optional

import torch

_CPP = "torch::Tensor oseen_apply(torch::Tensor b, torch::Tensor s, torch::Tensor S, torch::Tensor ptr, torch::Tensor idx, int64_t R, int64_t mode);"

_CUDA = r"""
#include <torch/extension.h>
#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAException.h>
#include <cuda_runtime.h>
#include <mma.h>
using namespace nvcuda;

#define INV8PI 0.039788735772973836

constexpr int TI = 32;            // target nodes per block -> 96 rows
constexpr int TJ = 8;             // sources per k-chunk    -> 24 k
constexpr int TN = 32;            // columns per block (4 warps x 8)
constexpr int AR = 3 * TI;        // 96
constexpr int AK = 3 * TJ;        // 24
constexpr int NFRAG = AR / 8;     // 12 row fragments per warp

__device__ __forceinline__ void oseen9(double rx, double ry, double rz, double* g) {
  const double inv = rsqrt(rx * rx + ry * ry + rz * rz);
  const double inv3 = inv * inv * inv;
  g[0] = inv + rx * rx * inv3; g[1] = rx * ry * inv3;       g[2] = rx * rz * inv3;
  g[3] = g[1];                 g[4] = inv + ry * ry * inv3; g[5] = ry * rz * inv3;
  g[6] = g[2];                 g[7] = g[5];                 g[8] = inv + rz * rz * inv3;
}

__global__ void __launch_bounds__(128) oseen_mma_kernel(
    const double* __restrict__ b, const double* __restrict__ s, const double* __restrict__ S,
    const int* __restrict__ ptr, const int* __restrict__ idx, double* __restrict__ W,
    int N, int M, int R, long long LD) {
#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ >= 800
  // A (96 x 24) and B (24 x 32) during the loop; C (96 x 32) afterwards, in the same buffer
  __shared__ __align__(32) double smem[AR * TN > AR * AK + AK * TN ? AR * TN : AR * AK + AK * TN];
  double* sA = smem;
  double* sB = smem + AR * AK;
  const int p = blockIdx.z, n0 = blockIdx.x * TI, c0 = blockIdx.y * TN;
  const int tid = threadIdx.x, warp = tid >> 5;
  wmma::fragment<wmma::accumulator, 8, 8, 4, double> acc[NFRAG];
#pragma unroll
  for (int f = 0; f < NFRAG; ++f) wmma::fill_fragment(acc[f], 0.0);
  // each thread fills two (node, source) cells of the 32 x 8 tile: nodes ii and ii + 16, source jj
  const int ii = tid / TJ, jj = tid % TJ;
  double bp[2][3];
#pragma unroll
  for (int h = 0; h < 2; ++h) {
    const int n = n0 + ii + 16 * h;
    for (int c = 0; c < 3; ++c) bp[h][c] = (n < N) ? b[((long long)p * N + n) * 3 + c] : 0.0;
  }
  for (int e = ptr[p]; e < ptr[p + 1]; ++e) {
    const int q = idx[e];
    const double* sq = s + (long long)q * M * 3;
    const long long colq = (long long)q * R;
    for (int m0 = 0; m0 < M; m0 += TJ) {
      const int m = m0 + jj;
      double sx = 0.0, sy = 0.0, sz = 0.0;
      if (m < M) { sx = sq[m * 3]; sy = sq[m * 3 + 1]; sz = sq[m * 3 + 2]; }
#pragma unroll
      for (int h = 0; h < 2; ++h) {
        const int il = ii + 16 * h;
        double g[9];
        if (n0 + il < N && m < M) {
          oseen9(bp[h][0] - sx, bp[h][1] - sy, bp[h][2] - sz, g);
        } else {
#pragma unroll
          for (int k = 0; k < 9; ++k) g[k] = 0.0;
        }
#pragma unroll
        for (int a = 0; a < 3; ++a)
#pragma unroll
          for (int c = 0; c < 3; ++c) sA[(3 * il + a) * AK + 3 * jj + c] = g[3 * a + c];
      }
      for (int t = tid; t < AK * TN; t += 128) {               // B tile: rows 3 m0 + k, columns c0 .. c0 + 31
        const int kr = t / TN, cc = t % TN;
        const int col = c0 + cc;
        sB[t] = (m0 + kr / 3 < M && col < R) ? S[(long long)(3 * m0 + kr) * LD + colq + col] : 0.0;
      }
      __syncthreads();
#pragma unroll
      for (int kk = 0; kk < AK / 4; ++kk) {
        wmma::fragment<wmma::matrix_b, 8, 8, 4, double, wmma::row_major> fb;
        wmma::load_matrix_sync(fb, sB + (4 * kk) * TN + 8 * warp, TN);
#pragma unroll
        for (int f = 0; f < NFRAG; ++f) {
          wmma::fragment<wmma::matrix_a, 8, 8, 4, double, wmma::row_major> fa;
          wmma::load_matrix_sync(fa, sA + (8 * f) * AK + 4 * kk, AK);
          wmma::mma_sync(acc[f], fa, fb, acc[f]);
        }
      }
      __syncthreads();
    }
  }
  double* sC = smem;
#pragma unroll
  for (int f = 0; f < NFRAG; ++f) wmma::store_matrix_sync(sC + (8 * f) * TN + 8 * warp, acc[f], TN, wmma::mem_row_major);
  __syncthreads();
  for (int t = tid; t < AR * TN; t += 128) {
    const int row = t / TN, cc = t % TN;
    const int col = c0 + cc;
    if (n0 + row / 3 < N && col < R) W[(long long)(3 * n0 + row) * LD + (long long)p * R + col] = sC[t] * INV8PI;
  }
#endif
}

template <int RT>
__global__ void __launch_bounds__(128) oseen_fma_kernel(
    const double* __restrict__ b, const double* __restrict__ s, const double* __restrict__ S,
    const int* __restrict__ ptr, const int* __restrict__ idx, double* __restrict__ W,
    int N, int M, int R, long long LD) {
  __shared__ double ss[128 * 3];
  __shared__ double sS[128 * 3 * RT];
  const int p = blockIdx.y, n = blockIdx.x * 128 + threadIdx.x, t = threadIdx.x;
  double bx = 0.0, by = 0.0, bz = 0.0;
  if (n < N) { const double* bq = b + ((long long)p * N + n) * 3; bx = bq[0]; by = bq[1]; bz = bq[2]; }
  double acc[3][RT];
#pragma unroll
  for (int a = 0; a < 3; ++a)
#pragma unroll
    for (int r = 0; r < RT; ++r) acc[a][r] = 0.0;
  for (int e = ptr[p]; e < ptr[p + 1]; ++e) {
    const int q = idx[e];
    const double* sq = s + (long long)q * M * 3;
    const long long colq = (long long)q * R;
    for (int m0 = 0; m0 < M; m0 += 128) {
      const int m = m0 + t;
      if (m < M) {
        ss[3 * t] = sq[3 * m]; ss[3 * t + 1] = sq[3 * m + 1]; ss[3 * t + 2] = sq[3 * m + 2];
#pragma unroll
        for (int c = 0; c < 3; ++c)
#pragma unroll
          for (int r = 0; r < RT; ++r) sS[(3 * t + c) * RT + r] = (r < R) ? S[(long long)(3 * m + c) * LD + colq + r] : 0.0;
      }
      __syncthreads();
      const int cnt = min(128, M - m0);
      if (n < N) {
        for (int j = 0; j < cnt; ++j) {
          double g[9];
          oseen9(bx - ss[3 * j], by - ss[3 * j + 1], bz - ss[3 * j + 2], g);
#pragma unroll
          for (int r = 0; r < RT; ++r) {
            const double f0 = sS[(3 * j) * RT + r], f1 = sS[(3 * j + 1) * RT + r], f2 = sS[(3 * j + 2) * RT + r];
            acc[0][r] += g[0] * f0 + g[1] * f1 + g[2] * f2;
            acc[1][r] += g[3] * f0 + g[4] * f1 + g[5] * f2;
            acc[2][r] += g[6] * f0 + g[7] * f1 + g[8] * f2;
          }
        }
      }
      __syncthreads();
    }
  }
  if (n < N) {
#pragma unroll
    for (int a = 0; a < 3; ++a)
#pragma unroll
      for (int r = 0; r < RT; ++r)
        if (r < R) W[(long long)(3 * n + a) * LD + (long long)p * R + r] = acc[a][r] * INV8PI;
  }
}

torch::Tensor oseen_apply(torch::Tensor b, torch::Tensor s, torch::Tensor S, torch::Tensor ptr, torch::Tensor idx,
                          int64_t R, int64_t mode) {
  TORCH_CHECK(b.is_cuda() && s.is_cuda() && S.is_cuda() && ptr.is_cuda() && idx.is_cuda(), "CUDA tensors expected");
  TORCH_CHECK(b.scalar_type() == torch::kFloat64 && s.scalar_type() == torch::kFloat64 && S.scalar_type() == torch::kFloat64, "fp64 expected");
  TORCH_CHECK(ptr.scalar_type() == torch::kInt32 && idx.scalar_type() == torch::kInt32, "int32 CSR expected");
  b = b.contiguous(); s = s.contiguous(); S = S.contiguous();
  const int P = b.size(0), N = b.size(1), M = s.size(1);
  const long long LD = S.size(1);
  TORCH_CHECK(S.size(0) == 3 * M && LD == (long long)P * R, "S must be (3M, P*R)");
  auto W = torch::empty({3 * N, LD}, S.options());
  auto stream = at::cuda::getCurrentCUDAStream();
  if (mode == 0) mode = (R > 8) ? 1 : 2;
  const int* pp = ptr.data_ptr<int>();
  const int* ii = idx.data_ptr<int>();
  if (mode == 1) {
    dim3 grid((N + TI - 1) / TI, (R + TN - 1) / TN, P);
    oseen_mma_kernel<<<grid, 128, 0, stream>>>(b.data_ptr<double>(), s.data_ptr<double>(), S.data_ptr<double>(), pp, ii,
                                               W.data_ptr<double>(), N, M, (int)R, LD);
  } else {
    dim3 grid((N + 127) / 128, P);
#define LAUNCH(RT) oseen_fma_kernel<RT><<<grid, 128, 0, stream>>>(b.data_ptr<double>(), s.data_ptr<double>(), \
        S.data_ptr<double>(), pp, ii, W.data_ptr<double>(), N, M, (int)R, LD)
    if (R <= 1) LAUNCH(1); else if (R <= 2) LAUNCH(2); else if (R <= 4) LAUNCH(4); else if (R <= 8) LAUNCH(8);
    else {                                                  // 9..15 columns: blocks of 8
      TORCH_CHECK(false, "fma path supports R <= 8; use mode 1 (mma) for R > 8");
    }
#undef LAUNCH
  }
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return W;
}
"""

_EXT = None
_ERR: Optional[str] = None


def _load():
    global _EXT, _ERR
    if _EXT is not None or _ERR is not None:
        return _EXT
    try:
        from torch.utils.cpp_extension import load_inline
        _EXT = load_inline(name="mfs_oseen_cuda_v1", cpp_sources=_CPP, cuda_sources=_CUDA, functions=["oseen_apply"],
                           extra_cuda_cflags=["-O3", "--expt-relaxed-constexpr", "-lineinfo"],
                           verbose=bool(os.environ.get("MFS_CUDA_VERBOSE")))
    except Exception as e:                                  # noqa: BLE001
        _ERR = f"{type(e).__name__}: {e}"
    return _EXT


def available() -> bool:
    return torch.cuda.is_available() and _load() is not None


def error() -> Optional[str]:
    _load()
    return _ERR


def csr(p: torch.Tensor, q: torch.Tensor, P_tot: int):
    """Partners grouped by target: ptr (P_tot + 1,) and idx (n_pairs,), int32, on p's device."""
    order = torch.argsort(p, stable=True)
    counts = torch.bincount(p, minlength=P_tot)
    ptr = torch.zeros(P_tot + 1, dtype=torch.int64, device=p.device)
    ptr[1:] = torch.cumsum(counts, 0)
    return ptr.to(torch.int32).contiguous(), q[order].to(torch.int32).contiguous()


def oseen_apply(b_lab: torch.Tensor, s_lab: torch.Tensor, S: torch.Tensor, ptr: torch.Tensor, idx: torch.Tensor,
                R: int, mode: str = "auto") -> torch.Tensor:
    """W (3N, P*R) fp64 = sum over each target's partners of G(b_p, s_q) S_q / (8 pi)."""
    ext = _load()
    assert ext is not None, f"CUDA MFS kernel unavailable: {_ERR}"
    m = {"auto": 0, "mma": 1, "fma": 2}[mode]
    return ext.oseen_apply(b_lab, s_lab, S, ptr, idx, int(R), m)


def reference(b_lab, s_lab, S, p, q, R) -> torch.Tensor:
    """The same operator with explicit blocks in torch (any device): the kernels' test oracle."""
    P_tot, N, M = b_lab.shape[0], b_lab.shape[1], s_lab.shape[1]
    Sv = S.view(3 * M, P_tot, R).permute(1, 0, 2)
    Wv = torch.zeros(P_tot, 3 * N, R, dtype=S.dtype, device=S.device)
    for i in range(len(p)):
        r = b_lab[p[i]][:, None, :] - s_lab[q[i]][None, :, :]
        inv = 1.0 / r.norm(dim=-1)
        G = inv[..., None, None] * torch.eye(3, dtype=S.dtype, device=S.device) + r[..., :, None] * r[..., None, :] * (inv ** 3)[..., None, None]
        Wv[p[i]] += (G.permute(0, 2, 1, 3).reshape(3 * N, 3 * M) @ Sv[q[i]]) * 0.039788735772973836
    return Wv.permute(1, 0, 2).reshape(3 * N, P_tot * R)
