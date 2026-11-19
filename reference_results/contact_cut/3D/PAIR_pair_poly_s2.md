# Two-body accuracy of `data/final_c/models/pair_poly_s2.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.081 | 0.397 | 0.096 | 1.07 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.086 / 0.508 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.070 | 0.386 | 0.094 | 0.77 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.071 / 0.361 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.119 | 0.617 | 0.145 | 1.32 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.125 / 0.661 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.146 | 0.853 | 0.176 | 2.30 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.145 / 0.760 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.239 | 1.508 | 0.274 | 3.87 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.242 / 1.421 | 0.052 / 0.391 | 0.0 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.158 | 0.859 | 0.179 | 2.98 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.142 / 0.687 | 0.046 / 0.249 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.109 | 0.686 | 0.152 | 1.09 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.112 / 0.710 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.096 | 0.639 | 0.134 | 0.85 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.083 / 0.556 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.111 | 0.606 | 0.144 | 1.27 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.120 / 0.839 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.092 | 0.492 | 0.114 | 1.10 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.080 / 0.446 | 0.042 / 0.294 | 0.0 % |
| triaxial_123__triaxial_2_5_test | 4024 | 0.243 | 1.306 | 0.286 | 3.47 | 4.23 / 13.78 | 0.053 / 0.353 (508) | 0.255 / 1.257 | 0.051 / 0.360 | 0.0 % |
| prolateSpheroid__triaxial_2_5_test | 4030 | 0.291 | 1.624 | 0.350 | 3.61 | 4.17 / 15.40 | 0.117 / 0.760 (504) | 0.245 / 1.382 | 0.091 / 0.582 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.109 | 0.701 | 0.153 | 0.97 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.091 / 0.622 | 0.004 / 0.024 | 0.0 % |
| triaxial_123__triaxial_1p5_2_test | 4038 | 0.110 | 0.559 | 0.138 | 1.34 | 4.57 / 11.54 | 0.079 / 0.402 (500) | 0.113 / 0.605 | 0.051 / 0.350 | 0.0 % |
| triaxial_123__triaxial_2_4_test | 4042 | 0.143 | 0.765 | 0.171 | 2.04 | 4.18 / 12.46 | 0.124 / 0.411 (512) | 0.181 / 0.786 | 0.052 / 0.375 | 0.0 % |
| triaxial_123__triaxial_3_4_test | 4036 | 0.189 | 0.999 | 0.222 | 3.00 | 3.83 / 12.07 | 0.114 / 0.792 (506) | 0.179 / 0.982 | 0.051 / 0.293 | 0.0 % |
| oblateSpheroid__triaxial_1p5_2_test | 4048 | 0.084 | 0.492 | 0.113 | 0.91 | 5.12 / 11.20 | 0.019 / 0.060 (506) | 0.075 / 0.496 | 0.006 / 0.039 | 0.0 % |
| prolateSpheroid__triaxial_2_4_test | 4020 | 0.195 | 0.944 | 0.231 | 2.30 | 4.13 / 13.13 | 0.100 / 0.512 (504) | 0.158 / 0.906 | 0.081 / 0.531 | 0.0 % |
| triaxial_2_5__triaxial_3_4_test | 4052 | 0.248 | 1.442 | 0.281 | 4.13 | 3.80 / 12.54 | 0.079 / 0.458 (502) | 0.224 / 1.368 | 0.042 / 0.275 | 0.0 % |
| triaxial_123_x0p75__triaxial_123_test | 4026 | 0.137 | 0.636 | 0.166 | 1.87 | 4.16 / 12.62 | 0.075 / 0.477 (500) | 0.121 / 0.689 | 0.051 / 0.336 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.100 | 0.727 | 0.132 | 1.17 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.102 / 0.777 | 0.004 / 0.024 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_test | 4044 | 0.129 | 0.865 | 0.173 | 1.42 | 4.64 / 12.36 | 0.030 / 0.207 (500) | 0.131 / 0.875 | 0.005 / 0.028 | 0.0 % |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 4024 | 0.092 | 0.490 | 0.113 | 1.17 | 4.73 / 10.69 | 0.041 / 0.184 (512) | 0.109 / 0.522 | 0.014 / 0.094 | 0.0 % |
| triaxial_123_x0p75__prolateSpheroid_test | 4020 | 0.151 | 0.748 | 0.196 | 1.73 | 4.67 / 12.89 | 0.048 / 0.254 (508) | 0.131 / 0.765 | 0.044 / 0.288 | 0.0 % |
| oblateSpheroid_x1p5__triaxial_123_test | 4042 | 0.093 | 0.532 | 0.112 | 1.18 | 4.50 / 10.84 | 0.029 / 0.128 (506) | 0.086 / 0.541 | 0.023 / 0.162 | 0.0 % |
| oblateSpheroid__triaxial_2_5_test | 4016 | 0.863 | 3.699 | 0.974 | 6.76 | 4.37 / 15.31 | 0.072 / 0.571 (502) | 0.844 / 3.699 | 0.061 / 0.418 | 0.0 % |
| triaxial_1p5_2__triaxial_3_4_test | 4020 | 0.632 | 3.398 | 0.746 | 5.89 | 4.05 / 14.29 | 0.098 / 0.402 (496) | 0.573 / 3.112 | 0.071 / 0.395 | 0.0 % |
| triaxial_123__triaxial_2p5_3p5_test | 4034 | 0.140 | 0.732 | 0.164 | 1.87 | 4.09 / 11.77 | 0.061 / 0.389 (504) | 0.159 / 0.778 | 0.053 / 0.350 | 0.0 % |
| prolateSpheroid__triaxial_3_6_test | 4024 | 2.016 | 10.437 | 2.266 | 11.31 | 3.88 / 17.30 | 0.100 / 0.494 (502) | 1.912 / 9.613 | 0.058 / 0.340 | 100.0 % |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 4036 | 0.063 | 0.501 | 0.081 | 0.80 | 5.09 / 9.84 | 0.023 / 0.049 (506) | 0.071 / 0.569 | 0.005 / 0.032 | 0.0 % |
| triaxial_123_x0p75__triaxial_3_4_test | 4024 | 0.767 | 4.026 | 0.923 | 8.33 | 3.75 / 14.24 | 0.111 / 0.515 (502) | 0.781 / 4.321 | 0.071 / 0.397 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 4042 | 0.095 | 0.631 | 0.123 | 1.04 | 4.57 / 11.09 | 0.016 / 0.091 (506) | 0.087 / 0.519 | 0.004 / 0.024 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.123 / 0.505 (666) | 0.066 / 0.332 (868) | 0.048 / 0.288 (688) | 0.042 / 0.268 (672) | 0.043 / 0.284 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.096 / 0.437 (642) | 0.068 / 0.385 (962) | 0.048 / 0.309 (710) | 0.036 / 0.258 (674) | 0.039 / 0.249 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.169 / 0.726 (756) | 0.099 / 0.568 (852) | 0.079 / 0.467 (622) | 0.067 / 0.431 (728) | 0.067 / 0.426 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.211 / 1.147 (706) | 0.126 / 0.678 (872) | 0.096 / 0.537 (730) | 0.085 / 0.570 (648) | 0.085 / 0.587 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.330 / 1.906 (704) | 0.214 / 1.409 (898) | 0.174 / 0.993 (634) | 0.152 / 0.905 (676) | 0.158 / 0.971 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.232 / 1.173 (686) | 0.136 / 0.671 (866) | 0.104 / 0.555 (686) | 0.086 / 0.509 (724) | 0.094 / 0.514 (1058) | - |
| prolateSpheroid__prolateSpheroid_test | 0.149 / 0.810 (684) | 0.097 / 0.637 (898) | 0.084 / 0.565 (660) | 0.075 / 0.512 (754) | 0.073 / 0.622 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.130 / 0.790 (650) | 0.100 / 0.597 (936) | 0.061 / 0.451 (680) | 0.037 / 0.361 (738) | 0.033 / 0.322 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.159 / 0.749 (668) | 0.098 / 0.533 (876) | 0.073 / 0.431 (668) | 0.066 / 0.464 (738) | 0.063 / 0.487 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.140 / 0.639 (686) | 0.072 / 0.409 (916) | 0.054 / 0.330 (684) | 0.046 / 0.306 (688) | 0.042 / 0.276 (1058) | - |
| triaxial_123__triaxial_2_5_test | 0.336 / 1.643 (700) | 0.232 / 1.173 (918) | 0.171 / 0.960 (744) | 0.145 / 0.870 (648) | 0.126 / 0.889 (1014) | - |
| prolateSpheroid__triaxial_2_5_test | 0.433 / 2.264 (626) | 0.256 / 1.374 (962) | 0.192 / 1.045 (656) | 0.168 / 0.920 (710) | 0.156 / 1.021 (1076) | - |
| prolateSpheroid__oblateSpheroid_test | 0.139 / 0.752 (702) | 0.112 / 0.722 (952) | 0.084 / 0.608 (668) | 0.064 / 0.537 (632) | 0.050 / 0.463 (1086) | - |
| triaxial_123__triaxial_1p5_2_test | 0.158 / 0.660 (652) | 0.096 / 0.526 (948) | 0.078 / 0.443 (690) | 0.070 / 0.413 (662) | 0.063 / 0.381 (1086) | - |
| triaxial_123__triaxial_2_4_test | 0.204 / 0.937 (684) | 0.132 / 0.698 (850) | 0.098 / 0.603 (728) | 0.083 / 0.502 (668) | 0.079 / 0.542 (1112) | - |
| triaxial_123__triaxial_3_4_test | 0.274 / 1.312 (658) | 0.171 / 0.867 (932) | 0.120 / 0.638 (676) | 0.109 / 0.619 (724) | 0.098 / 0.565 (1046) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.115 / 0.581 (700) | 0.079 / 0.464 (866) | 0.057 / 0.367 (752) | 0.045 / 0.333 (678) | 0.040 / 0.282 (1052) | - |
| prolateSpheroid__triaxial_2_4_test | 0.285 / 1.190 (678) | 0.170 / 0.794 (876) | 0.128 / 0.763 (728) | 0.107 / 0.672 (686) | 0.100 / 0.666 (1052) | - |
| triaxial_2_5__triaxial_3_4_test | 0.349 / 1.857 (678) | 0.226 / 1.237 (864) | 0.178 / 1.106 (688) | 0.153 / 0.975 (744) | 0.154 / 1.045 (1078) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.200 / 0.819 (666) | 0.117 / 0.538 (942) | 0.089 / 0.439 (686) | 0.076 / 0.416 (698) | 0.069 / 0.402 (1034) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.138 / 0.867 (662) | 0.095 / 0.710 (936) | 0.068 / 0.504 (688) | 0.058 / 0.429 (712) | 0.050 / 0.321 (1034) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.174 / 1.086 (716) | 0.117 / 0.782 (888) | 0.089 / 0.586 (688) | 0.092 / 0.652 (726) | 0.088 / 0.647 (1026) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.128 / 0.574 (642) | 0.080 / 0.454 (836) | 0.068 / 0.411 (674) | 0.059 / 0.366 (706) | 0.059 / 0.345 (1166) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.203 / 0.894 (742) | 0.139 / 0.693 (864) | 0.106 / 0.572 (710) | 0.098 / 0.501 (658) | 0.085 / 0.502 (1046) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.136 / 0.645 (664) | 0.079 / 0.502 (938) | 0.059 / 0.381 (692) | 0.053 / 0.326 (632) | 0.059 / 0.354 (1116) | - |
| oblateSpheroid__triaxial_2_5_test | 1.073 / 4.213 (690) | 0.944 / 3.625 (878) | 0.683 / 3.256 (712) | 0.501 / 2.634 (674) | 0.375 / 2.037 (1062) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.844 / 4.269 (672) | 0.611 / 3.192 (918) | 0.474 / 2.430 (608) | 0.449 / 1.730 (676) | 0.349 / 1.356 (1146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.194 / 0.905 (650) | 0.131 / 0.692 (912) | 0.100 / 0.517 (700) | 0.087 / 0.477 (664) | 0.078 / 0.442 (1108) | - |
| prolateSpheroid__triaxial_3_6_test | 2.660 / 12.701 (654) | 2.059 / 10.360 (872) | 1.614 / 8.352 (702) | 1.309 / 7.020 (678) | 1.092 / 5.910 (1118) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.084 / 0.629 (636) | 0.060 / 0.446 (896) | 0.043 / 0.368 (620) | 0.039 / 0.306 (676) | 0.038 / 0.250 (1208) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 1.060 / 5.105 (738) | 0.732 / 3.661 (896) | 0.502 / 2.785 (730) | 0.403 / 2.015 (632) | 0.390 / 1.574 (1028) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.132 / 0.737 (672) | 0.086 / 0.616 (936) | 0.069 / 0.442 (714) | 0.066 / 0.536 (690) | 0.070 / 0.603 (1030) | - |

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.129 / 0.789 (68) | 0.040 / 0.185 (116) | 0.015 / 0.051 (90) | 0.008 / 0.038 (78) | 0.006 / 0.028 (146) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.032 / 0.127 (70) | 0.004 / 0.014 (140) | 0.001 / 0.004 (90) | 0.001 / 0.002 (76) | 0.000 / 0.002 (126) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.157 / 0.667 (102) | 0.035 / 0.162 (100) | 0.011 / 0.039 (64) | 0.006 / 0.025 (98) | 0.004 / 0.016 (142) | - |
| triaxial_2_4__triaxial_2_4_test | 0.172 / 0.596 (74) | 0.039 / 0.291 (94) | 0.015 / 0.091 (92) | 0.008 / 0.038 (78) | 0.005 / 0.025 (168) | - |
| triaxial_2_5__triaxial_2_5_test | 0.120 / 0.507 (118) | 0.039 / 0.239 (90) | 0.018 / 0.098 (66) | 0.015 / 0.075 (104) | 0.009 / 0.052 (128) | - |
| triaxial_3_4__triaxial_3_4_test | 0.096 / 0.399 (102) | 0.050 / 0.255 (94) | 0.029 / 0.120 (64) | 0.015 / 0.071 (104) | 0.009 / 0.046 (140) | - |
| prolateSpheroid__prolateSpheroid_test | 0.044 / 0.249 (74) | 0.007 / 0.030 (110) | 0.002 / 0.006 (76) | 0.002 / 0.005 (96) | 0.001 / 0.005 (146) | - |
| oblateSpheroid__oblateSpheroid_test | 0.023 / 0.043 (72) | 0.005 / 0.011 (118) | 0.002 / 0.005 (68) | 0.001 / 0.004 (116) | 0.001 / 0.003 (130) | - |
| triaxial_123__prolateSpheroid_test | 0.125 / 0.868 (84) | 0.046 / 0.195 (126) | 0.012 / 0.046 (80) | 0.009 / 0.031 (80) | 0.004 / 0.025 (138) | - |
| triaxial_123__oblateSpheroid_test | 0.128 / 0.548 (80) | 0.030 / 0.101 (118) | 0.012 / 0.057 (90) | 0.008 / 0.028 (76) | 0.004 / 0.023 (140) | - |
| triaxial_123__triaxial_2_5_test | 0.094 / 0.606 (64) | 0.045 / 0.223 (144) | 0.015 / 0.065 (82) | 0.015 / 0.066 (84) | 0.010 / 0.052 (134) | - |
| prolateSpheroid__triaxial_2_5_test | 0.241 / 1.467 (64) | 0.055 / 0.193 (118) | 0.025 / 0.109 (94) | 0.012 / 0.068 (102) | 0.010 / 0.050 (126) | - |
| prolateSpheroid__oblateSpheroid_test | 0.035 / 0.104 (96) | 0.006 / 0.018 (122) | 0.002 / 0.006 (76) | 0.001 / 0.005 (74) | 0.001 / 0.004 (138) | - |
| triaxial_123__triaxial_1p5_2_test | 0.154 / 0.697 (62) | 0.043 / 0.141 (138) | 0.015 / 0.050 (96) | 0.009 / 0.036 (66) | 0.005 / 0.022 (138) | - |
| triaxial_123__triaxial_2_4_test | 0.198 / 0.607 (114) | 0.041 / 0.173 (86) | 0.017 / 0.058 (86) | 0.010 / 0.039 (72) | 0.005 / 0.027 (154) | - |
| triaxial_123__triaxial_3_4_test | 0.183 / 1.217 (104) | 0.058 / 0.215 (114) | 0.033 / 0.147 (76) | 0.017 / 0.067 (80) | 0.009 / 0.040 (132) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.034 / 0.091 (86) | 0.005 / 0.016 (106) | 0.001 / 0.005 (106) | 0.001 / 0.003 (78) | 0.000 / 0.003 (130) | - |
| prolateSpheroid__triaxial_2_4_test | 0.195 / 0.845 (66) | 0.067 / 0.366 (98) | 0.019 / 0.078 (116) | 0.008 / 0.041 (102) | 0.006 / 0.025 (122) | - |
| triaxial_2_5__triaxial_3_4_test | 0.134 / 0.716 (86) | 0.054 / 0.307 (108) | 0.028 / 0.104 (86) | 0.014 / 0.068 (94) | 0.010 / 0.052 (128) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.133 / 0.784 (76) | 0.047 / 0.217 (120) | 0.018 / 0.064 (100) | 0.008 / 0.036 (94) | 0.006 / 0.027 (110) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.065 / 0.188 (72) | 0.008 / 0.026 (112) | 0.001 / 0.005 (96) | 0.001 / 0.004 (82) | 0.001 / 0.003 (142) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.051 / 0.326 (106) | 0.007 / 0.026 (118) | 0.002 / 0.007 (64) | 0.002 / 0.005 (78) | 0.001 / 0.005 (134) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.071 / 0.289 (90) | 0.008 / 0.023 (110) | 0.001 / 0.005 (84) | 0.001 / 0.003 (82) | 0.000 / 0.002 (146) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.085 / 0.411 (78) | 0.020 / 0.086 (100) | 0.009 / 0.040 (86) | 0.005 / 0.022 (90) | 0.004 / 0.020 (154) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.052 / 0.205 (80) | 0.016 / 0.061 (96) | 0.007 / 0.027 (98) | 0.004 / 0.025 (74) | 0.004 / 0.023 (158) | - |
| oblateSpheroid__triaxial_2_5_test | 0.119 / 0.902 (98) | 0.038 / 0.163 (104) | 0.021 / 0.076 (78) | 0.012 / 0.047 (90) | 0.007 / 0.037 (132) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.152 / 0.616 (84) | 0.092 / 0.296 (112) | 0.051 / 0.182 (84) | 0.020 / 0.074 (70) | 0.010 / 0.039 (146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.102 / 0.617 (92) | 0.034 / 0.198 (128) | 0.021 / 0.091 (84) | 0.012 / 0.076 (86) | 0.008 / 0.069 (114) | - |
| prolateSpheroid__triaxial_3_6_test | 0.163 / 0.776 (80) | 0.108 / 0.481 (90) | 0.029 / 0.108 (118) | 0.018 / 0.061 (72) | 0.013 / 0.057 (142) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.040 / 0.074 (86) | 0.008 / 0.013 (102) | 0.001 / 0.004 (84) | 0.001 / 0.003 (74) | 0.000 / 0.003 (160) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 0.179 / 0.771 (86) | 0.090 / 0.407 (100) | 0.050 / 0.195 (86) | 0.024 / 0.088 (96) | 0.011 / 0.039 (134) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.033 / 0.166 (66) | 0.005 / 0.025 (108) | 0.002 / 0.006 (90) | 0.002 / 0.006 (116) | 0.001 / 0.004 (126) | - |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly_s2.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 2: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_1p5_2_test`: triaxial_1p5_2 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_3__triaxial_1p5_3_test`: triaxial_1p5_3 (target or source) with triaxial_1p5_3, 2048 configurations (both orderings scored: 4028 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_4__triaxial_2_4_test`: triaxial_2_4 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_2_5_test`: triaxial_2_5 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_3_4__triaxial_3_4_test`: triaxial_3_4 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__prolateSpheroid_test`: prolateSpheroid (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4022 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__prolateSpheroid_test`: triaxial_123 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__oblateSpheroid_test`: triaxial_123 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_5_test`: triaxial_123 (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_5_test`: prolateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4030 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__oblateSpheroid_test`: prolateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4040 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_1p5_2_test`: triaxial_123 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4038 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2_4_test`: triaxial_123 (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_3_4_test`: triaxial_123 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_1p5_2_test`: oblateSpheroid (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4048 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_2_4_test`: prolateSpheroid (target or source) with triaxial_2_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_2_5__triaxial_3_4_test`: triaxial_2_5 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4052 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_123_test`: triaxial_123_x0p75 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4026 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__oblateSpheroid_test`: oblateSpheroid_x1p5 (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4032 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4044 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2_x1p5__triaxial_1p5_2_test`: triaxial_1p5_2_x1p5 (target or source) with triaxial_1p5_2, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__prolateSpheroid_test`: triaxial_123_x0p75 (target or source) with prolateSpheroid, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_123_test`: oblateSpheroid_x1p5 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid__triaxial_2_5_test`: oblateSpheroid (target or source) with triaxial_2_5, 2048 configurations (both orderings scored: 4016 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_1p5_2__triaxial_3_4_test`: triaxial_1p5_2 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4020 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123__triaxial_2p5_3p5_test`: triaxial_123 (target or source) with triaxial_2p5_3p5, 2048 configurations (both orderings scored: 4034 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid__triaxial_3_6_test`: prolateSpheroid (target or source) with triaxial_3_6, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test`: oblateSpheroid_x1p5 (target or source) with triaxial_1p5_2_x1p5, 2048 configurations (both orderings scored: 4036 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `triaxial_123_x0p75__triaxial_3_4_test`: triaxial_123_x0p75 (target or source) with triaxial_3_4, 2048 configurations (both orderings scored: 4024 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
  - `prolateSpheroid_x1p25__prolateSpheroid_x1p25_test`: prolateSpheroid_x1p25 (target or source) with prolateSpheroid_x1p25, 2048 configurations (both orderings scored: 4042 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 3.2], any centre distance
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

