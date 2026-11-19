# Short-time self-diffusion in suspensions of oblateSpheroid

D / D0 = (trace of a particle's own translation block) / (the same for the particle alone), averaged over the particles in the middle of the box; and the same for rotation.  Below 1: neighbours slow a particle down.

| phi | particles averaged | MFS: translation / rotation | far field: translation / rotation | + two-body: translation / rotation | + many-body: translation / rotation |
|---|---|---|---|---|---|
| 0.05 | 32 | 0.9193 / 0.9628 | 1.0000 / 1.0000 | 0.9236 / 0.9617 | 0.9236 / 0.9617 |
| 0.1 | 37 | 0.8295 / 0.8993 | 1.0000 / 1.0000 | 0.8206 / 0.8920 | 0.8206 / 0.8920 |
| 0.2 | 31 | 0.7035 / 0.7761 | 1.0000 / 1.0000 | 0.6520 / 0.7370 | 0.6520 / 0.7370 |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Configurations**: N = 64, shapes oblateSpheroid in equal numbers, uniform in a cube at phi in [0.05, 0.1, 0.2], random orientations, contact factor >= 1.05; 3 per phi.  A finite cloud in unbounded fluid: only particles within a quarter of the box side of the centre are averaged, to stay away from the edge.
- **What it is not**: the hindered settling speed.  That needs a periodic box (zero mean flow); in a finite cloud the settling speed grows with the size of the cloud.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of each configuration (read from the ceiling test's cache when it is there).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 |

