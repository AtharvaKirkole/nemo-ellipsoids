# Dynamics: pair of prolateSpheroid, oblateSpheroid under gravity

MFS (fine) at every RK4 stage, dt 0.1: 1500 steps, fell 110.9, 252 s.

| run | steps | COM error, % of fallen | position error (max) | axis error, deg (max) |
|---|---|---|---|---|
| far field | 1500 | 0.48 | 0.564 | 2.61 |
| + two-body | 1500 | 0.02 | 0.023 | 0.10 |
| + many-body | 1500 | 0.02 | 0.023 | 0.10 |
| MFS Xfine (the truth's own error) | 1500 | 0.002 | 0.0031 | 0.027 |

## Conditions

- **Two-body model** `data/final_c/models/pair_poly.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 256, 175,004 parameters, learned inside contact factor 4 (far field beyond).  Trained on 159,696 ordered pairs, 600000 steps, seed 0: prolate_ar1p5__prolate_ar1p5 prolate_ar2__prolate_ar2 prolateSpheroid__prolateSpheroid prolate_ar4__prolate_ar4 oblate_ar1p5__oblate_ar1p5 oblateSpheroid__oblateSpheroid oblate_ar3__oblate_ar3 prolateSpheroid__oblateSpheroid prolate_ar2__oblateSpheroid prolate_ar4__oblate_ar3 prolate_ar2__oblate_ar1p5 prolate_ar1p5__oblate_ar3 prolateSpheroid__prolate_ar2 oblateSpheroid__oblate_ar3 prolate_ar4__oblateSpheroid prolateSpheroid__oblate_ar1p5 prolateSpheroid_x0p75__prolateSpheroid oblateSpheroid_x1p5__oblateSpheroid prolate_ar2_x1p5__prolate_ar2 oblate_ar3_x0p75__oblate_ar3 oblateSpheroid_x1p5__prolateSpheroid_x0p75 prolate_ar2_x1p5__oblateSpheroid.
- **Many-body model** `data/final_c/models/nbody_poly.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 148,262 ordered pairs from 260 clusters `poly` (mean 28.1 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_poly.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 12 particle lengths.  Trained on 7,536 particles of clusters `poly`; self blocks against MFS on validation: pairwise sum 1.987 % -> 1.400 %.
- **Start**: two particles side by side along x at contact factor 1.5, long axes tilted +-45 degrees in the x-z plane; shapes in order: prolateSpheroid, oblateSpheroid.
- **Motion**: the same force (gravity, -z, 6 pi) on every particle, no torque; rigid-body RK4, dt 0.1, up to 1500 steps; a run stops when any pair reaches contact factor 1.05.
- **Metric**: each run against the MFS run at the last step both reached: centre-of-mass error as % of the distance fallen, largest particle position error (lengths), largest axis error (degrees, axes as lines).  `steps` = how long the run went before a near-contact stopped it (the MFS run: see the first line).
- **Truth**: MFS, `fine` clouds, viscosity 1; solved at each of the 4 RK4 stages of every step (direct solve for small systems, else GMRES to 1e-07 with a warm start).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

