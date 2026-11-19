#!/usr/bin/env python3
"""A movie of particles settling under gravity: MFS (solid bodies) with one operator drawn over it (wire outlines).
Run from the workspace.  Needs matplotlib; writes .mp4 when ffmpeg is found, otherwise an animated .gif (Pillow).
The trajectories are saved first (.npz next to the movie), so a failed drawing never loses the simulation:
`--render file.npz` draws a movie from saved trajectories without solving anything.

    python movie.py --kinds prolateSpheroid --case pair    --out prolate_pair.mp4
    python movie.py --kinds oblateSpheroid  --case cluster --N 6 --out oblate_cluster.mp4
    python movie.py --kinds prolateSpheroid --case cluster --pair pair.pt --nbody nbody.pt --out prolate_full.mp4

case pair     two particles side by side along x; --tilt gives the angle (degrees) of each long axis from the vertical,
              in the x-z plane.  Default 0 45: one upright, one tilted -- they turn through 90 degrees and circle each
              other.  45 -45 is the two-body dynamics test of evaluate.py (they glide apart, slowly).
     cluster  N particles grown into a loose random cluster (neighbours at contact factor 1 + --delta)
     ring     N particles on a vertical ring (the many-body dynamics test)
The same force (gravity, -z, 6 pi) on every particle, no torque; RK4, the same integrator for every run; a run stops
when a pair reaches contact factor 1.05.  The outlines are the best operator available: far field only (no model
given), + two-body (--pair), + many-body (--pair and --nbody).
The camera FALLS WITH the particles (it follows the MFS centre of mass), so what you see is their motion relative to
each other; the lines are the paths of the centres in that falling frame (coloured = MFS, black = the operator).
A single particle with no neighbour would not turn at all and would glide on a straight slanted line: every turn and
every curved path in the movie is hydrodynamic interaction.
"""
from __future__ import annotations

import argparse
import os
import time

import numpy as np
import torch

from evaluate import SIX_PI, axis_error_deg, operator, run
from geometry import (axes_of, contact_factor, frame_quat, grown_config, min_contact, quat_to_matrix, ring_config,
                      shape_matrix)
from truth import Truth


def surface(shape: str, x, q, nu: int = 22, nv: int = 14):
    """Mesh of one ellipsoid: (3, nu, nv)."""
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, nu), np.linspace(0, np.pi, nv), indexing="ij")
    body = np.stack([np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v)], -1) * axes_of(shape)
    return np.moveaxis(body @ quat_to_matrix(q).T + x, -1, 0)


def pair_start(kinds, contact: float, tilts):
    """Two particles side by side along x at the given contact factor; long axes at tilts[i] degrees from +z towards +x."""
    sh = [kinds[i % len(kinds)] for i in range(2)]
    t = np.radians(tilts)
    q = np.array([frame_quat(sh[i], [np.sin(t[i]), 0.0, np.cos(t[i])], [0.0, 1.0, 0.0]) for i in range(2)])
    R = quat_to_matrix(q)
    d = contact / contact_factor(shape_matrix(sh[0], R[0]), shape_matrix(sh[1], R[1]), np.array([1.0, 0.0, 0.0]))
    return np.array([[-0.5 * d, 0.0, 0.0], [0.5 * d, 0.0, 0.0]]), q, sh


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kinds", nargs="+", default=None)
    ap.add_argument("--render", default=None, help="draw from this saved .npz instead of simulating")
    ap.add_argument("--case", choices=["pair", "cluster", "ring"], default="pair")
    ap.add_argument("--N", type=int, default=6)
    ap.add_argument("--contact", type=float, default=1.3, help="pair / ring: starting contact factor of neighbours")
    ap.add_argument("--tilt", type=float, nargs=2, default=[0.0, 45.0], help="pair: tilt of each long axis from the vertical, degrees")
    ap.add_argument("--delta", type=float, default=0.3, help="cluster: neighbours start at contact factor 1 + delta")
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--dt", type=float, default=0.2)
    ap.add_argument("--steps", type=int, default=500)
    ap.add_argument("--acc", default="medium")
    ap.add_argument("--pair", default=None)
    ap.add_argument("--nbody", default=None)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--fps", type=int, default=15)
    ap.add_argument("--frames", type=int, default=240, help="at most this many frames are drawn (steps are skipped evenly)")
    ap.add_argument("--ffmpeg", default=None, help="path of the ffmpeg executable if it is not on PATH")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if args.render:
        z = np.load(args.render)
        render(args, z["Xt"], z["Qt"], z["Xm"], z["Qm"], [str(x) for x in z["shapes"]], float(z["dt"]), str(z["label"]), str(z["case"]),
               str(z["solid"]) if "solid" in z.files else "MFS")
        return
    assert args.kinds, "--kinds is required"
    if args.case == "pair":
        pos, q, shapes = pair_start(args.kinds, args.contact, args.tilt)
    elif args.case == "ring":
        pos, q, shapes = ring_config(args.kinds, args.N, args.contact)
    else:
        shapes = [args.kinds[i % len(args.kinds)] for i in range(args.N)]
        pos, q = grown_config(shapes, args.delta, np.random.default_rng(args.seed))
    N = len(pos)
    F = np.zeros((N, 6))
    F[:, 2] = -SIX_PI
    op, modes = operator(args)
    mode = modes[-1]
    label = {"far": "far field only", "pair": "far field + two-body model", "full": "far field + two-body + many-body model"}[mode]
    truth = Truth(shapes, args.acc, args.device, warm_start=True)
    t0 = time.time()
    Xt, Qt = run(lambda x, qq: truth.velocities(x, qq, shapes, F), shapes, pos, q, args.dt, args.steps)
    print(f"MFS ({args.acc}): {len(Xt) - 1} steps in {time.time() - t0:.0f} s", flush=True)
    Xm, Qm = run(lambda x, qq: op.apply(x, qq, shapes, F, mode), shapes, pos, q, args.dt, len(Xt) - 1)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    npz = args.out.rsplit(".", 1)[0] + ".npz"
    np.savez_compressed(npz, Xt=Xt, Qt=Qt, Xm=Xm, Qm=Qm, shapes=np.array(shapes), dt=args.dt, label=label, case=args.case)
    n = min(len(Xt), len(Xm)) - 1
    print(f"MFS ran {len(Xt) - 1} steps, the operator {len(Xm) - 1}; at step {n}: position error "
          f"{float(np.linalg.norm(Xm[n] - Xt[n], axis=1).max()):.3f}, axis error "
          f"{float(axis_error_deg(shapes, Qm[n], Qt[n]).max()):.2f} deg -> {npz}", flush=True)
    render(args, Xt, Qt, Xm, Qm, shapes, args.dt, label, args.case)


def render(args, Xt, Qt, Xm, Qm, shapes, dt, label, case, solid="MFS"):
    import shutil
    try:
        import matplotlib
    except ImportError:
        print("matplotlib is not installed here: pip install matplotlib, then  python movie.py --render <the .npz> --out <movie>")
        return
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import animation
    N, n = len(shapes), min(len(Xt), len(Xm))
    ffmpeg = args.ffmpeg or shutil.which("ffmpeg")
    if ffmpeg:
        plt.rcParams["animation.ffmpeg_path"] = ffmpeg
    reach = max(float(axes_of(s).max()) for s in shapes)
    com = Xt[:n].mean(1, keepdims=True)
    Rt, Rm = Xt[:n] - com, Xm[:n] - com                    # paths in the frame that falls with the MFS centre of mass
    half = max(float(np.abs(Rt).max()), float(np.abs(Rm).max())) + reach
    colours = plt.cm.tab10(np.arange(N) % 10)
    fig = plt.figure(figsize=(7.2, 7.6), dpi=110)
    ax = fig.add_subplot(111, projection="3d")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=0.9)

    def draw(k):
        ax.cla()
        c = Xt[k].mean(0)
        for p in range(N):
            ax.plot_surface(*surface(shapes[p], Xt[k, p], Qt[k, p]), color=colours[p], alpha=0.75, linewidth=0, shade=True)
            ax.plot_wireframe(*surface(shapes[p], Xm[k, p], Qm[k, p], 12, 8), color="k", linewidth=0.5, alpha=0.8)
            ax.plot(*(Rt[:k + 1, p] + c).T, color=colours[p], linewidth=1.6)
            ax.plot(*(Rm[:k + 1, p] + c).T, color="k", linewidth=0.7, linestyle="--")
        ax.set_xlim(c[0] - half, c[0] + half), ax.set_ylim(c[1] - half, c[1] + half), ax.set_zlim(c[2] - half, c[2] + half)
        ax.set_box_aspect((1, 1, 1))
        ax.set_xlabel("x"), ax.set_ylabel("y"), ax.set_zlabel("z (gravity is -z; the camera falls with the particles)")
        ax.view_init(elev=14, azim=-62)
        err = float(np.linalg.norm(Xm[k] - Xt[k], axis=1).max())
        fig.suptitle(f"{', '.join(dict.fromkeys(shapes))}: {case}, {N} particles, settling under gravity\n"
                     f"solid = {solid}; black outline = {label}; lines = paths seen from the falling camera\n"
                     f"t = {k * dt:5.1f}   fallen {Xt[0].mean(0)[2] - c[2]:5.1f}   outline off by {err:.2f} (position), "
                     f"{float(axis_error_deg(shapes, Qm[k], Qt[k]).max()):.1f} deg (axis)   closest contact factor "
                     f"{min_contact(shapes, Xt[k], Qt[k]):.2f}", fontsize=9)

    frames = list(range(0, n, max(1, -(-n // args.frames))))
    out = args.out if ffmpeg else args.out.rsplit(".", 1)[0] + ".gif"
    writer = animation.FFMpegWriter(fps=args.fps, bitrate=2400) if ffmpeg else animation.PillowWriter(fps=args.fps)
    animation.FuncAnimation(fig, draw, frames=frames, interval=1000 / args.fps).save(out, writer=writer)
    print(f"{len(frames)} frames -> {out}" + ("" if ffmpeg else "   (no ffmpeg found: wrote a GIF)"))


if __name__ == "__main__":
    main()
