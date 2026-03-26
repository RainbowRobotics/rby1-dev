# OptimalControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](./commandheader-request.md#rb-api-commandheader-request) |  |  |
| cartesian_costs | [OptimalControlCommand.CartesianCost](./optimalcontrolcommand-cartesiancost.md#rb-api-optimalcontrolcommand-cartesiancost) | repeated |  |
| center_of_mass_cost | [OptimalControlCommand.CenterOfMassCost](./optimalcontrolcommand-centerofmasscost.md#rb-api-optimalcontrolcommand-centerofmasscost) |  |  |
| joint_position_costs | [OptimalControlCommand.JointPositionCost](./optimalcontrolcommand-jointpositioncost.md#rb-api-optimalcontrolcommand-jointpositioncost) | repeated |  |
| velocity_limit_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | velocity scaling factor: qdot_limit * default.velocity_limit_scaling * velocity_limit_scaling default: 1.0, range: (0, 1] |
| acceleration_limit_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | acceleration scaling factor: qddot_limit * default.acceleration_limit_scaling * acceleration_limit_scaling default: 1.0, range: (0, ∞) |
| velocity_tracking_gain | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | velocity tracking gain default: default.optimal_control_command.velocity_tracking_gain, range: (0, 1] DEPRECATED since 0.4.3 For robots prior to version 0.4.1, differences in the optimization method may cause unintended behavior if the value is used. Therefore, to prevent this issue, this value is forcibly set to 0. |
| error_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | Like step size, range: (0, ∞) |
| stop_cost | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | stop cost default: default.optimal_control_command.stop_cost, range: (0, ∞) |
| min_delta_cost | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | minimum delta cost, optional, range: (0, ∞) |
| patience | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | patience parameter, optional, range: (0, ∞) |
