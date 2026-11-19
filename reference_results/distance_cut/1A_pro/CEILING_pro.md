# Ceiling of the many-body correction, prolateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 8.54 (8.69 / 6.55) | 5.48 (5.57 / 4.44) | 2.53 (2.56 / 2.23) | 1.70 (1.74 / 1.04) | 1.64 (1.69 / 0.99) |
| 0.1 | 64 | 3 | 13.28 (13.27 / 14.44) | 10.15 (10.12 / 11.76) | 3.52 (3.49 / 4.53) | 2.30 (2.33 / 2.02) | 2.23 (2.26 / 1.75) |
| 0.2 | 64 | 3 | 18.62 (18.29 / 29.24) | 14.98 (14.69 / 24.25) | 3.83 (3.65 / 8.35) | 2.64 (2.60 / 3.99) | 1.94 (1.94 / 2.02) |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
- **Configurations**: N in [64], shapes prolateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

