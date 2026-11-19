# Stress model data/stress/models/stress_tri.pt

Error of each block of the cross block against the truth, % (Frobenius, validation pairs inside the range): far field alone -> with the model.

| set | pairs | velocity from strain | rotation from strain | stresslet from strain | stresslet from force / torque | self: U-E | self: W-E | self: S-E |
|---|---|---|---|---|---|---|---|---|
| tri | 1640 | 16.73 -> 3.258 | 20.33 -> 9.400 | 34.20 -> 7.222 | 17.26 -> 4.626 | 5.1 | 17.2 | 5.7 |

## Conditions
- truth: fine clouds, direct solve with strain columns (truth.dense_grand); not symmetrised
- learned inside distance 14; far field beyond; self columns: error of the learned self correction relative to that correction
- width 128, 2084 epochs of batch 512, lr 0.002, 1811 s; no many-body stress model
