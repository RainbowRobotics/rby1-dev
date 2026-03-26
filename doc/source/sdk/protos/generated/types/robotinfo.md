# RobotInfo

- Source proto: `rb/api/robot_info.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| sdk_version | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| robot_model_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| robot_model_version | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| battery_info | [BatteryInfo](./batteryinfo.md#rb-api-batteryinfo) |  |  |
| power_infos | [PowerInfo](./powerinfo.md#rb-api-powerinfo) | repeated |  |
| emo_infos | [EMOInfo](./emoinfo.md#rb-api-emoinfo) | repeated |  |
| degree_of_freedom | [int32](./scalar-value-types.md#scalar-value-types) |  |  |
| joint_infos | [JointInfo](./jointinfo.md#rb-api-jointinfo) | repeated |  |
| mobility_joint_idx | [uint32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| body_joint_idx | [uint32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| head_joint_idx | [uint32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| torso_joint_idx | [uint32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| right_arm_joint_idx | [uint32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| left_arm_joint_idx | [uint32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| robot_version | [string](./scalar-value-types.md#scalar-value-types) |  | [DEPRECATED] Will be removed in the future. Use `robot_model_name` instead. |
| sdk_commit_id | [string](./scalar-value-types.md#scalar-value-types) |  | [DEPRECATED] |
