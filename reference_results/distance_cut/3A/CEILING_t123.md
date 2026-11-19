# Ceiling of the many-body correction, triaxial_123

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.14 (7.10 / 10.29) | 5.05 (5.04 / 6.55) | 2.23 (2.21 / 3.45) | 1.72 (1.73 / 1.92) | 1.66 (1.66 / 1.84) |
| 0.1 | 64 | 3 | 10.74 (10.61 / 20.10) | 7.99 (7.85 / 16.88) | 3.00 (2.93 / 7.02) | 2.32 (2.31 / 3.37) | 2.21 (2.20 / 2.85) |
| 0.2 | 64 | 3 | 23.64 (23.36 / 37.66) | 18.75 (18.45 / 32.13) | 5.40 (5.27 / 10.62) | 4.50 (4.47 / 6.30) | 3.74 (3.74 / 3.70) |

## Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
- **Configurations**: N in [64], shapes triaxial_123 in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

