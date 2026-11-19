# Two-body accuracy of `data/final/models/pair_t123.pt`

All numbers are % errors.

| set | rows | model: trans | rot | whole block | self | far field alone trans / rot | MFS fine vs Xfine: trans / rot (rows) | model vs Xfine: trans / rot | MFS reciprocity defect: trans / rot | outside training range |
|---|---|---|---|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 4096 | 0.061 | 0.296 | 0.072 | 0.75 | 4.33 / 11.49 | 0.078 / 0.456 (512) | 0.063 / 0.352 | 0.041 / 0.300 | 0.0 % |

## Model error by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.096 / 0.428 (660) | 0.047 / 0.215 (956) | 0.032 / 0.142 (738) | 0.031 / 0.138 (698) | 0.035 / 0.150 (960) | 0.051 / 0.222 (84) |

## MFS error (fine vs Xfine) by contact factor: trans / rot (rows)

| set | c 1-1.1 | c 1.1-1.25 | c 1.25-1.5 | c 1.5-2 | c 2-4 | c > 4 |
|---|---|---|---|---|---|---|
| triaxial_123__triaxial_123_test | 0.152 / 0.755 (68) | 0.035 / 0.157 (130) | 0.014 / 0.071 (86) | 0.008 / 0.033 (72) | 0.005 / 0.027 (142) | - |

## Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Test pairs**: two particles, orientations uniform on SO(3), direction uniform on the sphere; seeds never used in training:
  - `triaxial_123__triaxial_123_test`: triaxial_123 (target or source) with triaxial_123, 2048 configurations (both orderings scored: 4096 rows inside r_cut), contact factor c with c - 1 log-uniform in [0.05, 7], centre distance below 14 pair lengths
- **Metric**: one random unit force and one random unit torque on the source of every pair (fixed seed); PRMSE (%) of the target's velocity (trans) and angular velocity (rot) over all rows; whole block = Frobenius error of the 6x6 cross block; self = Frobenius error of M_tt - M_iso.
- **MFS columns**: `fine vs Xfine` = the same pairs solved with both cloud resolutions, same metric (the label floor); `reciprocity defect` = raw MFS block against its symmetrised value, same metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; ONE direct dense solve per pair (exact to round-off for its cloud); blocks read from the symmetrised matrix 1/2 (M + M^T).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

