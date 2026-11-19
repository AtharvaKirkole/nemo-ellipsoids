# Two-body accuracy of `data/final_c/models/pair_poly.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4044 | 0.081 | 0.401 | 0.097 | 1.12 | 4.37 / 11.50 | 0.069 / 0.461 (498) | 0.084 / 0.499 | 0.040 / 0.283 | 0.0 % |
| triaxial_1p5_2__triaxial_1p5_2_test | 4028 | 0.071 | 0.383 | 0.095 | 0.77 | 5.22 / 11.03 | 0.016 / 0.073 (502) | 0.073 / 0.356 | 0.009 / 0.053 | 0.0 % |
| triaxial_1p5_3__triaxial_1p5_3_test | 4028 | 0.117 | 0.646 | 0.147 | 1.38 | 4.67 / 11.85 | 0.095 / 0.466 (506) | 0.122 / 0.710 | 0.059 / 0.382 | 0.0 % |
| triaxial_2_4__triaxial_2_4_test | 4034 | 0.155 | 0.908 | 0.183 | 2.41 | 4.19 / 12.82 | 0.092 / 0.384 (506) | 0.158 / 0.814 | 0.051 / 0.371 | 0.0 % |
| triaxial_2_5__triaxial_2_5_test | 4052 | 0.243 | 1.538 | 0.283 | 3.97 | 4.26 / 14.71 | 0.077 / 0.376 (506) | 0.245 / 1.482 | 0.052 / 0.391 | 0.0 % |
| triaxial_3_4__triaxial_3_4_test | 4020 | 0.164 | 0.876 | 0.184 | 3.11 | 3.67 / 11.39 | 0.062 / 0.306 (504) | 0.141 / 0.727 | 0.046 / 0.249 | 0.0 % |
| prolateSpheroid__prolateSpheroid_test | 4034 | 0.112 | 0.789 | 0.168 | 1.19 | 4.79 / 11.93 | 0.024 / 0.140 (502) | 0.116 / 0.840 | 0.004 / 0.024 | 0.0 % |
| oblateSpheroid__oblateSpheroid_test | 4022 | 0.095 | 0.631 | 0.133 | 0.85 | 4.97 / 11.39 | 0.012 / 0.027 (504) | 0.081 / 0.545 | 0.004 / 0.020 | 0.0 % |
| triaxial_123__prolateSpheroid_test | 4052 | 0.111 | 0.615 | 0.143 | 1.34 | 4.39 / 12.12 | 0.073 / 0.527 (508) | 0.118 / 0.899 | 0.055 / 0.389 | 0.0 % |
| triaxial_123__oblateSpheroid_test | 4032 | 0.094 | 0.496 | 0.115 | 1.11 | 4.57 / 11.38 | 0.071 / 0.330 (504) | 0.078 / 0.432 | 0.042 / 0.294 | 0.0 % |
| triaxial_123__triaxial_2_5_test | 4024 | 0.246 | 1.328 | 0.286 | 3.46 | 4.23 / 13.78 | 0.053 / 0.353 (508) | 0.236 / 1.433 | 0.051 / 0.360 | 0.0 % |
| prolateSpheroid__triaxial_2_5_test | 4030 | 0.301 | 1.645 | 0.355 | 3.62 | 4.17 / 15.40 | 0.117 / 0.760 (504) | 0.249 / 1.427 | 0.091 / 0.582 | 0.0 % |
| prolateSpheroid__oblateSpheroid_test | 4040 | 0.106 | 0.694 | 0.151 | 0.97 | 4.83 / 11.88 | 0.020 / 0.066 (506) | 0.087 / 0.611 | 0.004 / 0.024 | 0.0 % |
| triaxial_123__triaxial_1p5_2_test | 4038 | 0.114 | 0.572 | 0.140 | 1.36 | 4.57 / 11.54 | 0.079 / 0.402 (500) | 0.112 / 0.590 | 0.051 / 0.350 | 0.0 % |
| triaxial_123__triaxial_2_4_test | 4042 | 0.139 | 0.778 | 0.169 | 2.06 | 4.18 / 12.46 | 0.124 / 0.411 (512) | 0.169 / 0.821 | 0.052 / 0.375 | 0.0 % |
| triaxial_123__triaxial_3_4_test | 4036 | 0.208 | 1.010 | 0.236 | 3.00 | 3.83 / 12.07 | 0.114 / 0.792 (506) | 0.195 / 0.970 | 0.051 / 0.293 | 0.0 % |
| oblateSpheroid__triaxial_1p5_2_test | 4048 | 0.087 | 0.499 | 0.116 | 0.93 | 5.12 / 11.20 | 0.019 / 0.060 (506) | 0.077 / 0.480 | 0.006 / 0.039 | 0.0 % |
| prolateSpheroid__triaxial_2_4_test | 4020 | 0.190 | 0.966 | 0.230 | 2.34 | 4.13 / 13.13 | 0.100 / 0.512 (504) | 0.165 / 0.877 | 0.081 / 0.531 | 0.0 % |
| triaxial_2_5__triaxial_3_4_test | 4052 | 0.261 | 1.449 | 0.296 | 4.22 | 3.80 / 12.54 | 0.079 / 0.458 (502) | 0.230 / 1.372 | 0.042 / 0.275 | 0.0 % |
| triaxial_123_x0p75__triaxial_123_test | 4026 | 0.137 | 0.636 | 0.165 | 1.91 | 4.16 / 12.62 | 0.075 / 0.477 (500) | 0.134 / 0.645 | 0.051 / 0.336 | 0.0 % |
| oblateSpheroid_x1p5__oblateSpheroid_test | 4032 | 0.103 | 0.723 | 0.134 | 1.20 | 4.47 / 11.22 | 0.034 / 0.111 (504) | 0.100 / 0.771 | 0.004 / 0.024 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_test | 4044 | 0.138 | 0.956 | 0.186 | 1.52 | 4.64 / 12.36 | 0.030 / 0.207 (500) | 0.132 / 0.981 | 0.005 / 0.028 | 0.0 % |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 4024 | 0.092 | 0.507 | 0.113 | 1.15 | 4.73 / 10.69 | 0.041 / 0.184 (512) | 0.105 / 0.517 | 0.014 / 0.094 | 0.0 % |
| triaxial_123_x0p75__prolateSpheroid_test | 4020 | 0.150 | 0.764 | 0.198 | 1.77 | 4.67 / 12.89 | 0.048 / 0.254 (508) | 0.140 / 0.771 | 0.044 / 0.288 | 0.0 % |
| oblateSpheroid_x1p5__triaxial_123_test | 4042 | 0.101 | 0.532 | 0.116 | 1.19 | 4.50 / 10.84 | 0.029 / 0.128 (506) | 0.094 / 0.517 | 0.023 / 0.162 | 0.0 % |
| oblateSpheroid__triaxial_2_5_test | 4016 | 0.747 | 4.495 | 0.920 | 6.37 | 4.37 / 15.31 | 0.072 / 0.571 (502) | 0.779 / 4.621 | 0.061 / 0.418 | 0.0 % |
| triaxial_1p5_2__triaxial_3_4_test | 4020 | 0.667 | 3.033 | 0.763 | 5.22 | 4.05 / 14.29 | 0.098 / 0.402 (496) | 0.644 / 2.703 | 0.071 / 0.395 | 0.0 % |
| triaxial_123__triaxial_2p5_3p5_test | 4034 | 0.180 | 1.231 | 0.231 | 2.02 | 4.09 / 11.77 | 0.061 / 0.389 (504) | 0.182 / 1.273 | 0.053 / 0.350 | 0.0 % |
| prolateSpheroid__triaxial_3_6_test | 4024 | 1.883 | 9.977 | 2.141 | 12.08 | 3.88 / 17.30 | 0.100 / 0.494 (502) | 1.812 / 9.474 | 0.058 / 0.340 | 100.0 % |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 4036 | 0.062 | 0.496 | 0.081 | 0.82 | 5.09 / 9.84 | 0.023 / 0.049 (506) | 0.073 / 0.572 | 0.005 / 0.032 | 0.0 % |
| triaxial_123_x0p75__triaxial_3_4_test | 4024 | 0.700 | 4.061 | 0.867 | 6.94 | 3.75 / 14.24 | 0.111 / 0.515 (502) | 0.677 / 4.256 | 0.071 / 0.397 | 0.0 % |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 4042 | 0.098 | 0.717 | 0.132 | 1.13 | 4.57 / 11.09 | 0.016 / 0.091 (506) | 0.089 / 0.602 | 0.004 / 0.024 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.122 / 0.512 (666) | 0.067 / 0.338 (868) | 0.047 / 0.282 (688) | 0.045 / 0.269 (672) | 0.046 / 0.284 (1150) | - |
| triaxial_1p5_2__triaxial_1p5_2_test | 0.096 / 0.440 (642) | 0.068 / 0.375 (962) | 0.051 / 0.317 (710) | 0.040 / 0.245 (674) | 0.037 / 0.245 (1040) | - |
| triaxial_1p5_3__triaxial_1p5_3_test | 0.163 / 0.761 (756) | 0.102 / 0.593 (852) | 0.076 / 0.488 (622) | 0.070 / 0.456 (728) | 0.063 / 0.455 (1070) | - |
| triaxial_2_4__triaxial_2_4_test | 0.227 / 1.224 (706) | 0.130 / 0.733 (872) | 0.095 / 0.563 (730) | 0.093 / 0.553 (648) | 0.091 / 0.597 (1078) | - |
| triaxial_2_5__triaxial_2_5_test | 0.330 / 1.947 (704) | 0.230 / 1.431 (898) | 0.173 / 1.037 (634) | 0.148 / 0.882 (676) | 0.147 / 0.993 (1140) | - |
| triaxial_3_4__triaxial_3_4_test | 0.243 / 1.192 (686) | 0.132 / 0.684 (866) | 0.106 / 0.596 (686) | 0.096 / 0.508 (724) | 0.098 / 0.522 (1058) | - |
| prolateSpheroid__prolateSpheroid_test | 0.151 / 0.954 (684) | 0.101 / 0.723 (898) | 0.088 / 0.634 (660) | 0.076 / 0.548 (754) | 0.075 / 0.631 (1038) | - |
| oblateSpheroid__oblateSpheroid_test | 0.129 / 0.785 (650) | 0.099 / 0.586 (936) | 0.059 / 0.435 (680) | 0.036 / 0.363 (738) | 0.031 / 0.323 (1018) | - |
| triaxial_123__prolateSpheroid_test | 0.157 / 0.756 (668) | 0.099 / 0.544 (876) | 0.074 / 0.445 (668) | 0.067 / 0.469 (738) | 0.067 / 0.497 (1102) | - |
| triaxial_123__oblateSpheroid_test | 0.144 / 0.642 (686) | 0.073 / 0.412 (916) | 0.056 / 0.342 (684) | 0.045 / 0.318 (688) | 0.042 / 0.299 (1058) | - |
| triaxial_123__triaxial_2_5_test | 0.346 / 1.670 (700) | 0.226 / 1.173 (918) | 0.164 / 0.997 (744) | 0.151 / 0.949 (648) | 0.141 / 0.921 (1014) | - |
| prolateSpheroid__triaxial_2_5_test | 0.448 / 2.279 (626) | 0.264 / 1.396 (962) | 0.200 / 1.092 (656) | 0.171 / 0.950 (710) | 0.159 / 1.004 (1076) | - |
| prolateSpheroid__oblateSpheroid_test | 0.137 / 0.754 (702) | 0.106 / 0.710 (952) | 0.081 / 0.585 (668) | 0.062 / 0.527 (632) | 0.047 / 0.459 (1086) | - |
| triaxial_123__triaxial_1p5_2_test | 0.161 / 0.685 (652) | 0.105 / 0.533 (948) | 0.078 / 0.437 (690) | 0.066 / 0.408 (662) | 0.060 / 0.388 (1086) | - |
| triaxial_123__triaxial_2_4_test | 0.195 / 0.961 (684) | 0.126 / 0.711 (850) | 0.097 / 0.587 (728) | 0.083 / 0.514 (668) | 0.082 / 0.538 (1112) | - |
| triaxial_123__triaxial_3_4_test | 0.316 / 1.337 (658) | 0.177 / 0.864 (932) | 0.128 / 0.640 (676) | 0.104 / 0.611 (724) | 0.100 / 0.594 (1046) | - |
| oblateSpheroid__triaxial_1p5_2_test | 0.123 / 0.604 (700) | 0.077 / 0.448 (866) | 0.058 / 0.378 (752) | 0.044 / 0.334 (678) | 0.042 / 0.286 (1052) | - |
| prolateSpheroid__triaxial_2_4_test | 0.276 / 1.217 (678) | 0.167 / 0.786 (876) | 0.131 / 0.834 (728) | 0.109 / 0.696 (686) | 0.104 / 0.671 (1052) | - |
| triaxial_2_5__triaxial_3_4_test | 0.360 / 1.839 (678) | 0.239 / 1.260 (864) | 0.193 / 1.123 (688) | 0.173 / 1.054 (744) | 0.172 / 1.050 (1078) | - |
| triaxial_123_x0p75__triaxial_123_test | 0.200 / 0.809 (666) | 0.117 / 0.546 (942) | 0.089 / 0.447 (686) | 0.076 / 0.442 (698) | 0.072 / 0.422 (1034) | - |
| oblateSpheroid_x1p5__oblateSpheroid_test | 0.146 / 0.866 (662) | 0.096 / 0.702 (936) | 0.068 / 0.498 (688) | 0.053 / 0.423 (712) | 0.047 / 0.326 (1034) | - |
| prolateSpheroid_x1p25__prolateSpheroid_test | 0.194 / 1.202 (716) | 0.123 / 0.889 (888) | 0.084 / 0.615 (688) | 0.091 / 0.669 (726) | 0.082 / 0.645 (1026) | - |
| triaxial_1p5_2_x1p5__triaxial_1p5_2_test | 0.131 / 0.604 (642) | 0.080 / 0.468 (836) | 0.064 / 0.402 (674) | 0.056 / 0.357 (706) | 0.058 / 0.355 (1166) | - |
| triaxial_123_x0p75__prolateSpheroid_test | 0.199 / 0.910 (742) | 0.144 / 0.702 (864) | 0.107 / 0.594 (710) | 0.097 / 0.537 (658) | 0.085 / 0.535 (1046) | - |
| oblateSpheroid_x1p5__triaxial_123_test | 0.147 / 0.638 (664) | 0.083 / 0.500 (938) | 0.065 / 0.395 (692) | 0.060 / 0.359 (632) | 0.065 / 0.362 (1116) | - |
| oblateSpheroid__triaxial_2_5_test | 0.945 / 5.156 (690) | 0.789 / 4.408 (878) | 0.621 / 3.887 (712) | 0.436 / 3.105 (674) | 0.292 / 2.388 (1062) | - |
| triaxial_1p5_2__triaxial_3_4_test | 0.861 / 3.547 (672) | 0.668 / 2.965 (918) | 0.567 / 2.540 (608) | 0.456 / 2.051 (676) | 0.281 / 1.457 (1146) | - |
| triaxial_123__triaxial_2p5_3p5_test | 0.237 / 1.375 (650) | 0.171 / 1.233 (912) | 0.148 / 1.055 (700) | 0.121 / 0.958 (664) | 0.104 / 0.943 (1108) | - |
| prolateSpheroid__triaxial_3_6_test | 2.625 / 12.616 (654) | 2.021 / 9.919 (872) | 1.260 / 7.317 (702) | 0.806 / 5.573 (678) | 0.562 / 4.207 (1118) | - |
| oblateSpheroid_x1p5__triaxial_1p5_2_x1p5_test | 0.082 / 0.625 (636) | 0.060 / 0.439 (896) | 0.043 / 0.361 (620) | 0.039 / 0.300 (676) | 0.042 / 0.254 (1208) | - |
| triaxial_123_x0p75__triaxial_3_4_test | 0.972 / 5.216 (738) | 0.685 / 3.668 (896) | 0.451 / 2.656 (730) | 0.331 / 1.882 (632) | 0.231 / 1.475 (1028) | - |
| prolateSpheroid_x1p25__prolateSpheroid_x1p25_test | 0.136 / 0.846 (672) | 0.090 / 0.712 (936) | 0.072 / 0.472 (714) | 0.066 / 0.561 (690) | 0.068 / 0.634 (1030) | - |

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

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
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

