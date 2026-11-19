# Suspensions of prolateSpheroid, oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 6.86 (6.83 / 7.69; 2.63) | 4.82 (4.79 / 5.46; 1.96) | 2.19 (2.16 / 2.84; 0.78) | 0.008 (0.006 / 0.022; 0.000) (1) |
| 0.05 | 100 | 5 | 6.35 (6.31 / 7.81; 2.25) | 4.57 (4.56 / 5.18; 1.81) | 2.39 (2.38 / 2.69; 0.85) | 0.004 (0.003 / 0.020; 0.000) (1) |
| 0.05 | 200 | 5 | 6.78 (6.78 / 7.84; 2.15) | 5.06 (5.07 / 5.37; 1.88) | 3.01 (3.02 / 3.06; 1.16) | not measured |
| 0.05 | 300 | 5 | 7.77 (7.78 / 7.98; 2.13) | 5.68 (5.70 / 5.40; 1.91) | 3.46 (3.49 / 3.12; 1.33) | not measured |
| 0.1 | 50 | 5 | 11.72 (11.62 / 14.31; 4.59) | 8.33 (8.25 / 10.37; 3.57) | 3.15 (3.08 / 4.77; 1.27) | 0.009 (0.007 / 0.031; 0.001) (1) |
| 0.1 | 100 | 5 | 12.69 (12.69 / 13.71; 4.08) | 9.67 (9.67 / 10.63; 3.42) | 3.95 (3.94 / 4.63; 1.23) | 0.016 (0.014 / 0.030; 0.001) (1) |
| 0.1 | 200 | 5 | 13.85 (13.84 / 14.43; 3.98) | 11.32 (11.33 / 11.44; 3.55) | 5.66 (5.67 / 5.30; 1.70) | not measured |
| 0.1 | 300 | 5 | 12.51 (12.48 / 14.54; 3.98) | 10.35 (10.32 / 11.75; 3.63) | 5.40 (5.40 / 5.58; 2.04) | not measured |
| 0.15 | 50 | 5 | 15.33 (15.13 / 21.52; 6.04) | 11.37 (11.21 / 16.42; 4.74) | 3.60 (3.50 / 6.13; 1.50) | 0.024 (0.020 / 0.109; 0.003) (1) |
| 0.15 | 100 | 5 | 18.91 (18.85 / 22.71; 6.22) | 15.51 (15.47 / 18.80; 5.31) | 5.44 (5.41 / 7.07; 1.62) | 0.008 (0.007 / 0.028; 0.002) (1) |
| 0.15 | 200 | 5 | 17.36 (17.23 / 22.05; 5.88) | 14.29 (14.18 / 17.93; 5.30) | 5.77 (5.73 / 7.12; 2.11) | not measured |
| 0.15 | 300 | 5 | 20.71 (20.66 / 23.81; 5.91) | 17.53 (17.51 / 19.56; 5.44) | 8.04 (8.06 / 7.97; 2.68) | not measured |
| 0.2 | 50 | 5 | 23.53 (23.27 / 29.73; 7.77) | 18.28 (18.00 / 24.84; 6.18) | 4.93 (4.75 / 8.21; 1.44) | 0.025 (0.022 / 0.052; 0.002) (1) |
| 0.2 | 100 | 5 | 23.56 (23.33 / 30.62; 7.64) | 19.30 (19.10 / 25.11; 6.54) | 6.12 (6.02 / 8.68; 1.81) | 0.028 (0.025 / 0.052; 0.002) (1) |
| 0.2 | 200 | 5 | 23.01 (22.81 / 32.55; 7.55) | 19.65 (19.46 / 28.12; 6.82) | 7.09 (7.04 / 9.65; 2.47) | not measured |
| 0.2 | 300 | 5 | 22.88 (22.70 / 32.80; 7.71) | 20.07 (19.92 / 28.50; 7.12) | 8.32 (8.29 / 10.55; 3.18) | not measured |

## Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 73,724 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 192,592 ordered pairs from 270 clusters `mixed` (mean 32.7 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,208 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.372 % -> 1.174 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes prolateSpheroid, oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
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

