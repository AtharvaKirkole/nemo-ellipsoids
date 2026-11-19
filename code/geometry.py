"""Shapes, orientations, the contact factor and particle placement.  Everything here is geometry only.

Shapes are registered by the workspace: data/points/shapes.json (name -> semi-axes) next to the point clouds.

Conventions (the repo's): a configuration is positions (P, 3), scalar-LAST quaternions (P, 4) and one registered shape
name per particle.  R = quat_to_matrix(q) maps body to lab; a shape's semi-axes (a1, a2, a3) lie along the body axes.
A = R diag(a^2) R^T is the particle's shape matrix: its surface is x^T A^-1 x = 1.

Contact factor (Perram-Wertheim): the factor by which BOTH particles of a pair can be inflated before they touch,
c = sqrt(max_lam lam (1 - lam) d^T [(1 - lam) A1 + lam A2]^-1 d).  c = 1 touching; for unit spheres c = r / 2.
Clearance g = r (1 - 1 / c): the centre distance minus the centre distance at which this pair, so oriented, touches.
"""
from __future__ import annotations

import json
import math
import os

import numpy as np
import torch
from scipy.optimize import minimize_scalar

POINTS_DIR = os.path.join("data", "points")     # relative to the WORKSPACE = the directory the scripts are run from
SHAPES = {"sphere": (1.0, 1.0, 1.0), "prolateSpheroid": (1.0, 1.0, 3.0), "oblateSpheroid": (2.0, 2.0, 1.0)}
if os.path.exists(os.path.join(POINTS_DIR, "shapes.json")):
    for _name, _axes in json.load(open(os.path.join(POINTS_DIR, "shapes.json"))).items():
        SHAPES.setdefault(_name, tuple(float(x) for x in _axes))


def axes_of(shape: str) -> np.ndarray:
    assert shape in SHAPES, f"unknown shape {shape!r}; registered: {sorted(SHAPES)}"
    return np.asarray(SHAPES[shape], dtype=np.float64)


def volume(shape: str) -> float:
    return float(4.0 / 3.0 * math.pi * np.prod(axes_of(shape)))


def is_spheroid(shape: str) -> bool:
    a = axes_of(shape)
    return int(np.sum(np.isclose(a, np.median(a)))) == 2


def symmetry_axis(shape: str) -> int:
    """Index of a spheroid's body axis of revolution (the odd one out)."""
    a = axes_of(shape)
    assert is_spheroid(shape), f"{shape} is not a spheroid"
    return int(np.argmax(np.abs(a - np.median(a))))


# ----------------------------------------------------------------------------------------------- orientations
def quat_to_matrix(q) -> np.ndarray:
    """Scalar-last quaternions (..., 4) -> rotation matrices (..., 3, 3), body to lab."""
    q = np.asarray(q, dtype=np.float64)
    q = q / np.linalg.norm(q, axis=-1, keepdims=True)
    x, y, z, w = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    R = np.empty(q.shape[:-1] + (3, 3))
    R[..., 0, 0] = 1 - 2 * (y * y + z * z); R[..., 0, 1] = 2 * (x * y - w * z); R[..., 0, 2] = 2 * (x * z + w * y)
    R[..., 1, 0] = 2 * (x * y + w * z); R[..., 1, 1] = 1 - 2 * (x * x + z * z); R[..., 1, 2] = 2 * (y * z - w * x)
    R[..., 2, 0] = 2 * (x * z - w * y); R[..., 2, 1] = 2 * (y * z + w * x); R[..., 2, 2] = 1 - 2 * (x * x + y * y)
    return R


def matrix_to_quat(R) -> np.ndarray:
    from scipy.spatial.transform import Rotation
    return Rotation.from_matrix(np.asarray(R)).as_quat()


def random_quats(rng: np.random.Generator, n: int) -> np.ndarray:
    """Uniform on SO(3), scalar-last, (n, 4)."""
    q = rng.normal(size=(n, 4))
    return q / np.linalg.norm(q, axis=1, keepdims=True)


def shape_matrix(shape: str, R: np.ndarray) -> np.ndarray:
    """A = R diag(a^2) R^T for one frame (3, 3) or a batch (..., 3, 3)."""
    return (R * axes_of(shape) ** 2) @ np.swapaxes(R, -1, -2)


def rotate_block(M: np.ndarray, R: np.ndarray) -> np.ndarray:
    """diag(R, R) M diag(R, R)^T for (..., 6, 6) blocks and (..., 3, 3) rotations."""
    out = np.empty(np.broadcast_shapes(M.shape[:-2], R.shape[:-2]) + (6, 6))
    for i in (0, 3):
        for j in (0, 3):
            out[..., i:i + 3, j:j + 3] = np.einsum("...ab,...bc,...dc->...ad", R, M[..., i:i + 3, j:j + 3], R)
    return out


# ----------------------------------------------------------------------------------------------- contact factor
def contact_factor(A1: np.ndarray, A2: np.ndarray, d: np.ndarray) -> float:
    """Scalar reference (SciPy bounded search): > 1 disjoint, 1 touching, < 1 overlapping."""
    def neg(lam):
        return -lam * (1.0 - lam) * float(d @ np.linalg.solve((1.0 - lam) * A1 + lam * A2, d))
    res = minimize_scalar(neg, bounds=(1e-9, 1.0 - 1e-9), method="bounded", options={"xatol": 1e-10})
    return float(np.sqrt(max(-res.fun, 0.0)))


def _solve_sym3(C: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    """C^-1 v for a batch of symmetric 3x3 C, by the adjugate (no batched LAPACK call)."""
    a, b, c = C[:, 0, 0], C[:, 1, 1], C[:, 2, 2]
    d, e, f = C[:, 0, 1], C[:, 1, 2], C[:, 0, 2]
    A, B_, Cc = b * c - e * e, a * c - f * f, a * b - d * d
    D, E, F = f * e - d * c, d * f - a * e, d * e - b * f
    det = a * A + d * D + f * F
    x = torch.stack([A * v[:, 0] + D * v[:, 1] + F * v[:, 2], D * v[:, 0] + B_ * v[:, 1] + E * v[:, 2],
                     F * v[:, 0] + E * v[:, 1] + Cc * v[:, 2]], -1)
    return x / det[:, None]


def contact_factor_torch(A1: torch.Tensor, A2: torch.Tensor, d: torch.Tensor, iters: int = 32) -> torch.Tensor:
    """Batched contact factor on the device.  The function of lam is concave, so a golden-section search converges;
    32 steps fix lam to 2e-7 (equal to the SciPy reference to 1e-12: tests.py)."""
    g = (math.sqrt(5.0) - 1.0) / 2.0
    lo = torch.full_like(d[:, 0], 1e-9)
    hi = torch.full_like(d[:, 0], 1.0 - 1e-9)

    def F(lam):
        C = (1.0 - lam)[:, None, None] * A1 + lam[:, None, None] * A2
        return lam * (1.0 - lam) * (d * _solve_sym3(C, d)).sum(-1)

    for _ in range(iters):
        x1, x2 = hi - g * (hi - lo), lo + g * (hi - lo)
        left = F(x1) > F(x2)
        hi, lo = torch.where(left, x2, hi), torch.where(left, lo, x1)
    return F(0.5 * (lo + hi)).clamp_min(0.0).sqrt()


def clearance_torch(A_t: torch.Tensor, A_s: torch.Tensor, d: torch.Tensor) -> torch.Tensor:
    """g = r (1 - 1 / c) for a batch of pairs."""
    return d.norm(dim=-1) * (1.0 - 1.0 / contact_factor_torch(A_t, A_s, d))


def min_contact(shapes, pos, quats) -> float:
    """Smallest contact factor over all pairs (pairs too far apart to matter are skipped)."""
    R = quat_to_matrix(quats)
    A = [shape_matrix(s, R[i]) for i, s in enumerate(shapes)]
    reach = [float(axes_of(s).max()) for s in shapes]
    best = np.inf
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            d = pos[j] - pos[i]
            if d @ d > (2.0 * (reach[i] + reach[j])) ** 2:          # contact factor >= 2 there
                continue
            best = min(best, contact_factor(A[i], A[j], d))
    return float(best)


# ----------------------------------------------------------------------------------------------- placement
MARGIN = 0.05                 # contact factor floor 1.05 everywhere (= surface gap 0.1 for unit spheres)


def pair_config(shapes, rng, cmax: float = 8.0, r_max: float | None = None):
    """Two particles, random orientations and direction, contact factor c with c - 1 log-uniform in [0.05, cmax - 1].
    r_max: redraw until the centre distance is below it (pairs beyond the model's range are never trained on, so they
    are not solved either)."""
    while True:
        q = random_quats(rng, 2)
        R = quat_to_matrix(q)
        u = rng.normal(size=3)
        u /= np.linalg.norm(u)
        c = 1.0 + MARGIN * math.exp(rng.uniform(0.0, math.log((cmax - 1.0) / MARGIN)))
        r = c / contact_factor(shape_matrix(shapes[0], R[0]), shape_matrix(shapes[1], R[1]), u)
        if r_max is None or r < r_max:
            return np.array([np.zeros(3), r * u]), q


def _place(shapes, rng, propose, floor, max_attempts=4000, aligned=False):
    """Sequential placement: propose(i, pos, A_list, A_i) -> (x, skip), kept if x clears every placed particle but
    `skip` (the one it was attached to; -1: none) by `floor`.  aligned: one orientation for every particle."""
    q = np.tile(random_quats(rng, 1), (len(shapes), 1)) if aligned else random_quats(rng, len(shapes))
    reach = [float(axes_of(s).max()) for s in shapes]
    pos, A_list = [np.zeros(3)], [shape_matrix(shapes[0], quat_to_matrix(q[0]))]
    for i in range(1, len(shapes)):
        for _ in range(max_attempts):
            A = shape_matrix(shapes[i], quat_to_matrix(q[i]))
            x, skip = propose(i, pos, A_list, A)
            ok = True
            for j, (y, B) in enumerate(zip(pos, A_list)):
                if j == skip:
                    continue
                d = x - y
                lim = (reach[i] + reach[j]) * floor
                if d @ d < lim * lim and contact_factor(B, A, d) < floor - 1e-9:
                    ok = False
                    break
            if ok:
                pos.append(x)
                A_list.append(A)
                break
            if not aligned:
                q[i] = random_quats(rng, 1)[0]                   # a fresh orientation helps a crowded box
        else:
            return None
    return np.array(pos), q


def uniform_config(shapes, phi: float, rng, aligned: bool = False):
    """Centres uniform in a cube of volume (sum of particle volumes) / phi, random orientations, every pair at contact
    factor >= 1.05: the configurations of the paper's Figs. 3 and 4.  None if it could not place everyone."""
    shapes = list(shapes)
    L = (sum(volume(s) for s in shapes) / phi) ** (1.0 / 3.0)
    half = 0.5 * L - float(np.mean([np.prod(axes_of(s)) ** (1.0 / 3.0) for s in shapes]))
    if half <= 0:
        return None
    return _place(shapes, rng, lambda i, pos, A_list, A: (rng.uniform(-half, half, 3), -1), 1.0 + MARGIN, aligned=aligned)


def grown_config(shapes, delta: float, rng):
    """A compact cluster: each new particle is attached to a random placed one at contact factor 1 + delta."""
    def propose(i, pos, A_list, A):
        k = int(rng.integers(len(pos)))
        u = rng.normal(size=3)
        u /= np.linalg.norm(u)
        return pos[k] + (1.0 + delta) / contact_factor(A_list[k], A, u) * u, k
    return _place(list(shapes), rng, propose, 1.0 + delta)


def assign_shapes(kinds, N: int, rng) -> list:
    """N shape names: the kinds in equal number fractions, in random order."""
    kinds = list(kinds)
    out = [kinds[i % len(kinds)] for i in range(N)]
    rng.shuffle(out)
    return out


def frame_quat(shape: str, long_dir, mid_dir) -> np.ndarray:
    """Quaternion that puts the longest body axis on long_dir and the middle one on mid_dir (made orthogonal)."""
    order = np.argsort(axes_of(shape), kind="stable")           # shortest, middle, longest body axes
    L = np.asarray(long_dir, float)
    L = L / np.linalg.norm(L)
    Mv = np.asarray(mid_dir, float)
    Mv = Mv - (Mv @ L) * L
    Mv = Mv / np.linalg.norm(Mv)
    R = np.zeros((3, 3))
    R[:, order[2]], R[:, order[1]], R[:, order[0]] = L, Mv, np.cross(Mv, L)
    if np.linalg.det(R) < 0:
        R[:, order[0]] *= -1
    return matrix_to_quat(R)


def ring_config(shapes, P: int = 5, contact: float = 1.25):
    """P particles on a vertical ring (x-z plane), long axes along y, neighbours at the given contact factor.  The
    dynamics test: under gravity along -z the ring's shape evolves through many-body interactions."""
    sh = [shapes[i % len(shapes)] for i in range(P)]
    th = 2 * np.pi * np.arange(P) / P
    radial = np.stack([np.cos(th), np.zeros(P), np.sin(th)], 1)
    q = np.array([frame_quat(sh[i], [0.0, 1.0, 0.0], radial[i]) for i in range(P)])
    R = quat_to_matrix(q)
    touch = 0.0                                     # the contact factor is linear in the distance
    for i in range(P):
        j = (i + 1) % P
        chord = radial[j] - radial[i]
        chord /= np.linalg.norm(chord)
        touch = max(touch, 1.0 / contact_factor(shape_matrix(sh[i], R[i]), shape_matrix(sh[j], R[j]), chord))
    return contact * touch / (2 * np.sin(np.pi / P)) * radial, q, sh


def tilted_pair_config(shapes, contact: float = 1.5):
    """Two particles side by side along x at the given contact factor, long axes tilted +-45 degrees in the x-z plane:
    under gravity they drift, rotate and interact (the two-body dynamics test)."""
    sh = [shapes[i % len(shapes)] for i in range(2)]
    s2 = math.sqrt(0.5)
    q = np.array([frame_quat(sh[0], [s2, 0, s2], [0, 1, 0]), frame_quat(sh[1], [-s2, 0, s2], [0, 1, 0])])
    R = quat_to_matrix(q)
    d = contact / contact_factor(shape_matrix(sh[0], R[0]), shape_matrix(sh[1], R[1]), np.array([1.0, 0.0, 0.0]))
    return np.array([[-0.5 * d, 0.0, 0.0], [0.5 * d, 0.0, 0.0]]), q, sh
