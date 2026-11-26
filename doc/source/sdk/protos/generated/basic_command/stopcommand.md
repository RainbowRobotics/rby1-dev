(rb-api-stopcommand)=
# StopCommand

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Controlled stop of the whole robot: all joints decelerate to zero velocity within the default joint acceleration limits, then the robot holds still for the control hold time.

```{warning}
StopCommand is not an emergency stop. It does not cut motor power and does not engage the brakes. In an emergency, press the E-Stop.
```

See also: [E-Stop Basics](../../../../getting-started/estop-basics.md), [Control Hold Time and Minimum Time](../../../controllers/generated/control_hold_time_and_minimum_time.md).


## Subtypes

- [StopCommand.Feedback](stopcommand-feedback.md)
- [StopCommand.Request](stopcommand-request.md)

