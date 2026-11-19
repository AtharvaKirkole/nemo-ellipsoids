#!/usr/bin/env python3
"""Physics experiments with the force / torque operator, each against MFS where MFS is affordable.
Run from the workspace.  Every experiment writes EXP_<name>.md (numbers + conditions), .json and .npz (trajectories;
`python movie.py --render EXP_<name>.npz --out x.mp4` draws them).

    python experiments.py orbits    --kinds oblateSpheroid --pair pair.pt                   two settling disks: bound or not?
    python experiments.py three     --kinds prolateSpheroid --pair pair.pt --nbody nbody.pt three settling particles: error growth
    python experiments.py cloud     --kinds prolateSpheroid --pair ... --nbody ... --N 200   a settling cloud
    python experiments.py diffusion --kinds prolateSpheroid --pair ... --nbody ... --name pro   short-time self-diffusion vs phi
    python experiments.py spinners  --kinds oblateSpheroid --pair ... --nbody ...            torque-driven ring
    python experiments.py fibre     --kinds prolateSpheroid --pair ... --nbody ...           a flexible chain settling

orbits     Two identical spheroids released side by side, symmetry axes tilted +-theta from the vertical, for a grid of
           separations and tilts.  Each run is classified from the horizontal separation s(t): BOUND (it oscillates),
           SCATTER (it grows without return), CONTACT (they reach contact factor 1.05).  The operator maps the whole
           grid; MFS at every step repeats a few grid points (--truth-n) to check the classification and the orbit.
three      Three particles on a triangle, random orientations.  MFS, MFS started 1e-3 away (how fast the true system
           itself separates: the yardstick for any error), and each operator.  Position error at T/4, T/2, T.
cloud      N particles filling a sphere at volume fraction --phi0, settling.  Operator only above --truth-max
           particles.  Shape of the cloud in time (horizontal and vertical extent), particles left behind, alignment
           of the axes with gravity.  A short-range central repulsion (the same in every run) keeps pairs apart.
diffusion  No time stepping: the short-time self-diffusion (translation and rotation) of particles inside a suspension,
           relative to an isolated particle, from the diagonal blocks of the mobility matrix; MFS from the matrices the
           ceiling test cached (same configurations), so the truth costs nothing if that test has run.
spinners   N spheroids on a horizontal ring, the same torque about the vertical on each, no force: they orbit the ring
           centre through hydrodynamic coupling alone.  Angle turned about the centre in time, each operator against MFS.
fibre      A chain of prolate spheroids joined tip to tip by springs with a bending stiffness, settling broadside.
           Shape (sag of the middle against the ends) in time, each operator against MFS.
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
import torch

from evaluate import (MARGIN, SIX_PI, axis_error_deg, model_conditions, operator, rk4_step, truth_conditions, write)
from geometry import (_place, assign_shapes, axes_of, contact_factor_torch, min_contact, quat_to_matrix, matrix_to_quat,
                      random_quats, shape_matrix, symmetry_axis, is_spheroid, uniform_config, volume)
from truth import Truth

LABEL = {"far": "far field", "pair": "+ two-body", "full": "+ many-body", "mfs": "MFS"}


# ----------------------------------------------------------------------------------------------- shared pieces
def axis_quat(shape: str, n) -> np.ndarray:
    """Quaternion that puts a spheroid's symmetry axis (any ellipsoid's longest axis otherwise) along n."""
    n = np.asarray(n, float) / np.linalg.norm(n)
    i = symmetry_axis(shape) if is_spheroid(shape) else int(np.argmax(axes_of(shape)))
    a = np.cross(n, [0.0, 1.0, 0.0] if abs(n[1]) < 0.9 else [1.0, 0.0, 0.0])
    a /= np.linalg.norm(a)
    R = np.zeros((3, 3))
    R[:, i], R[:, (i + 1) % 3], R[:, (i + 2) % 3] = n, a, np.cross(n, a)
    return matrix_to_quat(R)


def body_axis(shapes, q) -> np.ndarray:
    """(N, 3) lab direction of each particle's symmetry (or longest) axis."""
    R = quat_to_matrix(q)
    return np.stack([R[p][:, symmetry_axis(s) if is_spheroid(s) else int(np.argmax(axes_of(s)))] for p, s in enumerate(shapes)])


def gravity(N: int) -> np.ndarray:
    F = np.zeros((N, 6))
    F[:, 2] = -SIX_PI
    return F


def repulsion(shapes, x, q, c0: float, f0: float) -> np.ndarray:
    """Central pair forces that switch on below contact factor c0: f0 ((c0 - c) / (c0 - 1))^2 along the line of centres.
    A model force, applied identically in every run (MFS and operators), so runs can pass close encounters."""
    N = len(x)
    F = np.zeros((N, 6))
    if f0 <= 0 or N < 2:
        return F
    reach = np.array([axes_of(s).max() for s in shapes])
    i, j = np.triu_indices(N, 1)
    d = x[j] - x[i]
    r = np.linalg.norm(d, axis=1)
    m = r < c0 * (reach[i] + reach[j])
    if not m.any():
        return F
    i, j, d, r = i[m], j[m], d[m], r[m]
    R = quat_to_matrix(q)
    A = torch.as_tensor(np.stack([shape_matrix(s, R[p]) for p, s in enumerate(shapes)]))
    c = contact_factor_torch(A[i], A[j], torch.as_tensor(d)).numpy()
    k = c < c0
    f = (f0 * ((c0 - c[k]) / (c0 - 1.0)) ** 2)[:, None] * d[k] / r[k, None]
    np.add.at(F[:, :3], i[k], -f)
    np.add.at(F[:, :3], j[k], f)
    return F


def sim(vel, shapes, pos, q, dt, steps, load, floor=1.0 + MARGIN):
    """RK4 with a load that may depend on the state.  vel(x, q, F) -> (N, 6).  Stops at contact factor `floor`."""
    X, Q = [pos], [q]
    f = lambda x, qq: vel(x, qq, load(x, qq))
    for _ in range(steps):
        x, qq = rk4_step(f, X[-1], Q[-1], dt)
        if not np.isfinite(x).all():
            break
        X.append(x), Q.append(qq)
        if len(x) > 1 and min_contact(shapes, x, qq) < floor:
            break
    return np.array(X), np.array(Q)


def runners(args, shapes):
    """{name: vel(x, q, F)} for each operator available, and the MFS one (None when args.truth is off)."""
    op, modes = operator(args)
    out = {m: (lambda x, q, F, m=m: op.apply(x, q, shapes, F, m)) for m in modes}
    truth = None
    if args.truth:
        T = Truth(shapes, args.acc, args.device, warm_start=True)
        truth = lambda x, q, F: T.velocities(x, q, shapes, F)
    return out, truth, modes


def conditions(args, shapes, what: str, extra: list) -> tuple:
    mlines, mcond = model_conditions(args)
    tlines, tcond = truth_conditions(args, shapes, what)
    return ["", "## Conditions", ""] + mlines + extra + tlines, {"models": mcond, "truth": tcond}


def save_tracks(path: Path, Xt, Qt, Xm, Qm, shapes, dt, label, case, solid="MFS") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path, Xt=Xt, Qt=Qt, Xm=Xm, Qm=Qm, shapes=np.array(shapes), dt=dt, label=label, case=case, solid=solid)


def compare(shapes, X, Q, Xt, Qt, k) -> dict:
    k = min(k, len(X) - 1, len(Xt) - 1)
    return {"step": k, "pos": float(np.linalg.norm(X[k] - Xt[k], axis=1).max()),
            "axis": float(axis_error_deg(shapes, Q[k], Qt[k]).max())}


# ----------------------------------------------------------------------------------------------- 1. two settling disks
def classify(s: np.ndarray, stopped: bool) -> tuple:
    """From the horizontal separation in time: outcome and, when it oscillates, the number of turning points."""
    if stopped:
        return "CONTACT", 0
    ds = np.diff(s)
    turns = int(np.sum(ds[1:] * ds[:-1] < 0))
    if turns >= 3 and s.max() < 3.0 * s[0] + 1.0:
        return "BOUND", turns
    if s[-1] > 2.0 * s[0] and ds[-max(3, len(ds) // 10):].min() > 0:
        return "SCATTER", turns
    return "UNDECIDED", turns


def exp_orbits(args) -> None:
    shape = args.kinds[0]
    sh = [shape, shape]
    args.truth = True
    run, truth, modes = runners(args, sh)
    mode = modes[-1] if modes[-1] != "full" else "pair"            # two particles: the many-body terms are zero anyway
    amax = float(axes_of(shape).max())
    seps = [amax * f for f in args.sep]
    grid, tracks = {}, {}
    F0 = gravity(2)
    load = lambda x, q: F0
    t0 = time.time()
    for s0 in seps:
        for th in args.tilt:
            t = np.radians(th)
            pos = np.array([[-0.5 * s0, 0.0, 0.0], [0.5 * s0, 0.0, 0.0]])
            q = np.array([axis_quat(shape, [np.sin(t), 0.0, np.cos(t)]), axis_quat(shape, [-np.sin(t), 0.0, np.cos(t)])])
            if min_contact(sh, pos, q) < 1.1:
                grid[(s0, th)] = ("TOO CLOSE", 0, 0, 0.0)
                continue
            X, Q = sim(run[mode], sh, pos, q, args.dt, args.steps, load)
            s = np.linalg.norm((X[:, 1] - X[:, 0])[:, :2], axis=1)
            out, turns = classify(s, len(X) - 1 < args.steps)
            grid[(s0, th)] = (out, turns, len(X) - 1, float(s.max() / s[0]))
            tracks[(s0, th)] = (pos, q, X, Q, s)
        print(f"separation {s0:.2f}: " + "  ".join(f"{th:g}:{grid[(s0, th)][0]}" for th in args.tilt) + f"  [{time.time() - t0:.0f} s]", flush=True)
    lines = [f"# Two settling {shape}s: bound orbit or not", "",
             f"Operator: {LABEL[mode]}.  Rows = starting centre separation (in longest semi-axes: {args.sep}); columns = tilt of "
             "the symmetry axes from the vertical, +theta and -theta (degrees).  Entry: outcome, turning points of the "
             "horizontal separation, largest separation / starting separation.", "",
             "| separation | " + " | ".join(f"tilt {th:g}" for th in args.tilt) + " |", "|---|" + "---|" * len(args.tilt)]
    for s0 in seps:
        lines.append(f"| {s0:.2f} | " + " | ".join(f"{g[0]}, {g[1]}, {g[3]:.2f}" for g in (grid[(s0, th)] for th in args.tilt)) + " |")
    # MFS on a few grid points, spread over the outcomes found
    keys = [k for k in tracks]
    by = {}
    for k in keys:
        by.setdefault(grid[k][0], []).append(k)
    pick = [v[len(v) // 2] for v in by.values()][:args.truth_n]
    pick += [k for k in keys if k not in pick][:max(0, args.truth_n - len(pick))]
    lines += ["", "## The same runs with MFS at every step", "",
              "| separation | tilt | operator: outcome, turning points | MFS: outcome, turning points | steps compared | "
              "position error at the end | axis error, deg | separation error, % of the separation |", "|---|---|---|---|---|---|---|---|"]
    res, first = {}, None
    for k in pick:
        pos, q, X, Q, s = tracks[k]
        Xt, Qt = sim(truth, sh, pos, q, args.dt, args.steps, load)
        st = np.linalg.norm((Xt[:, 1] - Xt[:, 0])[:, :2], axis=1)
        ot, tt = classify(st, len(Xt) - 1 < args.steps)
        n = min(len(X), len(Xt)) - 1
        e = compare(sh, X, Q, Xt, Qt, n)
        res[f"{k[0]:.2f}|{k[1]:g}"] = {"operator": grid[k][0], "mfs": ot, **e, "sep_pct": float(100 * abs(s[n] - st[n]) / st[n])}
        lines.append(f"| {k[0]:.2f} | {k[1]:g} | {grid[k][0]}, {grid[k][1]} | {ot}, {tt} | {n} | {e['pos']:.3f} | {e['axis']:.2f} | "
                     f"{100 * abs(s[n] - st[n]) / st[n]:.2f} |")
        print(lines[-1], flush=True)
        if first is None:
            first = (Xt, Qt, X, Q)
    cond, cj = conditions(args, sh, "one direct solve of the two particles at each RK4 stage.", [
        f"- **Start**: two {shape}s at the same height, centres {args.sep} longest semi-axes apart along x, symmetry axes in the "
        f"x-z plane at +theta and -theta from the vertical, theta in {args.tilt} degrees.",
        f"- **Motion**: the same force (gravity, -z, 6 pi) on both, no torque; RK4, dt {args.dt:g}, {args.steps} steps "
        f"(time {args.dt * args.steps:g}); a run stops at contact factor {1 + MARGIN:g}.",
        "- **Outcome**: from the horizontal separation s(t).  BOUND: at least 3 turning points and s never above 3 s(0) + 1.  "
        "SCATTER: s ends above 2 s(0) and is still growing.  CONTACT: the run stopped.  UNDECIDED: none of these within the time."])
    name = f"EXP_orbits_{args.name or shape}"
    if first is not None:
        save_tracks(Path(args.results) / f"{name}.npz", *first, sh, args.dt, LABEL[mode], "orbits")
    write(Path(args.results) / name, lines + cond,
          {"grid": {f"{k[0]:.2f}|{k[1]:g}": dict(outcome=v[0], turns=v[1], steps=v[2], smax=v[3]) for k, v in grid.items()},
           "truth": res, "conditions": cj})


# ----------------------------------------------------------------------------------------------- 2. three particles
def exp_three(args) -> None:
    rng = np.random.default_rng(args.seed)
    sh = [args.kinds[i % len(args.kinds)] for i in range(3)]
    a = max(float(axes_of(s).max()) for s in sh)
    L = args.side * a
    jitter = rng.normal(size=(3, 3)) * 0.05 * a
    q = random_quats(rng, 3)
    for k in range(2000):                     # new orientations; every 200 tries the triangle grows by 5 % (oblates need it)
        pos = np.array([[0.0, 0.0, 0.0], [L, 0.0, 0.0], [0.5 * L, 0.866 * L, 0.0]]) + jitter
        if min_contact(sh, pos, q) > 1.3:
            break
        q = random_quats(rng, 3)
        if k % 200 == 199:
            L *= 1.05
    else:
        raise RuntimeError("could not place three particles at contact factor > 1.3")
    args.side = L / a
    args.truth = True
    run, truth, modes = runners(args, sh)
    F0 = gravity(3)
    load = lambda x, qq: F0
    Xt, Qt = sim(truth, sh, pos, q, args.dt, args.steps, load)
    Xp, Qp = sim(truth, sh, pos + rng.normal(size=(3, 3)) * 1e-3, q, args.dt, len(Xt) - 1, load)
    T = len(Xt) - 1
    marks = [T // 4, T // 2, T]
    fell = float(Xt[0].mean(0)[2] - Xt[-1].mean(0)[2])
    lines = [f"# Three settling particles ({', '.join(sh)}): how errors grow", "",
             f"MFS ran {T} steps (time {T * args.dt:g}), fell {fell:.1f}.  Largest particle position error against MFS at a "
             "quarter, half and the end of the run (lengths), and the axis error at the end (degrees).  The first row is MFS "
             "itself started 0.001 away: any error below it cannot be told from the system's own sensitivity.", "",
             "| run | steps | error at T/4 | at T/2 | at T | axis error at T, deg |", "|---|---|---|---|---|---|"]
    out = {"steps": T, "fell": fell}
    rows = [("MFS started 0.001 away", Xp, Qp)] + [(LABEL[m], *sim(run[m], sh, pos, q, args.dt, T, load)) for m in modes]
    best = None
    for name, X, Q in rows:
        e = [compare(sh, X, Q, Xt, Qt, k) for k in marks]
        out[name] = {"steps": len(X) - 1, "errors": e}
        lines.append(f"| {name} | {len(X) - 1} | {e[0]['pos']:.4f} | {e[1]['pos']:.4f} | {e[2]['pos']:.4f} | {e[2]['axis']:.2f} |")
        best = (X, Q)
    cond, cj = conditions(args, sh, "one direct solve of the three particles at each RK4 stage.", [
        f"- **Start**: three particles on a horizontal triangle of side {args.side:g} longest semi-axes (each centre moved "
        f"by a random 5 % of that), random orientations (seed {args.seed}), every pair at contact factor above 1.3.",
        f"- **Motion**: gravity (-z, 6 pi) on each, no torque; RK4, dt {args.dt:g}, up to {args.steps} steps; stops at contact "
        f"factor {1 + MARGIN:g}."])
    name = f"EXP_three_{args.name or '_'.join(dict.fromkeys(sh))}"
    save_tracks(Path(args.results) / f"{name}.npz", Xt, Qt, *best, sh, args.dt, LABEL[modes[-1]], "three")
    write(Path(args.results) / name, lines + cond, dict(out, conditions=cj))


# ----------------------------------------------------------------------------------------------- 3. settling cloud
def sphere_cloud(shapes, phi0: float, rng, gap: float = 1.3):
    Rc = (sum(volume(s) for s in shapes) / (phi0 * 4.0 / 3.0 * np.pi)) ** (1.0 / 3.0)

    def propose(i, pos, A_list, A):
        while True:
            x = rng.uniform(-Rc, Rc, 3)
            if x @ x < Rc * Rc:
                return x, -1
    made = _place(list(shapes), rng, propose, gap)
    return made, Rc


def cloud_stats(shapes, X, Q, Rc) -> dict:
    c = X.mean(0)
    rel = X - c
    ax = body_axis(shapes, Q)
    return {"z": float(c[2]), "horizontal": float(np.sqrt((rel[:, :2] ** 2).sum(1).mean())), "vertical": float(np.sqrt((rel[:, 2] ** 2).mean())),
            "left_behind": float(np.mean(rel[:, 2] > 1.5 * Rc)), "alignment": float(np.mean(1.5 * ax[:, 2] ** 2 - 0.5))}


def exp_cloud(args) -> None:
    rng = np.random.default_rng(args.seed)
    sh = assign_shapes(args.kinds, args.N, rng)
    made, Rc = sphere_cloud(sh, args.phi0, rng)
    assert made is not None, "could not fill the sphere: lower --phi0"
    pos, q = made
    args.truth = args.N <= args.truth_max
    run, truth, modes = runners(args, sh)
    U0 = args.N * SIX_PI / (5.0 * np.pi * Rc)                       # Hadamard-Rybczynski speed of a drop of the same force
    dt = args.dt if args.dt > 0 else 0.02 * Rc / U0
    F0 = gravity(args.N)
    load = lambda x, qq: F0 + repulsion(sh, x, qq, args.c0, args.f0 * SIX_PI)
    marks = [0, args.steps // 4, args.steps // 2, args.steps]
    lines = [f"# A settling cloud of {args.N} particles ({', '.join(args.kinds)})", "",
             f"Start: a sphere of radius {Rc:.1f} at volume fraction {args.phi0:g}.  A drop of the same total force and radius "
             f"would fall at U0 = {U0:.2f}; time is in units of Rc / U0 (dt = {dt * U0 / Rc:.3f} of it).  Per run and time: distance "
             "fallen / Rc; horizontal and vertical root-mean-square extent / the starting value; share of particles left behind "
             "(more than 1.5 Rc above the centre); alignment of the axes with gravity (1 = all vertical, 0 = random, "
             "-0.5 = all horizontal).", "",
             "| run | time, Rc/U0 | fallen / Rc | horizontal | vertical | left behind | alignment |", "|---|---|---|---|---|---|---|"]
    out, tracks = {"Rc": Rc, "U0": U0, "dt": dt}, {}
    todo = ([("mfs", truth)] if truth else []) + [(m, run[m]) for m in modes]
    for name, vel in todo:
        t0 = time.time()
        X, Q = sim(vel, sh, pos, q, dt, args.steps, load, floor=1.0 + 0.4 * MARGIN)
        tracks[name] = (X, Q)
        s0 = cloud_stats(sh, X[0], Q[0], Rc)
        out[name] = {"steps": len(X) - 1, "seconds": round(time.time() - t0, 1), "marks": []}
        for k in marks:
            k = min(k, len(X) - 1)
            s = cloud_stats(sh, X[k], Q[k], Rc)
            out[name]["marks"].append(dict(s, step=k))
            lines.append(f"| {LABEL[name]} | {k * dt * U0 / Rc:.2f} | {(s0['z'] - s['z']) / Rc:.2f} | {s['horizontal'] / s0['horizontal']:.3f} | "
                         f"{s['vertical'] / s0['vertical']:.3f} | {s['left_behind']:.3f} | {s['alignment']:.3f} |")
        print(f"{name}: {len(X) - 1} steps in {time.time() - t0:.0f} s", flush=True)
    if truth:
        lines += ["", "## Against MFS, particle by particle", "", "| run | steps compared | largest position error / Rc | largest axis error, deg |",
                  "|---|---|---|---|"]
        Xt, Qt = tracks["mfs"]
        for m in modes:
            e = compare(sh, *tracks[m], Xt, Qt, len(Xt) - 1)
            out[m]["vs_mfs"] = e
            lines.append(f"| {LABEL[m]} | {e['step']} | {e['pos'] / Rc:.4f} | {e['axis']:.2f} |")
    cond, cj = conditions(args, sh, "the whole cloud at each RK4 stage (iterative solver)." if truth else
                          f"NOT run: {args.N} particles is above --truth-max {args.truth_max}.", [
        f"- **Start**: {args.N} particles, shapes {', '.join(args.kinds)} in equal numbers, centres uniform in a sphere at volume "
        f"fraction {args.phi0:g}, random orientations, every pair at contact factor >= 1.3 (seed {args.seed}).",
        f"- **Forces**: gravity (-z, 6 pi) on each; plus a central pair repulsion below contact factor {args.c0:g}, "
        f"{args.f0:g} x 6 pi x ((c0 - c) / (c0 - 1))^2, the same in every run.  RK4, {args.steps} steps; a run stops if a pair "
        f"still reaches contact factor {1 + 0.4 * MARGIN:g}."])
    name = f"EXP_cloud_{args.name or '_'.join(args.kinds)}_N{args.N}"
    X, Q = tracks[modes[-1]]
    Xt, Qt = tracks.get("mfs", (X, Q))
    save_tracks(Path(args.results) / f"{name}.npz", Xt, Qt, X, Q, sh, dt, LABEL[modes[-1]], "cloud", "MFS" if truth else LABEL[modes[-1]])
    write(Path(args.results) / name, lines + cond, dict(out, conditions=cj))


# ----------------------------------------------------------------------------------------------- 4. short-time diffusion
def exp_diffusion(args) -> None:
    op, modes = operator(args)
    name = args.name or "_".join(args.kinds)
    cache = Path(args.data) / "truth_cache" / f"ceiling_{name}_{args.acc}"
    truth = Truth(args.kinds, args.acc, args.device) if args.truth else None
    acc = {}
    for phi in args.phi:
        for seed in range(args.seeds):
            rng = np.random.default_rng([20261111, int(round(phi * 1e6)), args.N, seed])      # the ceiling test's configurations
            shapes = assign_shapes(args.kinds, args.N, rng)
            made = uniform_config(shapes, phi, rng)
            if made is None:
                continue
            pos, q = made
            N = len(pos)
            Lbox = (sum(volume(s) for s in shapes) / phi) ** (1.0 / 3.0)
            inner = np.abs(pos).max(1) < 0.25 * Lbox                 # particles in the middle of the box
            if inner.sum() < 2:
                inner = np.argsort(np.abs(pos).max(1))[:max(2, N // 8)]
            Ms = {m: op.grand_M(pos, q, shapes, m).cpu().numpy() for m in modes}
            f = cache / f"M_phi{phi:g}_N{N}_s{seed}.npz"
            if f.exists() and np.allclose(np.load(f)["pos"], pos):
                Ms["mfs"] = np.load(f)["M"]
            elif truth is not None:
                try:
                    Ms["mfs"] = truth.mobility(pos, q, shapes)
                    cache.mkdir(parents=True, exist_ok=True)
                    np.savez_compressed(f, pos=pos, q=q, M=Ms["mfs"])
                except Exception as e:                                # noqa: BLE001
                    print(f"phi {phi} seed {seed}: MFS failed ({str(e)[:80]})", flush=True)
            for m, M in Ms.items():
                B = M.reshape(N, 6, N, 6)
                tt, rr = [], []
                for p in np.flatnonzero(inner) if inner.dtype == bool else inner:
                    i0 = op.grand_M(pos[p:p + 1], q[p:p + 1], [shapes[p]], "far").cpu().numpy()
                    tt.append(np.trace(B[p, :3, p, :3]) / np.trace(i0[:3, :3]))
                    rr.append(np.trace(B[p, 3:, p, 3:]) / np.trace(i0[3:, 3:]))
                acc.setdefault((phi, m), []).append((np.mean(tt), np.mean(rr), len(tt)))
            print(f"phi {phi:g} seed {seed}: " + "  ".join(f"{m} {acc[(phi, m)][-1][0]:.4f}" for m in Ms), flush=True)
    cols = [m for m in ("mfs", "far", "pair", "full") if any(k[1] == m for k in acc)]
    lines = [f"# Short-time self-diffusion in suspensions of {', '.join(args.kinds)}", "",
             "D / D0 = (trace of a particle's own translation block) / (the same for the particle alone), averaged over the "
             "particles in the middle of the box; and the same for rotation.  Below 1: neighbours slow a particle down.", "",
             "| phi | particles averaged | " + " | ".join(f"{LABEL[m]}: translation / rotation" for m in cols) + " |",
             "|---|---|" + "---|" * len(cols)]
    out = {}
    for phi in args.phi:
        cells, n = [], 0
        for m in cols:
            v = acc.get((phi, m))
            if not v:
                cells.append("not available")
                continue
            t, r, n = float(np.mean([x[0] for x in v])), float(np.mean([x[1] for x in v])), int(sum(x[2] for x in v))
            out[f"{phi:g}|{m}"] = {"translation": t, "rotation": r, "particles": n, "configs": len(v)}
            cells.append(f"{t:.4f} / {r:.4f}")
        lines.append(f"| {phi:g} | {n} | " + " | ".join(cells) + " |")
    cond, cj = conditions(args, args.kinds, "the whole mobility matrix of each configuration (read from the ceiling test's cache when "
                          "it is there).", [
        f"- **Configurations**: N = {args.N}, shapes {', '.join(args.kinds)} in equal numbers, uniform in a cube at phi in {args.phi}, "
        f"random orientations, contact factor >= {1 + MARGIN:g}; {args.seeds} per phi.  A finite cloud in unbounded fluid: only "
        "particles within a quarter of the box side of the centre are averaged, to stay away from the edge.",
        "- **What it is not**: the hindered settling speed.  That needs a periodic box (zero mean flow); in a finite cloud the "
        "settling speed grows with the size of the cloud."])
    write(Path(args.results) / f"EXP_diffusion_{name}", lines + cond, dict(out, conditions=cj))


# ----------------------------------------------------------------------------------------------- 5. torque-driven ring
def exp_spinners(args) -> None:
    shape = args.kinds[0]
    sh = [args.kinds[i % len(args.kinds)] for i in range(args.N)]
    th = 2 * np.pi * np.arange(args.N) / args.N
    amax = max(float(axes_of(s).max()) for s in sh)
    rad = args.spacing * 2 * amax / (2 * np.sin(np.pi / args.N))
    pos = rad * np.stack([np.cos(th), np.sin(th), np.zeros(args.N)], 1)
    q = np.array([axis_quat(s, [0.0, 0.0, 1.0]) for s in sh])
    assert min_contact(sh, pos, q) > 1.1, "ring too tight: raise --spacing"
    args.truth = True
    run, truth, modes = runners(args, sh)
    F0 = np.zeros((args.N, 6))
    F0[:, 5] = args.torque * 8 * np.pi
    load = lambda x, qq: F0
    Xt, Qt = sim(truth, sh, pos, q, args.dt, args.steps, load)
    T = len(Xt) - 1

    def turned(X):                                                   # mean angle of the particles about the ring centre, unwrapped
        c = X.mean(1, keepdims=True)
        ang = np.unwrap(np.arctan2(X[:, :, 1] - c[:, :, 1], X[:, :, 0] - c[:, :, 0]), axis=0)
        return (ang - ang[0]).mean(1)
    at = turned(Xt)
    lines = [f"# {args.N} {shape}s on a ring, the same vertical torque on each", "",
             f"No force on any particle: all motion of the centres is hydrodynamic coupling.  MFS: {T} steps (time {T * args.dt:g}); "
             f"the ring turned {np.degrees(at[-1]):.2f} degrees about its centre and its radius changed by "
             f"{100 * (np.linalg.norm(Xt[-1, 0, :2] - Xt[-1].mean(0)[:2]) / rad - 1):.2f} %.", "",
             "| run | steps | ring angle turned, deg | error in it, % | largest position error |", "|---|---|---|---|---|"]
    out = {"steps": T, "mfs_angle_deg": float(np.degrees(at[-1]))}
    best = None
    for m in modes:
        X, Q = sim(run[m], sh, pos, q, args.dt, T, load)
        n = min(len(X), len(Xt)) - 1
        a = turned(X)
        e = compare(sh, X, Q, Xt, Qt, n)
        out[m] = {"steps": len(X) - 1, "angle_deg": float(np.degrees(a[n])), "angle_err_pct": float(100 * abs(a[n] - at[n]) / max(abs(at[n]), 1e-12)), **e}
        lines.append(f"| {LABEL[m]} | {len(X) - 1} | {np.degrees(a[n]):.2f} | {out[m]['angle_err_pct']:.2f} | {e['pos']:.4f} |")
        best = (X, Q)
    cond, cj = conditions(args, sh, "one solve of the ring at each RK4 stage.", [
        f"- **Start**: {args.N} particles on a horizontal ring, neighbours {args.spacing:g} x (two longest semi-axes) apart, symmetry "
        "axes vertical.",
        f"- **Loads**: torque {args.torque:g} x 8 pi about +z on every particle, no force.  RK4, dt {args.dt:g}, {args.steps} steps."])
    name = f"EXP_spinners_{args.name or shape}"
    save_tracks(Path(args.results) / f"{name}.npz", Xt, Qt, *best, sh, args.dt, LABEL[modes[-1]], "spinners")
    write(Path(args.results) / name, lines + cond, dict(out, conditions=cj))


# ----------------------------------------------------------------------------------------------- 6. flexible fibre
def exp_fibre(args) -> None:
    shape = args.kinds[0]
    n = args.N
    sh = [shape] * n
    a = float(axes_of(shape).max())
    step = 2 * a * args.spacing
    pos = np.stack([(np.arange(n) - 0.5 * (n - 1)) * step, np.zeros(n), np.zeros(n)], 1)
    q = np.array([axis_quat(shape, [1.0, 0.0, 0.0])] * n)
    rest = step - 2 * a
    ks, kb = args.spring * SIX_PI, args.bend * SIX_PI

    def load(x, qq):
        F = gravity(n)
        ax = body_axis(sh, qq)
        for i in range(n - 1):
            ai, aj = ax[i], ax[i + 1]
            if ai @ aj < 0:                                           # an axis is a line: keep neighbours pointing the same way
                aj = -aj
            pi, pj = x[i] + a * ai, x[i + 1] - a * aj                 # facing tips
            d = pj - pi
            L = np.linalg.norm(d)
            f = ks * (L - rest) * d / max(L, 1e-12)                   # spring between the tips
            F[i, :3] += f
            F[i + 1, :3] -= f
            F[i, 3:] += np.cross(a * ai, f)
            F[i + 1, 3:] += np.cross(-a * aj, -f)
            tb = kb * np.cross(ai, aj)                                # bending: turns the two axes towards each other
            F[i, 3:] += tb
            F[i + 1, 3:] -= tb
        return F
    args.truth = True
    run, truth, modes = runners(args, sh)
    Xt, Qt = sim(truth, sh, pos, q, args.dt, args.steps, load, floor=1.0 + 0.4 * MARGIN)
    T = len(Xt) - 1
    sag = lambda X: float(0.5 * (X[0, 2] + X[-1, 2]) - X[len(X) // 2, 2])       # ends above the middle
    lines = [f"# A flexible chain of {n} {shape}s settling broadside", "",
             f"MFS: {T} steps (time {T * args.dt:g}), fell {Xt[0].mean(0)[2] - Xt[-1].mean(0)[2]:.1f}; the middle ended "
             f"{sag(Xt[-1]):.3f} below the ends (chain length {step * (n - 1) + 2 * a:.1f}).", "",
             "| run | steps | sag of the middle | error in it, % | largest position error | largest axis error, deg |", "|---|---|---|---|---|---|"]
    out = {"steps": T, "mfs_sag": sag(Xt[-1])}
    best = None
    for m in modes:
        X, Q = sim(run[m], sh, pos, q, args.dt, T, load, floor=1.0 + 0.4 * MARGIN)
        k = min(len(X), len(Xt)) - 1
        e = compare(sh, X, Q, Xt, Qt, k)
        out[m] = {"steps": len(X) - 1, "sag": sag(X[k]), "sag_err_pct": float(100 * abs(sag(X[k]) - sag(Xt[k])) / max(abs(sag(Xt[k])), 1e-12)), **e}
        lines.append(f"| {LABEL[m]} | {len(X) - 1} | {sag(X[k]):.3f} | {out[m]['sag_err_pct']:.2f} | {e['pos']:.4f} | {e['axis']:.2f} |")
        best = (X, Q)
    cond, cj = conditions(args, sh, "one solve of the chain at each RK4 stage.", [
        f"- **Start**: {n} particles in a horizontal line along x, long axes along x, centres {args.spacing:g} x (two long "
        "semi-axes) apart.",
        f"- **Forces**: gravity (-z, 6 pi) on each; a spring of stiffness {args.spring:g} x 6 pi between facing tips (rest length = "
        f"the starting gap {rest:.2f}); a bending torque {args.bend:g} x 6 pi x (a_i x a_j) between neighbours.  RK4, dt {args.dt:g}, "
        f"{args.steps} steps."])
    name = f"EXP_fibre_{args.name or shape}"
    save_tracks(Path(args.results) / f"{name}.npz", Xt, Qt, *best, sh, args.dt, LABEL[modes[-1]], "fibre")
    write(Path(args.results) / name, lines + cond, dict(out, conditions=cj))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--kinds", nargs="+", required=True)
    common.add_argument("--pair", default=None)
    common.add_argument("--nbody", default=None)
    common.add_argument("--nself", default=None)
    common.add_argument("--data", default="data/final")
    common.add_argument("--acc", default="fine")
    common.add_argument("--ref-acc", default=None)
    common.add_argument("--results", default="experiments_out")
    common.add_argument("--name", default=None)
    common.add_argument("--seed", type=int, default=0)
    common.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    a = sub.add_parser("orbits", parents=[common])
    a.add_argument("--sep", type=float, nargs="+", default=[1.5, 2.0, 2.5, 3.0, 4.0, 5.0], help="starting separations, in longest semi-axes")
    a.add_argument("--tilt", type=float, nargs="+", default=[0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0])
    a.add_argument("--dt", type=float, default=0.25)
    a.add_argument("--steps", type=int, default=2400)
    a.add_argument("--truth-n", type=int, default=4)
    a = sub.add_parser("three", parents=[common])
    a.add_argument("--side", type=float, default=1.6)
    a.add_argument("--dt", type=float, default=0.1)
    a.add_argument("--steps", type=int, default=1500)
    a = sub.add_parser("cloud", parents=[common])
    a.add_argument("--N", type=int, default=200)
    a.add_argument("--phi0", type=float, default=0.1)
    a.add_argument("--dt", type=float, default=0.0, help="0: 0.02 Rc / U0")
    a.add_argument("--steps", type=int, default=400)
    a.add_argument("--truth-max", type=int, default=0, help="run MFS too when N is at most this")
    a.add_argument("--c0", type=float, default=1.3)
    a.add_argument("--f0", type=float, default=4.0)
    a = sub.add_parser("diffusion", parents=[common])
    a.add_argument("--N", type=int, default=64)
    a.add_argument("--phi", type=float, nargs="+", default=[0.05, 0.1, 0.2])
    a.add_argument("--seeds", type=int, default=3)
    a.add_argument("--truth", action="store_true", help="solve MFS for configurations that are not in the ceiling test's cache")
    a = sub.add_parser("spinners", parents=[common])
    a.add_argument("--N", type=int, default=6)
    a.add_argument("--spacing", type=float, default=1.4)
    a.add_argument("--torque", type=float, default=1.0)
    a.add_argument("--dt", type=float, default=0.2)
    a.add_argument("--steps", type=int, default=600)
    a = sub.add_parser("fibre", parents=[common])
    a.add_argument("--N", type=int, default=5)
    a.add_argument("--spacing", type=float, default=1.2)
    a.add_argument("--spring", type=float, default=10.0)
    a.add_argument("--bend", type=float, default=5.0)
    a.add_argument("--dt", type=float, default=0.02)
    a.add_argument("--steps", type=int, default=1200)
    args = ap.parse_args()
    if not hasattr(args, "truth"):
        args.truth = False
    {"orbits": exp_orbits, "three": exp_three, "cloud": exp_cloud, "diffusion": exp_diffusion, "spinners": exp_spinners,
     "fibre": exp_fibre}[args.cmd](args)


if __name__ == "__main__":
    main()
