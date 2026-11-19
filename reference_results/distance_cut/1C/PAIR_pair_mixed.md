# Two-body accuracy of `data/final/models/pair_mixed.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.047 | 0.387 | 0.076 | 0.52 | 4.70 / 11.48 | 0.026 / 0.237 (512) | 0.045 / 0.452 | 0.005 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.028 | 0.164 | 0.037 | 0.32 | 4.97 / 11.38 | 0.013 / 0.036 (512) | 0.030 / 0.181 | 0.003 / 0.019 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4096 | 0.070 | 0.433 | 0.097 | 0.71 | 4.88 / 11.26 | 0.015 / 0.062 (512) | 0.070 / 0.378 | 0.004 / 0.022 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.069 / 0.455 (682) | 0.035 / 0.369 (894) | 0.032 / 0.338 (690) | 0.035 / 0.251 (680) | 0.034 / 0.279 (988) | 0.035 / 0.316 (162) |
| oblateSpheroid__oblateSpheroid_test | 0.040 / 0.175 (668) | 0.022 / 0.156 (956) | 0.018 / 0.155 (734) | 0.018 / 0.153 (720) | 0.025 / 0.180 (984) | 0.047 / 0.154 (34) |
| prolateSpheroid__oblateSpheroid_test | 0.091 / 0.500 (748) | 0.062 / 0.420 (928) | 0.055 / 0.323 (704) | 0.052 / 0.305 (704) | 0.060 / 0.327 (902) | 0.065 / 0.385 (110) |

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.047 / 0.375 (84) | 0.006 / 0.026 (102) | 0.002 / 0.006 (80) | 0.002 / 0.006 (86) | 0.001 / 0.005 (138) | 0.001 / 0.005 (22) |
| oblateSpheroid__oblateSpheroid_test | 0.025 / 0.060 (66) | 0.008 / 0.017 (112) | 0.001 / 0.005 (110) | 0.001 / 0.003 (76) | 0.001 / 0.003 (142) | - |
| prolateSpheroid__oblateSpheroid_test | 0.027 / 0.093 (102) | 0.004 / 0.014 (110) | 0.002 / 0.006 (82) | 0.001 / 0.005 (98) | 0.001 / 0.004 (110) | - |

## Conditions

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

