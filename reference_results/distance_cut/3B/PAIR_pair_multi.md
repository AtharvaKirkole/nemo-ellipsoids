# Two-body accuracy of `data/final/models/pair_multi.pt`

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

## Model error by contact factor: trans / rot (rows)

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

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

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

## Conditions

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

