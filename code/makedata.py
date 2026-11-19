#!/usr/bin/env python3
"""Training and test data: MFS grand mobility matrices of pairs and clusters, and the rows the networks train on.

    python makedata.py pairs    --shapes prolateSpheroid prolateSpheroid --tag PP --n 16384 --r-max 12
    python makedata.py clusters --kinds prolateSpheroid --tag P
    python makedata.py nbody-rows --clusters P --pair-model data/final/models/pair_A.pt --tag P

Run from the workspace (the directory that holds data/points); everything is written under data/final there.

pairs       two particles (shapes[0], shapes[1]); random orientations and direction; contact factor c with c - 1
            log-uniform in [0.05, cmax - 1]; pairs beyond --r-max (the pair model's range, in units of the pair
            length sqrt(l_t l_s)) are redrawn, not solved.
            One direct MFS solve each.  -> {out}/pairs/{tag}_{acc}/shard_XXXX.npz
clusters    whole configurations for the many-body model: uniform boxes (phi 2.5-20 %, P 16 / 32), grown compact
            clusters (contact factor 1.05-1.5, P 8-24), aligned boxes, and LARGE uniform boxes (phi 10-20 %, P 64 / 96:
            a pair deep inside has the full neighbourhood of a bulk suspension, which a 32-particle box never shows;
            the old models degraded from N 100 to 200+ in Fig. 4); shapes drawn from --kinds in equal numbers.
            -> {out}/clusters/{tag}_{acc}/item*_part*.npz
self-rows   every particle of every cluster with the many-body remainder of its SELF block,
            R = M_tt - [M_iso + the pair model's self corrections], and its neighbourhood.  -> {out}/self_rows/{tag}_{acc}.npz
nbody-rows  every near ordered pair of every cluster with its many-body residual R = M_ts - two-body block (the label
            of f_nb, through the SAME code as the operator) and its neighbourhood.  -> {out}/nbody_rows/{tag}_{acc}.npz

Labels are made reciprocal before use: MFS on finite clouds gives M_st = M_ts^T only to 3e-4 near contact (1e-2 for
the worst shapes), the networks are reciprocal exactly, so the antisymmetric part is label noise no model can fit.
Every block is read from 1/2 (M + M^T); the raw block is kept next to it ("raw"), so the size of what was removed
(the reciprocity defect of the truth) is reported with every accuracy number.

Every configuration has its own seed (seed0 + index), so a second run with another --acc (Xfine) re-solves exactly the
same configurations: that difference is the label floor.  seed % 10 == 0 is the validation split, by configuration.
Shards already on disk are skipped and no shard is started after --time-budget seconds, so a job can be resubmitted.
"""
from __future__ import annotations

import argparse
import glob
import itertools
import json
import math
import os
import time
import zlib
from pathlib import Path

import numpy as np
import torch

import pair as P
from farfield import far_blocks
from geometry import (assign_shapes, axes_of, clearance_torch, grown_config, pair_config, quat_to_matrix, rotate_block,
                      uniform_config)
from truth import Truth, dense_mobility, iso_mobility

OUT = "data/final"
PLANS = {
    "default": {"uniform": {"phi": [0.025, 0.05, 0.1, 0.15, 0.2], "P": [16, 32]},
                "large": {"phi": [0.1, 0.15, 0.2], "P": [64, 96]},
                "grown": {"delta": [0.05, 0.1, 0.2, 0.5], "P": [8, 12, 16, 24]},
                "aligned": {"phi": [0.05, 0.1], "P": [16, 32]}},
    "smoke": {"uniform": {"phi": [0.05, 0.15], "P": [6]}, "grown": {"delta": [0.1], "P": [5]}, "large": {"phi": [0.1], "P": [10]}},
}
FAMILIES = ["uniform", "grown", "aligned", "large"]
LARGE_SHARE = 3          # "large" = uniform boxes of 64 / 96 particles: 1 / LARGE_SHARE as many configurations each


def seed0_of(tag: str) -> int:
    """A reproducible seed block per data set, so different tags never share configurations."""
    return (zlib.crc32(tag.encode()) % 2000) * 1_000_000


def _save(path: Path, **arrays) -> None:
    tmp = path.with_suffix(".tmp.npz")
    np.savez(tmp, **arrays)
    os.replace(tmp, path)


# ----------------------------------------------------------------------------------------------- generation
def gen_pairs(args) -> None:
    out = Path(args.out) / "pairs" / f"{args.tag}_{args.acc}"
    out.mkdir(parents=True, exist_ok=True)
    seed0 = seed0_of(args.tag) if args.seed0 is None else args.seed0
    r_max = None if args.r_max is None else args.r_max * math.sqrt(axes_of(args.shapes[0]).min() * axes_of(args.shapes[1]).min())
    t0 = time.time()
    for j in range(args.worker, math.ceil(args.n / args.shard_size), args.num_workers):
        path = out / f"shard_{j:04d}.npz"
        if path.exists():
            continue
        if time.time() - t0 > args.time_budget:
            print(f"time budget reached before shard {j}", flush=True)
            break
        pos, quats, Ms, seeds, ts = [], [], [], [], time.time()
        for k in range(min(args.shard_size, args.n - j * args.shard_size)):
            seed = seed0 + j * args.shard_size + k
            x, q = pair_config(args.shapes, np.random.default_rng(seed), args.cmax, r_max)
            pos.append(x), quats.append(q), seeds.append(seed)
            Ms.append(dense_mobility(x, q, args.shapes, args.acc, args.device))
        meta = {"shapes": list(args.shapes), "acc": args.acc, "cmax": args.cmax, "r_max": args.r_max,
                "seconds": round(time.time() - ts, 1)}
        _save(path, positions=np.array(pos), quats=np.array(quats), M=np.array(Ms),
              seed=np.array(seeds, dtype=np.int64), meta=json.dumps(meta))
        print(f"shard {j}: {len(pos)} pairs, {meta['seconds']:.0f} s -> {path}", flush=True)


def gen_clusters(args) -> None:
    out = Path(args.out) / "clusters" / f"{args.tag}_{args.acc}"
    out.mkdir(parents=True, exist_ok=True)
    seed0 = seed0_of("clusters:" + args.tag) if args.seed0 is None else args.seed0
    truth = Truth(args.kinds, args.acc, args.device)
    items = []
    for family, spec in PLANS[args.plan].items():
        keys = [k for k in spec if k != "P"]
        for combo in itertools.product(*[spec[k] for k in keys]):
            items += [(family, dict(zip(keys, combo)), int(n)) for n in spec["P"]]
    t0 = time.time()
    per_of = lambda i: max(2, args.per // LARGE_SHARE) if items[i][0] == "large" else args.per
    size_of = lambda i: 1 if items[i][0] == "large" else args.shard_size        # a large box is minutes of MFS: one per file
    parts = [(i, j) for i in range(len(items)) for j in range(math.ceil(per_of(i) / size_of(i)))]
    for i, j in parts[args.worker::args.num_workers]:
        family, prm, n = items[i]
        path = out / f"item{i:03d}_part{j:03d}.npz"
        if path.exists():
            continue
        if time.time() - t0 > args.time_budget:
            print(f"time budget reached before item {i} part {j}", flush=True)
            break
        pos, quats, Ms, seeds, shapes, ts = [], [], [], [], [], time.time()
        for k in range(j * size_of(i), min((j + 1) * size_of(i), per_of(i))):
            seed = seed0 + 100_000 * i + k
            rng = np.random.default_rng(seed)
            # B (multi-shape): every cluster is ONE shape, drawn from the kinds; C / D: the kinds mixed in each cluster
            sh = [args.kinds[int(rng.integers(len(args.kinds)))]] * n if args.one_kind else assign_shapes(args.kinds, n, rng)
            made = (grown_config(sh, prm["delta"], rng) if family == "grown"
                    else uniform_config(sh, prm["phi"], rng, aligned=family == "aligned"))        # "large" = uniform
            if made is None:
                continue
            try:
                M = truth.mobility(made[0], made[1], sh)
            except Exception as e:                                      # noqa: BLE001  (a bad solve is skipped, not stored)
                print(f"  seed {seed}: MFS failed, skipped ({str(e)[:120]})", flush=True)
                continue
            pos.append(made[0]), quats.append(made[1]), seeds.append(seed), shapes.append(sh)
            Ms.append(M)
        meta = {"family": family, "params": prm, "P": n, "kinds": list(args.kinds), "acc": args.acc,
                "seconds": round(time.time() - ts, 1)}
        _save(path, positions=np.array(pos), quats=np.array(quats), M=np.array(Ms), seed=np.array(seeds, dtype=np.int64),
              shapes=np.array(shapes), meta=json.dumps(meta))
        print(f"{family} {prm} P {n} part {j}: {len(pos)} configurations, {meta['seconds']:.0f} s -> {path}", flush=True)


# ----------------------------------------------------------------------------------------------- pair rows
def take_rows(rows: dict, idx) -> dict:
    return {k: ({a: b[idx] for a, b in v.items()} if isinstance(v, dict) else v[idx]) for k, v in rows.items()}


def cat_rows(parts: list) -> dict:
    return {k: ({a: torch.cat([p[k][a] for p in parts]) for a in parts[0][k]} if isinstance(parts[0][k], dict)
                else torch.cat([p[k] for p in parts])) for k in parts[0]}


def rows_to(rows: dict, device, dtype=torch.float32) -> dict:
    f = lambda v: v.to(device=device, dtype=dtype if v.is_floating_point() else v.dtype)
    return {k: ({a: f(b) for a, b in v.items()} if isinstance(v, dict) else f(v)) for k, v in rows.items()}


def load_pair_rows(tag: str, acc: str = "fine", root: str = OUT, max_configs: int | None = None) -> dict:
    """Both ordered pairs of every stored configuration of one pair set, float64 on the CPU:
    d, g (clearance), c (contact factor), ell (pair length), pt / ps (particle descriptors), cross = M_ts,
    self = M_tt - M_iso (both from the symmetrised M), raw = M_ts as MFS gave it (not symmetrised), far (the
    12-Stokeslet far field of the same pair), seed."""
    files = sorted(glob.glob(f"{root}/pairs/{tag}_{acc}/shard_*.npz"))
    assert files, f"no pair data {root}/pairs/{tag}_{acc}: python makedata.py pairs --tag {tag} ..."
    parts, n_done = [], 0
    for f in files:
        z = np.load(f)
        shapes = json.loads(str(z["meta"]))["shapes"]
        pos, q, M, seed = z["positions"], z["quats"], z["M"], z["seed"]
        if max_configs is not None:
            keep = max(0, min(len(pos), max_configs - n_done))
            pos, q, M, seed = pos[:keep], q[:keep], M[:keep], seed[:keep]
        n = len(pos)
        if n == 0:
            break
        n_done += n
        Rn = quat_to_matrix(q)                                                   # (n, 2, 3, 3)
        R = torch.as_tensor(Rn.reshape(2 * n, 3, 3))
        desc = P.describe([shapes[0], shapes[1]] * n, R)
        Mb = (0.5 * (M + M.transpose(0, 2, 1))).reshape(n, 2, 6, 2, 6)        # reciprocal labels
        Mraw = M.reshape(n, 2, 6, 2, 6)
        for t, s in ((0, 1), (1, 0)):
            it, is_ = torch.arange(n) * 2 + t, torch.arange(n) * 2 + s
            d = torch.as_tensor(pos[:, s] - pos[:, t])
            g = clearance_torch(desc["A"][it], desc["A"][is_], d)
            r = d.norm(dim=-1)
            keys = [k for k in P.KEYS if k in desc]
            pt, ps = {k: desc[k][it] for k in keys}, {k: desc[k][is_] for k in keys}
            parts.append({"d": d, "g": g, "c": r / (r - g), "ell": P.pair_length(pt, ps), "pt": pt, "ps": ps,
                          "cross": torch.as_tensor(Mb[:, t, :, s, :].copy()), "raw": torch.as_tensor(Mraw[:, t, :, s, :].copy()),
                          "self": torch.as_tensor(Mb[:, t, :, t, :] - rotate_block(iso_mobility(shapes[t], acc), Rn[:, t])),
                          "far": far_blocks(shapes[t], shapes[s], d, R[it], R[is_]),
                          "seed": torch.as_tensor(seed.astype(np.int64))})
    return cat_rows(parts)


# ----------------------------------------------------------------------------------------------- many-body rows
def iter_clusters(tag: str, acc: str = "fine", root: str = OUT):
    """Yields (positions (P, 3), quats (P, 4), shapes [P], M (6P, 6P), meta dict with family / params / seed)."""
    files = sorted(glob.glob(f"{root}/clusters/{tag}_{acc}/item*_part*.npz"))
    assert files, f"no cluster data {root}/clusters/{tag}_{acc}: python makedata.py clusters --tag {tag} ..."
    for f in files:
        z = np.load(f)
        meta = json.loads(str(z["meta"]))
        for i in range(len(z["positions"])):
            yield (z["positions"][i].astype(np.float64), z["quats"][i].astype(np.float64), [str(x) for x in z["shapes"][i]],
                   z["M"][i].astype(np.float64), dict(meta, seed=int(z["seed"][i])))


def build_nbody_rows(args) -> None:
    from mobility import Operator
    from nbody import neighbours, to6
    op = Operator(P.load_pair(args.pair_model), acc=args.acc, device=args.device, psd=False)   # labels: the RAW sum
    rc = op.pair.form.r_cut                                 # f_nb's ranges are distances (pair lengths) for either kind of cut
    pc, nc = args.pair_cutoff or rc, args.neighbor_cutoff or rc
    if op.pair.cut == "distance":
        pc = min(pc, op.pair.r_cut)
    parts, cfgs, t0 = [], [], time.time()
    for pos, q, shapes, M, meta in iter_clusters(args.clusters, args.acc, args.out):
        X, R, desc, kinds, kid = op.geometry(pos, q, shapes)
        n = len(X)
        L = P.length(desc)
        D = (X[:, None] - X[None]).norm(dim=-1) / (L[:, None] * L[None]).sqrt()          # in units of each pair's length
        t, s = torch.nonzero((D < pc) & ~torch.eye(n, dtype=torch.bool, device=X.device), as_tuple=True)
        if len(t) == 0:
            continue
        cross, _, g = op.two_body(X, R, desc, kinds, kid, t, s)
        Mb = torch.as_tensor(0.5 * (M + M.T), dtype=torch.float64, device=X.device).reshape(n, 6, n, 6)   # reciprocal labels
        nbr, nD, mask, nz = neighbours(X, desc["D"], 0.5 * (X[t] + X[s]), torch.stack([t, s], 1), nc * (L[t] * L[s]).sqrt(), desc["z"])
        row = {"d": X[s] - X[t], "g": g, "R": ((Mb[t, :, s, :] - cross) * P.SIX_PI).reshape(-1, 36),
               "P2": (cross * P.SIX_PI).reshape(-1, 36), "nbr": nbr, "nbr_D": to6(nD), "mask": mask, "nbr_z": nz,
               "cfg": torch.full((len(t),), len(cfgs), dtype=torch.int64)}
        keys = [k for k in P.KEYS if k in desc]
        row.update({f"pt.{k}": desc[k][t] for k in keys})
        row.update({f"ps.{k}": desc[k][s] for k in keys})
        parts.append({k: v.cpu().numpy() for k, v in row.items()})
        prm = meta["params"]
        cfgs.append({"family": FAMILIES.index(meta["family"]), "phi": prm.get("phi", np.nan), "P": n,
                     "seed": meta["seed"], "is_val": meta["seed"] % 10 == 0})
        if len(cfgs) % 100 == 0:
            print(f"  {len(cfgs)} configurations, {sum(len(p['d']) for p in parts):,} rows [{time.time() - t0:.0f} s]", flush=True)
    assert parts, "no near pairs found"
    K = max(p["nbr"].shape[1] for p in parts)
    for p in parts:
        for k in ("nbr", "nbr_D", "mask", "nbr_z"):
            if p[k].shape[1] < K:
                full = np.zeros((p[k].shape[0], K) + p[k].shape[2:], dtype=p[k].dtype)
                full[:, :p[k].shape[1]] = p[k]
                p[k] = full
    cat = {k: np.concatenate([p[k] for p in parts], 0) for k in parts[0]}
    rows = {k: (v.astype(np.float32) if v.dtype == np.float64 else v) for k, v in cat.items()}
    meta = {"clusters": args.clusters, "acc": args.acc, "pair_model": args.pair_model, "form": op.pair.form.name, "pair_cutoff": pc,
            "neighbor_cutoff": nc, "n_configs": len(cfgs), "n_rows": int(len(cat["d"])), "K_max": int(K),
            "neighbours_mean": float(cat["mask"].sum(1).mean()),
            "residual_rel_to_M": float(np.linalg.norm(cat["R"]) / np.linalg.norm(cat["R"] + cat["P2"]))}
    path = Path(args.out) / "nbody_rows" / f"{args.tag or args.clusters}_{args.acc}.npz"
    path.parent.mkdir(parents=True, exist_ok=True)
    _save(path, meta=json.dumps(meta), **rows, **{f"cfg.{k}": np.array([c[k] for c in cfgs]) for k in cfgs[0]})
    print(json.dumps(meta, indent=2), f"\n-> {path}")


def build_self_rows(args) -> None:
    """One row per particle of every cluster: the many-body remainder of its SELF block,
    R = M_tt(MFS) - [M_iso + sum of the pair model's self corrections] (x 6 pi), and its neighbourhood."""
    from mobility import Operator
    from nbody import neighbours, to6
    op = Operator(P.load_pair(args.pair_model), acc=args.acc, device=args.device, psd=False)   # labels: the RAW sum
    nc = args.neighbor_cutoff or op.pair.form.r_cut
    parts, cfgs, t0 = [], [], time.time()
    for pos, q, shapes, M, meta in iter_clusters(args.clusters, args.acc, args.out):
        X, R, desc, kinds, kid = op.geometry(pos, q, shapes)
        n = len(X)
        ar = torch.arange(n, device=X.device)
        base = op.grand_M(pos, q, shapes, "pair").reshape(n, 6, n, 6)[ar, :, ar, :]
        Mb = torch.as_tensor(0.5 * (M + M.T), dtype=torch.float64, device=X.device).reshape(n, 6, n, 6)[ar, :, ar, :]
        nbr, nD, mask, nz = neighbours(X, desc["D"], X, ar[:, None], nc * P.length(desc), desc["z"])
        row = {"R": ((Mb - base) * P.SIX_PI).reshape(-1, 36), "P2": (base * P.SIX_PI).reshape(-1, 36), "nbr": nbr, "nbr_D": to6(nD),
               "mask": mask, "nbr_z": nz, "cfg": torch.full((n,), len(cfgs), dtype=torch.int64)}
        row.update({f"pt.{k}": desc[k] for k in ("D", "code", "z")})
        parts.append({k: v.cpu().numpy() for k, v in row.items()})
        prm = meta["params"]
        cfgs.append({"family": FAMILIES.index(meta["family"]), "phi": prm.get("phi", np.nan), "P": n,
                     "seed": meta["seed"], "is_val": meta["seed"] % 10 == 0})
        if len(cfgs) % 100 == 0:
            print(f"  {len(cfgs)} configurations, {sum(len(p['R']) for p in parts):,} rows [{time.time() - t0:.0f} s]", flush=True)
    assert parts, "no clusters"
    K = max(p["nbr"].shape[1] for p in parts)
    for p in parts:
        for k in ("nbr", "nbr_D", "mask", "nbr_z"):
            if p[k].shape[1] < K:
                full = np.zeros((p[k].shape[0], K) + p[k].shape[2:], dtype=p[k].dtype)
                full[:, :p[k].shape[1]] = p[k]
                p[k] = full
    cat = {k: np.concatenate([p[k] for p in parts], 0) for k in parts[0]}
    rows = {k: (v.astype(np.float32) if v.dtype == np.float64 else v) for k, v in cat.items()}
    meta = {"clusters": args.clusters, "acc": args.acc, "pair_model": args.pair_model, "neighbor_cutoff": nc,
            "n_configs": len(cfgs), "n_rows": int(len(cat["R"])), "K_max": int(K), "neighbours_mean": float(cat["mask"].sum(1).mean()),
            "residual_rel_to_M": float(np.linalg.norm(cat["R"]) / np.linalg.norm(cat["R"] + cat["P2"]))}
    path = Path(args.out) / "self_rows" / f"{args.tag or args.clusters}_{args.acc}.npz"
    path.parent.mkdir(parents=True, exist_ok=True)
    _save(path, meta=json.dumps(meta), **rows, **{f"cfg.{k}": np.array([c[k] for c in cfgs]) for k in cfgs[0]})
    print(json.dumps(meta, indent=2), f"\n-> {path}")


def load_nbody_rows(path: str, device="cpu"):
    """-> rows (float32 tensors, nested pt / ps), per-configuration arrays, meta."""
    z = np.load(path)
    meta = json.loads(str(z["meta"]))
    rows, cfg = {"pt": {}, "ps": {}}, {}
    for k in z.files:
        if k == "meta":
            continue
        if k.startswith("cfg."):
            cfg[k[4:]] = z[k]
        elif k[:3] in ("pt.", "ps."):
            rows[k[:2]][k[3:]] = torch.as_tensor(z[k], device=device)
        else:
            rows[k] = torch.as_tensor(z[k], device=device)
    return rows, cfg, meta


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--out", default=OUT)
    common.add_argument("--acc", default="fine", help="cloud resolution: coarse / medium / fine / Xfine")
    common.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    common.add_argument("--seed0", type=int, default=None)
    common.add_argument("--worker", type=int, default=0)
    common.add_argument("--num-workers", type=int, default=1)
    common.add_argument("--time-budget", type=float, default=float("inf"))
    a = sub.add_parser("pairs", parents=[common])
    a.add_argument("--shapes", nargs=2, required=True)
    a.add_argument("--tag", required=True)
    a.add_argument("--n", type=int, default=16384, help="configurations (each gives both ordered pairs)")
    a.add_argument("--shard-size", type=int, default=1024)
    a.add_argument("--cmax", type=float, default=8.0)
    a.add_argument("--r-max", type=float, default=None, help="distance cut: the pair model's r_cut (12 spheroid form, 14 triaxial), "
                   "farther pairs are redrawn.  Contact cut: leave it out and set --cmax just above the model's contact-factor range")
    a = sub.add_parser("clusters", parents=[common])
    a.add_argument("--kinds", nargs="+", required=True)
    a.add_argument("--tag", required=True)
    a.add_argument("--plan", choices=list(PLANS), default="default")
    a.add_argument("--one-kind", action="store_true", help="each cluster is a single shape drawn from --kinds (multi-shape, B)")
    a.add_argument("--per", type=int, default=24, help="configurations per (family, parameter, P)")
    a.add_argument("--shard-size", type=int, default=8)
    a = sub.add_parser("nbody-rows", parents=[common])
    a.add_argument("--clusters", required=True, help="tag of the cluster data")
    a.add_argument("--pair-model", required=True)
    a.add_argument("--tag", default=None)
    a.add_argument("--pair-cutoff", type=float, default=None, help="default: the pair model's r_cut")
    a.add_argument("--neighbor-cutoff", type=float, default=None, help="default: the pair model's r_cut")
    a = sub.add_parser("self-rows", parents=[common])
    a.add_argument("--clusters", required=True, help="tag of the cluster data")
    a.add_argument("--pair-model", required=True)
    a.add_argument("--tag", default=None)
    a.add_argument("--neighbor-cutoff", type=float, default=None, help="in particle lengths; default: the pair form's r_cut")
    args = ap.parse_args()
    {"pairs": gen_pairs, "clusters": gen_clusters, "nbody-rows": build_nbody_rows, "self-rows": build_self_rows}[args.cmd](args)


if __name__ == "__main__":
    main()
