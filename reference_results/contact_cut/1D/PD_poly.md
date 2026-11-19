# Positive definiteness of the operator, prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 16 of 20; -0.945 / 0.751 | 19 of 20; -0.103 / 0.892 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 10 of 20; -1.422 / -0.008 | 17 of 20; -0.179 / 0.436 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -0.891 / -0.263 | 17 of 20; -0.063 / 0.355 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 7 of 20; -1.404 / -0.158 | 19 of 20; -0.110 / 0.669 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.100 / -1.140 | 14 of 20; -2.229 / 0.199 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.228 / -1.899 | 10 of 20; -1.541 / -0.001 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.314 / -2.175 | 10 of 20; -0.893 / 0.003 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.313 / -2.866 | 7 of 20; -1.190 / -0.198 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.626 / -4.107 | 0 of 20; -2.466 / -2.006 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.150 / -2.741 | 5 of 20; -1.308 / -0.498 |
| 0.2 | 50 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -8.045 / -4.488 | 1 of 19; -2.495 / -0.764 |
| 0.2 | 100 | 13 | 13 of 13; 1.000 / 1.000 | 0 of 13; -6.940 / -5.738 | 0 of 13; -4.718 / -4.041 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -8.045 | 0.82 | oblateSpheroid, oblate_ar3 | 2.43 | 1.125 | 2.22e-03 / 9.27e-04 (0.418) | 0.358, 0.441 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 17 | -4.718 | 0.07 | oblate_ar3, oblateSpheroid_x1p5 | 6.17 | 1.981 | 2.07e-03 / 2.07e-03 (0.997) | 0.807, 0.623 (7 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 400 | 400 | 0.995 / 1.000 | 1.076, 2.22 |
| prolate_ar2__prolate_ar2_test | 400 | 400 | 0.988 / 1.000 | 1.053, 2.34 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.985 / 1.000 | 1.052, 2.44 |
| prolate_ar4__prolate_ar4_test | 400 | 400 | 0.970 / 1.000 | 1.077, 3.55 |
| oblate_ar1p5__oblate_ar1p5_test | 400 | 400 | 0.995 / 1.000 | 1.053, 2.44 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.984 / 1.000 | 1.066, 2.50 |
| oblate_ar3__oblate_ar3_test | 400 | 400 | 0.928 / 1.000 | 1.074, 3.24 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.988 / 1.000 | 1.054, 3.51 |
| prolate_ar2__oblateSpheroid_test | 400 | 400 | 0.973 / 1.000 | 1.059, 2.34 |
| prolate_ar4__oblate_ar3_test | 400 | 400 | 0.742 / 1.000 | 1.051, 5.20 |
| prolate_ar2__oblate_ar1p5_test | 400 | 400 | 0.985 / 1.000 | 1.051, 2.40 |
| prolate_ar1p5__oblate_ar3_test | 400 | 400 | 0.923 / 1.000 | 1.056, 2.22 |
| prolateSpheroid__prolate_ar2_test | 400 | 400 | 0.986 / 1.000 | 1.065, 2.17 |
| oblateSpheroid__oblate_ar3_test | 400 | 400 | 0.849 / 1.000 | 1.060, 2.70 |
| prolate_ar4__oblateSpheroid_test | 400 | 400 | 0.925 / 1.000 | 1.050, 2.73 |
| prolateSpheroid__oblate_ar1p5_test | 400 | 400 | 0.976 / 1.000 | 1.051, 2.81 |
| prolateSpheroid_x0p75__prolateSpheroid_test | 400 | 400 | 0.983 / 1.000 | 1.063, 2.73 |
| oblateSpheroid_x1p5__oblateSpheroid_test | 400 | 400 | 0.986 / 1.000 | 1.057, 3.26 |
| prolate_ar2_x1p5__prolate_ar2_test | 400 | 400 | 0.988 / 1.000 | 1.052, 2.93 |
| oblate_ar3_x0p75__oblate_ar3_test | 400 | 400 | 0.876 / 1.000 | 1.069, 3.38 |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 400 | 400 | 0.981 / 1.000 | 1.061, 3.17 |
| prolate_ar2_x1p5__oblateSpheroid_test | 400 | 400 | 0.969 / 1.000 | 1.055, 2.73 |
| prolate_ar2__oblate_ar3_test | 400 | 400 | 0.659 / 0.999 | 1.059, 2.31 |
| prolate_ar4__oblate_ar1p5_test | 400 | 400 | 0.670 / 0.996 | 1.053, 2.48 |
| prolate_ar2p5__oblate_ar2p5_test | 400 | 400 | 0.649 / 1.000 | 1.054, 2.19 |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 400 | 400 | 0.983 / 1.000 | 1.050, 2.90 |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 400 | 400 | 0.136 / 0.999 | 1.054, 3.37 |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 400 | 400 | 0.978 / 1.000 | 1.053, 3.71 |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
