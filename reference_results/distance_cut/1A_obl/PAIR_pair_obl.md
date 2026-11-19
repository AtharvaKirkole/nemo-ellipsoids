# Two-body accuracy of `data/final/models/pair_obl.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 4096 | 0.019 | 0.158 | 0.030 | 0.24 | 4.97 / 11.38 | 0.013 / 0.036 (512) | 0.022 / 0.168 | 0.003 / 0.019 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.029 / 0.187 (668) | 0.015 / 0.146 (956) | 0.009 / 0.124 (734) | 0.009 / 0.125 (720) | 0.011 / 0.151 (984) | 0.017 / 0.052 (34) |

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| oblateSpheroid__oblateSpheroid_test | 0.025 / 0.060 (66) | 0.008 / 0.017 (112) | 0.001 / 0.005 (110) | 0.001 / 0.003 (76) | 0.001 / 0.003 (142) | - |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `oblateSpheroid__oblateSpheroid_test`: oblateSpheroid (target or source) with oblateSpheroid, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 12 pair lengths
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

