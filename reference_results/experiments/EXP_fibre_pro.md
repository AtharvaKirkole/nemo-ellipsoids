# A flexible chain of 5 prolateSpheroids settling broadside

MFS: 1200 steps (time 24), fell 21.1; the middle ended 2.401 below the ends (chain length 34.8).

| run | steps | sag of the middle | error in it, % | largest position error | largest axis error, deg |
|---|---|---|---|---|---|
| far field | 1200 | 2.424 | 0.94 | 0.0646 | 0.06 |
| + two-body | 1200 | 2.402 | 0.02 | 0.0197 | 0.05 |
| + many-body | 1200 | 2.412 | 0.44 | 0.0172 | 0.08 |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Start**: 5 particles in a horizontal line along x, long axes along x, centres 1.2 x (two long semi-axes) apart.
- **Forces**: gravity (-z, 6 pi) on each; a spring of stiffness 10 x 6 pi between facing tips (rest length = the starting gap 1.20); a bending torque 5 x 6 pi x (a_i x a_j) between neighbours.  RK4, dt 0.02, 1200 steps.
- **Truth**: MFS, `fine` clouds, viscosity 1; one solve of the chain at each RK4 stage.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 |

