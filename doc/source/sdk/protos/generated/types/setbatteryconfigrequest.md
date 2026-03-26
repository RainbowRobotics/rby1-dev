# SetBatteryConfigRequest

- Source proto: `rb/api/system.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](./requestheader.md#rb-api-requestheader) |  |  |
| cut_off_voltage | [double](./scalar-value-types.md#scalar-value-types) |  | voltage at 0 % |
| fully_charged_voltage | [double](./scalar-value-types.md#scalar-value-types) |  | voltage at 100 % |
| coefficients | [double](./scalar-value-types.md#scalar-value-types) | repeated | double[4]; coefficients for 3rd order polynomial |
