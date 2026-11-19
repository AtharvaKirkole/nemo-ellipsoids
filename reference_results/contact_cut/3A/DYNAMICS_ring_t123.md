# Dynamics: ring of triaxial_123, triaxial_123, triaxial_123, triaxial_123, triaxial_123 under gravity

MFS (fine) at every RK4 stage, dt 0.1: 356 steps, fell 45.8, 274 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 99 | 6.14 | 1.043 | 18.67 |
| + two-body | 124 | 2.41 | 0.690 | 13.76 |
| + many-body | 160 | 0.38 | 0.232 | 4.73 |
| MFS Xfine (the truth's own error) | 356 | 0.014 | 0.0115 | 0.240 |

## Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: triaxial_123, triaxial_123, triaxial_123, triaxial_123, triaxial_123.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

