# Model A

Model A is RB-Y1 with a differential-drive mobile base (two wheels), a six-joint torso, two 7-DoF arms and a 2-DoF head.

::: info Note
The most accurate information about the model is in the URDF file of your hardware version in the rby1-sdk repository
(for example <a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1a/urdf/model_v1.2.urdf"
target="_blank" rel="noopener noreferrer">`models/rby1a/urdf/model_v1.2.urdf`</a>) and in `rb::y1_model::A` (`include/rby1-sdk/model.h`).
See [Hardware Versions](../hardware-versions.md) for the file of each version.
:::

<img :src="$withBase('/images/model/model_a/model_a.png')" alt="Model A" class="center white-bg" style="width:400px">

---
### Using the model in the SDK

- Python: `rby1_sdk.create_robot(address, "a")` returns `Robot_A`; the model descriptor is `rby1_sdk.Model_A`.
- C++: `rb::Robot<rb::y1_model::A>`.
- Robot parameter `robot_model_name`: `"rby1a"`.

---
### Degrees of Freedom (DOF)

- Total DOF: 24 (wheels 2, torso 6, right arm 7, left arm 7, head 2).

---
### Joint Names and Indexes

| Part | Joint names | Indexes |
| ---- | ----------- | ------- |
| Wheels | `right_wheel`, `left_wheel` | 0, 1 |
| Torso | `torso_0` … `torso_5` | 2 – 7 |
| Right arm | `right_arm_0` … `right_arm_6` | 8 – 14 |
| Left arm | `left_arm_0` … `left_arm_6` | 15 – 21 |
| Head | `head_0`, `head_1` | 22, 23 |

- Mobility indexes: 0, 1
- Body indexes (torso and both arms): 2 – 21
- Head indexes: 22, 23

The torso joints are numbered from bottom to top, the arm joints from shoulder to wrist.

---
### Joint Range and Speed Limits

Model A, hardware versions v1.0, v1.1 and v1.2:

<!--@include: ../../../hardware/generated/joint_limits_a.md{5,}-->

---
### Brake and Motor Information

#### Components Without Brakes

- **Wheels**: `right_wheel`, `left_wheel`
- **Right Arm**: `right_arm_6`
- **Left Arm**: `left_arm_6`
- **Head** (v1.0 and v1.1): `head_0`, `head_1`. From v1.2 the head joints have brakes (see [Hardware Versions](../hardware-versions.md)).

#### Components Without Physical Brake Buttons

The following components have brakes but do not have physical buttons for releasing them (can only be released electronically):

- **Torso**: `torso_3`, `torso_4`, `torso_5`
- **Right Arm**: `right_arm_4`, `right_arm_5`
- **Left Arm**: `left_arm_4`, `left_arm_5`

#### Components With Physical Brake Buttons

The following components have brakes and include physical buttons for releasing them:

- **Torso**: `torso_0`, `torso_1`, `torso_2`
- **Right Arm**: `right_arm_0`, `right_arm_1`, `right_arm_2`, `right_arm_3`
- **Left Arm**: `left_arm_0`, `left_arm_1`, `left_arm_2`, `left_arm_3`

::: danger
A joint whose brake is released can fall under gravity. Support the arm or the torso before you release a brake,
by button or in software.
:::

---
### Parameters

Model A uses the common robot parameters; see the [Parameter Reference](../../controllers/generated/parameter.md).
Read the parameters and their current values from your robot with `robot.get_parameter_list()` and `robot.get_parameter(name)`.

---

Verified against: rby1-sdk v0.10.1 `include/rby1-sdk/model.h` (`A`: joint names, indexes), `python/rby1_sdk/__init__.py` (`create_robot`),
`python/model.cpp` (`Model_A`), `models/rby1a/urdf/model_v1.0.urdf` … `model_v1.2.urdf`; robot core `core/robots/rby1a/parameters.h`
(`robot_model_name`), `core/robots/rby1a/robot_hardware.cpp` (head brakes for `ROBOT_MODEL_V1_2`).
