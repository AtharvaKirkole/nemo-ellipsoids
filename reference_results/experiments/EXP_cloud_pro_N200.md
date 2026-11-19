# A settling cloud of 200 particles (prolateSpheroid)

Start: a sphere of radius 18.2 at volume fraction 0.1.  A drop of the same total force and radius would fall at U0 = 13.21; time is in units of Rc / U0 (dt = 0.020 of it).  Per run and time: distance fallen / Rc; horizontal and vertical root-mean-square extent / the starting value; share of particles left behind (more than 1.5 Rc above the centre); alignment of the axes with gravity (1 = all vertical, 0 = random, -0.5 = all horizontal).

| run | time, Rc/U0 | fallen / Rc | horizontal | vertical | left behind | alignment |
|---|---|---|---|---|---|---|
| far field | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | 0.041 |
| far field | 2.00 | 1.96 | 1.000 | 1.000 | 0.000 | 0.100 |
| far field | 4.00 | 3.91 | 1.015 | 0.956 | 0.000 | 0.238 |
| far field | 8.00 | 7.83 | 1.019 | 0.918 | 0.000 | 0.094 |
| + two-body | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | 0.041 |
| + two-body | 1.86 | 1.82 | 1.000 | 1.000 | 0.000 | 0.090 |
| + two-body | 1.86 | 1.82 | 1.000 | 1.000 | 0.000 | 0.090 |
| + two-body | 1.86 | 1.82 | 1.000 | 1.000 | 0.000 | 0.090 |
| + many-body | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | 0.041 |
| + many-body | 2.00 | 1.92 | 1.002 | 0.992 | 0.000 | 0.095 |
| + many-body | 2.76 | 2.65 | 1.008 | 0.974 | 0.000 | 0.139 |
| + many-body | 2.76 | 2.65 | 1.008 | 0.974 | 0.000 | 0.139 |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Many-body model** `data/final/models/nbody_pro.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 173,740 ordered pairs from 263 clusters `pro` (mean 31.0 neighbours per pair), seed 0.
- **Start**: 200 particles, shapes prolateSpheroid in equal numbers, centres uniform in a sphere at volume fraction 0.1, random orientations, every pair at contact factor >= 1.3 (seed 0).
- **Forces**: gravity (-z, 6 pi) on each; plus a central pair repulsion below contact factor 1.3, 4 x 6 pi x ((c0 - c) / (c0 - 1))^2, the same in every run.  RK4, 400 steps; a run stops if a pair still reaches contact factor 1.02.
- **Truth**: MFS, `fine` clouds, viscosity 1; NOT run: 200 particles is above --truth-max 0.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 |

