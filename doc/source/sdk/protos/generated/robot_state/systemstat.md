(rb-api-systemstat)=
# SystemStat

- Source proto: [`rb/api/robot_state.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state.proto) (rby1-sdk v0.10.1)

CPU and memory usage and uptime of the robot PC (RPC).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cpu_usage | [double](../scalar-value-types.md) |  | % |
| memory_usage | [double](../scalar-value-types.md) |  | % |
| uptime | [double](../scalar-value-types.md) |  | sec |
| program_uptime | [double](../scalar-value-types.md) |  | sec |
