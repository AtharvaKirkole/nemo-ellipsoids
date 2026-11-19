#!/usr/bin/env python3
"""One report from everything in results/<case>/: results/REPORT.md.

    python report.py

Two summary tables (two-body, full body) with, next to every model error, the error of MFS itself under the same
conditions; then, per case, every result file as written by evaluate.py, each with its full list of conditions.
Needs only the standard library: it reads the .json / .md files, it computes nothing.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "results"
CASES = {  # case: (two-body cell, full-body cell, name, what)
    "1A_pro": ("1A", "2A", "pro", "spheroid form, one shape: prolate 1:1:3"),
    "1A_obl": ("1A", "2A", "obl", "spheroid form, one shape: oblate 2:2:1"),
    "1B": ("1B", "2B", "multi", "spheroid form, many shapes (7 aspect ratios), one shape per pair / cluster"),
    "1C": ("1C", "2C", "mixed", "spheroid form, prolate and oblate mixed"),
    "1D": ("1D", "2D", "poly", "spheroid form, every shape and size mixed"),
    "3A": ("3A", "4A", "t123", "triaxial form, one shape: 1:2:3"),
    "3B": ("3B", "4B", "multi", "triaxial form, many shapes (6 triaxial), one shape per pair / cluster"),
    "3C": ("3C", "4C", "mixed", "triaxial form, 1:2:3 + prolate + oblate mixed"),
    "3D": ("3D", "4D", "poly", "triaxial form, every shape and size mixed"),
}


def load(path: Path):
    return json.load(open(path)) if path.exists() else None


def rng(vals, d=3) -> str:
    vals = [v for v in vals if v is not None]
    if not vals:
        return "not measured"
    lo, hi = min(vals), max(vals)
    return f"{lo:.{d}f}" if abs(hi - lo) < 0.5 * 10 ** -d else f"{lo:.{d}f}-{hi:.{d}f}"


def tr(e, d=3) -> str:
    return f"{e['trans']:.{d}f} / {e['rot']:.{d}f}" if e else "not measured"


def two_body_row(case: str) -> str | None:
    cell, _, name, _ = CASES[case]
    j = load(RES / case / f"PAIR_pair_{name}.json")
    if not j:
        return None
    trained = set(j["conditions"]["models"]["pair"].get("train_sets") or [])
    seen = {k: e for k, e in j["sets"].items() if k.removesuffix("_test") in trained}
    unseen = {k: e for k, e in j["sets"].items() if k not in seen}
    both = lambda sets, key, sub=None: (rng([(e.get(sub) or {}).get(key) if sub else e.get(key) for e in sets.values()]))
    pair = lambda sets, sub=None: f"{both(sets, 'trans', sub)} / {both(sets, 'rot', sub)}"
    spread = ""
    seeds = [load(p) for p in sorted((RES / case).glob(f"PAIR_pair_{name}_s*.json"))]
    if seeds:
        allv = [[e["trans"] for k, e in s["sets"].items() if k in seen] for s in [j] + seeds]
        mean = [sum(v) / len(v) for v in allv if v]
        spread = f"{min(mean):.3f}-{max(mean):.3f} ({len(mean)} seeds)"
    return (f"| {cell} | {case} | {len(seen)} | {pair(seen)} | {pair(seen, 'mfs_resolution')} | {pair(seen, 'model_vs_ref')} | "
            f"{pair(seen, 'mfs_reciprocity')} | {pair(seen, 'far_only')} | "
            f"{(str(len(unseen)) + ': ' + pair(unseen)) if unseen else 'none'} | {spread or 'one seed'} |")


def full_body_row(case: str) -> str | None:
    _, cell, name, _ = CASES[case]
    f3 = load(RES / case / f"SUSPENSION_{name}_fig3.json")
    if not f3:
        return None
    N = max(int(k.split("|")[1]) for k in f3["cells"])

    def sus(phi):
        c = lambda m: f3["cells"].get(f"{phi:g}|{N}|{m}")
        if not c("far"):
            return "not run", "not run"
        ops = " -> ".join(f"{c(m)['all']:.2f}" for m in ("far", "pair", "full") if c(m))
        full = c("full") or c("pair") or c("far")
        return f"{ops} ({full['trans']:.2f} / {full['rot']:.2f})", (f"{c('mfs')['all']:.3f} ({tr(c('mfs'))})" if c("mfs") else "not measured")

    phis = sorted({float(k.split("|")[0]) for k in f3["cells"]})
    a, b = (min(phis, key=lambda x: abs(x - 0.1)), max(phis))
    (s1, m1), (s2, m2) = sus(a), sus(b)
    ck = load(RES / case / f"CHECK_{name}.json") or {}
    op = ck.get("full") or ck.get("pair") or {}
    chk = f"{op['vs_mfs_pct']:.2f}" if op else "not run"
    chk_m = f"{ck['mfs']['vs_mfs_pct']:.3f}" if ck.get("mfs") else "not measured"
    ps = load(RES / case / f"PSD_{name}.json") or {}
    pm = (ps.get("modes") or {})
    pm = pm.get("full") or pm.get("pair") or {}
    if pm:
        after = pm["n"] if pm.get("lam_proj_min", 0) > 0 else "**NOT ALL**"
        pd = (f"before the fix {pm['pd_raw']} of {pm['n']} -> after {after} of {pm['n']} (velocity error {pm['v_raw']:.2f} -> {pm['v_proj']:.2f})")
    elif op:
        pd = (f"raw {'yes' if op.get('min_eig_raw', op['min_eig']) > 0 else 'no'}; operator {'yes' if op['min_eig'] > 0 else '**NO**'}")
    else:
        pd = "not run"
    dy = load(RES / case / f"DYNAMICS_ring_{name}.json") or {}
    ring = " -> ".join(f"{dy[m]['com_pct']:.2f}" for m in ("far", "pair", "full") if m in dy) or "not run"
    ring_m = f"{dy['mfs']['com_pct']:.3f}" if dy.get("mfs") else "not measured"
    return (f"| {cell} | {case} | {N} | {a:g}: {s1} | {m1} | {b:g}: {s2} | {m2} | {chk} | {chk_m} | {pd} | {ring} | {ring_m} |")


def psd_row(case: str) -> str | None:
    _, cell, name, _ = CASES[case]
    ps, pdj = load(RES / case / f"PSD_{name}.json"), load(RES / case / f"PD_{name}.json")
    if not ps and not pdj:
        return None
    raw = "not run"
    if pdj:
        cells = [v for k, v in pdj["cells"].items() if k.endswith("|full")] or [v for k, v in pdj["cells"].items() if k.endswith("|pair")]
        if cells:
            raw = (f"{sum(c['pd'] for c in cells)} of {sum(c['n'] for c in cells)}; worst {min(c['min'] for c in cells):+.2f}; "
                   f"largest change {max(c.get('change_max_pct', float('nan')) for c in cells):.2f} %")
    if ps:
        m = ps["modes"].get("full") or ps["modes"].get("pair")
        held = (f"{ps['n']} | {ps['truth_lam_min']:.4f} | {m['lam_raw_min']:+.4f} | {m['weyl_median']:.3f} | {m['pd_raw']} -> {m['n'] if m.get('lam_proj_min', 0) > 0 else '**NOT ALL**'} of {m['n']} | "
                f"{m['w_raw']:.2f} -> {m['w_proj']:.2f} | {m['v_raw']:.2f} -> {m['v_proj']:.2f} | {m['worse_w']}")
    else:
        held = "not run | | | | | | |"
    return f"| {cell.replace('1', '2').replace('3', '4')} | {case} | {raw} | {held} |"


def resolutions() -> tuple:
    """(acc, ref) of the results: read from the first result that states them."""
    for f in sorted(RES.glob("*/*.json")):
        t = (load(f).get("conditions") or {}).get("truth") or {}
        if t.get("acc"):
            return t["acc"], t.get("ref_acc") or "Xfine"
    return "fine", "Xfine"


def main():
    acc, ref = resolutions()
    text = build(acc, ref)
    out = RES / "REPORT.md"
    out.write_text(text.replace("fine vs Xfine", f"{acc} vs {ref}").replace("on fine clouds", f"on {acc} clouds")
                   .replace("model vs Xfine", f"model vs {ref}"), encoding="utf-8")
    print(f"-> {out}")


def build(acc: str, ref: str) -> str:
    lines = ["# Accuracy of the two-body and full-body models, with the error of MFS itself", "",
             f"Built {time.strftime('%Y-%m-%d %H:%M')} by `report.py` from `{RES.name}/<case>/`.  All numbers are % errors "
             "against MFS on fine clouds unless a column says otherwise.  trans / rot = translation / rotation.", "",
             "How to read the MFS columns: a model error is only meaningful down to the error of the truth it is "
             "compared with.  `MFS fine vs Xfine` is the same test solved with both cloud resolutions, in the same "
             "metric; `reciprocity` is how far the raw MFS blocks are from the symmetry the exact ones have.  Where a "
             "model error is close to these, the model is at the floor of its labels and cannot be shown to be better.", "",
             "## 1. Two-body (cells 1A-1D spheroid form, 3A-3D triaxial form)", "",
             "Pair test sets (unseen seeds), one random unit force and torque on the source, PRMSE of the target's "
             "velocity.  Ranges are over the test sets of the pairings the model was trained on.", "",
             "| cell | case | trained pairings tested | model: trans / rot | MFS fine vs Xfine: trans / rot | model vs Xfine: trans / rot | "
             "MFS reciprocity defect: trans / rot | far field alone: trans / rot | pairings never trained on: trans / rot | "
             "mean trans over training seeds |", "|---|---|---|---|---|---|---|---|---|---|"]
    rows = [two_body_row(c) for c in CASES if (RES / c).is_dir()]
    lines += [r for r in rows if r] or ["| (no pair results yet) | | | | | | | | | |"]
    lines += ["", "## 2. Full body (cells 2A-2D spheroid form, 4A-4D triaxial form)", "",
              "Suspensions in unbounded fluid, random unit forces and torques on every particle, PRMSE of all six "
              "velocity components: far field -> + two-body -> + many-body (translation / rotation of the last).  "
              "Whole matrix = Frobenius error of the full operator's grand mobility matrix on one small "
              "suspension (16 particles in the full runs).  Ring = centre-of-mass error (% of the distance fallen) of 5 particles sedimenting.", "",
              "| cell | case | N | phi: far -> two-body -> many-body (trans / rot) | MFS fine vs Xfine | phi: far -> two-body -> many-body (trans / rot) | "
              "MFS fine vs Xfine | whole matrix vs MFS | MFS fine vs Xfine (matrix) | positive definite (held-out clusters) | ring: far -> two-body -> many-body | "
              "MFS fine vs Xfine (ring) |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    rows = [full_body_row(c) for c in CASES if (RES / c).is_dir()]
    lines += [r for r in rows if r] or ["| (no suspension results yet) | | | | | | | | | | | |"]
    lines += ["", "## 3. Positive definiteness", "",
              "Every operator matrix is projected onto the positive semi-definite matrices in the metric of the isolated "
              "particles (psd.py), so the operator is positive definite in every configuration.  'Raw' is the sum of the "
              "blocks before that step.  Random suspensions: the PD test (N 16-100, phi 0.05-0.2), + many-body operator.  "
              "Held-out clusters: MFS matrices of clusters never used in training; eigenvalues relative to the isolated "
              "particles; Weyl |M - T|_2 = the spectral norm of the raw error, which bounds how far the raw smallest "
              "eigenvalue can be from the truth's.  The last column must be 0: the projection never moves the operator "
              "further from the truth in its metric.", "",
              "| cell | case | raw positive definite, random suspensions; worst eigenvalue ratio; largest change by the projection | "
              "held-out clusters | truth's smallest eigenvalue (min) | raw smallest (min) | Weyl |M - T|_2 (median) | positive definite: before -> after the fix | "
              "error in the metric: raw -> projected | velocity error: raw -> projected | worse after the projection |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    rows = [psd_row(c) for c in CASES if (RES / c).is_dir()]
    lines += [r for r in rows if r] or ["| (no positive-definiteness results yet) | | | | | | | | | | |"]
    lines += ["", "## 4. Every result, with its conditions", ""]
    for case, (c2, cf, name, what) in CASES.items():
        files = sorted((RES / case).glob("*.md")) if (RES / case).is_dir() else []
        if not files:
            continue
        lines += [f"### Case {case} (cells {c2} and {cf}): {what}", ""]
        order = {"CLOUDS": 0, "PAIR": 1, "SUSPENSION": 2, "DYNAMICS": 3, "CHECK": 4, "PD": 5, "PSD": 6, "SPEED": 7, "CEILING": 8}
        for f in sorted(files, key=lambda p: (order.get(p.stem.split("_")[0], 9), p.name)):
            body = f.read_text(encoding="utf-8").strip().splitlines()
            lines += ["#" * 3 + ln if ln.startswith("#") else ln for ln in body] + [""]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
