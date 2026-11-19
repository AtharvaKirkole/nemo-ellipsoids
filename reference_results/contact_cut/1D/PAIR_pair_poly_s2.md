# Two-body accuracy of `data/final_c/models/pair_poly_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4044 | 0.031 | 0.080 | 0.035 | 0.34 | 5.70 / 10.61 | 0.005 / 0.031 (510) | 0.034 / 0.092 | 0.002 / 0.009 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4040 | 0.044 | 0.182 | 0.056 | 0.50 | 5.19 / 11.22 | 0.016 / 0.067 (504) | 0.048 / 0.159 | 0.005 / 0.029 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.051 | 0.373 | 0.076 | 0.62 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.053 / 0.484 | 0.004 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4024 | 0.144 | 0.556 | 0.160 | 2.25 | 4.80 / 14.98 | 0.067 / 0.482 (500) | 0.143 / 0.605 | 0.030 / 0.169 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4006 | 0.029 | 0.081 | 0.032 | 0.34 | 5.57 / 10.07 | 0.003 / 0.014 (504) | 0.027 / 0.087 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.027 | 0.147 | 0.035 | 0.34 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.027 / 0.119 | 0.004 / 0.020 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4020 | 0.095 | 0.476 | 0.109 | 1.36 | 4.05 / 11.39 | 0.058 / 0.336 (504) | 0.080 / 0.349 | 0.070 / 0.366 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.074 | 0.412 | 0.094 | 0.85 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.067 / 0.333 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2__oblateSpheroid_test | 4046 | 0.082 | 0.351 | 0.101 | 0.90 | 4.89 / 11.55 | 0.021 / 0.065 (498) | 0.091 / 0.365 | 0.004 / 0.021 | 0.0 % |
| prolate_ar4__oblate_ar3_test | 4028 | 0.216 | 0.829 | 0.236 | 3.12 | 4.06 / 12.07 | 0.069 / 0.364 (506) | 0.192 / 0.738 | 0.075 / 0.483 | 0.0 % |
| prolate_ar2__oblate_ar1p5_test | 4018 | 0.068 | 0.242 | 0.081 | 0.80 | 5.45 / 10.67 | 0.008 / 0.033 (502) | 0.068 / 0.234 | 0.005 / 0.025 | 0.0 % |
| prolate_ar1p5__oblate_ar3_test | 4044 | 0.153 | 0.590 | 0.175 | 1.39 | 4.09 / 14.18 | 0.132 / 0.454 (508) | 0.163 / 0.664 | 0.115 / 0.565 | 0.0 % |
| prolateSpheroid__prolate_ar2_test | 4022 | 0.111 | 0.477 | 0.138 | 1.22 | 4.85 / 11.78 | 0.017 / 0.131 (508) | 0.102 / 0.429 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblate_ar3_test | 4000 | 0.141 | 0.515 | 0.153 | 1.59 | 4.25 / 11.86 | 0.091 / 0.419 (500) | 0.129 / 0.501 | 0.076 / 0.415 | 0.0 % |
| prolate_ar4__oblateSpheroid_test | 4042 | 0.154 | 0.633 | 0.178 | 2.05 | 4.77 / 12.73 | 0.043 / 0.254 (508) | 0.157 / 0.639 | 0.024 / 0.155 | 0.0 % |
| prolateSpheroid__oblate_ar1p5_test | 4026 | 0.099 | 0.374 | 0.116 | 1.05 | 4.97 / 11.76 | 0.018 / 0.081 (508) | 0.110 / 0.440 | 0.004 / 0.021 | 0.0 % |
| prolateSpheroid_x0p75__prolateSpheroid_test | 4046 | 0.125 | 0.607 | 0.162 | 1.30 | 4.72 / 13.40 | 0.024 / 0.203 (504) | 0.139 / 0.546 | 0.006 / 0.032 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.088 | 0.315 | 0.093 | 0.82 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.088 / 0.295 | 0.004 / 0.024 | 0.0 % |
| prolate_ar2_x1p5__prolate_ar2_test | 4022 | 0.095 | 0.335 | 0.107 | 0.91 | 4.83 / 11.46 | 0.021 / 0.101 (498) | 0.104 / 0.343 | 0.008 / 0.050 | 0.0 % |
| oblate_ar3_x0p75__oblate_ar3_test | 4018 | 0.162 | 0.646 | 0.178 | 2.16 | 3.85 / 11.95 | 0.090 / 0.371 (498) | 0.143 / 0.490 | 0.074 / 0.397 | 0.0 % |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 4028 | 0.123 | 0.551 | 0.143 | 1.04 | 3.56 / 12.87 | 0.037 / 0.211 (506) | 0.122 / 0.498 | 0.007 / 0.043 | 0.0 % |
| prolate_ar2_x1p5__oblateSpheroid_test | 4016 | 0.094 | 0.340 | 0.106 | 1.01 | 4.90 / 10.45 | 0.031 / 0.078 (500) | 0.108 / 0.349 | 0.005 / 0.031 | 0.0 % |
| prolate_ar2__oblate_ar3_test | 4032 | 0.616 | 3.276 | 0.772 | 7.57 | 3.98 / 12.62 | 0.112 / 0.491 (506) | 0.605 / 3.374 | 0.098 / 0.537 | 0.0 % |
| prolate_ar4__oblate_ar1p5_test | 4022 | 1.155 | 3.075 | 1.225 | 5.10 | 5.13 / 14.89 | 0.073 / 0.459 (502) | 1.298 / 3.350 | 0.038 / 0.249 | 0.0 % |
| prolate_ar2p5__oblate_ar2p5_test | 4040 | 0.409 | 1.837 | 0.487 | 4.97 | 4.39 / 11.86 | 0.046 / 0.226 (506) | 0.390 / 1.777 | 0.039 / 0.257 | 0.0 % |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 4020 | 0.064 | 0.356 | 0.080 | 0.74 | 4.86 / 10.50 | 0.031 / 0.199 (504) | 0.061 / 0.368 | 0.016 / 0.102 | 0.0 % |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 4054 | 1.371 | 4.504 | 1.499 | 22.46 | 4.50 / 11.02 | 0.044 / 0.240 (510) | 1.401 / 4.157 | 0.048 / 0.291 | 0.0 % |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 4006 | 0.311 | 0.973 | 0.337 | 2.75 | 4.85 / 10.92 | 0.022 / 0.134 (506) | 0.336 / 1.067 | 0.015 / 0.099 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.038 / 0.081 (652) | 0.025 / 0.065 (896) | 0.022 / 0.086 (690) | 0.026 / 0.106 (688) | 0.043 / 0.148 (1118) | - |
| prolate_ar2__prolate_ar2_test | 0.056 / 0.193 (708) | 0.039 / 0.187 (840) | 0.034 / 0.124 (756) | 0.036 / 0.177 (620) | 0.043 / 0.272 (1116) | - |
| prolateSpheroid__prolateSpheroid_test | 0.070 / 0.434 (684) | 0.047 / 0.376 (898) | 0.035 / 0.296 (660) | 0.036 / 0.217 (754) | 0.034 / 0.233 (1038) | - |
| prolate_ar4__prolate_ar4_test | 0.211 / 0.730 (680) | 0.127 / 0.470 (904) | 0.101 / 0.459 (734) | 0.080 / 0.324 (660) | 0.069 / 0.300 (1046) | - |
| oblate_ar1p5__oblate_ar1p5_test | 0.032 / 0.080 (652) | 0.024 / 0.073 (922) | 0.023 / 0.087 (714) | 0.031 / 0.100 (704) | 0.040 / 0.135 (1014) | - |
| oblateSpheroid__oblateSpheroid_test | 0.039 / 0.165 (650) | 0.021 / 0.133 (936) | 0.018 / 0.118 (680) | 0.019 / 0.169 (738) | 0.026 / 0.165 (1018) | - |
| oblate_ar3__oblate_ar3_test | 0.132 / 0.638 (726) | 0.081 / 0.376 (854) | 0.066 / 0.265 (702) | 0.064 / 0.258 (660) | 0.074 / 0.272 (1078) | - |
| prolateSpheroid__oblateSpheroid_test | 0.099 / 0.435 (702) | 0.067 / 0.440 (952) | 0.054 / 0.324 (668) | 0.052 / 0.302 (632) | 0.053 / 0.316 (1086) | - |
| prolate_ar2__oblateSpheroid_test | 0.111 / 0.390 (696) | 0.068 / 0.334 (904) | 0.061 / 0.297 (670) | 0.061 / 0.313 (652) | 0.068 / 0.313 (1124) | - |
| prolate_ar4__oblate_ar3_test | 0.314 / 1.129 (680) | 0.182 / 0.644 (874) | 0.139 / 0.592 (714) | 0.133 / 0.557 (726) | 0.172 / 0.565 (1034) | - |
| prolate_ar2__oblate_ar1p5_test | 0.094 / 0.288 (674) | 0.055 / 0.196 (926) | 0.049 / 0.214 (678) | 0.052 / 0.245 (708) | 0.068 / 0.270 (1032) | - |
| prolate_ar1p5__oblate_ar3_test | 0.217 / 0.753 (722) | 0.126 / 0.515 (904) | 0.099 / 0.384 (690) | 0.102 / 0.386 (652) | 0.126 / 0.425 (1076) | - |
| prolateSpheroid__prolate_ar2_test | 0.154 / 0.564 (654) | 0.090 / 0.444 (918) | 0.090 / 0.392 (648) | 0.089 / 0.366 (660) | 0.080 / 0.372 (1142) | - |
| oblateSpheroid__oblate_ar3_test | 0.204 / 0.671 (704) | 0.117 / 0.416 (886) | 0.091 / 0.348 (740) | 0.086 / 0.330 (622) | 0.095 / 0.356 (1048) | - |
| prolate_ar4__oblateSpheroid_test | 0.212 / 0.759 (676) | 0.139 / 0.609 (926) | 0.114 / 0.482 (718) | 0.105 / 0.423 (672) | 0.099 / 0.437 (1050) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.135 / 0.456 (638) | 0.083 / 0.332 (892) | 0.073 / 0.294 (658) | 0.079 / 0.298 (700) | 0.090 / 0.312 (1138) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.174 / 0.778 (702) | 0.112 / 0.554 (874) | 0.088 / 0.393 (718) | 0.079 / 0.341 (676) | 0.079 / 0.360 (1076) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.130 / 0.394 (662) | 0.069 / 0.266 (936) | 0.056 / 0.237 (688) | 0.057 / 0.232 (712) | 0.066 / 0.260 (1034) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.125 / 0.401 (750) | 0.081 / 0.283 (820) | 0.063 / 0.270 (676) | 0.073 / 0.263 (668) | 0.084 / 0.301 (1108) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.246 / 0.900 (716) | 0.125 / 0.475 (898) | 0.098 / 0.362 (724) | 0.088 / 0.366 (642) | 0.094 / 0.402 (1038) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.164 / 0.670 (684) | 0.108 / 0.466 (874) | 0.089 / 0.460 (746) | 0.090 / 0.456 (714) | 0.117 / 0.513 (1010) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.135 / 0.404 (630) | 0.077 / 0.302 (886) | 0.065 / 0.252 (638) | 0.062 / 0.308 (742) | 0.082 / 0.357 (1120) | - |
| prolate_ar2__oblate_ar3_test | 0.829 / 3.896 (680) | 0.639 / 3.319 (890) | 0.417 / 2.380 (726) | 0.306 / 1.657 (628) | 0.253 / 1.170 (1108) | - |
| prolate_ar4__oblate_ar1p5_test | 1.568 / 3.773 (718) | 1.164 / 2.984 (896) | 0.790 / 2.133 (696) | 0.485 / 1.387 (612) | 0.252 / 0.851 (1100) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.509 / 2.145 (732) | 0.436 / 1.849 (866) | 0.316 / 1.309 (682) | 0.234 / 0.965 (706) | 0.167 / 0.732 (1054) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.089 / 0.456 (706) | 0.055 / 0.316 (894) | 0.045 / 0.218 (670) | 0.043 / 0.183 (602) | 0.049 / 0.206 (1148) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 1.561 / 5.207 (706) | 1.453 / 4.207 (890) | 1.278 / 3.791 (718) | 1.010 / 3.456 (650) | 0.736 / 3.328 (1090) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.385 / 1.139 (666) | 0.330 / 0.947 (926) | 0.264 / 0.769 (644) | 0.183 / 0.597 (702) | 0.109 / 0.510 (1068) | - |

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
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| prolate_ar2__oblateSpheroid_test | 0.036 / 0.099 (92) | 0.009 / 0.016 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (138) | - |
| prolate_ar4__oblate_ar3_test | 0.110 / 0.607 (68) | 0.065 / 0.278 (142) | 0.035 / 0.110 (90) | 0.027 / 0.116 (86) | 0.017 / 0.077 (120) | - |
| prolate_ar2__oblate_ar1p5_test | 0.015 / 0.056 (78) | 0.001 / 0.002 (112) | 0.000 / 0.000 (92) | 0.000 / 0.000 (88) | 0.000 / 0.000 (132) | - |
| prolate_ar1p5__oblate_ar3_test | 0.216 / 0.670 (90) | 0.092 / 0.332 (114) | 0.050 / 0.143 (72) | 0.056 / 0.137 (94) | 0.040 / 0.119 (138) | - |
| prolateSpheroid__prolate_ar2_test | 0.034 / 0.235 (76) | 0.005 / 0.022 (148) | 0.002 / 0.007 (80) | 0.001 / 0.003 (80) | 0.001 / 0.003 (124) | - |
| oblateSpheroid__oblate_ar3_test | 0.141 / 0.681 (86) | 0.070 / 0.204 (134) | 0.048 / 0.136 (82) | 0.027 / 0.095 (70) | 0.026 / 0.079 (128) | - |
| prolate_ar4__oblateSpheroid_test | 0.076 / 0.406 (94) | 0.018 / 0.070 (102) | 0.003 / 0.010 (104) | 0.001 / 0.007 (80) | 0.001 / 0.003 (128) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.036 / 0.154 (68) | 0.004 / 0.023 (110) | 0.002 / 0.005 (102) | 0.001 / 0.004 (70) | 0.001 / 0.003 (158) | - |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.041 / 0.317 (94) | 0.010 / 0.076 (98) | 0.002 / 0.006 (96) | 0.002 / 0.005 (86) | 0.001 / 0.005 (130) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.036 / 0.158 (102) | 0.005 / 0.024 (102) | 0.000 / 0.000 (92) | 0.000 / 0.000 (72) | 0.000 / 0.000 (130) | - |
| oblate_ar3_x0p75__oblate_ar3_test | 0.140 / 0.539 (76) | 0.086 / 0.315 (118) | 0.037 / 0.141 (88) | 0.031 / 0.143 (90) | 0.019 / 0.093 (126) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.069 / 0.368 (72) | 0.014 / 0.035 (106) | 0.002 / 0.008 (86) | 0.001 / 0.005 (84) | 0.001 / 0.004 (158) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.055 / 0.117 (84) | 0.005 / 0.013 (88) | 0.001 / 0.003 (84) | 0.001 / 0.002 (106) | 0.000 / 0.002 (138) | - |
| prolate_ar2__oblate_ar3_test | 0.174 / 0.731 (100) | 0.072 / 0.242 (120) | 0.059 / 0.157 (90) | 0.033 / 0.120 (74) | 0.022 / 0.091 (122) | - |
| prolate_ar4__oblate_ar1p5_test | 0.123 / 0.724 (106) | 0.024 / 0.108 (102) | 0.005 / 0.015 (106) | 0.002 / 0.005 (70) | 0.000 / 0.001 (118) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.089 / 0.392 (72) | 0.020 / 0.074 (110) | 0.011 / 0.031 (84) | 0.008 / 0.024 (114) | 0.006 / 0.021 (126) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.054 / 0.309 (84) | 0.006 / 0.030 (68) | 0.001 / 0.001 (98) | 0.000 / 0.000 (90) | 0.000 / 0.000 (164) | - |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 0.069 / 0.346 (86) | 0.033 / 0.131 (98) | 0.021 / 0.088 (88) | 0.018 / 0.076 (102) | 0.015 / 0.074 (136) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.038 / 0.212 (100) | 0.005 / 0.016 (114) | 0.001 / 0.004 (74) | 0.001 / 0.003 (74) | 0.000 / 0.002 (144) | - |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly_s2.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 2: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblateSpheroid_test`: prolate_ar2 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar3_test`: prolate_ar4 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar1p5_test`: prolate_ar2 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar1p5__oblate_ar3_test`: prolate_ar1p5 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolate_ar2_test`: prolateSpheroid (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblate_ar3_test`: oblateSpheroid (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4000 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblateSpheroid_test`: prolate_ar4 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblate_ar1p5_test`: prolateSpheroid (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x0p75__prolateSpheroid_test`: prolateSpheroid_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4046 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__prolate_ar2_test`: prolate_ar2_x1p5 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__oblate_ar3_test`: oblate_ar3_x0p75 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4018 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__prolateSpheroid_x0p75_test`: oblateSpheroid_x1p5 (target or source) with prolateSpheroid_x0p75, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2_x1p5__oblateSpheroid_test`: prolate_ar2_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2__oblate_ar3_test`: prolate_ar2 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar4__oblate_ar1p5_test`: prolate_ar4 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5__oblate_ar2p5_test`: prolate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test`: prolate_ar2p5_x1p25 (target or source) with prolate_ar2p5_x1p25, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblate_ar3_x0p75__prolate_ar2_x1p5_test`: oblate_ar3_x0p75 (target or source) with prolate_ar2_x1p5, 2048 configurations (both orderings scored: 4054 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolate_ar2p5_x1p25__oblateSpheroid_test`: prolate_ar2p5_x1p25 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4006 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
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
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2_x1p5 | 1.5 : 1.5 : 3 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3_x0p75 | 2.25 : 2.25 : 0.75 | 660 / 560; 0.0236 / 0.0510 | 1400 / 1190; 0.0086 / 0.0183 |
| prolate_ar2p5 | 1 : 1 : 2.5 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar2p5 | 2.5 : 2.5 : 1 | 660 / 560; 0.0027 / 0.0092 | 1400 / 1190; 0.0004 / 0.0006 |
| prolate_ar2p5_x1p25 | 1.25 : 1.25 : 3.125 | 660 / 560; 0.0002 / 0.0003 | 1400 / 1190; 0.0000 / 0.0000 |

