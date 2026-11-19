# Positive definiteness of the operator, triaxial_123, prolateSpheroid, oblateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 17 of 20; -0.348 / 0.632 | 20 of 20; 0.328 / 0.723 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 14 of 20; -0.422 / 0.317 | 20 of 20; 0.412 / 0.556 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 8 of 20; -0.867 / -0.041 | 20 of 20; 0.098 / 0.361 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 4 of 20; -1.608 / -0.451 | 20 of 20; 0.100 / 0.447 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.157 / -0.989 | 18 of 20; -0.132 / 0.408 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.471 / -1.645 | 14 of 20; -0.201 / 0.110 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.590 / -1.260 | 17 of 20; -0.391 / 0.415 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.433 / -2.554 | 13 of 20; -0.300 / 0.116 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.876 / -2.827 | 0 of 20; -1.394 / -0.940 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.050 / -2.646 | 13 of 20; -0.492 / 0.092 |
| 0.2 | 50 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -5.336 / -3.563 | 4 of 19; -0.640 / -0.108 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -6.355 / -4.709 | 0 of 20; -2.085 / -1.432 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -6.355 | 0.77 | oblateSpheroid, prolateSpheroid | 3.13 | 1.113 | 4.70e-03 / 2.10e-03 (0.447) | 0.461, 0.359 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 5 | -2.085 | 0.06 | triaxial_123, triaxial_123 | 13.71 | inf | 3.78e-03 / 3.78e-03 (1.000) | 0.827, 0.815 (9 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.944 / 1.000 | 1.057, 2.73 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.977 / 1.000 | 1.059, 3.75 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.973 / 1.000 | 1.066, 2.50 |
| triaxial_123__prolateSpheroid_test | 400 | 400 | 0.924 / 1.000 | 1.054, 3.29 |
| triaxial_123__oblateSpheroid_test | 400 | 400 | 0.945 / 1.000 | 1.068, 2.48 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.990 / 1.000 | 1.053, 3.94 |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
