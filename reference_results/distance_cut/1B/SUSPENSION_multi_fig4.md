# Suspensions of prolate_ar2: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 6.51 (6.61 / 5.89; 2.22) | 4.13 (4.17 / 3.82; 1.61) | 1.71 (1.70 / 1.83; 0.66) | 0.001 (0.001 / 0.002; 0.000) (1) |
| 0.05 | 100 | 5 | 6.05 (5.99 / 6.95; 2.36) | 4.21 (4.22 / 4.22; 1.91) | 1.71 (1.69 / 2.01; 0.73) | 0.002 (0.002 / 0.004; 0.000) (1) |
| 0.05 | 200 | 5 | 7.61 (7.77 / 6.51; 2.11) | 5.56 (5.69 / 4.49; 1.82) | 2.67 (2.74 / 2.19; 0.93) | not measured |
| 0.05 | 300 | 5 | 7.35 (7.40 / 6.85; 2.04) | 5.39 (5.47 / 4.35; 1.82) | 2.89 (2.94 / 2.26; 1.10) | not measured |
| 0.1 | 50 | 5 | 12.90 (13.00 / 12.79; 4.38) | 9.34 (9.51 / 8.20; 3.37) | 2.77 (2.69 / 3.49; 0.98) | 0.004 (0.003 / 0.014; 0.001) (1) |
| 0.1 | 100 | 5 | 10.61 (10.46 / 13.08; 4.11) | 8.11 (8.02 / 9.77; 3.40) | 2.81 (2.74 / 3.98; 1.04) | 0.007 (0.006 / 0.017; 0.000) (1) |
| 0.1 | 200 | 5 | 13.16 (13.23 / 12.71; 3.92) | 10.20 (10.28 / 9.54; 3.47) | 3.97 (3.97 / 4.05; 1.32) | not measured |
| 0.1 | 300 | 5 | 14.31 (14.45 / 13.07; 3.89) | 11.66 (11.83 / 9.87; 3.53) | 5.05 (5.13 / 4.16; 1.67) | not measured |
| 0.15 | 50 | 5 | 17.78 (17.72 / 19.05; 5.94) | 13.31 (13.24 / 14.65; 4.64) | 3.65 (3.48 / 5.38; 0.81) | 0.008 (0.008 / 0.011; 0.000) (1) |
| 0.15 | 100 | 5 | 15.82 (15.82 / 18.86; 6.09) | 12.92 (12.96 / 14.95; 5.15) | 4.05 (4.00 / 5.55; 1.43) | 0.003 (0.002 / 0.007; 0.000) (1) |
| 0.15 | 200 | 5 | 16.95 (16.84 / 20.06; 5.84) | 14.03 (13.94 / 16.43; 5.23) | 5.20 (5.17 / 5.90; 2.20) | not measured |
| 0.15 | 300 | 5 | 22.64 (22.94 / 20.31; 5.82) | 19.24 (19.54 / 16.49; 5.33) | 8.16 (8.31 / 6.48; 2.70) | not measured |
| 0.2 | 50 | 5 | 19.68 (19.24 / 28.20; 7.72) | 15.32 (14.94 / 22.62; 6.09) | 3.91 (3.69 / 7.21; 0.98) | 0.015 (0.010 / 0.046; 0.002) (1) |
| 0.2 | 100 | 5 | 24.53 (24.37 / 28.15; 7.75) | 20.61 (20.58 / 22.33; 6.61) | 7.15 (7.09 / 8.39; 2.34) | 0.025 (0.014 / 0.069; 0.002) (1) |
| 0.2 | 200 | 5 | 25.92 (26.12 / 26.64; 7.53) | 22.31 (22.58 / 21.50; 6.77) | 9.71 (9.86 / 8.68; 3.87) | not measured |
| 0.2 | 300 | 5 | 24.11 (24.02 / 28.00; 7.56) | 21.17 (21.19 / 22.89; 6.96) | 10.01 (10.07 / 9.59; 4.27) | not measured |

## Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
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

