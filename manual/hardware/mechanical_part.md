# Mechanical Part

::: info Note
RB-Y1 is a research platform and its hardware is improved often. If a value on this page does not match your robot, contact rby.support@rainbow-robotics.com or ask on
<a href="https://github.com/RainbowRobotics/rby1-sdk/discussions" target="_blank" rel="noopener noreferrer">rby1-sdk Discussions</a>.
:::

---

## Motor Specifications

The tables on this page are actuator ratings. The joint range and speed limits that the controller enforces come from the robot model; see [Joint Range and Speed Limits](overview.md#joint-range-and-speed-limits).

The wheel actuators use a planetary gear. All other joints use a harmonic gear; arm_6 adds a pulley stage.

| Actuator | SDK joints (Model A / M) | Gear Type | Motor Power | Max. measurable current / Limit current | Rated Max Output Speed |
| --- | --- | --- | --- | --- | --- |
| `RWH/LWH` | `right_wheel`, `left_wheel` (Model A) | Planetary | 200W | — | 150 RPM (1.5 m/s) |
| `AR`, `AP`, `KN` | `torso_0` – `torso_2` | Harmonic | 250(450)W | 53/46 A | 120°/s |
| `HP`, `HR`, `HY` | `torso_3` – `torso_5` | Harmonic | 200(280)W | 26/23 A | 180°/s |
| `RSP/LSP`, `RSR/LSR`, `RSY/LSY` | `right_arm_0` – `right_arm_2`, `left_arm_0` – `left_arm_2` | Harmonic | 80(180)W | 26/14 A | 180°/s |
| `RELB/LELB` | `right_arm_3`, `left_arm_3` | Harmonic | 50(75)W | 8/7 A | 180°/s |
| `RWY1/LWY1`, `RWP/LWP` | `right_arm_4`, `right_arm_5`, `left_arm_4`, `left_arm_5` | Harmonic | 30(95)W | 8/7 A | 360°/s |
| `RWY2/LWY2` | `right_arm_6`, `left_arm_6` | Harmonic + Pulley | 45W | 8/7 A | see note |

- In the actuator names, R and L mean right and left. The torso actuators use the former leg names (AR, AP, KN, HP, HR, HY); in the SDK they are `torso_0` to `torso_5`.
- A dash (—) means that the value is not listed.
- Motor Power: some rows give a second value in parentheses, for example 250(450)W. The source table does not say which rating the value in parentheses is (for example peak or maximum), and this manual has not verified it. Contact the support team if you need the exact meaning.
- On Model A and on Model M v1.0 – v1.2, arm_6 has a 200:1 reduction (twice the ratio of the other wrist joints) and a 12-bit motor encoder. On Model M v1.3, arm_6 has a 100:1 reduction and a 14-bit motor encoder. Its controller speed limit is 120°/s (see [Joint Range and Speed Limits](overview.md#joint-range-and-speed-limits)).
- The Model M wheels (`wheel_fr`, `wheel_fl`, `wheel_rr`, `wheel_rl`) are not in this table.

---
## Torque Specifications

This table lists the torque ratings in newton-meters (Nm), the gear ratio, the output speed in degrees per second (deg/s), the motor encoder resolution in bits, the transmission error in arcseconds, the stiffness in Nm/rad and the motor torque constant in Nm/A.

| Type | AR, AP, KN | HP, HR, HY | R/L SP, R/L SR, R/L SY | R/L ELB | R/L WY1, R/L WP | R/L WY2 |
| --- | --- | --- | --- | --- | --- | --- |
| SDK joints | `torso_0` – `torso_2` | `torso_3` – `torso_5` | `*_arm_0` – `*_arm_2` | `*_arm_3` | `*_arm_4`, `*_arm_5` | `*_arm_6` |
| Continuous Torque (Nm) | 250 | 125 | 65 | 35 | 14 | 14 |
| Repeated Peak Torque (Nm) | 433 | 204 | 70 | 36 | 36 | 36 |
| Momentary Peak Torque (Nm) | 841 | 369 | 143 | 70 | 70 | 70 |
| Gear Ratio | 101:1 | 101:1 | 101:1 | 101:1 | 100:1 | 200:1 (Model M v1.3: 100:1) |
| Output Speed (deg/s) | 120 | 180 | 180 | 180 | 360 | 120 (controller limit) |
| Motor Encoder Resolution (bit) | 14 | 14 | 14 | 14 | 14 | 12 (Model M v1.3: 14) |
| Transmission Error (arcsec) | ~50 | ~50 | ~50 | ~50 | ~50 | ~50 |
| Stiffness (Nm/rad) | 110,000 | 50,000 | 14,000 | 6,100 | 6,100 | 6,100 |
| Motor Torque Constant (Nm/A) | 0.15 | 0.10 | 0.10 | 0.10 | 0.055 | 0.0837 |

The gear ratios, the arm_6 encoder resolution and the torque constants are the values that the robot PC uses for each joint. The other WY2 values are the ratings published for the wrist actuators.

---
## Robot Dimensions

See [General Specifications](overview.md#general-specifications) for the size and weight of each model.

::: info Note
Physical limits and control limits can differ. The control limits are in the URDF files of each model in rby1-sdk v0.10.1:
<a href="https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/models/rby1a/urdf" target="_blank" rel="noopener noreferrer">Model A</a>,
<a href="https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/models/rby1m/urdf" target="_blank" rel="noopener noreferrer">Model M</a>,
<a href="https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/models/rby1ub/urdf" target="_blank" rel="noopener noreferrer">Model UB</a>.
:::
