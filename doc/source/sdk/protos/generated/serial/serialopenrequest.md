(rb-api-serialopenrequest)=
# SerialOpenRequest

- Source proto: [`rb/api/serial.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/serial.proto) (rby1-sdk v0.10.1)

Opens a serial device: path, baud rate and frame format. Sent in an OpenSerialStreamRequest.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device_path | [string](../scalar-value-types.md) |  |  |
| baudrate | [int32](../scalar-value-types.md) |  |  |
| bytesize | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | default: 8 |
| parity | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | default: &#39;N&#39; |
| stopbits | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | default: 1 |
