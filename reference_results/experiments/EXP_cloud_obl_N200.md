# A settling cloud of 200 particles (oblateSpheroid)

Start: a sphere of radius 20.0 at volume fraction 0.1.  A drop of the same total force and radius would fall at U0 = 12.00; time is in units of Rc / U0 (dt = 0.020 of it).  Per run and time: distance fallen / Rc; horizontal and vertical root-mean-square extent / the starting value; share of particles left behind (more than 1.5 Rc above the centre); alignment of the axes with gravity (1 = all vertical, 0 = random, -0.5 = all horizontal).

| run | time, Rc/U0 | fallen / Rc | horizontal | vertical | left behind | alignment |
|---|---|---|---|---|---|---|
| far field | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | -0.044 |
| far field | 2.00 | 1.96 | 1.012 | 0.966 | 0.000 | -0.054 |
| far field | 4.00 | 3.92 | 1.023 | 0.926 | 0.000 | -0.148 |
| far field | 8.00 | 7.88 | 0.994 | 0.976 | 0.000 | -0.042 |
| + two-body | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | -0.044 |
| + two-body | 2.00 | 1.96 | 1.012 | 0.965 | 0.000 | -0.052 |
| + two-body | 2.32 | 2.27 | 1.014 | 0.958 | 0.000 | -0.063 |
| + two-body | 2.32 | 2.27 | 1.014 | 0.958 | 0.000 | -0.063 |
| + many-body | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | -0.044 |
| + many-body | 2.00 | 1.93 | 1.013 | 0.960 | 0.000 | -0.053 |
| + many-body | 4.00 | 3.86 | 1.029 | 0.908 | 0.000 | -0.139 |
| + many-body | 4.00 | 3.86 | 1.029 | 0.908 | 0.000 | -0.139 |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Start**: 200 particles, shapes oblateSpheroid in equal numbers, centres uniform in a sphere at volume fraction 0.1, random orientations, every pair at contact factor >= 1.3 (seed 0).
- **Forces**: gravity (-z, 6 pi) on each; plus a central pair repulsion below contact factor 1.3, 4 x 6 pi x ((c0 - c) / (c0 - 1))^2, the same in every run.  RK4, 400 steps; a run stops if a pair still reaches contact factor 1.02.
- **Truth**: MFS, `fine` clouds, viscosity 1; NOT run: 200 particles is above --truth-max 0.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 |

