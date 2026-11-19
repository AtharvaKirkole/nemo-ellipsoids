# Suspensions of prolateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.32 (4.33 / 4.28; 1.19) | 2.83 (2.86 / 2.41; 1.00) | 1.87 (1.89 / 1.55; 0.73) | 0.004 (0.004 / 0.011; 0.000) (1) |
| 0.05 | 200 | 10 | 7.00 (7.01 / 7.29; 2.19) | 5.12 (5.14 / 5.02; 1.91) | 2.86 (2.87 / 2.85; 1.17) | 0.009 (0.006 / 0.029; 0.000) (1) |
| 0.075 | 200 | 10 | 11.45 (11.48 / 11.70; 3.32) | 8.94 (8.96 / 8.89; 2.93) | 4.40 (4.42 / 4.31; 1.50) | 0.021 (0.017 / 0.048; 0.001) (1) |
| 0.1 | 200 | 10 | 13.85 (13.86 / 14.37; 4.09) | 10.98 (11.00 / 11.24; 3.63) | 5.16 (5.17 / 5.24; 1.65) | 0.009 (0.007 / 0.038; 0.001) (1) |
| 0.15 | 200 | 10 | 18.56 (18.49 / 22.71; 6.05) | 15.65 (15.59 / 19.11; 5.44) | 5.98 (5.95 / 7.46; 2.07) | 0.008 (0.006 / 0.034; 0.001) (1) |
| 0.2 | 200 | 10 | 27.33 (27.30 / 30.80; 7.74) | 23.44 (23.40 / 26.55; 7.00) | 8.47 (8.47 / 9.32; 2.56) | 0.014 (0.011 / 0.075; 0.003) (1) |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,552 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.095 % -> 1.015 %.
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

