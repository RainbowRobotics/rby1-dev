# Visualization & Robot Description

## RB-Y1 Description

`rby1_description` holds a URDF per model and version (`urdf/rby1<model>/model_v<version>.urdf`), their meshes, and a launch file that shows one in RViz with a slider per joint.
The MoveIt packages build on these files; use them for anything of your own about the robot.

```bash
source install/setup.bash
ros2 launch rby1_description rby1_state_publisher.launch.py model:=a version:=1_1
ros2 launch rby1_description rby1_state_publisher.launch.py model:=m version:=1_3
```

| Launch argument | Default | Values |
|---|---|---|
| `model` | `a` | `a` (RB-Y1 A) or `m` (RB-Y1 M) |
| `version` | `1_0` | `1_0`, `1_1`, `1_2`, and `1_3` on `m` only. Write it with an underscore |
| `use_sim_time` | `false` | |

The launch starts `robot_state_publisher` with the URDF, `joint_state_publisher_gui` and RViz.
RViz opens with the robot model and its frames already set up (`rviz/robot.rviz`: RobotModel from `/robot_description`, TF, Fixed Frame `base`); you do not need to add displays.

Move the sliders in the joint state publisher GUI and the model follows:

<img :src="$withBase('/images/ros2/state_checker_guide_5.png')" alt="" class="center white-bg" style="width:100%">

## Frames and joints

- **Root link**: `base`, on the floor. On Model A, `base` is 0.228 m behind the wheel axle; on Model M it is on the axle.
- **Tool frames**: `ee_right` and `ee_left`, 0.125 m beyond `link_right_arm_6` / `link_left_arm_6`. `link_torso_5` carries the head and the arms.
- **Joints**, as the SDK names them: `torso_0` to `torso_5`, `right_arm_0` to `right_arm_6`, `left_arm_0` to `left_arm_6`, `head_0`, `head_1`, and the wheels.
- **Gripper**: up to v1.2 the URDFs end at the tool frames. The gripper model for TF and RViz comes from `rby1_tools` ([Tools](tools.md#gripper)). The M v1.3 URDF has the gripper in it (`gripper_finger_r1_joint`, `gripper_finger_l1_joint` and their mimic joints).
- **With the driver**: the driver publishes TF `odom → base_footprint` and the static `base_footprint → base`. To show the real robot, have `robot_state_publisher` read `/rby1/joint_overall_states` (remap `joint_states` to it) instead of the sliders.

Verified against: rby1-ros2 v1.0.0 `rby1_description/launch/rby1_state_publisher.launch.py`, `rby1_description/rviz/robot.rviz`, `Doc/manual/04_description.md`.
