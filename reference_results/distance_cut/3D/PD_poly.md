# Positive definiteness of the operator, triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 18 of 20; -0.349 / 0.915 | 20 of 20; 0.350 / 0.975 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -1.069 / 0.099 | 20 of 20; 0.420 / 0.814 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 8 of 20; -1.344 / -0.110 | 20 of 20; 0.129 / 0.684 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 8 of 20; -1.561 / -0.247 | 20 of 20; 0.368 / 0.889 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 2 of 20; -3.498 / -1.229 | 18 of 20; -0.576 / 0.546 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.254 / -2.038 | 16 of 20; -0.997 / 0.296 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 1 of 20; -4.482 / -1.635 | 18 of 20; -1.094 / 0.650 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.842 / -3.404 | 16 of 20; -0.434 / 0.204 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.398 / -3.617 | 0 of 20; -1.854 / -1.280 |
| 0.2 | 16 | 16 | 16 of 16; 1.000 / 1.000 | 0 of 16; -6.549 / -3.467 | 12 of 16; -1.135 / 0.328 |
| 0.2 | 50 | 14 | 14 of 14; 1.000 / 1.000 | 0 of 14; -6.032 / -4.855 | 5 of 14; -0.638 / -0.064 |
| 0.2 | 100 | 12 | 12 of 12; 1.000 / 1.000 | 0 of 12; -8.129 / -6.531 | 0 of 12; -3.669 / -2.448 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -8.129 | 0.65 | triaxial_1p5_2, prolateSpheroid | 2.92 | 1.051 | 4.96e-03 / 2.31e-03 (0.466) | 0.577, 0.570 (13 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 5 | -3.669 | 0.66 | oblateSpheroid_x1p5, triaxial_123_x0p75 | 4.41 | 1.103 | 1.97e-03 / 1.87e-03 (0.945) | 0.824, 0.769 (8 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.933 / 1.000 | 1.058, 2.74 |
| triaxial_1p5_2__triaxial_1p5_2_test | 400 | 400 | 0.978 / 1.000 | 1.057, 3.07 |
| triaxial_1p5_3__triaxial_1p5_3_test | 400 | 400 | 0.954 / 1.000 | 1.066, 2.53 |
| triaxial_2_4__triaxial_2_4_test | 400 | 400 | 0.884 / 1.000 | 1.050, 3.30 |
| triaxial_2_5__triaxial_2_5_test | 400 | 400 | 0.738 / 1.000 | 1.070, 4.01 |
| triaxial_3_4__triaxial_3_4_test | 400 | 400 | 0.491 / 1.000 | 1.058, 2.46 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.982 / 1.000 | 1.054, 3.07 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.974 / 1.000 | 1.060, 2.54 |
| triaxial_123__prolateSpheroid_test | 400 | 400 | 0.953 / 1.000 | 1.065, 4.42 |
| triaxial_123__oblateSpheroid_test | 400 | 400 | 0.964 / 1.000 | 1.053, 4.05 |
| triaxial_123__triaxial_2_5_test | 400 | 400 | 0.907 / 1.000 | 1.082, 3.22 |
| prolateSpheroid__triaxial_2_5_test | 400 | 400 | 0.835 / 1.000 | 1.055, 3.99 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.982 / 1.000 | 1.084, 2.19 |
| triaxial_123__triaxial_1p5_2_test | 400 | 400 | 0.960 / 1.000 | 1.061, 2.65 |
| triaxial_123__triaxial_2_4_test | 400 | 400 | 0.910 / 1.000 | 1.085, 2.50 |
| triaxial_123__triaxial_3_4_test | 400 | 400 | 0.764 / 1.000 | 1.065, 3.02 |
| oblateSpheroid__triaxial_1p5_2_test | 400 | 400 | 0.988 / 1.000 | 1.077, 3.11 |
| prolateSpheroid__triaxial_2_4_test | 400 | 400 | 0.912 / 1.000 | 1.064, 2.36 |
| triaxial_2_5__triaxial_3_4_test | 400 | 400 | 0.907 / 1.000 | 1.050, 2.72 |
| triaxial_123_x0p75__triaxial_123_test | 400 | 400 | 0.915 / 1.000 | 1.070, 4.28 |
| oblateSpheroid_x1p5__oblateSpheroid_test | 400 | 400 | 0.991 / 1.000 | 1.055, 3.49 |
| prolateSpheroid_x1p25__prolateSpheroid_test | 400 | 400 | 0.941 / 1.000 | 1.052, 5.18 |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 400 | 400 | 0.988 / 1.000 | 1.054, 4.11 |
| triaxial_123_x0p75__prolateSpheroid_test | 400 | 400 | 0.884 / 1.000 | 1.051, 2.01 |
| oblateSpheroid_x1p5__triaxial_123_test | 400 | 400 | 0.971 / 1.000 | 1.059, 3.96 |
| oblateSpheroid__triaxial_2_5_test | 400 | 400 | 0.354 / 0.993 | 1.052, 2.76 |
| triaxial_1p5_2__triaxial_3_4_test | 400 | 400 | 0.542 / 0.998 | 1.080, 2.91 |
| triaxial_123__triaxial_2p5_3p5_test | 400 | 400 | 0.988 / 1.001 | 1.068, 2.84 |
| prolateSpheroid__triaxial_3_6_test | 400 | 398 | -0.387 / 0.997 | 1.090, 4.33 |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 400 | 400 | 0.994 / 1.000 | 1.057, 5.39 |
| triaxial_123_x0p75__triaxial_3_4_test | 400 | 400 | 0.011 / 0.998 | 1.058, 3.10 |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 400 | 400 | 0.989 / 1.000 | 1.076, 4.76 |

## Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 165,316 ordered pairs from 261 clusters `poly` (mean 30.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
