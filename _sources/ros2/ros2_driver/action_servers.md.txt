# Action Servers

| Action Server | Type | Description |
|---------------|------|-------------|
| `robot_joint` | `rby1_msgs/Rby1JointCommand` | Whole-body joint position command. Each body part (torso, right_arm, left_arm, head) can be commanded independently in a single goal. |
| `robot_cartesian` | `rby1_msgs/Rby1CartesianCommand` | Whole-body Cartesian command. Each arm and torso can be assigned a target pose. |
| `follow_joint_trajectory` | `control_msgs/FollowJointTrajectory` | Standard ROS 2 trajectory execution action server (used directly by MoveIt). |
| `stream_joint` | `rby1_msgs/StreamJoint` | Continuous joint trajectory streaming. Allows feeding joint stream commands sequentially over an active connection. |
| `stream_cartesian` | `rby1_msgs/StreamCartesian` | Continuous Cartesian trajectory streaming. Allows feeding Cartesian commands sequentially over an active connection. |
