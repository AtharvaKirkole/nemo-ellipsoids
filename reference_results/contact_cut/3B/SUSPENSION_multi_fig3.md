# Suspensions of triaxial_2_4: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.26 (4.23 / 6.75; 1.23) | 2.82 (2.80 / 3.94; 1.05) | 2.02 (2.01 / 2.87; 0.81) | 0.030 (0.027 / 0.110; 0.002) (1) |
| 0.05 | 200 | 10 | 7.39 (7.35 / 11.21; 2.21) | 5.58 (5.56 / 8.22; 1.93) | 3.51 (3.49 / 5.13; 1.31) | 0.022 (0.017 / 0.154; 0.002) (1) |
| 0.075 | 200 | 10 | 10.27 (10.21 / 16.24; 3.37) | 8.10 (8.05 / 12.82; 3.00) | 4.74 (4.71 / 7.35; 1.79) | 0.042 (0.038 / 0.169; 0.003) (1) |
| 0.1 | 200 | 10 | 15.01 (14.94 / 20.82; 4.30) | 12.22 (12.16 / 17.44; 3.85) | 6.38 (6.35 / 8.92; 2.10) | 0.063 (0.058 / 0.283; 0.004) (1) |
| 0.15 | 200 | 10 | 20.54 (20.40 / 31.24; 6.03) | 17.13 (17.01 / 26.99; 5.43) | 8.20 (8.15 / 12.15; 2.58) | 0.068 (0.062 / 0.283; 0.005) (1) |
| 0.2 | 200 | 10 | 23.62 (23.47 / 43.11; 7.82) | 20.44 (20.30 / 38.43; 7.07) | 9.24 (9.18 / 16.63; 3.13) | 0.101 (0.091 / 0.426; 0.008) (1) |

## Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 65,236 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 101,930 ordered pairs from 238 clusters `multi` (mean 23.0 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,032 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.706 % -> 0.961 %.
- **Configurations**: N in [200] particles, shapes triaxial_2_4 in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 200) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

