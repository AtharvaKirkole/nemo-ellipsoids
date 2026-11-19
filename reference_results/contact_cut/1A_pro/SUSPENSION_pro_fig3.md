# Suspensions of prolateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.32 (4.33 / 4.28; 1.19) | 2.84 (2.87 / 2.41; 1.00) | 1.86 (1.88 / 1.56; 0.72) | 0.004 (0.004 / 0.011; 0.000) (1) |
| 0.05 | 200 | 10 | 7.00 (7.01 / 7.29; 2.19) | 5.12 (5.15 / 5.02; 1.91) | 2.84 (2.85 / 2.87; 1.14) | 0.009 (0.006 / 0.029; 0.000) (1) |
| 0.075 | 200 | 10 | 11.45 (11.48 / 11.70; 3.32) | 8.94 (8.97 / 8.89; 2.94) | 4.37 (4.38 / 4.34; 1.44) | 0.021 (0.017 / 0.048; 0.001) (1) |
| 0.1 | 200 | 10 | 13.85 (13.86 / 14.37; 4.09) | 10.99 (11.00 / 11.24; 3.64) | 5.15 (5.15 / 5.32; 1.59) | 0.009 (0.007 / 0.038; 0.001) (1) |
| 0.15 | 200 | 10 | 18.56 (18.49 / 22.71; 6.05) | 15.64 (15.59 / 19.11; 5.45) | 5.94 (5.91 / 7.47; 1.95) | 0.008 (0.006 / 0.034; 0.001) (1) |
| 0.2 | 200 | 10 | 27.33 (27.30 / 30.80; 7.74) | 23.44 (23.40 / 26.55; 7.01) | 8.25 (8.24 / 9.32; 2.33) | 0.014 (0.011 / 0.075; 0.003) (1) |

## Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configurations**: N in [200] particles, shapes prolateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

