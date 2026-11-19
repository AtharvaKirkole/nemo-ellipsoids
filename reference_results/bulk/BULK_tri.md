# Bulk suspension in a periodic box: triaxial_123

| phi | operator | settling U / U0 | self-diffusion, translation | rotation | viscosity eta / eta0 | (eta/eta0 - 1) / phi |
|---|---|---|---|---|---|---|
| 0.01 | far | 0.8378 +- 0.0389 | 0.8977 | 0.9997 | 1.0276 +- 0.0000 | 2.764 |
| 0.01 | pair | 0.8269 +- 0.0373 | 0.8846 | 0.9908 | 1.0276 +- 0.0000 | 2.764 |
| 0.01 | full | 0.8193 +- 0.0361 | 0.8830 | 0.9908 | 1.0276 +- 0.0000 | 2.764 |
| 0.01 | full + stress model | 0.8193 +- 0.0361 | 0.8830 | 0.9908 | 1.0279 +- 0.0001 | 2.786 |
| 0.02 | far | 0.7775 +- 0.0382 | 0.8712 | 0.9995 | 1.0558 +- 0.0001 | 2.791 |
| 0.02 | pair | 0.7561 +- 0.0369 | 0.8458 | 0.9834 | 1.0558 +- 0.0001 | 2.791 |
| 0.02 | full | 0.7290 +- 0.0347 | 0.8437 | 0.9837 | 1.0558 +- 0.0001 | 2.791 |
| 0.02 | full + stress model | 0.7290 +- 0.0347 | 0.8437 | 0.9837 | 1.0566 +- 0.0001 | 2.830 |
| 0.05 | far | 0.6126 +- 0.0395 | 0.8258 | 0.9987 | 1.1436 +- 0.0003 | 2.872 |
| 0.05 | pair | 0.5566 +- 0.0366 | 0.7577 | 0.9534 | 1.1436 +- 0.0003 | 2.872 |
| 0.05 | full | 0.3961 +- 0.0324 | 0.7561 | 0.9552 | 1.1436 +- 0.0003 | 2.872 |
| 0.05 | full + stress model | 0.3961 +- 0.0324 | 0.7561 | 0.9552 | 1.1495 +- 0.0009 | 2.989 |
| 0.1 | far | 0.4401 +- 0.0158 | 0.7814 | 0.9973 | 1.3016 +- 0.0004 | 3.016 |
| 0.1 | pair | 0.3247 +- 0.0150 | 0.6418 | 0.9079 | 1.3016 +- 0.0004 | 3.016 |
| 0.1 | full | -0.2941 +- 0.0106 | 0.6441 | 0.9124 | 1.3016 +- 0.0004 | 3.016 |
| 0.1 | full + stress model | -0.2941 +- 0.0106 | 0.6441 | 0.9124 | 1.3253 +- 0.0010 | 3.253 |
| 0.15 | far | 0.3127 +- 0.0148 | 0.7506 | 0.9960 | 1.4712 +- 0.0011 | 3.142 |
| 0.15 | pair | 0.1354 +- 0.0129 | 0.5351 | 0.8529 | 1.4712 +- 0.0011 | 3.142 |
| 0.15 | full | -1.1388 +- 0.0153 | 0.5469 | 0.8645 | 1.4712 +- 0.0011 | 3.142 |
| 0.15 | full + stress model | -1.1388 +- 0.0153 | 0.5469 | 0.8645 | 1.5268 +- 0.0020 | 3.512 |

## Conditions
- 64 particles per box, 5 random boxes per volume fraction, random orientations, every pair at contact factor >= 1.05
- periodic cube, no mean flow; far field = 12 periodic Stokeslets per particle (Ewald sum); learned parts added for every pair with images
- settling: mean speed along gravity under equal forces, over the three directions of gravity, / the isolated orientation average
- a box of N particles is not an infinite suspension: settling and translational self-diffusion come out lower by about 1.76 (phi / N)^(1/3) (Hasimoto; 0.17 at phi 0.02, N 24); the viscosity has no such first-order shift.  Compare trends, or repeat with larger N
- viscosity: force- and torque-free particles in a uniform strain, average over the 5 strains; instantaneous (no Brownian, no contact stress)
- the stresslet blocks have no many-body model: far field (+ the two-body stress model where it says so)
- dilute limit of (eta/eta0 - 1) / phi = intrinsic viscosity from the fine cloud: triaxial_123 2.7361
- NO truth: MFS is free-space.  Spheres for reference: settling 1 - 6.55 phi (Batchelor), viscosity 1 + 2.5 phi + 5.0 phi^2 (Batchelor & Green)
- models: pair data/final/models/pair_t123.pt, nbody data/final/models/nbody_t123.pt, nself data/final/models/nself_t123.pt, stress data/stress/models/stress_tri.pt; clouds fine
