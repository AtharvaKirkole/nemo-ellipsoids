"""Many-body correction f_nb: what the pairwise operator misses for a near pair because other particles are around.

For each near ordered pair (t, s) of a suspension the label is the residual of the two-body operator,

    R_ts = M_ts(MFS of the whole configuration) - [(1 - w) far + w two-body](t, s)

and the model predicts it from the pair and a summary of its neighbourhood.  The summary is NeMO's: moments of the
neighbours k (not t, s) in radial bands about the pair MIDPOINT, so it is the same for both orderings of the pair,
with every neighbour in every band (no top-K selection).  Particles enter only through their shape tensor
D = 3 A / tr(A) - I (traceless; 0 for a sphere; beta(kappa) (n n^T - 1/3) for a spheroid; unchanged by a turn about an
axis of revolution; size-free), so nothing depends on how a frame was chosen:

    s_a = sum w_a          v_a = sum w_a u_k          Q_a = sum w_a (u_k u_k^T - I/3)        (where the neighbours are)
    S_a = sum w_a D_k      T_a = sum w_a D_k^2                                              (what they are, how turned)

Band weights w_a(r): overlapping tents, a partition of unity out to the last band centre, then a linear fade to ZERO
at the neighbour cutoff.  Nothing jumps when a neighbour crosses a band edge or enters / leaves the neighbourhood.
(Before, the last tent was cut at half height at the cutoff, a small discontinuity of f_nb in the positions.)

Inputs: the pair form's inputs (12 / 22) + 20 invariants per band (band_inputs); 8 bands = 172 / 182 inputs.
Tensors: the pair form's tensors (12 + 27 / 34 + 61) + per band (8 bands: 40 + 40 more), from the neighbour POSITIONS only,
    true    Q, v v^T, z v^T, v z^T, S(z z^T Q)                                           S(X) = X + X^T
    pseudo  E(v), E(Q z), S(z (z x v)^T), (z.v) E(z), [E(z), Q]
The neighbours' shapes and orientations inform the coefficients (through S_a, T_a in the inputs) but add no tensors:
band tensors built from S changed the triaxial error by 1 % (2.77 / 10.75 -> 2.80 / 10.86),
while dropping every band tensor cost 48 % and dropping the shape inputs 7 %.

Exact for any weights: rotation / reflection equivariance; reciprocity (swap average, as the pair model); zero
correction for a pair with no neighbours (gate s_tot / (1 + s_tot)) and beyond the pair cutoff (window); continuity;
scale covariance: every length (pair separation, neighbour positions, both cutoffs) is measured in the pair's length
l = sqrt(l_t l_s) and the block is scaled back (TT 1/l, TR / RT 1/l^2, RR 1/l^3), so a whole neighbourhood enlarged
by lam is exact.  Neighbours whose SIZE differs from the pair's enter through two more moments per band of
lam_k = log(l_k / l), m1_a = sum w_a lam_k and m2_a = sum w_a lam_k^2 (both 0 when every particle has the pair's size,
so one-size models are unchanged; they are ratios, so scale covariance stays exact).
Output in units of 1/(6 pi).  There is no learned diagonal (per-particle self correction): measured, it adds nothing in
suspensions (Fig. 3, phi 0.2: prolate 12.19 -> 12.82 %, 1:2:3 12.02 -> 11.96 %) and hurts an isolated pair.
"""
from __future__ import annotations

import torch
import torch.nn as nn

import pair as P
from farfield import window
from pair import _outer, _skew, assemble

BAND_IN, BAND_TRUE, BAND_PSEUDO = 20, 5, 5
_IU = ([0, 1, 2, 0, 0, 1], [0, 1, 2, 1, 2, 2])


def to6(M: torch.Tensor) -> torch.Tensor:
    """Symmetric (..., 3, 3) -> (..., 6): xx, yy, zz, xy, xz, yz."""
    return M[..., _IU[0], _IU[1]]


def from6(x: torch.Tensor) -> torch.Tensor:
    xx, yy, zz, xy, xz, yz = x.unbind(-1)
    return torch.stack([torch.stack([xx, xy, xz], -1), torch.stack([xy, yy, yz], -1), torch.stack([xz, yz, zz], -1)], -2)


def as_mat(D: torch.Tensor) -> torch.Tensor:
    return from6(D) if D.shape[-1] == 6 else D


# ----------------------------------------------------------------------------------------------- neighbourhood
def band_weights(v: torch.Tensor, mask: torch.Tensor, n_bands: int, r_max: float):
    """v (B, K, 3) neighbours from the midpoint -> unit directions u (B, K, 3), weights W (B, K, NB).
    Tent centres (a + 1/2) h, h = r_max / (NB + 1/2): sum_a W = 1 for r <= the last centre, W -> 0 at r_max."""
    r = v.norm(dim=-1, keepdim=True).clamp_min(1e-9)
    u = v / r
    h = r_max / (n_bands + 0.5)
    c = (torch.arange(n_bands, dtype=v.dtype, device=v.device) + 0.5) * h
    W = (1 - (r - c).abs() / h).clamp_min(0)
    W = torch.where(r <= c[0], (c == c[0]).to(v.dtype), W)          # innermost tent is flat towards the midpoint
    return u, W * mask[..., None]


def band_moments(v, Dn, mask, n_bands: int, r_max: float, lam=None):
    """-> s (B, NB), vm (B, NB, 3), Q, S, T (B, NB, 3, 3), m1, m2 (B, NB).  lam (B, K): log size of each neighbour
    relative to the pair (None: all equal)."""
    u, W = band_weights(v, mask, n_bands, r_max)
    eye = torch.eye(3, dtype=v.dtype, device=v.device)
    s = W.sum(1)
    vm = torch.einsum("bka,bki->bai", W, u)
    Q = torch.einsum("bka,bki,bkj->baij", W, u, u) - s[..., None, None] * eye / 3
    S = torch.einsum("bka,bkij->baij", W, Dn)
    T = torch.einsum("bka,bkij->baij", W, Dn @ Dn)
    lam = torch.zeros_like(mask) if lam is None else lam
    return s, vm, Q, S, T, torch.einsum("bka,bk->ba", W, lam), torch.einsum("bka,bk->ba", W, lam * lam)


def band_inputs(z, Dt, Ds, s, vm, Q, S, T, m1, m2) -> torch.Tensor:
    """20 scalars per band, invariant under rotations and reflections, for the ORDERED pair, (B, 18 NB):
    s, |v|^2, (z.v)^2, z.Q.z, tr Q^2, z.S.z, tr S^2, z.T.z, tr T, tr(D_t Q), tr(D_s Q), tr(D_t S), tr(D_s S),
    v.Q.v, v.S.v, z.Q.v, z.S.v, tr(Q S), m1, m2 (neighbour sizes).  The first two alone ("how many neighbours, and on which side") already take
    the pair error from 10.2 to 3.4 %; the rest takes it to 3.0 (spheroids) -- all are kept, they cost nothing."""
    q = lambda X: torch.einsum("bi,baij,bj->ba", z, X, z)
    vv = lambda X: torch.einsum("bai,baij,baj->ba", vm, X, vm)
    zv = lambda X: torch.einsum("bi,baij,baj->ba", z, X, vm)
    tr2 = lambda X, Y: torch.einsum("baij,baji->ba", X, Y)
    trD = lambda D, X: torch.einsum("bij,baji->ba", D, X)
    zdv = torch.einsum("bai,bi->ba", vm, z)
    return torch.cat([s, (vm * vm).sum(-1), zdv * zdv, q(Q), tr2(Q, Q), q(S), tr2(S, S), q(T),
                      T.diagonal(dim1=-2, dim2=-1).sum(-1), trD(Dt, Q), trD(Ds, Q), trD(Dt, S), trD(Ds, S),
                      vv(Q), vv(S), zv(Q), zv(S), tr2(Q, S), m1, m2], -1)


def band_tensors(z, vm, Q):
    """-> true (B, 5 NB, 3, 3), pseudo (B, 5 NB, 3, 3)."""
    B, NB = vm.shape[:2]
    zb = z[:, None].expand_as(vm)
    zz = _outer(z, z)[:, None]
    Sym = lambda X: X + X.transpose(-1, -2)
    Ez = _skew(z)[:, None]
    Qz = torch.einsum("baij,bj->bai", Q, z)
    zv = (vm * zb).sum(-1)[..., None, None]
    true = torch.stack([Q, _outer(vm, vm), _outer(zb, vm), _outer(vm, zb), Sym(zz @ Q)], 2)
    pseudo = torch.stack([_skew(vm), _skew(Qz), Sym(_outer(zb, torch.cross(zb, vm, dim=-1))), zv * Ez.expand_as(Q),
                          Ez @ Q - Q @ Ez], 2)
    return true.reshape(B, BAND_TRUE * NB, 3, 3), pseudo.reshape(B, BAND_PSEUDO * NB, 3, 3)


def neighbours(X: torch.Tensor, D: torch.Tensor, centre: torch.Tensor, exclude: torch.Tensor, cutoff, z=None):
    """Every particle within `cutoff` (a number, or one per centre (C,)) of each centre (C, 3), minus the excluded
    indices (C, e): positions relative to the centre (C, K, 3), shape tensors (C, K, 3, 3), a mask (C, K) and the
    neighbours' log sizes (C, K) (z = log size per particle; zeros if not given), padded to the largest count.  The ONE selection used to build training rows and by the operator."""
    rel = X[None, :, :] - centre[:, None, :]
    ok = rel.norm(dim=-1) < (cutoff[:, None] if torch.is_tensor(cutoff) else cutoff)
    ar = torch.arange(len(centre), device=X.device)
    for j in range(exclude.shape[1]):
        ok[ar, exclude[:, j]] = False
    K = max(1, int(ok.sum(1).max()))
    order = torch.argsort((~ok).to(torch.int8), dim=1, stable=True)[:, :K]      # real neighbours first, index order
    mask = torch.gather(ok, 1, order)
    nbr = torch.gather(rel, 1, order[..., None].expand(-1, -1, 3)) * mask[..., None]
    nz = z[order] * mask if z is not None else torch.zeros_like(mask, dtype=X.dtype)
    return nbr, D[order] * mask[..., None, None], mask.to(X.dtype), nz


# ----------------------------------------------------------------------------------------------- the model
class NbodyModel(nn.Module):
    """forward(d, g, pt, ps, nbr, nbr_D, mask) -> correction to the cross block (B, 6, 6), units of 1/(6 pi).
    form: the pair form whose inputs and tensors it extends ("spheroid" / "triaxial").
    pair_cutoff: pairs corrected (window to zero there); neighbor_cutoff: neighbours within this distance of the pair
    midpoint are seen, in n_bands bands.  Both in units of the pair length l (pair.py pair_length)."""

    def __init__(self, form: str, pair_cutoff: float | None = None, neighbor_cutoff: float | None = None, n_bands: int = 8,
                 width: int = 128, taper: float = 1.0):
        super().__init__()
        self.form = P.FORMS[form]
        self.pair_cutoff = float(pair_cutoff or self.form.r_cut)
        self.neighbor_cutoff = float(neighbor_cutoff or self.form.r_cut)
        self.n_bands, self.width, self.taper = int(n_bands), int(width), float(taper)
        self.n_true = self.form.n_true + BAND_TRUE * self.n_bands
        self.n_pseudo = self.form.n_pseudo + BAND_PSEUDO * self.n_bands
        self.n_in = self.form.n_in + BAND_IN * self.n_bands
        self.n_out = 2 * self.n_true + 2 * self.n_pseudo
        hidden = (width, max(width // 2, 1), width, max(width // 2, 1))        # NeMO's many-body network shape
        layers, last = [], self.n_in
        for h in hidden:
            layers += [nn.Linear(last, h), nn.SiLU()]
            last = h
        layers.append(nn.Linear(last, self.n_out))
        nn.init.zeros_(layers[-1].weight)                # start at "no correction" = the pairwise operator
        nn.init.zeros_(layers[-1].bias)
        self.mlp = nn.Sequential(*layers)
        self.register_buffer("mu", torch.zeros(self.n_in))
        self.register_buffer("sd", torch.ones(self.n_in))

    def moments(self, nbr, nbr_D, mask, ell, nbr_z=None):
        mask = mask.to(nbr.dtype)
        lam = None if nbr_z is None else (nbr_z - torch.log(ell)[:, None]) * mask
        return band_moments(nbr / ell[:, None, None], as_mat(nbr_D), mask, self.n_bands, self.neighbor_cutoff, lam)

    def features(self, d, g, pt, ps, s, vm, Q, S, T, m1, m2):
        z = d / d.norm(dim=-1, keepdim=True)
        return torch.cat([self.form.inputs(d, g, pt, ps), band_inputs(z, pt["D"], ps["D"], s, vm, Q, S, T, m1, m2)], -1)

    def _raw(self, d, g, pt, ps, s, vm, Q, S, T, m1, m2):
        z = d / d.norm(dim=-1, keepdim=True)
        c = self.mlp((self.features(d, g, pt, ps, s, vm, Q, S, T, m1, m2) - self.mu) / self.sd)
        t0, p0 = self.form.tensors(z, pt, ps)
        t1, p1 = band_tensors(z, vm, Q)
        ell = P.pair_length(pt, ps)[:, None, None]                 # the block of the unit-length problem, scaled back
        return assemble(c, torch.cat([t0, t1], 1), torch.cat([p0, p1], 1), (1 / ell, 1 / ell ** 2, 1 / ell ** 3))

    def gate(self, d, s, ell):
        stot = s.sum(-1)
        return (stot / (1.0 + stot)) * window(d.norm(dim=-1) / ell, self.pair_cutoff, self.taper)

    def forward(self, d, g, pt, ps, nbr, nbr_D, mask, nbr_z=None):
        ell = P.pair_length(pt, ps)
        mom = self.moments(nbr, nbr_D, mask, ell, nbr_z)
        K = 0.5 * (self._raw(d, g, pt, ps, *mom) + self._raw(-d, g, ps, pt, *mom).transpose(-1, -2))
        return self.gate(d, mom[0], ell)[:, None, None] * K

    def config(self) -> dict:
        return {"form": self.form.name, "pair_cutoff": self.pair_cutoff, "neighbor_cutoff": self.neighbor_cutoff,
                "n_bands": self.n_bands, "width": self.width, "taper": self.taper}


@torch.no_grad()
def fit_normalisation(model: NbodyModel, d, g, pt, ps, nbr, nbr_D, mask, nbr_z=None) -> None:
    """mu / sd of the inputs on training rows.  Outer bands that are rarely filled get a floored spread, or an unseen
    neighbourhood becomes a huge normalised input."""
    x = model.features(d, g, pt, ps, *model.moments(nbr, nbr_D, mask, P.pair_length(pt, ps), nbr_z))
    model.mu.copy_(x.mean(0))
    model.sd.copy_(torch.maximum(x.std(0), 0.1 * x.abs().mean(0)).clamp_min(1e-3))


def save_nbody(model: NbodyModel, path: str, extra: dict | None = None) -> None:
    torch.save({"state": model.state_dict(), **model.config(), **(extra or {})}, path)


def load_nbody(path: str) -> NbodyModel:
    ck = torch.load(path, map_location="cpu", weights_only=False)
    m = NbodyModel(ck["form"], ck["pair_cutoff"], ck["neighbor_cutoff"], ck["n_bands"], ck["width"], ck["taper"])
    m.load_state_dict(ck["state"])
    m.pair_model = ck.get("pair_model")              # the pair model its labels were made with
    m.report = ck.get("report", {})
    return m.eval()


# ----------------------------------------------------------------------------------------------- many-body SELF correction
# What the pairwise operator misses on the DIAGONAL: M_tt(MFS of the whole configuration) - [M_iso + sum_s self(t, s)].
# Adding the two-body self corrections of every neighbour as if each were alone over-counts; the remainder is small in
# velocity error (1.2 -> 0.3 % with exact blocks, 20 particles) but it is what decides positive definiteness once the
# cross blocks are right: with EXACT many-body cross blocks and pairwise-summed self blocks the smallest eigenvalue of a
# mixed prolate / oblate suspension was -0.19 x MFS's, with exact self blocks too it was 1.00 (measured 2026-11-13).
#
# One network for both forms: a particle enters through its shape tensor D (and its shape code), its neighbourhood
# through the same band moments as f_nb, taken about the PARTICLE's centre, lengths in units of its own length l_t.
#   inputs   shape code (2) + 14 invariants per band:
#            s, |v|^2, tr Q^2, tr S^2, tr T, tr(D Q), tr(D S), tr(D^2 Q), v.D.v, v.Q.v, v.S.v, tr(Q S), m1, m2
#   tensors  TT and RR (symmetric, true):  I, D, D^2;  per band  Q, v v^T, D Q + Q D, S, D v v^T + v v^T D
#            TR (pseudo; RT = TR^T):       per band  E(v), E(D v), E(Q v), D E(v) + E(v) D, D E(v) - E(v) D
# Exact for any weights: equivariance; a symmetric block; scale covariance; and ZERO for a particle with no neighbour
# or with exactly one (the pair model's self correction is already exact there): the gate is
#   s / (1 + s) x (1 - sum_k w_k^2 / (sum_k w_k)^2),   w_k = the total band weight of neighbour k,
# which vanishes continuously as a second neighbour leaves.
SELF_IN, SELF_TRUE, SELF_PSEUDO = 14, 5, 5


class SelfModel(nn.Module):
    """forward(pt, nbr, nbr_D, mask[, nbr_z]) -> correction to the self block (B, 6, 6), units of 1/(6 pi).
    neighbor_cutoff in units of the particle's length l_t."""

    def __init__(self, neighbor_cutoff: float = 12.0, n_bands: int = 8, width: int = 128):
        super().__init__()
        self.neighbor_cutoff, self.n_bands, self.width = float(neighbor_cutoff), int(n_bands), int(width)
        self.n_true, self.n_pseudo = 3 + SELF_TRUE * self.n_bands, SELF_PSEUDO * self.n_bands
        self.n_in, self.n_out = 2 + SELF_IN * self.n_bands, 2 * self.n_true + self.n_pseudo
        layers, last = [], self.n_in
        for h in (width, max(width // 2, 1), width, max(width // 2, 1)):
            layers += [nn.Linear(last, h), nn.SiLU()]
            last = h
        layers.append(nn.Linear(last, self.n_out))
        nn.init.zeros_(layers[-1].weight)
        nn.init.zeros_(layers[-1].bias)
        self.mlp = nn.Sequential(*layers)
        self.register_buffer("mu", torch.zeros(self.n_in))
        self.register_buffer("sd", torch.ones(self.n_in))

    def moments(self, pt, nbr, nbr_D, mask, nbr_z=None):
        ell = P.length(pt)
        mask = mask.to(nbr.dtype)
        lam = None if nbr_z is None else (nbr_z - pt["z"][:, None]) * mask
        v = nbr / ell[:, None, None]
        mom = band_moments(v, as_mat(nbr_D), mask, self.n_bands, self.neighbor_cutoff, lam)
        wk = band_weights(v, mask, self.n_bands, self.neighbor_cutoff)[1].sum(-1)            # (B, K)
        tot = wk.sum(1)
        gate = tot / (1.0 + tot) * (1.0 - (wk ** 2).sum(1) / (tot ** 2).clamp_min(1e-12))
        return mom, torch.where(tot > 1e-9, gate, torch.zeros_like(gate))

    def features(self, pt, s, vm, Q, S, T, m1, m2):
        D = pt["D"]
        D2 = D @ D
        tr2 = lambda X, Y: torch.einsum("baij,baji->ba", X, Y)
        trD = lambda A, X: torch.einsum("bij,baji->ba", A, X)
        quad = lambda X: torch.einsum("bai,baij,baj->ba", vm, X, vm)
        return torch.cat([pt["code"], s, (vm * vm).sum(-1), tr2(Q, Q), tr2(S, S), T.diagonal(dim1=-2, dim2=-1).sum(-1),
                          trD(D, Q), trD(D, S), trD(D2, Q), torch.einsum("bai,bij,baj->ba", vm, D, vm), quad(Q), quad(S),
                          tr2(Q, S), m1, m2], -1)

    def tensors(self, pt, vm, Q, S):
        B, NB = vm.shape[:2]
        D = pt["D"]
        Db = D[:, None].expand(B, NB, 3, 3)
        eye = torch.eye(3, dtype=D.dtype, device=D.device).expand(B, 3, 3)
        vv = _outer(vm, vm)
        true = torch.stack([Q, vv, Db @ Q + Q @ Db, S, Db @ vv + vv @ Db], 2).reshape(B, SELF_TRUE * NB, 3, 3)
        Ev = _skew(vm)
        pseudo = torch.stack([Ev, _skew(torch.einsum("bij,baj->bai", D, vm)), _skew(torch.einsum("baij,baj->bai", Q, vm)),
                              Db @ Ev + Ev @ Db, Db @ Ev - Ev @ Db], 2).reshape(B, SELF_PSEUDO * NB, 3, 3)
        return torch.cat([torch.stack([eye, D, D @ D], 1), true], 1), pseudo

    def forward(self, pt, nbr, nbr_D, mask, nbr_z=None):
        (s, vm, Q, S, T, m1, m2), gate = self.moments(pt, nbr, nbr_D, mask, nbr_z)
        c = self.mlp((self.features(pt, s, vm, Q, S, T, m1, m2) - self.mu) / self.sd)
        true, pseudo = self.tensors(pt, vm, Q, S)
        nt = self.n_true
        ell = P.length(pt)[:, None, None]
        tt = torch.einsum("bn,bnij->bij", c[:, :nt], true) / ell
        rr = torch.einsum("bn,bnij->bij", c[:, nt:2 * nt], true) / ell ** 3
        tr = torch.einsum("bn,bnij->bij", c[:, 2 * nt:], pseudo) / ell ** 2
        K = torch.cat([torch.cat([tt, tr], -1), torch.cat([tr.transpose(-1, -2), rr], -1)], -2)
        return gate[:, None, None] * K

    def config(self) -> dict:
        return {"neighbor_cutoff": self.neighbor_cutoff, "n_bands": self.n_bands, "width": self.width}


@torch.no_grad()
def fit_self_normalisation(model: SelfModel, pt, nbr, nbr_D, mask, nbr_z=None) -> None:
    x = model.features(pt, *model.moments(pt, nbr, nbr_D, mask, nbr_z)[0])
    model.mu.copy_(x.mean(0))
    model.sd.copy_(torch.maximum(x.std(0), 0.1 * x.abs().mean(0)).clamp_min(1e-3))


def save_self(model: SelfModel, path: str, extra: dict | None = None) -> None:
    torch.save({"state": model.state_dict(), **model.config(), **(extra or {})}, path)


def load_self(path: str) -> SelfModel:
    ck = torch.load(path, map_location="cpu", weights_only=False)
    m = SelfModel(ck["neighbor_cutoff"], ck["n_bands"], ck["width"])
    m.load_state_dict(ck["state"])
    m.pair_model = ck.get("pair_model")
    m.report = ck.get("report", {})
    return m.eval()
