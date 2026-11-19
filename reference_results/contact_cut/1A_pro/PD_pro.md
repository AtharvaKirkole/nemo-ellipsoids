# Positive definiteness of the operator, prolateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.032 / 0.466 | 20 of 20; 0.344 / 0.679 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 11 of 20; -0.665 / 0.019 | 20 of 20; 0.194 / 0.422 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 10 of 20; -0.367 / -0.013 | 20 of 20; 0.295 / 0.419 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -1.198 / -0.432 | 20 of 20; 0.140 / 0.400 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.066 / -1.084 | 19 of 20; -0.084 / 0.273 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.244 / -1.297 | 11 of 20; -0.409 / 0.040 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.967 / -0.978 | 18 of 20; -0.108 / 0.296 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.387 / -1.998 | 14 of 20; -0.506 / 0.064 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.003 / -2.464 | 0 of 20; -2.055 / -1.566 |
| 0.2 | 16 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -3.650 / -1.927 | 14 of 19; -0.231 / 0.121 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.988 / -3.271 | 1 of 20; -0.607 / -0.138 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.568 / -3.896 | 0 of 20; -2.861 / -2.499 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 17 | -4.988 | 0.68 | prolateSpheroid, prolateSpheroid | 2.27 | 1.106 | 3.88e-03 / 2.35e-03 (0.605) | 0.322, 0.470 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 2 | -2.861 | 0.04 | prolateSpheroid, prolateSpheroid | 11.83 | 5.536 | 5.64e-03 / 5.64e-03 (1.000) | 0.764, 0.808 (10 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.984 / 1.000 | 1.053, 2.23 |

## Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
