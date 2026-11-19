# Bulk suspension in a periodic box: prolateSpheroid

| phi | operator | settling U / U0 | self-diffusion, translation | rotation | viscosity eta / eta0 | (eta/eta0 - 1) / phi |
|---|---|---|---|---|---|---|
| 0.01 | far | 0.8283 +- 0.0367 | 0.8948 | 0.9997 | 1.0281 +- 0.0001 | 2.815 |
| 0.01 | pair | 0.8168 +- 0.0351 | 0.8811 | 0.9922 | 1.0281 +- 0.0001 | 2.815 |
| 0.01 | full | 0.8079 +- 0.0341 | 0.8797 | 0.9919 | 1.0281 +- 0.0001 | 2.815 |
| 0.01 | full + stress model | 0.8079 +- 0.0341 | 0.8797 | 0.9919 | 1.0284 +- 0.0001 | 2.835 |
| 0.02 | far | 0.7771 +- 0.0532 | 0.8677 | 0.9995 | 1.0569 +- 0.0001 | 2.844 |
| 0.02 | pair | 0.7536 +- 0.0508 | 0.8400 | 0.9854 | 1.0569 +- 0.0001 | 2.844 |
| 0.02 | full | 0.7232 +- 0.0481 | 0.8384 | 0.9851 | 1.0569 +- 0.0001 | 2.844 |
| 0.02 | full + stress model | 0.7232 +- 0.0481 | 0.8384 | 0.9851 | 1.0578 +- 0.0002 | 2.888 |
| 0.05 | far | 0.5827 +- 0.0302 | 0.8212 | 0.9987 | 1.1462 +- 0.0003 | 2.924 |
| 0.05 | pair | 0.5246 +- 0.0288 | 0.7518 | 0.9611 | 1.1462 +- 0.0003 | 2.924 |
| 0.05 | full | 0.3555 +- 0.0256 | 0.7517 | 0.9617 | 1.1462 +- 0.0003 | 2.924 |
| 0.05 | full + stress model | 0.3555 +- 0.0256 | 0.7517 | 0.9617 | 1.1518 +- 0.0008 | 3.036 |
| 0.1 | far | 0.4449 +- 0.0342 | 0.7758 | 0.9973 | 1.3064 +- 0.0005 | 3.064 |
| 0.1 | pair | 0.3206 +- 0.0314 | 0.6260 | 0.9150 | 1.3064 +- 0.0005 | 3.064 |
| 0.1 | full | -0.3762 +- 0.0226 | 0.6321 | 0.9191 | 1.3064 +- 0.0005 | 3.064 |
| 0.1 | full + stress model | -0.3762 +- 0.0226 | 0.6321 | 0.9191 | 1.3318 +- 0.0017 | 3.318 |
| 0.15 | far | 0.3401 +- 0.0198 | 0.7445 | 0.9960 | 1.4794 +- 0.0012 | 3.196 |
| 0.15 | pair | 0.1454 +- 0.0178 | 0.5080 | 0.8589 | 1.4794 +- 0.0012 | 3.196 |
| 0.15 | full | -1.4065 +- 0.0185 | 0.5248 | 0.8704 | 1.4794 +- 0.0012 | 3.196 |
| 0.15 | full + stress model | -1.4065 +- 0.0185 | 0.5248 | 0.8704 | 1.5403 +- 0.0025 | 3.602 |

## Conditions
- 64 particles per box, 5 random boxes per volume fraction, random orientations, every pair at contact factor >= 1.05
- periodic cube, no mean flow; far field = 12 periodic Stokeslets per particle (Ewald sum); learned parts added for every pair with images
- settling: mean speed along gravity under equal forces, over the three directions of gravity, / the isolated orientation average
- a box of N particles is not an infinite suspension: settling and translational self-diffusion come out lower by about 1.76 (phi / N)^(1/3) (Hasimoto; 0.17 at phi 0.02, N 24); the viscosity has no such first-order shift.  Compare trends, or repeat with larger N
- viscosity: force- and torque-free particles in a uniform strain, average over the 5 strains; instantaneous (no Brownian, no contact stress)
- the stresslet blocks have no many-body model: far field (+ the two-body stress model where it says so)
- dilute limit of (eta/eta0 - 1) / phi = intrinsic viscosity from the fine cloud: prolateSpheroid 2.7858
- NO truth: MFS is free-space.  Spheres for reference: settling 1 - 6.55 phi (Batchelor), viscosity 1 + 2.5 phi + 5.0 phi^2 (Batchelor & Green)
- models: pair data/final/models/pair_pro.pt, nbody data/final/models/nbody_pro.pt, nself data/final/models/nself_pro.pt, stress data/stress/models/stress_pro.pt; clouds fine
