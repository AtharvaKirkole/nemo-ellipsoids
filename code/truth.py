"""Ground truth: the Method of Fundamental Solutions (MFS) for rigid ellipsoids in Stokes flow, viscosity 1.

Each particle carries a template in its body frame (data/points/{b,s}_{shape}_{acc}.txt): boundary nodes b (N, 3) on
its surface, Stokeslet sources s (M, 3) inside it, and B^+ = pinv(B), where B maps (source strengths, U, Omega) to
(no-slip residual at the nodes, total force, total torque).  For P particles the discrete problem is

    x_p + B_p^+ [ sum_{q != p} G(b_p, s_q) f_q ; 0 ] = B_p^+ [ 0 ; F_p ; T_p ],      x_p = [f_p ; U_p ; Omega_p]

Two solvers of these SAME equations:
  dense_mobility   one direct solve for all 6P unit loads.  Exact to round-off; pairs and small clusters.
  the iterative solver in truth_mfs/ (GMRES on the boundary velocities, fused CUDA kernels): suspensions of hundreds of particles.  Agrees with the dense solve to the
  GMRES tolerance (1e-7).
`Truth` picks by problem size.  Accuracy levels acc = coarse / medium / fine / Xfine are the cloud resolutions; the
difference between fine and Xfine labels is the LABEL FLOOR quoted next to every model error.
"""
from __future__ import annotations

import numpy as np
import torch

from geometry import POINTS_DIR, axes_of, quat_to_matrix

INV_8PI = 1.0 / (8.0 * np.pi)
_TEMPLATES: dict = {}


def _skew_rows(w: np.ndarray) -> np.ndarray:
    z = np.zeros(w.shape[0])
    return np.stack([np.stack([z, -w[:, 2], w[:, 1]], -1), np.stack([w[:, 2], z, -w[:, 0]], -1),
                     np.stack([-w[:, 1], w[:, 0], z], -1)], -2)


def load_template(shape: str, acc: str = "fine"):
    """-> boundary nodes (N, 3), sources (M, 3), B^+ (3M + 6, 3N + 6), all float64, body frame."""
    key = (shape, acc)
    if key not in _TEMPLATES:
        b = np.loadtxt(f"{POINTS_DIR}/b_{shape}_{acc}.txt", dtype=np.float64)
        s = np.loadtxt(f"{POINTS_DIR}/s_{shape}_{acc}.txt", dtype=np.float64)
        N, M = len(b), len(s)
        r = b[:, None, :] - s[None, :, :]
        inv = 1.0 / np.linalg.norm(r, axis=-1)
        G = (inv[..., None, None] * np.eye(3) + r[..., :, None] * r[..., None, :] * (inv ** 3)[..., None, None]) * INV_8PI
        B = np.zeros((3 * N + 6, 3 * M + 6))
        B[:3 * N, :3 * M] = G.transpose(0, 2, 1, 3).reshape(3 * N, 3 * M)       # velocity at the nodes
        B[:3 * N, 3 * M:3 * M + 3] = -np.tile(np.eye(3), (N, 1))                 # - U
        B[:3 * N, 3 * M + 3:] = _skew_rows(b).reshape(3 * N, 3)                  # - Omega x b
        B[3 * N:3 * N + 3, :3 * M] = np.tile(np.eye(3), (1, M))                  # total force
        B[3 * N + 3:, :3 * M] = _skew_rows(s).transpose(1, 0, 2).reshape(3, 3 * M)   # total torque
        _TEMPLATES[key] = (b, s, np.linalg.pinv(B))
    return _TEMPLATES[key]


def iso_mobility(shape: str, acc: str = "fine") -> np.ndarray:
    """Body-frame 6x6 mobility of ONE isolated particle as its cloud discretises it.  The operator uses this (not the
    exact Oberbeck value) so that the cloud's own error does not leak into the learned self corrections.
    Symmetrised: the exact block is symmetric, the cloud's is not quite (1e-5 on fine clouds, 1e-4 for 1:2:3), and with
    the raw block the assembled grand mobility matrix would not be exactly symmetric."""
    b, s, B_inv = load_template(shape, acc)
    M = B_inv[3 * len(s):, 3 * len(b):]
    return 0.5 * (M + M.T)


def exact_iso_mobility(shape: str) -> np.ndarray:
    """Body-frame 6x6 mobility of ONE isolated ellipsoid, exact (Oberbeck 1876 translation, Jeffery / Edwardes
    rotation), viscosity 1.  With chi = int_0^inf dl / Delta and alpha_i = int_0^inf dl / ((a_i^2 + l) Delta),
    Delta = sqrt(prod (a_k^2 + l)):   U_i / F_i = (chi + a_i^2 alpha_i) / (16 pi),
    Omega_i / T_i = 3 (a_j^2 alpha_j + a_k^2 alpha_k) / (16 pi (a_j^2 + a_k^2)).   Sphere: 1 / (6 pi a), 1 / (8 pi a^3).
    The integrals are Carlson's: chi = 2 R_F(a1^2, a2^2, a3^2), alpha_i = (2/3) R_D(a_j^2, a_k^2, a_i^2)."""
    from scipy.special import elliprd, elliprf
    a2 = axes_of(shape) ** 2
    chi = 2.0 * elliprf(*a2)
    alpha = np.array([2.0 / 3.0 * elliprd(a2[(i + 1) % 3], a2[(i + 2) % 3], a2[i]) for i in range(3)])
    M = np.zeros((6, 6))
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        M[i, i] = (chi + a2[i] * alpha[i]) / (16.0 * np.pi)
        M[3 + i, 3 + i] = 3.0 * (a2[j] * alpha[j] + a2[k] * alpha[k]) / (16.0 * np.pi * (a2[j] + a2[k]))
    return M


def cloud_error(shape: str, acc: str = "fine") -> dict:
    """How well a shape's cloud reproduces the exact isolated mobility: % error of the translation and rotation
    diagonals, the size of what should be zero (off-diagonal, relative), and the cloud's size.  The one MFS error
    that is known ABSOLUTELY (everything else is a difference between two resolutions)."""
    import os
    if not os.path.exists(f"{POINTS_DIR}/b_{shape}_{acc}.txt"):
        return {}
    b, s, B_inv = load_template(shape, acc)
    M, E = B_inv[3 * len(s):, 3 * len(b):], exact_iso_mobility(shape)
    d, e = np.diag(M), np.diag(E)
    off = M - np.diag(d)
    return {"nodes": len(b), "sources": len(s), "trans_pct": float(100 * np.abs(d[:3] / e[:3] - 1).max()),
            "rot_pct": float(100 * np.abs(d[3:] / e[3:] - 1).max()),
            "offdiag": float(max(np.abs(off[:3, :3]).max() / e[:3].max(), np.abs(off[3:, 3:]).max() / e[3:].max())),
            "asym": float(np.abs(M - M.T).max() / np.abs(M).max())}


def have_cloud(shapes, acc: str) -> bool:
    import os
    return all(os.path.exists(f"{POINTS_DIR}/b_{s}_{acc}.txt") for s in set(shapes))


def n_unknowns(shapes, acc: str) -> int:
    return int(sum(3 * len(load_template(s, acc)[1]) + 6 for s in shapes))


def _stokeslet(bp: torch.Tensor, sq: torch.Tensor) -> torch.Tensor:
    """Field points (N, 3), sources (M, 3) -> (3N, 3M)."""
    r = bp[:, None, :] - sq[None, :, :]
    inv = 1.0 / r.norm(dim=-1)
    eye = torch.eye(3, dtype=r.dtype, device=r.device)
    G = inv[..., None, None] * eye + r[..., :, None] * r[..., None, :] * (inv ** 3)[..., None, None]
    return (G * INV_8PI).permute(0, 2, 1, 3).reshape(3 * len(bp), 3 * len(sq))


def dense_mobility(pos, quats, shapes, acc: str = "fine", device="cpu") -> np.ndarray:
    """Grand mobility (6P, 6P), rows 6t + i, columns 6s + j, lab frame, by one direct solve (float64)."""
    f64 = dict(dtype=torch.float64, device=device)
    pos = torch.as_tensor(np.asarray(pos, dtype=np.float64), **f64)
    Rm = torch.as_tensor(quat_to_matrix(quats), **f64)
    P = len(pos)
    tm = [tuple(torch.as_tensor(x, **f64) for x in load_template(sh, acc)) for sh in shapes]
    nus = [3 * len(s0) + 6 for _, s0, _ in tm]
    off = np.concatenate([[0], np.cumsum(nus)])
    bnd = [tm[p][0] @ Rm[p].T + pos[p] for p in range(P)]
    src = [tm[p][1] @ Rm[p].T + pos[p] for p in range(P)]
    A = torch.eye(int(off[-1]), **f64)
    rhs = torch.zeros(int(off[-1]), 6 * P, **f64)
    for p in range(P):
        b0, s0, B_inv = tm[p]
        N, M = len(b0), len(s0)
        Bp = torch.einsum("ia,mank,jk->minj", Rm[p], B_inv.reshape(M + 2, 3, N + 2, 3), Rm[p]).reshape(3 * M + 6, 3 * N + 6)
        rhs[off[p]:off[p + 1], 6 * p:6 * p + 6] = Bp[:, 3 * N:]
        for q in range(P):
            if q != p:
                A[off[p]:off[p + 1], off[q]:off[q] + 3 * len(tm[q][1])] = Bp[:, :3 * N] @ _stokeslet(bnd[p], src[q])
    sol = torch.linalg.solve(A, rhs)
    rows = torch.cat([torch.arange(off[p] + nus[p] - 6, off[p] + nus[p], device=device) for p in range(P)])
    return sol[rows].cpu().numpy()


# ----------------------------------------------------------------------------------------------- stress and strain
# The five traceless symmetric 3x3 matrices, orthonormal (e_a : e_b = delta_ab): a rate of strain E and a stresslet S
# are 5 numbers each, E = sum_a E_a e_a.
_S2, _S6 = 1.0 / np.sqrt(2.0), 1.0 / np.sqrt(6.0)
STRAIN_BASIS = np.array([[[_S2, 0, 0], [0, -_S2, 0], [0, 0, 0]], [[_S6, 0, 0], [0, _S6, 0], [0, 0, -2 * _S6]],
                         [[0, _S2, 0], [_S2, 0, 0], [0, 0, 0]], [[0, 0, _S2], [0, 0, 0], [_S2, 0, 0]],
                         [[0, 0, 0], [0, 0, _S2], [0, _S2, 0]]])


def dense_grand(pos, quats, shapes, acc: str = "fine", device="cpu") -> np.ndarray:
    """The grand matrix with stress and strain, (11P, 11P), lab frame, by one direct solve:

        [U; Omega; S]_t = sum_s G_ts [F; T; E]_s          rows 11 t + (0..5 velocity, 6..10 stresslet)
                                                           columns 11 s + (0..5 force / torque, 6..10 strain)

    F, T: force and torque on particle s.  E_s: a straining flow u = E (x - x_s) seen by particle s (the fluid far
    away is at rest for the others; a uniform strain of the whole suspension is E_s = E for every s).  U, Omega: velocities.
    S_t: the stresslet of particle t, in the usual sign (a rigid sphere of radius a in a strain E has S = (20 pi / 3) a^3 E,
    positive: it raises the viscosity) = minus the symmetric, traceless first moment, about its centre, of the forces the
    particle puts on the fluid.  E and S in the basis STRAIN_BASIS.  The 6 x 6 force-velocity corner is dense_mobility.
    Checked (tests.py): the sphere's (20 pi / 3) and Einstein's 5 / 2; Jeffery's rotation of an ellipsoid in a strain,
    Omega_i = (a_j^2 - a_k^2) / (a_j^2 + a_k^2) E_jk; reciprocity, velocity-from-strain (t, s) = - [stresslet-from-force
    (s, t)]^T; a symmetric stresslet-from-strain block.

    Same equations as dense_mobility; a straining flow only changes the right-hand side (the no-slip condition at the
    nodes of particle s becomes u_sources = U + Omega x r - E r), and the stresslet is read from the source strengths."""
    f64 = dict(dtype=torch.float64, device=device)
    pos = torch.as_tensor(np.asarray(pos, dtype=np.float64), **f64)
    Rm = torch.as_tensor(quat_to_matrix(quats), **f64)
    E5 = torch.as_tensor(STRAIN_BASIS, **f64)
    P = len(pos)
    tm = [tuple(torch.as_tensor(x, **f64) for x in load_template(sh, acc)) for sh in shapes]
    nus = [3 * len(s0) + 6 for _, s0, _ in tm]
    off = np.concatenate([[0], np.cumsum(nus)])
    bnd = [tm[p][0] @ Rm[p].T + pos[p] for p in range(P)]
    src = [tm[p][1] @ Rm[p].T + pos[p] for p in range(P)]
    A = torch.eye(int(off[-1]), **f64)
    rhs = torch.zeros(int(off[-1]), 11 * P, **f64)
    for p in range(P):
        b0, s0, B_inv = tm[p]
        N, M = len(b0), len(s0)
        Bp = torch.einsum("ia,mank,jk->minj", Rm[p], B_inv.reshape(M + 2, 3, N + 2, 3), Rm[p]).reshape(3 * M + 6, 3 * N + 6)
        rhs[off[p]:off[p + 1], 11 * p:11 * p + 6] = Bp[:, 3 * N:]
        rel = bnd[p] - pos[p]                                             # (N, 3) nodes about the centre, lab frame
        strain = -torch.einsum("aij,nj->ani", E5, rel).reshape(5, 3 * N)  # - E r at the nodes, one row per basis strain
        rhs[off[p]:off[p + 1], 11 * p + 6:11 * p + 11] = Bp[:, :3 * N] @ strain.T
        for q in range(P):
            if q != p:
                A[off[p]:off[p + 1], off[q]:off[q] + 3 * len(tm[q][1])] = Bp[:, :3 * N] @ _stokeslet(bnd[p], src[q])
    sol = torch.linalg.solve(A, rhs)
    G = torch.zeros(11 * P, 11 * P, **f64)
    for p in range(P):
        M = len(tm[p][1])
        G[11 * p:11 * p + 6] = sol[off[p] + 3 * M:off[p] + 3 * M + 6]
        moment = torch.einsum("aij,mj->ami", E5, src[p] - pos[p]).reshape(5, 3 * M)       # sum_j f_j . e_a r_j
        G[11 * p + 6:11 * p + 11] = -moment @ sol[off[p]:off[p] + 3 * M]                   # f = force ON the fluid: S = - moment
    return G.cpu().numpy()


def intrinsic_viscosity(shape: str, acc: str = "fine") -> float:
    """[eta] of a dilute suspension of this particle at random orientation, from its cloud: the suspension's viscosity
    is 1 + [eta] phi.  = (trace of the particle's 5 x 5 stresslet-per-strain block) / (10 x its volume); 5 / 2 for a
    sphere (Einstein)."""
    G = dense_grand(np.zeros((1, 3)), np.array([[0.0, 0.0, 0.0, 1.0]]), [shape], acc)
    return float(np.trace(G[6:, 6:]) / (10.0 * 4.0 / 3.0 * np.pi * np.prod(axes_of(shape))))


class Truth:
    """MFS truth for configurations of the given shape kinds.  Small problems: the direct solve.  Large ones: the
    iterative CUDA solver (built on first use).  dense_limit = unknowns up to which the direct solve is used."""

    def __init__(self, kinds, acc: str = "fine", device: str | None = None, tol_v: float = 1e-7, dense_limit: int = 16000,
                 warm_start: bool = False):
        self.kinds, self.acc, self.tol_v = list(dict.fromkeys(kinds)), acc, tol_v
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.dense_limit, self.warm_start, self._solver = int(dense_limit), warm_start, None
        self.block = 4                                     # particles per column block of an iterative mobility solve

    def _iterative(self):
        """The fast solver (fused CUDA kernel when it builds).  Used for few-column solves (Fig. 3 / 4 loads)."""
        if self._solver is None:
            from truth_mfs.mfs_mixed import mixed_truth_solver
            self._solver = mixed_truth_solver(self.kinds, self.acc, self.device, self.tol_v, self.warm_start)
        return self._solver

    def _iterative_torch(self):
        """The same equations with the plain torch kernel, for many-column solves (whole mobility matrices).  On the
        GPU the fused CUDA kernel returned wrong matrices for 24 or more columns at once (self-check 2026-11-11:
        asymmetry 1.4), while this path matches the direct solve to 1e-9."""
        if getattr(self, "_solver_t", None) is None:
            from truth_mfs.mfs_fast import tight_kwargs
            from truth_mfs.mfs_mixed import MixedFastMFS
            self._solver_t = MixedFastMFS(self.kinds, self.acc, self.device, kernel="torch", warm_start=False,
                                          tol_v=self.tol_v, **tight_kwargs(self.tol_v))
        return self._solver_t

    def _solve(self, solver, pos, quats, shapes, F):
        vel, info = solver.solve(np.asarray(pos), F, orientations=np.asarray(quats), shapes=list(shapes), raise_on_fail=False)
        assert bool(info.converged), "MFS did not converge"
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        return np.asarray(vel.cpu() if torch.is_tensor(vel) else vel, dtype=np.float64).reshape(F.shape)

    def is_dense(self, shapes) -> bool:
        return n_unknowns(shapes, self.acc) <= self.dense_limit

    def mobility(self, pos, quats, shapes) -> np.ndarray:
        """(6P, 6P) float64."""
        if self.is_dense(shapes):
            return dense_mobility(pos, quats, shapes, self.acc, self.device)
        # Column by column, a few particles' unit loads at a time, through the same few-column solve that the suspension
        # truths use.  (The one-shot 6P-column solve_mobility_matrix diverged on the GPU for clusters: residual 1.1,
        # and where it did not stop, it returned matrices 50-100 % off; 2026-11-11.)
        P = len(pos)
        M = np.zeros((6 * P, 6 * P))
        for p0 in range(0, P, self.block):
            ps = list(range(p0, min(P, p0 + self.block)))
            F = np.zeros((P, 6, 6 * len(ps)))
            for k, p in enumerate(ps):
                F[p, :, 6 * k:6 * k + 6] = np.eye(6)
            M[:, 6 * p0:6 * p0 + F.shape[2]] = self._solve(self._iterative_torch(), pos, quats, shapes, F).reshape(6 * P, -1)
        asym = np.linalg.norm(M - M.T) / np.linalg.norm(M)
        assert asym < 5e-2, f"MFS mobility not symmetric ({asym:.1e}): not converged"   # coarse clouds: ~1e-2; fine: ~1e-4
        return M

    def velocities(self, pos, quats, shapes, F) -> np.ndarray:
        """Loads F (P, 6[, k]) -> velocities of the same shape."""
        F = np.asarray(F, dtype=np.float64)
        if self.is_dense(shapes):
            M = dense_mobility(pos, quats, shapes, self.acc, self.device)
            return (M @ F.reshape(6 * len(pos), -1)).reshape(F.shape)
        if F.ndim == 2:                  # one load case: the iterative solver wants a column axis (it failed without: the
            return self.velocities(pos, quats, shapes, F[:, :, None])[:, :, 0]     # Xfine ring runs of 2026-11-13)
        # At most 6 load columns per fast-kernel solve: on the GPU the fused kernel is exact for 1-6 columns (1e-8) but
        # wrong for 24 (0.65 relative error, self-check 2026-11-11), so larger load sets go through in batches of 6.
        out = np.empty_like(F)
        for c in range(0, F.shape[2], 6):
            out[:, :, c:c + 6] = self._solve(self._iterative(), pos, quats, shapes, np.ascontiguousarray(F[:, :, c:c + 6]))
        return out


if __name__ == "__main__":
    # Self-check on this machine (GPU if present), every solver path against the direct solve on a small mixed cluster:
    #   python <this folder>/truth.py [shape ...]        (from the workspace)
    # Exit 1 if a path that the pipeline relies on is off by more than 1e-5.
    import sys
    from geometry import assign_shapes, grown_config
    kinds = sys.argv[1:] or ["prolateSpheroid", "oblateSpheroid"]
    rng = np.random.default_rng(11)
    sh = assign_shapes(kinds, 6, rng)
    pos, q = grown_config(sh, 0.1, rng)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    Md = dense_mobility(pos, q, sh, "fine", dev)
    T = Truth(kinds, "fine", dense_limit=0)
    rel = lambda a, b: float(np.linalg.norm(a - b) / np.linalg.norm(b))
    out = {}
    for k in (1, 2, 6, 24):                          # the fast kernel with k load columns at once
        F = rng.normal(size=(6, 6, k))
        try:
            out[f"fast kernel, {k} columns"] = rel(T.velocities(pos, q, sh, F), (Md @ F.reshape(36, k)).reshape(F.shape))
        except Exception as e:                       # noqa: BLE001
            out[f"fast kernel, {k} columns"] = f"failed: {str(e)[:80]}"
    try:
        out["mobility matrix (torch kernel, used for clusters)"] = rel(T.mobility(pos, q, sh), Md)
    except Exception as e:                           # noqa: BLE001
        out["mobility matrix (torch kernel, used for clusters)"] = f"failed: {str(e)[:80]}"
    for name, v in out.items():
        print(f"  {name:52} {v if isinstance(v, str) else f'{v:.2e}'}")
    need = list(out.values())        # every path, the 24-column one included (it now runs as batches of 6)
    ok = all(not isinstance(v, str) and v < 1e-5 for v in need)
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
