# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [rb/api/arm_command.proto](#rb_api_arm_command-proto)
    - [ArmCommand](#rb-api-ArmCommand)
    - [ArmCommand.Feedback](#rb-api-ArmCommand-Feedback)
    - [ArmCommand.Request](#rb-api-ArmCommand-Request)
  
- [rb/api/basic_command.proto](#rb_api_basic_command-proto)
    - [CartesianCommand](#rb-api-CartesianCommand)
    - [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback)
    - [CartesianCommand.JointPositionTarget](#rb-api-CartesianCommand-JointPositionTarget)
    - [CartesianCommand.Request](#rb-api-CartesianCommand-Request)
    - [CartesianCommand.SE3PoseTarget](#rb-api-CartesianCommand-SE3PoseTarget)
    - [CartesianCommand.TrackingError](#rb-api-CartesianCommand-TrackingError)
    - [CartesianImpedanceControlCommand](#rb-api-CartesianImpedanceControlCommand)
    - [CartesianImpedanceControlCommand.Feedback](#rb-api-CartesianImpedanceControlCommand-Feedback)
    - [CartesianImpedanceControlCommand.JointLimit](#rb-api-CartesianImpedanceControlCommand-JointLimit)
    - [CartesianImpedanceControlCommand.JointPositionTarget](#rb-api-CartesianImpedanceControlCommand-JointPositionTarget)
    - [CartesianImpedanceControlCommand.NullspaceJointTarget](#rb-api-CartesianImpedanceControlCommand-NullspaceJointTarget)
    - [CartesianImpedanceControlCommand.Request](#rb-api-CartesianImpedanceControlCommand-Request)
    - [CartesianImpedanceControlCommand.SE3PoseTarget](#rb-api-CartesianImpedanceControlCommand-SE3PoseTarget)
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
    - [JointGroupPositionCommand](#rb-api-JointGroupPositionCommand)
    - [JointGroupPositionCommand.Feedback](#rb-api-JointGroupPositionCommand-Feedback)
    - [JointGroupPositionCommand.Request](#rb-api-JointGroupPositionCommand-Request)
    - [JointImpedanceControlCommand](#rb-api-JointImpedanceControlCommand)
    - [JointImpedanceControlCommand.Feedback](#rb-api-JointImpedanceControlCommand-Feedback)
    - [JointImpedanceControlCommand.Request](#rb-api-JointImpedanceControlCommand-Request)
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
  
- [rb/api/body_command.proto](#rb_api_body_command-proto)
    - [BodyCommand](#rb-api-BodyCommand)
    - [BodyCommand.Feedback](#rb-api-BodyCommand-Feedback)
    - [BodyCommand.Request](#rb-api-BodyCommand-Request)
  
- [rb/api/body_component_based_command.proto](#rb_api_body_component_based_command-proto)
    - [BodyComponentBasedCommand](#rb-api-BodyComponentBasedCommand)
    - [BodyComponentBasedCommand.Feedback](#rb-api-BodyComponentBasedCommand-Feedback)
    - [BodyComponentBasedCommand.Request](#rb-api-BodyComponentBasedCommand-Request)
  
- [rb/api/color.proto](#rb_api_color-proto)
    - [Color](#rb-api-Color)
  
- [rb/api/command_header.proto](#rb_api_command_header-proto)
    - [CommandHeader](#rb-api-CommandHeader)
    - [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback)
    - [CommandHeader.Request](#rb-api-CommandHeader-Request)
  
- [rb/api/component_based_command.proto](#rb_api_component_based_command-proto)
    - [ComponentBasedCommand](#rb-api-ComponentBasedCommand)
    - [ComponentBasedCommand.Feedback](#rb-api-ComponentBasedCommand-Feedback)
    - [ComponentBasedCommand.Request](#rb-api-ComponentBasedCommand-Request)
  
- [rb/api/control_manager.proto](#rb_api_control_manager-proto)
    - [CancelControlRequest](#rb-api-CancelControlRequest)
    - [CancelControlResponse](#rb-api-CancelControlResponse)
    - [ControlManagerCommandRequest](#rb-api-ControlManagerCommandRequest)
    - [ControlManagerCommandResponse](#rb-api-ControlManagerCommandResponse)
    - [ControlManagerState](#rb-api-ControlManagerState)
    - [GetTimeScaleRequest](#rb-api-GetTimeScaleRequest)
    - [GetTimeScaleResponse](#rb-api-GetTimeScaleResponse)
    - [SetTimeScaleRequest](#rb-api-SetTimeScaleRequest)
    - [SetTimeScaleResponse](#rb-api-SetTimeScaleResponse)
    - [WaitForControlReadyRequest](#rb-api-WaitForControlReadyRequest)
    - [WaitForControlReadyResponse](#rb-api-WaitForControlReadyResponse)
  
    - [ControlManagerCommandRequest.Command](#rb-api-ControlManagerCommandRequest-Command)
    - [ControlManagerState.ControlState](#rb-api-ControlManagerState-ControlState)
    - [ControlManagerState.State](#rb-api-ControlManagerState-State)
  
- [rb/api/control_manager_service.proto](#rb_api_control_manager_service-proto)
    - [ControlManagerService](#rb-api-ControlManagerService)
  
- [rb/api/file.proto](#rb_api_file-proto)
    - [DownloadFileRequest](#rb-api-DownloadFileRequest)
    - [DownloadFileResponse](#rb-api-DownloadFileResponse)
  
- [rb/api/file_service.proto](#rb_api_file_service-proto)
    - [FileService](#rb-api-FileService)
  
- [rb/api/gamepad.proto](#rb_api_gamepad-proto)
    - [Gamepad](#rb-api-Gamepad)
    - [UploadGamepadDataRequest](#rb-api-UploadGamepadDataRequest)
    - [UploadGamepadDataResponse](#rb-api-UploadGamepadDataResponse)
  
- [rb/api/gamepad_service.proto](#rb_api_gamepad_service-proto)
    - [GamepadService](#rb-api-GamepadService)
  
- [rb/api/geometry.proto](#rb_api_geometry-proto)
    - [EulerAngleZYX](#rb-api-EulerAngleZYX)
    - [Inertia](#rb-api-Inertia)
    - [Inertial](#rb-api-Inertial)
    - [Quaternion](#rb-api-Quaternion)
    - [SE2Pose](#rb-api-SE2Pose)
    - [SE2Velocity](#rb-api-SE2Velocity)
    - [SE3Pose](#rb-api-SE3Pose)
    - [Vec2](#rb-api-Vec2)
    - [Vec3](#rb-api-Vec3)
  
- [rb/api/gripper_command.proto](#rb_api_gripper_command-proto)
    - [GripperInitializationRequest](#rb-api-GripperInitializationRequest)
    - [GripperInitializationResponse](#rb-api-GripperInitializationResponse)
    - [GripperMoveRequest](#rb-api-GripperMoveRequest)
    - [GripperMoveResponse](#rb-api-GripperMoveResponse)
  
- [rb/api/gripper_command_service.proto](#rb_api_gripper_command_service-proto)
    - [GripperCommandService](#rb-api-GripperCommandService)
  
- [rb/api/head_command.proto](#rb_api_head_command-proto)
    - [HeadCommand](#rb-api-HeadCommand)
    - [HeadCommand.Feedback](#rb-api-HeadCommand-Feedback)
    - [HeadCommand.Request](#rb-api-HeadCommand-Request)
  
- [rb/api/header.proto](#rb_api_header-proto)
    - [CommonError](#rb-api-CommonError)
    - [RequestHeader](#rb-api-RequestHeader)
    - [ResponseHeader](#rb-api-ResponseHeader)
  
    - [CommonError.Code](#rb-api-CommonError-Code)
  
- [rb/api/joint_operation.proto](#rb_api_joint_operation-proto)
    - [BrakeEngageRequest](#rb-api-BrakeEngageRequest)
    - [BrakeEngageResponse](#rb-api-BrakeEngageResponse)
    - [BrakeReleaseRequest](#rb-api-BrakeReleaseRequest)
    - [BrakeReleaseResponse](#rb-api-BrakeReleaseResponse)
    - [GetPositionPIDGainRequest](#rb-api-GetPositionPIDGainRequest)
    - [GetPositionPIDGainResponse](#rb-api-GetPositionPIDGainResponse)
    - [HomeOffsetResetRequest](#rb-api-HomeOffsetResetRequest)
    - [HomeOffsetResetResponse](#rb-api-HomeOffsetResetResponse)
    - [PositionPIDGain](#rb-api-PositionPIDGain)
    - [ServoOffRequest](#rb-api-ServoOffRequest)
    - [ServoOffResponse](#rb-api-ServoOffResponse)
    - [ServoOnRequest](#rb-api-ServoOnRequest)
    - [ServoOnResponse](#rb-api-ServoOnResponse)
    - [SetPositionPIDGainRequest](#rb-api-SetPositionPIDGainRequest)
    - [SetPositionPIDGainResponse](#rb-api-SetPositionPIDGainResponse)
    - [SetPresetPositionRequest](#rb-api-SetPresetPositionRequest)
    - [SetPresetPositionResponse](#rb-api-SetPresetPositionResponse)
  
    - [BrakeEngageResponse.Status](#rb-api-BrakeEngageResponse-Status)
    - [BrakeReleaseResponse.Status](#rb-api-BrakeReleaseResponse-Status)
    - [GetPositionPIDGainRequest.TargetComponent](#rb-api-GetPositionPIDGainRequest-TargetComponent)
    - [HomeOffsetResetResponse.Status](#rb-api-HomeOffsetResetResponse-Status)
    - [ServoOffResponse.Status](#rb-api-ServoOffResponse-Status)
    - [ServoOnResponse.Status](#rb-api-ServoOnResponse-Status)
    - [SetPositionPIDGainResponse.Status](#rb-api-SetPositionPIDGainResponse-Status)
  
- [rb/api/joint_operation_service.proto](#rb_api_joint_operation_service-proto)
    - [JointOperationService](#rb-api-JointOperationService)
  
- [rb/api/led.proto](#rb_api_led-proto)
    - [SetLEDColorRequest](#rb-api-SetLEDColorRequest)
    - [SetLEDColorResponse](#rb-api-SetLEDColorResponse)
  
- [rb/api/led_service.proto](#rb_api_led_service-proto)
    - [LEDService](#rb-api-LEDService)
  
- [rb/api/log.proto](#rb_api_log-proto)
    - [GetFaultLogListRequest](#rb-api-GetFaultLogListRequest)
    - [GetFaultLogListResponse](#rb-api-GetFaultLogListResponse)
    - [GetLastLogRequest](#rb-api-GetLastLogRequest)
    - [GetLastLogResponse](#rb-api-GetLastLogResponse)
    - [GetLogStreamRequest](#rb-api-GetLogStreamRequest)
    - [GetLogStreamResponse](#rb-api-GetLogStreamResponse)
    - [Log](#rb-api-Log)
    - [SetLogLevelRequest](#rb-api-SetLogLevelRequest)
    - [SetLogLevelResponse](#rb-api-SetLogLevelResponse)
  
    - [Log.Level](#rb-api-Log-Level)
  
- [rb/api/log_service.proto](#rb_api_log_service-proto)
    - [LogService](#rb-api-LogService)
  
- [rb/api/mobility_command.proto](#rb_api_mobility_command-proto)
    - [MobilityCommand](#rb-api-MobilityCommand)
    - [MobilityCommand.Feedback](#rb-api-MobilityCommand-Feedback)
    - [MobilityCommand.Request](#rb-api-MobilityCommand-Request)
  
- [rb/api/parameter.proto](#rb_api_parameter-proto)
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
  
- [rb/api/parameter_service.proto](#rb_api_parameter_service-proto)
    - [ParameterService](#rb-api-ParameterService)
  
- [rb/api/ping.proto](#rb_api_ping-proto)
    - [PingRequest](#rb-api-PingRequest)
    - [PingResponse](#rb-api-PingResponse)
  
- [rb/api/ping_service.proto](#rb_api_ping_service-proto)
    - [PingService](#rb-api-PingService)
  
- [rb/api/power.proto](#rb_api_power-proto)
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
  
- [rb/api/power_service.proto](#rb_api_power_service-proto)
    - [PowerService](#rb-api-PowerService)
  
- [rb/api/robot_command.proto](#rb_api_robot_command-proto)
    - [RobotCommand](#rb-api-RobotCommand)
    - [RobotCommand.Feedback](#rb-api-RobotCommand-Feedback)
    - [RobotCommand.Request](#rb-api-RobotCommand-Request)
    - [RobotCommandRequest](#rb-api-RobotCommandRequest)
    - [RobotCommandResponse](#rb-api-RobotCommandResponse)
  
    - [RobotCommand.Feedback.FinishCode](#rb-api-RobotCommand-Feedback-FinishCode)
    - [RobotCommand.Feedback.Status](#rb-api-RobotCommand-Feedback-Status)
  
- [rb/api/robot_command_service.proto](#rb_api_robot_command_service-proto)
    - [RobotCommandService](#rb-api-RobotCommandService)
  
- [rb/api/robot_info.proto](#rb_api_robot_info-proto)
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
  
- [rb/api/robot_info_service.proto](#rb_api_robot_info_service-proto)
    - [RobotInfoService](#rb-api-RobotInfoService)
  
- [rb/api/robot_state.proto](#rb_api_robot_state-proto)
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
  
- [rb/api/robot_state_service.proto](#rb_api_robot_state_service-proto)
    - [RobotStateService](#rb-api-RobotStateService)
  
- [rb/api/serial.proto](#rb_api_serial-proto)
    - [GetSerialDeviceListRequest](#rb-api-GetSerialDeviceListRequest)
    - [GetSerialDeviceListResponse](#rb-api-GetSerialDeviceListResponse)
    - [OpenSerialStreamRequest](#rb-api-OpenSerialStreamRequest)
    - [OpenSerialStreamResponse](#rb-api-OpenSerialStreamResponse)
    - [SerialConnectionStatus](#rb-api-SerialConnectionStatus)
    - [SerialDeviceInfo](#rb-api-SerialDeviceInfo)
    - [SerialOpenRequest](#rb-api-SerialOpenRequest)
    - [SerialWriteRequest](#rb-api-SerialWriteRequest)
    - [SerialWriteResult](#rb-api-SerialWriteResult)
  
- [rb/api/serial_service.proto](#rb_api_serial_service-proto)
    - [SerialService](#rb-api-SerialService)
  
- [rb/api/system.proto](#rb_api_system-proto)
    - [ConnectWifiRequest](#rb-api-ConnectWifiRequest)
    - [ConnectWifiResponse](#rb-api-ConnectWifiResponse)
    - [DisconnectWifiRequest](#rb-api-DisconnectWifiRequest)
    - [DisconnectWifiResponse](#rb-api-DisconnectWifiResponse)
    - [GetSystemTimeRequest](#rb-api-GetSystemTimeRequest)
    - [GetSystemTimeResponse](#rb-api-GetSystemTimeResponse)
    - [GetWifiStatusRequest](#rb-api-GetWifiStatusRequest)
    - [GetWifiStatusResponse](#rb-api-GetWifiStatusResponse)
    - [ResetBatteryConfigRequest](#rb-api-ResetBatteryConfigRequest)
    - [ResetBatteryConfigResponse](#rb-api-ResetBatteryConfigResponse)
    - [ResetNetworkSettingRequest](#rb-api-ResetNetworkSettingRequest)
    - [ResetNetworkSettingResponse](#rb-api-ResetNetworkSettingResponse)
    - [ScanWifiRequest](#rb-api-ScanWifiRequest)
    - [ScanWifiResponse](#rb-api-ScanWifiResponse)
    - [SetBatteryConfigRequest](#rb-api-SetBatteryConfigRequest)
    - [SetBatteryConfigResponse](#rb-api-SetBatteryConfigResponse)
    - [SetBatteryLevelRequest](#rb-api-SetBatteryLevelRequest)
    - [SetBatteryLevelResponse](#rb-api-SetBatteryLevelResponse)
    - [SetSystemTimeRequest](#rb-api-SetSystemTimeRequest)
    - [SetSystemTimeResponse](#rb-api-SetSystemTimeResponse)
    - [WifiNetwork](#rb-api-WifiNetwork)
  
- [rb/api/system_service.proto](#rb_api_system_service-proto)
    - [SystemService](#rb-api-SystemService)
  
- [rb/api/tool_flange.proto](#rb_api_tool_flange-proto)
    - [SetToolFlangeDigitalOutputRequest](#rb-api-SetToolFlangeDigitalOutputRequest)
    - [SetToolFlangeDigitalOutputRequest.DualChannel](#rb-api-SetToolFlangeDigitalOutputRequest-DualChannel)
    - [SetToolFlangeDigitalOutputRequest.SingleChannel](#rb-api-SetToolFlangeDigitalOutputRequest-SingleChannel)
    - [SetToolFlangeDigitalOutputResponse](#rb-api-SetToolFlangeDigitalOutputResponse)
  
- [rb/api/tool_flange_service.proto](#rb_api_tool_flange_service-proto)
    - [ToolFlangeService](#rb-api-ToolFlangeService)
  
- [rb/api/torso_command.proto](#rb_api_torso_command-proto)
    - [TorsoCommand](#rb-api-TorsoCommand)
    - [TorsoCommand.Feedback](#rb-api-TorsoCommand-Feedback)
    - [TorsoCommand.Request](#rb-api-TorsoCommand-Request)
  
- [rb/api/whole_body_command.proto](#rb_api_whole_body_command-proto)
    - [WholeBodyCommand](#rb-api-WholeBodyCommand)
    - [WholeBodyCommand.Feedback](#rb-api-WholeBodyCommand-Feedback)
    - [WholeBodyCommand.Request](#rb-api-WholeBodyCommand-Request)
  
- [Scalar Value Types](#scalar-value-types)



(rb_api_arm_command-proto)=
## rb/api/arm_command.proto



(rb-api-armcommand)=
### ArmCommand







(rb-api-armcommand-feedback)=
### ArmCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |
| gravity_compensation_command_feedback | [GravityCompensationCommand.Feedback](#rb-api-GravityCompensationCommand-Feedback) |  |  |
| cartesian_command_feedback | [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback) |  |  |
| impedance_control_command_feedback | [ImpedanceControlCommand.Feedback](#rb-api-ImpedanceControlCommand-Feedback) |  |  |
| joint_impedance_control_command_feedback | [JointImpedanceControlCommand.Feedback](#rb-api-JointImpedanceControlCommand-Feedback) |  |  |
| cartesian_impedance_control_command_feedback | [CartesianImpedanceControlCommand.Feedback](#rb-api-CartesianImpedanceControlCommand-Feedback) |  |  |






(rb-api-armcommand-request)=
### ArmCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint_position_command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](#rb-api-GravityCompensationCommand-Request) |  |  |
| cartesian_command | [CartesianCommand.Request](#rb-api-CartesianCommand-Request) |  |  |
| impedance_control_command | [ImpedanceControlCommand.Request](#rb-api-ImpedanceControlCommand-Request) |  |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](#rb-api-JointImpedanceControlCommand-Request) |  |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](#rb-api-CartesianImpedanceControlCommand-Request) |  |  |





 

 

 

 



(rb_api_basic_command-proto)=
## rb/api/basic_command.proto



(rb-api-cartesiancommand)=
### CartesianCommand







(rb-api-cartesiancommand-feedback)=
### CartesianCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| se3_pose_tracking_errors | [CartesianCommand.TrackingError](#rb-api-CartesianCommand-TrackingError) | repeated |  |
| joint_position_tracking_errors | [double](#scalar-value-types) | repeated |  |
| remain_time | [double](#scalar-value-types) |  |  |
| manipulability | [double](#scalar-value-types) |  |  |






(rb-api-cartesiancommand-jointpositiontarget)=
### CartesianCommand.JointPositionTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| joint_name | [string](#scalar-value-types) |  |  |
| target_position | [double](#scalar-value-types) |  |  |
| velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |






(rb-api-cartesiancommand-request)=
### CartesianCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| targets | [CartesianCommand.SE3PoseTarget](#rb-api-CartesianCommand-SE3PoseTarget) | repeated |  |
| joint_position_targets | [CartesianCommand.JointPositionTarget](#rb-api-CartesianCommand-JointPositionTarget) | repeated |  |
| stop_position_tracking_error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| stop_orientation_tracking_error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| stop_joint_position_tracking_error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |






(rb-api-cartesiancommand-se3posetarget)=
### CartesianCommand.SE3PoseTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](#scalar-value-types) |  |  |
| link_name | [string](#scalar-value-types) |  |  |
| T | [SE3Pose](#rb-api-SE3Pose) |  |  |
| linear_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (m/s) |
| angular_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) |
| acceleration_limit_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default.linear_acceleration_limit * acceleration_limit_scaling default.angular_acceleration_limit * acceleration_limit_scaling

`(0, 1]` |






(rb-api-cartesiancommand-trackingerror)=
### CartesianCommand.TrackingError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position_error | [double](#scalar-value-types) |  |  |
| orientation_error | [double](#scalar-value-types) |  |  |






(rb-api-cartesianimpedancecontrolcommand)=
### CartesianImpedanceControlCommand







(rb-api-cartesianimpedancecontrolcommand-feedback)=
### CartesianImpedanceControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| set_position | [double](#scalar-value-types) | repeated |  |
| remain_time | [double](#scalar-value-types) |  |  |
| manipulability | [double](#scalar-value-types) |  |  |






(rb-api-cartesianimpedancecontrolcommand-jointlimit)=
### CartesianImpedanceControlCommand.JointLimit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| joint_name | [string](#scalar-value-types) |  |  |
| lower | [double](#scalar-value-types) |  |  |
| upper | [double](#scalar-value-types) |  |  |






(rb-api-cartesianimpedancecontrolcommand-jointpositiontarget)=
### CartesianImpedanceControlCommand.JointPositionTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| joint_name | [string](#scalar-value-types) |  |  |
| target_position | [double](#scalar-value-types) |  |  |
| velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |






(rb-api-cartesianimpedancecontrolcommand-nullspacejointtarget)=
### CartesianImpedanceControlCommand.NullspaceJointTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_position | [double](#scalar-value-types) | repeated | Length: DOF |
| weight | [double](#scalar-value-types) | repeated | Length: DOF, [0, inf), default = 1 |
| k_p | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 0.2 |
| k_d | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 0.2 |
| cost_weight | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 1e-3 |






(rb-api-cartesianimpedancecontrolcommand-request)=
### CartesianImpedanceControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  | default = 0 |
| targets | [CartesianImpedanceControlCommand.SE3PoseTarget](#rb-api-CartesianImpedanceControlCommand-SE3PoseTarget) | repeated |  |
| joint_position_targets | [CartesianImpedanceControlCommand.JointPositionTarget](#rb-api-CartesianImpedanceControlCommand-JointPositionTarget) | repeated |  |
| stop_position_tracking_error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| stop_orientation_tracking_error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| stop_joint_position_tracking_error | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  |  |
| joint_stiffness | [double](#scalar-value-types) | repeated |  |
| joint_damping_ratio | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 1 |
| joint_torque_limit | [double](#scalar-value-types) | repeated |  |
| joint_limits | [CartesianImpedanceControlCommand.JointLimit](#rb-api-CartesianImpedanceControlCommand-JointLimit) | repeated |  |
| reset_reference | [google.protobuf.BoolValue](#google-protobuf-BoolValue) |  | default = false |
| nullspace_joint_target | [CartesianImpedanceControlCommand.NullspaceJointTarget](#rb-api-CartesianImpedanceControlCommand-NullspaceJointTarget) |  |  |






(rb-api-cartesianimpedancecontrolcommand-se3posetarget)=
### CartesianImpedanceControlCommand.SE3PoseTarget



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](#scalar-value-types) |  |  |
| link_name | [string](#scalar-value-types) |  |  |
| T | [SE3Pose](#rb-api-SE3Pose) |  |  |
| linear_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (m/s) |
| angular_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) |
| linear_acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (m/s^2) |
| angular_acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s^2) |






(rb-api-gravitycompensationcommand)=
### GravityCompensationCommand







(rb-api-gravitycompensationcommand-feedback)=
### GravityCompensationCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






(rb-api-gravitycompensationcommand-request)=
### GravityCompensationCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| on | [bool](#scalar-value-types) |  |  |






(rb-api-impedancecontrolcommand)=
### ImpedanceControlCommand







(rb-api-impedancecontrolcommand-feedback)=
### ImpedanceControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| tracking_error | [ImpedanceControlCommand.TrackingError](#rb-api-ImpedanceControlCommand-TrackingError) |  |  |






(rb-api-impedancecontrolcommand-request)=
### ImpedanceControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| ref_link_name | [string](#scalar-value-types) |  |  |
| link_name | [string](#scalar-value-types) |  |  |
| T | [SE3Pose](#rb-api-SE3Pose) |  |  |
| translation_weight | [Vec3](#rb-api-Vec3) |  | Translation part of stiffness |
| rotation_weight | [Vec3](#rb-api-Vec3) |  | Rotation part of stiffness |
| damping_ratio | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 1 |






(rb-api-impedancecontrolcommand-trackingerror)=
### ImpedanceControlCommand.TrackingError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position_error | [double](#scalar-value-types) |  |  |
| rotation_error | [double](#scalar-value-types) |  |  |






(rb-api-jogcommand)=
### JogCommand







(rb-api-jogcommand-feedback)=
### JogCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| target_joint_name | [string](#scalar-value-types) |  |  |






(rb-api-jogcommand-request)=
### JogCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint_name | [string](#scalar-value-types) |  |  |
| velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) (optional) |
| acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s^2) (optional) |
| absolute_position | [double](#scalar-value-types) |  | (rad) |
| relative_position | [double](#scalar-value-types) |  | (rad) current position &#43; relative position |
| one_step | [bool](#scalar-value-types) |  | 5 deg, true is positive move, false is negative move |






(rb-api-jointgrouppositioncommand)=
### JointGroupPositionCommand







(rb-api-jointgrouppositioncommand-feedback)=
### JointGroupPositionCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint_indices | [int32](#scalar-value-types) | repeated |  |
| time_based_progress | [double](#scalar-value-types) |  | [0, 1] |
| position_based_progress | [double](#scalar-value-types) |  | (-inf, 1] |






(rb-api-jointgrouppositioncommand-request)=
### JointGroupPositionCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint_names | [string](#scalar-value-types) | repeated |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| position | [double](#scalar-value-types) | repeated |  |
| velocity_limit | [double](#scalar-value-types) | repeated |  |
| acceleration_limit | [double](#scalar-value-types) | repeated |  |






(rb-api-jointimpedancecontrolcommand)=
### JointImpedanceControlCommand







(rb-api-jointimpedancecontrolcommand-feedback)=
### JointImpedanceControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| set_position | [double](#scalar-value-types) | repeated |  |
| error | [double](#scalar-value-types) | repeated |  |






(rb-api-jointimpedancecontrolcommand-request)=
### JointImpedanceControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| position | [double](#scalar-value-types) | repeated |  |
| velocity_limit | [double](#scalar-value-types) | repeated |  |
| acceleration_limit | [double](#scalar-value-types) | repeated |  |
| stiffness | [double](#scalar-value-types) | repeated |  |
| damping_ratio | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 1 |
| torque_limit | [double](#scalar-value-types) | repeated |  |






(rb-api-jointpositioncommand)=
### JointPositionCommand







(rb-api-jointpositioncommand-feedback)=
### JointPositionCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| time_based_progress | [double](#scalar-value-types) |  | [0, 1] |
| position_based_progress | [double](#scalar-value-types) |  | (-inf, 1] |






(rb-api-jointpositioncommand-request)=
### JointPositionCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| position | [double](#scalar-value-types) | repeated |  |
| velocity_limit | [double](#scalar-value-types) | repeated |  |
| acceleration_limit | [double](#scalar-value-types) | repeated |  |






(rb-api-jointvelocitycommand)=
### JointVelocityCommand







(rb-api-jointvelocitycommand-feedback)=
### JointVelocityCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






(rb-api-jointvelocitycommand-request)=
### JointVelocityCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| velocity | [double](#scalar-value-types) | repeated |  |
| acceleration_limit | [double](#scalar-value-types) | repeated |  |






(rb-api-optimalcontrolcommand)=
### OptimalControlCommand







(rb-api-optimalcontrolcommand-cartesiancost)=
### OptimalControlCommand.CartesianCost



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](#scalar-value-types) |  |  |
| link_name | [string](#scalar-value-types) |  |  |
| T | [SE3Pose](#rb-api-SE3Pose) |  |  |
| translation_weight | [double](#scalar-value-types) |  | default = 1 |
| rotation_weight | [double](#scalar-value-types) |  | default = 1 |






(rb-api-optimalcontrolcommand-centerofmasscost)=
### OptimalControlCommand.CenterOfMassCost



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](#scalar-value-types) |  |  |
| pose | [Vec3](#rb-api-Vec3) |  |  |
| weight | [double](#scalar-value-types) |  | default = 1 |






(rb-api-optimalcontrolcommand-feedback)=
### OptimalControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| total_cost | [double](#scalar-value-types) |  |  |
| cartesian_costs | [double](#scalar-value-types) | repeated |  |
| center_of_mass_cost | [double](#scalar-value-types) |  |  |
| joint_position_costs | [double](#scalar-value-types) | repeated |  |






(rb-api-optimalcontrolcommand-jointpositioncost)=
### OptimalControlCommand.JointPositionCost



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| joint_name | [string](#scalar-value-types) |  |  |
| target_position | [double](#scalar-value-types) |  |  |
| weight | [double](#scalar-value-types) |  |  |






(rb-api-optimalcontrolcommand-request)=
### OptimalControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| cartesian_costs | [OptimalControlCommand.CartesianCost](#rb-api-OptimalControlCommand-CartesianCost) | repeated |  |
| center_of_mass_cost | [OptimalControlCommand.CenterOfMassCost](#rb-api-OptimalControlCommand-CenterOfMassCost) |  |  |
| joint_position_costs | [OptimalControlCommand.JointPositionCost](#rb-api-OptimalControlCommand-JointPositionCost) | repeated |  |
| velocity_limit_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | velocity scaling factor: qdot_limit * default.velocity_limit_scaling * velocity_limit_scaling default: 1.0, range: (0, 1] |
| acceleration_limit_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | acceleration scaling factor: qddot_limit * default.acceleration_limit_scaling * acceleration_limit_scaling default: 1.0, range: (0, ∞) |
| velocity_tracking_gain | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | velocity tracking gain default: default.optimal_control_command.velocity_tracking_gain, range: (0, 1] DEPRECATED since 0.4.3 For robots prior to version 0.4.1, differences in the optimization method may cause unintended behavior if the value is used. Therefore, to prevent this issue, this value is forcibly set to 0. |
| error_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | Like step size, range: (0, ∞) |
| stop_cost | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | stop cost default: default.optimal_control_command.stop_cost, range: (0, ∞) |
| min_delta_cost | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | minimum delta cost, optional, range: (0, ∞) |
| patience | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | patience parameter, optional, range: (0, ∞) |






(rb-api-realtimecontrolcommand)=
### RealTimeControlCommand







(rb-api-realtimecontrolcommand-feedback)=
### RealTimeControlCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






(rb-api-realtimecontrolcommand-request)=
### RealTimeControlCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| port | [uint32](#scalar-value-types) |  |  |






(rb-api-se2velocitycommand)=
### SE2VelocityCommand







(rb-api-se2velocitycommand-feedback)=
### SE2VelocityCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






(rb-api-se2velocitycommand-request)=
### SE2VelocityCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| velocity | [SE2Velocity](#rb-api-SE2Velocity) |  |  |
| acceleration_limit | [SE2Velocity](#rb-api-SE2Velocity) |  |  |






(rb-api-stopcommand)=
### StopCommand







(rb-api-stopcommand-feedback)=
### StopCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |






(rb-api-stopcommand-request)=
### StopCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |





 

 

 

 



(rb_api_body_command-proto)=
## rb/api/body_command.proto



(rb-api-bodycommand)=
### BodyCommand







(rb-api-bodycommand-feedback)=
### BodyCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |
| optimal_control_command_feedback | [OptimalControlCommand.Feedback](#rb-api-OptimalControlCommand-Feedback) |  |  |
| gravity_compensation_command_feedback | [GravityCompensationCommand.Feedback](#rb-api-GravityCompensationCommand-Feedback) |  |  |
| cartesian_command_feedback | [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback) |  |  |
| body_component_based_command_feedback | [BodyComponentBasedCommand.Feedback](#rb-api-BodyComponentBasedCommand-Feedback) |  |  |
| joint_impedance_control_command_feedback | [JointImpedanceControlCommand.Feedback](#rb-api-JointImpedanceControlCommand-Feedback) |  |  |
| cartesian_impedance_control_command_feedback | [CartesianImpedanceControlCommand.Feedback](#rb-api-CartesianImpedanceControlCommand-Feedback) |  |  |






(rb-api-bodycommand-request)=
### BodyCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint_position_command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |
| optimal_control_command | [OptimalControlCommand.Request](#rb-api-OptimalControlCommand-Request) |  |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](#rb-api-GravityCompensationCommand-Request) |  |  |
| cartesian_command | [CartesianCommand.Request](#rb-api-CartesianCommand-Request) |  |  |
| body_component_based_command | [BodyComponentBasedCommand.Request](#rb-api-BodyComponentBasedCommand-Request) |  |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](#rb-api-JointImpedanceControlCommand-Request) |  |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](#rb-api-CartesianImpedanceControlCommand-Request) |  |  |





 

 

 

 



(rb_api_body_component_based_command-proto)=
## rb/api/body_component_based_command.proto



(rb-api-bodycomponentbasedcommand)=
### BodyComponentBasedCommand







(rb-api-bodycomponentbasedcommand-feedback)=
### BodyComponentBasedCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| right_arm_command_feedback | [ArmCommand.Feedback](#rb-api-ArmCommand-Feedback) |  |  |
| left_arm_command_feedback | [ArmCommand.Feedback](#rb-api-ArmCommand-Feedback) |  |  |
| torso_command_feedback | [TorsoCommand.Feedback](#rb-api-TorsoCommand-Feedback) |  |  |






(rb-api-bodycomponentbasedcommand-request)=
### BodyComponentBasedCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| right_arm_command | [ArmCommand.Request](#rb-api-ArmCommand-Request) |  |  |
| left_arm_command | [ArmCommand.Request](#rb-api-ArmCommand-Request) |  |  |
| torso_command | [TorsoCommand.Request](#rb-api-TorsoCommand-Request) |  |  |





 

 

 

 



(rb_api_color-proto)=
## rb/api/color.proto



(rb-api-color)=
### Color
Represents a color in the RGB color space.
Each color component is an unsigned 32-bit integer value in the range [0, 255].


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| red | [uint32](#scalar-value-types) |  | The red component of the color, specified as a value in the range [0, 255]. |
| green | [uint32](#scalar-value-types) |  | The green component of the color, specified as a value in the range [0, 255]. |
| blue | [uint32](#scalar-value-types) |  | The blue component of the color, specified as a value in the range [0, 255]. |





 

 

 

 



(rb_api_command_header-proto)=
## rb/api/command_header.proto



(rb-api-commandheader)=
### CommandHeader







(rb-api-commandheader-feedback)=
### CommandHeader.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| finished | [bool](#scalar-value-types) |  |  |






(rb-api-commandheader-request)=
### CommandHeader.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| control_hold_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |





 

 

 

 



(rb_api_component_based_command-proto)=
## rb/api/component_based_command.proto



(rb-api-componentbasedcommand)=
### ComponentBasedCommand







(rb-api-componentbasedcommand-feedback)=
### ComponentBasedCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| mobility_command_feedback | [MobilityCommand.Feedback](#rb-api-MobilityCommand-Feedback) |  |  |
| body_command_feedback | [BodyCommand.Feedback](#rb-api-BodyCommand-Feedback) |  |  |
| head_command_feedback | [HeadCommand.Feedback](#rb-api-HeadCommand-Feedback) |  |  |






(rb-api-componentbasedcommand-request)=
### ComponentBasedCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| mobility_command | [MobilityCommand.Request](#rb-api-MobilityCommand-Request) |  |  |
| body_command | [BodyCommand.Request](#rb-api-BodyCommand-Request) |  |  |
| head_command | [HeadCommand.Request](#rb-api-HeadCommand-Request) |  |  |





 

 

 

 



(rb_api_control_manager-proto)=
## rb/api/control_manager.proto



(rb-api-cancelcontrolrequest)=
### CancelControlRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |






(rb-api-cancelcontrolresponse)=
### CancelControlResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |






(rb-api-controlmanagercommandrequest)=
### ControlManagerCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| command | [ControlManagerCommandRequest.Command](#rb-api-ControlManagerCommandRequest-Command) |  |  |
| unlimited_mode_enabled | [google.protobuf.BoolValue](#google-protobuf-BoolValue) |  |  |






(rb-api-controlmanagercommandresponse)=
### ControlManagerCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| control_manager_state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






(rb-api-controlmanagerstate)=
### ControlManagerState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [ControlManagerState.State](#rb-api-ControlManagerState-State) |  |  |
| time_scale | [double](#scalar-value-types) |  |  |
| control_state | [ControlManagerState.ControlState](#rb-api-ControlManagerState-ControlState) |  |  |
| enabled_joint_idx | [uint32](#scalar-value-types) | repeated |  |
| unlimited_mode_enabled | [bool](#scalar-value-types) |  |  |






(rb-api-gettimescalerequest)=
### GetTimeScaleRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |






(rb-api-gettimescaleresponse)=
### GetTimeScaleResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| time_scale | [double](#scalar-value-types) |  |  |






(rb-api-settimescalerequest)=
### SetTimeScaleRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| time_scale | [double](#scalar-value-types) |  |  |






(rb-api-settimescaleresponse)=
### SetTimeScaleResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| current_time_scale | [double](#scalar-value-types) |  |  |






(rb-api-waitforcontrolreadyrequest)=
### WaitForControlReadyRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| timeout | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |






(rb-api-waitforcontrolreadyresponse)=
### WaitForControlReadyResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| ready | [bool](#scalar-value-types) |  |  |





 


(rb-api-controlmanagercommandrequest-command)=
### ControlManagerCommandRequest.Command
Control manager command

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND_UNKNOWN | 0 |  |
| COMMAND_ENABLE | 1 |  |
| COMMAND_DISABLE | 2 |  |
| COMMAND_RESET_FAULT | 3 |  |



(rb-api-controlmanagerstate-controlstate)=
### ControlManagerState.ControlState


| Name | Number | Description |
| ---- | ------ | ----------- |
| CONTROL_STATE_UNKNOWN | 0 |  |
| CONTROL_STATE_IDLE | 1 |  |
| CONTROL_STATE_EXECUTING | 2 |  |
| CONTROL_STATE_SWITCHING | 3 |  |



(rb-api-controlmanagerstate-state)=
### ControlManagerState.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| CONTROL_MANAGER_STATE_UNKNOWN | 0 |  |
| CONTROL_MANAGER_STATE_IDLE | 1 |  |
| CONTROL_MANAGER_STATE_ENABLED | 2 |  |
| CONTROL_MANAGER_STATE_MINOR_FAULT | 3 |  |
| CONTROL_MANAGER_STATE_MAJOR_FAULT | 4 |  |


 

 

 



(rb_api_control_manager_service-proto)=
## rb/api/control_manager_service.proto


 

 

 


(rb-api-controlmanagerservice)=
### ControlManagerService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ControlManagerCommand | [ControlManagerCommandRequest](#rb-api-ControlManagerCommandRequest) | [ControlManagerCommandResponse](#rb-api-ControlManagerCommandResponse) |  |
| CancelControl | [CancelControlRequest](#rb-api-CancelControlRequest) | [CancelControlResponse](#rb-api-CancelControlResponse) |  |
| GetTimeScale | [GetTimeScaleRequest](#rb-api-GetTimeScaleRequest) | [GetTimeScaleResponse](#rb-api-GetTimeScaleResponse) |  |
| SetTimeScale | [SetTimeScaleRequest](#rb-api-SetTimeScaleRequest) | [SetTimeScaleResponse](#rb-api-SetTimeScaleResponse) |  |
| WaitForControlReady | [WaitForControlReadyRequest](#rb-api-WaitForControlReadyRequest) | [WaitForControlReadyResponse](#rb-api-WaitForControlReadyResponse) |  |

 



(rb_api_file-proto)=
## rb/api/file.proto



(rb-api-downloadfilerequest)=
### DownloadFileRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| file_path | [string](#scalar-value-types) |  |  |






(rb-api-downloadfileresponse)=
### DownloadFileResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| file_content | [bytes](#scalar-value-types) |  |  |





 

 

 

 



(rb_api_file_service-proto)=
## rb/api/file_service.proto


 

 

 


(rb-api-fileservice)=
### FileService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DownloadFile | [DownloadFileRequest](#rb-api-DownloadFileRequest) | [DownloadFileResponse](#rb-api-DownloadFileResponse) stream |  |

 



(rb_api_gamepad-proto)=
## rb/api/gamepad.proto



(rb-api-gamepad)=
### Gamepad



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buttons | [bool](#scalar-value-types) | repeated |  |
| joystick | [double](#scalar-value-types) | repeated |  |






(rb-api-uploadgamepaddatarequest)=
### UploadGamepadDataRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| data | [Gamepad](#rb-api-Gamepad) |  |  |






(rb-api-uploadgamepaddataresponse)=
### UploadGamepadDataResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 

 

 

 



(rb_api_gamepad_service-proto)=
## rb/api/gamepad_service.proto


 

 

 


(rb-api-gamepadservice)=
### GamepadService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| UploadGamepadData | [Gamepad](#rb-api-Gamepad) stream | [UploadGamepadDataResponse](#rb-api-UploadGamepadDataResponse) |  |

 



(rb_api_geometry-proto)=
## rb/api/geometry.proto



(rb-api-euleranglezyx)=
### EulerAngleZYX



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| z | [double](#scalar-value-types) |  |  |
| y | [double](#scalar-value-types) |  |  |
| x | [double](#scalar-value-types) |  |  |






(rb-api-inertia)=
### Inertia
Inertia tensor components (kg*m^2)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ixx | [double](#scalar-value-types) |  |  |
| iyy | [double](#scalar-value-types) |  |  |
| izz | [double](#scalar-value-types) |  |  |
| ixy | [double](#scalar-value-types) |  |  |
| ixz | [double](#scalar-value-types) |  |  |
| iyz | [double](#scalar-value-types) |  |  |






(rb-api-inertial)=
### Inertial



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mass | [double](#scalar-value-types) |  | Mass (kg) |
| center_of_mass | [Vec3](#rb-api-Vec3) |  | Center of mass (m) |
| inertia | [Inertia](#rb-api-Inertia) |  | Inertia tensor |






(rb-api-quaternion)=
### Quaternion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#scalar-value-types) |  |  |
| y | [double](#scalar-value-types) |  |  |
| z | [double](#scalar-value-types) |  |  |
| w | [double](#scalar-value-types) |  |  |






(rb-api-se2pose)=
### SE2Pose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Vec2](#rb-api-Vec2) |  | (m) |
| angle | [double](#scalar-value-types) |  | (rad) |






(rb-api-se2velocity)=
### SE2Velocity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| linear | [Vec2](#rb-api-Vec2) |  | (m/s) |
| angular | [double](#scalar-value-types) |  | (rad/s) |






(rb-api-se3pose)=
### SE3Pose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Vec3](#rb-api-Vec3) |  | (m) |
| quaternion | [Quaternion](#rb-api-Quaternion) |  |  |
| euler | [EulerAngleZYX](#rb-api-EulerAngleZYX) |  |  |






(rb-api-vec2)=
### Vec2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#scalar-value-types) |  |  |
| y | [double](#scalar-value-types) |  |  |






(rb-api-vec3)=
### Vec3



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#scalar-value-types) |  |  |
| y | [double](#scalar-value-types) |  |  |
| z | [double](#scalar-value-types) |  |  |





 

 

 

 



(rb_api_gripper_command-proto)=
## rb/api/gripper_command.proto



(rb-api-gripperinitializationrequest)=
### GripperInitializationRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |






(rb-api-gripperinitializationresponse)=
### GripperInitializationResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |






(rb-api-grippermoverequest)=
### GripperMoveRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |
| position | [int32](#scalar-value-types) |  |  |
| velocity | [int32](#scalar-value-types) |  |  |
| force | [int32](#scalar-value-types) |  |  |






(rb-api-grippermoveresponse)=
### GripperMoveResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |





 

 

 

 



(rb_api_gripper_command_service-proto)=
## rb/api/gripper_command_service.proto


 

 

 


(rb-api-grippercommandservice)=
### GripperCommandService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GripperInitialization | [GripperInitializationRequest](#rb-api-GripperInitializationRequest) | [GripperInitializationResponse](#rb-api-GripperInitializationResponse) |  |
| GripperMove | [GripperMoveRequest](#rb-api-GripperMoveRequest) | [GripperMoveResponse](#rb-api-GripperMoveResponse) | Joint command |

 



(rb_api_head_command-proto)=
## rb/api/head_command.proto



(rb-api-headcommand)=
### HeadCommand







(rb-api-headcommand-feedback)=
### HeadCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |






(rb-api-headcommand-request)=
### HeadCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint_position_command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |





 

 

 

 



(rb_api_header-proto)=
## rb/api/header.proto



(rb-api-commonerror)=
### CommonError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [CommonError.Code](#rb-api-CommonError-Code) |  | Error code |
| message | [string](#scalar-value-types) |  | Human-readable error message |






(rb-api-requestheader)=
### RequestHeader
Standard request header


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Client local system clock |






(rb-api-responseheader)=
### ResponseHeader
Standard response header


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Echo |
| request_received_timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Robot clock |
| response_timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Robot clock |
| error | [CommonError](#rb-api-CommonError) |  | If set, there is error |





 


(rb-api-commonerror-code)=
### CommonError.Code


| Name | Number | Description |
| ---- | ------ | ----------- |
| CODE_UNSPECIFIED | 0 | Code is not specified. |
| CODE_OK | 1 | Not an error. Request was successful. |
| CODE_INTERNAL_SERVER_ERROR | 2 | Service experienced an unexpected error state. |
| CODE_INVALID_REQUEST | 3 | Ill-formed request. Request arguments were not valid. |


 

 

 



(rb_api_joint_operation-proto)=
## rb/api/joint_operation.proto



(rb-api-brakeengagerequest)=
### BrakeEngageRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |






(rb-api-brakeengageresponse)=
### BrakeEngageResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [BrakeEngageResponse.Status](#rb-api-BrakeEngageResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  | Human-readable message for status |






(rb-api-brakereleaserequest)=
### BrakeReleaseRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |






(rb-api-brakereleaseresponse)=
### BrakeReleaseResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [BrakeReleaseResponse.Status](#rb-api-BrakeReleaseResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  | Human-readable message for status |






(rb-api-getpositionpidgainrequest)=
### GetPositionPIDGainRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| dev_name | [string](#scalar-value-types) |  |  |
| target_component | [GetPositionPIDGainRequest.TargetComponent](#rb-api-GetPositionPIDGainRequest-TargetComponent) |  |  |






(rb-api-getpositionpidgainresponse)=
### GetPositionPIDGainResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| position_gain | [PositionPIDGain](#rb-api-PositionPIDGain) | repeated |  |






(rb-api-homeoffsetresetrequest)=
### HomeOffsetResetRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |






(rb-api-homeoffsetresetresponse)=
### HomeOffsetResetResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [HomeOffsetResetResponse.Status](#rb-api-HomeOffsetResetResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  | Human-readable message for status |






(rb-api-positionpidgain)=
### PositionPIDGain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| p_gain | [uint32](#scalar-value-types) |  |  |
| i_gain | [uint32](#scalar-value-types) |  |  |
| d_gain | [uint32](#scalar-value-types) |  |  |






(rb-api-servooffrequest)=
### ServoOffRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |






(rb-api-servooffresponse)=
### ServoOffResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [ServoOffResponse.Status](#rb-api-ServoOffResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  |  |






(rb-api-servoonrequest)=
### ServoOnRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |






(rb-api-servoonresponse)=
### ServoOnResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [ServoOnResponse.Status](#rb-api-ServoOnResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  | Human-readable message for status |






(rb-api-setpositionpidgainrequest)=
### SetPositionPIDGainRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  |  |
| p_gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |
| i_gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |
| d_gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |






(rb-api-setpositionpidgainresponse)=
### SetPositionPIDGainResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [SetPositionPIDGainResponse.Status](#rb-api-SetPositionPIDGainResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  | Human-readable message for status |






(rb-api-setpresetpositionrequest)=
### SetPresetPositionRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  |  |






(rb-api-setpresetpositionresponse)=
### SetPresetPositionResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 


(rb-api-brakeengageresponse-status)=
### BrakeEngageResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |



(rb-api-brakereleaseresponse-status)=
### BrakeReleaseResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |



(rb-api-getpositionpidgainrequest-targetcomponent)=
### GetPositionPIDGainRequest.TargetComponent


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| TORSO | 1 |  |
| RIGHT_ARM | 2 |  |
| LEFT_ARM | 3 |  |
| HEAD | 4 |  |



(rb-api-homeoffsetresetresponse-status)=
### HomeOffsetResetResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |



(rb-api-servooffresponse-status)=
### ServoOffResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |



(rb-api-servoonresponse-status)=
### ServoOnResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |



(rb-api-setpositionpidgainresponse-status)=
### SetPositionPIDGainResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |


 

 

 



(rb_api_joint_operation_service-proto)=
## rb/api/joint_operation_service.proto


 

 

 


(rb-api-jointoperationservice)=
### JointOperationService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ServoOn | [ServoOnRequest](#rb-api-ServoOnRequest) | [ServoOnResponse](#rb-api-ServoOnResponse) |  |
| ServoOff | [ServoOffRequest](#rb-api-ServoOffRequest) | [ServoOffResponse](#rb-api-ServoOffResponse) |  |
| BrakeEngage | [BrakeEngageRequest](#rb-api-BrakeEngageRequest) | [BrakeEngageResponse](#rb-api-BrakeEngageResponse) |  |
| BrakeRelease | [BrakeReleaseRequest](#rb-api-BrakeReleaseRequest) | [BrakeReleaseResponse](#rb-api-BrakeReleaseResponse) |  |
| HomeOffsetReset | [HomeOffsetResetRequest](#rb-api-HomeOffsetResetRequest) | [HomeOffsetResetResponse](#rb-api-HomeOffsetResetResponse) |  |
| GetPositionPIDGain | [GetPositionPIDGainRequest](#rb-api-GetPositionPIDGainRequest) | [GetPositionPIDGainResponse](#rb-api-GetPositionPIDGainResponse) |  |
| SetPositionPIDGain | [SetPositionPIDGainRequest](#rb-api-SetPositionPIDGainRequest) | [SetPositionPIDGainResponse](#rb-api-SetPositionPIDGainResponse) |  |
| SetPresetPosition | [SetPresetPositionRequest](#rb-api-SetPresetPositionRequest) | [SetPresetPositionResponse](#rb-api-SetPresetPositionResponse) |  |

 



(rb_api_led-proto)=
## rb/api/led.proto



(rb-api-setledcolorrequest)=
### SetLEDColorRequest
Request message for configuring the LED color and behavior


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| color | [Color](#rb-api-Color) |  | Desired LED color |
| duration | [google.protobuf.Duration](#google-protobuf-Duration) |  | Duration for which the LED will maintain the requested color. If blinking is enabled, this duration applies to the blinking cycle. Default: 1s |
| transition_time | [google.protobuf.Duration](#google-protobuf-Duration) |  | Specifies the time for transitioning from the current color to the new requested color. If omitted or zero, the transition is immediate. Default: 0s |
| blinking | [bool](#scalar-value-types) |  | Indicates whether to enable blinking Default: False |
| blinking_freq | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | Blinking frequency in Hz. This field is only relevant if blinking is set to true. Default: 1Hz |






(rb-api-setledcolorresponse)=
### SetLEDColorResponse
Response message for the SetLEDColor RPC call


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |





 

 

 

 



(rb_api_led_service-proto)=
## rb/api/led_service.proto


 

 

 


(rb-api-ledservice)=
### LEDService
Service for controlling LED behavior

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| SetLEDColor | [SetLEDColorRequest](#rb-api-SetLEDColorRequest) | [SetLEDColorResponse](#rb-api-SetLEDColorResponse) | Sets the LED color and (optionally) its blinking behavior. If blinking is true, the LED blinks at &#39;blinking_freq&#39; for &#39;duration&#39;. Otherwise, the LED remains in the requested color for &#39;duration&#39;. |

 



(rb_api_log-proto)=
## rb/api/log.proto



(rb-api-getfaultloglistrequest)=
### GetFaultLogListRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getfaultloglistresponse)=
### GetFaultLogListResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| fault_log_list | [string](#scalar-value-types) | repeated |  |






(rb-api-getlastlogrequest)=
### GetLastLogRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| log_count | [int32](#scalar-value-types) |  |  |






(rb-api-getlastlogresponse)=
### GetLastLogResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| logs | [Log](#rb-api-Log) | repeated |  |






(rb-api-getlogstreamrequest)=
### GetLogStreamRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| update_rate | [double](#scalar-value-types) |  | Hz |






(rb-api-getlogstreamresponse)=
### GetLogStreamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| logs | [Log](#rb-api-Log) | repeated |  |






(rb-api-log)=
### Log



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| robot_system_timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| level | [Log.Level](#rb-api-Log-Level) |  |  |
| message | [string](#scalar-value-types) |  |  |






(rb-api-setloglevelrequest)=
### SetLogLevelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| level | [Log.Level](#rb-api-Log-Level) |  |  |






(rb-api-setloglevelresponse)=
### SetLogLevelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 


(rb-api-log-level)=
### Log.Level


| Name | Number | Description |
| ---- | ------ | ----------- |
| LEVEL_TRACE | 0 |  |
| LEVEL_DEBUG | 1 |  |
| LEVEL_INFO | 2 |  |
| LEVEL_WARN | 3 |  |
| LEVEL_ERROR | 4 |  |
| LEVEL_CRITICAL | 5 |  |


 

 

 



(rb_api_log_service-proto)=
## rb/api/log_service.proto


 

 

 


(rb-api-logservice)=
### LogService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLastLog | [GetLastLogRequest](#rb-api-GetLastLogRequest) | [GetLastLogResponse](#rb-api-GetLastLogResponse) |  |
| GetLogStream | [GetLogStreamRequest](#rb-api-GetLogStreamRequest) | [GetLogStreamResponse](#rb-api-GetLogStreamResponse) stream |  |
| SetLogLevel | [SetLogLevelRequest](#rb-api-SetLogLevelRequest) | [SetLogLevelResponse](#rb-api-SetLogLevelResponse) |  |
| GetFaultLogList | [GetFaultLogListRequest](#rb-api-GetFaultLogListRequest) | [GetFaultLogListResponse](#rb-api-GetFaultLogListResponse) |  |

 



(rb_api_mobility_command-proto)=
## rb/api/mobility_command.proto



(rb-api-mobilitycommand)=
### MobilityCommand







(rb-api-mobilitycommand-feedback)=
### MobilityCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint_velocity_command_feedback | [JointVelocityCommand.Feedback](#rb-api-JointVelocityCommand-Feedback) |  |  |
| se2_velocity_command_feedback | [SE2VelocityCommand.Feedback](#rb-api-SE2VelocityCommand-Feedback) |  |  |






(rb-api-mobilitycommand-request)=
### MobilityCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint_velocity_command | [JointVelocityCommand.Request](#rb-api-JointVelocityCommand-Request) |  |  |
| se2_velocity_command | [SE2VelocityCommand.Request](#rb-api-SE2VelocityCommand-Request) |  |  |





 

 

 

 



(rb_api_parameter-proto)=
## rb/api/parameter.proto



(rb-api-factoryresetallparametersrequest)=
### FactoryResetAllParametersRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-factoryresetallparametersresponse)=
### FactoryResetAllParametersResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-factoryresetparameterrequest)=
### FactoryResetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  |  |






(rb-api-factoryresetparameterresponse)=
### FactoryResetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-getparameterlistrequest)=
### GetParameterListRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getparameterlistresponse)=
### GetParameterListResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| parameters | [GetParameterListResponse.ParameterType](#rb-api-GetParameterListResponse-ParameterType) | repeated |  |






(rb-api-getparameterlistresponse-parametertype)=
### GetParameterListResponse.ParameterType



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#scalar-value-types) |  |  |
| type | [int32](#scalar-value-types) |  | Type of parameter 0: int 1: double 2: std::string 3: std::array&lt;double, 3&gt; 4: std::array&lt;double, 6&gt; 5: std::array&lt;double, 7&gt; |






(rb-api-getparameterrequest)=
### GetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  |  |






(rb-api-getparameterresponse)=
### GetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| parameter | [string](#scalar-value-types) |  |  |






(rb-api-resetallparametersrequest)=
### ResetAllParametersRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-resetallparametersresponse)=
### ResetAllParametersResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-resetallparameterstodefaultrequest)=
### ResetAllParametersToDefaultRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-resetallparameterstodefaultresponse)=
### ResetAllParametersToDefaultResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-resetparameterrequest)=
### ResetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  |  |






(rb-api-resetparameterresponse)=
### ResetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-resetparametertodefaultrequest)=
### ResetParameterToDefaultRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  |  |






(rb-api-resetparametertodefaultresponse)=
### ResetParameterToDefaultResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-setparameterrequest)=
### SetParameterRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  |  |
| parameter | [string](#scalar-value-types) |  |  |






(rb-api-setparameterresponse)=
### SetParameterResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 

 

 

 



(rb_api_parameter_service-proto)=
## rb/api/parameter_service.proto


 

 

 


(rb-api-parameterservice)=
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

 



(rb_api_ping-proto)=
## rb/api/ping.proto



(rb-api-pingrequest)=
### PingRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-pingresponse)=
### PingResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 

 

 

 



(rb_api_ping_service-proto)=
## rb/api/ping_service.proto


 

 

 


(rb-api-pingservice)=
### PingService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Ping | [PingRequest](#rb-api-PingRequest) | [PingResponse](#rb-api-PingResponse) |  |

 



(rb_api_power-proto)=
## rb/api/power.proto



(rb-api-jointcommandrequest)=
### JointCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  | Motor ID |
| command | [JointCommandRequest.Command](#rb-api-JointCommandRequest-Command) |  |  |






(rb-api-jointcommandresponse)=
### JointCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [JointCommandResponse.Status](#rb-api-JointCommandResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  | Human-readable message for status |






(rb-api-powercommandrequest)=
### PowerCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  | Power ID |
| command | [PowerCommandRequest.Command](#rb-api-PowerCommandRequest-Command) |  |  |






(rb-api-powercommandresponse)=
### PowerCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |
| status | [PowerCommandResponse.Status](#rb-api-PowerCommandResponse-Status) |  |  |
| message | [string](#scalar-value-types) |  | Human-readable message for status |






(rb-api-toolflangepowercommandrequest)=
### ToolFlangePowerCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  | Request header |
| name | [string](#scalar-value-types) |  | Tool Flange name |
| command | [ToolFlangePowerCommandRequest.Command](#rb-api-ToolFlangePowerCommandRequest-Command) |  |  |






(rb-api-toolflangepowercommandresponse)=
### ToolFlangePowerCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  | Response header |





 


(rb-api-jointcommandrequest-command)=
### JointCommandRequest.Command
Modes for joint/motor command

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND_UNKNOWN | 0 |  |
| COMMAND_SERVO_ON | 1 |  |
| COMMAND_BRAKE_ENGAGE | 2 |  |
| COMMAND_BRAKE_RELEASE | 3 |  |
| COMMAND_HOME_OFFSET_RST | 4 |  |



(rb-api-jointcommandresponse-status)=
### JointCommandResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |



(rb-api-powercommandrequest-command)=
### PowerCommandRequest.Command
Power command

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND_UNKNOWN | 0 |  |
| COMMAND_POWER_ON | 1 |  |
| COMMAND_POWER_OFF | 2 |  |



(rb-api-powercommandresponse-status)=
### PowerCommandResponse.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_UNKNOWN | 0 |  |
| STATUS_SUCCESS | 1 |  |
| STATUS_INTERNAL_ERROR | 2 |  |



(rb-api-toolflangepowercommandrequest-command)=
### ToolFlangePowerCommandRequest.Command


| Name | Number | Description |
| ---- | ------ | ----------- |
| COMMAND_UNKNOWN | 0 |  |
| COMMAND_POWER_OFF | 1 |  |
| COMMAND_POWER_12V | 2 |  |
| COMMAND_POWER_24V | 3 |  |


 

 

 



(rb_api_power_service-proto)=
## rb/api/power_service.proto


 

 

 


(rb-api-powerservice)=
### PowerService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PowerCommand | [PowerCommandRequest](#rb-api-PowerCommandRequest) | [PowerCommandResponse](#rb-api-PowerCommandResponse) | Control power of the robot |
| JointCommand | [JointCommandRequest](#rb-api-JointCommandRequest) | [JointCommandResponse](#rb-api-JointCommandResponse) | Joint command |
| ToolFlangePowerCommand | [ToolFlangePowerCommandRequest](#rb-api-ToolFlangePowerCommandRequest) | [ToolFlangePowerCommandResponse](#rb-api-ToolFlangePowerCommandResponse) | Tool Flange |

 



(rb_api_robot_command-proto)=
## rb/api/robot_command.proto



(rb-api-robotcommand)=
### RobotCommand







(rb-api-robotcommand-feedback)=
### RobotCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| whole_body_command_feedback | [WholeBodyCommand.Feedback](#rb-api-WholeBodyCommand-Feedback) |  |  |
| component_based_command_feedback | [ComponentBasedCommand.Feedback](#rb-api-ComponentBasedCommand-Feedback) |  |  |
| jog_command_feedback | [JogCommand.Feedback](#rb-api-JogCommand-Feedback) |  |  |
| status | [RobotCommand.Feedback.Status](#rb-api-RobotCommand-Feedback-Status) |  |  |
| finish_code | [RobotCommand.Feedback.FinishCode](#rb-api-RobotCommand-Feedback-FinishCode) |  |  |






(rb-api-robotcommand-request)=
### RobotCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| whole_body_command | [WholeBodyCommand.Request](#rb-api-WholeBodyCommand-Request) |  |  |
| component_based_command | [ComponentBasedCommand.Request](#rb-api-ComponentBasedCommand-Request) |  |  |
| jog_command | [JogCommand.Request](#rb-api-JogCommand-Request) |  |  |






(rb-api-robotcommandrequest)=
### RobotCommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| robot_command | [RobotCommand.Request](#rb-api-RobotCommand-Request) |  |  |
| priority | [int32](#scalar-value-types) |  |  |






(rb-api-robotcommandresponse)=
### RobotCommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| feedback | [RobotCommand.Feedback](#rb-api-RobotCommand-Feedback) |  |  |





 


(rb-api-robotcommand-feedback-finishcode)=
### RobotCommand.Feedback.FinishCode


| Name | Number | Description |
| ---- | ------ | ----------- |
| FINISH_CODE_UNKNOWN | 0 |  |
| FINISH_CODE_OK | 1 |  |
| FINISH_CODE_CANCELED | 2 |  |
| FINISH_CODE_PREEMPTED | 3 |  |
| FINISH_CODE_INITIALIZED_FAILED | 4 |  |
| FINISH_CODE_CONTROL_MANAGER_IDLE | 5 |  |
| FINISH_CODE_CONTROL_MANAGER_FAULT | 6 |  |
| FINISH_CODE_UNEXPECTED_STATE | 7 |  |



(rb-api-robotcommand-feedback-status)=
### RobotCommand.Feedback.Status


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATUS_IDLE | 0 |  |
| STATUS_INITIALIZING | 1 |  |
| STATUS_RUNNING | 2 |  |
| STATUS_FINISHED | 3 |  |


 

 

 



(rb_api_robot_command_service-proto)=
## rb/api/robot_command_service.proto


 

 

 


(rb-api-robotcommandservice)=
### RobotCommandService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| RobotCommand | [RobotCommandRequest](#rb-api-RobotCommandRequest) | [RobotCommandResponse](#rb-api-RobotCommandResponse) | In case of sending and receiving a single command |
| RobotCommandStream | [RobotCommandRequest](#rb-api-RobotCommandRequest) stream | [RobotCommandResponse](#rb-api-RobotCommandResponse) stream | In case of sending and receiving commands continuously |

 



(rb_api_robot_info-proto)=
## rb/api/robot_info.proto



(rb-api-batteryinfo)=
### BatteryInfo







(rb-api-emoinfo)=
### EMOInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#scalar-value-types) |  |  |






(rb-api-getrobotinforequest)=
### GetRobotInfoRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getrobotinforesponse)=
### GetRobotInfoResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| robot_info | [RobotInfo](#rb-api-RobotInfo) |  |  |






(rb-api-getrobotmodelrequest)=
### GetRobotModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getrobotmodelresponse)=
### GetRobotModelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| model | [string](#scalar-value-types) |  |  |






(rb-api-importrobotmodelrequest)=
### ImportRobotModelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  |  |
| model | [string](#scalar-value-types) |  |  |






(rb-api-importrobotmodelresponse)=
### ImportRobotModelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-jointinfo)=
### JointInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#scalar-value-types) |  | Joint Motor Name |
| has_brake | [bool](#scalar-value-types) |  | Whether the joint has a brake |
| product_name | [string](#scalar-value-types) |  | RB or Dynamixel |
| firmware_version | [string](#scalar-value-types) |  | Firmware Version Name |






(rb-api-powerinfo)=
### PowerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#scalar-value-types) |  |  |






(rb-api-robotinfo)=
### RobotInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#scalar-value-types) |  |  |
| sdk_version | [string](#scalar-value-types) |  |  |
| robot_model_name | [string](#scalar-value-types) |  |  |
| robot_model_version | [string](#scalar-value-types) |  |  |
| battery_info | [BatteryInfo](#rb-api-BatteryInfo) |  |  |
| power_infos | [PowerInfo](#rb-api-PowerInfo) | repeated |  |
| emo_infos | [EMOInfo](#rb-api-EMOInfo) | repeated |  |
| degree_of_freedom | [int32](#scalar-value-types) |  |  |
| joint_infos | [JointInfo](#rb-api-JointInfo) | repeated |  |
| mobility_joint_idx | [uint32](#scalar-value-types) | repeated |  |
| body_joint_idx | [uint32](#scalar-value-types) | repeated |  |
| head_joint_idx | [uint32](#scalar-value-types) | repeated |  |
| torso_joint_idx | [uint32](#scalar-value-types) | repeated |  |
| right_arm_joint_idx | [uint32](#scalar-value-types) | repeated |  |
| left_arm_joint_idx | [uint32](#scalar-value-types) | repeated |  |
| robot_version | [string](#scalar-value-types) |  | [DEPRECATED] Will be removed in the future. Use `robot_model_name` instead. |
| sdk_commit_id | [string](#scalar-value-types) |  | [DEPRECATED] |





 

 

 

 



(rb_api_robot_info_service-proto)=
## rb/api/robot_info_service.proto


 

 

 


(rb-api-robotinfoservice)=
### RobotInfoService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRobotInfo | [GetRobotInfoRequest](#rb-api-GetRobotInfoRequest) | [GetRobotInfoResponse](#rb-api-GetRobotInfoResponse) |  |
| GetRobotModel | [GetRobotModelRequest](#rb-api-GetRobotModelRequest) | [GetRobotModelResponse](#rb-api-GetRobotModelResponse) |  |
| ImportRobotModel | [ImportRobotModelRequest](#rb-api-ImportRobotModelRequest) | [ImportRobotModelResponse](#rb-api-ImportRobotModelResponse) |  |

 



(rb_api_robot_state-proto)=
## rb/api/robot_state.proto



(rb-api-batterystate)=
### BatteryState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| voltage | [double](#scalar-value-types) |  | V |
| current | [double](#scalar-value-types) |  | Amp |
| level_percent | [double](#scalar-value-types) |  | % |






(rb-api-collision)=
### Collision



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| link1 | [string](#scalar-value-types) |  |  |
| link2 | [string](#scalar-value-types) |  |  |
| position1 | [Vec3](#rb-api-Vec3) |  |  |
| position2 | [Vec3](#rb-api-Vec3) |  |  |
| distance | [double](#scalar-value-types) |  |  |






(rb-api-emostate)=
### EMOState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [EMOState.State](#rb-api-EMOState-State) |  |  |






(rb-api-ftsensordata)=
### FTSensorData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_since_last_update | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| force | [Vec3](#rb-api-Vec3) |  |  |
| torque | [Vec3](#rb-api-Vec3) |  |  |






(rb-api-getcontrolmanagerstaterequest)=
### GetControlManagerStateRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getcontrolmanagerstateresponse)=
### GetControlManagerStateResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| control_manager_state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






(rb-api-getrobotstaterequest)=
### GetRobotStateRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getrobotstateresponse)=
### GetRobotStateResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| robot_state | [RobotState](#rb-api-RobotState) |  |  |
| control_manager_state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






(rb-api-getrobotstatestreamrequest)=
### GetRobotStateStreamRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| update_rate | [double](#scalar-value-types) |  | Hz |






(rb-api-getrobotstatestreamresponse)=
### GetRobotStateStreamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| robot_state | [RobotState](#rb-api-RobotState) |  |  |
| control_manager_state | [ControlManagerState](#rb-api-ControlManagerState) |  |  |






(rb-api-jointstate)=
### JointState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is_ready | [bool](#scalar-value-types) |  |  |
| fet_state | [JointState.FETState](#rb-api-JointState-FETState) |  |  |
| run_state | [JointState.RunState](#rb-api-JointState-RunState) |  |  |
| init_state | [JointState.InitializationState](#rb-api-JointState-InitializationState) |  |  |
| motor_type | [uint32](#scalar-value-types) |  | MOTOR STATE |
| motor_state | [uint64](#scalar-value-types) |  |  |
| time_since_last_update | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| power_on | [bool](#scalar-value-types) |  |  |
| position | [double](#scalar-value-types) |  |  |
| velocity | [double](#scalar-value-types) |  |  |
| current | [double](#scalar-value-types) |  |  |
| torque | [double](#scalar-value-types) |  |  |
| target_position | [double](#scalar-value-types) |  |  |
| target_velocity | [double](#scalar-value-types) |  |  |
| target_feedback_gain | [uint32](#scalar-value-types) |  |  |
| target_feedforward_torque | [double](#scalar-value-types) |  |  |
| temperature | [int32](#scalar-value-types) |  |  |






(rb-api-powerstate)=
### PowerState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [PowerState.State](#rb-api-PowerState-State) |  |  |
| voltage | [double](#scalar-value-types) |  |  |






(rb-api-resetodometryrequest)=
### ResetOdometryRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| initial_pose | [SE2Pose](#rb-api-SE2Pose) |  |  |






(rb-api-resetodometryresponse)=
### ResetOdometryResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-robotstate)=
### RobotState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| system_stat | [SystemStat](#rb-api-SystemStat) |  | System Statistic |
| battery_state | [BatteryState](#rb-api-BatteryState) |  | Battery State |
| power_states | [PowerState](#rb-api-PowerState) | repeated | Power State |
| emo_states | [EMOState](#rb-api-EMOState) | repeated | EMO state |
| joint_states | [JointState](#rb-api-JointState) | repeated | Joint State |
| tool_flange_right | [ToolFlangeState](#rb-api-ToolFlangeState) |  | Tool Flange State |
| tool_flange_left | [ToolFlangeState](#rb-api-ToolFlangeState) |  |  |
| ft_sensor_right | [FTSensorData](#rb-api-FTSensorData) |  | Force Torque Sensor |
| ft_sensor_left | [FTSensorData](#rb-api-FTSensorData) |  |  |
| is_ready | [double](#scalar-value-types) | repeated |  |
| position | [double](#scalar-value-types) | repeated |  |
| velocity | [double](#scalar-value-types) | repeated |  |
| current | [double](#scalar-value-types) | repeated |  |
| torque | [double](#scalar-value-types) | repeated |  |
| target_position | [double](#scalar-value-types) | repeated |  |
| target_velocity | [double](#scalar-value-types) | repeated |  |
| target_feedback_gain | [uint32](#scalar-value-types) | repeated |  |
| target_feedforward_torque | [double](#scalar-value-types) | repeated |  |
| odometry | [SE2Pose](#rb-api-SE2Pose) |  | Mobility State |
| center_of_mass | [Vec3](#rb-api-Vec3) |  | Center Of Mass

Position of center of mass with respect t base link |
| collisions | [Collision](#rb-api-Collision) | repeated | Collisions |
| temperature | [int32](#scalar-value-types) | repeated | Temperature |






(rb-api-systemstat)=
### SystemStat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cpu_usage | [double](#scalar-value-types) |  | % |
| memory_usage | [double](#scalar-value-types) |  | % |
| uptime | [double](#scalar-value-types) |  | sec |
| program_uptime | [double](#scalar-value-types) |  | sec |






(rb-api-toolflangestate)=
### ToolFlangeState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_since_last_update | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| gyro | [Vec3](#rb-api-Vec3) |  |  |
| acceleration | [Vec3](#rb-api-Vec3) |  |  |
| switch_A | [bool](#scalar-value-types) |  |  |
| output_voltage | [int32](#scalar-value-types) |  |  |
| digital_input_A | [bool](#scalar-value-types) |  |  |
| digital_input_B | [bool](#scalar-value-types) |  |  |
| digital_output_A | [bool](#scalar-value-types) |  |  |
| digital_output_B | [bool](#scalar-value-types) |  |  |





 


(rb-api-emostate-state)=
### EMOState.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATE_RELEASED | 0 |  |
| STATE_PRESSED | 1 |  |



(rb-api-jointstate-fetstate)=
### JointState.FETState


| Name | Number | Description |
| ---- | ------ | ----------- |
| FET_STATE_UNKNOWN | 0 |  |
| FET_STATE_ON | 1 |  |
| FET_STATE_OFF | 2 |  |



(rb-api-jointstate-initializationstate)=
### JointState.InitializationState


| Name | Number | Description |
| ---- | ------ | ----------- |
| INIT_STATE_UNKNOWN | 0 |  |
| INIT_STATE_INITIALIZED | 1 |  |
| INIT_STATE_UNINITIALIZED | 2 |  |



(rb-api-jointstate-runstate)=
### JointState.RunState


| Name | Number | Description |
| ---- | ------ | ----------- |
| RUN_STATE_UNKNOWN | 0 |  |
| RUN_STATE_CONTROL_ON | 1 |  |
| RUN_STATE_CONTROL_OFF | 2 |  |



(rb-api-powerstate-state)=
### PowerState.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATE_UNKNOWN | 0 |  |
| STATE_POWER_ON | 1 |  |
| STATE_POWER_OFF | 2 |  |


 

 

 



(rb_api_robot_state_service-proto)=
## rb/api/robot_state_service.proto


 

 

 


(rb-api-robotstateservice)=
### RobotStateService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetRobotState | [GetRobotStateRequest](#rb-api-GetRobotStateRequest) | [GetRobotStateResponse](#rb-api-GetRobotStateResponse) |  |
| GetRobotStateStream | [GetRobotStateStreamRequest](#rb-api-GetRobotStateStreamRequest) | [GetRobotStateStreamResponse](#rb-api-GetRobotStateStreamResponse) stream |  |
| GetControlManagerState | [GetControlManagerStateRequest](#rb-api-GetControlManagerStateRequest) | [GetControlManagerStateResponse](#rb-api-GetControlManagerStateResponse) |  |
| ResetOdometry | [ResetOdometryRequest](#rb-api-ResetOdometryRequest) | [ResetOdometryResponse](#rb-api-ResetOdometryResponse) |  |

 



(rb_api_serial-proto)=
## rb/api/serial.proto



(rb-api-getserialdevicelistrequest)=
### GetSerialDeviceListRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getserialdevicelistresponse)=
### GetSerialDeviceListResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| devices | [SerialDeviceInfo](#rb-api-SerialDeviceInfo) | repeated |  |






(rb-api-openserialstreamrequest)=
### OpenSerialStreamRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| connect | [SerialOpenRequest](#rb-api-SerialOpenRequest) |  |  |
| write | [SerialWriteRequest](#rb-api-SerialWriteRequest) |  |  |






(rb-api-openserialstreamresponse)=
### OpenSerialStreamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| connect_result | [SerialConnectionStatus](#rb-api-SerialConnectionStatus) |  |  |
| write_result | [SerialWriteResult](#rb-api-SerialWriteResult) |  |  |
| read_data | [bytes](#scalar-value-types) |  |  |






(rb-api-serialconnectionstatus)=
### SerialConnectionStatus



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success | [bool](#scalar-value-types) |  |  |
| message | [string](#scalar-value-types) |  |  |






(rb-api-serialdeviceinfo)=
### SerialDeviceInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| path | [string](#scalar-value-types) |  |  |
| description | [string](#scalar-value-types) |  |  |






(rb-api-serialopenrequest)=
### SerialOpenRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device_path | [string](#scalar-value-types) |  |  |
| baudrate | [int32](#scalar-value-types) |  |  |
| bytesize | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | default: 8 |
| parity | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | default: &#39;N&#39; |
| stopbits | [google.protobuf.Int32Value](#google-protobuf-Int32Value) |  | default: 1 |






(rb-api-serialwriterequest)=
### SerialWriteRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| data | [bytes](#scalar-value-types) |  |  |






(rb-api-serialwriteresult)=
### SerialWriteResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success | [bool](#scalar-value-types) |  |  |
| message | [string](#scalar-value-types) |  |  |





 

 

 

 



(rb_api_serial_service-proto)=
## rb/api/serial_service.proto


 

 

 


(rb-api-serialservice)=
### SerialService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetSerialDeviceList | [GetSerialDeviceListRequest](#rb-api-GetSerialDeviceListRequest) | [GetSerialDeviceListResponse](#rb-api-GetSerialDeviceListResponse) |  |
| OpenSerialStream | [OpenSerialStreamRequest](#rb-api-OpenSerialStreamRequest) stream | [OpenSerialStreamResponse](#rb-api-OpenSerialStreamResponse) stream |  |

 



(rb_api_system-proto)=
## rb/api/system.proto



(rb-api-connectwifirequest)=
### ConnectWifiRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| ssid | [string](#scalar-value-types) |  |  |
| password | [string](#scalar-value-types) |  |  |
| use_dhcp | [bool](#scalar-value-types) |  |  |
| ip_address | [string](#scalar-value-types) |  |  |
| gateway | [string](#scalar-value-types) |  |  |
| dns | [string](#scalar-value-types) | repeated |  |






(rb-api-connectwifiresponse)=
### ConnectWifiResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| success | [bool](#scalar-value-types) |  |  |






(rb-api-disconnectwifirequest)=
### DisconnectWifiRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-disconnectwifiresponse)=
### DisconnectWifiResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-getsystemtimerequest)=
### GetSystemTimeRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getsystemtimeresponse)=
### GetSystemTimeResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| utc_time | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| time_zone | [string](#scalar-value-types) |  | https://en.wikipedia.org/wiki/List_of_tz_database_time_zones |
| local_time | [string](#scalar-value-types) |  |  |






(rb-api-getwifistatusrequest)=
### GetWifiStatusRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-getwifistatusresponse)=
### GetWifiStatusResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| ssid | [string](#scalar-value-types) |  |  |
| ip_address | [string](#scalar-value-types) |  |  |
| gateway | [string](#scalar-value-types) |  |  |
| dns | [string](#scalar-value-types) | repeated |  |
| connected | [bool](#scalar-value-types) |  |  |






(rb-api-resetbatteryconfigrequest)=
### ResetBatteryConfigRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-resetbatteryconfigresponse)=
### ResetBatteryConfigResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-resetnetworksettingrequest)=
### ResetNetworkSettingRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-resetnetworksettingresponse)=
### ResetNetworkSettingResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-scanwifirequest)=
### ScanWifiRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |






(rb-api-scanwifiresponse)=
### ScanWifiResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |
| networks | [WifiNetwork](#rb-api-WifiNetwork) | repeated |  |






(rb-api-setbatteryconfigrequest)=
### SetBatteryConfigRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| cut_off_voltage | [double](#scalar-value-types) |  | voltage at 0 % |
| fully_charged_voltage | [double](#scalar-value-types) |  | voltage at 100 % |
| coefficients | [double](#scalar-value-types) | repeated | double[4]; coefficients for 3rd order polynomial |






(rb-api-setbatteryconfigresponse)=
### SetBatteryConfigResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-setbatterylevelrequest)=
### SetBatteryLevelRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| level | [double](#scalar-value-types) |  | [0, 100] |






(rb-api-setbatterylevelresponse)=
### SetBatteryLevelResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-setsystemtimerequest)=
### SetSystemTimeRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| utc_time | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| time_zone | [string](#scalar-value-types) |  | https://en.wikipedia.org/wiki/List_of_tz_database_time_zones |






(rb-api-setsystemtimeresponse)=
### SetSystemTimeResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |






(rb-api-wifinetwork)=
### WifiNetwork



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ssid | [string](#scalar-value-types) |  |  |
| signal_strength | [int32](#scalar-value-types) |  | dBm |
| secured | [bool](#scalar-value-types) |  |  |





 

 

 

 



(rb_api_system_service-proto)=
## rb/api/system_service.proto


 

 

 


(rb-api-systemservice)=
### SystemService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetSystemTime | [GetSystemTimeRequest](#rb-api-GetSystemTimeRequest) | [GetSystemTimeResponse](#rb-api-GetSystemTimeResponse) |  |
| SetSystemTime | [SetSystemTimeRequest](#rb-api-SetSystemTimeRequest) | [SetSystemTimeResponse](#rb-api-SetSystemTimeResponse) |  |
| SetBatteryLevel | [SetBatteryLevelRequest](#rb-api-SetBatteryLevelRequest) | [SetBatteryLevelResponse](#rb-api-SetBatteryLevelResponse) |  |
| SetBatteryConfig | [SetBatteryConfigRequest](#rb-api-SetBatteryConfigRequest) | [SetBatteryConfigResponse](#rb-api-SetBatteryConfigResponse) |  |
| ResetBatteryConfig | [ResetBatteryConfigRequest](#rb-api-ResetBatteryConfigRequest) | [ResetBatteryConfigResponse](#rb-api-ResetBatteryConfigResponse) |  |
| ResetNetworkSetting | [ResetNetworkSettingRequest](#rb-api-ResetNetworkSettingRequest) | [ResetNetworkSettingResponse](#rb-api-ResetNetworkSettingResponse) |  |
| ScanWifi | [ScanWifiRequest](#rb-api-ScanWifiRequest) | [ScanWifiResponse](#rb-api-ScanWifiResponse) |  |
| ConnectWifi | [ConnectWifiRequest](#rb-api-ConnectWifiRequest) | [ConnectWifiResponse](#rb-api-ConnectWifiResponse) |  |
| DisconnectWifi | [DisconnectWifiRequest](#rb-api-DisconnectWifiRequest) | [DisconnectWifiResponse](#rb-api-DisconnectWifiResponse) |  |
| GetWifiStatus | [GetWifiStatusRequest](#rb-api-GetWifiStatusRequest) | [GetWifiStatusResponse](#rb-api-GetWifiStatusResponse) |  |

 



(rb_api_tool_flange-proto)=
## rb/api/tool_flange.proto



(rb-api-settoolflangedigitaloutputrequest)=
### SetToolFlangeDigitalOutputRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](#rb-api-RequestHeader) |  |  |
| name | [string](#scalar-value-types) |  | tool flange name; &#39;left&#39; or &#39;right&#39; |
| single | [SetToolFlangeDigitalOutputRequest.SingleChannel](#rb-api-SetToolFlangeDigitalOutputRequest-SingleChannel) |  |  |
| dual | [SetToolFlangeDigitalOutputRequest.DualChannel](#rb-api-SetToolFlangeDigitalOutputRequest-DualChannel) |  |  |






(rb-api-settoolflangedigitaloutputrequest-dualchannel)=
### SetToolFlangeDigitalOutputRequest.DualChannel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state_0 | [bool](#scalar-value-types) |  |  |
| state_1 | [bool](#scalar-value-types) |  |  |






(rb-api-settoolflangedigitaloutputrequest-singlechannel)=
### SetToolFlangeDigitalOutputRequest.SingleChannel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| channel | [uint32](#scalar-value-types) |  |  |
| state | [bool](#scalar-value-types) |  |  |






(rb-api-settoolflangedigitaloutputresponse)=
### SetToolFlangeDigitalOutputResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](#rb-api-ResponseHeader) |  |  |





 

 

 

 



(rb_api_tool_flange_service-proto)=
## rb/api/tool_flange_service.proto


 

 

 


(rb-api-toolflangeservice)=
### ToolFlangeService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| SetDigitalOutput | [SetToolFlangeDigitalOutputRequest](#rb-api-SetToolFlangeDigitalOutputRequest) | [SetToolFlangeDigitalOutputResponse](#rb-api-SetToolFlangeDigitalOutputResponse) |  |

 



(rb_api_torso_command-proto)=
## rb/api/torso_command.proto



(rb-api-torsocommand)=
### TorsoCommand







(rb-api-torsocommand-feedback)=
### TorsoCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](#rb-api-JointPositionCommand-Feedback) |  |  |
| gravity_compensation_command_feedback | [GravityCompensationCommand.Feedback](#rb-api-GravityCompensationCommand-Feedback) |  |  |
| cartesian_command_feedback | [CartesianCommand.Feedback](#rb-api-CartesianCommand-Feedback) |  |  |
| impedance_control_command_feedback | [ImpedanceControlCommand.Feedback](#rb-api-ImpedanceControlCommand-Feedback) |  |  |
| optimal_control_command_feedback | [OptimalControlCommand.Feedback](#rb-api-OptimalControlCommand-Feedback) |  |  |
| joint_impedance_control_command_feedback | [JointImpedanceControlCommand.Feedback](#rb-api-JointImpedanceControlCommand-Feedback) |  |  |
| cartesian_impedance_control_command_feedback | [CartesianImpedanceControlCommand.Feedback](#rb-api-CartesianImpedanceControlCommand-Feedback) |  |  |
| joint_group_position_command_feedback | [JointGroupPositionCommand.Feedback](#rb-api-JointGroupPositionCommand-Feedback) |  |  |






(rb-api-torsocommand-request)=
### TorsoCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| joint_position_command | [JointPositionCommand.Request](#rb-api-JointPositionCommand-Request) |  |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](#rb-api-GravityCompensationCommand-Request) |  |  |
| cartesian_command | [CartesianCommand.Request](#rb-api-CartesianCommand-Request) |  |  |
| impedance_control_command | [ImpedanceControlCommand.Request](#rb-api-ImpedanceControlCommand-Request) |  |  |
| optimal_control_command | [OptimalControlCommand.Request](#rb-api-OptimalControlCommand-Request) |  |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](#rb-api-JointImpedanceControlCommand-Request) |  |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](#rb-api-CartesianImpedanceControlCommand-Request) |  |  |
| joint_group_position_command | [JointGroupPositionCommand.Request](#rb-api-JointGroupPositionCommand-Request) |  |  |





 

 

 

 



(rb_api_whole_body_command-proto)=
## rb/api/whole_body_command.proto



(rb-api-wholebodycommand)=
### WholeBodyCommand







(rb-api-wholebodycommand-feedback)=
### WholeBodyCommand.Feedback



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](#rb-api-CommandHeader-Feedback) |  |  |
| stop_command_feedback | [StopCommand.Feedback](#rb-api-StopCommand-Feedback) |  |  |
| real_time_control_command_feedback | [RealTimeControlCommand.Feedback](#rb-api-RealTimeControlCommand-Feedback) |  |  |






(rb-api-wholebodycommand-request)=
### WholeBodyCommand.Request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](#rb-api-CommandHeader-Request) |  |  |
| stop_command | [StopCommand.Request](#rb-api-StopCommand-Request) |  |  |
| real_time_control_command | [RealTimeControlCommand.Request](#rb-api-RealTimeControlCommand-Request) |  |  |





 

 

 

 



(scalar-value-types)=
## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| double |  | double | double | float | float64 | double | float | Float |
| float |  | float | float | float | float32 | float | float | Float |
| int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

