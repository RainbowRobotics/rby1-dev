(rb-api-jointcommandrequest)=
# JointCommandRequest

- Source proto: [`rb/api/power.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/power.proto) (rby1-sdk v0.10.1)

Request of the `JointCommand` RPC of [PowerService](../power_service/powerservice.md).

```{danger}
COMMAND_BRAKE_RELEASE can let a joint fall under gravity, and COMMAND_HOME_OFFSET_RST changes the zero of the joint. Read the warnings on the JointOperationService page before you use them.
```

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Required. Regex for the joint names, for example `right_arm_2`, `right_arm_.*` or `.*` for all joints. The whole name must match. An empty name matches no joint. |
| command | [JointCommandRequest.Command](jointcommandrequest-command.md) |  |  |
