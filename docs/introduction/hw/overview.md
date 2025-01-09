---
title: Hardware Overview
outline: deep
---

# Overview
<figure style="text-align: center">
    <img src="/images/robot-joint-configuration.png" alt="missing" style="width:80%;margin:auto;" />
</figure>

# Technical Specifications
## General Specifications
| **Attribute**                    | **Value**                                              |
|----------------------------------|--------------------------------------------------------|
| **Size**                         | 600 x 690 x 1,400mm (W x D x H)                        |
| **Battery Capacity**             | 50V, 25Ah (1,270Wh)                                    |
| **Degrees of Freedom**           | See [Degrees of Freedom](#degrees-of-freedom)          |
| **Weight**                       | See [Weight](#weight)                                  |
| **Arm Payload**                  | 3kg (per arm)                                          |
| **Arm Reach**                    | 600 mm (to wrist) + hand                               |
| **Joint Maximum Speed, Angle Range** | See [Joint Maximum Speed, Angle Range](#joint-maximum-speed-angle-range) |
| **Power Supply Voltage and Frequency** | 48 VDC                                           |
| **Ambient Operating Temperature** | 40°C                                                  |
| **Arm Repeatability**            | < ±0.05 mm                                             |
| **Exterior Materials**           | Aluminum                                               |
| **Mobile Base Speed**            | 1.5 m/s                                                |

## Degrees of Freedom
| **PART**       | **# of DOF**    |
|----------------|-----------------|
| Wheel          | 1 DOF x 2       |
| Torso          | 6 DOF           |
| Arm            | 7 DOF x 2       |
| Head           | 2 DOF x 1       |
| **Total**      | **24 DOF**      |

## Weight
| **PART**       | **WEIGHT (kg)**                     |
|----------------|-------------------------------------|
| Upper body     | 38kg (Arm 11kg x 2, Torso 16kg)     |
| Lower body     | 42kg                                |
| Mobile         | 51kg                                |
| **Total**      | **131kg**                           |

## Joint Maximum Speed, Angle Range
| **Joint**      | **Speed**      | **Range**          |
|----------------|----------------|--------------------|
| torso_0, Ankle roll     | 120°/s         | -20° ~ 20°         |
| torso_1, Ankle pitch    | 120°/s         | -60° ~ 87°         |
| torso_2, Knee           | 180°/s         | -142° ~ 90°        |
| torso_3, Hip pitch      | 180°/s         | -45° ~ 90°         |
| torso_4, Hip roll       | 180°/s         | -30° ~ 30°         |
| torso_5, Hip yaw        | 180°/s         | -90° ~ 90°         |
| *_arm_0, Shoulder pitch | 180°/s         | -135° ~ 135°       |
| *_arm_1, Shoulder roll  | 180°/s         | -180° ~ 0.05° / -0.05° ~ 180°          |
| *_arm_2, Shoulder yaw   | 180°/s         | -120° ~ 120°       |
| *_arm_3, Elbow pitch    | 180°/s         | -150° ~ 0.01°         |
| *_arm_4, Wrist yaw1     | 180°/s         | -360° ~ 360°       |
| *_arm_5, Wrist pitch    | 180°/s         | -100° ~ 115°       |
| *_arm_6, Wrist yaw2     | 180°/s         | -170° ~ 170°       |
| head_0, Pan     | 180°/s         | -30° ~  30°      |
| head_1, Tilt     | 180°/s         | -20° ~  90°      |






