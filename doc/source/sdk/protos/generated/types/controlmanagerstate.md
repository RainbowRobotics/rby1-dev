# ControlManagerState

- Source proto: `rb/api/control_manager.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [ControlManagerState.State](./controlmanagerstate-state.md#rb-api-controlmanagerstate-state) |  |  |
| time_scale | [double](./scalar-value-types.md#scalar-value-types) |  |  |
| control_state | [ControlManagerState.ControlState](./controlmanagerstate-controlstate.md#rb-api-controlmanagerstate-controlstate) |  |  |
| enabled_joint_idx | [uint32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| unlimited_mode_enabled | [bool](./scalar-value-types.md#scalar-value-types) |  |  |
