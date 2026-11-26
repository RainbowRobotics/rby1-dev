(rb-api-optimalcontrolcommand-request)=
# OptimalControlCommand.Request

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Request part of [OptimalControlCommand](optimalcontrolcommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| cartesian_costs | [OptimalControlCommand.CartesianCost](optimalcontrolcommand-cartesiancost.md) | repeated |  |
| center_of_mass_cost | [OptimalControlCommand.CenterOfMassCost](optimalcontrolcommand-centerofmasscost.md) |  |  |
| joint_position_costs | [OptimalControlCommand.JointPositionCost](optimalcontrolcommand-jointpositioncost.md) | repeated |  |
| velocity_limit_scaling | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | velocity scaling factor: qdot_limit * default.velocity_limit_scaling * velocity_limit_scaling default: 1.0, range: (0, 1] |
| acceleration_limit_scaling | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | acceleration scaling factor: qddot_limit * default.acceleration_limit_scaling * acceleration_limit_scaling default: 1.0, range: (0, ∞) |
| velocity_tracking_gain | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | **Deprecated since 0.4.3.** The robot sets this value to 0 to avoid unintended behavior. (Velocity tracking gain, range (0, 1].) |
| error_scaling | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | Like step size, range: (0, ∞) |
| stop_cost | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | stop cost default: default.optimal_control_command.stop_cost, range: (0, ∞) |
| min_delta_cost | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | minimum delta cost, optional, range: (0, ∞) |
| patience | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | patience parameter, optional, range: (0, ∞) |
