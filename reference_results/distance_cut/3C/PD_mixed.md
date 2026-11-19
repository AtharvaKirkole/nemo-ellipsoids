# Positive definiteness of the operator, triaxial_123, prolateSpheroid, oblateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 17 of 20; -0.357 / 0.640 | 20 of 20; 0.314 / 0.736 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 13 of 20; -0.427 / 0.300 | 20 of 20; 0.394 / 0.570 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 7 of 20; -0.890 / -0.042 | 20 of 20; 0.084 / 0.372 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 4 of 20; -1.657 / -0.488 | 20 of 20; 0.144 / 0.467 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.194 / -1.086 | 18 of 20; -0.124 / 0.450 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.541 / -1.676 | 17 of 20; -0.180 / 0.146 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.570 / -1.274 | 17 of 20; -0.401 / 0.436 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.421 / -2.558 | 13 of 20; -0.292 / 0.139 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.103 / -2.882 | 0 of 20; -1.490 / -1.041 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.031 / -2.632 | 12 of 20; -0.586 / 0.040 |
| 0.2 | 50 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -5.335 / -3.563 | 6 of 19; -0.675 / -0.132 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -6.606 / -4.771 | 0 of 20; -2.150 / -1.524 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -6.606 | 0.79 | oblateSpheroid, prolateSpheroid | 3.13 | 1.113 | 4.70e-03 / 1.84e-03 (0.391) | 0.440, 0.321 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 5 | -2.150 | 0.05 | triaxial_123, triaxial_123 | 13.71 | inf | 3.78e-03 / 3.78e-03 (1.000) | 0.787, 0.855 (7 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.939 / 1.000 | 1.058, 2.74 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.984 / 1.000 | 1.052, 2.44 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.983 / 1.000 | 1.070, 2.51 |
| triaxial_123__prolateSpheroid_test | 400 | 400 | 0.949 / 1.000 | 1.065, 4.42 |
| triaxial_123__oblateSpheroid_test | 400 | 400 | 0.959 / 1.000 | 1.053, 4.05 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.773 / 1.000 | 1.064, 2.52 |

## Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
