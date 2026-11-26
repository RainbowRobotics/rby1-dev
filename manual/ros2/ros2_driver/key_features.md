# Key Features

## Robot Control
- **Joint Position Control**: Command each body part (torso, right arm, left arm, head) to target joint angles (rad) with the `robot_joint` action. All parts can be commanded in one goal.
- **Cartesian Position Control**: Command the pose of a tool frame (for example `ee_right`) in a reference link with the `robot_cartesian` action. The pose is a `geometry_msgs/Transform` (translation and quaternion), see [Custom Message Types](custom_message_types.md).
- **Impedance Control**: Joint and Cartesian commands both support impedance control with configurable stiffness and damping.
- **Gravity Compensation**: Makes the torso and arms back-drivable for direct teaching; the robot compensates gravity while it is on.
- **Trajectories**: Send a pre-computed `JointTrajectory` (multi-waypoint) with the standard `follow_joint_trajectory` action. It runs over the [command streams](command_streams.md).
- **Mobile Base + Upper Body Simultaneous Control**: While `cmd_vel` drives the base, the `robot_joint` action can move the arms and head. Set `priority = 1` on the upper-body goal to match the mobile base's default priority (example `12_mobile_base_control`).

## Safety & Fault Management
- Motion commands are rejected if the Control Manager is not in `ENABLE` or `EXECUTING` state.
- A minor fault during a command is reset by the driver and control resumes. A major fault needs `control_manager_command` `CMD_RESET`.
- The driver stops when it cannot read the robot state for 1 s.
- At shutdown, on `cancel_control` and on servo off, the driver cancels the running control, closes its streams and disables the Control Manager.

### Predictive Collision Checking
The driver checks the **target pose** for collisions *before* it executes a `robot_joint` or `robot_cartesian` command:
- **Joint commands**: the SDK's dynamics model (from the URDF) evaluates the target joint configuration for link collisions.
- **Cartesian commands**: the driver solves the inverse kinematics with its own IK to get joint angles, then evaluates them. If the IK does not converge, the check is skipped with a warning.
- If the predicted configuration is in collision (minimum link distance below `collision_threshold`), the driver logs `[PREDICTIVE COLLISION WARNING]` and **still executes the command**. It does not abort or reject it.
- The same applies while the robot moves: the driver sets `robot_state.collision` and logs `Collision detected!`, but it does not stop the robot. Stopping is the job of your application (see example `14_collision_safety_control`).
- The measured link distances are checked in every state cycle, at the fixed state rate of 100 Hz.

::: warning
The collision check only warns. It does not stop the robot and it does not see objects outside the robot model.
Keep the E-Stop within reach when you command poses near the robot's own body.
:::
