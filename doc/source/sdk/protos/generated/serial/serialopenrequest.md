(rb-api-serialopenrequest)=
# SerialOpenRequest

- Source proto: `rb/api/serial.proto`

Request to serial open.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device_path | [string](../scalar-value-types.md) |  |  |
| baudrate | [int32](../scalar-value-types.md) |  |  |
| bytesize | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | default: 8 |
| parity | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | default: &#39;N&#39; |
| stopbits | [google.protobuf.Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32value) |  | default: 1 |
