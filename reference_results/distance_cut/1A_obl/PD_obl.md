# Positive definiteness of the operator, oblateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 16 of 20; -0.184 / 0.365 | 20 of 20; 0.198 / 0.734 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 15 of 20; -0.456 / 0.229 | 20 of 20; 0.189 / 0.514 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 3 of 20; -0.772 / -0.124 | 20 of 20; 0.156 / 0.340 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -1.113 / -0.348 | 20 of 20; 0.262 / 0.537 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.178 / -0.596 | 19 of 20; -0.002 / 0.424 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.541 / -0.935 | 17 of 20; -0.099 / 0.138 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.542 / -0.650 | 20 of 20; 0.206 / 0.389 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.079 / -1.411 | 20 of 20; 0.035 / 0.223 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.513 / -1.688 | 0 of 20; -1.339 / -0.891 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.413 / -1.572 | 17 of 20; -0.068 / 0.178 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.099 / -2.236 | 15 of 20; -0.203 / 0.085 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.248 / -2.894 | 0 of 20; -1.792 / -1.513 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 1 | -3.248 | 0.64 | oblateSpheroid, oblateSpheroid | 3.34 | 1.102 | 6.16e-03 / 3.87e-03 (0.629) | 0.560, 0.607 (14 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 7 | -1.792 | 0.04 | oblateSpheroid, oblateSpheroid | 4.66 | 1.660 | 6.92e-03 / 6.89e-03 (0.995) | 0.761, 0.844 (8 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.996 / 1.000 | 1.052, 3.56 |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
- **Configurations**: N in [16, 50, 100], shapes oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
