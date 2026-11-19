# Suspensions of triaxial_123: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.17 (4.13 / 6.00; 1.18) | 2.76 (2.75 / 3.73; 0.99) | 1.82 (1.81 / 2.31; 0.73) | 0.019 (0.017 / 0.066; 0.001) (1) |
| 0.05 | 200 | 10 | 7.10 (7.05 / 10.32; 2.18) | 5.26 (5.24 / 7.10; 1.90) | 3.05 (3.03 / 4.16; 1.18) | 0.026 (0.021 / 0.112; 0.002) (1) |
| 0.075 | 200 | 10 | 11.46 (11.41 / 14.76; 3.20) | 8.84 (8.80 / 11.25; 2.84) | 4.42 (4.40 / 5.57; 1.50) | 0.050 (0.040 / 0.174; 0.003) (1) |
| 0.1 | 200 | 10 | 14.34 (14.26 / 19.33; 4.16) | 11.69 (11.63 / 15.91; 3.71) | 5.57 (5.54 / 7.28; 1.77) | 0.036 (0.033 / 0.130; 0.003) (1) |
| 0.15 | 200 | 10 | 18.49 (18.36 / 29.27; 5.94) | 15.36 (15.24 / 24.85; 5.35) | 6.41 (6.37 / 9.96; 2.15) | 0.051 (0.041 / 0.332; 0.005) (1) |
| 0.2 | 200 | 10 | 26.45 (26.26 / 39.97; 7.71) | 22.99 (22.84 / 34.70; 6.98) | 8.67 (8.61 / 12.83; 2.56) | 0.093 (0.080 / 0.393; 0.006) (1) |

## Conditions

- **Two-body model** `data/final/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 201,350 ordered pairs from 389 clusters `t123` (mean 29.3 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 9,856 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.164 % -> 1.145 %.
- **Configurations**: N in [200] particles, shapes triaxial_123 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

