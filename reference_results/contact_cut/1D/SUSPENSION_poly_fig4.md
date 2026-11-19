# Suspensions of prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.46 (7.72 / 5.45; 2.78) | 4.57 (4.76 / 2.88; 1.96) | 2.84 (2.94 / 1.99; 1.08) | 0.035 (0.021 / 0.076; 0.003) (1) |
| 0.05 | 100 | 5 | 6.80 (6.95 / 5.13; 2.42) | 4.47 (4.57 / 3.22; 1.89) | 3.08 (3.15 / 2.29; 1.18) | 0.026 (0.023 / 0.051; 0.002) (1) |
| 0.05 | 200 | 5 | 7.84 (8.05 / 5.69; 2.30) | 5.48 (5.66 / 3.36; 1.96) | 3.93 (4.06 / 2.39; 1.43) | not measured |
| 0.05 | 300 | 5 | 7.93 (8.13 / 5.79; 2.21) | 5.65 (5.84 / 3.34; 1.96) | 3.89 (4.01 / 2.35; 1.51) | not measured |
| 0.1 | 50 | 5 | 13.21 (13.48 / 11.12; 4.77) | 8.25 (8.45 / 6.57; 3.57) | 4.27 (4.34 / 3.73; 1.46) | 0.050 (0.044 / 0.082; 0.008) (1) |
| 0.1 | 100 | 5 | 14.22 (14.71 / 9.71; 4.28) | 10.08 (10.46 / 6.47; 3.55) | 5.55 (5.75 / 3.80; 1.74) | 0.032 (0.028 / 0.056; 0.005) (1) |
| 0.1 | 200 | 5 | 13.72 (14.01 / 10.08; 4.23) | 10.46 (10.71 / 7.37; 3.71) | 6.19 (6.33 / 4.45; 2.25) | not measured |
| 0.1 | 300 | 5 | 13.52 (13.78 / 9.94; 4.18) | 10.61 (10.86 / 6.86; 3.78) | 6.96 (7.13 / 4.38; 2.62) | not measured |
| 0.15 | 50 | 5 | 17.66 (17.99 / 14.74; 6.43) | 12.43 (12.72 / 9.81; 4.94) | 5.68 (5.72 / 5.54; 1.72) | 0.034 (0.030 / 0.056; 0.005) (1) |
| 0.15 | 100 | 5 | 19.88 (20.51 / 14.18; 6.47) | 14.91 (15.40 / 10.38; 5.42) | 7.64 (7.88 / 5.53; 2.29) | 0.076 (0.071 / 0.097; 0.007) (1) |
| 0.15 | 200 | 5 | 18.28 (18.72 / 14.53; 6.19) | 14.83 (15.25 / 10.92; 5.50) | 8.29 (8.52 / 6.10; 3.08) | not measured |
| 0.15 | 300 | 5 | 17.80 (18.03 / 14.55; 6.04) | 14.41 (14.64 / 10.84; 5.51) | 8.56 (8.72 / 5.93; 3.50) | not measured |
| 0.2 | 50 | 5 | 22.18 (22.47 / 19.95; 8.77) | 16.62 (16.81 / 15.15; 6.81) | 6.69 (6.65 / 7.54; 1.94) | 0.084 (0.058 / 0.197; 0.007) (1) |
| 0.2 | 100 | 5 | 23.99 (24.47 / 20.43; 8.61) | 19.16 (19.54 / 16.29; 7.30) | 8.27 (8.39 / 7.99; 2.51) | 0.026 (0.021 / 0.099; 0.005) (1) |
| 0.2 | 200 | 3 | 23.65 (23.95 / 20.27; 8.27) | 20.03 (20.39 / 15.49; 7.41) | 10.13 (10.30 / 7.83; 3.75) | not measured |
| 0.2 | 300 | 2 | 21.17 (21.39 / 19.02; 7.95) | 17.94 (18.18 / 14.89; 7.30) | 9.68 (9.82 / 7.70; 4.31) | not measured |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |
| oblate_ar3 | 3 : 3 : 1 | 660 / 560; 0.0227 / 0.0502 | 1400 / 1190; 0.0089 / 0.0186 |
| oblateSpheroid_x1p5 | 3 : 3 : 1.5 | 678 / 593; 0.0005 / 0.0017 | 1328 / 1162; 0.0001 / 0.0001 |
| prolateSpheroid_x0p75 | 0.75 : 0.75 : 2.25 | 654 / 572; 0.0006 / 0.0019 | 1388 / 1214; 0.0001 / 0.0003 |

