# A settling cloud of 30 particles (oblateSpheroid)

Start: a sphere of radius 10.6 at volume fraction 0.1.  A drop of the same total force and radius would fall at U0 = 3.39; time is in units of Rc / U0 (dt = 0.020 of it).  Per run and time: distance fallen / Rc; horizontal and vertical root-mean-square extent / the starting value; share of particles left behind (more than 1.5 Rc above the centre); alignment of the axes with gravity (1 = all vertical, 0 = random, -0.5 = all horizontal).

| run | time, Rc/U0 | fallen / Rc | horizontal | vertical | left behind | alignment |
|---|---|---|---|---|---|---|
| MFS | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | -0.033 |
| MFS | 1.50 | 1.51 | 1.024 | 0.943 | 0.000 | -0.156 |
| MFS | 3.00 | 3.01 | 1.052 | 0.890 | 0.000 | -0.261 |
| MFS | 6.00 | 5.98 | 1.086 | 0.868 | 0.000 | -0.088 |
| far field | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | -0.033 |
| far field | 1.50 | 1.54 | 1.028 | 0.938 | 0.000 | -0.169 |
| far field | 3.00 | 3.07 | 1.058 | 0.881 | 0.000 | -0.269 |
| far field | 6.00 | 6.08 | 1.084 | 0.865 | 0.000 | -0.031 |
| + two-body | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | -0.033 |
| + two-body | 1.50 | 1.53 | 1.027 | 0.936 | 0.000 | -0.169 |
| + two-body | 3.00 | 3.05 | 1.056 | 0.873 | 0.000 | -0.266 |
| + two-body | 6.00 | 6.04 | 1.080 | 0.850 | 0.000 | -0.018 |
| + many-body | 0.00 | 0.00 | 1.000 | 1.000 | 0.000 | -0.033 |
| + many-body | 1.50 | 1.50 | 1.026 | 0.940 | 0.000 | -0.154 |
| + many-body | 3.00 | 2.99 | 1.056 | 0.877 | 0.000 | -0.262 |
| + many-body | 6.00 | 5.94 | 1.087 | 0.844 | 0.000 | -0.079 |

## Against MFS, particle by particle

| run | steps compared | largest position error / Rc | largest axis error, deg |
|---|---|---|---|
| far field | 300 | 0.2580 | 23.10 |
| + two-body | 300 | 0.2438 | 32.92 |
| + many-body | 300 | 0.0959 | 17.87 |

## Conditions

- **Two-body model** `data/final/models/pair_obl.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: oblateSpheroid__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_obl.pt`: 172 inputs (12 of the pair + 20 per band x 8 bands), 52 true + 67 pseudo tensors, width 128, 62,446 parameters; corrects pairs within 12, sees neighbours within 12 (pair lengths) of the pair midpoint.  Trained on 157,186 ordered pairs from 264 clusters `obl` (mean 27.4 neighbours per pair), seed 0.
- **Start**: 30 particles, shapes oblateSpheroid in equal numbers, centres uniform in a sphere at volume fraction 0.1, random orientations, every pair at contact factor >= 1.3 (seed 0).
- **Forces**: gravity (-z, 6 pi) on each; plus a central pair repulsion below contact factor 1.3, 4 x 6 pi x ((c0 - c) / (c0 - 1))^2, the same in every run.  RK4, 300 steps; a run stops if a pair still reaches contact factor 1.02.
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole cloud at each RK4 stage (iterative solver).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 |

