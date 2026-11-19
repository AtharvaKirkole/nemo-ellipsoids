# Suspensions of prolate_ar2: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 6.51 (6.61 / 5.89; 2.22) | 4.12 (4.17 / 3.82; 1.64) | 1.73 (1.72 / 1.86; 0.66) | 0.001 (0.001 / 0.002; 0.000) (1) |
| 0.05 | 100 | 5 | 6.05 (5.99 / 6.95; 2.36) | 4.22 (4.22 / 4.22; 1.93) | 1.71 (1.70 / 1.99; 0.72) | 0.002 (0.002 / 0.004; 0.000) (1) |
| 0.05 | 200 | 5 | 7.61 (7.77 / 6.51; 2.11) | 5.57 (5.70 / 4.49; 1.84) | 2.68 (2.74 / 2.20; 0.93) | not measured |
| 0.05 | 300 | 5 | 7.35 (7.40 / 6.85; 2.04) | 5.40 (5.48 / 4.35; 1.84) | 2.89 (2.94 / 2.26; 1.10) | not measured |
| 0.1 | 50 | 5 | 12.90 (13.00 / 12.79; 4.38) | 9.33 (9.49 / 8.20; 3.41) | 2.73 (2.66 / 3.42; 1.01) | 0.004 (0.003 / 0.014; 0.001) (1) |
| 0.1 | 100 | 5 | 10.61 (10.46 / 13.08; 4.11) | 8.09 (8.00 / 9.76; 3.43) | 2.82 (2.74 / 3.97; 1.05) | 0.007 (0.006 / 0.017; 0.000) (1) |
| 0.1 | 200 | 5 | 13.16 (13.23 / 12.71; 3.92) | 10.21 (10.28 / 9.54; 3.49) | 3.97 (3.98 / 4.03; 1.29) | not measured |
| 0.1 | 300 | 5 | 14.31 (14.45 / 13.07; 3.89) | 11.66 (11.83 / 9.87; 3.55) | 5.03 (5.12 / 4.16; 1.64) | not measured |
| 0.15 | 50 | 5 | 17.78 (17.72 / 19.05; 5.94) | 13.30 (13.23 / 14.64; 4.67) | 3.68 (3.52 / 5.31; 0.82) | 0.008 (0.008 / 0.011; 0.000) (1) |
| 0.15 | 100 | 5 | 15.82 (15.82 / 18.86; 6.09) | 12.89 (12.92 / 14.95; 5.19) | 4.04 (3.99 / 5.43; 1.47) | 0.003 (0.002 / 0.007; 0.000) (1) |
| 0.15 | 200 | 5 | 16.95 (16.84 / 20.06; 5.84) | 14.04 (13.95 / 16.43; 5.26) | 5.25 (5.23 / 5.95; 2.24) | not measured |
| 0.15 | 300 | 5 | 22.64 (22.94 / 20.31; 5.82) | 19.22 (19.52 / 16.49; 5.36) | 8.20 (8.35 / 6.49; 2.74) | not measured |
| 0.2 | 50 | 5 | 19.68 (19.24 / 28.20; 7.72) | 15.31 (14.93 / 22.63; 6.13) | 3.82 (3.61 / 6.95; 0.92) | 0.015 (0.010 / 0.046; 0.002) (1) |
| 0.2 | 100 | 5 | 24.53 (24.37 / 28.15; 7.75) | 20.56 (20.52 / 22.32; 6.65) | 7.34 (7.28 / 8.49; 2.78) | 0.025 (0.014 / 0.069; 0.002) (1) |
| 0.2 | 200 | 5 | 25.92 (26.12 / 26.64; 7.53) | 22.27 (22.53 / 21.49; 6.81) | 10.04 (10.18 / 9.11; 4.27) | not measured |
| 0.2 | 300 | 5 | 24.11 (24.02 / 28.00; 7.56) | 21.11 (21.13 / 22.89; 6.99) | 10.45 (10.52 / 10.10; 4.66) | not measured |

## Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolate_ar2 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

