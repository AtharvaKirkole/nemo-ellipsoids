"""MixedFastMFS: FastMFS (the CUDA truth solver) for suspensions of DIFFERENT shapes, one MFS template per particle.

The equations are those of truth.dense_mobility (each particle its own boundary nodes, sources and
pseudo-inverse), solved like FastMFS: GMRES on the boundary velocities W, the off-diagonal Oseen sum by the fused CUDA
kernels (mfs_cuda.py), optional warm start between consecutive solves.

How one solver carries several templates: every template is PADDED to the largest node count N and source count M.
  * padded sources sit at the particle centre with zero strength: their rows of K_f and C are zero, so f stays 0 there
    and they add nothing to any other particle's field;
  * padded boundary nodes sit at the particle centre too: their columns of K_f and K_v are zero (they never drive the
    particle) and their rows of W are zeroed after every Oseen apply, so they stay outside the Krylov space.
The padded points never coincide with a point of another particle (particles do not overlap), so every Oseen entry
stays finite.  With one shape this IS FastMFS(far=False); with several it reproduces dense_mixed to the solver
tolerance (tests/test_mfs_mixed.py).

    solver = MixedFastMFS(["prolateSpheroid", "oblateSpheroid"], device="cuda")
    vel, info = solver.solve(pos, F, orientations=q, shapes=["prolateSpheroid", "oblateSpheroid", ...])
    M, info = solver.solve_mobility_matrix(pos, q, shapes=[...])

Per-particle K_f, K_v and C are applied per shape on the columns of the particles of that shape (column p*R + r).
No ambient flow and no far skeletons (the truth runs never use either).
"""
from __future__ import annotations

import os
from typing import Optional, Sequence

import numpy as np
import torch

from .mfs_batched import POINTS_DIR, _Ctx, load_template
from .mfs_fast import FastMFS


class _PerShape:
    """Block-diagonal operator: mats[kind[p]] acts on the columns of particle p (layout of BatchedMFS)."""

    def __init__(self, mats: Sequence[torch.Tensor], owner: "MixedFastMFS"):
        self.mats, self.owner = list(mats), owner

    def __matmul__(self, X: torch.Tensor) -> torch.Tensor:
        cols = self.owner._column_kinds(X.shape[1])
        out = torch.zeros(self.mats[0].shape[0], X.shape[1], dtype=X.dtype, device=X.device)
        for k, A in enumerate(self.mats):
            idx = cols[k]
            if idx is not None:
                out[:, idx] = A.to(X.dtype) @ X[:, idx]
        return out


class MixedFastMFS(FastMFS):
    def __init__(self, kinds: Sequence[str], acc: str = "fine", device="cuda", kernel: str = "cuda",
                 warm_start: bool = True, tol_v: float = 1e-7, mem_budget_gb: Optional[float] = None,
                 points_dir: str = POINTS_DIR, **kw):
        kinds = list(dict.fromkeys(kinds))
        dev = torch.device(device)
        if mem_budget_gb is None:
            mem_budget_gb = 0.45 * torch.cuda.get_device_properties(dev).total_memory / 2 ** 30 if dev.type == "cuda" else 8.0
        super().__init__(acc=acc, device=device, shape=kinds[0], far=False, kernel=kernel, warm_start=warm_start,
                         tol_v=tol_v, mem_budget_gb=mem_budget_gb, points_dir=points_dir, **kw)
        self.kinds = kinds
        tm = [load_template(acc, points_dir, k) for k in kinds]
        N, M = max(len(b) for b, _, _ in tm), max(len(s) for _, s, _ in tm)
        K = len(kinds)
        f64 = dict(dtype=torch.float64, device=self.device)
        bp, sp = torch.zeros(K, N, 3, **f64), torch.zeros(K, M, 3, **f64)
        Kf, Kv = torch.zeros(K, 3 * M, 3 * N, **f64), torch.zeros(K, 6, 3 * N, **f64)
        C, mask = torch.zeros(K, 3 * M + 6, 6, **f64), torch.zeros(K, 3 * N, **f64)
        self.sizes = {}
        for k, (b, s, B_inv) in enumerate(tm):
            n, m = len(b), len(s)
            Bt = torch.as_tensor(B_inv, **f64)
            bp[k, :n], sp[k, :m] = torch.as_tensor(b, **f64), torch.as_tensor(s, **f64)
            Kf[k, :3 * m, :3 * n] = Bt[:3 * m, :3 * n]
            Kv[k, :, :3 * n] = Bt[3 * m:, :3 * n]
            C[k, :3 * m] = Bt[:3 * m, 3 * n:]
            C[k, 3 * M:] = Bt[3 * m:, 3 * n:]
            mask[k, :3 * n] = 1.0
            self.sizes[kinds[k]] = (n, m)
        self.N, self.M = N, M
        self._bp, self._sp, self._nmask = bp, sp, mask
        self.b64, self.s64 = bp[0], sp[0]                        # unused (no ambient flow, no skeletons)
        self.K_f = self.K_f_gemm = _PerShape(list(Kf), self)
        self.K_v = _PerShape(list(Kv), self)
        self.C = _PerShape(list(C), self)
        self._kind_pp: Optional[torch.Tensor] = None
        self._col_cache: dict = {}

    # ------------------------------------------------------------------ shapes per particle
    def _set_shapes(self, shapes, n_sys: int, P_c: int) -> None:
        rows = shapes if (len(shapes) and isinstance(shapes[0], (list, tuple, np.ndarray))) else [shapes] * n_sys
        assert len(rows) == n_sys and all(len(r) == P_c for r in rows), "one shape per particle (per system)"
        unknown = {s for r in rows for s in r} - set(self.kinds)
        assert not unknown, f"shapes {unknown} not in this solver's kinds {self.kinds}"
        kind = torch.as_tensor([self.kinds.index(s) for r in rows for s in r], device=self.device)
        if self._kind_pp is None or kind.shape != self._kind_pp.shape or not torch.equal(kind, self._kind_pp):
            self.release()                                        # other shapes: no cached plan, no warm start
            self._kind_pp = kind
            self._col_cache = {}
            self._mask_pp = self._nmask[kind].T.contiguous()      # (3N, P_tot)

    def _column_kinds(self, LD: int):
        """For each kind, the column indices (layout p*R + r) of its particles, or None."""
        if LD not in self._col_cache:
            P = self._kind_pp.numel()
            assert LD % P == 0, (LD, P)
            ck = self._kind_pp.repeat_interleave(LD // P)
            self._col_cache[LD] = [(ck == k).nonzero().squeeze(1) if bool((ck == k).any()) else None
                                   for k in range(len(self.kinds))]
        return self._col_cache[LD]

    def solve(self, positions, forces, *, shapes, orientations=None, ambient=None, **kw):
        """FastMFS.solve with `shapes`: one shape name per particle ((P,) list), or a list of such lists, one per
        system."""
        assert ambient is None, "MixedFastMFS: no ambient flow"
        pos_list = self._to_positions_list(positions)
        self._set_shapes(shapes, len(pos_list), pos_list[0].shape[0])
        return super().solve(positions, forces, orientations=orientations, **kw)

    def solve_mobility_matrix_batch(self, *a, **kw):
        raise NotImplementedError("MixedFastMFS: solve one configuration at a time (solve_mobility_matrix)")

    # ------------------------------------------------------------------ operator
    def _make_plan(self, ctx: _Ctx) -> dict:
        dev = self.device
        loc = torch.arange(ctx.P_c, device=dev)
        pl, ql = torch.meshgrid(loc, loc, indexing="ij")
        off = pl != ql
        base = (torch.arange(ctx.n_sys, device=dev) * ctx.P_c)[:, None]
        p = (base + pl[off][None]).reshape(-1)
        q = (base + ql[off][None]).reshape(-1)
        body_b, body_s = self._bp[self._kind_pp], self._sp[self._kind_pp]           # (P_tot, N|M, 3)
        if ctx.rot is None:
            bl, sl = body_b + ctx.c64[:, None, :], body_s + ctx.c64[:, None, :]
        else:
            bl = torch.einsum("pij,pnj->pni", ctx.rot, body_b) + ctx.c64[:, None, :]
            sl = torch.einsum("pij,pnj->pni", ctx.rot, body_s) + ctx.c64[:, None, :]
        plan = {"near_p": p, "near_q": q, "far_p": p[:0], "far_q": q[:0], "b_lab": bl.contiguous(),
                "s_lab": sl.contiguous(), "near_cache": [], "n_cached": 0}
        if self.kernel == "cuda":
            plan["csr"] = self._cu.csr(p, q, ctx.P_tot)
        self.stats["plans"] += 1
        self.stats["near_pairs"] += int(len(p))
        return plan

    def oseen_offdiag(self, S: torch.Tensor, ctx: _Ctx) -> torch.Tensor:
        W = super().oseen_offdiag(S, ctx)
        Wv = W.view(3 * self.N, ctx.P_tot, ctx.R) * self._mask_pp[:, :, None].to(W.dtype)
        return Wv.reshape(W.shape)


def mixed_truth_solver(kinds, acc: str = "fine", device="cuda", tol_v: float = 1e-7, warm_start: bool = True,
                       verbose: bool = True) -> MixedFastMFS:
    """The truth solver for mixed suspensions: the CUDA kernel when it builds (MFS_SOLVER=batched forces torch)."""
    kernel = "torch"
    if torch.device(device).type == "cuda" and os.environ.get("MFS_SOLVER", "fast") != "batched":
        from . import mfs_cuda
        kernel = "cuda" if mfs_cuda.available() else "torch"
    if verbose:
        print(f"[mixed truth solver] {kernel} kernel, warm start {warm_start}, shapes {list(kinds)} ({acc})", flush=True)
    from .mfs_fast import tight_kwargs
    return MixedFastMFS(kinds, acc, device, kernel=kernel, warm_start=warm_start, tol_v=tol_v, **tight_kwargs(tol_v))
