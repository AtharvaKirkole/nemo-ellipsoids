# Two-body accuracy of `data/final_c/models/pair_mixed.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.090 | 0.397 | 0.104 | 1.17 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.085 / 0.530 | 0.040 / 0.283 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.121 | 0.824 | 0.178 | 1.25 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.125 / 0.900 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.099 | 0.653 | 0.139 | 0.88 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.088 / 0.563 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.124 | 0.644 | 0.157 | 1.41 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.131 / 0.905 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.096 | 0.471 | 0.115 | 1.07 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.083 / 0.443 | 0.042 / 0.294 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.110 | 0.700 | 0.154 | 0.96 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.090 / 0.629 | 0.004 / 0.024 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.132 / 0.512 (666) | 0.074 / 0.321 (868) | 0.057 / 0.276 (688) | 0.057 / 0.284 (672) | 0.063 / 0.306 (1150) | - |
| prolateSpheroid__prolateSpheroid_test | 0.162 / 0.983 (684) | 0.109 / 0.754 (898) | 0.094 / 0.686 (660) | 0.087 / 0.608 (754) | 0.090 / 0.705 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.132 / 0.803 (650) | 0.104 / 0.612 (936) | 0.063 / 0.472 (680) | 0.044 / 0.384 (738) | 0.036 / 0.343 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.176 / 0.803 (668) | 0.109 / 0.562 (876) | 0.081 / 0.452 (668) | 0.075 / 0.463 (738) | 0.085 / 0.523 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.145 / 0.603 (686) | 0.074 / 0.406 (916) | 0.060 / 0.315 (684) | 0.052 / 0.281 (688) | 0.057 / 0.295 (1058) | - |
| prolateSpheroid__oblateSpheroid_test | 0.141 / 0.760 (702) | 0.109 / 0.707 (952) | 0.086 / 0.607 (668) | 0.065 / 0.542 (632) | 0.057 / 0.470 (1086) | - |

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

## Conditions

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

