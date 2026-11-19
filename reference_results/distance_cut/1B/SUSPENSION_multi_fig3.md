# Suspensions of prolate_ar2: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.28 (4.31 / 4.03; 1.13) | 2.67 (2.72 / 2.17; 0.94) | 1.56 (1.59 / 1.26; 0.61) | 0.003 (0.003 / 0.005; 0.000) (1) |
| 0.05 | 200 | 10 | 7.40 (7.51 / 6.56; 2.10) | 5.41 (5.52 / 4.49; 1.81) | 2.61 (2.66 / 2.20; 0.91) | 0.005 (0.004 / 0.008; 0.000) (1) |
| 0.075 | 200 | 10 | 11.14 (11.25 / 10.13; 3.13) | 8.68 (8.82 / 7.10; 2.74) | 3.75 (3.80 / 3.20; 1.14) | 0.005 (0.005 / 0.009; 0.000) (1) |
| 0.1 | 200 | 10 | 13.72 (13.83 / 12.50; 3.94) | 10.81 (10.93 / 9.43; 3.49) | 4.32 (4.36 / 3.98; 1.34) | 0.006 (0.005 / 0.014; 0.000) (1) |
| 0.15 | 200 | 10 | 16.91 (16.78 / 19.81; 5.83) | 14.08 (14.00 / 16.00; 5.21) | 5.30 (5.28 / 6.03; 2.21) | 0.010 (0.007 / 0.027; 0.001) (1) |
| 0.2 | 200 | 10 | 24.52 (24.59 / 27.70; 7.59) | 21.02 (21.14 / 22.80; 6.83) | 9.16 (9.26 / 9.00; 3.89) | 0.015 (0.011 / 0.037; 0.001) (1) |

## Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 95,840 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 165,480 ordered pairs from 254 clusters `multi` (mean 34.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,152 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.718 % -> 1.071 %.
- **Configurations**: N in [200] particles, shapes prolate_ar2 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

