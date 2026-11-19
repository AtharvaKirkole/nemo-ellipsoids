# Two-body accuracy of `data/final_c/models/pair_multi.pt`

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

## Model error by contact factor: trans / rot (rows)

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

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

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

## Conditions

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

