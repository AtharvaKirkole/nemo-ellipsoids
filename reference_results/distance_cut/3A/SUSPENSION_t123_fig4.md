# Suspensions of triaxial_123: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.28 (7.23 / 9.70; 2.35) | 4.64 (4.60 / 6.29; 1.75) | 2.18 (2.15 / 3.29; 0.77) | 0.027 (0.025 / 0.064; 0.002) (1) |
| 0.05 | 100 | 5 | 6.54 (6.48 / 9.85; 2.38) | 4.52 (4.48 / 6.80; 1.94) | 2.35 (2.32 / 3.58; 0.95) | 0.026 (0.024 / 0.112; 0.002) (1) |
| 0.05 | 200 | 5 | 6.73 (6.68 / 10.08; 2.18) | 5.05 (5.02 / 7.01; 1.91) | 2.91 (2.89 / 4.15; 1.19) | not measured |
| 0.05 | 300 | 5 | 7.09 (7.04 / 10.06; 2.17) | 5.43 (5.41 / 7.33; 1.96) | 3.29 (3.28 / 4.36; 1.37) | not measured |
| 0.1 | 50 | 5 | 12.27 (12.15 / 18.29; 4.42) | 8.91 (8.81 / 13.97; 3.41) | 2.94 (2.87 / 5.98; 1.35) | 0.031 (0.027 / 0.134; 0.004) (1) |
| 0.1 | 100 | 5 | 13.12 (13.02 / 18.29; 4.22) | 10.24 (10.15 / 14.68; 3.55) | 4.30 (4.25 / 6.97; 1.31) | 0.050 (0.040 / 0.238; 0.003) (1) |
| 0.1 | 200 | 5 | 12.81 (12.73 / 18.45; 4.06) | 10.49 (10.42 / 15.20; 3.62) | 5.08 (5.05 / 7.06; 1.74) | not measured |
| 0.1 | 300 | 5 | 11.26 (11.17 / 19.21; 4.01) | 9.38 (9.31 / 15.81; 3.67) | 4.82 (4.79 / 7.80; 2.10) | not measured |
| 0.15 | 50 | 5 | 15.15 (14.91 / 27.20; 5.82) | 11.96 (11.76 / 21.85; 4.57) | 3.86 (3.74 / 8.62; 1.59) | 0.047 (0.039 / 0.204; 0.005) (1) |
| 0.15 | 100 | 5 | 18.74 (18.57 / 28.19; 6.23) | 15.03 (14.87 / 23.67; 5.32) | 4.93 (4.85 / 8.98; 1.57) | 0.065 (0.058 / 0.232; 0.006) (1) |
| 0.15 | 200 | 5 | 19.15 (19.02 / 29.64; 5.98) | 15.78 (15.66 / 24.97; 5.38) | 6.64 (6.59 / 10.22; 2.18) | not measured |
| 0.15 | 300 | 5 | 17.04 (16.90 / 29.29; 5.94) | 14.61 (14.49 / 25.15; 5.47) | 6.64 (6.60 / 10.47; 2.72) | not measured |
| 0.2 | 50 | 5 | 23.43 (23.13 / 39.41; 7.91) | 18.70 (18.42 / 32.91; 6.32) | 4.95 (4.79 / 11.39; 1.42) | 0.040 (0.031 / 0.363; 0.012) (1) |
| 0.2 | 100 | 5 | 25.51 (25.28 / 37.89; 7.69) | 21.25 (21.02 / 33.12; 6.60) | 6.96 (6.86 / 11.74; 1.85) | 0.070 (0.064 / 0.191; 0.004) (1) |
| 0.2 | 200 | 5 | 29.95 (29.80 / 40.55; 7.67) | 25.88 (25.74 / 35.52; 6.94) | 9.53 (9.48 / 12.90; 2.54) | not measured |
| 0.2 | 300 | 5 | 24.75 (24.55 / 40.40; 7.70) | 21.81 (21.63 / 35.55; 7.13) | 9.45 (9.40 / 13.57; 3.35) | not measured |

## Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes triaxial_123 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

