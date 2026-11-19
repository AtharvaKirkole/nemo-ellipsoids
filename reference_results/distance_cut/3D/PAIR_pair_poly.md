# Two-body accuracy of `data/final/models/pair_poly.pt`

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

## Model error by contact factor: trans / rot (rows)

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

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

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

## Conditions

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

