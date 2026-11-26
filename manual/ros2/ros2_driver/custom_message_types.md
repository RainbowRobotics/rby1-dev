# Custom Message Types

## `rby1_msgs/JointCommand` (used inside `Rby1JointCommand` goals and stream commands)

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `joint_names` | `string[]` | — | Optional joint name list |
| `position` | `float64[]` | — | Target joint positions (rad) |
| `use_impedance` | `bool` | `false` | Use joint impedance instead of position control |
| `use_group_joint` | `bool` | `false` | Enable group joint movement logic if True |
| `minimum_time` | `float64` | `2.0` | Minimum execution time (s) |
| `control_hold_time` | `float64` | `0.1` | Duration to hold position control after reaching target (s) |
| `velocity_limit` | `float64` | `4.7` | Joint velocity limit (rad/s) |
| `acceleration_limit` | `float64` | `1.0` | Acceleration scaling |
| `stiffness` | `float64[]` | — | Impedance stiffness coefficients |
| `damping_ratio` | `float64` | `1.0` | Impedance damping ratio |
| `torque_limit` | `float64` | `10.0` | Impedance torque safety limit (N·m) |

## `rby1_msgs/CartesianCommand` (used inside `Rby1CartesianCommand` goals and stream commands)

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `transform` | `geometry_msgs/Transform` | — | Target Cartesian transformation (pose) command |
| `ref_link` | `string` | — | Reference coordinate frame link name |
| `target_link` | `string` | — | Target coordinate frame link name (e.g. tool flange or end effector link) |
| `use_impedance` | `bool` | `false` | Use Cartesian impedance instead of position control |
| `minimum_time` | `float64` | `2.0` | Minimum execution time (s) |
| `control_hold_time` | `float64` | `0.1` | Duration to hold position control after reaching target (s) |
| `linear_velocity_limit` | `float64` | `1.5` | Limit for linear velocity of the end-effector (m/s) |
| `angular_velocity_limit` | `float64` | `4.7` | Limit for angular velocity of the end-effector (rad/s) |
| `acceleration_limit_scaling` | `float64` | `1.0` | Scaling factor for acceleration limits `[0.0, 1.0]` |
| `translation_weight` | `float64[]` | — | Weights for linear translation degrees of freedom `[x, y, z]` during QP optimization |
| `rotation_weight` | `float64[]` | — | Weights for rotation degrees of freedom during QP optimization |
| `add_joint_position_target` | `bool` | `false` | Flag to specify an additional single joint target along with the Cartesian pose |
| `add_joint_name` | `string` | — | Name of the additional joint to move |
| `add_joint_value` | `float64` | — | Target position value for the additional joint (rad or meters) |

## `rby1_msgs/StreamJointCommand`

| Field | Type | Description |
|-------|------|-------------|
| `torso` | `rby1_msgs/JointCommand` | Joint command for the torso |
| `right_arm` | `rby1_msgs/JointCommand` | Joint command for the right arm |
| `left_arm` | `rby1_msgs/JointCommand` | Joint command for the left arm |
| `head` | `rby1_msgs/JointCommand` | Joint command for the head |

## `rby1_msgs/StreamCartesianCommand`

| Field | Type | Description |
|-------|------|-------------|
| `torso` | `rby1_msgs/CartesianCommand` | Cartesian command for the torso |
| `right_arm` | `rby1_msgs/CartesianCommand` | Cartesian command for the right arm |
| `left_arm` | `rby1_msgs/CartesianCommand` | Cartesian command for the left arm |

## `rby1_msgs/RobotState`

| Field | Type | Description |
|-------|------|-------------|
| `control_manager_state` | `int32` | Current Control Manager state (see constants above) |
| `brake_state` | `BrakeState` | Brake engagement per joint (left_arm[], right_arm[], torso[], head[]) |
| `tool_flange_left`, `tool_flange_right` | `ToolFlange` | Tool flange connection, output voltage and switch (see below) |
| `emo_state` | `bool` | Emergency Stop pressed status |
| `center_of_mass` | `float64[3]` | Calculated CoM position `[x, y, z]` in meters |
| `robot_stream_state` | `bool` | `true` if the persistent command stream is currently open, `false` if closed |
| `collision` | `bool` | `true` if a link distance is below `collision_threshold`. Reported only; the driver does not stop the robot. |
| `robot_version` | `float64` | Robot version |

### Control Manager States

The `RobotState.control_manager_state` field (and the `robot_state` topic) uses the following integer constants, also accessible as `RobotState.STATE_*`:

| Value | Constant | Description |
|-------|----------|-------------|
| `0` | `STATE_NONE` | Driver not initialized or disconnected |
| `1` | `STATE_IDLE` | Control Manager is disabled (IDLE) |
| `2` | `STATE_ENABLE` | Control Manager is active and holding position |
| `3` | `STATE_EXECUTING` | A motion command is currently being executed |
| `4` | `STATE_MAJOR_FAULT` | Unrecoverable hardware fault — requires reset |
| `5` | `STATE_MINOR_FAULT` | Recoverable fault — driver auto-resets by default |

## `rby1_msgs/ToolFlange`

One tool flange, used in `RobotState` (`tool_flange_left`, `tool_flange_right`).
The flange IMU and force/torque sensor are published as standard types on `tool_flange/<side>/imu` (`sensor_msgs/Imu`)
and `tool_flange/<side>/wrench` (`geometry_msgs/WrenchStamped`); see [Topics](topics.md).

| Field | Type | Description |
|-------|------|-------------|
| `connected` | `bool` | `true` while the robot receives state updates from this flange |
| `output_voltage` | `int32` | Output voltage supplied to the tool in volts: 0, 12 or 24 (set with `tool_flange_power`) |
| `switch_a` | `bool` | Physical switch A state |

## `rby1_msgs/PartJointStates`

Joint state per part, published on `joint_states`. The standard-typed `joint_overall_states`
(`sensor_msgs/JointState`, every joint including the wheels) is what TF, MoveIt and RViz read.

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | Time stamp |
| `torso` | `sensor_msgs/JointState` | Torso joints |
| `right_arm` | `sensor_msgs/JointState` | Right arm joints |
| `left_arm` | `sensor_msgs/JointState` | Left arm joints |
| `head` | `sensor_msgs/JointState` | Head joints |
