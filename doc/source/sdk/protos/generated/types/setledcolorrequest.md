# SetLEDColorRequest

- Source proto: `rb/api/led.proto`

Request message for configuring the LED color and behavior


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](./requestheader.md#rb-api-requestheader) |  | Request header |
| color | [Color](./color.md#rb-api-color) |  | Desired LED color |
| duration | [google.protobuf.Duration](#google-protobuf-Duration) |  | Duration for which the LED will maintain the requested color. If blinking is enabled, this duration applies to the blinking cycle. Default: 1s |
| transition_time | [google.protobuf.Duration](#google-protobuf-Duration) |  | Specifies the time for transitioning from the current color to the new requested color. If omitted or zero, the transition is immediate. Default: 0s |
| blinking | [bool](./scalar-value-types.md#scalar-value-types) |  | Indicates whether to enable blinking Default: False |
| blinking_freq | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | Blinking frequency in Hz. This field is only relevant if blinking is set to true. Default: 1Hz |
