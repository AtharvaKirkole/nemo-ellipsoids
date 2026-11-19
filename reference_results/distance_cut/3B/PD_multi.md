# Positive definiteness of the operator, triaxial_2_4

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 15 of 20; -1.360 / 0.418 | 19 of 20; -0.084 / 0.566 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 17 of 20; -0.443 / 0.196 | 20 of 20; 0.352 / 0.524 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 4 of 20; -1.113 / -0.111 | 20 of 20; 0.150 / 0.391 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 2 of 20; -3.009 / -0.459 | 19 of 20; -0.013 / 0.393 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.478 / -1.669 | 19 of 20; -0.050 / 0.232 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.999 / -2.315 | 6 of 20; -0.761 / -0.177 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.998 / -2.537 | 13 of 20; -0.436 / 0.126 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -6.081 / -4.023 | 8 of 20; -0.768 / -0.052 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -9.102 / -4.936 | 0 of 20; -4.555 / -3.237 |
| 0.2 | 16 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -5.193 / -3.725 | 6 of 19; -0.802 / -0.095 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -14.237 / -6.376 | 0 of 20; -1.260 / -0.428 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -10.845 / -7.682 | 0 of 20; -6.364 / -4.761 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 11 | -14.237 | 0.75 | triaxial_2_4, triaxial_2_4 | 2.69 | 1.051 | 1.60e-03 / 2.25e-04 (0.140) | 0.432, 0.452 (3 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 11 | -6.364 | 0.05 | triaxial_2_4, triaxial_2_4 | 10.01 | 3.110 | 2.01e-03 / 2.01e-03 (0.998) | 0.791, 0.596 (4 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.933 / 1.000 | 1.052, 3.28 |
| triaxial_1p5_2__triaxial_1p5_2_test | 400 | 400 | 0.975 / 1.000 | 1.050, 2.24 |
| triaxial_1p5_3__triaxial_1p5_3_test | 400 | 400 | 0.957 / 1.000 | 1.066, 2.53 |
| triaxial_2_4__triaxial_2_4_test | 400 | 400 | 0.929 / 1.000 | 1.050, 3.30 |
| triaxial_2_5__triaxial_2_5_test | 400 | 400 | 0.868 / 1.000 | 1.052, 4.03 |
| triaxial_3_4__triaxial_3_4_test | 400 | 400 | 0.620 / 1.000 | 1.075, 2.75 |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 400 | 400 | 0.891 / 1.000 | 1.064, 2.98 |
| triaxial_3_6__triaxial_3_6_test | 400 | 374 | -49.376 / 0.970 | 1.051, 2.63 |

## Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_2_4 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
