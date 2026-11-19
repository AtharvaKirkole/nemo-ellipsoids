# Three settling particles (oblateSpheroid, oblateSpheroid, oblateSpheroid): how errors grow

MFS ran 1 steps (time 0.1), fell 0.1.  Largest particle position error against MFS at a quarter, half and the end of the run (lengths), and the axis error at the end (degrees).  The first row is MFS itself started 0.001 away: any error below it cannot be told from the system's own sensitivity.

| run | steps | error at T/4 | at T/2 | at T | axis error at T, deg |
|---|---|---|---|---|---|
| MFS started 0.001 away | 1 | 0.0018 | 0.0018 | 0.0014 | 0.07 |
| far field | 1 | 0.0000 | 0.0000 | 0.0076 | 0.46 |
| + two-body | 1 | 0.0000 | 0.0000 | 0.3091 | 4.30 |
| + many-body | 1 | 0.0000 | 0.0000 | 0.3101 | 4.35 |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Start**: three particles on a horizontal triangle of side 1.6 longest semi-axes (each centre moved by a random 5 % of that), random orientations (seed 0), every pair at contact factor above 1.3.
- **Motion**: gravity (-z, 6 pi) on each, no torque; RK4, dt 0.1, up to 1500 steps; stops at contact factor 1.05.
- **Truth**: MFS, `fine` clouds, viscosity 1; one direct solve of the three particles at each RK4 stage.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 |

