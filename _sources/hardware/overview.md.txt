# Overview

```{figure} ../_static/images/hardware/overview/robot-joint-configuration.png
   :alt: robot joint configuration
   :align: center
   :width: 400px
   :class: white_bg
   ```

---
## Technical Specifications
<br>

### General Specifications
| **Attribute**                        | **Value**                        |
| ------------------------------------ | -------------------------------- |
| **Size**                             | 600 x 690 x 1,400 mm (W x D x H) |
| **Battery Capacity**                 | 50 V, 25 Ah (1,270 Wh)           |
| **Degrees of Freedom**               | Model A: 24 DOF, Model M: 26 DOF |
| **Weight**                           | 131 kg                           |
| **Arm Payload**                      | 3 kg (per arm)                   |
| **Arm Reach**                        | 600 mm (to wrist) + hand         |
| **Joint Maximum Speed, Angle Range** | See [Joint Maximum Speed and Angle Range](#joint-maximum-speed-and-angle-range)|
| **Power Supply Voltage**             | 48 VDC                           |
| **Ambient Operating Temperature**    | Up to 40 °C                      |
| **Arm Repeatability**                | < ±0.05 mm                       |
| **Exterior Materials**               | Aluminum                         |
| **Mobile Base Speed**                | 1.5 m/s                          |

---
### Degrees of Freedom

#### Model A DOF

| **Part**  | **# of DOF** |
| --------- | ------------ |
| Wheel     | 1 DOF × 2    |
| Torso     | 6 DOF        |
| Arm       | 7 DOF × 2    |
| Head      | 2 DOF        |
| **Total** | **24 DOF**   |

#### Model M DOF

| **Part**  | **# of DOF** |
| --------- | ------------ |
| Wheel     | 1 DOF × 4    |
| Torso     | 6 DOF        |
| Arm       | 7 DOF × 2    |
| Head      | 2 DOF        |
| **Total** | **24 DOF**   |

---
### Weight

#### Model A Weight

| **Part**    | **Weight (kg)**           |
| ----------- | ------------------------- |
| Upper body  | 38 (Arm 11 × 2, Torso 16) |
| Lower body  | 42                        |
| Mobile base | 51                        |
| **Total**   | **131**                   |

#### Model M Weight

| **Part**    | **Weight (kg)**           |
| ----------- | ------------------------- |
| Upper body  | 38 (Arm 11 × 2, Torso 16) |
| Lower body  | 42                        |
| Mobile base | 90                        |
| **Total**   | **170**                   |

---
### Joint Maximum Speed and Angle Range
| **Joint**                | **Speed** | **Range**                           |
| ------------------------ | --------- | ----------------------------------- |
| torso_0 (Ankle roll)     | 120°/s    | -15° ~ 15°                          |
| torso_1 (Ankle pitch)    | 120°/s    | -30° ~ 90°                          |
| torso_2 (Knee)           | 180°/s    | -150° ~ 90°                         |
| torso_3 (Hip pitch)      | 180°/s    | -45° ~ 90°                          |
| torso_4 (Hip roll)       | 180°/s    | -30° ~ 30°                          |
| torso_5 (Hip yaw)        | 180°/s    | -135° ~ 135°                        |
| *_arm_0 (Shoulder pitch) | 180°/s    | -180° ~ 180°                        |
| *_arm_1 (Shoulder roll)  | 180°/s    |  R : -180° ~ 0°  L : 0° ~ 180°      |
| *_arm_2 (Shoulder yaw)   | 180°/s    | -180° ~ 180°                        |
| *_arm_3 (Elbow pitch)    | 180°/s    | -150° ~ 0°                          |
| *_arm_4 (Wrist yaw1)     | 180°/s    | -180° ~ 180°                        |
| *_arm_5 (Wrist pitch)    | 180°/s    | -90° ~ 110°                         |
| *_arm_6 (Wrist yaw2)     | 180°/s    | -155° ~ 155°                        |
| head_0 (Pan)             | 180°/s    | -180° ~ 180°                          |
| head_1 (Tilt)            | 180°/s    | -180° ~ 180°                          |
