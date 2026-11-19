# Two-body accuracy of `data/final_c/models/pair_mixed_s1.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.045 | 0.420 | 0.078 | 0.59 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.045 / 0.525 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.166 | 0.036 | 0.33 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.025 / 0.136 | 0.004 / 0.020 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.072 | 0.440 | 0.098 | 0.78 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.064 / 0.403 | 0.004 / 0.024 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.064 / 0.512 (684) | 0.037 / 0.401 (898) | 0.033 / 0.328 (660) | 0.033 / 0.222 (754) | 0.034 / 0.255 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.039 / 0.193 (650) | 0.020 / 0.142 (936) | 0.017 / 0.141 (680) | 0.017 / 0.180 (738) | 0.026 / 0.183 (1018) | - |
| prolateSpheroid__oblateSpheroid_test | 0.093 / 0.491 (702) | 0.064 / 0.454 (952) | 0.053 / 0.319 (668) | 0.054 / 0.297 (632) | 0.068 / 0.335 (1086) | - |

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |

## Conditions

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

