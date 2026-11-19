# Positive definiteness of the operator, prolateSpheroid, oblateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.555 / 0.406 | 20 of 20; 0.382 / 0.632 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 14 of 20; -0.588 / 0.231 | 20 of 20; 0.235 / 0.534 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -0.673 / 0.008 | 20 of 20; 0.105 / 0.427 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -0.790 / -0.254 | 20 of 20; 0.126 / 0.506 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.696 / -0.797 | 19 of 20; -0.005 / 0.362 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.964 / -1.072 | 19 of 20; -0.083 / 0.164 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.039 / -1.194 | 20 of 20; 0.021 / 0.353 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.555 / -1.978 | 17 of 20; -0.035 / 0.184 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.353 / -2.305 | 0 of 20; -1.412 / -1.153 |
| 0.2 | 16 | 18 | 18 of 18; 1.000 / 1.000 | 0 of 18; -2.852 / -1.899 | 14 of 18; -0.175 / 0.111 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.954 / -3.074 | 6 of 20; -0.302 / -0.060 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.763 / -3.713 | 0 of 20; -2.387 / -1.924 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 11 | -4.763 | 0.77 | oblateSpheroid, oblateSpheroid | 3.32 | 1.116 | 6.58e-03 / 3.98e-03 (0.606) | 0.511, 0.491 (15 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 9 | -2.387 | 0.05 | oblateSpheroid, prolateSpheroid | 13.04 | inf | 5.66e-03 / 5.66e-03 (1.000) | 0.788, 0.607 (9 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.982 / 1.000 | 1.053, 2.23 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.992 / 1.000 | 1.052, 2.57 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.987 / 1.000 | 1.054, 2.69 |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
