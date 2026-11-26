(rb-api-robotstateservice)=
# RobotStateService

- Source proto: [`rb/api/robot_state_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state_service.proto) (rby1-sdk v0.10.1)

Returns the robot state once or as a stream, returns the Control Manager state and resets the odometry.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRobotState | [GetRobotStateRequest](../robot_state/getrobotstaterequest.md) | [GetRobotStateResponse](../robot_state/getrobotstateresponse.md) |  |
| GetRobotStateStream | [GetRobotStateStreamRequest](../robot_state/getrobotstatestreamrequest.md) | [GetRobotStateStreamResponse](../robot_state/getrobotstatestreamresponse.md) stream |  |
| GetControlManagerState | [GetControlManagerStateRequest](../robot_state/getcontrolmanagerstaterequest.md) | [GetControlManagerStateResponse](../robot_state/getcontrolmanagerstateresponse.md) |  |
| ResetOdometry | [ResetOdometryRequest](../robot_state/resetodometryrequest.md) | [ResetOdometryResponse](../robot_state/resetodometryresponse.md) |  |
