"""Positive (semi-)definiteness of every operator output, exactly, at no cost in accuracy.

Why the operator needs it (measured, see `evaluate.py psd` and `pd`):
  * Adding pair interactions in mobility space is not positive definite in dense suspensions, even when every pair
    block is EXACT (the summed self corrections over-subtract; cross blocks add up coherently).
  * More fundamentally (Weyl's inequality): |lam_min(M) - lam_min(T)| <= |M - T|_2.  In a dense suspension the
    truth's smallest eigenvalue (the softest collective mode, relative to the isolated mobilities) is a few percent,
    while a percent-level operator error has a spectral norm of the same size or larger.  So NO operator at this
    accuracy can be positive definite by luck; it has to be made so.

What this does: the nearest positive semi-definite matrix in the metric of the isolated particles,

    W = blockdiag(M_iso,1 ... M_iso,N)^(-1/2)          (each particle's own isolated mobility, in the lab frame)
    W M W^T = V diag(lam) V^T,     P(M) = W^-1 V diag(max(lam, floor)) V^T W^-T

(Higham 1988, in the weighted norm |X|_W = |W X W^T|_F).  Properties, all tested (tests.py):
  exact        every eigenvalue of W P(M) W^T is >= floor / 2, those of a projected matrix >= floor (up to
               round-off): P(M) is positive definite.  (A matrix is left alone if its eigenvalues are >= floor / 2, so
               that a projected matrix, whose lowest eigenvalues sit at the floor, is recognised as admissible.)
  no loss      for EVERY matrix T with eigenvalues of W T W^T >= floor -- the MFS truth is one, its smallest is
               reported next to every result -- |P(M) - T|_W <= |M - T|_W.  (Projection onto a closed convex set that
               contains T never moves away from T.)  So the operator gets closer to the truth, never further.
  untouched    if M already has every eigenvalue >= floor / 2 it is returned as it is, bit for bit; so P(P(M)) = P(M).
  symmetry     equivariant under rotations and reflections of the whole configuration and under relabelling of the
               particles (spectral functions are); exactly covariant under enlarging the suspension (the metric
               scales with the particles, so the projection does not mix translation and rotation units); the
               result does not depend on which square root W is used.
  continuous   1-Lipschitz in the W-norm, so trajectories stay continuous when a mode crosses zero.
Cost: one symmetric eigendecomposition of the (6N, 6N) matrix (the operator is dense anyway); skipped by a Cholesky
test when the matrix is already positive definite.

The same for the stress blocks (11 x 11 per particle, rows [U; Omega; S], columns [F; T; E]): the grand matrix is
admissible (it comes from a positive definite grand resistance matrix) if and only if its velocity-from-force part A
and its stresslet-from-strain part C are positive semi-definite; the coupling blocks can be anything.  `project_grand`
projects A in the metric of the isolated mobilities and C in the metric of the isolated stresslet-per-strain blocks.
"""
from __future__ import annotations

import torch

FLOOR = 1e-10            # smallest eigenvalue kept, relative to the isolated particles (MFS truths: 1e-3 and above)
_BODY: dict = {}


def _body_sqrt(key, make):
    """(B^-1/2, B^1/2) of a symmetric positive definite body-frame block B = make(), cached per (shape, kind, acc, dtype,
    device): computed once."""
    if key not in _BODY:
        block = make()
        B = 0.5 * (block + block.T)
        w, V = torch.linalg.eigh(B)
        assert float(w.min()) > 0, f"{key}: the isolated block is not positive definite"
        _BODY[key] = ((V / w.sqrt()) @ V.T, (V * w.sqrt()) @ V.T)
    return _BODY[key]


def whitening(shapes, R: torch.Tensor, acc: str):
    """W, W^-1 per particle, (N, 6, 6): W M_iso,t W^T = I with M_iso,t the isolated mobility in the lab frame."""
    from truth import iso_mobility
    N = len(shapes)
    W = torch.zeros(N, 6, 6, dtype=R.dtype, device=R.device)
    Wi = torch.zeros_like(W)
    G = torch.zeros_like(W)
    G[:, :3, :3] = G[:, 3:, 3:] = R
    for kind in dict.fromkeys(shapes):
        idx = torch.as_tensor([i for i, s in enumerate(shapes) if s == kind], device=R.device)
        a, b = _body_sqrt((kind, "mobility", acc, R.dtype, str(R.device)),
                          lambda: torch.as_tensor(iso_mobility(kind, acc), dtype=R.dtype, device=R.device))
        W[idx], Wi[idx] = G[idx] @ a @ G[idx].transpose(1, 2), G[idx] @ b @ G[idx].transpose(1, 2)
    return W, Wi


def whitening_stress(shapes, R: torch.Tensor, acc: str):
    """The same for the stresslet-from-strain blocks (N, 5, 5), from each particle's isolated block."""
    from farfield import body_operator11, rot5
    N = len(shapes)
    W = torch.zeros(N, 5, 5, dtype=R.dtype, device=R.device)
    Wi = torch.zeros_like(W)
    G = rot5(R)
    for kind in dict.fromkeys(shapes):
        idx = torch.as_tensor([i for i, s in enumerate(shapes) if s == kind], device=R.device)
        a, b = _body_sqrt((kind, "stress", acc, R.dtype, str(R.device)), lambda: body_operator11(kind, acc, R.dtype, R.device)[3][6:, 6:])
        W[idx], Wi[idx] = G[idx] @ a @ G[idx].transpose(1, 2), G[idx] @ b @ G[idx].transpose(1, 2)
    return W, Wi


def _congruence(M: torch.Tensor, W: torch.Tensor) -> torch.Tensor:
    """blockdiag(W) M blockdiag(W)^T for M (N b, N b), W (N, b, b)."""
    N, b = W.shape[0], W.shape[1]
    X = torch.einsum("tij,tjsk,slk->tisl", W, M.reshape(N, b, N, b), W)
    return X.reshape(N * b, N * b)


def project(M: torch.Tensor, W: torch.Tensor, Wi: torch.Tensor, floor: float = FLOOR):
    """-> (P(M), info).  M symmetric (N b, N b); W, Wi (N, b, b) the metric and its inverse.
    info: lam_min = smallest eigenvalue of W M W^T before; changed = |P(M) - M|_W / |M|_W (0 when untouched)."""
    X = _congruence(M, W)
    X = 0.5 * (X + X.T)
    n = X.shape[0]
    eye = torch.eye(n, dtype=X.dtype, device=X.device)
    _, bad = torch.linalg.cholesky_ex(X - 0.5 * floor * eye)
    if int(bad) == 0:                                   # already every eigenvalue >= floor / 2: untouched
        return M, {"lam_min": None, "changed": 0.0, "projected": False}
    lam, V = torch.linalg.eigh(X)
    lam_c = lam.clamp_min(floor)
    Xp = (V * lam_c) @ V.T
    Xp = 0.5 * (Xp + Xp.T)
    out = _congruence(Xp, Wi)
    out = 0.5 * (out + out.T)
    return out, {"lam_min": float(lam[0]), "changed": float((lam_c - lam).norm() / lam.norm()), "projected": True}


def project_mobility(M: torch.Tensor, shapes, R: torch.Tensor, acc: str, floor: float = FLOOR):
    """P(M) for a grand mobility matrix (6N, 6N) of particles `shapes` with frames R (N, 3, 3)."""
    W, Wi = whitening(list(shapes), R.to(M.dtype), acc)
    return project(M, W, Wi, floor)


def project_grand(G: torch.Tensor, shapes, R: torch.Tensor, acc: str, floor: float = FLOOR):
    """The grand matrix with stress (11N, 11N): velocity-from-force and stresslet-from-strain parts made positive
    semi-definite in their own metrics; the coupling parts are left as they are (any coupling is admissible)."""
    N = len(shapes)
    Gb = G.reshape(N, 11, N, 11).clone()
    A, ia = project_mobility(Gb[:, :6, :, :6].reshape(6 * N, 6 * N), shapes, R, acc, floor)
    W, Wi = whitening_stress(list(shapes), R.to(G.dtype), acc)
    C, ic = project(Gb[:, 6:, :, 6:].reshape(5 * N, 5 * N), W, Wi, floor)
    Gb[:, :6, :, :6] = A.reshape(N, 6, N, 6)
    Gb[:, 6:, :, 6:] = C.reshape(N, 5, N, 5)
    return Gb.reshape(11 * N, 11 * N), {"mobility": ia, "stress": ic}


def spectrum(M: torch.Tensor, shapes, R: torch.Tensor, acc: str) -> torch.Tensor:
    """Eigenvalues of W M W^T (ascending): the spectrum relative to the isolated particles (1 = no interaction)."""
    W, _ = whitening(list(shapes), R.to(M.dtype), acc)
    X = _congruence(M, W)
    return torch.linalg.eigvalsh(0.5 * (X + X.T))


def wnorm(X: torch.Tensor, shapes, R: torch.Tensor, acc: str) -> torch.Tensor:
    """|X|_W = |W X W^T|_F, the norm in which the projection is non-expansive."""
    W, _ = whitening(list(shapes), R.to(X.dtype), acc)
    return _congruence(X, W).norm()
