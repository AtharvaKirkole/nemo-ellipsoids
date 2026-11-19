# Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.08 (7.08 / 7.39; 2.61) | 4.89 (4.88 / 5.36; 1.95) | 2.11 (2.08 / 2.81; 0.80) | 0.020 (0.020 / 0.029; 0.002) (1) |
| 0.05 | 100 | 5 | 6.83 (6.81 / 7.46; 2.35) | 4.89 (4.88 / 5.27; 1.95) | 2.39 (2.37 / 2.83; 0.86) | 0.032 (0.030 / 0.076; 0.002) (1) |
| 0.05 | 200 | 5 | 7.81 (7.80 / 8.58; 2.24) | 5.84 (5.85 / 5.91; 1.96) | 3.17 (3.17 / 3.44; 1.13) | not measured |
| 0.05 | 300 | 5 | 7.24 (7.22 / 8.24; 2.16) | 5.56 (5.56 / 5.67; 1.95) | 3.38 (3.38 / 3.44; 1.29) | not measured |
| 0.1 | 50 | 5 | 12.61 (12.55 / 14.44; 4.59) | 9.29 (9.21 / 11.61; 3.59) | 3.29 (3.23 / 4.60; 1.18) | 0.036 (0.032 / 0.086; 0.002) (1) |
| 0.1 | 100 | 5 | 11.73 (11.66 / 14.08; 4.09) | 8.87 (8.82 / 10.61; 3.44) | 3.69 (3.65 / 4.97; 1.16) | 0.028 (0.023 / 0.110; 0.004) (1) |
| 0.1 | 200 | 5 | 12.76 (12.72 / 14.53; 4.10) | 10.08 (10.05 / 11.49; 3.67) | 4.42 (4.39 / 5.39; 1.59) | not measured |
| 0.1 | 300 | 5 | 12.68 (12.62 / 15.32; 4.06) | 10.45 (10.41 / 12.16; 3.73) | 5.16 (5.14 / 6.04; 1.99) | not measured |
| 0.15 | 50 | 5 | 16.71 (16.57 / 21.87; 6.07) | 12.97 (12.84 / 17.43; 4.75) | 4.06 (3.92 / 7.15; 1.34) | 0.050 (0.042 / 0.117; 0.006) (1) |
| 0.15 | 100 | 5 | 16.75 (16.59 / 23.13; 6.08) | 13.81 (13.69 / 18.93; 5.20) | 4.30 (4.18 / 7.86; 1.46) | 0.032 (0.028 / 0.116; 0.004) (1) |
| 0.15 | 200 | 5 | 17.56 (17.44 / 22.21; 5.94) | 14.99 (14.90 / 18.74; 5.37) | 5.96 (5.90 / 8.21; 1.90) | not measured |
| 0.15 | 300 | 5 | 20.72 (20.67 / 23.72; 5.89) | 17.29 (17.24 / 19.81; 5.44) | 7.06 (7.04 / 8.18; 2.38) | not measured |
| 0.2 | 50 | 5 | 18.62 (18.35 / 29.33; 7.86) | 14.35 (14.07 / 24.73; 6.26) | 3.83 (3.63 / 9.23; 1.31) | 0.037 (0.030 / 0.165; 0.007) (1) |
| 0.2 | 100 | 5 | 24.91 (24.71 / 32.14; 7.83) | 20.67 (20.51 / 26.74; 6.75) | 6.32 (6.19 / 10.17; 1.67) | 0.048 (0.038 / 0.271; 0.006) (1) |
| 0.2 | 200 | 5 | 28.20 (28.19 / 30.89; 7.61) | 24.39 (24.38 / 26.81; 6.90) | 8.38 (8.32 / 10.74; 2.38) | not measured |
| 0.2 | 300 | 5 | 23.67 (23.54 / 33.15; 7.68) | 20.92 (20.81 / 28.97; 7.11) | 8.62 (8.59 / 11.32; 2.95) | not measured |

## Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

