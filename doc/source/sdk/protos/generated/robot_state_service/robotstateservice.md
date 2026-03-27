# RobotStateService

- Source proto: `rb/api/robot_state_service.proto`

gRPC service for robot state.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRobotState | [GetRobotStateRequest](../robot_state/getrobotstaterequest.md#rb-api-getrobotstaterequest) | [GetRobotStateResponse](../robot_state/getrobotstateresponse.md#rb-api-getrobotstateresponse) |  |
| GetRobotStateStream | [GetRobotStateStreamRequest](../robot_state/getrobotstatestreamrequest.md#rb-api-getrobotstatestreamrequest) | [GetRobotStateStreamResponse](../robot_state/getrobotstatestreamresponse.md#rb-api-getrobotstatestreamresponse) stream |  |
| GetControlManagerState | [GetControlManagerStateRequest](../robot_state/getcontrolmanagerstaterequest.md#rb-api-getcontrolmanagerstaterequest) | [GetControlManagerStateResponse](../robot_state/getcontrolmanagerstateresponse.md#rb-api-getcontrolmanagerstateresponse) |  |
| ResetOdometry | [ResetOdometryRequest](../robot_state/resetodometryrequest.md#rb-api-resetodometryrequest) | [ResetOdometryResponse](../robot_state/resetodometryresponse.md#rb-api-resetodometryresponse) |  |
