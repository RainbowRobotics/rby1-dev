---
title: Mechanical Part
outline: deep
---

# Mechanical Part
> :warning: **Note:** This robot is a research platform, and rapid improvements are constantly being made. While most of the information provided is accurate, we recommend double-checking for the most up-to-date details. For further inquiries, feel free to contact us at **rby.support@rainbow-robotics.com** or discuss on our GitHub Discussions page at [rby1-sdk Discussions](https://github.com/RainbowRobotics/rby1-sdk/discussions).


## Motor Specifications
The table provides details of each motor's gear type, motor power, maximum measurable current, speed, and range of motion. For example, the R/LWH model has a planetary gear system and uses a 200W motor. Other systems utilize harmonic gears, and the movement range and maximum speed vary according to each axis.

|| Gear Type | Motor Power | Max. measurable current/ Limit current | Max Speed     | Range               |
|---|-----------|-------------|----------------------------------------|---------------|---------------------|
| R/LWH     | Planetary   | 200W                                  | 150 RPM (1.5m/s) | Infinite           |
| AR        | Harmonic    | 250(450)W                             | 53/46 A       | 120°/s             | -20° ~ 20°         |
| AP        | Harmonic    | 250(450)W                             | 53/46 A       | 120°/s             | -60° ~ 70°         |
| KN        | Harmonic    | 250(450)W                             | 53/46 A       | 120°/s             | -140° ~ 45°        |
| HP        | Harmonic    | 200(280)W                             | 26/23 A       | 180°/s             | -45° ~ 90°         |
| HR        | Harmonic    | 200(280)W                             | 26/23 A       | 180°/s             | -30° ~ 30°         |
| HY        | Harmonic    | 200(280)W                             | 26/23 A       | 180°/s             | -90° ~ 90°         |
| R/LSP     | Harmonic    | 80(180)W                              | 26/14 A       | 180°/s             | -135° ~ 135°       |
| R/LSR     | Harmonic    | 80(180)W                              | 26/14 A       | 180°/s             | R : -180° ~ 4°<br> L : -4° ~ 180° |
| R/LSY     | Harmonic    | 80(180)W                              | 26/14 A       | 180°/s             | -120° ~ 120°       |
| R/LELB    | Harmonic    | 50(75)W                               | 8/7 A         | 180°/s             | -150° ~ 0°         |
| R/LWY1    | Harmonic    | 30(95)W                               | 8/7 A         | 360°/s             | -360° ~ 360°       |
| R/LWP     | Harmonic    | 30(95)W                               | 8/7 A         | 360°/s             | -100° ~ 115°       |
| R/LWY2    | Harmonic + Pulley | 45W                            | 8/7 A         | 360°/s             | -170° ~ 170°       |


## Torque Specifications
This table details the torque performance of various motor types. It includes continuous torque, repeated peak torque, and momentary peak torque in Newton-meters (Nm). Additionally, the table specifies the gear ratio, output speed in degrees per second (deg/s), motor encoder resolution in bits, transmission error in arcseconds, stiffness in Newton-meters per radian (Nm/rad), and the motor torque constant in Newton-meters per Ampere (Nm/A).
| Type                 | AR, AP, KN | HP, HR, HY | R/L SP, R/L SR, R/L SY | R/L ELB | R/L WY1, R/L WP, R/L WY2 |
|----------------------|------------|------------|-------------------------|---------|--------------------------|
| Continuous Torque (Nm) | 250        | 125        | 65                      | 35      | 14                       |
| Repeated Peak Torque (Nm) | 433        | 204        | 70                      | 36      | 36                       |
| Momentary Peak Torque (Nm) | 841        | 369        | 143                     | 70      | 70                       |
| Output Speed (deg/s) | 120        | 180        | 180                     | 180     | 360                      |
| Motor Encoder Resolution (bit) | 14         | 14         | 14                      | 14      | 14                       |
| Transmission Error (arcsec) | ~50        | ~50        | ~50                     | ~50     | ~50                      |
| Stiffness (Nm/rad)   | 110,000    | 50,000     | 14,000                  | 6,100   | 6,100                    |
| Motor Torque Constant (Nm/A) | 0.15       | 0.10       | 0.10                    | 0.10    | 0.05                     |




## Robot Dimensions
The diagrams show the front and side views of the robot with detailed measurements. The total height of the robot is 1470 mm, and the arm span is 566.67 mm, with a 140-degree range of motion. The base dimensions are 662.62 mm in length and 580 mm in width. These measurements provide an understanding of the physical space the robot occupies, as well as its potential reach and movement range.

> :warning: **Note:** Physical limits and control limits may differ. For detailed operation ranges, please refer to the [URDF files](https://github.com/RainbowRobotics/rby1-sdk/tree/main/models/rby1a/urdf).

<figure style="text-align: center">
    <img src="/images/blueprint1.png" alt="Robot Dimensions" style="width:100%;margin:auto;" />
</figure>

