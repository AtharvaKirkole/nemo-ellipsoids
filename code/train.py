#!/usr/bin/env python3
"""Train the two networks.  Both trainings are resumable: started again with the same arguments they continue from the
last checkpoint, so a long training runs as a chain of short jobs.

    python train.py pair  --form spheroid --sets PP OO PO --out data/final/models/pair_C.pt
    python train.py nbody --rows data/final/nbody_rows/P_fine.npz --out data/final/models/nbody_P.pt

pair    One model for all the given pair sets (makedata.py pairs): one set = one shape (A), several same-shape sets =
        multi-shape (B), + mixed sets = mixed (C) / polydisperse (D).  Rows inside r_cut only; target of the cross
        head: M_ts - (1 - w) far, of the self head: M_tt - M_iso (both x 6 pi).  Loss: L1, each 3x3 part weighted by
        (mean |TT|) / (mean |part|) so the small rotation parts count as much as translation.  Adam 2e-3, cosine,
        batch 512, a fixed number of optimizer STEPS (so less data does not mean less training).  The epoch with the
        best validation score is kept (mean over sets of the four cross-part errors + the self error).
nbody   Rows of makedata.py nbody-rows.  Loss: L1 over the 36 entries, each 3x3 part weighted by 1 / its RMS.
        Adam 1e-3, cosine over all steps, batch 4096, 300 epochs; best epoch by validation residual.

Scores printed and written next to the model (.json), all % against MFS:
pair    per set: PRMSE of the target velocity under one random unit force AND torque on the source, translation /
        rotation (NeMO's two-body metric; NeMO spheres 0.040 / 0.156), whole block, four parts, self; far field alone.
nbody   the same metric for pairs INSIDE clusters, two-body alone -> + f_nb (NeMO's Fig. 2; spheres 3.15 / 8.29).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import time
from pathlib import Path

import numpy as np
import torch

import pair as P
from farfield import window
from makedata import OUT, cat_rows, load_nbody_rows, load_pair_rows, rows_to, take_rows
from nbody import NbodyModel, SelfModel, fit_normalisation, fit_self_normalisation, save_nbody, save_self

PARTS = {"F-V": (slice(0, 3), slice(0, 3)), "T-V": (slice(0, 3), slice(3, 6)),
         "F-W": (slice(3, 6), slice(0, 3)), "T-W": (slice(3, 6), slice(3, 6))}


# ----------------------------------------------------------------------------------------------- shared
class Resumer:
    """Checkpoint at every selection step; a restart with the same arguments continues (model, optimizer, schedule,
    shuffling generator, best state so far, seconds spent)."""

    def __init__(self, out: str, args: dict):
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        self.args = {k: v for k, v in args.items() if k != "device"}
        tag = hashlib.md5(json.dumps(self.args, sort_keys=True, default=str).encode()).hexdigest()[:10]
        self.path = f"{out}.ckpt_{tag}"

    def load(self, model, opt, sched, gen, device):
        if not os.path.exists(self.path):
            return 1, float("inf"), None, 0.0
        ck = torch.load(self.path, map_location=device, weights_only=False)
        model.load_state_dict(ck["model"]), opt.load_state_dict(ck["opt"]), sched.load_state_dict(ck["sched"])
        gen.set_state(ck["gen"].cpu())                    # the CPU generator needs a CPU ByteTensor (map_location moved it)
        print(f"resumed {self.path} at epoch {ck['epoch']} (best {ck['best']:.4g})", flush=True)
        return ck["epoch"] + 1, ck["best"], ck["best_state"], ck["spent"]

    def save(self, epoch, model, opt, sched, gen, best, best_state, spent):
        torch.save({"model": model.state_dict(), "opt": opt.state_dict(), "sched": sched.state_dict(),
                    "gen": gen.get_state(), "epoch": epoch, "best": best, "best_state": best_state, "spent": spent},
                   self.path + ".tmp")
        os.replace(self.path + ".tmp", self.path)

    def done(self):
        if os.path.exists(self.path):
            os.remove(self.path)


def unit_loads(n: int, seed: int = 4) -> torch.Tensor:
    """One random unit force and one random unit torque per row, (n, 6)."""
    gen = torch.Generator().manual_seed(seed)
    f, t = torch.randn(n, 3, generator=gen, dtype=torch.float64), torch.randn(n, 3, generator=gen, dtype=torch.float64)
    return torch.cat([f / f.norm(dim=1, keepdim=True), t / t.norm(dim=1, keepdim=True)], 1)


def rel(a: torch.Tensor, b: torch.Tensor) -> float:
    return float(100.0 * (a - b).norm() / b.norm().clamp_min(1e-300))


def block_scores(pred: torch.Tensor, true: torch.Tensor, load: torch.Tensor) -> dict:
    """% errors of predicted 6x6 blocks: velocity PRMSE under `load` (trans / rot), whole block, the four parts."""
    pred, true, load = pred.double().cpu(), true.double().cpu(), load.double()
    up, ut = (pred @ load[:, :, None])[..., 0], (true @ load[:, :, None])[..., 0]
    out = {"trans": rel(up[:, :3], ut[:, :3]), "rot": rel(up[:, 3:], ut[:, 3:]), "whole": rel(pred, true)}
    out.update({k: rel(pred[:, a, b], true[:, a, b]) for k, (a, b) in PARTS.items()})
    return out


# ----------------------------------------------------------------------------------------------- pair model
def pair_targets(rows: dict, r_cut: float, taper: float | None = None, cut: str = "distance") -> dict:
    """Adds what the heads learn: base = (1 - w) far, cross_res = (cross - base) 6 pi, self6 = self 6 pi; and
    reach = where the pair is in the unit of the cut (pair lengths, or contact factor)."""
    rows["reach"] = P.reach(cut, rows["d"], rows["g"], rows["pt"], rows["ps"])
    w = window(rows["reach"], r_cut, taper or P.TAPER[cut])[:, None, None]
    rows["base"] = (1.0 - w) * rows["far"]
    rows["cross_res"] = (rows["cross"] - rows["base"]) * P.SIX_PI
    rows["self6"] = rows["self"] * P.SIX_PI
    return rows


def split_pair_set(tag: str, acc: str, root: str, r_cut: float, max_configs, dev, cut: str = "distance") -> dict:
    rows = pair_targets(load_pair_rows(tag, acc, root, max_configs), r_cut, cut=cut)
    near = rows["reach"] < r_cut
    val = (rows["seed"] % 10) == 0
    return {"train": rows_to(take_rows(rows, near & ~val), dev), "val": rows_to(take_rows(rows, near & val), dev)}


@torch.no_grad()
def score_pair(model, s: dict, load: torch.Tensor) -> dict:
    """Scores of one prepared set (pair_targets applied): the operator's cross block = base + learned / 6 pi."""
    model.eval()
    c, sf = model(s["d"], s["g"], s["pt"], s["ps"])
    sc = block_scores(s["base"] + c / P.SIX_PI, s["cross"], load)
    sc["self"] = rel(sf / P.SIX_PI, s["self"])
    sc["far_only"] = block_scores(s["far"], s["cross"], load)
    sc["rows"] = int(len(s["d"]))
    return sc


def part_weights(target: torch.Tensor) -> torch.Tensor:
    typ = {k: target[:, a, b].abs().mean() for k, (a, b) in PARTS.items()}
    W = torch.empty(6, 6, dtype=target.dtype, device=target.device)
    for k, (a, b) in PARTS.items():
        W[a, b] = typ["F-V"] / typ[k]
    return W


def train_pair(args) -> None:
    torch.manual_seed(args.seed)
    dev = torch.device(args.device)
    args.r_cut = args.r_cut or P.CUTS[args.cut] or P.FORMS[args.form].r_cut
    sets = {}
    for spec in args.sets:
        tag, _, mx = spec.partition(":")
        sets[tag] = split_pair_set(tag, args.acc, args.data, args.r_cut, int(mx) if mx else args.max_configs, dev, args.cut)
        print(f"  {tag:32} train rows {len(sets[tag]['train']['d']):>8,}  val rows {len(sets[tag]['val']['d']):>7,}", flush=True)
    tr = cat_rows([s["train"] for s in sets.values()])
    n_tr = len(tr["d"])
    loads = {k: unit_loads(len(s["val"]["d"])) for k, s in sets.items()}

    model = P.PairModel(args.form, args.r_cut, args.width, cut=args.cut).to(dev)
    with torch.no_grad():
        x = model.features(tr["d"], tr["g"], tr["pt"], tr["ps"])
        model.mu.copy_(x.mean(0))
        model.sd.copy_(x.std(0).clamp_min(1e-3))
        in_range = torch.stack([x.min(0).values, x.max(0).values]).cpu().tolist()
    w_cross, w_self = part_weights(tr["cross_res"]), part_weights(tr["self6"])
    per_epoch = math.ceil(n_tr / args.batch)
    epochs = max(1, math.ceil(args.steps / per_epoch))
    opt = torch.optim.Adam(model.parameters(), lr=args.lr)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, epochs)
    every = max(1, epochs // 60)
    print(f"{n_tr:,} training rows, {epochs} epochs x {per_epoch} steps, width {args.width}, device {dev}", flush=True)

    def select_score():
        evs = [score_pair(model, s["val"], loads[k]) for k, s in sets.items()]
        return float(np.mean([np.mean([e[p] for p in PARTS]) + e["self"] for e in evs]))

    gen = torch.Generator(device="cpu").manual_seed(args.seed)
    ck = Resumer(args.out, vars(args))
    start, best, best_state, spent = ck.load(model, opt, sched, gen, dev)
    t0 = time.time() - spent
    for epoch in range(start, epochs + 1):
        model.train()
        perm = torch.randperm(n_tr, generator=gen).to(dev)
        for i in range(0, n_tr, args.batch):
            b = take_rows(tr, perm[i:i + args.batch])
            c, sf = model(b["d"], b["g"], b["pt"], b["ps"])
            loss = ((c - b["cross_res"]).abs() * w_cross).mean() + ((sf - b["self6"]).abs() * w_self).mean()
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step()
        sched.step()
        if epoch % every == 0 or epoch == epochs:
            sc = select_score()
            if sc < best:
                best, best_state = sc, {k: v.detach().clone() for k, v in model.state_dict().items()}
            if epoch % max(1, epochs // 10) == 0 or epoch == epochs:
                print(f"epoch {epoch:6d}  selection score {sc:8.3f}  [{time.time() - t0:.0f} s]", flush=True)
            ck.save(epoch, model, opt, sched, gen, best, best_state, time.time() - t0)
    model.load_state_dict(best_state)
    report = {"args": vars(args), "train_rows": n_tr, "epochs": epochs, "train_seconds": round(time.time() - t0, 1),
              "input_range": in_range, "validation": {k: score_pair(model, s["val"], loads[k]) for k, s in sets.items()}}
    P.save_pair(model.cpu(), args.out, {"report": report})
    json.dump(report, open(args.out + ".json", "w"), indent=2)
    ck.done()
    print(f"\n{'set':32} {'trans':>7} {'rot':>7} {'whole':>7} {'self':>6}   far field alone trans / rot")
    for k, e in report["validation"].items():
        print(f"{k:32} {e['trans']:7.3f} {e['rot']:7.3f} {e['whole']:7.3f} {e['self']:6.2f}   "
              f"{e['far_only']['trans']:.2f} / {e['far_only']['rot']:.2f}")
    print(f"saved {args.out}")


# ----------------------------------------------------------------------------------------------- many-body model
NB_KEYS = ("d", "g", "pt", "ps", "nbr", "nbr_D", "mask", "nbr_z")


@torch.no_grad()
def predict_nbody(model, rows: dict, chunk: int = 8192) -> torch.Tensor:
    model.eval()
    return torch.cat([model(*(take_rows(rows, slice(i, i + chunk))[k] for k in NB_KEYS)).reshape(-1, 36)
                      for i in range(0, len(rows["d"]), chunk)])


def fig2_metric(P2: torch.Tensor, K: torch.Tensor, M: torch.Tensor, seed: int = 1234) -> dict:
    """NeMO's Fig. 2 metric: PRMSE (%) of the target velocity under a random unit force and torque on the source,
    two-body block alone and with the many-body correction."""
    P2, K, M = P2.double().cpu(), K.double().cpu(), M.double().cpu()
    F = unit_loads(len(M), seed)
    vt = (M @ F[..., None])[..., 0]
    out = {}
    for name, blk in (("two_body", P2), ("with_fnb", P2 + K)):
        v = (blk @ F[..., None])[..., 0]
        out[name] = {"trans": rel(v[:, :3], vt[:, :3]), "rot": rel(v[:, 3:], vt[:, 3:])}
    return out


def score_nbody(model, va: dict, cfg: dict) -> dict:
    K6 = predict_nbody(model, va).reshape(-1, 6, 6)
    R6, P26 = va["R"].reshape(-1, 6, 6), va["P2"].reshape(-1, 6, 6)
    M6 = P26 + R6
    rep = {"residual": {"all": rel(K6, R6), **{k: rel(K6[:, a, b], R6[:, a, b]) for k, (a, b) in PARTS.items()}},
           "fig2": fig2_metric(P26, K6, M6), "by_phi_uniform": {}, "rows": int(len(R6))}
    fam = torch.as_tensor(cfg["family"], device=va["cfg"].device)[va["cfg"]]
    phi = torch.as_tensor(np.nan_to_num(cfg["phi"].astype(float), nan=-1.0), device=va["cfg"].device)[va["cfg"]]
    for name, fi in (("large boxes (P 64 / 96)", 3),):
        m = fam == fi
        if int(m.sum()) > 50:
            rep["by_phi_uniform"][name] = dict(rows=int(m.sum()), **fig2_metric(P26[m], K6[m], M6[m], 7))
    for ph in sorted({float(x) for x in cfg["phi"][cfg["family"] == 0] if np.isfinite(x)}):
        m = (fam == 0) & ((phi - ph).abs() < 1e-9)
        if int(m.sum()) > 50:
            rep["by_phi_uniform"][f"{ph:g}"] = dict(rows=int(m.sum()), **fig2_metric(P26[m], K6[m], M6[m], 7))
    return rep


def train_nbody(args) -> None:
    torch.manual_seed(args.seed)
    torch.set_float32_matmul_precision("high")
    dev = torch.device(args.device)
    rows, cfg, meta = load_nbody_rows(args.rows, dev)
    val = torch.as_tensor(cfg["is_val"].astype(bool), device=dev)[rows["cfg"]]
    tr, va = take_rows(rows, ~val), take_rows(rows, val)
    n_tr = len(tr["d"])
    print(f"{int((~cfg['is_val'].astype(bool)).sum())} training configurations ({n_tr:,} ordered pairs), "
          f"{int(cfg['is_val'].sum())} validation ({len(va['d']):,}); neighbours per pair: mean "
          f"{meta['neighbours_mean']:.1f}, max {meta['K_max']}; device {dev}", flush=True)
    form = meta.get("form") or P.load_pair(meta["pair_model"]).form.name
    model = NbodyModel(form, meta["pair_cutoff"], meta["neighbor_cutoff"], args.bands, args.width).to(dev)
    gen = torch.Generator(device="cpu").manual_seed(args.seed)
    fit = take_rows(tr, torch.randperm(n_tr, generator=gen)[:min(n_tr, 131072)].to(dev))
    fit_normalisation(model, *(fit[k] for k in NB_KEYS))
    steps = args.epochs * math.ceil(n_tr / args.batch)
    opt = torch.optim.Adam(model.parameters(), lr=args.lr)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, steps)
    R6 = tr["R"].reshape(-1, 6, 6)
    wts = torch.ones(6, 6, device=dev)
    for a, b in PARTS.values():
        wts[a, b] = 1.0 / R6[:, a, b].pow(2).mean().sqrt().clamp_min(1e-12)
    wflat = (wts / wts.mean()).reshape(36)
    ck = Resumer(args.out, vars(args))
    start, best, best_state, spent = ck.load(model, opt, sched, gen, dev)
    t0 = time.time() - spent
    for epoch in range(start, args.epochs + 1):
        model.train()
        perm = torch.randperm(n_tr, generator=gen).to(dev)
        for i in range(0, n_tr, args.batch):
            b = take_rows(tr, perm[i:i + args.batch])
            loss = ((model(*(b[k] for k in NB_KEYS)).reshape(-1, 36) - b["R"]).abs() * wflat).mean()
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step()
            sched.step()
        if epoch % args.eval_every == 0 or epoch == args.epochs:
            e = rel(predict_nbody(model, va), va["R"])
            if e < best:
                best, best_state = e, {k: v.detach().clone() for k, v in model.state_dict().items()}
            print(f"epoch {epoch:4d}  validation residual error {e:7.2f} %  [{time.time() - t0:.0f} s]", flush=True)
            ck.save(epoch, model, opt, sched, gen, best, best_state, time.time() - t0)
    model.load_state_dict(best_state)
    report = {"args": vars(args), "rows_meta": meta, "train_rows": n_tr, "train_seconds": round(time.time() - t0, 1),
              "n_inputs": model.n_in, "n_outputs": model.n_out, **score_nbody(model, va, cfg)}
    save_nbody(model.cpu(), args.out, {"report": report, "pair_model": meta["pair_model"]})
    json.dump(report, open(args.out + ".json", "w"), indent=2)
    ck.done()
    f = report["fig2"]
    print(f"\nresidual error {report['residual']['all']:.2f} %; pairs in clusters, translation / rotation PRMSE: two-body "
          f"{f['two_body']['trans']:.2f} / {f['two_body']['rot']:.2f} %  ->  + f_nb {f['with_fnb']['trans']:.2f} / "
          f"{f['with_fnb']['rot']:.2f} %\nsaved {args.out}")


# ----------------------------------------------------------------------------------------------- many-body self model
SELF_KEYS = ("pt", "nbr", "nbr_D", "mask", "nbr_z")


@torch.no_grad()
def predict_self(model, rows: dict, chunk: int = 8192) -> torch.Tensor:
    model.eval()
    return torch.cat([model(*(take_rows(rows, slice(i, i + chunk))[k] for k in SELF_KEYS)).reshape(-1, 36)
                      for i in range(0, len(rows["R"]), chunk)])


def train_self(args) -> None:
    """Rows of makedata.py self-rows.  Same loss and schedule as the many-body model."""
    torch.manual_seed(args.seed)
    dev = torch.device(args.device)
    rows, cfg, meta = load_nbody_rows(args.rows, dev)
    rows.pop("ps", None)
    val = torch.as_tensor(cfg["is_val"].astype(bool), device=dev)[rows["cfg"]]
    tr, va = take_rows(rows, ~val), take_rows(rows, val)
    n_tr = len(tr["R"])
    print(f"{n_tr:,} training particles, {len(va['R']):,} validation; neighbours per particle: mean {meta['neighbours_mean']:.1f}, "
          f"max {meta['K_max']}; device {dev}", flush=True)
    model = SelfModel(meta["neighbor_cutoff"], args.bands, args.width).to(dev)
    gen = torch.Generator(device="cpu").manual_seed(args.seed)
    fit = take_rows(tr, torch.randperm(n_tr, generator=gen)[:min(n_tr, 131072)].to(dev))
    fit_self_normalisation(model, *(fit[k] for k in SELF_KEYS))
    steps = args.epochs * math.ceil(n_tr / args.batch)
    opt = torch.optim.Adam(model.parameters(), lr=args.lr)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, steps)
    R6 = tr["R"].reshape(-1, 6, 6)
    wts = torch.ones(6, 6, device=dev)
    for a, b in PARTS.values():
        wts[a, b] = 1.0 / R6[:, a, b].pow(2).mean().sqrt().clamp_min(1e-12)
    wflat = (wts / wts.mean()).reshape(36)
    ck = Resumer(args.out, vars(args))
    start, best, best_state, spent = ck.load(model, opt, sched, gen, dev)
    t0 = time.time() - spent
    for epoch in range(start, args.epochs + 1):
        model.train()
        perm = torch.randperm(n_tr, generator=gen).to(dev)
        for i in range(0, n_tr, args.batch):
            b = take_rows(tr, perm[i:i + args.batch])
            loss = ((model(*(b[k] for k in SELF_KEYS)).reshape(-1, 36) - b["R"]).abs() * wflat).mean()
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step()
            sched.step()
        if epoch % args.eval_every == 0 or epoch == args.epochs:
            e = rel(predict_self(model, va), va["R"])
            if e < best:
                best, best_state = e, {k: v.detach().clone() for k, v in model.state_dict().items()}
            print(f"epoch {epoch:4d}  validation residual error {e:7.2f} %  [{time.time() - t0:.0f} s]", flush=True)
            ck.save(epoch, model, opt, sched, gen, best, best_state, time.time() - t0)
    model.load_state_dict(best_state)
    K = predict_self(model, va)
    truth = va["P2"] + va["R"]
    report = {"args": vars(args), "rows_meta": meta, "train_rows": n_tr, "train_seconds": round(time.time() - t0, 1),
              "n_inputs": model.n_in, "n_outputs": model.n_out, "residual": rel(K, va["R"]),
              "self_block_error": {"pairwise_sum": rel(va["P2"], truth), "with_self_model": rel(va["P2"] + K, truth)}}
    save_self(model.cpu(), args.out, {"report": report, "pair_model": meta["pair_model"]})
    json.dump(report, open(args.out + ".json", "w"), indent=2)
    ck.done()
    e = report["self_block_error"]
    print(f"\nresidual error {report['residual']:.2f} %; self blocks against MFS: pairwise sum {e['pairwise_sum']:.3f} %  ->  "
          f"+ self model {e['with_self_model']:.3f} %\nsaved {args.out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("pair")
    a.add_argument("--sets", nargs="+", required=True, help="pair-data tags, optionally tag:max_configs")
    a.add_argument("--data", default=OUT)
    a.add_argument("--acc", default="fine")
    a.add_argument("--max-configs", type=int, default=None)
    a.add_argument("--form", required=True, choices=list(P.FORMS))
    a.add_argument("--cut", default="distance", choices=list(P.CUTS), help="range of the learned part: centre distance or contact factor")
    a.add_argument("--r-cut", type=float, default=None, help="default: 12 / 14 pair lengths (distance), contact factor 4 (contact)")
    a.add_argument("--width", type=int, default=128)
    a.add_argument("--steps", type=int, default=200_000, help="optimizer steps in total")
    a.add_argument("--batch", type=int, default=512)
    a.add_argument("--lr", type=float, default=2e-3)
    a.add_argument("--seed", type=int, default=0)
    a.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    a.add_argument("--out", required=True)
    a = sub.add_parser("nbody")
    a.add_argument("--rows", required=True)
    a.add_argument("--width", type=int, default=128)
    a.add_argument("--bands", type=int, default=8)
    a.add_argument("--epochs", type=int, default=300)
    a.add_argument("--batch", type=int, default=4096)
    a.add_argument("--lr", type=float, default=1e-3)
    a.add_argument("--eval-every", type=int, default=5)
    a.add_argument("--seed", type=int, default=0)
    a.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    a.add_argument("--out", required=True)
    a = sub.add_parser("self")
    a.add_argument("--rows", required=True)
    a.add_argument("--width", type=int, default=128)
    a.add_argument("--bands", type=int, default=8)
    a.add_argument("--epochs", type=int, default=300)
    a.add_argument("--batch", type=int, default=1024)
    a.add_argument("--lr", type=float, default=1e-3)
    a.add_argument("--eval-every", type=int, default=5)
    a.add_argument("--seed", type=int, default=0)
    a.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    a.add_argument("--out", required=True)
    args = ap.parse_args()
    {"pair": train_pair, "nbody": train_nbody, "self": train_self}[args.cmd](args)


if __name__ == "__main__":
    main()
