(rb-api-controlmanagerstate)=
# ControlManagerState

- Source proto: `rb/api/control_manager.proto`

State snapshot for control manager.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [ControlManagerState.State](controlmanagerstate-state.md) |  |  |
| time_scale | [double](../scalar-value-types.md) |  |  |
| control_state | [ControlManagerState.ControlState](controlmanagerstate-controlstate.md) |  |  |
| enabled_joint_idx | [uint32](../scalar-value-types.md) | repeated |  |
| unlimited_mode_enabled | [bool](../scalar-value-types.md) |  |  |
