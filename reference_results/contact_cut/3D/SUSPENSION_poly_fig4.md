# Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.36 (7.33 / 8.08; 2.70) | 4.72 (4.72 / 4.91; 1.97) | 2.45 (2.42 / 3.08; 0.83) | 0.024 (0.015 / 0.086; 0.003) (1) |
| 0.05 | 100 | 5 | 6.99 (6.95 / 8.30; 2.45) | 4.69 (4.69 / 5.01; 1.96) | 2.64 (2.63 / 3.07; 0.90) | 0.008 (0.007 / 0.024; 0.002) (1) |
| 0.05 | 200 | 5 | 7.22 (7.21 / 7.49; 2.14) | 5.06 (5.08 / 4.60; 1.83) | 3.13 (3.14 / 3.00; 1.16) | not measured |
| 0.05 | 300 | 5 | 7.78 (7.80 / 7.60; 2.13) | 5.54 (5.57 / 4.83; 1.89) | 3.65 (3.68 / 3.19; 1.32) | not measured |
| 0.1 | 50 | 5 | 11.63 (11.55 / 13.02; 4.33) | 8.34 (8.32 / 8.84; 3.27) | 4.21 (4.18 / 4.75; 1.16) | 0.066 (0.048 / 0.200; 0.002) (1) |
| 0.1 | 100 | 5 | 14.07 (14.07 / 14.39; 4.39) | 9.86 (9.88 / 9.59; 3.68) | 5.09 (5.09 / 5.24; 1.49) | 0.015 (0.014 / 0.026; 0.002) (1) |
| 0.1 | 200 | 5 | 13.45 (13.47 / 13.06; 4.01) | 10.47 (10.50 / 9.80; 3.55) | 5.83 (5.83 / 5.74; 1.77) | not measured |
| 0.1 | 300 | 5 | 11.85 (11.81 / 13.74; 4.04) | 9.52 (9.50 / 10.52; 3.68) | 5.48 (5.46 / 6.14; 2.24) | not measured |
| 0.15 | 50 | 5 | 19.59 (19.56 / 20.14; 6.56) | 14.77 (14.79 / 14.73; 5.15) | 5.67 (5.58 / 7.06; 1.47) | 0.070 (0.063 / 0.139; 0.005) (1) |
| 0.15 | 100 | 5 | 18.73 (18.74 / 19.65; 6.00) | 14.96 (14.97 / 15.51; 5.04) | 6.66 (6.61 / 8.20; 1.61) | 0.014 (0.012 / 0.058; 0.002) (1) |
| 0.15 | 200 | 5 | 17.70 (17.67 / 20.88; 6.12) | 14.53 (14.53 / 16.54; 5.48) | 9.24 (9.26 / 10.03; 2.62) | not measured |
| 0.15 | 300 | 5 | 20.37 (20.36 / 20.90; 5.90) | 16.99 (17.01 / 16.69; 5.41) | 11.30 (11.32 / 10.93; 3.05) | not measured |
| 0.2 | 50 | 4 | 19.35 (19.15 / 26.59; 8.04) | 14.89 (14.72 / 20.55; 6.33) | 5.88 (5.74 / 9.61; 1.56) | 0.060 (0.056 / 0.097; 0.008) (1) |
| 0.2 | 100 | 4 | 19.89 (19.72 / 26.40; 8.31) | 16.24 (16.11 / 21.40; 7.12) | 8.48 (8.38 / 12.32; 2.32) | 0.027 (0.021 / 0.144; 0.004) (1) |
| 0.2 | 200 | 4 | 28.72 (28.78 / 28.80; 8.21) | 24.15 (24.25 / 23.33; 7.41) | 27.16 (27.30 / 24.36; 5.13) | not measured |
| 0.2 | 300 | 5 | 27.18 (27.16 / 29.12; 7.80) | 22.92 (22.92 / 23.94; 7.18) | 28.85 (28.94 / 26.56; 4.53) | not measured |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
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
| triaxial_1p5_2 | 1 : 1.5 : 2 | 660 / 560; 0.0009 / 0.0006 | 1400 / 1190; 0.0000 / 0.0000 |
| triaxial_123_x0p75 | 0.75 : 1.5 : 2.25 | 660 / 560; 0.0075 / 0.0052 | 1400 / 1190; 0.0020 / 0.0011 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |

