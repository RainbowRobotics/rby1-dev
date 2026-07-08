# Key Features

## Robot Control
- **Joint Position Control**: Command each body part (Torso, Right/Left Arm, Head) to target joint angles (rad) via the `robot_joint` action. All parts can be commanded simultaneously in one goal.
- **Cartesian Position Control**: Command end-effector pose as a 4×4 SE3 transform via the `robot_cartesian` action.
- **Impedance Control**: Both joint and Cartesian modes support impedance control with configurable stiffness and damping.
- **Gravity Compensation**: Enables back-drivable joints for direct teaching; the driver continuously compensates gravity.
- **Trajectory Streaming**: Send a pre-computed `JointTrajectory` (multi-waypoint) via the standard `follow_joint_trajectory` action.
- **Mobile Base + Upper Body Simultaneous Control**: While driving the base via `cmd_vel`, you can also command the arms/head via the `robot_joint` action at the same time. Set `priority = 1` on upper-body goals to match the mobile base's default priority.

## Safety & Fault Management
- Motion commands are rejected if the Control Manager is not in `ENABLE` or `EXECUTING` state.
- Minor faults encountered during execution are automatically reset and control is resumed.

### Predictive Collision Checking
The driver checks the **target pose** for collisions *before* executing any joint or Cartesian command:
- **Joint commands**: uses the URDF-based dynamics model to evaluate the target joint configuration for link collisions.
- **Cartesian commands**: solves the Inverse Kinematics via the built-in optimal control solver to obtain joint angles, then evaluates those angles for collisions.
- If the predicted configuration is in collision (minimum distance below the threshold), the driver prints a warning log (`RCLCPP_WARN`) rather than aborting or rejecting the command, allowing safer manual intervention.
- ⚠️ This check runs at the same rate as `get_state_period`. A slow period means the check fires less frequently.
