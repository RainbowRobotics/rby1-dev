(rb-api-realtimecontrolcommand)=
# RealTimeControlCommand

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Starts a real-time control session. The request carries only the UDP `port`: the robot and the client then exchange robot state and joint commands over UDP on that port, not through this message. In the C++ SDK, `Robot::Control()` runs this loop.

See also: [ControlInput & ControlState (C++)](../../../cpp/client/control-loop-types.md), [RealTimeControlCommandBuilder (C++)](../../../cpp/builders/real-time-control-command-builder.md).


## Subtypes

- [RealTimeControlCommand.Feedback](realtimecontrolcommand-feedback.md)
- [RealTimeControlCommand.Request](realtimecontrolcommand-request.md)

