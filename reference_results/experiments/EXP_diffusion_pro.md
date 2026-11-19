# Short-time self-diffusion in suspensions of prolateSpheroid

D / D0 = (trace of a particle's own translation block) / (the same for the particle alone), averaged over the particles in the middle of the box; and the same for rotation.  Below 1: neighbours slow a particle down.

| phi | particles averaged | MFS: translation / rotation | far field: translation / rotation | + two-body: translation / rotation | + many-body: translation / rotation |
|---|---|---|---|---|---|
| 0.05 | 34 | 0.9145 / 0.9605 | 1.0000 / 1.0000 | 0.9157 / 0.9593 | 0.9157 / 0.9593 |
| 0.1 | 31 | 0.8286 / 0.8984 | 1.0000 / 1.0000 | 0.8141 / 0.8888 | 0.8141 / 0.8888 |
| 0.2 | 26 | 0.7105 / 0.7930 | 1.0000 / 1.0000 | 0.6483 / 0.7497 | 0.6483 / 0.7497 |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Configurations**: N = 64, shapes prolateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per phi.  A finite cloud in unbounded fluid: only particles within a quarter of the box side of the centre are averaged, to stay away from the edge.
- **What it is not**: the hindered settling speed.  That needs a periodic box (zero mean flow); in a finite cloud the settling speed grows with the size of the cloud.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of each configuration (read from the ceiling test's cache when it is there).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 |

