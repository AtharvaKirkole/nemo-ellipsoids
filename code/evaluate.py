#!/usr/bin/env python3
"""Every accuracy number, from trained models, against MFS -- and next to each one the error of MFS ITSELF under the
same conditions, and the conditions.  Run from the workspace (the directory that holds data/points and data/final).

    python evaluate.py clouds     --kinds prolateSpheroid oblateSpheroid                    the clouds against the exact isolated particle
    python evaluate.py pair       --pair pair.pt --sets PP_test PO_test [--ref-acc Xfine]   two-body accuracy (NeMO Fig. 1 metric)
    python evaluate.py suspension --kinds prolateSpheroid --pair pair.pt --nbody nbody.pt [--ref-acc Xfine]   Fig. 3 (N 200, phi sweep)
    python evaluate.py suspension ... --N 50 100 200 300 --phi 0.05 0.1 0.15 0.2 --seeds 5  Fig. 4 (N sweep)
    python evaluate.py dynamics   --kinds prolateSpheroid --case ring --pair pair.pt --nbody nbody.pt [--ref-acc Xfine]
    python evaluate.py check      --kinds prolateSpheroid --pair pair.pt --nbody nbody.pt [--ref-acc Xfine]
    python evaluate.py ceiling    --kinds prolateSpheroid --pair pair.pt --nbody nbody.pt

The error of MFS (the truth).  The model can only be trusted down to it, so it is measured three ways:
  exact        the cloud of ONE particle against the exact mobility of an isolated ellipsoid (Oberbeck / Jeffery): the
               only absolute number.  `clouds`, and in the conditions of every report.
  resolution   the same configurations, loads and metric solved again with the next finer cloud (--ref-acc Xfine):
               "fine against Xfine".  Reported per test set / volume fraction / trajectory, where the finer clouds
               exist in data/points (otherwise the report says so).
  reciprocity  the exact mobility matrix is symmetric; what MFS returns is not quite.  The size of the part removed
               when labels are symmetrised, in the metric of the test.  Needs no extra solve: always reported.

pair        per set: PRMSE of the target velocity under one random unit force and torque on the source, translation /
            rotation; by contact-factor band; the far field alone; how many rows lie outside the training input range.
suspension  N particles placed uniformly at random at volume fraction phi (random orientations, contact factor >= 1.05),
            shapes drawn from --kinds in equal numbers.  Loads: a random unit force and torque on every particle (PRMSE
            of all six velocity components, and translation / rotation apart), and gravity (translation).  Operators:
            far field only (the RPY analogue), + two-body, + many-body.  Truth cached per configuration.
dynamics    a ring of 5 (or a pair) falling under gravity, RK4, the SAME integrator with MFS at every stage as truth.
            Errors when the first run stops (a pair reaching contact factor 1.05, or --steps): centre of mass (% of the
            distance fallen), largest particle position error, largest axis error (degrees, axes as lines).
ceiling     the operator with every near cross block replaced by the EXACT MFS block (a perfect many-body correction),
            and then also every self block.  What is left is the pairs beyond the cutoff: the floor of any near-field
            model.
pd          positive definiteness of the RAW operator (before psd.py's projection) over MANY random suspensions (no MFS
            needed), the particles carrying the weakest mode of the worst one, the two-body operator on stored pairs
            alone against MFS, and how much the projection changes the operator.
psd         the projection against the truth, on the held-out clusters (seed % 10 == 0: never trained on) of the case:
            the truth's smallest eigenvalue, the raw operator's, Weyl's bound |M - T|_2, and every error before and after
            the projection (it can only decrease in the metric of the isolated particles).
check       symmetry of the grand mobility matrix (exact by construction), its smallest eigenvalue before and after the
            projection against MFS's, equivariance under a rotation of everything.

Every operator here is the projected one (positive definite, psd.py) unless a table says "raw"; --raw turns the
projection off everywhere.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import time
from pathlib import Path

import numpy as np
import torch

import pair as P
from geometry import (MARGIN, assign_shapes, axes_of, matrix_to_quat, min_contact, quat_to_matrix, ring_config,
                      tilted_pair_config, uniform_config)
from makedata import OUT, load_pair_rows, rows_to, take_rows
from mobility import Operator
from nbody import load_nbody, load_self
from train import block_scores, pair_targets, rel, score_pair, unit_loads
from truth import Truth, cloud_error, have_cloud
import psd as PSD

SIX_PI = 6.0 * np.pi
BANDS = [(1.0, 1.1), (1.1, 1.25), (1.25, 1.5), (1.5, 2.0), (2.0, 4.0), (4.0, 1e9)]
TOL_V = 1e-7                                    # GMRES velocity tolerance of the iterative MFS solver


def operator(args) -> tuple:
    pair = P.load_pair(args.pair) if args.pair else None
    nb = load_nbody(args.nbody) if getattr(args, "nbody", None) else None
    ns = load_self(args.nself) if getattr(args, "nself", None) else None
    modes = ["far"] + (["pair"] if pair is not None else []) + (["full"] if nb is not None else [])
    return Operator(pair, nb, acc=args.acc, device=args.device, self_model=ns, psd=not getattr(args, "raw", False)), modes


def write(path: Path, lines: list, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    json.dump(obj, open(path.with_suffix(".json"), "w"), indent=2, default=float)
    print("\n".join(lines), f"\n-> {path.with_suffix('.md')}")


def prmse(v: np.ndarray, t: np.ndarray) -> dict:
    f = lambda a, b: float(100 * np.sqrt(((a - b) ** 2).sum() / max((b ** 2).sum(), 1e-300)))
    return {"all": f(v, t), "trans": f(v[:, :3], t[:, :3]), "rot": f(v[:, 3:], t[:, 3:])}


# ----------------------------------------------------------------------------------------------- conditions
def cloud_table(kinds, accs) -> tuple:
    """Markdown rows + dict: each shape's semi-axes and, per resolution, cloud size and error against the exact
    isolated mobility."""
    lines = ["| shape | semi-axes | " + " | ".join(f"{a}: nodes / sources; exact-mobility error trans / rot %" for a in accs) + " |",
             "|---|---|" + "---|" * len(accs)]
    out = {}
    for s in dict.fromkeys(kinds):
        cells, out[s] = [], {"axes": [float(x) for x in axes_of(s)]}
        for a in accs:
            e = cloud_error(s, a)
            out[s][a] = e
            cells.append(f"{e['nodes']} / {e['sources']}; {e['trans_pct']:.4f} / {e['rot_pct']:.4f}" if e else "no cloud")
        lines.append(f"| {s} | {' : '.join(f'{x:g}' for x in axes_of(s))} | " + " | ".join(cells) + " |")
    return lines, out


def psd_condition(args) -> str:
    if getattr(args, "raw", False):
        return ("- **Positive definiteness**: NOT enforced (--raw): the operators are the raw sums, symmetric but not "
                "necessarily positive definite.")
    return ("- **Positive definiteness**: every operator matrix is projected onto the positive semi-definite matrices in the "
            f"metric of the isolated particles (psd.py: eigenvalues relative to the isolated mobilities >= {PSD.FLOOR:g}); "
            "a matrix that already is positive definite is used as it is.")


def model_conditions(args) -> tuple:
    """What the models are: form, sizes, what they were trained on."""
    lines, out = [], {}
    if getattr(args, "pair", None):
        m = P.load_pair(args.pair)
        a = m.report.get("args", {})
        n_par = sum(p.numel() for p in m.parameters())
        out["pair"] = {"file": args.pair, "form": m.form.name, "inputs": m.form.n_in, "true": m.form.n_true,
                       "pseudo": m.form.n_pseudo, "r_cut": m.r_cut, "cut": m.cut, "width": m.width, "parameters": n_par,
                       "train_sets": a.get("sets"), "train_rows": m.report.get("train_rows"), "steps": a.get("steps"),
                       "seed": a.get("seed")}
        lines.append(f"- **Two-body model** `{args.pair}`: {m.form.name} form, {m.form.n_in} inputs, {m.form.n_true} true + "
                     f"{m.form.n_pseudo} pseudo tensors ({m.n_coeff} coefficients per block, two blocks), width {m.width}, "
                     f"{n_par:,} parameters, learned inside "
                     + (f"r_cut = {m.r_cut:g} pair lengths" if m.cut == "distance" else f"contact factor {m.r_cut:g}")
                     + " (far field beyond).  Trained on "
                     f"{m.report.get('train_rows', '?'):,} ordered pairs, {a.get('steps', '?')} steps, seed {a.get('seed', '?')}: "
                     f"{' '.join(a.get('sets', []))}." if a else f"- **Two-body model** `{args.pair}`: {m.form.name} form.")
    if getattr(args, "nbody", None):
        m = load_nbody(args.nbody)
        a, rm = m.report.get("args", {}), m.report.get("rows_meta", {})
        n_par = sum(p.numel() for p in m.parameters())
        out["nbody"] = {"file": args.nbody, "form": m.form.name, "inputs": m.n_in, "true": m.n_true, "pseudo": m.n_pseudo,
                        "bands": m.n_bands, "pair_cutoff": m.pair_cutoff, "neighbor_cutoff": m.neighbor_cutoff,
                        "width": m.width, "parameters": n_par, "clusters": rm.get("clusters"), "configs": rm.get("n_configs"),
                        "rows": rm.get("n_rows"), "neighbours_mean": rm.get("neighbours_mean"), "seed": a.get("seed")}
        lines.append(f"- **Many-body model** `{args.nbody}`: {m.n_in} inputs ({m.form.n_in} of the pair + 20 per band x "
                     f"{m.n_bands} bands), {m.n_true} true + {m.n_pseudo} pseudo tensors, width {m.width}, {n_par:,} "
                     f"parameters; corrects pairs within {m.pair_cutoff:g}, sees neighbours within {m.neighbor_cutoff:g} "
                     f"(pair lengths) of the pair midpoint.  Trained on {rm.get('n_rows', '?'):,} ordered pairs from "
                     f"{rm.get('n_configs', '?')} clusters `{rm.get('clusters', '?')}` (mean {rm.get('neighbours_mean', 0):.1f} "
                     f"neighbours per pair), seed {a.get('seed', '?')}." if rm else f"- **Many-body model** `{args.nbody}`.")
    if getattr(args, "nself", None):
        m = load_self(args.nself)
        rm, e = m.report.get("rows_meta", {}), m.report.get("self_block_error", {})
        out["nself"] = {"file": args.nself, "inputs": m.n_in, "true": m.n_true, "pseudo": m.n_pseudo, "bands": m.n_bands,
                        "neighbor_cutoff": m.neighbor_cutoff, "width": m.width, "rows": rm.get("n_rows"), **e}
        lines.append(f"- **Many-body self model** `{args.nself}` (part of '+ many-body'): {m.n_in} inputs, {m.n_true} true + "
                     f"{m.n_pseudo} pseudo tensors, width {m.width}; neighbours within {m.neighbor_cutoff:g} particle lengths.  "
                     + (f"Trained on {rm.get('n_rows', 0):,} particles of clusters `{rm.get('clusters', '?')}`; self blocks against "
                        f"MFS on validation: pairwise sum {e.get('pairwise_sum', 0):.3f} % -> {e.get('with_self_model', 0):.3f} %." if rm else ""))
    lines.append(psd_condition(args))
    out["psd"] = {"projected": not getattr(args, "raw", False), "floor": PSD.FLOOR}
    return lines, out


def truth_conditions(args, kinds, what: str) -> tuple:
    ref = getattr(args, "ref_acc", None)
    accs = [args.acc] + ([ref] if ref and have_cloud(kinds, ref) else [])
    lines = [f"- **Truth**: MFS, `{args.acc}` clouds, viscosity 1; {what}"]
    if ref and len(accs) == 1:
        lines.append(f"- **MFS resolution error not measured**: no `{ref}` cloud in data/points for "
                     f"{', '.join(s for s in dict.fromkeys(kinds) if not have_cloud([s], ref))}.")
    tab, out = cloud_table(kinds, accs)
    if len(accs) > 1:                                # a finer cloud that is not closer to the exact particle is not a reference
        bad = [s for s, e in out.items() if e[ref] and e[args.acc] and
               max(e[ref]["trans_pct"], e[ref]["rot_pct"]) > max(e[args.acc]["trans_pct"], e[args.acc]["rot_pct"])]
        if bad:
            lines.append(f"- **WARNING**: the `{ref}` cloud of {', '.join(bad)} is NOT closer to the exact isolated particle "
                         f"than the `{args.acc}` one: the `{args.acc} vs {ref}` columns involving it are not an error estimate.")
    return lines + ["- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):", ""] + tab + [""], \
        {"acc": args.acc, "ref_acc": accs[1] if len(accs) > 1 else None, "clouds": out}


# ----------------------------------------------------------------------------------------------- clouds
def eval_clouds(args) -> None:
    accs = [a for a in ("coarse", "medium", "fine", "Xfine") if any(have_cloud([s], a) for s in args.kinds)]
    tab, out = cloud_table(args.kinds, accs)
    lines = ["# MFS clouds against the exact isolated ellipsoid", "",
             "For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three "
             "translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; "
             "Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.", ""] + tab
    write(Path(args.results) / "CLOUDS", lines, out)


# ----------------------------------------------------------------------------------------------- two-body accuracy
def set_meta(tag: str, acc: str, root: str) -> dict:
    files = sorted(glob.glob(f"{root}/pairs/{tag}_{acc}/shard_*.npz"))
    if not files:
        return {}
    meta = json.loads(str(np.load(files[0])["meta"]))
    return dict(meta, configs=int(sum(len(np.load(f)["seed"]) for f in files)))


def eval_pair(args) -> None:
    model = P.load_pair(args.pair).double()
    lo, hi = (torch.as_tensor(x, dtype=torch.float64) for x in model.report["input_range"])
    prep = lambda tag, acc, mx: rows_to(pair_targets(load_pair_rows(tag, acc, args.data, mx), model.r_cut, model.taper, model.cut),
                                        "cpu", torch.float64)
    ref = args.ref_acc
    head = ["| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | "
            f"MFS {args.acc} vs {ref or 'finer'}: trans / rot (rows) | model vs {ref or 'finer'}: trans / rot | "
            "MFS reciprocity defect: trans / rot | outside training range |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    band_head = "| set | " + " | ".join(f"c {a:g}-{b:g}" if b < 1e8 else f"c > {a:g}" for a, b in BANDS) + " |"
    band_lines = ["", "## Model error by contact factor: trans / rot (rows)", "", band_head, "|---|" + "---|" * len(BANDS)]
    mfs_bands = ["", f"## MFS error ({args.acc} vs {ref}) by contact factor: trans / rot (rows)", "", band_head,
                 "|---|" + "---|" * len(BANDS)]
    out, rows_md, cond_sets, kinds = {}, [], [], []
    for tag in args.sets:
        meta = set_meta(tag, args.acc, args.data)
        kinds += meta["shapes"]
        rows = prep(tag, args.acc, args.max_configs)
        near = take_rows(rows, rows["reach"] < model.r_cut)
        load = unit_loads(len(near["d"]))
        e = score_pair(model, near, load)
        x = model.features(near["d"], near["g"], near["pt"], near["ps"])
        tol = 0.05 * (hi - lo) + 1e-4                              # 5 % beyond the training range counts as outside
        e["outside_range_pct"] = float(100 * ((x < lo - tol) | (x > hi + tol)).any(1).double().mean())
        e["mfs_reciprocity"] = block_scores(near["raw"], near["cross"], load)
        with torch.no_grad():
            c, _ = model(near["d"], near["g"], near["pt"], near["ps"])
        pred, cells = near["base"] + c / P.SIX_PI, []
        for a, b in BANDS:
            m = (near["c"] >= a) & (near["c"] < b)
            if int(m.sum()) > 20:
                s = block_scores(pred[m], near["cross"][m], load[m])
                e[f"band_{a:g}"] = s
                cells.append(f"{s['trans']:.3f} / {s['rot']:.3f} ({int(m.sum())})")
            else:
                cells.append("-")
        band_lines.append(f"| {tag} | " + " | ".join(cells) + " |")
        mfs_txt = mod_txt = "not measured"
        if ref and set_meta(tag, ref, args.data):                 # the same configurations solved with the finer clouds
            rr = prep(tag, ref, None)
            ff = prep(tag, args.acc, len(rr["d"]) // 2)
            assert torch.equal(ff["seed"], rr["seed"]) and torch.allclose(ff["d"], rr["d"]), f"{tag}: {ref} set is not the same configurations"
            m = ff["reach"] < model.r_cut
            f2, r2 = take_rows(ff, m), take_rows(rr, m)
            l2 = unit_loads(len(f2["d"]))
            with torch.no_grad():
                c2, _ = model(f2["d"], f2["g"], f2["pt"], f2["ps"])
            e["mfs_resolution"] = dict(block_scores(f2["cross"], r2["cross"], l2), self=rel(f2["self"], r2["self"]), rows=int(m.sum()))
            e["model_vs_ref"] = block_scores(f2["base"] + c2 / P.SIX_PI, r2["cross"], l2)
            mfs_txt = f"{e['mfs_resolution']['trans']:.3f} / {e['mfs_resolution']['rot']:.3f} ({int(m.sum())})"
            mod_txt = f"{e['model_vs_ref']['trans']:.3f} / {e['model_vs_ref']['rot']:.3f}"
            cells = []
            for a, b in BANDS:
                mb = (f2["c"] >= a) & (f2["c"] < b)
                if int(mb.sum()) > 20:
                    s = block_scores(f2["cross"][mb], r2["cross"][mb], l2[mb])
                    e["mfs_resolution"][f"band_{a:g}"] = s
                    cells.append(f"{s['trans']:.3f} / {s['rot']:.3f} ({int(mb.sum())})")
                else:
                    cells.append("-")
            mfs_bands.append(f"| {tag} | " + " | ".join(cells) + " |")
        e["conditions"] = meta
        out[tag] = e
        rows_md.append(f"| {tag} | {e['rows']} | {e['trans']:.3f} | {e['rot']:.3f} | {e['whole']:.3f} | {e['self']:.2f} | "
                       f"{e['far_only']['trans']:.2f} / {e['far_only']['rot']:.2f} | {mfs_txt} | {mod_txt} | "
                       f"{e['mfs_reciprocity']['trans']:.3f} / {e['mfs_reciprocity']['rot']:.3f} | {e['outside_range_pct']:.1f} % |")
        cond_sets.append(f"  - `{tag}`: {meta['shapes'][0]} (target or source) with {meta['shapes'][1]}, {meta['configs']} "
                         f"configurations (both orderings scored: {e['rows']} rows inside r_cut), contact factor c with "
                         f"c - 1 log-uniform in [{MARGIN:g}, {meta['cmax'] - 1:g}]"
                         + (f", centre distance below {meta['r_max']:g} pair lengths" if meta.get("r_max") else ", any centre distance"))
    mlines, mcond = model_conditions(args)
    tlines, tcond = truth_conditions(args, kinds, "ONE direct dense solve per pair (exact to round-off for its cloud); "
                                     "blocks read from the symmetrised matrix 1/2 (M + M^T).")
    cond = ["## Conditions", ""] + mlines + [
        "- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never "
        "used in training:"] + cond_sets + [
        "- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); "
        "PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius "
        "error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.",
        "- **MFS columns**: `" + f"{args.acc} vs {ref}" + "` = the same pairs solved with both cloud resolutions, same "
        "metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric."] + tlines
    lines = [f"# Two-body accuracy of `{args.pair}`", "", "All numbers are % errors.", ""] + head + rows_md + band_lines
    if len(mfs_bands) > 5:
        lines += mfs_bands
    write(Path(args.results) / f"PAIR_{Path(args.pair).stem}", lines + [""] + cond,
          {"sets": out, "conditions": {"models": mcond, "truth": tcond}})


# ----------------------------------------------------------------------------------------------- suspensions
def random_loads(rng, N: int) -> np.ndarray:
    """(N, 6, 2): column 0 a random unit force and torque on every particle, column 1 gravity; both x 6 pi."""
    u = lambda x: x / np.linalg.norm(x, axis=1, keepdims=True)
    F = np.zeros((N, 6, 2))
    F[:, :3, 0], F[:, 3:, 0] = u(rng.normal(size=(N, 3))), u(rng.normal(size=(N, 3)))
    F[:, 2, 1] = -1.0
    return F * SIX_PI


def cached_truth(truth, cache: Path, key: str, pos, q, shapes, F):
    f = cache / f"{key}.npz"
    if f.exists() and np.allclose(np.load(f)["pos"], pos):
        return np.load(f)["tv"]
    tv = truth.velocities(pos, q, shapes, F)
    cache.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(f, pos=pos, q=q, F=F, tv=tv)
    return tv


def eval_suspension(args) -> None:
    op, modes = operator(args)
    truth = Truth(args.kinds, args.acc, args.device)
    name = args.name or "_".join(args.kinds)
    cache = Path(args.data) / "truth_cache" / f"{name}_{args.acc}"
    ref = args.ref_acc if args.ref_acc and have_cloud(args.kinds, args.ref_acc) else None
    truth_ref = Truth(args.kinds, ref, args.device) if ref else None
    csv_path = Path(args.results) / f"SUSPENSION_{name}.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["phi", "N", "seed", "operator", "all", "trans", "rot", "gravity_trans"]
    rows, contact = [], {}
    for phi in args.phi:
        for N in args.N:
            for seed in range(args.seeds):
                rng = np.random.default_rng([20261110, int(round(phi * 1e6)), N, seed])
                shapes = assign_shapes(args.kinds, N, rng)
                made = uniform_config(shapes, phi, rng)
                if made is None:
                    print(f"phi {phi} N {N} seed {seed}: could not place", flush=True)
                    continue
                pos, q = made
                F = random_loads(rng, N)
                t0 = time.time()
                tv = cached_truth(truth, cache, f"phi{phi:g}_N{N}_s{seed}", pos, q, shapes, F)
                line = f"phi {phi:<6g} N {N:<4d} seed {seed} (MFS {time.time() - t0:.0f} s):"
                for mode in modes:
                    v = op.apply(pos, q, shapes, F, mode)
                    r, g = prmse(v[..., 0], tv[..., 0]), prmse(v[..., 1], tv[..., 1])
                    rows.append(dict(phi=phi, N=N, seed=seed, operator=mode, all=r["all"], trans=r["trans"], rot=r["rot"],
                                     gravity_trans=g["trans"]))
                    line += f"  {mode} {r['all']:.2f}"
                if ref and seed < args.ref_seeds and N <= args.ref_max_n:          # MFS itself: fine against the finer clouds
                    try:
                        tr = cached_truth(truth_ref, Path(args.data) / "truth_cache" / f"{name}_{ref}",
                                          f"phi{phi:g}_N{N}_s{seed}", pos, q, shapes, F)
                        r, g = prmse(tv[..., 0], tr[..., 0]), prmse(tv[..., 1], tr[..., 1])
                        rows.append(dict(phi=phi, N=N, seed=seed, operator="mfs", all=r["all"], trans=r["trans"], rot=r["rot"],
                                         gravity_trans=g["trans"]))
                        line += f"  | MFS {args.acc} vs {ref} {r['all']:.3f}"
                    except Exception as e:                            # noqa: BLE001
                        line += f"  | MFS {ref} failed ({str(e)[:60]})"
                print(line, flush=True)
                with open(csv_path, "w", newline="") as fh:
                    w = csv.DictWriter(fh, fieldnames=fields)
                    w.writeheader()
                    w.writerows(rows)
    cols = modes + (["mfs"] if ref else [])
    label = {"far": "far field", "pair": "+ two-body", "full": "+ many-body", "mfs": f"MFS {args.acc} vs {ref} (n)"}
    lines = [f"# Suspensions of {', '.join(args.kinds)}: operator against MFS ({args.acc})", "",
             "PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; "
             "in brackets translation / rotation apart, then translation under gravity.", "",
             "| phi | N | n | " + " | ".join(label[c] for c in cols) + " |", "|---|---|---|" + "---|" * len(cols)]
    summ = {}
    for phi in args.phi:
        for N in args.N:
            cell = [r for r in rows if r["phi"] == phi and r["N"] == N]
            if not cell:
                continue
            txt = []
            for mode in cols:
                c = [r for r in cell if r["operator"] == mode]
                if not c:
                    txt.append("not measured")
                    continue
                m = {k: float(np.mean([r[k] for r in c])) for k in ("all", "trans", "rot", "gravity_trans")}
                summ[f"{phi:g}|{N}|{mode}"] = dict(m, n=len(c))
                d = 3 if mode == "mfs" else 2
                txt.append(f"{m['all']:.{d}f} ({m['trans']:.{d}f} / {m['rot']:.{d}f}; {m['gravity_trans']:.{d}f})"
                           + (f" ({len(c)})" if mode == "mfs" else ""))
            lines.append(f"| {phi:g} | {N} | {len([r for r in cell if r['operator'] == modes[0]])} | " + " | ".join(txt) + " |")
    mlines, mcond = model_conditions(args)
    tlines, tcond = truth_conditions(args, args.kinds, f"iterative solve (GMRES, velocity tolerance {TOL_V:g}) of the whole "
                                     "configuration, both load cases at once; cached per configuration.")
    cond = ["", "## Conditions", ""] + mlines + [
        f"- **Configurations**: N in {args.N} particles, shapes {', '.join(args.kinds)} in equal numbers (random order); "
        f"centres uniform in a cube of volume (total particle volume) / phi, phi in {args.phi}; orientations uniform on "
        f"SO(3); every pair at contact factor >= {1 + MARGIN:g} (rejection); no periodic images (a finite cloud in "
        f"unbounded fluid); {args.seeds} independent configurations per (phi, N).",
        "- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force "
        "on every particle.  All x 6 pi.",
        "- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity "
        "components, of translation and rotation apart (load 1), and of translation under gravity (load 2).",
        "- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the "
        "pair model inside r_cut; + many-body = the many-body correction on top.",
        f"- **MFS column**: the first {args.ref_seeds} configurations of each (phi, N <= {args.ref_max_n}) solved again "
        f"with the `{args.ref_acc}` clouds, same loads and metric." if args.ref_acc else "- **MFS column**: not requested (--ref-acc)."] + tlines
    write(Path(args.results) / f"SUSPENSION_{name}", lines + cond,
          {"kinds": args.kinds, "cells": summ, "conditions": {"models": mcond, "truth": tcond, "N": args.N, "phi": args.phi,
                                                               "seeds": args.seeds, "contact_floor": 1 + MARGIN}})


# ----------------------------------------------------------------------------------------------- dynamics
def rk4_step(velocity, x, q, dt):
    """One RK4 step of rigid-body motion; velocity(x, q) -> (P, 6) lab-frame [U, Omega]."""
    from scipy.spatial.transform import Rotation

    def advance(U, h):
        return x + h * U[:, :3], (Rotation.from_rotvec(h * U[:, 3:]) * Rotation.from_quat(q)).as_quat()

    k1 = velocity(x, q)
    k2 = velocity(*advance(k1, 0.5 * dt))
    k3 = velocity(*advance(k2, 0.5 * dt))
    k4 = velocity(*advance(k3, dt))
    return advance((k1 + 2 * k2 + 2 * k3 + k4) / 6.0, dt)


def axis_error_deg(shapes, qa, qb) -> np.ndarray:
    """Per particle: the largest angle between corresponding body axes, as lines, over the axes that are
    distinguishable (a spheroid's two equal axes are not: only its symmetry axis counts)."""
    Ra, Rb = quat_to_matrix(qa), quat_to_matrix(qb)
    out = np.zeros(len(shapes))
    for p, s in enumerate(shapes):
        ax = axes_of(s)
        for i in range(3):
            if np.sum(np.isclose(ax, ax[i])) == 1:
                out[p] = max(out[p], np.degrees(np.arccos(np.clip(abs(Ra[p, :, i] @ Rb[p, :, i]), 0.0, 1.0))))
    return out


def run(velocity, shapes, pos, q, dt, steps, floor=1 + MARGIN):
    X, Q = [pos], [q]
    for _ in range(steps):
        x, qq = rk4_step(velocity, X[-1], Q[-1], dt)
        X.append(x), Q.append(qq)
        if min_contact(shapes, x, qq) < floor:
            break
    return np.array(X), np.array(Q)


def eval_dynamics(args) -> None:
    op, modes = operator(args)
    if args.case == "ring":
        pos, q, shapes = ring_config(args.kinds, args.P, args.contact)
    else:
        pos, q, shapes = tilted_pair_config(args.kinds, args.contact)
    N = len(pos)
    F = np.zeros((N, 6))
    F[:, 2] = -SIX_PI
    t0 = time.time()
    truth = Truth(shapes, args.acc, args.device, warm_start=True)
    Xt, Qt = run(lambda x, qq: truth.velocities(x, qq, shapes, F), shapes, pos, q, args.dt, args.steps)
    fell = float(abs(Xt[-1].mean(0)[2] - Xt[0].mean(0)[2]))
    name = f"{args.case}_{args.name or '_'.join(args.kinds)}"
    lines = [f"# Dynamics: {args.case} of {', '.join(shapes)} under gravity", "",
             f"MFS ({args.acc}) at every RK4 stage, dt {args.dt}: {len(Xt) - 1} steps, fell {fell:.1f}, {time.time() - t0:.0f} s.",
             "", "| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |", "|---|---|---|---|---|"]
    out = {"truth_steps": len(Xt) - 1, "fell": fell}

    def compare(X, Q):
        n = min(len(X), len(Xt)) - 1                              # compare at the last step both runs reached
        fallen = max(abs(Xt[n].mean(0)[2] - Xt[0].mean(0)[2]), 1e-12)
        return {"steps": len(X) - 1, "compared_at": n, "com_pct": float(100 * np.linalg.norm(X[n].mean(0) - Xt[n].mean(0)) / fallen),
                "pos_max": float(np.linalg.norm(X[n] - Xt[n], axis=1).max()),
                "axis_deg_max": float(axis_error_deg(shapes, Q[n], Qt[n]).max())}

    label = {"far": "far field", "pair": "+ two-body", "full": "+ many-body"}
    for mode in modes:
        e = compare(*run(lambda x, qq: op.apply(x, qq, shapes, F, mode), shapes, pos, q, args.dt, len(Xt) - 1))
        out[mode] = e
        lines.append(f"| {label[mode]} | {e['steps']} | {e['com_pct']:.2f} | {e['pos_max']:.3f} | {e['axis_deg_max']:.2f} |")
    ref = args.ref_acc if args.ref_acc and have_cloud(shapes, args.ref_acc) else None
    if ref:                                                         # MFS itself: the same run with the finer clouds
        try:
            tr = Truth(shapes, ref, args.device, warm_start=True)
            e = compare(*run(lambda x, qq: tr.velocities(x, qq, shapes, F), shapes, pos, q, args.dt, len(Xt) - 1))
            out["mfs"] = e
            lines.append(f"| MFS {ref} (the truth's own error) | {e['steps']} | {e['com_pct']:.3f} | {e['pos_max']:.4f} | {e['axis_deg_max']:.3f} |")
        except Exception as e:                                      # noqa: BLE001
            lines.append(f"| MFS {ref} | failed: {str(e)[:60]} | | | |")
    mlines, mcond = model_conditions(args)
    tlines, tcond = truth_conditions(args, shapes, "solved at each of the 4 RK4 stages of every step (direct solve for "
                                     f"small systems, else GMRES to {TOL_V:g} with a warm start).")
    start = (f"{args.P} particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor {args.contact:g}"
             if args.case == "ring" else
             f"two particles side by side along x at contact factor {args.contact:g}, long axes tilted +-45 degrees in the x-z plane")
    cond = ["", "## Conditions", ""] + mlines + [
        f"- **Start**: {start}; shapes in order: {', '.join(shapes)}.",
        f"- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt {args.dt:g}, up "
        f"to {args.steps} steps; a run stops when any pair reaches contact factor {1 + MARGIN:g}.",
        "- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the "
        "distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  "
        "`steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line)."] + tlines
    write(Path(args.results) / f"DYNAMICS_{name}", lines + cond,
          dict(out, conditions={"models": mcond, "truth": tcond, "case": args.case, "shapes": shapes, "contact": args.contact,
                                "dt": args.dt, "steps": args.steps}))


# ----------------------------------------------------------------------------------------------- ceiling
def eval_ceiling(args) -> None:
    op, modes = operator(args)
    assert op.pair is not None, "ceiling needs the pair model"
    truth = Truth(args.kinds, args.acc, args.device)
    names = modes + ["exact f_nb", "exact f_nb + exact self"]
    cache = Path(args.data) / "truth_cache" / f"ceiling_{args.name or '_'.join(args.kinds)}_{args.acc}"
    acc = {}
    for phi in args.phi:
        for N in args.N:
            for seed in range(args.seeds):
                rng = np.random.default_rng([20261111, int(round(phi * 1e6)), N, seed])
                shapes = assign_shapes(args.kinds, N, rng)
                made = uniform_config(shapes, phi, rng)
                if made is None:
                    continue
                pos, q = made
                f = cache / f"M_phi{phi:g}_N{N}_s{seed}.npz"       # the matrix is hours of MFS: kept, so a second run is free
                try:
                    if f.exists() and np.allclose(np.load(f)["pos"], pos):
                        Mt = np.load(f)["M"]
                    else:
                        Mt = truth.mobility(pos, q, shapes)
                        cache.mkdir(parents=True, exist_ok=True)
                        np.savez_compressed(f, pos=pos, q=q, M=Mt)
                    Mt = torch.as_tensor(Mt, device=op.dev)
                except Exception as e:                    # noqa: BLE001  (a solve that does not converge is skipped, not fatal)
                    print(f"phi {phi:<5g} N {N} seed {seed}: MFS failed, skipped ({str(e)[:100]})", flush=True)
                    continue
                Mt = 0.5 * (Mt + Mt.T)
                X, R, desc, _, _ = op.geometry(pos, q, shapes)
                L = P.length(desc)
                rng_nb = op.nbody.pair_cutoff if op.nbody is not None else op.pair.form.r_cut      # pair lengths
                near = (X[:, None] - X[None]).norm(dim=-1) / (L[:, None] * L[None]).sqrt() < rng_nb
                near &= ~torch.eye(N, dtype=torch.bool, device=op.dev)
                t, s_ = torch.nonzero(near, as_tuple=True)
                ar = torch.arange(N, device=op.dev)
                Ms = {m: op.grand_M(pos, q, shapes, m, psd=False) for m in modes}       # raw: what the blocks alone give
                Mc = Ms["pair"].clone().reshape(N, 6, N, 6)
                Mc[t, :, s_, :] = Mt.reshape(N, 6, N, 6)[t, :, s_, :]
                Md = Mc.clone()
                Md[ar, :, ar, :] = Mt.reshape(N, 6, N, 6)[ar, :, ar, :]
                Ms["exact f_nb"], Ms["exact f_nb + exact self"] = Mc.reshape(6 * N, 6 * N), Md.reshape(6 * N, 6 * N)
                F = torch.as_tensor(random_loads(rng, N)[..., 0].reshape(-1), device=op.dev)
                vt = (Mt @ F).reshape(N, 6).cpu().numpy()
                line = f"phi {phi:<5g} N {N} seed {seed}:"
                for m in names:
                    e = prmse((Ms[m] @ F).reshape(N, 6).cpu().numpy(), vt)
                    acc.setdefault((phi, N, m), []).append(e)
                    line += f"  {m} {e['all']:.2f}"
                print(line, flush=True)
    label = {"far": "far field", "pair": "+ two-body", "full": "+ many-body"}
    lines = [f"# Ceiling of the many-body correction, {', '.join(args.kinds)}", "",
             "PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with "
             "every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: "
             "the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).", "",
             "| phi | N | n | " + " | ".join(label.get(n, n) for n in names) + " |", "|---|---|---|" + "---|" * len(names)]
    out = {}
    for (phi, N) in sorted({(k[0], k[1]) for k in acc}):
        cells = []
        for m in names:
            v = acc[(phi, N, m)]
            mean = {k: float(np.mean([e[k] for e in v])) for k in ("all", "trans", "rot")}
            out[f"{phi:g}|{N}|{m}"] = dict(mean, n=len(v))
            cells.append(f"{mean['all']:.2f} ({mean['trans']:.2f} / {mean['rot']:.2f})")
        lines.append(f"| {phi:g} | {N} | {len(v)} | " + " | ".join(cells) + " |")
    mlines, mcond = model_conditions(args)
    tlines, tcond = truth_conditions(args, args.kinds, "the whole (6N, 6N) mobility matrix of each configuration (direct solve when "
                                     f"small, else GMRES with the plain torch kernel, velocity tolerance {TOL_V:g}, 24 unit loads at a "
                                     "time), symmetrised.")
    cond = ["", "## Conditions", ""] + mlines + [
        f"- **Configurations**: N in {args.N}, shapes {', '.join(args.kinds)} in equal numbers, uniform in a cube at phi in "
        f"{args.phi}, random orientations, contact factor >= {1 + MARGIN:g}; {args.seeds} per (phi, N); a configuration "
        "whose MFS solve does not converge is skipped (n counts those kept).",
        "- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.",
        "- **Matrices**: RAW sums (no positive-definiteness projection), so that only the blocks are compared."] + tlines
    write(Path(args.results) / f"CEILING_{args.name or '_'.join(args.kinds)}", lines + cond,
          {"cells": out, "conditions": {"models": mcond, "truth": tcond, "N": args.N, "phi": args.phi, "seeds": args.seeds}})


# ----------------------------------------------------------------------------------------------- checks
def eval_check(args) -> None:
    op, modes = operator(args)
    rng = np.random.default_rng(args.seed)
    shapes = assign_shapes(args.kinds, args.N[0], rng)
    pos, q = uniform_config(shapes, args.phi[0], rng)
    N = len(pos)
    Qr = quat_to_matrix(np.asarray(rng.normal(size=4)))
    G = torch.kron(torch.eye(N, dtype=torch.float64), torch.block_diag(*(torch.as_tensor(Qr),) * 2)).to(op.dev)
    q_rot = matrix_to_quat(Qr @ quat_to_matrix(q))
    Mt = torch.as_tensor(Truth(args.kinds, args.acc, args.device).mobility(pos, q, shapes))
    lines = [f"# Structural checks, {N} particles of {', '.join(args.kinds)} at phi {args.phi[0]:g}", "",
             "| matrix | asymmetry | smallest eigenvalue / MFS's, raw -> projected | rotation equivariance error | against MFS, %, raw -> projected |",
             "|---|---|---|---|---|"]
    lam_t = float(torch.linalg.eigvalsh(0.5 * (Mt + Mt.T)).min())
    out = {"mfs_min_eig": lam_t, "mfs_asymmetry": float((Mt - Mt.T).norm() / Mt.norm())}
    label = {"far": "far field", "pair": "+ two-body", "full": "+ many-body"}
    for mode in modes:
        Mraw = op.grand_M(pos, q, shapes, mode, psd=False)
        M = op.grand_M(pos, q, shapes, mode)
        Mr = op.grand_M(pos @ Qr.T, q_rot, shapes, mode)
        e = {"asymmetry": float((M - M.T).norm() / M.norm()), "min_eig": float(torch.linalg.eigvalsh(0.5 * (M + M.T)).min()),
             "min_eig_raw": float(torch.linalg.eigvalsh(0.5 * (Mraw + Mraw.T)).min()),
             "rotation": float((Mr - G @ M @ G.T).norm() / M.norm()), "vs_mfs_pct": rel(M.cpu(), 0.5 * (Mt + Mt.T)),
             "vs_mfs_pct_raw": rel(Mraw.cpu(), 0.5 * (Mt + Mt.T))}
        out[mode] = e
        lines.append(f"| {label[mode]} | {e['asymmetry']:.1e} | {e['min_eig_raw'] / lam_t:.4f} -> {e['min_eig'] / lam_t:.4f} | "
                     f"{e['rotation']:.1e} | {e['vs_mfs_pct_raw']:.2f} -> {e['vs_mfs_pct']:.2f} |")
    lines.append(f"| MFS {args.acc} (the truth) | {out['mfs_asymmetry']:.1e} | 1 | | 0 |")
    ref = args.ref_acc if args.ref_acc and have_cloud(args.kinds, args.ref_acc) else None
    if ref:
        try:
            Mr = torch.as_tensor(Truth(args.kinds, ref, args.device).mobility(pos, q, shapes))
            out["mfs"] = {"asymmetry": float((Mr - Mr.T).norm() / Mr.norm()),
                          "min_eig": float(torch.linalg.eigvalsh(0.5 * (Mr + Mr.T)).min()),
                          "vs_mfs_pct": rel(0.5 * (Mt + Mt.T), 0.5 * (Mr + Mr.T))}
            lines.append(f"| MFS {ref} | {out['mfs']['asymmetry']:.1e} | {out['mfs']['min_eig'] / lam_t:.4f} | | "
                         f"{out['mfs']['vs_mfs_pct']:.3f} (= the error of the {args.acc} truth) |")
        except Exception as e:                                      # noqa: BLE001
            lines.append(f"| MFS {ref} | failed: {str(e)[:60]} | | | |")
    lines += ["", f"MFS smallest eigenvalue {lam_t:.4e} (positive).  A ratio > 0 means that matrix is positive definite on "
              "this configuration.  The operators are symmetric by construction; 'raw' is the sum of the blocks, the operator "
              "itself is projected onto the positive semi-definite matrices (psd.py), which is positive definite always."]
    mlines, mcond = model_conditions(args)
    tlines, tcond = truth_conditions(args, args.kinds, "the whole mobility matrix of the configuration (direct solve when "
                                     f"small, else GMRES to {TOL_V:g}).")
    cond = ["", "## Conditions", ""] + mlines + [
        f"- **Configuration**: ONE random suspension, N = {N}, shapes {', '.join(args.kinds)} in equal numbers, phi "
        f"{args.phi[0]:g}, random orientations, contact factor >= {1 + MARGIN:g}, seed {args.seed}.",
        "- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; "
        "equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = "
        "Frobenius error of the whole matrix (%)."] + tlines
    write(Path(args.results) / f"CHECK_{args.name or '_'.join(args.kinds)}", lines + cond,
          dict(out, conditions={"models": mcond, "truth": tcond, "N": N, "phi": args.phi[0], "seed": args.seed}))


# ----------------------------------------------------------------------------------------------- positive definiteness
def eval_pd(args) -> None:
    """Is the RAW operator positive definite, how often, and if not: which particles do it?  No MFS solve is needed for
    the suspensions (the sign of the smallest eigenvalue is a property of the operator alone), so many configurations
    are tested.  The smallest eigenvalue is given relative to the far-field operator's on the same configuration.  And
    how much psd.py's projection changes each operator (relative size of the change, in the metric of the isolated
    particles; 0 where the raw matrix already is positive definite)."""
    op, modes = operator(args)
    change = {}
    label = {"far": "far field", "pair": "+ two-body", "full": "+ many-body"}
    stats, worst = {}, {}
    for phi in args.phi:
        for N in args.N:
            for seed in range(args.seeds):
                rng = np.random.default_rng([20261113, int(round(phi * 1e6)), N, seed])
                shapes = assign_shapes(args.kinds, N, rng)
                made = uniform_config(shapes, phi, rng)
                if made is None:
                    continue
                pos, q = made
                lam_far = None
                for mode in modes:
                    raw = op.grand_M(pos, q, shapes, mode, psd=False)
                    w, V = torch.linalg.eigh(raw)
                    _, info = PSD.project_mobility(raw, shapes, op.geometry(pos, q, shapes)[1], op.acc, op.psd_floor)
                    change.setdefault((phi, N, mode), []).append(info["changed"])
                    lam_far = float(w[0]) if mode == "far" else lam_far
                    r = float(w[0]) / lam_far
                    stats.setdefault((phi, N, mode), []).append(r)
                    if r < worst.get(mode, (np.inf,))[0]:
                        worst[mode] = (r, phi, N, seed, pos, q, shapes, V[:, 0].cpu().numpy())
            print(f"phi {phi:g} N {N}: " + "  ".join(f"{m} min {min(stats[(phi, N, m)]):.3f}" for m in modes if (phi, N, m) in stats), flush=True)
    lines = [f"# Positive definiteness of the raw operator, {', '.join(args.kinds)}", "",
             "Per (phi, N): how many random suspensions give a positive definite RAW grand mobility matrix (the sum of the "
             "blocks, before psd.py's projection), its smallest eigenvalue relative to the far-field operator's on the same "
             "configuration (smallest / median over the configurations; negative = not positive definite), and how much "
             "the projection changes the matrix (largest relative change, % in the metric of the isolated particles).  "
             "The operator itself is the projected matrix: positive definite in every configuration.", "",
             "| phi | N | n | " + " | ".join(f"{label[m]}: raw positive definite; smallest eigenvalue ratio min / median; largest change by the projection" for m in modes) + " |",
             "|---|---|---|" + "---|" * len(modes)]
    out = {"cells": {}}
    for phi in args.phi:
        for N in args.N:
            cells = []
            for m in modes:
                v = stats.get((phi, N, m))
                if not v:
                    continue
                ch = change[(phi, N, m)]
                out["cells"][f"{phi:g}|{N}|{m}"] = {"n": len(v), "pd": int(sum(x > 0 for x in v)), "min": min(v), "median": float(np.median(v)),
                                                    "change_max_pct": 100 * max(ch), "change_median_pct": 100 * float(np.median(ch))}
                cells.append(f"{sum(x > 0 for x in v)} of {len(v)}; {min(v):.3f} / {np.median(v):.3f}; {100 * max(ch):.2f} %")
            if cells:
                lines.append(f"| {phi:g} | {N} | {len(stats[(phi, N, modes[0])])} | " + " | ".join(cells) + " |")
    # where the weakest mode of each learned operator lives
    lines += ["", "## The weakest configuration of each operator", "",
              "The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by "
              "its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest "
              "eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  "
              "If that number is negative the two-body model is not positive definite for this pair by itself; if it is "
              "positive the loss of definiteness comes from adding up several neighbours.", "",
              "| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | "
              "the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for mode in modes[1:]:
        r, phi, N, seed, pos, q, shapes, v = worst[mode]
        share = (v.reshape(N, 6) ** 2).sum(1)
        i, j = np.argsort(share)[::-1][:2]
        two = [shapes[i], shapes[j]]
        p2, q2 = pos[[i, j]], q[[i, j]]
        e_far = float(torch.linalg.eigvalsh(op.grand_M(p2, q2, two, "far", psd=False))[0])
        e_pair = float(torch.linalg.eigvalsh(op.grand_M(p2, q2, two, "pair", psd=False))[0])
        M = op.grand_M(pos, q, shapes, mode, psd=False).reshape(N, 6, N, 6)
        Mf = op.grand_M(pos, q, shapes, "far", psd=False).reshape(N, 6, N, 6)
        selfr = [float(torch.linalg.eigvalsh(M[k, :, k, :])[0] / torch.linalg.eigvalsh(Mf[k, :, k, :])[0]) for k in (i, j)]
        X, R, desc, _, _ = op.geometry(p2, q2, two)
        dist = float((X[1] - X[0]).norm() / P.pair_length(P.take(desc, [0]), P.take(desc, [1])))
        c = min_contact(two, p2, q2)
        nn = int(((np.linalg.norm(pos - pos[i], axis=1) < 6.0).sum() - 1))
        out[f"worst_{mode}"] = {"ratio": r, "phi": phi, "N": N, "seed": seed, "particles": [int(i), int(j)], "share": float(share[i] + share[j]),
                                "shapes": two, "distance": dist, "contact": c, "pair_alone_far": e_far, "pair_alone_model": e_pair,
                                "self_ratio": selfr, "neighbours_within_6": nn}
        lines.append(f"| {label[mode]} | {phi:g} | {N} | {seed} | {r:.3f} | {share[i] + share[j]:.2f} | {two[0]}, {two[1]} | {dist:.2f} | "
                     f"{c:.3f} | {e_far:.2e} / {e_pair:.2e} ({e_pair / e_far:.3f}) | {selfr[0]:.3f}, {selfr[1]:.3f} "
                     f"({nn} particles within 6 of the first) |")
    # the two-body model on pairs alone, against MFS
    if args.sets and op.pair is not None:
        lines += ["", "## The two-body operator on pairs alone, against MFS", "",
                  "The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on "
                  "stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.", "",
                  "| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |",
                  "|---|---|---|---|---|"]
        for tag in args.sets:
            files = sorted(glob.glob(f"{args.data}/pairs/{tag}_{args.acc}/shard_*.npz"))
            if not files:
                continue
            z = np.load(files[0])
            sh = json.loads(str(z["meta"]))["shapes"]
            ratios, info = [], []
            for k in range(min(args.max_pairs, len(z["positions"]))):
                pos, q = z["positions"][k], z["quats"][k]
                Mt = 0.5 * (z["M"][k] + z["M"][k].T)
                ratios.append(float(torch.linalg.eigvalsh(op.grand_M(pos, q, sh, "pair", psd=False))[0]) / float(np.linalg.eigvalsh(Mt)[0]))
                info.append((min_contact(sh, pos, q), float(np.linalg.norm(pos[1] - pos[0]))))
            w = int(np.argmin(ratios))
            out.setdefault("pairs", {})[tag] = {"n": len(ratios), "pd": int(sum(x > 0 for x in ratios)), "min": min(ratios),
                                                "median": float(np.median(ratios)), "worst_contact": info[w][0], "worst_distance": info[w][1]}
            lines.append(f"| {tag} | {len(ratios)} | {sum(x > 0 for x in ratios)} | {min(ratios):.3f} / {np.median(ratios):.3f} | "
                         f"{info[w][0]:.3f}, {info[w][1]:.2f} |")
    mlines, _ = model_conditions(args)
    cond = ["", "## Conditions", ""] + mlines + [
        f"- **Configurations**: N in {args.N}, shapes {', '.join(args.kinds)} in equal numbers, uniform in a cube at phi in "
        f"{args.phi}, random orientations, contact factor >= {1 + MARGIN:g}; {args.seeds} per (phi, N).  Isolated self "
        f"blocks from the `{args.acc}` clouds.",
        "- **Eigenvalues**: of the full (6N, 6N) RAW operator matrix (symmetric by construction), dense, float64."]
    write(Path(args.results) / f"PD_{args.name or '_'.join(args.kinds)}", lines + cond, out)


def eval_psd(args) -> None:
    """The projection against the truth, on the held-out clusters of the case (seed % 10 == 0, never trained on):
    MFS matrices of whole clusters of 8-96 particles that are already on disk (makedata.py clusters), so nothing is
    solved here.  Per configuration and operator mode: smallest eigenvalue relative to the isolated particles (truth,
    raw, projected), Weyl's bound |M - T|_2 in the same metric (if it exceeds the truth's smallest eigenvalue, nothing
    guarantees the raw matrix is positive definite), and the errors before and after the projection: in the metric of
    the isolated particles (where it can only decrease), and in velocity (random unit loads, gravity)."""
    op, modes = operator(args)
    files = sorted(glob.glob(f"{args.data}/clusters/{args.clusters}_{args.acc}/item*_part*.npz"))
    assert files, f"no clusters {args.data}/clusters/{args.clusters}_{args.acc}"
    label = {"far": "far field", "pair": "+ two-body", "full": "+ many-body"}
    recs, n_cfg = [], 0
    for f in files:
        z = np.load(f)
        meta = json.loads(str(z["meta"]))
        for k in range(len(z["seed"])):
            if int(z["seed"][k]) % 10 != 0 or (args.max_configs and n_cfg >= args.max_configs):
                continue
            n_cfg += 1
            pos, q, shapes = z["positions"][k], z["quats"][k], [str(x) for x in z["shapes"][k]]
            N = len(pos)
            R = op.geometry(pos, q, shapes)[1]
            T = torch.as_tensor(z["M"][k], device=op.dev)
            T = 0.5 * (T + T.T)
            W, Wi = PSD.whitening(shapes, R, op.acc)
            wn = lambda X: float(PSD._congruence(X, W).norm())
            lam_t = float(PSD.spectrum(T, shapes, R, op.acc)[0])
            rng = np.random.default_rng(int(z["seed"][k]))
            F = torch.as_tensor(rng.normal(size=(6 * N, 16)), device=op.dev)
            g = torch.zeros(N, 6, dtype=torch.float64, device=op.dev)
            g[:, 2] = -1.0
            g = g.reshape(-1, 1)
            vel = lambda M, X: float(100 * ((M - T) @ X).norm() / (T @ X).norm())
            bucket = f"{meta['family']} " + ", ".join(f"{a} {b:g}" for a, b in meta["params"].items()) + f", N {N}"
            for mode in modes:
                raw = op.grand_M(pos, q, shapes, mode, psd=False)
                prj, info = PSD.project(raw, W, Wi, op.psd_floor)
                E = PSD._congruence(raw - T, W)
                recs.append({"bucket": bucket, "family": meta["family"], "N": N, "mode": mode, "lam_truth": lam_t,
                             "lam_raw": float(PSD.spectrum(raw, shapes, R, op.acc)[0]),
                             "lam_proj": float(PSD.spectrum(prj, shapes, R, op.acc)[0]),
                             "weyl": float(torch.linalg.matrix_norm(0.5 * (E + E.T), 2)),
                             "w_raw": 100 * wn(raw - T) / wn(T), "w_proj": 100 * wn(prj - T) / wn(T),
                             "v_raw": vel(raw, F), "v_proj": vel(prj, F), "g_raw": vel(raw, g), "g_proj": vel(prj, g),
                             "changed": 100 * info["changed"]})
            print(f"{bucket}: truth {lam_t:.4f}  " + "  ".join(f"{r['mode']} raw {r['lam_raw']:+.4f} err {r['v_raw']:.2f}->{r['v_proj']:.2f}"
                                                             for r in recs[-len(modes):]), flush=True)
    assert recs, "no held-out clusters"
    lam_ts = [r["lam_truth"] for r in recs if r["mode"] == modes[0]]
    lines = [f"# Positive definiteness against the truth, held-out clusters `{args.clusters}` ({', '.join(sorted({r['bucket'].split(',')[0] for r in recs}))})", "",
             f"{n_cfg} clusters never used in training (seed % 10 == 0), their MFS matrices from disk.  Eigenvalues are relative to "
             "the isolated particles (1 = no interaction; the truth's smallest is the softest collective mode).  Weyl: "
             "|lam_min(M) - lam_min(T)| <= |M - T|_2, so where |M - T|_2 exceeds the truth's smallest eigenvalue, a raw "
             "operator with that error is positive definite only by luck.  Errors (%): W = in the metric of the isolated "
             "particles (the projection can only lower it); velocity = PRMSE of all six components under 16 random unit "
             "loads; gravity = translation under equal forces.", "",
             f"The truth: smallest eigenvalue min {min(lam_ts):.4f}, median {np.median(lam_ts):.4f} (all >= the floor "
             f"{op.psd_floor:g}: {'yes' if min(lam_ts) >= op.psd_floor else '**NO**'}, so the no-loss guarantee holds).", "",
             "## All held-out clusters", "",
             "| operator | n | raw positive definite | raw smallest eigenvalue: min / median | Weyl bound |M - T|_2: median / max | "
             "error W: raw -> projected | velocity: raw -> projected | gravity: raw -> projected | change by the projection: "
             "median / max | W error larger after the projection |", "|---|---|---|---|---|---|---|---|---|---|"]
    out = {"modes": {}, "buckets": {}, "truth_lam_min": min(lam_ts), "truth_lam_median": float(np.median(lam_ts)), "n": n_cfg}
    mean = lambda rs, k: float(np.mean([r[k] for r in rs]))
    for mode in modes:
        rs = [r for r in recs if r["mode"] == mode]
        o = {"n": len(rs), "pd_raw": sum(r["lam_raw"] > 0 for r in rs), "lam_raw_min": min(r["lam_raw"] for r in rs),
             "lam_raw_median": float(np.median([r["lam_raw"] for r in rs])), "lam_proj_min": min(r["lam_proj"] for r in rs),
             "weyl_median": float(np.median([r["weyl"] for r in rs])), "weyl_max": max(r["weyl"] for r in rs),
             "worse_w": sum(r["w_proj"] > r["w_raw"] * (1 + 1e-9) for r in rs),
             "changed_median": float(np.median([r["changed"] for r in rs])), "changed_max": max(r["changed"] for r in rs)}
        o.update({k: mean(rs, k) for k in ("w_raw", "w_proj", "v_raw", "v_proj", "g_raw", "g_proj")})
        out["modes"][mode] = o
        lines.append(f"| {label[mode]} | {o['n']} | {o['pd_raw']} of {o['n']} | {o['lam_raw_min']:+.4f} / {o['lam_raw_median']:+.4f} | "
                     f"{o['weyl_median']:.4f} / {o['weyl_max']:.4f} | {o['w_raw']:.3f} -> {o['w_proj']:.3f} | {o['v_raw']:.3f} -> "
                     f"{o['v_proj']:.3f} | {o['g_raw']:.3f} -> {o['g_proj']:.3f} | {o['changed_median']:.3f} / {o['changed_max']:.3f} | {o['worse_w']} |")
    last = modes[-1]
    lines += ["", f"## By kind of cluster ({label[last]})", "",
              "| clusters | n | truth smallest eigenvalue: min | raw smallest: min | Weyl |M - T|_2: median | raw positive definite | "
              "velocity error: raw -> projected | W error: raw -> projected |", "|---|---|---|---|---|---|---|---|"]
    for b in sorted({r["bucket"] for r in recs}, key=lambda x: (x.split()[0], recs[[r["bucket"] for r in recs].index(x)]["N"], x)):
        rs = [r for r in recs if r["bucket"] == b and r["mode"] == last]
        o = {"n": len(rs), "lam_truth_min": min(r["lam_truth"] for r in rs), "lam_raw_min": min(r["lam_raw"] for r in rs),
             "weyl_median": float(np.median([r["weyl"] for r in rs])), "pd_raw": sum(r["lam_raw"] > 0 for r in rs),
             **{k: mean(rs, k) for k in ("v_raw", "v_proj", "w_raw", "w_proj")}}
        out["buckets"][b] = o
        lines.append(f"| {b} | {o['n']} | {o['lam_truth_min']:.4f} | {o['lam_raw_min']:+.4f} | {o['weyl_median']:.4f} | {o['pd_raw']} of {o['n']} | "
                     f"{o['v_raw']:.3f} -> {o['v_proj']:.3f} | {o['w_raw']:.3f} -> {o['w_proj']:.3f} |")
    mlines, mcond = model_conditions(args)
    tlines, tcond = truth_conditions(args, args.kinds,
                                     "the whole mobility matrix of each held-out cluster as stored by makedata.py clusters (direct "
                                     "solve or GMRES), symmetrised.")
    cond = ["", "## Conditions", ""] + mlines + [
        f"- **Clusters**: `{args.data}/clusters/{args.clusters}_{args.acc}`, every configuration with seed % 10 == 0 (the "
        "validation split: never used to train the many-body or self models)" + (f", at most {args.max_configs}" if args.max_configs else "") + ".",
        f"- **Projection**: psd.py, eigenvalues of W M W^T clipped at {op.psd_floor:g}, W = blockdiag(M_iso)^(-1/2) from the "
        f"`{op.acc}` clouds; raw = the sum of the blocks.  'change' = |P(M) - M|_W / |M|_W (%)."] + tlines
    write(Path(args.results) / f"PSD_{args.name or args.clusters}", lines + cond,
          dict(out, conditions={"models": mcond, "truth": tcond, "clusters": args.clusters}))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--pair", default=None, help="pair model (.pt)")
    common.add_argument("--nbody", default=None, help="many-body model (.pt)")
    common.add_argument("--nself", default=None, help="many-body self model (.pt); used in the '+ many-body' operator")
    common.add_argument("--data", default=OUT)
    common.add_argument("--acc", default="fine")
    common.add_argument("--ref-acc", default=None, help="finer clouds to measure the error of MFS itself with (Xfine)")
    common.add_argument("--results", default="results")
    common.add_argument("--name", default=None)
    common.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    common.add_argument("--raw", action="store_true", help="do not project the operator onto positive semi-definite matrices")
    a = sub.add_parser("clouds", parents=[common])
    a.add_argument("--kinds", nargs="+", required=True)
    a = sub.add_parser("pair", parents=[common])
    a.add_argument("--sets", nargs="+", required=True)
    a.add_argument("--max-configs", type=int, default=None)
    for cmd in ("suspension", "check", "ceiling"):
        a = sub.add_parser(cmd, parents=[common])
        a.add_argument("--kinds", nargs="+", required=True)
        a.add_argument("--N", type=int, nargs="+", default={"suspension": [200], "check": [16], "ceiling": [64]}[cmd])
        a.add_argument("--phi", type=float, nargs="+", default={"suspension": [0.025, 0.05, 0.075, 0.1, 0.15, 0.2], "check": [0.1],
                                                                "ceiling": [0.05, 0.1, 0.2]}[cmd])
        a.add_argument("--seeds", type=int, default=3 if cmd == "ceiling" else 10)
        a.add_argument("--seed", type=int, default=0)
        a.add_argument("--ref-seeds", type=int, default=2, help="configurations per (phi, N) also solved with --ref-acc")
        a.add_argument("--ref-max-n", type=int, default=200, help="largest N solved with --ref-acc")
    a = sub.add_parser("pd", parents=[common])
    a.add_argument("--kinds", nargs="+", required=True)
    a.add_argument("--N", type=int, nargs="+", default=[16, 50, 100])
    a.add_argument("--phi", type=float, nargs="+", default=[0.05, 0.1, 0.15, 0.2])
    a.add_argument("--seeds", type=int, default=20)
    a.add_argument("--sets", nargs="*", default=[], help="pair test sets: the operator on two particles alone, against MFS")
    a.add_argument("--max-pairs", type=int, default=400)
    a = sub.add_parser("psd", parents=[common])
    a.add_argument("--clusters", required=True, help="cluster tag of makedata.py clusters (the case's name)")
    a.add_argument("--kinds", nargs="+", required=True)
    a.add_argument("--max-configs", type=int, default=None)
    a = sub.add_parser("dynamics", parents=[common])
    a.add_argument("--kinds", nargs="+", required=True)
    a.add_argument("--case", choices=["ring", "pair"], default="ring")
    a.add_argument("--P", type=int, default=5)
    a.add_argument("--contact", type=float, default=1.25)
    a.add_argument("--dt", type=float, default=0.1)
    a.add_argument("--steps", type=int, default=600)
    args = ap.parse_args()
    {"clouds": eval_clouds, "pair": eval_pair, "suspension": eval_suspension, "dynamics": eval_dynamics, "check": eval_check, "pd": eval_pd,
     "ceiling": eval_ceiling, "psd": eval_psd}[args.cmd](args)


if __name__ == "__main__":
    main()
