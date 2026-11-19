# Ceiling of the many-body correction, triaxial_123, prolateSpheroid, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.69 (7.65 / 8.50) | 4.99 (4.98 / 5.39) | 2.33 (2.31 / 2.80) | 1.68 (1.69 / 1.38) | 1.58 (1.59 / 1.21) |
| 0.1 | 64 | 3 | 13.26 (13.18 / 15.32) | 9.36 (9.27 / 11.50) | 3.70 (3.63 / 5.11) | 2.36 (2.38 / 2.04) | 2.17 (2.19 / 1.72) |
| 0.2 | 64 | 3 | 26.36 (26.15 / 35.18) | 21.79 (21.54 / 31.09) | 5.18 (5.01 / 9.49) | 3.51 (3.49 / 4.37) | 2.15 (2.18 / 1.62) |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configurations**: N in [64], shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

