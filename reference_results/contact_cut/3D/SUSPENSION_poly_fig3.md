# Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.48 (4.47 / 4.81; 1.22) | 2.71 (2.73 / 2.37; 1.02) | 1.80 (1.81 / 1.69; 0.72) | 0.012 (0.010 / 0.032; 0.001) (1) |
| 0.05 | 200 | 10 | 7.35 (7.35 / 7.89; 2.17) | 5.18 (5.20 / 4.79; 1.87) | 3.24 (3.25 / 3.07; 1.17) | 0.015 (0.013 / 0.041; 0.001) (1) |
| 0.075 | 200 | 10 | 9.77 (9.75 / 10.74; 3.30) | 7.38 (7.37 / 7.70; 2.90) | 4.15 (4.14 / 4.62; 1.62) | 0.029 (0.026 / 0.087; 0.002) (1) |
| 0.1 | 200 | 10 | 14.38 (14.45 / 13.27; 4.11) | 11.13 (11.19 / 10.00; 3.64) | 6.10 (6.12 / 5.81; 1.82) | 0.015 (0.013 / 0.046; 0.001) (1) |
| 0.15 | 200 | 10 | 19.62 (19.63 / 21.15; 6.06) | 15.95 (15.97 / 16.87; 5.42) | 9.70 (9.73 / 9.78; 2.58) | 0.053 (0.041 / 0.142; 0.003) (1) |
| 0.2 | 200 | 8 | 26.03 (26.00 / 28.27; 8.07) | 21.74 (21.73 / 23.20; 7.26) | 24.60 (24.69 / 22.75; 4.70) | 0.058 (0.049 / 0.175; 0.007) (1) |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 256, 235,132 parameters, learned inside contact factor 4 (far field beyond).  Trained on 174,164 ordered pairs, 600000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid triaxial_123__triaxial_2_5 prolateSpheroid__triaxial_2_5 prolateSpheroid__oblateSpheroid triaxial_123__triaxial_1p5_2 triaxial_123__triaxial_2_4 triaxial_123__triaxial_3_4 oblateSpheroid__triaxial_1p5_2 prolateSpheroid__triaxial_2_4 triaxial_2_5__triaxial_3_4 triaxial_123_x0p75__triaxial_123 oblateSpheroid_x1p5__oblateSpheroid prolateSpheroid_x1p25__prolateSpheroid triaxial_1p5_2_x1p5__triaxial_1p5_2 triaxial_123_x0p75__prolateSpheroid oblateSpheroid_x1p5__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 105,776 ordered pairs from 239 clusters `poly` (mean 23.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 5,936 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 2.055 % -> 1.336 %.
- **Configurations**: N in [200] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_1p5_2, triaxial_123_x0p75, oblateSpheroid_x1p5 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
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

