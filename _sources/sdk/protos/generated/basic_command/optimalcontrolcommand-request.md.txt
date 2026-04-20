(rb-api-optimalcontrolcommand-request)=
# OptimalControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for OptimalControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| cartesian_costs | [OptimalControlCommand.CartesianCost](optimalcontrolcommand-cartesiancost.md) | repeated |  |
| center_of_mass_cost | [OptimalControlCommand.CenterOfMassCost](optimalcontrolcommand-centerofmasscost.md) |  |  |
| joint_position_costs | [OptimalControlCommand.JointPositionCost](optimalcontrolcommand-jointpositioncost.md) | repeated |  |
| velocity_limit_scaling | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | velocity scaling factor: qdot_limit * default.velocity_limit_scaling * velocity_limit_scaling default: 1.0, range: (0, 1] |
| acceleration_limit_scaling | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | acceleration scaling factor: qddot_limit * default.acceleration_limit_scaling * acceleration_limit_scaling default: 1.0, range: (0, ∞) |
| velocity_tracking_gain | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | velocity tracking gain default: default.optimal_control_command.velocity_tracking_gain, range: (0, 1] DEPRECATED since 0.4.3 For robots prior to version 0.4.1, differences in the optimization method may cause unintended behavior if the value is used. Therefore, to prevent this issue, this value is forcibly set to 0. |
| error_scaling | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | Like step size, range: (0, ∞) |
| stop_cost | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | stop cost default: default.optimal_control_command.stop_cost, range: (0, ∞) |
| min_delta_cost | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | minimum delta cost, optional, range: (0, ∞) |
| patience | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | patience parameter, optional, range: (0, ∞) |
