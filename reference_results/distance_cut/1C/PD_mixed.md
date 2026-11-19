# Positive definiteness of the operator, prolateSpheroid, oblateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.552 / 0.402 | 20 of 20; 0.379 / 0.629 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 14 of 20; -0.596 / 0.225 | 20 of 20; 0.231 / 0.544 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 11 of 20; -0.685 / 0.007 | 20 of 20; 0.101 / 0.445 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -0.789 / -0.261 | 20 of 20; 0.135 / 0.508 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.709 / -0.812 | 19 of 20; -0.009 / 0.353 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.968 / -1.093 | 19 of 20; -0.050 / 0.191 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.046 / -1.197 | 20 of 20; 0.032 / 0.336 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.605 / -1.997 | 18 of 20; -0.070 / 0.189 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.385 / -2.357 | 0 of 20; -1.482 / -1.203 |
| 0.2 | 16 | 18 | 18 of 18; 1.000 / 1.000 | 0 of 18; -2.851 / -1.895 | 15 of 18; -0.218 / 0.130 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.996 / -3.093 | 7 of 20; -0.288 / -0.020 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.798 / -3.744 | 0 of 20; -2.779 / -2.289 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 11 | -4.798 | 0.77 | oblateSpheroid, oblateSpheroid | 3.32 | 1.116 | 6.58e-03 / 3.99e-03 (0.607) | 0.510, 0.488 (15 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 9 | -2.779 | 0.05 | oblateSpheroid, prolateSpheroid | 13.04 | inf | 5.66e-03 / 5.66e-03 (1.000) | 0.789, 0.605 (9 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.969 / 1.000 | 1.052, 2.35 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.990 / 1.000 | 1.051, 2.57 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.988 / 1.000 | 1.055, 2.48 |

## Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
