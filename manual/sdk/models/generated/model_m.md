# Model M

Model M is RB-Y1 with a mecanum-wheel mobile base (four wheels), a six-joint torso, two 7-DoF arms and a 2-DoF head.

::: info Note
The most accurate information about the model is in the URDF file of your hardware version in the rby1-sdk repository
(for example <a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1m/urdf/model_v1.3.urdf"
target="_blank" rel="noopener noreferrer">`models/rby1m/urdf/model_v1.3.urdf`</a>) and in `rb::y1_model::M` (`include/rby1-sdk/model.h`).
See [Hardware Versions](../hardware-versions.md) for the file of each version.
:::

<img :src="$withBase('/images/model/model_m/model_m.png')" alt="Model M" class="center white-bg" style="width:400px">

<img :src="$withBase('/images/model/model_m/mecanum_wheel.png')" alt="Mecanum Wheel" class="center white-bg" style="width:400px">

---
### Using the model in the SDK

- Python: `rby1_sdk.create_robot(address, "m")` returns `Robot_M`; the model descriptor is `rby1_sdk.Model_M`.
- C++: `rb::Robot<rb::y1_model::M>`.
- Robot parameter `robot_model_name`: `"rby1m"`.

---
### Degrees of Freedom (DOF)

- Total DOF: 26 (wheels 4, torso 6, right arm 7, left arm 7, head 2).

---
### Joint Names and Indexes

| Part | Joint names | Indexes |
| ---- | ----------- | ------- |
| Wheels | `wheel_fr` (front right), `wheel_fl` (front left), `wheel_rr` (rear right), `wheel_rl` (rear left) | 0 – 3 |
| Torso | `torso_0` … `torso_5` | 4 – 9 |
| Right arm | `right_arm_0` … `right_arm_6` | 10 – 16 |
| Left arm | `left_arm_0` … `left_arm_6` | 17 – 23 |
| Head | `head_0`, `head_1` | 24, 25 |

- Mobility indexes: 0 – 3
- Body indexes (torso and both arms): 4 – 23
- Head indexes: 24, 25

The torso joints are numbered from bottom to top, the arm joints from shoulder to wrist.

---
### Joint Range and Speed Limits

Model M, hardware versions v1.0, v1.1, v1.2 and v1.3:

<!--@include: ../../../hardware/generated/joint_limits_m.md{5,}-->

---
### Brake and Motor Information

#### Components Without Brakes

- **Wheels**: `wheel_fr`, `wheel_fl`, `wheel_rr`, `wheel_rl`
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

Model M uses the common robot parameters; see the [Parameter Reference](../../controllers/generated/parameter.md).
Read the parameters and their current values from your robot with `robot.get_parameter_list()` and `robot.get_parameter(name)`.

---

Verified against: rby1-sdk v0.10.1 `include/rby1-sdk/model.h` (`M`: joint names, indexes), `python/rby1_sdk/__init__.py` (`create_robot`),
`python/model.cpp` (`Model_M`), `models/rby1m/urdf/model_v1.0.urdf` … `model_v1.3.urdf` (wheel positions front/rear, right/left);
robot core `core/robots/rby1m/parameters.h` (`robot_model_name`), `core/robots/rby1m/robot_hardware.cpp` (head brakes for `ROBOT_MODEL_V1_2`/`V1_3`).
