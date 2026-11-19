# Two-body accuracy of `data/final_c/models/pair_multi_s2.pt`

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

## Model error by contact factor: trans / rot (rows)

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

