(rb-api-robotstateservice)=
# RobotStateService

- Source proto: `rb/api/robot_state_service.proto`

gRPC service for robot state.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRobotState | [GetRobotStateRequest](../robot_state/getrobotstaterequest.md) | [GetRobotStateResponse](../robot_state/getrobotstateresponse.md) |  |
| GetRobotStateStream | [GetRobotStateStreamRequest](../robot_state/getrobotstatestreamrequest.md) | [GetRobotStateStreamResponse](../robot_state/getrobotstatestreamresponse.md) stream |  |
| GetControlManagerState | [GetControlManagerStateRequest](../robot_state/getcontrolmanagerstaterequest.md) | [GetControlManagerStateResponse](../robot_state/getcontrolmanagerstateresponse.md) |  |
| ResetOdometry | [ResetOdometryRequest](../robot_state/resetodometryrequest.md) | [ResetOdometryResponse](../robot_state/resetodometryresponse.md) |  |
