# Units and Frames

The SDK, the robot state and all commands use SI units and radians. This page lists the units, the joint order of each model,
the base frame and the link names you use in Cartesian commands.

## Units

| Quantity | Unit | Where you meet it |
| --- | --- | --- |
| Joint position | rad | `RobotState.position`, `JointPositionCommandBuilder.set_position()` |
| Joint velocity | rad/s | `RobotState.velocity`, `JointVelocityCommandBuilder.set_velocity()`, velocity limits |
| Joint acceleration | rad/s² | acceleration limits |
| Joint torque | N·m | `RobotState.torque`, feedforward torque, torque limits |
| Motor current | A | `RobotState.current` |
| Joint stiffness | N·m/rad | joint impedance commands |
| Cartesian position | m | the translation part of a pose |
| Cartesian stiffness | N/m (translation), N·m/rad (rotation) | impedance commands |
| Linear velocity / acceleration | m/s, m/s² | Cartesian and SE2 velocity limits |
| Angular velocity / acceleration | rad/s, rad/s² | Cartesian and SE2 velocity limits |
| Pose | 4×4 homogeneous transform (rotation and translation in m), `numpy.ndarray` of shape (4, 4) | `CartesianCommandBuilder.add_target()` |
| Base velocity (SE2) | `[vx, vy]` in m/s and `wz` in rad/s | `SE2VelocityCommandBuilder.set_velocity(linear, angular)` |
| Odometry | 3×3 SE(2) transform (x, y in m, yaw) | `RobotState.odometry`, `reset_odometry(angle, position)` |
| Time | s | minimum time, control hold time, timeouts |
| Gravity | m/s² | parameter `gravity` |
| Temperature | °C | `RobotState.temperature` |
| Battery | V, A, % | `RobotState.battery_state` |

The [hardware tables](../hardware/overview.md) give joint ranges in degrees (°) and speeds in °/s, because they are easier to read.
Convert them before you use them in the SDK: `numpy.deg2rad(90)` = 1.5708 rad. The SDK examples use `D2R = np.pi / 180`.

The control period of the robot software is 2 ms (`robot.model().control_period` = 0.002 s).

## Joint order

Every per-joint array (state, targets, limits) has one entry per joint, in this order. Indexes start at 0.

| Index | Model A (24) | Model M (26) | Model UB (18) |
| --- | --- | --- | --- |
| Wheels | 0 `right_wheel`, 1 `left_wheel` | 0 `wheel_fr`, 1 `wheel_fl`, 2 `wheel_rr`, 3 `wheel_rl` | none |
| Torso | 2 – 7: `torso_0` … `torso_5` | 4 – 9: `torso_0` … `torso_5` | 0 `torso_hp`, 1 `torso_5` |
| Right arm | 8 – 14: `right_arm_0` … `right_arm_6` | 10 – 16: `right_arm_0` … `right_arm_6` | 2 – 8: `right_arm_0` … `right_arm_6` |
| Left arm | 15 – 21: `left_arm_0` … `left_arm_6` | 17 – 23: `left_arm_0` … `left_arm_6` | 9 – 15: `left_arm_0` … `left_arm_6` |
| Head | 22 `head_0`, 23 `head_1` | 24 `head_0`, 25 `head_1` | 16 `head_0`, 17 `head_1` |

Do not hard-code these numbers. Read them from the model:

```python
model = robot.model()           # or rby1_sdk.Model_A(), Model_M(), Model_UB()
print(model.robot_joint_names)  # names in index order
print(model.torso_idx, model.right_arm_idx, model.left_arm_idx, model.head_idx, model.mobility_idx)
```

A body command (`BodyCommandBuilder`) takes the joints of `model.body_idx` in this order: torso, right arm, left arm.
An arm or torso command takes only the joints of that part.

## Base frame

All models have a root link named **`base`**. Its axes are:

- **x**: forward
- **y**: left
- **z**: up

So the right wheel and the right arm are on the negative y side. Gravity in this frame is `[0, 0, -9.8]` (parameter `gravity`).
`RobotState.center_of_mass` is given in the `base` frame.

## Link names

Use these names as `ref_link_name` and `link_name` in Cartesian, impedance and optimal control commands.

| Link | Model A | Model M | Model UB | Use |
| --- | :-: | :-: | :-: | --- |
| `base` | ✓ | ✓ | ✓ | Root of the robot; the usual reference frame |
| `link_torso_5` | ✓ | ✓ | ✓ | Top of the torso; target link for torso commands |
| `link_torso_0` … `link_torso_4` | ✓ | ✓ | | Torso links |
| `link_torso_hp` | | | ✓ | Torso link of Model UB |
| `link_right_arm_0` … `link_right_arm_6`, `link_left_arm_0` … `link_left_arm_6` | ✓ | ✓ | ✓ | Arm links |
| `ee_right`, `ee_left` | ✓ | ✓ | ✓ | End effectors of the right and left arm (after `link_right_arm_6` / `link_left_arm_6`) |
| `link_head_0` … `link_head_2` | ✓ | ✓ | ✓ | Head links |
| `wheel_r`, `wheel_l` | ✓ | | | Wheel links of Model A |
| `wheel_fr_link`, `wheel_fl_link`, `wheel_rr_link`, `wheel_rl_link` | | ✓ | | Wheel links of Model M |

The URDF of your hardware version has the full list (see [Hardware Versions](../sdk/models/hardware-versions.md)).
Example: move the right hand relative to the base. The call is the same as in the SDK example `24_demo_motion.py`; the values are different.

```python
import numpy as np
import rby1_sdk as rby

T = np.eye(4)                    # target pose of ee_right in the base frame
T[:3, 3] = [0.5, -0.3, 1.0]      # x forward, y left, z up, in meters

cmd = rby.CartesianCommandBuilder().add_target(
    "base", "ee_right", T,
    1.0,          # linear velocity limit [m/s]
    np.pi,        # angular velocity limit [rad/s]
    1.0,          # acceleration limit scaling (no unit)
)
```

This only builds a command; send it in a [command](../sdk/controllers/generated/command_and_control_architecture.md#example)
to move the robot. Check that the target is reachable and the path is clear before you send it.

## Kinematics and dynamics

`robot.get_dynamics()` returns the dynamics model of the robot, loaded from the URDF stored on the robot. It uses the same joint names,
link names and units as above: forward kinematics returns 4×4 transforms in m, and gravity terms are in N·m.
See the [Python API](../sdk/python/index.md) and the SDK example `19_dynamics_robot.py`.

---

Verified against: rby1-sdk v0.10.1 `include/rby1-sdk/model.h` (joint order, indexes, `kControlPeriod`), `include/rby1-sdk/robot_state.h`
(unit comments), `python/robot_command_builder.cpp` (units in the builder docs: `add_target`, `set_velocity`, stiffness, torque limit),
`python/model.cpp`, `include/rby1-sdk/robot.h` (`ResetOdometry`, `GetDynamics`), `models/rby1a/urdf/model_v1.2.urdf`,
`models/rby1m/urdf/model_v1.3.urdf`, `models/rby1ub/urdf/model.urdf` (link names; wheel and arm positions give the axis directions),
`examples/python/24_demo_motion.py`; robot core `core/robots/rby1a/parameters.h` (`gravity`).
