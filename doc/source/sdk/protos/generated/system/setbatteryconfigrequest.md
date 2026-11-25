(rb-api-setbatteryconfigrequest)=
# SetBatteryConfigRequest

- Source proto: `rb/api/system.proto`

Request to set battery config.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| cut_off_voltage | [double](../scalar-value-types.md) |  | voltage at 0 % |
| fully_charged_voltage | [double](../scalar-value-types.md) |  | voltage at 100 % |
| coefficients | [double](../scalar-value-types.md) | repeated | double[4]; coefficients for 3rd order polynomial |
