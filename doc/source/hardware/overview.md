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
### Joint Range and Speed Limits

The controller enforces the joint range and speed limits of the robot model (URDF).
The tables below are generated from the URDF files in rby1-sdk; use them, not the actuator ratings, when you plan trajectories.
Check your robot's model and version in the Web UI or with `robot.get_robot_info()`.

```{include} generated/joint_limits.md
```
