# Mechanical Part

::: info This robot is a research platform, and rapid improvements are constantly being made. While most of the information provided is accurate, we recommend double-checking for the most up-to-date details. For further inquiries, feel free to contact us at rby.support@rainbow-robotics.com or discuss on our GitHub Discussions page at 
<a href="https://github.com/RainbowRobotics/rby1-sdk/discussions"
   target="_blank" rel="noopener noreferrer">
   rby1-sdk Discussions
</a>
.
:::
---

## Motor Specifications

The table provides details of each motor's gear type, motor power, maximum measurable current and rated maximum output speed. For example, the R/LWH model has a planetary gear system and uses a 200W motor. Other systems utilize harmonic gears.
These are actuator ratings. The joint range and speed limits that the controller enforces come from the robot model; see [Joint Range and Speed Limits](overview.md#joint-range-and-speed-limits).

|        | Gear Type         | Motor Power | Max. measurable current/ Limit current | Rated Max Output Speed |
| ------ | ----------------- | ----------- | -------------------------------------- | --------- |
|`RWH/LWH` | Planetary         |	200W       |	    |150 RPM (1.5m/s)       |
|`AR`    | Harmonic          |	250(450)W  |	53/46 A                             |	120°/s  |
|`AP`    | Harmonic          |	250(450)W  |	53/46 A                             |	120°/s  |
|`KN`    | Harmonic          |	250(450)W  |	53/46 A                             |	120°/s  |
|`HP`    | Harmonic          |	200(280)W  |	26/23 A                             |	180°/s  |
|`HR`    | Harmonic          |	200(280)W  |	26/23 A                             |	180°/s  |
|`HY`    | Harmonic          |	200(280)W  |	26/23 A                             |	180°/s  |
|`RSP/LSP` | Harmonic          |	80(180)W   |	26/14 A                             |	180°/s  |
|`RSR/LSR` | Harmonic          |	80(180)W   |	26/14 A                             |	180°/s  |
|`RSY/LSY` | Harmonic          |	80(180)W   |	26/14 A                             |	180°/s  |
|`RELB/LELB`| Harmonic          |	50(75)W    |	8/7 A                               |	180°/s  |
|`RWY1/LWY1`| Harmonic          |	30(95)W    |	8/7 A                               |	360°/s  |
|`RWP/LWP` | Harmonic          |	30(95)W    |	8/7 A                               |	360°/s  |
|`RWY2/LWY2`| Harmonic + Pulley |	45W        |	8/7 A                               |	360°/s  |

---
## Torque Specifications

This table details the torque performance of various motor types. It includes continuous torque, repeated peak torque, and momentary peak torque in Newton-meters (Nm). Additionally, the table specifies the gear ratio, output speed in degrees per second (deg/s), motor encoder resolution in bits, transmission error in arcseconds, stiffness in Newton-meters per radian (Nm/rad), and the motor torque constant in Newton-meters per Ampere (Nm/A).

| Type                           |	AR, AP, KN | HP, HR, HY |	R/L SP, R/L SR, R/L SY | R/L ELB | R/L WY1, R/L WP, R/L WY2 |
| ------------------------------ | ----------- | ---------  | ------------------------ | ------- | -----------------------  |
|Continuous Torque (Nm)          |	250        |	125     |	65                     |	35   |	14                      |
|Repeated Peak Torque (Nm)       |	433        |	204     |	70                     |	36   |	36                      |
|Momentary Peak Torque (Nm)      |	841        |	369     |	143                    |	70   |	70                      |
|Output Speed (deg/s)            |	120        |	180     |	180                    |	180  |	360                     |
| Motor Encoder Resolution (bit) |	14         |	14      |	14                     |	14   |	14                      |
|Transmission Error (arcsec)     |	~50        |	~50     |	~50                    |	~50  |	~50                     |
|Stiffness (Nm/rad)              |	110,000    |	50,000  |	14,000                 | 6,100   |	6,100                   |
|Motor Torque Constant (Nm/A)    |	0.15       |	0.10    |	0.10                   |	0.10 |	0.05                    |

---
## Robot Dimensions

The diagrams show the front and side views of the robot with detailed measurements. The total height of the robot is 1400 mm, and the width is 600 mm. These measurements provide an understanding of the physical space the robot occupies, as well as its potential reach and movement range.

::: info Physical limits and control limits may differ. For detailed operation ranges, please refer to the 
<a href="https://github.com/RainbowRobotics/rby1-sdk/tree/main/models/rby1a/urdf"
   target="_blank" rel="noopener noreferrer">
   URDF files
</a>
.
:::

<!-- ```{image} ../_static/images/hardware/mechanical_part/blueprint1.png
   :alt: blueprint1
   :align: center
   :width: 600px
``` -->
