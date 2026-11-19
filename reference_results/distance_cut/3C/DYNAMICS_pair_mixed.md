# Dynamics: pair of triaxial_123, prolateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 89.7, 247 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.09 | 0.094 | 0.31 |
| + two-body | 1500 | 0.02 | 0.017 | 0.17 |
| + many-body | 1500 | 0.02 | 0.017 | 0.17 |
| MFS Xfine (the truth's own error) | 1500 | 0.005 | 0.0104 | 0.283 |

## Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: triaxial_123, prolateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |

