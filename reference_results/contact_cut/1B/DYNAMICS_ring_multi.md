# Dynamics: ring of prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 105 steps, fell 19.6, 84 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 42 | 5.42 | 0.629 | 0.00 |
| + two-body | 41 | 1.76 | 0.297 | 0.00 |
| + many-body | 71 | 0.56 | 0.119 | 0.00 |
| MFS Xfine (the truth's own error) | 105 | 0.001 | 0.0006 | 0.002 |

## Conditions

- **Two-body model** `data/final_c/models/pair_multi.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 94,360 ordered pairs, 400000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3.
- **Many-body model** `data/final_c/models/nbody_multi.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 174,894 ordered pairs from 258 clusters `multi` (mean 35.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,408 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.697 % -> 1.131 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2, prolate_ar2.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolate_ar2 | 1 : 1 : 2 | 660 / 560; 0.0000 / 0.0000 | 1400 / 1190; 0.0000 / 0.0000 |

