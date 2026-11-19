# Suspensions of oblateSpheroid: operator against MFS (fine)

PRMSE % of all six velocity components under random unit forces and torques, mean over configurations; in brackets translation / rotation apart, then translation under gravity.

| phi | N | n | far field | + two-body | + many-body | MFS fine vs Xfine (n) |
|---|---|---|---|---|---|---|
| 0.05 | 50 | 5 | 7.94 (7.88 / 9.64; 2.48) | 5.21 (5.16 / 6.27; 1.81) | 2.20 (2.16 / 3.06; 0.77) | 0.006 (0.006 / 0.012; 0.001) (1) |
| 0.05 | 100 | 5 | 6.64 (6.57 / 8.70; 2.39) | 4.67 (4.64 / 5.76; 1.97) | 2.42 (2.40 / 2.92; 0.98) | 0.003 (0.002 / 0.010; 0.000) (1) |
| 0.05 | 200 | 5 | 7.37 (7.34 / 9.05; 2.18) | 5.35 (5.34 / 6.25; 1.90) | 3.12 (3.12 / 3.34; 1.23) | not measured |
| 0.05 | 300 | 5 | 7.30 (7.25 / 8.87; 2.06) | 5.50 (5.49 / 6.02; 1.85) | 3.44 (3.45 / 3.25; 1.33) | not measured |
| 0.1 | 50 | 5 | 12.29 (12.17 / 15.08; 3.94) | 8.74 (8.63 / 11.15; 3.01) | 3.38 (3.34 / 4.29; 1.24) | 0.008 (0.008 / 0.017; 0.000) (1) |
| 0.1 | 100 | 5 | 11.58 (11.50 / 15.40; 4.02) | 8.83 (8.75 / 12.17; 3.37) | 3.63 (3.59 / 5.18; 1.27) | 0.015 (0.014 / 0.029; 0.001) (1) |
| 0.1 | 200 | 5 | 12.55 (12.45 / 16.35; 3.94) | 9.97 (9.90 / 12.56; 3.51) | 4.48 (4.46 / 5.50; 1.76) | not measured |
| 0.1 | 300 | 5 | 12.05 (11.96 / 15.94; 3.94) | 9.97 (9.91 / 12.54; 3.60) | 5.04 (5.02 / 5.82; 2.09) | not measured |
| 0.15 | 50 | 5 | 14.69 (14.46 / 22.95; 5.78) | 11.26 (11.06 / 18.42; 4.51) | 3.51 (3.43 / 6.28; 1.62) | 0.013 (0.011 / 0.041; 0.002) (1) |
| 0.15 | 100 | 5 | 16.39 (16.21 / 23.34; 5.93) | 13.41 (13.27 / 18.99; 5.06) | 4.63 (4.57 / 6.91; 1.63) | 0.020 (0.019 / 0.035; 0.002) (1) |
| 0.15 | 200 | 5 | 17.80 (17.62 / 24.85; 6.06) | 15.01 (14.87 / 20.77; 5.48) | 5.95 (5.91 / 7.74; 2.34) | not measured |
| 0.15 | 300 | 5 | 21.70 (21.65 / 25.25; 5.82) | 18.48 (18.44 / 21.35; 5.36) | 8.32 (8.34 / 7.97; 2.74) | not measured |
| 0.2 | 50 | 5 | 23.94 (23.63 / 32.91; 7.93) | 18.91 (18.64 / 26.48; 6.34) | 5.11 (4.97 / 8.22; 1.43) | 0.008 (0.007 / 0.026; 0.001) (1) |
| 0.2 | 100 | 5 | 21.46 (21.15 / 34.64; 7.68) | 17.56 (17.27 / 29.47; 6.60) | 5.55 (5.44 / 9.72; 1.85) | 0.020 (0.019 / 0.045; 0.002) (1) |
| 0.2 | 200 | 5 | 19.96 (19.72 / 34.72; 7.59) | 17.25 (17.03 / 30.59; 6.87) | 6.47 (6.42 / 10.30; 2.62) | not measured |
| 0.2 | 300 | 5 | 24.77 (24.56 / 37.93; 7.57) | 21.57 (21.39 / 32.63; 7.00) | 9.22 (9.20 / 11.42; 3.34) | not measured |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_obl.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,696 particles of clusters `obl`; self blocks against MFS on validation: pairwise sum 1.847 % -> 0.915 %.
- **Configurations**: N in [50, 100, 200, 300] particles, shapes oblateSpheroid in equal numbers (random order); centres uniform in a cube of volume (total particle volume) / phi, phi in [0.05, 0.1, 0.15, 0.2]; orientations uniform on SO(3); every pair at contact factor >= 1.05 (rejection); no periodic images (a finite cloud in unbounded fluid); 5 independent configurations per (phi, N).
- **Loads**: (1) a random unit force and a random unit torque on every particle; (2) gravity, the same force on every particle.  All x 6 pi.
- **Metric**: PRMSE (%) = 100 x sqrt(sum |v - v_MFS|^2 / sum |v_MFS|^2) over all particles, of all six velocity components, of translation and rotation apart (load 1), and of translation under gravity (load 2).
- **Operators**: far field = 12-Stokeslet pair blocks + isolated self blocks (no learning); + two-body = the pair model inside r_cut; + many-body = the many-body correction on top.
- **MFS column**: the first 1 configurations of each (phi, N <= 100) solved again with the `Xfine` clouds, same loads and metric.
- **Truth**: MFS, `fine` clouds, viscosity 1; iterative solve (GMRES, velocity tolerance 1e-07) of the whole configuration, both load cases at once; cached per configuration.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

