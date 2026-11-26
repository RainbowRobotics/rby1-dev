(rb-api-robotinfo)=
# RobotInfo

- Source proto: [`rb/api/robot_info.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_info.proto) (rby1-sdk v0.10.1)

Static information about the robot: versions, model, joints, power outputs, EMO inputs and the joint index of each component.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](../scalar-value-types.md) |  |  |
| sdk_version | [string](../scalar-value-types.md) |  |  |
| robot_model_name | [string](../scalar-value-types.md) |  |  |
| robot_model_version | [string](../scalar-value-types.md) |  |  |
| battery_info | [BatteryInfo](batteryinfo.md) |  |  |
| power_infos | [PowerInfo](powerinfo.md) | repeated |  |
| emo_infos | [EMOInfo](emoinfo.md) | repeated |  |
| degree_of_freedom | [int32](../scalar-value-types.md) |  |  |
| joint_infos | [JointInfo](jointinfo.md) | repeated |  |
| mobility_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| body_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| head_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| torso_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| right_arm_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| left_arm_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| robot_version | [string](../scalar-value-types.md) |  | [DEPRECATED] Will be removed in the future. Use `robot_model_name` instead. |
| sdk_commit_id | [string](../scalar-value-types.md) |  | [DEPRECATED] |
