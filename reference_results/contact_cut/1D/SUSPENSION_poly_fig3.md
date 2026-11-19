# Suspensions of prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.53 (4.64 / 3.46; 1.17) | 2.69 (2.78 / 1.60; 0.96) | 2.09 (2.17 / 1.26; 0.77) | 0.016 (0.014 / 0.026; 0.001) (1) |
| 0.05 | 200 | 10 | 7.90 (8.10 / 5.83; 2.30) | 5.47 (5.65 / 3.42; 1.96) | 3.88 (4.00 / 2.44; 1.41) | 0.030 (0.028 / 0.046; 0.002) (1) |
| 0.075 | 200 | 10 | 9.69 (9.82 / 7.73; 3.24) | 7.19 (7.31 / 5.12; 2.82) | 4.67 (4.75 / 3.38; 1.85) | 0.064 (0.054 / 0.129; 0.011) (1) |
| 0.1 | 200 | 10 | 14.39 (14.87 / 9.67; 4.30) | 10.82 (11.20 / 6.90; 3.78) | 6.34 (6.55 / 4.16; 2.32) | 0.034 (0.032 / 0.050; 0.003) (1) |
| 0.15 | 200 | 10 | 18.52 (18.90 / 14.62; 6.19) | 14.85 (15.19 / 10.98; 5.50) | 8.09 (8.27 / 6.04; 3.02) | 0.053 (0.041 / 0.196; 0.004) (1) |
| 0.2 | 200 | 8 | 23.17 (23.45 / 19.58; 8.26) | 19.20 (19.50 / 14.99; 7.41) | 9.48 (9.62 / 7.59; 3.76) | not measured |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Configurations**: N in [200] particles, shapes prolateSpheroid, oblateSpheroid, prolate_ar2, oblate_ar3, oblateSpheroid_x1p5, prolateSpheroid_x0p75 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
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

