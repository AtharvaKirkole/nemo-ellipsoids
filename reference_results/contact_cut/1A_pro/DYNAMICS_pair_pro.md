# Dynamics: pair of prolateSpheroid, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 98.5, 239 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.01 | 0.037 | 0.20 |
| + two-body | 1500 | 0.01 | 0.010 | 0.05 |
| + many-body | 1500 | 0.01 | 0.010 | 0.05 |
| MFS Xfine (the truth's own error) | 1500 | 0.003 | 0.0060 | 0.040 |

## Conditions

- **Two-body model** `data/final_c/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,068 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final_c/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,368 ordered pairs from 268 clusters `pro` (mean 32.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_pro.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,904 particles of clusters `pro`; self blocks against MFS on validation: pairwise sum 2.508 % -> 1.235 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolateSpheroid, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

