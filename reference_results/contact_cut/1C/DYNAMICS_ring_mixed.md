# Dynamics: ring of prolateSpheroid, oblateSpheroid, prolateSpheroid, oblateSpheroid, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 173 steps, fell 26.9, 151 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 33 | 6.24 | 0.498 | 12.49 |
| + two-body | 40 | 2.27 | 0.266 | 8.02 |
| + many-body | 80 | 0.54 | 0.144 | 1.50 |
| MFS Xfine (the truth's own error) | 173 | 0.002 | 0.0012 | 0.016 |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside contact factor 4 (far field beyond).  Trained on 72,632 ordered pairs, 400000 steps, seed 0: prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 189,708 ordered pairs from 270 clusters `mixed` (mean 31.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 8,176 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.152 % -> 1.101 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: prolateSpheroid, oblateSpheroid, prolateSpheroid, oblateSpheroid, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

