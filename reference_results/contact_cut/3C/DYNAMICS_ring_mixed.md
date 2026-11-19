# Dynamics: ring of triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_123, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 123 steps, fell 16.8, 111 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 41 | 5.25 | 0.472 | 7.59 |
| + two-body | 69 | 1.93 | 0.323 | 6.66 |
| + many-body | 82 | 0.49 | 0.121 | 3.51 |
| MFS Xfine (the truth's own error) | 123 | 0.006 | 0.0023 | 0.245 |

## Conditions

- **Two-body model** `data/final_c/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 87,082 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid prolateSpheroid__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 190,186 ordered pairs from 260 clusters `mixed` (mean 34.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,648 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.466 % -> 1.463 %.
- **Start**: 5 particles on a vertical ring (x-z plane), long axes along y, neighbours at contact factor 1.25; shapes in order: triaxial_123, prolateSpheroid, oblateSpheroid, triaxial_123, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 600 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

