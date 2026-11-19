# Suspensions of oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.58 (4.56 / 5.17; 1.13) | 2.89 (2.90 / 2.86; 0.95) | 1.85 (1.86 / 1.74; 0.71) | 0.002 (0.002 / 0.004; 0.000) (1) |
| 0.05 | 200 | 10 | 6.93 (6.89 / 8.87; 2.16) | 5.01 (4.99 / 6.04; 1.88) | 2.94 (2.94 / 3.33; 1.19) | 0.010 (0.009 / 0.023; 0.001) (1) |
| 0.075 | 200 | 10 | 10.13 (10.06 / 13.11; 3.20) | 7.73 (7.69 / 9.52; 2.83) | 3.75 (3.73 / 4.59; 1.55) | 0.014 (0.013 / 0.027; 0.000) (1) |
| 0.1 | 200 | 10 | 12.95 (12.87 / 16.18; 4.00) | 10.25 (10.18 / 12.71; 3.56) | 4.65 (4.63 / 5.54; 1.76) | 0.010 (0.009 / 0.024; 0.001) (1) |
| 0.15 | 200 | 10 | 19.77 (19.67 / 25.46; 5.98) | 16.61 (16.52 / 21.27; 5.39) | 6.66 (6.63 / 8.20; 2.30) | 0.014 (0.013 / 0.038; 0.001) (1) |
| 0.2 | 200 | 10 | 21.83 (21.58 / 34.96; 7.63) | 18.71 (18.49 / 30.15; 6.90) | 7.28 (7.23 / 10.44; 2.81) | 0.015 (0.014 / 0.045; 0.002) (1) |

## Conditions

- **Two-body model** `data/final_c/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,038 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 162,722 ordered pairs from 266 clusters `obl` (mean 28.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,824 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 2.217 % -> 1.073 %.
- **Configurations**: N in [200] particles, shapes oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

