(rb-api-getrobotstatestreamrequest)=
# GetRobotStateStreamRequest

- Source proto: [`rb/api/robot_state.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state.proto) (rby1-sdk v0.10.1)

Request of the `GetRobotStateStream` RPC of [RobotStateService](../robot_state_service/robotstateservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| update_rate | [double](../scalar-value-types.md) |  | Hz |
