# Learned mobility operators for suspensions of ellipsoids

Code to build, train and test a learned grand mobility operator for rigid ellipsoids in Stokes flow: spheroids
(prolate and oblate, any aspect ratio and size) and general triaxial ellipsoids, as two-body models and as full-body
operators for whole suspensions. The ground truth is the method of fundamental solutions (MFS). Every accuracy number
is reported next to the error of MFS itself under the same conditions.

The work extends NeMO (learned mobility operators for spheres) to non-spherical particles. This repository holds
everything needed to reproduce our results: the code, the MFS point clouds, our trained models (optional), and the
results we obtained.

## What is in here

| path | what |
|---|---|
| `code/` | all the code (Python + Slurm scripts); nothing outside it is imported |
| `points/` | the MFS point clouds of every particle shape, packed (`setup.sh` unpacks them) |
| `models/` | our trained models, packed (optional: only for evaluating without training) |
| `reference_results/` | the results we obtained, to compare with yours |
| `setup.sh` | unpacks clouds (and optionally models) into `workspaces/` |
| `requirements.txt` | Python packages |

## The study

Four parts, each in four rows (A one shape, B several shapes but one per suspension, C shapes mixed, D shapes and
sizes mixed). Each case of `run.sh` produces a two-body cell and its full-body cell:

| case | cells | particles |
|---|---|---|
| `1A_pro`, `1A_obl` | 1A + 2A | one shape: prolate 1:1:3, oblate 2:2:1 |
| `1B` | 1B + 2B | 7 spheroid aspect ratios, one per pair / cluster; also tested on unseen ones |
| `1C` | 1C + 2C | prolate and oblate mixed |
| `1D` | 1D + 2D | every spheroid shape and size mixed; also tested on unseen pairings |
| `3A` | 3A + 4A | one triaxial shape: 1:2:3 |
| `3B` | 3B + 4B | 6 triaxial shapes, one per pair / cluster; also tested on unseen ones |
| `3C` | 3C + 4C | 1:2:3, prolate and oblate mixed |
| `3D` | 3D + 4D | every shape and size mixed; also tested on unseen pairings |

Parts 1 and 3 are two-body accuracy (pairs); parts 2 and 4 are full suspensions (up to 300 particles, volume fraction
up to 0.2), ring sedimentation and pair dynamics, all against MFS.

## Requirements

- Linux with an NVIDIA GPU (we used V100 32 GB). The truth solver also runs on a CPU, but only the tests and the smoke
  run are practical there.
- Python >= 3.10 with `pip install -r requirements.txt` (install PyTorch for your CUDA version first).
- For speed, the CUDA toolkit (`nvcc` on `PATH`): the MFS kernel is compiled on first use. Without it the solver
  falls back to a dense path that gives the same answers 60-100 times slower.
- For the full runs, a Slurm cluster. Everything also runs without Slurm (`LOCAL=1`), one step after another.

`code/env.sh` is sourced by every job. It activates `$NEMO_VENV`, or `<repo>/.venv`, and on clusters with Lmod
tries to load a CUDA module. Edit it if your cluster needs something else.

## Setup

```bash
git clone <this repo> && cd <repo>
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
bash setup.sh              # clouds only (full reproduction)
# or: bash setup.sh --models   # clouds + our trained models (evaluation only)
```

This creates two workspaces, `workspaces/spheroid` and `workspaces/triaxial`. The two forms of the model use separate
workspaces because their pair data share names but not ranges. All generated data goes there (`data/final`);
results go to `results/`, job logs to `logs/`.

## Run

### 1. Check that everything works (minutes, CPU is fine)

```bash
cd workspaces/triaxial && python ../../code/tests.py && cd ../..
SMOKE=1 LOCAL=1 bash code/run.sh 3A
```

`tests.py` checks everything that holds by construction, for both forms (19 tests): rotation and reflection
equivariance, reciprocity, size scaling, continuity, the far field, the periodic sum, the stress model. The smoke run
goes through the whole pipeline on coarse clouds with tiny models, ending in `results_smoke/REPORT.md`. Its numbers
mean nothing; it only proves the chain runs.

### 2. Evaluate our trained models (needs `setup.sh --models`)

```bash
EVAL_ONLY=1 bash code/run.sh             # all 9 cases; or name some: EVAL_ONLY=1 bash code/run.sh 1A_pro 3A
```

This skips all training data and training. It generates only the test pairs, the MFS reference solves and the
suspension tests, then writes `results/REPORT.md`.

### 3. Full reproduction (clouds only)

```bash
bash code/run.sh                         # all 9 cases, every stage, as Slurm jobs
DRY=1 bash code/run.sh                   # print the jobs without submitting
```

Per case, the stages are: MFS pair data → two-body model → MFS cluster data → many-body rows → many-body model and
self model → evaluation → report. Each stage is skipped when its output exists, so the script can be run again
after a failure, or with `REDO="clusters rows nbody"` to rebuild stages. Every job is under 4 hours; long stages are
chains of resumable jobs. Job names start with their paper cell (`1A_...`, `4D_...`).

Cost, roughly: our run was about 1,000 Slurm jobs on single V100s, most of the time in MFS solves of the 64- and
96-particle clusters (up to 3 hours each for the polydisperse triaxial case). Plan for on the order of a thousand
GPU-hours for everything; case 1A alone is much less.

### Other scripts (optional)

| command | what |
|---|---|
| `CUT=contact bash code/run.sh` | the variant where the learned range is set by contact factor (< 4) instead of distance; results in `results_contact/` |
| `bash code/experiments.sh` | physics experiments with MFS at every step: orbits of two settling particles, three settling particles, a settling cloud, short-time diffusion, spinners, a flexible fibre |
| `bash code/stress.sh` | stresslet / strain truth and a two-body stress model, and periodic-box numbers (hindered settling, viscosity) |
| `bash code/movies.sh` | movies of settling spheroids (MFS against the operator) |

These need the models of the main run (`pair_*.pt`, `nbody_*.pt`, `nself_*.pt`) in the workspaces.

## What to compare with

`reference_results/distance_cut/REPORT.md` is our main result: two summary tables (two-body, full body), then every
result with its conditions and the MFS error beside it. `reference_results/contact_cut/` is the contact-factor
variant; `experiments/`, `bulk/` and `stress_models/` are the optional scripts.

Configurations are seeded one by one, so your training and test data are identical to ours. GPU training is not
bit-reproducible, so expect the model numbers to agree within the spread of training seeds (for the two-body cells
about ±0.001-0.003 percentage points; the report lists the spread of 3 seeds where we ran them).

Our headline numbers (% error against MFS on fine clouds; translation / rotation):

| | two-body, one shape | full body, 200 particles, volume fraction 0.1 / 0.2 |
|---|---|---|
| prolate spheroid 1:1:3 | 0.033 / 0.31 (MFS's own error 0.026 / 0.24) | 5.2 / 8.5 (far field alone 13.9 / 27.3) |
| oblate spheroid 2:2:1 | 0.019 / 0.16 (MFS 0.013 / 0.036) | 4.7 / 7.2 |
| triaxial 1:2:3 | 0.061 / 0.30 (MFS 0.078 / 0.46) | 5.6 / 8.7 |

## Known limitations

Stated so that nobody is surprised by them:

- **Positive definiteness is not built in.** The two-body blocks are positive definite pair by pair, and the full
  operator is positive definite for small or dilute systems, but at volume fraction >= 0.15 with 100 particles almost no configuration gives a
  positive definite matrix (see `PD_*.md` in each case). Adding pairs in mobility space causes this even with exact
  pair data. This does not affect the velocity accuracy above, but it rules out Brownian dynamics in dense systems.
- **The many-body model is trained on finite clusters in unbounded fluid.** It must not be used in a periodic box:
  there it produces unphysical results (particles settling upwards in `reference_results/bulk/`). The far field and
  the two-body model are fine in a periodic box.
- **Nothing is learned below contact factor 1.05** (no lubrication limit). Simulations stop when a pair gets that close.
- **There is no truth for periodic boxes**; the periodic numbers are checked only against known sphere results.
- In `reference_results/experiments/`, the three-oblate run started from an overlapping configuration (fixed in the
  code since), and the diffusion runs used no self model.
- Full-body accuracy (5-13 %) is far above the MFS floor (0.01-0.1 %); the two-body models are at that floor.

## Code map

| file | what |
|---|---|
| `geometry.py` | shapes, quaternions, contact factor, configurations |
| `truth.py`, `truth_mfs/` | MFS truth: direct and iterative solvers, the exact isolated ellipsoid, stress and strain |
| `farfield.py` | the 12-point far field of any two ellipsoids (+ stresslets and strain) |
| `pair.py` | the two-body model, both forms (spheroid: 12 inputs; triaxial: 22 inputs) |
| `nbody.py` | the many-body correction of cross blocks and of self blocks |
| `mobility.py` | the assembled operator: far field, + two-body, + many-body |
| `makedata.py`, `train.py` | data generation and training (resumable) |
| `evaluate.py`, `report.py` | every test and the combined report |
| `periodic.py`, `stress.py` | periodic box, stress model |
| `experiments.py`, `movie.py` | physics experiments, movies |
| `tests.py` | tests of what holds by construction |
| `run.sh`, `experiments.sh`, `stress.sh`, `movies.sh`, `env.sh` | the pipelines as Slurm jobs, and the job environment |

Shapes are registered in `data/points/shapes.json` of each workspace (name → three semi-axes). A new shape needs its
clouds (`b_<name>_<acc>.txt` boundary nodes, `s_<name>_<acc>.txt` sources) for each accuracy level used.
