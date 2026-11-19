# Two settling prolateSpheroids: bound orbit or not

Operator: + two-body.  Rows = starting centre separation (in longest semi-axes: [1.5, 2.0, 2.5, 3.0, 4.0, 5.0]); columns = tilt of the symmetry axes from the vertical, +theta and -theta (degrees).  Entry: outcome, turning points of the horizontal separation, largest separation / starting separation.

| separation | tilt 0 | tilt 15 | tilt 30 | tilt 45 | tilt 60 | tilt 75 | tilt 90 |
|---|---|---|---|---|---|---|---|
| 4.50 | SCATTER, 0, 8.38 | SCATTER, 2, 4.82 | BOUND, 6, 2.25 | TOO CLOSE, 0, 0.00 | TOO CLOSE, 0, 0.00 | TOO CLOSE, 0, 0.00 | TOO CLOSE, 0, 0.00 |
| 6.00 | SCATTER, 0, 12.43 | SCATTER, 0, 11.46 | UNDECIDED, 1, 4.77 | BOUND, 6, 1.86 | BOUND, 11, 1.23 | TOO CLOSE, 0, 0.00 | TOO CLOSE, 0, 0.00 |
| 7.50 | SCATTER, 0, 10.89 | SCATTER, 0, 10.94 | SCATTER, 0, 8.78 | SCATTER, 2, 2.67 | BOUND, 6, 1.39 | BOUND, 10, 1.07 | BOUND, 10, 1.00 |
| 9.00 | SCATTER, 0, 9.13 | SCATTER, 0, 9.56 | SCATTER, 0, 8.83 | SCATTER, 0, 4.42 | BOUND, 4, 1.56 | BOUND, 7, 1.10 | BOUND, 7, 1.00 |
| 12.00 | SCATTER, 0, 6.51 | SCATTER, 0, 7.25 | SCATTER, 0, 7.48 | SCATTER, 0, 5.97 | UNDECIDED, 2, 2.04 | BOUND, 4, 1.15 | BOUND, 5, 1.00 |
| 15.00 | SCATTER, 0, 4.86 | SCATTER, 0, 5.72 | SCATTER, 0, 6.27 | SCATTER, 0, 5.59 | SCATTER, 0, 2.86 | BOUND, 3, 1.20 | BOUND, 3, 1.00 |

## The same runs with MFS at every step

| separation | tilt | operator: outcome, turning points | MFS: outcome, turning points | steps compared | position error at the end | axis error, deg | separation error, % of the separation |
|---|---|---|---|---|---|---|---|
| 9.00 | 30 | SCATTER, 0 | SCATTER, 0 | 2400 | 0.082 | 0.18 | 0.02 |
| 9.00 | 60 | BOUND, 4 | BOUND, 4 | 2400 | 0.025 | 0.21 | 0.09 |
| 12.00 | 60 | UNDECIDED, 2 | UNDECIDED, 2 | 2400 | 0.069 | 0.75 | 0.41 |
| 4.50 | 0 | SCATTER, 0 | SCATTER, 0 | 2400 | 0.076 | 0.15 | 0.22 |

## Conditions

- **Two-body model** `data/final/models/pair_pro.pt`: spheroid form, 12 inputs, 12 true + 27 pseudo tensors (78 coefficients per block, two blocks), width 128, 54,812 parameters, learned inside r_cut = 12 pair lengths (far field beyond).  Trained on 29,490 ordered pairs, 200000 steps, seed 0: prolateSpheroid__prolateSpheroid.
- **Start**: two prolateSpheroids at the same height, centres [1.5, 2.0, 2.5, 3.0, 4.0, 5.0] longest semi-axes apart along x, symmetry axes in the x-z plane at +theta and -theta from the vertical, theta in [0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0] degrees.
- **Motion**: the same force (gravity, -z, 6 pi) on both, no torque; RK4, dt 0.25, 2400 steps (time 600); a run stops at contact factor 1.05.
- **Outcome**: from the horizontal separation s(t).  BOUND: at least 3 turning points and s never above 3 s(0) + 1.  SCATTER: s ends above 2 s(0) and is still growing.  CONTACT: the run stopped.  UNDECIDED: none of these within the time.
- **Truth**: MFS, `fine` clouds, viscosity 1; one direct solve of the two particles at each RK4 stage.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 |

