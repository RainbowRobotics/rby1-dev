(rb-api-jointoperationservice)=
# JointOperationService

- Source proto: [`rb/api/joint_operation_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation_service.proto) (rby1-sdk v0.10.1)

Low-level joint operations: servo on and off, brakes, home offset, position PID gains and preset position. These calls act on the motor drivers directly, not through robot commands.

```{danger}
BrakeRelease: a joint whose servo is off is held only by its brake. When you release the brake, the joint can fall under gravity. Support the arm or torso and keep people clear before you release a brake.
```

```{danger}
HomeOffsetReset changes the zero of the joint. Every later position reading and command uses the new zero, so a wrong zero makes the robot move to wrong poses and can drive the joint past its real mechanical range. Use it only when a maintenance procedure tells you to.
```

```{warning}
SetPositionPIDGain changes the gains on the motor driver at once. Wrong gains can make a joint oscillate or move abruptly the next time it is controlled.
```

See also: [Maintenance](../../../../maintenance/index.md).

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ServoOn | [ServoOnRequest](../joint_operation/servoonrequest.md) | [ServoOnResponse](../joint_operation/servoonresponse.md) | Turns on the servo (motor control) of the named joints. Rejected while the Control Manager is enabled. |
| ServoOff | [ServoOffRequest](../joint_operation/servooffrequest.md) | [ServoOffResponse](../joint_operation/servooffresponse.md) | Turns off the servo of the named joints. Rejected while the Control Manager is enabled. |
| BrakeEngage | [BrakeEngageRequest](../joint_operation/brakeengagerequest.md) | [BrakeEngageResponse](../joint_operation/brakeengageresponse.md) | Engages the brakes of the named joints. `name` supports regex patterns. |
| BrakeRelease | [BrakeReleaseRequest](../joint_operation/brakereleaserequest.md) | [BrakeReleaseResponse](../joint_operation/brakereleaseresponse.md) | Releases the brakes of the named joints. `name` supports regex patterns. Read the warning on this page first. |
| HomeOffsetReset | [HomeOffsetResetRequest](../joint_operation/homeoffsetresetrequest.md) | [HomeOffsetResetResponse](../joint_operation/homeoffsetresetresponse.md) | Sets the current position of the named joints as their zero (home) position and overwrites the stored home offset. Read the warning on this page first. |
| GetPositionPIDGain | [GetPositionPIDGainRequest](../joint_operation/getpositionpidgainrequest.md) | [GetPositionPIDGainResponse](../joint_operation/getpositionpidgainresponse.md) | Returns the position PID gains of one joint (`dev_name`) or of all joints of a component. Works only while the Control Manager is idle. |
| SetPositionPIDGain | [SetPositionPIDGainRequest](../joint_operation/setpositionpidgainrequest.md) | [SetPositionPIDGainResponse](../joint_operation/setpositionpidgainresponse.md) | Writes position PID gains to the motor driver of the named joints; gains that are not set keep their value. Works only while the Control Manager is idle. |
| SetPresetPosition | [SetPresetPositionRequest](../joint_operation/setpresetpositionrequest.md) | [SetPresetPositionResponse](../joint_operation/setpresetpositionresponse.md) | Sets the preset position of the named joint (PVL-based motors only). Rejected while the Control Manager is enabled. |
