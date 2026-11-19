# Positive definiteness of the operator, prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 16 of 20; -0.967 / 0.731 | 19 of 20; -0.111 / 0.891 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 9 of 20; -1.418 / -0.022 | 17 of 20; -0.204 / 0.411 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 5 of 20; -0.877 / -0.268 | 16 of 20; -0.117 / 0.392 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 7 of 20; -1.577 / -0.216 | 18 of 20; -0.197 / 0.661 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.381 / -1.250 | 13 of 20; -2.552 / 0.168 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.233 / -1.848 | 11 of 20; -1.662 / 0.047 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.224 / -2.283 | 10 of 20; -0.849 / 0.007 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.469 / -2.903 | 7 of 20; -1.259 / -0.172 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.729 / -4.089 | 0 of 20; -2.683 / -2.167 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.273 / -2.955 | 3 of 20; -1.688 / -0.577 |
| 0.2 | 50 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -8.109 / -4.691 | 0 of 19; -2.644 / -0.962 |
| 0.2 | 100 | 13 | 13 of 13; 1.000 / 1.000 | 0 of 13; -6.993 / -5.812 | 0 of 13; -5.093 / -4.382 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -8.109 | 0.81 | oblateSpheroid, oblate_ar3 | 2.43 | 1.125 | 2.22e-03 / 9.07e-04 (0.409) | 0.356, 0.478 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 17 | -5.093 | 0.07 | oblateSpheroid_x1p5, oblateSpheroid_x1p5 | 3.85 | 1.323 | 1.93e-03 / 1.91e-03 (0.987) | 0.739, 0.851 (11 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 400 | 400 | 0.994 / 1.000 | 1.052, 2.22 |
| prolate_ar2__prolate_ar2_test | 400 | 400 | 0.991 / 1.000 | 1.053, 2.40 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.977 / 1.000 | 1.052, 2.35 |
| prolate_ar4__prolate_ar4_test | 400 | 400 | 0.966 / 1.000 | 1.055, 4.04 |
| oblate_ar1p5__oblate_ar1p5_test | 400 | 400 | 0.966 / 1.000 | 1.053, 2.23 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.993 / 1.000 | 1.061, 2.69 |
| oblate_ar3__oblate_ar3_test | 400 | 400 | 0.899 / 1.000 | 1.080, 3.26 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.982 / 1.000 | 1.055, 2.48 |
| prolate_ar2__oblateSpheroid_test | 400 | 400 | 0.987 / 1.000 | 1.053, 2.78 |
| prolate_ar4__oblate_ar3_test | 400 | 400 | 0.791 / 1.000 | 1.052, 5.20 |
| prolate_ar2__oblate_ar1p5_test | 400 | 400 | 0.967 / 1.000 | 1.051, 2.40 |
| prolate_ar1p5__oblate_ar3_test | 400 | 400 | 0.913 / 1.000 | 1.057, 2.22 |
| prolateSpheroid__prolate_ar2_test | 400 | 400 | 0.981 / 1.000 | 1.051, 4.04 |
| oblateSpheroid__oblate_ar3_test | 400 | 400 | 0.878 / 1.000 | 1.062, 2.70 |
| prolate_ar4__oblateSpheroid_test | 400 | 400 | 0.953 / 1.000 | 1.056, 3.66 |
| prolateSpheroid__oblate_ar1p5_test | 400 | 400 | 0.984 / 1.000 | 1.059, 3.62 |
| prolateSpheroid_x0p75__prolateSpheroid_test | 400 | 400 | 0.970 / 1.000 | 1.051, 3.26 |
| oblateSpheroid_x1p5__oblateSpheroid_test | 400 | 400 | 0.992 / 1.000 | 1.055, 3.49 |
| prolate_ar2_x1p5__prolate_ar2_test | 400 | 400 | 0.992 / 1.000 | 1.058, 3.35 |
| oblate_ar3_x0p75__oblate_ar3_test | 400 | 400 | 0.525 / 1.000 | 1.061, 2.64 |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 400 | 400 | 0.984 / 1.000 | 1.057, 4.21 |
| prolate_ar2_x1p5__oblateSpheroid_test | 400 | 400 | 0.950 / 1.000 | 1.056, 2.74 |
| prolate_ar2__oblate_ar3_test | 400 | 400 | 0.465 / 1.000 | 1.061, 2.31 |
| prolate_ar4__oblate_ar1p5_test | 400 | 400 | 0.573 / 0.996 | 1.051, 2.20 |
| prolate_ar2p5__oblate_ar2p5_test | 400 | 400 | 0.390 / 1.000 | 1.055, 2.19 |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 400 | 400 | 0.969 / 1.000 | 1.052, 2.94 |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 400 | 400 | 0.503 / 0.999 | 1.054, 3.37 |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 400 | 400 | 0.880 / 1.000 | 1.058, 2.68 |

## Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
