"""Two-body model for ellipsoids, in the two forms that were selected (one code, one training, one operator):

    form "spheroid"   prolate / oblate spheroids of any aspect ratio and size.   12 inputs, 12 true + 27 pseudo tensors,
                      range r_cut = 12.  A particle enters through its symmetry axis n (a line, not an arrow).
    form "triaxial"   general ellipsoids (three semi-axes); spheroids and spheres are special cases of the same
                      network.   22 inputs, 34 true + 61 pseudo tensors, range r_cut = 14.  A particle enters only
                      through its shape tensor D = 3 A / tr(A) - I and D^2 (A = R diag(a^2) R^T), never through a frame.

For an ordered pair (target t, source s) with d = x_s - x_t = r z the network predicts two 6x6 lab-frame blocks as
scalar coefficients on analytic tensors, K = sum_n c_n(inputs) T_n:

    cross   M_ts                       velocity of t per unit force / torque on s
    self    M_tt - M_iso(R_t)          what the presence of s does to t's own mobility

Inputs.  Every length is in units of the pair length l = sqrt(l_t l_s), l_p = shortest semi-axis of particle p.
    spheroid   1/r, (a.z)^2, (b.z)^2, (a.b)^2, (a.z)(b.z)(a.b);  1/r^2, 1/r^3, g, 1/(g + 0.5);
               log kappa_t, log kappa_s (aspect ratio, > 0 prolate), log(l_t / l_s)                              = 12
    triaxial   with P_1 = D_t, P_2 = D_t^2, Q_1 = D_s, Q_2 = D_s^2:
               1/r;  z.P_i.z (2), z.Q_j.z (2);  tr(P_i Q_j) (4);  z.P_i Q_j.z (4);
               shape code of t and of s (log a_mid/a_min, log a_max/a_min), log(l_t / l_s);
               1/r^2, 1/r^3, g, 1/(g + 0.5)                                                                      = 22
    g = r (1 - 1/c) is the clearance (c the contact factor).  The four "radial extras" are redundant functions that
    resolve near contact (20-35 % better on prolate spheroids); the sign-carrying products (a.z)(b.z)(a.b) and
    z.P_i Q_j.z cannot be dropped (9-20x and 4x worse without).

Tensors.  TT and RR are built on true tensors, TR and RT on pseudotensors (they change sign under a reflection).
    spheroid   N_a = a a^T, N_b = b b^T, u_a = (a.z) a, u_b = (b.z) b, E(v) x = v x x:
               true    I, z z^T, N_a, N_b, N_a N_b, N_b N_a, z u_a^T, u_a z^T, z u_b^T, u_b z^T, u_a u_b^T, u_b u_a^T
               pseudo  E(z), E(u_a), E(u_b); v w^T, w v^T for v in {z, u_a, u_b}, w in {z x u_a, z x u_b, (a.b) a x b};
                       N_a E(z), E(z) N_a, N_b E(z), E(z) N_b, N_a E(z) N_b, N_b E(z) N_a
    triaxial   N = [P_1, P_2, Q_1, Q_2], u_i = N_i z, w_i = z x u_i:
               true    I, z z^T, N_i, N_i N_j and N_j N_i (target x source), z u_i^T, u_i z^T, u_i u_j^T, u_j u_i^T
               pseudo  E(z), E(u_i), N_i E(z), E(z) N_i, N_i E(z) N_j, z w_i^T, w_i z^T, tr(E(z) N_j N_i) z z^T,
                       u_p w_q^T, w_q u_p^T
    Coefficients per block: 2 n_true + 2 n_pseudo = 78 (spheroid), 190 (triaxial); the network has two such heads.

Exact by construction, for any weights (tests.py): rotation and reflection equivariance; reciprocity M_st = M_ts^T
(swap average, exchanging shapes and sizes with the particles); symmetric self block; continuity into the far field
(learned part x w(r / l), w = 1 inside, 0 from r_cut on); Stokes similarity (enlarging the pair by lam scales TT,
TR / RT, RR by 1/lam, 1/lam^2, 1/lam^3: lengths in units of l, blocks scaled back, only the size RATIO is an input);
spheroid form: invariance to the sign of each axis.
Outputs in units of 1/(6 pi), pre-scaled by their point-particle decay (TT 1/r, TR / RT 1/r^2, RR 1/r^3, self 1/r^4).
There is no Oseen (or any other) base inside r_cut: the network is the whole near-field block.

Range of the learned part (`cut`).  Two choices, stored with the model:
    "distance"  w(r / l): learned inside r_cut pair lengths (12 spheroid form, 14 triaxial).  The first models.
    "contact"   w(c): learned inside contact factor c_cut = 4, far field beyond.  The error of the far field is a
                function of the contact factor and nearly the same for every shape (medium clouds, 2026-11-13: cross
                block 0.2-0.4 % at c 2-2.5, 0.06-0.13 % at 2.5-3, 0.02-0.08 % at 3-4, <= 0.013 % beyond 4, for prolate
                1:3, prolate 1:5 and oblate 2:1 alike), while a fixed distance in SHORT semi-axes means very different
                contact factors: two 1:5 prolates end to end touch at 10 and were handed to the far field at 12.
"""
from __future__ import annotations

import math

import numpy as np
import torch
import torch.nn as nn

from farfield import window
from geometry import axes_of, is_spheroid, symmetry_axis

SIX_PI = 6.0 * math.pi
CUTS = {"distance": None, "contact": 4.0}        # default range per kind of cut (None: the form's r_cut)
TAPER = {"distance": 1.0, "contact": 0.5}        # width of the blend into the far field, in the cut's own unit
KEYS = ("n", "k", "code", "z", "D")              # what the networks may read of a particle (stored with training rows)


# ----------------------------------------------------------------------------------------------- particles
def describe(shapes, R: torch.Tensor) -> dict:
    """Per-particle descriptors from shape names and frames R (P, 3, 3), on R's device:
    A = R diag(a^2) R^T, D = 3 A / tr A - I, z = log of the shortest semi-axis (size), code = (log a_mid/a_min,
    log a_max/a_min); and, when every particle is a spheroid, n = symmetry axis, k = log kappa (polar / equatorial)."""
    shapes = list(shapes)
    ax = np.stack([axes_of(s) for s in shapes])
    to = lambda x: torch.as_tensor(np.asarray(x), dtype=R.dtype, device=R.device)
    a2 = to(ax ** 2)
    A = (R * a2[:, None, :]) @ R.transpose(1, 2)
    srt = np.sort(ax, axis=1)
    out = {"A": A, "D": 3.0 * A / a2.sum(-1)[:, None, None] - torch.eye(3, dtype=R.dtype, device=R.device),
           "amax": to(srt[:, 2]), "z": to(np.log(srt[:, 0])), "code": to(np.stack([np.log(srt[:, 1] / srt[:, 0]), np.log(srt[:, 2] / srt[:, 0])], 1))}
    kinds = {s: is_spheroid(s) for s in set(shapes)}
    if all(kinds.values()):
        sym = {s: symmetry_axis(s) for s in kinds}
        idx = np.array([sym[s] for s in shapes])
        rows = np.arange(len(shapes))
        out["n"] = R[torch.arange(len(shapes), device=R.device), :, torch.as_tensor(idx, device=R.device)]
        out["k"] = to(np.log(ax[rows, idx] / ax[rows, (idx + 1) % 3]))
    return out


def take(desc: dict, idx) -> dict:
    return {k: v[idx] for k, v in desc.items()}


def length(desc: dict) -> torch.Tensor:
    """A particle's length scale l_p: its shortest semi-axis."""
    return torch.exp(desc["z"])


def pair_length(pt: dict, ps: dict) -> torch.Tensor:
    """The pair's length scale l = sqrt(l_t l_s): the unit in which the models measure r, g and the cutoffs."""
    return torch.exp(0.5 * (pt["z"] + ps["z"]))


def rescale(desc: dict, lam: float) -> dict:
    """The descriptors of the same particles enlarged by lam (D and the shape inputs are size-free)."""
    out = dict(desc, z=desc["z"] + math.log(lam))
    if "A" in desc:
        out["A"] = desc["A"] * lam ** 2
    if "amax" in desc:
        out["amax"] = desc["amax"] * lam
    return out


def rotate(desc: dict, Q: torch.Tensor) -> dict:
    """The descriptors of the same particles after the orthogonal map x -> Q x."""
    out = dict(desc)
    if "n" in desc:
        out["n"] = (Q @ desc["n"][..., None])[..., 0]
    for k in ("A", "D"):
        if k in desc:
            out[k] = Q @ desc[k] @ Q.transpose(-1, -2)
    return out


# ----------------------------------------------------------------------------------------------- helpers
def _outer(u, v):
    return u[..., :, None] * v[..., None, :]


def _skew(u):
    z = torch.zeros_like(u[..., 0])
    return torch.stack([torch.stack([z, -u[..., 2], u[..., 1]], -1), torch.stack([u[..., 2], z, -u[..., 0]], -1),
                        torch.stack([-u[..., 1], u[..., 0], z], -1)], -2)


def _qf(M, z):
    return torch.einsum("bi,bij,bj->b", z, M, z)


def _tr(M):
    return M.diagonal(dim1=-2, dim2=-1).sum(-1)


def _radial(d, g, pt, ps):
    """-> r, g in units of the pair length, and z."""
    ell = pair_length(pt, ps)
    r = d.norm(dim=-1)
    return r / ell, g / ell, d / r[:, None]


def reach(cut: str, d, g, pt, ps) -> torch.Tensor:
    """Where a pair is, in the unit of the cut: centre distance in pair lengths, or contact factor c = r / (r - g)."""
    r = d.norm(dim=-1)
    return r / pair_length(pt, ps) if cut == "distance" else r / (r - g)


# ----------------------------------------------------------------------------------------------- the two forms
class Spheroid:
    name, r_cut, n_in, n_true, n_pseudo = "spheroid", 12.0, 12, 12, 27
    test_kinds = ("prolateSpheroid", "oblateSpheroid")

    @staticmethod
    def inputs(d, g, pt, ps) -> torch.Tensor:
        r, g, z = _radial(d, g, pt, ps)
        a, b = pt["n"], ps["n"]
        az, bz, ab = (a * z).sum(-1), (b * z).sum(-1), (a * b).sum(-1)
        return torch.stack([1 / r, az ** 2, bz ** 2, ab ** 2, az * bz * ab, 1 / r ** 2, 1 / r ** 3, g, 1 / (g + 0.5),
                            pt["k"], ps["k"], pt["z"] - ps["z"]], -1)

    @staticmethod
    def tensors(z, pt, ps):
        a, b = pt["n"], ps["n"]
        eye = torch.eye(3, dtype=z.dtype, device=z.device).expand(z.shape[0], 3, 3)
        az, bz, ab = (a * z).sum(-1, keepdim=True), (b * z).sum(-1, keepdim=True), (a * b).sum(-1, keepdim=True)
        ua, ub = az * a, bz * b
        Na, Nb = _outer(a, a), _outer(b, b)
        true = torch.stack([eye, _outer(z, z), Na, Nb, Na @ Nb, Nb @ Na, _outer(z, ua), _outer(ua, z),
                            _outer(z, ub), _outer(ub, z), _outer(ua, ub), _outer(ub, ua)], 1)
        wa, wb, wab = torch.cross(z, ua, dim=-1), torch.cross(z, ub, dim=-1), ab * torch.cross(a, b, dim=-1)
        Ez = _skew(z)
        pseudo = [Ez, _skew(ua), _skew(ub)]
        for v in (z, ua, ub):
            for w in (wa, wb, wab):
                pseudo += [_outer(v, w), _outer(w, v)]
        pseudo += [Na @ Ez, Ez @ Na, Nb @ Ez, Ez @ Nb, Na @ Ez @ Nb, Nb @ Ez @ Na]
        return true, torch.stack(pseudo, 1)


class Triaxial:
    name, r_cut, n_in, n_true, n_pseudo = "triaxial", 14.0, 22, 34, 61
    test_kinds = ("triaxial_123", "prolateSpheroid", "oblateSpheroid")

    @staticmethod
    def inputs(d, g, pt, ps) -> torch.Tensor:
        r, g, z = _radial(d, g, pt, ps)
        Pa, Pb = [pt["D"], pt["D"] @ pt["D"]], [ps["D"], ps["D"] @ ps["D"]]
        cols = ([1 / r] + [_qf(X, z) for X in Pa] + [_qf(Y, z) for Y in Pb] + [_tr(X @ Y) for X in Pa for Y in Pb]
                + [_qf(X @ Y, z) for X in Pa for Y in Pb])
        return torch.cat([torch.stack(cols, 1), pt["code"], ps["code"], (pt["z"] - ps["z"])[:, None],
                          torch.stack([1 / r ** 2, 1 / r ** 3, g, 1 / (g + 0.5)], 1)], 1)

    @staticmethod
    def tensors(z, pt, ps):
        N = [pt["D"], pt["D"] @ pt["D"], ps["D"], ps["D"] @ ps["D"]]
        eye = torch.eye(3, dtype=z.dtype, device=z.device).expand(z.shape[0], 3, 3)
        u = [(n @ z[:, :, None])[:, :, 0] for n in N]
        w = [torch.cross(z, x, dim=-1) for x in u]
        Ez, zz = _skew(z), _outer(z, z)
        cross_pairs = [(i, j) for i in (0, 1) for j in (2, 3)]
        true = [eye, zz] + N
        for i, j in cross_pairs:
            true += [N[i] @ N[j], N[j] @ N[i]]
        for x in u:
            true += [_outer(z, x), _outer(x, z)]
        for i, j in cross_pairs + [(0, 1), (2, 3)]:
            true += [_outer(u[i], u[j]), _outer(u[j], u[i])]
        pseudo = [Ez] + [_skew(x) for x in u]
        for n in N:
            pseudo += [n @ Ez, Ez @ n]
        for i, j in cross_pairs + [(0, 1), (2, 3)]:
            pseudo += [N[i] @ Ez @ N[j], N[j] @ Ez @ N[i]]
        for x in w:
            pseudo += [_outer(z, x), _outer(x, z)]
        for i, j in cross_pairs:                  # needed when z lies along an axis and the other particle is twisted about it
            pseudo.append(_tr(Ez @ N[j] @ N[i])[:, None, None] * zz)
        for p in range(4):
            for q in range(4):
                if p != q:
                    pseudo += [_outer(u[p], w[q]), _outer(w[q], u[p])]
        return torch.stack(true, 1), torch.stack(pseudo, 1)


FORMS = {"spheroid": Spheroid, "triaxial": Triaxial}


def assemble(c, true, pseudo, scale=(1.0, 1.0, 1.0)) -> torch.Tensor:
    """Coefficients (B, 2 nt + 2 np) -> blocks [[TT, TR], [RT, RR]]: TT, RR on true tensors, TR, RT on pseudotensors."""
    nt, npz = true.shape[1], pseudo.shape[1]
    s_tt, s_c, s_rr = scale
    tt = torch.einsum("bn,bnij->bij", c[:, :nt], true) * s_tt
    rr = torch.einsum("bn,bnij->bij", c[:, nt:2 * nt], true) * s_rr
    tr = torch.einsum("bn,bnij->bij", c[:, 2 * nt:2 * nt + npz], pseudo) * s_c
    rt = torch.einsum("bn,bnij->bij", c[:, 2 * nt + npz:], pseudo) * s_c
    return torch.cat([torch.cat([tt, tr], -1), torch.cat([rt, rr], -1)], -2)


# ----------------------------------------------------------------------------------------------- the model
class PairModel(nn.Module):
    """forward(d, g, pt, ps) -> learned cross block and self correction (B, 6, 6), units of 1/(6 pi), windowed.
    A 3-hidden-layer SiLU MLP of the given width: inputs -> 2 x (2 n_true + 2 n_pseudo) coefficients."""

    def __init__(self, form: str, r_cut: float | None = None, width: int = 128, taper: float | None = None,
                 cut: str = "distance"):
        super().__init__()
        self.form, self.cut = FORMS[form], cut
        self.r_cut = float(r_cut or CUTS[cut] or self.form.r_cut)          # in pair lengths, or a contact factor
        self.width, self.taper = int(width), float(taper or TAPER[cut])
        self.n_coeff = 2 * self.form.n_true + 2 * self.form.n_pseudo
        self.mlp = nn.Sequential(nn.Linear(self.form.n_in, width), nn.SiLU(), nn.Linear(width, width), nn.SiLU(),
                                 nn.Linear(width, width), nn.SiLU(), nn.Linear(width, 2 * self.n_coeff))
        self.register_buffer("mu", torch.zeros(self.form.n_in))
        self.register_buffer("sd", torch.ones(self.form.n_in))

    def features(self, d, g, pt, ps):
        return self.form.inputs(d, g, pt, ps)

    def _raw(self, d, g, pt, ps):
        r = d.norm(dim=-1)
        c = self.mlp((self.features(d, g, pt, ps) - self.mu) / self.sd)
        true, pseudo = self.form.tensors(d / r[:, None], pt, ps)
        ell = pair_length(pt, ps)[:, None, None]
        rr = r[:, None, None] / ell                               # decay in pair units, then back to physical units
        nc = self.n_coeff
        cross = assemble(c[:, :nc], true, pseudo, (1 / (rr * ell), 1 / (rr * ell) ** 2, 1 / (rr * ell) ** 3))
        self_ = assemble(c[:, nc:], true, pseudo, (1 / (rr ** 4 * ell), 1 / (rr ** 4 * ell ** 2), 1 / (rr ** 4 * ell ** 3)))
        return cross, self_

    def forward(self, d, g, pt, ps):
        cross, self_ = self._raw(d, g, pt, ps)
        swapped, _ = self._raw(-d, g, ps, pt)                     # the same pair seen from the source
        w = self.weight(d, g, pt, ps)[:, None, None]
        return w * 0.5 * (cross + swapped.transpose(-1, -2)), w * 0.5 * (self_ + self_.transpose(-1, -2))

    def weight(self, d, g, pt, ps) -> torch.Tensor:
        """1 where the block is learned, 0 where it is the far field, a smooth ramp over the last `taper`."""
        return window(reach(self.cut, d, g, pt, ps), self.r_cut, self.taper)

    def config(self) -> dict:
        return {"form": self.form.name, "r_cut": self.r_cut, "width": self.width, "taper": self.taper, "inputs": "full",
                "cut": self.cut}


def save_pair(model: PairModel, path: str, extra: dict | None = None) -> None:
    torch.save({"state": model.state_dict(), **model.config(), **(extra or {})}, path)


def load_pair(path: str) -> PairModel:
    """Also reads the models trained by the earlier per-form folders (same layers, same checkpoint fields)."""
    ck = torch.load(path, map_location="cpu", weights_only=False)
    assert ck.get("inputs", "full") == "full", f"{path}: only the selected 'full' input set is kept here"
    m = PairModel(ck["form"], ck["r_cut"], ck["width"], ck["taper"], ck.get("cut", "distance"))
    m.load_state_dict(ck["state"])
    m.report = ck.get("report", {})
    return m.eval()
