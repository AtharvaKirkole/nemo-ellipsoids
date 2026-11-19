# Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.08 (7.08 / 7.39; 2.61) | 4.84 (4.83 / 5.20; 1.92) | 2.10 (2.07 / 2.78; 0.80) | 0.020 (0.020 / 0.029; 0.002) (1) |
| 0.05 | 100 | 5 | 6.83 (6.81 / 7.46; 2.35) | 4.85 (4.84 / 5.13; 1.93) | 2.39 (2.38 / 2.75; 0.87) | 0.032 (0.030 / 0.076; 0.002) (1) |
| 0.05 | 200 | 5 | 7.81 (7.80 / 8.58; 2.24) | 5.80 (5.81 / 5.74; 1.95) | 3.15 (3.14 / 3.38; 1.13) | not measured |
| 0.05 | 300 | 5 | 7.24 (7.22 / 8.24; 2.16) | 5.53 (5.53 / 5.53; 1.94) | 3.38 (3.39 / 3.40; 1.30) | not measured |
| 0.1 | 50 | 5 | 12.61 (12.55 / 14.44; 4.59) | 9.20 (9.13 / 11.30; 3.55) | 3.29 (3.23 / 4.53; 1.19) | 0.036 (0.032 / 0.086; 0.002) (1) |
| 0.1 | 100 | 5 | 11.73 (11.66 / 14.08; 4.09) | 8.83 (8.78 / 10.45; 3.41) | 3.68 (3.64 / 4.85; 1.15) | 0.028 (0.023 / 0.110; 0.004) (1) |
| 0.1 | 200 | 5 | 12.76 (12.72 / 14.53; 4.10) | 10.01 (9.98 / 11.35; 3.65) | 4.39 (4.36 / 5.33; 1.58) | not measured |
| 0.1 | 300 | 5 | 12.68 (12.62 / 15.32; 4.06) | 10.39 (10.36 / 12.02; 3.71) | 5.11 (5.10 / 5.92; 1.98) | not measured |
| 0.15 | 50 | 5 | 16.71 (16.57 / 21.87; 6.07) | 12.94 (12.82 / 17.23; 4.71) | 4.07 (3.94 / 7.04; 1.31) | 0.050 (0.042 / 0.117; 0.006) (1) |
| 0.15 | 100 | 5 | 16.75 (16.59 / 23.13; 6.08) | 13.71 (13.60 / 18.61; 5.15) | 4.36 (4.26 / 7.68; 1.43) | 0.032 (0.028 / 0.116; 0.004) (1) |
| 0.15 | 200 | 5 | 17.56 (17.44 / 22.21; 5.94) | 14.90 (14.81 / 18.63; 5.34) | 5.91 (5.86 / 7.98; 1.84) | not measured |
| 0.15 | 300 | 5 | 20.72 (20.67 / 23.72; 5.89) | 17.21 (17.17 / 19.62; 5.42) | 7.06 (7.04 / 8.05; 2.31) | not measured |
| 0.2 | 50 | 5 | 18.62 (18.35 / 29.33; 7.86) | 14.30 (14.03 / 24.44; 6.21) | 3.87 (3.68 / 9.15; 1.27) | 0.037 (0.030 / 0.165; 0.007) (1) |
| 0.2 | 100 | 5 | 24.91 (24.71 / 32.14; 7.83) | 20.60 (20.44 / 26.58; 6.70) | 6.34 (6.23 / 9.80; 1.59) | 0.048 (0.038 / 0.271; 0.006) (1) |
| 0.2 | 200 | 5 | 28.20 (28.19 / 30.89; 7.61) | 24.28 (24.27 / 26.53; 6.87) | 8.48 (8.43 / 10.39; 2.34) | not measured |
| 0.2 | 300 | 5 | 23.67 (23.54 / 33.15; 7.68) | 20.84 (20.74 / 28.80; 7.09) | 8.59 (8.57 / 11.11; 2.83) | not measured |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
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

