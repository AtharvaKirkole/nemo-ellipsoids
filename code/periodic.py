#!/usr/bin/env python3
"""A periodic box (bulk suspension): the same operator with every image of every particle.

Each particle is 12 point forces (farfield.py), so the far field in a periodic cube of side L is the 12-point far
field with the Stokeslet replaced by its periodic sum (Hasimoto 1959; Ewald splitting as Beenakker 1986, plain
Stokeslet).  The k = 0 term is left out: no net flow through the box, the mean force is balanced by a pressure
gradient (the usual choice for sedimentation and rheology).  The learned parts (two-body model, many-body models,
stress model) are short-ranged corrections to the far field, so they are added for every pair of a particle and a
(periodic image of a) particle inside their range, with neighbourhoods that include the images.

    M = periodic_M(op, pos, quats, shapes, L, mode)            (6N, 6N)   [11N with stress=...: + strain and stresslet]

Checks (tests.py): the settling speed of a cubic array of point-like spheres, 1 - 2.837297 a / L (Hasimoto); the
result does not depend on the splitting parameter; a huge box gives the free-space matrix.
There is NO truth for periodic boxes here (MFS is free-space): the periodic far field is exact to the order of the
12-point rule, the learned corrections are the ones validated in free space.

    python periodic.py bulk --kinds prolateSpheroid --phi 0.02 0.05 0.1 --N 64 --pair pair.pt --nbody nbody.pt --stress stress.pt
    python periodic.py streamers --kinds prolateSpheroid --phi 0.01 --N 200

bulk      random periodic suspensions at each volume fraction: hindered settling (mean speed along gravity / the
          isolated particle's), short-time self-diffusion (translation, rotation) and the relative viscosity
          eta / eta_0 = 1 + (1 / 2V) < sum_t S_t : E > / (E : E), averaged over the 5 strains (isotropic average)
          -- each for the far field alone and with every model given.
streamers settling of N particles in a periodic box in time (far field + a short-range repulsion that keeps them
          apart): mean speed, velocity fluctuations, alignment with gravity and the number-density structure against
          time -- the settling instability of spheroids (Koch & Shaqfeh 1989).  Statistics only, no truth.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import time

import numpy as np
import torch

import pair as P
from farfield import _lab_operator, body_operator, body_operator11, far_blocks11, lab_operator11, rot11
from geometry import axes_of, clearance_torch, contact_factor_torch, quat_to_matrix, random_quats, volume
from truth import iso_mobility

INV_8PI = 1.0 / (8.0 * math.pi)
HASIMOTO = 2.837297


# ----------------------------------------------------------------------------------------------- periodic Stokeslet
def _grid(n: int, dtype, device) -> torch.Tensor:
    a = torch.arange(-n, n + 1, dtype=dtype, device=device)
    return torch.stack(torch.meshgrid(a, a, a, indexing="ij"), -1).reshape(-1, 3)


def stokeslet_periodic(pa, pb, L: float, same=None, xi: float | None = None, chunk: int = 256) -> torch.Tensor:
    """Periodic Stokeslet (n, m, 3, 3) between points pa (n, 3) and pb (m, 3) in a cube of side L, no mean flow.
    same (n, m) bool: for these entries the free-space Stokeslet of the direct separation pa - pb is left out (points
    of the same particle: only the images act; pa = pb gives the Hasimoto constant)."""
    dt, dev = pa.dtype, pa.device
    xi = xi or 2.0 * math.sqrt(math.pi) / L
    n, m = len(pa), len(pb)
    eye = torch.eye(3, dtype=dt, device=dev)
    shifts = L * _grid(2, dt, dev)
    out = torch.zeros(n, m, 3, 3, dtype=dt, device=dev)
    for i in range(0, n, chunk):
        x = pa[i:i + chunk, None, :] - pb[None, :, :]
        x = x - L * torch.round(x / L)
        sm = same[i:i + chunk] if same is not None else torch.zeros(x.shape[:2], dtype=torch.bool, device=dev)
        acc = torch.zeros(*x.shape[:2], 3, 3, dtype=dt, device=dev)
        for sh in shifts:
            r = x + sh
            rn = r.norm(dim=-1)
            ok = rn > 1e-12
            rs = torch.where(ok, rn, torch.ones_like(rn))
            a = xi * rs
            e = torch.exp(-a * a) * 2.0 * a / math.sqrt(math.pi)
            C, D = torch.erfc(a) + e * (2 * a * a - 3), torch.erfc(a) + e * (1 - 2 * a * a)
            if not bool(sh.abs().max() > 0):                               # the direct separation
                C, D = torch.where(sm, C - 1.0, C), torch.where(sm, D - 1.0, D)
            term = (C / rs)[..., None, None] * eye + (D / rs ** 3)[..., None, None] * r[..., :, None] * r[..., None, :]
            term = torch.where(ok[..., None, None], term, (-8.0 * xi / math.sqrt(math.pi)) * eye.expand_as(term))
            acc += term
        out[i:i + chunk] = acc * INV_8PI
    mk = _grid(6, dt, dev)
    key = mk[:, 0] * 169 + mk[:, 1] * 13 + mk[:, 2]
    k = 2.0 * math.pi / L * mk[key > 0]                                    # half of the modes; the other half doubles them
    k2 = (k * k).sum(-1)
    q = k2 / (4 * xi * xi)
    A = 2.0 / L ** 3 * (1 + q + 2 * q * q) * torch.exp(-q) / k2
    W = A[:, None, None] * (eye - k[:, :, None] * k[:, None, :] / k2[:, None, None])
    ca, sa, cb, sb = torch.cos(pa @ k.T), torch.sin(pa @ k.T), torch.cos(pb @ k.T), torch.sin(pb @ k.T)
    for i in range(3):
        for j in range(i, 3):
            g = (ca * W[:, i, j]) @ cb.T + (sa * W[:, i, j]) @ sb.T
            out[:, :, i, j] += g
            if j != i:
                out[:, :, j, i] += g
    return out


# ----------------------------------------------------------------------------------------------- far field
def periodic_far(pos, R, shapes, L: float, acc: str = "fine", strain: bool = False, xi: float | None = None) -> torch.Tensor:
    """The far-field matrix of N particles in the periodic cube: (6N, 6N), or (11N, 11N) with strain and stresslets
    (rows [U; Omega; S], columns [F; T; E] as truth.dense_grand).  pos (N, 3), R (N, 3, 3) tensors."""
    N, b = len(pos), 11 if strain else 6
    shapes = list(shapes)
    pts = torch.zeros(N, 12, 3, dtype=pos.dtype, device=pos.device)
    Pl = torch.zeros(N, b, 36, dtype=pos.dtype, device=pos.device)
    single = torch.zeros(N, b, b, dtype=pos.dtype, device=pos.device)
    for kind in dict.fromkeys(shapes):
        idx = torch.as_tensor([i for i, s in enumerate(shapes) if s == kind], device=pos.device)
        if strain:
            body, C, ZQ, G1 = body_operator11(kind, acc, pos.dtype, pos.device)
            Pl[idx], T = lab_operator11(C, ZQ, R[idx]), rot11(R[idx])
        else:
            body, C = body_operator(kind, pos.dtype, pos.device)
            G1 = torch.as_tensor(iso_mobility(kind, acc), dtype=pos.dtype, device=pos.device)
            Pl[idx] = _lab_operator(C, R[idx])
            T = torch.zeros(len(idx), 6, 6, dtype=pos.dtype, device=pos.device)
            T[:, :3, :3] = T[:, 3:, 3:] = R[idx]
        single[idx] = T @ G1 @ T.transpose(1, 2)
        pts[idx] = body @ R[idx].transpose(1, 2) + pos[idx, None, :]
    flat = pts.reshape(-1, 3)
    owner = torch.arange(N, device=pos.device).repeat_interleave(12)
    G = stokeslet_periodic(flat, flat, L, owner[:, None] == owner[None, :], xi)
    G = G.reshape(N, 12, N, 12, 3, 3).permute(0, 1, 4, 2, 3, 5).reshape(N, 36, N, 36)
    M = torch.einsum("tai,tisj,sbj->tasb", Pl, G, Pl)
    if strain:
        M[..., 6:] = -M[..., 6:]
    ar = torch.arange(N, device=pos.device)
    M[ar, :, ar, :] += single
    return M.reshape(b * N, b * N)


# ----------------------------------------------------------------------------------------------- with the models
def _ghosts(pos: np.ndarray, L: float, reach: float):
    """Every image (shift != 0) of a particle that lies within `reach` of the box -> positions, parent indices."""
    m = int(math.ceil(reach / L))
    out_x, out_p = [np.zeros((0, 3))], [np.zeros(0, dtype=np.int64)]
    for sh in _grid(m, torch.float64, "cpu").numpy():
        if not sh.any():
            continue
        x = pos + L * sh
        dist = np.linalg.norm(np.maximum(np.maximum(-x, x - L), 0.0), axis=1)        # distance to the box [0, L]^3
        keep = np.nonzero(dist < reach)[0]
        out_x.append(x[keep]), out_p.append(keep)
    return np.concatenate(out_x), np.concatenate(out_p)


def _pair_reach(model, lmax: float, amax: float) -> float:
    return model.r_cut * (lmax if model.cut == "distance" else 2.0 * amax)


@torch.no_grad()
def periodic_M(op, pos, quats, shapes, L: float, mode: str = "full", stress=None, xi: float | None = None) -> torch.Tensor:
    """The operator of mobility.py in the periodic cube of side L.  mode as Operator.grand_M ("far", "pair", "full").
    stress: None -> (6N, 6N); True -> (11N, 11N), the strain / stresslet blocks from the far field alone;
    a StressModel -> + its two-body corrections of those blocks."""
    from nbody import neighbours
    shapes = list(shapes)
    N = len(shapes)
    pos = np.mod(np.asarray(pos, dtype=np.float64), L)
    quats = np.asarray(quats, dtype=np.float64)
    b = 6 if stress is None else 11
    X, R, _, _, _ = op.geometry(pos, quats, shapes)
    M = periodic_far(X, R, shapes, L, op.acc, strain=stress is not None, xi=xi)
    smodel = stress.double().to(op.dev).eval() if isinstance(stress, torch.nn.Module) else None
    learned = mode != "far"
    if not learned and smodel is None:
        return M
    lmax, amax = max(float(axes_of(s).min()) for s in shapes), max(float(axes_of(s).max()) for s in shapes)
    reach = max(_pair_reach(op.pair, lmax, amax) if learned else 0.0, _pair_reach(smodel, lmax, amax) if smodel is not None else 0.0)
    ghost = reach
    if mode == "full":
        ghost = max(ghost, 0.5 * op.nbody.pair_cutoff * lmax + op.nbody.neighbor_cutoff * lmax,
                    op.nself.neighbor_cutoff * lmax if op.nself is not None else 0.0)
    gx, gp = _ghosts(pos, L, ghost)
    parent = torch.as_tensor(np.concatenate([np.arange(N), gp]), device=op.dev)
    Xe, Re, desc, kinds, kid = op.geometry(np.concatenate([pos, gx]), np.concatenate([quats, quats[gp]]), shapes + [shapes[i] for i in gp])
    C = torch.zeros(N * N, b, b, dtype=torch.float64, device=op.dev)
    selfsum = torch.zeros(N, b, b, dtype=torch.float64, device=op.dev)
    for i in range(0, N, 64):
        tt = torch.arange(i, min(N, i + 64), device=op.dev)
        dist = torch.cdist(Xe[tt], Xe)
        dist[torch.arange(len(tt), device=op.dev), tt] = float("inf")
        a, s = torch.nonzero(dist < reach, as_tuple=True)
        t = tt[a]
        if not len(t):
            continue
        d = Xe[s] - Xe[t]
        flat = t * N + parent[s]
        if learned:
            cross, self_, g = op.two_body(Xe, Re, desc, kinds, kid, t, s)
            corr = cross - op.far(Xe, Re, kinds, kid, t, s)
            if mode == "full":
                k = torch.nonzero(d.norm(dim=-1) / P.pair_length(P.take(desc, t), P.take(desc, s)) < op.nbody.pair_cutoff)[:, 0]
                if len(k):
                    corr[k] += op.many_body(Xe, desc, t[k], s[k], g[k])
            pad = torch.zeros(len(t), b, b, dtype=torch.float64, device=op.dev)
            pad[:, :6, :6] = corr
            C.index_add_(0, flat, pad)
            pad[:, :6, :6] = self_
            selfsum.index_add_(0, t, pad)
        if smodel is not None:
            pt, ps = P.take(desc, t), P.take(desc, s)
            lim = smodel.r_cut * (P.pair_length(pt, ps) if smodel.cut == "distance" else desc["amax"][t] + desc["amax"][s])
            k = torch.nonzero(d.norm(dim=-1) < lim)[:, 0]
            if len(k):
                pt, ps = P.take(desc, t[k]), P.take(desc, s[k])
                g = clearance_torch(pt["A"], ps["A"], d[k])
                cs, sf = smodel(d[k], g, pt, ps)
                far = torch.zeros_like(cs)                                  # the model replaces w x the far field of these blocks
                for ka in range(len(kinds)):
                    for kb in range(len(kinds)):
                        m = torch.nonzero((kid[t[k]] == ka) & (kid[s[k]] == kb))[:, 0]
                        if len(m):
                            far[m] = far_blocks11(kinds[ka], kinds[kb], d[k][m], Re[t[k][m]], Re[s[k][m]], op.acc)
                far[:, :6, :6] = 0.0
                C.index_add_(0, flat[k], cs - smodel.weight(d[k], g, pt, ps)[:, None, None] * far)
                selfsum.index_add_(0, t[k], sf)
    if mode == "full" and op.nself is not None:
        for i in range(0, N, op.nb_chunk):
            idx = torch.arange(i, min(N, i + op.nb_chunk), device=op.dev)
            pt = P.take(desc, idx)
            nbr, nD, mask, nz = neighbours(Xe, desc["D"], Xe[idx], idx[:, None], op.nself.neighbor_cutoff * P.length(pt), desc["z"])
            selfsum[idx, :6, :6] += op.nself(pt, nbr, nD, mask, nz) / P.SIX_PI
    C = C.reshape(N, N, b, b)
    ar = torch.arange(N, device=op.dev)
    C[ar, ar] += selfsum
    return M + C.permute(0, 2, 1, 3).reshape(b * N, b * N)


# ----------------------------------------------------------------------------------------------- configurations
def periodic_config(shapes, phi: float, rng, floor: float = 1.05, tries: int = 200000):
    """Random positions and orientations in a periodic cube at volume fraction phi, every pair (images included) at
    contact factor >= floor.  -> pos (N, 3), quats (N, 4), L; None if it could not place everyone."""
    shapes = list(shapes)
    L = (sum(volume(s) for s in shapes) / phi) ** (1.0 / 3.0)
    amax = np.array([axes_of(s).max() for s in shapes])
    assert L > 2.0 * floor * amax.max(), f"box {L:.2f} too small for the longest particle (needs > {2 * floor * amax.max():.2f})"
    pos, quats, A = [], [], []
    for i, s in enumerate(shapes):
        for _ in range(tries):
            x, q = rng.uniform(0, L, 3), random_quats(rng, 1)[0]
            Rm = quat_to_matrix(q[None])[0]
            Ai = (Rm * axes_of(s) ** 2) @ Rm.T
            if pos:
                d = np.array(pos) - x
                d -= L * np.round(d / L)
                near = np.nonzero(np.linalg.norm(d, axis=1) < floor * (amax[:len(pos)] + amax[i]))[0]
                if len(near):
                    c = contact_factor_torch(torch.as_tensor(Ai).expand(len(near), 3, 3), torch.as_tensor(np.array(A)[near]),
                                             torch.as_tensor(d[near]))
                    if float(c.min()) < floor:
                        continue
            pos.append(x), quats.append(q), A.append(Ai)
            break
        else:
            return None
    return np.array(pos), np.array(quats), L


# ----------------------------------------------------------------------------------------------- bulk properties
def bulk_numbers(M: torch.Tensor, shapes, L: float, acc: str) -> dict:
    """From one periodic matrix (6N or 11N): hindered settling, short-time self-diffusion, relative viscosity."""
    N = len(shapes)
    b = M.shape[0] // N
    Mb = M.reshape(N, b, N, b)
    iso = {s: iso_mobility(s, acc) for s in set(shapes)}
    u0 = np.mean([np.trace(iso[s][:3, :3]) / 3 for s in shapes])            # orientation-averaged isolated speed per unit force
    w0 = np.mean([np.trace(iso[s][3:, 3:]) / 3 for s in shapes])
    ar = torch.arange(N, device=M.device)
    Ms = Mb[ar, :, ar, :]
    out = {"settling": float(sum(Mb[:, i, :, i].sum() for i in range(3)) / (3 * N) / u0),   # mean over the 3 directions of gravity
           "D_trans": float(Ms[:, :3, :3].diagonal(dim1=1, dim2=2).sum() / (3 * N) / u0),
           "D_rot": float(Ms[:, 3:6, 3:6].diagonal(dim1=1, dim2=2).sum() / (3 * N) / w0)}
    if b == 11:
        Z = Mb[:, 6:, :, 6:].sum((0, 2))                                    # total stresslet per unit uniform strain, (5, 5)
        out["viscosity"] = float(1.0 + Z.trace() / 5.0 / (2.0 * L ** 3))
    return out


def cmd_bulk(args) -> None:
    from evaluate import operator
    from truth import intrinsic_viscosity
    op, modes = operator(args)
    smodel = None
    if args.stress:
        from stress import load_stress
        smodel = load_stress(args.stress)
    cases = [(m, True) for m in modes] + ([(modes[-1], smodel)] if smodel is not None else [])
    names = [m + (" + stress model" if s is not True else "") for m, s in cases]
    rows, t0 = [], time.time()
    for phi in args.phi:
        acc = {n: [] for n in names}
        for seed in range(args.seeds):
            rng = np.random.default_rng(1000 * seed + int(round(1e4 * phi)))
            shapes = [args.kinds[i % len(args.kinds)] for i in range(args.N)]
            made = periodic_config(shapes, phi, rng)
            if made is None:
                print(f"phi {phi}: could not place seed {seed}", flush=True)
                continue
            pos, quats, L = made
            for n, (mode, st) in zip(names, cases):
                acc[n].append(bulk_numbers(periodic_M(op, pos, quats, shapes, L, mode, st), shapes, L, args.acc))
            print(f"phi {phi} seed {seed}  L {L:.2f}  {time.time() - t0:.0f} s", flush=True)
        for n in names:
            if acc[n]:
                rows.append({"phi": phi, "operator": n, "configs": len(acc[n]),
                             **{k: float(np.mean([a[k] for a in acc[n]])) for k in acc[n][0]},
                             **{k + "_sd": float(np.std([a[k] for a in acc[n]])) for k in acc[n][0]}})
    iv = {k: intrinsic_viscosity(k, args.acc) for k in dict.fromkeys(args.kinds)}
    lines = [f"# Bulk suspension in a periodic box: {', '.join(args.kinds)}", "",
             "| phi | operator | settling U / U0 | self-diffusion, translation | rotation | viscosity eta / eta0 | (eta/eta0 - 1) / phi |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['phi']} | {r['operator']} | {r['settling']:.4f} +- {r['settling_sd']:.4f} | {r['D_trans']:.4f} | {r['D_rot']:.4f} | "
                     f"{r['viscosity']:.4f} +- {r['viscosity_sd']:.4f} | {(r['viscosity'] - 1) / r['phi']:.3f} |")
    lines += ["", "## Conditions",
              f"- {args.N} particles per box, {args.seeds} random boxes per volume fraction, random orientations, every pair at contact factor >= 1.05",
              "- periodic cube, no mean flow; far field = 12 periodic Stokeslets per particle (Ewald sum); learned parts added for every pair with images",
              "- settling: mean speed along gravity under equal forces, over the three directions of gravity, / the isolated orientation average",
              "- a box of N particles is not an infinite suspension: settling and translational self-diffusion come out lower by about 1.76 (phi / N)^(1/3) "
              "(Hasimoto; 0.17 at phi 0.02, N 24); the viscosity has no such first-order shift.  Compare trends, or repeat with larger N",
              "- viscosity: force- and torque-free particles in a uniform strain, average over the 5 strains; instantaneous (no Brownian, no contact stress)",
              "- the stresslet blocks have no many-body model: far field (+ the two-body stress model where it says so)",
              f"- dilute limit of (eta/eta0 - 1) / phi = intrinsic viscosity from the {args.acc} cloud: " + ", ".join(f"{k} {v:.4f}" for k, v in iv.items()),
              "- NO truth: MFS is free-space.  Spheres for reference: settling 1 - 6.55 phi (Batchelor), viscosity 1 + 2.5 phi + 5.0 phi^2 (Batchelor & Green)",
              f"- models: pair {args.pair}, nbody {args.nbody}, nself {args.nself}, stress {args.stress}; clouds {args.acc}"]
    os.makedirs(args.results, exist_ok=True)
    stem = os.path.join(args.results, f"BULK_{args.name}")
    open(stem + ".md", "w").write("\n".join(lines) + "\n")
    json.dump(rows, open(stem + ".json", "w"), indent=1)
    print("\n".join(lines))


# ----------------------------------------------------------------------------------------------- settling in time
def _rotate(R: torch.Tensor, w: torch.Tensor, dt: float) -> torch.Tensor:
    """R after turning with angular velocity w (lab) for dt: exp(dt [w]x) R."""
    wn = w.norm(dim=-1).clamp_min(1e-300)
    K = P._skew(w / wn[:, None])
    th = wn * dt
    eye = torch.eye(3, dtype=R.dtype, device=R.device)
    return (eye + torch.sin(th)[:, None, None] * K + (1 - torch.cos(th))[:, None, None] * (K @ K)) @ R


def cmd_streamers(args) -> None:
    """Far-field settling in the periodic box, midpoint steps, with a soft repulsion at small clearance."""
    dev = torch.device(args.device)
    rng = np.random.default_rng(args.seed)
    shapes = [args.kinds[i % len(args.kinds)] for i in range(args.N)]
    pos, quats, L = periodic_config(shapes, args.phi, rng)
    X = torch.as_tensor(pos, device=dev)
    R = torch.as_tensor(quat_to_matrix(quats), device=dev)
    ax = np.stack([axes_of(s) for s in shapes])
    a2 = torch.as_tensor(ax ** 2, device=dev)
    odd = np.abs(ax - np.median(ax, axis=1, keepdims=True)).argmax(1)       # the long axis of a rod, the short axis of a disk
    odd_axis = torch.as_tensor(odd, device=dev)
    amax = torch.as_tensor(ax.max(1), device=dev)
    iso = {s: iso_mobility(s, args.acc) for s in set(shapes)}
    u0 = float(np.mean([np.trace(iso[s][:3, :3]) / 3 for s in shapes])) * P.SIX_PI
    ar = torch.arange(args.N, device=dev)

    def velocity(X, R):
        F = torch.zeros(args.N, 6, dtype=torch.float64, device=dev)
        F[:, 2] = -P.SIX_PI
        d = X[None] - X[:, None]                                            # d[t, s] = x_s - x_t, nearest image
        d = d - L * torch.round(d / L)
        rn = d.norm(dim=-1)
        t, s = torch.nonzero((rn < 1.3 * (amax[:, None] + amax[None])) & (rn > 0), as_tuple=True)
        if len(t):
            A = (R * a2[:, None, :]) @ R.transpose(1, 2)
            g = clearance_torch(A[t], A[s], d[t, s])
            push = P.SIX_PI * args.repel * torch.exp(-g / args.repel_range).clamp_max(50.0)      # on t, away from s
            F[:, :3].index_add_(0, t, -push[:, None] * d[t, s] / rn[t, s][:, None])
        M = periodic_far(torch.remainder(X, L), R, shapes, L, args.acc)
        return (M @ F.reshape(-1)).reshape(args.N, 6)

    rows, traj, t0 = [], [], time.time()
    kk = 2 * math.pi / L * torch.tensor([[1.0, 0, 0], [0, 1.0, 0]], dtype=torch.float64, device=dev)   # waves across gravity
    for k in range(args.steps + 1):
        V = velocity(X, R)
        if k % args.every == 0:
            axis = R[ar, :, odd_axis]
            ph = torch.remainder(X, L) @ kk.T
            sk = float(((torch.cos(ph).sum(0) ** 2 + torch.sin(ph).sum(0) ** 2) / args.N).mean())
            rows.append({"t": k * args.dt, "speed": float(-V[:, 2].mean() / u0), "fluct_z": float(V[:, 2].std() / u0),
                         "fluct_xy": float(V[:, :2].std() / u0), "align": float((1.5 * axis[:, 2] ** 2 - 0.5).mean()), "S_k1": sk})
            traj.append((torch.remainder(X, L).cpu().numpy(), R.cpu().numpy()))
            print(f"t {k * args.dt:7.1f}  speed {rows[-1]['speed']:.3f}  fluct {rows[-1]['fluct_z']:.3f}  align {rows[-1]['align']:+.3f}  "
                  f"S(k1) {sk:.2f}  ({time.time() - t0:.0f} s)", flush=True)
        Vh = velocity(X + 0.5 * args.dt * V[:, :3], _rotate(R, V[:, 3:], 0.5 * args.dt))
        X, R = X + args.dt * Vh[:, :3], _rotate(R, Vh[:, 3:], args.dt)
    lines = [f"# Settling in a periodic box: {args.N} x {', '.join(args.kinds)}, phi {args.phi}", "",
             "| time | mean speed / isolated | fluctuation along gravity | across | alignment with gravity | S(k) at the longest wave across gravity |",
             "|---|---|---|---|---|---|"]
    lines += [f"| {r['t']:.1f} | {r['speed']:.3f} | {r['fluct_z']:.3f} | {r['fluct_xy']:.3f} | {r['align']:+.3f} | {r['S_k1']:.2f} |" for r in rows]
    lines += ["", "## Conditions",
              f"- periodic cube L {L:.2f}, no mean flow, far field only (12 periodic Stokeslets per particle), midpoint steps dt {args.dt}",
              f"- repulsion {args.repel} x weight x exp(-clearance / {args.repel_range}) keeps particles apart (not physical lubrication)",
              "- alignment = mean of (3 cos^2 - 1) / 2 between gravity and the symmetry axis (long axis of a rod, short axis of a disk): 0 random, 1 along gravity",
              "- S(k) = |sum exp(i k x)|^2 / N at k = 2 pi / L across gravity: about 1 for a random suspension, grows when streamers form",
              "- statistics only: no truth at this size; speeds / the isolated orientation-averaged speed, lengths in shortest semi-axes"]
    os.makedirs(args.results, exist_ok=True)
    stem = os.path.join(args.results, f"STREAM_{args.name}_N{args.N}")
    open(stem + ".md", "w").write("\n".join(lines) + "\n")
    json.dump(rows, open(stem + ".json", "w"), indent=1)
    np.savez_compressed(stem + ".npz", X=np.array([a for a, _ in traj]), R=np.array([b for _, b in traj]), shapes=np.array(shapes), L=L,
                        t=np.array([r["t"] for r in rows]))
    print("\n".join(lines[:4] + lines[-8:]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("bulk", "streamers"):
        p = sub.add_parser(name)
        p.add_argument("--kinds", nargs="+", required=True)
        p.add_argument("--N", type=int, default=64)
        p.add_argument("--acc", default="fine")
        p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
        p.add_argument("--results", default="bulk_out")
        p.add_argument("--name", default="run")
    p = sub.choices["bulk"]
    p.add_argument("--phi", type=float, nargs="+", default=[0.01, 0.02, 0.05, 0.1, 0.15])
    p.add_argument("--seeds", type=int, default=5)
    for k in ("pair", "nbody", "nself", "stress"):
        p.add_argument("--" + k, default=None)
    p = sub.choices["streamers"]
    p.add_argument("--phi", type=float, default=0.01)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--dt", type=float, default=0.5)
    p.add_argument("--steps", type=int, default=2000)
    p.add_argument("--every", type=int, default=20)
    p.add_argument("--repel", type=float, default=2.0)
    p.add_argument("--repel-range", type=float, default=0.1)
    args = ap.parse_args()
    {"bulk": cmd_bulk, "streamers": cmd_streamers}[args.cmd](args)


if __name__ == "__main__":
    main()
