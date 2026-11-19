# Accuracy of the two-body and full-body models, with the error of MFS itself

Built 2026-11-15 20:38 by `report.py` from `results_c/<case>/`.  All numbers are % errors against MFS on fine clouds unless a column says otherwise.  trans / rot = translation / rotation.

How to read the MFS columns: a model error is only meaningful down to the error of the truth it is compared with.  `MFS fine vs Xfine` is the same test solved with both cloud resolutions, in the same metric; `reciprocity` is how far the raw MFS blocks are from the symmetry the exact ones have.  Where a model error is close to these, the model is at the floor of its labels and cannot be shown to be better.

## 1. Two-body (cells 1A-1D spheroid form, 3A-3D triaxial form)

Pair test sets (unseen seeds), one random unit force and torque on the source, PRMSE of the target's velocity.  Ranges are over the test sets of the pairings the model was trained on.

| cell | case | trained pairings tested | model: trans / rot | MFS fine vs Xfine: trans / rot | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | far field alone: trans / rot | pairings never trained on: trans / rot | mean trans over training seeds |
|---|---|---|---|---|---|---|---|---|---|
| 1A | 1A_pro | 1 | 0.032 / 0.346 | 0.024 / 0.140 | 0.037 / 0.413 | 0.004 / 0.024 | 4.794 / 11.925 | none | 0.032-0.034 (3 seeds) |
| 1A | 1A_obl | 1 | 0.019 / 0.170 | 0.012 / 0.027 | 0.019 / 0.125 | 0.004 / 0.020 | 4.974 / 11.392 | none | 0.018-0.019 (3 seeds) |
| 1B | 1B | 7 | 0.028-0.155 / 0.081-0.610 | 0.003-0.067 / 0.014-0.482 | 0.027-0.143 / 0.083-0.633 | 0.002-0.070 / 0.009-0.366 | 4.052-5.699 / 10.071-14.983 | 3: 0.185-1.904 / 0.491-6.131 | 0.063-0.067 (3 seeds) |
| 1C | 1C | 3 | 0.027-0.074 / 0.148-0.439 | 0.012-0.024 / 0.027-0.140 | 0.026-0.067 / 0.125-0.475 | 0.004-0.004 / 0.020-0.024 | 4.794-4.974 / 11.392-11.925 | none | 0.048-0.049 (3 seeds) |
| 1D | 1D | 22 | 0.027-0.213 / 0.083-0.810 | 0.003-0.132 / 0.014-0.482 | 0.027-0.201 / 0.086-0.804 | 0.002-0.115 / 0.009-0.565 | 3.561-5.699 / 10.071-14.983 | 6: 0.071-1.450 / 0.356-4.821 | 0.100-0.102 (3 seeds) |
| 3A | 3A | 1 | 0.064 / 0.293 | 0.069 / 0.461 | 0.070 / 0.442 | 0.040 / 0.283 | 4.374 / 11.505 | none | 0.064-0.065 (3 seeds) |
| 3B | 3B | 6 | 0.069-0.234 / 0.350-1.345 | 0.016-0.095 / 0.073-0.466 | 0.070-0.235 / 0.348-1.377 | 0.009-0.059 / 0.053-0.391 | 3.668-5.216 / 11.028-14.715 | 2: 0.169-1.726 / 0.865-15.191 | 0.127-0.132 (3 seeds) |
| 3C | 3C | 6 | 0.090-0.124 / 0.397-0.824 | 0.012-0.073 / 0.027-0.527 | 0.083-0.131 / 0.443-0.905 | 0.004-0.055 / 0.020-0.389 | 4.374-4.974 / 11.377-12.116 | none | 0.105-0.107 (3 seeds) |
| 3D | 3D | 25 | 0.071-0.301 / 0.383-1.645 | 0.012-0.124 / 0.027-0.792 | 0.073-0.249 / 0.356-1.482 | 0.004-0.091 / 0.020-0.582 | 3.668-5.216 / 10.690-15.399 | 7: 0.062-1.883 / 0.496-9.977 | 0.141-0.145 (3 seeds) |

## 2. Full body (cells 2A-2D spheroid form, 4A-4D triaxial form)

Suspensions in unbounded fluid, random unit forces and torques on every particle, PRMSE of all six velocity components: far field -> + two-body -> + many-body (translation / rotation of the last).  Whole matrix = Frobenius error of the full operator's grand mobility matrix on one small suspension (16 particles in the full runs).  Ring = centre-of-mass error (% of the distance fallen) of 5 particles sedimenting.

| cell | case | N | phi: far -> two-body -> many-body (trans / rot) | MFS fine vs Xfine | phi: far -> two-body -> many-body (trans / rot) | MFS fine vs Xfine | whole matrix vs MFS | MFS fine vs Xfine (matrix) | positive definite | ring: far -> two-body -> many-body | MFS fine vs Xfine (ring) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2A | 1A_pro | 200 | 0.1: 13.85 -> 10.99 -> 5.15 (5.15 / 5.32) | 0.009 (0.007 / 0.038) | 0.2: 27.33 -> 23.44 -> 8.25 (8.24 / 9.32) | 0.014 (0.011 / 0.075) | 1.66 | 0.013 | yes | 6.01 -> 2.00 -> 1.15 | 0.003 |
| 2A | 1A_obl | 200 | 0.1: 12.95 -> 10.25 -> 4.65 (4.63 / 5.54) | 0.010 (0.009 / 0.024) | 0.2: 21.83 -> 18.71 -> 7.28 (7.23 / 10.44) | 0.015 (0.014 / 0.045) | 1.95 | 0.004 | yes | 5.41 -> 2.08 -> 0.48 | 0.001 |
| 2B | 1B | 200 | 0.1: 13.72 -> 10.81 -> 4.32 (4.35 / 3.97) | 0.006 (0.005 / 0.014) | 0.2: 24.52 -> 20.99 -> 9.59 (9.68 / 9.46) | 0.015 (0.011 / 0.037) | 1.64 | 0.002 | yes | 5.42 -> 1.76 -> 0.56 | 0.001 |
| 2C | 1C | 200 | 0.1: 13.71 -> 11.06 -> 5.42 (5.43 / 5.32) | 0.011 (0.010 / 0.029) | 0.2: 23.59 -> 20.14 -> 7.40 (7.35 / 9.63) | 0.009 (0.006 / 0.089) | 2.52 | 0.014 | **NO** | 6.24 -> 2.27 -> 0.54 | 0.002 |
| 2D | 1D | 200 | 0.1: 14.39 -> 10.82 -> 6.34 (6.55 / 4.16) | 0.034 (0.032 / 0.050) | 0.2: 23.17 -> 19.20 -> 9.48 (9.62 / 7.59) | not measured | 2.86 | 0.020 | yes | 4.14 -> 0.68 -> 0.12 | 0.004 |
| 4A | 3A | 200 | 0.1: 14.34 -> 11.69 -> 5.58 (5.55 / 7.30) | 0.036 (0.033 / 0.130) | 0.2: 26.45 -> 23.00 -> 8.64 (8.58 / 13.01) | 0.093 (0.080 / 0.393) | 1.61 | 0.014 | yes | 6.14 -> 2.41 -> 0.38 | 0.014 |
| 4B | 3B | 200 | 0.1: 15.01 -> 12.22 -> 6.38 (6.35 / 8.92) | 0.063 (0.058 / 0.283) | 0.2: 23.62 -> 20.44 -> 9.24 (9.18 / 16.63) | 0.101 (0.091 / 0.426) | 1.93 | 0.021 | yes | 6.59 -> 2.60 -> 1.39 | 0.007 |
| 4C | 3C | 200 | 0.1: 13.82 -> 11.01 -> 4.80 (4.78 / 5.45) | 0.034 (0.030 / 0.120) | 0.2: 25.10 -> 21.52 -> 7.58 (7.52 / 10.28) | 0.060 (0.048 / 0.251) | 1.98 | 0.019 | yes | 5.25 -> 1.93 -> 0.49 | 0.006 |
| 4D | 3D | 200 | 0.1: 14.38 -> 11.13 -> 6.10 (6.12 / 5.81) | 0.015 (0.013 / 0.046) | 0.2: 26.03 -> 21.74 -> 24.60 (24.69 / 22.75) | 0.058 (0.049 / 0.175) | 2.57 | 0.007 | yes | 4.77 -> 1.75 -> 0.97 | 0.002 |

## 3. Every result, with its conditions

### Case 1A_pro (cells 1A and 2A): spheroid form, one shape: prolate 1:1:3

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 150 / 131; 0.0325 / 0.1955 | 348 / 304; 0.0230 / 0.0079 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Two-body accuracy of `data/final_c/models/pair_pro.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.032 | 0.346 | 0.062 | 0.46 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.037 / 0.413 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.046 / 0.398 (684) | 0.023 / 0.348 (898) | 0.024 / 0.289 (660) | 0.024 / 0.206 (754) | 0.023 / 0.231 (1038) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Two-body accuracy of `data/final_c/models/pair_pro_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.034 | 0.407 | 0.071 | 0.44 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.040 / 0.509 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.048 / 0.493 (684) | 0.025 / 0.389 (898) | 0.027 / 0.328 (660) | 0.027 / 0.225 (754) | 0.024 / 0.232 (1038) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro_s1.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 1: prolateSpheroid__prolateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Two-body accuracy of `data/final_c/models/pair_pro_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.032 | 0.369 | 0.065 | 0.45 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.040 / 0.471 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.046 / 0.441 (684) | 0.025 / 0.361 (898) | 0.025 / 0.296 (660) | 0.025 / 0.202 (754) | 0.024 / 0.229 (1038) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro_s2.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 2: prolateSpheroid__prolateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Suspensions of prolateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.32 (4.33 / 4.28; 1.19) | 2.84 (2.87 / 2.41; 1.00) | 1.86 (1.88 / 1.56; 0.72) | 0.004 (0.004 / 0.011; 0.000) (1) |
| 0.05 | 200 | 10 | 7.00 (7.01 / 7.29; 2.19) | 5.12 (5.15 / 5.02; 1.91) | 2.84 (2.85 / 2.87; 1.14) | 0.009 (0.006 / 0.029; 0.000) (1) |
| 0.075 | 200 | 10 | 11.45 (11.48 / 11.70; 3.32) | 8.94 (8.97 / 8.89; 2.94) | 4.37 (4.38 / 4.34; 1.44) | 0.021 (0.017 / 0.048; 0.001) (1) |
| 0.1 | 200 | 10 | 13.85 (13.86 / 14.37; 4.09) | 10.99 (11.00 / 11.24; 3.64) | 5.15 (5.15 / 5.32; 1.59) | 0.009 (0.007 / 0.038; 0.001) (1) |
| 0.15 | 200 | 10 | 18.56 (18.49 / 22.71; 6.05) | 15.64 (15.59 / 19.11; 5.45) | 5.94 (5.91 / 7.47; 1.95) | 0.008 (0.006 / 0.034; 0.001) (1) |
| 0.2 | 200 | 10 | 27.33 (27.30 / 30.80; 7.74) | 23.44 (23.40 / 26.55; 7.01) | 8.25 (8.24 / 9.32; 2.33) | 0.014 (0.011 / 0.075; 0.003) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configurations**: N in [200] particles, shapes prolateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Suspensions of prolateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.27 (7.27 / 7.64; 2.40) | 4.90 (4.89 / 5.13; 1.76) | 2.14 (2.11 / 2.71; 0.75) | 0.009 (0.009 / 0.012; 0.001) (1) |
| 0.05 | 100 | 5 | 7.38 (7.38 / 7.58; 2.48) | 5.30 (5.28 / 5.62; 2.03) | 2.65 (2.64 / 3.06; 0.94) | 0.012 (0.011 / 0.019; 0.001) (1) |
| 0.05 | 200 | 5 | 6.81 (6.82 / 7.39; 2.21) | 5.02 (5.05 / 4.92; 1.93) | 2.86 (2.88 / 2.82; 1.17) | not measured |
| 0.05 | 300 | 5 | 7.34 (7.35 / 7.49; 2.19) | 5.55 (5.58 / 5.11; 1.97) | 3.36 (3.39 / 2.94; 1.33) | not measured |
| 0.1 | 50 | 5 | 11.94 (11.96 / 12.24; 4.59) | 8.88 (8.89 / 9.26; 3.58) | 3.30 (3.25 / 4.04; 1.31) | 0.012 (0.012 / 0.020; 0.001) (1) |
| 0.1 | 100 | 5 | 14.77 (14.92 / 13.65; 4.05) | 11.00 (11.12 / 10.31; 3.39) | 4.73 (4.77 / 4.56; 1.16) | 0.010 (0.009 / 0.014; 0.001) (1) |
| 0.1 | 200 | 5 | 12.24 (12.18 / 14.36; 4.10) | 10.01 (9.99 / 11.08; 3.64) | 4.74 (4.73 / 5.31; 1.54) | not measured |
| 0.1 | 300 | 5 | 11.12 (11.02 / 15.05; 4.20) | 9.16 (9.09 / 12.22; 3.85) | 4.37 (4.34 / 5.69; 2.02) | not measured |
| 0.15 | 50 | 5 | 17.91 (17.85 / 19.73; 6.11) | 13.91 (13.84 / 15.38; 4.80) | 4.01 (3.87 / 6.16; 1.45) | 0.015 (0.013 / 0.034; 0.002) (1) |
| 0.15 | 100 | 5 | 15.59 (15.42 / 21.18; 5.99) | 12.72 (12.56 / 17.60; 5.09) | 4.17 (4.09 / 6.49; 1.47) | 0.013 (0.008 / 0.061; 0.001) (1) |
| 0.15 | 200 | 5 | 18.65 (18.59 / 22.30; 6.12) | 15.64 (15.59 / 18.79; 5.52) | 6.03 (6.02 / 7.27; 2.00) | not measured |
| 0.15 | 300 | 5 | 16.92 (16.83 / 21.60; 5.89) | 14.58 (14.51 / 18.43; 5.43) | 6.33 (6.31 / 7.50; 2.44) | not measured |
| 0.2 | 50 | 5 | 24.26 (24.11 / 27.41; 7.96) | 19.53 (19.41 / 22.00; 6.37) | 5.46 (5.33 / 7.30; 1.28) | 0.038 (0.035 / 0.072; 0.003) (1) |
| 0.2 | 100 | 5 | 21.82 (21.59 / 28.88; 7.38) | 18.22 (18.04 / 24.06; 6.31) | 5.39 (5.27 / 8.47; 1.74) | 0.014 (0.012 / 0.051; 0.003) (1) |
| 0.2 | 200 | 5 | 26.35 (26.25 / 31.47; 7.81) | 22.81 (22.70 / 27.34; 7.07) | 7.77 (7.74 / 9.40; 2.32) | not measured |
| 0.2 | 300 | 5 | 29.85 (29.78 / 31.96; 7.57) | 26.18 (26.14 / 27.43; 6.99) | 10.67 (10.71 / 9.80; 2.89) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Dynamics: pair of prolateSpheroid, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 98.5, 239 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.01 | 0.037 | 0.20 |
| + two-body | 1500 | 0.01 | 0.010 | 0.05 |
| + many-body | 1500 | 0.01 | 0.010 | 0.05 |
| MFS Xfine (the truth's own error) | 1500 | 0.003 | 0.0060 | 0.040 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolateSpheroid, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Dynamics: ring of prolateSpheroid, prolateSpheroid, prolateSpheroid, prolateSpheroid, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 131 steps, fell 20.8, 108 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 46 | 6.01 | 0.642 | 0.00 |
| + two-body | 47 | 2.00 | 0.308 | 0.00 |
| + many-body | 93 | 1.15 | 0.233 | 0.01 |
| MFS Xfine (the truth's own error) | 131 | 0.003 | 0.0021 | 0.007 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: prolateSpheroid, prolateSpheroid, prolateSpheroid, prolateSpheroid, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Structural checks, 16 particles of prolateSpheroid at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.3e-16 | 2.1287 | 6.1e-16 | 7.40 |
| + two-body | 9.8e-17 | 0.4605 | 5.1e-16 | 4.43 |
| + many-body | 1.0e-16 | 1.0487 | 5.1e-16 | 1.66 |
| MFS fine (the truth) | 3.7e-05 | 1 | | 0 |
| MFS Xfine | 3.6e-06 | 0.9904 | | 0.013 (= the error of the fine truth) |

MFS smallest eigenvalue 1.6006e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configuration**: ONE random suspension, N = 16, shapes prolateSpheroid in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Positive definiteness of the operator, prolateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.032 / 0.466 | 20 of 20; 0.344 / 0.679 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 11 of 20; -0.665 / 0.019 | 20 of 20; 0.194 / 0.422 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 10 of 20; -0.367 / -0.013 | 20 of 20; 0.295 / 0.419 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -1.198 / -0.432 | 20 of 20; 0.140 / 0.400 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.066 / -1.084 | 19 of 20; -0.084 / 0.273 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.244 / -1.297 | 11 of 20; -0.409 / 0.040 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.967 / -0.978 | 18 of 20; -0.108 / 0.296 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.387 / -1.998 | 14 of 20; -0.506 / 0.064 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.003 / -2.464 | 0 of 20; -2.055 / -1.566 |
| 0.2 | 16 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -3.650 / -1.927 | 14 of 19; -0.231 / 0.121 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.988 / -3.271 | 1 of 20; -0.607 / -0.138 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.568 / -3.896 | 0 of 20; -2.861 / -2.499 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 17 | -4.988 | 0.68 | prolateSpheroid, prolateSpheroid | 2.27 | 1.106 | 3.88e-03 / 2.35e-03 (0.605) | 0.322, 0.470 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 2 | -2.861 | 0.04 | prolateSpheroid, prolateSpheroid | 11.83 | 5.536 | 5.64e-03 / 5.64e-03 (1.000) | 0.764, 0.808 (10 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.984 / 1.000 | 1.053, 2.23 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 8.54 (8.69 / 6.55) | 5.50 (5.59 / 4.44) | 2.53 (2.56 / 2.23) | 1.72 (1.77 / 1.04) | 1.64 (1.69 / 0.99) |
| 0.1 | 64 | 3 | 13.28 (13.27 / 14.44) | 10.16 (10.13 / 11.76) | 3.57 (3.53 / 4.54) | 2.30 (2.32 / 2.01) | 2.23 (2.26 / 1.75) |
| 0.2 | 64 | 3 | 18.62 (18.29 / 29.24) | 14.98 (14.69 / 24.26) | 3.72 (3.54 / 8.18) | 2.58 (2.54 / 3.96) | 1.94 (1.94 / 2.02) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configurations**: N in [64], shapes prolateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

### Case 1A_obl (cells 1A and 2A): spheroid form, one shape: oblate 2:2:1

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 174 / 152; 2.8747 / 0.1707 | 334 / 292; 0.0385 / 0.0193 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_obl.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.019 | 0.170 | 0.032 | 0.24 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.019 / 0.125 | 0.004 / 0.020 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.028 / 0.215 (650) | 0.015 / 0.140 (936) | 0.011 / 0.116 (680) | 0.009 / 0.162 (738) | 0.012 / 0.153 (1018) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_obl_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.018 | 0.171 | 0.031 | 0.24 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.018 / 0.131 | 0.004 / 0.020 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.028 / 0.215 (650) | 0.013 / 0.138 (936) | 0.010 / 0.122 (680) | 0.008 / 0.165 (738) | 0.012 / 0.162 (1018) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl_s1.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 1: oblateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_obl_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.019 | 0.189 | 0.034 | 0.24 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.020 / 0.140 | 0.004 / 0.020 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.029 / 0.239 (650) | 0.016 / 0.154 (936) | 0.011 / 0.134 (680) | 0.009 / 0.177 (738) | 0.011 / 0.166 (1018) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl_s2.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 2: oblateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Suspensions of oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.58 (4.56 / 5.17; 1.13) | 2.89 (2.90 / 2.86; 0.95) | 1.85 (1.86 / 1.74; 0.71) | 0.002 (0.002 / 0.004; 0.000) (1) |
| 0.05 | 200 | 10 | 6.93 (6.89 / 8.87; 2.16) | 5.01 (4.99 / 6.04; 1.88) | 2.94 (2.94 / 3.33; 1.19) | 0.010 (0.009 / 0.023; 0.001) (1) |
| 0.075 | 200 | 10 | 10.13 (10.06 / 13.11; 3.20) | 7.73 (7.69 / 9.52; 2.83) | 3.75 (3.73 / 4.59; 1.55) | 0.014 (0.013 / 0.027; 0.000) (1) |
| 0.1 | 200 | 10 | 12.95 (12.87 / 16.18; 4.00) | 10.25 (10.18 / 12.71; 3.56) | 4.65 (4.63 / 5.54; 1.76) | 0.010 (0.009 / 0.024; 0.001) (1) |
| 0.15 | 200 | 10 | 19.77 (19.67 / 25.46; 5.98) | 16.61 (16.52 / 21.27; 5.39) | 6.66 (6.63 / 8.20; 2.30) | 0.014 (0.013 / 0.038; 0.001) (1) |
| 0.2 | 200 | 10 | 21.83 (21.58 / 34.96; 7.63) | 18.71 (18.49 / 30.15; 6.90) | 7.28 (7.23 / 10.44; 2.81) | 0.015 (0.014 / 0.045; 0.002) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configurations**: N in [200] particles, shapes oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Suspensions of oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.94 (7.88 / 9.64; 2.48) | 5.21 (5.16 / 6.28; 1.80) | 2.20 (2.16 / 3.04; 0.78) | 0.006 (0.006 / 0.012; 0.001) (1) |
| 0.05 | 100 | 5 | 6.64 (6.57 / 8.70; 2.39) | 4.67 (4.64 / 5.76; 1.96) | 2.41 (2.40 / 2.93; 0.97) | 0.003 (0.002 / 0.010; 0.000) (1) |
| 0.05 | 200 | 5 | 7.37 (7.34 / 9.05; 2.18) | 5.34 (5.33 / 6.25; 1.90) | 3.10 (3.10 / 3.33; 1.22) | not measured |
| 0.05 | 300 | 5 | 7.30 (7.25 / 8.87; 2.06) | 5.50 (5.49 / 6.02; 1.85) | 3.43 (3.44 / 3.24; 1.32) | not measured |
| 0.1 | 50 | 5 | 12.29 (12.17 / 15.08; 3.94) | 8.74 (8.63 / 11.15; 3.00) | 3.37 (3.34 / 4.24; 1.25) | 0.008 (0.008 / 0.017; 0.000) (1) |
| 0.1 | 100 | 5 | 11.58 (11.50 / 15.40; 4.02) | 8.82 (8.75 / 12.17; 3.36) | 3.63 (3.59 / 5.12; 1.27) | 0.015 (0.014 / 0.029; 0.001) (1) |
| 0.1 | 200 | 5 | 12.55 (12.45 / 16.35; 3.94) | 9.97 (9.90 / 12.57; 3.51) | 4.45 (4.43 / 5.46; 1.75) | not measured |
| 0.1 | 300 | 5 | 12.05 (11.96 / 15.94; 3.94) | 9.97 (9.91 / 12.54; 3.59) | 5.03 (5.01 / 5.80; 2.07) | not measured |
| 0.15 | 50 | 5 | 14.69 (14.46 / 22.95; 5.78) | 11.25 (11.05 / 18.42; 4.51) | 3.49 (3.41 / 6.34; 1.62) | 0.013 (0.011 / 0.041; 0.002) (1) |
| 0.15 | 100 | 5 | 16.39 (16.21 / 23.34; 5.93) | 13.40 (13.26 / 18.99; 5.05) | 4.63 (4.57 / 6.89; 1.63) | 0.020 (0.019 / 0.035; 0.002) (1) |
| 0.15 | 200 | 5 | 17.80 (17.62 / 24.85; 6.06) | 15.02 (14.88 / 20.77; 5.47) | 5.99 (5.95 / 7.75; 2.38) | not measured |
| 0.15 | 300 | 5 | 21.70 (21.65 / 25.25; 5.82) | 18.46 (18.43 / 21.35; 5.35) | 8.33 (8.36 / 7.97; 2.77) | not measured |
| 0.2 | 50 | 5 | 23.94 (23.63 / 32.91; 7.93) | 18.90 (18.63 / 26.48; 6.34) | 5.08 (4.94 / 8.20; 1.47) | 0.008 (0.007 / 0.026; 0.001) (1) |
| 0.2 | 100 | 5 | 21.46 (21.15 / 34.64; 7.68) | 17.56 (17.27 / 29.47; 6.59) | 5.58 (5.47 / 9.70; 1.87) | 0.020 (0.019 / 0.045; 0.002) (1) |
| 0.2 | 200 | 5 | 19.96 (19.72 / 34.72; 7.59) | 17.25 (17.03 / 30.59; 6.86) | 6.56 (6.50 / 10.46; 2.75) | not measured |
| 0.2 | 300 | 5 | 24.77 (24.56 / 37.93; 7.57) | 21.57 (21.39 / 32.63; 6.99) | 9.46 (9.44 / 11.55; 3.48) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: pair of oblateSpheroid, oblateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 110.2, 256 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.06 | 0.074 | 2.51 |
| + two-body | 1500 | 0.00 | 0.001 | 0.02 |
| + many-body | 1500 | 0.00 | 0.001 | 0.02 |
| MFS Xfine (the truth's own error) | 1500 | 0.000 | 0.0004 | 0.008 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: oblateSpheroid, oblateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: ring of oblateSpheroid, oblateSpheroid, oblateSpheroid, oblateSpheroid, oblateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 186 steps, fell 27.7, 166 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 81 | 5.41 | 0.840 | 15.02 |
| + two-body | 98 | 2.08 | 0.552 | 11.12 |
| + many-body | 131 | 0.48 | 0.275 | 4.36 |
| MFS Xfine (the truth's own error) | 186 | 0.001 | 0.0002 | 0.004 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: oblateSpheroid, oblateSpheroid, oblateSpheroid, oblateSpheroid, oblateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Structural checks, 16 particles of oblateSpheroid at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.3e-16 | 1.7238 | 7.0e-16 | 8.91 |
| + two-body | 8.4e-17 | 0.2682 | 5.5e-16 | 5.45 |
| + many-body | 9.1e-17 | 0.9235 | 5.9e-16 | 1.95 |
| MFS fine (the truth) | 2.5e-05 | 1 | | 0 |
| MFS Xfine | 6.2e-06 | 0.9985 | | 0.004 (= the error of the fine truth) |

MFS smallest eigenvalue 3.3442e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configuration**: ONE random suspension, N = 16, shapes oblateSpheroid in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Positive definiteness of the operator, oblateSpheroid

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 16 of 20; -0.180 / 0.364 | 20 of 20; 0.194 / 0.736 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 15 of 20; -0.456 / 0.225 | 20 of 20; 0.212 / 0.509 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 3 of 20; -0.776 / -0.124 | 20 of 20; 0.174 / 0.350 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -1.113 / -0.347 | 20 of 20; 0.251 / 0.533 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.168 / -0.596 | 20 of 20; 0.091 / 0.421 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.531 / -0.939 | 17 of 20; -0.107 / 0.145 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.542 / -0.645 | 20 of 20; 0.183 / 0.384 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.062 / -1.407 | 20 of 20; 0.004 / 0.221 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.504 / -1.696 | 0 of 20; -1.215 / -0.827 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.413 / -1.570 | 18 of 20; -0.152 / 0.191 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.094 / -2.235 | 13 of 20; -0.189 / 0.066 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.244 / -2.893 | 0 of 20; -1.666 / -1.410 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 1 | -3.244 | 0.64 | oblateSpheroid, oblateSpheroid | 3.34 | 1.102 | 6.16e-03 / 3.87e-03 (0.629) | 0.560, 0.607 (14 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 8 | -1.666 | 0.04 | oblateSpheroid, oblateSpheroid | 5.85 | 1.727 | 6.88e-03 / 6.87e-03 (0.998) | 0.855, 0.962 (11 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.997 / 1.000 | 1.059, 2.69 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configurations**: N in [16, 50, 100], shapes oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.88 (7.80 / 9.90) | 5.10 (5.06 / 6.13) | 2.69 (2.68 / 2.90) | 2.08 (2.09 / 1.82) | 2.02 (2.03 / 1.71) |
| 0.1 | 64 | 3 | 12.86 (12.72 / 17.02) | 9.80 (9.71 / 12.72) | 3.81 (3.75 / 5.50) | 3.07 (3.07 / 2.90) | 2.88 (2.89 / 2.56) |
| 0.2 | 64 | 3 | 25.37 (25.10 / 34.07) | 19.92 (19.68 / 27.03) | 5.70 (5.59 / 8.56) | 4.72 (4.73 / 5.07) | 3.90 (3.96 / 2.73) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configurations**: N in [64], shapes oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

### Case 1B (cells 1B and 2B): spheroid form, many shapes (7 aspect ratios), one shape per pair / cluster

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | no cloud | no cloud | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 160 / 136; 0.0313 / 0.0171 | 340 / 290; 0.0024 / 0.0003 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 150 / 131; 0.0325 / 0.1955 | 348 / 304; 0.0230 / 0.0079 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | no cloud | no cloud | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | no cloud | no cloud | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 174 / 152; 2.8747 / 0.1707 | 334 / 292; 0.0385 / 0.0193 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 160 / 136; 1.4664 / 2.9934 | 340 / 290; 0.0503 / 0.2693 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 160 / 136; 0.3052 / 0.0807 | 340 / 290; 0.0485 / 0.0077 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | no cloud | no cloud | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar5 | 1 : 1 : 5 | 160 / 136; 1.5981 / 0.6942 | 340 / 290; 0.1892 / 0.1178 | 660 / 560; 0.0024 / 0.0023 | 1400 / 1190; 0.0002 / 0.0002 |

#### Two-body accuracy of `data/final_c/models/pair_multi.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4044 | 0.030 | 0.081 | 0.034 | 0.33 | 5.70 / 10.61 | 0.005 / 0.031 (510) | 0.031 / 0.088 | 0.002 / 0.009 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4040 | 0.049 | 0.188 | 0.063 | 0.52 | 5.19 / 11.22 | 0.016 / 0.067 (504) | 0.051 / 0.161 | 0.005 / 0.029 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.050 | 0.421 | 0.081 | 0.67 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.047 / 0.516 | 0.004 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4024 | 0.155 | 0.610 | 0.168 | 2.39 | 4.80 / 14.98 | 0.067 / 0.482 (500) | 0.143 / 0.633 | 0.030 / 0.169 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4006 | 0.030 | 0.082 | 0.032 | 0.34 | 5.57 / 10.07 | 0.003 / 0.014 (504) | 0.029 / 0.083 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.028 | 0.154 | 0.037 | 0.37 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.027 / 0.119 | 0.004 / 0.020 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4020 | 0.114 | 0.517 | 0.127 | 1.58 | 4.05 / 11.39 | 0.058 / 0.336 (504) | 0.107 / 0.398 | 0.070 / 0.366 | 0.0 % |
| prolate_ar2p5__prolate_ar2p5_test | 4040 | 0.185 | 0.491 | 0.200 | 0.89 | 4.92 / 11.60 | 0.027 / 0.141 (510) | 0.185 / 0.398 | 0.018 / 0.100 | 0.0 % |
| oblate_ar2p5__oblate_ar2p5_test | 4044 | 0.398 | 0.946 | 0.414 | 3.18 | 4.18 / 11.10 | 0.041 / 0.107 (502) | 0.415 / 0.897 | 0.025 / 0.168 | 0.0 % |
| prolate_ar5__prolate_ar5_test | 4044 | 1.904 | 6.131 | 1.993 | 7.48 | 5.01 / 17.89 | 0.789 / 4.234 (508) | 2.095 / 7.177 | 0.090 / 0.496 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.031 / 0.085 (652) | 0.026 / 0.064 (896) | 0.023 / 0.085 (690) | 0.030 / 0.107 (688) | 0.052 / 0.154 (1118) | - |
| prolate_ar2__prolate_ar2_test | 0.061 / 0.202 (708) | 0.048 / 0.192 (840) | 0.032 / 0.133 (756) | 0.035 / 0.174 (620) | 0.048 / 0.262 (1116) | - |
| prolateSpheroid__prolateSpheroid_test | 0.069 / 0.514 (684) | 0.043 / 0.400 (898) | 0.036 / 0.337 (660) | 0.036 / 0.219 (754) | 0.037 / 0.228 (1038) | - |
| prolate_ar4__prolate_ar4_test | 0.222 / 0.787 (680) | 0.140 / 0.530 (904) | 0.119 / 0.520 (734) | 0.081 / 0.346 (660) | 0.072 / 0.312 (1046) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.033 / 0.079 (652) | 0.023 / 0.072 (922) | 0.024 / 0.089 (714) | 0.031 / 0.103 (704) | 0.048 / 0.140 (1014) | - |
| oblateSpheroid__oblateSpheroid_test | 0.041 / 0.183 (650) | 0.021 / 0.133 (936) | 0.019 / 0.117 (680) | 0.020 / 0.162 (738) | 0.028 / 0.165 (1018) | - |
| oblate_ar3__oblate_ar3_test | 0.165 / 0.693 (726) | 0.094 / 0.409 (854) | 0.069 / 0.286 (702) | 0.069 / 0.266 (660) | 0.086 / 0.336 (1078) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.254 / 0.590 (696) | 0.188 / 0.499 (896) | 0.125 / 0.309 (740) | 0.068 / 0.246 (696) | 0.052 / 0.234 (1012) | - |
| oblate_ar2p5__oblate_ar2p5_test | 0.563 / 1.192 (640) | 0.398 / 0.877 (874) | 0.260 / 0.621 (740) | 0.178 / 0.549 (734) | 0.169 / 0.539 (1056) | - |
| prolate_ar5__prolate_ar5_test | 2.388 / 7.462 (688) | 2.135 / 6.646 (938) | 1.539 / 4.291 (672) | 1.033 / 2.869 (708) | 0.501 / 1.326 (1038) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.009 / 0.046 (90) | 0.000 / 0.002 (88) | 0.000 / 0.000 (92) | 0.000 / 0.000 (98) | 0.000 / 0.000 (142) | - |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.101 (98) | 0.001 / 0.005 (110) | 0.000 / 0.000 (84) | 0.000 / 0.000 (84) | 0.000 / 0.000 (128) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| prolate_ar4__prolate_ar4_test | 0.125 / 0.838 (76) | 0.037 / 0.278 (110) | 0.003 / 0.016 (90) | 0.002 / 0.005 (70) | 0.001 / 0.003 (154) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.006 / 0.022 (84) | 0.000 / 0.001 (108) | 0.000 / 0.000 (110) | 0.000 / 0.000 (92) | 0.000 / 0.000 (110) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| oblate_ar3__oblate_ar3_test | 0.079 / 0.471 (96) | 0.054 / 0.232 (120) | 0.037 / 0.150 (90) | 0.038 / 0.128 (82) | 0.027 / 0.109 (116) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.048 / 0.221 (96) | 0.008 / 0.034 (98) | 0.001 / 0.002 (114) | 0.000 / 0.000 (80) | 0.000 / 0.000 (122) | - |
| oblate_ar2p5__oblate_ar2p5_test | 0.068 / 0.154 (98) | 0.021 / 0.071 (116) | 0.009 / 0.033 (88) | 0.009 / 0.030 (80) | 0.006 / 0.021 (120) | - |
| prolate_ar5__prolate_ar5_test | 1.406 / 6.806 (100) | 0.093 / 0.489 (112) | 0.015 / 0.053 (74) | 0.003 / 0.009 (80) | 0.001 / 0.004 (142) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5__prolate_ar2p5_test`: prolate_ar2p5 (target or source) with prolate_ar2p5, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar2p5__oblate_ar2p5_test`: oblate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar5__prolate_ar5_test`: prolate_ar5 (target or source) with prolate_ar5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar5 | 1 : 1 : 5 | 660 / 560; 0.0024 / 0.0023 | 1400 / 1190; 0.0002 / 0.0002 |

#### Two-body accuracy of `data/final_c/models/pair_multi_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4044 | 0.031 | 0.088 | 0.035 | 0.34 | 5.70 / 10.61 | 0.005 / 0.031 (510) | 0.031 / 0.100 | 0.002 / 0.009 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4040 | 0.052 | 0.191 | 0.062 | 0.52 | 5.19 / 11.22 | 0.016 / 0.067 (504) | 0.053 / 0.167 | 0.005 / 0.029 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.048 | 0.407 | 0.078 | 0.68 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.042 / 0.495 | 0.004 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4024 | 0.142 | 0.583 | 0.159 | 2.40 | 4.80 / 14.98 | 0.067 / 0.482 (500) | 0.135 / 0.590 | 0.030 / 0.169 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4006 | 0.031 | 0.087 | 0.034 | 0.32 | 5.57 / 10.07 | 0.003 / 0.014 (504) | 0.031 / 0.090 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.164 | 0.037 | 0.37 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.026 / 0.142 | 0.004 / 0.020 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4020 | 0.113 | 0.517 | 0.124 | 1.65 | 4.05 / 11.39 | 0.058 / 0.336 (504) | 0.107 / 0.409 | 0.070 / 0.366 | 0.0 % |
| prolate_ar2p5__prolate_ar2p5_test | 4040 | 0.182 | 0.510 | 0.200 | 0.91 | 4.92 / 11.60 | 0.027 / 0.141 (510) | 0.186 / 0.418 | 0.018 / 0.100 | 0.0 % |
| oblate_ar2p5__oblate_ar2p5_test | 4044 | 0.264 | 0.833 | 0.285 | 1.84 | 4.18 / 11.10 | 0.041 / 0.107 (502) | 0.270 / 0.866 | 0.025 / 0.168 | 0.0 % |
| prolate_ar5__prolate_ar5_test | 4044 | 1.959 | 4.693 | 1.995 | 7.22 | 5.01 / 17.89 | 0.789 / 4.234 (508) | 2.158 / 6.238 | 0.090 / 0.496 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.036 / 0.090 (652) | 0.025 / 0.072 (896) | 0.024 / 0.092 (690) | 0.033 / 0.116 (688) | 0.045 / 0.162 (1118) | - |
| prolate_ar2__prolate_ar2_test | 0.067 / 0.198 (708) | 0.051 / 0.197 (840) | 0.034 / 0.142 (756) | 0.037 / 0.193 (620) | 0.047 / 0.284 (1116) | - |
| prolateSpheroid__prolateSpheroid_test | 0.065 / 0.474 (684) | 0.041 / 0.402 (898) | 0.036 / 0.347 (660) | 0.036 / 0.223 (754) | 0.038 / 0.252 (1038) | - |
| prolate_ar4__prolate_ar4_test | 0.200 / 0.739 (680) | 0.131 / 0.512 (904) | 0.095 / 0.499 (734) | 0.087 / 0.379 (660) | 0.093 / 0.336 (1046) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.034 / 0.080 (652) | 0.026 / 0.079 (922) | 0.025 / 0.097 (714) | 0.030 / 0.114 (704) | 0.048 / 0.155 (1014) | - |
| oblateSpheroid__oblateSpheroid_test | 0.039 / 0.180 (650) | 0.021 / 0.150 (936) | 0.018 / 0.142 (680) | 0.022 / 0.184 (738) | 0.030 / 0.185 (1018) | - |
| oblate_ar3__oblate_ar3_test | 0.156 / 0.697 (726) | 0.095 / 0.397 (854) | 0.079 / 0.302 (702) | 0.077 / 0.278 (660) | 0.095 / 0.315 (1078) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.241 / 0.594 (696) | 0.191 / 0.522 (896) | 0.121 / 0.344 (740) | 0.091 / 0.324 (696) | 0.072 / 0.339 (1012) | - |
| oblate_ar2p5__oblate_ar2p5_test | 0.342 / 0.947 (640) | 0.269 / 0.815 (874) | 0.203 / 0.720 (740) | 0.176 / 0.618 (734) | 0.146 / 0.522 (1056) | - |
| prolate_ar5__prolate_ar5_test | 2.321 / 5.739 (688) | 2.219 / 4.930 (938) | 1.751 / 3.557 (672) | 1.172 / 2.360 (708) | 0.641 / 1.362 (1038) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.009 / 0.046 (90) | 0.000 / 0.002 (88) | 0.000 / 0.000 (92) | 0.000 / 0.000 (98) | 0.000 / 0.000 (142) | - |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.101 (98) | 0.001 / 0.005 (110) | 0.000 / 0.000 (84) | 0.000 / 0.000 (84) | 0.000 / 0.000 (128) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| prolate_ar4__prolate_ar4_test | 0.125 / 0.838 (76) | 0.037 / 0.278 (110) | 0.003 / 0.016 (90) | 0.002 / 0.005 (70) | 0.001 / 0.003 (154) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.006 / 0.022 (84) | 0.000 / 0.001 (108) | 0.000 / 0.000 (110) | 0.000 / 0.000 (92) | 0.000 / 0.000 (110) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| oblate_ar3__oblate_ar3_test | 0.079 / 0.471 (96) | 0.054 / 0.232 (120) | 0.037 / 0.150 (90) | 0.038 / 0.128 (82) | 0.027 / 0.109 (116) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.048 / 0.221 (96) | 0.008 / 0.034 (98) | 0.001 / 0.002 (114) | 0.000 / 0.000 (80) | 0.000 / 0.000 (122) | - |
| oblate_ar2p5__oblate_ar2p5_test | 0.068 / 0.154 (98) | 0.021 / 0.071 (116) | 0.009 / 0.033 (88) | 0.009 / 0.030 (80) | 0.006 / 0.021 (120) | - |
| prolate_ar5__prolate_ar5_test | 1.406 / 6.806 (100) | 0.093 / 0.489 (112) | 0.015 / 0.053 (74) | 0.003 / 0.009 (80) | 0.001 / 0.004 (142) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi_s1.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 1: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5__prolate_ar2p5_test`: prolate_ar2p5 (target or source) with prolate_ar2p5, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar2p5__oblate_ar2p5_test`: oblate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar5__prolate_ar5_test`: prolate_ar5 (target or source) with prolate_ar5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar5 | 1 : 1 : 5 | 660 / 560; 0.0024 / 0.0023 | 1400 / 1190; 0.0002 / 0.0002 |

#### Two-body accuracy of `data/final_c/models/pair_multi_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4044 | 0.034 | 0.089 | 0.038 | 0.35 | 5.70 / 10.61 | 0.005 / 0.031 (510) | 0.038 / 0.099 | 0.002 / 0.009 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4040 | 0.062 | 0.195 | 0.069 | 0.53 | 5.19 / 11.22 | 0.016 / 0.067 (504) | 0.055 / 0.168 | 0.005 / 0.029 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.048 | 0.396 | 0.077 | 0.66 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.051 / 0.488 | 0.004 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4024 | 0.151 | 0.576 | 0.169 | 2.40 | 4.80 / 14.98 | 0.067 / 0.482 (500) | 0.147 / 0.628 | 0.030 / 0.169 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4006 | 0.033 | 0.090 | 0.037 | 0.35 | 5.57 / 10.07 | 0.003 / 0.014 (504) | 0.034 / 0.086 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.029 | 0.157 | 0.038 | 0.37 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.028 / 0.133 | 0.004 / 0.020 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4020 | 0.113 | 0.514 | 0.125 | 1.63 | 4.05 / 11.39 | 0.058 / 0.336 (504) | 0.108 / 0.451 | 0.070 / 0.366 | 0.0 % |
| prolate_ar2p5__prolate_ar2p5_test | 4040 | 0.139 | 0.559 | 0.167 | 1.15 | 4.92 / 11.60 | 0.027 / 0.141 (510) | 0.116 / 0.479 | 0.018 / 0.100 | 0.0 % |
| oblate_ar2p5__oblate_ar2p5_test | 4044 | 0.254 | 1.097 | 0.293 | 1.94 | 4.18 / 11.10 | 0.041 / 0.107 (502) | 0.247 / 1.144 | 0.025 / 0.168 | 0.0 % |
| prolate_ar5__prolate_ar5_test | 4044 | 1.039 | 5.209 | 1.185 | 8.89 | 5.01 / 17.89 | 0.789 / 4.234 (508) | 1.276 / 6.604 | 0.090 / 0.496 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.043 / 0.092 (652) | 0.027 / 0.075 (896) | 0.026 / 0.091 (690) | 0.031 / 0.117 (688) | 0.047 / 0.161 (1118) | - |
| prolate_ar2__prolate_ar2_test | 0.065 / 0.198 (708) | 0.077 / 0.203 (840) | 0.040 / 0.151 (756) | 0.042 / 0.198 (620) | 0.049 / 0.285 (1116) | - |
| prolateSpheroid__prolateSpheroid_test | 0.067 / 0.466 (684) | 0.039 / 0.391 (898) | 0.038 / 0.321 (660) | 0.036 / 0.230 (754) | 0.038 / 0.258 (1038) | - |
| prolate_ar4__prolate_ar4_test | 0.218 / 0.746 (680) | 0.139 / 0.489 (904) | 0.100 / 0.488 (734) | 0.085 / 0.357 (660) | 0.082 / 0.332 (1046) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.037 / 0.093 (652) | 0.028 / 0.077 (922) | 0.027 / 0.094 (714) | 0.031 / 0.112 (704) | 0.053 / 0.147 (1014) | - |
| oblateSpheroid__oblateSpheroid_test | 0.041 / 0.178 (650) | 0.023 / 0.142 (936) | 0.020 / 0.129 (680) | 0.021 / 0.174 (738) | 0.033 / 0.171 (1018) | - |
| oblate_ar3__oblate_ar3_test | 0.156 / 0.691 (726) | 0.099 / 0.396 (854) | 0.079 / 0.302 (702) | 0.069 / 0.281 (660) | 0.092 / 0.327 (1078) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.204 / 0.653 (696) | 0.122 / 0.572 (896) | 0.090 / 0.396 (740) | 0.065 / 0.332 (696) | 0.053 / 0.277 (1012) | - |
| oblate_ar2p5__oblate_ar2p5_test | 0.299 / 1.374 (640) | 0.263 / 1.069 (874) | 0.212 / 0.668 (740) | 0.210 / 0.507 (734) | 0.201 / 0.449 (1056) | - |
| prolate_ar5__prolate_ar5_test | 1.294 / 6.102 (688) | 1.122 / 5.449 (938) | 0.909 / 4.422 (672) | 0.642 / 3.357 (708) | 0.361 / 1.613 (1038) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.009 / 0.046 (90) | 0.000 / 0.002 (88) | 0.000 / 0.000 (92) | 0.000 / 0.000 (98) | 0.000 / 0.000 (142) | - |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.101 (98) | 0.001 / 0.005 (110) | 0.000 / 0.000 (84) | 0.000 / 0.000 (84) | 0.000 / 0.000 (128) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| prolate_ar4__prolate_ar4_test | 0.125 / 0.838 (76) | 0.037 / 0.278 (110) | 0.003 / 0.016 (90) | 0.002 / 0.005 (70) | 0.001 / 0.003 (154) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.006 / 0.022 (84) | 0.000 / 0.001 (108) | 0.000 / 0.000 (110) | 0.000 / 0.000 (92) | 0.000 / 0.000 (110) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| oblate_ar3__oblate_ar3_test | 0.079 / 0.471 (96) | 0.054 / 0.232 (120) | 0.037 / 0.150 (90) | 0.038 / 0.128 (82) | 0.027 / 0.109 (116) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.048 / 0.221 (96) | 0.008 / 0.034 (98) | 0.001 / 0.002 (114) | 0.000 / 0.000 (80) | 0.000 / 0.000 (122) | - |
| oblate_ar2p5__oblate_ar2p5_test | 0.068 / 0.154 (98) | 0.021 / 0.071 (116) | 0.009 / 0.033 (88) | 0.009 / 0.030 (80) | 0.006 / 0.021 (120) | - |
| prolate_ar5__prolate_ar5_test | 1.406 / 6.806 (100) | 0.093 / 0.489 (112) | 0.015 / 0.053 (74) | 0.003 / 0.009 (80) | 0.001 / 0.004 (142) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi_s2.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 2: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5__prolate_ar2p5_test`: prolate_ar2p5 (target or source) with prolate_ar2p5, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar2p5__oblate_ar2p5_test`: oblate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar5__prolate_ar5_test`: prolate_ar5 (target or source) with prolate_ar5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar5 | 1 : 1 : 5 | 660 / 560; 0.0024 / 0.0023 | 1400 / 1190; 0.0002 / 0.0002 |

#### Suspensions of prolate_ar2: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.28 (4.31 / 4.03; 1.13) | 2.68 (2.73 / 2.17; 0.95) | 1.57 (1.60 / 1.27; 0.62) | 0.003 (0.003 / 0.005; 0.000) (1) |
| 0.05 | 200 | 10 | 7.40 (7.51 / 6.56; 2.10) | 5.43 (5.53 / 4.49; 1.83) | 2.62 (2.67 / 2.20; 0.92) | 0.005 (0.004 / 0.008; 0.000) (1) |
| 0.075 | 200 | 10 | 11.14 (11.25 / 10.13; 3.13) | 8.69 (8.83 / 7.10; 2.77) | 3.76 (3.81 / 3.21; 1.13) | 0.005 (0.005 / 0.009; 0.000) (1) |
| 0.1 | 200 | 10 | 13.72 (13.83 / 12.50; 3.94) | 10.81 (10.93 / 9.43; 3.52) | 4.32 (4.35 / 3.97; 1.32) | 0.006 (0.005 / 0.014; 0.000) (1) |
| 0.15 | 200 | 10 | 16.91 (16.78 / 19.81; 5.83) | 14.07 (13.99 / 16.00; 5.24) | 5.32 (5.29 / 6.04; 2.25) | 0.010 (0.007 / 0.027; 0.001) (1) |
| 0.2 | 200 | 10 | 24.52 (24.59 / 27.70; 7.59) | 20.99 (21.10 / 22.80; 6.86) | 9.59 (9.68 / 9.46; 4.34) | 0.015 (0.011 / 0.037; 0.001) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Configurations**: N in [200] particles, shapes prolate_ar2 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

#### Suspensions of prolate_ar2: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 6.51 (6.61 / 5.89; 2.22) | 4.12 (4.17 / 3.82; 1.64) | 1.73 (1.72 / 1.86; 0.66) | 0.001 (0.001 / 0.002; 0.000) (1) |
| 0.05 | 100 | 5 | 6.05 (5.99 / 6.95; 2.36) | 4.22 (4.22 / 4.22; 1.93) | 1.71 (1.70 / 1.99; 0.72) | 0.002 (0.002 / 0.004; 0.000) (1) |
| 0.05 | 200 | 5 | 7.61 (7.77 / 6.51; 2.11) | 5.57 (5.70 / 4.49; 1.84) | 2.68 (2.74 / 2.20; 0.93) | not measured |
| 0.05 | 300 | 5 | 7.35 (7.40 / 6.85; 2.04) | 5.40 (5.48 / 4.35; 1.84) | 2.89 (2.94 / 2.26; 1.10) | not measured |
| 0.1 | 50 | 5 | 12.90 (13.00 / 12.79; 4.38) | 9.33 (9.49 / 8.20; 3.41) | 2.73 (2.66 / 3.42; 1.01) | 0.004 (0.003 / 0.014; 0.001) (1) |
| 0.1 | 100 | 5 | 10.61 (10.46 / 13.08; 4.11) | 8.09 (8.00 / 9.76; 3.43) | 2.82 (2.74 / 3.97; 1.05) | 0.007 (0.006 / 0.017; 0.000) (1) |
| 0.1 | 200 | 5 | 13.16 (13.23 / 12.71; 3.92) | 10.21 (10.28 / 9.54; 3.49) | 3.97 (3.98 / 4.03; 1.29) | not measured |
| 0.1 | 300 | 5 | 14.31 (14.45 / 13.07; 3.89) | 11.66 (11.83 / 9.87; 3.55) | 5.03 (5.12 / 4.16; 1.64) | not measured |
| 0.15 | 50 | 5 | 17.78 (17.72 / 19.05; 5.94) | 13.30 (13.23 / 14.64; 4.67) | 3.68 (3.52 / 5.31; 0.82) | 0.008 (0.008 / 0.011; 0.000) (1) |
| 0.15 | 100 | 5 | 15.82 (15.82 / 18.86; 6.09) | 12.89 (12.92 / 14.95; 5.19) | 4.04 (3.99 / 5.43; 1.47) | 0.003 (0.002 / 0.007; 0.000) (1) |
| 0.15 | 200 | 5 | 16.95 (16.84 / 20.06; 5.84) | 14.04 (13.95 / 16.43; 5.26) | 5.25 (5.23 / 5.95; 2.24) | not measured |
| 0.15 | 300 | 5 | 22.64 (22.94 / 20.31; 5.82) | 19.22 (19.52 / 16.49; 5.36) | 8.20 (8.35 / 6.49; 2.74) | not measured |
| 0.2 | 50 | 5 | 19.68 (19.24 / 28.20; 7.72) | 15.31 (14.93 / 22.63; 6.13) | 3.82 (3.61 / 6.95; 0.92) | 0.015 (0.010 / 0.046; 0.002) (1) |
| 0.2 | 100 | 5 | 24.53 (24.37 / 28.15; 7.75) | 20.56 (20.52 / 22.32; 6.65) | 7.34 (7.28 / 8.49; 2.78) | 0.025 (0.014 / 0.069; 0.002) (1) |
| 0.2 | 200 | 5 | 25.92 (26.12 / 26.64; 7.53) | 22.27 (22.53 / 21.49; 6.81) | 10.04 (10.18 / 9.11; 4.27) | not measured |
| 0.2 | 300 | 5 | 24.11 (24.02 / 28.00; 7.56) | 21.11 (21.13 / 22.89; 6.99) | 10.45 (10.52 / 10.10; 4.66) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolate_ar2 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

#### Dynamics: pair of prolate_ar2, prolate_ar2 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 136.8, 240 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.06 | 0.098 | 1.98 |
| + two-body | 1500 | 0.01 | 0.015 | 0.23 |
| + many-body | 1500 | 0.01 | 0.015 | 0.23 |
| MFS Xfine (the truth's own error) | 1500 | 0.000 | 0.0000 | 0.000 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolate_ar2, prolate_ar2.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

#### Dynamics: ring of prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 105 steps, fell 19.6, 84 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 42 | 5.42 | 0.629 | 0.00 |
| + two-body | 41 | 1.76 | 0.297 | 0.00 |
| + many-body | 71 | 0.56 | 0.119 | 0.00 |
| MFS Xfine (the truth's own error) | 105 | 0.001 | 0.0006 | 0.002 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

#### Structural checks, 16 particles of prolate_ar2 at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.2e-16 | 1.9529 | 7.7e-16 | 8.45 |
| + two-body | 8.1e-17 | 0.4235 | 6.6e-16 | 4.99 |
| + many-body | 8.6e-17 | 0.8790 | 6.5e-16 | 1.64 |
| MFS fine (the truth) | 2.0e-05 | 1 | | 0 |
| MFS Xfine | 1.2e-06 | 0.9996 | | 0.002 (= the error of the fine truth) |

MFS smallest eigenvalue 4.6459e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Configuration**: ONE random suspension, N = 16, shapes prolate_ar2 in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

#### Positive definiteness of the operator, prolate_ar2

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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -3.298 | 0.71 | prolate_ar2, prolate_ar2 | 2.82 | 1.081 | 1.04e-02 / 5.03e-03 (0.484) | 0.441, 0.479 (24 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 18 | -0.655 | 0.83 | prolate_ar2, prolate_ar2 | 2.41 | 1.054 | 1.04e-02 / 3.38e-03 (0.325) | 0.443, 0.719 (24 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

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

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Configurations**: N in [16, 50, 100], shapes prolate_ar2 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolate_ar2

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.44 (7.49 / 6.96) | 5.09 (5.15 / 4.35) | 1.97 (1.93 / 2.32) | 1.22 (1.25 / 0.89) | 1.14 (1.17 / 0.79) |
| 0.1 | 64 | 3 | 12.45 (12.38 / 13.24) | 9.09 (9.09 / 9.42) | 3.02 (2.94 / 3.91) | 1.89 (1.93 / 1.53) | 1.63 (1.68 / 1.00) |
| 0.2 | 64 | 3 | 23.92 (24.16 / 25.54) | 19.78 (20.08 / 20.48) | 5.53 (5.42 / 7.51) | 3.15 (3.18 / 3.42) | 1.89 (1.99 / 1.09) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Configurations**: N in [64], shapes prolate_ar2 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

### Case 1C (cells 1C and 2C): spheroid form, prolate and oblate mixed

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 150 / 131; 0.0325 / 0.1955 | 348 / 304; 0.0230 / 0.0079 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 174 / 152; 2.8747 / 0.1707 | 334 / 292; 0.0385 / 0.0193 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_mixed.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.046 | 0.392 | 0.075 | 0.56 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.045 / 0.475 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.148 | 0.035 | 0.33 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.026 / 0.125 | 0.004 / 0.020 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.074 | 0.439 | 0.099 | 0.78 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.067 / 0.390 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.065 / 0.466 (684) | 0.036 / 0.378 (898) | 0.033 / 0.324 (660) | 0.033 / 0.231 (754) | 0.034 / 0.226 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.038 / 0.164 (650) | 0.021 / 0.136 (936) | 0.017 / 0.121 (680) | 0.019 / 0.168 (738) | 0.028 / 0.165 (1018) | - |
| prolateSpheroid__oblateSpheroid_test | 0.096 / 0.490 (702) | 0.067 / 0.452 (952) | 0.052 / 0.324 (668) | 0.054 / 0.299 (632) | 0.065 / 0.331 (1086) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_mixed_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.045 | 0.420 | 0.078 | 0.59 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.045 / 0.525 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.166 | 0.036 | 0.33 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.025 / 0.136 | 0.004 / 0.020 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.072 | 0.440 | 0.098 | 0.78 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.064 / 0.403 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.064 / 0.512 (684) | 0.037 / 0.401 (898) | 0.033 / 0.328 (660) | 0.033 / 0.222 (754) | 0.034 / 0.255 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.039 / 0.193 (650) | 0.020 / 0.142 (936) | 0.017 / 0.141 (680) | 0.017 / 0.180 (738) | 0.026 / 0.183 (1018) | - |
| prolateSpheroid__oblateSpheroid_test | 0.093 / 0.491 (702) | 0.064 / 0.454 (952) | 0.053 / 0.319 (668) | 0.054 / 0.297 (632) | 0.068 / 0.335 (1086) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed_s1.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 1: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_mixed_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.047 | 0.406 | 0.078 | 0.55 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.049 / 0.490 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.028 | 0.156 | 0.036 | 0.33 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.027 / 0.126 | 0.004 / 0.020 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.072 | 0.420 | 0.096 | 0.76 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.064 / 0.354 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.066 / 0.479 (684) | 0.038 / 0.394 (898) | 0.034 / 0.345 (660) | 0.032 / 0.221 (754) | 0.035 / 0.241 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.040 / 0.182 (650) | 0.021 / 0.137 (936) | 0.019 / 0.123 (680) | 0.019 / 0.165 (738) | 0.026 / 0.164 (1018) | - |
| prolateSpheroid__oblateSpheroid_test | 0.092 / 0.468 (702) | 0.064 / 0.432 (952) | 0.053 / 0.306 (668) | 0.055 / 0.292 (632) | 0.066 / 0.311 (1086) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed_s2.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 2: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Suspensions of prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.15 (4.13 / 4.73; 1.18) | 2.70 (2.70 / 2.59; 0.99) | 1.75 (1.76 / 1.66; 0.73) | 0.004 (0.003 / 0.012; 0.000) (1) |
| 0.05 | 200 | 10 | 7.04 (7.02 / 8.05; 2.15) | 5.18 (5.19 / 5.41; 1.88) | 3.03 (3.04 / 3.05; 1.16) | 0.008 (0.007 / 0.020; 0.000) (1) |
| 0.075 | 200 | 10 | 10.32 (10.30 / 11.29; 3.18) | 8.05 (8.04 / 8.77; 2.82) | 4.09 (4.09 / 4.29; 1.53) | 0.026 (0.025 / 0.042; 0.001) (1) |
| 0.1 | 200 | 10 | 13.71 (13.68 / 14.59; 4.06) | 11.06 (11.05 / 11.38; 3.62) | 5.42 (5.43 / 5.32; 1.72) | 0.011 (0.010 / 0.029; 0.001) (1) |
| 0.15 | 200 | 10 | 19.40 (19.34 / 21.97; 5.87) | 16.06 (16.01 / 18.06; 5.28) | 6.47 (6.46 / 7.17; 2.12) | 0.018 (0.016 / 0.044; 0.002) (1) |
| 0.2 | 200 | 10 | 23.59 (23.38 / 31.98; 7.63) | 20.14 (19.94 / 27.81; 6.90) | 7.40 (7.35 / 9.63; 2.55) | 0.009 (0.006 / 0.089; 0.002) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Configurations**: N in [200] particles, shapes prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Suspensions of prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 6.86 (6.83 / 7.69; 2.63) | 4.82 (4.79 / 5.47; 1.96) | 2.18 (2.15 / 2.82; 0.78) | 0.008 (0.006 / 0.022; 0.000) (1) |
| 0.05 | 100 | 5 | 6.35 (6.31 / 7.81; 2.25) | 4.57 (4.56 / 5.18; 1.81) | 2.37 (2.37 / 2.71; 0.85) | 0.004 (0.003 / 0.020; 0.000) (1) |
| 0.05 | 200 | 5 | 6.78 (6.78 / 7.84; 2.15) | 5.06 (5.07 / 5.37; 1.88) | 3.01 (3.02 / 3.07; 1.16) | not measured |
| 0.05 | 300 | 5 | 7.77 (7.78 / 7.98; 2.13) | 5.68 (5.71 / 5.39; 1.91) | 3.46 (3.48 / 3.12; 1.33) | not measured |
| 0.1 | 50 | 5 | 11.72 (11.62 / 14.31; 4.59) | 8.33 (8.24 / 10.37; 3.57) | 3.15 (3.07 / 4.75; 1.27) | 0.009 (0.007 / 0.031; 0.001) (1) |
| 0.1 | 100 | 5 | 12.69 (12.69 / 13.71; 4.08) | 9.68 (9.68 / 10.63; 3.42) | 3.94 (3.92 / 4.62; 1.23) | 0.016 (0.014 / 0.030; 0.001) (1) |
| 0.1 | 200 | 5 | 13.85 (13.84 / 14.43; 3.98) | 11.33 (11.33 / 11.44; 3.55) | 5.64 (5.65 / 5.29; 1.70) | not measured |
| 0.1 | 300 | 5 | 12.51 (12.48 / 14.54; 3.98) | 10.35 (10.32 / 11.74; 3.63) | 5.38 (5.39 / 5.57; 2.04) | not measured |
| 0.15 | 50 | 5 | 15.33 (15.13 / 21.52; 6.04) | 11.37 (11.20 / 16.41; 4.75) | 3.56 (3.46 / 6.09; 1.52) | 0.024 (0.020 / 0.109; 0.003) (1) |
| 0.15 | 100 | 5 | 18.91 (18.85 / 22.71; 6.22) | 15.50 (15.46 / 18.80; 5.32) | 5.46 (5.43 / 7.13; 1.62) | 0.008 (0.007 / 0.028; 0.002) (1) |
| 0.15 | 200 | 5 | 17.36 (17.23 / 22.05; 5.88) | 14.30 (14.20 / 17.93; 5.30) | 5.78 (5.74 / 7.12; 2.11) | not measured |
| 0.15 | 300 | 5 | 20.71 (20.66 / 23.81; 5.91) | 17.53 (17.51 / 19.56; 5.44) | 8.02 (8.05 / 7.96; 2.68) | not measured |
| 0.2 | 50 | 5 | 23.53 (23.27 / 29.73; 7.77) | 18.27 (17.99 / 24.83; 6.19) | 4.97 (4.79 / 8.23; 1.43) | 0.025 (0.022 / 0.052; 0.002) (1) |
| 0.2 | 100 | 5 | 23.56 (23.33 / 30.62; 7.64) | 19.31 (19.12 / 25.12; 6.55) | 6.15 (6.05 / 8.78; 1.78) | 0.028 (0.025 / 0.052; 0.002) (1) |
| 0.2 | 200 | 5 | 23.01 (22.81 / 32.55; 7.55) | 19.64 (19.45 / 28.12; 6.82) | 7.16 (7.11 / 9.69; 2.52) | not measured |
| 0.2 | 300 | 5 | 22.88 (22.70 / 32.80; 7.71) | 20.07 (19.91 / 28.50; 7.12) | 8.35 (8.32 / 10.63; 3.22) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: pair of prolateSpheroid, oblateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 110.9, 259 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.48 | 0.564 | 2.61 |
| + two-body | 1500 | 0.04 | 0.046 | 0.18 |
| + many-body | 1500 | 0.04 | 0.046 | 0.18 |
| MFS Xfine (the truth's own error) | 1500 | 0.002 | 0.0031 | 0.027 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolateSpheroid, oblateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: ring of prolateSpheroid, oblateSpheroid, prolateSpheroid, oblateSpheroid, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 173 steps, fell 26.9, 151 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 33 | 6.24 | 0.498 | 12.49 |
| + two-body | 40 | 2.27 | 0.266 | 8.02 |
| + many-body | 80 | 0.54 | 0.144 | 1.50 |
| MFS Xfine (the truth's own error) | 173 | 0.002 | 0.0012 | 0.016 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: prolateSpheroid, oblateSpheroid, prolateSpheroid, oblateSpheroid, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Structural checks, 16 particles of prolateSpheroid, oblateSpheroid at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.3e-16 | 2.9882 | 8.6e-16 | 11.05 |
| + two-body | 9.3e-17 | -2.7731 | 7.7e-16 | 7.19 |
| + many-body | 9.8e-17 | -0.1007 | 7.7e-16 | 2.52 |
| MFS fine (the truth) | 5.7e-05 | 1 | | 0 |
| MFS Xfine | 3.2e-06 | 0.9959 | | 0.014 (= the error of the fine truth) |

MFS smallest eigenvalue 1.2134e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Configuration**: ONE random suspension, N = 16, shapes prolateSpheroid, oblateSpheroid in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Positive definiteness of the operator, prolateSpheroid, oblateSpheroid

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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 11 | -4.763 | 0.77 | oblateSpheroid, oblateSpheroid | 3.32 | 1.116 | 6.58e-03 / 3.98e-03 (0.606) | 0.511, 0.491 (15 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 9 | -2.387 | 0.05 | oblateSpheroid, prolateSpheroid | 13.04 | inf | 5.66e-03 / 5.66e-03 (1.000) | 0.788, 0.607 (9 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.982 / 1.000 | 1.053, 2.23 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.992 / 1.000 | 1.052, 2.57 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.987 / 1.000 | 1.054, 2.69 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolateSpheroid, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.21 (7.19 / 7.90) | 4.93 (4.93 / 4.80) | 2.51 (2.50 / 2.61) | 1.78 (1.79 / 1.48) | 1.74 (1.75 / 1.44) |
| 0.1 | 64 | 3 | 12.19 (12.09 / 13.98) | 8.93 (8.88 / 9.92) | 3.64 (3.59 / 4.39) | 2.57 (2.58 / 2.18) | 2.47 (2.50 / 1.81) |
| 0.2 | 64 | 3 | 24.39 (24.13 / 30.29) | 19.57 (19.29 / 25.79) | 5.71 (5.57 / 8.42) | 4.38 (4.37 / 4.68) | 3.59 (3.63 / 2.61) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Configurations**: N in [64], shapes prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

### Case 1D (cells 1D and 2D): spheroid form, every shape and size mixed

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | no cloud | no cloud | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 160 / 136; 0.0313 / 0.0171 | 340 / 290; 0.0024 / 0.0003 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 150 / 131; 0.0325 / 0.1955 | 348 / 304; 0.0230 / 0.0079 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | no cloud | no cloud | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | no cloud | no cloud | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 174 / 152; 2.8747 / 0.1707 | 334 / 292; 0.0385 / 0.0193 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 160 / 136; 1.4664 / 2.9934 | 340 / 290; 0.0503 / 0.2693 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 150 / 131; 0.0400 / 0.1996 | 348 / 304; 0.0240 / 0.0072 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 174 / 152; 2.7969 / 0.1689 | 334 / 292; 0.0405 / 0.0196 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2_x1p5 | 1.5 : 1.5 : 3 | 160 / 136; 0.0312 / 0.0173 | 340 / 290; 0.0024 / 0.0003 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3_x0p75 | 2.25 : 2.25 : 0.75 | 160 / 136; 1.4726 / 2.9994 | 340 / 290; 0.0533 / 0.2724 | 660 / 560; 0.0236 / 0.0510 | 1400 / 1190; 0.0086 / 0.0183 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 160 / 136; 0.3052 / 0.0807 | 340 / 290; 0.0485 / 0.0077 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | no cloud | no cloud | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar2p5_x1p25 | 1.25 : 1.25 : 3.125 | 160 / 136; 0.3050 / 0.0807 | 340 / 290; 0.0485 / 0.0077 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |

#### Two-body accuracy of `data/final_c/models/pair_poly.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4044 | 0.030 | 0.083 | 0.034 | 0.35 | 5.70 / 10.61 | 0.005 / 0.031 (510) | 0.034 / 0.092 | 0.002 / 0.009 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4040 | 0.046 | 0.183 | 0.058 | 0.49 | 5.19 / 11.22 | 0.016 / 0.067 (504) | 0.056 / 0.162 | 0.005 / 0.029 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.052 | 0.353 | 0.075 | 0.66 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.052 / 0.440 | 0.004 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4024 | 0.149 | 0.568 | 0.167 | 2.47 | 4.80 / 14.98 | 0.067 / 0.482 (500) | 0.145 / 0.626 | 0.030 / 0.169 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4006 | 0.033 | 0.083 | 0.036 | 0.32 | 5.57 / 10.07 | 0.003 / 0.014 (504) | 0.032 / 0.086 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.153 | 0.036 | 0.33 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.027 / 0.127 | 0.004 / 0.020 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4020 | 0.105 | 0.468 | 0.113 | 1.35 | 4.05 / 11.39 | 0.058 / 0.336 (504) | 0.092 / 0.350 | 0.070 / 0.366 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.072 | 0.401 | 0.093 | 0.80 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.064 / 0.337 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2__oblateSpheroid_test | 4046 | 0.085 | 0.340 | 0.102 | 0.87 | 4.89 / 11.55 | 0.021 / 0.065 (498) | 0.092 / 0.357 | 0.004 / 0.021 | 0.0 % |
| prolate_ar4__oblate_ar3_test | 4028 | 0.213 | 0.810 | 0.235 | 3.42 | 4.06 / 12.07 | 0.069 / 0.364 (506) | 0.201 / 0.804 | 0.075 / 0.483 | 0.0 % |
| prolate_ar2__oblate_ar1p5_test | 4018 | 0.068 | 0.227 | 0.079 | 0.77 | 5.45 / 10.67 | 0.008 / 0.033 (502) | 0.065 / 0.217 | 0.005 / 0.025 | 0.0 % |
| prolate_ar1p5__oblate_ar3_test | 4044 | 0.151 | 0.597 | 0.175 | 1.41 | 4.09 / 14.18 | 0.132 / 0.454 (508) | 0.153 / 0.618 | 0.115 / 0.565 | 0.0 % |
| prolateSpheroid__prolate_ar2_test | 4022 | 0.122 | 0.471 | 0.144 | 1.38 | 4.85 / 11.78 | 0.017 / 0.131 (508) | 0.113 / 0.442 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblate_ar3_test | 4000 | 0.132 | 0.537 | 0.147 | 1.53 | 4.25 / 11.86 | 0.091 / 0.419 (500) | 0.126 / 0.541 | 0.076 / 0.415 | 0.0 % |
| prolate_ar4__oblateSpheroid_test | 4042 | 0.150 | 0.644 | 0.174 | 2.02 | 4.77 / 12.73 | 0.043 / 0.254 (508) | 0.152 / 0.642 | 0.024 / 0.155 | 0.0 % |
| prolateSpheroid__oblate_ar1p5_test | 4026 | 0.094 | 0.366 | 0.111 | 1.06 | 4.97 / 11.76 | 0.018 / 0.081 (508) | 0.096 / 0.421 | 0.004 / 0.021 | 0.0 % |
| prolateSpheroid_x0p75__prolateSpheroid_test | 4046 | 0.134 | 0.597 | 0.168 | 1.32 | 4.72 / 13.40 | 0.024 / 0.203 (504) | 0.124 / 0.543 | 0.006 / 0.032 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.086 | 0.325 | 0.094 | 0.83 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.086 / 0.287 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2_x1p5__prolate_ar2_test | 4022 | 0.086 | 0.338 | 0.098 | 0.85 | 4.83 / 11.46 | 0.021 / 0.101 (498) | 0.088 / 0.353 | 0.008 / 0.050 | 0.0 % |
| oblate_ar3_x0p75__oblate_ar3_test | 4018 | 0.183 | 0.681 | 0.193 | 2.22 | 3.85 / 11.95 | 0.090 / 0.371 (498) | 0.137 / 0.555 | 0.074 / 0.397 | 0.0 % |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 4028 | 0.130 | 0.548 | 0.151 | 1.08 | 3.56 / 12.87 | 0.037 / 0.211 (506) | 0.130 / 0.533 | 0.007 / 0.043 | 0.0 % |
| prolate_ar2_x1p5__oblateSpheroid_test | 4016 | 0.085 | 0.330 | 0.095 | 1.02 | 4.90 / 10.45 | 0.031 / 0.078 (500) | 0.093 / 0.358 | 0.005 / 0.031 | 0.0 % |
| prolate_ar2__oblate_ar3_test | 4032 | 0.671 | 2.796 | 0.778 | 5.07 | 3.98 / 12.62 | 0.112 / 0.491 (506) | 0.686 / 2.756 | 0.098 / 0.537 | 0.0 % |
| prolate_ar4__oblate_ar1p5_test | 4022 | 1.450 | 3.118 | 1.514 | 5.11 | 5.13 / 14.89 | 0.073 / 0.459 (502) | 1.462 / 3.258 | 0.038 / 0.249 | 0.0 % |
| prolate_ar2p5__oblate_ar2p5_test | 4040 | 0.500 | 1.629 | 0.545 | 4.03 | 4.39 / 11.86 | 0.046 / 0.226 (506) | 0.476 / 1.544 | 0.039 / 0.257 | 0.0 % |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 4020 | 0.071 | 0.356 | 0.085 | 0.88 | 4.86 / 10.50 | 0.031 / 0.199 (504) | 0.061 / 0.366 | 0.016 / 0.102 | 0.0 % |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 4054 | 1.228 | 4.821 | 1.368 | 18.91 | 4.50 / 11.02 | 0.044 / 0.240 (510) | 1.251 / 4.521 | 0.048 / 0.291 | 0.0 % |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 4006 | 0.221 | 1.047 | 0.264 | 2.53 | 4.85 / 10.92 | 0.022 / 0.134 (506) | 0.245 / 1.115 | 0.015 / 0.099 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.036 / 0.088 (652) | 0.024 / 0.068 (896) | 0.024 / 0.085 (690) | 0.029 / 0.105 (688) | 0.044 / 0.140 (1118) | - |
| prolate_ar2__prolate_ar2_test | 0.062 / 0.190 (708) | 0.040 / 0.190 (840) | 0.034 / 0.139 (756) | 0.030 / 0.180 (620) | 0.042 / 0.252 (1116) | - |
| prolateSpheroid__prolateSpheroid_test | 0.073 / 0.403 (684) | 0.044 / 0.360 (898) | 0.038 / 0.291 (660) | 0.036 / 0.212 (754) | 0.034 / 0.228 (1038) | - |
| prolate_ar4__prolate_ar4_test | 0.219 / 0.757 (680) | 0.138 / 0.479 (904) | 0.089 / 0.433 (734) | 0.085 / 0.346 (660) | 0.072 / 0.318 (1046) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.040 / 0.082 (652) | 0.027 / 0.075 (922) | 0.027 / 0.089 (714) | 0.029 / 0.101 (704) | 0.038 / 0.132 (1014) | - |
| oblateSpheroid__oblateSpheroid_test | 0.040 / 0.168 (650) | 0.022 / 0.145 (936) | 0.018 / 0.124 (680) | 0.017 / 0.169 (738) | 0.021 / 0.166 (1018) | - |
| oblate_ar3__oblate_ar3_test | 0.156 / 0.628 (726) | 0.081 / 0.363 (854) | 0.066 / 0.278 (702) | 0.058 / 0.249 (660) | 0.069 / 0.269 (1078) | - |
| prolateSpheroid__oblateSpheroid_test | 0.095 / 0.436 (702) | 0.067 / 0.420 (952) | 0.053 / 0.314 (668) | 0.051 / 0.276 (632) | 0.051 / 0.304 (1086) | - |
| prolate_ar2__oblateSpheroid_test | 0.116 / 0.370 (696) | 0.074 / 0.329 (904) | 0.061 / 0.293 (670) | 0.060 / 0.315 (652) | 0.065 / 0.329 (1124) | - |
| prolate_ar4__oblate_ar3_test | 0.309 / 1.051 (680) | 0.183 / 0.669 (874) | 0.141 / 0.638 (714) | 0.134 / 0.572 (726) | 0.145 / 0.647 (1034) | - |
| prolate_ar2__oblate_ar1p5_test | 0.089 / 0.266 (674) | 0.056 / 0.183 (926) | 0.052 / 0.208 (678) | 0.059 / 0.228 (708) | 0.067 / 0.283 (1032) | - |
| prolate_ar1p5__oblate_ar3_test | 0.206 / 0.769 (722) | 0.131 / 0.508 (904) | 0.101 / 0.389 (690) | 0.111 / 0.399 (652) | 0.126 / 0.429 (1076) | - |
| prolateSpheroid__prolate_ar2_test | 0.175 / 0.560 (654) | 0.097 / 0.428 (918) | 0.091 / 0.406 (648) | 0.088 / 0.354 (660) | 0.088 / 0.359 (1142) | - |
| oblateSpheroid__oblate_ar3_test | 0.189 / 0.699 (704) | 0.110 / 0.431 (886) | 0.083 / 0.373 (740) | 0.086 / 0.355 (622) | 0.086 / 0.346 (1048) | - |
| prolate_ar4__oblateSpheroid_test | 0.208 / 0.786 (676) | 0.133 / 0.608 (926) | 0.109 / 0.484 (718) | 0.102 / 0.411 (672) | 0.111 / 0.453 (1050) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.125 / 0.429 (638) | 0.083 / 0.350 (892) | 0.073 / 0.288 (658) | 0.071 / 0.267 (700) | 0.082 / 0.319 (1138) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.190 / 0.763 (702) | 0.119 / 0.545 (874) | 0.089 / 0.391 (718) | 0.076 / 0.355 (676) | 0.071 / 0.354 (1076) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.116 / 0.404 (662) | 0.071 / 0.278 (936) | 0.064 / 0.245 (688) | 0.069 / 0.236 (712) | 0.071 / 0.270 (1034) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.113 / 0.406 (750) | 0.073 / 0.284 (820) | 0.060 / 0.274 (676) | 0.061 / 0.258 (668) | 0.069 / 0.306 (1108) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.291 / 0.952 (716) | 0.125 / 0.500 (898) | 0.096 / 0.374 (724) | 0.089 / 0.366 (642) | 0.093 / 0.395 (1038) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.176 / 0.677 (684) | 0.115 / 0.455 (874) | 0.094 / 0.439 (746) | 0.097 / 0.460 (714) | 0.109 / 0.515 (1010) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.112 / 0.407 (630) | 0.072 / 0.280 (886) | 0.068 / 0.239 (638) | 0.068 / 0.286 (742) | 0.086 / 0.340 (1120) | - |
| prolate_ar2__oblate_ar3_test | 0.792 / 3.343 (680) | 0.693 / 2.703 (890) | 0.618 / 2.147 (726) | 0.524 / 1.823 (628) | 0.333 / 1.557 (1108) | - |
| prolate_ar4__oblate_ar1p5_test | 1.757 / 3.917 (718) | 1.530 / 2.935 (896) | 1.274 / 2.042 (696) | 0.945 / 1.415 (612) | 0.402 / 0.881 (1100) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.561 / 1.918 (732) | 0.549 / 1.549 (866) | 0.453 / 1.252 (682) | 0.361 / 1.081 (706) | 0.268 / 0.830 (1054) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.098 / 0.435 (706) | 0.063 / 0.321 (894) | 0.045 / 0.258 (670) | 0.048 / 0.260 (602) | 0.049 / 0.262 (1148) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 1.512 / 5.344 (706) | 1.254 / 4.595 (890) | 1.024 / 4.427 (718) | 0.821 / 4.180 (650) | 0.692 / 2.964 (1090) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.304 / 1.222 (666) | 0.215 / 1.012 (926) | 0.152 / 0.822 (644) | 0.123 / 0.699 (702) | 0.099 / 0.637 (1068) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.009 / 0.046 (90) | 0.000 / 0.002 (88) | 0.000 / 0.000 (92) | 0.000 / 0.000 (98) | 0.000 / 0.000 (142) | - |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.101 (98) | 0.001 / 0.005 (110) | 0.000 / 0.000 (84) | 0.000 / 0.000 (84) | 0.000 / 0.000 (128) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| prolate_ar4__prolate_ar4_test | 0.125 / 0.838 (76) | 0.037 / 0.278 (110) | 0.003 / 0.016 (90) | 0.002 / 0.005 (70) | 0.001 / 0.003 (154) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.006 / 0.022 (84) | 0.000 / 0.001 (108) | 0.000 / 0.000 (110) | 0.000 / 0.000 (92) | 0.000 / 0.000 (110) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| oblate_ar3__oblate_ar3_test | 0.079 / 0.471 (96) | 0.054 / 0.232 (120) | 0.037 / 0.150 (90) | 0.038 / 0.128 (82) | 0.027 / 0.109 (116) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| prolate_ar2__oblateSpheroid_test | 0.036 / 0.099 (92) | 0.009 / 0.016 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (138) | - |
| prolate_ar4__oblate_ar3_test | 0.110 / 0.607 (68) | 0.065 / 0.278 (142) | 0.035 / 0.110 (90) | 0.027 / 0.116 (86) | 0.017 / 0.077 (120) | - |
| prolate_ar2__oblate_ar1p5_test | 0.015 / 0.056 (78) | 0.001 / 0.002 (112) | 0.000 / 0.000 (92) | 0.000 / 0.000 (88) | 0.000 / 0.000 (132) | - |
| prolate_ar1p5__oblate_ar3_test | 0.216 / 0.670 (90) | 0.092 / 0.332 (114) | 0.050 / 0.143 (72) | 0.056 / 0.137 (94) | 0.040 / 0.119 (138) | - |
| prolateSpheroid__prolate_ar2_test | 0.034 / 0.235 (76) | 0.005 / 0.022 (148) | 0.002 / 0.007 (80) | 0.001 / 0.003 (80) | 0.001 / 0.003 (124) | - |
| oblateSpheroid__oblate_ar3_test | 0.141 / 0.681 (86) | 0.070 / 0.204 (134) | 0.048 / 0.136 (82) | 0.027 / 0.095 (70) | 0.026 / 0.079 (128) | - |
| prolate_ar4__oblateSpheroid_test | 0.076 / 0.406 (94) | 0.018 / 0.070 (102) | 0.003 / 0.010 (104) | 0.001 / 0.007 (80) | 0.001 / 0.003 (128) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.036 / 0.154 (68) | 0.004 / 0.023 (110) | 0.002 / 0.005 (102) | 0.001 / 0.004 (70) | 0.001 / 0.003 (158) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.041 / 0.317 (94) | 0.010 / 0.076 (98) | 0.002 / 0.006 (96) | 0.002 / 0.005 (86) | 0.001 / 0.005 (130) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.036 / 0.158 (102) | 0.005 / 0.024 (102) | 0.000 / 0.000 (92) | 0.000 / 0.000 (72) | 0.000 / 0.000 (130) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.140 / 0.539 (76) | 0.086 / 0.315 (118) | 0.037 / 0.141 (88) | 0.031 / 0.143 (90) | 0.019 / 0.093 (126) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.069 / 0.368 (72) | 0.014 / 0.035 (106) | 0.002 / 0.008 (86) | 0.001 / 0.005 (84) | 0.001 / 0.004 (158) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.055 / 0.117 (84) | 0.005 / 0.013 (88) | 0.001 / 0.003 (84) | 0.001 / 0.002 (106) | 0.000 / 0.002 (138) | - |
| prolate_ar2__oblate_ar3_test | 0.174 / 0.731 (100) | 0.072 / 0.242 (120) | 0.059 / 0.157 (90) | 0.033 / 0.120 (74) | 0.022 / 0.091 (122) | - |
| prolate_ar4__oblate_ar1p5_test | 0.123 / 0.724 (106) | 0.024 / 0.108 (102) | 0.005 / 0.015 (106) | 0.002 / 0.005 (70) | 0.000 / 0.001 (118) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.089 / 0.392 (72) | 0.020 / 0.074 (110) | 0.011 / 0.031 (84) | 0.008 / 0.024 (114) | 0.006 / 0.021 (126) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.054 / 0.309 (84) | 0.006 / 0.030 (68) | 0.001 / 0.001 (98) | 0.000 / 0.000 (90) | 0.000 / 0.000 (164) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 0.069 / 0.346 (86) | 0.033 / 0.131 (98) | 0.021 / 0.088 (88) | 0.018 / 0.076 (102) | 0.015 / 0.074 (136) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.038 / 0.212 (100) | 0.005 / 0.016 (114) | 0.001 / 0.004 (74) | 0.001 / 0.003 (74) | 0.000 / 0.002 (144) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblateSpheroid_test`: prolate_ar2 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar3_test`: prolate_ar4 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar1p5_test`: prolate_ar2 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar1p5__oblate_ar3_test`: prolate_ar1p5 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolate_ar2_test`: prolateSpheroid (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblate_ar3_test`: oblateSpheroid (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4000 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblateSpheroid_test`: prolate_ar4 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblate_ar1p5_test`: prolateSpheroid (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x0p75__prolateSpheroid_test`: prolateSpheroid_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__prolate_ar2_test`: prolate_ar2_x1p5 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__oblate_ar3_test`: oblate_ar3_x0p75 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__prolateSpheroid_x0p75_test`: oblateSpheroid_x1p5 (target or source) with prolateSpheroid_x0p75, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__oblateSpheroid_test`: prolate_ar2_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar3_test`: prolate_ar2 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar1p5_test`: prolate_ar4 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5__oblate_ar2p5_test`: prolate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test`: prolate_ar2p5_x1p25 (target or source) with prolate_ar2p5_x1p25, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__prolate_ar2_x1p5_test`: oblate_ar3_x0p75 (target or source) with prolate_ar2_x1p5, 2048 configurations (both orderings scored: 4054 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__oblateSpheroid_test`: prolate_ar2p5_x1p25 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2_x1p5 | 1.5 : 1.5 : 3 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3_x0p75 | 2.25 : 2.25 : 0.75 | 660 / 560; 0.0236 / 0.0510 | 1400 / 1190; 0.0086 / 0.0183 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar2p5_x1p25 | 1.25 : 1.25 : 3.125 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |

#### Two-body accuracy of `data/final_c/models/pair_poly_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4044 | 0.029 | 0.081 | 0.032 | 0.34 | 5.70 / 10.61 | 0.005 / 0.031 (510) | 0.032 / 0.088 | 0.002 / 0.009 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4040 | 0.045 | 0.181 | 0.056 | 0.49 | 5.19 / 11.22 | 0.016 / 0.067 (504) | 0.049 / 0.152 | 0.005 / 0.029 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.048 | 0.381 | 0.075 | 0.63 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.046 / 0.479 | 0.004 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4024 | 0.135 | 0.563 | 0.153 | 2.33 | 4.80 / 14.98 | 0.067 / 0.482 (500) | 0.129 / 0.612 | 0.030 / 0.169 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4006 | 0.031 | 0.088 | 0.035 | 0.33 | 5.57 / 10.07 | 0.003 / 0.014 (504) | 0.031 / 0.094 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.159 | 0.036 | 0.35 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.024 / 0.133 | 0.004 / 0.020 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4020 | 0.098 | 0.490 | 0.110 | 1.35 | 4.05 / 11.39 | 0.058 / 0.336 (504) | 0.085 / 0.370 | 0.070 / 0.366 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.075 | 0.418 | 0.097 | 0.84 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.064 / 0.369 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2__oblateSpheroid_test | 4046 | 0.087 | 0.340 | 0.104 | 0.88 | 4.89 / 11.55 | 0.021 / 0.065 (498) | 0.089 / 0.374 | 0.004 / 0.021 | 0.0 % |
| prolate_ar4__oblate_ar3_test | 4028 | 0.211 | 0.859 | 0.230 | 3.49 | 4.06 / 12.07 | 0.069 / 0.364 (506) | 0.189 / 0.770 | 0.075 / 0.483 | 0.0 % |
| prolate_ar2__oblate_ar1p5_test | 4018 | 0.067 | 0.235 | 0.080 | 0.79 | 5.45 / 10.67 | 0.008 / 0.033 (502) | 0.071 / 0.220 | 0.005 / 0.025 | 0.0 % |
| prolate_ar1p5__oblate_ar3_test | 4044 | 0.160 | 0.605 | 0.183 | 1.42 | 4.09 / 14.18 | 0.132 / 0.454 (508) | 0.170 / 0.678 | 0.115 / 0.565 | 0.0 % |
| prolateSpheroid__prolate_ar2_test | 4022 | 0.110 | 0.482 | 0.136 | 1.32 | 4.85 / 11.78 | 0.017 / 0.131 (508) | 0.099 / 0.438 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblate_ar3_test | 4000 | 0.135 | 0.518 | 0.151 | 1.49 | 4.25 / 11.86 | 0.091 / 0.419 (500) | 0.131 / 0.475 | 0.076 / 0.415 | 0.0 % |
| prolate_ar4__oblateSpheroid_test | 4042 | 0.161 | 0.668 | 0.184 | 2.12 | 4.77 / 12.73 | 0.043 / 0.254 (508) | 0.158 / 0.652 | 0.024 / 0.155 | 0.0 % |
| prolateSpheroid__oblate_ar1p5_test | 4026 | 0.097 | 0.383 | 0.115 | 1.07 | 4.97 / 11.76 | 0.018 / 0.081 (508) | 0.100 / 0.428 | 0.004 / 0.021 | 0.0 % |
| prolateSpheroid_x0p75__prolateSpheroid_test | 4046 | 0.124 | 0.606 | 0.164 | 1.36 | 4.72 / 13.40 | 0.024 / 0.203 (504) | 0.131 / 0.582 | 0.006 / 0.032 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.080 | 0.319 | 0.087 | 0.81 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.077 / 0.308 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2_x1p5__prolate_ar2_test | 4022 | 0.085 | 0.335 | 0.098 | 0.89 | 4.83 / 11.46 | 0.021 / 0.101 (498) | 0.087 / 0.338 | 0.008 / 0.050 | 0.0 % |
| oblate_ar3_x0p75__oblate_ar3_test | 4018 | 0.176 | 0.691 | 0.191 | 2.20 | 3.85 / 11.95 | 0.090 / 0.371 (498) | 0.156 / 0.544 | 0.074 / 0.397 | 0.0 % |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 4028 | 0.132 | 0.544 | 0.150 | 1.05 | 3.56 / 12.87 | 0.037 / 0.211 (506) | 0.138 / 0.513 | 0.007 / 0.043 | 0.0 % |
| prolate_ar2_x1p5__oblateSpheroid_test | 4016 | 0.086 | 0.332 | 0.099 | 1.03 | 4.90 / 10.45 | 0.031 / 0.078 (500) | 0.092 / 0.344 | 0.005 / 0.031 | 0.0 % |
| prolate_ar2__oblate_ar3_test | 4032 | 0.757 | 3.237 | 0.871 | 6.97 | 3.98 / 12.62 | 0.112 / 0.491 (506) | 0.742 / 3.305 | 0.098 / 0.537 | 0.0 % |
| prolate_ar4__oblate_ar1p5_test | 4022 | 0.820 | 2.639 | 0.913 | 5.11 | 5.13 / 14.89 | 0.073 / 0.459 (502) | 0.814 / 2.925 | 0.038 / 0.249 | 0.0 % |
| prolate_ar2p5__oblate_ar2p5_test | 4040 | 0.392 | 1.762 | 0.474 | 4.57 | 4.39 / 11.86 | 0.046 / 0.226 (506) | 0.398 / 1.766 | 0.039 / 0.257 | 0.0 % |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 4020 | 0.084 | 0.365 | 0.097 | 1.12 | 4.86 / 10.50 | 0.031 / 0.199 (504) | 0.071 / 0.380 | 0.016 / 0.102 | 0.0 % |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 4054 | 1.243 | 6.519 | 1.520 | 17.98 | 4.50 / 11.02 | 0.044 / 0.240 (510) | 1.349 / 6.126 | 0.048 / 0.291 | 0.0 % |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 4006 | 0.356 | 1.364 | 0.398 | 2.44 | 4.85 / 10.92 | 0.022 / 0.134 (506) | 0.372 / 1.380 | 0.015 / 0.099 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.034 / 0.084 (652) | 0.023 / 0.065 (896) | 0.024 / 0.084 (690) | 0.029 / 0.108 (688) | 0.040 / 0.150 (1118) | - |
| prolate_ar2__prolate_ar2_test | 0.058 / 0.195 (708) | 0.043 / 0.178 (840) | 0.030 / 0.127 (756) | 0.034 / 0.189 (620) | 0.039 / 0.281 (1116) | - |
| prolateSpheroid__prolateSpheroid_test | 0.067 / 0.454 (684) | 0.039 / 0.374 (898) | 0.035 / 0.297 (660) | 0.035 / 0.209 (754) | 0.032 / 0.252 (1038) | - |
| prolate_ar4__prolate_ar4_test | 0.189 / 0.741 (680) | 0.124 / 0.472 (904) | 0.105 / 0.465 (734) | 0.079 / 0.324 (660) | 0.066 / 0.317 (1046) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.037 / 0.090 (652) | 0.026 / 0.078 (922) | 0.024 / 0.090 (714) | 0.033 / 0.105 (704) | 0.044 / 0.139 (1014) | - |
| oblateSpheroid__oblateSpheroid_test | 0.039 / 0.182 (650) | 0.021 / 0.143 (936) | 0.017 / 0.127 (680) | 0.017 / 0.177 (738) | 0.024 / 0.171 (1018) | - |
| oblate_ar3__oblate_ar3_test | 0.143 / 0.658 (726) | 0.079 / 0.379 (854) | 0.062 / 0.288 (702) | 0.055 / 0.261 (660) | 0.070 / 0.280 (1078) | - |
| prolateSpheroid__oblateSpheroid_test | 0.101 / 0.459 (702) | 0.068 / 0.439 (952) | 0.053 / 0.301 (668) | 0.049 / 0.281 (632) | 0.054 / 0.300 (1086) | - |
| prolate_ar2__oblateSpheroid_test | 0.118 / 0.390 (696) | 0.074 / 0.317 (904) | 0.065 / 0.276 (670) | 0.061 / 0.272 (652) | 0.067 / 0.307 (1124) | - |
| prolate_ar4__oblate_ar3_test | 0.316 / 1.163 (680) | 0.165 / 0.677 (874) | 0.126 / 0.614 (714) | 0.139 / 0.587 (726) | 0.147 / 0.588 (1034) | - |
| prolate_ar2__oblate_ar1p5_test | 0.091 / 0.290 (674) | 0.054 / 0.179 (926) | 0.051 / 0.193 (678) | 0.054 / 0.231 (708) | 0.067 / 0.286 (1032) | - |
| prolate_ar1p5__oblate_ar3_test | 0.227 / 0.790 (722) | 0.130 / 0.505 (904) | 0.105 / 0.391 (690) | 0.115 / 0.368 (652) | 0.113 / 0.416 (1076) | - |
| prolateSpheroid__prolate_ar2_test | 0.151 / 0.557 (654) | 0.095 / 0.462 (918) | 0.085 / 0.402 (648) | 0.087 / 0.368 (660) | 0.078 / 0.385 (1142) | - |
| oblateSpheroid__oblate_ar3_test | 0.193 / 0.681 (704) | 0.112 / 0.405 (886) | 0.093 / 0.357 (740) | 0.084 / 0.346 (622) | 0.082 / 0.338 (1048) | - |
| prolate_ar4__oblateSpheroid_test | 0.224 / 0.820 (676) | 0.147 / 0.629 (926) | 0.112 / 0.487 (718) | 0.110 / 0.443 (672) | 0.098 / 0.436 (1050) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.135 / 0.465 (638) | 0.082 / 0.353 (892) | 0.071 / 0.294 (658) | 0.074 / 0.272 (700) | 0.077 / 0.309 (1138) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.170 / 0.774 (702) | 0.113 / 0.552 (874) | 0.089 / 0.403 (718) | 0.079 / 0.347 (676) | 0.071 / 0.368 (1076) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.110 / 0.397 (662) | 0.064 / 0.271 (936) | 0.060 / 0.237 (688) | 0.062 / 0.252 (712) | 0.078 / 0.281 (1034) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.112 / 0.402 (750) | 0.066 / 0.280 (820) | 0.065 / 0.269 (676) | 0.069 / 0.265 (668) | 0.077 / 0.294 (1108) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.275 / 0.977 (716) | 0.126 / 0.484 (898) | 0.091 / 0.379 (724) | 0.095 / 0.373 (642) | 0.094 / 0.414 (1038) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.179 / 0.660 (684) | 0.113 / 0.474 (874) | 0.098 / 0.427 (746) | 0.099 / 0.452 (714) | 0.111 / 0.493 (1010) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.119 / 0.402 (630) | 0.071 / 0.293 (886) | 0.062 / 0.239 (638) | 0.065 / 0.276 (742) | 0.077 / 0.342 (1120) | - |
| prolate_ar2__oblate_ar3_test | 0.980 / 3.832 (680) | 0.766 / 3.239 (890) | 0.638 / 2.479 (726) | 0.431 / 1.775 (628) | 0.284 / 1.227 (1108) | - |
| prolate_ar4__oblate_ar1p5_test | 1.151 / 3.189 (718) | 0.815 / 2.630 (896) | 0.478 / 1.815 (696) | 0.286 / 1.201 (612) | 0.171 / 0.808 (1100) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.501 / 2.112 (732) | 0.399 / 1.660 (866) | 0.317 / 1.346 (682) | 0.217 / 0.950 (706) | 0.149 / 0.695 (1054) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.121 / 0.457 (706) | 0.075 / 0.339 (894) | 0.049 / 0.225 (670) | 0.042 / 0.194 (602) | 0.045 / 0.222 (1148) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 1.652 / 7.772 (706) | 1.201 / 6.252 (890) | 0.921 / 4.803 (718) | 0.778 / 3.917 (650) | 0.538 / 3.065 (1090) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.440 / 1.661 (666) | 0.368 / 1.302 (926) | 0.296 / 0.979 (644) | 0.237 / 0.660 (702) | 0.187 / 0.508 (1068) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.009 / 0.046 (90) | 0.000 / 0.002 (88) | 0.000 / 0.000 (92) | 0.000 / 0.000 (98) | 0.000 / 0.000 (142) | - |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.101 (98) | 0.001 / 0.005 (110) | 0.000 / 0.000 (84) | 0.000 / 0.000 (84) | 0.000 / 0.000 (128) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| prolate_ar4__prolate_ar4_test | 0.125 / 0.838 (76) | 0.037 / 0.278 (110) | 0.003 / 0.016 (90) | 0.002 / 0.005 (70) | 0.001 / 0.003 (154) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.006 / 0.022 (84) | 0.000 / 0.001 (108) | 0.000 / 0.000 (110) | 0.000 / 0.000 (92) | 0.000 / 0.000 (110) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| oblate_ar3__oblate_ar3_test | 0.079 / 0.471 (96) | 0.054 / 0.232 (120) | 0.037 / 0.150 (90) | 0.038 / 0.128 (82) | 0.027 / 0.109 (116) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| prolate_ar2__oblateSpheroid_test | 0.036 / 0.099 (92) | 0.009 / 0.016 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (138) | - |
| prolate_ar4__oblate_ar3_test | 0.110 / 0.607 (68) | 0.065 / 0.278 (142) | 0.035 / 0.110 (90) | 0.027 / 0.116 (86) | 0.017 / 0.077 (120) | - |
| prolate_ar2__oblate_ar1p5_test | 0.015 / 0.056 (78) | 0.001 / 0.002 (112) | 0.000 / 0.000 (92) | 0.000 / 0.000 (88) | 0.000 / 0.000 (132) | - |
| prolate_ar1p5__oblate_ar3_test | 0.216 / 0.670 (90) | 0.092 / 0.332 (114) | 0.050 / 0.143 (72) | 0.056 / 0.137 (94) | 0.040 / 0.119 (138) | - |
| prolateSpheroid__prolate_ar2_test | 0.034 / 0.235 (76) | 0.005 / 0.022 (148) | 0.002 / 0.007 (80) | 0.001 / 0.003 (80) | 0.001 / 0.003 (124) | - |
| oblateSpheroid__oblate_ar3_test | 0.141 / 0.681 (86) | 0.070 / 0.204 (134) | 0.048 / 0.136 (82) | 0.027 / 0.095 (70) | 0.026 / 0.079 (128) | - |
| prolate_ar4__oblateSpheroid_test | 0.076 / 0.406 (94) | 0.018 / 0.070 (102) | 0.003 / 0.010 (104) | 0.001 / 0.007 (80) | 0.001 / 0.003 (128) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.036 / 0.154 (68) | 0.004 / 0.023 (110) | 0.002 / 0.005 (102) | 0.001 / 0.004 (70) | 0.001 / 0.003 (158) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.041 / 0.317 (94) | 0.010 / 0.076 (98) | 0.002 / 0.006 (96) | 0.002 / 0.005 (86) | 0.001 / 0.005 (130) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.036 / 0.158 (102) | 0.005 / 0.024 (102) | 0.000 / 0.000 (92) | 0.000 / 0.000 (72) | 0.000 / 0.000 (130) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.140 / 0.539 (76) | 0.086 / 0.315 (118) | 0.037 / 0.141 (88) | 0.031 / 0.143 (90) | 0.019 / 0.093 (126) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.069 / 0.368 (72) | 0.014 / 0.035 (106) | 0.002 / 0.008 (86) | 0.001 / 0.005 (84) | 0.001 / 0.004 (158) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.055 / 0.117 (84) | 0.005 / 0.013 (88) | 0.001 / 0.003 (84) | 0.001 / 0.002 (106) | 0.000 / 0.002 (138) | - |
| prolate_ar2__oblate_ar3_test | 0.174 / 0.731 (100) | 0.072 / 0.242 (120) | 0.059 / 0.157 (90) | 0.033 / 0.120 (74) | 0.022 / 0.091 (122) | - |
| prolate_ar4__oblate_ar1p5_test | 0.123 / 0.724 (106) | 0.024 / 0.108 (102) | 0.005 / 0.015 (106) | 0.002 / 0.005 (70) | 0.000 / 0.001 (118) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.089 / 0.392 (72) | 0.020 / 0.074 (110) | 0.011 / 0.031 (84) | 0.008 / 0.024 (114) | 0.006 / 0.021 (126) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.054 / 0.309 (84) | 0.006 / 0.030 (68) | 0.001 / 0.001 (98) | 0.000 / 0.000 (90) | 0.000 / 0.000 (164) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 0.069 / 0.346 (86) | 0.033 / 0.131 (98) | 0.021 / 0.088 (88) | 0.018 / 0.076 (102) | 0.015 / 0.074 (136) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.038 / 0.212 (100) | 0.005 / 0.016 (114) | 0.001 / 0.004 (74) | 0.001 / 0.003 (74) | 0.000 / 0.002 (144) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly_s1.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 1: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblateSpheroid_test`: prolate_ar2 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar3_test`: prolate_ar4 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar1p5_test`: prolate_ar2 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar1p5__oblate_ar3_test`: prolate_ar1p5 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolate_ar2_test`: prolateSpheroid (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblate_ar3_test`: oblateSpheroid (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4000 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblateSpheroid_test`: prolate_ar4 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblate_ar1p5_test`: prolateSpheroid (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x0p75__prolateSpheroid_test`: prolateSpheroid_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__prolate_ar2_test`: prolate_ar2_x1p5 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__oblate_ar3_test`: oblate_ar3_x0p75 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__prolateSpheroid_x0p75_test`: oblateSpheroid_x1p5 (target or source) with prolateSpheroid_x0p75, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__oblateSpheroid_test`: prolate_ar2_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar3_test`: prolate_ar2 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar1p5_test`: prolate_ar4 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5__oblate_ar2p5_test`: prolate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test`: prolate_ar2p5_x1p25 (target or source) with prolate_ar2p5_x1p25, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__prolate_ar2_x1p5_test`: oblate_ar3_x0p75 (target or source) with prolate_ar2_x1p5, 2048 configurations (both orderings scored: 4054 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__oblateSpheroid_test`: prolate_ar2p5_x1p25 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2_x1p5 | 1.5 : 1.5 : 3 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3_x0p75 | 2.25 : 2.25 : 0.75 | 660 / 560; 0.0236 / 0.0510 | 1400 / 1190; 0.0086 / 0.0183 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar2p5_x1p25 | 1.25 : 1.25 : 3.125 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |

#### Two-body accuracy of `data/final_c/models/pair_poly_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4044 | 0.031 | 0.080 | 0.035 | 0.34 | 5.70 / 10.61 | 0.005 / 0.031 (510) | 0.034 / 0.092 | 0.002 / 0.009 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4040 | 0.044 | 0.182 | 0.056 | 0.50 | 5.19 / 11.22 | 0.016 / 0.067 (504) | 0.048 / 0.159 | 0.005 / 0.029 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.051 | 0.373 | 0.076 | 0.62 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.053 / 0.484 | 0.004 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4024 | 0.144 | 0.556 | 0.160 | 2.25 | 4.80 / 14.98 | 0.067 / 0.482 (500) | 0.143 / 0.605 | 0.030 / 0.169 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4006 | 0.029 | 0.081 | 0.032 | 0.34 | 5.57 / 10.07 | 0.003 / 0.014 (504) | 0.027 / 0.087 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.147 | 0.035 | 0.34 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.027 / 0.119 | 0.004 / 0.020 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4020 | 0.095 | 0.476 | 0.109 | 1.36 | 4.05 / 11.39 | 0.058 / 0.336 (504) | 0.080 / 0.349 | 0.070 / 0.366 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.074 | 0.412 | 0.094 | 0.85 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.067 / 0.333 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2__oblateSpheroid_test | 4046 | 0.082 | 0.351 | 0.101 | 0.90 | 4.89 / 11.55 | 0.021 / 0.065 (498) | 0.091 / 0.365 | 0.004 / 0.021 | 0.0 % |
| prolate_ar4__oblate_ar3_test | 4028 | 0.216 | 0.829 | 0.236 | 3.12 | 4.06 / 12.07 | 0.069 / 0.364 (506) | 0.192 / 0.738 | 0.075 / 0.483 | 0.0 % |
| prolate_ar2__oblate_ar1p5_test | 4018 | 0.068 | 0.242 | 0.081 | 0.80 | 5.45 / 10.67 | 0.008 / 0.033 (502) | 0.068 / 0.234 | 0.005 / 0.025 | 0.0 % |
| prolate_ar1p5__oblate_ar3_test | 4044 | 0.153 | 0.590 | 0.175 | 1.39 | 4.09 / 14.18 | 0.132 / 0.454 (508) | 0.163 / 0.664 | 0.115 / 0.565 | 0.0 % |
| prolateSpheroid__prolate_ar2_test | 4022 | 0.111 | 0.477 | 0.138 | 1.22 | 4.85 / 11.78 | 0.017 / 0.131 (508) | 0.102 / 0.429 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblate_ar3_test | 4000 | 0.141 | 0.515 | 0.153 | 1.59 | 4.25 / 11.86 | 0.091 / 0.419 (500) | 0.129 / 0.501 | 0.076 / 0.415 | 0.0 % |
| prolate_ar4__oblateSpheroid_test | 4042 | 0.154 | 0.633 | 0.178 | 2.05 | 4.77 / 12.73 | 0.043 / 0.254 (508) | 0.157 / 0.639 | 0.024 / 0.155 | 0.0 % |
| prolateSpheroid__oblate_ar1p5_test | 4026 | 0.099 | 0.374 | 0.116 | 1.05 | 4.97 / 11.76 | 0.018 / 0.081 (508) | 0.110 / 0.440 | 0.004 / 0.021 | 0.0 % |
| prolateSpheroid_x0p75__prolateSpheroid_test | 4046 | 0.125 | 0.607 | 0.162 | 1.30 | 4.72 / 13.40 | 0.024 / 0.203 (504) | 0.139 / 0.546 | 0.006 / 0.032 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.088 | 0.315 | 0.093 | 0.82 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.088 / 0.295 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2_x1p5__prolate_ar2_test | 4022 | 0.095 | 0.335 | 0.107 | 0.91 | 4.83 / 11.46 | 0.021 / 0.101 (498) | 0.104 / 0.343 | 0.008 / 0.050 | 0.0 % |
| oblate_ar3_x0p75__oblate_ar3_test | 4018 | 0.162 | 0.646 | 0.178 | 2.16 | 3.85 / 11.95 | 0.090 / 0.371 (498) | 0.143 / 0.490 | 0.074 / 0.397 | 0.0 % |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 4028 | 0.123 | 0.551 | 0.143 | 1.04 | 3.56 / 12.87 | 0.037 / 0.211 (506) | 0.122 / 0.498 | 0.007 / 0.043 | 0.0 % |
| prolate_ar2_x1p5__oblateSpheroid_test | 4016 | 0.094 | 0.340 | 0.106 | 1.01 | 4.90 / 10.45 | 0.031 / 0.078 (500) | 0.108 / 0.349 | 0.005 / 0.031 | 0.0 % |
| prolate_ar2__oblate_ar3_test | 4032 | 0.616 | 3.276 | 0.772 | 7.57 | 3.98 / 12.62 | 0.112 / 0.491 (506) | 0.605 / 3.374 | 0.098 / 0.537 | 0.0 % |
| prolate_ar4__oblate_ar1p5_test | 4022 | 1.155 | 3.075 | 1.225 | 5.10 | 5.13 / 14.89 | 0.073 / 0.459 (502) | 1.298 / 3.350 | 0.038 / 0.249 | 0.0 % |
| prolate_ar2p5__oblate_ar2p5_test | 4040 | 0.409 | 1.837 | 0.487 | 4.97 | 4.39 / 11.86 | 0.046 / 0.226 (506) | 0.390 / 1.777 | 0.039 / 0.257 | 0.0 % |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 4020 | 0.064 | 0.356 | 0.080 | 0.74 | 4.86 / 10.50 | 0.031 / 0.199 (504) | 0.061 / 0.368 | 0.016 / 0.102 | 0.0 % |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 4054 | 1.371 | 4.504 | 1.499 | 22.46 | 4.50 / 11.02 | 0.044 / 0.240 (510) | 1.401 / 4.157 | 0.048 / 0.291 | 0.0 % |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 4006 | 0.311 | 0.973 | 0.337 | 2.75 | 4.85 / 10.92 | 0.022 / 0.134 (506) | 0.336 / 1.067 | 0.015 / 0.099 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.038 / 0.081 (652) | 0.025 / 0.065 (896) | 0.022 / 0.086 (690) | 0.026 / 0.106 (688) | 0.043 / 0.148 (1118) | - |
| prolate_ar2__prolate_ar2_test | 0.056 / 0.193 (708) | 0.039 / 0.187 (840) | 0.034 / 0.124 (756) | 0.036 / 0.177 (620) | 0.043 / 0.272 (1116) | - |
| prolateSpheroid__prolateSpheroid_test | 0.070 / 0.434 (684) | 0.047 / 0.376 (898) | 0.035 / 0.296 (660) | 0.036 / 0.217 (754) | 0.034 / 0.233 (1038) | - |
| prolate_ar4__prolate_ar4_test | 0.211 / 0.730 (680) | 0.127 / 0.470 (904) | 0.101 / 0.459 (734) | 0.080 / 0.324 (660) | 0.069 / 0.300 (1046) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.032 / 0.080 (652) | 0.024 / 0.073 (922) | 0.023 / 0.087 (714) | 0.031 / 0.100 (704) | 0.040 / 0.135 (1014) | - |
| oblateSpheroid__oblateSpheroid_test | 0.039 / 0.165 (650) | 0.021 / 0.133 (936) | 0.018 / 0.118 (680) | 0.019 / 0.169 (738) | 0.026 / 0.165 (1018) | - |
| oblate_ar3__oblate_ar3_test | 0.132 / 0.638 (726) | 0.081 / 0.376 (854) | 0.066 / 0.265 (702) | 0.064 / 0.258 (660) | 0.074 / 0.272 (1078) | - |
| prolateSpheroid__oblateSpheroid_test | 0.099 / 0.435 (702) | 0.067 / 0.440 (952) | 0.054 / 0.324 (668) | 0.052 / 0.302 (632) | 0.053 / 0.316 (1086) | - |
| prolate_ar2__oblateSpheroid_test | 0.111 / 0.390 (696) | 0.068 / 0.334 (904) | 0.061 / 0.297 (670) | 0.061 / 0.313 (652) | 0.068 / 0.313 (1124) | - |
| prolate_ar4__oblate_ar3_test | 0.314 / 1.129 (680) | 0.182 / 0.644 (874) | 0.139 / 0.592 (714) | 0.133 / 0.557 (726) | 0.172 / 0.565 (1034) | - |
| prolate_ar2__oblate_ar1p5_test | 0.094 / 0.288 (674) | 0.055 / 0.196 (926) | 0.049 / 0.214 (678) | 0.052 / 0.245 (708) | 0.068 / 0.270 (1032) | - |
| prolate_ar1p5__oblate_ar3_test | 0.217 / 0.753 (722) | 0.126 / 0.515 (904) | 0.099 / 0.384 (690) | 0.102 / 0.386 (652) | 0.126 / 0.425 (1076) | - |
| prolateSpheroid__prolate_ar2_test | 0.154 / 0.564 (654) | 0.090 / 0.444 (918) | 0.090 / 0.392 (648) | 0.089 / 0.366 (660) | 0.080 / 0.372 (1142) | - |
| oblateSpheroid__oblate_ar3_test | 0.204 / 0.671 (704) | 0.117 / 0.416 (886) | 0.091 / 0.348 (740) | 0.086 / 0.330 (622) | 0.095 / 0.356 (1048) | - |
| prolate_ar4__oblateSpheroid_test | 0.212 / 0.759 (676) | 0.139 / 0.609 (926) | 0.114 / 0.482 (718) | 0.105 / 0.423 (672) | 0.099 / 0.437 (1050) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.135 / 0.456 (638) | 0.083 / 0.332 (892) | 0.073 / 0.294 (658) | 0.079 / 0.298 (700) | 0.090 / 0.312 (1138) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.174 / 0.778 (702) | 0.112 / 0.554 (874) | 0.088 / 0.393 (718) | 0.079 / 0.341 (676) | 0.079 / 0.360 (1076) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.130 / 0.394 (662) | 0.069 / 0.266 (936) | 0.056 / 0.237 (688) | 0.057 / 0.232 (712) | 0.066 / 0.260 (1034) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.125 / 0.401 (750) | 0.081 / 0.283 (820) | 0.063 / 0.270 (676) | 0.073 / 0.263 (668) | 0.084 / 0.301 (1108) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.246 / 0.900 (716) | 0.125 / 0.475 (898) | 0.098 / 0.362 (724) | 0.088 / 0.366 (642) | 0.094 / 0.402 (1038) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.164 / 0.670 (684) | 0.108 / 0.466 (874) | 0.089 / 0.460 (746) | 0.090 / 0.456 (714) | 0.117 / 0.513 (1010) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.135 / 0.404 (630) | 0.077 / 0.302 (886) | 0.065 / 0.252 (638) | 0.062 / 0.308 (742) | 0.082 / 0.357 (1120) | - |
| prolate_ar2__oblate_ar3_test | 0.829 / 3.896 (680) | 0.639 / 3.319 (890) | 0.417 / 2.380 (726) | 0.306 / 1.657 (628) | 0.253 / 1.170 (1108) | - |
| prolate_ar4__oblate_ar1p5_test | 1.568 / 3.773 (718) | 1.164 / 2.984 (896) | 0.790 / 2.133 (696) | 0.485 / 1.387 (612) | 0.252 / 0.851 (1100) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.509 / 2.145 (732) | 0.436 / 1.849 (866) | 0.316 / 1.309 (682) | 0.234 / 0.965 (706) | 0.167 / 0.732 (1054) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.089 / 0.456 (706) | 0.055 / 0.316 (894) | 0.045 / 0.218 (670) | 0.043 / 0.183 (602) | 0.049 / 0.206 (1148) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 1.561 / 5.207 (706) | 1.453 / 4.207 (890) | 1.278 / 3.791 (718) | 1.010 / 3.456 (650) | 0.736 / 3.328 (1090) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.385 / 1.139 (666) | 0.330 / 0.947 (926) | 0.264 / 0.769 (644) | 0.183 / 0.597 (702) | 0.109 / 0.510 (1068) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.009 / 0.046 (90) | 0.000 / 0.002 (88) | 0.000 / 0.000 (92) | 0.000 / 0.000 (98) | 0.000 / 0.000 (142) | - |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.101 (98) | 0.001 / 0.005 (110) | 0.000 / 0.000 (84) | 0.000 / 0.000 (84) | 0.000 / 0.000 (128) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| prolate_ar4__prolate_ar4_test | 0.125 / 0.838 (76) | 0.037 / 0.278 (110) | 0.003 / 0.016 (90) | 0.002 / 0.005 (70) | 0.001 / 0.003 (154) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.006 / 0.022 (84) | 0.000 / 0.001 (108) | 0.000 / 0.000 (110) | 0.000 / 0.000 (92) | 0.000 / 0.000 (110) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| oblate_ar3__oblate_ar3_test | 0.079 / 0.471 (96) | 0.054 / 0.232 (120) | 0.037 / 0.150 (90) | 0.038 / 0.128 (82) | 0.027 / 0.109 (116) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| prolate_ar2__oblateSpheroid_test | 0.036 / 0.099 (92) | 0.009 / 0.016 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (138) | - |
| prolate_ar4__oblate_ar3_test | 0.110 / 0.607 (68) | 0.065 / 0.278 (142) | 0.035 / 0.110 (90) | 0.027 / 0.116 (86) | 0.017 / 0.077 (120) | - |
| prolate_ar2__oblate_ar1p5_test | 0.015 / 0.056 (78) | 0.001 / 0.002 (112) | 0.000 / 0.000 (92) | 0.000 / 0.000 (88) | 0.000 / 0.000 (132) | - |
| prolate_ar1p5__oblate_ar3_test | 0.216 / 0.670 (90) | 0.092 / 0.332 (114) | 0.050 / 0.143 (72) | 0.056 / 0.137 (94) | 0.040 / 0.119 (138) | - |
| prolateSpheroid__prolate_ar2_test | 0.034 / 0.235 (76) | 0.005 / 0.022 (148) | 0.002 / 0.007 (80) | 0.001 / 0.003 (80) | 0.001 / 0.003 (124) | - |
| oblateSpheroid__oblate_ar3_test | 0.141 / 0.681 (86) | 0.070 / 0.204 (134) | 0.048 / 0.136 (82) | 0.027 / 0.095 (70) | 0.026 / 0.079 (128) | - |
| prolate_ar4__oblateSpheroid_test | 0.076 / 0.406 (94) | 0.018 / 0.070 (102) | 0.003 / 0.010 (104) | 0.001 / 0.007 (80) | 0.001 / 0.003 (128) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.036 / 0.154 (68) | 0.004 / 0.023 (110) | 0.002 / 0.005 (102) | 0.001 / 0.004 (70) | 0.001 / 0.003 (158) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.041 / 0.317 (94) | 0.010 / 0.076 (98) | 0.002 / 0.006 (96) | 0.002 / 0.005 (86) | 0.001 / 0.005 (130) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.036 / 0.158 (102) | 0.005 / 0.024 (102) | 0.000 / 0.000 (92) | 0.000 / 0.000 (72) | 0.000 / 0.000 (130) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.140 / 0.539 (76) | 0.086 / 0.315 (118) | 0.037 / 0.141 (88) | 0.031 / 0.143 (90) | 0.019 / 0.093 (126) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.069 / 0.368 (72) | 0.014 / 0.035 (106) | 0.002 / 0.008 (86) | 0.001 / 0.005 (84) | 0.001 / 0.004 (158) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.055 / 0.117 (84) | 0.005 / 0.013 (88) | 0.001 / 0.003 (84) | 0.001 / 0.002 (106) | 0.000 / 0.002 (138) | - |
| prolate_ar2__oblate_ar3_test | 0.174 / 0.731 (100) | 0.072 / 0.242 (120) | 0.059 / 0.157 (90) | 0.033 / 0.120 (74) | 0.022 / 0.091 (122) | - |
| prolate_ar4__oblate_ar1p5_test | 0.123 / 0.724 (106) | 0.024 / 0.108 (102) | 0.005 / 0.015 (106) | 0.002 / 0.005 (70) | 0.000 / 0.001 (118) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.089 / 0.392 (72) | 0.020 / 0.074 (110) | 0.011 / 0.031 (84) | 0.008 / 0.024 (114) | 0.006 / 0.021 (126) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.054 / 0.309 (84) | 0.006 / 0.030 (68) | 0.001 / 0.001 (98) | 0.000 / 0.000 (90) | 0.000 / 0.000 (164) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 0.069 / 0.346 (86) | 0.033 / 0.131 (98) | 0.021 / 0.088 (88) | 0.018 / 0.076 (102) | 0.015 / 0.074 (136) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.038 / 0.212 (100) | 0.005 / 0.016 (114) | 0.001 / 0.004 (74) | 0.001 / 0.003 (74) | 0.000 / 0.002 (144) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly_s2.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 2: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblateSpheroid_test`: prolate_ar2 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar3_test`: prolate_ar4 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar1p5_test`: prolate_ar2 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar1p5__oblate_ar3_test`: prolate_ar1p5 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolate_ar2_test`: prolateSpheroid (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblate_ar3_test`: oblateSpheroid (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4000 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblateSpheroid_test`: prolate_ar4 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblate_ar1p5_test`: prolateSpheroid (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x0p75__prolateSpheroid_test`: prolateSpheroid_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__prolate_ar2_test`: prolate_ar2_x1p5 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__oblate_ar3_test`: oblate_ar3_x0p75 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__prolateSpheroid_x0p75_test`: oblateSpheroid_x1p5 (target or source) with prolateSpheroid_x0p75, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__oblateSpheroid_test`: prolate_ar2_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar3_test`: prolate_ar2 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar1p5_test`: prolate_ar4 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5__oblate_ar2p5_test`: prolate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test`: prolate_ar2p5_x1p25 (target or source) with prolate_ar2p5_x1p25, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__prolate_ar2_x1p5_test`: oblate_ar3_x0p75 (target or source) with prolate_ar2_x1p5, 2048 configurations (both orderings scored: 4054 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__oblateSpheroid_test`: prolate_ar2p5_x1p25 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar1p5 | 1 : 1 : 1.5 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| prolate_ar4 | 1 : 1 : 4 | 660 / 560; 0.0019 / 0.0009 | 1400 / 1190; 0.0003 / 0.0008 |
| oblate_ar1p5 | 1.5 : 1.5 : 1 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2_x1p5 | 1.5 : 1.5 : 3 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3_x0p75 | 2.25 : 2.25 : 0.75 | 660 / 560; 0.0236 / 0.0510 | 1400 / 1190; 0.0086 / 0.0183 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar2p5_x1p25 | 1.25 : 1.25 : 3.125 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |

#### Suspensions of prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.53 (4.64 / 3.46; 1.17) | 2.69 (2.78 / 1.60; 0.96) | 2.09 (2.17 / 1.26; 0.77) | 0.016 (0.014 / 0.026; 0.001) (1) |
| 0.05 | 200 | 10 | 7.90 (8.10 / 5.83; 2.30) | 5.47 (5.65 / 3.42; 1.96) | 3.88 (4.00 / 2.44; 1.41) | 0.030 (0.028 / 0.046; 0.002) (1) |
| 0.075 | 200 | 10 | 9.69 (9.82 / 7.73; 3.24) | 7.19 (7.31 / 5.12; 2.82) | 4.67 (4.75 / 3.38; 1.85) | 0.064 (0.054 / 0.129; 0.011) (1) |
| 0.1 | 200 | 10 | 14.39 (14.87 / 9.67; 4.30) | 10.82 (11.20 / 6.90; 3.78) | 6.34 (6.55 / 4.16; 2.32) | 0.034 (0.032 / 0.050; 0.003) (1) |
| 0.15 | 200 | 10 | 18.52 (18.90 / 14.62; 6.19) | 14.85 (15.19 / 10.98; 5.50) | 8.09 (8.27 / 6.04; 3.02) | 0.053 (0.041 / 0.196; 0.004) (1) |
| 0.2 | 200 | 8 | 23.17 (23.45 / 19.58; 8.26) | 19.20 (19.50 / 14.99; 7.41) | 9.48 (9.62 / 7.59; 3.76) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configurations**: N in [200] particles, shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |

#### Suspensions of prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.46 (7.72 / 5.45; 2.78) | 4.57 (4.76 / 2.88; 1.96) | 2.84 (2.94 / 1.99; 1.08) | 0.035 (0.021 / 0.076; 0.003) (1) |
| 0.05 | 100 | 5 | 6.80 (6.95 / 5.13; 2.42) | 4.47 (4.57 / 3.22; 1.89) | 3.08 (3.15 / 2.29; 1.18) | 0.026 (0.023 / 0.051; 0.002) (1) |
| 0.05 | 200 | 5 | 7.84 (8.05 / 5.69; 2.30) | 5.48 (5.66 / 3.36; 1.96) | 3.93 (4.06 / 2.39; 1.43) | not measured |
| 0.05 | 300 | 5 | 7.93 (8.13 / 5.79; 2.21) | 5.65 (5.84 / 3.34; 1.96) | 3.89 (4.01 / 2.35; 1.51) | not measured |
| 0.1 | 50 | 5 | 13.21 (13.48 / 11.12; 4.77) | 8.25 (8.45 / 6.57; 3.57) | 4.27 (4.34 / 3.73; 1.46) | 0.050 (0.044 / 0.082; 0.008) (1) |
| 0.1 | 100 | 5 | 14.22 (14.71 / 9.71; 4.28) | 10.08 (10.46 / 6.47; 3.55) | 5.55 (5.75 / 3.80; 1.74) | 0.032 (0.028 / 0.056; 0.005) (1) |
| 0.1 | 200 | 5 | 13.72 (14.01 / 10.08; 4.23) | 10.46 (10.71 / 7.37; 3.71) | 6.19 (6.33 / 4.45; 2.25) | not measured |
| 0.1 | 300 | 5 | 13.52 (13.78 / 9.94; 4.18) | 10.61 (10.86 / 6.86; 3.78) | 6.96 (7.13 / 4.38; 2.62) | not measured |
| 0.15 | 50 | 5 | 17.66 (17.99 / 14.74; 6.43) | 12.43 (12.72 / 9.81; 4.94) | 5.68 (5.72 / 5.54; 1.72) | 0.034 (0.030 / 0.056; 0.005) (1) |
| 0.15 | 100 | 5 | 19.88 (20.51 / 14.18; 6.47) | 14.91 (15.40 / 10.38; 5.42) | 7.64 (7.88 / 5.53; 2.29) | 0.076 (0.071 / 0.097; 0.007) (1) |
| 0.15 | 200 | 5 | 18.28 (18.72 / 14.53; 6.19) | 14.83 (15.25 / 10.92; 5.50) | 8.29 (8.52 / 6.10; 3.08) | not measured |
| 0.15 | 300 | 5 | 17.80 (18.03 / 14.55; 6.04) | 14.41 (14.64 / 10.84; 5.51) | 8.56 (8.72 / 5.93; 3.50) | not measured |
| 0.2 | 50 | 5 | 22.18 (22.47 / 19.95; 8.77) | 16.62 (16.81 / 15.15; 6.81) | 6.69 (6.65 / 7.54; 1.94) | 0.084 (0.058 / 0.197; 0.007) (1) |
| 0.2 | 100 | 5 | 23.99 (24.47 / 20.43; 8.61) | 19.16 (19.54 / 16.29; 7.30) | 8.27 (8.39 / 7.99; 2.51) | 0.026 (0.021 / 0.099; 0.005) (1) |
| 0.2 | 200 | 3 | 23.65 (23.95 / 20.27; 8.27) | 20.03 (20.39 / 15.49; 7.41) | 10.13 (10.30 / 7.83; 3.75) | not measured |
| 0.2 | 300 | 2 | 21.17 (21.39 / 19.02; 7.95) | 17.94 (18.18 / 14.89; 7.30) | 9.68 (9.82 / 7.70; 4.31) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |

#### Dynamics: pair of prolateSpheroid, oblateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 110.9, 252 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.48 | 0.564 | 2.61 |
| + two-body | 1500 | 0.02 | 0.023 | 0.10 |
| + many-body | 1500 | 0.02 | 0.023 | 0.10 |
| MFS Xfine (the truth's own error) | 1500 | 0.002 | 0.0031 | 0.027 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolateSpheroid, oblateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: ring of prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 152 steps, fell 18.2, 138 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 87 | 4.14 | 0.905 | 5.57 |
| + two-body | 147 | 0.68 | 0.359 | 4.66 |
| + many-body | 147 | 0.12 | 0.172 | 3.14 |
| MFS Xfine (the truth's own error) | 152 | 0.004 | 0.0029 | 0.202 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |

#### Structural checks, 16 particles of prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.2e-16 | 1.1157 | 8.9e-16 | 9.69 |
| + two-body | 9.0e-17 | 0.8173 | 8.4e-16 | 5.58 |
| + many-body | 9.8e-17 | 0.9286 | 8.2e-16 | 2.86 |
| MFS fine (the truth) | 3.1e-04 | 1 | | 0 |
| MFS Xfine | 2.9e-05 | 0.9996 | | 0.020 (= the error of the fine truth) |

MFS smallest eigenvalue 1.6464e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configuration**: ONE random suspension, N = 16, shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |

#### Positive definiteness of the operator, prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75

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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -8.045 | 0.82 | oblateSpheroid, oblate_ar3 | 2.43 | 1.125 | 2.22e-03 / 9.27e-04 (0.418) | 0.358, 0.441 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 17 | -4.718 | 0.07 | oblate_ar3, oblateSpheroid_x1p5 | 6.17 | 1.981 | 2.07e-03 / 2.07e-03 (0.997) | 0.807, 0.623 (7 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

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

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.46 (7.68 / 5.52) | 4.45 (4.62 / 2.81) | 2.85 (2.95 / 1.98) | 2.11 (2.20 / 1.18) | 2.04 (2.14 / 1.08) |
| 0.1 | 64 | 3 | 12.66 (12.88 / 10.49) | 8.57 (8.75 / 6.77) | 4.64 (4.70 / 4.08) | 3.17 (3.27 / 2.03) | 3.01 (3.11 / 1.80) |
| 0.2 | 64 | 3 | 20.39 (20.43 / 20.05) | 15.67 (15.71 / 15.15) | 5.93 (5.87 / 6.94) | 3.87 (3.90 / 3.43) | 3.48 (3.52 / 2.50) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configurations**: N in [64], shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |

### Case 3A (cells 3A and 4A): triaxial form, one shape: 1:2:3

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 160 / 136; 1.0202 / 0.6747 | 340 / 290; 0.0860 / 0.1317 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Two-body accuracy of `data/final_c/models/pair_t123.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.064 | 0.293 | 0.074 | 0.80 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.070 / 0.442 | 0.040 / 0.283 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.101 / 0.408 (666) | 0.048 / 0.215 (868) | 0.033 / 0.158 (688) | 0.030 / 0.146 (672) | 0.036 / 0.151 (1150) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Two-body accuracy of `data/final_c/models/pair_t123_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.065 | 0.292 | 0.076 | 0.80 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.067 / 0.462 | 0.040 / 0.283 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.103 / 0.408 (666) | 0.049 / 0.209 (868) | 0.033 / 0.162 (688) | 0.031 / 0.146 (672) | 0.036 / 0.157 (1150) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123_s1.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 1: triaxial_123__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Two-body accuracy of `data/final_c/models/pair_t123_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.064 | 0.289 | 0.074 | 0.80 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.070 / 0.453 | 0.040 / 0.283 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.102 / 0.403 (666) | 0.047 / 0.208 (868) | 0.032 / 0.157 (688) | 0.030 / 0.144 (672) | 0.034 / 0.149 (1150) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123_s2.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 2: triaxial_123__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Suspensions of triaxial_123: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.17 (4.13 / 6.00; 1.18) | 2.76 (2.74 / 3.73; 0.99) | 1.80 (1.79 / 2.34; 0.72) | 0.019 (0.017 / 0.066; 0.001) (1) |
| 0.05 | 200 | 10 | 7.10 (7.05 / 10.32; 2.18) | 5.27 (5.24 / 7.10; 1.90) | 3.04 (3.02 / 4.17; 1.17) | 0.026 (0.021 / 0.112; 0.002) (1) |
| 0.075 | 200 | 10 | 11.46 (11.41 / 14.76; 3.20) | 8.84 (8.80 / 11.25; 2.83) | 4.41 (4.39 / 5.59; 1.50) | 0.050 (0.040 / 0.174; 0.003) (1) |
| 0.1 | 200 | 10 | 14.34 (14.26 / 19.33; 4.16) | 11.69 (11.63 / 15.91; 3.71) | 5.58 (5.55 / 7.30; 1.77) | 0.036 (0.033 / 0.130; 0.003) (1) |
| 0.15 | 200 | 10 | 18.49 (18.36 / 29.27; 5.94) | 15.36 (15.23 / 24.85; 5.35) | 6.40 (6.36 / 9.95; 2.13) | 0.051 (0.041 / 0.332; 0.005) (1) |
| 0.2 | 200 | 10 | 26.45 (26.26 / 39.97; 7.71) | 23.00 (22.84 / 34.70; 6.97) | 8.64 (8.58 / 13.01; 2.53) | 0.093 (0.080 / 0.393; 0.006) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Configurations**: N in [200] particles, shapes triaxial_123 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Suspensions of triaxial_123: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.28 (7.23 / 9.70; 2.35) | 4.64 (4.60 / 6.29; 1.75) | 2.18 (2.15 / 3.36; 0.77) | 0.027 (0.025 / 0.064; 0.002) (1) |
| 0.05 | 100 | 5 | 6.54 (6.48 / 9.85; 2.38) | 4.52 (4.48 / 6.80; 1.93) | 2.34 (2.32 / 3.56; 0.94) | 0.026 (0.024 / 0.112; 0.002) (1) |
| 0.05 | 200 | 5 | 6.73 (6.68 / 10.08; 2.18) | 5.05 (5.02 / 7.01; 1.91) | 2.90 (2.89 / 4.14; 1.18) | not measured |
| 0.05 | 300 | 5 | 7.09 (7.04 / 10.06; 2.17) | 5.43 (5.40 / 7.33; 1.96) | 3.29 (3.27 / 4.39; 1.37) | not measured |
| 0.1 | 50 | 5 | 12.27 (12.15 / 18.29; 4.42) | 8.91 (8.81 / 13.96; 3.41) | 2.94 (2.87 / 5.93; 1.36) | 0.031 (0.027 / 0.134; 0.004) (1) |
| 0.1 | 100 | 5 | 13.12 (13.02 / 18.29; 4.22) | 10.24 (10.15 / 14.68; 3.54) | 4.30 (4.24 / 7.01; 1.30) | 0.050 (0.040 / 0.238; 0.003) (1) |
| 0.1 | 200 | 5 | 12.81 (12.73 / 18.45; 4.06) | 10.49 (10.42 / 15.20; 3.62) | 5.08 (5.06 / 7.06; 1.73) | not measured |
| 0.1 | 300 | 5 | 11.26 (11.17 / 19.21; 4.01) | 9.38 (9.31 / 15.82; 3.67) | 4.82 (4.79 / 7.80; 2.10) | not measured |
| 0.15 | 50 | 5 | 15.15 (14.91 / 27.20; 5.82) | 11.96 (11.75 / 21.85; 4.56) | 3.86 (3.74 / 8.51; 1.61) | 0.047 (0.039 / 0.204; 0.005) (1) |
| 0.15 | 100 | 5 | 18.74 (18.57 / 28.19; 6.23) | 15.02 (14.86 / 23.67; 5.31) | 4.92 (4.83 / 9.01; 1.56) | 0.065 (0.058 / 0.232; 0.006) (1) |
| 0.15 | 200 | 5 | 19.15 (19.02 / 29.64; 5.98) | 15.78 (15.66 / 24.97; 5.38) | 6.61 (6.57 / 10.22; 2.16) | not measured |
| 0.15 | 300 | 5 | 17.04 (16.90 / 29.29; 5.94) | 14.62 (14.50 / 25.15; 5.47) | 6.63 (6.59 / 10.51; 2.71) | not measured |
| 0.2 | 50 | 5 | 23.43 (23.13 / 39.41; 7.91) | 18.68 (18.40 / 32.91; 6.31) | 4.90 (4.73 / 11.51; 1.48) | 0.040 (0.031 / 0.363; 0.012) (1) |
| 0.2 | 100 | 5 | 25.51 (25.28 / 37.89; 7.69) | 21.23 (21.00 / 33.11; 6.59) | 6.91 (6.81 / 11.69; 1.84) | 0.070 (0.064 / 0.191; 0.004) (1) |
| 0.2 | 200 | 5 | 29.95 (29.80 / 40.55; 7.67) | 25.88 (25.74 / 35.52; 6.93) | 9.48 (9.43 / 13.09; 2.51) | not measured |
| 0.2 | 300 | 5 | 24.75 (24.55 / 40.40; 7.70) | 21.81 (21.64 / 35.55; 7.13) | 9.40 (9.36 / 13.57; 3.31) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_123 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Dynamics: pair of triaxial_123, triaxial_123 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 81.1, 242 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.03 | 0.034 | 0.26 |
| + two-body | 1500 | 0.02 | 0.029 | 0.35 |
| + many-body | 1500 | 0.02 | 0.029 | 0.35 |
| MFS Xfine (the truth's own error) | 1500 | 0.013 | 0.0119 | 0.285 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: triaxial_123, triaxial_123.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Dynamics: ring of triaxial_123, triaxial_123, triaxial_123, triaxial_123, triaxial_123 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 356 steps, fell 45.8, 274 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 99 | 6.14 | 1.043 | 18.67 |
| + two-body | 124 | 2.41 | 0.690 | 13.76 |
| + many-body | 160 | 0.38 | 0.232 | 4.73 |
| MFS Xfine (the truth's own error) | 356 | 0.014 | 0.0115 | 0.240 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: triaxial_123, triaxial_123, triaxial_123, triaxial_123, triaxial_123.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Structural checks, 16 particles of triaxial_123 at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.4e-16 | 1.2238 | 8.1e-16 | 7.94 |
| + two-body | 8.4e-17 | 0.7020 | 6.3e-16 | 4.84 |
| + many-body | 8.9e-17 | 0.9775 | 6.4e-16 | 1.61 |
| MFS fine (the truth) | 1.9e-04 | 1 | | 0 |
| MFS Xfine | 6.5e-05 | 1.0008 | | 0.014 (= the error of the fine truth) |

MFS smallest eigenvalue 2.3143e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Configuration**: ONE random suspension, N = 16, shapes triaxial_123 in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Positive definiteness of the operator, triaxial_123

Per (phi, N): how many random suspensions give a positive definite grand mobility matrix, and its smallest eigenvalue relative to the far-field operator's on the same configuration (smallest / median over the configurations).  A negative number = not positive definite.

| phi | N | n | far field: positive definite; smallest eigenvalue ratio min / median | + two-body: positive definite; smallest eigenvalue ratio min / median | + many-body: positive definite; smallest eigenvalue ratio min / median |
|---|---|---|---|---|---|
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 18 of 20; -0.657 / 0.553 | 20 of 20; 0.208 / 0.693 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -1.085 / 0.156 | 19 of 20; -0.004 / 0.514 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 3 of 20; -1.063 / -0.126 | 19 of 20; -0.023 / 0.412 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -0.859 / -0.266 | 20 of 20; 0.291 / 0.507 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 1 of 20; -2.099 / -1.192 | 18 of 20; -0.092 / 0.223 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.093 / -1.464 | 11 of 20; -0.144 / 0.005 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.000 / -1.354 | 19 of 20; -0.082 / 0.321 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.360 / -2.403 | 16 of 20; -0.199 / 0.113 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.165 / -2.791 | 0 of 20; -2.543 / -1.975 |
| 0.2 | 16 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -3.506 / -2.626 | 12 of 19; -0.147 / 0.064 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.169 / -3.444 | 4 of 20; -0.592 / -0.107 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.345 / -4.465 | 0 of 20; -4.044 / -3.344 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 12 | -5.345 | 0.66 | triaxial_123, triaxial_123 | 3.06 | 1.121 | 3.02e-03 / 1.79e-03 (0.592) | 0.409, 0.569 (10 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 17 | -4.044 | 0.05 | triaxial_123, triaxial_123 | 12.61 | inf | 3.78e-03 / 3.78e-03 (1.000) | 0.760, 0.831 (5 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.958 / 1.000 | 1.063, 3.06 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_123

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.14 (7.10 / 10.29) | 5.04 (5.02 / 6.55) | 2.23 (2.21 / 3.48) | 1.72 (1.72 / 1.92) | 1.66 (1.66 / 1.84) |
| 0.1 | 64 | 3 | 10.74 (10.61 / 20.10) | 7.98 (7.84 / 16.87) | 3.00 (2.92 / 7.21) | 2.34 (2.32 / 3.37) | 2.21 (2.20 / 2.85) |
| 0.2 | 64 | 3 | 23.64 (23.36 / 37.66) | 18.73 (18.44 / 32.12) | 5.35 (5.22 / 10.67) | 4.49 (4.45 / 6.30) | 3.74 (3.74 / 3.70) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Configurations**: N in [64], shapes triaxial_123 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

### Case 3B (cells 3B and 4B): triaxial form, many shapes (6 triaxial), one shape per pair / cluster

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 160 / 136; 1.0202 / 0.6747 | 340 / 290; 0.0860 / 0.1317 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 160 / 136; 0.1260 / 0.1371 | 340 / 290; 0.0028 / 0.0029 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 160 / 136; 0.9743 / 0.9167 | 340 / 290; 0.0749 / 0.0953 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 208 / 177; 0.4098 / 0.8140 | 441 / 376; 0.1718 / 0.0670 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 256 / 218; 0.8042 / 0.8770 | 544 / 464; 0.0609 / 0.2178 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 290 / 246; 0.6170 / 0.5146 | 616 / 525; 0.2287 / 0.2159 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 220 / 187; 0.9932 / 1.1209 | 467 / 399; 0.1688 / 0.2584 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 424 / 360; 0.6915 / 1.0622 | 901 / 768; 0.1195 / 0.5111 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Two-body accuracy of `data/final_c/models/pair_multi.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.077 | 0.350 | 0.089 | 1.00 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.076 / 0.490 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.069 | 0.378 | 0.092 | 0.72 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.070 / 0.348 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.117 | 0.585 | 0.143 | 1.35 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.131 / 0.670 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.146 | 0.818 | 0.172 | 2.09 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.155 / 0.720 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.234 | 1.345 | 0.262 | 3.27 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.235 / 1.377 | 0.052 / 0.391 | 0.1 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.152 | 0.785 | 0.167 | 2.51 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.128 / 0.607 | 0.046 / 0.249 | 0.0 % |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 4018 | 0.169 | 0.865 | 0.195 | 2.14 | 4.02 / 11.68 | 0.047 / 0.261 (498) | 0.152 / 0.745 | 0.044 / 0.294 | 0.0 % |
| triaxial_3_6__triaxial_3_6_test | 4026 | 1.726 | 15.191 | 2.107 | 15.46 | 3.73 / 13.74 | 0.039 / 0.209 (508) | 1.682 / 14.976 | 0.026 / 0.190 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.117 / 0.461 (666) | 0.061 / 0.278 (868) | 0.043 / 0.231 (688) | 0.043 / 0.227 (672) | 0.051 / 0.249 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.094 / 0.432 (642) | 0.066 / 0.372 (962) | 0.046 / 0.308 (710) | 0.041 / 0.246 (674) | 0.040 / 0.239 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.166 / 0.698 (756) | 0.097 / 0.515 (852) | 0.078 / 0.457 (622) | 0.065 / 0.422 (728) | 0.075 / 0.432 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.207 / 1.125 (706) | 0.123 / 0.624 (872) | 0.098 / 0.486 (730) | 0.094 / 0.499 (648) | 0.109 / 0.560 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.326 / 1.737 (704) | 0.206 / 1.220 (898) | 0.159 / 0.840 (634) | 0.146 / 0.780 (676) | 0.165 / 0.915 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.223 / 1.082 (686) | 0.125 / 0.599 (866) | 0.098 / 0.501 (686) | 0.089 / 0.453 (724) | 0.107 / 0.463 (1058) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.215 / 1.088 (716) | 0.166 / 0.768 (868) | 0.132 / 0.595 (664) | 0.122 / 0.523 (672) | 0.098 / 0.472 (1098) | - |
| triaxial_3_6__triaxial_3_6_test | 2.023 / 17.733 (732) | 1.783 / 15.655 (886) | 1.601 / 12.172 (646) | 1.379 / 10.344 (744) | 0.960 / 7.347 (1018) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.032 / 0.127 (70) | 0.004 / 0.014 (140) | 0.001 / 0.004 (90) | 0.001 / 0.002 (76) | 0.000 / 0.002 (126) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.667 (102) | 0.035 / 0.162 (100) | 0.011 / 0.039 (64) | 0.006 / 0.025 (98) | 0.004 / 0.016 (142) | - |
| triaxial_2_4__triaxial_2_4_test | 0.172 / 0.596 (74) | 0.039 / 0.291 (94) | 0.015 / 0.091 (92) | 0.008 / 0.038 (78) | 0.005 / 0.025 (168) | - |
| triaxial_2_5__triaxial_2_5_test | 0.120 / 0.507 (118) | 0.039 / 0.239 (90) | 0.018 / 0.098 (66) | 0.015 / 0.075 (104) | 0.009 / 0.052 (128) | - |
| triaxial_3_4__triaxial_3_4_test | 0.096 / 0.399 (102) | 0.050 / 0.255 (94) | 0.029 / 0.120 (64) | 0.015 / 0.071 (104) | 0.009 / 0.046 (140) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.084 / 0.398 (72) | 0.038 / 0.197 (136) | 0.019 / 0.124 (70) | 0.013 / 0.112 (86) | 0.010 / 0.077 (134) | - |
| triaxial_3_6__triaxial_3_6_test | 0.065 / 0.318 (80) | 0.031 / 0.159 (122) | 0.019 / 0.086 (84) | 0.016 / 0.096 (108) | 0.013 / 0.067 (114) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2p5_3p5__triaxial_2p5_3p5_test`: triaxial_2p5_3p5 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_6__triaxial_3_6_test`: triaxial_3_6 (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Two-body accuracy of `data/final_c/models/pair_multi_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.076 | 0.353 | 0.089 | 1.02 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.075 / 0.480 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.068 | 0.366 | 0.090 | 0.73 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.070 / 0.340 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.112 | 0.588 | 0.139 | 1.35 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.122 / 0.630 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.136 | 0.803 | 0.164 | 2.03 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.129 / 0.680 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.219 | 1.370 | 0.253 | 3.19 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.232 / 1.328 | 0.052 / 0.391 | 0.1 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.152 | 0.777 | 0.166 | 2.54 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.127 / 0.600 | 0.046 / 0.249 | 0.0 % |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 4018 | 0.212 | 0.831 | 0.232 | 1.87 | 4.02 / 11.68 | 0.047 / 0.261 (498) | 0.198 / 0.709 | 0.044 / 0.294 | 0.0 % |
| triaxial_3_6__triaxial_3_6_test | 4026 | 2.402 | 10.779 | 2.569 | 13.19 | 3.73 / 13.74 | 0.039 / 0.209 (508) | 2.436 / 10.458 | 0.026 / 0.190 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.115 / 0.467 (666) | 0.060 / 0.275 (868) | 0.046 / 0.235 (688) | 0.044 / 0.230 (672) | 0.049 / 0.242 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.094 / 0.419 (642) | 0.064 / 0.359 (962) | 0.047 / 0.302 (710) | 0.040 / 0.242 (674) | 0.042 / 0.243 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.702 (756) | 0.092 / 0.514 (852) | 0.077 / 0.453 (622) | 0.072 / 0.438 (728) | 0.074 / 0.448 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.193 / 1.101 (706) | 0.119 / 0.613 (872) | 0.093 / 0.478 (730) | 0.086 / 0.508 (648) | 0.095 / 0.566 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.299 / 1.785 (704) | 0.204 / 1.222 (898) | 0.151 / 0.848 (634) | 0.142 / 0.789 (676) | 0.147 / 0.918 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.222 / 1.056 (686) | 0.125 / 0.611 (866) | 0.098 / 0.513 (686) | 0.098 / 0.470 (724) | 0.101 / 0.470 (1058) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.254 / 1.025 (716) | 0.217 / 0.758 (868) | 0.188 / 0.589 (664) | 0.162 / 0.526 (672) | 0.114 / 0.503 (1098) | - |
| triaxial_3_6__triaxial_3_6_test | 2.618 / 12.968 (732) | 2.558 / 10.552 (886) | 2.380 / 8.505 (646) | 2.067 / 7.770 (744) | 1.356 / 6.378 (1018) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.032 / 0.127 (70) | 0.004 / 0.014 (140) | 0.001 / 0.004 (90) | 0.001 / 0.002 (76) | 0.000 / 0.002 (126) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.667 (102) | 0.035 / 0.162 (100) | 0.011 / 0.039 (64) | 0.006 / 0.025 (98) | 0.004 / 0.016 (142) | - |
| triaxial_2_4__triaxial_2_4_test | 0.172 / 0.596 (74) | 0.039 / 0.291 (94) | 0.015 / 0.091 (92) | 0.008 / 0.038 (78) | 0.005 / 0.025 (168) | - |
| triaxial_2_5__triaxial_2_5_test | 0.120 / 0.507 (118) | 0.039 / 0.239 (90) | 0.018 / 0.098 (66) | 0.015 / 0.075 (104) | 0.009 / 0.052 (128) | - |
| triaxial_3_4__triaxial_3_4_test | 0.096 / 0.399 (102) | 0.050 / 0.255 (94) | 0.029 / 0.120 (64) | 0.015 / 0.071 (104) | 0.009 / 0.046 (140) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.084 / 0.398 (72) | 0.038 / 0.197 (136) | 0.019 / 0.124 (70) | 0.013 / 0.112 (86) | 0.010 / 0.077 (134) | - |
| triaxial_3_6__triaxial_3_6_test | 0.065 / 0.318 (80) | 0.031 / 0.159 (122) | 0.019 / 0.086 (84) | 0.016 / 0.096 (108) | 0.013 / 0.067 (114) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi_s1.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 1: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2p5_3p5__triaxial_2p5_3p5_test`: triaxial_2p5_3p5 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_6__triaxial_3_6_test`: triaxial_3_6 (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Two-body accuracy of `data/final_c/models/pair_multi_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.075 | 0.347 | 0.088 | 1.02 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.077 / 0.488 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.067 | 0.361 | 0.089 | 0.72 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.068 / 0.334 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.114 | 0.590 | 0.139 | 1.37 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.121 / 0.669 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.143 | 0.798 | 0.168 | 2.04 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.146 / 0.668 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.223 | 1.359 | 0.255 | 3.20 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.211 / 1.374 | 0.052 / 0.391 | 0.1 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.144 | 0.770 | 0.163 | 2.51 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.128 / 0.600 | 0.046 / 0.249 | 0.0 % |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 4018 | 0.164 | 0.825 | 0.189 | 1.96 | 4.02 / 11.68 | 0.047 / 0.261 (498) | 0.143 / 0.671 | 0.044 / 0.294 | 0.0 % |
| triaxial_3_6__triaxial_3_6_test | 4026 | 1.542 | 10.608 | 1.762 | 14.72 | 3.73 / 13.74 | 0.039 / 0.209 (508) | 1.486 / 10.384 | 0.026 / 0.190 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.115 / 0.463 (666) | 0.058 / 0.267 (868) | 0.043 / 0.227 (688) | 0.045 / 0.219 (672) | 0.049 / 0.256 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.092 / 0.406 (642) | 0.063 / 0.359 (962) | 0.047 / 0.301 (710) | 0.040 / 0.240 (674) | 0.040 / 0.249 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.161 / 0.709 (756) | 0.093 / 0.520 (852) | 0.072 / 0.441 (622) | 0.070 / 0.414 (728) | 0.074 / 0.444 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.207 / 1.090 (706) | 0.118 / 0.616 (872) | 0.098 / 0.483 (730) | 0.088 / 0.490 (648) | 0.095 / 0.574 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.309 / 1.738 (704) | 0.197 / 1.243 (898) | 0.153 / 0.894 (634) | 0.150 / 0.799 (676) | 0.156 / 0.908 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.208 / 1.053 (686) | 0.121 / 0.603 (866) | 0.096 / 0.488 (686) | 0.093 / 0.453 (724) | 0.096 / 0.469 (1058) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.203 / 1.019 (716) | 0.158 / 0.751 (868) | 0.134 / 0.573 (664) | 0.133 / 0.543 (672) | 0.119 / 0.521 (1098) | - |
| triaxial_3_6__triaxial_3_6_test | 1.866 / 12.578 (732) | 1.504 / 10.540 (886) | 1.356 / 8.442 (646) | 1.308 / 7.709 (744) | 1.023 / 6.591 (1018) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.032 / 0.127 (70) | 0.004 / 0.014 (140) | 0.001 / 0.004 (90) | 0.001 / 0.002 (76) | 0.000 / 0.002 (126) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.667 (102) | 0.035 / 0.162 (100) | 0.011 / 0.039 (64) | 0.006 / 0.025 (98) | 0.004 / 0.016 (142) | - |
| triaxial_2_4__triaxial_2_4_test | 0.172 / 0.596 (74) | 0.039 / 0.291 (94) | 0.015 / 0.091 (92) | 0.008 / 0.038 (78) | 0.005 / 0.025 (168) | - |
| triaxial_2_5__triaxial_2_5_test | 0.120 / 0.507 (118) | 0.039 / 0.239 (90) | 0.018 / 0.098 (66) | 0.015 / 0.075 (104) | 0.009 / 0.052 (128) | - |
| triaxial_3_4__triaxial_3_4_test | 0.096 / 0.399 (102) | 0.050 / 0.255 (94) | 0.029 / 0.120 (64) | 0.015 / 0.071 (104) | 0.009 / 0.046 (140) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.084 / 0.398 (72) | 0.038 / 0.197 (136) | 0.019 / 0.124 (70) | 0.013 / 0.112 (86) | 0.010 / 0.077 (134) | - |
| triaxial_3_6__triaxial_3_6_test | 0.065 / 0.318 (80) | 0.031 / 0.159 (122) | 0.019 / 0.086 (84) | 0.016 / 0.096 (108) | 0.013 / 0.067 (114) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi_s2.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 2: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2p5_3p5__triaxial_2p5_3p5_test`: triaxial_2p5_3p5 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_6__triaxial_3_6_test`: triaxial_3_6 (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Suspensions of triaxial_2_4: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.26 (4.23 / 6.75; 1.23) | 2.82 (2.80 / 3.94; 1.05) | 2.02 (2.01 / 2.87; 0.81) | 0.030 (0.027 / 0.110; 0.002) (1) |
| 0.05 | 200 | 10 | 7.39 (7.35 / 11.21; 2.21) | 5.58 (5.56 / 8.22; 1.93) | 3.51 (3.49 / 5.13; 1.31) | 0.022 (0.017 / 0.154; 0.002) (1) |
| 0.075 | 200 | 10 | 10.27 (10.21 / 16.24; 3.37) | 8.10 (8.05 / 12.82; 3.00) | 4.74 (4.71 / 7.35; 1.79) | 0.042 (0.038 / 0.169; 0.003) (1) |
| 0.1 | 200 | 10 | 15.01 (14.94 / 20.82; 4.30) | 12.22 (12.16 / 17.44; 3.85) | 6.38 (6.35 / 8.92; 2.10) | 0.063 (0.058 / 0.283; 0.004) (1) |
| 0.15 | 200 | 10 | 20.54 (20.40 / 31.24; 6.03) | 17.13 (17.01 / 26.99; 5.43) | 8.20 (8.15 / 12.15; 2.58) | 0.068 (0.062 / 0.283; 0.005) (1) |
| 0.2 | 200 | 10 | 23.62 (23.47 / 43.11; 7.82) | 20.44 (20.30 / 38.43; 7.07) | 9.24 (9.18 / 16.63; 3.13) | 0.101 (0.091 / 0.426; 0.008) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Configurations**: N in [200] particles, shapes triaxial_2_4 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

#### Suspensions of triaxial_2_4: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.70 (7.65 / 10.07; 2.54) | 5.01 (4.96 / 7.43; 1.87) | 2.37 (2.33 / 4.26; 0.86) | 0.024 (0.021 / 0.086; 0.003) (1) |
| 0.05 | 100 | 5 | 6.64 (6.59 / 11.40; 2.43) | 4.83 (4.79 / 8.01; 1.96) | 2.82 (2.80 / 5.07; 1.03) | 0.023 (0.020 / 0.142; 0.003) (1) |
| 0.05 | 200 | 5 | 7.03 (7.00 / 10.91; 2.22) | 5.34 (5.32 / 8.03; 1.95) | 3.48 (3.47 / 5.05; 1.34) | not measured |
| 0.05 | 300 | 5 | 8.11 (8.08 / 11.58; 2.27) | 6.39 (6.36 / 8.64; 2.05) | 4.36 (4.35 / 5.53; 1.52) | not measured |
| 0.1 | 50 | 5 | 9.41 (9.29 / 19.10; 4.70) | 7.02 (6.92 / 15.20; 3.62) | 2.92 (2.85 / 7.55; 1.26) | 0.027 (0.024 / 0.143; 0.006) (1) |
| 0.1 | 100 | 5 | 12.62 (12.52 / 19.92; 4.42) | 9.76 (9.67 / 16.21; 3.74) | 4.64 (4.59 / 8.23; 1.67) | 0.021 (0.018 / 0.127; 0.003) (1) |
| 0.1 | 200 | 5 | 14.68 (14.61 / 20.70; 4.29) | 11.98 (11.91 / 17.43; 3.83) | 6.23 (6.19 / 9.16; 2.06) | not measured |
| 0.1 | 300 | 5 | 12.91 (12.84 / 21.12; 4.18) | 10.73 (10.66 / 17.93; 3.82) | 6.37 (6.35 / 9.59; 2.38) | not measured |
| 0.15 | 50 | 5 | 15.97 (15.80 / 29.98; 6.19) | 12.46 (12.31 / 24.55; 4.89) | 4.46 (4.38 / 10.28; 1.53) | 0.055 (0.051 / 0.233; 0.014) (1) |
| 0.15 | 100 | 5 | 21.12 (20.99 / 32.08; 6.33) | 17.17 (17.04 / 27.56; 5.39) | 7.07 (7.01 / 12.07; 1.87) | 0.056 (0.051 / 0.307; 0.006) (1) |
| 0.15 | 200 | 5 | 20.67 (20.54 / 31.47; 5.92) | 17.47 (17.35 / 27.16; 5.33) | 8.65 (8.60 / 12.52; 2.56) | not measured |
| 0.15 | 300 | 5 | 20.00 (19.89 / 32.46; 6.20) | 17.27 (17.16 / 28.60; 5.72) | 9.14 (9.11 / 13.57; 3.14) | not measured |
| 0.2 | 50 | 5 | 22.32 (22.02 / 39.78; 7.74) | 17.92 (17.65 / 33.76; 6.18) | 5.90 (5.75 / 13.30; 1.80) | 0.102 (0.091 / 0.373; 0.013) (1) |
| 0.2 | 100 | 5 | 22.81 (22.57 / 41.98; 7.72) | 19.17 (18.98 / 35.43; 6.63) | 7.49 (7.41 / 14.09; 2.26) | 0.077 (0.064 / 0.373; 0.007) (1) |
| 0.2 | 200 | 5 | 22.68 (22.50 / 43.29; 7.79) | 19.48 (19.30 / 38.89; 7.05) | 8.88 (8.82 / 16.83; 3.13) | not measured |
| 0.2 | 300 | 5 | 25.40 (25.26 / 44.42; 7.88) | 22.66 (22.53 / 40.01; 7.28) | 11.35 (11.31 / 17.81; 3.76) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_2_4 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

#### Dynamics: pair of triaxial_2_4, triaxial_2_4 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 69.2, 380 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.01 | 0.012 | 0.07 |
| + two-body | 1500 | 0.03 | 0.038 | 0.26 |
| + many-body | 1500 | 0.03 | 0.038 | 0.26 |
| MFS Xfine (the truth's own error) | 1500 | 0.007 | 0.0139 | 0.147 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: triaxial_2_4, triaxial_2_4.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

#### Dynamics: ring of triaxial_2_4, triaxial_2_4, triaxial_2_4, triaxial_2_4, triaxial_2_4 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 449 steps, fell 51.4, 651 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 119 | 6.59 | 1.208 | 22.08 |
| + two-body | 152 | 2.60 | 0.819 | 15.81 |
| + many-body | 172 | 1.39 | 0.426 | 3.54 |
| MFS Xfine (the truth's own error) | 449 | 0.007 | 0.0063 | 0.358 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: triaxial_2_4, triaxial_2_4, triaxial_2_4, triaxial_2_4, triaxial_2_4.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

#### Structural checks, 16 particles of triaxial_2_4 at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.3e-16 | 1.2682 | 5.3e-16 | 7.95 |
| + two-body | 8.2e-17 | 0.3494 | 4.0e-16 | 5.08 |
| + many-body | 8.9e-17 | 0.9361 | 4.1e-16 | 1.93 |
| MFS fine (the truth) | 2.6e-04 | 1 | | 0 |
| MFS Xfine | 6.1e-05 | 0.9981 | | 0.021 (= the error of the fine truth) |

MFS smallest eigenvalue 1.1028e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Configuration**: ONE random suspension, N = 16, shapes triaxial_2_4 in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

#### Positive definiteness of the operator, triaxial_2_4

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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 11 | -13.924 | 0.73 | triaxial_2_4, triaxial_2_4 | 2.69 | 1.051 | 1.60e-03 / 2.52e-04 (0.157) | 0.433, 0.453 (3 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 11 | -6.204 | 0.05 | triaxial_2_4, triaxial_2_4 | 19.11 | inf | 2.10e-03 / 2.10e-03 (1.000) | 0.807, 0.652 (4 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

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

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_2_4 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_2_4

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 6.41 (6.36 / 10.70) | 4.41 (4.35 / 8.23) | 2.34 (2.31 / 4.78) | 1.97 (1.96 / 3.05) | 1.93 (1.92 / 3.02) |
| 0.1 | 64 | 3 | 13.20 (13.06 / 21.56) | 10.01 (9.91 / 15.87) | 4.19 (4.12 / 7.82) | 3.39 (3.38 / 4.43) | 3.25 (3.24 / 3.75) |
| 0.2 | 64 | 2 | 33.16 (32.93 / 45.73) | 26.63 (26.38 / 39.15) | 9.27 (9.13 / 15.52) | 7.19 (7.19 / 7.87) | 6.52 (6.55 / 5.32) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Configurations**: N in [64], shapes triaxial_2_4 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

### Case 3C (cells 3C and 4C): triaxial form, 1:2:3 + prolate + oblate mixed

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 160 / 136; 1.0202 / 0.6747 | 340 / 290; 0.0860 / 0.1317 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 150 / 131; 0.0325 / 0.1955 | 348 / 304; 0.0230 / 0.0079 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 174 / 152; 2.8747 / 0.1707 | 334 / 292; 0.0385 / 0.0193 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_mixed.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.090 | 0.397 | 0.104 | 1.17 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.085 / 0.530 | 0.040 / 0.283 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.121 | 0.824 | 0.178 | 1.25 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.125 / 0.900 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.099 | 0.653 | 0.139 | 0.88 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.088 / 0.563 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.124 | 0.644 | 0.157 | 1.41 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.131 / 0.905 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.096 | 0.471 | 0.115 | 1.07 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.083 / 0.443 | 0.042 / 0.294 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.110 | 0.700 | 0.154 | 0.96 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.090 / 0.629 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.132 / 0.512 (666) | 0.074 / 0.321 (868) | 0.057 / 0.276 (688) | 0.057 / 0.284 (672) | 0.063 / 0.306 (1150) | - |
| prolateSpheroid__prolateSpheroid_test | 0.162 / 0.983 (684) | 0.109 / 0.754 (898) | 0.094 / 0.686 (660) | 0.087 / 0.608 (754) | 0.090 / 0.705 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.132 / 0.803 (650) | 0.104 / 0.612 (936) | 0.063 / 0.472 (680) | 0.044 / 0.384 (738) | 0.036 / 0.343 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.176 / 0.803 (668) | 0.109 / 0.562 (876) | 0.081 / 0.452 (668) | 0.075 / 0.463 (738) | 0.085 / 0.523 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.145 / 0.603 (686) | 0.074 / 0.406 (916) | 0.060 / 0.315 (684) | 0.052 / 0.281 (688) | 0.057 / 0.295 (1058) | - |
| prolateSpheroid__oblateSpheroid_test | 0.141 / 0.760 (702) | 0.109 / 0.707 (952) | 0.086 / 0.607 (668) | 0.065 / 0.542 (632) | 0.057 / 0.470 (1086) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_mixed_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.090 | 0.401 | 0.105 | 1.17 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.094 / 0.516 | 0.040 / 0.283 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.121 | 0.783 | 0.173 | 1.20 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.128 / 0.826 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.097 | 0.628 | 0.133 | 0.84 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.086 / 0.542 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.121 | 0.639 | 0.157 | 1.42 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.130 / 0.904 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.096 | 0.462 | 0.114 | 1.06 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.082 / 0.425 | 0.042 / 0.294 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.109 | 0.698 | 0.152 | 0.99 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.093 / 0.643 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.134 / 0.515 (666) | 0.073 / 0.330 (868) | 0.057 / 0.281 (688) | 0.056 / 0.277 (672) | 0.063 / 0.304 (1150) | - |
| prolateSpheroid__prolateSpheroid_test | 0.155 / 0.925 (684) | 0.113 / 0.713 (898) | 0.098 / 0.659 (660) | 0.093 / 0.619 (754) | 0.097 / 0.719 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.131 / 0.774 (650) | 0.101 / 0.587 (936) | 0.061 / 0.446 (680) | 0.042 / 0.365 (738) | 0.037 / 0.331 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.166 / 0.804 (668) | 0.107 / 0.552 (876) | 0.084 / 0.438 (668) | 0.083 / 0.464 (738) | 0.091 / 0.503 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.142 / 0.587 (686) | 0.077 / 0.399 (916) | 0.059 / 0.321 (684) | 0.059 / 0.294 (688) | 0.063 / 0.296 (1058) | - |
| prolateSpheroid__oblateSpheroid_test | 0.139 / 0.764 (702) | 0.109 / 0.709 (952) | 0.082 / 0.584 (668) | 0.067 / 0.533 (632) | 0.056 / 0.462 (1086) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed_s1.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 1: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Two-body accuracy of `data/final_c/models/pair_mixed_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.087 | 0.408 | 0.103 | 1.18 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.085 / 0.521 | 0.040 / 0.283 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.123 | 0.808 | 0.177 | 1.21 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.133 / 0.859 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.096 | 0.634 | 0.134 | 0.85 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.082 / 0.536 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.120 | 0.630 | 0.155 | 1.39 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.134 / 0.913 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.097 | 0.459 | 0.117 | 1.05 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.083 / 0.427 | 0.042 / 0.294 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.108 | 0.705 | 0.154 | 0.95 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.090 / 0.602 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.125 / 0.531 (666) | 0.074 / 0.331 (868) | 0.057 / 0.278 (688) | 0.058 / 0.266 (672) | 0.065 / 0.309 (1150) | - |
| prolateSpheroid__prolateSpheroid_test | 0.160 / 0.974 (684) | 0.115 / 0.734 (898) | 0.095 / 0.657 (660) | 0.093 / 0.596 (754) | 0.096 / 0.708 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.128 / 0.779 (650) | 0.102 / 0.596 (936) | 0.061 / 0.454 (680) | 0.042 / 0.369 (738) | 0.039 / 0.337 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.165 / 0.794 (668) | 0.105 / 0.536 (876) | 0.084 / 0.441 (668) | 0.080 / 0.459 (738) | 0.096 / 0.524 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.146 / 0.580 (686) | 0.076 / 0.401 (916) | 0.059 / 0.320 (684) | 0.056 / 0.299 (688) | 0.064 / 0.300 (1058) | - |
| prolateSpheroid__oblateSpheroid_test | 0.138 / 0.759 (702) | 0.109 / 0.722 (952) | 0.083 / 0.608 (668) | 0.066 / 0.549 (632) | 0.058 / 0.468 (1086) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed_s2.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 2: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.36 (4.35 / 4.92; 1.17) | 2.79 (2.80 / 2.66; 0.98) | 1.79 (1.79 / 1.70; 0.69) | 0.022 (0.019 / 0.056; 0.001) (1) |
| 0.05 | 200 | 10 | 7.47 (7.45 / 8.25; 2.23) | 5.53 (5.54 / 5.52; 1.94) | 3.08 (3.08 / 3.22; 1.15) | 0.013 (0.012 / 0.040; 0.001) (1) |
| 0.075 | 200 | 10 | 10.20 (10.18 / 11.62; 3.16) | 7.96 (7.95 / 8.66; 2.79) | 3.84 (3.83 / 4.52; 1.42) | 0.036 (0.033 / 0.065; 0.001) (1) |
| 0.1 | 200 | 10 | 13.82 (13.80 / 14.89; 4.19) | 11.01 (11.00 / 11.67; 3.73) | 4.80 (4.78 / 5.45; 1.57) | 0.034 (0.030 / 0.120; 0.002) (1) |
| 0.15 | 200 | 10 | 16.28 (16.15 / 22.42; 5.98) | 13.74 (13.63 / 18.69; 5.37) | 5.40 (5.34 / 7.90; 1.86) | 0.049 (0.041 / 0.156; 0.004) (1) |
| 0.2 | 200 | 10 | 25.10 (24.99 / 31.54; 7.59) | 21.52 (21.43 / 27.01; 6.84) | 7.58 (7.52 / 10.28; 2.30) | 0.060 (0.048 / 0.251; 0.006) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configurations**: N in [200] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.08 (7.08 / 7.39; 2.61) | 4.84 (4.83 / 5.20; 1.92) | 2.10 (2.07 / 2.78; 0.80) | 0.020 (0.020 / 0.029; 0.002) (1) |
| 0.05 | 100 | 5 | 6.83 (6.81 / 7.46; 2.35) | 4.85 (4.84 / 5.13; 1.93) | 2.39 (2.38 / 2.75; 0.87) | 0.032 (0.030 / 0.076; 0.002) (1) |
| 0.05 | 200 | 5 | 7.81 (7.80 / 8.58; 2.24) | 5.80 (5.81 / 5.74; 1.95) | 3.15 (3.14 / 3.38; 1.13) | not measured |
| 0.05 | 300 | 5 | 7.24 (7.22 / 8.24; 2.16) | 5.53 (5.53 / 5.53; 1.94) | 3.38 (3.39 / 3.40; 1.30) | not measured |
| 0.1 | 50 | 5 | 12.61 (12.55 / 14.44; 4.59) | 9.20 (9.13 / 11.30; 3.55) | 3.29 (3.23 / 4.53; 1.19) | 0.036 (0.032 / 0.086; 0.002) (1) |
| 0.1 | 100 | 5 | 11.73 (11.66 / 14.08; 4.09) | 8.83 (8.78 / 10.45; 3.41) | 3.68 (3.64 / 4.85; 1.15) | 0.028 (0.023 / 0.110; 0.004) (1) |
| 0.1 | 200 | 5 | 12.76 (12.72 / 14.53; 4.10) | 10.01 (9.98 / 11.35; 3.65) | 4.39 (4.36 / 5.33; 1.58) | not measured |
| 0.1 | 300 | 5 | 12.68 (12.62 / 15.32; 4.06) | 10.39 (10.36 / 12.02; 3.71) | 5.11 (5.10 / 5.92; 1.98) | not measured |
| 0.15 | 50 | 5 | 16.71 (16.57 / 21.87; 6.07) | 12.94 (12.82 / 17.23; 4.71) | 4.07 (3.94 / 7.04; 1.31) | 0.050 (0.042 / 0.117; 0.006) (1) |
| 0.15 | 100 | 5 | 16.75 (16.59 / 23.13; 6.08) | 13.71 (13.60 / 18.61; 5.15) | 4.36 (4.26 / 7.68; 1.43) | 0.032 (0.028 / 0.116; 0.004) (1) |
| 0.15 | 200 | 5 | 17.56 (17.44 / 22.21; 5.94) | 14.90 (14.81 / 18.63; 5.34) | 5.91 (5.86 / 7.98; 1.84) | not measured |
| 0.15 | 300 | 5 | 20.72 (20.67 / 23.72; 5.89) | 17.21 (17.17 / 19.62; 5.42) | 7.06 (7.04 / 8.05; 2.31) | not measured |
| 0.2 | 50 | 5 | 18.62 (18.35 / 29.33; 7.86) | 14.30 (14.03 / 24.44; 6.21) | 3.87 (3.68 / 9.15; 1.27) | 0.037 (0.030 / 0.165; 0.007) (1) |
| 0.2 | 100 | 5 | 24.91 (24.71 / 32.14; 7.83) | 20.60 (20.44 / 26.58; 6.70) | 6.34 (6.23 / 9.80; 1.59) | 0.048 (0.038 / 0.271; 0.006) (1) |
| 0.2 | 200 | 5 | 28.20 (28.19 / 30.89; 7.61) | 24.28 (24.27 / 26.53; 6.87) | 8.48 (8.43 / 10.39; 2.34) | not measured |
| 0.2 | 300 | 5 | 23.67 (23.54 / 33.15; 7.68) | 20.84 (20.74 / 28.80; 7.09) | 8.59 (8.57 / 11.11; 2.83) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: pair of triaxial_123, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 89.7, 245 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.09 | 0.094 | 0.31 |
| + two-body | 1500 | 0.01 | 0.041 | 0.24 |
| + many-body | 1500 | 0.01 | 0.041 | 0.24 |
| MFS Xfine (the truth's own error) | 1500 | 0.005 | 0.0104 | 0.283 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: triaxial_123, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Dynamics: ring of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_123, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 123 steps, fell 16.8, 111 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 41 | 5.25 | 0.472 | 7.59 |
| + two-body | 69 | 1.93 | 0.323 | 6.66 |
| + many-body | 82 | 0.49 | 0.121 | 3.51 |
| MFS Xfine (the truth's own error) | 123 | 0.006 | 0.0023 | 0.245 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_123, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Structural checks, 16 particles of triaxial_123, prolateSpheroid, oblateSpheroid at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.3e-16 | 1.5557 | 5.7e-16 | 8.53 |
| + two-body | 9.8e-17 | 0.6182 | 4.7e-16 | 5.32 |
| + many-body | 1.0e-16 | 0.9593 | 4.8e-16 | 1.98 |
| MFS fine (the truth) | 2.4e-04 | 1 | | 0 |
| MFS Xfine | 6.0e-05 | 0.9893 | | 0.019 (= the error of the fine truth) |

MFS smallest eigenvalue 1.8431e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configuration**: ONE random suspension, N = 16, shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Positive definiteness of the operator, triaxial_123, prolateSpheroid, oblateSpheroid

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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -6.355 | 0.77 | oblateSpheroid, prolateSpheroid | 3.13 | 1.113 | 4.70e-03 / 2.10e-03 (0.447) | 0.461, 0.359 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 5 | -2.085 | 0.06 | triaxial_123, triaxial_123 | 13.71 | inf | 3.78e-03 / 3.78e-03 (1.000) | 0.827, 0.815 (9 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.944 / 1.000 | 1.057, 2.73 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.977 / 1.000 | 1.059, 3.75 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.973 / 1.000 | 1.066, 2.50 |
| triaxial_123__prolateSpheroid_test | 400 | 400 | 0.924 / 1.000 | 1.054, 3.29 |
| triaxial_123__oblateSpheroid_test | 400 | 400 | 0.945 / 1.000 | 1.068, 2.48 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.990 / 1.000 | 1.053, 3.94 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_123, prolateSpheroid, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.69 (7.65 / 8.50) | 4.99 (4.98 / 5.39) | 2.33 (2.31 / 2.80) | 1.68 (1.69 / 1.38) | 1.58 (1.59 / 1.21) |
| 0.1 | 64 | 3 | 13.26 (13.18 / 15.32) | 9.36 (9.27 / 11.50) | 3.70 (3.63 / 5.11) | 2.36 (2.38 / 2.04) | 2.17 (2.19 / 1.72) |
| 0.2 | 64 | 3 | 26.36 (26.15 / 35.18) | 21.79 (21.54 / 31.09) | 5.18 (5.01 / 9.49) | 3.51 (3.49 / 4.37) | 2.15 (2.18 / 1.62) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configurations**: N in [64], shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

### Case 3D (cells 3D and 4D): triaxial form, every shape and size mixed

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 160 / 136; 1.0202 / 0.6747 | 340 / 290; 0.0860 / 0.1317 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 160 / 136; 0.1260 / 0.1371 | 340 / 290; 0.0028 / 0.0029 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 160 / 136; 0.9743 / 0.9167 | 340 / 290; 0.0749 / 0.0953 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 208 / 177; 0.4098 / 0.8140 | 441 / 376; 0.1718 / 0.0670 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 256 / 218; 0.8042 / 0.8770 | 544 / 464; 0.0609 / 0.2178 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 290 / 246; 0.6170 / 0.5146 | 616 / 525; 0.2287 / 0.2159 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| prolateSpheroid | 1 : 1 : 3 | 150 / 131; 0.0325 / 0.1955 | 348 / 304; 0.0230 / 0.0079 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 174 / 152; 2.8747 / 0.1707 | 334 / 292; 0.0385 / 0.0193 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 160 / 136; 1.0207 / 0.6783 | 340 / 290; 0.0857 / 0.1304 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 174 / 152; 2.7969 / 0.1689 | 334 / 292; 0.0405 / 0.0196 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x1p25 | 1.25 : 1.25 : 3.75 | 150 / 131; 0.0314 / 0.1944 | 348 / 304; 0.0225 / 0.0081 | 654 / 572; 0.0005 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| triaxial_1p5_2_x1p5 | 1.5 : 2.25 : 3 | 160 / 136; 0.1257 / 0.1361 | 340 / 290; 0.0028 / 0.0029 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 220 / 187; 0.9932 / 1.1209 | 467 / 399; 0.1688 / 0.2584 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 424 / 360; 0.6915 / 1.0622 | 901 / 768; 0.1195 / 0.5111 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Two-body accuracy of `data/final_c/models/pair_poly.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.081 | 0.401 | 0.097 | 1.12 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.084 / 0.499 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.071 | 0.383 | 0.095 | 0.77 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.073 / 0.356 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.117 | 0.646 | 0.147 | 1.38 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.122 / 0.710 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.155 | 0.908 | 0.183 | 2.41 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.158 / 0.814 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.243 | 1.538 | 0.283 | 3.97 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.245 / 1.482 | 0.052 / 0.391 | 0.0 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.164 | 0.876 | 0.184 | 3.11 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.141 / 0.727 | 0.046 / 0.249 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.112 | 0.789 | 0.168 | 1.19 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.116 / 0.840 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.095 | 0.631 | 0.133 | 0.85 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.081 / 0.545 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.111 | 0.615 | 0.143 | 1.34 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.118 / 0.899 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.094 | 0.496 | 0.115 | 1.11 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.078 / 0.432 | 0.042 / 0.294 | 0.0 % |
| triaxial_123__triaxial_2_5_test | 4024 | 0.246 | 1.328 | 0.286 | 3.46 | 4.23 / 13.78 | 0.053 / 0.353 (508) | 0.236 / 1.433 | 0.051 / 0.360 | 0.0 % |
| prolateSpheroid__triaxial_2_5_test | 4030 | 0.301 | 1.645 | 0.355 | 3.62 | 4.17 / 15.40 | 0.117 / 0.760 (504) | 0.249 / 1.427 | 0.091 / 0.582 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.106 | 0.694 | 0.151 | 0.97 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.087 / 0.611 | 0.004 / 0.024 | 0.0 % |
| triaxial_123__triaxial_1p5_2_test | 4038 | 0.114 | 0.572 | 0.140 | 1.36 | 4.57 / 11.54 | 0.079 / 0.402 (500) | 0.112 / 0.590 | 0.051 / 0.350 | 0.0 % |
| triaxial_123__triaxial_2_4_test | 4042 | 0.139 | 0.778 | 0.169 | 2.06 | 4.18 / 12.46 | 0.124 / 0.411 (512) | 0.169 / 0.821 | 0.052 / 0.375 | 0.0 % |
| triaxial_123__triaxial_3_4_test | 4036 | 0.208 | 1.010 | 0.236 | 3.00 | 3.83 / 12.07 | 0.114 / 0.792 (506) | 0.195 / 0.970 | 0.051 / 0.293 | 0.0 % |
| oblateSpheroid__triaxial_1p5_2_test | 4048 | 0.087 | 0.499 | 0.116 | 0.93 | 5.12 / 11.20 | 0.019 / 0.060 (506) | 0.077 / 0.480 | 0.006 / 0.039 | 0.0 % |
| prolateSpheroid__triaxial_2_4_test | 4020 | 0.190 | 0.966 | 0.230 | 2.34 | 4.13 / 13.13 | 0.100 / 0.512 (504) | 0.165 / 0.877 | 0.081 / 0.531 | 0.0 % |
| triaxial_2_5__triaxial_3_4_test | 4052 | 0.261 | 1.449 | 0.296 | 4.22 | 3.80 / 12.54 | 0.079 / 0.458 (502) | 0.230 / 1.372 | 0.042 / 0.275 | 0.0 % |
| triaxial_123_x0p75__triaxial_123_test | 4026 | 0.137 | 0.636 | 0.165 | 1.91 | 4.16 / 12.62 | 0.075 / 0.477 (500) | 0.134 / 0.645 | 0.051 / 0.336 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.103 | 0.723 | 0.134 | 1.20 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.100 / 0.771 | 0.004 / 0.024 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_test | 4044 | 0.138 | 0.956 | 0.186 | 1.52 | 4.64 / 12.36 | 0.030 / 0.207 (500) | 0.132 / 0.981 | 0.005 / 0.028 | 0.0 % |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 4024 | 0.092 | 0.507 | 0.113 | 1.15 | 4.73 / 10.69 | 0.041 / 0.184 (512) | 0.105 / 0.517 | 0.014 / 0.094 | 0.0 % |
| triaxial_123_x0p75__prolateSpheroid_test | 4020 | 0.150 | 0.764 | 0.198 | 1.77 | 4.67 / 12.89 | 0.048 / 0.254 (508) | 0.140 / 0.771 | 0.044 / 0.288 | 0.0 % |
| oblateSpheroid_x1p5__triaxial_123_test | 4042 | 0.101 | 0.532 | 0.116 | 1.19 | 4.50 / 10.84 | 0.029 / 0.128 (506) | 0.094 / 0.517 | 0.023 / 0.162 | 0.0 % |
| oblateSpheroid__triaxial_2_5_test | 4016 | 0.747 | 4.495 | 0.920 | 6.37 | 4.37 / 15.31 | 0.072 / 0.571 (502) | 0.779 / 4.621 | 0.061 / 0.418 | 0.0 % |
| triaxial_1p5_2__triaxial_3_4_test | 4020 | 0.667 | 3.033 | 0.763 | 5.22 | 4.05 / 14.29 | 0.098 / 0.402 (496) | 0.644 / 2.703 | 0.071 / 0.395 | 0.0 % |
| triaxial_123__triaxial_2p5_3p5_test | 4034 | 0.180 | 1.231 | 0.231 | 2.02 | 4.09 / 11.77 | 0.061 / 0.389 (504) | 0.182 / 1.273 | 0.053 / 0.350 | 0.0 % |
| prolateSpheroid__triaxial_3_6_test | 4024 | 1.883 | 9.977 | 2.141 | 12.08 | 3.88 / 17.30 | 0.100 / 0.494 (502) | 1.812 / 9.474 | 0.058 / 0.340 | 100.0 % |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 4036 | 0.062 | 0.496 | 0.081 | 0.82 | 5.09 / 9.84 | 0.023 / 0.049 (506) | 0.073 / 0.572 | 0.005 / 0.032 | 0.0 % |
| triaxial_123_x0p75__triaxial_3_4_test | 4024 | 0.700 | 4.061 | 0.867 | 6.94 | 3.75 / 14.24 | 0.111 / 0.515 (502) | 0.677 / 4.256 | 0.071 / 0.397 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 4042 | 0.098 | 0.717 | 0.132 | 1.13 | 4.57 / 11.09 | 0.016 / 0.091 (506) | 0.089 / 0.602 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.122 / 0.512 (666) | 0.067 / 0.338 (868) | 0.047 / 0.282 (688) | 0.045 / 0.269 (672) | 0.046 / 0.284 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.096 / 0.440 (642) | 0.068 / 0.375 (962) | 0.051 / 0.317 (710) | 0.040 / 0.245 (674) | 0.037 / 0.245 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.163 / 0.761 (756) | 0.102 / 0.593 (852) | 0.076 / 0.488 (622) | 0.070 / 0.456 (728) | 0.063 / 0.455 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.227 / 1.224 (706) | 0.130 / 0.733 (872) | 0.095 / 0.563 (730) | 0.093 / 0.553 (648) | 0.091 / 0.597 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.330 / 1.947 (704) | 0.230 / 1.431 (898) | 0.173 / 1.037 (634) | 0.148 / 0.882 (676) | 0.147 / 0.993 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.243 / 1.192 (686) | 0.132 / 0.684 (866) | 0.106 / 0.596 (686) | 0.096 / 0.508 (724) | 0.098 / 0.522 (1058) | - |
| prolateSpheroid__prolateSpheroid_test | 0.151 / 0.954 (684) | 0.101 / 0.723 (898) | 0.088 / 0.634 (660) | 0.076 / 0.548 (754) | 0.075 / 0.631 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.129 / 0.785 (650) | 0.099 / 0.586 (936) | 0.059 / 0.435 (680) | 0.036 / 0.363 (738) | 0.031 / 0.323 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.157 / 0.756 (668) | 0.099 / 0.544 (876) | 0.074 / 0.445 (668) | 0.067 / 0.469 (738) | 0.067 / 0.497 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.144 / 0.642 (686) | 0.073 / 0.412 (916) | 0.056 / 0.342 (684) | 0.045 / 0.318 (688) | 0.042 / 0.299 (1058) | - |
| triaxial_123__triaxial_2_5_test | 0.346 / 1.670 (700) | 0.226 / 1.173 (918) | 0.164 / 0.997 (744) | 0.151 / 0.949 (648) | 0.141 / 0.921 (1014) | - |
| prolateSpheroid__triaxial_2_5_test | 0.448 / 2.279 (626) | 0.264 / 1.396 (962) | 0.200 / 1.092 (656) | 0.171 / 0.950 (710) | 0.159 / 1.004 (1076) | - |
| prolateSpheroid__oblateSpheroid_test | 0.137 / 0.754 (702) | 0.106 / 0.710 (952) | 0.081 / 0.585 (668) | 0.062 / 0.527 (632) | 0.047 / 0.459 (1086) | - |
| triaxial_123__triaxial_1p5_2_test | 0.161 / 0.685 (652) | 0.105 / 0.533 (948) | 0.078 / 0.437 (690) | 0.066 / 0.408 (662) | 0.060 / 0.388 (1086) | - |
| triaxial_123__triaxial_2_4_test | 0.195 / 0.961 (684) | 0.126 / 0.711 (850) | 0.097 / 0.587 (728) | 0.083 / 0.514 (668) | 0.082 / 0.538 (1112) | - |
| triaxial_123__triaxial_3_4_test | 0.316 / 1.337 (658) | 0.177 / 0.864 (932) | 0.128 / 0.640 (676) | 0.104 / 0.611 (724) | 0.100 / 0.594 (1046) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.123 / 0.604 (700) | 0.077 / 0.448 (866) | 0.058 / 0.378 (752) | 0.044 / 0.334 (678) | 0.042 / 0.286 (1052) | - |
| prolateSpheroid__triaxial_2_4_test | 0.276 / 1.217 (678) | 0.167 / 0.786 (876) | 0.131 / 0.834 (728) | 0.109 / 0.696 (686) | 0.104 / 0.671 (1052) | - |
| triaxial_2_5__triaxial_3_4_test | 0.360 / 1.839 (678) | 0.239 / 1.260 (864) | 0.193 / 1.123 (688) | 0.173 / 1.054 (744) | 0.172 / 1.050 (1078) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.200 / 0.809 (666) | 0.117 / 0.546 (942) | 0.089 / 0.447 (686) | 0.076 / 0.442 (698) | 0.072 / 0.422 (1034) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.146 / 0.866 (662) | 0.096 / 0.702 (936) | 0.068 / 0.498 (688) | 0.053 / 0.423 (712) | 0.047 / 0.326 (1034) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.194 / 1.202 (716) | 0.123 / 0.889 (888) | 0.084 / 0.615 (688) | 0.091 / 0.669 (726) | 0.082 / 0.645 (1026) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.131 / 0.604 (642) | 0.080 / 0.468 (836) | 0.064 / 0.402 (674) | 0.056 / 0.357 (706) | 0.058 / 0.355 (1166) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.199 / 0.910 (742) | 0.144 / 0.702 (864) | 0.107 / 0.594 (710) | 0.097 / 0.537 (658) | 0.085 / 0.535 (1046) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.147 / 0.638 (664) | 0.083 / 0.500 (938) | 0.065 / 0.395 (692) | 0.060 / 0.359 (632) | 0.065 / 0.362 (1116) | - |
| oblateSpheroid__triaxial_2_5_test | 0.945 / 5.156 (690) | 0.789 / 4.408 (878) | 0.621 / 3.887 (712) | 0.436 / 3.105 (674) | 0.292 / 2.388 (1062) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.861 / 3.547 (672) | 0.668 / 2.965 (918) | 0.567 / 2.540 (608) | 0.456 / 2.051 (676) | 0.281 / 1.457 (1146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.237 / 1.375 (650) | 0.171 / 1.233 (912) | 0.148 / 1.055 (700) | 0.121 / 0.958 (664) | 0.104 / 0.943 (1108) | - |
| prolateSpheroid__triaxial_3_6_test | 2.625 / 12.616 (654) | 2.021 / 9.919 (872) | 1.260 / 7.317 (702) | 0.806 / 5.573 (678) | 0.562 / 4.207 (1118) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.082 / 0.625 (636) | 0.060 / 0.439 (896) | 0.043 / 0.361 (620) | 0.039 / 0.300 (676) | 0.042 / 0.254 (1208) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 0.972 / 5.216 (738) | 0.685 / 3.668 (896) | 0.451 / 2.656 (730) | 0.331 / 1.882 (632) | 0.231 / 1.475 (1028) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.136 / 0.846 (672) | 0.090 / 0.712 (936) | 0.072 / 0.472 (714) | 0.066 / 0.561 (690) | 0.068 / 0.634 (1030) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.032 / 0.127 (70) | 0.004 / 0.014 (140) | 0.001 / 0.004 (90) | 0.001 / 0.002 (76) | 0.000 / 0.002 (126) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.667 (102) | 0.035 / 0.162 (100) | 0.011 / 0.039 (64) | 0.006 / 0.025 (98) | 0.004 / 0.016 (142) | - |
| triaxial_2_4__triaxial_2_4_test | 0.172 / 0.596 (74) | 0.039 / 0.291 (94) | 0.015 / 0.091 (92) | 0.008 / 0.038 (78) | 0.005 / 0.025 (168) | - |
| triaxial_2_5__triaxial_2_5_test | 0.120 / 0.507 (118) | 0.039 / 0.239 (90) | 0.018 / 0.098 (66) | 0.015 / 0.075 (104) | 0.009 / 0.052 (128) | - |
| triaxial_3_4__triaxial_3_4_test | 0.096 / 0.399 (102) | 0.050 / 0.255 (94) | 0.029 / 0.120 (64) | 0.015 / 0.071 (104) | 0.009 / 0.046 (140) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| triaxial_123__triaxial_2_5_test | 0.094 / 0.606 (64) | 0.045 / 0.223 (144) | 0.015 / 0.065 (82) | 0.015 / 0.066 (84) | 0.010 / 0.052 (134) | - |
| prolateSpheroid__triaxial_2_5_test | 0.241 / 1.467 (64) | 0.055 / 0.193 (118) | 0.025 / 0.109 (94) | 0.012 / 0.068 (102) | 0.010 / 0.050 (126) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| triaxial_123__triaxial_1p5_2_test | 0.154 / 0.697 (62) | 0.043 / 0.141 (138) | 0.015 / 0.050 (96) | 0.009 / 0.036 (66) | 0.005 / 0.022 (138) | - |
| triaxial_123__triaxial_2_4_test | 0.198 / 0.607 (114) | 0.041 / 0.173 (86) | 0.017 / 0.058 (86) | 0.010 / 0.039 (72) | 0.005 / 0.027 (154) | - |
| triaxial_123__triaxial_3_4_test | 0.183 / 1.217 (104) | 0.058 / 0.215 (114) | 0.033 / 0.147 (76) | 0.017 / 0.067 (80) | 0.009 / 0.040 (132) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.034 / 0.091 (86) | 0.005 / 0.016 (106) | 0.001 / 0.005 (106) | 0.001 / 0.003 (78) | 0.000 / 0.003 (130) | - |
| prolateSpheroid__triaxial_2_4_test | 0.195 / 0.845 (66) | 0.067 / 0.366 (98) | 0.019 / 0.078 (116) | 0.008 / 0.041 (102) | 0.006 / 0.025 (122) | - |
| triaxial_2_5__triaxial_3_4_test | 0.134 / 0.716 (86) | 0.054 / 0.307 (108) | 0.028 / 0.104 (86) | 0.014 / 0.068 (94) | 0.010 / 0.052 (128) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.133 / 0.784 (76) | 0.047 / 0.217 (120) | 0.018 / 0.064 (100) | 0.008 / 0.036 (94) | 0.006 / 0.027 (110) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.051 / 0.326 (106) | 0.007 / 0.026 (118) | 0.002 / 0.007 (64) | 0.002 / 0.005 (78) | 0.001 / 0.005 (134) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.071 / 0.289 (90) | 0.008 / 0.023 (110) | 0.001 / 0.005 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (146) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.085 / 0.411 (78) | 0.020 / 0.086 (100) | 0.009 / 0.040 (86) | 0.005 / 0.022 (90) | 0.004 / 0.020 (154) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.052 / 0.205 (80) | 0.016 / 0.061 (96) | 0.007 / 0.027 (98) | 0.004 / 0.025 (74) | 0.004 / 0.023 (158) | - |
| oblateSpheroid__triaxial_2_5_test | 0.119 / 0.902 (98) | 0.038 / 0.163 (104) | 0.021 / 0.076 (78) | 0.012 / 0.047 (90) | 0.007 / 0.037 (132) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.152 / 0.616 (84) | 0.092 / 0.296 (112) | 0.051 / 0.182 (84) | 0.020 / 0.074 (70) | 0.010 / 0.039 (146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.102 / 0.617 (92) | 0.034 / 0.198 (128) | 0.021 / 0.091 (84) | 0.012 / 0.076 (86) | 0.008 / 0.069 (114) | - |
| prolateSpheroid__triaxial_3_6_test | 0.163 / 0.776 (80) | 0.108 / 0.481 (90) | 0.029 / 0.108 (118) | 0.018 / 0.061 (72) | 0.013 / 0.057 (142) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.040 / 0.074 (86) | 0.008 / 0.013 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (74) | 0.000 / 0.003 (160) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 0.179 / 0.771 (86) | 0.090 / 0.407 (100) | 0.050 / 0.195 (86) | 0.024 / 0.088 (96) | 0.011 / 0.039 (134) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.033 / 0.166 (66) | 0.005 / 0.025 (108) | 0.002 / 0.006 (90) | 0.002 / 0.006 (116) | 0.001 / 0.004 (126) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_5_test`: triaxial_123 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_5_test`: prolateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4030 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_1p5_2_test`: triaxial_123 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4038 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_4_test`: triaxial_123 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_3_4_test`: triaxial_123 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_1p5_2_test`: oblateSpheroid (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4048 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_4_test`: prolateSpheroid (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_3_4_test`: triaxial_2_5 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_123_test`: triaxial_123_x0p75 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2_x1p5__triaxial_1p5_2_test`: triaxial_1p5_2_x1p5 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__prolateSpheroid_test`: triaxial_123_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_123_test`: oblateSpheroid_x1p5 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_2_5_test`: oblateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_3_4_test`: triaxial_1p5_2 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2p5_3p5_test`: triaxial_123 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_3_6_test`: prolateSpheroid (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test`: oblateSpheroid_x1p5 (target or source) with triaxial_1p5_2_x1p5, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_3_4_test`: triaxial_123_x0p75 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_x1p25_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid_x1p25, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x1p25 | 1.25 : 1.25 : 3.75 | 654 / 572; 0.0005 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| triaxial_1p5_2_x1p5 | 1.5 : 2.25 : 3 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Two-body accuracy of `data/final_c/models/pair_poly_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.081 | 0.399 | 0.096 | 1.09 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.078 / 0.508 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.071 | 0.386 | 0.095 | 0.76 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.075 / 0.346 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.117 | 0.639 | 0.147 | 1.33 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.120 / 0.696 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.146 | 0.863 | 0.178 | 2.32 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.142 / 0.803 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.251 | 1.530 | 0.286 | 3.82 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.258 / 1.521 | 0.052 / 0.391 | 0.0 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.165 | 0.889 | 0.181 | 2.99 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.138 / 0.712 | 0.046 / 0.249 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.113 | 0.767 | 0.166 | 1.12 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.112 / 0.817 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.092 | 0.615 | 0.128 | 0.81 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.079 / 0.528 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.109 | 0.618 | 0.143 | 1.30 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.115 / 0.884 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.093 | 0.495 | 0.114 | 1.10 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.077 / 0.442 | 0.042 / 0.294 | 0.0 % |
| triaxial_123__triaxial_2_5_test | 4024 | 0.247 | 1.312 | 0.289 | 3.40 | 4.23 / 13.78 | 0.053 / 0.353 (508) | 0.250 / 1.322 | 0.051 / 0.360 | 0.0 % |
| prolateSpheroid__triaxial_2_5_test | 4030 | 0.304 | 1.619 | 0.360 | 3.52 | 4.17 / 15.40 | 0.117 / 0.760 (504) | 0.278 / 1.453 | 0.091 / 0.582 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.107 | 0.703 | 0.152 | 0.95 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.094 / 0.648 | 0.004 / 0.024 | 0.0 % |
| triaxial_123__triaxial_1p5_2_test | 4038 | 0.111 | 0.556 | 0.138 | 1.33 | 4.57 / 11.54 | 0.079 / 0.402 (500) | 0.116 / 0.606 | 0.051 / 0.350 | 0.0 % |
| triaxial_123__triaxial_2_4_test | 4042 | 0.139 | 0.768 | 0.168 | 2.03 | 4.18 / 12.46 | 0.124 / 0.411 (512) | 0.172 / 0.831 | 0.052 / 0.375 | 0.0 % |
| triaxial_123__triaxial_3_4_test | 4036 | 0.197 | 1.014 | 0.230 | 2.93 | 3.83 / 12.07 | 0.114 / 0.792 (506) | 0.187 / 1.003 | 0.051 / 0.293 | 0.0 % |
| oblateSpheroid__triaxial_1p5_2_test | 4048 | 0.084 | 0.489 | 0.113 | 0.90 | 5.12 / 11.20 | 0.019 / 0.060 (506) | 0.076 / 0.493 | 0.006 / 0.039 | 0.0 % |
| prolateSpheroid__triaxial_2_4_test | 4020 | 0.194 | 0.989 | 0.234 | 2.32 | 4.13 / 13.13 | 0.100 / 0.512 (504) | 0.180 / 0.919 | 0.081 / 0.531 | 0.0 % |
| triaxial_2_5__triaxial_3_4_test | 4052 | 0.248 | 1.425 | 0.285 | 4.28 | 3.80 / 12.54 | 0.079 / 0.458 (502) | 0.233 / 1.377 | 0.042 / 0.275 | 0.0 % |
| triaxial_123_x0p75__triaxial_123_test | 4026 | 0.135 | 0.639 | 0.167 | 1.84 | 4.16 / 12.62 | 0.075 / 0.477 (500) | 0.128 / 0.665 | 0.051 / 0.336 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.101 | 0.713 | 0.130 | 1.17 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.105 / 0.756 | 0.004 / 0.024 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_test | 4044 | 0.135 | 0.939 | 0.183 | 1.47 | 4.64 / 12.36 | 0.030 / 0.207 (500) | 0.129 / 0.988 | 0.005 / 0.028 | 0.0 % |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 4024 | 0.093 | 0.501 | 0.114 | 1.14 | 4.73 / 10.69 | 0.041 / 0.184 (512) | 0.101 / 0.526 | 0.014 / 0.094 | 0.0 % |
| triaxial_123_x0p75__prolateSpheroid_test | 4020 | 0.149 | 0.784 | 0.197 | 1.73 | 4.67 / 12.89 | 0.048 / 0.254 (508) | 0.134 / 0.759 | 0.044 / 0.288 | 0.0 % |
| oblateSpheroid_x1p5__triaxial_123_test | 4042 | 0.095 | 0.533 | 0.112 | 1.22 | 4.50 / 10.84 | 0.029 / 0.128 (506) | 0.091 / 0.547 | 0.023 / 0.162 | 0.0 % |
| oblateSpheroid__triaxial_2_5_test | 4016 | 0.767 | 4.509 | 0.942 | 6.13 | 4.37 / 15.31 | 0.072 / 0.571 (502) | 0.804 / 4.676 | 0.061 / 0.418 | 0.0 % |
| triaxial_1p5_2__triaxial_3_4_test | 4020 | 0.705 | 3.286 | 0.803 | 5.77 | 4.05 / 14.29 | 0.098 / 0.402 (496) | 0.626 / 2.795 | 0.071 / 0.395 | 0.0 % |
| triaxial_123__triaxial_2p5_3p5_test | 4034 | 0.129 | 0.697 | 0.154 | 1.84 | 4.09 / 11.77 | 0.061 / 0.389 (504) | 0.149 / 0.770 | 0.053 / 0.350 | 0.0 % |
| prolateSpheroid__triaxial_3_6_test | 4024 | 1.786 | 10.166 | 2.054 | 12.99 | 3.88 / 17.30 | 0.100 / 0.494 (502) | 1.734 / 9.606 | 0.058 / 0.340 | 100.0 % |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 4036 | 0.062 | 0.491 | 0.081 | 0.78 | 5.09 / 9.84 | 0.023 / 0.049 (506) | 0.072 / 0.557 | 0.005 / 0.032 | 0.0 % |
| triaxial_123_x0p75__triaxial_3_4_test | 4024 | 0.879 | 4.326 | 1.025 | 8.16 | 3.75 / 14.24 | 0.111 / 0.515 (502) | 0.829 / 4.492 | 0.071 / 0.397 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 4042 | 0.098 | 0.711 | 0.131 | 1.04 | 4.57 / 11.09 | 0.016 / 0.091 (506) | 0.087 / 0.606 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.123 / 0.509 (666) | 0.065 / 0.340 (868) | 0.046 / 0.276 (688) | 0.045 / 0.265 (672) | 0.045 / 0.288 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.097 / 0.450 (642) | 0.068 / 0.373 (962) | 0.049 / 0.311 (710) | 0.038 / 0.237 (674) | 0.037 / 0.261 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.164 / 0.761 (756) | 0.102 / 0.576 (852) | 0.077 / 0.486 (622) | 0.066 / 0.431 (728) | 0.062 / 0.428 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.207 / 1.154 (706) | 0.129 / 0.697 (872) | 0.099 / 0.546 (730) | 0.088 / 0.557 (648) | 0.097 / 0.591 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.345 / 1.931 (704) | 0.232 / 1.442 (898) | 0.170 / 0.999 (634) | 0.161 / 0.873 (676) | 0.167 / 0.995 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.243 / 1.202 (686) | 0.137 / 0.718 (866) | 0.108 / 0.583 (686) | 0.097 / 0.513 (724) | 0.099 / 0.501 (1058) | - |
| prolateSpheroid__prolateSpheroid_test | 0.154 / 0.917 (684) | 0.101 / 0.708 (898) | 0.089 / 0.631 (660) | 0.078 / 0.555 (754) | 0.075 / 0.638 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.126 / 0.770 (650) | 0.096 / 0.571 (936) | 0.057 / 0.408 (680) | 0.036 / 0.345 (738) | 0.029 / 0.305 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.156 / 0.782 (668) | 0.097 / 0.529 (876) | 0.071 / 0.426 (668) | 0.067 / 0.438 (738) | 0.069 / 0.480 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.142 / 0.647 (686) | 0.072 / 0.409 (916) | 0.055 / 0.330 (684) | 0.045 / 0.305 (688) | 0.047 / 0.281 (1058) | - |
| triaxial_123__triaxial_2_5_test | 0.342 / 1.646 (700) | 0.230 / 1.171 (918) | 0.173 / 0.998 (744) | 0.160 / 0.895 (648) | 0.147 / 0.860 (1014) | - |
| prolateSpheroid__triaxial_2_5_test | 0.446 / 2.201 (626) | 0.274 / 1.419 (962) | 0.196 / 1.090 (656) | 0.177 / 0.957 (710) | 0.174 / 0.999 (1076) | - |
| prolateSpheroid__oblateSpheroid_test | 0.139 / 0.780 (702) | 0.106 / 0.712 (952) | 0.078 / 0.573 (668) | 0.061 / 0.512 (632) | 0.049 / 0.441 (1086) | - |
| triaxial_123__triaxial_1p5_2_test | 0.156 / 0.651 (652) | 0.101 / 0.529 (948) | 0.076 / 0.441 (690) | 0.067 / 0.406 (662) | 0.060 / 0.391 (1086) | - |
| triaxial_123__triaxial_2_4_test | 0.194 / 0.940 (684) | 0.129 / 0.716 (850) | 0.097 / 0.567 (728) | 0.084 / 0.530 (668) | 0.085 / 0.536 (1112) | - |
| triaxial_123__triaxial_3_4_test | 0.292 / 1.349 (658) | 0.172 / 0.856 (932) | 0.122 / 0.643 (676) | 0.113 / 0.609 (724) | 0.104 / 0.578 (1046) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.117 / 0.593 (700) | 0.076 / 0.438 (866) | 0.057 / 0.365 (752) | 0.046 / 0.327 (678) | 0.037 / 0.285 (1052) | - |
| prolateSpheroid__triaxial_2_4_test | 0.284 / 1.257 (678) | 0.169 / 0.801 (876) | 0.133 / 0.833 (728) | 0.103 / 0.696 (686) | 0.107 / 0.673 (1052) | - |
| triaxial_2_5__triaxial_3_4_test | 0.350 / 1.819 (678) | 0.219 / 1.248 (864) | 0.182 / 1.070 (688) | 0.155 / 0.999 (744) | 0.169 / 1.018 (1078) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.199 / 0.815 (666) | 0.112 / 0.551 (942) | 0.089 / 0.440 (686) | 0.077 / 0.425 (698) | 0.076 / 0.413 (1034) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.139 / 0.861 (662) | 0.095 / 0.685 (936) | 0.073 / 0.492 (688) | 0.057 / 0.410 (712) | 0.048 / 0.318 (1034) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.188 / 1.178 (716) | 0.120 / 0.868 (888) | 0.091 / 0.612 (688) | 0.091 / 0.682 (726) | 0.081 / 0.658 (1026) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.129 / 0.594 (642) | 0.083 / 0.460 (836) | 0.068 / 0.413 (674) | 0.061 / 0.360 (706) | 0.061 / 0.350 (1166) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.199 / 0.956 (742) | 0.140 / 0.705 (864) | 0.102 / 0.589 (710) | 0.090 / 0.515 (658) | 0.092 / 0.515 (1046) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.136 / 0.642 (664) | 0.082 / 0.507 (938) | 0.062 / 0.384 (692) | 0.059 / 0.342 (632) | 0.057 / 0.334 (1116) | - |
| oblateSpheroid__triaxial_2_5_test | 1.010 / 5.451 (690) | 0.795 / 4.331 (878) | 0.577 / 3.478 (712) | 0.428 / 2.590 (674) | 0.298 / 1.870 (1062) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.977 / 4.149 (672) | 0.729 / 3.130 (918) | 0.455 / 2.189 (608) | 0.309 / 1.526 (676) | 0.209 / 1.183 (1146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.188 / 0.890 (650) | 0.113 / 0.624 (912) | 0.085 / 0.480 (700) | 0.072 / 0.445 (664) | 0.069 / 0.428 (1108) | - |
| prolateSpheroid__triaxial_3_6_test | 2.491 / 13.136 (654) | 1.846 / 9.950 (872) | 1.254 / 7.033 (702) | 0.895 / 5.470 (678) | 0.720 / 4.561 (1118) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.083 / 0.617 (636) | 0.062 / 0.436 (896) | 0.043 / 0.362 (620) | 0.038 / 0.298 (676) | 0.034 / 0.248 (1208) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 1.221 / 5.622 (738) | 0.849 / 3.939 (896) | 0.575 / 2.524 (730) | 0.437 / 1.746 (632) | 0.312 / 1.412 (1028) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.136 / 0.831 (672) | 0.090 / 0.710 (936) | 0.069 / 0.476 (714) | 0.068 / 0.568 (690) | 0.068 / 0.626 (1030) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.032 / 0.127 (70) | 0.004 / 0.014 (140) | 0.001 / 0.004 (90) | 0.001 / 0.002 (76) | 0.000 / 0.002 (126) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.667 (102) | 0.035 / 0.162 (100) | 0.011 / 0.039 (64) | 0.006 / 0.025 (98) | 0.004 / 0.016 (142) | - |
| triaxial_2_4__triaxial_2_4_test | 0.172 / 0.596 (74) | 0.039 / 0.291 (94) | 0.015 / 0.091 (92) | 0.008 / 0.038 (78) | 0.005 / 0.025 (168) | - |
| triaxial_2_5__triaxial_2_5_test | 0.120 / 0.507 (118) | 0.039 / 0.239 (90) | 0.018 / 0.098 (66) | 0.015 / 0.075 (104) | 0.009 / 0.052 (128) | - |
| triaxial_3_4__triaxial_3_4_test | 0.096 / 0.399 (102) | 0.050 / 0.255 (94) | 0.029 / 0.120 (64) | 0.015 / 0.071 (104) | 0.009 / 0.046 (140) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| triaxial_123__triaxial_2_5_test | 0.094 / 0.606 (64) | 0.045 / 0.223 (144) | 0.015 / 0.065 (82) | 0.015 / 0.066 (84) | 0.010 / 0.052 (134) | - |
| prolateSpheroid__triaxial_2_5_test | 0.241 / 1.467 (64) | 0.055 / 0.193 (118) | 0.025 / 0.109 (94) | 0.012 / 0.068 (102) | 0.010 / 0.050 (126) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| triaxial_123__triaxial_1p5_2_test | 0.154 / 0.697 (62) | 0.043 / 0.141 (138) | 0.015 / 0.050 (96) | 0.009 / 0.036 (66) | 0.005 / 0.022 (138) | - |
| triaxial_123__triaxial_2_4_test | 0.198 / 0.607 (114) | 0.041 / 0.173 (86) | 0.017 / 0.058 (86) | 0.010 / 0.039 (72) | 0.005 / 0.027 (154) | - |
| triaxial_123__triaxial_3_4_test | 0.183 / 1.217 (104) | 0.058 / 0.215 (114) | 0.033 / 0.147 (76) | 0.017 / 0.067 (80) | 0.009 / 0.040 (132) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.034 / 0.091 (86) | 0.005 / 0.016 (106) | 0.001 / 0.005 (106) | 0.001 / 0.003 (78) | 0.000 / 0.003 (130) | - |
| prolateSpheroid__triaxial_2_4_test | 0.195 / 0.845 (66) | 0.067 / 0.366 (98) | 0.019 / 0.078 (116) | 0.008 / 0.041 (102) | 0.006 / 0.025 (122) | - |
| triaxial_2_5__triaxial_3_4_test | 0.134 / 0.716 (86) | 0.054 / 0.307 (108) | 0.028 / 0.104 (86) | 0.014 / 0.068 (94) | 0.010 / 0.052 (128) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.133 / 0.784 (76) | 0.047 / 0.217 (120) | 0.018 / 0.064 (100) | 0.008 / 0.036 (94) | 0.006 / 0.027 (110) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.051 / 0.326 (106) | 0.007 / 0.026 (118) | 0.002 / 0.007 (64) | 0.002 / 0.005 (78) | 0.001 / 0.005 (134) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.071 / 0.289 (90) | 0.008 / 0.023 (110) | 0.001 / 0.005 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (146) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.085 / 0.411 (78) | 0.020 / 0.086 (100) | 0.009 / 0.040 (86) | 0.005 / 0.022 (90) | 0.004 / 0.020 (154) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.052 / 0.205 (80) | 0.016 / 0.061 (96) | 0.007 / 0.027 (98) | 0.004 / 0.025 (74) | 0.004 / 0.023 (158) | - |
| oblateSpheroid__triaxial_2_5_test | 0.119 / 0.902 (98) | 0.038 / 0.163 (104) | 0.021 / 0.076 (78) | 0.012 / 0.047 (90) | 0.007 / 0.037 (132) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.152 / 0.616 (84) | 0.092 / 0.296 (112) | 0.051 / 0.182 (84) | 0.020 / 0.074 (70) | 0.010 / 0.039 (146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.102 / 0.617 (92) | 0.034 / 0.198 (128) | 0.021 / 0.091 (84) | 0.012 / 0.076 (86) | 0.008 / 0.069 (114) | - |
| prolateSpheroid__triaxial_3_6_test | 0.163 / 0.776 (80) | 0.108 / 0.481 (90) | 0.029 / 0.108 (118) | 0.018 / 0.061 (72) | 0.013 / 0.057 (142) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.040 / 0.074 (86) | 0.008 / 0.013 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (74) | 0.000 / 0.003 (160) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 0.179 / 0.771 (86) | 0.090 / 0.407 (100) | 0.050 / 0.195 (86) | 0.024 / 0.088 (96) | 0.011 / 0.039 (134) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.033 / 0.166 (66) | 0.005 / 0.025 (108) | 0.002 / 0.006 (90) | 0.002 / 0.006 (116) | 0.001 / 0.004 (126) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly_s1.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 1: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_5_test`: triaxial_123 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_5_test`: prolateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4030 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_1p5_2_test`: triaxial_123 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4038 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_4_test`: triaxial_123 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_3_4_test`: triaxial_123 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_1p5_2_test`: oblateSpheroid (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4048 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_4_test`: prolateSpheroid (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_3_4_test`: triaxial_2_5 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_123_test`: triaxial_123_x0p75 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2_x1p5__triaxial_1p5_2_test`: triaxial_1p5_2_x1p5 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__prolateSpheroid_test`: triaxial_123_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_123_test`: oblateSpheroid_x1p5 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_2_5_test`: oblateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_3_4_test`: triaxial_1p5_2 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2p5_3p5_test`: triaxial_123 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_3_6_test`: prolateSpheroid (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test`: oblateSpheroid_x1p5 (target or source) with triaxial_1p5_2_x1p5, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_3_4_test`: triaxial_123_x0p75 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_x1p25_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid_x1p25, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x1p25 | 1.25 : 1.25 : 3.75 | 654 / 572; 0.0005 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| triaxial_1p5_2_x1p5 | 1.5 : 2.25 : 3 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Two-body accuracy of `data/final_c/models/pair_poly_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.081 | 0.397 | 0.096 | 1.07 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.086 / 0.508 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.070 | 0.386 | 0.094 | 0.77 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.071 / 0.361 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.119 | 0.617 | 0.145 | 1.32 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.125 / 0.661 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.146 | 0.853 | 0.176 | 2.30 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.145 / 0.760 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.239 | 1.508 | 0.274 | 3.87 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.242 / 1.421 | 0.052 / 0.391 | 0.0 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.158 | 0.859 | 0.179 | 2.98 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.142 / 0.687 | 0.046 / 0.249 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.109 | 0.686 | 0.152 | 1.09 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.112 / 0.710 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.096 | 0.639 | 0.134 | 0.85 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.083 / 0.556 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.111 | 0.606 | 0.144 | 1.27 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.120 / 0.839 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.092 | 0.492 | 0.114 | 1.10 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.080 / 0.446 | 0.042 / 0.294 | 0.0 % |
| triaxial_123__triaxial_2_5_test | 4024 | 0.243 | 1.306 | 0.286 | 3.47 | 4.23 / 13.78 | 0.053 / 0.353 (508) | 0.255 / 1.257 | 0.051 / 0.360 | 0.0 % |
| prolateSpheroid__triaxial_2_5_test | 4030 | 0.291 | 1.624 | 0.350 | 3.61 | 4.17 / 15.40 | 0.117 / 0.760 (504) | 0.245 / 1.382 | 0.091 / 0.582 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.109 | 0.701 | 0.153 | 0.97 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.091 / 0.622 | 0.004 / 0.024 | 0.0 % |
| triaxial_123__triaxial_1p5_2_test | 4038 | 0.110 | 0.559 | 0.138 | 1.34 | 4.57 / 11.54 | 0.079 / 0.402 (500) | 0.113 / 0.605 | 0.051 / 0.350 | 0.0 % |
| triaxial_123__triaxial_2_4_test | 4042 | 0.143 | 0.765 | 0.171 | 2.04 | 4.18 / 12.46 | 0.124 / 0.411 (512) | 0.181 / 0.786 | 0.052 / 0.375 | 0.0 % |
| triaxial_123__triaxial_3_4_test | 4036 | 0.189 | 0.999 | 0.222 | 3.00 | 3.83 / 12.07 | 0.114 / 0.792 (506) | 0.179 / 0.982 | 0.051 / 0.293 | 0.0 % |
| oblateSpheroid__triaxial_1p5_2_test | 4048 | 0.084 | 0.492 | 0.113 | 0.91 | 5.12 / 11.20 | 0.019 / 0.060 (506) | 0.075 / 0.496 | 0.006 / 0.039 | 0.0 % |
| prolateSpheroid__triaxial_2_4_test | 4020 | 0.195 | 0.944 | 0.231 | 2.30 | 4.13 / 13.13 | 0.100 / 0.512 (504) | 0.158 / 0.906 | 0.081 / 0.531 | 0.0 % |
| triaxial_2_5__triaxial_3_4_test | 4052 | 0.248 | 1.442 | 0.281 | 4.13 | 3.80 / 12.54 | 0.079 / 0.458 (502) | 0.224 / 1.368 | 0.042 / 0.275 | 0.0 % |
| triaxial_123_x0p75__triaxial_123_test | 4026 | 0.137 | 0.636 | 0.166 | 1.87 | 4.16 / 12.62 | 0.075 / 0.477 (500) | 0.121 / 0.689 | 0.051 / 0.336 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.100 | 0.727 | 0.132 | 1.17 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.102 / 0.777 | 0.004 / 0.024 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_test | 4044 | 0.129 | 0.865 | 0.173 | 1.42 | 4.64 / 12.36 | 0.030 / 0.207 (500) | 0.131 / 0.875 | 0.005 / 0.028 | 0.0 % |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 4024 | 0.092 | 0.490 | 0.113 | 1.17 | 4.73 / 10.69 | 0.041 / 0.184 (512) | 0.109 / 0.522 | 0.014 / 0.094 | 0.0 % |
| triaxial_123_x0p75__prolateSpheroid_test | 4020 | 0.151 | 0.748 | 0.196 | 1.73 | 4.67 / 12.89 | 0.048 / 0.254 (508) | 0.131 / 0.765 | 0.044 / 0.288 | 0.0 % |
| oblateSpheroid_x1p5__triaxial_123_test | 4042 | 0.093 | 0.532 | 0.112 | 1.18 | 4.50 / 10.84 | 0.029 / 0.128 (506) | 0.086 / 0.541 | 0.023 / 0.162 | 0.0 % |
| oblateSpheroid__triaxial_2_5_test | 4016 | 0.863 | 3.699 | 0.974 | 6.76 | 4.37 / 15.31 | 0.072 / 0.571 (502) | 0.844 / 3.699 | 0.061 / 0.418 | 0.0 % |
| triaxial_1p5_2__triaxial_3_4_test | 4020 | 0.632 | 3.398 | 0.746 | 5.89 | 4.05 / 14.29 | 0.098 / 0.402 (496) | 0.573 / 3.112 | 0.071 / 0.395 | 0.0 % |
| triaxial_123__triaxial_2p5_3p5_test | 4034 | 0.140 | 0.732 | 0.164 | 1.87 | 4.09 / 11.77 | 0.061 / 0.389 (504) | 0.159 / 0.778 | 0.053 / 0.350 | 0.0 % |
| prolateSpheroid__triaxial_3_6_test | 4024 | 2.016 | 10.437 | 2.266 | 11.31 | 3.88 / 17.30 | 0.100 / 0.494 (502) | 1.912 / 9.613 | 0.058 / 0.340 | 100.0 % |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 4036 | 0.063 | 0.501 | 0.081 | 0.80 | 5.09 / 9.84 | 0.023 / 0.049 (506) | 0.071 / 0.569 | 0.005 / 0.032 | 0.0 % |
| triaxial_123_x0p75__triaxial_3_4_test | 4024 | 0.767 | 4.026 | 0.923 | 8.33 | 3.75 / 14.24 | 0.111 / 0.515 (502) | 0.781 / 4.321 | 0.071 / 0.397 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 4042 | 0.095 | 0.631 | 0.123 | 1.04 | 4.57 / 11.09 | 0.016 / 0.091 (506) | 0.087 / 0.519 | 0.004 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.123 / 0.505 (666) | 0.066 / 0.332 (868) | 0.048 / 0.288 (688) | 0.042 / 0.268 (672) | 0.043 / 0.284 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.096 / 0.437 (642) | 0.068 / 0.385 (962) | 0.048 / 0.309 (710) | 0.036 / 0.258 (674) | 0.039 / 0.249 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.169 / 0.726 (756) | 0.099 / 0.568 (852) | 0.079 / 0.467 (622) | 0.067 / 0.431 (728) | 0.067 / 0.426 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.211 / 1.147 (706) | 0.126 / 0.678 (872) | 0.096 / 0.537 (730) | 0.085 / 0.570 (648) | 0.085 / 0.587 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.330 / 1.906 (704) | 0.214 / 1.409 (898) | 0.174 / 0.993 (634) | 0.152 / 0.905 (676) | 0.158 / 0.971 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.232 / 1.173 (686) | 0.136 / 0.671 (866) | 0.104 / 0.555 (686) | 0.086 / 0.509 (724) | 0.094 / 0.514 (1058) | - |
| prolateSpheroid__prolateSpheroid_test | 0.149 / 0.810 (684) | 0.097 / 0.637 (898) | 0.084 / 0.565 (660) | 0.075 / 0.512 (754) | 0.073 / 0.622 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.130 / 0.790 (650) | 0.100 / 0.597 (936) | 0.061 / 0.451 (680) | 0.037 / 0.361 (738) | 0.033 / 0.322 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.159 / 0.749 (668) | 0.098 / 0.533 (876) | 0.073 / 0.431 (668) | 0.066 / 0.464 (738) | 0.063 / 0.487 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.140 / 0.639 (686) | 0.072 / 0.409 (916) | 0.054 / 0.330 (684) | 0.046 / 0.306 (688) | 0.042 / 0.276 (1058) | - |
| triaxial_123__triaxial_2_5_test | 0.336 / 1.643 (700) | 0.232 / 1.173 (918) | 0.171 / 0.960 (744) | 0.145 / 0.870 (648) | 0.126 / 0.889 (1014) | - |
| prolateSpheroid__triaxial_2_5_test | 0.433 / 2.264 (626) | 0.256 / 1.374 (962) | 0.192 / 1.045 (656) | 0.168 / 0.920 (710) | 0.156 / 1.021 (1076) | - |
| prolateSpheroid__oblateSpheroid_test | 0.139 / 0.752 (702) | 0.112 / 0.722 (952) | 0.084 / 0.608 (668) | 0.064 / 0.537 (632) | 0.050 / 0.463 (1086) | - |
| triaxial_123__triaxial_1p5_2_test | 0.158 / 0.660 (652) | 0.096 / 0.526 (948) | 0.078 / 0.443 (690) | 0.070 / 0.413 (662) | 0.063 / 0.381 (1086) | - |
| triaxial_123__triaxial_2_4_test | 0.204 / 0.937 (684) | 0.132 / 0.698 (850) | 0.098 / 0.603 (728) | 0.083 / 0.502 (668) | 0.079 / 0.542 (1112) | - |
| triaxial_123__triaxial_3_4_test | 0.274 / 1.312 (658) | 0.171 / 0.867 (932) | 0.120 / 0.638 (676) | 0.109 / 0.619 (724) | 0.098 / 0.565 (1046) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.115 / 0.581 (700) | 0.079 / 0.464 (866) | 0.057 / 0.367 (752) | 0.045 / 0.333 (678) | 0.040 / 0.282 (1052) | - |
| prolateSpheroid__triaxial_2_4_test | 0.285 / 1.190 (678) | 0.170 / 0.794 (876) | 0.128 / 0.763 (728) | 0.107 / 0.672 (686) | 0.100 / 0.666 (1052) | - |
| triaxial_2_5__triaxial_3_4_test | 0.349 / 1.857 (678) | 0.226 / 1.237 (864) | 0.178 / 1.106 (688) | 0.153 / 0.975 (744) | 0.154 / 1.045 (1078) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.200 / 0.819 (666) | 0.117 / 0.538 (942) | 0.089 / 0.439 (686) | 0.076 / 0.416 (698) | 0.069 / 0.402 (1034) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.138 / 0.867 (662) | 0.095 / 0.710 (936) | 0.068 / 0.504 (688) | 0.058 / 0.429 (712) | 0.050 / 0.321 (1034) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.174 / 1.086 (716) | 0.117 / 0.782 (888) | 0.089 / 0.586 (688) | 0.092 / 0.652 (726) | 0.088 / 0.647 (1026) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.128 / 0.574 (642) | 0.080 / 0.454 (836) | 0.068 / 0.411 (674) | 0.059 / 0.366 (706) | 0.059 / 0.345 (1166) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.203 / 0.894 (742) | 0.139 / 0.693 (864) | 0.106 / 0.572 (710) | 0.098 / 0.501 (658) | 0.085 / 0.502 (1046) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.136 / 0.645 (664) | 0.079 / 0.502 (938) | 0.059 / 0.381 (692) | 0.053 / 0.326 (632) | 0.059 / 0.354 (1116) | - |
| oblateSpheroid__triaxial_2_5_test | 1.073 / 4.213 (690) | 0.944 / 3.625 (878) | 0.683 / 3.256 (712) | 0.501 / 2.634 (674) | 0.375 / 2.037 (1062) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.844 / 4.269 (672) | 0.611 / 3.192 (918) | 0.474 / 2.430 (608) | 0.449 / 1.730 (676) | 0.349 / 1.356 (1146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.194 / 0.905 (650) | 0.131 / 0.692 (912) | 0.100 / 0.517 (700) | 0.087 / 0.477 (664) | 0.078 / 0.442 (1108) | - |
| prolateSpheroid__triaxial_3_6_test | 2.660 / 12.701 (654) | 2.059 / 10.360 (872) | 1.614 / 8.352 (702) | 1.309 / 7.020 (678) | 1.092 / 5.910 (1118) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.084 / 0.629 (636) | 0.060 / 0.446 (896) | 0.043 / 0.368 (620) | 0.039 / 0.306 (676) | 0.038 / 0.250 (1208) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 1.060 / 5.105 (738) | 0.732 / 3.661 (896) | 0.502 / 2.785 (730) | 0.403 / 2.015 (632) | 0.390 / 1.574 (1028) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.132 / 0.737 (672) | 0.086 / 0.616 (936) | 0.069 / 0.442 (714) | 0.066 / 0.536 (690) | 0.070 / 0.603 (1030) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.032 / 0.127 (70) | 0.004 / 0.014 (140) | 0.001 / 0.004 (90) | 0.001 / 0.002 (76) | 0.000 / 0.002 (126) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.667 (102) | 0.035 / 0.162 (100) | 0.011 / 0.039 (64) | 0.006 / 0.025 (98) | 0.004 / 0.016 (142) | - |
| triaxial_2_4__triaxial_2_4_test | 0.172 / 0.596 (74) | 0.039 / 0.291 (94) | 0.015 / 0.091 (92) | 0.008 / 0.038 (78) | 0.005 / 0.025 (168) | - |
| triaxial_2_5__triaxial_2_5_test | 0.120 / 0.507 (118) | 0.039 / 0.239 (90) | 0.018 / 0.098 (66) | 0.015 / 0.075 (104) | 0.009 / 0.052 (128) | - |
| triaxial_3_4__triaxial_3_4_test | 0.096 / 0.399 (102) | 0.050 / 0.255 (94) | 0.029 / 0.120 (64) | 0.015 / 0.071 (104) | 0.009 / 0.046 (140) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| triaxial_123__triaxial_2_5_test | 0.094 / 0.606 (64) | 0.045 / 0.223 (144) | 0.015 / 0.065 (82) | 0.015 / 0.066 (84) | 0.010 / 0.052 (134) | - |
| prolateSpheroid__triaxial_2_5_test | 0.241 / 1.467 (64) | 0.055 / 0.193 (118) | 0.025 / 0.109 (94) | 0.012 / 0.068 (102) | 0.010 / 0.050 (126) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| triaxial_123__triaxial_1p5_2_test | 0.154 / 0.697 (62) | 0.043 / 0.141 (138) | 0.015 / 0.050 (96) | 0.009 / 0.036 (66) | 0.005 / 0.022 (138) | - |
| triaxial_123__triaxial_2_4_test | 0.198 / 0.607 (114) | 0.041 / 0.173 (86) | 0.017 / 0.058 (86) | 0.010 / 0.039 (72) | 0.005 / 0.027 (154) | - |
| triaxial_123__triaxial_3_4_test | 0.183 / 1.217 (104) | 0.058 / 0.215 (114) | 0.033 / 0.147 (76) | 0.017 / 0.067 (80) | 0.009 / 0.040 (132) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.034 / 0.091 (86) | 0.005 / 0.016 (106) | 0.001 / 0.005 (106) | 0.001 / 0.003 (78) | 0.000 / 0.003 (130) | - |
| prolateSpheroid__triaxial_2_4_test | 0.195 / 0.845 (66) | 0.067 / 0.366 (98) | 0.019 / 0.078 (116) | 0.008 / 0.041 (102) | 0.006 / 0.025 (122) | - |
| triaxial_2_5__triaxial_3_4_test | 0.134 / 0.716 (86) | 0.054 / 0.307 (108) | 0.028 / 0.104 (86) | 0.014 / 0.068 (94) | 0.010 / 0.052 (128) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.133 / 0.784 (76) | 0.047 / 0.217 (120) | 0.018 / 0.064 (100) | 0.008 / 0.036 (94) | 0.006 / 0.027 (110) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.051 / 0.326 (106) | 0.007 / 0.026 (118) | 0.002 / 0.007 (64) | 0.002 / 0.005 (78) | 0.001 / 0.005 (134) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.071 / 0.289 (90) | 0.008 / 0.023 (110) | 0.001 / 0.005 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (146) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.085 / 0.411 (78) | 0.020 / 0.086 (100) | 0.009 / 0.040 (86) | 0.005 / 0.022 (90) | 0.004 / 0.020 (154) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.052 / 0.205 (80) | 0.016 / 0.061 (96) | 0.007 / 0.027 (98) | 0.004 / 0.025 (74) | 0.004 / 0.023 (158) | - |
| oblateSpheroid__triaxial_2_5_test | 0.119 / 0.902 (98) | 0.038 / 0.163 (104) | 0.021 / 0.076 (78) | 0.012 / 0.047 (90) | 0.007 / 0.037 (132) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.152 / 0.616 (84) | 0.092 / 0.296 (112) | 0.051 / 0.182 (84) | 0.020 / 0.074 (70) | 0.010 / 0.039 (146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.102 / 0.617 (92) | 0.034 / 0.198 (128) | 0.021 / 0.091 (84) | 0.012 / 0.076 (86) | 0.008 / 0.069 (114) | - |
| prolateSpheroid__triaxial_3_6_test | 0.163 / 0.776 (80) | 0.108 / 0.481 (90) | 0.029 / 0.108 (118) | 0.018 / 0.061 (72) | 0.013 / 0.057 (142) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.040 / 0.074 (86) | 0.008 / 0.013 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (74) | 0.000 / 0.003 (160) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 0.179 / 0.771 (86) | 0.090 / 0.407 (100) | 0.050 / 0.195 (86) | 0.024 / 0.088 (96) | 0.011 / 0.039 (134) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.033 / 0.166 (66) | 0.005 / 0.025 (108) | 0.002 / 0.006 (90) | 0.002 / 0.006 (116) | 0.001 / 0.004 (126) | - |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly_s2.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 2: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_5_test`: triaxial_123 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_5_test`: prolateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4030 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_1p5_2_test`: triaxial_123 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4038 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_4_test`: triaxial_123 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_3_4_test`: triaxial_123 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_1p5_2_test`: oblateSpheroid (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4048 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_4_test`: prolateSpheroid (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_3_4_test`: triaxial_2_5 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_123_test`: triaxial_123_x0p75 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2_x1p5__triaxial_1p5_2_test`: triaxial_1p5_2_x1p5 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__prolateSpheroid_test`: triaxial_123_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_123_test`: oblateSpheroid_x1p5 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_2_5_test`: oblateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_3_4_test`: triaxial_1p5_2 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2p5_3p5_test`: triaxial_123 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_3_6_test`: prolateSpheroid (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test`: oblateSpheroid_x1p5 (target or source) with triaxial_1p5_2_x1p5, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_3_4_test`: triaxial_123_x0p75 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_x1p25_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid_x1p25, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_1p5_3 | 1 : 1.5 : 3 | 660 / 560; 0.0041 / 0.0030 | 1400 / 1190; 0.0010 / 0.0006 |
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |
| triaxial_2_5 | 1 : 2 : 5 | 1056 / 896; 0.0262 / 0.0922 | 2239 / 1904; 0.0019 / 0.0079 |
| triaxial_3_4 | 1 : 3 : 4 | 1196 / 1014; 0.0248 / 0.0034 | 2536 / 2156; 0.0034 / 0.0055 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x1p25 | 1.25 : 1.25 : 3.75 | 654 / 572; 0.0005 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| triaxial_1p5_2_x1p5 | 1.5 : 2.25 : 3 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_2p5_3p5 | 1 : 2.5 : 3.5 | 907 / 770; 0.0314 / 0.0978 | 1924 / 1635; 0.0090 / 0.0310 |
| triaxial_3_6 | 1 : 3 : 6 | 1748 / 1483; 0.0462 / 0.1752 | 3708 / 3152; 0.0129 / 0.0547 |

#### Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.48 (4.47 / 4.81; 1.22) | 2.71 (2.73 / 2.37; 1.02) | 1.80 (1.81 / 1.69; 0.72) | 0.012 (0.010 / 0.032; 0.001) (1) |
| 0.05 | 200 | 10 | 7.35 (7.35 / 7.89; 2.17) | 5.18 (5.20 / 4.79; 1.87) | 3.24 (3.25 / 3.07; 1.17) | 0.015 (0.013 / 0.041; 0.001) (1) |
| 0.075 | 200 | 10 | 9.77 (9.75 / 10.74; 3.30) | 7.38 (7.37 / 7.70; 2.90) | 4.15 (4.14 / 4.62; 1.62) | 0.029 (0.026 / 0.087; 0.002) (1) |
| 0.1 | 200 | 10 | 14.38 (14.45 / 13.27; 4.11) | 11.13 (11.19 / 10.00; 3.64) | 6.10 (6.12 / 5.81; 1.82) | 0.015 (0.013 / 0.046; 0.001) (1) |
| 0.15 | 200 | 10 | 19.62 (19.63 / 21.15; 6.06) | 15.95 (15.97 / 16.87; 5.42) | 9.70 (9.73 / 9.78; 2.58) | 0.053 (0.041 / 0.142; 0.003) (1) |
| 0.2 | 200 | 8 | 26.03 (26.00 / 28.27; 8.07) | 21.74 (21.73 / 23.20; 7.26) | 24.60 (24.69 / 22.75; 4.70) | 0.058 (0.049 / 0.175; 0.007) (1) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configurations**: N in [200] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |

#### Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.36 (7.33 / 8.08; 2.70) | 4.72 (4.72 / 4.91; 1.97) | 2.45 (2.42 / 3.08; 0.83) | 0.024 (0.015 / 0.086; 0.003) (1) |
| 0.05 | 100 | 5 | 6.99 (6.95 / 8.30; 2.45) | 4.69 (4.69 / 5.01; 1.96) | 2.64 (2.63 / 3.07; 0.90) | 0.008 (0.007 / 0.024; 0.002) (1) |
| 0.05 | 200 | 5 | 7.22 (7.21 / 7.49; 2.14) | 5.06 (5.08 / 4.60; 1.83) | 3.13 (3.14 / 3.00; 1.16) | not measured |
| 0.05 | 300 | 5 | 7.78 (7.80 / 7.60; 2.13) | 5.54 (5.57 / 4.83; 1.89) | 3.65 (3.68 / 3.19; 1.32) | not measured |
| 0.1 | 50 | 5 | 11.63 (11.55 / 13.02; 4.33) | 8.34 (8.32 / 8.84; 3.27) | 4.21 (4.18 / 4.75; 1.16) | 0.066 (0.048 / 0.200; 0.002) (1) |
| 0.1 | 100 | 5 | 14.07 (14.07 / 14.39; 4.39) | 9.86 (9.88 / 9.59; 3.68) | 5.09 (5.09 / 5.24; 1.49) | 0.015 (0.014 / 0.026; 0.002) (1) |
| 0.1 | 200 | 5 | 13.45 (13.47 / 13.06; 4.01) | 10.47 (10.50 / 9.80; 3.55) | 5.83 (5.83 / 5.74; 1.77) | not measured |
| 0.1 | 300 | 5 | 11.85 (11.81 / 13.74; 4.04) | 9.52 (9.50 / 10.52; 3.68) | 5.48 (5.46 / 6.14; 2.24) | not measured |
| 0.15 | 50 | 5 | 19.59 (19.56 / 20.14; 6.56) | 14.77 (14.79 / 14.73; 5.15) | 5.67 (5.58 / 7.06; 1.47) | 0.070 (0.063 / 0.139; 0.005) (1) |
| 0.15 | 100 | 5 | 18.73 (18.74 / 19.65; 6.00) | 14.96 (14.97 / 15.51; 5.04) | 6.66 (6.61 / 8.20; 1.61) | 0.014 (0.012 / 0.058; 0.002) (1) |
| 0.15 | 200 | 5 | 17.70 (17.67 / 20.88; 6.12) | 14.53 (14.53 / 16.54; 5.48) | 9.24 (9.26 / 10.03; 2.62) | not measured |
| 0.15 | 300 | 5 | 20.37 (20.36 / 20.90; 5.90) | 16.99 (17.01 / 16.69; 5.41) | 11.30 (11.32 / 10.93; 3.05) | not measured |
| 0.2 | 50 | 4 | 19.35 (19.15 / 26.59; 8.04) | 14.89 (14.72 / 20.55; 6.33) | 5.88 (5.74 / 9.61; 1.56) | 0.060 (0.056 / 0.097; 0.008) (1) |
| 0.2 | 100 | 4 | 19.89 (19.72 / 26.40; 8.31) | 16.24 (16.11 / 21.40; 7.12) | 8.48 (8.38 / 12.32; 2.32) | 0.027 (0.021 / 0.144; 0.004) (1) |
| 0.2 | 200 | 4 | 28.72 (28.78 / 28.80; 8.21) | 24.15 (24.25 / 23.33; 7.41) | 27.16 (27.30 / 24.36; 5.13) | not measured |
| 0.2 | 300 | 5 | 27.18 (27.16 / 29.12; 7.80) | 22.92 (22.92 / 23.94; 7.18) | 28.85 (28.94 / 26.56; 4.53) | not measured |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: pair of triaxial_123, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 89.7, 246 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.09 | 0.094 | 0.31 |
| + two-body | 1500 | 0.02 | 0.043 | 0.24 |
| + many-body | 1500 | 0.02 | 0.043 | 0.24 |
| MFS Xfine (the truth's own error) | 1500 | 0.005 | 0.0104 | 0.283 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: triaxial_123, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Dynamics: ring of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 323 steps, fell 46.4, 279 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 81 | 4.77 | 0.761 | 15.85 |
| + two-body | 78 | 1.75 | 0.333 | 9.60 |
| + many-body | 125 | 0.97 | 0.365 | 4.68 |
| MFS Xfine (the truth's own error) | 323 | 0.002 | 0.0020 | 0.111 |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |

#### Structural checks, 16 particles of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.4e-16 | 1.1054 | 8.2e-16 | 9.44 |
| + two-body | 1.1e-16 | 0.1785 | 5.8e-16 | 5.65 |
| + many-body | 1.1e-16 | 0.9963 | 5.8e-16 | 2.57 |
| MFS fine (the truth) | 8.4e-05 | 1 | | 0 |
| MFS Xfine | 1.8e-05 | 1.0000 | | 0.007 (= the error of the fine truth) |

MFS smallest eigenvalue 1.6718e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configuration**: ONE random suspension, N = 16, shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |

#### Positive definiteness of the operator, triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5

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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -7.981 | 0.66 | triaxial_1p5_2, prolateSpheroid | 2.92 | 1.051 | 4.96e-03 / 2.21e-03 (0.445) | 0.573, 0.569 (13 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 10 | -9.004 | 0.49 | oblateSpheroid_x1p5, oblateSpheroid_x1p5 | 3.35 | 1.059 | 1.88e-03 / 1.07e-03 (0.566) | -0.498, 0.697 (2 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

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

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.12 (7.06 / 8.08) | 4.43 (4.44 / 4.26) | 2.53 (2.52 / 2.64) | 1.73 (1.76 / 1.28) | 1.71 (1.73 / 1.21) |
| 0.1 | 64 | 3 | 12.57 (12.41 / 16.59) | 9.40 (9.36 / 10.60) | 4.26 (4.21 / 5.57) | 2.50 (2.51 / 2.21) | 2.28 (2.29 / 1.76) |
| 0.2 | 64 | 2 | 21.21 (21.06 / 26.61) | 17.11 (16.99 / 21.51) | 6.51 (6.35 / 10.44) | 3.77 (3.76 / 4.31) | 3.13 (3.16 / 2.44) |

##### Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configurations**: N in [64], shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |

