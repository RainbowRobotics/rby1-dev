(rb-api-getrobotstateresponse)=
# GetRobotStateResponse

- Source proto: [`rb/api/robot_state.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state.proto) (rby1-sdk v0.10.1)

Response of the `GetRobotState` RPC of [RobotStateService](../robot_state_service/robotstateservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| robot_state | [RobotState](robotstate.md) |  |  |
| control_manager_state | [ControlManagerState](../control_manager/controlmanagerstate.md) |  |  |
