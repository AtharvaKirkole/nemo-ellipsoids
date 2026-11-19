# Two-body accuracy of `data/final/models/pair_multi.pt`

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

## Model error by contact factor: trans / rot (rows)

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

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

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

## Conditions

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

