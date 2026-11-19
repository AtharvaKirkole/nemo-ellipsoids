# Two-body accuracy of `data/final/models/pair_mixed.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4096 | 0.080 | 0.378 | 0.093 | 1.00 | 4.33 / 11.49 | 0.078 / 0.456 (512) | 0.079 / 0.424 | 0.041 / 0.300 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.125 | 0.807 | 0.175 | 1.12 | 4.70 / 11.56 | 0.023 / 0.232 (512) | 0.124 / 0.793 | 0.005 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.097 | 0.655 | 0.137 | 0.83 | 4.94 / 11.24 | 0.013 / 0.034 (512) | 0.101 / 0.661 | 0.003 / 0.018 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4096 | 0.119 | 0.634 | 0.150 | 1.24 | 4.49 / 11.89 | 0.064 / 0.343 (512) | 0.133 / 0.799 | 0.053 / 0.375 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4096 | 0.088 | 0.464 | 0.112 | 0.96 | 4.55 / 11.24 | 0.070 / 0.326 (512) | 0.091 / 0.453 | 0.040 / 0.301 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4096 | 1.553 | 8.890 | 2.045 | 12.32 | 4.88 / 11.24 | 0.015 / 0.063 (512) | 1.477 / 9.127 | 0.004 / 0.022 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.122 / 0.525 (660) | 0.063 / 0.290 (956) | 0.049 / 0.227 (738) | 0.048 / 0.224 (698) | 0.052 / 0.254 (960) | 0.080 / 0.341 (84) |
| prolateSpheroid__prolateSpheroid_test | 0.162 / 0.984 (648) | 0.119 / 0.713 (854) | 0.097 / 0.667 (656) | 0.096 / 0.645 (644) | 0.088 / 0.678 (1018) | 0.094 / 0.675 (276) |
| oblateSpheroid__oblateSpheroid_test | 0.130 / 0.771 (626) | 0.102 / 0.635 (908) | 0.065 / 0.533 (704) | 0.039 / 0.397 (682) | 0.035 / 0.316 (1050) | 0.067 / 0.246 (126) |
| triaxial_123__prolateSpheroid_test | 0.169 / 0.826 (686) | 0.102 / 0.509 (904) | 0.079 / 0.450 (628) | 0.072 / 0.406 (702) | 0.079 / 0.465 (1056) | 0.088 / 0.594 (120) |
| triaxial_123__oblateSpheroid_test | 0.135 / 0.599 (664) | 0.069 / 0.395 (930) | 0.056 / 0.340 (744) | 0.048 / 0.322 (670) | 0.051 / 0.284 (1000) | 0.059 / 0.308 (88) |
| prolateSpheroid__oblateSpheroid_test | 1.857 / 9.691 (718) | 1.610 / 8.966 (880) | 1.348 / 7.805 (678) | 1.081 / 6.625 (676) | 0.806 / 5.510 (944) | 0.642 / 4.493 (200) |

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.152 / 0.755 (68) | 0.035 / 0.157 (130) | 0.014 / 0.071 (86) | 0.008 / 0.033 (72) | 0.005 / 0.027 (142) | - |
| prolateSpheroid__prolateSpheroid_test | 0.042 / 0.373 (76) | 0.006 / 0.021 (96) | 0.002 / 0.006 (76) | 0.002 / 0.006 (84) | 0.001 / 0.005 (140) | 0.001 / 0.005 (40) |
| oblateSpheroid__oblateSpheroid_test | 0.024 / 0.057 (64) | 0.008 / 0.017 (102) | 0.001 / 0.005 (104) | 0.001 / 0.003 (76) | 0.001 / 0.003 (150) | - |
| triaxial_123__prolateSpheroid_test | 0.114 / 0.590 (78) | 0.045 / 0.170 (132) | 0.014 / 0.048 (80) | 0.008 / 0.030 (92) | 0.004 / 0.025 (114) | - |
| triaxial_123__oblateSpheroid_test | 0.127 / 0.519 (86) | 0.029 / 0.110 (116) | 0.016 / 0.050 (102) | 0.008 / 0.030 (84) | 0.005 / 0.026 (112) | - |
| prolateSpheroid__oblateSpheroid_test | 0.026 / 0.095 (98) | 0.004 / 0.014 (108) | 0.002 / 0.006 (82) | 0.001 / 0.004 (94) | 0.001 / 0.004 (116) | - |

## Conditions

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

