#!/usr/bin/env python3
"""A movie of particles settling under gravity: MFS (solid bodies) with the trained operator drawn over it (wire
outlines), seen from three sides at once -- looking along x, along y and along z (from above) -- in one frame.
Run from the workspace.  Needs matplotlib; writes .mp4 when ffmpeg is found, otherwise an animated .gif (Pillow).

    python movie.py --shapes prolateSpheroid oblateSpheroid --case pair --tilt 0 45 --pair pair.pt --out pair.mp4
    python movie.py --shapes prolate_ar4 --N 8 --case cluster --pair pair.pt --nbody nbody.pt --nself nself.pt --out c.mp4
    python movie.py --render c.npz --out c.mp4                    draw again from saved trajectories (no solve)

Particles.  --shapes gives them one by one (a cluster cycles through the list up to --N); --kinds is the old name of
the same option.
case pair     two particles side by side at the same height, along the horizontal diagonal e = (x + y) / sqrt 2 (so
              that every view shows both), at contact factor --contact.  --tilt gives, per particle, the angle
              (degrees, in the vertical plane through e) between the vertical and its symmetry axis (spheroids: the
              long axis of a rod, the short axis of a disk) or its longest axis (triaxial ellipsoids).  0 45: one
              upright, one tilted.
     cluster  --N particles grown into a compact random cluster, neighbours at contact factor 1 + --delta.
     ring     --N particles on a vertical ring (the many-body dynamics test).
Motion.  The same force (gravity, -z, 6 pi) on every particle, no torque; RK4, the same integrator for every run; a
run stops when a pair reaches contact factor 1.05.  MFS runs first, for at most --time-budget seconds (then the movie
is as long as MFS got); the operator then runs the same number of steps.  The trajectories are saved (.npz next to
the movie) BEFORE drawing, so a failed drawing never loses the simulation.
Operator (outlines).  The best one given: far field only (no model), + two-body (--pair), + many-body (--pair, --nbody
and, if given, --nself).  It is positive definite (psd.py), as everywhere.
Camera.  It falls with the particles (it follows the MFS centre of mass), so each view shows the motion relative to
each other; the lines are the paths of the centres in that falling frame (coloured = MFS, dashed black = operator).
The three views are orthographic: what you see is the true projection of the bodies on that plane.  In the view along
z, gravity points into the screen.
"""
from __future__ import annotations

import argparse
import os
import time

import numpy as np
import torch

from evaluate import SIX_PI, axis_error_deg, operator, rk4_step
from geometry import (MARGIN, SHAPES, axes_of, contact_factor, frame_quat, grown_config, is_spheroid, min_contact,
                      quat_to_matrix, ring_config, shape_matrix, symmetry_axis)
from truth import Truth

VIEWS = {   # name: (elevation, azimuth, title, the axis pointing at the viewer)
    "x": (0.0, 0.0, "looking along x  (y to the right, z up)", "x"),
    "y": (0.0, -90.0, "looking along y  (x to the right, z up)", "y"),
    "z": (90.0, -90.0, "looking along z, from above  (x to the right, y up)", "z"),
}


def surface(shape: str, x, q, nu: int = 22, nv: int = 14):
    """Mesh of one ellipsoid: (3, nu, nv)."""
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, nu), np.linspace(0, np.pi, nv), indexing="ij")
    body = np.stack([np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v)], -1) * axes_of(shape)
    return np.moveaxis(body @ quat_to_matrix(q).T + x, -1, 0)


PAIR_DIR = np.array([1.0, 1.0, 0.0]) / np.sqrt(2.0)      # the pair's line of centres: seen apart in every view


def tilted_quat(shape: str, tilt_deg: float, e=PAIR_DIR) -> np.ndarray:
    """Orientation whose characteristic axis -- symmetry axis of a spheroid, longest axis otherwise -- is at tilt_deg
    from the vertical, in the vertical plane through the horizontal direction e (tilted towards +e)."""
    t = np.radians(tilt_deg)
    zhat = np.array([0.0, 0.0, 1.0])
    d = np.sin(t) * e + np.cos(t) * zhat
    perp = np.cos(t) * e - np.sin(t) * zhat
    side = np.cross(zhat, e)
    ax = axes_of(shape)
    if is_spheroid(shape) and ax[symmetry_axis(shape)] < np.median(ax):      # a disk: its short axis along d
        return frame_quat(shape, perp, side)
    return frame_quat(shape, d, side)                                        # a rod or a triaxial body: long axis along d


def pair_start(shapes, contact: float, tilts):
    """Two particles at the same height along PAIR_DIR at the given contact factor, tilted as tilted_quat."""
    q = np.array([tilted_quat(shapes[i], tilts[i]) for i in range(2)])
    R = quat_to_matrix(q)
    d = contact / contact_factor(shape_matrix(shapes[0], R[0]), shape_matrix(shapes[1], R[1]), PAIR_DIR)
    return np.array([-0.5 * d * PAIR_DIR, 0.5 * d * PAIR_DIR]), q


def integrate(velocity, shapes, pos, q, dt, steps, budget=None):
    """RK4 until `steps`, contact factor 1.05, or `budget` seconds -> X (n+1, N, 3), Q (n+1, N, 4), why it stopped."""
    X, Q, t0, why = [pos], [q], time.time(), "steps"
    for _ in range(steps):
        x, qq = rk4_step(velocity, X[-1], Q[-1], dt)
        X.append(x), Q.append(qq)
        if min_contact(shapes, x, qq) < 1.0 + MARGIN:
            why = "contact"
            break
        if budget is not None and time.time() - t0 > budget:
            why = "time budget"
            break
    return np.array(X), np.array(Q), why


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shapes", "--kinds", dest="shapes", nargs="+", default=None)
    ap.add_argument("--render", default=None, help="draw from this saved .npz instead of simulating")
    ap.add_argument("--case", choices=["pair", "cluster", "ring"], default="pair")
    ap.add_argument("--N", type=int, default=8)
    ap.add_argument("--contact", type=float, default=1.3, help="pair / ring: starting contact factor of neighbours")
    ap.add_argument("--tilt", type=float, nargs=2, default=[0.0, 45.0], help="pair: tilt of each particle's axis, degrees")
    ap.add_argument("--delta", type=float, default=0.3, help="cluster: neighbours start at contact factor 1 + delta")
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--dt", type=float, default=0.1)
    ap.add_argument("--steps", type=int, default=1000)
    ap.add_argument("--time-budget", type=float, default=None, help="seconds of MFS integration at most (then stop)")
    ap.add_argument("--acc", default="fine")
    ap.add_argument("--pair", default=None)
    ap.add_argument("--nbody", default=None)
    ap.add_argument("--nself", default=None)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--title", default=None, help="first line of the movie's heading")
    ap.add_argument("--views", default="xyz", help="which views, in order (any of x, y, z)")
    ap.add_argument("--fps", type=int, default=15)
    ap.add_argument("--frames", type=int, default=240, help="at most this many frames are drawn (steps are skipped evenly)")
    ap.add_argument("--still", type=float, default=None, help="also save one frame as PNG, at this fraction of the run (0-1)")
    ap.add_argument("--ffmpeg", default=None, help="path of the ffmpeg executable if it is not on PATH")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if args.render:
        z = np.load(args.render)
        get = lambda k, d: str(z[k]) if k in z.files else d
        if "axes" in z.files:                    # the shapes travel with the trajectories: drawing needs no workspace
            for s, ax in zip(z["shapes"], z["axes"]):
                SHAPES.setdefault(str(s), tuple(float(a) for a in ax))
        render(args, z["Xt"], z["Qt"], z["Xm"], z["Qm"], [str(x) for x in z["shapes"]], float(z["dt"]), get("label", "operator"),
               get("case", ""), get("solid", "MFS"), args.title or get("title", ""), get("stopped", ""))
        return
    assert args.shapes, "--shapes is required"
    if args.case == "pair":
        shapes = [args.shapes[i % len(args.shapes)] for i in range(2)]
        pos, q = pair_start(shapes, args.contact, args.tilt)
    elif args.case == "ring":
        shapes = [args.shapes[i % len(args.shapes)] for i in range(args.N)]
        pos, q, shapes = ring_config(shapes, args.N, args.contact)
    else:
        shapes = [args.shapes[i % len(args.shapes)] for i in range(args.N)]
        made = grown_config(shapes, args.delta, np.random.default_rng(args.seed))
        assert made is not None, "could not grow the cluster: try another --seed or a larger --delta"
        pos, q = made
    N = len(pos)
    F = np.zeros((N, 6))
    F[:, 2] = -SIX_PI
    op, modes = operator(args)
    mode = modes[-1]
    label = {"far": "far field only", "pair": "far field + two-body model",
             "full": "far field + two-body + many-body model" + (" (+ self model)" if args.nself else "")}[mode]
    truth = Truth(shapes, args.acc, args.device, warm_start=True)
    t0 = time.time()
    Xt, Qt, why = integrate(lambda x, qq: truth.velocities(x, qq, shapes, F), shapes, pos, q, args.dt, args.steps, args.time_budget)
    print(f"MFS ({args.acc}): {len(Xt) - 1} steps in {time.time() - t0:.0f} s, stopped by: {why}", flush=True)
    Xm, Qm, _ = integrate(lambda x, qq: op.apply(x, qq, shapes, F, mode), shapes, pos, q, args.dt, len(Xt) - 1)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    npz = args.out.rsplit(".", 1)[0] + ".npz"
    np.savez_compressed(npz, Xt=Xt, Qt=Qt, Xm=Xm, Qm=Qm, shapes=np.array(shapes), axes=np.array([axes_of(s) for s in shapes]),
                        dt=args.dt, label=label, case=args.case,
                        title=args.title or "", stopped=why, pair=str(args.pair), nbody=str(args.nbody), nself=str(args.nself))
    n = min(len(Xt), len(Xm)) - 1
    print(f"MFS ran {len(Xt) - 1} steps, the operator {len(Xm) - 1}; at step {n}: position error "
          f"{float(np.linalg.norm(Xm[n] - Xt[n], axis=1).max()):.3f}, axis error "
          f"{float(axis_error_deg(shapes, Qm[n], Qt[n]).max()):.2f} deg -> {npz}", flush=True)
    render(args, Xt, Qt, Xm, Qm, shapes, args.dt, label, args.case, "MFS", args.title or "", why)


def render(args, Xt, Qt, Xm, Qm, shapes, dt, label, case, solid="MFS", title="", stopped=""):
    import shutil
    try:
        import matplotlib
    except ImportError:
        print("matplotlib is not installed here: pip install matplotlib, then  python movie.py --render <the .npz> --out <movie>")
        return
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import animation
    views = [v for v in args.views if v in VIEWS] or list("xyz")
    N, n = len(shapes), min(len(Xt), len(Xm))
    ffmpeg = args.ffmpeg or shutil.which("ffmpeg")
    if ffmpeg:
        plt.rcParams["animation.ffmpeg_path"] = ffmpeg
    reach = max(float(axes_of(s).max()) for s in shapes)
    com = Xt[:n].mean(1, keepdims=True)
    Rt, Rm = Xt[:n] - com, Xm[:n] - com                    # paths in the frame that falls with the MFS centre of mass
    half = max(float(np.abs(Rt).max()), float(np.abs(Rm).max())) + reach
    colours = plt.cm.tab10(np.arange(N) % 10)
    kinds = list(dict.fromkeys(shapes))
    what = ", ".join(f"{shapes.count(k)} x {k} ({':'.join(f'{a:g}' for a in axes_of(k))})" for k in kinds)
    fig = plt.figure(figsize=(5.4 * len(views), 6.4), dpi=100)
    axs = [fig.add_subplot(1, len(views), i + 1, projection="3d") for i in range(len(views))]
    fig.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=0.86, wspace=0.0)

    def draw(k):
        c = Xt[k].mean(0)
        err = float(np.linalg.norm(Xm[k] - Xt[k], axis=1).max())
        cmin = min_contact(shapes, Xt[k], Qt[k])
        closest = f"{cmin:.2f}" if np.isfinite(cmin) else "> 8 (far apart)"
        mesh_t = [surface(shapes[p], Xt[k, p], Qt[k, p]) for p in range(N)]
        mesh_m = [surface(shapes[p], Xm[k, p], Qm[k, p], 12, 8) for p in range(N)]
        for ax, v in zip(axs, views):
            ax.cla()
            elev, azim, vtitle, depth = VIEWS[v]
            for p in range(N):
                ax.plot_surface(*mesh_t[p], color=colours[p], alpha=0.75, linewidth=0, shade=True)
                ax.plot_wireframe(*mesh_m[p], color="k", linewidth=0.45, alpha=0.8)
                ax.plot(*(Rt[:k + 1, p] + c).T, color=colours[p], linewidth=1.5)
                ax.plot(*(Rm[:k + 1, p] + c).T, color="k", linewidth=0.7, linestyle="--")
            ax.set_xlim(c[0] - half, c[0] + half), ax.set_ylim(c[1] - half, c[1] + half), ax.set_zlim(c[2] - half, c[2] + half)
            try:
                ax.set_box_aspect((1, 1, 1), zoom=1.3)        # matplotlib >= 3.6
            except TypeError:
                ax.set_box_aspect((1, 1, 1))
            ax.set_proj_type("ortho")
            ax.view_init(elev=elev, azim=azim)
            for a in "xyz":                                   # the axis pointing at the viewer carries no information
                getattr(ax, f"set_{a}ticks")([] if a == depth else getattr(ax, f"get_{a}ticks")())
                getattr(ax, f"set_{a}label")("" if a == depth else a)
            ax.tick_params(labelsize=6)
            ax.set_title(vtitle, fontsize=10, pad=-6)
        fig.suptitle((f"{title}\n" if title else "") +
                     f"{what}: {case}, settling under gravity (-z)\n"
                     f"solid = {solid}; black outline = {label}; lines = paths seen from the falling camera\n"
                     f"t = {k * dt:6.1f}   fallen {Xt[0].mean(0)[2] - c[2]:6.1f}   outline off by {err:.3f} (position), "
                     f"{float(axis_error_deg(shapes, Qm[k], Qt[k]).max()):.2f} deg (axis)   closest contact factor "
                     f"{closest}" + (f"   [run stopped by: {stopped}]" if stopped and k == n - 1 else ""),
                     fontsize=9)

    frames = list(range(0, n, max(1, -(-n // args.frames))))
    if frames[-1] != n - 1:
        frames.append(n - 1)
    if args.still is not None:
        draw(frames[min(len(frames) - 1, int(args.still * (len(frames) - 1)))])
        png = args.out.rsplit(".", 1)[0] + ".png"
        fig.savefig(png)
        print(f"still -> {png}")
    out = args.out if ffmpeg else args.out.rsplit(".", 1)[0] + ".gif"
    writer = animation.FFMpegWriter(fps=args.fps, bitrate=3600) if ffmpeg else animation.PillowWriter(fps=args.fps)
    animation.FuncAnimation(fig, draw, frames=frames, interval=1000 / args.fps).save(out, writer=writer)
    print(f"{len(frames)} frames, views {' '.join(views)} -> {out}" + ("" if ffmpeg else "   (no ffmpeg found: wrote a GIF)"))


if __name__ == "__main__":
    main()
