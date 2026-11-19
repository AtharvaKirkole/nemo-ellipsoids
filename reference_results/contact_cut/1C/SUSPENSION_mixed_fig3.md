# Suspensions of prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.025 | 200 | 10 | 4.15 (4.13 / 4.73; 1.18) | 2.70 (2.70 / 2.59; 0.99) | 1.75 (1.76 / 1.66; 0.73) | 0.004 (0.003 / 0.012; 0.000) (1) |
| 0.05 | 200 | 10 | 7.04 (7.02 / 8.05; 2.15) | 5.18 (5.19 / 5.41; 1.88) | 3.03 (3.04 / 3.05; 1.16) | 0.008 (0.007 / 0.020; 0.000) (1) |
| 0.075 | 200 | 10 | 10.32 (10.30 / 11.29; 3.18) | 8.05 (8.04 / 8.77; 2.82) | 4.09 (4.09 / 4.29; 1.53) | 0.026 (0.025 / 0.042; 0.001) (1) |
| 0.1 | 200 | 10 | 13.71 (13.68 / 14.59; 4.06) | 11.06 (11.05 / 11.38; 3.62) | 5.42 (5.43 / 5.32; 1.72) | 0.011 (0.010 / 0.029; 0.001) (1) |
| 0.15 | 200 | 10 | 19.40 (19.34 / 21.97; 5.87) | 16.06 (16.01 / 18.06; 5.28) | 6.47 (6.46 / 7.17; 2.12) | 0.018 (0.016 / 0.044; 0.002) (1) |
| 0.2 | 200 | 10 | 23.59 (23.38 / 31.98; 7.63) | 20.14 (19.94 / 27.81; 6.90) | 7.40 (7.35 / 9.63; 2.55) | 0.009 (0.006 / 0.089; 0.002) (1) |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Configurations**: N in [200] particles, shapes prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.025, 0.05, 0.075, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 10 independent configurations per (phi, N).
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

