# Suspensions of triaxial_2_4: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.70 (7.65 / 10.07; 2.54) | 5.01 (4.95 / 7.43; 1.89) | 2.38 (2.33 / 4.25; 0.87) | 0.024 (0.021 / 0.086; 0.003) (1) |
| 0.05 | 100 | 5 | 6.64 (6.59 / 11.40; 2.43) | 4.84 (4.81 / 8.03; 1.99) | 2.85 (2.82 / 5.10; 1.05) | 0.023 (0.020 / 0.142; 0.003) (1) |
| 0.05 | 200 | 5 | 7.03 (7.00 / 10.91; 2.22) | 5.36 (5.33 / 8.03; 1.97) | 3.51 (3.50 / 5.07; 1.36) | not measured |
| 0.05 | 300 | 5 | 8.11 (8.08 / 11.58; 2.27) | 6.41 (6.39 / 8.64; 2.06) | 4.40 (4.39 / 5.51; 1.54) | not measured |
| 0.1 | 50 | 5 | 9.41 (9.29 / 19.10; 4.70) | 7.01 (6.91 / 15.21; 3.65) | 2.93 (2.86 / 7.51; 1.29) | 0.027 (0.024 / 0.143; 0.006) (1) |
| 0.1 | 100 | 5 | 12.62 (12.52 / 19.92; 4.42) | 9.76 (9.67 / 16.23; 3.77) | 4.66 (4.60 / 8.30; 1.68) | 0.021 (0.018 / 0.127; 0.003) (1) |
| 0.1 | 200 | 5 | 14.68 (14.61 / 20.70; 4.29) | 12.00 (11.93 / 17.43; 3.85) | 6.26 (6.22 / 9.12; 2.08) | not measured |
| 0.1 | 300 | 5 | 12.91 (12.84 / 21.12; 4.18) | 10.74 (10.68 / 17.93; 3.84) | 6.38 (6.36 / 9.54; 2.40) | not measured |
| 0.15 | 50 | 5 | 15.97 (15.80 / 29.98; 6.19) | 12.47 (12.32 / 24.53; 4.92) | 4.46 (4.37 / 10.24; 1.57) | 0.055 (0.051 / 0.233; 0.014) (1) |
| 0.15 | 100 | 5 | 21.12 (20.99 / 32.08; 6.33) | 17.17 (17.04 / 27.55; 5.42) | 7.06 (7.00 / 12.08; 1.86) | 0.056 (0.051 / 0.307; 0.006) (1) |
| 0.15 | 200 | 5 | 20.67 (20.54 / 31.47; 5.92) | 17.47 (17.35 / 27.18; 5.35) | 8.62 (8.57 / 12.44; 2.55) | not measured |
| 0.15 | 300 | 5 | 20.00 (19.89 / 32.46; 6.20) | 17.27 (17.17 / 28.58; 5.74) | 9.13 (9.09 / 13.44; 3.15) | not measured |
| 0.2 | 50 | 5 | 22.32 (22.02 / 39.78; 7.74) | 17.89 (17.62 / 33.78; 6.21) | 5.84 (5.70 / 13.19; 1.83) | 0.102 (0.091 / 0.373; 0.013) (1) |
| 0.2 | 100 | 5 | 22.81 (22.57 / 41.98; 7.72) | 19.12 (18.93 / 35.42; 6.65) | 7.48 (7.41 / 14.01; 2.23) | 0.077 (0.064 / 0.373; 0.007) (1) |
| 0.2 | 200 | 5 | 22.68 (22.50 / 43.29; 7.79) | 19.46 (19.28 / 38.87; 7.08) | 8.74 (8.68 / 16.56; 3.10) | not measured |
| 0.2 | 300 | 5 | 25.40 (25.26 / 44.42; 7.88) | 22.65 (22.52 / 39.99; 7.31) | 11.23 (11.19 / 17.76; 3.76) | not measured |

## Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_2_4 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

