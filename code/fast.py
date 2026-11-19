"""Matrix-free operator for large suspensions: velocities U = M F without building the (6N, 6N) matrix.

    fast = FastOperator(op)                          op: a mobility.Operator (the same trained models)
    U = fast.apply(pos, quats, shapes, F, mode)      mode "far", "pair" or "full", as Operator.grand_M

  far field   the 12-point far field of every pair (farfield.py), summed in O(N) with Hasimoto's split of the Stokeslet:
              the smooth part on a grid (FFT, free space, Lagrange interpolation of order p), the short part directly
              for points closer than r_short; each particle's own points are taken out again (they are not a pair).
  self        the isolated blocks.
  "pair"      + the two-body model where it acts: for every pair within its range (cell list), the cross block minus
              the far field already counted, and the self corrections.
  "full"      + the many-body corrections (f_nb, self model) through mobility.Operator's own functions.  Their neighbour
              search is dense (memory ~ 2048 x N per chunk), so "full" is for N up to ~10^4; "far" and "pair" scale to
              ~10^6 particles on one large GPU.

The same operator as Operator.grand_M(..., psd=False), to the accuracy of the grid sum (2e-4 of the far field with
the defaults; tests.py).  NOT projected onto positive definite matrices: the projection (psd.py) needs the matrix itself.
Ported from the research code's src/aniso_far.py (StokesGridSum, neighbour_pairs), generalised to any mix of shapes
and sizes and to the unified models.
"""
from __future__ import annotations

import math
import time

import numpy as np
import torch

import pair as P
from farfield import _lab_operator, body_operator
from geometry import axes_of, random_quats, volume

INV_8PI = 1.0 / (8.0 * math.pi)


# ----------------------------------------------------------------------------------------------- Hasimoto split
def _smooth_coeffs(r2: torch.Tensor, xi: float):
    """G_smooth = A I + B x x^T: the Stokeslet minus Hasimoto's short part (finite at r = 0)."""
    r = r2.clamp_min(1e-30).sqrt()
    q = xi * r
    e = torch.exp(-q * q)
    c = 2.0 * xi / math.sqrt(math.pi)
    A = (torch.erf(q) / r + c * e) * INV_8PI
    B = (torch.erf(q) / (r * r2.clamp_min(1e-30)) - c * e / r2.clamp_min(1e-30)) * INV_8PI
    small = q < 0.1
    if bool(small.any()):                                # series: the two terms of B cancel near r = 0
        q2 = (q * q)[small]
        A[small] = c * (2.0 - 4.0 / 3.0 * q2 + 0.6 * q2 * q2) * INV_8PI
        B[small] = c * xi * xi * (2.0 / 3.0 - 0.4 * q2 + q2 * q2 / 7.0) * INV_8PI
    return A, B


def _short_coeffs(r2: torch.Tensor, xi: float):
    """G - G_smooth = A I + B x x^T (decays like exp(-xi^2 r^2))."""
    r = r2.clamp_min(1e-30).sqrt()
    q = xi * r
    e = torch.exp(-q * q)
    c = 2.0 * xi / math.sqrt(math.pi)
    return (torch.erfc(q) / r - c * e) * INV_8PI, (torch.erfc(q) / (r * r2.clamp_min(1e-30)) + c * e / r2.clamp_min(1e-30)) * INV_8PI


def _apply_coeffs(A, B, x, f):
    """(A I + B x x^T) f summed over the source points: x (K, n, m, 3), f (K, m, 3) -> (K, n, 3)."""
    fd = (x * f[:, None, :, :]).sum(-1, keepdim=True)
    return (A[..., None] * f[:, None, :, :] + B[..., None] * fd * x).sum(2)


def neighbour_pairs(X: torch.Tensor, cutoff: float, chunk: int = 20_000_000):
    """Unordered pairs t != s with |x_t - x_s| < cutoff, by a cell list: (t, s) long tensors."""
    if len(X) < 2:
        e = torch.zeros(0, dtype=torch.long, device=X.device)
        return e, e
    lo = X.min(0).values
    ijk = ((X - lo) / cutoff).floor().long() + 1
    dims = ijk.max(0).values + 2
    key = ijk[:, 0] * dims[1] * dims[2] + ijk[:, 1] * dims[2] + ijk[:, 2]
    order = torch.argsort(key)
    ukeys, counts = torch.unique_consecutive(key[order], return_counts=True)
    starts = torch.cat([torch.zeros(1, dtype=torch.long, device=X.device), counts.cumsum(0)[:-1]])
    Ts, Ss = [], []
    Y = X[order]
    half = [(0, 0, 0)] + [(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1) if (a, b, c) > (0, 0, 0)]
    for off in half:
        nk = ukeys + off[0] * dims[1] * dims[2] + off[1] * dims[2] + off[2]
        pos = torch.searchsorted(ukeys, nk).clamp_max(len(ukeys) - 1)
        ok = ukeys[pos] == nk
        c1, c2 = torch.nonzero(ok)[:, 0], pos[ok]
        sizes = counts[c1] * counts[c2]
        cum = sizes.cumsum(0)
        i0 = 0
        while i0 < len(c1):
            base = 0 if i0 == 0 else int(cum[i0 - 1])
            i1 = max(int(torch.searchsorted(cum, torch.as_tensor(base + chunk, device=X.device), right=True)), i0 + 1)
            cell = torch.arange(i0, i1, device=X.device).repeat_interleave(sizes[i0:i1])
            k = torch.arange(int(sizes[i0:i1].sum()), device=X.device) - (cum[cell] - sizes[cell] - base)
            a = starts[c1[cell]] + k // counts[c2[cell]]
            b = starts[c2[cell]] + k % counts[c2[cell]]
            keep = ((Y[a] - Y[b]) ** 2).sum(-1) < cutoff * cutoff
            if off == (0, 0, 0):
                keep &= a < b
            Ts.append(order[a[keep]]), Ss.append(order[b[keep]])
            i0 = i1
    return torch.cat(Ts), torch.cat(Ss)


class StokesGridSum:
    """Smooth part of the Stokes sum on a regular grid: free space (doubled grid), Lagrange interpolation of order p."""

    def __init__(self, xi: float, h: float, p: int = 6, device="cuda", dtype=torch.float32):
        assert p % 2 == 0
        self.xi, self.h, self.p, self.dev, self.dtype = float(xi), float(h), int(p), device, dtype
        self.M = None

    def _kernel(self, M):
        ax = [torch.fft.fftfreq(2 * m, d=1.0 / (2 * m), device=self.dev, dtype=self.dtype) * self.h for m in M]
        x = ax[0][:, None, None].expand(-1, 2 * M[1], 2 * M[2])
        y = ax[1][None, :, None].expand(2 * M[0], -1, 2 * M[2])
        z = ax[2][None, None, :].expand(2 * M[0], 2 * M[1], -1)
        A, B = _smooth_coeffs(x * x + y * y + z * z, self.xi)
        K = []
        for i, u in enumerate((x, y, z)):
            for j, v in enumerate((x, y, z)):
                if j >= i:
                    K.append(torch.fft.rfftn(((A if i == j else 0.0) + B * u * v).to(self.dtype)))
        return K

    def setup(self, pts: torch.Tensor):
        pad = (self.p / 2 + 1) * self.h
        lo, hi = pts.min(0).values - pad, pts.max(0).values + pad
        M = tuple(int(m) for m in ((hi - lo) / self.h).ceil().long().tolist())
        if M != self.M:
            self.K = None
            self.K, self.M = self._kernel(M), M
        self.lo = lo

    def _stencil(self, x):
        s = (x - self.lo.to(x.dtype)) / self.h
        base = s.floor().long() - (self.p // 2 - 1)
        t = (s - base)[:, :, None]
        nodes = torch.arange(self.p, device=x.device, dtype=x.dtype)
        W = torch.ones(x.shape[0], 3, self.p, device=x.device, dtype=x.dtype)
        for j in range(self.p):
            for m in range(self.p):
                if m != j:
                    W[:, :, j] *= (t[:, :, 0] - nodes[m]) / (nodes[j] - nodes[m])
        return base, W

    def _flat(self, base, W):
        o = torch.arange(self.p, device=base.device)
        idx = ((base[:, 0, None] + o)[:, :, None, None] * self.M[1] * self.M[2] + (base[:, 1, None] + o)[:, None, :, None] * self.M[2]
               + (base[:, 2, None] + o)[:, None, None, :])
        w = W[:, 0, :, None, None] * W[:, 1, None, :, None] * W[:, 2, None, None, :]
        return idx.reshape(len(base), -1), w.reshape(len(base), -1)

    def apply(self, pts: torch.Tensor, f: torch.Tensor, chunk: int = 1_000_000) -> torch.Tensor:
        """Points (m, 3), forces (m, 3) -> smooth-part velocities (m, 3): every pair, and each point on itself."""
        grid = torch.zeros(3, int(np.prod(self.M)), device=self.dev, dtype=self.dtype)
        for i in range(0, len(pts), chunk):
            idx, w = self._flat(*self._stencil(pts[i:i + chunk]))
            for c in range(3):
                grid[c].index_add_(0, idx.reshape(-1), (w * f[i:i + chunk, c, None]).reshape(-1))
        s = tuple(2 * m for m in self.M)
        Fh = [torch.fft.rfftn(grid[c].reshape(self.M), s=s) for c in range(3)]
        xx, xy, xz, yy, yz, zz = self.K
        out = (xx * Fh[0] + xy * Fh[1] + xz * Fh[2], xy * Fh[0] + yy * Fh[1] + yz * Fh[2], xz * Fh[0] + yz * Fh[1] + zz * Fh[2])
        del Fh
        for c in range(3):
            grid[c] = torch.fft.irfftn(out[c], s=s)[: self.M[0], : self.M[1], : self.M[2]].reshape(-1)
        u = torch.zeros_like(f)
        for i in range(0, len(pts), chunk):
            idx, w = self._flat(*self._stencil(pts[i:i + chunk]))
            for c in range(3):
                u[i:i + chunk, c] = (w * grid[c][idx]).sum(1)
        return u


# ----------------------------------------------------------------------------------------------- the operator
class FastOperator:
    def __init__(self, op, xi: float = 0.35, h: float = 1.0, p: int = 6, dtype=torch.float32, pair_chunk: int = 100_000):
        """op: mobility.Operator.  xi, h, p: the grid sum (far field 2e-4 relative to the dense one with these defaults,
        4e-5 with p = 8, 2e-3 with h = 1.5; tests.py); dtype of the far-field sum (float32 is as accurate here)."""
        self.op, self.dev, self.dtype = op, op.dev, dtype
        self.xi, self.r_short, self.pair_chunk = float(xi), 3.5 / float(xi), int(pair_chunk)      # erfc(3.5) = 7e-7
        self.grid = StokesGridSum(xi, h, p, op.dev, dtype)
        self.times: dict = {}

    def _now(self):
        if self.dev.type == "cuda":
            torch.cuda.synchronize()
        return time.perf_counter()

    def _points(self, X, R, shapes):
        """Lab points (N, 12, 3) and lab operators P (N, 6, 36) of every particle, in the far-field dtype."""
        N, dt = len(X), self.dtype
        body = torch.zeros(N, 12, 3, dtype=dt, device=self.dev)
        Pl = torch.zeros(N, 6, 36, dtype=dt, device=self.dev)
        reach = 0.0
        for kind in dict.fromkeys(shapes):
            idx = torch.as_tensor([i for i, s in enumerate(shapes) if s == kind], device=self.dev)
            b, C = body_operator(kind, dt, self.dev)
            body[idx], Pl[idx] = b, _lab_operator(C, R[idx].to(dt))
            reach = max(reach, float(b.norm(dim=1).max()))
        return X.to(dt)[:, None, :] + body @ R.to(dt).transpose(1, 2), Pl, reach

    def _pair_term(self, u, x, f, t, s, mask_cut):
        """u[t] += G_short f[s] and the reciprocal, for unordered particle pairs (t, s), point pairs within mask_cut."""
        for i in range(0, len(t), self.pair_chunk):
            a, b = t[i:i + self.pair_chunk], s[i:i + self.pair_chunk]
            dx = x[a][:, :, None, :] - x[b][:, None, :, :]
            r2 = (dx ** 2).sum(-1)
            A, B = _short_coeffs(r2, self.xi)
            m = r2 < mask_cut * mask_cut
            A, B = A * m, B * m
            u.index_add_(0, a, _apply_coeffs(A, B, dx, f[b]))
            u.index_add_(0, b, _apply_coeffs(A.transpose(1, 2), B.transpose(1, 2), dx.transpose(1, 2), f[a]))

    @torch.no_grad()
    def far(self, X, R, shapes, F) -> torch.Tensor:
        """Far-field velocities (N, 6) of all pairs (no self blocks), float64."""
        N = len(X)
        x, Pl, reach = self._points(X, R, shapes)
        f = (Pl.transpose(1, 2) @ F.to(self.dtype)[:, :, None])[..., 0].reshape(N, 12, 3)             # P^T F: 12 point forces
        self.grid.setup(x.reshape(-1, 3))
        u = self.grid.apply(x.reshape(-1, 3), f.reshape(-1, 3)).reshape(N, 12, 3)
        for i in range(0, N, self.pair_chunk):                                                      # a particle's own points
            k = slice(i, i + self.pair_chunk)
            dx = x[k][:, :, None, :] - x[k][:, None, :, :]
            A, B = _smooth_coeffs((dx ** 2).sum(-1), self.xi)
            u[k] -= _apply_coeffs(A, B, dx, f[k])
        t, s = neighbour_pairs(X, self.r_short + 2.0 * reach)
        self._pair_term(u, x, f, t, s, self.r_short)
        return (Pl @ u.reshape(N, 36, 1))[..., 0].to(torch.float64)

    @torch.no_grad()
    def apply(self, pos, quats, shapes, F, mode: str = "pair") -> np.ndarray:
        """Velocities (N, 6) under loads F (N, 6).  Same as Operator.apply(..., psd=False), without the matrix."""
        op = self.op
        assert mode in ("far", "pair", "full") and (mode == "far" or op.pair is not None) and (mode != "full" or op.nbody is not None)
        shapes = list(shapes)
        t0 = self._now()
        X, R, desc, kinds, kid = op.geometry(pos, quats, shapes)
        F = torch.as_tensor(np.asarray(F, dtype=np.float64), device=self.dev).reshape(len(X), 6)
        v = self.far(X, R, shapes, F)
        t1 = self._now()
        v += (op.iso_blocks(shapes, R) @ F[:, :, None])[..., 0]
        if mode != "far":
            lmax = float(P.length(desc).max())
            cut = op.pair.r_cut * lmax if op.pair.cut == "distance" else op.pair.r_cut * 2.0 * float(desc["amax"].max())
            if mode == "full":
                cut = max(cut, op.nbody.pair_cutoff * lmax)
            t, s = neighbour_pairs(X, cut)
            T, S = torch.cat([t, s]), torch.cat([s, t])
            for i in range(0, len(T), op.pair_chunk):
                a, b = T[i:i + op.pair_chunk], S[i:i + op.pair_chunk]
                cross, self_, g = op.two_body(X, R, desc, kinds, kid, a, b)
                corr = cross - op.far(X, R, kinds, kid, a, b)                       # the far field is already in v
                v.index_add_(0, a, (corr @ F[b][:, :, None])[..., 0] + (self_ @ F[a][:, :, None])[..., 0])
                if mode == "full":
                    keep = (X[b] - X[a]).norm(dim=-1) / P.pair_length(P.take(desc, a), P.take(desc, b)) < op.nbody.pair_cutoff
                    if bool(keep.any()):
                        a2, b2 = a[keep], b[keep]
                        v.index_add_(0, a2, (op.many_body(X, desc, a2, b2, g[keep]) @ F[b2][:, :, None])[..., 0])
            if mode == "full" and op.nself is not None:
                v += (op.many_self(X, desc) @ F[:, :, None])[..., 0]
        t2 = self._now()
        self.times = {"far": t1 - t0, "learned": t2 - t1, "total": t2 - t0}
        return v.cpu().numpy()


def lattice_config(kinds, N: int, phi: float, rng):
    """N particles (shapes cycled from kinds) on a jittered cubic lattice, random orientations, spacing set by phi but
    never below 2.1 x the longest semi-axis (so no two can touch).  For timing large N, where random placement with
    overlap checks would take longer than the test.  -> pos, quats, shapes, the volume fraction actually reached."""
    shapes = [kinds[i % len(kinds)] for i in range(N)]
    vmean = float(np.mean([volume(k) for k in kinds]))
    amax = max(float(axes_of(k).max()) for k in kinds)
    a = max((vmean / phi) ** (1.0 / 3.0), 2.1 * amax)
    n = int(math.ceil(N ** (1.0 / 3.0)))
    g = np.stack(np.meshgrid(*(np.arange(n),) * 3, indexing="ij"), -1).reshape(-1, 3)[:N] * a
    pos = g + rng.uniform(-0.02 * a, 0.02 * a, size=g.shape)
    return pos, random_quats(rng, N), shapes, vmean / a ** 3
