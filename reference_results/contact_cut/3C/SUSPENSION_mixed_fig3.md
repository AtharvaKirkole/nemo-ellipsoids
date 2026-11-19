# Suspensions of triaxial_123, prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.36 (4.35 / 4.92; 1.17) | 2.79 (2.80 / 2.66; 0.98) | 1.79 (1.79 / 1.70; 0.69) | 0.022 (0.019 / 0.056; 0.001) (1) |
| 0.05 | 200 | 10 | 7.47 (7.45 / 8.25; 2.23) | 5.53 (5.54 / 5.52; 1.94) | 3.08 (3.08 / 3.22; 1.15) | 0.013 (0.012 / 0.040; 0.001) (1) |
| 0.075 | 200 | 10 | 10.20 (10.18 / 11.62; 3.16) | 7.96 (7.95 / 8.66; 2.79) | 3.84 (3.83 / 4.52; 1.42) | 0.036 (0.033 / 0.065; 0.001) (1) |
| 0.1 | 200 | 10 | 13.82 (13.80 / 14.89; 4.19) | 11.01 (11.00 / 11.67; 3.73) | 4.80 (4.78 / 5.45; 1.57) | 0.034 (0.030 / 0.120; 0.002) (1) |
| 0.15 | 200 | 10 | 16.28 (16.15 / 22.42; 5.98) | 13.74 (13.63 / 18.69; 5.37) | 5.40 (5.34 / 7.90; 1.86) | 0.049 (0.041 / 0.156; 0.004) (1) |
| 0.2 | 200 | 10 | 25.10 (24.99 / 31.54; 7.59) | 21.52 (21.43 / 27.01; 6.84) | 7.58 (7.52 / 10.28; 2.30) | 0.060 (0.048 / 0.251; 0.006) (1) |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Configurations**: N in [200] particles, shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
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

