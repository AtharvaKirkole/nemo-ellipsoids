# Two-body accuracy of `data/final/models/pair_poly.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 4096 | 0.031 | 0.080 | 0.035 | 0.32 | 5.65 / 10.69 | 0.006 / 0.029 (512) | 0.034 / 0.082 | 0.002 / 0.010 | 0.0 % |
| prolate_ar2__prolate_ar2_test | 4096 | 0.047 | 0.179 | 0.057 | 0.49 | 5.09 / 11.13 | 0.016 / 0.083 (512) | 0.045 / 0.162 | 0.004 / 0.027 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4096 | 0.051 | 0.350 | 0.073 | 0.61 | 4.70 / 11.48 | 0.026 / 0.237 (512) | 0.049 / 0.384 | 0.005 / 0.024 | 0.0 % |
| prolate_ar4__prolate_ar4_test | 4096 | 0.137 | 0.528 | 0.153 | 2.23 | 4.63 / 14.02 | 0.064 / 0.393 (512) | 0.131 / 0.605 | 0.030 / 0.170 | 0.0 % |
| oblate_ar1p5__oblate_ar1p5_test | 4096 | 0.030 | 0.088 | 0.034 | 0.32 | 5.69 / 10.60 | 0.004 / 0.012 (512) | 0.028 / 0.091 | 0.003 / 0.015 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.026 | 0.150 | 0.035 | 0.32 | 4.97 / 11.38 | 0.013 / 0.036 (512) | 0.027 / 0.164 | 0.003 / 0.019 | 0.0 % |
| oblate_ar3__oblate_ar3_test | 4096 | 0.100 | 0.446 | 0.111 | 1.38 | 4.07 / 11.49 | 0.063 / 0.301 (512) | 0.084 / 0.309 | 0.072 / 0.375 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4096 | 0.071 | 0.381 | 0.092 | 0.80 | 4.88 / 11.26 | 0.015 / 0.062 (512) | 0.065 / 0.312 | 0.004 / 0.022 | 0.0 % |
| prolate_ar2__oblateSpheroid_test | 4096 | 0.088 | 0.339 | 0.102 | 0.85 | 4.91 / 11.40 | 0.023 / 0.064 (512) | 0.096 / 0.330 | 0.003 / 0.021 | 0.0 % |
| prolate_ar4__oblate_ar3_test | 4096 | 0.200 | 0.812 | 0.223 | 3.16 | 4.15 / 12.28 | 0.062 / 0.355 (512) | 0.183 / 0.783 | 0.074 / 0.485 | 0.0 % |
| prolate_ar2__oblate_ar1p5_test | 4096 | 0.072 | 0.228 | 0.082 | 0.77 | 5.32 / 10.61 | 0.006 / 0.029 (512) | 0.074 / 0.216 | 0.005 / 0.023 | 0.0 % |
| prolate_ar1p5__oblate_ar3_test | 4096 | 0.150 | 0.603 | 0.169 | 1.37 | 4.16 / 14.22 | 0.133 / 0.462 (512) | 0.159 / 0.584 | 0.117 / 0.602 | 0.0 % |
| prolateSpheroid__prolate_ar2_test | 4096 | 0.111 | 0.480 | 0.135 | 1.33 | 4.78 / 11.51 | 0.014 / 0.112 (512) | 0.110 / 0.452 | 0.004 / 0.023 | 0.0 % |
| oblateSpheroid__oblate_ar3_test | 4096 | 0.123 | 0.507 | 0.140 | 1.45 | 4.22 / 12.13 | 0.086 / 0.392 (512) | 0.117 / 0.506 | 0.080 / 0.435 | 0.0 % |
| prolate_ar4__oblateSpheroid_test | 4096 | 0.155 | 0.656 | 0.179 | 2.00 | 4.83 / 13.18 | 0.040 / 0.236 (512) | 0.170 / 0.747 | 0.022 / 0.152 | 0.0 % |
| prolateSpheroid__oblate_ar1p5_test | 4096 | 0.097 | 0.381 | 0.116 | 1.08 | 5.10 / 12.27 | 0.016 / 0.101 (512) | 0.103 / 0.408 | 0.004 / 0.022 | 0.0 % |
| prolateSpheroid_x0p75__prolateSpheroid_test | 4096 | 0.119 | 0.587 | 0.158 | 1.32 | 4.62 / 13.66 | 0.027 / 0.252 (512) | 0.120 / 0.644 | 0.006 / 0.032 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4096 | 0.083 | 0.303 | 0.090 | 0.77 | 4.48 / 10.82 | 0.027 / 0.079 (512) | 0.083 / 0.278 | 0.004 / 0.025 | 0.0 % |
| prolate_ar2_x1p5__prolate_ar2_test | 4096 | 0.081 | 0.327 | 0.094 | 0.84 | 4.78 / 11.12 | 0.020 / 0.103 (512) | 0.080 / 0.378 | 0.008 / 0.052 | 0.0 % |
| oblate_ar3_x0p75__oblate_ar3_test | 4096 | 0.139 | 0.594 | 0.159 | 2.10 | 3.86 / 11.87 | 0.070 / 0.269 (512) | 0.130 / 0.454 | 0.073 / 0.384 | 0.0 % |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 4096 | 0.126 | 0.532 | 0.145 | 1.03 | 3.53 / 13.05 | 0.037 / 0.174 (512) | 0.129 / 0.423 | 0.007 / 0.046 | 0.0 % |
| prolate_ar2_x1p5__oblateSpheroid_test | 4096 | 0.094 | 0.339 | 0.104 | 1.00 | 4.97 / 10.48 | 0.028 / 0.077 (512) | 0.104 / 0.366 | 0.005 / 0.030 | 0.0 % |
| prolate_ar2__oblate_ar3_test | 4096 | 1.114 | 3.509 | 1.202 | 5.95 | 3.96 / 12.73 | 0.124 / 0.506 (512) | 1.057 / 3.526 | 0.101 / 0.548 | 0.0 % |
| prolate_ar4__oblate_ar1p5_test | 4096 | 1.597 | 3.847 | 1.688 | 5.39 | 5.03 / 14.99 | 0.085 / 0.435 (512) | 1.517 / 4.040 | 0.038 / 0.240 | 0.0 % |
| prolate_ar2p5__oblate_ar2p5_test | 4096 | 0.739 | 1.986 | 0.790 | 4.27 | 4.24 / 11.82 | 0.047 / 0.228 (512) | 0.763 / 2.027 | 0.042 / 0.243 | 0.0 % |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 4096 | 0.107 | 0.372 | 0.118 | 0.75 | 4.91 / 10.34 | 0.030 / 0.178 (512) | 0.104 / 0.393 | 0.017 / 0.111 | 0.0 % |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 4096 | 1.854 | 4.909 | 1.984 | 15.96 | 4.49 / 11.40 | 0.039 / 0.200 (512) | 1.893 / 5.046 | 0.052 / 0.272 | 0.0 % |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 4096 | 0.219 | 1.124 | 0.267 | 2.72 | 4.90 / 10.80 | 0.026 / 0.124 (512) | 0.232 / 1.075 | 0.015 / 0.104 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| prolate_ar1p5__prolate_ar1p5_test | 0.034 / 0.086 (638) | 0.024 / 0.062 (824) | 0.026 / 0.076 (652) | 0.035 / 0.112 (628) | 0.045 / 0.130 (1022) | 0.075 / 0.231 (332) |
| prolate_ar2__prolate_ar2_test | 0.065 / 0.202 (678) | 0.040 / 0.164 (844) | 0.032 / 0.146 (684) | 0.031 / 0.165 (700) | 0.042 / 0.231 (944) | 0.050 / 0.251 (246) |
| prolateSpheroid__prolateSpheroid_test | 0.072 / 0.386 (682) | 0.045 / 0.356 (894) | 0.038 / 0.323 (690) | 0.033 / 0.229 (680) | 0.031 / 0.226 (988) | 0.036 / 0.281 (162) |
| prolate_ar4__prolate_ar4_test | 0.214 / 0.716 (686) | 0.110 / 0.447 (956) | 0.089 / 0.406 (736) | 0.072 / 0.320 (788) | 0.063 / 0.255 (786) | 0.061 / 0.356 (144) |
| oblate_ar1p5__oblate_ar1p5_test | 0.036 / 0.095 (648) | 0.024 / 0.079 (862) | 0.025 / 0.080 (724) | 0.030 / 0.095 (640) | 0.037 / 0.128 (1064) | 0.063 / 0.217 (158) |
| oblateSpheroid__oblateSpheroid_test | 0.038 / 0.175 (668) | 0.020 / 0.139 (956) | 0.017 / 0.122 (734) | 0.018 / 0.127 (720) | 0.024 / 0.153 (984) | 0.032 / 0.140 (34) |
| oblate_ar3__oblate_ar3_test | 0.143 / 0.600 (862) | 0.084 / 0.355 (1016) | 0.062 / 0.262 (868) | 0.057 / 0.248 (726) | 0.063 / 0.214 (608) | - |
| prolateSpheroid__oblateSpheroid_test | 0.094 / 0.419 (748) | 0.063 / 0.388 (928) | 0.055 / 0.309 (704) | 0.047 / 0.270 (704) | 0.051 / 0.287 (902) | 0.052 / 0.309 (110) |
| prolate_ar2__oblateSpheroid_test | 0.119 / 0.384 (692) | 0.075 / 0.318 (896) | 0.062 / 0.279 (720) | 0.060 / 0.300 (656) | 0.077 / 0.308 (1038) | 0.126 / 0.403 (94) |
| prolate_ar4__oblate_ar3_test | 0.287 / 1.060 (742) | 0.165 / 0.646 (946) | 0.141 / 0.633 (756) | 0.140 / 0.549 (772) | 0.134 / 0.576 (842) | 0.133 / 0.611 (38) |
| prolate_ar2__oblate_ar1p5_test | 0.092 / 0.269 (672) | 0.060 / 0.192 (824) | 0.049 / 0.184 (656) | 0.060 / 0.212 (666) | 0.084 / 0.293 (1080) | 0.100 / 0.408 (198) |
| prolate_ar1p5__oblate_ar3_test | 0.214 / 0.790 (762) | 0.124 / 0.500 (972) | 0.099 / 0.357 (644) | 0.095 / 0.366 (730) | 0.103 / 0.376 (892) | 0.150 / 0.532 (96) |
| prolateSpheroid__prolate_ar2_test | 0.154 / 0.580 (644) | 0.090 / 0.443 (916) | 0.082 / 0.390 (698) | 0.095 / 0.337 (660) | 0.092 / 0.373 (966) | 0.082 / 0.384 (212) |
| oblateSpheroid__oblate_ar3_test | 0.173 / 0.680 (772) | 0.099 / 0.377 (966) | 0.086 / 0.340 (822) | 0.081 / 0.331 (752) | 0.099 / 0.344 (754) | 0.179 / 0.427 (30) |
| prolate_ar4__oblateSpheroid_test | 0.212 / 0.832 (690) | 0.149 / 0.584 (970) | 0.107 / 0.483 (702) | 0.099 / 0.445 (754) | 0.096 / 0.420 (906) | 0.081 / 0.488 (74) |
| prolateSpheroid__oblate_ar1p5_test | 0.130 / 0.463 (642) | 0.084 / 0.347 (898) | 0.075 / 0.288 (596) | 0.077 / 0.276 (698) | 0.078 / 0.308 (1092) | 0.092 / 0.482 (170) |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.167 / 0.722 (708) | 0.107 / 0.567 (920) | 0.084 / 0.409 (686) | 0.073 / 0.335 (716) | 0.075 / 0.325 (912) | 0.056 / 0.314 (154) |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.116 / 0.362 (688) | 0.063 / 0.278 (940) | 0.057 / 0.221 (738) | 0.062 / 0.244 (728) | 0.083 / 0.279 (966) | 0.128 / 0.320 (36) |
| prolate_ar2_x1p5__prolate_ar2_test | 0.107 / 0.397 (738) | 0.066 / 0.262 (800) | 0.058 / 0.265 (688) | 0.062 / 0.262 (642) | 0.074 / 0.279 (1024) | 0.084 / 0.351 (204) |
| oblate_ar3_x0p75__oblate_ar3_test | 0.203 / 0.822 (852) | 0.114 / 0.437 (1036) | 0.088 / 0.339 (876) | 0.080 / 0.334 (784) | 0.084 / 0.326 (536) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.161 / 0.647 (702) | 0.114 / 0.467 (890) | 0.100 / 0.393 (718) | 0.098 / 0.473 (776) | 0.115 / 0.476 (960) | 0.141 / 0.646 (50) |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.130 / 0.413 (662) | 0.075 / 0.294 (890) | 0.068 / 0.236 (646) | 0.074 / 0.291 (634) | 0.082 / 0.336 (1148) | 0.115 / 0.499 (116) |
| prolate_ar2__oblate_ar3_test | 1.408 / 4.195 (720) | 1.162 / 3.442 (952) | 0.899 / 2.683 (732) | 0.678 / 1.846 (684) | 0.364 / 1.178 (930) | 0.178 / 0.649 (78) |
| prolate_ar4__oblate_ar1p5_test | 2.099 / 4.657 (714) | 1.714 / 3.894 (934) | 1.149 / 2.557 (666) | 0.603 / 1.494 (704) | 0.252 / 0.820 (916) | 0.132 / 0.630 (162) |
| prolate_ar2p5__oblate_ar2p5_test | 0.922 / 2.307 (728) | 0.813 / 1.985 (940) | 0.569 / 1.537 (700) | 0.349 / 1.085 (750) | 0.160 / 0.719 (922) | 0.118 / 0.501 (56) |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.145 / 0.482 (686) | 0.111 / 0.331 (928) | 0.065 / 0.223 (694) | 0.040 / 0.191 (638) | 0.040 / 0.199 (972) | 0.043 / 0.235 (178) |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 2.413 / 5.683 (780) | 1.832 / 4.611 (938) | 1.366 / 4.018 (684) | 1.045 / 3.572 (706) | 0.920 / 3.233 (944) | 1.220 / 2.757 (44) |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.279 / 1.330 (680) | 0.228 / 1.108 (916) | 0.174 / 0.851 (680) | 0.130 / 0.641 (698) | 0.093 / 0.502 (1026) | 0.083 / 0.458 (96) |

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
| prolateSpheroid__oblateSpheroid_test | 0.027 / 0.093 (102) | 0.004 / 0.014 (110) | 0.002 / 0.006 (82) | 0.001 / 0.005 (98) | 0.001 / 0.004 (110) | - |
| prolate_ar2__oblateSpheroid_test | 0.040 / 0.098 (88) | 0.008 / 0.016 (118) | 0.001 / 0.004 (72) | 0.001 / 0.003 (86) | 0.000 / 0.002 (138) | - |
| prolate_ar4__oblate_ar3_test | 0.108 / 0.584 (66) | 0.054 / 0.281 (160) | 0.038 / 0.134 (86) | 0.023 / 0.095 (96) | 0.019 / 0.073 (102) | - |
| prolate_ar2__oblate_ar1p5_test | 0.010 / 0.046 (80) | 0.000 / 0.002 (104) | 0.000 / 0.000 (76) | 0.000 / 0.000 (96) | 0.000 / 0.000 (128) | 0.000 / 0.000 (28) |
| prolate_ar1p5__oblate_ar3_test | 0.224 / 0.705 (94) | 0.088 / 0.270 (124) | 0.053 / 0.173 (64) | 0.036 / 0.122 (82) | 0.032 / 0.104 (136) | - |
| prolateSpheroid__prolate_ar2_test | 0.029 / 0.222 (68) | 0.006 / 0.020 (132) | 0.002 / 0.005 (102) | 0.002 / 0.004 (70) | 0.001 / 0.004 (110) | 0.001 / 0.003 (30) |
| oblateSpheroid__oblate_ar3_test | 0.131 / 0.588 (94) | 0.063 / 0.189 (134) | 0.059 / 0.160 (92) | 0.034 / 0.108 (84) | 0.024 / 0.083 (104) | - |
| prolate_ar4__oblateSpheroid_test | 0.074 / 0.390 (86) | 0.015 / 0.063 (112) | 0.003 / 0.010 (82) | 0.001 / 0.005 (112) | 0.001 / 0.003 (114) | - |
| prolateSpheroid__oblate_ar1p5_test | 0.032 / 0.171 (72) | 0.004 / 0.020 (106) | 0.002 / 0.004 (94) | 0.001 / 0.004 (84) | 0.001 / 0.003 (134) | 0.001 / 0.003 (22) |
| prolateSpheroid_x0p75__prolateSpheroid_test | 0.047 / 0.419 (92) | 0.008 / 0.045 (102) | 0.002 / 0.006 (82) | 0.002 / 0.005 (96) | 0.001 / 0.004 (118) | 0.001 / 0.004 (22) |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.050 / 0.127 (80) | 0.008 / 0.024 (112) | 0.002 / 0.006 (90) | 0.001 / 0.003 (98) | 0.001 / 0.004 (130) | - |
| prolate_ar2_x1p5__prolate_ar2_test | 0.035 / 0.153 (100) | 0.004 / 0.017 (90) | 0.000 / 0.000 (98) | 0.000 / 0.000 (74) | 0.000 / 0.000 (124) | 0.000 / 0.000 (26) |
| oblate_ar3_x0p75__oblate_ar3_test | 0.091 / 0.330 (94) | 0.080 / 0.278 (134) | 0.046 / 0.168 (114) | 0.031 / 0.127 (110) | 0.027 / 0.128 (58) | - |
| oblateSpheroid_x1p5__prolateSpheroid_x0p75_test | 0.071 / 0.301 (76) | 0.007 / 0.027 (108) | 0.002 / 0.007 (94) | 0.001 / 0.004 (98) | 0.001 / 0.004 (124) | - |
| prolate_ar2_x1p5__oblateSpheroid_test | 0.045 / 0.108 (104) | 0.004 / 0.014 (86) | 0.001 / 0.003 (68) | 0.001 / 0.002 (98) | 0.000 / 0.002 (148) | - |
| prolate_ar2__oblate_ar3_test | 0.198 / 0.758 (100) | 0.063 / 0.207 (122) | 0.067 / 0.197 (94) | 0.047 / 0.154 (82) | 0.030 / 0.107 (106) | - |
| prolate_ar4__oblate_ar1p5_test | 0.150 / 0.713 (96) | 0.032 / 0.091 (122) | 0.006 / 0.028 (86) | 0.002 / 0.005 (94) | 0.000 / 0.001 (96) | - |
| prolate_ar2p5__oblate_ar2p5_test | 0.093 / 0.412 (66) | 0.017 / 0.066 (116) | 0.011 / 0.029 (80) | 0.009 / 0.024 (120) | 0.005 / 0.018 (124) | - |
| prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test | 0.056 / 0.303 (76) | 0.009 / 0.032 (90) | 0.000 / 0.002 (78) | 0.000 / 0.000 (88) | 0.000 / 0.000 (152) | 0.000 / 0.000 (28) |
| oblate_ar3_x0p75__prolate_ar2_x1p5_test | 0.055 / 0.269 (98) | 0.032 / 0.143 (112) | 0.026 / 0.086 (60) | 0.022 / 0.080 (104) | 0.013 / 0.077 (132) | - |
| prolate_ar2p5_x1p25__oblateSpheroid_test | 0.045 / 0.193 (102) | 0.004 / 0.011 (124) | 0.001 / 0.004 (82) | 0.001 / 0.003 (82) | 0.000 / 0.003 (110) | - |

## Conditions

- **Two-body model** `data/final/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 162,188 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `prolate_ar1p5__prolate_ar1p5_test`: prolate_ar1p5 (target or source) with prolate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__prolate_ar2_test`: prolate_ar2 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__prolate_ar4_test`: prolate_ar4 (target or source) with prolate_ar4, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar1p5__oblate_ar1p5_test`: oblate_ar1p5 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar3__oblate_ar3_test`: oblate_ar3 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__oblateSpheroid_test`: prolate_ar2 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__oblate_ar3_test`: prolate_ar4 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__oblate_ar1p5_test`: prolate_ar2 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar1p5__oblate_ar3_test`: prolate_ar1p5 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__prolate_ar2_test`: prolateSpheroid (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid__oblate_ar3_test`: oblateSpheroid (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__oblateSpheroid_test`: prolate_ar4 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid__oblate_ar1p5_test`: prolateSpheroid (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolateSpheroid_x0p75__prolateSpheroid_test`: prolateSpheroid_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2_x1p5__prolate_ar2_test`: prolate_ar2_x1p5 (target or source) with prolate_ar2, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar3_x0p75__oblate_ar3_test`: oblate_ar3_x0p75 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblateSpheroid_x1p5__prolateSpheroid_x0p75_test`: oblateSpheroid_x1p5 (target or source) with prolateSpheroid_x0p75, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2_x1p5__oblateSpheroid_test`: prolate_ar2_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2__oblate_ar3_test`: prolate_ar2 (target or source) with oblate_ar3, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar4__oblate_ar1p5_test`: prolate_ar4 (target or source) with oblate_ar1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2p5__oblate_ar2p5_test`: prolate_ar2p5 (target or source) with oblate_ar2p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2p5_x1p25__prolate_ar2p5_x1p25_test`: prolate_ar2p5_x1p25 (target or source) with prolate_ar2p5_x1p25, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `oblate_ar3_x0p75__prolate_ar2_x1p5_test`: oblate_ar3_x0p75 (target or source) with prolate_ar2_x1p5, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
  - `prolate_ar2p5_x1p25__oblateSpheroid_test`: prolate_ar2p5_x1p25 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
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

