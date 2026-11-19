# Bulk suspension in a periodic box: oblateSpheroid

| phi | operator | settling U / U0 | self-diffusion, translation | rotation | viscosity eta / eta0 | (eta/eta0 - 1) / phi |
|---|---|---|---|---|---|---|
| 0.01 | far | 0.8321 +- 0.0334 | 0.9014 | 0.9998 | 1.0264 +- 0.0000 | 2.636 |
| 0.01 | pair | 0.8228 +- 0.0321 | 0.8906 | 0.9948 | 1.0264 +- 0.0000 | 2.636 |
| 0.01 | full | 0.8159 +- 0.0311 | 0.8890 | 0.9948 | 1.0264 +- 0.0000 | 2.636 |
| 0.01 | full + stress model | 0.8159 +- 0.0311 | 0.8890 | 0.9948 | 1.0265 +- 0.0000 | 2.652 |
| 0.02 | far | 0.7923 +- 0.0501 | 0.8759 | 0.9996 | 1.0533 +- 0.0001 | 2.664 |
| 0.02 | pair | 0.7718 +- 0.0479 | 0.8514 | 0.9868 | 1.0533 +- 0.0001 | 2.664 |
| 0.02 | full | 0.7468 +- 0.0452 | 0.8493 | 0.9871 | 1.0533 +- 0.0001 | 2.664 |
| 0.02 | full + stress model | 0.7468 +- 0.0452 | 0.8493 | 0.9871 | 1.0541 +- 0.0002 | 2.704 |
| 0.05 | far | 0.6174 +- 0.0399 | 0.8321 | 0.9989 | 1.1371 +- 0.0002 | 2.742 |
| 0.05 | pair | 0.5669 +- 0.0378 | 0.7715 | 0.9673 | 1.1371 +- 0.0002 | 2.742 |
| 0.05 | full | 0.4252 +- 0.0331 | 0.7696 | 0.9682 | 1.1371 +- 0.0002 | 2.742 |
| 0.05 | full + stress model | 0.4252 +- 0.0331 | 0.7696 | 0.9682 | 1.1420 +- 0.0004 | 2.840 |
| 0.1 | far | 0.4551 +- 0.0195 | 0.7891 | 0.9978 | 1.2875 +- 0.0009 | 2.875 |
| 0.1 | pair | 0.3467 +- 0.0178 | 0.6563 | 0.9234 | 1.2875 +- 0.0009 | 2.875 |
| 0.1 | full | -0.2131 +- 0.0105 | 0.6572 | 0.9273 | 1.2875 +- 0.0009 | 2.875 |
| 0.1 | full + stress model | -0.2131 +- 0.0105 | 0.6572 | 0.9273 | 1.3106 +- 0.0010 | 3.106 |
| 0.15 | far | 0.3209 +- 0.0146 | 0.7593 | 0.9968 | 1.4505 +- 0.0007 | 3.004 |
| 0.15 | pair | 0.1538 +- 0.0125 | 0.5536 | 0.8743 | 1.4505 +- 0.0007 | 3.004 |
| 0.15 | full | -1.0381 +- 0.0102 | 0.5605 | 0.8837 | 1.4505 +- 0.0007 | 3.004 |
| 0.15 | full + stress model | -1.0381 +- 0.0102 | 0.5605 | 0.8837 | 1.5050 +- 0.0024 | 3.366 |

## Conditions
- 64 particles per box, 5 random boxes per volume fraction, random orientations, every pair at contact factor >= 1.05
- periodic cube, no mean flow; far field = 12 periodic Stokeslets per particle (Ewald sum); learned parts added for every pair with images
- settling: mean speed along gravity under equal forces, over the three directions of gravity, / the isolated orientation average
- a box of N particles is not an infinite suspension: settling and translational self-diffusion come out lower by about 1.76 (phi / N)^(1/3) (Hasimoto; 0.17 at phi 0.02, N 24); the viscosity has no such first-order shift.  Compare trends, or repeat with larger N
- viscosity: force- and torque-free particles in a uniform strain, average over the 5 strains; instantaneous (no Brownian, no contact stress)
- the stresslet blocks have no many-body model: far field (+ the two-body stress model where it says so)
- dilute limit of (eta/eta0 - 1) / phi = intrinsic viscosity from the fine cloud: oblateSpheroid 2.6098
- NO truth: MFS is free-space.  Spheres for reference: settling 1 - 6.55 phi (Batchelor), viscosity 1 + 2.5 phi + 5.0 phi^2 (Batchelor & Green)
- models: pair data/final/models/pair_obl.pt, nbody data/final/models/nbody_obl.pt, nself data/final/models/nself_obl.pt, stress data/stress/models/stress_obl.pt; clouds fine
