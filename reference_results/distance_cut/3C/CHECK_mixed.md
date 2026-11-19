# Structural checks, 16 particles of triaxial_123, prolateSpheroid, oblateSpheroid at phi 0.1

| matrix | asymmetry | smallest eigenvalue / MFS's | rotation equivariance error | against MFS, % |
|---|---|---|---|---|
| far field | 1.3e-16 | 1.5557 | 5.7e-16 | 8.53 |
| + two-body | 9.9e-17 | 0.6127 | 4.5e-16 | 5.40 |
| + many-body | 1.1e-16 | 0.9772 | 4.7e-16 | 1.99 |
| MFS fine (the truth) | 2.4e-04 | 1 | | 0 |
| MFS Xfine | 6.0e-05 | 0.9893 | | 0.019 (= the error of the fine truth) |

MFS smallest eigenvalue 1.8431e-03 (positive).  A ratio > 0 means that matrix is positive definite on this configuration; the operators are symmetric by construction, positive definiteness is only verified.

## Conditions

- **Two-body model** `data/final/models/pair_mixed.pt`: triaxial form, 22 inputs, 34 true + 61 pseudo tensors (190 coefficients per block, two blocks), width 128, 84,988 parameters, learned inside r_cut = 14 pair lengths (far field beyond).  Trained on 73,722 ordered pairs, 400000 steps, seed 0: triaxial_123__triaxial_123 prolateSpheroid__prolateSpheroid oblateSpheroid__oblateSpheroid triaxial_123__prolateSpheroid triaxial_123__oblateSpheroid.
- **Many-body model** `data/final/models/nbody_mixed.pt`: 182 inputs (22 of the pair + 20 per band x 8 bands), 74 true + 101 pseudo tensors, width 128, 71,006 parameters; corrects pairs within 14, sees neighbours within 14 (pair lengths) of the pair midpoint.  Trained on 194,572 ordered pairs from 261 clusters `mixed` (mean 34.5 neighbours per pair), seed 0.
- **Many-body self model** `data/final/models/nself_mixed.pt` (part of '+ many-body'): 114 inputs, 43 true + 40 pseudo tensors, width 128; neighbours within 14 particle lengths.  Trained on 7,744 particles of clusters `mixed`; self blocks against MFS on validation: pairwise sum 2.287 % -> 1.402 %.
- **Configuration**: ONE random suspension, N = 16, shapes triaxial_123, prolateSpheroid, oblateSpheroid in equal numbers, phi 0.1, random orientations, contact factor >= 1.05, seed 0.
- **Columns**: asymmetry = |M - M^T| / |M|; eigenvalue of the symmetric part relative to MFS's smallest; equivariance = |M(Q x) - G M(x) G^T| / |M| for a random rotation Q of the whole configuration; against MFS = Frobenius error of the whole matrix (%).
- **Truth**: MFS, `fine` clouds, viscosity 1; the whole mobility matrix of the configuration (direct solve when small, else GMRES to 1e-07).
- **Particles and clouds** (error of each cloud against the exact isolated ellipsoid):

| shape | semi-axes | fine: nodes / sources; exact-mobility error trans / rot % | Xfine: nodes / sources; exact-mobility error trans / rot % |
|---|---|---|---|
| triaxial_123 | 1 : 2 : 3 | 660 / 560; 0.0074 / 0.0055 | 1400 / 1190; 0.0020 / 0.0011 |
| prolateSpheroid | 1 : 1 : 3 | 654 / 572; 0.0004 / 0.0020 | 1388 / 1214; 0.0001 / 0.0003 |
| oblateSpheroid | 2 : 2 : 1 | 678 / 593; 0.0006 / 0.0016 | 1328 / 1162; 0.0001 / 0.0001 |

