(rb-api-commandheader)=
# CommandHeader

- Source proto: [`rb/api/command_header.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/command_header.proto) (rby1-sdk v0.10.1)

Header of every command. The request sets the control hold time; the feedback reports whether the command has finished.

See also: [Control Hold Time and Minimum Time](../../../controllers/generated/control_hold_time_and_minimum_time.md).


## Subtypes

- [CommandHeader.Feedback](commandheader-feedback.md)
- [CommandHeader.Request](commandheader-request.md)

