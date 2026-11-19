# Positive definiteness of the operator, triaxial_2_4

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 15 of 20; -1.327 / 0.422 | 19 of 20; -0.044 / 0.580 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 17 of 20; -0.466 / 0.204 | 20 of 20; 0.315 / 0.519 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 4 of 20; -1.155 / -0.131 | 20 of 20; 0.132 / 0.395 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 2 of 20; -2.992 / -0.448 | 19 of 20; -0.038 / 0.396 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.463 / -1.675 | 18 of 20; -0.068 / 0.244 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.025 / -2.333 | 8 of 20; -0.721 / -0.116 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.991 / -2.539 | 14 of 20; -0.301 / 0.187 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -6.046 / -4.041 | 10 of 20; -0.602 / -0.005 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -9.444 / -4.941 | 0 of 20; -4.410 / -2.950 |
| 0.2 | 16 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -5.212 / -3.716 | 7 of 19; -0.612 / -0.059 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -13.924 / -6.386 | 0 of 20; -1.062 / -0.406 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -10.942 / -7.635 | 0 of 20; -6.204 / -4.469 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 11 | -13.924 | 0.73 | triaxial_2_4, triaxial_2_4 | 2.69 | 1.051 | 1.60e-03 / 2.52e-04 (0.157) | 0.433, 0.453 (3 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 11 | -6.204 | 0.05 | triaxial_2_4, triaxial_2_4 | 19.11 | inf | 2.10e-03 / 2.10e-03 (1.000) | 0.807, 0.652 (4 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.937 / 1.000 | 1.057, 2.73 |
| triaxial_1p5_2__triaxial_1p5_2_test | 400 | 400 | 0.974 / 1.000 | 1.050, 2.24 |
| triaxial_1p5_3__triaxial_1p5_3_test | 400 | 400 | 0.963 / 1.000 | 1.059, 3.09 |
| triaxial_2_4__triaxial_2_4_test | 400 | 400 | 0.912 / 1.000 | 1.050, 3.30 |
| triaxial_2_5__triaxial_2_5_test | 400 | 400 | 0.734 / 1.000 | 1.061, 2.60 |
| triaxial_3_4__triaxial_3_4_test | 400 | 400 | 0.875 / 1.000 | 1.061, 3.75 |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 400 | 400 | 0.874 / 1.000 | 1.062, 2.97 |
| triaxial_3_6__triaxial_3_6_test | 400 | 389 | -1.984 / 0.992 | 1.073, 6.43 |

## Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_2_4 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
