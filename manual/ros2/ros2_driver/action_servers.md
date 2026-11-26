# Action Servers

All action names are relative to the driver's namespace, `rby1` by default (for example, `/rby1/robot_joint`).

| Action Server | Type | Description |
|---------------|------|-------------|
| `robot_joint` | `rby1_msgs/Rby1JointCommand` | Whole-body joint command. Each body part (torso, right_arm, left_arm, head) can be commanded in one goal, in position or impedance control per part. |
| `robot_cartesian` | `rby1_msgs/Rby1CartesianCommand` | Whole-body Cartesian command. Each arm and the torso can be given a target pose. |
| `follow_joint_trajectory` | `control_msgs/FollowJointTrajectory` | Standard ROS 2 trajectory action for the torso, the arms and the head, in any combination. Runs on the [command streams](command_streams.md): open the channels of the parts first. |
| `stream_joint` | `rby1_msgs/StreamJoint` | One joint command on the parts' stream channels, for a client that sends them continuously. |
| `stream_cartesian` | `rby1_msgs/StreamCartesian` | One Cartesian target per arm on its stream channel; the driver solves the joints itself. |

Goal fields are in [Custom Message Types](custom_message_types.md). `StreamPosition.action` is defined in `rby1_msgs` but no server provides it.

::: warning
Every action here moves the robot. Clear the robot's reach and keep the E-Stop within reach. Try new commands in the simulator first.
With a stream channel open, `robot_joint` and `robot_cartesian` behave differently; see [Services](services.md#robot_joint-and-robot_cartesian-while-a-channel-is-open).
:::

Verified against: rby1-ros2 v1.0.0 `rby1_msgs/action/*.action`, `rby1_driver/src/rby1_ros2_driver.cpp`, `Doc/manual/02_driver.md` (Actions).
