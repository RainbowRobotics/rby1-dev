# Motor Driver

## Actuator System Overview

<img :src="$withBase('/images/hardware/motor_driver/actuator_system.png')" alt="Exploded view of an RB-Y1 joint actuator" class="center rounded-img" style="width:800px">

---
## Actuator Detail Specifications

The actuators are named by their size (#32, #25, #17, #14, #14CP/C). The first row shows the SDK joints that use each size.

| Type | #32 | #25 | #17 | #14 | #14CP/C |
| --- | --- | --- | --- | --- | --- |
| SDK joints | `torso_0` – `torso_2` | `torso_3` – `torso_5` | `right_arm_0` – `right_arm_2`, `left_arm_0` – `left_arm_2` | `right_arm_3`, `left_arm_3` | `right_arm_4`, `right_arm_5`, `left_arm_4`, `left_arm_5` |
| Continuous Torque (Nm) | 250 | 125 | 65 | 35 | 14 |
| Repeated Peak Torque (Nm) | 433 | 204 | 70 | 36 | 36 |
| Momentary Peak Torque (Nm) | 841 | 369 | 143 | 70 | 70 |
| Gear Ratio | 101:1 | 101:1 | 101:1 | 101:1 | 100:1 |
| Output Speed (deg/s) | 120 | 180 | 180 | 180 | 360 |
| Motor Encoder Resolution (bit) | 14 | 14 | 14 | 14 | 14 |
| Transmission Error (arcsec) | ~50 | ~50 | ~50 | ~50 | ~50 |
| Stiffness (Nm/rad) | 110,000 | 50,000 | 14,000 | 6,100 | 6,100 |
| Motor Torque Constant (Nm/A) | 0.15 | 0.10 | 0.10 | 0.10 | 0.055 |

- On Model A v1.2 and Model M v1.2 and v1.3, `head_0` and `head_1` also use 100:1 CAN actuators with a torque constant of 0.055 Nm/A. On v1.0 and v1.1 robots, the head uses Dynamixel actuators. Model UB always uses Dynamixel actuators for the head, not CAN.
- `right_arm_6` and `left_arm_6` are not in this table. They have a 200:1 reduction on Model A and Model M v1.0 – v1.2, and a 100:1 reduction on Model M v1.3 (see [Mechanical Part](mechanical_part.md#torque-specifications)).
- These are actuator ratings. The joint range and speed limits that the controller enforces are in [Joint Range and Speed Limits](overview.md#joint-range-and-speed-limits).
