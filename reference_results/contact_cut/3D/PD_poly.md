# Positive definiteness of the operator, triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 18 of 20; -0.337 / 0.924 | 20 of 20; 0.331 / 0.971 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -1.020 / 0.107 | 20 of 20; 0.392 / 0.795 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 8 of 20; -1.331 / -0.106 | 19 of 20; -0.077 / 0.685 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 8 of 20; -1.538 / -0.228 | 20 of 20; 0.292 / 0.864 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 2 of 20; -3.287 / -1.218 | 18 of 20; -0.720 / 0.536 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.144 / -2.001 | 15 of 20; -1.099 / 0.266 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 1 of 20; -4.499 / -1.565 | 18 of 20; -1.199 / 0.613 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.765 / -3.337 | 12 of 20; -0.379 / 0.121 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.315 / -3.523 | 0 of 20; -2.060 / -0.783 |
| 0.2 | 16 | 16 | 16 of 16; 1.000 / 1.000 | 0 of 16; -6.523 / -3.464 | 11 of 16; -1.397 / 0.187 |
| 0.2 | 50 | 14 | 14 of 14; 1.000 / 1.000 | 0 of 14; -6.005 / -4.792 | 6 of 14; -1.064 / -0.136 |
| 0.2 | 100 | 12 | 12 of 12; 1.000 / 1.000 | 0 of 12; -7.981 / -6.414 | 0 of 12; -9.004 / -5.581 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -7.981 | 0.66 | triaxial_1p5_2, prolateSpheroid | 2.92 | 1.051 | 4.96e-03 / 2.21e-03 (0.445) | 0.573, 0.569 (13 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 10 | -9.004 | 0.49 | oblateSpheroid_x1p5, oblateSpheroid_x1p5 | 3.35 | 1.059 | 1.88e-03 / 1.07e-03 (0.566) | -0.498, 0.697 (2 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.942 / 1.000 | 1.057, 2.73 |
| triaxial_1p5_2__triaxial_1p5_2_test | 400 | 400 | 0.980 / 1.000 | 1.056, 3.06 |
| triaxial_1p5_3__triaxial_1p5_3_test | 400 | 400 | 0.957 / 1.000 | 1.059, 3.09 |
| triaxial_2_4__triaxial_2_4_test | 400 | 400 | 0.896 / 1.000 | 1.050, 3.30 |
| triaxial_2_5__triaxial_2_5_test | 400 | 400 | 0.803 / 1.000 | 1.084, 5.24 |
| triaxial_3_4__triaxial_3_4_test | 400 | 400 | 0.890 / 1.000 | 1.061, 3.75 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.976 / 1.000 | 1.052, 2.44 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.971 / 1.000 | 1.058, 2.54 |
| triaxial_123__prolateSpheroid_test | 400 | 400 | 0.945 / 1.000 | 1.062, 4.41 |
| triaxial_123__oblateSpheroid_test | 400 | 400 | 0.962 / 1.000 | 1.064, 3.50 |
| triaxial_123__triaxial_2_5_test | 400 | 400 | 0.694 / 1.000 | 1.052, 4.90 |
| prolateSpheroid__triaxial_2_5_test | 400 | 400 | 0.859 / 1.000 | 1.060, 3.76 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.988 / 1.000 | 1.054, 2.48 |
| triaxial_123__triaxial_1p5_2_test | 400 | 400 | 0.949 / 1.000 | 1.059, 2.65 |
| triaxial_123__triaxial_2_4_test | 400 | 400 | 0.905 / 1.000 | 1.050, 3.65 |
| triaxial_123__triaxial_3_4_test | 400 | 400 | 0.795 / 1.000 | 1.062, 3.02 |
| oblateSpheroid__triaxial_1p5_2_test | 400 | 400 | 0.982 / 1.000 | 1.054, 2.47 |
| prolateSpheroid__triaxial_2_4_test | 400 | 400 | 0.928 / 1.000 | 1.062, 2.35 |
| triaxial_2_5__triaxial_3_4_test | 400 | 400 | 0.568 / 1.000 | 1.051, 2.32 |
| triaxial_123_x0p75__triaxial_123_test | 400 | 400 | 0.905 / 1.000 | 1.066, 4.26 |
| oblateSpheroid_x1p5__oblateSpheroid_test | 400 | 400 | 0.986 / 1.000 | 1.058, 3.81 |
| prolateSpheroid_x1p25__prolateSpheroid_test | 400 | 400 | 0.966 / 1.000 | 1.052, 5.17 |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 400 | 400 | 0.986 / 1.000 | 1.054, 4.10 |
| triaxial_123_x0p75__prolateSpheroid_test | 400 | 400 | 0.883 / 1.000 | 1.051, 2.01 |
| oblateSpheroid_x1p5__triaxial_123_test | 400 | 400 | 0.981 / 1.000 | 1.058, 4.09 |
| oblateSpheroid__triaxial_2_5_test | 400 | 400 | 0.570 / 1.001 | 1.070, 2.56 |
| triaxial_1p5_2__triaxial_3_4_test | 400 | 400 | 0.868 / 1.000 | 1.054, 3.25 |
| triaxial_123__triaxial_2p5_3p5_test | 400 | 400 | 0.931 / 1.000 | 1.072, 2.42 |
| prolateSpheroid__triaxial_3_6_test | 400 | 398 | -0.322 / 1.000 | 1.051, 2.54 |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 400 | 400 | 0.994 / 1.000 | 1.055, 5.39 |
| triaxial_123_x0p75__triaxial_3_4_test | 400 | 400 | 0.523 / 1.000 | 1.056, 3.10 |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 400 | 400 | 0.980 / 1.000 | 1.051, 2.86 |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
