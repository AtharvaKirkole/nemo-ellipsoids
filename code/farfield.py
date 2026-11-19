"""Analytic far field of any two ellipsoids: 12 Stokeslets per particle (the anisotropic counterpart of RPY).

Each particle is 12 plain Stokeslets on its surface, at x = R diag(a) y with y the vertices of the icosahedron on the
unit sphere (an integration rule exact to degree 5):

    U      = (1/12) sum u(x_j)                              surface mean of the fluid velocity (Faxen, to second order)
    grad u = (3/12) sum (y_jl / a_l) u(x_j)                 volume mean, by the divergence theorem
    Omega  = 1/2 curl u + lam_i E_jk,  lam_i = (a_j^2 - a_k^2) / (a_j^2 + a_k^2)       Jeffery's rotation law

So [U; Omega] = C : u with a constant body-frame operator C (6, 12, 3), and the pair block is

    M_ts = P_t G P_s^T        (P = C rotated to the lab frame, G the 36 x 36 Stokeslet matrix between the two point sets)

reciprocal (M_st = M_ts^T) by construction, for any two shapes and sizes, with no fitted parameter.  It needs no
torque kernel: P^T turns a force and torque into 12 point forces.  Error against fine MFS at r = 12 for the 1:1:3
prolate: 0.005 / 0.054 / 0.053 / 0.188 % of the four 3x3 parts (measured when the far field was chosen).
The operator uses it for every pair beyond the pair model's range and blends into it across the last unit of r.
"""
from __future__ import annotations

import math

import torch

from geometry import axes_of

INV_8PI = 1.0 / (8.0 * math.pi)
_BODY: dict = {}


def icosahedron(dtype=torch.float64, device="cpu") -> torch.Tensor:
    g = (1.0 + 5.0 ** 0.5) / 2.0
    p = []
    for s1 in (1.0, -1.0):
        for s2 in (1.0, -1.0):
            p += [[0.0, s1, s2 * g], [s1, s2 * g, 0.0], [s2 * g, 0.0, s1]]
    p = torch.tensor(p, dtype=dtype, device=device)
    return p / p.norm(dim=1, keepdim=True)


def body_operator(shape: str, dtype=torch.float64, device="cpu"):
    """-> points (12, 3) and C (6, 12, 3) in the body frame: [U; Omega]_body = C : u_body."""
    key = (shape, dtype, str(device))
    if key not in _BODY:
        Y = icosahedron(dtype, device)
        ax = torch.as_tensor(axes_of(shape), dtype=dtype, device=device)
        n, a2 = len(Y), ax ** 2
        C = torch.zeros(6, n, 3, dtype=dtype, device=device)
        C[0, :, 0] = C[1, :, 1] = C[2, :, 2] = 1.0 / n
        grad = torch.zeros(3, 3, n, 3, dtype=dtype, device=device)         # grad[m, l] = d u_m / d x_l
        for l in range(3):
            for m in range(3):
                grad[m, l, :, m] = 3.0 / n * Y[:, l] / ax[l]
        for i in range(3):
            j, k = (i + 1) % 3, (i + 2) % 3
            lam = (a2[j] - a2[k]) / (a2[j] + a2[k])
            C[3 + i] = 0.5 * (grad[k, j] - grad[j, k]) + lam * 0.5 * (grad[j, k] + grad[k, j])
        _BODY[key] = (Y * ax, C)
    return _BODY[key]


def _lab_operator(C: torch.Tensor, R: torch.Tensor) -> torch.Tensor:
    """(B, 6, 36): [U; Omega]_lab = P u_lab."""
    n = C.shape[1]
    Pb = (C[None] @ R.transpose(1, 2)[:, None]).reshape(len(R), 6, 3 * n)
    return torch.cat([R @ Pb[:, :3], R @ Pb[:, 3:]], 1)


def far_blocks(shape_t: str, shape_s: str, d: torch.Tensor, Rt: torch.Tensor, Rs: torch.Tensor) -> torch.Tensor:
    """Cross blocks (B, 6, 6) M_ts of pairs with d = x_s - x_t (B, 3) and frames Rt, Rs (B, 3, 3)."""
    bt, Ct = body_operator(shape_t, d.dtype, d.device)
    bs, Cs = body_operator(shape_s, d.dtype, d.device)
    pt, ps = bt @ Rt.transpose(1, 2), d[:, None, :] + bs @ Rs.transpose(1, 2)
    x = pt[:, :, None, :] - ps[:, None, :, :]
    r2 = (x ** 2).sum(-1)
    eye = torch.eye(3, dtype=d.dtype, device=d.device)
    G = (eye / r2.sqrt()[..., None, None] + x[..., None] * x[..., None, :] / (r2 ** 1.5)[..., None, None]) * INV_8PI
    B, n, m = G.shape[:3]
    Gm = G.permute(0, 1, 3, 2, 4).reshape(B, 3 * n, 3 * m)
    return _lab_operator(Ct, Rt) @ Gm @ _lab_operator(Cs, Rs).transpose(1, 2)


def far_blocks_mixed(shapes_t, shapes_s, d, Rt, Rs, chunk: int = 8192) -> torch.Tensor:
    """far_blocks for rows whose shapes differ row by row (lists of names, one per row)."""
    out = torch.zeros(len(d), 6, 6, dtype=d.dtype, device=d.device)
    combos: dict = {}
    for i, c in enumerate(zip(shapes_t, shapes_s)):
        combos.setdefault(c, []).append(i)
    for (st, ss), idx in combos.items():
        idx = torch.as_tensor(idx, device=d.device)
        for i in range(0, len(idx), chunk):
            j = idx[i:i + chunk]
            out[j] = far_blocks(st, ss, d[j], Rt[j], Rs[j])
    return out


def window(r: torch.Tensor, r_cut: float, taper: float = 1.0) -> torch.Tensor:
    """1 for r <= r_cut - taper, 0 for r >= r_cut, C^1 cosine ramp between: learned inside, far field outside."""
    t = ((r - (r_cut - taper)) / taper).clamp(0.0, 1.0)
    return 0.5 * (1.0 + torch.cos(math.pi * t))


# ----------------------------------------------------------------------------------------------- stress and strain
# The same 12 points carry the stresslet and feel the strain.  With Q (5, 12, 3) the mean rate of strain of the fluid
# over the particle (the symmetric traceless part of grad u above, in truth.STRAIN_BASIS) and Z (5, 5) the stresslet
# of the free particle per unit strain (from its cloud):
#
#     a particle with force / torque [F; T] in a strain E puts the point forces  P^T [F; T] - Q^T Z E  on the fluid
#     (their stresslet is exactly  g [F; T] + Z E,  since the moment of Q^T is the identity);
#     the fluid velocity u at its 12 points gives it  [U; Omega] = P u  and the stresslet  S = Z Q u  (Faxen).
#
# So with  P11 = [P; Z Q]  (11, 36):   block_ts = P11_t G P11_s^T diag(1 x 6, -1 x 5),
# reciprocal by construction (velocity-from-strain (t, s) = - [stresslet-from-force (s, t)]^T), no fitted parameter.
_BODY11: dict = {}
_S2, _S6 = 0.5 ** 0.5, 6.0 ** -0.5
_E5 = [[[_S2, 0, 0], [0, -_S2, 0], [0, 0, 0]], [[_S6, 0, 0], [0, _S6, 0], [0, 0, -2 * _S6]],
       [[0, _S2, 0], [_S2, 0, 0], [0, 0, 0]], [[0, 0, _S2], [0, 0, 0], [_S2, 0, 0]], [[0, 0, 0], [0, 0, _S2], [0, _S2, 0]]]


def body_operator11(shape: str, acc: str = "fine", dtype=torch.float64, device="cpu"):
    """-> points (12, 3), C (6, 12, 3), ZQ (5, 12, 3) in the body frame, and the single-particle matrix G1 (11, 11)."""
    key = (shape, acc, dtype, str(device))
    if key not in _BODY11:
        from truth import dense_grand
        import numpy as np
        pts, C = body_operator(shape, dtype, device)
        ax = torch.as_tensor(axes_of(shape), dtype=dtype, device=device)
        E5 = torch.tensor(_E5, dtype=dtype, device=device)
        G1 = torch.as_tensor(dense_grand(np.zeros((1, 3)), np.array([[0.0, 0.0, 0.0, 1.0]]), [shape], acc), dtype=dtype, device=device)
        from truth import iso_mobility                      # made reciprocal: the same 6 x 6 corner as the mobility operator,
        G1[:6, :6] = torch.as_tensor(iso_mobility(shape, acc), dtype=dtype, device=device)
        G1[6:, :6] = 0.5 * (G1[6:, :6] - G1[:6, 6:].T)      # stresslet from force = - (velocity from strain)^T,
        G1[:6, 6:] = -G1[6:, :6].T
        G1[6:, 6:] = 0.5 * (G1[6:, 6:] + G1[6:, 6:].T)      # a symmetric stresslet-from-strain block
        Q = 3.0 / len(pts) * torch.einsum("aml,jl->ajm", E5, pts / ax ** 2)          # E_a = sum Q[a, j, m] u_m(x_j)
        Z = G1[6:, 6:]
        _BODY11[key] = (pts, C, torch.einsum("ab,bjm->ajm", Z, Q), G1)
    return _BODY11[key]


def rot5(R: torch.Tensor) -> torch.Tensor:
    """(B, 5, 5): the components of a symmetric traceless matrix in the lab frame from those in the body frame."""
    E5 = torch.tensor(_E5, dtype=R.dtype, device=R.device)
    return torch.einsum("aij,bik,bjl,ckl->bac", E5, R, R, E5)


def rot11(R: torch.Tensor) -> torch.Tensor:
    """(B, 11, 11): block rotation of [U; Omega; S]."""
    T = torch.zeros(len(R), 11, 11, dtype=R.dtype, device=R.device)
    T[:, :3, :3] = T[:, 3:6, 3:6] = R
    T[:, 6:, 6:] = rot5(R)
    return T


def lab_operator11(C: torch.Tensor, ZQ: torch.Tensor, R: torch.Tensor) -> torch.Tensor:
    """(B, 11, 36): [U; Omega; S]_lab = P11 u_lab."""
    Sb = (ZQ[None] @ R.transpose(1, 2)[:, None]).reshape(len(R), 5, -1)
    return torch.cat([_lab_operator(C, R), rot5(R) @ Sb], 1)


def far_blocks11(shape_t: str, shape_s: str, d, Rt, Rs, acc: str = "fine") -> torch.Tensor:
    """Cross blocks (B, 11, 11) of truth.dense_grand for pairs with d = x_s - x_t: rows [U; Omega; S] of t, columns
    [F; T; E] of s.  The 6 x 6 corner is far_blocks."""
    bt, Ct, Zt, _ = body_operator11(shape_t, acc, d.dtype, d.device)
    bs, Cs, Zs, _ = body_operator11(shape_s, acc, d.dtype, d.device)
    pt, ps = bt @ Rt.transpose(1, 2), d[:, None, :] + bs @ Rs.transpose(1, 2)
    x = pt[:, :, None, :] - ps[:, None, :, :]
    r2 = (x ** 2).sum(-1)
    eye = torch.eye(3, dtype=d.dtype, device=d.device)
    G = (eye / r2.sqrt()[..., None, None] + x[..., None] * x[..., None, :] / (r2 ** 1.5)[..., None, None]) * INV_8PI
    B, n, m = G.shape[:3]
    Gm = G.permute(0, 1, 3, 2, 4).reshape(B, 3 * n, 3 * m)

    out = lab_operator11(Ct, Zt, Rt) @ Gm @ lab_operator11(Cs, Zs, Rs).transpose(1, 2)
    out[:, :, 6:] = -out[:, :, 6:]
    return out


def far_grand(pos, R, shapes, acc: str = "fine") -> torch.Tensor:
    """The whole (11 P, 11 P) matrix of truth.dense_grand from the far field alone: single-particle blocks on the
    diagonal (rotated), far_blocks11 off it.  pos (P, 3) and R (P, 3, 3) tensors."""
    P = len(pos)
    out = torch.zeros(P, 11, P, 11, dtype=pos.dtype, device=pos.device)
    T = rot11(R)
    for p in range(P):
        G1 = body_operator11(shapes[p], acc, pos.dtype, pos.device)[3]
        out[p, :, p, :] = T[p] @ G1 @ T[p].T
    for kt in dict.fromkeys(shapes):
        for ks in dict.fromkeys(shapes):
            it = [i for i, s in enumerate(shapes) if s == kt]
            js = [j for j, s in enumerate(shapes) if s == ks]
            ii, jj = [x.reshape(-1) for x in torch.meshgrid(torch.as_tensor(it), torch.as_tensor(js), indexing="ij")]
            keep = ii != jj
            ii, jj = ii[keep], jj[keep]
            if len(ii):
                out[ii, :, jj, :] = far_blocks11(kt, ks, pos[jj] - pos[ii], R[ii], R[jj], acc)
    return out.reshape(11 * P, 11 * P)
