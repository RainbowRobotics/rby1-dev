# Overview & Specifications

RB-Y1 comes in three models:

- **Model A**: two-wheel differential mobile base, 6-joint torso, two 7-joint arms and a 2-joint head.
- **Model M**: four-wheel mecanum mobile base, with the same torso, arms and head as Model A.
- **Model UB**: upper body only, with a 2-joint torso, two 7-joint arms and a 2-joint head. It has no mobile base.

Each model also has a hardware version (v1.0 to v1.3). To check the model and version of your robot, look at the bottom of the Web UI **Dashboard** page, or call `robot.get_robot_info()` in the SDK and read `robot_model_name` and `robot_model_version`.
The differences between hardware versions are listed in [Hardware Versions](../sdk/models/hardware-versions.md).

<img :src="$withBase('/images/hardware/overview/robot-joint-configuration.png')" alt="Joint configuration of RB-Y1 Model A" class="center white-bg" style="width:400px">

The figure shows Model A. The SDK joint names of every model are listed in [Joint Range and Speed Limits](#joint-range-and-speed-limits).

---
## Technical Specifications

### General Specifications

A dash (—) means that this manual does not list the value. Contact the support team for it. This manual does not list the size, weight, battery or power supply of Model UB.

| **Attribute** | **Model A** | **Model M** | **Model UB** |
| --- | --- | --- | --- |
| **Size (W x D x H)** | 600 x 690 x 1,400 mm | — | — |
| **Weight** | 131 kg | 170 kg | — |
| **Degrees of Freedom** | 24 DOF | 26 DOF | 18 DOF |
| **Battery** | 50 V, 25 Ah (1,250 Wh) | 50 V, 50 Ah (2,500 Wh) | — |
| **Mobile Base Speed** | 1.5 m/s | — | No mobile base |
| **Arm Payload** | 3 kg (per arm) | 3 kg (per arm) | — |
| **Arm Reach** | 600 mm (to wrist) + hand | 600 mm (to wrist) + hand | — |
| **Arm Repeatability** | < ±0.05 mm | < ±0.05 mm | — |
| **Power Supply Voltage** | 48 VDC | 48 VDC | — |
| **Ambient Operating Temperature** | Up to 40 °C | Up to 40 °C | — |
| **Exterior Materials** | Aluminum | Aluminum | — |
| **Joint Range and Speed Limits** | See [Joint Range and Speed Limits](#joint-range-and-speed-limits) | See [Joint Range and Speed Limits](#joint-range-and-speed-limits) | See [Joint Range and Speed Limits](#joint-range-and-speed-limits) |

The battery voltage is the marked voltage; the nominal voltage is 51.7 V. See [Battery](battery.md) for the battery packs.

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
| **Total** | **26 DOF**   |

#### Model UB DOF

| **Part**  | **# of DOF** |
| --------- | ------------ |
| Torso     | 2 DOF        |
| Arm       | 7 DOF × 2    |
| Head      | 2 DOF        |
| **Total** | **18 DOF**   |

The joint names and indexes in the SDK are listed on the model pages: [Model A](../sdk/models/generated/model_a.md), [Model M](../sdk/models/generated/model_m.md), [Model UB](../sdk/models/generated/model_ub.md).

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
The tables below are generated from the URDF files in rby1-sdk v0.10.1 (<a href="https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/models" target="_blank" rel="noopener noreferrer">`models/`</a>); use them, not the actuator ratings, when you plan trajectories.

<!--@include: generated/joint_limits_a.md-->

<!--@include: generated/joint_limits_m.md-->

<!--@include: generated/joint_limits_ub.md-->
