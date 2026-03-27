# Mechanical Part

```{note} This robot is a research platform, and rapid improvements are constantly being made. While most of the information provided is accurate, we recommend double-checking for the most up-to-date details. For further inquiries, feel free to contact us at rby.support@rainbow-robotics.com or discuss on our GitHub Discussions page at 
<a href="https://github.com/RainbowRobotics/rby1-sdk/discussions"
   target="_blank" rel="noopener noreferrer">
   rby1-sdk Discussions
</a>
.
```
---

## Motor Specifications
<br>

The table provides details of each motor's gear type, motor power, maximum measurable current, speed, and range of motion. For example, the R/LWH model has a planetary gear system and uses a 200W motor. Other systems utilize harmonic gears, and the movement range and maximum speed vary according to each axis.
<br>

|        | Gear Type         | Motor Power | Max. measurable current/ Limit current | Max Speed | Range                        |
| ------ | ----------------- | ----------- | -------------------------------------- | --------- | ---------------------------- |
|`RWH/LWH` | Planetary         |	200W       |	    |150 RPM (1.5m/s)       |  Infinite |                              | 
|`AR`    | Harmonic          |	250(450)W  |	53/46 A                             |	120°/s  | -15° ~ 15°                   |
|`AP`    | Harmonic          |	250(450)W  |	53/46 A                             |	120°/s  | -30° ~ 90°                   |
|`KN`    | Harmonic          |	250(450)W  |	53/46 A                             |	120°/s  | -150° ~ 90°                  |
|`HP`    | Harmonic          |	200(280)W  |	26/23 A                             |	180°/s  | -45° ~ 90°                   |
|`HR`    | Harmonic          |	200(280)W  |	26/23 A                             |	180°/s  | -30° ~ 30°                   |
|`HY`    | Harmonic          |	200(280)W  |	26/23 A                             |	180°/s  | -135° ~ 135°                   |
|`RSP/LSP` | Harmonic          |	80(180)W   |	26/14 A                             |	180°/s  | -180° ~ 180°                 |
|`RSR/LSR` | Harmonic          |	80(180)W   |	26/14 A                             |	180°/s  | R : -180° ~ 0°  L : 0° ~ 180°|
|`RSY/LSY` | Harmonic          |	80(180)W   |	26/14 A                             |	180°/s  | -180° ~ 180°                 |
|`RELB/LELB`| Harmonic          |	50(75)W    |	8/7 A                               |	180°/s  | -150° ~ 0°                   |
|`RWY1/LWY1`| Harmonic          |	30(95)W    |	8/7 A                               |	360°/s  | -180° ~ 180°                 |
|`RWP/LWP` | Harmonic          |	30(95)W    |	8/7 A                               |	360°/s  | -90° ~ 110°                 |
|`RWY2/LWY2`| Harmonic + Pulley |	45W        |	8/7 A                               |	360°/s  | -155° ~ 155°                 |

---
## Torque Specifications
<br>

This table details the torque performance of various motor types. It includes continuous torque, repeated peak torque, and momentary peak torque in Newton-meters (Nm). Additionally, the table specifies the gear ratio, output speed in degrees per second (deg/s), motor encoder resolution in bits, transmission error in arcseconds, stiffness in Newton-meters per radian (Nm/rad), and the motor torque constant in Newton-meters per Ampere (Nm/A).
<br>

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
<br>

The diagrams show the front and side views of the robot with detailed measurements. The total height of the robot is 1400 mm, and the width is 600 mm. These measurements provide an understanding of the physical space the robot occupies, as well as its potential reach and movement range.

```{note} Physical limits and control limits may differ. For detailed operation ranges, please refer to the 
<a href="https://github.com/RainbowRobotics/rby1-sdk/tree/main/models/rby1a/urdf"
   target="_blank" rel="noopener noreferrer">
   URDF files
</a>
.
```
<br>

<!-- ```{image} ../_static/images/hardware/mechanical_part/blueprint1.png
   :alt: blueprint1
   :align: center
   :width: 600px
``` -->