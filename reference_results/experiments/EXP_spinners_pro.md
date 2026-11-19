# 6 prolateSpheroids on a ring, the same vertical torque on each

No force on any particle: all motion of the centres is hydrodynamic coupling.  MFS: 600 steps (time 120); the ring turned 20.19 degrees about its centre and its radius changed by -0.00 %.

| run | steps | ring angle turned, deg | error in it, % | largest position error |
|---|---|---|---|---|
| far field | 600 | 20.05 | 0.71 | 0.0210 |
| + two-body | 600 | 20.05 | 0.69 | 0.0204 |
| + many-body | 600 | 20.02 | 0.84 | 0.0249 |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Start**: 6 particles on a horizontal ring, neighbours 1.4 x (two longest semi-axes) apart, symmetry axes vertical.
- **Loads**: torque 1 x 8 pi about +z on every particle, no force.  RK4, dt 0.2, 600 steps.
- **Truth**: MFS, `fine` clouds, viscosity 1; one solve of the ring at each RK4 stage.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 |

