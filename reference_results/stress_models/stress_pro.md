# Stress model data/stress/models/stress_pro.pt

Error of each block of the cross block against the truth, % (Frobenius, validation pairs inside the range): far field alone -> with the model.

| set | pairs | velocity from strain | rotation from strain | stresslet from strain | stresslet from force / torque | self: U-E | self: W-E | self: S-E |
|---|---|---|---|---|---|---|---|---|
| pro | 1640 | 19.10 -> 0.298 | 24.28 -> 4.465 | 45.33 -> 0.744 | 20.11 -> 1.892 | 0.6 | 6.4 | 0.8 |

## Conditions
- truth: fine clouds, direct solve with strain columns (truth.dense_grand); not symmetrised
- learned inside distance 14; far field beyond; self columns: error of the learned self correction relative to that correction
- width 128, 2084 epochs of batch 512, lr 0.002, 1612 s; no many-body stress model
