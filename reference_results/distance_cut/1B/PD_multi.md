# Positive definiteness of the operator, prolate_ar2

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.310 / 0.411 | 20 of 20; 0.264 / 0.572 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -0.419 / 0.013 | 20 of 20; 0.255 / 0.405 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 8 of 20; -0.468 / -0.036 | 20 of 20; 0.190 / 0.392 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 7 of 20; -0.878 / -0.117 | 20 of 20; 0.163 / 0.438 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.153 / -0.533 | 20 of 20; 0.125 / 0.315 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.123 / -0.742 | 20 of 20; 0.016 / 0.200 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.510 / -0.729 | 19 of 20; -0.100 / 0.310 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.900 / -1.203 | 16 of 20; -0.072 / 0.145 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.128 / -1.563 | 15 of 20; -0.102 / 0.124 |
| 0.2 | 16 | 18 | 18 of 18; 1.000 / 1.000 | 0 of 18; -1.699 / -1.271 | 17 of 18; -0.034 / 0.215 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.309 / -2.048 | 11 of 20; -0.471 / 0.063 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.909 / -2.489 | 3 of 20; -0.694 / -0.161 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -3.309 | 0.71 | prolate_ar2, prolate_ar2 | 2.82 | 1.081 | 1.04e-02 / 5.04e-03 (0.485) | 0.443, 0.478 (24 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 18 | -0.694 | 0.81 | prolate_ar2, prolate_ar2 | 2.41 | 1.054 | 1.04e-02 / 3.39e-03 (0.326) | 0.444, 0.740 (24 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 400 | 400 | 0.997 / 1.000 | 1.073, 2.16 |
| prolate_ar2__prolate_ar2_test | 400 | 400 | 0.991 / 1.000 | 1.053, 2.40 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.974 / 1.000 | 1.052, 2.35 |
| prolate_ar4__prolate_ar4_test | 400 | 400 | 0.969 / 1.000 | 1.055, 4.04 |
| oblate_ar1p5__oblate_ar1p5_test | 400 | 400 | 0.991 / 1.000 | 1.054, 2.44 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.984 / 1.000 | 1.070, 2.51 |
| oblate_ar3__oblate_ar3_test | 400 | 400 | 0.746 / 1.000 | 1.077, 2.86 |
| prolate_ar2p5__prolate_ar2p5_test | 400 | 400 | 0.965 / 1.000 | 1.058, 3.29 |
| oblate_ar2p5__oblate_ar2p5_test | 400 | 400 | 0.992 / 1.002 | 1.077, 5.34 |
| prolate_ar5__prolate_ar5_test | 400 | 400 | 0.753 / 1.000 | 1.056, 3.56 |

## Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
- **Configurations**: N in [16, 50, 100], shapes prolate_ar2 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
