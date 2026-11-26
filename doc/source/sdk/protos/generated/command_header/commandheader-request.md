(rb-api-commandheader-request)=
# CommandHeader.Request

- Source proto: [`rb/api/command_header.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/command_header.proto) (rby1-sdk v0.10.1)

Request part of [CommandHeader](commandheader.md).

See also: [Control Hold Time and Minimum Time](../../../controllers/generated/control_hold_time_and_minimum_time.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| control_hold_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  | How long the robot keeps the target after reaching it, before the command finishes. Default 0 s. |
