# Two-body accuracy of `data/final_c/models/pair_multi.pt`

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

## Model error by contact factor: trans / rot (rows)

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

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

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

## Conditions

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

