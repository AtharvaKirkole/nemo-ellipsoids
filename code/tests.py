#!/usr/bin/env python3
"""Tests of everything that is claimed to hold BY CONSTRUCTION, on random (untrained) weights, for BOTH forms.
Runs on a CPU in about a minute, from the workspace (needs the coarse clouds in data/points):

    python tests.py            (or: pytest tests.py)

  geometry     batched contact factor = the SciPy reference
  truth        the grand mobility matrix is symmetric and positive definite; the exact isolated-ellipsoid mobility
               reduces to Stokes' sphere, and the clouds approach it as they are refined
  stress       the solver with stresslets and straining flows: the sphere's stresslet and Einstein's 5/2, Jeffery's
               rotation law, reciprocity between the strain and stresslet blocks, positive dissipation
  far field    reciprocal
  pair model   rotation AND reflection equivariance; invariance to the sign of every axis (spheroid form); reciprocity
               M_st = M_ts^T under exchange of the particles (shapes and sizes included); symmetric self block; zero at
               r_cut; exact scaling with size (TT 1/lam, TR 1/lam^2, RR 1/lam^3); no tensor identically zero, no two
               tensors proportional; a spheroid's turn about its own axis changes nothing
               the same for the contact-factor cut: zero from contact factor 4 on, at any distance
  many-body    the same symmetries and scaling; zero without neighbours; continuous when a neighbour crosses a band
               edge or the neighbour cutoff, and when the pair crosses the pair cutoff
  self model   the same symmetries and scaling; a symmetric block; zero for a particle with no neighbour or exactly one;
               continuous when a second neighbour leaves
  operator     symmetric grand mobility in every mode; equivariant under a rotation of the whole configuration;
               independent of particle order; a suspension of particles enlarged by lam scales exactly
  stress model the strain / stresslet blocks: the same symmetries, reciprocity with the force blocks, scaling
  periodic box Hasimoto's constant, independence of the Ewald splitting, a huge box = free space, no origin
  fast         the matrix-free operator (fast.py) gives the dense operator's velocities in every mode
  positive     psd.py's projection: every eigenvalue above the floor; never further from ANY admissible truth (the
  definiteness   no-loss guarantee); untouched and bit for bit the same when already positive definite; idempotent;
               independent of the square root used; 1-Lipschitz; exactly covariant under enlarging the particles.  The
               operator in every mode on a dense suspension whose raw sum is indefinite: positive definite, symmetric,
               rotation equivariant, independent of particle order; the far field untouched.  The stress grand matrix:
               both diagonal parts positive semi-definite, the coupling kept
"""
from __future__ import annotations

import os

import numpy as np
import torch

import pair as P
from farfield import far_blocks
from geometry import (POINTS_DIR, SHAPES, assign_shapes, clearance_torch, contact_factor, contact_factor_torch, grown_config,
                      is_spheroid, matrix_to_quat, quat_to_matrix, random_quats, symmetry_axis, uniform_config)
from mobility import Operator
from nbody import NbodyModel, SelfModel, band_weights
from truth import cloud_error, dense_mobility, exact_iso_mobility

torch.set_default_dtype(torch.float64)
ACC = "coarse"
FORMS = [f for f in P.FORMS.values() if all(os.path.exists(f"{POINTS_DIR}/b_{k}_{ACC}.txt") for k in f.test_kinds)]


def random_pairs(kinds, B: int, seed: int = 0, r_lo: float = 4.0, r_hi: float = 9.0):
    """B ordered pairs of random shapes from kinds: d, g, pt, ps, shape names, frames."""
    rng = np.random.default_rng(seed)
    st, ss = [kinds[i] for i in rng.integers(len(kinds), size=B)], [kinds[i] for i in rng.integers(len(kinds), size=B)]
    Rt, Rs = (torch.as_tensor(quat_to_matrix(random_quats(rng, B))) for _ in range(2))
    u = rng.normal(size=(B, 3))
    d = torch.as_tensor(u / np.linalg.norm(u, axis=1, keepdims=True) * rng.uniform(r_lo, r_hi, size=(B, 1)))
    pt, ps = P.describe(st, Rt), P.describe(ss, Rs)
    return d, clearance_torch(pt["A"], ps["A"], d), pt, ps, st, ss, Rt, Rs


def random_orthogonal(rng, reflect: bool) -> torch.Tensor:
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if (np.linalg.det(Q) < 0) != reflect:
        Q[:, 0] *= -1
    return torch.as_tensor(Q)


def block_map(Q: torch.Tensor) -> torch.Tensor:
    """How a 6x6 mobility block transforms under x -> Q x: K -> D K D^T, D = diag(Q, det(Q) Q)."""
    return torch.block_diag(Q, torch.det(Q) * Q)


def scale_map(lam: float) -> torch.Tensor:
    """How a 6x6 mobility block scales when every length is multiplied by lam."""
    S = torch.empty(6, 6)
    S[:3, :3], S[:3, 3:], S[3:, :3], S[3:, 3:] = 1 / lam, 1 / lam ** 2, 1 / lam ** 2, 1 / lam ** 3
    return S


def randomise(model):
    torch.manual_seed(0)
    with torch.no_grad():
        for p in model.parameters():
            p.copy_(torch.randn_like(p) * 0.3)
        model.mu.normal_()
        model.sd.uniform_(0.5, 2.0)
    return model.double().eval()


def rel(a, b):
    return float((a - b).norm() / b.norm().clamp_min(1e-300))


def each_form(fn):
    """Run a test once per form; the form is the test's first argument."""
    def wrapped():
        assert FORMS, f"no form has its coarse test clouds in {POINTS_DIR}"
        for form in FORMS:
            fn(form)
    wrapped.__name__ = fn.__name__
    return wrapped


# ----------------------------------------------------------------------------------------------- geometry, truth
@each_form
def test_contact_factor(form):
    d, _, pt, ps, *_ = random_pairs(list(form.test_kinds), 40)
    c = contact_factor_torch(pt["A"], ps["A"], d)
    ref = np.array([contact_factor(pt["A"][i].numpy(), ps["A"][i].numpy(), d[i].numpy()) for i in range(len(d))])
    assert np.abs(c.numpy() - ref).max() < 1e-9


@each_form
def test_truth_symmetric_positive(form):
    rng = np.random.default_rng(1)
    shapes = assign_shapes(form.test_kinds, 4, rng)
    pos, q = grown_config(shapes, 0.2, rng)
    M = dense_mobility(pos, q, shapes, ACC)
    assert np.abs(M - M.T).max() / np.abs(M).max() < 2e-2              # the coarse cloud's own asymmetry
    assert np.linalg.eigvalsh(0.5 * (M + M.T)).min() > 0


def test_exact_isolated_mobility():
    M = exact_iso_mobility("sphere")
    assert abs(M[0, 0] * 6 * np.pi - 1) < 1e-12 and abs(M[3, 3] * 8 * np.pi - 1) < 1e-12      # Stokes
    for shape in ("prolateSpheroid", "triaxial_123"):
        errs = [cloud_error(shape, a) for a in ("coarse", "medium", "fine")]
        errs = [e for e in errs if e]
        if len(errs) > 1:                                              # finer clouds are closer to the exact value
            assert errs[-1]["trans_pct"] < errs[0]["trans_pct"] and errs[-1]["rot_pct"] < errs[0]["rot_pct"], shape
            assert errs[-1]["trans_pct"] < 0.1 and errs[-1]["rot_pct"] < 0.2, shape


def test_stress_and_strain():
    """The solver with stresslets and straining flows, against what is known exactly."""
    from truth import STRAIN_BASIS, dense_grand, intrinsic_viscosity
    q0 = np.array([[0.0, 0.0, 0.0, 1.0]])
    G = dense_grand(np.zeros((1, 3)), q0, ["sphere"], ACC)
    assert np.abs(G[6:, 6:] - 20 * np.pi / 3 * np.eye(5)).max() < 2e-2            # a sphere in a strain
    assert abs(intrinsic_viscosity("sphere", ACC) - 2.5) < 2e-3                     # Einstein
    assert np.abs(G[:6, 6:]).max() < 1e-3 and np.abs(G[6:, :6]).max() < 1e-3       # no coupling for a sphere
    shape = "triaxial_123" if os.path.exists(f"{POINTS_DIR}/b_triaxial_123_medium.txt") else "prolateSpheroid"
    G = dense_grand(np.zeros((1, 3)), q0, [shape], "medium")
    a2 = np.asarray(SHAPES[shape]) ** 2
    for i in range(3):                                                              # Jeffery: rotation in a pure strain
        j, k = (i + 1) % 3, (i + 2) % 3
        assert np.abs(G[3 + i, 6:] - (a2[j] - a2[k]) / (a2[j] + a2[k]) * STRAIN_BASIS[:, j, k]).max() < 5e-3, i
    rng = np.random.default_rng(41)
    sh = ["prolateSpheroid", "oblateSpheroid"]
    pos, q = grown_config(sh, 0.4, rng)
    G = dense_grand(pos, q, sh, "medium").reshape(2, 11, 2, 11)
    assert np.abs(G[:, :6, :, :6] - dense_mobility(pos, q, sh, "medium").reshape(2, 6, 2, 6)).max() < 1e-12
    UE, SF, SE = G[:, :6, :, 6:], G[:, 6:, :, :6], G[:, 6:, :, 6:]
    assert np.linalg.norm(UE + SF.transpose(2, 3, 0, 1)) / np.linalg.norm(UE) < 5e-3                # reciprocity
    assert np.linalg.norm(SE - SE.transpose(2, 3, 0, 1)) / np.linalg.norm(SE) < 5e-3
    assert np.linalg.eigvalsh(0.5 * (SE.reshape(10, 10) + SE.reshape(10, 10).T)).min() > 0          # dissipation is positive


@each_form
def test_far_field(form):
    d, _, _, _, st, ss, Rt, Rs = random_pairs(list(form.test_kinds), 12, r_lo=10.0, r_hi=20.0)
    for i in range(len(d)):
        K = far_blocks(st[i], ss[i], d[i:i + 1], Rt[i:i + 1], Rs[i:i + 1])
        Kb = far_blocks(ss[i], st[i], -d[i:i + 1], Rs[i:i + 1], Rt[i:i + 1])
        assert rel(Kb.transpose(1, 2), K) < 1e-13                      # reciprocity


def test_far_field_stress():
    """The 12-point far field with stresslets and strains against the solver, far apart; exact reciprocity."""
    from farfield import far_grand
    from truth import dense_grand
    rng = np.random.default_rng(43)
    sh = ["prolateSpheroid", "oblateSpheroid"]
    q = rng.normal(size=(2, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    d = rng.normal(size=3)
    pos = np.array([np.zeros(3), 14.0 * d / np.linalg.norm(d)])
    Gt = dense_grand(pos, q, sh, "medium").reshape(2, 11, 2, 11)
    Gf = far_grand(torch.as_tensor(pos), torch.as_tensor(quat_to_matrix(q)), sh, "medium").numpy().reshape(2, 11, 2, 11)
    assert np.abs(Gf[0, :6, 1, 6:] + Gf[1, 6:, 0, :6].T).max() < 1e-12                            # reciprocity of the cross blocks
    for rows, cols, tol in ((slice(0, 6), slice(0, 6), 1e-3), (slice(0, 6), slice(6, 11), 5e-3), (slice(6, 11), slice(0, 6), 5e-3),
                            (slice(6, 11), slice(6, 11), 1e-2)):
        a, b = Gt[0, rows, 1, cols], Gf[0, rows, 1, cols]
        assert np.linalg.norm(a - b) / np.linalg.norm(a) < tol, (rows, cols)


# ----------------------------------------------------------------------------------------------- pair model
@each_form
def test_tensors_distinct(form):
    d, g, pt, ps, *_ = random_pairs(list(form.test_kinds), 64, 3)
    true, pseudo = form.tensors(d / d.norm(dim=-1, keepdim=True), pt, ps)
    assert true.shape[1] == form.n_true and pseudo.shape[1] == form.n_pseudo
    assert form.inputs(d, g, pt, ps).shape[1] == form.n_in
    for T in (true, pseudo):
        flat = T.permute(1, 0, 2, 3).reshape(T.shape[1], -1)
        assert float(flat.norm(dim=1).min()) > 1e-6, "a tensor is identically zero"
        unit = flat / flat.norm(dim=1, keepdim=True)
        cos = (unit @ unit.T).abs() - torch.eye(len(unit))
        assert float(cos.max()) < 1 - 1e-9, "two tensors are proportional"


@each_form
def test_pair_symmetries(form):
    model = randomise(P.PairModel(form.name, width=16))
    d, g, pt, ps, *_ = random_pairs(list(form.test_kinds), 32, 4)
    with torch.no_grad():
        cross, self_ = model(d, g, pt, ps)
    assert float(cross.abs().max()) > 1e-6
    rng = np.random.default_rng(5)
    for reflect in (False, True):                                      # rotation / reflection equivariance
        Q = random_orthogonal(rng, reflect)
        Dm = block_map(Q)
        c2, s2 = model(d @ Q.T, g, P.rotate(pt, Q), P.rotate(ps, Q))
        assert rel(c2, Dm @ cross @ Dm.T) < 1e-10 and rel(s2, Dm @ self_ @ Dm.T) < 1e-10
    cs, _ = model(-d, g, ps, pt)                                       # reciprocity: the pair seen from the source
    assert rel(cs.transpose(1, 2), cross) < 1e-12
    assert rel(self_.transpose(1, 2), self_) < 1e-12
    if form.name == "spheroid":                                        # an axis is a line, not an arrow
        c3, s3 = model(d, g, dict(pt, n=-pt["n"]), ps)
        assert rel(c3, cross) < 1e-12 and rel(s3, self_) < 1e-12
    far = d / d.norm(dim=-1, keepdim=True) * model.r_cut               # nothing learned at or beyond r_cut
    c4, s4 = model(far, g, pt, ps)
    assert float(c4.abs().max()) == 0.0 and float(s4.abs().max()) == 0.0
    for lam in (0.5, 3.0):                                             # Stokes similarity: the pair enlarged by lam
        c5, s5 = model(lam * d, lam * g, P.rescale(pt, lam), P.rescale(ps, lam))
        assert rel(c5, scale_map(lam) * cross) < 1e-12 and rel(s5, scale_map(lam) * self_) < 1e-12


@each_form
def test_pair_contact_cut(form):
    """The contact-factor cut: learned inside c_cut, exactly zero from c_cut on, for any shapes and distance; the
    symmetries and the scaling hold as for the distance cut."""
    kinds = list(form.test_kinds)
    model = randomise(P.PairModel(form.name, width=16, cut="contact"))
    assert model.r_cut == 4.0
    d0, _, pt, ps, *_ = random_pairs(kinds, 24, 31)
    c0 = contact_factor_torch(pt["A"], ps["A"], d0)

    def at(c):                                                         # the same pairs moved to contact factor c
        d = d0 * (c / c0)[:, None]
        return d, clearance_torch(pt["A"], ps["A"], d)

    d, g = at(torch.linspace(1.2, 3.2, 24))
    with torch.no_grad():
        cross, self_ = model(d, g, pt, ps)
    assert float(cross.flatten(1).norm(dim=1).min()) > 1e-9
    for c in (4.0, 4.5, 7.0):                                          # the far field's range: nothing learned
        c4, s4 = model(*at(torch.full((24,), c)), pt, ps)
        assert float(c4.abs().max()) < 1e-12 and float(s4.abs().max()) < 1e-12
    a, b = model(*at(torch.full((24,), 3.999)), pt, ps), model(*at(torch.full((24,), 3.9)), pt, ps)
    assert float(a[0].abs().max()) < 1e-3 * float(b[0].abs().max())    # and it gets there continuously
    rng = np.random.default_rng(32)
    for reflect in (False, True):
        Q = random_orthogonal(rng, reflect)
        Dm = block_map(Q)
        c2, s2 = model(d @ Q.T, g, P.rotate(pt, Q), P.rotate(ps, Q))
        assert rel(c2, Dm @ cross @ Dm.T) < 1e-10 and rel(s2, Dm @ self_ @ Dm.T) < 1e-10
    assert rel(model(-d, g, ps, pt)[0].transpose(1, 2), cross) < 1e-12
    for lam in (0.5, 3.0):
        c5, s5 = model(lam * d, lam * g, P.rescale(pt, lam), P.rescale(ps, lam))
        assert rel(c5, scale_map(lam) * cross) < 1e-12 and rel(s5, scale_map(lam) * self_) < 1e-12


def test_spin_invariance():
    """A spheroid turned about its axis of revolution is the same particle: no descriptor the networks read changes."""
    from scipy.spatial.transform import Rotation
    rng = np.random.default_rng(13)
    for kind in [k for k in ("prolateSpheroid", "oblateSpheroid") if k in SHAPES]:
        assert is_spheroid(kind)
        R = quat_to_matrix(random_quats(rng, 8))
        spin = Rotation.from_rotvec(np.eye(3)[symmetry_axis(kind)] * rng.uniform(0, 6.28, size=(8, 1))).as_matrix()
        a, b = P.describe([kind] * 8, torch.as_tensor(R)), P.describe([kind] * 8, torch.as_tensor(R @ spin))
        for key in P.KEYS:
            assert float((a[key] - b[key]).abs().max()) < 1e-12, (kind, key)


# ----------------------------------------------------------------------------------------------- many-body model
def neighbourhood(kinds, B: int, K: int, seed: int, r_max: float = 10.0):
    rng = np.random.default_rng(seed)
    nbr = torch.as_tensor(rng.normal(size=(B, K, 3)) * r_max / 3)
    sh = [kinds[i] for i in rng.integers(len(kinds), size=B * K)]
    desc = P.describe(sh, torch.as_tensor(quat_to_matrix(random_quats(rng, B * K))))
    return nbr, desc["D"].reshape(B, K, 3, 3), torch.ones(B, K)


def test_band_weights():
    r = torch.linspace(0.01, 13.0, 4001)
    v = torch.stack([r, torch.zeros_like(r), torch.zeros_like(r)], -1)[None]
    _, W = band_weights(v, torch.ones(1, len(r)), 8, 12.0)
    tot = W[0].sum(-1)
    last_centre = 7.5 * 12.0 / 8.5
    assert float((tot[r <= last_centre] - 1).abs().max()) < 1e-12          # partition of unity
    assert float(tot[r >= 12.0].abs().max()) == 0.0                        # nothing beyond the cutoff
    assert float((W[0, 1:] - W[0, :-1]).abs().max()) < 2 * float(r[1] - r[0]) / (12.0 / 8.5) + 1e-12   # continuous


@each_form
def test_nbody_symmetries(form):
    kinds = list(form.test_kinds)
    model = randomise(NbodyModel(form.name, 12.0, 12.0, n_bands=4, width=16))
    assert model.n_in == form.n_in + 80 and model.n_true == form.n_true + 20 and model.n_pseudo == form.n_pseudo + 20
    d, g, pt, ps, *_ = random_pairs(kinds, 16, 7)
    nbr, nD, mask = neighbourhood(kinds, 16, 6, 8)
    K = model(d, g, pt, ps, nbr, nD, mask)
    assert float(K.abs().max()) > 1e-8
    rng = np.random.default_rng(9)
    for reflect in (False, True):
        Q = random_orthogonal(rng, reflect)
        Dm = block_map(Q)
        K2 = model(d @ Q.T, g, P.rotate(pt, Q), P.rotate(ps, Q), nbr @ Q.T, Q @ nD @ Q.T, mask)
        assert rel(K2, Dm @ K @ Dm.T) < 1e-10
    Ks = model(-d, g, ps, pt, nbr, nD, mask)                           # the midpoint neighbourhood is the same
    assert rel(Ks.transpose(1, 2), K) < 1e-12
    assert float(model(d, g, pt, ps, nbr, nD, torch.zeros_like(mask)).abs().max()) == 0.0     # no neighbours
    for lam in (0.5, 3.0):                                             # the whole neighbourhood enlarged by lam
        K3 = model(lam * d, lam * g, P.rescale(pt, lam), P.rescale(ps, lam), lam * nbr, nD, mask)
        assert rel(K3, scale_map(lam) * K) < 1e-12
        nz = torch.randn(nbr.shape[:2])                                # neighbours of other sizes: still exact
        Ka = model(d, g, pt, ps, nbr, nD, mask, nz)
        Kb = model(lam * d, lam * g, P.rescale(pt, lam), P.rescale(ps, lam), lam * nbr, nD, mask, nz + np.log(lam))
        assert rel(Kb, scale_map(lam) * Ka) < 1e-12 and rel(Ka, K) > 1e-6
    perm = torch.randperm(nbr.shape[1])                                # neighbour order does not matter
    assert rel(model(d, g, pt, ps, nbr[:, perm], nD[:, perm], mask), K) < 1e-12


@each_form
def test_nbody_continuity(form):
    """f_nb as a neighbour moves radially through every band edge and out of the neighbourhood: no jump."""
    kinds = list(form.test_kinds)
    model = randomise(NbodyModel(form.name, 12.0, 12.0, n_bands=4, width=16))
    d, g, pt, ps, *_ = random_pairs(kinds, 1, 10)
    nbr, nD, mask = neighbourhood(kinds, 1, 3, 11)
    u = nbr[0, 0] / nbr[0, 0].norm()
    rs = torch.linspace(0.5, 13.0, 2501)
    out = []
    for r in rs:
        n2 = nbr.clone()
        n2[0, 0] = r * u
        m2 = mask.clone()
        m2[0, 0] = float(r < 12.0)                                     # what the operator's selection does
        out.append(model(d, g, pt, ps, n2, nD, m2)[0])
    out = torch.stack(out)
    jump = (out[1:] - out[:-1]).flatten(1).norm(dim=1)
    assert float(jump.max()) < 30 * float(jump.median()) + 1e-12, "f_nb jumps as a neighbour moves"
    for r_pair in (11.999999, 12.0):                                   # and vanishes continuously at the pair cutoff
        K = model(d / d.norm() * r_pair, g, pt, ps, nbr, nD, mask)
        assert float(K.abs().max()) < 1e-9


@each_form
def test_self_model(form):
    kinds = list(form.test_kinds)
    model = randomise(SelfModel(12.0, n_bands=4, width=16))
    _, _, pt, _, *_ = random_pairs(kinds, 16, 21)
    nbr, nD, mask = neighbourhood(kinds, 16, 6, 22)
    K = model(pt, nbr, nD, mask)
    assert float(K.abs().max()) > 1e-8 and rel(K.transpose(1, 2), K) < 1e-12              # a symmetric self block
    rng = np.random.default_rng(23)
    for reflect in (False, True):
        Q = random_orthogonal(rng, reflect)
        Dm = block_map(Q)
        assert rel(model(P.rotate(pt, Q), nbr @ Q.T, Q @ nD @ Q.T, mask), Dm @ K @ Dm.T) < 1e-10
    assert float(model(pt, nbr, nD, torch.zeros_like(mask)).abs().max()) == 0.0               # no neighbour
    one = torch.zeros_like(mask)
    one[:, 0] = 1.0
    assert float(model(pt, nbr, nD, one).abs().max()) < 1e-12                                 # exactly one: the pair model's job
    for lam in (0.5, 3.0):
        assert rel(model(P.rescale(pt, lam), lam * nbr, nD, mask), scale_map(lam) * K) < 1e-12
    perm = torch.randperm(nbr.shape[1])
    assert rel(model(pt, nbr[:, perm], nD[:, perm], mask), K) < 1e-12
    two = one.clone()                                                  # a second neighbour moving out of range: no jump
    two[:, 1] = 1.0
    u = nbr[:, 1] / nbr[:, 1].norm(dim=-1, keepdim=True)
    ell = P.length(pt)[:, None]
    vals = []
    for r in (11.9, 11.99, 11.999):
        n2 = nbr.clone()
        n2[:, 1] = r * ell * u
        vals.append(float(model(pt, n2, nD, two).abs().max()))
    assert vals[2] < vals[1] < vals[0] and vals[2] < 0.05 * vals[0] + 1e-9      # falls with the fading weight (1 / 100 here)


# ----------------------------------------------------------------------------------------------- operator
def small_operator(form, cut="distance"):
    pair = randomise(P.PairModel(form.name, 12.0 if cut == "distance" else None, 16, cut=cut))
    with torch.no_grad():                                              # keep the random model a small perturbation
        pair.mlp[-1].weight.mul_(1e-2), pair.mlp[-1].bias.mul_(1e-2)
    return Operator(pair, randomise(NbodyModel(form.name, 12.0, 12.0, n_bands=4, width=16)), acc=ACC, device="cpu",
                    self_model=randomise(SelfModel(12.0, n_bands=4, width=16)))


@each_form
def test_operator(form):
    rng = np.random.default_rng(12)
    shapes = assign_shapes(form.test_kinds, 7, rng)
    pos, q = uniform_config(shapes, 0.08, rng)
    Q = quat_to_matrix(random_quats(rng, 1)[0])
    G = torch.kron(torch.eye(len(pos)), torch.block_diag(torch.as_tensor(Q), torch.as_tensor(Q)))
    p = rng.permutation(len(pos))
    idx = torch.as_tensor(np.concatenate([6 * i + np.arange(6) for i in p]))
    for cut in ("contact", "distance"):
        op = small_operator(form, cut)
        for mode in ("far", "pair", "full"):
            M = op.grand_M(pos, q, shapes, mode)
            assert rel(M.T, M) < 1e-12, (cut, mode)
            Mr = op.grand_M(pos @ Q.T, matrix_to_quat(Q @ quat_to_matrix(q)), shapes, mode)
            assert rel(Mr, G @ M @ G.T) < 1e-9, (cut, mode)
            Mp = op.grand_M(pos[p], q[p], [shapes[i] for i in p], mode)
            assert rel(Mp, M[idx][:, idx]) < 1e-10, (cut, mode)
        assert rel(op.grand_M(pos, q, shapes, "pair"), op.grand_M(pos, q, shapes, "far")) > 1e-6, cut
    F = rng.normal(size=(len(pos), 6))
    assert np.abs(op.apply(pos, q, shapes, F, "full") - (op.grand_M(pos, q, shapes, "full").numpy() @ F.reshape(-1)).reshape(-1, 6)).max() < 1e-12


@each_form
def test_operator_scaling(form):
    """The same suspension with every particle and distance enlarged by lam (registered sized shapes, e.g.
    prolateSpheroid_x0p75): the learned terms scale exactly."""
    import re
    sized = {}
    for name in SHAPES:
        m = re.fullmatch(r"(.+)_x(\d+)p(\d+)", name)
        if m and m.group(1) in form.test_kinds and os.path.exists(f"{POINTS_DIR}/b_{name}_{ACC}.txt"):
            sized[m.group(1)] = (name, float(f"{m.group(2)}.{m.group(3)}"))
    if not sized:
        print(f"  ({form.name}: no sized shape with a coarse cloud for the test kinds, skipped)")
        return
    base, (big, lam) = next(iter(sized.items()))
    rng = np.random.default_rng(14)
    pos, q = uniform_config([base] * 5, 0.08, rng)
    op = small_operator(form)
    S = torch.kron(torch.ones(5, 5), scale_map(lam))
    for mode in ("pair", "full"):
        learned = lambda shapes, x: op.grand_M(x, q, shapes, mode) - op.grand_M(x, q, shapes, "far")
        a, b = learned([base] * 5, pos), learned([big] * 5, lam * pos)
        assert rel(b, S * a) < 1e-9, mode


# ----------------------------------------------------------------------------------------------- stress model, periodic box
@each_form
def test_stress_model(form):
    from farfield import rot5
    from stress import StressModel, bases
    model = randomise(StressModel(width=16))
    d, g, pt, ps, *_ = random_pairs(list(form.test_kinds), 16, 6)
    t3, p3, t4 = bases(d / d.norm(dim=-1, keepdim=True), pt, ps)
    if "sphere" not in form.test_kinds:                                # the tensor sets span everything at a generic pair
        assert [int(torch.linalg.matrix_rank(x[0].reshape(x.shape[1], -1), rtol=1e-9)) for x in (t3, p3, t4)] == [15, 15, 25]
    with torch.no_grad():
        cross, self_ = model(d, g, pt, ps)
        assert float(cross[:, :6, :6].abs().max()) == 0.0 and float(cross.abs().max()) > 1e-6
        rng = np.random.default_rng(6)
        for reflect in (False, True):
            Q = random_orthogonal(rng, reflect)
            T = torch.zeros(11, 11)
            T[:6, :6], T[6:, 6:] = block_map(Q), rot5(Q[None])[0]
            c2, s2 = model(d @ Q.T, g, P.rotate(pt, Q), P.rotate(ps, Q))
            assert rel(c2, T @ cross @ T.T) < 1e-10 and rel(s2, T @ self_ @ T.T) < 1e-10
        cs, _ = model(-d, g, ps, pt)                                   # the pair seen from the source
        assert rel(-cs[:, :6, 6:].transpose(1, 2), cross[:, 6:, :6]) < 1e-12        # stresslet from force = - (velocity from strain)^T
        assert rel(cs[:, 6:, 6:].transpose(1, 2), cross[:, 6:, 6:]) < 1e-12
        assert rel(self_[:, 6:, 6:].transpose(1, 2), self_[:, 6:, 6:]) < 1e-12
        assert rel(-self_[:, :6, 6:].transpose(1, 2), self_[:, 6:, :6]) < 1e-12
        c4, s4 = model(d / d.norm(dim=-1, keepdim=True) * model.r_cut, g, pt, ps)
        assert float(c4.abs().max()) == 0.0 and float(s4.abs().max()) == 0.0
        lam = 1.7                                                      # Stokes similarity
        S = torch.ones(11, 11)
        S[:3, 6:] = S[6:, :3] = lam
        S[6:, 6:] = lam ** 3
        c5, s5 = model(lam * d, lam * g, P.rescale(pt, lam), P.rescale(ps, lam))
        assert rel(c5, S * cross) < 1e-12 and rel(s5, S * self_) < 1e-12


def test_periodic_stokeslet():
    from periodic import HASIMOTO, stokeslet_periodic
    z = torch.zeros(1, 3)
    for L in (1.0, 7.0):                                               # a cubic array of point forces: Hasimoto's constant
        g = stokeslet_periodic(z, z, L, torch.ones(1, 1, dtype=torch.bool))[0, 0]
        assert abs(float(-g[0, 0]) * 6 * np.pi * L - HASIMOTO) < 1e-6 and abs(float(g[0, 1])) < 1e-12
    rng = np.random.default_rng(8)
    a, b = torch.as_tensor(rng.uniform(0, 5, (4, 3))), torch.as_tensor(rng.uniform(0, 5, (3, 3)))
    G = stokeslet_periodic(a, b, 5.0)
    assert rel(stokeslet_periodic(a, b, 5.0, xi=0.9), G) < 1e-7        # independent of the splitting
    assert rel(stokeslet_periodic(a + 5.0 * torch.tensor([1.0, -2.0, 0.0]), b, 5.0), G) < 1e-10


@each_form
def test_periodic_operator(form):
    from periodic import periodic_M, periodic_config
    from stress import StressModel
    rng = np.random.default_rng(14)
    shapes = assign_shapes(form.test_kinds, 6, rng)
    op = small_operator(form)
    pos, q = uniform_config(shapes, 0.08, rng)
    for mode in ("far", "pair", "full"):                               # a huge box is free space
        assert rel(periodic_M(op, pos - pos.min(0), q, shapes, 1e7, mode), op.grand_M(pos, q, shapes, mode)) < 1e-4, mode
    pos, q, L = periodic_config(shapes, 0.05, rng)
    sm = randomise(StressModel(width=16))
    with torch.no_grad():
        sm.mlp[-1].weight.mul_(1e-2), sm.mlp[-1].bias.mul_(1e-2)
    shift = rng.uniform(0, L, 3)
    for mode in ("far", "pair", "full"):
        M = periodic_M(op, pos, q, shapes, L, mode)
        assert rel(M.T, M) < 1e-10, mode
        assert rel(periodic_M(op, pos + shift, q, shapes, L, mode), M) < 1e-8, mode      # the box has no origin
    G = periodic_M(op, pos, q, shapes, L, "full", sm)
    assert rel(G.reshape(6, 11, 6, 11)[:, :6, :, :6].reshape(36, 36), M) < 1e-12
    Cm = (G - periodic_M(op, pos, q, shapes, L, "full", True)).reshape(6, 11, 6, 11)     # what the stress model adds
    assert float(Cm.abs().max()) > 1e-8
    assert rel(-Cm[:, :6, :, 6:].permute(2, 3, 0, 1), Cm[:, 6:, :, :6]) < 1e-10
    assert rel(Cm[:, 6:, :, 6:].permute(2, 3, 0, 1), Cm[:, 6:, :, 6:]) < 1e-10
    assert rel(periodic_M(op, pos + shift, q, shapes, L, "full", sm), G) < 1e-8


# ----------------------------------------------------------------------------------------------- positive definiteness
def _roots(D: torch.Tensor):
    """Symmetric W = D^-1/2 and W^-1 per block of D (N, b, b)."""
    w, V = torch.linalg.eigh(D)
    return (V / w.sqrt()[:, None, :]) @ V.transpose(1, 2), (V * w.sqrt()[:, None, :]) @ V.transpose(1, 2)


def _blockdiag_congruence(X: torch.Tensor, A: torch.Tensor) -> torch.Tensor:
    N, b = A.shape[:2]
    return torch.einsum("tij,tjsk,slk->tisl", A, X.reshape(N, b, N, b), A).reshape(N * b, N * b)


def test_psd_projection():
    """psd.project: exact floor, never further from any admissible truth, untouched when already positive definite,
    idempotent, independent of the square root used, 1-Lipschitz, covariant under enlarging every particle."""
    import psd
    rng = np.random.default_rng(31)
    N, b = 5, 6
    for trial in range(40):
        A = torch.as_tensor(rng.normal(size=(N, b, b)))
        D = A @ A.transpose(1, 2) + 0.5 * torch.eye(b)                  # isolated blocks: any positive definite ones
        W, Wi = _roots(D)
        X = torch.as_tensor(rng.normal(size=(N * b, N * b)))
        M = _blockdiag_congruence(0.5 * (X + X.T) + 1.5 * torch.eye(N * b), Wi)     # symmetric, usually indefinite
        P_, info = psd.project(M, W, Wi)
        lam = torch.linalg.eigvalsh(_blockdiag_congruence(P_, W))
        assert float(lam[0]) >= 0.5 * psd.FLOOR and rel(P_, P_.T) < 1e-14
        Y = torch.as_tensor(rng.normal(size=(N * b, N * b)))
        T = _blockdiag_congruence(Y @ Y.T / (N * b) + 1e-3 * torch.eye(N * b), Wi)          # an admissible "truth"
        wn = lambda Z: float(_blockdiag_congruence(Z, W).norm())
        assert wn(P_ - T) <= wn(M - T) * (1 + 1e-12), trial                             # never further from the truth
        P2, info2 = psd.project(P_, W, Wi)
        assert not info2["projected"] and P2 is P_                                       # idempotent, untouched when PD
        Q = torch.linalg.qr(torch.as_tensor(rng.normal(size=(N, b, b))))[0]             # another square root: O W
        P3, _ = psd.project(M, Q @ W, Wi @ Q.transpose(1, 2))
        assert rel(P3, P_) < 1e-10
        dM = _blockdiag_congruence(torch.as_tensor(rng.normal(size=(N * b, N * b))), Wi)
        dM = 1e-3 * 0.5 * (dM + dM.T)
        P4, _ = psd.project(M + dM, W, Wi)
        assert wn(P4 - P_) <= wn(dM) * (1 + 1e-9)                                        # 1-Lipschitz
        lam_s = float(rng.uniform(0.5, 3.0))                                             # every length x lam_s
        S = torch.ones(b) / lam_s ** 0.5
        S[3:] /= lam_s
        Sm = torch.diag(S).expand(N, b, b)
        Ws, Wis = _roots(Sm @ D @ Sm)
        P5, _ = psd.project(_blockdiag_congruence(M, Sm), Ws, Wis)
        assert rel(P5, _blockdiag_congruence(P_, Sm)) < 1e-10                            # exactly covariant
    Z = torch.as_tensor(rng.normal(size=(N * b, N * b)))
    M = _blockdiag_congruence(Z @ Z.T + torch.eye(N * b), Wi)                            # positive definite: bit for bit
    assert psd.project(M, W, Wi)[0] is M


@each_form
def test_psd_operator(form):
    """The operator in every mode, on a dense suspension where the raw sum is NOT positive definite: projected it is,
    and it stays symmetric, rotation equivariant and independent of particle order."""
    import psd
    rng = np.random.default_rng(32)
    shapes = assign_shapes(form.test_kinds, 9, rng)
    pos, q = uniform_config(shapes, 0.2, rng)
    pair = randomise(P.PairModel(form.name, 12.0, 16))                  # NOT damped: a strongly indefinite raw sum
    op = Operator(pair, randomise(NbodyModel(form.name, 12.0, 12.0, n_bands=4, width=16)), acc=ACC, device="cpu",
                  self_model=randomise(SelfModel(12.0, n_bands=4, width=16)))
    N = len(pos)
    R = torch.as_tensor(quat_to_matrix(q))
    Q = quat_to_matrix(random_quats(rng, 1)[0])
    G = torch.kron(torch.eye(N), torch.block_diag(torch.as_tensor(Q), torch.as_tensor(Q)))
    perm = rng.permutation(N)
    idx = torch.as_tensor(np.concatenate([6 * i + np.arange(6) for i in perm]))
    for mode in ("pair", "full"):
        raw = op.grand_M(pos, q, shapes, mode, psd=False)
        assert float(psd.spectrum(raw, shapes, R, ACC)[0]) < 0, (mode, "the test needs an indefinite raw sum")
        M = op.grand_M(pos, q, shapes, mode)
        assert op.last_psd["projected"] and float(psd.spectrum(M, shapes, R, ACC)[0]) >= 0.5 * psd.FLOOR
        assert rel(M, M.T) < 1e-13
        Mr = op.grand_M(pos @ Q.T, matrix_to_quat(Q @ quat_to_matrix(q)), shapes, mode)
        assert rel(Mr, G @ M @ G.T) < 1e-8, mode                       # rotation of everything
        Mp = op.grand_M(pos[perm], q[perm], [shapes[i] for i in perm], mode)
        assert rel(Mp, M[idx][:, idx]) < 1e-9, mode                    # relabelling of the particles
    M = op.grand_M(pos, q, shapes, "far")                            # the far field alone is positive definite: untouched
    assert not op.last_psd["projected"] and torch.equal(M, op.grand_M(pos, q, shapes, "far", psd=False))


def test_psd_grand():
    """Stress blocks: velocity-from-force and stresslet-from-strain parts made positive semi-definite, coupling kept."""
    import psd
    rng = np.random.default_rng(33)
    shapes = ["prolateSpheroid", "oblateSpheroid", "prolateSpheroid", "oblateSpheroid"]
    N = len(shapes)
    R = torch.as_tensor(quat_to_matrix(random_quats(rng, N)))
    X = torch.as_tensor(rng.normal(size=(11 * N, 11 * N))) * 0.3
    G = X + X.T
    Gp, info = psd.project_grand(G, shapes, R, "medium")
    Gb, Gpb = G.reshape(N, 11, N, 11), Gp.reshape(N, 11, N, 11)
    assert info["mobility"]["projected"] and info["stress"]["projected"]
    assert torch.equal(Gpb[:, :6, :, 6:], Gb[:, :6, :, 6:]) and torch.equal(Gpb[:, 6:, :, :6], Gb[:, 6:, :, :6])
    W, _ = psd.whitening_stress(shapes, R, "medium")
    C = psd._congruence(Gpb[:, 6:, :, 6:].reshape(5 * N, 5 * N), W)
    assert float(torch.linalg.eigvalsh(C)[0]) >= 0.5 * psd.FLOOR
    assert float(psd.spectrum(Gpb[:, :6, :, :6].reshape(6 * N, 6 * N), shapes, R, "medium")[0]) >= 0.5 * psd.FLOOR


@each_form
def test_fast_operator(form):
    """fast.FastOperator (matrix-free: grid far field, cell lists) gives the dense operator's velocities in every mode."""
    from fast import FastOperator
    rng = np.random.default_rng(34)
    shapes = assign_shapes(form.test_kinds, 24, rng)
    pos, q = uniform_config(shapes, 0.1, rng)
    op = small_operator(form)
    fast = FastOperator(op, dtype=torch.float64)
    F = rng.normal(size=(len(pos), 6))
    for mode in ("far", "pair", "full"):
        ref = op.apply(pos, q, shapes, F, mode, psd=False)
        assert np.linalg.norm(fast.apply(pos, q, shapes, F, mode) - ref) / np.linalg.norm(ref) < 1e-3, mode


def main():
    tests = [(k, v) for k, v in globals().items() if k.startswith("test_") and callable(v)]
    for name, fn in tests:
        fn()
        print(f"ok   {name}")
    print(f"\n{len(tests)} tests passed (forms: {', '.join(f.name for f in FORMS)}; {ACC} clouds)")


if __name__ == "__main__":
    main()
