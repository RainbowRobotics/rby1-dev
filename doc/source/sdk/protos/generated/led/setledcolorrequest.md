(rb-api-setledcolorrequest)=
# SetLEDColorRequest

- Source proto: `rb/api/led.proto`

Request to set led color.

Request message for configuring the LED color and behavior


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| color | [Color](../color/color.md) |  | Desired LED color |
| duration | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  | Duration for which the LED will maintain the requested color. If blinking is enabled, this duration applies to the blinking cycle. Default: 1s |
| transition_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  | Specifies the time for transitioning from the current color to the new requested color. If omitted or zero, the transition is immediate. Default: 0s |
| blinking | [bool](../scalar-value-types.md) |  | Indicates whether to enable blinking Default: False |
| blinking_freq | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | Blinking frequency in Hz. This field is only relevant if blinking is set to true. Default: 1Hz |
