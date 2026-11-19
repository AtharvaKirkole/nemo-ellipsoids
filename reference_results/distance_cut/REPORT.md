# Accuracy of the two-body and full-body models, with the error of MFS itself

Built 2026-11-15 11:39 by `report.py` from `results_v2/<case>/`.  All numbers are % errors against MFS on fine clouds unless a column says otherwise.  trans / rot = translation / rotation.

How to read the MFS columns: a model error is only meaningful down to the error of the truth it is compared with.  `MFS fine vs Xfine` is the same test solved with both cloud resolutions, in the same metric; `reciprocity` is how far the raw MFS blocks are from the symmetry the exact ones have.  Where a model error is close to these, the model is at the floor of its labels and cannot be shown to be better.

## 1. Two-body (cells 1A-1D spheroid form, 3A-3D triaxial form)

Pair test sets (unseen seeds), one random unit force and torque on the source, PRMSE of the target's velocity.  Ranges are over the test sets of the pairings the model was trained on.

| cell | case | trained pairings tested | model: trans / rot | MFS fine vs Xfine: trans / rot | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | far field alone: trans / rot | pairings never trained on: trans / rot | mean trans over training seeds |
|---|---|---|---|---|---|---|---|---|---|
| 1A | 1A_pro | 1 | 0.033 / 0.310 | 0.026 / 0.237 | 0.034 / 0.349 | 0.005 / 0.024 | 4.695 / 11.482 | none | one seed |
| 1A | 1A_obl | 1 | 0.019 / 0.158 | 0.013 / 0.036 | 0.022 / 0.168 | 0.003 / 0.019 | 4.967 / 11.383 | none | one seed |
| 1B | 1B | 7 | 0.029-0.153 / 0.093-0.564 | 0.004-0.064 / 0.012-0.393 | 0.028-0.162 / 0.090-0.650 | 0.002-0.072 / 0.010-0.375 | 4.067-5.687 / 10.600-14.017 | 3: 0.129-0.955 / 0.472-3.679 | one seed |
| 1C | 1C | 3 | 0.028-0.070 / 0.164-0.433 | 0.013-0.026 / 0.036-0.237 | 0.030-0.070 / 0.181-0.452 | 0.003-0.005 / 0.019-0.024 | 4.695-4.967 / 11.260-11.482 | none | one seed |
| 1D | 1D | 22 | 0.026-0.200 / 0.080-0.812 | 0.004-0.133 / 0.012-0.462 | 0.027-0.183 / 0.082-0.783 | 0.002-0.117 / 0.010-0.602 | 3.531-5.687 / 10.478-14.217 | 6: 0.107-1.854 / 0.372-4.909 | one seed |
| 3A | 3A | 1 | 0.061 / 0.296 | 0.078 / 0.456 | 0.063 / 0.352 | 0.041 / 0.300 | 4.325 / 11.489 | none | one seed |
| 3B | 3B | 6 | 0.073-0.216 / 0.364-1.249 | 0.020-0.105 / 0.099-0.504 | 0.069-0.220 / 0.370-1.306 | 0.009-0.066 / 0.054-0.401 | 3.649-5.187 / 10.762-14.752 | 2: 0.161-1.907 / 0.792-12.369 | one seed |
| 3C | 3C | 5 | 0.080-0.125 / 0.378-0.807 | 0.013-0.078 / 0.034-0.456 | 0.079-0.133 / 0.424-0.799 | 0.003-0.053 / 0.018-0.375 | 4.325-4.941 / 11.240-11.886 | 1: 1.553 / 8.890 | one seed |
| 3D | 3D | 25 | 0.070-0.323 / 0.383-1.763 | 0.013-0.164 / 0.034-1.050 | 0.069-0.290 / 0.367-1.631 | 0.003-0.109 / 0.018-0.589 | 3.649-5.187 / 10.228-15.353 | 7: 0.063-1.773 / 0.519-11.864 | one seed |

## 2. Full body (cells 2A-2D spheroid form, 4A-4D triaxial form)

Suspensions in unbounded fluid, random unit forces and torques on every particle, PRMSE of all six velocity components: far field -> + two-body -> + many-body (translation / rotation of the last).  Whole matrix = Frobenius error of the full operator's grand mobility matrix on one small suspension (16 particles in the full runs).  Ring = centre-of-mass error (% of the distance fallen) of 5 particles sedimenting.

| cell | case | N | phi: far -> two-body -> many-body (trans / rot) | MFS fine vs Xfine | phi: far -> two-body -> many-body (trans / rot) | MFS fine vs Xfine | whole matrix vs MFS | MFS fine vs Xfine (matrix) | positive definite | ring: far -> two-body -> many-body | MFS fine vs Xfine (ring) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2A | 1A_pro | 200 | 0.1: 13.85 -> 10.98 -> 5.16 (5.17 / 5.24) | 0.009 (0.007 / 0.038) | 0.2: 27.33 -> 23.44 -> 8.47 (8.47 / 9.32) | 0.014 (0.011 / 0.075) | 1.63 | 0.013 | yes | 6.01 -> 1.99 -> 0.81 | 0.003 |
| 2A | 1A_obl | 200 | 0.1: 12.95 -> 10.25 -> 4.68 (4.66 / 5.56) | 0.010 (0.009 / 0.024) | 0.2: 21.83 -> 18.70 -> 7.21 (7.16 / 10.37) | 0.015 (0.014 / 0.045) | 1.90 | 0.004 | yes | 5.41 -> 2.09 -> 0.63 | 0.001 |
| 2B | 1B | 200 | 0.1: 13.72 -> 10.81 -> 4.32 (4.36 / 3.98) | 0.006 (0.005 / 0.014) | 0.2: 24.52 -> 21.02 -> 9.16 (9.26 / 9.00) | 0.015 (0.011 / 0.037) | 1.63 | 0.002 | yes | 5.42 -> 1.80 -> 0.51 | 0.001 |
| 2C | 1C | 200 | 0.1: 13.71 -> 11.06 -> 5.44 (5.44 / 5.33) | 0.011 (0.010 / 0.029) | 0.2: 23.59 -> 20.14 -> 7.34 (7.29 / 9.58) | 0.009 (0.006 / 0.089) | 2.50 | 0.014 | **NO** | 6.24 -> 2.26 -> 0.71 | 0.002 |
| 2D | 1D | 200 | 0.1: 14.39 -> 10.85 -> 6.31 (6.53 / 4.13) | 0.034 (0.032 / 0.050) | 0.2: 23.17 -> 19.24 -> 9.49 (9.63 / 7.50) | not measured | 2.84 | 0.020 | yes | 4.14 -> 0.63 -> 0.29 | 0.004 |
| 4A | 3A | 200 | 0.1: 14.34 -> 11.69 -> 5.57 (5.54 / 7.28) | 0.036 (0.033 / 0.130) | 0.2: 26.45 -> 22.99 -> 8.67 (8.61 / 12.83) | 0.093 (0.080 / 0.393) | 1.60 | 0.014 | yes | 6.14 -> 2.41 -> 0.09 | 0.014 |
| 4B | 3B | 200 | 0.1: 15.01 -> 12.24 -> 6.41 (6.38 / 8.87) | 0.063 (0.058 / 0.283) | 0.2: 23.62 -> 20.42 -> 9.08 (9.02 / 16.38) | 0.101 (0.091 / 0.426) | 1.93 | 0.021 | yes | 6.59 -> 2.60 -> 1.16 | 0.007 |
| 4C | 3C | 200 | 0.1: 13.82 -> 11.08 -> 4.83 (4.81 / 5.54) | 0.034 (0.030 / 0.120) | 0.2: 25.10 -> 21.63 -> 7.51 (7.44 / 10.58) | 0.060 (0.048 / 0.251) | 1.99 | 0.019 | yes | 5.25 -> 2.09 -> 0.37 | 0.006 |
| 4D | 3D | 200 | 0.1: 14.38 -> 11.14 -> 5.59 (5.60 / 5.54) | 0.015 (0.013 / 0.046) | 0.2: 26.03 -> 21.77 -> 12.91 (12.92 / 13.64) | 0.058 (0.049 / 0.175) | 2.62 | 0.007 | yes | 4.77 -> 1.74 -> 0.92 | 0.002 |

## 3. Every result, with its conditions

### Case 1A_pro (cells 1A and 2A): spheroid form, one shape: prolate 1:1:3

#### MFS clouds against the exact isolated ellipsoid

For each shape and resolution: boundary nodes / Stokeslet sources, then the largest error (%) of the three translation and of the three rotation mobilities of ONE particle against the exact values (Oberbeck 1876; Jeffery 1922).  This is the absolute accuracy of the truth for a particle with no neighbour.

| shape | semi-axes | coarse: nodes / sources; exact-mobility error trans / rot % | medium: nodes / sources; exact-mobility error trans / rot % | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 150 / 131; 0.0325 / 0.1955 | 348 / 304; 0.0230 / 0.0079 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Two-body accuracy of `data/final/models/pair_pro.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.033 | 0.310 | 0.058 | 0.37 | 4.70 / 11.48 | 0.026 / 0.237 (512) | 0.034 / 0.349 | 0.005 / 0.024 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.048 / 0.346 (682) | 0.026 / 0.299 (894) | 0.023 / 0.293 (690) | 0.024 / 0.230 (680) | 0.022 / 0.249 (988) | 0.029 / 0.311 (162) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.047 / 0.375 (84) | 0.006 / 0.026 (102) | 0.002 / 0.006 (80) | 0.002 / 0.006 (86) | 0.001 / 0.005 (138) | 0.001 / 0.005 (22) |

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
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
| 0.025 | 200 | 10 | 4.32 (4.33 / 4.28; 1.19) | 2.83 (2.86 / 2.41; 1.00) | 1.87 (1.89 / 1.55; 0.73) | 0.004 (0.004 / 0.011; 0.000) (1) |
| 0.05 | 200 | 10 | 7.00 (7.01 / 7.29; 2.19) | 5.12 (5.14 / 5.02; 1.91) | 2.86 (2.87 / 2.85; 1.17) | 0.009 (0.006 / 0.029; 0.000) (1) |
| 0.075 | 200 | 10 | 11.45 (11.48 / 11.70; 3.32) | 8.94 (8.96 / 8.89; 2.93) | 4.40 (4.42 / 4.31; 1.50) | 0.021 (0.017 / 0.048; 0.001) (1) |
| 0.1 | 200 | 10 | 13.85 (13.86 / 14.37; 4.09) | 10.98 (11.00 / 11.24; 3.63) | 5.16 (5.17 / 5.24; 1.65) | 0.009 (0.007 / 0.038; 0.001) (1) |
| 0.15 | 200 | 10 | 18.56 (18.49 / 22.71; 6.05) | 15.65 (15.59 / 19.11; 5.44) | 5.98 (5.95 / 7.46; 2.07) | 0.008 (0.006 / 0.034; 0.001) (1) |
| 0.2 | 200 | 10 | 27.33 (27.30 / 30.80; 7.74) | 23.44 (23.40 / 26.55; 7.00) | 8.47 (8.47 / 9.32; 2.56) | 0.014 (0.011 / 0.075; 0.003) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
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
| 0.05 | 50 | 5 | 7.27 (7.27 / 7.64; 2.40) | 4.87 (4.87 / 5.13; 1.75) | 2.17 (2.14 / 2.67; 0.75) | 0.009 (0.009 / 0.012; 0.001) (1) |
| 0.05 | 100 | 5 | 7.38 (7.38 / 7.58; 2.48) | 5.30 (5.29 / 5.63; 2.02) | 2.67 (2.65 / 3.09; 0.97) | 0.012 (0.011 / 0.019; 0.001) (1) |
| 0.05 | 200 | 5 | 6.81 (6.82 / 7.39; 2.21) | 5.01 (5.05 / 4.92; 1.92) | 2.87 (2.89 / 2.80; 1.21) | not measured |
| 0.05 | 300 | 5 | 7.34 (7.35 / 7.49; 2.19) | 5.55 (5.58 / 5.11; 1.97) | 3.39 (3.42 / 2.92; 1.36) | not measured |
| 0.1 | 50 | 5 | 11.94 (11.96 / 12.24; 4.59) | 8.89 (8.90 / 9.26; 3.56) | 3.23 (3.18 / 3.99; 1.25) | 0.012 (0.012 / 0.020; 0.001) (1) |
| 0.1 | 100 | 5 | 14.77 (14.92 / 13.65; 4.05) | 11.00 (11.12 / 10.31; 3.38) | 4.72 (4.76 / 4.51; 1.19) | 0.010 (0.009 / 0.014; 0.001) (1) |
| 0.1 | 200 | 5 | 12.24 (12.18 / 14.36; 4.10) | 10.00 (9.98 / 11.08; 3.63) | 4.75 (4.74 / 5.22; 1.60) | not measured |
| 0.1 | 300 | 5 | 11.12 (11.02 / 15.05; 4.20) | 9.16 (9.09 / 12.22; 3.85) | 4.41 (4.38 / 5.65; 2.08) | not measured |
| 0.15 | 50 | 5 | 17.91 (17.85 / 19.73; 6.11) | 13.93 (13.86 / 15.38; 4.78) | 4.08 (3.95 / 6.08; 1.38) | 0.015 (0.013 / 0.034; 0.002) (1) |
| 0.15 | 100 | 5 | 15.59 (15.42 / 21.18; 5.99) | 12.71 (12.56 / 17.60; 5.07) | 4.07 (3.99 / 6.41; 1.51) | 0.013 (0.008 / 0.061; 0.001) (1) |
| 0.15 | 200 | 5 | 18.65 (18.59 / 22.30; 6.12) | 15.65 (15.60 / 18.79; 5.51) | 6.02 (6.00 / 7.29; 2.12) | not measured |
| 0.15 | 300 | 5 | 16.92 (16.83 / 21.60; 5.89) | 14.58 (14.51 / 18.43; 5.42) | 6.37 (6.35 / 7.47; 2.53) | not measured |
| 0.2 | 50 | 5 | 24.26 (24.11 / 27.41; 7.96) | 19.59 (19.47 / 21.99; 6.35) | 5.50 (5.38 / 7.26; 1.26) | 0.038 (0.035 / 0.072; 0.003) (1) |
| 0.2 | 100 | 5 | 21.82 (21.59 / 28.88; 7.38) | 18.21 (18.04 / 24.06; 6.29) | 5.32 (5.20 / 8.39; 1.83) | 0.014 (0.012 / 0.051; 0.003) (1) |
| 0.2 | 200 | 5 | 26.35 (26.25 / 31.47; 7.81) | 22.80 (22.70 / 27.35; 7.06) | 8.02 (7.99 / 9.48; 2.57) | not measured |
| 0.2 | 300 | 5 | 29.85 (29.78 / 31.96; 7.57) | 26.18 (26.14 / 27.43; 6.98) | 10.91 (10.95 / 9.91; 3.08) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
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
| + two-body | 1500 | 0.00 | 0.007 | 0.05 |
| + many-body | 1500 | 0.00 | 0.007 | 0.05 |
| MFS Xfine (the truth's own error) | 1500 | 0.003 | 0.0060 | 0.040 |

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolateSpheroid, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

#### Dynamics: ring of prolateSpheroid, prolateSpheroid, prolateSpheroid, prolateSpheroid, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 131 steps, fell 20.8, 106 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 46 | 6.01 | 0.642 | 0.00 |
| + two-body | 47 | 1.99 | 0.307 | 0.00 |
| + many-body | 131 | 0.81 | 0.457 | 0.01 |
| MFS Xfine (the truth's own error) | 131 | 0.003 | 0.0021 | 0.007 |

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
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
| + two-body | 9.1e-17 | 0.4506 | 5.4e-16 | 4.43 |
| + many-body | 9.7e-17 | 1.0230 | 5.5e-16 | 1.63 |
| MFS fine (the truth) | 3.7e-05 | 1 | | 0 |
| MFS Xfine | 3.6e-06 | 0.9904 | | 0.013 (= the error of the fine truth) |

MFS smallest eigenvalue 1.6006e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
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
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.031 / 0.463 | 20 of 20; 0.337 / 0.677 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 11 of 20; -0.693 / 0.010 | 20 of 20; 0.195 / 0.423 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 9 of 20; -0.391 / -0.037 | 20 of 20; 0.290 / 0.420 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 4 of 20; -1.201 / -0.434 | 20 of 20; 0.151 / 0.414 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.120 / -1.118 | 19 of 20; -0.064 / 0.289 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.315 / -1.333 | 13 of 20; -0.325 / 0.122 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.972 / -0.977 | 18 of 20; -0.042 / 0.286 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.411 / -2.048 | 14 of 20; -0.485 / 0.088 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.050 / -2.545 | 0 of 20; -1.464 / -1.084 |
| 0.2 | 16 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -3.653 / -1.927 | 14 of 19; -0.167 / 0.137 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.056 / -3.317 | 5 of 20; -0.390 / -0.085 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.676 / -3.977 | 0 of 20; -1.876 / -1.533 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 17 | -5.056 | 0.67 | prolateSpheroid, prolateSpheroid | 2.27 | 1.106 | 3.88e-03 / 2.35e-03 (0.604) | 0.320, 0.468 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 17 | -1.876 | 0.05 | prolateSpheroid, prolateSpheroid | 9.00 | 4.045 | 5.58e-03 / 5.58e-03 (1.000) | 0.667, 0.603 (9 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.979 / 1.000 | 1.052, 2.35 |

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 8.54 (8.69 / 6.55) | 5.48 (5.57 / 4.44) | 2.53 (2.56 / 2.23) | 1.70 (1.74 / 1.04) | 1.64 (1.69 / 0.99) |
| 0.1 | 64 | 3 | 13.28 (13.27 / 14.44) | 10.15 (10.12 / 11.76) | 3.52 (3.49 / 4.53) | 2.30 (2.33 / 2.02) | 2.23 (2.26 / 1.75) |
| 0.2 | 64 | 3 | 18.62 (18.29 / 29.24) | 14.98 (14.69 / 24.25) | 3.83 (3.65 / 8.35) | 2.64 (2.60 / 3.99) | 1.94 (1.94 / 2.02) |

##### Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
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

#### Two-body accuracy of `data/final/models/pair_obl.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.019 | 0.158 | 0.030 | 0.24 | 4.97 / 11.38 | 0.013 / 0.036 (512) | 0.022 / 0.168 | 0.003 / 0.019 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.029 / 0.187 (668) | 0.015 / 0.146 (956) | 0.009 / 0.124 (734) | 0.009 / 0.125 (720) | 0.011 / 0.151 (984) | 0.017 / 0.052 (34) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.025 / 0.060 (66) | 0.008 / 0.017 (112) | 0.001 / 0.005 (110) | 0.001 / 0.003 (76) | 0.001 / 0.003 (142) | - |

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
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
| 0.025 | 200 | 10 | 4.58 (4.56 / 5.17; 1.13) | 2.90 (2.90 / 2.86; 0.96) | 1.87 (1.87 / 1.74; 0.72) | 0.002 (0.002 / 0.004; 0.000) (1) |
| 0.05 | 200 | 10 | 6.93 (6.89 / 8.87; 2.16) | 5.01 (5.00 / 6.04; 1.88) | 2.96 (2.96 / 3.34; 1.20) | 0.010 (0.009 / 0.023; 0.001) (1) |
| 0.075 | 200 | 10 | 10.13 (10.06 / 13.11; 3.20) | 7.73 (7.69 / 9.52; 2.84) | 3.76 (3.74 / 4.59; 1.57) | 0.014 (0.013 / 0.027; 0.000) (1) |
| 0.1 | 200 | 10 | 12.95 (12.87 / 16.18; 4.00) | 10.25 (10.18 / 12.71; 3.57) | 4.68 (4.66 / 5.56; 1.78) | 0.010 (0.009 / 0.024; 0.001) (1) |
| 0.15 | 200 | 10 | 19.77 (19.67 / 25.46; 5.98) | 16.61 (16.52 / 21.27; 5.39) | 6.61 (6.58 / 8.15; 2.25) | 0.014 (0.013 / 0.038; 0.001) (1) |
| 0.2 | 200 | 10 | 21.83 (21.58 / 34.96; 7.63) | 18.70 (18.49 / 30.16; 6.91) | 7.21 (7.16 / 10.37; 2.68) | 0.015 (0.014 / 0.045; 0.002) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
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
| 0.05 | 50 | 5 | 7.94 (7.88 / 9.64; 2.48) | 5.21 (5.16 / 6.27; 1.81) | 2.20 (2.16 / 3.06; 0.77) | 0.006 (0.006 / 0.012; 0.001) (1) |
| 0.05 | 100 | 5 | 6.64 (6.57 / 8.70; 2.39) | 4.67 (4.64 / 5.76; 1.97) | 2.42 (2.40 / 2.92; 0.98) | 0.003 (0.002 / 0.010; 0.000) (1) |
| 0.05 | 200 | 5 | 7.37 (7.34 / 9.05; 2.18) | 5.35 (5.34 / 6.25; 1.90) | 3.12 (3.12 / 3.34; 1.23) | not measured |
| 0.05 | 300 | 5 | 7.30 (7.25 / 8.87; 2.06) | 5.50 (5.49 / 6.02; 1.85) | 3.44 (3.45 / 3.25; 1.33) | not measured |
| 0.1 | 50 | 5 | 12.29 (12.17 / 15.08; 3.94) | 8.74 (8.63 / 11.15; 3.01) | 3.38 (3.34 / 4.29; 1.24) | 0.008 (0.008 / 0.017; 0.000) (1) |
| 0.1 | 100 | 5 | 11.58 (11.50 / 15.40; 4.02) | 8.83 (8.75 / 12.17; 3.37) | 3.63 (3.59 / 5.18; 1.27) | 0.015 (0.014 / 0.029; 0.001) (1) |
| 0.1 | 200 | 5 | 12.55 (12.45 / 16.35; 3.94) | 9.97 (9.90 / 12.56; 3.51) | 4.48 (4.46 / 5.50; 1.76) | not measured |
| 0.1 | 300 | 5 | 12.05 (11.96 / 15.94; 3.94) | 9.97 (9.91 / 12.54; 3.60) | 5.04 (5.02 / 5.82; 2.09) | not measured |
| 0.15 | 50 | 5 | 14.69 (14.46 / 22.95; 5.78) | 11.26 (11.06 / 18.42; 4.51) | 3.51 (3.43 / 6.28; 1.62) | 0.013 (0.011 / 0.041; 0.002) (1) |
| 0.15 | 100 | 5 | 16.39 (16.21 / 23.34; 5.93) | 13.41 (13.27 / 18.99; 5.06) | 4.63 (4.57 / 6.91; 1.63) | 0.020 (0.019 / 0.035; 0.002) (1) |
| 0.15 | 200 | 5 | 17.80 (17.62 / 24.85; 6.06) | 15.01 (14.87 / 20.77; 5.48) | 5.95 (5.91 / 7.74; 2.34) | not measured |
| 0.15 | 300 | 5 | 21.70 (21.65 / 25.25; 5.82) | 18.48 (18.44 / 21.35; 5.36) | 8.32 (8.34 / 7.97; 2.74) | not measured |
| 0.2 | 50 | 5 | 23.94 (23.63 / 32.91; 7.93) | 18.91 (18.64 / 26.48; 6.34) | 5.11 (4.97 / 8.22; 1.43) | 0.008 (0.007 / 0.026; 0.001) (1) |
| 0.2 | 100 | 5 | 21.46 (21.15 / 34.64; 7.68) | 17.56 (17.27 / 29.47; 6.60) | 5.55 (5.44 / 9.72; 1.85) | 0.020 (0.019 / 0.045; 0.002) (1) |
| 0.2 | 200 | 5 | 19.96 (19.72 / 34.72; 7.59) | 17.25 (17.03 / 30.59; 6.87) | 6.47 (6.42 / 10.30; 2.62) | not measured |
| 0.2 | 300 | 5 | 24.77 (24.56 / 37.93; 7.57) | 21.57 (21.39 / 32.63; 7.00) | 9.22 (9.20 / 11.42; 3.34) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 110.2, 257 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.06 | 0.074 | 2.51 |
| + two-body | 1500 | 0.00 | 0.001 | 0.01 |
| + many-body | 1500 | 0.00 | 0.001 | 0.01 |
| MFS Xfine (the truth's own error) | 1500 | 0.000 | 0.0004 | 0.008 |

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: oblateSpheroid, oblateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

#### Dynamics: ring of oblateSpheroid, oblateSpheroid, oblateSpheroid, oblateSpheroid, oblateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 186 steps, fell 27.7, 168 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 81 | 5.41 | 0.840 | 15.02 |
| + two-body | 98 | 2.09 | 0.553 | 11.13 |
| + many-body | 142 | 0.63 | 0.388 | 5.44 |
| MFS Xfine (the truth's own error) | 186 | 0.001 | 0.0002 | 0.004 |

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
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
| + two-body | 8.2e-17 | 0.2562 | 5.5e-16 | 5.46 |
| + many-body | 8.6e-17 | 0.9259 | 5.8e-16 | 1.90 |
| MFS fine (the truth) | 2.5e-05 | 1 | | 0 |
| MFS Xfine | 6.2e-06 | 0.9985 | | 0.004 (= the error of the fine truth) |

MFS smallest eigenvalue 3.3442e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
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
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 16 of 20; -0.184 / 0.365 | 20 of 20; 0.198 / 0.734 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 15 of 20; -0.456 / 0.229 | 20 of 20; 0.189 / 0.514 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 3 of 20; -0.772 / -0.124 | 20 of 20; 0.156 / 0.340 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -1.113 / -0.348 | 20 of 20; 0.262 / 0.537 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.178 / -0.596 | 19 of 20; -0.002 / 0.424 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.541 / -0.935 | 17 of 20; -0.099 / 0.138 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.542 / -0.650 | 20 of 20; 0.206 / 0.389 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.079 / -1.411 | 20 of 20; 0.035 / 0.223 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.513 / -1.688 | 0 of 20; -1.339 / -0.891 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.413 / -1.572 | 17 of 20; -0.068 / 0.178 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.099 / -2.236 | 15 of 20; -0.203 / 0.085 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.248 / -2.894 | 0 of 20; -1.792 / -1.513 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 1 | -3.248 | 0.64 | oblateSpheroid, oblateSpheroid | 3.34 | 1.102 | 6.16e-03 / 3.87e-03 (0.629) | 0.560, 0.607 (14 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 7 | -1.792 | 0.04 | oblateSpheroid, oblateSpheroid | 4.66 | 1.660 | 6.92e-03 / 6.89e-03 (0.995) | 0.761, 0.844 (8 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.996 / 1.000 | 1.052, 3.56 |

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
- **Configurations**: N in [16, 50, 100], shapes oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.88 (7.80 / 9.90) | 5.09 (5.05 / 6.13) | 2.70 (2.70 / 2.85) | 2.08 (2.09 / 1.82) | 2.02 (2.03 / 1.71) |
| 0.1 | 64 | 3 | 12.86 (12.72 / 17.02) | 9.79 (9.70 / 12.71) | 3.77 (3.71 / 5.54) | 3.07 (3.07 / 2.89) | 2.88 (2.89 / 2.56) |
| 0.2 | 64 | 3 | 25.37 (25.10 / 34.07) | 19.91 (19.67 / 27.03) | 5.59 (5.45 / 8.82) | 4.71 (4.73 / 5.07) | 3.90 (3.96 / 2.73) |

##### Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
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

#### Two-body accuracy of `data/final/models/pair_multi.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4096 | 0.031 | 0.093 | 0.036 | 0.34 | 5.65 / 10.69 | 0.006 / 0.029 (512) | 0.033 / 0.094 | 0.002 / 0.010 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4096 | 0.052 | 0.208 | 0.064 | 0.52 | 5.09 / 11.13 | 0.016 / 0.083 (512) | 0.049 / 0.203 | 0.004 / 0.027 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.051 | 0.403 | 0.079 | 0.63 | 4.70 / 11.48 | 0.026 / 0.237 (512) | 0.048 / 0.477 | 0.005 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4096 | 0.153 | 0.564 | 0.168 | 2.36 | 4.63 / 14.02 | 0.064 / 0.393 (512) | 0.162 / 0.650 | 0.030 / 0.170 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4096 | 0.033 | 0.094 | 0.037 | 0.34 | 5.69 / 10.60 | 0.004 / 0.012 (512) | 0.032 / 0.090 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.029 | 0.175 | 0.039 | 0.35 | 4.97 / 11.38 | 0.013 / 0.036 (512) | 0.028 / 0.185 | 0.003 / 0.019 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4096 | 0.110 | 0.504 | 0.123 | 1.63 | 4.07 / 11.49 | 0.063 / 0.301 (512) | 0.082 / 0.396 | 0.072 / 0.375 | 0.0 % |
| prolate_ar2p5__prolate_ar2p5_test | 4096 | 0.129 | 0.472 | 0.146 | 1.22 | 4.99 / 11.63 | 0.026 / 0.167 (512) | 0.130 / 0.364 | 0.017 / 0.102 | 0.0 % |
| oblate_ar2p5__oblate_ar2p5_test | 4096 | 0.409 | 1.269 | 0.444 | 4.16 | 4.28 / 11.30 | 0.039 / 0.130 (512) | 0.411 / 1.257 | 0.024 / 0.160 | 0.0 % |
| prolate_ar5__prolate_ar5_test | 4096 | 0.955 | 3.679 | 1.036 | 8.68 | 5.01 / 17.59 | 1.089 / 14.628 (512) | 1.396 / 15.305 | 0.099 / 0.495 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.036 / 0.099 (638) | 0.024 / 0.073 (824) | 0.025 / 0.090 (652) | 0.032 / 0.133 (628) | 0.045 / 0.162 (1022) | 0.062 / 0.265 (332) |
| prolate_ar2__prolate_ar2_test | 0.072 / 0.224 (678) | 0.042 / 0.198 (844) | 0.035 / 0.177 (684) | 0.039 / 0.203 (700) | 0.044 / 0.289 (944) | 0.049 / 0.314 (246) |
| prolateSpheroid__prolateSpheroid_test | 0.075 / 0.478 (682) | 0.038 / 0.381 (894) | 0.037 / 0.347 (690) | 0.038 / 0.264 (680) | 0.036 / 0.283 (988) | 0.031 / 0.334 (162) |
| prolate_ar4__prolate_ar4_test | 0.233 / 0.732 (686) | 0.128 / 0.507 (956) | 0.105 / 0.452 (736) | 0.091 / 0.367 (788) | 0.071 / 0.314 (786) | 0.074 / 0.436 (144) |
| oblate_ar1p5__oblate_ar1p5_test | 0.036 / 0.091 (648) | 0.029 / 0.087 (862) | 0.029 / 0.095 (724) | 0.030 / 0.110 (640) | 0.044 / 0.158 (1064) | 0.057 / 0.281 (158) |
| oblateSpheroid__oblateSpheroid_test | 0.040 / 0.187 (668) | 0.024 / 0.170 (956) | 0.018 / 0.161 (734) | 0.021 / 0.164 (720) | 0.028 / 0.190 (984) | 0.038 / 0.181 (34) |
| oblate_ar3__oblate_ar3_test | 0.154 / 0.683 (862) | 0.092 / 0.378 (1016) | 0.068 / 0.317 (868) | 0.071 / 0.288 (726) | 0.083 / 0.305 (608) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.172 / 0.561 (678) | 0.105 / 0.449 (886) | 0.104 / 0.362 (708) | 0.106 / 0.336 (646) | 0.124 / 0.379 (1024) | 0.087 / 0.367 (154) |
| oblate_ar2p5__oblate_ar2p5_test | 0.532 / 1.536 (734) | 0.410 / 1.143 (964) | 0.309 / 0.956 (784) | 0.253 / 0.980 (750) | 0.204 / 0.971 (844) | - |
| prolate_ar5__prolate_ar5_test | 1.290 / 5.010 (740) | 0.980 / 3.424 (994) | 0.730 / 2.348 (732) | 0.508 / 1.788 (720) | 0.441 / 1.358 (802) | 0.344 / 1.300 (108) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.010 / 0.045 (80) | 0.001 / 0.002 (92) | 0.000 / 0.000 (68) | 0.000 / 0.000 (88) | 0.000 / 0.000 (132) | 0.000 / 0.000 (52) |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.131 (94) | 0.002 / 0.013 (114) | 0.000 / 0.000 (72) | 0.000 / 0.000 (92) | 0.000 / 0.000 (122) | - |
| prolateSpheroid__prolateSpheroid_test | 0.047 / 0.375 (84) | 0.006 / 0.026 (102) | 0.002 / 0.006 (80) | 0.002 / 0.006 (86) | 0.001 / 0.005 (138) | 0.001 / 0.005 (22) |
| prolate_ar4__prolate_ar4_test | 0.115 / 0.651 (90) | 0.031 / 0.220 (100) | 0.004 / 0.014 (110) | 0.001 / 0.005 (84) | 0.001 / 0.002 (108) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.007 / 0.019 (74) | 0.001 / 0.003 (96) | 0.000 / 0.000 (100) | 0.000 / 0.000 (88) | 0.000 / 0.000 (130) | 0.000 / 0.000 (24) |
| oblateSpheroid__oblateSpheroid_test | 0.025 / 0.060 (66) | 0.008 / 0.017 (112) | 0.001 / 0.005 (110) | 0.001 / 0.003 (76) | 0.001 / 0.003 (142) | - |
| oblate_ar3__oblate_ar3_test | 0.081 / 0.376 (106) | 0.064 / 0.294 (152) | 0.038 / 0.140 (102) | 0.035 / 0.115 (90) | 0.033 / 0.114 (60) | - |
| prolate_ar2p5__prolate_ar2p5_test | 0.045 / 0.256 (102) | 0.009 / 0.040 (90) | 0.001 / 0.002 (102) | 0.000 / 0.001 (80) | 0.000 / 0.000 (120) | - |
| oblate_ar2p5__oblate_ar2p5_test | 0.062 / 0.189 (120) | 0.019 / 0.063 (108) | 0.010 / 0.032 (112) | 0.007 / 0.026 (90) | 0.006 / 0.023 (76) | - |
| prolate_ar5__prolate_ar5_test | 1.845 / 22.880 (116) | 0.094 / 0.462 (112) | 0.009 / 0.042 (94) | 0.003 / 0.010 (80) | 0.001 / 0.004 (96) | - |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2p5__prolate_ar2p5_test`: prolate_ar2p5 (target or source) with prolate_ar2p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar2p5__oblate_ar2p5_test`: oblate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar5__prolate_ar5_test`: prolate_ar5 (target or source) with prolate_ar5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
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
| 0.025 | 200 | 10 | 4.28 (4.31 / 4.03; 1.13) | 2.67 (2.72 / 2.17; 0.94) | 1.56 (1.59 / 1.26; 0.61) | 0.003 (0.003 / 0.005; 0.000) (1) |
| 0.05 | 200 | 10 | 7.40 (7.51 / 6.56; 2.10) | 5.41 (5.52 / 4.49; 1.81) | 2.61 (2.66 / 2.20; 0.91) | 0.005 (0.004 / 0.008; 0.000) (1) |
| 0.075 | 200 | 10 | 11.14 (11.25 / 10.13; 3.13) | 8.68 (8.82 / 7.10; 2.74) | 3.75 (3.80 / 3.20; 1.14) | 0.005 (0.005 / 0.009; 0.000) (1) |
| 0.1 | 200 | 10 | 13.72 (13.83 / 12.50; 3.94) | 10.81 (10.93 / 9.43; 3.49) | 4.32 (4.36 / 3.98; 1.34) | 0.006 (0.005 / 0.014; 0.000) (1) |
| 0.15 | 200 | 10 | 16.91 (16.78 / 19.81; 5.83) | 14.08 (14.00 / 16.00; 5.21) | 5.30 (5.28 / 6.03; 2.21) | 0.010 (0.007 / 0.027; 0.001) (1) |
| 0.2 | 200 | 10 | 24.52 (24.59 / 27.70; 7.59) | 21.02 (21.14 / 22.80; 6.83) | 9.16 (9.26 / 9.00; 3.89) | 0.015 (0.011 / 0.037; 0.001) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
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
| 0.05 | 50 | 5 | 6.51 (6.61 / 5.89; 2.22) | 4.13 (4.17 / 3.82; 1.61) | 1.71 (1.70 / 1.83; 0.66) | 0.001 (0.001 / 0.002; 0.000) (1) |
| 0.05 | 100 | 5 | 6.05 (5.99 / 6.95; 2.36) | 4.21 (4.22 / 4.22; 1.91) | 1.71 (1.69 / 2.01; 0.73) | 0.002 (0.002 / 0.004; 0.000) (1) |
| 0.05 | 200 | 5 | 7.61 (7.77 / 6.51; 2.11) | 5.56 (5.69 / 4.49; 1.82) | 2.67 (2.74 / 2.19; 0.93) | not measured |
| 0.05 | 300 | 5 | 7.35 (7.40 / 6.85; 2.04) | 5.39 (5.47 / 4.35; 1.82) | 2.89 (2.94 / 2.26; 1.10) | not measured |
| 0.1 | 50 | 5 | 12.90 (13.00 / 12.79; 4.38) | 9.34 (9.51 / 8.20; 3.37) | 2.77 (2.69 / 3.49; 0.98) | 0.004 (0.003 / 0.014; 0.001) (1) |
| 0.1 | 100 | 5 | 10.61 (10.46 / 13.08; 4.11) | 8.11 (8.02 / 9.77; 3.40) | 2.81 (2.74 / 3.98; 1.04) | 0.007 (0.006 / 0.017; 0.000) (1) |
| 0.1 | 200 | 5 | 13.16 (13.23 / 12.71; 3.92) | 10.20 (10.28 / 9.54; 3.47) | 3.97 (3.97 / 4.05; 1.32) | not measured |
| 0.1 | 300 | 5 | 14.31 (14.45 / 13.07; 3.89) | 11.66 (11.83 / 9.87; 3.53) | 5.05 (5.13 / 4.16; 1.67) | not measured |
| 0.15 | 50 | 5 | 17.78 (17.72 / 19.05; 5.94) | 13.31 (13.24 / 14.65; 4.64) | 3.65 (3.48 / 5.38; 0.81) | 0.008 (0.008 / 0.011; 0.000) (1) |
| 0.15 | 100 | 5 | 15.82 (15.82 / 18.86; 6.09) | 12.92 (12.96 / 14.95; 5.15) | 4.05 (4.00 / 5.55; 1.43) | 0.003 (0.002 / 0.007; 0.000) (1) |
| 0.15 | 200 | 5 | 16.95 (16.84 / 20.06; 5.84) | 14.03 (13.94 / 16.43; 5.23) | 5.20 (5.17 / 5.90; 2.20) | not measured |
| 0.15 | 300 | 5 | 22.64 (22.94 / 20.31; 5.82) | 19.24 (19.54 / 16.49; 5.33) | 8.16 (8.31 / 6.48; 2.70) | not measured |
| 0.2 | 50 | 5 | 19.68 (19.24 / 28.20; 7.72) | 15.32 (14.94 / 22.62; 6.09) | 3.91 (3.69 / 7.21; 0.98) | 0.015 (0.010 / 0.046; 0.002) (1) |
| 0.2 | 100 | 5 | 24.53 (24.37 / 28.15; 7.75) | 20.61 (20.58 / 22.33; 6.61) | 7.15 (7.09 / 8.39; 2.34) | 0.025 (0.014 / 0.069; 0.002) (1) |
| 0.2 | 200 | 5 | 25.92 (26.12 / 26.64; 7.53) | 22.31 (22.58 / 21.50; 6.77) | 9.71 (9.86 / 8.68; 3.87) | not measured |
| 0.2 | 300 | 5 | 24.11 (24.02 / 28.00; 7.56) | 21.17 (21.19 / 22.89; 6.96) | 10.01 (10.07 / 9.59; 4.27) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 136.8, 237 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.06 | 0.098 | 1.98 |
| + two-body | 1500 | 0.02 | 0.025 | 0.03 |
| + many-body | 1500 | 0.02 | 0.025 | 0.03 |
| MFS Xfine (the truth's own error) | 1500 | 0.000 | 0.0000 | 0.000 |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolate_ar2, prolate_ar2.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

#### Dynamics: ring of prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 105 steps, fell 19.6, 83 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 42 | 5.42 | 0.629 | 0.00 |
| + two-body | 41 | 1.80 | 0.300 | 0.00 |
| + many-body | 59 | 0.51 | 0.120 | 0.00 |
| MFS Xfine (the truth's own error) | 105 | 0.001 | 0.0006 | 0.002 |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
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
| + two-body | 7.3e-17 | 0.4030 | 6.7e-16 | 4.99 |
| + many-body | 7.9e-17 | 0.8843 | 6.8e-16 | 1.63 |
| MFS fine (the truth) | 2.0e-05 | 1 | | 0 |
| MFS Xfine | 1.2e-06 | 0.9996 | | 0.002 (= the error of the fine truth) |

MFS smallest eigenvalue 4.6459e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
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
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 19 of 20; -0.310 / 0.411 | 20 of 20; 0.264 / 0.572 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -0.419 / 0.013 | 20 of 20; 0.255 / 0.405 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 8 of 20; -0.468 / -0.036 | 20 of 20; 0.190 / 0.392 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 7 of 20; -0.878 / -0.117 | 20 of 20; 0.163 / 0.438 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.153 / -0.533 | 20 of 20; 0.125 / 0.315 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.123 / -0.742 | 20 of 20; 0.016 / 0.200 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.510 / -0.729 | 19 of 20; -0.100 / 0.310 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -1.900 / -1.203 | 16 of 20; -0.072 / 0.145 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.128 / -1.563 | 15 of 20; -0.102 / 0.124 |
| 0.2 | 16 | 18 | 18 of 18; 1.000 / 1.000 | 0 of 18; -1.699 / -1.271 | 17 of 18; -0.034 / 0.215 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.309 / -2.048 | 11 of 20; -0.471 / 0.063 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.909 / -2.489 | 3 of 20; -0.694 / -0.161 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -3.309 | 0.71 | prolate_ar2, prolate_ar2 | 2.82 | 1.081 | 1.04e-02 / 5.04e-03 (0.485) | 0.443, 0.478 (24 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 18 | -0.694 | 0.81 | prolate_ar2, prolate_ar2 | 2.41 | 1.054 | 1.04e-02 / 3.39e-03 (0.326) | 0.444, 0.740 (24 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 400 | 400 | 0.997 / 1.000 | 1.073, 2.16 |
| prolate_ar2__prolate_ar2_test | 400 | 400 | 0.991 / 1.000 | 1.053, 2.40 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.974 / 1.000 | 1.052, 2.35 |
| prolate_ar4__prolate_ar4_test | 400 | 400 | 0.969 / 1.000 | 1.055, 4.04 |
| oblate_ar1p5__oblate_ar1p5_test | 400 | 400 | 0.991 / 1.000 | 1.054, 2.44 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.984 / 1.000 | 1.070, 2.51 |
| oblate_ar3__oblate_ar3_test | 400 | 400 | 0.746 / 1.000 | 1.077, 2.86 |
| prolate_ar2p5__prolate_ar2p5_test | 400 | 400 | 0.965 / 1.000 | 1.058, 3.29 |
| oblate_ar2p5__oblate_ar2p5_test | 400 | 400 | 0.992 / 1.002 | 1.077, 5.34 |
| prolate_ar5__prolate_ar5_test | 400 | 400 | 0.753 / 1.000 | 1.056, 3.56 |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
- **Configurations**: N in [16, 50, 100], shapes prolate_ar2 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolate_ar2

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.44 (7.49 / 6.96) | 5.06 (5.12 / 4.35) | 1.96 (1.92 / 2.34) | 1.18 (1.21 / 0.90) | 1.14 (1.17 / 0.79) |
| 0.1 | 64 | 3 | 12.45 (12.38 / 13.24) | 9.10 (9.09 / 9.43) | 3.07 (3.00 / 3.87) | 1.90 (1.93 / 1.53) | 1.63 (1.68 / 1.00) |
| 0.2 | 64 | 3 | 23.92 (24.16 / 25.54) | 19.82 (20.12 / 20.50) | 5.98 (5.91 / 7.72) | 3.25 (3.29 / 3.44) | 1.89 (1.99 / 1.09) |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
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

#### Two-body accuracy of `data/final/models/pair_mixed.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.047 | 0.387 | 0.076 | 0.52 | 4.70 / 11.48 | 0.026 / 0.237 (512) | 0.045 / 0.452 | 0.005 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.028 | 0.164 | 0.037 | 0.32 | 4.97 / 11.38 | 0.013 / 0.036 (512) | 0.030 / 0.181 | 0.003 / 0.019 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4096 | 0.070 | 0.433 | 0.097 | 0.71 | 4.88 / 11.26 | 0.015 / 0.062 (512) | 0.070 / 0.378 | 0.004 / 0.022 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.069 / 0.455 (682) | 0.035 / 0.369 (894) | 0.032 / 0.338 (690) | 0.035 / 0.251 (680) | 0.034 / 0.279 (988) | 0.035 / 0.316 (162) |
| oblateSpheroid__oblateSpheroid_test | 0.040 / 0.175 (668) | 0.022 / 0.156 (956) | 0.018 / 0.155 (734) | 0.018 / 0.153 (720) | 0.025 / 0.180 (984) | 0.047 / 0.154 (34) |
| prolateSpheroid__oblateSpheroid_test | 0.091 / 0.500 (748) | 0.062 / 0.420 (928) | 0.055 / 0.323 (704) | 0.052 / 0.305 (704) | 0.060 / 0.327 (902) | 0.065 / 0.385 (110) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.047 / 0.375 (84) | 0.006 / 0.026 (102) | 0.002 / 0.006 (80) | 0.002 / 0.006 (86) | 0.001 / 0.005 (138) | 0.001 / 0.005 (22) |
| oblateSpheroid__oblateSpheroid_test | 0.025 / 0.060 (66) | 0.008 / 0.017 (112) | 0.001 / 0.005 (110) | 0.001 / 0.003 (76) | 0.001 / 0.003 (142) | - |
| prolateSpheroid__oblateSpheroid_test | 0.027 / 0.093 (102) | 0.004 / 0.014 (110) | 0.002 / 0.006 (82) | 0.001 / 0.005 (98) | 0.001 / 0.004 (110) | - |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
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
| 0.025 | 200 | 10 | 4.15 (4.13 / 4.73; 1.18) | 2.70 (2.70 / 2.58; 0.99) | 1.76 (1.76 / 1.67; 0.74) | 0.004 (0.003 / 0.012; 0.000) (1) |
| 0.05 | 200 | 10 | 7.04 (7.02 / 8.05; 2.15) | 5.18 (5.19 / 5.41; 1.88) | 3.03 (3.04 / 3.05; 1.16) | 0.008 (0.007 / 0.020; 0.000) (1) |
| 0.075 | 200 | 10 | 10.32 (10.30 / 11.29; 3.18) | 8.05 (8.04 / 8.77; 2.82) | 4.09 (4.09 / 4.29; 1.53) | 0.026 (0.025 / 0.042; 0.001) (1) |
| 0.1 | 200 | 10 | 13.71 (13.68 / 14.59; 4.06) | 11.06 (11.05 / 11.38; 3.62) | 5.44 (5.44 / 5.33; 1.73) | 0.011 (0.010 / 0.029; 0.001) (1) |
| 0.15 | 200 | 10 | 19.40 (19.34 / 21.97; 5.87) | 16.06 (16.01 / 18.07; 5.28) | 6.45 (6.43 / 7.16; 2.12) | 0.018 (0.016 / 0.044; 0.002) (1) |
| 0.2 | 200 | 10 | 23.59 (23.38 / 31.98; 7.63) | 20.14 (19.95 / 27.83; 6.90) | 7.34 (7.29 / 9.58; 2.49) | 0.009 (0.006 / 0.089; 0.002) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
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
| 0.05 | 50 | 5 | 6.86 (6.83 / 7.69; 2.63) | 4.82 (4.79 / 5.46; 1.96) | 2.19 (2.16 / 2.84; 0.78) | 0.008 (0.006 / 0.022; 0.000) (1) |
| 0.05 | 100 | 5 | 6.35 (6.31 / 7.81; 2.25) | 4.57 (4.56 / 5.18; 1.81) | 2.39 (2.38 / 2.69; 0.85) | 0.004 (0.003 / 0.020; 0.000) (1) |
| 0.05 | 200 | 5 | 6.78 (6.78 / 7.84; 2.15) | 5.06 (5.07 / 5.37; 1.88) | 3.01 (3.02 / 3.06; 1.16) | not measured |
| 0.05 | 300 | 5 | 7.77 (7.78 / 7.98; 2.13) | 5.68 (5.70 / 5.40; 1.91) | 3.46 (3.49 / 3.12; 1.33) | not measured |
| 0.1 | 50 | 5 | 11.72 (11.62 / 14.31; 4.59) | 8.33 (8.25 / 10.37; 3.57) | 3.15 (3.08 / 4.77; 1.27) | 0.009 (0.007 / 0.031; 0.001) (1) |
| 0.1 | 100 | 5 | 12.69 (12.69 / 13.71; 4.08) | 9.67 (9.67 / 10.63; 3.42) | 3.95 (3.94 / 4.63; 1.23) | 0.016 (0.014 / 0.030; 0.001) (1) |
| 0.1 | 200 | 5 | 13.85 (13.84 / 14.43; 3.98) | 11.32 (11.33 / 11.44; 3.55) | 5.66 (5.67 / 5.30; 1.70) | not measured |
| 0.1 | 300 | 5 | 12.51 (12.48 / 14.54; 3.98) | 10.35 (10.32 / 11.75; 3.63) | 5.40 (5.40 / 5.58; 2.04) | not measured |
| 0.15 | 50 | 5 | 15.33 (15.13 / 21.52; 6.04) | 11.37 (11.21 / 16.42; 4.74) | 3.60 (3.50 / 6.13; 1.50) | 0.024 (0.020 / 0.109; 0.003) (1) |
| 0.15 | 100 | 5 | 18.91 (18.85 / 22.71; 6.22) | 15.51 (15.47 / 18.80; 5.31) | 5.44 (5.41 / 7.07; 1.62) | 0.008 (0.007 / 0.028; 0.002) (1) |
| 0.15 | 200 | 5 | 17.36 (17.23 / 22.05; 5.88) | 14.29 (14.18 / 17.93; 5.30) | 5.77 (5.73 / 7.12; 2.11) | not measured |
| 0.15 | 300 | 5 | 20.71 (20.66 / 23.81; 5.91) | 17.53 (17.51 / 19.56; 5.44) | 8.04 (8.06 / 7.97; 2.68) | not measured |
| 0.2 | 50 | 5 | 23.53 (23.27 / 29.73; 7.77) | 18.28 (18.00 / 24.84; 6.18) | 4.93 (4.75 / 8.21; 1.44) | 0.025 (0.022 / 0.052; 0.002) (1) |
| 0.2 | 100 | 5 | 23.56 (23.33 / 30.62; 7.64) | 19.30 (19.10 / 25.11; 6.54) | 6.12 (6.02 / 8.68; 1.81) | 0.028 (0.025 / 0.052; 0.002) (1) |
| 0.2 | 200 | 5 | 23.01 (22.81 / 32.55; 7.55) | 19.65 (19.46 / 28.12; 6.82) | 7.09 (7.04 / 9.65; 2.47) | not measured |
| 0.2 | 300 | 5 | 22.88 (22.70 / 32.80; 7.71) | 20.07 (19.92 / 28.50; 7.12) | 8.32 (8.29 / 10.55; 3.18) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 110.9, 255 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.48 | 0.564 | 2.61 |
| + two-body | 1500 | 0.01 | 0.017 | 0.08 |
| + many-body | 1500 | 0.01 | 0.017 | 0.08 |
| MFS Xfine (the truth's own error) | 1500 | 0.002 | 0.0031 | 0.027 |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 173 steps, fell 26.9, 148 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 33 | 6.24 | 0.498 | 12.49 |
| + two-body | 40 | 2.26 | 0.265 | 7.97 |
| + many-body | 78 | 0.71 | 0.157 | 1.22 |
| MFS Xfine (the truth's own error) | 173 | 0.002 | 0.0012 | 0.016 |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
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
| + two-body | 9.0e-17 | -2.7767 | 7.5e-16 | 7.18 |
| + many-body | 9.7e-17 | -0.0331 | 7.4e-16 | 2.50 |
| MFS fine (the truth) | 5.7e-05 | 1 | | 0 |
| MFS Xfine | 3.2e-06 | 0.9959 | | 0.014 (= the error of the fine truth) |

MFS smallest eigenvalue 1.2134e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 11 | -4.798 | 0.77 | oblateSpheroid, oblateSpheroid | 3.32 | 1.116 | 6.58e-03 / 3.99e-03 (0.607) | 0.510, 0.488 (15 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 9 | -2.779 | 0.05 | oblateSpheroid, prolateSpheroid | 13.04 | inf | 5.66e-03 / 5.66e-03 (1.000) | 0.789, 0.605 (9 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.969 / 1.000 | 1.052, 2.35 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.990 / 1.000 | 1.051, 2.57 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.988 / 1.000 | 1.055, 2.48 |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolateSpheroid, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.21 (7.19 / 7.90) | 4.93 (4.93 / 4.80) | 2.51 (2.51 / 2.64) | 1.78 (1.79 / 1.49) | 1.74 (1.75 / 1.44) |
| 0.1 | 64 | 3 | 12.19 (12.09 / 13.98) | 8.93 (8.88 / 9.91) | 3.59 (3.54 / 4.34) | 2.56 (2.57 / 2.18) | 2.47 (2.50 / 1.81) |
| 0.2 | 64 | 3 | 24.39 (24.13 / 30.29) | 19.56 (19.28 / 25.78) | 5.72 (5.57 / 8.53) | 4.40 (4.39 / 4.70) | 3.59 (3.63 / 2.61) |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
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

#### Two-body accuracy of `data/final/models/pair_poly.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4096 | 0.031 | 0.080 | 0.035 | 0.32 | 5.65 / 10.69 | 0.006 / 0.029 (512) | 0.034 / 0.082 | 0.002 / 0.010 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4096 | 0.047 | 0.179 | 0.057 | 0.49 | 5.09 / 11.13 | 0.016 / 0.083 (512) | 0.045 / 0.162 | 0.004 / 0.027 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.051 | 0.350 | 0.073 | 0.61 | 4.70 / 11.48 | 0.026 / 0.237 (512) | 0.049 / 0.384 | 0.005 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4096 | 0.137 | 0.528 | 0.153 | 2.23 | 4.63 / 14.02 | 0.064 / 0.393 (512) | 0.131 / 0.605 | 0.030 / 0.170 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4096 | 0.030 | 0.088 | 0.034 | 0.32 | 5.69 / 10.60 | 0.004 / 0.012 (512) | 0.028 / 0.091 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.026 | 0.150 | 0.035 | 0.32 | 4.97 / 11.38 | 0.013 / 0.036 (512) | 0.027 / 0.164 | 0.003 / 0.019 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4096 | 0.100 | 0.446 | 0.111 | 1.38 | 4.07 / 11.49 | 0.063 / 0.301 (512) | 0.084 / 0.309 | 0.072 / 0.375 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4096 | 0.071 | 0.381 | 0.092 | 0.80 | 4.88 / 11.26 | 0.015 / 0.062 (512) | 0.065 / 0.312 | 0.004 / 0.022 | 0.0 % |
| prolate_ar2__oblateSpheroid_test | 4096 | 0.088 | 0.339 | 0.102 | 0.85 | 4.91 / 11.40 | 0.023 / 0.064 (512) | 0.096 / 0.330 | 0.003 / 0.021 | 0.0 % |
| prolate_ar4__oblate_ar3_test | 4096 | 0.200 | 0.812 | 0.223 | 3.16 | 4.15 / 12.28 | 0.062 / 0.355 (512) | 0.183 / 0.783 | 0.074 / 0.485 | 0.0 % |
| prolate_ar2__oblate_ar1p5_test | 4096 | 0.072 | 0.228 | 0.082 | 0.77 | 5.32 / 10.61 | 0.006 / 0.029 (512) | 0.074 / 0.216 | 0.005 / 0.023 | 0.0 % |
| prolate_ar1p5__oblate_ar3_test | 4096 | 0.150 | 0.603 | 0.169 | 1.37 | 4.16 / 14.22 | 0.133 / 0.462 (512) | 0.159 / 0.584 | 0.117 / 0.602 | 0.0 % |
| prolateSpheroid__prolate_ar2_test | 4096 | 0.111 | 0.480 | 0.135 | 1.33 | 4.78 / 11.51 | 0.014 / 0.112 (512) | 0.110 / 0.452 | 0.004 / 0.023 | 0.0 % |
| oblateSpheroid__oblate_ar3_test | 4096 | 0.123 | 0.507 | 0.140 | 1.45 | 4.22 / 12.13 | 0.086 / 0.392 (512) | 0.117 / 0.506 | 0.080 / 0.435 | 0.0 % |
| prolate_ar4__oblateSpheroid_test | 4096 | 0.155 | 0.656 | 0.179 | 2.00 | 4.83 / 13.18 | 0.040 / 0.236 (512) | 0.170 / 0.747 | 0.022 / 0.152 | 0.0 % |
| prolateSpheroid__oblate_ar1p5_test | 4096 | 0.097 | 0.381 | 0.116 | 1.08 | 5.10 / 12.27 | 0.016 / 0.101 (512) | 0.103 / 0.408 | 0.004 / 0.022 | 0.0 % |
| prolateSpheroid_x0p75__prolateSpheroid_test | 4096 | 0.119 | 0.587 | 0.158 | 1.32 | 4.62 / 13.66 | 0.027 / 0.252 (512) | 0.120 / 0.644 | 0.006 / 0.032 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4096 | 0.083 | 0.303 | 0.090 | 0.77 | 4.48 / 10.82 | 0.027 / 0.079 (512) | 0.083 / 0.278 | 0.004 / 0.025 | 0.0 % |
| prolate_ar2_x1p5__prolate_ar2_test | 4096 | 0.081 | 0.327 | 0.094 | 0.84 | 4.78 / 11.12 | 0.020 / 0.103 (512) | 0.080 / 0.378 | 0.008 / 0.052 | 0.0 % |
| oblate_ar3_x0p75__oblate_ar3_test | 4096 | 0.139 | 0.594 | 0.159 | 2.10 | 3.86 / 11.87 | 0.070 / 0.269 (512) | 0.130 / 0.454 | 0.073 / 0.384 | 0.0 % |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 4096 | 0.126 | 0.532 | 0.145 | 1.03 | 3.53 / 13.05 | 0.037 / 0.174 (512) | 0.129 / 0.423 | 0.007 / 0.046 | 0.0 % |
| prolate_ar2_x1p5__oblateSpheroid_test | 4096 | 0.094 | 0.339 | 0.104 | 1.00 | 4.97 / 10.48 | 0.028 / 0.077 (512) | 0.104 / 0.366 | 0.005 / 0.030 | 0.0 % |
| prolate_ar2__oblate_ar3_test | 4096 | 1.114 | 3.509 | 1.202 | 5.95 | 3.96 / 12.73 | 0.124 / 0.506 (512) | 1.057 / 3.526 | 0.101 / 0.548 | 0.0 % |
| prolate_ar4__oblate_ar1p5_test | 4096 | 1.597 | 3.847 | 1.688 | 5.39 | 5.03 / 14.99 | 0.085 / 0.435 (512) | 1.517 / 4.040 | 0.038 / 0.240 | 0.0 % |
| prolate_ar2p5__oblate_ar2p5_test | 4096 | 0.739 | 1.986 | 0.790 | 4.27 | 4.24 / 11.82 | 0.047 / 0.228 (512) | 0.763 / 2.027 | 0.042 / 0.243 | 0.0 % |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 4096 | 0.107 | 0.372 | 0.118 | 0.75 | 4.91 / 10.34 | 0.030 / 0.178 (512) | 0.104 / 0.393 | 0.017 / 0.111 | 0.0 % |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 4096 | 1.854 | 4.909 | 1.984 | 15.96 | 4.49 / 11.40 | 0.039 / 0.200 (512) | 1.893 / 5.046 | 0.052 / 0.272 | 0.0 % |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 4096 | 0.219 | 1.124 | 0.267 | 2.72 | 4.90 / 10.80 | 0.026 / 0.124 (512) | 0.232 / 1.075 | 0.015 / 0.104 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.034 / 0.086 (638) | 0.024 / 0.062 (824) | 0.026 / 0.076 (652) | 0.035 / 0.112 (628) | 0.045 / 0.130 (1022) | 0.075 / 0.231 (332) |
| prolate_ar2__prolate_ar2_test | 0.065 / 0.202 (678) | 0.040 / 0.164 (844) | 0.032 / 0.146 (684) | 0.031 / 0.165 (700) | 0.042 / 0.231 (944) | 0.050 / 0.251 (246) |
| prolateSpheroid__prolateSpheroid_test | 0.072 / 0.386 (682) | 0.045 / 0.356 (894) | 0.038 / 0.323 (690) | 0.033 / 0.229 (680) | 0.031 / 0.226 (988) | 0.036 / 0.281 (162) |
| prolate_ar4__prolate_ar4_test | 0.214 / 0.716 (686) | 0.110 / 0.447 (956) | 0.089 / 0.406 (736) | 0.072 / 0.320 (788) | 0.063 / 0.255 (786) | 0.061 / 0.356 (144) |
| oblate_ar1p5__oblate_ar1p5_test | 0.036 / 0.095 (648) | 0.024 / 0.079 (862) | 0.025 / 0.080 (724) | 0.030 / 0.095 (640) | 0.037 / 0.128 (1064) | 0.063 / 0.217 (158) |
| oblateSpheroid__oblateSpheroid_test | 0.038 / 0.175 (668) | 0.020 / 0.139 (956) | 0.017 / 0.122 (734) | 0.018 / 0.127 (720) | 0.024 / 0.153 (984) | 0.032 / 0.140 (34) |
| oblate_ar3__oblate_ar3_test | 0.143 / 0.600 (862) | 0.084 / 0.355 (1016) | 0.062 / 0.262 (868) | 0.057 / 0.248 (726) | 0.063 / 0.214 (608) | - |
| prolateSpheroid__oblateSpheroid_test | 0.094 / 0.419 (748) | 0.063 / 0.388 (928) | 0.055 / 0.309 (704) | 0.047 / 0.270 (704) | 0.051 / 0.287 (902) | 0.052 / 0.309 (110) |
| prolate_ar2__oblateSpheroid_test | 0.119 / 0.384 (692) | 0.075 / 0.318 (896) | 0.062 / 0.279 (720) | 0.060 / 0.300 (656) | 0.077 / 0.308 (1038) | 0.126 / 0.403 (94) |
| prolate_ar4__oblate_ar3_test | 0.287 / 1.060 (742) | 0.165 / 0.646 (946) | 0.141 / 0.633 (756) | 0.140 / 0.549 (772) | 0.134 / 0.576 (842) | 0.133 / 0.611 (38) |
| prolate_ar2__oblate_ar1p5_test | 0.092 / 0.269 (672) | 0.060 / 0.192 (824) | 0.049 / 0.184 (656) | 0.060 / 0.212 (666) | 0.084 / 0.293 (1080) | 0.100 / 0.408 (198) |
| prolate_ar1p5__oblate_ar3_test | 0.214 / 0.790 (762) | 0.124 / 0.500 (972) | 0.099 / 0.357 (644) | 0.095 / 0.366 (730) | 0.103 / 0.376 (892) | 0.150 / 0.532 (96) |
| prolateSpheroid__prolate_ar2_test | 0.154 / 0.580 (644) | 0.090 / 0.443 (916) | 0.082 / 0.390 (698) | 0.095 / 0.337 (660) | 0.092 / 0.373 (966) | 0.082 / 0.384 (212) |
| oblateSpheroid__oblate_ar3_test | 0.173 / 0.680 (772) | 0.099 / 0.377 (966) | 0.086 / 0.340 (822) | 0.081 / 0.331 (752) | 0.099 / 0.344 (754) | 0.179 / 0.427 (30) |
| prolate_ar4__oblateSpheroid_test | 0.212 / 0.832 (690) | 0.149 / 0.584 (970) | 0.107 / 0.483 (702) | 0.099 / 0.445 (754) | 0.096 / 0.420 (906) | 0.081 / 0.488 (74) |
| prolateSpheroid__oblate_ar1p5_test | 0.130 / 0.463 (642) | 0.084 / 0.347 (898) | 0.075 / 0.288 (596) | 0.077 / 0.276 (698) | 0.078 / 0.308 (1092) | 0.092 / 0.482 (170) |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.167 / 0.722 (708) | 0.107 / 0.567 (920) | 0.084 / 0.409 (686) | 0.073 / 0.335 (716) | 0.075 / 0.325 (912) | 0.056 / 0.314 (154) |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.116 / 0.362 (688) | 0.063 / 0.278 (940) | 0.057 / 0.221 (738) | 0.062 / 0.244 (728) | 0.083 / 0.279 (966) | 0.128 / 0.320 (36) |
| prolate_ar2_x1p5__prolate_ar2_test | 0.107 / 0.397 (738) | 0.066 / 0.262 (800) | 0.058 / 0.265 (688) | 0.062 / 0.262 (642) | 0.074 / 0.279 (1024) | 0.084 / 0.351 (204) |
| oblate_ar3_x0p75__oblate_ar3_test | 0.203 / 0.822 (852) | 0.114 / 0.437 (1036) | 0.088 / 0.339 (876) | 0.080 / 0.334 (784) | 0.084 / 0.326 (536) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.161 / 0.647 (702) | 0.114 / 0.467 (890) | 0.100 / 0.393 (718) | 0.098 / 0.473 (776) | 0.115 / 0.476 (960) | 0.141 / 0.646 (50) |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.130 / 0.413 (662) | 0.075 / 0.294 (890) | 0.068 / 0.236 (646) | 0.074 / 0.291 (634) | 0.082 / 0.336 (1148) | 0.115 / 0.499 (116) |
| prolate_ar2__oblate_ar3_test | 1.408 / 4.195 (720) | 1.162 / 3.442 (952) | 0.899 / 2.683 (732) | 0.678 / 1.846 (684) | 0.364 / 1.178 (930) | 0.178 / 0.649 (78) |
| prolate_ar4__oblate_ar1p5_test | 2.099 / 4.657 (714) | 1.714 / 3.894 (934) | 1.149 / 2.557 (666) | 0.603 / 1.494 (704) | 0.252 / 0.820 (916) | 0.132 / 0.630 (162) |
| prolate_ar2p5__oblate_ar2p5_test | 0.922 / 2.307 (728) | 0.813 / 1.985 (940) | 0.569 / 1.537 (700) | 0.349 / 1.085 (750) | 0.160 / 0.719 (922) | 0.118 / 0.501 (56) |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.145 / 0.482 (686) | 0.111 / 0.331 (928) | 0.065 / 0.223 (694) | 0.040 / 0.191 (638) | 0.040 / 0.199 (972) | 0.043 / 0.235 (178) |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 2.413 / 5.683 (780) | 1.832 / 4.611 (938) | 1.366 / 4.018 (684) | 1.045 / 3.572 (706) | 0.920 / 3.233 (944) | 1.220 / 2.757 (44) |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.279 / 1.330 (680) | 0.228 / 1.108 (916) | 0.174 / 0.851 (680) | 0.130 / 0.641 (698) | 0.093 / 0.502 (1026) | 0.083 / 0.458 (96) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.010 / 0.045 (80) | 0.001 / 0.002 (92) | 0.000 / 0.000 (68) | 0.000 / 0.000 (88) | 0.000 / 0.000 (132) | 0.000 / 0.000 (52) |
| prolate_ar2__prolate_ar2_test | 0.026 / 0.131 (94) | 0.002 / 0.013 (114) | 0.000 / 0.000 (72) | 0.000 / 0.000 (92) | 0.000 / 0.000 (122) | - |
| prolateSpheroid__prolateSpheroid_test | 0.047 / 0.375 (84) | 0.006 / 0.026 (102) | 0.002 / 0.006 (80) | 0.002 / 0.006 (86) | 0.001 / 0.005 (138) | 0.001 / 0.005 (22) |
| prolate_ar4__prolate_ar4_test | 0.115 / 0.651 (90) | 0.031 / 0.220 (100) | 0.004 / 0.014 (110) | 0.001 / 0.005 (84) | 0.001 / 0.002 (108) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.007 / 0.019 (74) | 0.001 / 0.003 (96) | 0.000 / 0.000 (100) | 0.000 / 0.000 (88) | 0.000 / 0.000 (130) | 0.000 / 0.000 (24) |
| oblateSpheroid__oblateSpheroid_test | 0.025 / 0.060 (66) | 0.008 / 0.017 (112) | 0.001 / 0.005 (110) | 0.001 / 0.003 (76) | 0.001 / 0.003 (142) | - |
| oblate_ar3__oblate_ar3_test | 0.081 / 0.376 (106) | 0.064 / 0.294 (152) | 0.038 / 0.140 (102) | 0.035 / 0.115 (90) | 0.033 / 0.114 (60) | - |
| prolateSpheroid__oblateSpheroid_test | 0.027 / 0.093 (102) | 0.004 / 0.014 (110) | 0.002 / 0.006 (82) | 0.001 / 0.005 (98) | 0.001 / 0.004 (110) | - |
| prolate_ar2__oblateSpheroid_test | 0.040 / 0.098 (88) | 0.008 / 0.016 (118) | 0.001 / 0.004 (72) | 0.001 / 0.003 (86) | 0.000 / 0.002 (138) | - |
| prolate_ar4__oblate_ar3_test | 0.108 / 0.584 (66) | 0.054 / 0.281 (160) | 0.038 / 0.134 (86) | 0.023 / 0.095 (96) | 0.019 / 0.073 (102) | - |
| prolate_ar2__oblate_ar1p5_test | 0.010 / 0.046 (80) | 0.000 / 0.002 (104) | 0.000 / 0.000 (76) | 0.000 / 0.000 (96) | 0.000 / 0.000 (128) | 0.000 / 0.000 (28) |
| prolate_ar1p5__oblate_ar3_test | 0.224 / 0.705 (94) | 0.088 / 0.270 (124) | 0.053 / 0.173 (64) | 0.036 / 0.122 (82) | 0.032 / 0.104 (136) | - |
| prolateSpheroid__prolate_ar2_test | 0.029 / 0.222 (68) | 0.006 / 0.020 (132) | 0.002 / 0.005 (102) | 0.002 / 0.004 (70) | 0.001 / 0.004 (110) | 0.001 / 0.003 (30) |
| oblateSpheroid__oblate_ar3_test | 0.131 / 0.588 (94) | 0.063 / 0.189 (134) | 0.059 / 0.160 (92) | 0.034 / 0.108 (84) | 0.024 / 0.083 (104) | - |
| prolate_ar4__oblateSpheroid_test | 0.074 / 0.390 (86) | 0.015 / 0.063 (112) | 0.003 / 0.010 (82) | 0.001 / 0.005 (112) | 0.001 / 0.003 (114) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.032 / 0.171 (72) | 0.004 / 0.020 (106) | 0.002 / 0.004 (94) | 0.001 / 0.004 (84) | 0.001 / 0.003 (134) | 0.001 / 0.003 (22) |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.047 / 0.419 (92) | 0.008 / 0.045 (102) | 0.002 / 0.006 (82) | 0.002 / 0.005 (96) | 0.001 / 0.004 (118) | 0.001 / 0.004 (22) |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.050 / 0.127 (80) | 0.008 / 0.024 (112) | 0.002 / 0.006 (90) | 0.001 / 0.003 (98) | 0.001 / 0.004 (130) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.035 / 0.153 (100) | 0.004 / 0.017 (90) | 0.000 / 0.000 (98) | 0.000 / 0.000 (74) | 0.000 / 0.000 (124) | 0.000 / 0.000 (26) |
| oblate_ar3_x0p75__oblate_ar3_test | 0.091 / 0.330 (94) | 0.080 / 0.278 (134) | 0.046 / 0.168 (114) | 0.031 / 0.127 (110) | 0.027 / 0.128 (58) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.071 / 0.301 (76) | 0.007 / 0.027 (108) | 0.002 / 0.007 (94) | 0.001 / 0.004 (98) | 0.001 / 0.004 (124) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.045 / 0.108 (104) | 0.004 / 0.014 (86) | 0.001 / 0.003 (68) | 0.001 / 0.002 (98) | 0.000 / 0.002 (148) | - |
| prolate_ar2__oblate_ar3_test | 0.198 / 0.758 (100) | 0.063 / 0.207 (122) | 0.067 / 0.197 (94) | 0.047 / 0.154 (82) | 0.030 / 0.107 (106) | - |
| prolate_ar4__oblate_ar1p5_test | 0.150 / 0.713 (96) | 0.032 / 0.091 (122) | 0.006 / 0.028 (86) | 0.002 / 0.005 (94) | 0.000 / 0.001 (96) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.093 / 0.412 (66) | 0.017 / 0.066 (116) | 0.011 / 0.029 (80) | 0.009 / 0.024 (120) | 0.005 / 0.018 (124) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.056 / 0.303 (76) | 0.009 / 0.032 (90) | 0.000 / 0.002 (78) | 0.000 / 0.000 (88) | 0.000 / 0.000 (152) | 0.000 / 0.000 (28) |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 0.055 / 0.269 (98) | 0.032 / 0.143 (112) | 0.026 / 0.086 (60) | 0.022 / 0.080 (104) | 0.013 / 0.077 (132) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.045 / 0.193 (102) | 0.004 / 0.011 (124) | 0.001 / 0.004 (82) | 0.001 / 0.003 (82) | 0.000 / 0.003 (110) | - |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__oblateSpheroid_test`: prolate_ar2 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__oblate_ar3_test`: prolate_ar4 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__oblate_ar1p5_test`: prolate_ar2 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar1p5__oblate_ar3_test`: prolate_ar1p5 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__prolate_ar2_test`: prolateSpheroid (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid__oblate_ar3_test`: oblateSpheroid (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__oblateSpheroid_test`: prolate_ar4 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__oblate_ar1p5_test`: prolateSpheroid (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid_x0p75__prolateSpheroid_test`: prolateSpheroid_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2_x1p5__prolate_ar2_test`: prolate_ar2_x1p5 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar3_x0p75__oblate_ar3_test`: oblate_ar3_x0p75 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid_x1p5__prolateSpheroid_x0p75_test`: oblateSpheroid_x1p5 (target or source) with prolateSpheroid_x0p75, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2_x1p5__oblateSpheroid_test`: prolate_ar2_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__oblate_ar3_test`: prolate_ar2 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__oblate_ar1p5_test`: prolate_ar4 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2p5__oblate_ar2p5_test`: prolate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test`: prolate_ar2p5_x1p25 (target or source) with prolate_ar2p5_x1p25, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar3_x0p75__prolate_ar2_x1p5_test`: oblate_ar3_x0p75 (target or source) with prolate_ar2_x1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2p5_x1p25__oblateSpheroid_test`: prolate_ar2p5_x1p25 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
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
| 0.025 | 200 | 10 | 4.53 (4.64 / 3.46; 1.17) | 2.71 (2.80 / 1.61; 0.97) | 2.10 (2.17 / 1.25; 0.78) | 0.016 (0.014 / 0.026; 0.001) (1) |
| 0.05 | 200 | 10 | 7.90 (8.10 / 5.83; 2.30) | 5.50 (5.68 / 3.45; 1.97) | 3.88 (4.01 / 2.43; 1.42) | 0.030 (0.028 / 0.046; 0.002) (1) |
| 0.075 | 200 | 10 | 9.69 (9.82 / 7.73; 3.24) | 7.22 (7.35 / 5.14; 2.83) | 4.66 (4.74 / 3.37; 1.86) | 0.064 (0.054 / 0.129; 0.011) (1) |
| 0.1 | 200 | 10 | 14.39 (14.87 / 9.67; 4.30) | 10.85 (11.23 / 6.93; 3.80) | 6.31 (6.53 / 4.13; 2.32) | 0.034 (0.032 / 0.050; 0.003) (1) |
| 0.15 | 200 | 10 | 18.52 (18.90 / 14.62; 6.19) | 14.90 (15.25 / 11.02; 5.52) | 8.08 (8.26 / 5.99; 3.03) | 0.053 (0.041 / 0.196; 0.004) (1) |
| 0.2 | 200 | 8 | 23.17 (23.45 / 19.58; 8.26) | 19.24 (19.55 / 15.04; 7.43) | 9.49 (9.63 / 7.50; 3.75) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
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
| 0.05 | 50 | 5 | 7.46 (7.72 / 5.45; 2.78) | 4.60 (4.78 / 2.91; 1.98) | 2.83 (2.93 / 2.00; 1.08) | 0.035 (0.021 / 0.076; 0.003) (1) |
| 0.05 | 100 | 5 | 6.80 (6.95 / 5.13; 2.42) | 4.48 (4.59 / 3.24; 1.92) | 3.08 (3.14 / 2.29; 1.19) | 0.026 (0.023 / 0.051; 0.002) (1) |
| 0.05 | 200 | 5 | 7.84 (8.05 / 5.69; 2.30) | 5.51 (5.69 / 3.38; 1.98) | 3.94 (4.07 / 2.38; 1.43) | not measured |
| 0.05 | 300 | 5 | 7.93 (8.13 / 5.79; 2.21) | 5.69 (5.88 / 3.35; 1.97) | 3.89 (4.02 / 2.34; 1.52) | not measured |
| 0.1 | 50 | 5 | 13.21 (13.48 / 11.12; 4.77) | 8.26 (8.46 / 6.60; 3.59) | 4.25 (4.32 / 3.70; 1.47) | 0.050 (0.044 / 0.082; 0.008) (1) |
| 0.1 | 100 | 5 | 14.22 (14.71 / 9.71; 4.28) | 10.12 (10.50 / 6.50; 3.57) | 5.55 (5.74 / 3.82; 1.73) | 0.032 (0.028 / 0.056; 0.005) (1) |
| 0.1 | 200 | 5 | 13.72 (14.01 / 10.08; 4.23) | 10.49 (10.73 / 7.39; 3.73) | 6.17 (6.31 / 4.42; 2.26) | not measured |
| 0.1 | 300 | 5 | 13.52 (13.78 / 9.94; 4.18) | 10.64 (10.89 / 6.89; 3.80) | 6.97 (7.14 / 4.37; 2.62) | not measured |
| 0.15 | 50 | 5 | 17.66 (17.99 / 14.74; 6.43) | 12.49 (12.79 / 9.78; 4.97) | 5.59 (5.64 / 5.41; 1.73) | 0.034 (0.030 / 0.056; 0.005) (1) |
| 0.15 | 100 | 5 | 19.88 (20.51 / 14.18; 6.47) | 14.96 (15.46 / 10.41; 5.45) | 7.56 (7.80 / 5.42; 2.28) | 0.076 (0.071 / 0.097; 0.007) (1) |
| 0.15 | 200 | 5 | 18.28 (18.72 / 14.53; 6.19) | 14.90 (15.32 / 10.95; 5.52) | 8.29 (8.54 / 6.03; 3.08) | not measured |
| 0.15 | 300 | 5 | 17.80 (18.03 / 14.55; 6.04) | 14.44 (14.67 / 10.89; 5.53) | 8.53 (8.68 / 5.92; 3.50) | not measured |
| 0.2 | 50 | 5 | 22.18 (22.47 / 19.95; 8.77) | 16.71 (16.91 / 15.24; 6.82) | 6.62 (6.58 / 7.39; 1.93) | 0.084 (0.058 / 0.197; 0.007) (1) |
| 0.2 | 100 | 5 | 23.99 (24.47 / 20.43; 8.61) | 19.21 (19.59 / 16.34; 7.33) | 8.30 (8.43 / 7.80; 2.51) | 0.026 (0.021 / 0.099; 0.005) (1) |
| 0.2 | 200 | 3 | 23.65 (23.95 / 20.27; 8.27) | 20.08 (20.44 / 15.53; 7.44) | 10.19 (10.37 / 7.81; 3.73) | not measured |
| 0.2 | 300 | 2 | 21.17 (21.39 / 19.02; 7.95) | 17.96 (18.19 / 14.94; 7.32) | 9.65 (9.79 / 7.60; 4.27) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 110.9, 257 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.48 | 0.564 | 2.61 |
| + two-body | 1500 | 0.03 | 0.041 | 0.10 |
| + many-body | 1500 | 0.03 | 0.041 | 0.10 |
| MFS Xfine (the truth's own error) | 1500 | 0.002 | 0.0031 | 0.027 |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 152 steps, fell 18.2, 137 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 87 | 4.14 | 0.905 | 5.57 |
| + two-body | 152 | 0.63 | 0.361 | 5.23 |
| + many-body | 152 | 0.29 | 0.216 | 3.12 |
| MFS Xfine (the truth's own error) | 152 | 0.004 | 0.0029 | 0.202 |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
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
| + two-body | 1.1e-16 | 0.7450 | 8.4e-16 | 5.63 |
| + many-body | 1.2e-16 | 0.8795 | 8.5e-16 | 2.84 |
| MFS fine (the truth) | 3.1e-04 | 1 | | 0 |
| MFS Xfine | 2.9e-05 | 0.9996 | | 0.020 (= the error of the fine truth) |

MFS smallest eigenvalue 1.6464e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
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
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 16 of 20; -0.967 / 0.731 | 19 of 20; -0.111 / 0.891 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 9 of 20; -1.418 / -0.022 | 17 of 20; -0.204 / 0.411 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 5 of 20; -0.877 / -0.268 | 16 of 20; -0.117 / 0.392 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 7 of 20; -1.577 / -0.216 | 18 of 20; -0.197 / 0.661 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.381 / -1.250 | 13 of 20; -2.552 / 0.168 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.233 / -1.848 | 11 of 20; -1.662 / 0.047 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.224 / -2.283 | 10 of 20; -0.849 / 0.007 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.469 / -2.903 | 7 of 20; -1.259 / -0.172 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.729 / -4.089 | 0 of 20; -2.683 / -2.167 |
| 0.2 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.273 / -2.955 | 3 of 20; -1.688 / -0.577 |
| 0.2 | 50 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -8.109 / -4.691 | 0 of 19; -2.644 / -0.962 |
| 0.2 | 100 | 13 | 13 of 13; 1.000 / 1.000 | 0 of 13; -6.993 / -5.812 | 0 of 13; -5.093 / -4.382 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 0 | -8.109 | 0.81 | oblateSpheroid, oblate_ar3 | 2.43 | 1.125 | 2.22e-03 / 9.07e-04 (0.409) | 0.356, 0.478 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 17 | -5.093 | 0.07 | oblateSpheroid_x1p5, oblateSpheroid_x1p5 | 3.85 | 1.323 | 1.93e-03 / 1.91e-03 (0.987) | 0.739, 0.851 (11 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 400 | 400 | 0.994 / 1.000 | 1.052, 2.22 |
| prolate_ar2__prolate_ar2_test | 400 | 400 | 0.991 / 1.000 | 1.053, 2.40 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.977 / 1.000 | 1.052, 2.35 |
| prolate_ar4__prolate_ar4_test | 400 | 400 | 0.966 / 1.000 | 1.055, 4.04 |
| oblate_ar1p5__oblate_ar1p5_test | 400 | 400 | 0.966 / 1.000 | 1.053, 2.23 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.993 / 1.000 | 1.061, 2.69 |
| oblate_ar3__oblate_ar3_test | 400 | 400 | 0.899 / 1.000 | 1.080, 3.26 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.982 / 1.000 | 1.055, 2.48 |
| prolate_ar2__oblateSpheroid_test | 400 | 400 | 0.987 / 1.000 | 1.053, 2.78 |
| prolate_ar4__oblate_ar3_test | 400 | 400 | 0.791 / 1.000 | 1.052, 5.20 |
| prolate_ar2__oblate_ar1p5_test | 400 | 400 | 0.967 / 1.000 | 1.051, 2.40 |
| prolate_ar1p5__oblate_ar3_test | 400 | 400 | 0.913 / 1.000 | 1.057, 2.22 |
| prolateSpheroid__prolate_ar2_test | 400 | 400 | 0.981 / 1.000 | 1.051, 4.04 |
| oblateSpheroid__oblate_ar3_test | 400 | 400 | 0.878 / 1.000 | 1.062, 2.70 |
| prolate_ar4__oblateSpheroid_test | 400 | 400 | 0.953 / 1.000 | 1.056, 3.66 |
| prolateSpheroid__oblate_ar1p5_test | 400 | 400 | 0.984 / 1.000 | 1.059, 3.62 |
| prolateSpheroid_x0p75__prolateSpheroid_test | 400 | 400 | 0.970 / 1.000 | 1.051, 3.26 |
| oblateSpheroid_x1p5__oblateSpheroid_test | 400 | 400 | 0.992 / 1.000 | 1.055, 3.49 |
| prolate_ar2_x1p5__prolate_ar2_test | 400 | 400 | 0.992 / 1.000 | 1.058, 3.35 |
| oblate_ar3_x0p75__oblate_ar3_test | 400 | 400 | 0.525 / 1.000 | 1.061, 2.64 |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 400 | 400 | 0.984 / 1.000 | 1.057, 4.21 |
| prolate_ar2_x1p5__oblateSpheroid_test | 400 | 400 | 0.950 / 1.000 | 1.056, 2.74 |
| prolate_ar2__oblate_ar3_test | 400 | 400 | 0.465 / 1.000 | 1.061, 2.31 |
| prolate_ar4__oblate_ar1p5_test | 400 | 400 | 0.573 / 0.996 | 1.051, 2.20 |
| prolate_ar2p5__oblate_ar2p5_test | 400 | 400 | 0.390 / 1.000 | 1.055, 2.19 |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 400 | 400 | 0.969 / 1.000 | 1.052, 2.94 |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 400 | 400 | 0.503 / 0.999 | 1.054, 3.37 |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 400 | 400 | 0.880 / 1.000 | 1.058, 2.68 |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
- **Configurations**: N in [16, 50, 100], shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.46 (7.68 / 5.52) | 4.47 (4.65 / 2.81) | 2.84 (2.93 / 1.97) | 2.11 (2.20 / 1.20) | 2.04 (2.13 / 1.08) |
| 0.1 | 64 | 3 | 12.66 (12.88 / 10.49) | 8.58 (8.75 / 6.77) | 4.54 (4.59 / 4.04) | 3.19 (3.29 / 2.01) | 3.01 (3.11 / 1.80) |
| 0.2 | 64 | 3 | 20.39 (20.43 / 20.05) | 15.71 (15.74 / 15.22) | 5.89 (5.82 / 6.96) | 3.90 (3.92 / 3.46) | 3.48 (3.52 / 2.50) |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 168,500 ordered pairs from 267 clusters `poly` (mean 30.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,080 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.391 % -> 1.749 %.
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

#### Two-body accuracy of `data/final/models/pair_t123.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4096 | 0.061 | 0.296 | 0.072 | 0.75 | 4.33 / 11.49 | 0.078 / 0.456 (512) | 0.063 / 0.352 | 0.041 / 0.300 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.096 / 0.428 (660) | 0.047 / 0.215 (956) | 0.032 / 0.142 (738) | 0.031 / 0.138 (698) | 0.035 / 0.150 (960) | 0.051 / 0.222 (84) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.152 / 0.755 (68) | 0.035 / 0.157 (130) | 0.014 / 0.071 (86) | 0.008 / 0.033 (72) | 0.005 / 0.027 (142) | - |

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
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
| 0.025 | 200 | 10 | 4.17 (4.13 / 6.00; 1.18) | 2.76 (2.75 / 3.73; 0.99) | 1.82 (1.81 / 2.31; 0.73) | 0.019 (0.017 / 0.066; 0.001) (1) |
| 0.05 | 200 | 10 | 7.10 (7.05 / 10.32; 2.18) | 5.26 (5.24 / 7.10; 1.90) | 3.05 (3.03 / 4.16; 1.18) | 0.026 (0.021 / 0.112; 0.002) (1) |
| 0.075 | 200 | 10 | 11.46 (11.41 / 14.76; 3.20) | 8.84 (8.80 / 11.25; 2.84) | 4.42 (4.40 / 5.57; 1.50) | 0.050 (0.040 / 0.174; 0.003) (1) |
| 0.1 | 200 | 10 | 14.34 (14.26 / 19.33; 4.16) | 11.69 (11.63 / 15.91; 3.71) | 5.57 (5.54 / 7.28; 1.77) | 0.036 (0.033 / 0.130; 0.003) (1) |
| 0.15 | 200 | 10 | 18.49 (18.36 / 29.27; 5.94) | 15.36 (15.24 / 24.85; 5.35) | 6.41 (6.37 / 9.96; 2.15) | 0.051 (0.041 / 0.332; 0.005) (1) |
| 0.2 | 200 | 10 | 26.45 (26.26 / 39.97; 7.71) | 22.99 (22.84 / 34.70; 6.98) | 8.67 (8.61 / 12.83; 2.56) | 0.093 (0.080 / 0.393; 0.006) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
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
| 0.05 | 50 | 5 | 7.28 (7.23 / 9.70; 2.35) | 4.64 (4.60 / 6.29; 1.75) | 2.18 (2.15 / 3.29; 0.77) | 0.027 (0.025 / 0.064; 0.002) (1) |
| 0.05 | 100 | 5 | 6.54 (6.48 / 9.85; 2.38) | 4.52 (4.48 / 6.80; 1.94) | 2.35 (2.32 / 3.58; 0.95) | 0.026 (0.024 / 0.112; 0.002) (1) |
| 0.05 | 200 | 5 | 6.73 (6.68 / 10.08; 2.18) | 5.05 (5.02 / 7.01; 1.91) | 2.91 (2.89 / 4.15; 1.19) | not measured |
| 0.05 | 300 | 5 | 7.09 (7.04 / 10.06; 2.17) | 5.43 (5.41 / 7.33; 1.96) | 3.29 (3.28 / 4.36; 1.37) | not measured |
| 0.1 | 50 | 5 | 12.27 (12.15 / 18.29; 4.42) | 8.91 (8.81 / 13.97; 3.41) | 2.94 (2.87 / 5.98; 1.35) | 0.031 (0.027 / 0.134; 0.004) (1) |
| 0.1 | 100 | 5 | 13.12 (13.02 / 18.29; 4.22) | 10.24 (10.15 / 14.68; 3.55) | 4.30 (4.25 / 6.97; 1.31) | 0.050 (0.040 / 0.238; 0.003) (1) |
| 0.1 | 200 | 5 | 12.81 (12.73 / 18.45; 4.06) | 10.49 (10.42 / 15.20; 3.62) | 5.08 (5.05 / 7.06; 1.74) | not measured |
| 0.1 | 300 | 5 | 11.26 (11.17 / 19.21; 4.01) | 9.38 (9.31 / 15.81; 3.67) | 4.82 (4.79 / 7.80; 2.10) | not measured |
| 0.15 | 50 | 5 | 15.15 (14.91 / 27.20; 5.82) | 11.96 (11.76 / 21.85; 4.57) | 3.86 (3.74 / 8.62; 1.59) | 0.047 (0.039 / 0.204; 0.005) (1) |
| 0.15 | 100 | 5 | 18.74 (18.57 / 28.19; 6.23) | 15.03 (14.87 / 23.67; 5.32) | 4.93 (4.85 / 8.98; 1.57) | 0.065 (0.058 / 0.232; 0.006) (1) |
| 0.15 | 200 | 5 | 19.15 (19.02 / 29.64; 5.98) | 15.78 (15.66 / 24.97; 5.38) | 6.64 (6.59 / 10.22; 2.18) | not measured |
| 0.15 | 300 | 5 | 17.04 (16.90 / 29.29; 5.94) | 14.61 (14.49 / 25.15; 5.47) | 6.64 (6.60 / 10.47; 2.72) | not measured |
| 0.2 | 50 | 5 | 23.43 (23.13 / 39.41; 7.91) | 18.70 (18.42 / 32.91; 6.32) | 4.95 (4.79 / 11.39; 1.42) | 0.040 (0.031 / 0.363; 0.012) (1) |
| 0.2 | 100 | 5 | 25.51 (25.28 / 37.89; 7.69) | 21.25 (21.02 / 33.12; 6.60) | 6.96 (6.86 / 11.74; 1.85) | 0.070 (0.064 / 0.191; 0.004) (1) |
| 0.2 | 200 | 5 | 29.95 (29.80 / 40.55; 7.67) | 25.88 (25.74 / 35.52; 6.94) | 9.53 (9.48 / 12.90; 2.54) | not measured |
| 0.2 | 300 | 5 | 24.75 (24.55 / 40.40; 7.70) | 21.81 (21.63 / 35.55; 7.13) | 9.45 (9.40 / 13.57; 3.35) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 81.1, 248 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.03 | 0.034 | 0.26 |
| + two-body | 1500 | 0.00 | 0.004 | 0.18 |
| + many-body | 1500 | 0.00 | 0.004 | 0.18 |
| MFS Xfine (the truth's own error) | 1500 | 0.013 | 0.0119 | 0.285 |

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: triaxial_123, triaxial_123.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

#### Dynamics: ring of triaxial_123, triaxial_123, triaxial_123, triaxial_123, triaxial_123 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 356 steps, fell 45.8, 272 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 99 | 6.14 | 1.043 | 18.67 |
| + two-body | 124 | 2.41 | 0.689 | 13.74 |
| + many-body | 164 | 0.09 | 0.168 | 3.39 |
| MFS Xfine (the truth's own error) | 356 | 0.014 | 0.0115 | 0.240 |

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
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
| + two-body | 8.6e-17 | 0.7005 | 6.5e-16 | 4.84 |
| + many-body | 9.3e-17 | 0.9844 | 6.5e-16 | 1.60 |
| MFS fine (the truth) | 1.9e-04 | 1 | | 0 |
| MFS Xfine | 6.5e-05 | 1.0008 | | 0.014 (= the error of the fine truth) |

MFS smallest eigenvalue 2.3143e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
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
| 0.05 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 18 of 20; -0.658 / 0.552 | 20 of 20; 0.289 / 0.697 |
| 0.05 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 12 of 20; -1.092 / 0.160 | 19 of 20; -0.048 / 0.519 |
| 0.05 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 3 of 20; -1.090 / -0.135 | 19 of 20; -0.015 / 0.457 |
| 0.1 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 6 of 20; -0.877 / -0.277 | 20 of 20; 0.307 / 0.519 |
| 0.1 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.135 / -1.233 | 18 of 20; -0.089 / 0.227 |
| 0.1 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -2.092 / -1.462 | 13 of 20; -0.093 / 0.034 |
| 0.15 | 16 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.004 / -1.357 | 19 of 20; -0.053 / 0.331 |
| 0.15 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -3.379 / -2.425 | 17 of 20; -0.465 / 0.138 |
| 0.15 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.239 / -2.807 | 0 of 20; -2.401 / -1.829 |
| 0.2 | 16 | 19 | 19 of 19; 1.000 / 1.000 | 0 of 19; -3.510 / -2.624 | 14 of 19; -0.122 / 0.115 |
| 0.2 | 50 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -4.209 / -3.459 | 8 of 20; -0.532 / -0.053 |
| 0.2 | 100 | 20 | 20 of 20; 1.000 / 1.000 | 0 of 20; -5.355 / -4.463 | 0 of 20; -3.713 / -3.062 |

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 9 | -5.355 | 0.68 | triaxial_123, triaxial_123 | 4.60 | 1.052 | 2.41e-03 / 7.94e-04 (0.329) | 0.349, 0.412 (8 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 17 | -3.713 | 0.05 | triaxial_123, triaxial_123 | 9.28 | 2.168 | 3.75e-03 / 3.74e-03 (0.999) | 0.831, 0.659 (5 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.962 / 1.000 | 1.065, 3.07 |

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_123

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.14 (7.10 / 10.29) | 5.05 (5.04 / 6.55) | 2.23 (2.21 / 3.45) | 1.72 (1.73 / 1.92) | 1.66 (1.66 / 1.84) |
| 0.1 | 64 | 3 | 10.74 (10.61 / 20.10) | 7.99 (7.85 / 16.88) | 3.00 (2.93 / 7.02) | 2.32 (2.31 / 3.37) | 2.21 (2.20 / 2.85) |
| 0.2 | 64 | 3 | 23.64 (23.36 / 37.66) | 18.75 (18.45 / 32.13) | 5.40 (5.27 / 10.62) | 4.50 (4.47 / 6.30) | 3.74 (3.74 / 3.70) |

##### Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
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

#### Two-body accuracy of `data/final/models/pair_multi.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4096 | 0.075 | 0.364 | 0.088 | 0.97 | 4.33 / 11.49 | 0.078 / 0.456 (512) | 0.074 / 0.412 | 0.041 / 0.300 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4096 | 0.073 | 0.385 | 0.096 | 0.71 | 5.19 / 10.76 | 0.020 / 0.099 (512) | 0.069 / 0.370 | 0.009 / 0.054 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4096 | 0.117 | 0.590 | 0.141 | 1.34 | 4.76 / 11.86 | 0.105 / 0.504 (512) | 0.134 / 0.705 | 0.066 / 0.401 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4096 | 0.141 | 0.770 | 0.165 | 2.03 | 4.17 / 12.25 | 0.076 / 0.342 (512) | 0.137 / 0.670 | 0.051 / 0.347 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4096 | 0.216 | 1.249 | 0.249 | 3.16 | 4.19 / 14.75 | 0.060 / 0.333 (512) | 0.220 / 1.306 | 0.047 / 0.339 | 0.0 % |
| triaxial_3_4__triaxial_3_4_test | 4096 | 0.147 | 0.761 | 0.163 | 2.52 | 3.65 / 11.65 | 0.081 / 0.448 (512) | 0.134 / 0.644 | 0.042 / 0.234 | 0.0 % |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 4096 | 0.161 | 0.792 | 0.181 | 1.91 | 3.95 / 11.58 | 0.048 / 0.256 (512) | 0.149 / 0.627 | 0.050 / 0.324 | 0.0 % |
| triaxial_3_6__triaxial_3_6_test | 4096 | 1.907 | 12.369 | 2.143 | 17.25 | 3.75 / 14.30 | 0.037 / 0.216 (512) | 1.894 / 12.803 | 0.026 / 0.178 | 100.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.116 / 0.502 (660) | 0.057 / 0.283 (956) | 0.045 / 0.223 (738) | 0.042 / 0.220 (698) | 0.049 / 0.250 (960) | 0.071 / 0.303 (84) |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.097 / 0.460 (622) | 0.073 / 0.360 (908) | 0.053 / 0.302 (678) | 0.041 / 0.244 (664) | 0.040 / 0.249 (1008) | 0.052 / 0.262 (216) |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.165 / 0.727 (726) | 0.094 / 0.495 (866) | 0.081 / 0.473 (620) | 0.076 / 0.431 (752) | 0.089 / 0.448 (1004) | 0.097 / 0.494 (128) |
| triaxial_2_4__triaxial_2_4_test | 0.205 / 1.060 (728) | 0.116 / 0.599 (978) | 0.093 / 0.471 (750) | 0.090 / 0.467 (774) | 0.105 / 0.559 (816) | 0.121 / 0.688 (50) |
| triaxial_2_5__triaxial_2_5_test | 0.306 / 1.593 (792) | 0.192 / 1.083 (992) | 0.142 / 0.882 (728) | 0.138 / 0.813 (774) | 0.143 / 0.938 (772) | 0.154 / 1.385 (38) |
| triaxial_3_4__triaxial_3_4_test | 0.208 / 1.027 (788) | 0.128 / 0.638 (954) | 0.096 / 0.455 (850) | 0.090 / 0.426 (746) | 0.095 / 0.442 (738) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.214 / 1.022 (792) | 0.152 / 0.693 (932) | 0.117 / 0.502 (778) | 0.106 / 0.428 (776) | 0.096 / 0.412 (776) | 0.128 / 0.543 (42) |
| triaxial_3_6__triaxial_3_6_test | 2.289 / 13.932 (886) | 1.938 / 12.458 (1090) | 1.639 / 10.790 (820) | 1.436 / 9.591 (752) | 1.220 / 7.912 (528) | - |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.152 / 0.755 (68) | 0.035 / 0.157 (130) | 0.014 / 0.071 (86) | 0.008 / 0.033 (72) | 0.005 / 0.027 (142) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.040 / 0.174 (70) | 0.004 / 0.020 (136) | 0.001 / 0.004 (72) | 0.001 / 0.003 (84) | 0.000 / 0.002 (122) | 0.000 / 0.001 (28) |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.173 / 0.731 (98) | 0.050 / 0.171 (82) | 0.013 / 0.038 (78) | 0.007 / 0.028 (92) | 0.003 / 0.014 (148) | - |
| triaxial_2_4__triaxial_2_4_test | 0.141 / 0.564 (84) | 0.038 / 0.217 (118) | 0.014 / 0.082 (80) | 0.008 / 0.031 (124) | 0.006 / 0.024 (100) | - |
| triaxial_2_5__triaxial_2_5_test | 0.093 / 0.479 (112) | 0.045 / 0.237 (128) | 0.018 / 0.084 (76) | 0.013 / 0.058 (96) | 0.010 / 0.061 (96) | - |
| triaxial_3_4__triaxial_3_4_test | 0.125 / 0.661 (118) | 0.056 / 0.228 (108) | 0.026 / 0.118 (106) | 0.016 / 0.072 (90) | 0.010 / 0.056 (88) | - |
| triaxial_2p5_3p5__triaxial_2p5_3p5_test | 0.083 / 0.360 (82) | 0.040 / 0.222 (128) | 0.021 / 0.132 (104) | 0.013 / 0.090 (100) | 0.010 / 0.079 (96) | - |
| triaxial_3_6__triaxial_3_6_test | 0.056 / 0.352 (108) | 0.031 / 0.106 (144) | 0.022 / 0.107 (100) | 0.017 / 0.073 (92) | 0.011 / 0.055 (62) | - |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_2p5_3p5__triaxial_2p5_3p5_test`: triaxial_2p5_3p5 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_3_6__triaxial_3_6_test`: triaxial_3_6 (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
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
| 0.025 | 200 | 10 | 4.26 (4.23 / 6.75; 1.23) | 2.83 (2.82 / 3.94; 1.06) | 2.03 (2.02 / 2.87; 0.82) | 0.030 (0.027 / 0.110; 0.002) (1) |
| 0.05 | 200 | 10 | 7.39 (7.35 / 11.21; 2.21) | 5.60 (5.58 / 8.22; 1.95) | 3.54 (3.52 / 5.13; 1.33) | 0.022 (0.017 / 0.154; 0.002) (1) |
| 0.075 | 200 | 10 | 10.27 (10.21 / 16.24; 3.37) | 8.11 (8.06 / 12.82; 3.02) | 4.77 (4.75 / 7.31; 1.81) | 0.042 (0.038 / 0.169; 0.003) (1) |
| 0.1 | 200 | 10 | 15.01 (14.94 / 20.82; 4.30) | 12.24 (12.17 / 17.44; 3.87) | 6.41 (6.38 / 8.87; 2.12) | 0.063 (0.058 / 0.283; 0.004) (1) |
| 0.15 | 200 | 10 | 20.54 (20.40 / 31.24; 6.03) | 17.12 (17.00 / 27.00; 5.45) | 8.14 (8.09 / 12.10; 2.58) | 0.068 (0.062 / 0.283; 0.005) (1) |
| 0.2 | 200 | 10 | 23.62 (23.47 / 43.11; 7.82) | 20.42 (20.28 / 38.41; 7.10) | 9.08 (9.02 / 16.38; 3.10) | 0.101 (0.091 / 0.426; 0.008) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
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
| 0.05 | 50 | 5 | 7.70 (7.65 / 10.07; 2.54) | 5.01 (4.95 / 7.43; 1.89) | 2.38 (2.33 / 4.25; 0.87) | 0.024 (0.021 / 0.086; 0.003) (1) |
| 0.05 | 100 | 5 | 6.64 (6.59 / 11.40; 2.43) | 4.84 (4.81 / 8.03; 1.99) | 2.85 (2.82 / 5.10; 1.05) | 0.023 (0.020 / 0.142; 0.003) (1) |
| 0.05 | 200 | 5 | 7.03 (7.00 / 10.91; 2.22) | 5.36 (5.33 / 8.03; 1.97) | 3.51 (3.50 / 5.07; 1.36) | not measured |
| 0.05 | 300 | 5 | 8.11 (8.08 / 11.58; 2.27) | 6.41 (6.39 / 8.64; 2.06) | 4.40 (4.39 / 5.51; 1.54) | not measured |
| 0.1 | 50 | 5 | 9.41 (9.29 / 19.10; 4.70) | 7.01 (6.91 / 15.21; 3.65) | 2.93 (2.86 / 7.51; 1.29) | 0.027 (0.024 / 0.143; 0.006) (1) |
| 0.1 | 100 | 5 | 12.62 (12.52 / 19.92; 4.42) | 9.76 (9.67 / 16.23; 3.77) | 4.66 (4.60 / 8.30; 1.68) | 0.021 (0.018 / 0.127; 0.003) (1) |
| 0.1 | 200 | 5 | 14.68 (14.61 / 20.70; 4.29) | 12.00 (11.93 / 17.43; 3.85) | 6.26 (6.22 / 9.12; 2.08) | not measured |
| 0.1 | 300 | 5 | 12.91 (12.84 / 21.12; 4.18) | 10.74 (10.68 / 17.93; 3.84) | 6.38 (6.36 / 9.54; 2.40) | not measured |
| 0.15 | 50 | 5 | 15.97 (15.80 / 29.98; 6.19) | 12.47 (12.32 / 24.53; 4.92) | 4.46 (4.37 / 10.24; 1.57) | 0.055 (0.051 / 0.233; 0.014) (1) |
| 0.15 | 100 | 5 | 21.12 (20.99 / 32.08; 6.33) | 17.17 (17.04 / 27.55; 5.42) | 7.06 (7.00 / 12.08; 1.86) | 0.056 (0.051 / 0.307; 0.006) (1) |
| 0.15 | 200 | 5 | 20.67 (20.54 / 31.47; 5.92) | 17.47 (17.35 / 27.18; 5.35) | 8.62 (8.57 / 12.44; 2.55) | not measured |
| 0.15 | 300 | 5 | 20.00 (19.89 / 32.46; 6.20) | 17.27 (17.17 / 28.58; 5.74) | 9.13 (9.09 / 13.44; 3.15) | not measured |
| 0.2 | 50 | 5 | 22.32 (22.02 / 39.78; 7.74) | 17.89 (17.62 / 33.78; 6.21) | 5.84 (5.70 / 13.19; 1.83) | 0.102 (0.091 / 0.373; 0.013) (1) |
| 0.2 | 100 | 5 | 22.81 (22.57 / 41.98; 7.72) | 19.12 (18.93 / 35.42; 6.65) | 7.48 (7.41 / 14.01; 2.23) | 0.077 (0.064 / 0.373; 0.007) (1) |
| 0.2 | 200 | 5 | 22.68 (22.50 / 43.29; 7.79) | 19.46 (19.28 / 38.87; 7.08) | 8.74 (8.68 / 16.56; 3.10) | not measured |
| 0.2 | 300 | 5 | 25.40 (25.26 / 44.42; 7.88) | 22.65 (22.52 / 39.99; 7.31) | 11.23 (11.19 / 17.76; 3.76) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 69.2, 379 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.01 | 0.012 | 0.07 |
| + two-body | 1500 | 0.01 | 0.014 | 0.08 |
| + many-body | 1500 | 0.01 | 0.014 | 0.08 |
| MFS Xfine (the truth's own error) | 1500 | 0.007 | 0.0139 | 0.147 |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 449 steps, fell 51.4, 649 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 119 | 6.59 | 1.208 | 22.08 |
| + two-body | 154 | 2.60 | 0.816 | 15.96 |
| + many-body | 165 | 1.16 | 0.361 | 4.23 |
| MFS Xfine (the truth's own error) | 449 | 0.007 | 0.0063 | 0.358 |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
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
| + two-body | 8.7e-17 | 0.3586 | 4.4e-16 | 5.08 |
| + many-body | 8.9e-17 | 0.9310 | 4.6e-16 | 1.93 |
| MFS fine (the truth) | 2.6e-04 | 1 | | 0 |
| MFS Xfine | 6.1e-05 | 0.9981 | | 0.021 (= the error of the fine truth) |

MFS smallest eigenvalue 1.1028e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 50 | 11 | -14.237 | 0.75 | triaxial_2_4, triaxial_2_4 | 2.69 | 1.051 | 1.60e-03 / 2.25e-04 (0.140) | 0.432, 0.452 (3 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 11 | -6.364 | 0.05 | triaxial_2_4, triaxial_2_4 | 10.01 | 3.110 | 2.01e-03 / 2.01e-03 (0.998) | 0.791, 0.596 (4 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

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

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_2_4 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_2_4

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 6.41 (6.36 / 10.70) | 4.43 (4.38 / 8.20) | 2.36 (2.32 / 4.73) | 1.98 (1.97 / 3.03) | 1.94 (1.93 / 3.01) |
| 0.1 | 64 | 3 | 13.20 (13.06 / 21.56) | 9.98 (9.88 / 15.87) | 4.19 (4.12 / 7.75) | 3.43 (3.42 / 4.44) | 3.25 (3.24 / 3.75) |
| 0.2 | 64 | 2 | 33.16 (32.93 / 45.73) | 26.63 (26.38 / 39.17) | 9.05 (8.91 / 15.16) | 7.19 (7.19 / 7.76) | 6.53 (6.55 / 5.32) |

##### Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
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

#### Two-body accuracy of `data/final/models/pair_mixed.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4096 | 0.080 | 0.378 | 0.093 | 1.00 | 4.33 / 11.49 | 0.078 / 0.456 (512) | 0.079 / 0.424 | 0.041 / 0.300 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.125 | 0.807 | 0.175 | 1.12 | 4.70 / 11.56 | 0.023 / 0.232 (512) | 0.124 / 0.793 | 0.005 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.097 | 0.655 | 0.137 | 0.83 | 4.94 / 11.24 | 0.013 / 0.034 (512) | 0.101 / 0.661 | 0.003 / 0.018 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4096 | 0.119 | 0.634 | 0.150 | 1.24 | 4.49 / 11.89 | 0.064 / 0.343 (512) | 0.133 / 0.799 | 0.053 / 0.375 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4096 | 0.088 | 0.464 | 0.112 | 0.96 | 4.55 / 11.24 | 0.070 / 0.326 (512) | 0.091 / 0.453 | 0.040 / 0.301 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4096 | 1.553 | 8.890 | 2.045 | 12.32 | 4.88 / 11.24 | 0.015 / 0.063 (512) | 1.477 / 9.127 | 0.004 / 0.022 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.122 / 0.525 (660) | 0.063 / 0.290 (956) | 0.049 / 0.227 (738) | 0.048 / 0.224 (698) | 0.052 / 0.254 (960) | 0.080 / 0.341 (84) |
| prolateSpheroid__prolateSpheroid_test | 0.162 / 0.984 (648) | 0.119 / 0.713 (854) | 0.097 / 0.667 (656) | 0.096 / 0.645 (644) | 0.088 / 0.678 (1018) | 0.094 / 0.675 (276) |
| oblateSpheroid__oblateSpheroid_test | 0.130 / 0.771 (626) | 0.102 / 0.635 (908) | 0.065 / 0.533 (704) | 0.039 / 0.397 (682) | 0.035 / 0.316 (1050) | 0.067 / 0.246 (126) |
| triaxial_123__prolateSpheroid_test | 0.169 / 0.826 (686) | 0.102 / 0.509 (904) | 0.079 / 0.450 (628) | 0.072 / 0.406 (702) | 0.079 / 0.465 (1056) | 0.088 / 0.594 (120) |
| triaxial_123__oblateSpheroid_test | 0.135 / 0.599 (664) | 0.069 / 0.395 (930) | 0.056 / 0.340 (744) | 0.048 / 0.322 (670) | 0.051 / 0.284 (1000) | 0.059 / 0.308 (88) |
| prolateSpheroid__oblateSpheroid_test | 1.857 / 9.691 (718) | 1.610 / 8.966 (880) | 1.348 / 7.805 (678) | 1.081 / 6.625 (676) | 0.806 / 5.510 (944) | 0.642 / 4.493 (200) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.152 / 0.755 (68) | 0.035 / 0.157 (130) | 0.014 / 0.071 (86) | 0.008 / 0.033 (72) | 0.005 / 0.027 (142) | - |
| prolateSpheroid__prolateSpheroid_test | 0.042 / 0.373 (76) | 0.006 / 0.021 (96) | 0.002 / 0.006 (76) | 0.002 / 0.006 (84) | 0.001 / 0.005 (140) | 0.001 / 0.005 (40) |
| oblateSpheroid__oblateSpheroid_test | 0.024 / 0.057 (64) | 0.008 / 0.017 (102) | 0.001 / 0.005 (104) | 0.001 / 0.003 (76) | 0.001 / 0.003 (150) | - |
| triaxial_123__prolateSpheroid_test | 0.114 / 0.590 (78) | 0.045 / 0.170 (132) | 0.014 / 0.048 (80) | 0.008 / 0.030 (92) | 0.004 / 0.025 (114) | - |
| triaxial_123__oblateSpheroid_test | 0.127 / 0.519 (86) | 0.029 / 0.110 (116) | 0.016 / 0.050 (102) | 0.008 / 0.030 (84) | 0.005 / 0.026 (112) | - |
| prolateSpheroid__oblateSpheroid_test | 0.026 / 0.095 (98) | 0.004 / 0.014 (108) | 0.002 / 0.006 (82) | 0.001 / 0.004 (94) | 0.001 / 0.004 (116) | - |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
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
| 0.025 | 200 | 10 | 4.36 (4.35 / 4.92; 1.17) | 2.82 (2.82 / 2.80; 0.99) | 1.80 (1.80 / 1.76; 0.69) | 0.022 (0.019 / 0.056; 0.001) (1) |
| 0.05 | 200 | 10 | 7.47 (7.45 / 8.25; 2.23) | 5.57 (5.58 / 5.71; 1.96) | 3.10 (3.10 / 3.28; 1.14) | 0.013 (0.012 / 0.040; 0.001) (1) |
| 0.075 | 200 | 10 | 10.20 (10.18 / 11.62; 3.16) | 8.01 (8.00 / 8.80; 2.81) | 3.84 (3.83 / 4.60; 1.41) | 0.036 (0.033 / 0.065; 0.001) (1) |
| 0.1 | 200 | 10 | 13.82 (13.80 / 14.89; 4.19) | 11.08 (11.07 / 11.77; 3.75) | 4.83 (4.81 / 5.54; 1.59) | 0.034 (0.030 / 0.120; 0.002) (1) |
| 0.15 | 200 | 10 | 16.28 (16.15 / 22.42; 5.98) | 13.82 (13.71 / 18.83; 5.40) | 5.44 (5.38 / 8.11; 1.91) | 0.049 (0.041 / 0.156; 0.004) (1) |
| 0.2 | 200 | 10 | 25.10 (24.99 / 31.54; 7.59) | 21.63 (21.53 / 27.26; 6.87) | 7.51 (7.44 / 10.58; 2.34) | 0.060 (0.048 / 0.251; 0.006) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
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
| 0.05 | 50 | 5 | 7.08 (7.08 / 7.39; 2.61) | 4.89 (4.88 / 5.36; 1.95) | 2.11 (2.08 / 2.81; 0.80) | 0.020 (0.020 / 0.029; 0.002) (1) |
| 0.05 | 100 | 5 | 6.83 (6.81 / 7.46; 2.35) | 4.89 (4.88 / 5.27; 1.95) | 2.39 (2.37 / 2.83; 0.86) | 0.032 (0.030 / 0.076; 0.002) (1) |
| 0.05 | 200 | 5 | 7.81 (7.80 / 8.58; 2.24) | 5.84 (5.85 / 5.91; 1.96) | 3.17 (3.17 / 3.44; 1.13) | not measured |
| 0.05 | 300 | 5 | 7.24 (7.22 / 8.24; 2.16) | 5.56 (5.56 / 5.67; 1.95) | 3.38 (3.38 / 3.44; 1.29) | not measured |
| 0.1 | 50 | 5 | 12.61 (12.55 / 14.44; 4.59) | 9.29 (9.21 / 11.61; 3.59) | 3.29 (3.23 / 4.60; 1.18) | 0.036 (0.032 / 0.086; 0.002) (1) |
| 0.1 | 100 | 5 | 11.73 (11.66 / 14.08; 4.09) | 8.87 (8.82 / 10.61; 3.44) | 3.69 (3.65 / 4.97; 1.16) | 0.028 (0.023 / 0.110; 0.004) (1) |
| 0.1 | 200 | 5 | 12.76 (12.72 / 14.53; 4.10) | 10.08 (10.05 / 11.49; 3.67) | 4.42 (4.39 / 5.39; 1.59) | not measured |
| 0.1 | 300 | 5 | 12.68 (12.62 / 15.32; 4.06) | 10.45 (10.41 / 12.16; 3.73) | 5.16 (5.14 / 6.04; 1.99) | not measured |
| 0.15 | 50 | 5 | 16.71 (16.57 / 21.87; 6.07) | 12.97 (12.84 / 17.43; 4.75) | 4.06 (3.92 / 7.15; 1.34) | 0.050 (0.042 / 0.117; 0.006) (1) |
| 0.15 | 100 | 5 | 16.75 (16.59 / 23.13; 6.08) | 13.81 (13.69 / 18.93; 5.20) | 4.30 (4.18 / 7.86; 1.46) | 0.032 (0.028 / 0.116; 0.004) (1) |
| 0.15 | 200 | 5 | 17.56 (17.44 / 22.21; 5.94) | 14.99 (14.90 / 18.74; 5.37) | 5.96 (5.90 / 8.21; 1.90) | not measured |
| 0.15 | 300 | 5 | 20.72 (20.67 / 23.72; 5.89) | 17.29 (17.24 / 19.81; 5.44) | 7.06 (7.04 / 8.18; 2.38) | not measured |
| 0.2 | 50 | 5 | 18.62 (18.35 / 29.33; 7.86) | 14.35 (14.07 / 24.73; 6.26) | 3.83 (3.63 / 9.23; 1.31) | 0.037 (0.030 / 0.165; 0.007) (1) |
| 0.2 | 100 | 5 | 24.91 (24.71 / 32.14; 7.83) | 20.67 (20.51 / 26.74; 6.75) | 6.32 (6.19 / 10.17; 1.67) | 0.048 (0.038 / 0.271; 0.006) (1) |
| 0.2 | 200 | 5 | 28.20 (28.19 / 30.89; 7.61) | 24.39 (24.38 / 26.81; 6.90) | 8.38 (8.32 / 10.74; 2.38) | not measured |
| 0.2 | 300 | 5 | 23.67 (23.54 / 33.15; 7.68) | 20.92 (20.81 / 28.97; 7.11) | 8.62 (8.59 / 11.32; 2.95) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 89.7, 247 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.09 | 0.094 | 0.31 |
| + two-body | 1500 | 0.02 | 0.017 | 0.17 |
| + many-body | 1500 | 0.02 | 0.017 | 0.17 |
| MFS Xfine (the truth's own error) | 1500 | 0.005 | 0.0104 | 0.283 |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 123 steps, fell 16.8, 108 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 41 | 5.25 | 0.472 | 7.59 |
| + two-body | 70 | 2.09 | 0.370 | 6.65 |
| + many-body | 83 | 0.37 | 0.129 | 3.39 |
| MFS Xfine (the truth's own error) | 123 | 0.006 | 0.0023 | 0.245 |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
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
| + two-body | 9.9e-17 | 0.6127 | 4.5e-16 | 5.40 |
| + many-body | 1.1e-16 | 0.9772 | 4.7e-16 | 1.99 |
| MFS fine (the truth) | 2.4e-04 | 1 | | 0 |
| MFS Xfine | 6.0e-05 | 0.9893 | | 0.019 (= the error of the fine truth) |

MFS smallest eigenvalue 1.8431e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -6.606 | 0.79 | oblateSpheroid, prolateSpheroid | 3.13 | 1.113 | 4.70e-03 / 1.84e-03 (0.391) | 0.440, 0.321 (12 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 5 | -2.150 | 0.05 | triaxial_123, triaxial_123 | 13.71 | inf | 3.78e-03 / 3.78e-03 (1.000) | 0.787, 0.855 (7 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

The 12 x 12 mobility matrix of two particles from the operator (far field + two-body model) and from MFS, on stored test pairs: how many are positive definite, and the smallest eigenvalue relative to MFS's.

| set | pairs | positive definite | smallest eigenvalue, operator / MFS: min / median | the worst pair: contact factor, distance |
|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 400 | 400 | 0.939 / 1.000 | 1.058, 2.74 |
| prolateSpheroid__prolateSpheroid_test | 400 | 400 | 0.984 / 1.000 | 1.052, 2.44 |
| oblateSpheroid__oblateSpheroid_test | 400 | 400 | 0.983 / 1.000 | 1.070, 2.51 |
| triaxial_123__prolateSpheroid_test | 400 | 400 | 0.949 / 1.000 | 1.065, 4.42 |
| triaxial_123__oblateSpheroid_test | 400 | 400 | 0.959 / 1.000 | 1.053, 4.05 |
| prolateSpheroid__oblateSpheroid_test | 400 | 400 | 0.773 / 1.000 | 1.064, 2.52 |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_123, prolateSpheroid, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.69 (7.65 / 8.50) | 5.05 (5.04 / 5.46) | 2.36 (2.34 / 2.88) | 1.69 (1.69 / 1.56) | 1.58 (1.59 / 1.21) |
| 0.1 | 64 | 3 | 13.26 (13.18 / 15.32) | 9.44 (9.34 / 11.60) | 3.71 (3.64 / 5.19) | 2.39 (2.39 / 2.42) | 2.17 (2.19 / 1.72) |
| 0.2 | 64 | 3 | 26.36 (26.15 / 35.18) | 21.92 (21.65 / 31.50) | 5.32 (5.13 / 9.70) | 3.57 (3.53 / 5.09) | 2.15 (2.18 / 1.62) |

##### Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
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

#### Two-body accuracy of `data/final/models/pair_poly.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4096 | 0.078 | 0.414 | 0.093 | 1.02 | 4.33 / 11.49 | 0.078 / 0.456 (512) | 0.077 / 0.438 | 0.041 / 0.300 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4096 | 0.070 | 0.383 | 0.094 | 0.74 | 5.19 / 10.76 | 0.020 / 0.099 (512) | 0.069 / 0.367 | 0.009 / 0.054 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4096 | 0.114 | 0.621 | 0.143 | 1.28 | 4.76 / 11.86 | 0.105 / 0.504 (512) | 0.135 / 0.739 | 0.066 / 0.401 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4096 | 0.146 | 0.836 | 0.169 | 2.13 | 4.17 / 12.25 | 0.076 / 0.342 (512) | 0.134 / 0.718 | 0.051 / 0.347 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4096 | 0.217 | 1.392 | 0.260 | 3.66 | 4.19 / 14.75 | 0.060 / 0.333 (512) | 0.211 / 1.376 | 0.047 / 0.339 | 0.0 % |
| triaxial_3_4__triaxial_3_4_test | 4096 | 0.150 | 0.829 | 0.171 | 2.92 | 3.65 / 11.65 | 0.081 / 0.448 (512) | 0.131 / 0.767 | 0.042 / 0.234 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.114 | 0.742 | 0.160 | 1.09 | 4.70 / 11.56 | 0.023 / 0.232 (512) | 0.120 / 0.747 | 0.005 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.097 | 0.665 | 0.138 | 0.84 | 4.94 / 11.24 | 0.013 / 0.034 (512) | 0.096 / 0.675 | 0.003 / 0.018 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4096 | 0.110 | 0.627 | 0.141 | 1.26 | 4.49 / 11.89 | 0.064 / 0.343 (512) | 0.120 / 0.765 | 0.053 / 0.375 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4096 | 0.091 | 0.515 | 0.117 | 1.09 | 4.55 / 11.24 | 0.070 / 0.326 (512) | 0.092 / 0.512 | 0.040 / 0.301 | 0.0 % |
| triaxial_123__triaxial_2_5_test | 4096 | 0.235 | 1.293 | 0.274 | 3.24 | 4.27 / 13.84 | 0.052 / 0.335 (512) | 0.230 / 1.234 | 0.049 / 0.329 | 0.0 % |
| prolateSpheroid__triaxial_2_5_test | 4096 | 0.323 | 1.763 | 0.359 | 3.52 | 4.23 / 15.35 | 0.164 / 1.050 (512) | 0.290 / 1.631 | 0.109 / 0.589 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4096 | 0.141 | 0.870 | 0.193 | 1.31 | 4.88 / 11.24 | 0.015 / 0.063 (512) | 0.120 / 0.768 | 0.004 / 0.022 | 0.0 % |
| triaxial_123__triaxial_1p5_2_test | 4096 | 0.109 | 0.550 | 0.133 | 1.32 | 4.59 / 11.65 | 0.067 / 0.291 (512) | 0.107 / 0.564 | 0.050 / 0.348 | 0.0 % |
| triaxial_123__triaxial_2_4_test | 4096 | 0.136 | 0.728 | 0.166 | 1.88 | 4.19 / 12.23 | 0.120 / 0.421 (512) | 0.171 / 0.780 | 0.049 / 0.343 | 0.0 % |
| triaxial_123__triaxial_3_4_test | 4096 | 0.183 | 0.950 | 0.210 | 2.87 | 3.82 / 12.33 | 0.102 / 0.658 (512) | 0.187 / 0.935 | 0.048 / 0.278 | 0.0 % |
| oblateSpheroid__triaxial_1p5_2_test | 4096 | 0.084 | 0.528 | 0.118 | 0.90 | 5.07 / 11.18 | 0.020 / 0.064 (512) | 0.088 / 0.464 | 0.006 / 0.039 | 0.0 % |
| prolateSpheroid__triaxial_2_4_test | 4096 | 0.179 | 0.968 | 0.219 | 2.22 | 4.17 / 13.14 | 0.131 / 0.596 (512) | 0.173 / 0.958 | 0.081 / 0.505 | 0.0 % |
| triaxial_2_5__triaxial_3_4_test | 4096 | 0.241 | 1.423 | 0.276 | 4.05 | 3.92 / 13.29 | 0.097 / 0.527 (512) | 0.260 / 1.451 | 0.042 / 0.287 | 0.0 % |
| triaxial_123_x0p75__triaxial_123_test | 4096 | 0.131 | 0.609 | 0.161 | 1.85 | 4.11 / 12.23 | 0.084 / 0.383 (512) | 0.142 / 0.687 | 0.052 / 0.339 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4096 | 0.102 | 0.752 | 0.134 | 1.19 | 4.48 / 10.87 | 0.027 / 0.081 (512) | 0.102 / 0.677 | 0.004 / 0.024 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_test | 4096 | 0.135 | 0.902 | 0.181 | 1.44 | 4.60 / 11.70 | 0.023 / 0.206 (512) | 0.137 / 0.890 | 0.005 / 0.029 | 0.0 % |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 4096 | 0.091 | 0.491 | 0.111 | 1.13 | 4.77 / 10.63 | 0.041 / 0.184 (512) | 0.101 / 0.538 | 0.015 / 0.103 | 0.0 % |
| triaxial_123_x0p75__prolateSpheroid_test | 4096 | 0.148 | 0.796 | 0.198 | 1.69 | 4.73 / 13.21 | 0.047 / 0.253 (512) | 0.151 / 0.754 | 0.045 / 0.289 | 0.0 % |
| oblateSpheroid_x1p5__triaxial_123_test | 4096 | 0.089 | 0.518 | 0.109 | 1.15 | 4.33 / 10.23 | 0.031 / 0.124 (512) | 0.088 / 0.462 | 0.022 / 0.143 | 0.0 % |
| oblateSpheroid__triaxial_2_5_test | 4096 | 0.793 | 4.203 | 0.936 | 6.32 | 4.34 / 14.63 | 0.090 / 0.487 (512) | 0.792 / 4.481 | 0.067 / 0.399 | 0.0 % |
| triaxial_1p5_2__triaxial_3_4_test | 4096 | 0.625 | 3.532 | 0.760 | 5.78 | 4.11 / 14.08 | 0.101 / 0.495 (512) | 0.644 / 3.130 | 0.075 / 0.427 | 0.0 % |
| triaxial_123__triaxial_2p5_3p5_test | 4096 | 0.150 | 0.933 | 0.190 | 1.80 | 4.06 / 11.60 | 0.056 / 0.459 (512) | 0.164 / 0.942 | 0.045 / 0.326 | 0.0 % |
| prolateSpheroid__triaxial_3_6_test | 4096 | 1.773 | 11.864 | 2.155 | 13.84 | 3.88 / 17.59 | 0.090 / 0.435 (512) | 1.780 / 10.917 | 0.061 / 0.366 | 100.0 % |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 4096 | 0.063 | 0.519 | 0.084 | 0.79 | 5.03 / 9.54 | 0.024 / 0.050 (512) | 0.080 / 0.560 | 0.005 / 0.034 | 0.0 % |
| triaxial_123_x0p75__triaxial_3_4_test | 4096 | 0.934 | 5.122 | 1.136 | 7.45 | 3.89 / 15.04 | 0.121 / 0.498 (512) | 0.870 / 4.803 | 0.068 / 0.394 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 4096 | 0.097 | 0.701 | 0.128 | 1.03 | 4.50 / 10.63 | 0.017 / 0.082 (512) | 0.089 / 0.737 | 0.004 / 0.023 | 0.0 % |

##### Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.120 / 0.564 (660) | 0.062 / 0.330 (956) | 0.046 / 0.255 (738) | 0.044 / 0.262 (698) | 0.045 / 0.277 (960) | 0.056 / 0.301 (84) |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.092 / 0.455 (622) | 0.070 / 0.363 (908) | 0.050 / 0.297 (678) | 0.037 / 0.241 (664) | 0.039 / 0.241 (1008) | 0.056 / 0.247 (216) |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.162 / 0.740 (726) | 0.093 / 0.555 (866) | 0.077 / 0.522 (620) | 0.068 / 0.445 (752) | 0.064 / 0.462 (1004) | 0.083 / 0.431 (128) |
| triaxial_2_4__triaxial_2_4_test | 0.216 / 1.118 (728) | 0.122 / 0.701 (978) | 0.092 / 0.514 (750) | 0.082 / 0.541 (774) | 0.082 / 0.566 (816) | 0.101 / 0.657 (50) |
| triaxial_2_5__triaxial_2_5_test | 0.302 / 1.768 (792) | 0.194 / 1.234 (992) | 0.156 / 0.970 (728) | 0.148 / 0.892 (774) | 0.139 / 0.977 (772) | 0.168 / 1.000 (38) |
| triaxial_3_4__triaxial_3_4_test | 0.217 / 1.100 (788) | 0.130 / 0.713 (954) | 0.090 / 0.522 (850) | 0.094 / 0.473 (746) | 0.099 / 0.500 (738) | - |
| prolateSpheroid__prolateSpheroid_test | 0.156 / 0.905 (648) | 0.105 / 0.663 (854) | 0.085 / 0.608 (656) | 0.083 / 0.573 (644) | 0.072 / 0.591 (1018) | 0.065 / 0.597 (276) |
| oblateSpheroid__oblateSpheroid_test | 0.131 / 0.806 (626) | 0.102 / 0.629 (908) | 0.064 / 0.512 (704) | 0.039 / 0.379 (682) | 0.029 / 0.305 (1050) | 0.040 / 0.179 (126) |
| triaxial_123__prolateSpheroid_test | 0.157 / 0.793 (686) | 0.092 / 0.522 (904) | 0.075 / 0.472 (628) | 0.064 / 0.452 (702) | 0.066 / 0.481 (1056) | 0.069 / 0.483 (120) |
| triaxial_123__oblateSpheroid_test | 0.139 / 0.667 (664) | 0.073 / 0.437 (930) | 0.059 / 0.385 (744) | 0.046 / 0.325 (670) | 0.045 / 0.289 (1000) | 0.049 / 0.332 (88) |
| triaxial_123__triaxial_2_5_test | 0.328 / 1.670 (742) | 0.212 / 1.118 (996) | 0.167 / 0.897 (718) | 0.140 / 0.880 (764) | 0.138 / 0.844 (810) | 0.129 / 0.983 (66) |
| prolateSpheroid__triaxial_2_5_test | 0.502 / 2.550 (656) | 0.269 / 1.352 (956) | 0.188 / 1.000 (718) | 0.176 / 1.026 (690) | 0.157 / 0.980 (938) | 0.142 / 1.187 (138) |
| prolateSpheroid__oblateSpheroid_test | 0.179 / 0.968 (718) | 0.140 / 0.888 (880) | 0.110 / 0.658 (678) | 0.090 / 0.673 (676) | 0.075 / 0.535 (944) | 0.083 / 0.482 (200) |
| triaxial_123__triaxial_1p5_2_test | 0.157 / 0.671 (686) | 0.096 / 0.488 (912) | 0.070 / 0.424 (668) | 0.063 / 0.410 (674) | 0.062 / 0.374 (1030) | 0.069 / 0.383 (126) |
| triaxial_123__triaxial_2_4_test | 0.195 / 0.907 (726) | 0.120 / 0.639 (954) | 0.092 / 0.565 (706) | 0.082 / 0.505 (746) | 0.087 / 0.545 (910) | 0.101 / 0.582 (54) |
| triaxial_123__triaxial_3_4_test | 0.268 / 1.221 (702) | 0.166 / 0.849 (958) | 0.115 / 0.625 (746) | 0.099 / 0.594 (796) | 0.096 / 0.571 (854) | 0.105 / 0.613 (40) |
| oblateSpheroid__triaxial_1p5_2_test | 0.117 / 0.643 (662) | 0.078 / 0.486 (810) | 0.059 / 0.390 (702) | 0.041 / 0.323 (746) | 0.040 / 0.285 (1024) | 0.060 / 0.297 (152) |
| prolateSpheroid__triaxial_2_4_test | 0.255 / 1.240 (684) | 0.164 / 0.815 (856) | 0.122 / 0.708 (740) | 0.108 / 0.725 (684) | 0.097 / 0.677 (974) | 0.106 / 0.769 (158) |
| triaxial_2_5__triaxial_3_4_test | 0.331 / 1.808 (778) | 0.223 / 1.273 (988) | 0.164 / 1.007 (782) | 0.160 / 0.998 (766) | 0.162 / 1.008 (752) | 0.184 / 1.059 (30) |
| triaxial_123_x0p75__triaxial_123_test | 0.194 / 0.765 (672) | 0.114 / 0.555 (982) | 0.085 / 0.423 (726) | 0.075 / 0.393 (730) | 0.072 / 0.397 (912) | 0.089 / 0.451 (74) |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.140 / 0.903 (656) | 0.101 / 0.718 (890) | 0.073 / 0.559 (696) | 0.051 / 0.435 (686) | 0.047 / 0.339 (1046) | 0.069 / 0.253 (122) |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.188 / 1.139 (686) | 0.125 / 0.803 (816) | 0.093 / 0.621 (674) | 0.082 / 0.610 (714) | 0.084 / 0.695 (940) | 0.085 / 0.678 (266) |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.127 / 0.573 (654) | 0.075 / 0.458 (812) | 0.066 / 0.389 (642) | 0.061 / 0.341 (658) | 0.057 / 0.326 (1086) | 0.068 / 0.317 (244) |
| triaxial_123_x0p75__prolateSpheroid_test | 0.202 / 0.955 (738) | 0.136 / 0.741 (884) | 0.108 / 0.620 (710) | 0.091 / 0.513 (686) | 0.084 / 0.537 (914) | 0.081 / 0.554 (164) |
| oblateSpheroid_x1p5__triaxial_123_test | 0.121 / 0.637 (668) | 0.083 / 0.481 (966) | 0.063 / 0.384 (690) | 0.058 / 0.352 (710) | 0.061 / 0.333 (964) | 0.067 / 0.370 (98) |
| oblateSpheroid__triaxial_2_5_test | 1.038 / 4.942 (708) | 0.808 / 4.142 (920) | 0.616 / 3.374 (770) | 0.487 / 3.009 (698) | 0.361 / 2.287 (912) | 0.319 / 1.928 (88) |
| triaxial_1p5_2__triaxial_3_4_test | 0.887 / 4.473 (690) | 0.615 / 3.453 (1002) | 0.396 / 2.309 (680) | 0.318 / 1.588 (688) | 0.238 / 1.292 (958) | 0.150 / 1.214 (78) |
| triaxial_123__triaxial_2p5_3p5_test | 0.200 / 1.073 (716) | 0.139 / 0.883 (952) | 0.118 / 0.805 (750) | 0.104 / 0.734 (744) | 0.092 / 0.751 (882) | 0.077 / 0.630 (52) |
| prolateSpheroid__triaxial_3_6_test | 2.413 / 14.354 (704) | 1.805 / 12.068 (956) | 1.378 / 9.286 (770) | 1.056 / 7.589 (740) | 0.725 / 6.516 (852) | 0.590 / 5.001 (74) |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.084 / 0.615 (656) | 0.062 / 0.512 (912) | 0.043 / 0.335 (606) | 0.034 / 0.317 (654) | 0.038 / 0.255 (1060) | 0.054 / 0.262 (208) |
| triaxial_123_x0p75__triaxial_3_4_test | 1.201 / 6.591 (792) | 0.963 / 4.717 (974) | 0.716 / 3.280 (764) | 0.535 / 2.760 (760) | 0.350 / 2.158 (766) | 0.270 / 1.284 (40) |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.136 / 0.801 (648) | 0.089 / 0.689 (860) | 0.070 / 0.571 (696) | 0.063 / 0.533 (672) | 0.064 / 0.631 (976) | 0.064 / 0.513 (244) |

##### MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.152 / 0.755 (68) | 0.035 / 0.157 (130) | 0.014 / 0.071 (86) | 0.008 / 0.033 (72) | 0.005 / 0.027 (142) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.040 / 0.174 (70) | 0.004 / 0.020 (136) | 0.001 / 0.004 (72) | 0.001 / 0.003 (84) | 0.000 / 0.002 (122) | 0.000 / 0.001 (28) |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.173 / 0.731 (98) | 0.050 / 0.171 (82) | 0.013 / 0.038 (78) | 0.007 / 0.028 (92) | 0.003 / 0.014 (148) | - |
| triaxial_2_4__triaxial_2_4_test | 0.141 / 0.564 (84) | 0.038 / 0.217 (118) | 0.014 / 0.082 (80) | 0.008 / 0.031 (124) | 0.006 / 0.024 (100) | - |
| triaxial_2_5__triaxial_2_5_test | 0.093 / 0.479 (112) | 0.045 / 0.237 (128) | 0.018 / 0.084 (76) | 0.013 / 0.058 (96) | 0.010 / 0.061 (96) | - |
| triaxial_3_4__triaxial_3_4_test | 0.125 / 0.661 (118) | 0.056 / 0.228 (108) | 0.026 / 0.118 (106) | 0.016 / 0.072 (90) | 0.010 / 0.056 (88) | - |
| prolateSpheroid__prolateSpheroid_test | 0.042 / 0.373 (76) | 0.006 / 0.021 (96) | 0.002 / 0.006 (76) | 0.002 / 0.006 (84) | 0.001 / 0.005 (140) | 0.001 / 0.005 (40) |
| oblateSpheroid__oblateSpheroid_test | 0.024 / 0.057 (64) | 0.008 / 0.017 (102) | 0.001 / 0.005 (104) | 0.001 / 0.003 (76) | 0.001 / 0.003 (150) | - |
| triaxial_123__prolateSpheroid_test | 0.114 / 0.590 (78) | 0.045 / 0.170 (132) | 0.014 / 0.048 (80) | 0.008 / 0.030 (92) | 0.004 / 0.025 (114) | - |
| triaxial_123__oblateSpheroid_test | 0.127 / 0.519 (86) | 0.029 / 0.110 (116) | 0.016 / 0.050 (102) | 0.008 / 0.030 (84) | 0.005 / 0.026 (112) | - |
| triaxial_123__triaxial_2_5_test | 0.102 / 0.601 (62) | 0.037 / 0.164 (142) | 0.021 / 0.100 (88) | 0.013 / 0.064 (98) | 0.009 / 0.054 (114) | - |
| prolateSpheroid__triaxial_2_5_test | 0.304 / 1.825 (84) | 0.059 / 0.208 (102) | 0.021 / 0.079 (100) | 0.016 / 0.078 (108) | 0.010 / 0.046 (94) | 0.006 / 0.025 (24) |
| prolateSpheroid__oblateSpheroid_test | 0.026 / 0.095 (98) | 0.004 / 0.014 (108) | 0.002 / 0.006 (82) | 0.001 / 0.004 (94) | 0.001 / 0.004 (116) | - |
| triaxial_123__triaxial_1p5_2_test | 0.121 / 0.479 (72) | 0.051 / 0.158 (120) | 0.015 / 0.057 (84) | 0.008 / 0.033 (96) | 0.005 / 0.026 (118) | 0.002 / 0.018 (22) |
| triaxial_123__triaxial_2_4_test | 0.196 / 0.601 (108) | 0.058 / 0.273 (98) | 0.019 / 0.071 (64) | 0.010 / 0.041 (106) | 0.005 / 0.021 (124) | - |
| triaxial_123__triaxial_3_4_test | 0.163 / 0.972 (108) | 0.063 / 0.273 (116) | 0.027 / 0.135 (98) | 0.021 / 0.093 (88) | 0.009 / 0.045 (98) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.034 / 0.095 (96) | 0.012 / 0.024 (82) | 0.001 / 0.005 (100) | 0.001 / 0.003 (102) | 0.000 / 0.003 (114) | - |
| prolateSpheroid__triaxial_2_4_test | 0.236 / 0.979 (72) | 0.106 / 0.390 (84) | 0.016 / 0.067 (114) | 0.011 / 0.036 (88) | 0.005 / 0.022 (134) | - |
| triaxial_2_5__triaxial_3_4_test | 0.171 / 0.853 (94) | 0.045 / 0.238 (126) | 0.026 / 0.092 (82) | 0.015 / 0.072 (104) | 0.011 / 0.054 (100) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.156 / 0.602 (74) | 0.045 / 0.213 (112) | 0.018 / 0.074 (96) | 0.011 / 0.039 (96) | 0.005 / 0.026 (126) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.053 / 0.133 (72) | 0.008 / 0.024 (108) | 0.002 / 0.006 (90) | 0.001 / 0.003 (94) | 0.001 / 0.004 (140) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.040 / 0.326 (94) | 0.006 / 0.028 (124) | 0.002 / 0.006 (70) | 0.002 / 0.006 (70) | 0.001 / 0.004 (126) | 0.001 / 0.005 (28) |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.070 / 0.282 (92) | 0.006 / 0.020 (114) | 0.001 / 0.004 (76) | 0.001 / 0.003 (76) | 0.000 / 0.002 (126) | 0.000 / 0.001 (28) |
| triaxial_123_x0p75__prolateSpheroid_test | 0.081 / 0.408 (80) | 0.024 / 0.092 (108) | 0.010 / 0.039 (86) | 0.006 / 0.025 (78) | 0.003 / 0.021 (124) | 0.002 / 0.015 (36) |
| oblateSpheroid_x1p5__triaxial_123_test | 0.055 / 0.188 (84) | 0.017 / 0.066 (102) | 0.008 / 0.031 (88) | 0.005 / 0.020 (90) | 0.003 / 0.022 (140) | - |
| oblateSpheroid__triaxial_2_5_test | 0.156 / 0.768 (102) | 0.040 / 0.187 (136) | 0.022 / 0.096 (82) | 0.013 / 0.051 (86) | 0.011 / 0.043 (100) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.183 / 0.873 (72) | 0.075 / 0.303 (152) | 0.041 / 0.152 (96) | 0.027 / 0.098 (76) | 0.010 / 0.031 (110) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.089 / 0.717 (98) | 0.038 / 0.224 (134) | 0.020 / 0.117 (82) | 0.012 / 0.091 (90) | 0.009 / 0.059 (108) | - |
| prolateSpheroid__triaxial_3_6_test | 0.148 / 0.644 (92) | 0.085 / 0.399 (112) | 0.024 / 0.113 (112) | 0.021 / 0.069 (88) | 0.015 / 0.050 (96) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.044 / 0.082 (82) | 0.005 / 0.012 (110) | 0.001 / 0.004 (86) | 0.001 / 0.004 (68) | 0.000 / 0.002 (134) | 0.000 / 0.002 (32) |
| triaxial_123_x0p75__triaxial_3_4_test | 0.208 / 0.768 (88) | 0.086 / 0.384 (96) | 0.049 / 0.177 (106) | 0.025 / 0.087 (110) | 0.012 / 0.050 (104) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.032 / 0.143 (64) | 0.005 / 0.040 (92) | 0.002 / 0.006 (88) | 0.002 / 0.005 (98) | 0.001 / 0.005 (142) | 0.001 / 0.004 (28) |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__triaxial_2_5_test`: triaxial_123 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid__triaxial_2_5_test`: prolateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__triaxial_1p5_2_test`: triaxial_123 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__triaxial_2_4_test`: triaxial_123 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__triaxial_3_4_test`: triaxial_123 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `oblateSpheroid__triaxial_1p5_2_test`: oblateSpheroid (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid__triaxial_2_4_test`: prolateSpheroid (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_2_5__triaxial_3_4_test`: triaxial_2_5 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123_x0p75__triaxial_123_test`: triaxial_123_x0p75 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid_x1p25__prolateSpheroid_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_1p5_2_x1p5__triaxial_1p5_2_test`: triaxial_1p5_2_x1p5 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123_x0p75__prolateSpheroid_test`: triaxial_123_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `oblateSpheroid_x1p5__triaxial_123_test`: oblateSpheroid_x1p5 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `oblateSpheroid__triaxial_2_5_test`: oblateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_1p5_2__triaxial_3_4_test`: triaxial_1p5_2 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123__triaxial_2p5_3p5_test`: triaxial_123 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid__triaxial_3_6_test`: prolateSpheroid (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test`: oblateSpheroid_x1p5 (target or source) with triaxial_1p5_2_x1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `triaxial_123_x0p75__triaxial_3_4_test`: triaxial_123_x0p75 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
  - `prolateSpheroid_x1p25__prolateSpheroid_x1p25_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid_x1p25, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
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
| 0.025 | 200 | 10 | 4.48 (4.47 / 4.81; 1.22) | 2.71 (2.72 / 2.37; 1.02) | 1.78 (1.78 / 1.68; 0.69) | 0.012 (0.010 / 0.032; 0.001) (1) |
| 0.05 | 200 | 10 | 7.35 (7.35 / 7.89; 2.17) | 5.18 (5.20 / 4.80; 1.86) | 3.10 (3.11 / 3.05; 1.04) | 0.015 (0.013 / 0.041; 0.001) (1) |
| 0.075 | 200 | 10 | 9.77 (9.75 / 10.74; 3.30) | 7.37 (7.37 / 7.71; 2.89) | 3.91 (3.90 / 4.48; 1.40) | 0.029 (0.026 / 0.087; 0.002) (1) |
| 0.1 | 200 | 10 | 14.38 (14.45 / 13.27; 4.11) | 11.14 (11.20 / 10.01; 3.63) | 5.59 (5.60 / 5.54; 1.54) | 0.015 (0.013 / 0.046; 0.001) (1) |
| 0.15 | 200 | 10 | 19.62 (19.63 / 21.15; 6.06) | 15.96 (15.98 / 16.87; 5.41) | 7.33 (7.32 / 8.25; 2.10) | 0.053 (0.041 / 0.142; 0.003) (1) |
| 0.2 | 200 | 8 | 26.03 (26.00 / 28.27; 8.07) | 21.77 (21.77 / 23.25; 7.25) | 12.91 (12.92 / 13.64; 2.80) | 0.058 (0.049 / 0.175; 0.007) (1) |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 139,252 ordered pairs from 252 clusters `poly` (mean 27.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
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
| 0.05 | 50 | 5 | 7.36 (7.33 / 8.08; 2.70) | 4.73 (4.73 / 4.92; 1.96) | 2.45 (2.42 / 3.06; 0.88) | 0.024 (0.015 / 0.086; 0.003) (1) |
| 0.05 | 100 | 5 | 6.99 (6.95 / 8.30; 2.45) | 4.70 (4.70 / 5.02; 1.95) | 2.60 (2.60 / 2.97; 0.86) | 0.008 (0.007 / 0.024; 0.002) (1) |
| 0.05 | 200 | 5 | 7.22 (7.21 / 7.49; 2.14) | 5.07 (5.09 / 4.61; 1.83) | 3.04 (3.04 / 2.98; 1.04) | not measured |
| 0.05 | 300 | 5 | 7.78 (7.80 / 7.60; 2.13) | 5.54 (5.58 / 4.84; 1.89) | 3.52 (3.55 / 3.13; 1.19) | not measured |
| 0.1 | 50 | 5 | 11.63 (11.55 / 13.02; 4.33) | 8.37 (8.36 / 8.88; 3.26) | 4.35 (4.34 / 4.62; 1.51) | 0.066 (0.048 / 0.200; 0.002) (1) |
| 0.1 | 100 | 5 | 14.07 (14.07 / 14.39; 4.39) | 9.86 (9.88 / 9.62; 3.67) | 4.89 (4.88 / 5.13; 1.44) | 0.015 (0.014 / 0.026; 0.002) (1) |
| 0.1 | 200 | 5 | 13.45 (13.47 / 13.06; 4.01) | 10.47 (10.51 / 9.82; 3.54) | 5.32 (5.32 / 5.49; 1.49) | not measured |
| 0.1 | 300 | 5 | 11.85 (11.81 / 13.74; 4.04) | 9.52 (9.50 / 10.54; 3.67) | 4.99 (4.97 / 5.91; 1.92) | not measured |
| 0.15 | 50 | 5 | 19.59 (19.56 / 20.14; 6.56) | 14.80 (14.81 / 14.75; 5.13) | 5.56 (5.48 / 6.81; 1.75) | 0.070 (0.063 / 0.139; 0.005) (1) |
| 0.15 | 100 | 5 | 18.73 (18.74 / 19.65; 6.00) | 14.98 (14.99 / 15.51; 5.02) | 5.82 (5.76 / 7.80; 1.69) | 0.014 (0.012 / 0.058; 0.002) (1) |
| 0.15 | 200 | 5 | 17.70 (17.67 / 20.88; 6.12) | 14.54 (14.54 / 16.55; 5.47) | 6.78 (6.76 / 8.42; 2.13) | not measured |
| 0.15 | 300 | 5 | 20.37 (20.36 / 20.90; 5.90) | 17.00 (17.02 / 16.70; 5.40) | 8.58 (8.58 / 8.57; 2.54) | not measured |
| 0.2 | 50 | 4 | 19.35 (19.15 / 26.59; 8.04) | 14.88 (14.72 / 20.57; 6.32) | 6.03 (5.90 / 9.61; 1.92) | 0.060 (0.056 / 0.097; 0.008) (1) |
| 0.2 | 100 | 4 | 19.89 (19.72 / 26.40; 8.31) | 16.25 (16.12 / 21.44; 7.10) | 6.78 (6.67 / 10.50; 1.89) | 0.027 (0.021 / 0.144; 0.004) (1) |
| 0.2 | 200 | 4 | 28.72 (28.78 / 28.80; 8.21) | 24.19 (24.28 / 23.39; 7.40) | 14.66 (14.71 / 14.27; 2.91) | not measured |
| 0.2 | 300 | 5 | 27.18 (27.16 / 29.12; 7.80) | 22.95 (22.95 / 23.96; 7.17) | 15.33 (15.39 / 13.59; 3.44) | not measured |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 139,252 ordered pairs from 252 clusters `poly` (mean 27.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 89.7, 243 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.09 | 0.094 | 0.31 |
| + two-body | 1500 | 0.02 | 0.027 | 0.19 |
| + many-body | 1500 | 0.02 | 0.027 | 0.19 |
| MFS Xfine (the truth's own error) | 1500 | 0.005 | 0.0104 | 0.283 |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 165,316 ordered pairs from 261 clusters `poly` (mean 30.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
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

MFS (fine) at every RK4 stage, dt 0.1: 323 steps, fell 46.4, 274 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 81 | 4.77 | 0.761 | 15.85 |
| + two-body | 77 | 1.74 | 0.331 | 9.57 |
| + many-body | 126 | 0.92 | 0.282 | 4.19 |
| MFS Xfine (the truth's own error) | 323 | 0.002 | 0.0020 | 0.111 |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 165,316 ordered pairs from 261 clusters `poly` (mean 30.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
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
| + two-body | 1.1e-16 | 0.1788 | 5.6e-16 | 5.65 |
| + many-body | 1.1e-16 | 0.9985 | 5.7e-16 | 2.62 |
| MFS fine (the truth) | 8.4e-05 | 1 | | 0 |
| MFS Xfine | 1.8e-05 | 1.0000 | | 0.007 (= the error of the fine truth) |

MFS smallest eigenvalue 1.6718e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 165,316 ordered pairs from 261 clusters `poly` (mean 30.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
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

##### The weakest configuration of each operator

The eigenvector of the smallest eigenvalue, by particle (share of its squared norm), and the pair formed by its two heaviest particles: their shapes, centre distance in pair lengths, contact factor, and the smallest eigenvalue of the operator applied to THOSE TWO PARTICLES ALONE (relative to the far field's for the two).  If that number is negative the two-body model is not positive definite for this pair by itself; if it is positive the loss of definiteness comes from adding up several neighbours.

| operator | phi | N | seed | eigenvalue ratio | share of the 2 heaviest particles | shapes | distance | contact factor | the two alone: far / + two-body | self-block eigenvalue ratio of each (operator / isolated) |
|---|---|---|---|---|---|---|---|---|---|---|
| + two-body | 0.2 | 100 | 8 | -8.129 | 0.65 | triaxial_1p5_2, prolateSpheroid | 2.92 | 1.051 | 4.96e-03 / 2.31e-03 (0.466) | 0.577, 0.570 (13 particles within 6 of the first) |
| + many-body | 0.2 | 100 | 5 | -3.669 | 0.66 | oblateSpheroid_x1p5, triaxial_123_x0p75 | 4.41 | 1.103 | 1.97e-03 / 1.87e-03 (0.945) | 0.824, 0.769 (8 particles within 6 of the first) |

##### The two-body operator on pairs alone, against MFS

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

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 165,316 ordered pairs from 261 clusters `poly` (mean 30.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
- **Configurations**: N in [16, 50, 100], shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.15, 0.2], random orientations, contact factor >= 1.05; 20 per (phi, N).  Isolated self blocks from the `fine` clouds.
- **Eigenvalues**: of the full (6N, 6N) operator matrix (symmetric by construction), dense, float64.

#### Ceiling of the many-body correction, triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.12 (7.06 / 8.08) | 4.43 (4.44 / 4.27) | 2.56 (2.56 / 2.65) | 1.72 (1.74 / 1.27) | 1.71 (1.73 / 1.22) |
| 0.1 | 64 | 3 | 12.57 (12.41 / 16.59) | 9.43 (9.39 / 10.61) | 4.14 (4.09 / 5.52) | 2.49 (2.50 / 2.23) | 2.28 (2.30 / 1.76) |
| 0.2 | 64 | 2 | 21.21 (21.06 / 26.61) | 17.11 (16.99 / 21.54) | 5.89 (5.71 / 10.11) | 3.79 (3.77 / 4.32) | 3.13 (3.16 / 2.44) |

##### Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 165,872 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 139,252 ordered pairs from 252 clusters `poly` (mean 27.8 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,960 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.194 % -> 1.446 %.
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

