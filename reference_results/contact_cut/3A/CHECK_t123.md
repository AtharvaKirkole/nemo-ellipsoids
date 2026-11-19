# Structural checks, 16 particles of triaxial_123 at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.4e-16 | 1.2238 | 8.1e-16 | 7.94 |
| + two-body | 8.4e-17 | 0.7020 | 6.3e-16 | 4.84 |
| + many-body | 8.9e-17 | 0.9775 | 6.4e-16 | 1.61 |
| MFS fine (the truth) | 1.9e-04 | 1 | | 0 |
| MFS Xfine | 6.5e-05 | 1.0008 | | 0.014 (= the error of the fine truth) |

MFS smallest eigenvalue 2.3143e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

## Conditions

- **Two-body model** `data/final_c/models/pair_t123.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside contact factor 4 (far field beyond).  Trained on 29,020 ordered pairs, 200000 steps, seed 0: triaxial_123__triaxial_123.
- **Many-body model** `data/final_c/models/nbody_t123.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 185,350 ordered pairs from 270 clusters `t123` (mean 31.2 neighbours per pair), seed 0.
- **Many-body self model** `data/final_c/models/nself_t123.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 8,256 particles of clusters `t123`; self blocks against MFS on validation: pairwise sum 2.235 % -> 1.142 %.
- **Configuration**: ONE random suspension, N = 16, shapes triaxial_123 in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |

