# Positive definiteness of the operator, prolate_ar2

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.304 / 0.415 | 20 of 20; 0.257 / 0.570 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -0.406 / 0.027 | 20 of 20; 0.227 / 0.396 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 9 of 20; -0.455 / -0.019 | 20 of 20; 0.166 / 0.386 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 7 of 20; -0.875 / -0.116 | 20 of 20; 0.158 / 0.443 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.127 / -0.512 | 20 of 20; 0.113 / 0.296 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.088 / -0.705 | 20 of 20; 0.071 / 0.200 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.508 / -0.727 | 18 of 20; -0.164 / 0.297 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.878 / -1.178 | 17 of 20; -0.069 / 0.182 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.082 / -1.512 | 17 of 20; -0.148 / 0.140 |
| 0.2 | 16 | 18 | 18 of 18; 1.000 / 1.000 | 0 of 18; -1.701 / -1.271 | 17 of 18; -0.054 / 0.168 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.298 / -2.028 | 13 of 20; -0.187 / 0.096 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.850 / -2.428 | 9 of 20; -0.655 / -0.005 |

## The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -3.298 | 0.71 | prolate_ar2, prolate_ar2 | 2.82 | 1.081 | 1.04e-02 / 5.03e-03 (0.484) | 0.441, 0.479 (24 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 18 | -0.655 | 0.83 | prolate_ar2, prolate_ar2 | 2.41 | 1.054 | 1.04e-02 / 3.38e-03 (0.325) | 0.443, 0.719 (24 particles within 6 of the first) |

## The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 400 | 400 | 0.994 / 1.000 | 1.053, 2.13 |
| prolate_ar2__prolate_ar2_test | 400 | 400 | 0.991 / 1.000 | 1.053, 2.34 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.985 / 1.000 | 1.052, 2.44 |
| prolate_ar4__prolate_ar4_test | 400 | 400 | 0.940 / 1.000 | 1.057, 3.46 |
| oblate_ar1p5__oblate_ar1p5_test | 400 | 400 | 0.995 / 1.000 | 1.055, 2.57 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.991 / 1.000 | 1.057, 2.96 |
| oblate_ar3__oblate_ar3_test | 400 | 400 | 0.837 / 1.000 | 1.072, 2.84 |
| prolate_ar2p5__prolate_ar2p5_test | 400 | 400 | 0.976 / 1.000 | 1.054, 2.86 |
| oblate_ar2p5__oblate_ar2p5_test | 400 | 400 | 0.984 / 1.001 | 1.195, 3.65 |
| prolate_ar5__prolate_ar5_test | 400 | 400 | 0.846 / 1.003 | 1.097, 6.26 |

## Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Configurations**: N in [16, 50, 100], shapes prolate_ar2 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.
