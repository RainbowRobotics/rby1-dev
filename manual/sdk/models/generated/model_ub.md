# Model UB
##

Model UB is the upper-body configuration of RB-Y1: a two-joint torso, two 7-DoF arms and a 2-DoF head, without a mobile base.

::: info Note
The most accurate information about the model is in the
<a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1ub/urdf/model.urdf"
target="_blank" rel="noopener noreferrer">URDF file (`models/rby1ub/urdf/model.urdf`)</a>
and in `rb::y1_model::UB` (`include/rby1-sdk/model.h`) of the rby1-sdk repository.
:::

<img :src="$withBase('/images/model/model_ub/model_ub.png')" alt="Model UB" class="center" style="width:400px">

---
### Using the model in the SDK

- Python: `rby1_sdk.create_robot(address, "ub")` returns `Robot_UB`; the model descriptor is `rby1_sdk.Model_UB`.
- C++: `rb::Robot<rb::y1_model::UB>`.
- Robot parameter `robot_model_name`: `"rby1ub"`.

---
### Degrees of Freedom (DOF)

- Total DOF: 18 (torso 2, right arm 7, left arm 7, head 2). There are no wheels.

---
### Joint Names and Indexes

| Part | Joint names | Indexes |
| ---- | ----------- | ------- |
| Torso | `torso_hp`, `torso_5` | 0, 1 |
| Right arm | `right_arm_0` … `right_arm_6` | 2 – 8 |
| Left arm | `left_arm_0` … `left_arm_6` | 9 – 15 |
| Head | `head_0`, `head_1` | 16, 17 |

- Body indexes (torso and both arms): 0 – 15
- Mobility indexes: none

---
### Joint Range and Speed Limits

<!--@include: ../../../hardware/generated/joint_limits_ub.md-->

---
### Parameters

Model UB uses the common robot parameters; see the [Parameter Reference](/sdk/controllers/generated/parameter).
Read the parameters and their current values from your robot with `robot.get_parameter_list()`.

<!-- TODO (owner): brake / brake-release button and motor type per joint for Model UB (not verified from the SDK or core). -->
