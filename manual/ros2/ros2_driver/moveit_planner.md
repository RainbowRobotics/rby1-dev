# MoveIt Planner

`rby1_moveit_executor` is a planner that takes tool pose targets on a topic, plans with MoveIt 2 (OMPL) around the planning scene,
and runs the trajectory through the driver's `follow_joint_trajectory`. It does not use `ros2_control`.
`rby1_moveit_objects` puts obstacles and modules (gripper, sensors, tools) into the planning scene.

| | `demo.launch.py` ([MoveIt 2](rby1_moveit2.md)) | `rby1_moveit_executor` (this page) |
|---|---|---|
| Starts | `move_group`, RViz, `ros2_control` with the [hardware plugin](hardware_interface.md) | `move_group`, RViz, the executor node, a joint state relay |
| Moves the robot through | `ros2_control` controllers | the driver's `follow_joint_trajectory` |
| Driven by | the RViz MotionPlanning panel | tool pose targets on a topic |
| Package | one per model and version | one; picks the configuration from the driver's model and version |

Only one `move_group` can run per ROS domain, so the two do not run together.

## Executor (`rby1_moveit_executor`)

::: danger The executor moves the robot at start and runs every plan at once
- At start it switches power and servos on and moves every straight part to the **ready pose** in one move. A straight part is an arm whose elbow (`right_arm_3`, `left_arm_3`) is within 0.3 rad of 0, or a torso whose knee (`torso_2`) is under half its ready angle.
- It runs each plan as soon as it is made, without a preview. OMPL can still find a roundabout path.
- MoveIt checks only what is in its planning scene. Without the gripper in the scene, it plans as if the hand ended at the tool frame.

Try new targets in the simulator first, keep `velocity_scaling` low on the robot, watch the planned path in its RViz, and keep the E-Stop within reach.
:::

```bash
ros2 launch rby1_driver rby1_ros2_driver.launch.py                      # terminal 1: the driver
ros2 launch rby1_moveit_executor moveit_executor.launch.py              # terminal 2: with RViz; rviz:=false without
```

- **Robot**: model and version are read from the driver and pick `rby1_moveit_<model>_<version>`. `model:=m version:=1.2` names it; write `version:=1.3` for an M v1.3.
- **Start**: it checks for an E-Stop and faults, switches power and servos on, and moves a straight part to the ready pose (`config/ready_pose.yaml`), then answers `READY`.
  A part already bent is left as it is. To skip the move, copy `config/ready_pose.yaml`, add `ready_if_straight: false` under `rby1_target_executor:` `ros__parameters:`, and start with `ready_pose:=/path/to/that.yaml`.
  There is no `ready_if_straight` launch argument, and `ros2 param set` after start has no effect on it. With `rby1_bringup`, put the same file in `moveit_executor.ready_pose` of `bringup.yaml`.
- **Both arms**: a target for one arm moves that arm and leaves the other where it is. Targets for both arms within 0.1 s of each other are planned as one move.
  A target that arrives during a move is kept (the latest per arm) and planned when the move ends.
- **Obstacles**: the planning scene is checked when a target is planned; nothing is checked while the arm moves.
- **Streams**: it opens the `right_arm, left_arm` stream channels for a move and closes them afterwards.

| Launch argument | Default | Description |
|-----------------|---------|-------------|
| `rviz` | `true` | RViz with the MotionPlanning display |
| `velocity_scaling` | `0.5` | Share of the joint velocity limits MoveIt times the path with |
| `minimum_time` | `2.0` | Shortest move (s) |
| `impedance` | `false` | Follow trajectories in joint impedance (sent to the driver's `set_trajectory_impedance` before the move) |
| `ready_pose` | `config/ready_pose.yaml` | The ready pose file |
| `model`, `version` | from the driver | Robot model and version |
| `driver_namespace` | `rby1` | Namespace of the driver |
| `target_namespace` | `rby1` | Namespace of the target topics |

Other node parameters can be changed while it runs: `ros2 param set /rby1_target_executor <name> <value>`
(for example `planning_time`, `planning_attempts`, `acceleration_scaling`, `duration`).

### Target interface

| Name | Type | Content |
|------|------|---------|
| `/rby1/<arm>/target_pose` | `std_msgs/Float64MultiArray` | 16 values: the row-major 4×4 pose of the tool frame (`ee_right`, `ee_left`) in `base`. `<arm>` is `right_arm` or `left_arm` |
| `/rby1/<arm>/target_status` | `std_msgs/String` | `READY`, `PLANNING`, `EXECUTING ...`, `DONE`, `FAILED: <reason and what to do>` |

Example `16_target_shuttle_publisher` sends targets on this interface ([Examples](examples.md#target-examples-15-16)).
Only one executor may listen on an arm's `target_pose` at a time.

Topic names before October 2026, for programs written against them: `/rby1/target_pose` and `/rby1/target_status` (now one pair per arm),
package `rby1_moveit_scene` (merged into `rby1_moveit_objects`), example `16_target_shuttle` (now `16_target_shuttle_publisher`).

## Planning scene (`rby1_moveit_objects`)

These tools put objects into the planning scene of a `move_group` on the same ROS domain. They work with either `demo.launch.py` or the executor.

| Tool | Started with | What it does |
|------|--------------|--------------|
| `scene` | `ros2 run rby1_moveit_objects scene ...`, `scene.launch.py` | Obstacles (box, sphere, cylinder): add, move, remove, list, load a file. Poses are in `base` |
| `publish_objects` | `objects.launch.py` | Modules on robot links and fixtures in the world, from a YAML file |
| `object_at_point` | `point_object.launch.py` | One obstacle kept where `/rby1/scene/object_point` (or a pose topic such as a marker's) says |

```bash
ros2 run rby1_moveit_objects scene add box table --xyz 0.7 0.0 0.35 --size 0.6 1.2 0.7
ros2 run rby1_moveit_objects scene add sphere ball --xyz 0.45 0.35 1.0 --radius 0.06
ros2 run rby1_moveit_objects scene list
ros2 run rby1_moveit_objects scene remove ball
ros2 run rby1_moveit_objects scene clear
ros2 launch rby1_moveit_objects scene.launch.py config:=/path/to/my_scene.yaml

ros2 launch rby1_moveit_objects objects.launch.py config:=rby1_tools/model/rby1_gripper/gripper.yaml   # the gripper on both hands
ros2 launch rby1_moveit_objects point_object.launch.py pose_topic:=/rby1/marker_7/pose
```

An obstacle file:

```yaml
objects:
  - name: table                # unique name in the scene
    type: box                  # box (size) / sphere (radius) / cylinder (radius, height; along z)
    xyz: [0.7, 0.0, 0.35]      # centre (m)
    size: [0.6, 1.2, 0.7]
    rpy: [0.0, 0.0, 0.0]       # (rad), default 0
    frame: base                # default base
```

- An object attached to the robot that overlaps robot links (a tool through the gripper) needs those links in its `touch_links`.
  Without them MoveIt sees the present pose as a collision and refuses every target (`FAILURE (MoveIt error 99999)`).
- On an M v1.3 the URDF already has the gripper; `objects.launch.py` refuses the gripper file there.

## Step by step

In the simulator first. Each step runs in its own terminal with `source install/setup.bash`, the driver running.

1. Start the planner. **The robot moves to the ready pose**, then the status is `READY`.
   ```bash
   ros2 launch rby1_moveit_executor moveit_executor.launch.py
   ros2 launch rby1_tools gripper.launch.py scene:=true      # optional: the gripper in the scene and on TF
   ```
2. Send targets. Example 16 sends two targets near the ready pose in turn; the planner answers `PLANNING`, `EXECUTING ...`, `DONE`.
   ```bash
   ros2 topic echo /rby1/right_arm/target_status std_msgs/msg/String
   ros2 run rby1_examples 16_target_shuttle_publisher
   ```
3. Put an obstacle where the hand passes. The next legs are planned around it; remove it and they are straight again. A way around takes longer: use `period:=8.0` or more.
   ```bash
   ros2 run rby1_examples 16_target_shuttle_publisher --ros-args -p period:=10.0 \
       -p "point_a:=[0.413,-0.367,1.034,-1.571,-1.071,1.571]" -p "point_b:=[0.413,-0.167,1.134,-1.571,-1.071,1.571]"
   ros2 run rby1_moveit_objects scene add box shuttle_box --xyz 0.515 -0.23 1.17 --size 0.06 0.06 0.06
   ros2 run rby1_moveit_objects scene remove shuttle_box
   ```

Verified against: rby1-ros2 v1.0.0 `rby1_moveit/rby1_moveit_executor/launch/moveit_executor.launch.py`, `rby1_moveit/rby1_moveit_executor/config/ready_pose.yaml`, `rby1_moveit/rby1_moveit_objects/`, `Doc/manual/06_moveit.md`.
