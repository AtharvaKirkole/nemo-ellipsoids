# Three settling particles (prolateSpheroid, prolateSpheroid, prolateSpheroid): how errors grow

MFS ran 1500 steps (time 150), fell 139.7.  Largest particle position error against MFS at a quarter, half and the end of the run (lengths), and the axis error at the end (degrees).  The first row is MFS itself started 0.001 away: any error below it cannot be told from the system's own sensitivity.

| run | steps | error at T/4 | at T/2 | at T | axis error at T, deg |
|---|---|---|---|---|---|
| MFS started 0.001 away | 1500 | 0.0032 | 0.0102 | 0.0193 | 0.17 |
| far field | 1500 | 0.5198 | 1.6179 | 2.7439 | 22.18 |
| + two-body | 1500 | 0.1671 | 1.3227 | 2.9941 | 12.09 |
| + many-body | 1500 | 0.0863 | 0.6364 | 1.4114 | 7.38 |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Start**: three particles on a horizontal triangle of side 1.6 longest semi-axes (each centre moved by a random 5 % of that), random orientations (seed 0), every pair at contact factor above 1.3.
- **Motion**: gravity (-z, 6 pi) on each, no torque; RK4, dt 0.1, up to 1500 steps; stops at contact factor 1.05.
- **Truth**: MFS, `fine` clouds, viscosity 1; one direct solve of the three particles at each RK4 stage.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 |

