# Stress model data/stress/models/stress_obl.pt

Error of each block of the cross block against the truth, % (Frobenius, validation pairs inside the range): far field alone -> with the model.

| set | pairs | velocity from strain | rotation from strain | stresslet from strain | stresslet from force / torque | self: U-E | self: W-E | self: S-E |
|---|---|---|---|---|---|---|---|---|
| obl | 1640 | 17.44 -> 0.198 | 18.05 -> 3.535 | 28.62 -> 1.367 | 17.55 -> 1.472 | 0.4 | 5.9 | 0.5 |

## Conditions
- truth: fine clouds, direct solve with strain columns (truth.dense_grand); not symmetrised
- learned inside distance 14; far field beyond; self columns: error of the learned self correction relative to that correction
- width 128, 2084 epochs of batch 512, lr 0.002, 1938 s; no many-body stress model
