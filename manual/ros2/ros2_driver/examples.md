# Examples

Python scripts in `rby1_examples`, one per feature of the driver. Run each in a **separate terminal** while the driver is running:

```bash
source install/setup.bash
ros2 run rby1_examples <example_name>
```

::: danger Most examples move the robot
**Try every example in the simulator first** ([MuJoCo](../../simulators/mujoco.md)). On a real robot:
- Keep the E-Stop within reach of the person running the example.
- Clear the reach of both arms and the torso. For `12_mobile_base_control` and `13_stream_command`, also clear the driving path around the base.
- Many control examples switch power and servos on by themselves before they move.
- The "Moves the robot" column below says what each example moves.
:::

The values an example uses (postures, times, speeds) are constants in one block at the top of its file, under the imports.
Examples 15 and 16 take theirs as ROS parameters.

| Example | Description | Moves the robot |
|---------|-------------|-----------------|
| `01_power_control` | Power on, servo on, servo off, power off | Power and servos only |
| `02_robot_status_monitor` | Prints the robot state until Ctrl+C: Control Manager, brakes, battery, tool flanges, E-Stop | No |
| `03_tool_flange_monitoring` | Prints the tool flanges: status from `robot_state`, IMU and wrench topics (needs `publish_tool_flange_state: true`) | No |
| `04_joint_state_monitoring` | Prints the joint positions per part (`joint_states`) | No |
| `05_gravity_compensation` | Gravity compensation on for the torso and both arms, 10 s for direct teaching, then off | Yes: the parts become back-drivable |
| `06_zero_pose` | Every joint to 0 rad in one goal (`robot_joint`) | Yes: whole body |
| `07_joint_command` | Zero pose, then a target pose with one control mode per part: joint impedance for the right arm, joint position for the left arm and the head, joint group position for three torso joints (`use_group_joint`) | Yes: whole body |
| `08_cartesian_command` | Ready pose, then a Cartesian target per arm: Cartesian position (right), Cartesian impedance (left) | Yes: whole body |
| `09_multi_controls` | Joint and Cartesian control of different parts at once | Yes: whole body |
| `10_trajectory_joint_command` | A pre-computed whole-body trajectory through `follow_joint_trajectory`, in position control and again in joint impedance (`stream_control`, `set_trajectory_impedance`) | Yes: whole body |
| `11_cancel_control` | An action cancel, then the `cancel_control` service | Yes: whole body |
| `12_mobile_base_control` | Opens the stream channels, drives the base with `cmd_vel` (forward, back, turn, sideways) while it moves the arms and head, then closes the channels | Yes: **the base drives**, arms and head |
| `13_stream_command` | Opens every stream channel, streams zero and ready poses of the torso, arms and head (`stream_joint`), and at the same time drives the base forward and back at 0.15 m/s with `cmd_vel` | Yes: whole body, **the base drives** |
| `14_collision_safety_control` | Records the pose, moves, and when `robot_state.collision` is set, cancels the goal and sends a goal back to the recorded pose. The client handles the collision; the driver does not stop the robot | Yes: whole body |
| `15_cartesian_target_move` | Moves the hand to each target received on `/rby1/right_arm/target_pose`, with the driver alone: no planner, **no collision check**. Answers on `/rby1/right_arm/target_status` | Yes: the arm |
| `16_target_shuttle_publisher` | Publishes two hand poses in turn on that target topic, for example 15 or the [MoveIt planner](moveit_planner.md) to carry out | Only through the node that executes the targets |

In the simulator, battery, force/torque and IMU values read 0.
Example 10's first trajectory ends with `error_code -1`: the second trajectory on the same parts replaces it on purpose.

## Two ways to stop a command

Example `11_cancel_control` shows both:

1. **Action cancel** cancels only the current goal. Stream channels stay open, so the next command goes out at once.
2. **`cancel_control` service** stops every command at once **and closes every stream channel**.
   After it, open the channels again (`/rby1/stream_control`) before you send `cmd_vel` or stream commands.

Sequential Python clients should spin while they wait (`rclpy.spin_once` in a loop, as `13_stream_command` does) instead of `time.sleep()`.
See [Troubleshooting](troubleshooting_and_known_issues.md#issue-client-side-warnings-ignoring-unexpected-goalresult-response).

## Target examples (15, 16)

Run them together, one terminal each, with `source install/setup.bash` in every terminal.
Before example 15 starts, the robot must be powered, its servos on and the right arm bent (for example, the ready pose of `08_cartesian_command`).

```bash
ros2 launch rby1_driver rby1_ros2_driver.launch.py                            # terminal 1: the driver
ros2 run rby1_examples 15_cartesian_target_move                              # terminal 2: moves the hand
ros2 run rby1_examples 16_target_shuttle_publisher                           # terminal 3: sends two targets in turn
ros2 topic echo /rby1/right_arm/target_status std_msgs/msg/String            # terminal 4 (optional): the answers
```

- A target is one `std_msgs/Float64MultiArray` of 16 values: the row-major 4×4 pose of the tool frame (`ee_right`, `ee_left`) in `base`.
- `15_cartesian_target_move --ros-args -p mode:=stream` streams small steps (up to 0.10 m/s) instead of one `robot_cartesian` goal per target.
- Only one executor may serve an arm. Example 15 refuses to start when `target_topic` already has a subscriber (for example the MoveIt planner). Stop a planner launch before you start example 15.
- Stop with Ctrl+C in terminal 3, then terminal 2.

::: warning
Example 15 checks nothing for collisions. A target in or behind an obstacle, or close to the robot's body, is driven straight to.
Use the [MoveIt planner](moveit_planner.md) to go around obstacles.
:::

Verified against: rby1-ros2 v1.0.0 `rby1_examples/setup.py`, `rby1_examples/rby1_examples/*.py` (docstrings), `Doc/manual/03_examples.md`.
