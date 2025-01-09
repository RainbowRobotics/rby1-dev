# Protocol Documentation
## Compatible Version
- **RBY1-RPC version**: [v0.2.0](https://github.com/RainbowRobotics/rby1-release/releases/tag/v0.2.0), [v0.2.1](https://github.com/RainbowRobotics/rby1-release/releases/tag/v0.2.1)
- **RBY1-SDK version**: v0.3.0 ([e8db0b3](https://github.com/RainbowRobotics/rby1-sdk/commit/e8db0b3912be93583531a39d1ea183041e98f72c))
<a name="top"></a>

## Table of Contents

- [rb/api/arm-command.proto](#rb-api-arm-command-proto)
    - [ArmCommand](#rb-api-ArmCommand)
    - [ArmCommand.Feedback](#rb-api-ArmCommand-Feedback)
    - [ArmCommand.Request](#rb-api-ArmCommand-Request)
  
- [rb/api/basic-command.proto](#rb-api-basic-command-proto)
    - [CartesianCommand](#rb-api-CartesianCommand)
    - [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback)
    - [CartesianCommand.JointPositionTarget](#rb-api-CartesianCommand-JointPositionTarget)
    - [CartesianCommand.Request](#rb-api-CartesianCommand-Request)
    - [CartesianCommand.SE3PoseTarget](#rb-api-CartesianCommand-SE3PoseTarget)
    - [CartesianCommand.TrackingError](#rb-api-CartesianCommand-TrackingError)
    - [GravityCompensationCommand](#rb-api-GravityCompensationCommand)
    - [GravityCompensationCommand.Feedback](#rb-api-GravityCompensationCommand-Feedback)
    - [GravityCompensationCommand.Request](#rb-api-GravityCompensationCommand-Request)
    - [ImpedanceControlCommand](#rb-api-ImpedanceControlCommand)
    - [ImpedanceControlCommand.Feedback](#rb-api-ImpedanceControlCommand-Feedback)
    - [ImpedanceControlCommand.Request](#rb-api-ImpedanceControlCommand-Request)
    - [ImpedanceControlCommand.TrackingError](#rb-api-ImpedanceControlCommand-TrackingError)
    - [JogCommand](#rb-api-JogCommand)
    - [JogCommand.Feedback](#rb-api-JogCommand-Feedback)
    - [JogCommand.Request](#rb-api-JogCommand-Request)
    - [JointPositionCommand](#rb-api-JointPositionCommand)
    - [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback)
    - [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request)
    - [JointVelocityCommand](#rb-api-JointVelocityCommand)
    - [JointVelocityCommand.Feedback](#rb-api-JointVelocityCommand-Feedback)
    - [JointVelocityCommand.Request](#rb-api-JointVelocityCommand-Request)
    - [OptimalControlCommand](#rb-api-OptimalControlCommand)
    - [OptimalControlCommand.CartesianCost](#rb-api-OptimalControlCommand-CartesianCost)
    - [OptimalControlCommand.CenterOfMassCost](#rb-api-OptimalControlCommand-CenterOfMassCost)
    - [OptimalControlCommand.Feedback](#rb-api-OptimalControlCommand-Feedback)
    - [OptimalControlCommand.JointPositionCost](#rb-api-OptimalControlCommand-JointPositionCost)
    - [OptimalControlCommand.Request](#rb-api-OptimalControlCommand-Request)
    - [RealTimeControlCommand](#rb-api-RealTimeControlCommand)
    - [RealTimeControlCommand.Feedback](#rb-api-RealTimeControlCommand-Feedback)
    - [RealTimeControlCommand.Request](#rb-api-RealTimeControlCommand-Request)
    - [SE2VelocityCommand](#rb-api-SE2VelocityCommand)
    - [SE2VelocityCommand.Feedback](#rb-api-SE2VelocityCommand-Feedback)
    - [SE2VelocityCommand.Request](#rb-api-SE2VelocityCommand-Request)
    - [StopCommand](#rb-api-StopCommand)
    - [StopCommand.Feedback](#rb-api-StopCommand-Feedback)
    - [StopCommand.Request](#rb-api-StopCommand-Request)
  
- [rb/api/body-command.proto](#rb-api-body-command-proto)
    - [BodyCommand](#rb-api-BodyCommand)
    - [BodyCommand.Feedback](#rb-api-BodyCommand-Feedback)
    - [BodyCommand.Request](#rb-api-BodyCommand-Request)
  
- [rb/api/body-component-based-command.proto](#rb-api-body-component-based-command-proto)
    - [BodyComponentBasedCommand](#rb-api-BodyComponentBasedCommand)
    - [BodyComponentBasedCommand.Feedback](#rb-api-BodyComponentBasedCommand-Feedback)
    - [BodyComponentBasedCommand.Request](#rb-api-BodyComponentBasedCommand-Request)
  
- [rb/api/command-header.proto](#rb-api-command-header-proto)
    - [CommandHeader](#rb-api-CommandHeader)
    - [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback)
    - [CommandHeader.Request](#rb-api-CommandHeader-Request)
  
- [rb/api/component-based-command.proto](#rb-api-component-based-command-proto)
    - [ComponentBasedCommand](#rb-api-ComponentBasedCommand)
    - [ComponentBasedCommand.Feedback](#rb-api-ComponentBasedCommand-Feedback)
    - [ComponentBasedCommand.Request](#rb-api-ComponentBasedCommand-Request)
  
- [rb/api/control-manager.proto](#rb-api-control-manager-proto)
    - [CancelControlRequest](#rb-api-CancelControlRequest)
    - [CancelControlResponse](#rb-api-CancelControlResponse)
    - [ControlManagerCommandRequest](#rb-api-ControlManagerCommandRequest)
    - [ControlManagerCommandResponse](#rb-api-ControlManagerCommandResponse)
    - [ControlManagerState](#rb-api-ControlManagerState)
    - [GetTimeScaleRequest](#rb-api-GetTimeScaleRequest)
    - [GetTimeScaleResponse](#rb-api-GetTimeScaleResponse)
    - [SetTimeScaleRequest](#rb-api-SetTimeScaleRequest)
    - [SetTimeScaleResponse](#rb-api-SetTimeScaleResponse)
  
    - [ControlManagerCommandRequest.Command](#rb-api-ControlManagerCommandRequest-Command)
    - [ControlManagerState.ControlState](#rb-api-ControlManagerState-ControlState)
    - [ControlManagerState.State](#rb-api-ControlManagerState-State)
  
- [rb/api/control-manager-service.proto](#rb-api-control-manager-service-proto)
    - [ControlManagerService](#rb-api-ControlManagerService)
  
- [rb/api/gamepad.proto](#rb-api-gamepad-proto)
    - [Gamepad](#rb-api-Gamepad)
    - [UploadGamepadDataRequest](#rb-api-UploadGamepadDataRequest)
    - [UploadGamepadDataResponse](#rb-api-UploadGamepadDataResponse)
  
- [rb/api/gamepad-service.proto](#rb-api-gamepad-service-proto)
    - [GamepadService](#rb-api-GamepadService)
  
- [rb/api/geometry.proto](#rb-api-geometry-proto)
    - [EulerAngleZYX](#rb-api-EulerAngleZYX)
    - [Inertia](#rb-api-Inertia)
    - [Inertial](#rb-api-Inertial)
    - [Quaternion](#rb-api-Quaternion)
    - [SE2Pose](#rb-api-SE2Pose)
    - [SE2Velocity](#rb-api-SE2Velocity)
    - [SE3Pose](#rb-api-SE3Pose)
    - [Vec2](#rb-api-Vec2)
    - [Vec3](#rb-api-Vec3)
  
- [rb/api/gripper-command.proto](#rb-api-gripper-command-proto)
    - [GripperInitializationRequest](#rb-api-GripperInitializationRequest)
    - [GripperInitializationResponse](#rb-api-GripperInitializationResponse)
    - [GripperMoveRequest](#rb-api-GripperMoveRequest)
    - [GripperMoveResponse](#rb-api-GripperMoveResponse)
  
- [rb/api/gripper-command-service.proto](#rb-api-gripper-command-service-proto)
    - [GripperCommandService](#rb-api-GripperCommandService)
  
- [rb/api/head-command.proto](#rb-api-head-command-proto)
    - [HeadCommand](#rb-api-HeadCommand)
    - [HeadCommand.Feedback](#rb-api-HeadCommand-Feedback)
    - [HeadCommand.Request](#rb-api-HeadCommand-Request)
  
- [rb/api/header.proto](#rb-api-header-proto)
    - [CommonError](#rb-api-CommonError)
    - [RequestHeader](#rb-api-RequestHeader)
    - [ResponseHeader](#rb-api-ResponseHeader)
  
    - [CommonError.Code](#rb-api-CommonError-Code)
  
- [rb/api/joint-operation.proto](#rb-api-joint-operation-proto)
    - [BrakeEngageRequest](#rb-api-BrakeEngageRequest)
    - [BrakeEngageResponse](#rb-api-BrakeEngageResponse)
    - [BrakeReleaseRequest](#rb-api-BrakeReleaseRequest)
    - [BrakeReleaseResponse](#rb-api-BrakeReleaseResponse)
    - [GetPositionPIDGainRequest](#rb-api-GetPositionPIDGainRequest)
    - [GetPositionPIDGainResponse](#rb-api-GetPositionPIDGainResponse)
    - [HomeOffsetResetRequest](#rb-api-HomeOffsetResetRequest)
    - [HomeOffsetResetResponse](#rb-api-HomeOffsetResetResponse)
    - [PositionPIDGain](#rb-api-PositionPIDGain)
    - [ServoOnRequest](#rb-api-ServoOnRequest)
    - [ServoOnResponse](#rb-api-ServoOnResponse)
    - [SetPositionPIDGainRequest](#rb-api-SetPositionPIDGainRequest)
    - [SetPositionPIDGainResponse](#rb-api-SetPositionPIDGainResponse)
  
    - [BrakeEngageResponse.Status](#rb-api-BrakeEngageResponse-Status)
    - [BrakeReleaseResponse.Status](#rb-api-BrakeReleaseResponse-Status)
    - [GetPositionPIDGainRequest.TargetComponent](#rb-api-GetPositionPIDGainRequest-TargetComponent)
    - [HomeOffsetResetResponse.Status](#rb-api-HomeOffsetResetResponse-Status)
    - [ServoOnResponse.Status](#rb-api-ServoOnResponse-Status)
    - [SetPositionPIDGainResponse.Status](#rb-api-SetPositionPIDGainResponse-Status)
  
- [rb/api/joint-operation-service.proto](#rb-api-joint-operation-service-proto)
    - [JointOperationService](#rb-api-JointOperationService)
  
- [rb/api/log.proto](#rb-api-log-proto)
    - [GetLastLogRequest](#rb-api-GetLastLogRequest)
    - [GetLastLogResponse](#rb-api-GetLastLogResponse)
    - [GetLogStreamRequest](#rb-api-GetLogStreamRequest)
    - [GetLogStreamResponse](#rb-api-GetLogStreamResponse)
    - [Log](#rb-api-Log)
    - [SetLogLevelRequest](#rb-api-SetLogLevelRequest)
    - [SetLogLevelResponse](#rb-api-SetLogLevelResponse)
  
    - [Log.Level](#rb-api-Log-Level)
  
- [rb/api/log-service.proto](#rb-api-log-service-proto)
    - [LogService](#rb-api-LogService)
  
- [rb/api/mobility-command.proto](#rb-api-mobility-command-proto)
    - [MobilityCommand](#rb-api-MobilityCommand)
    - [MobilityCommand.Feedback](#rb-api-MobilityCommand-Feedback)
    - [MobilityCommand.Request](#rb-api-MobilityCommand-Request)
  
- [rb/api/parameter.proto](#rb-api-parameter-proto)
    - [FactoryResetAllParametersRequest](#rb-api-FactoryResetAllParametersRequest)
    - [FactoryResetAllParametersResponse](#rb-api-FactoryResetAllParametersResponse)
    - [FactoryResetParameterRequest](#rb-api-FactoryResetParameterRequest)
    - [FactoryResetParameterResponse](#rb-api-FactoryResetParameterResponse)
    - [GetParameterListRequest](#rb-api-GetParameterListRequest)
    - [GetParameterListResponse](#rb-api-GetParameterListResponse)
    - [GetParameterListResponse.ParameterType](#rb-api-GetParameterListResponse-ParameterType)
    - [GetParameterRequest](#rb-api-GetParameterRequest)
    - [GetParameterResponse](#rb-api-GetParameterResponse)
    - [ResetAllParametersRequest](#rb-api-ResetAllParametersRequest)
    - [ResetAllParametersResponse](#rb-api-ResetAllParametersResponse)
    - [ResetAllParametersToDefaultRequest](#rb-api-ResetAllParametersToDefaultRequest)
    - [ResetAllParametersToDefaultResponse](#rb-api-ResetAllParametersToDefaultResponse)
    - [ResetParameterRequest](#rb-api-ResetParameterRequest)
    - [ResetParameterResponse](#rb-api-ResetParameterResponse)
    - [ResetParameterToDefaultRequest](#rb-api-ResetParameterToDefaultRequest)
    - [ResetParameterToDefaultResponse](#rb-api-ResetParameterToDefaultResponse)
    - [SetParameterRequest](#rb-api-SetParameterRequest)
    - [SetParameterResponse](#rb-api-SetParameterResponse)
  
- [rb/api/parameter-service.proto](#rb-api-parameter-service-proto)
    - [ParameterService](#rb-api-ParameterService)
  
- [rb/api/ping.proto](#rb-api-ping-proto)
    - [PingRequest](#rb-api-PingRequest)
    - [PingResponse](#rb-api-PingResponse)
  
- [rb/api/ping-service.proto](#rb-api-ping-service-proto)
    - [PingService](#rb-api-PingService)
  
- [rb/api/power.proto](#rb-api-power-proto)
    - [JointCommandRequest](#rb-api-JointCommandRequest)
    - [JointCommandResponse](#rb-api-JointCommandResponse)
    - [PowerCommandRequest](#rb-api-PowerCommandRequest)
    - [PowerCommandResponse](#rb-api-PowerCommandResponse)
    - [ToolFlangePowerCommandRequest](#rb-api-ToolFlangePowerCommandRequest)
    - [ToolFlangePowerCommandResponse](#rb-api-ToolFlangePowerCommandResponse)
  
    - [JointCommandRequest.Command](#rb-api-JointCommandRequest-Command)
    - [JointCommandResponse.Status](#rb-api-JointCommandResponse-Status)
    - [PowerCommandRequest.Command](#rb-api-PowerCommandRequest-Command)
    - [PowerCommandResponse.Status](#rb-api-PowerCommandResponse-Status)
    - [ToolFlangePowerCommandRequest.Command](#rb-api-ToolFlangePowerCommandRequest-Command)
  
- [rb/api/power-service.proto](#rb-api-power-service-proto)
    - [PowerService](#rb-api-PowerService)
  
- [rb/api/robot-command.proto](#rb-api-robot-command-proto)
    - [RobotCommand](#rb-api-RobotCommand)
    - [RobotCommand.Feedback](#rb-api-RobotCommand-Feedback)
    - [RobotCommand.Request](#rb-api-RobotCommand-Request)
    - [RobotCommandRequest](#rb-api-RobotCommandRequest)
    - [RobotCommandResponse](#rb-api-RobotCommandResponse)
  
    - [RobotCommand.Feedback.FinishCode](#rb-api-RobotCommand-Feedback-FinishCode)
    - [RobotCommand.Feedback.Status](#rb-api-RobotCommand-Feedback-Status)
  
- [rb/api/robot-command-service.proto](#rb-api-robot-command-service-proto)
    - [RobotCommandService](#rb-api-RobotCommandService)
  
- [rb/api/robot-info.proto](#rb-api-robot-info-proto)
    - [BatteryInfo](#rb-api-BatteryInfo)
    - [EMOInfo](#rb-api-EMOInfo)
    - [GetRobotInfoRequest](#rb-api-GetRobotInfoRequest)
    - [GetRobotInfoResponse](#rb-api-GetRobotInfoResponse)
    - [GetRobotModelRequest](#rb-api-GetRobotModelRequest)
    - [GetRobotModelResponse](#rb-api-GetRobotModelResponse)
    - [ImportRobotModelRequest](#rb-api-ImportRobotModelRequest)
    - [ImportRobotModelResponse](#rb-api-ImportRobotModelResponse)
    - [JointInfo](#rb-api-JointInfo)
    - [PowerInfo](#rb-api-PowerInfo)
    - [RobotInfo](#rb-api-RobotInfo)
  
- [rb/api/robot-info-service.proto](#rb-api-robot-info-service-proto)
    - [RobotInfoService](#rb-api-RobotInfoService)
  
- [rb/api/robot-state.proto](#rb-api-robot-state-proto)
    - [BatteryState](#rb-api-BatteryState)
    - [Collision](#rb-api-Collision)
    - [EMOState](#rb-api-EMOState)
    - [FTSensorData](#rb-api-FTSensorData)
    - [GetControlManagerStateRequest](#rb-api-GetControlManagerStateRequest)
    - [GetControlManagerStateResponse](#rb-api-GetControlManagerStateResponse)
    - [GetRobotStateRequest](#rb-api-GetRobotStateRequest)
    - [GetRobotStateResponse](#rb-api-GetRobotStateResponse)
    - [GetRobotStateStreamRequest](#rb-api-GetRobotStateStreamRequest)
    - [GetRobotStateStreamResponse](#rb-api-GetRobotStateStreamResponse)
    - [JointState](#rb-api-JointState)
    - [PowerState](#rb-api-PowerState)
    - [ResetOdometryRequest](#rb-api-ResetOdometryRequest)
    - [ResetOdometryResponse](#rb-api-ResetOdometryResponse)
    - [RobotState](#rb-api-RobotState)
    - [SystemStat](#rb-api-SystemStat)
    - [ToolFlangeState](#rb-api-ToolFlangeState)
  
    - [EMOState.State](#rb-api-EMOState-State)
    - [JointState.FETState](#rb-api-JointState-FETState)
    - [JointState.InitializationState](#rb-api-JointState-InitializationState)
    - [JointState.RunState](#rb-api-JointState-RunState)
    - [PowerState.State](#rb-api-PowerState-State)
  
- [rb/api/robot-state-service.proto](#rb-api-robot-state-service-proto)
    - [RobotStateService](#rb-api-RobotStateService)
  
- [rb/api/torso-command.proto](#rb-api-torso-command-proto)
    - [TorsoCommand](#rb-api-TorsoCommand)
    - [TorsoCommand.Feedback](#rb-api-TorsoCommand-Feedback)
    - [TorsoCommand.Request](#rb-api-TorsoCommand-Request)
  
- [rb/api/whole-body-command.proto](#rb-api-whole-body-command-proto)
    - [WholeBodyCommand](#rb-api-WholeBodyCommand)
    - [WholeBodyCommand.Feedback](#rb-api-WholeBodyCommand-Feedback)
    - [WholeBodyCommand.Request](#rb-api-WholeBodyCommand-Request)
  
- [Scalar Value Types](#scalar-value-types)



<a name="rb-api-arm-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/arm-command.proto



## ArmCommand {#rb-api-ArmCommand}

### ArmCommand







## ArmCommand-Feedback {#rb-api-ArmCommand-Feedback}

### ArmCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint-position-command-feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |
| gravity-compensation-command-feedback | [GravityCompensationCommand.Feedback](#rb-api-GravityCompensationCommand-Feedback) |  |  |
| cartesian-command-feedback | [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback) |  |  |
| impedance-control-command-feedback | [ImpedanceControlCommand.Feedback](#rb-api-ImpedanceControlCommand-Feedback) |  |  |






## ArmCommand-Request {#rb-api-ArmCommand-Request}

### ArmCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint-position-command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |
| gravity-compensation-command | [GravityCompensationCommand.Request](#rb-api-GravityCompensationCommand-Request) |  |  |
| cartesian-command | [CartesianCommand.Request](#rb-api-CartesianCommand-Request) |  |  |
| impedance-control-command | [ImpedanceControlCommand.Request](#rb-api-ImpedanceControlCommand-Request) |  |  |





 

 

 

 



<a name="rb-api-basic-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/basic-command.proto



## CartesianCommand {#rb-api-CartesianCommand}

### CartesianCommand







## CartesianCommand-Feedback {#rb-api-CartesianCommand-Feedback}

### CartesianCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| tracking-errors | [CartesianCommand.TrackingError](#rb-api-CartesianCommand-TrackingError) | repeated |  |






## CartesianCommand-JointPositionTarget {#rb-api-CartesianCommand-JointPositionTarget}

### CartesianCommand.JointPositionTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| joint-name | [string](#string) |  |  |
| target-position | [double](#double) |  |  |
| velocity-limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| acceleration-limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |






## CartesianCommand-Request {#rb-api-CartesianCommand-Request}

### CartesianCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum-time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| targets | [CartesianCommand.SE3PoseTarget](#rb-api-CartesianCommand-SE3PoseTarget) | repeated |  |
| joint-position-targets | [CartesianCommand.JointPositionTarget](#rb-api-CartesianCommand-JointPositionTarget) | repeated |  |
| stop-position-tracking-error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| stop-orientation-tracking-error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |






## CartesianCommand-SE3PoseTarget {#rb-api-CartesianCommand-SE3PoseTarget}

### CartesianCommand.SE3PoseTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref-link-name | [string](#string) |  |  |
| link-name | [string](#string) |  |  |
| T | [SE3Pose](#rb-api-SE3Pose) |  |  |
| linear-velocity-limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (m/s) |
| angular-velocity-limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) |
| acceleration-limit-scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default.linear-acceleration-limit * acceleration-limit-scaling default.angular-acceleration-limit * acceleration-limit-scaling

`(0, 1]` |






## CartesianCommand-TrackingError {#rb-api-CartesianCommand-TrackingError}

### CartesianCommand.TrackingError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position-error | [double](#double) |  |  |
| rotation-error | [double](#double) |  |  |






## GravityCompensationCommand {#rb-api-GravityCompensationCommand}

### GravityCompensationCommand







## GravityCompensationCommand-Feedback {#rb-api-GravityCompensationCommand-Feedback}

### GravityCompensationCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






## GravityCompensationCommand-Request {#rb-api-GravityCompensationCommand-Request}

### GravityCompensationCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| on | [bool](#bool) |  |  |






## ImpedanceControlCommand {#rb-api-ImpedanceControlCommand}

### ImpedanceControlCommand







## ImpedanceControlCommand-Feedback {#rb-api-ImpedanceControlCommand-Feedback}

### ImpedanceControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| tracking-error | [ImpedanceControlCommand.TrackingError](#rb-api-ImpedanceControlCommand-TrackingError) |  |  |






## ImpedanceControlCommand-Request {#rb-api-ImpedanceControlCommand-Request}

### ImpedanceControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| ref-link-name | [string](#string) |  |  |
| link-name | [string](#string) |  |  |
| T | [SE3Pose](#rb-api-SE3Pose) |  |  |
| translation-weight | [Vec3](#rb-api-Vec3) |  |  |
| rotation-weight | [Vec3](#rb-api-Vec3) |  |  |






## ImpedanceControlCommand-TrackingError {#rb-api-ImpedanceControlCommand-TrackingError}

### ImpedanceControlCommand.TrackingError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position-error | [double](#double) |  |  |
| rotation-error | [double](#double) |  |  |






## JogCommand {#rb-api-JogCommand}

### JogCommand







## JogCommand-Feedback {#rb-api-JogCommand-Feedback}

### JogCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| target-joint-name | [string](#string) |  |  |






## JogCommand-Request {#rb-api-JogCommand-Request}

### JogCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint-name | [string](#string) |  |  |
| velocity-limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) (optional) |
| acceleration-limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s^2) (optional) |
| absolute-position | [double](#double) |  | (rad) |
| relative-position | [double](#double) |  | (rad) current position &#43; relative position |
| one-step | [bool](#bool) |  | 5 deg, true is positive move, false is negative move |






## JointPositionCommand {#rb-api-JointPositionCommand}

### JointPositionCommand







## JointPositionCommand-Feedback {#rb-api-JointPositionCommand-Feedback}

### JointPositionCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






## JointPositionCommand-Request {#rb-api-JointPositionCommand-Request}

### JointPositionCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum-time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| position | [double](#double) | repeated |  |
| velocity-limit | [double](#double) | repeated |  |
| acceleration-limit | [double](#double) | repeated |  |
| cutoff-frequency | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |






## JointVelocityCommand {#rb-api-JointVelocityCommand}

### JointVelocityCommand







## JointVelocityCommand-Feedback {#rb-api-JointVelocityCommand-Feedback}

### JointVelocityCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






## JointVelocityCommand-Request {#rb-api-JointVelocityCommand-Request}

### JointVelocityCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum-time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| velocity | [double](#double) | repeated |  |
| acceleration-limit | [double](#double) | repeated |  |






## OptimalControlCommand {#rb-api-OptimalControlCommand}

### OptimalControlCommand







## OptimalControlCommand-CartesianCost {#rb-api-OptimalControlCommand-CartesianCost}

### OptimalControlCommand.CartesianCost



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref-link-name | [string](#string) |  |  |
| link-name | [string](#string) |  |  |
| T | [SE3Pose](#rb-api-SE3Pose) |  |  |
| translation-weight | [double](#double) |  | default = 1 |
| rotation-weight | [double](#double) |  | default = 1 |






## OptimalControlCommand-CenterOfMassCost {#rb-api-OptimalControlCommand-CenterOfMassCost}

### OptimalControlCommand.CenterOfMassCost



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref-link-name | [string](#string) |  |  |
| pose | [Vec3](#rb-api-Vec3) |  |  |
| weight | [double](#double) |  | default = 1 |






## OptimalControlCommand-Feedback {#rb-api-OptimalControlCommand-Feedback}

### OptimalControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| total-cost | [double](#double) |  |  |
| cartesian-costs | [double](#double) | repeated |  |
| center-of-mass-cost | [double](#double) |  |  |
| joint-position-costs | [double](#double) | repeated |  |






## OptimalControlCommand-JointPositionCost {#rb-api-OptimalControlCommand-JointPositionCost}

### OptimalControlCommand.JointPositionCost



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| joint-name | [string](#string) |  |  |
| target-position | [double](#double) |  |  |
| weight | [double](#double) |  |  |






## OptimalControlCommand-Request {#rb-api-OptimalControlCommand-Request}

### OptimalControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| cartesian-costs | [OptimalControlCommand.CartesianCost](#rb-api-OptimalControlCommand-CartesianCost) | repeated |  |
| center-of-mass-cost | [OptimalControlCommand.CenterOfMassCost](#rb-api-OptimalControlCommand-CenterOfMassCost) |  |  |
| joint-position-costs | [OptimalControlCommand.JointPositionCost](#rb-api-OptimalControlCommand-JointPositionCost) | repeated |  |
| velocity-limit-scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | velocity scaling factor: qdot-limit * default.velocity-limit-scaling * velocity-limit-scaling default: 1.0, range: (0, 1] |
| velocity-tracking-gain | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | velocity tracking gain default: default.optimal-control-command.velocity-tracking-gain, range: (0, 1] |
| stop-cost | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | stop cost default: default.optimal-control-command.stop-cost, range: (0, ∞) |
| min-delta-cost | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | minimum delta cost range: (0, ∞) |
| patience | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | patience parameter range: (0, ∞) |






## RealTimeControlCommand {#rb-api-RealTimeControlCommand}

### RealTimeControlCommand







## RealTimeControlCommand-Feedback {#rb-api-RealTimeControlCommand-Feedback}

### RealTimeControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






## RealTimeControlCommand-Request {#rb-api-RealTimeControlCommand-Request}

### RealTimeControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| port | [uint32](#uint32) |  |  |






## SE2VelocityCommand {#rb-api-SE2VelocityCommand}

### SE2VelocityCommand







## SE2VelocityCommand-Feedback {#rb-api-SE2VelocityCommand-Feedback}

### SE2VelocityCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






## SE2VelocityCommand-Request {#rb-api-SE2VelocityCommand-Request}

### SE2VelocityCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum-time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| velocity | [SE2Velocity](#rb-api-SE2Velocity) |  |  |
| acceleration-limit | [SE2Velocity](#rb-api-SE2Velocity) |  |  |






## StopCommand {#rb-api-StopCommand}

### StopCommand







## StopCommand-Feedback {#rb-api-StopCommand-Feedback}

### StopCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






## StopCommand-Request {#rb-api-StopCommand-Request}

### StopCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |





 

 

 

 



<a name="rb-api-body-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/body-command.proto



## BodyCommand {#rb-api-BodyCommand}

### BodyCommand







## BodyCommand-Feedback {#rb-api-BodyCommand-Feedback}

### BodyCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint-position-command-feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |
| optimal-control-command-feedback | [OptimalControlCommand.Feedback](#rb-api-OptimalControlCommand-Feedback) |  |  |
| gravity-compensation-command-feedback | [GravityCompensationCommand.Feedback](#rb-api-GravityCompensationCommand-Feedback) |  |  |
| cartesian-command-feedback | [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback) |  |  |
| body-component-based-command-feedback | [BodyComponentBasedCommand.Feedback](#rb-api-BodyComponentBasedCommand-Feedback) |  |  |






## BodyCommand-Request {#rb-api-BodyCommand-Request}

### BodyCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint-position-command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |
| optimal-control-command | [OptimalControlCommand.Request](#rb-api-OptimalControlCommand-Request) |  |  |
| gravity-compensation-command | [GravityCompensationCommand.Request](#rb-api-GravityCompensationCommand-Request) |  |  |
| cartesian-command | [CartesianCommand.Request](#rb-api-CartesianCommand-Request) |  |  |
| body-component-based-command | [BodyComponentBasedCommand.Request](#rb-api-BodyComponentBasedCommand-Request) |  |  |





 

 

 

 



<a name="rb-api-body-component-based-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/body-component-based-command.proto



## BodyComponentBasedCommand {#rb-api-BodyComponentBasedCommand}

### BodyComponentBasedCommand







## BodyComponentBasedCommand-Feedback {#rb-api-BodyComponentBasedCommand-Feedback}

### BodyComponentBasedCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| right-arm-command-feedback | [ArmCommand.Feedback](#rb-api-ArmCommand-Feedback) |  |  |
| left-arm-command-feedback | [ArmCommand.Feedback](#rb-api-ArmCommand-Feedback) |  |  |
| torso-command-feedback | [TorsoCommand.Feedback](#rb-api-TorsoCommand-Feedback) |  |  |






## BodyComponentBasedCommand-Request {#rb-api-BodyComponentBasedCommand-Request}

### BodyComponentBasedCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| right-arm-command | [ArmCommand.Request](#rb-api-ArmCommand-Request) |  |  |
| left-arm-command | [ArmCommand.Request](#rb-api-ArmCommand-Request) |  |  |
| torso-command | [TorsoCommand.Request](#rb-api-TorsoCommand-Request) |  |  |





 

 

 

 



<a name="rb-api-command-header-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/command-header.proto



## CommandHeader {#rb-api-CommandHeader}

### CommandHeader







## CommandHeader-Feedback {#rb-api-CommandHeader-Feedback}

### CommandHeader.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| finished | [bool](#bool) |  |  |






## CommandHeader-Request {#rb-api-CommandHeader-Request}

### CommandHeader.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| control-hold-time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |





 

 

 

 



<a name="rb-api-component-based-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/component-based-command.proto



## ComponentBasedCommand {#rb-api-ComponentBasedCommand}

### ComponentBasedCommand







## ComponentBasedCommand-Feedback {#rb-api-ComponentBasedCommand-Feedback}

### ComponentBasedCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| mobility-command-feedback | [MobilityCommand.Feedback](#rb-api-MobilityCommand-Feedback) |  |  |
| body-command-feedback | [BodyCommand.Feedback](#rb-api-BodyCommand-Feedback) |  |  |
| head-command-feedback | [HeadCommand.Feedback](#rb-api-HeadCommand-Feedback) |  |  |






## ComponentBasedCommand-Request {#rb-api-ComponentBasedCommand-Request}

### ComponentBasedCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| mobility-command | [MobilityCommand.Request](#rb-api-MobilityCommand-Request) |  |  |
| body-command | [BodyCommand.Request](#rb-api-BodyCommand-Request) |  |  |
| head-command | [HeadCommand.Request](#rb-api-HeadCommand-Request) |  |  |





 

 

 

 



<a name="rb-api-control-manager-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/control-manager.proto



## CancelControlRequest {#rb-api-CancelControlRequest}

### CancelControlRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |






## CancelControlResponse {#rb-api-CancelControlResponse}

### CancelControlResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |






## ControlManagerCommandRequest {#rb-api-ControlManagerCommandRequest}

### ControlManagerCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| command | [ControlManagerCommandRequest.Command](#rb-api-ControlManagerCommandRequest-Command) |  |  |
| unlimited-mode-enabled | [google.protobuf.BoolValue](#google-protobuf-BoolValue) |  |  |






## ControlManagerCommandResponse {#rb-api-ControlManagerCommandResponse}

### ControlManagerCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| control-manager-state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






## ControlManagerState {#rb-api-ControlManagerState}

### ControlManagerState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [ControlManagerState.State](#rb-api-ControlManagerState-State) |  |  |
| time-scale | [double](#double) |  |  |
| control-state | [ControlManagerState.ControlState](#rb-api-ControlManagerState-ControlState) |  |  |
| enabled-joint-idx | [uint32](#uint32) | repeated |  |
| unlimited-mode-enabled | [bool](#bool) |  |  |






## GetTimeScaleRequest {#rb-api-GetTimeScaleRequest}

### GetTimeScaleRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |






## GetTimeScaleResponse {#rb-api-GetTimeScaleResponse}

### GetTimeScaleResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| time-scale | [double](#double) |  |  |






## SetTimeScaleRequest {#rb-api-SetTimeScaleRequest}

### SetTimeScaleRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| time-scale | [double](#double) |  |  |






## SetTimeScaleResponse {#rb-api-SetTimeScaleResponse}

### SetTimeScaleResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| current-time-scale | [double](#double) |  |  |





 


## ControlManagerCommandRequest-Command {#rb-api-ControlManagerCommandRequest-Command}

### ControlManagerCommandRequest.Command
Control manager command

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND-UNKNOWN | 0 |  |
| COMMAND-ENABLE | 1 |  |
| COMMAND-DISABLE | 2 |  |
| COMMAND-RESET-FAULT | 3 |  |



## ControlManagerState-ControlState {#rb-api-ControlManagerState-ControlState}

### ControlManagerState.ControlState


| Name | Number | Description |
| ---- | ------ | ----------- |
| CONTROL-STATE-UNKNOWN | 0 |  |
| CONTROL-STATE-IDLE | 1 |  |
| CONTROL-STATE-EXECUTING | 2 |  |
| CONTROL-STATE-SWITCHING | 3 |  |



## ControlManagerState-State {#rb-api-ControlManagerState-State}

### ControlManagerState.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| CONTROL-MANAGER-STATE-UNKNOWN | 0 |  |
| CONTROL-MANAGER-STATE-IDLE | 1 |  |
| CONTROL-MANAGER-STATE-ENABLED | 2 |  |
| CONTROL-MANAGER-STATE-MINOR-FAULT | 3 |  |
| CONTROL-MANAGER-STATE-MAJOR-FAULT | 4 |  |


 

 

 



<a name="rb-api-control-manager-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/control-manager-service.proto


 

 

 


## ControlManagerService {#rb-api-ControlManagerService}

### ControlManagerService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ControlManagerCommand | [ControlManagerCommandRequest](#rb-api-ControlManagerCommandRequest) | [ControlManagerCommandResponse](#rb-api-ControlManagerCommandResponse) |  |
| CancelControl | [CancelControlRequest](#rb-api-CancelControlRequest) | [CancelControlResponse](#rb-api-CancelControlResponse) |  |
| GetTimeScale | [GetTimeScaleRequest](#rb-api-GetTimeScaleRequest) | [GetTimeScaleResponse](#rb-api-GetTimeScaleResponse) |  |
| SetTimeScale | [SetTimeScaleRequest](#rb-api-SetTimeScaleRequest) | [SetTimeScaleResponse](#rb-api-SetTimeScaleResponse) |  |

 



<a name="rb-api-gamepad-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/gamepad.proto



## Gamepad {#rb-api-Gamepad}

### Gamepad



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buttons | [bool](#bool) | repeated |  |
| joystick | [double](#double) | repeated |  |






## UploadGamepadDataRequest {#rb-api-UploadGamepadDataRequest}

### UploadGamepadDataRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| data | [Gamepad](#rb-api-Gamepad) |  |  |






## UploadGamepadDataResponse {#rb-api-UploadGamepadDataResponse}

### UploadGamepadDataResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 

 

 

 



<a name="rb-api-gamepad-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/gamepad-service.proto


 

 

 


## GamepadService {#rb-api-GamepadService}

### GamepadService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| UploadGamepadData | [Gamepad](#rb-api-Gamepad) stream | [UploadGamepadDataResponse](#rb-api-UploadGamepadDataResponse) |  |

 



<a name="rb-api-geometry-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/geometry.proto



## EulerAngleZYX {#rb-api-EulerAngleZYX}

### EulerAngleZYX



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| z | [double](#double) |  |  |
| y | [double](#double) |  |  |
| x | [double](#double) |  |  |






## Inertia {#rb-api-Inertia}

### Inertia
Inertia tensor components (kg*m^2)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ixx | [double](#double) |  |  |
| iyy | [double](#double) |  |  |
| izz | [double](#double) |  |  |
| ixy | [double](#double) |  |  |
| ixz | [double](#double) |  |  |
| iyz | [double](#double) |  |  |






## Inertial {#rb-api-Inertial}

### Inertial



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mass | [double](#double) |  | Mass (kg) |
| center-of-mass | [Vec3](#rb-api-Vec3) |  | Center of mass (m) |
| inertia | [Inertia](#rb-api-Inertia) |  | Inertia tensor |






## Quaternion {#rb-api-Quaternion}

### Quaternion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |
| z | [double](#double) |  |  |
| w | [double](#double) |  |  |






## SE2Pose {#rb-api-SE2Pose}

### SE2Pose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Vec2](#rb-api-Vec2) |  | (m) |
| angle | [double](#double) |  | (rad) |






## SE2Velocity {#rb-api-SE2Velocity}

### SE2Velocity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| linear | [Vec2](#rb-api-Vec2) |  | (m/s) |
| angular | [double](#double) |  | (rad/s) |






## SE3Pose {#rb-api-SE3Pose}

### SE3Pose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Vec3](#rb-api-Vec3) |  | (m) |
| quaternion | [Quaternion](#rb-api-Quaternion) |  |  |
| euler | [EulerAngleZYX](#rb-api-EulerAngleZYX) |  |  |






## Vec2 {#rb-api-Vec2}

### Vec2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |






## Vec3 {#rb-api-Vec3}

### Vec3



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |
| z | [double](#double) |  |  |





 

 

 

 



<a name="rb-api-gripper-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/gripper-command.proto



## GripperInitializationRequest {#rb-api-GripperInitializationRequest}

### GripperInitializationRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  |  |






## GripperInitializationResponse {#rb-api-GripperInitializationResponse}

### GripperInitializationResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |






## GripperMoveRequest {#rb-api-GripperMoveRequest}

### GripperMoveRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  |  |
| position | [int32](#int32) |  |  |
| velocity | [int32](#int32) |  |  |
| force | [int32](#int32) |  |  |






## GripperMoveResponse {#rb-api-GripperMoveResponse}

### GripperMoveResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |





 

 

 

 



<a name="rb-api-gripper-command-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/gripper-command-service.proto


 

 

 


## GripperCommandService {#rb-api-GripperCommandService}

### GripperCommandService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GripperInitialization | [GripperInitializationRequest](#rb-api-GripperInitializationRequest) | [GripperInitializationResponse](#rb-api-GripperInitializationResponse) |  |
| GripperMove | [GripperMoveRequest](#rb-api-GripperMoveRequest) | [GripperMoveResponse](#rb-api-GripperMoveResponse) | Joint command |

 



<a name="rb-api-head-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/head-command.proto



## HeadCommand {#rb-api-HeadCommand}

### HeadCommand







## HeadCommand-Feedback {#rb-api-HeadCommand-Feedback}

### HeadCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint-position-command-feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |






## HeadCommand-Request {#rb-api-HeadCommand-Request}

### HeadCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint-position-command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |





 

 

 

 



<a name="rb-api-header-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/header.proto



## CommonError {#rb-api-CommonError}

### CommonError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [CommonError.Code](#rb-api-CommonError-Code) |  | Error code |
| message | [string](#string) |  | Human-readable error message |






## RequestHeader {#rb-api-RequestHeader}

### RequestHeader
Standard request header


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Client local system clock |






## ResponseHeader {#rb-api-ResponseHeader}

### ResponseHeader
Standard response header


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Echo |
| request-received-timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Robot clock |
| response-timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Robot clock |
| error | [CommonError](#rb-api-CommonError) |  | If set, there is error |





 


## CommonError-Code {#rb-api-CommonError-Code}

### CommonError.Code


| Name | Number | Description |
| ---- | ------ | ----------- |
| CODE-UNSPECIFIED | 0 | Code is not specified. |
| CODE-OK | 1 | Not an error. Request was successful. |
| CODE-INTERNAL-SERVER-ERROR | 2 | Service experienced an unexpected error state. |
| CODE-INVALID-REQUEST | 3 | Ill-formed request. Request arguments were not valid. |


 

 

 



<a name="rb-api-joint-operation-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/joint-operation.proto



## BrakeEngageRequest {#rb-api-BrakeEngageRequest}

### BrakeEngageRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  |  |






## BrakeEngageResponse {#rb-api-BrakeEngageResponse}

### BrakeEngageResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [BrakeEngageResponse.Status](#rb-api-BrakeEngageResponse-Status) |  |  |
| message | [string](#string) |  | Human-readable message for status |






## BrakeReleaseRequest {#rb-api-BrakeReleaseRequest}

### BrakeReleaseRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  |  |






## BrakeReleaseResponse {#rb-api-BrakeReleaseResponse}

### BrakeReleaseResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [BrakeReleaseResponse.Status](#rb-api-BrakeReleaseResponse-Status) |  |  |
| message | [string](#string) |  | Human-readable message for status |






## GetPositionPIDGainRequest {#rb-api-GetPositionPIDGainRequest}

### GetPositionPIDGainRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| dev-name | [string](#string) |  |  |
| target-component | [GetPositionPIDGainRequest.TargetComponent](#rb-api-GetPositionPIDGainRequest-TargetComponent) |  |  |






## GetPositionPIDGainResponse {#rb-api-GetPositionPIDGainResponse}

### GetPositionPIDGainResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| position-gain | [PositionPIDGain](#rb-api-PositionPIDGain) | repeated |  |






## HomeOffsetResetRequest {#rb-api-HomeOffsetResetRequest}

### HomeOffsetResetRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  |  |






## HomeOffsetResetResponse {#rb-api-HomeOffsetResetResponse}

### HomeOffsetResetResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [HomeOffsetResetResponse.Status](#rb-api-HomeOffsetResetResponse-Status) |  |  |
| message | [string](#string) |  | Human-readable message for status |






## PositionPIDGain {#rb-api-PositionPIDGain}

### PositionPIDGain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| p-gain | [uint32](#uint32) |  |  |
| i-gain | [uint32](#uint32) |  |  |
| d-gain | [uint32](#uint32) |  |  |






## ServoOnRequest {#rb-api-ServoOnRequest}

### ServoOnRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  |  |






## ServoOnResponse {#rb-api-ServoOnResponse}

### ServoOnResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [ServoOnResponse.Status](#rb-api-ServoOnResponse-Status) |  |  |
| message | [string](#string) |  | Human-readable message for status |






## SetPositionPIDGainRequest {#rb-api-SetPositionPIDGainRequest}

### SetPositionPIDGainRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  |  |
| p-gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |
| i-gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |
| d-gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |






## SetPositionPIDGainResponse {#rb-api-SetPositionPIDGainResponse}

### SetPositionPIDGainResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [SetPositionPIDGainResponse.Status](#rb-api-SetPositionPIDGainResponse-Status) |  |  |
| message | [string](#string) |  | Human-readable message for status |





 


## BrakeEngageResponse-Status {#rb-api-BrakeEngageResponse-Status}

### BrakeEngageResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-UNKNOWN | 0 |  |
| STATUS-SUCCESS | 1 |  |
| STATUS-INTERNAL-ERROR | 2 |  |



## BrakeReleaseResponse-Status {#rb-api-BrakeReleaseResponse-Status}

### BrakeReleaseResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-UNKNOWN | 0 |  |
| STATUS-SUCCESS | 1 |  |
| STATUS-INTERNAL-ERROR | 2 |  |



## GetPositionPIDGainRequest-TargetComponent {#rb-api-GetPositionPIDGainRequest-TargetComponent}

### GetPositionPIDGainRequest.TargetComponent


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| TORSO | 1 |  |
| RIGHT-ARM | 2 |  |
| LEFT-ARM | 3 |  |
| HEAD | 4 |  |



## HomeOffsetResetResponse-Status {#rb-api-HomeOffsetResetResponse-Status}

### HomeOffsetResetResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-UNKNOWN | 0 |  |
| STATUS-SUCCESS | 1 |  |
| STATUS-INTERNAL-ERROR | 2 |  |



## ServoOnResponse-Status {#rb-api-ServoOnResponse-Status}

### ServoOnResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-UNKNOWN | 0 |  |
| STATUS-SUCCESS | 1 |  |
| STATUS-INTERNAL-ERROR | 2 |  |



## SetPositionPIDGainResponse-Status {#rb-api-SetPositionPIDGainResponse-Status}

### SetPositionPIDGainResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-UNKNOWN | 0 |  |
| STATUS-SUCCESS | 1 |  |
| STATUS-INTERNAL-ERROR | 2 |  |


 

 

 



<a name="rb-api-joint-operation-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/joint-operation-service.proto


 

 

 


## JointOperationService {#rb-api-JointOperationService}

### JointOperationService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ServoOn | [ServoOnRequest](#rb-api-ServoOnRequest) | [ServoOnResponse](#rb-api-ServoOnResponse) ||
| BrakeEngage | [BrakeEngageRequest](#rb-api-BrakeEngageRequest) | [BrakeEngageResponse](#rb-api-BrakeEngageResponse) |  |
| BrakeRelease | [BrakeReleaseRequest](#rb-api-BrakeReleaseRequest) | [BrakeReleaseResponse](#rb-api-BrakeReleaseResponse) |  |
| HomeOffsetReset | [HomeOffsetResetRequest](#rb-api-HomeOffsetResetRequest) | [HomeOffsetResetResponse](#rb-api-HomeOffsetResetResponse) |  |
| GetPositionPIDGain | [GetPositionPIDGainRequest](#rb-api-GetPositionPIDGainRequest) | [GetPositionPIDGainResponse](#rb-api-GetPositionPIDGainResponse) |  |
| SetPositionPIDGain | [SetPositionPIDGainRequest](#rb-api-SetPositionPIDGainRequest) | [SetPositionPIDGainResponse](#rb-api-SetPositionPIDGainResponse) |  |

 



<a name="rb-api-log-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/log.proto



## GetLastLogRequest {#rb-api-GetLastLogRequest}

### GetLastLogRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| log-count | [int32](#int32) |  |  |






## GetLastLogResponse {#rb-api-GetLastLogResponse}

### GetLastLogResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| logs | [Log](#rb-api-Log) | repeated |  |






## GetLogStreamRequest {#rb-api-GetLogStreamRequest}

### GetLogStreamRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| update-rate | [double](#double) |  | Hz |






## GetLogStreamResponse {#rb-api-GetLogStreamResponse}

### GetLogStreamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| logs | [Log](#rb-api-Log) | repeated |  |






## Log {#rb-api-Log}

### Log



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| robot-system-timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| level | [Log.Level](#rb-api-Log-Level) |  |  |
| message | [string](#string) |  |  |






## SetLogLevelRequest {#rb-api-SetLogLevelRequest}

### SetLogLevelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| level | [Log.Level](#rb-api-Log-Level) |  |  |






## SetLogLevelResponse {#rb-api-SetLogLevelResponse}

### SetLogLevelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 


## Log-Level {#rb-api-Log-Level}

### Log.Level


| Name | Number | Description |
| ---- | ------ | ----------- |
| LEVEL-TRACE | 0 |  |
| LEVEL-DEBUG | 1 |  |
| LEVEL-INFO | 2 |  |
| LEVEL-WARN | 3 |  |
| LEVEL-ERROR | 4 |  |
| LEVEL-CRITICAL | 5 |  |


 

 

 



<a name="rb-api-log-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/log-service.proto


 

 

 


## LogService {#rb-api-LogService}

### LogService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLastLog | [GetLastLogRequest](#rb-api-GetLastLogRequest) | [GetLastLogResponse](#rb-api-GetLastLogResponse) |  |
| GetLogStream | [GetLogStreamRequest](#rb-api-GetLogStreamRequest) | [GetLogStreamResponse](#rb-api-GetLogStreamResponse) stream |  |
| SetLogLevel | [SetLogLevelRequest](#rb-api-SetLogLevelRequest) | [SetLogLevelResponse](#rb-api-SetLogLevelResponse) |  |

 



<a name="rb-api-mobility-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/mobility-command.proto



## MobilityCommand {#rb-api-MobilityCommand}

### MobilityCommand







## MobilityCommand-Feedback {#rb-api-MobilityCommand-Feedback}

### MobilityCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint-velocity-command-feedback | [JointVelocityCommand.Feedback](#rb-api-JointVelocityCommand-Feedback) |  |  |
| se2-velocity-command-feedback | [SE2VelocityCommand.Feedback](#rb-api-SE2VelocityCommand-Feedback) |  |  |






## MobilityCommand-Request {#rb-api-MobilityCommand-Request}

### MobilityCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint-velocity-command | [JointVelocityCommand.Request](#rb-api-JointVelocityCommand-Request) |  |  |
| se2-velocity-command | [SE2VelocityCommand.Request](#rb-api-SE2VelocityCommand-Request) |  |  |





 

 

 

 



<a name="rb-api-parameter-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/parameter.proto



## FactoryResetAllParametersRequest {#rb-api-FactoryResetAllParametersRequest}

### FactoryResetAllParametersRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## FactoryResetAllParametersResponse {#rb-api-FactoryResetAllParametersResponse}

### FactoryResetAllParametersResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## FactoryResetParameterRequest {#rb-api-FactoryResetParameterRequest}

### FactoryResetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#string) |  |  |






## FactoryResetParameterResponse {#rb-api-FactoryResetParameterResponse}

### FactoryResetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## GetParameterListRequest {#rb-api-GetParameterListRequest}

### GetParameterListRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## GetParameterListResponse {#rb-api-GetParameterListResponse}

### GetParameterListResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| parameters | [GetParameterListResponse.ParameterType](#rb-api-GetParameterListResponse-ParameterType) | repeated |  |






## GetParameterListResponse-ParameterType {#rb-api-GetParameterListResponse-ParameterType}

### GetParameterListResponse.ParameterType



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| type | [int32](#int32) |  | Type of parameter 0: int 1: double 2: std::string 3: std::array&lt;double, 3&gt; 4: std::array&lt;double, 6&gt; 5: std::array&lt;double, 7&gt; |






## GetParameterRequest {#rb-api-GetParameterRequest}

### GetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#string) |  |  |






## GetParameterResponse {#rb-api-GetParameterResponse}

### GetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| parameter | [string](#string) |  |  |






## ResetAllParametersRequest {#rb-api-ResetAllParametersRequest}

### ResetAllParametersRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## ResetAllParametersResponse {#rb-api-ResetAllParametersResponse}

### ResetAllParametersResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## ResetAllParametersToDefaultRequest {#rb-api-ResetAllParametersToDefaultRequest}

### ResetAllParametersToDefaultRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## ResetAllParametersToDefaultResponse {#rb-api-ResetAllParametersToDefaultResponse}

### ResetAllParametersToDefaultResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## ResetParameterRequest {#rb-api-ResetParameterRequest}

### ResetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#string) |  |  |






## ResetParameterResponse {#rb-api-ResetParameterResponse}

### ResetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## ResetParameterToDefaultRequest {#rb-api-ResetParameterToDefaultRequest}

### ResetParameterToDefaultRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#string) |  |  |






## ResetParameterToDefaultResponse {#rb-api-ResetParameterToDefaultResponse}

### ResetParameterToDefaultResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## SetParameterRequest {#rb-api-SetParameterRequest}

### SetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#string) |  |  |
| parameter | [string](#string) |  |  |






## SetParameterResponse {#rb-api-SetParameterResponse}

### SetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 

 

 

 



<a name="rb-api-parameter-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/parameter-service.proto


 

 

 


## ParameterService {#rb-api-ParameterService}

### ParameterService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| FactoryResetAllParameters | [FactoryResetAllParametersRequest](#rb-api-FactoryResetAllParametersRequest) | [FactoryResetAllParametersResponse](#rb-api-FactoryResetAllParametersResponse) |  |
| FactoryResetParameter | [FactoryResetParameterRequest](#rb-api-FactoryResetParameterRequest) | [FactoryResetParameterResponse](#rb-api-FactoryResetParameterResponse) |  |
| ResetAllParameters | [ResetAllParametersRequest](#rb-api-ResetAllParametersRequest) | [ResetAllParametersResponse](#rb-api-ResetAllParametersResponse) |  |
| ResetParameter | [ResetParameterRequest](#rb-api-ResetParameterRequest) | [ResetParameterResponse](#rb-api-ResetParameterResponse) |  |
| GetParameter | [GetParameterRequest](#rb-api-GetParameterRequest) | [GetParameterResponse](#rb-api-GetParameterResponse) |  |
| SetParameter | [SetParameterRequest](#rb-api-SetParameterRequest) | [SetParameterResponse](#rb-api-SetParameterResponse) |  |
| GetParameterList | [GetParameterListRequest](#rb-api-GetParameterListRequest) | [GetParameterListResponse](#rb-api-GetParameterListResponse) |  |
| ResetAllParametersToDefault | [ResetAllParametersToDefaultRequest](#rb-api-ResetAllParametersToDefaultRequest) | [ResetAllParametersToDefaultResponse](#rb-api-ResetAllParametersToDefaultResponse) | Deprecated |
| ResetParameterToDefault | [ResetParameterToDefaultRequest](#rb-api-ResetParameterToDefaultRequest) | [ResetParameterToDefaultResponse](#rb-api-ResetParameterToDefaultResponse) | Deprecated |

 



<a name="rb-api-ping-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/ping.proto



## PingRequest {#rb-api-PingRequest}

### PingRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## PingResponse {#rb-api-PingResponse}

### PingResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 

 

 

 



<a name="rb-api-ping-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/ping-service.proto


 

 

 


## PingService {#rb-api-PingService}

### PingService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Ping | [PingRequest](#rb-api-PingRequest) | [PingResponse](#rb-api-PingResponse) |  |

 



<a name="rb-api-power-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/power.proto



## JointCommandRequest {#rb-api-JointCommandRequest}

### JointCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  | Motor ID |
| command | [JointCommandRequest.Command](#rb-api-JointCommandRequest-Command) |  |  |






## JointCommandResponse {#rb-api-JointCommandResponse}

### JointCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [JointCommandResponse.Status](#rb-api-JointCommandResponse-Status) |  |  |
| message | [string](#string) |  | Human-readable message for status |






## PowerCommandRequest {#rb-api-PowerCommandRequest}

### PowerCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  | Power ID |
| command | [PowerCommandRequest.Command](#rb-api-PowerCommandRequest-Command) |  |  |






## PowerCommandResponse {#rb-api-PowerCommandResponse}

### PowerCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [PowerCommandResponse.Status](#rb-api-PowerCommandResponse-Status) |  |  |
| message | [string](#string) |  | Human-readable message for status |






## ToolFlangePowerCommandRequest {#rb-api-ToolFlangePowerCommandRequest}

### ToolFlangePowerCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#string) |  | Tool Flange name |
| command | [ToolFlangePowerCommandRequest.Command](#rb-api-ToolFlangePowerCommandRequest-Command) |  |  |






## ToolFlangePowerCommandResponse {#rb-api-ToolFlangePowerCommandResponse}

### ToolFlangePowerCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |





 


## JointCommandRequest-Command {#rb-api-JointCommandRequest-Command}

### JointCommandRequest.Command
Modes for joint/motor command

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND-UNKNOWN | 0 |  |
| COMMAND-SERVO-ON | 1 |  |
| COMMAND-BRAKE-ENGAGE | 2 |  |
| COMMAND-BRAKE-RELEASE | 3 |  |
| COMMAND-HOME-OFFSET-RST | 4 |  |



## JointCommandResponse-Status {#rb-api-JointCommandResponse-Status}

### JointCommandResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-UNKNOWN | 0 |  |
| STATUS-SUCCESS | 1 |  |
| STATUS-INTERNAL-ERROR | 2 |  |



## PowerCommandRequest-Command {#rb-api-PowerCommandRequest-Command}

### PowerCommandRequest.Command
Power command

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND-UNKNOWN | 0 |  |
| COMMAND-POWER-ON | 1 |  |
| COMMAND-POWER-OFF | 2 |  |



## PowerCommandResponse-Status {#rb-api-PowerCommandResponse-Status}

### PowerCommandResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-UNKNOWN | 0 |  |
| STATUS-SUCCESS | 1 |  |
| STATUS-INTERNAL-ERROR | 2 |  |



## ToolFlangePowerCommandRequest-Command {#rb-api-ToolFlangePowerCommandRequest-Command}

### ToolFlangePowerCommandRequest.Command


| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND-UNKNOWN | 0 |  |
| COMMAND-POWER-OFF | 1 |  |
| COMMAND-POWER-12V | 2 |  |
| COMMAND-POWER-24V | 3 |  |


 

 

 



<a name="rb-api-power-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/power-service.proto


 

 

 


## PowerService {#rb-api-PowerService}

### PowerService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PowerCommand | [PowerCommandRequest](#rb-api-PowerCommandRequest) | [PowerCommandResponse](#rb-api-PowerCommandResponse) | Control power of the robot |
| JointCommand | [JointCommandRequest](#rb-api-JointCommandRequest) | [JointCommandResponse](#rb-api-JointCommandResponse) | Joint command |
| ToolFlangePowerCommand | [ToolFlangePowerCommandRequest](#rb-api-ToolFlangePowerCommandRequest) | [ToolFlangePowerCommandResponse](#rb-api-ToolFlangePowerCommandResponse) | Tool Flange |

 



<a name="rb-api-robot-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/robot-command.proto



## RobotCommand {#rb-api-RobotCommand}

### RobotCommand







## RobotCommand-Feedback {#rb-api-RobotCommand-Feedback}

### RobotCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| whole-body-command-feedback | [WholeBodyCommand.Feedback](#rb-api-WholeBodyCommand-Feedback) |  |  |
| component-based-command-feedback | [ComponentBasedCommand.Feedback](#rb-api-ComponentBasedCommand-Feedback) |  |  |
| jog-command-feedback | [JogCommand.Feedback](#rb-api-JogCommand-Feedback) |  |  |
| status | [RobotCommand.Feedback.Status](#rb-api-RobotCommand-Feedback-Status) |  |  |
| finish-code | [RobotCommand.Feedback.FinishCode](#rb-api-RobotCommand-Feedback-FinishCode) |  |  |






## RobotCommand-Request {#rb-api-RobotCommand-Request}

### RobotCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| whole-body-command | [WholeBodyCommand.Request](#rb-api-WholeBodyCommand-Request) |  |  |
| component-based-command | [ComponentBasedCommand.Request](#rb-api-ComponentBasedCommand-Request) |  |  |
| jog-command | [JogCommand.Request](#rb-api-JogCommand-Request) |  |  |






## RobotCommandRequest {#rb-api-RobotCommandRequest}

### RobotCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| robot-command | [RobotCommand.Request](#rb-api-RobotCommand-Request) |  |  |
| priority | [int32](#int32) |  |  |






## RobotCommandResponse {#rb-api-RobotCommandResponse}

### RobotCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| feedback | [RobotCommand.Feedback](#rb-api-RobotCommand-Feedback) |  |  |





 


## RobotCommand-Feedback-FinishCode {#rb-api-RobotCommand-Feedback-FinishCode}

### RobotCommand.Feedback.FinishCode


| Name | Number | Description |
| ---- | ------ | ----------- |
| FINISH-CODE-UNKNOWN | 0 |  |
| FINISH-CODE-OK | 1 |  |
| FINISH-CODE-CANCELED | 2 |  |
| FINISH-CODE-PREEMPTED | 3 |  |
| FINISH-CODE-INITIALIZED-FAILED | 4 |  |
| FINISH-CODE-CONTROL-MANAGER-IDLE | 5 |  |
| FINISH-CODE-CONTROL-MANAGER-FAULT | 6 |  |
| FINISH-CODE-UNEXPECTED-STATE | 7 |  |



## RobotCommand-Feedback-Status {#rb-api-RobotCommand-Feedback-Status}

### RobotCommand.Feedback.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS-IDLE | 0 |  |
| STATUS-INITIALIZING | 1 |  |
| STATUS-RUNNING | 2 |  |
| STATUS-FINISHED | 3 |  |


 

 

 



<a name="rb-api-robot-command-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/robot-command-service.proto


 

 

 


## RobotCommandService {#rb-api-RobotCommandService}

### RobotCommandService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| RobotCommand | [RobotCommandRequest](#rb-api-RobotCommandRequest) | [RobotCommandResponse](#rb-api-RobotCommandResponse) | In case of sending and receiving a single command |
| RobotCommandStream | [RobotCommandRequest](#rb-api-RobotCommandRequest) stream | [RobotCommandResponse](#rb-api-RobotCommandResponse) stream | In case of sending and receiving commands continuously |

 



<a name="rb-api-robot-info-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/robot-info.proto



## BatteryInfo {#rb-api-BatteryInfo}

### BatteryInfo







## EMOInfo {#rb-api-EMOInfo}

### EMOInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






## GetRobotInfoRequest {#rb-api-GetRobotInfoRequest}

### GetRobotInfoRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## GetRobotInfoResponse {#rb-api-GetRobotInfoResponse}

### GetRobotInfoResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| robot-info | [RobotInfo](#rb-api-RobotInfo) |  |  |






## GetRobotModelRequest {#rb-api-GetRobotModelRequest}

### GetRobotModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## GetRobotModelResponse {#rb-api-GetRobotModelResponse}

### GetRobotModelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| model | [string](#string) |  |  |






## ImportRobotModelRequest {#rb-api-ImportRobotModelRequest}

### ImportRobotModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#string) |  |  |
| model | [string](#string) |  |  |






## ImportRobotModelResponse {#rb-api-ImportRobotModelResponse}

### ImportRobotModelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## JointInfo {#rb-api-JointInfo}

### JointInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| has-brake | [bool](#bool) |  |  |






## PowerInfo {#rb-api-PowerInfo}

### PowerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






## RobotInfo {#rb-api-RobotInfo}

### RobotInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot-version | [string](#string) |  |  |
| sdk-commit-id | [string](#string) |  |  |
| battery-info | [BatteryInfo](#rb-api-BatteryInfo) |  |  |
| power-infos | [PowerInfo](#rb-api-PowerInfo) | repeated |  |
| emo-infos | [EMOInfo](#rb-api-EMOInfo) | repeated |  |
| degree-of-freedom | [int32](#int32) |  |  |
| joint-infos | [JointInfo](#rb-api-JointInfo) | repeated |  |
| mobility-joint-idx | [uint32](#uint32) | repeated |  |
| body-joint-idx | [uint32](#uint32) | repeated |  |
| head-joint-idx | [uint32](#uint32) | repeated |  |





 

 

 

 



<a name="rb-api-robot-info-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/robot-info-service.proto


 

 

 


## RobotInfoService {#rb-api-RobotInfoService}

### RobotInfoService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRobotInfo | [GetRobotInfoRequest](#rb-api-GetRobotInfoRequest) | [GetRobotInfoResponse](#rb-api-GetRobotInfoResponse) |  |
| GetRobotModel | [GetRobotModelRequest](#rb-api-GetRobotModelRequest) | [GetRobotModelResponse](#rb-api-GetRobotModelResponse) |  |
| ImportRobotModel | [ImportRobotModelRequest](#rb-api-ImportRobotModelRequest) | [ImportRobotModelResponse](#rb-api-ImportRobotModelResponse) |  |

 



<a name="rb-api-robot-state-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/robot-state.proto



## BatteryState {#rb-api-BatteryState}

### BatteryState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| voltage | [double](#double) |  | V |
| current | [double](#double) |  | Amp |
| level-percent | [double](#double) |  | % |






## Collision {#rb-api-Collision}

### Collision



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| link1 | [string](#string) |  |  |
| link2 | [string](#string) |  |  |
| position1 | [Vec3](#rb-api-Vec3) |  |  |
| position2 | [Vec3](#rb-api-Vec3) |  |  |
| distance | [double](#double) |  |  |






## EMOState {#rb-api-EMOState}

### EMOState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [EMOState.State](#rb-api-EMOState-State) |  |  |






## FTSensorData {#rb-api-FTSensorData}

### FTSensorData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time-since-last-update | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| force | [Vec3](#rb-api-Vec3) |  |  |
| torque | [Vec3](#rb-api-Vec3) |  |  |






## GetControlManagerStateRequest {#rb-api-GetControlManagerStateRequest}

### GetControlManagerStateRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## GetControlManagerStateResponse {#rb-api-GetControlManagerStateResponse}

### GetControlManagerStateResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| control-manager-state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






## GetRobotStateRequest {#rb-api-GetRobotStateRequest}

### GetRobotStateRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |






## GetRobotStateResponse {#rb-api-GetRobotStateResponse}

### GetRobotStateResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| robot-state | [RobotState](#rb-api-RobotState) |  |  |
| control-manager-state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






## GetRobotStateStreamRequest {#rb-api-GetRobotStateStreamRequest}

### GetRobotStateStreamRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| update-rate | [double](#double) |  | Hz |






## GetRobotStateStreamResponse {#rb-api-GetRobotStateStreamResponse}

### GetRobotStateStreamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| robot-state | [RobotState](#rb-api-RobotState) |  |  |
| control-manager-state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






## JointState {#rb-api-JointState}

### JointState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is-ready | [bool](#bool) |  |  |
| fet-state | [JointState.FETState](#rb-api-JointState-FETState) |  |  |
| run-state | [JointState.RunState](#rb-api-JointState-RunState) |  |  |
| init-state | [JointState.InitializationState](#rb-api-JointState-InitializationState) |  |  |
| motor-type | [uint32](#uint32) |  | MOTOR STATE |
| motor-state | [uint64](#uint64) |  |  |
| time-since-last-update | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| power-on | [bool](#bool) |  |  |
| position | [double](#double) |  |  |
| velocity | [double](#double) |  |  |
| current | [double](#double) |  |  |
| torque | [double](#double) |  |  |
| target-position | [double](#double) |  |  |
| target-velocity | [double](#double) |  |  |
| target-feedback-gain | [uint32](#uint32) |  |  |
| target-feedforward-torque | [double](#double) |  |  |
| temperature | [int32](#int32) |  |  |






## PowerState {#rb-api-PowerState}

### PowerState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [PowerState.State](#rb-api-PowerState-State) |  |  |
| voltage | [double](#double) |  |  |






## ResetOdometryRequest {#rb-api-ResetOdometryRequest}

### ResetOdometryRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request-header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| initial-pose | [SE2Pose](#rb-api-SE2Pose) |  |  |






## ResetOdometryResponse {#rb-api-ResetOdometryResponse}

### ResetOdometryResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response-header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






## RobotState {#rb-api-RobotState}

### RobotState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| system-stat | [SystemStat](#rb-api-SystemStat) |  | System Statistic |
| battery-state | [BatteryState](#rb-api-BatteryState) |  | Battery State |
| power-states | [PowerState](#rb-api-PowerState) | repeated | Power State |
| emo-states | [EMOState](#rb-api-EMOState) | repeated | EMO state |
| joint-states | [JointState](#rb-api-JointState) | repeated | Joint State |
| tool-flange-right | [ToolFlangeState](#rb-api-ToolFlangeState) |  | Tool Flange State |
| tool-flange-left | [ToolFlangeState](#rb-api-ToolFlangeState) |  |  |
| ft-sensor-right | [FTSensorData](#rb-api-FTSensorData) |  | Force Torque Sensor |
| ft-sensor-left | [FTSensorData](#rb-api-FTSensorData) |  |  |
| is-ready | [double](#double) | repeated |  |
| position | [double](#double) | repeated |  |
| velocity | [double](#double) | repeated |  |
| current | [double](#double) | repeated |  |
| torque | [double](#double) | repeated |  |
| target-position | [double](#double) | repeated |  |
| target-velocity | [double](#double) | repeated |  |
| target-feedback-gain | [uint32](#uint32) | repeated |  |
| target-feedforward-torque | [double](#double) | repeated |  |
| odometry | [SE2Pose](#rb-api-SE2Pose) |  | Mobility State |
| center-of-mass | [Vec3](#rb-api-Vec3) |  | Center Of Mass

Position of center of mass with respect t base link |
| collisions | [Collision](#rb-api-Collision) | repeated | Collisions |






## SystemStat {#rb-api-SystemStat}

### SystemStat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cpu-usage | [double](#double) |  | % |
| memory-usage | [double](#double) |  | % |
| uptime | [double](#double) |  | sec |
| program-uptime | [double](#double) |  | sec |






## ToolFlangeState {#rb-api-ToolFlangeState}

### ToolFlangeState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time-since-last-update | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| gyro | [Vec3](#rb-api-Vec3) |  |  |
| acceleration | [Vec3](#rb-api-Vec3) |  |  |
| switch-A | [bool](#bool) |  |  |
| output-voltage | [int32](#int32) |  |  |





 


## EMOState-State {#rb-api-EMOState-State}

### EMOState.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATE-RELEASED | 0 |  |
| STATE-PRESSED | 1 |  |



## JointState-FETState {#rb-api-JointState-FETState}

### JointState.FETState


| Name | Number | Description |
| ---- | ------ | ----------- |
| FET-STATE-UNKNOWN | 0 |  |
| FET-STATE-ON | 1 |  |
| FET-STATE-OFF | 2 |  |



## JointState-InitializationState {#rb-api-JointState-InitializationState}

### JointState.InitializationState


| Name | Number | Description |
| ---- | ------ | ----------- |
| INIT-STATE-UNKNOWN | 0 |  |
| INIT-STATE-INITIALIZED | 1 |  |
| INIT-STATE-UNINITIALIZED | 2 |  |



## JointState-RunState {#rb-api-JointState-RunState}

### JointState.RunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| RUN-STATE-UNKNOWN | 0 |  |
| RUN-STATE-CONTROL-ON | 1 |  |
| RUN-STATE-CONTROL-OFF | 2 |  |



## PowerState-State {#rb-api-PowerState-State}

### PowerState.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATE-UNKNOWN | 0 |  |
| STATE-POWER-ON | 1 |  |
| STATE-POWER-OFF | 2 |  |


 

 

 



<a name="rb-api-robot-state-service-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/robot-state-service.proto


 

 

 


## RobotStateService {#rb-api-RobotStateService}

### RobotStateService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRobotState | [GetRobotStateRequest](#rb-api-GetRobotStateRequest) | [GetRobotStateResponse](#rb-api-GetRobotStateResponse) |  |
| GetRobotStateStream | [GetRobotStateStreamRequest](#rb-api-GetRobotStateStreamRequest) | [GetRobotStateStreamResponse](#rb-api-GetRobotStateStreamResponse) stream |  |
| GetControlManagerState | [GetControlManagerStateRequest](#rb-api-GetControlManagerStateRequest) | [GetControlManagerStateResponse](#rb-api-GetControlManagerStateResponse) |  |
| ResetOdometry | [ResetOdometryRequest](#rb-api-ResetOdometryRequest) | [ResetOdometryResponse](#rb-api-ResetOdometryResponse) |  |

 



<a name="rb-api-torso-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/torso-command.proto



## TorsoCommand {#rb-api-TorsoCommand}

### TorsoCommand







## TorsoCommand-Feedback {#rb-api-TorsoCommand-Feedback}

### TorsoCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint-position-command-feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |
| gravity-compensation-command-feedback | [GravityCompensationCommand.Feedback](#rb-api-GravityCompensationCommand-Feedback) |  |  |
| cartesian-command-feedback | [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback) |  |  |
| impedance-control-command-feedback | [ImpedanceControlCommand.Feedback](#rb-api-ImpedanceControlCommand-Feedback) |  |  |
| optimal-control-command-feedback | [OptimalControlCommand.Feedback](#rb-api-OptimalControlCommand-Feedback) |  |  |






## TorsoCommand-Request {#rb-api-TorsoCommand-Request}

### TorsoCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint-position-command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |
| gravity-compensation-command | [GravityCompensationCommand.Request](#rb-api-GravityCompensationCommand-Request) |  |  |
| cartesian-command | [CartesianCommand.Request](#rb-api-CartesianCommand-Request) |  |  |
| impedance-control-command | [ImpedanceControlCommand.Request](#rb-api-ImpedanceControlCommand-Request) |  |  |
| optimal-control-command | [OptimalControlCommand.Request](#rb-api-OptimalControlCommand-Request) |  |  |





 

 

 

 



<a name="rb-api-whole-body-command-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## rb/api/whole-body-command.proto



## WholeBodyCommand {#rb-api-WholeBodyCommand}

### WholeBodyCommand







## WholeBodyCommand-Feedback {#rb-api-WholeBodyCommand-Feedback}

### WholeBodyCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header-feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| stop-command-feedback | [StopCommand.Feedback](#rb-api-StopCommand-Feedback) |  |  |
| real-time-control-command-feedback | [RealTimeControlCommand.Feedback](#rb-api-RealTimeControlCommand-Feedback) |  |  |






## WholeBodyCommand-Request {#rb-api-WholeBodyCommand-Request}

### WholeBodyCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command-header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| stop-command | [StopCommand.Request](#rb-api-StopCommand-Request) |  |  |
| real-time-control-command | [RealTimeControlCommand.Request](#rb-api-RealTimeControlCommand-Request) |  |  |





 

 

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

