# Suspensions of prolateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.27 (7.27 / 7.64; 2.40) | 4.90 (4.89 / 5.13; 1.76) | 2.14 (2.11 / 2.71; 0.75) | 0.009 (0.009 / 0.012; 0.001) (1) |
| 0.05 | 100 | 5 | 7.38 (7.38 / 7.58; 2.48) | 5.30 (5.28 / 5.62; 2.03) | 2.65 (2.64 / 3.06; 0.94) | 0.012 (0.011 / 0.019; 0.001) (1) |
| 0.05 | 200 | 5 | 6.81 (6.82 / 7.39; 2.21) | 5.02 (5.05 / 4.92; 1.93) | 2.86 (2.88 / 2.82; 1.17) | not measured |
| 0.05 | 300 | 5 | 7.34 (7.35 / 7.49; 2.19) | 5.55 (5.58 / 5.11; 1.97) | 3.36 (3.39 / 2.94; 1.33) | not measured |
| 0.1 | 50 | 5 | 11.94 (11.96 / 12.24; 4.59) | 8.88 (8.89 / 9.26; 3.58) | 3.30 (3.25 / 4.04; 1.31) | 0.012 (0.012 / 0.020; 0.001) (1) |
| 0.1 | 100 | 5 | 14.77 (14.92 / 13.65; 4.05) | 11.00 (11.12 / 10.31; 3.39) | 4.73 (4.77 / 4.56; 1.16) | 0.010 (0.009 / 0.014; 0.001) (1) |
| 0.1 | 200 | 5 | 12.24 (12.18 / 14.36; 4.10) | 10.01 (9.99 / 11.08; 3.64) | 4.74 (4.73 / 5.31; 1.54) | not measured |
| 0.1 | 300 | 5 | 11.12 (11.02 / 15.05; 4.20) | 9.16 (9.09 / 12.22; 3.85) | 4.37 (4.34 / 5.69; 2.02) | not measured |
| 0.15 | 50 | 5 | 17.91 (17.85 / 19.73; 6.11) | 13.91 (13.84 / 15.38; 4.80) | 4.01 (3.87 / 6.16; 1.45) | 0.015 (0.013 / 0.034; 0.002) (1) |
| 0.15 | 100 | 5 | 15.59 (15.42 / 21.18; 5.99) | 12.72 (12.56 / 17.60; 5.09) | 4.17 (4.09 / 6.49; 1.47) | 0.013 (0.008 / 0.061; 0.001) (1) |
| 0.15 | 200 | 5 | 18.65 (18.59 / 22.30; 6.12) | 15.64 (15.59 / 18.79; 5.52) | 6.03 (6.02 / 7.27; 2.00) | not measured |
| 0.15 | 300 | 5 | 16.92 (16.83 / 21.60; 5.89) | 14.58 (14.51 / 18.43; 5.43) | 6.33 (6.31 / 7.50; 2.44) | not measured |
| 0.2 | 50 | 5 | 24.26 (24.11 / 27.41; 7.96) | 19.53 (19.41 / 22.00; 6.37) | 5.46 (5.33 / 7.30; 1.28) | 0.038 (0.035 / 0.072; 0.003) (1) |
| 0.2 | 100 | 5 | 21.82 (21.59 / 28.88; 7.38) | 18.22 (18.04 / 24.06; 6.31) | 5.39 (5.27 / 8.47; 1.74) | 0.014 (0.012 / 0.051; 0.003) (1) |
| 0.2 | 200 | 5 | 26.35 (26.25 / 31.47; 7.81) | 22.81 (22.70 / 27.34; 7.07) | 7.77 (7.74 / 9.40; 2.32) | not measured |
| 0.2 | 300 | 5 | 29.85 (29.78 / 31.96; 7.57) | 26.18 (26.14 / 27.43; 6.99) | 10.67 (10.71 / 9.80; 2.89) | not measured |

## Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

