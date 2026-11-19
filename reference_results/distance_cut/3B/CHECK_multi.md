# Structural checks, 16 particles of triaxial_2_4 at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.3e-16 | 1.2682 | 5.3e-16 | 7.95 |
| + two-body | 8.7e-17 | 0.3586 | 4.4e-16 | 5.08 |
| + many-body | 8.9e-17 | 0.9310 | 4.6e-16 | 1.93 |
| MFS fine (the truth) | 2.6e-04 | 1 | | 0 |
| MFS Xfine | 6.1e-05 | 0.9981 | | 0.021 (= the error of the fine truth) |

MFS smallest eigenvalue 1.1028e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

## Conditions

- **Two-body model** `data/final/models/pair_multi.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 66,350 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 triaxial_1p5_2__triaxial_1p5_2 triaxial_1p5_3__triaxial_1p5_3 triaxial_2_4__triaxial_2_4 triaxial_2_5__triaxial_2_5 triaxial_3_4__triaxial_3_4.
- **Many-body model** `data/final/models/nbody_multi.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 108,412 ordered pairs from 239 clusters `multi` (mean 24.9 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_multi.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 6,160 particles of clusters `multi`; self blocks against MFS on validation: pairwise sum 1.737 % -> 0.999 %.
- **Configuration**: ONE random suspension, N = 16, shapes triaxial_2_4 in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **WARNING**: the `Xfine` cloud of triaxial_2_4 is NOT closer to the exact isolated particle than the `fine` one: the `fine vs Xfine` columns involving it are not an error estimate.
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_2_4 | 1 : 2 : 4 | 857 / 727; 0.0050 / 0.0022 | 1817 / 1545; 0.0015 / 0.0050 |

