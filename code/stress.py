#!/usr/bin/env python3
"""Two-body model for the strain and stresslet blocks (the door to rheology), for any two ellipsoids.

The grand matrix with stress (truth.dense_grand) has, per pair, 11 x 11 blocks: rows [U; Omega; S], columns [F; T; E].
The 6 x 6 corner is the mobility (pair.py).  This model gives the rest, in the same way as pair.py: inside its range
the network IS the block, and it blends into the 12-point far field (farfield.far_blocks11: 0.1-0.3 % at 12 lengths,
several % at 6) across the last unit of the range,   block = (1 - w) far + w network.   (A network for the
difference to the far field was tried first and cannot be trained: near contact the 12 points of the two particles
almost touch and the far field itself blows up, so the difference is a spiky target.)

    cross   velocity of t from a strain on s (U-E 3x5, Omega-E 3x5), stresslet of t from a strain on s (S-E 5x5);
            the stresslet of t from a force / torque on s is NOT learned separately: reciprocity gives it,
            [S-F, S-T]_ts = - [U-E, Omega-E]_st^T
    self    what the presence of s does to t's own blocks: U-E, Omega-E (and by reciprocity S-F, S-T), S-E

One network for every shape (the triaxial inputs, pair.Triaxial.inputs: a particle enters only through its shape
tensor D, so spheres, spheroids and triaxial ellipsoids are the same model).  Outputs are coefficients on analytic
tensors, as in pair.py:

    with z the unit vector t -> s, D_t, D_s, vectors u = z, D_t z, D_s z, D_t D_s z, D_s D_t z, matrices X = I, z z^T,
    D_t, D_s, strain basis e_a (truth.STRAIN_BASIS), and the 7 "strain scalars" s_a = e_a : Y for
    Y = z z^T, D_t, D_s, sym(z u_1), sym(z u_2), sym(u_1 u_2), D_t D_s + D_s D_t:
    U-E      (true, rank 3)     u_p s_a  (35),  X e_a u  for the first three u  (12)                         = 47
    Omega-E  (pseudo, rank 3)   w s_a for w = z x u_1, z x u_2, u_1 x u_2, axial(D_t D_s)  (28),
                                axial(X e_a Y) for the 6 pairs X < Y  (6)                                     = 34
    S-E      (true, rank 4)     s_a s'_b  (49),  tr(e_a X e_b Y)  (16)                                        = 65
The sets are deliberately redundant (the spaces have 15, 15, 25 dimensions at a generic configuration): they must
also span what symmetry allows at special configurations (two spheres: z (z e_a z), e_a z; z x e_a z; three rank-4
terms), and a redundant set costs nothing but a few outputs.

Exact by construction (tests.py): rotation and reflection equivariance, the reciprocity above, a symmetric S-E
(swap average), a symmetric self S-E, continuity into the far field (window, as pair.py: `cut` distance or contact),
Stokes similarity (U-E scales as length, Omega-E as 1, S-E as length^3; lengths in units of the pair length).

    python stress.py data  --shapes prolateSpheroid prolateSpheroid --tag PP --n 8192
    python stress.py train --sets PP --out data/stress/models/stress_pro.pt

data    random pairs as makedata.py pairs (same sampling), one direct solve each with strain columns.
        -> data/stress/pairs/{tag}_{acc}/shard_XXXX.npz
train   targets: cross block - (1 - w) far, and the self correction; L1 loss with each kind of block weighted by 1 / its mean size;
        Adam, cosine, resumable.  Scores (%, Frobenius, validation pairs = seed % 10 == 0): each block of the whole
        11 x 11 cross block against the truth, far field alone -> with the model; the self blocks likewise.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

import pair as P
from farfield import _E5, body_operator11, far_blocks11, rot11, window
from geometry import axes_of, clearance_torch, pair_config, quat_to_matrix

OUT = "data/stress"
N3T, N3P, N4 = 47, 34, 65
KINDS = ("U-E", "W-E", "S-E")
VE, WE, SE = (slice(0, 3), slice(6, 11)), (slice(3, 6), slice(6, 11)), (slice(6, 11), slice(6, 11))
MASK = torch.ones(11, 11)
MASK[:6, :6] = 0.0                      # the mobility corner is not this model's


# ----------------------------------------------------------------------------------------------- tensors
def _axial(M: torch.Tensor) -> torch.Tensor:
    """eps_ijk M_jk on the two indices before the last (..., 3, 3, n) -> (..., 3, n)."""
    return torch.stack([M[..., 1, 2, :] - M[..., 2, 1, :], M[..., 2, 0, :] - M[..., 0, 2, :], M[..., 0, 1, :] - M[..., 1, 0, :]], -2)


def bases(z: torch.Tensor, pt: dict, ps: dict):
    """-> true rank-3 (B, 47, 3, 5), pseudo rank-3 (B, 34, 3, 5), true rank-4 (B, 65, 5, 5)."""
    E5 = torch.tensor(_E5, dtype=z.dtype, device=z.device)
    Dt, Ds = pt["D"], ps["D"]
    mv = lambda M, v: (M @ v[:, :, None])[:, :, 0]
    u = [z, mv(Dt, z), mv(Ds, z), mv(Dt, mv(Ds, z)), mv(Ds, mv(Dt, z))]
    eye = torch.eye(3, dtype=z.dtype, device=z.device).expand(len(z), 3, 3)
    X = [eye, P._outer(z, z), Dt, Ds]
    sym = lambda a, b: 0.5 * (P._outer(a, b) + P._outer(b, a))
    sc = [torch.einsum("aij,bij->ba", E5, Y) for Y in (X[1], Dt, Ds, sym(z, u[1]), sym(z, u[2]), sym(u[1], u[2]), Dt @ Ds + Ds @ Dt)]
    t3 = [v[:, :, None] * s[:, None, :] for v in u for s in sc]
    t3 += [torch.einsum("bij,ajk,bk->bia", M, E5, v) for M in X for v in u[:3]]
    w = [torch.cross(z, u[1], dim=-1), torch.cross(z, u[2], dim=-1), torch.cross(u[1], u[2], dim=-1), _axial((Dt @ Ds)[..., None])[..., 0]]
    p3 = [v[:, :, None] * s[:, None, :] for v in w for s in sc]
    p3 += [_axial(torch.einsum("bij,ajk,bkl->bila", X[i], E5, X[j])) for i in range(4) for j in range(i + 1, 4)]
    t4 = [s[:, :, None] * q[:, None, :] for s in sc for q in sc]
    t4 += [torch.einsum("aij,bjk,ckl,bli->bac", E5, M, E5, Y) for M in X for Y in X]
    return torch.stack(t3, 1), torch.stack(p3, 1), torch.stack(t4, 1)


# ----------------------------------------------------------------------------------------------- the model
class StressModel(nn.Module):
    """forward(d, g, pt, ps) -> the learned cross block and the self correction (what s does to t's own block),
    (B, 11, 11) each, physical units, windowed (x w); the 6 x 6 mobility corner is zero (pair.py owns it).
    The operator's cross block is (1 - w) far + this, with w = weight(d, g, pt, ps)."""

    def __init__(self, r_cut: float | None = None, width: int = 128, taper: float | None = None, cut: str = "distance"):
        super().__init__()
        self.form, self.cut = P.Triaxial, cut
        self.r_cut = float(r_cut or P.CUTS[cut] or self.form.r_cut)
        self.width, self.taper = int(width), float(taper or P.TAPER[cut])
        self.n_coeff = N3T + N3P + N4
        self.mlp = nn.Sequential(nn.Linear(self.form.n_in, width), nn.SiLU(), nn.Linear(width, width), nn.SiLU(),
                                 nn.Linear(width, width), nn.SiLU(), nn.Linear(width, 2 * self.n_coeff))
        self.register_buffer("mu", torch.zeros(self.form.n_in))
        self.register_buffer("sd", torch.ones(self.form.n_in))
        self.register_buffer("scale", torch.ones(6))              # cross U-E, W-E, S-E; self U-E, W-E, S-E

    def decay(self, d, pt, ps):
        """The six pre-scales (B,): point-particle decay x the right power of the pair length."""
        ell = P.pair_length(pt, ps)
        x = ell / d.norm(dim=-1)
        return [ell * x ** 2, x ** 3, ell ** 3 * x ** 3, ell * x ** 4, x ** 5, ell ** 3 * x ** 5]

    def _raw(self, d, g, pt, ps):
        c = self.mlp((self.form.inputs(d, g, pt, ps) - self.mu) / self.sd)
        t3, p3, t4 = bases(d / d.norm(dim=-1, keepdim=True), pt, ps)
        dec = self.decay(d, pt, ps)
        out, k = [], 0
        for head in range(2):
            for j, (B, n) in enumerate(((t3, N3T), (p3, N3P), (t4, N4))):
                f = (self.scale[3 * head + j] * dec[3 * head + j])[:, None, None]
                out.append(torch.einsum("bn,bnij->bij", c[:, k:k + n], B) * f)
                k += n
        return out

    @staticmethod
    def _fill(ue, we, se, ue_r, we_r):
        """An 11 x 11 block from U-E, Omega-E, S-E and the blocks whose transpose gives S-F, S-T."""
        out = torch.zeros(len(ue), 11, 11, dtype=ue.dtype, device=ue.device)
        out[:, :3, 6:], out[:, 3:6, 6:], out[:, 6:, 6:] = ue, we, se
        out[:, 6:, :3], out[:, 6:, 3:6] = -ue_r.transpose(1, 2), -we_r.transpose(1, 2)
        return out

    def forward(self, d, g, pt, ps):
        a, b = self._raw(d, g, pt, ps), self._raw(-d, g, ps, pt)          # the pair, and the same pair seen from the source
        w = self.weight(d, g, pt, ps)[:, None, None]
        cross = self._fill(a[0], a[1], 0.5 * (a[2] + b[2].transpose(1, 2)), b[0], b[1])
        self_ = self._fill(a[3], a[4], 0.5 * (a[5] + a[5].transpose(1, 2)), a[3], a[4])
        return w * cross, w * self_

    def weight(self, d, g, pt, ps) -> torch.Tensor:
        return window(P.reach(self.cut, d, g, pt, ps), self.r_cut, self.taper)

    def config(self) -> dict:
        return {"r_cut": self.r_cut, "width": self.width, "taper": self.taper, "cut": self.cut}


def save_stress(model: StressModel, path: str, extra: dict | None = None) -> None:
    torch.save({"state": model.state_dict(), **model.config(), **(extra or {})}, path)


def load_stress(path: str) -> StressModel:
    ck = torch.load(path, map_location="cpu", weights_only=False)
    m = StressModel(ck["r_cut"], ck["width"], ck["taper"], ck["cut"])
    m.load_state_dict(ck["state"])
    m.report = ck.get("report", {})
    return m.eval()


# ----------------------------------------------------------------------------------------------- data
def gen(args) -> None:
    from truth import dense_grand
    out = Path(args.out) / "pairs" / f"{args.tag}_{args.acc}"
    out.mkdir(parents=True, exist_ok=True)
    import zlib
    seed0 = (zlib.crc32(("stress:" + args.tag).encode()) % 2000) * 1_000_000
    r_max = None if args.r_max is None else args.r_max * math.sqrt(axes_of(args.shapes[0]).min() * axes_of(args.shapes[1]).min())
    t0 = time.time()
    for j in range(args.worker, math.ceil(args.n / args.shard_size), args.num_workers):
        path = out / f"shard_{j:04d}.npz"
        if path.exists():
            continue
        if time.time() - t0 > args.time_budget:
            print(f"time budget reached before shard {j}", flush=True)
            break
        pos, quats, Gs, seeds, ts = [], [], [], [], time.time()
        for k in range(min(args.shard_size, args.n - j * args.shard_size)):
            seed = seed0 + j * args.shard_size + k
            x, q = pair_config(args.shapes, np.random.default_rng(seed), args.cmax, r_max)
            pos.append(x), quats.append(q), seeds.append(seed)
            Gs.append(dense_grand(x, q, args.shapes, args.acc, args.device))
        tmp = path.with_suffix(".tmp.npz")
        np.savez(tmp, positions=np.array(pos), quats=np.array(quats), G=np.array(Gs), seed=np.array(seeds, dtype=np.int64),
                 meta=json.dumps({"shapes": list(args.shapes), "acc": args.acc, "cmax": args.cmax, "r_max": args.r_max}))
        os.replace(tmp, path)
        print(f"shard {j}: {len(pos)} pairs, {time.time() - ts:.0f} s -> {path}", flush=True)


def load_rows(tag: str, acc: str, root: str = OUT, max_configs: int | None = None) -> dict:
    """Both ordered pairs of every stored configuration: d, g, descriptors, far field, truth cross and self blocks
    (11 x 11, physical units), the single-particle block, the seed."""
    files = sorted(glob.glob(f"{root}/pairs/{tag}_{acc}/shard_*.npz"))
    assert files, f"no stress pairs for {tag} ({acc}) under {root}"
    z = [np.load(f) for f in files]
    shapes = json.loads(str(z[0]["meta"]))["shapes"]
    pos, quats, G, seed = (np.concatenate([a[k] for a in z])[:max_configs] for k in ("positions", "quats", "G", "seed"))
    n = len(pos)
    G = torch.as_tensor(G).reshape(n, 2, 11, 2, 11)
    R = torch.as_tensor(quat_to_matrix(quats.reshape(-1, 4))).reshape(n, 2, 3, 3)
    X = torch.as_tensor(pos)
    rows = []
    for t, s in ((0, 1), (1, 0)):
        d = X[:, s] - X[:, t]
        pt, ps = P.describe([shapes[t]] * n, R[:, t]), P.describe([shapes[s]] * n, R[:, s])
        T = rot11(R[:, t])
        single = T @ body_operator11(shapes[t], acc)[3] @ T.transpose(1, 2)
        rows.append({"d": d, "g": clearance_torch(pt["A"], ps["A"], d), "pt": pt, "ps": ps,
                     "far": far_blocks11(shapes[t], shapes[s], d, R[:, t], R[:, s], acc),
                     "cross": G[:, t, :, s, :], "self": G[:, t, :, t, :] - single, "seed": torch.as_tensor(seed)})
    return cat_rows(rows)


def cat_rows(rows: list) -> dict:
    out = {}
    for k in rows[0]:
        out[k] = ({q: torch.cat([r[k][q] for r in rows]) for q in rows[0][k] if all(q in r[k] for r in rows)} if isinstance(rows[0][k], dict)
                  else torch.cat([r[k] for r in rows]))
    return out


def take_rows(rows: dict, m) -> dict:
    return {k: ({q: v[m] for q, v in x.items()} if isinstance(x, dict) else x[m]) for k, x in rows.items()}


def rows_to(rows: dict, dev, dtype=torch.float32) -> dict:
    f = lambda v: v.to(dev, dtype if v.is_floating_point() else v.dtype)
    return {k: ({q: f(v) for q, v in x.items()} if isinstance(x, dict) else f(x)) for k, x in rows.items()}


# ----------------------------------------------------------------------------------------------- training
def rel(a, b) -> float:
    return float(100.0 * (a - b).norm() / b.norm().clamp_min(1e-300))


@torch.no_grad()
def score(model, s: dict) -> dict:
    model.eval()
    c, sf = model(s["d"], s["g"], s["pt"], s["ps"])
    c = c - model.weight(s["d"], s["g"], s["pt"], s["ps"])[:, None, None] * s["far"] * MASK.to(c)      # so that far + c is the operator's block
    out = {"rows": int(len(s["d"]))}
    SF = (slice(6, 11), slice(0, 6))
    for name, (a, b) in (("U-E", VE), ("W-E", WE), ("S-E", SE), ("S-FT", SF)):
        out[name] = rel((s["far"] + c)[:, a, b], s["cross"][:, a, b])
        out["far " + name] = rel(s["far"][:, a, b], s["cross"][:, a, b])
        if name != "S-FT":
            out["self " + name] = rel(sf[:, a, b], s["self"][:, a, b])
    return out


def train(args) -> None:
    torch.manual_seed(args.seed)
    dev = torch.device(args.device)
    model = StressModel(args.r_cut, args.width, cut=args.cut).to(dev)
    sets = {}
    for spec in args.sets:
        tag, _, mx = spec.partition(":")
        rows = load_rows(tag, args.acc, args.data, int(mx) if mx else args.max_configs)
        near = P.reach(args.cut, rows["d"], rows["g"], rows["pt"], rows["ps"]) < model.r_cut
        val = (rows["seed"] % 10) == 0
        sets[tag] = {"train": rows_to(take_rows(rows, near & ~val), dev), "val": rows_to(take_rows(rows, near & val), dev)}
        print(f"  {tag:32} train rows {len(sets[tag]['train']['d']):>8,}  val rows {len(sets[tag]['val']['d']):>7,}", flush=True)
    tr = cat_rows([s["train"] for s in sets.values()])
    n_tr = len(tr["d"])
    with torch.no_grad():
        w = window(P.reach(args.cut, tr["d"], tr["g"], tr["pt"], tr["ps"]), model.r_cut, model.taper)[:, None, None]
        tr["t_cross"], tr["t_self"] = (tr["cross"] - (1.0 - w) * tr["far"]) * MASK.to(dev), tr["self"] * MASK.to(dev)
        x = model.form.inputs(tr["d"], tr["g"], tr["pt"], tr["ps"])
        model.mu.copy_(x.mean(0)), model.sd.copy_(x.std(0).clamp_min(1e-6))
        dec = model.decay(tr["d"], tr["pt"], tr["ps"])
        W = torch.zeros(2, 11, 11, device=dev)
        for h, key in enumerate(("t_cross", "t_self")):
            for j, (a, b) in enumerate((VE, WE, SE)):
                size = tr[key][:, a, b].abs().mean()
                model.scale[3 * h + j] = size / dec[3 * h + j].mean()
                W[h][a, b] = 1.0 / size
                if j < 2:
                    W[h][b, a] = 1.0 / size                                     # the reciprocal block: same weight
    epochs = max(1, math.ceil(args.steps * args.batch / n_tr))
    opt = torch.optim.Adam(model.parameters(), lr=args.lr)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, epochs * math.ceil(n_tr / args.batch))
    ck_path, start, best, best_state, spent = args.out + ".ckpt", 1, float("inf"), None, 0.0
    if os.path.exists(ck_path):
        ck = torch.load(ck_path, map_location=dev, weights_only=False)
        if ck["args"] == vars(args):
            model.load_state_dict(ck["model"]), opt.load_state_dict(ck["opt"]), sched.load_state_dict(ck["sched"])
            start, best, best_state, spent = ck["epoch"] + 1, ck["best"], ck["best_state"], ck["spent"]
            print(f"resumed at epoch {start} (best {best:.4g})", flush=True)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    for ep in range(start, epochs + 1):
        model.train()
        perm = torch.randperm(n_tr, device=dev)
        for i in range(0, n_tr, args.batch):
            b = take_rows(tr, perm[i:i + args.batch])
            c, sf = model(b["d"], b["g"], b["pt"], b["ps"])
            loss = ((c - b["t_cross"]).abs() * W[0]).mean() + ((sf - b["t_self"]).abs() * W[1]).mean()
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step(), sched.step()
        if ep % args.check == 0 or ep == epochs:
            sc = {k: score(model, s["val"]) for k, s in sets.items()}
            val = float(np.mean([v[n] for v in sc.values() for n in ("U-E", "W-E", "S-E", "self S-E")]))
            if val < best:
                best, best_state = val, {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            first = next(iter(sc.values()))
            print(f"epoch {ep:4d}/{epochs}  val {val:.3f} (best {best:.3f})  U-E {first['U-E']:.3f}  W-E {first['W-E']:.3f}  "
                  f"S-E {first['S-E']:.3f}  self S-E {first['self S-E']:.2f}  {spent + time.time() - t0:.0f} s", flush=True)
            torch.save({"model": model.state_dict(), "opt": opt.state_dict(), "sched": sched.state_dict(), "epoch": ep, "best": best,
                        "best_state": best_state, "spent": spent + time.time() - t0, "args": vars(args)}, ck_path + ".tmp")
            os.replace(ck_path + ".tmp", ck_path)
            if spent + time.time() - t0 > args.time_budget and ep < epochs:
                print("time budget reached: run the same command again to continue", flush=True)
                return
    model.load_state_dict(best_state)
    report = {k: score(model, s["val"]) for k, s in sets.items()}
    save_stress(model.cpu(), args.out, {"report": report, "sets": args.sets, "acc": args.acc})
    lines = [f"# Stress model {args.out}", "",
             "Error of each block of the cross block against the truth, % (Frobenius, validation pairs inside the range): far field alone -> with the model.", "",
             "| set | pairs | velocity from strain | rotation from strain | stresslet from strain | stresslet from force / torque | self: U-E | self: W-E | self: S-E |",
             "|---|---|---|---|---|---|---|---|---|"]
    for k, r in report.items():
        lines.append(f"| {k} | {r['rows']} | " + " | ".join(f"{r['far ' + n]:.2f} -> {r[n]:.3f}" for n in ("U-E", "W-E", "S-E", "S-FT"))
                     + " | " + " | ".join(f"{r['self ' + n]:.1f}" for n in KINDS) + " |")
    lines += ["", "## Conditions", f"- truth: {args.acc} clouds, direct solve with strain columns (truth.dense_grand); not symmetrised",
              f"- learned inside {args.cut} {model.r_cut:g}; far field beyond; self columns: error of the learned self correction relative to that correction",
              f"- width {args.width}, {epochs} epochs of batch {args.batch}, lr {args.lr}, {spent + time.time() - t0:.0f} s; no many-body stress model"]
    open(args.out.rsplit(".", 1)[0] + ".md", "w").write("\n".join(lines) + "\n")
    json.dump(report, open(args.out.rsplit(".", 1)[0] + ".json", "w"), indent=1)
    print("\n".join(lines))
    os.remove(ck_path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("data")
    p.add_argument("--shapes", nargs=2, required=True)
    p.add_argument("--tag", required=True)
    p.add_argument("--n", type=int, default=8192)
    p.add_argument("--shard-size", type=int, default=64)
    p.add_argument("--cmax", type=float, default=8.0)
    p.add_argument("--r-max", type=float, default=14.0)
    p.add_argument("--worker", type=int, default=0)
    p.add_argument("--num-workers", type=int, default=1)
    p.add_argument("--time-budget", type=float, default=3.5 * 3600)
    p.add_argument("--out", default=OUT)
    p = sub.add_parser("train")
    p.add_argument("--sets", nargs="+", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--data", default=OUT)
    p.add_argument("--cut", default="distance", choices=list(P.CUTS))
    p.add_argument("--r-cut", type=float, default=None)
    p.add_argument("--width", type=int, default=128)
    p.add_argument("--steps", type=int, default=60000)
    p.add_argument("--batch", type=int, default=512)
    p.add_argument("--lr", type=float, default=2e-3)
    p.add_argument("--check", type=int, default=5)
    p.add_argument("--max-configs", type=int, default=None)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--time-budget", type=float, default=3.5 * 3600)
    for p in sub.choices.values():
        p.add_argument("--acc", default="fine")
        p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = ap.parse_args()
    {"data": gen, "train": train}[args.cmd](args)


if __name__ == "__main__":
    main()
