# Positive definiteness of the operator, oblateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 16 of 20; -0.180 / 0.364 | 20 of 20; 0.194 / 0.736 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 15 of 20; -0.456 / 0.225 | 20 of 20; 0.212 / 0.509 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 3 of 20; -0.776 / -0.124 | 20 of 20; 0.174 / 0.350 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -1.113 / -0.347 | 20 of 20; 0.251 / 0.533 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.168 / -0.596 | 20 of 20; 0.091 / 0.421 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.531 / -0.939 | 17 of 20; -0.107 / 0.145 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.542 / -0.645 | 20 of 20; 0.183 / 0.384 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.062 / -1.407 | 20 of 20; 0.004 / 0.221 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.504 / -1.696 | 0 of 20; -1.215 / -0.827 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.413 / -1.570 | 18 of 20; -0.152 / 0.191 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.094 / -2.235 | 13 of 20; -0.189 / 0.066 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.244 / -2.893 | 0 of 20; -1.666 / -1.410 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 1 | -3.244 | 0.64 | oblateSpheroid, oblateSpheroid | 3.34 | 1.102 | 6.16e-03 / 3.87e-03 (0.629) | 0.560, 0.607 (14 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 8 | -1.666 | 0.04 | oblateSpheroid, oblateSpheroid | 5.85 | 1.727 | 6.88e-03 / 6.87e-03 (0.998) | 0.855, 0.962 (11 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.997 / 1.000 | 1.059, 2.69 |

## Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configurations**: N in [16, 50, 100], shapes oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
