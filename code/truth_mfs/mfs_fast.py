"""FastMFS: BatchedMFS (same equations, same GMRES, same velocity convergence) with a faster off-diagonal operator.

The only expensive piece of BatchedMFS is W = Wop S, the Oseen sum from every particle's sources to every other
particle's boundary nodes, and its fp64 path rebuilds every Oseen block at every Krylov step.  Here:

  1. Exact cache.  Once per solve the operator is planned: ordered particle pairs of every system, split into near and
     far by a centre-distance test.  Near blocks G_pq (3N x 3M) are built once, vectorised over pairs of ALL systems,
     and kept while they fit `cache_gb`; every Krylov step is then batched GEMMs (torch.bmm) + one index_add.  Blocks
     beyond the budget are rebuilt per step (vectorised, as before).  Exact: same numbers as BatchedMFS to round-off.
  2. Far compression (proxy-point interpolative decomposition, per shape, in the body frame).  For a pair whose centres
     are farther than rho a + a (a = largest boundary-node radius), the field of q's M sources at p's nodes equals, to
     ~1e-10 here, that of K_s skeleton sources carrying P_s f (3K_s x 3M), and p's nodes see it through K_t skeleton
     nodes and an interpolation L_t (3N x 3K_t).  Both maps are rotated with the particle (the Stokeslet is rotation
     covariant).  Far blocks shrink to 3K_t x 3K_s: less work per step and a cache that fits larger P.
  3. Warm start.  With warm_start=True each solve starts from the previous solve's boundary velocities W when the layout
     matches (same particle count and columns): the dynamics case, where every RK4 stage is close to the last one.

Everything else is inherited; FastMFS(...).solve / solve_mobility_matrix(_batch) are drop-in replacements.
benchmarks/bench_mfs_fast.py measures it against BatchedMFS; tests/test_mfs_fast.py checks it against BatchedMFS.
"""
from __future__ import annotations

import math
import os
from pathlib import Path
from typing import Optional

import numpy as np
import torch

from .mfs_batched import INV_8PI, BatchedMFS, POINTS_DIR, _Ctx, load_template

SKEL_DIR = os.environ.get("MFS_SKELETON_DIR", "data/points/skeletons")


def _G_np(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    r = x[:, None, :] - y[None, :, :]
    inv = 1.0 / np.linalg.norm(r, axis=-1)
    g = inv[..., None, None] * np.eye(3) + r[..., :, None] * r[..., None, :] * (inv ** 3)[..., None, None]
    return (g * INV_8PI).transpose(0, 2, 1, 3).reshape(3 * len(x), 3 * len(y))


def _fibonacci(n: int, rad: float) -> np.ndarray:
    i = np.arange(n) + 0.5
    phi, th = np.arccos(1 - 2 * i / n), math.pi * (1 + 5 ** 0.5) * i
    return rad * np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], 1)


def skeleton(shape: str, acc: str, rho: float = 2.0, eps: float = 1e-6, n_proxy: int = 400,
             points_dir: str = POINTS_DIR, cache: bool = True) -> dict:
    """Body-frame far-field skeletons of one MFS template, by pivoted QR against proxy points on two spheres of radii
    rho a and 1.3 rho a.  Whole points are kept (all three components), so the maps rotate with the particle.
    -> src_idx (K_s), P_s (3K_s, 3M), tgt_idx (K_t), L_t (3N, 3K_t), a, r_adm (= rho a + a)."""
    path = Path(SKEL_DIR) / f"skel_{shape}_{acc}_rho{rho:g}_eps{eps:g}_n{n_proxy}.npz"
    if cache and path.exists():
        d = np.load(path)
        return {k: (d[k] if d[k].ndim else float(d[k])) for k in d.files}
    import scipy.linalg as sl
    b, s, _ = load_template(acc, points_dir, shape)
    a = float(np.linalg.norm(b, axis=1).max())
    prox = np.concatenate([_fibonacci(n_proxy, rho * a), _fibonacci(n_proxy, 1.3 * rho * a)])
    A = _G_np(prox, s)                                                    # proxy <- sources
    _, Rr, piv = sl.qr(A, pivoting=True, mode="economic")
    d = np.abs(np.diag(Rr))
    J = np.unique(piv[: int((d > eps * d[0]).sum())] // 3)
    cols = (3 * J[:, None] + np.arange(3)).ravel()
    P_s = np.linalg.lstsq(A[:, cols], A, rcond=None)[0]
    B = _G_np(b, prox)                                                    # nodes <- proxy
    _, R2, piv2 = sl.qr(B.T, pivoting=True, mode="economic")
    d2 = np.abs(np.diag(R2))
    I = np.unique(piv2[: int((d2 > eps * d2[0]).sum())] // 3)
    rows = (3 * I[:, None] + np.arange(3)).ravel()
    L_t = np.linalg.lstsq(B[rows].T, B.T, rcond=None)[0].T
    out = {"src_idx": J, "P_s": P_s, "tgt_idx": I, "L_t": L_t, "a": a, "r_adm": rho * a + a, "rho": rho, "eps": eps}
    if cache:
        path.parent.mkdir(parents=True, exist_ok=True)
        np.savez(path, **out)
    return out


class FastMFS(BatchedMFS):
    def __init__(self, *args, cache_gb: float = 40.0, far: bool = True, far_target: bool = True, rho: float = 2.0,
                 eps: float = 1e-6, warm_start: bool = False, pair_chunk: int = 16, kernel: str = "torch", **kw):
        kw.setdefault("backend", "torch64")
        super().__init__(*args, **kw)
        assert self.backend == "torch64", "FastMFS is the fp64 path"
        self.cache_bytes = float(cache_gb) * (1 << 30)
        self.far, self.far_target, self.warm_start, self.pair_chunk = bool(far), bool(far_target), bool(warm_start), int(pair_chunk)
        assert kernel in ("torch", "cuda"), kernel
        self.kernel = kernel                       # "cuda": near pairs by the fused kernels of mfs_cuda.py, no cache
        if kernel == "cuda":
            from . import mfs_cuda
            assert mfs_cuda.available(), f"CUDA MFS kernel unavailable: {mfs_cuda.error()}"
            self._cu = mfs_cuda
        self._plan, self._last_key, self._last_W = None, None, None
        self.stats = {"plans": 0, "near_pairs": 0, "far_pairs": 0, "cached_near": 0, "warm_starts": 0}
        if self.far:
            sk = skeleton(self.shape, self.acc, rho, eps)
            dev, f64 = self.device, torch.float64
            self.src_idx = torch.as_tensor(sk["src_idx"], device=dev)
            self.tgt_idx = torch.as_tensor(sk["tgt_idx"], device=dev)
            self.P_s = torch.as_tensor(sk["P_s"], dtype=f64, device=dev)
            self.L_t = torch.as_tensor(sk["L_t"], dtype=f64, device=dev)
            self.r_adm = float(sk["r_adm"])
            self.K_s, self.K_t = len(sk["src_idx"]), len(sk["tgt_idx"])

    # ------------------------------------------------------------------ plan
    def _lab_points(self, ctx: _Ctx, body: torch.Tensor) -> torch.Tensor:
        """(P_tot, n, 3) lab positions of body-frame points `body` (n, 3) of every particle."""
        if ctx.rot is None:
            return body[None] + ctx.c64[:, None, :]
        return torch.einsum("pij,nj->pni", ctx.rot, body) + ctx.c64[:, None, :]

    def _blocks(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor:
        """Oseen blocks (n, 3|X|, 3|Y|) from points Y (n, m, 3) to points X (n, k, 3), fp64, 1/(8 pi) included."""
        r = X[:, :, None, :] - Y[:, None, :, :]
        inv = 1.0 / r.norm(dim=-1)
        G = inv[..., None, None] * self._I3_64 + r[..., :, None] * r[..., None, :] * (inv ** 3)[..., None, None]
        n, k, m = G.shape[:3]
        return (G.permute(0, 1, 3, 2, 4).reshape(n, 3 * k, 3 * m) * INV_8PI)

    def _make_plan(self, ctx: _Ctx) -> dict:
        P_c, n_sys = ctx.P_c, ctx.n_sys
        dev = self.device
        loc = torch.arange(P_c, device=dev)
        pl, ql = torch.meshgrid(loc, loc, indexing="ij")
        off = pl != ql
        pl, ql = pl[off], ql[off]
        base = (torch.arange(n_sys, device=dev) * P_c)[:, None]
        p = (base + pl[None]).reshape(-1)
        q = (base + ql[None]).reshape(-1)
        dist = (ctx.c64[p] - ctx.c64[q]).norm(dim=-1)
        far = (dist >= self.r_adm) if self.far else torch.zeros_like(dist, dtype=torch.bool)
        plan = {"near_p": p[~far], "near_q": q[~far], "far_p": p[far], "far_q": q[far]}
        bl = self._lab_points(ctx, self.b64)
        sl = self._lab_points(ctx, self.s64)
        plan["b_lab"], plan["s_lab"] = bl, sl
        # near blocks: cache as many as the budget allows (none with the fused CUDA kernels: they never form a block)
        per = 9 * self.N * self.M * 8
        budget_bytes = self.cache_bytes
        if self.device.type == "cuda":                   # never more than half of what is free now: other solvers,
            free, _ = torch.cuda.mem_get_info(self.device)  # GMRES's basis and the caller share the GPU
            budget_bytes = min(budget_bytes, 0.5 * free)
        plan["cache_budget_gb"] = budget_bytes / 2 ** 30
        n_cache = 0 if self.kernel == "cuda" else min(len(plan["near_p"]), int(budget_bytes // per))
        if self.kernel == "cuda":
            plan["csr"] = self._cu.csr(plan["near_p"], plan["near_q"], ctx.P_tot)
            plan["b_lab"], plan["s_lab"] = bl.contiguous(), sl.contiguous()
        plan["near_cache"] = []
        for i in range(0, n_cache, self.pair_chunk):
            j = slice(i, min(i + self.pair_chunk, n_cache))
            plan["near_cache"].append(self._blocks(bl[plan["near_p"][j]], sl[plan["near_q"][j]]))
        plan["n_cached"] = n_cache
        if self.far and len(plan["far_p"]):
            tgt = bl[:, self.tgt_idx] if self.far_target else bl
            src = sl[:, self.src_idx]
            fp, fq = plan["far_p"], plan["far_q"]
            per_far = 9 * tgt.shape[1] * src.shape[1] * 8
            budget = max(0, int((budget_bytes - n_cache * per) // per_far))
            plan["far_cache"] = [self._blocks(tgt[fp[i:i + 256]], src[fq[i:i + 256]]) for i in range(0, min(len(fp), budget), 256)]
            plan["far_cached"] = min(len(fp), budget)
            plan["tgt_pts"], plan["src_pts"] = tgt, src
        self.stats["plans"] += 1
        self.stats["near_pairs"] += int(len(plan["near_p"]))
        self.stats["far_pairs"] += int(len(plan["far_p"]))
        self.stats["cached_near"] += int(n_cache)
        return plan

    def release(self) -> None:
        """Drop the cached blocks and the warm-start state (the GPU memory they hold)."""
        self._plan, self._last_key, self._last_W = None, None, None
        if self.device.type == "cuda":
            torch.cuda.empty_cache()

    def _get_plan(self, ctx: _Ctx) -> dict:
        """The plan of this configuration: matched on the positions and rotations themselves (object ids and device
        addresses are reused between solves, so they must not decide whether cached blocks are still valid)."""
        p = self._plan
        same = (p is not None and p["c64"].shape == ctx.c64.shape and (p["n_sys"], p["P_c"]) == (ctx.n_sys, ctx.P_c)
                and torch.equal(p["c64"], ctx.c64)
                and ((p["rot"] is None and ctx.rot is None)
                     or (p["rot"] is not None and ctx.rot is not None and torch.equal(p["rot"], ctx.rot))))
        if not same:
            self._plan = None                                           # free the old cache first
            self._plan = self._make_plan(ctx)
            self._plan.update(c64=ctx.c64.clone(), rot=None if ctx.rot is None else ctx.rot.clone(),
                              n_sys=ctx.n_sys, P_c=ctx.P_c)
        return self._plan

    # ------------------------------------------------------------------ operator
    def _oseen_torch64(self, S: torch.Tensor, ctx: _Ctx) -> torch.Tensor:
        plan = self._get_plan(ctx)
        S = S.to(torch.float64)
        N3, M3, R = 3 * self.N, 3 * self.M, ctx.R
        if self.kernel == "cuda":
            W = self._cu.oseen_apply(plan["b_lab"], plan["s_lab"], S.contiguous(), *plan["csr"], R)
            if self.far and len(plan["far_p"]):
                Sv = S.view(M3, ctx.P_tot, R).permute(1, 0, 2)
                W = W + self._far(S, Sv, plan, ctx).permute(1, 0, 2).reshape(N3, ctx.LD)
            return W
        Sv = S.view(M3, ctx.P_tot, R).permute(1, 0, 2)                   # (P_tot, 3M, R)
        Wv = torch.zeros(ctx.P_tot, N3, R, dtype=torch.float64, device=self.device)
        p, q = plan["near_p"], plan["near_q"]
        k = 0
        for G in plan["near_cache"]:
            n = G.shape[0]
            Wv.index_add_(0, p[k:k + n], torch.bmm(G, Sv[q[k:k + n]]))
            k += n
        for i in range(k, len(p), self.pair_chunk):                      # beyond the cache: rebuilt every step
            j = slice(i, i + self.pair_chunk)
            G = self._blocks(plan["b_lab"][p[j]], plan["s_lab"][q[j]])
            Wv.index_add_(0, p[j], torch.bmm(G, Sv[q[j]]))
        if self.far and len(plan["far_p"]):
            Wv += self._far(S, Sv, plan, ctx)
        return Wv.permute(1, 0, 2).reshape(N3, ctx.LD)

    def _far(self, S, Sv, plan, ctx) -> torch.Tensor:
        """Far pairs through the skeletons: f -> P_s f per source particle, skeleton blocks, -> L_t per target."""
        R = ctx.R
        Sb = self._rotate(S, ctx, inverse=True)                           # body frame per particle
        Sk = self._rotate(self.P_s @ Sb, ctx)                             # (3K_s, LD), lab
        Skv = Sk.view(3 * self.K_s, ctx.P_tot, R).permute(1, 0, 2)
        nt = plan["tgt_pts"].shape[1]
        Uv = torch.zeros(ctx.P_tot, 3 * nt, R, dtype=torch.float64, device=self.device)
        fp, fq = plan["far_p"], plan["far_q"]
        k = 0
        for G in plan["far_cache"]:
            n = G.shape[0]
            Uv.index_add_(0, fp[k:k + n], torch.bmm(G, Skv[fq[k:k + n]]))
            k += n
        for i in range(k, len(fp), 256):
            j = slice(i, i + 256)
            G = self._blocks(plan["tgt_pts"][fp[j]], plan["src_pts"][fq[j]])
            Uv.index_add_(0, fp[j], torch.bmm(G, Skv[fq[j]]))
        if not self.far_target:
            return Uv
        U = Uv.permute(1, 0, 2).reshape(3 * nt, ctx.LD)
        Wb = self.L_t @ self._rotate(U, ctx, inverse=True)               # interpolate in each target's body frame
        return self._rotate(Wb, ctx).view(3 * self.N, ctx.P_tot, R).permute(1, 0, 2)

    # ------------------------------------------------------------------ warm start
    def _solve_ctx(self, ctx, X0, method, tol, tol_v, max_iter, m, max_restarts, info, ambient=None):
        if not (self.warm_start and method == "gmres"):
            return super()._solve_ctx(ctx, X0, method, tol, tol_v, max_iter, m, max_restarts, info, ambient)
        M3 = 3 * self.M
        X0_f, X0_v = X0[:M3].to(self.wdtype).contiguous(), X0[M3:].contiguous()
        b = self.oseen_offdiag(X0_f, ctx)
        if ambient is not None:
            b = b + self._ambient_W(ambient, ctx)
        info.n_matvec += 1
        key = (ctx.P_tot, ctx.R, ctx.n_sys)
        if self._last_key == key and self._last_W is not None:
            W0 = self._last_W
            r0 = b - self.matvec(W0, ctx)
            info.n_matvec += 1
            dW = self._gmres(r0, ctx, X0_v - self.apply_Kv(W0, ctx), tol, tol_v, m, max_restarts, info)
            W = W0 + dW
            self.stats["warm_starts"] += 1
        else:
            W = self._gmres(b, ctx, X0_v, tol, tol_v, m, max_restarts, info)
        self._last_key, self._last_W = key, W
        return self._velocities(X0_v, W, ctx)


def tight_kwargs(tol_v: float) -> dict:
    """Solver settings for a velocity tolerance below the production 1e-7 (the Xfine accuracy check, tol_v 1e-10):
    the W-residual safety stop 1000x below tol_v (so the velocity criterion governs) and room for more Krylov steps."""
    if tol_v >= 1e-8:
        return {}
    return {"tol": tol_v * 1e-3, "m": 40, "max_iter": 200, "max_restarts": 20}


def truth_solver(shape: str, acc: str = "fine", device="cuda", tol_v: float = 1e-7, mem_budget_gb: Optional[float] = None,
                 warm_start: bool = True, verbose: bool = True):
    """The solver for MFS-at-every-step runs (dynamics, falling-cloud truth): FastMFS with the fused CUDA kernels and a
    warm start (95x BatchedMFS on 64 particles, H200, errors <= 3e-8: benchmarks/results/BENCH_MFS_FAST_*.md) when the
    kernel builds, else BatchedMFS fp64 (the old path; same equations).  MFS_SOLVER=batched forces the old path."""
    dev = torch.device(device)
    if mem_budget_gb is None:
        mem_budget_gb = 0.45 * torch.cuda.get_device_properties(dev).total_memory / 2 ** 30 if dev.type == "cuda" else 8.0
    common = dict(acc=acc, device=device, shape=shape, tol_v=tol_v, mem_budget_gb=mem_budget_gb, **tight_kwargs(tol_v))
    if dev.type == "cuda" and os.environ.get("MFS_SOLVER", "fast") != "batched":
        from . import mfs_cuda
        if mfs_cuda.available():
            if verbose:
                print(f"[truth solver] FastMFS cuda kernel, warm start {warm_start} ({shape}, {acc})", flush=True)
            return FastMFS(far=False, kernel="cuda", warm_start=warm_start, **common)
        if verbose:
            print(f"[truth solver] CUDA MFS kernel unavailable ({mfs_cuda.error()}): BatchedMFS fp64", flush=True)
    elif verbose:
        print(f"[truth solver] BatchedMFS fp64 ({shape}, {acc})", flush=True)
    return BatchedMFS(backend="torch64", **common)
