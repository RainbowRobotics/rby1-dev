(rb-api-controlmanagerstate)=
# ControlManagerState

- Source proto: [`rb/api/control_manager.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/control_manager.proto) (rby1-sdk v0.10.1)

State of the Control Manager: its state, control state, time scale, enabled joints and whether unlimited mode is on.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [ControlManagerState.State](controlmanagerstate-state.md) |  |  |
| time_scale | [double](../scalar-value-types.md) |  |  |
| control_state | [ControlManagerState.ControlState](controlmanagerstate-controlstate.md) |  |  |
| enabled_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| unlimited_mode_enabled | [bool](../scalar-value-types.md) |  |  |
