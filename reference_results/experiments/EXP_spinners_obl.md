# 6 oblateSpheroids on a ring, the same vertical torque on each

No force on any particle: all motion of the centres is hydrodynamic coupling.  MFS: 600 steps (time 120); the ring turned 80.80 degrees about its centre and its radius changed by 0.00 %.

| run | steps | ring angle turned, deg | error in it, % | largest position error |
|---|---|---|---|---|
| far field | 600 | 75.98 | 5.96 | 0.4708 |
| + two-body | 600 | 76.83 | 4.91 | 0.3880 |
| + many-body | 600 | 79.71 | 1.34 | 0.1060 |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Start**: 6 particles on a horizontal ring, neighbours 1.4 x (two longest semi-axes) apart, symmetry axes vertical.
- **Loads**: torque 1 x 8 pi about +z on every particle, no force.  RK4, dt 0.2, 600 steps.
- **Truth**: MFS, `fine` clouds, viscosity 1; one solve of the ring at each RK4 stage.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 |

