# Ceiling of the many-body correction, oblateSpheroid

PRMSE % of all six velocity components (translation / rotation).  'exact f_nb' = the two-body operator with every cross block inside the pair cutoff replaced by the MFS block; '+ exact self' = every self block too: the floor of ANY near-field correction (only pairs beyond the cutoff are still approximate).

| phi | N | n | far field | + two-body | + many-body | exact f_nb | exact f_nb + exact self |
|---|---|---|---|---|---|---|---|
| 0.05 | 64 | 3 | 7.88 (7.80 / 9.90) | 5.10 (5.06 / 6.13) | 2.69 (2.68 / 2.90) | 2.08 (2.09 / 1.82) | 2.02 (2.03 / 1.71) |
| 0.1 | 64 | 3 | 12.86 (12.72 / 17.02) | 9.80 (9.71 / 12.72) | 3.81 (3.75 / 5.50) | 3.07 (3.07 / 2.90) | 2.88 (2.89 / 2.56) |
| 0.2 | 64 | 3 | 25.37 (25.10 / 34.07) | 19.92 (19.68 / 27.03) | 5.70 (5.59 / 8.56) | 4.72 (4.73 / 5.07) | 3.90 (3.96 / 2.73) |

## Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configurations**: N in [64], shapes oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per (phi, N); a configuration whose MFS solve does not converge is skipped (n counts those kept).
- **Load and metric**: a random unit force and torque on every particle (x 6 pi); PRMSE as in the suspension test.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole (6N, 6N) mobility matrix of each configuration (direct solve when small, else GMRES with the plain torch kernel, velocity tolerance 1e-07, 24 unit loads at a time), symmetrised.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

