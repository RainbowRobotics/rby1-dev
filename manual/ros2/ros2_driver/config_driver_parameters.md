# Config File

## driver_parameters.yaml

| Parameter | Default | Unit | Description |
|-----------|---------|------|-------------|
| `robot_ip` | `"127.0.0.1:50051"` | - | Robot IP address and gRPC port |
| `model` | `"m"` | - | Robot model — `"a"` (RBY1-A) or `"m"` (RBY1-M) |
| `get_state_period` | `0.01` | s | State publish interval — default 0.01 (100 Hz) |
| `minimum_time` | `2.0` | s | Default minimum execution time for motion commands |
| `stream_hz` | `30.0` | Hz | Frequency for trajectory streaming |
| `angular_velocity_limit` | `4.712388` | rad/s | Joint angular velocity limit |
| `linear_velocity_limit` | `1.5` | m/s | Cartesian linear velocity limit |
| `acceleration_limit` | `1.0` | - | Acceleration scaling factor |
| `stop_orientation_tracking_error` | `1e-5` | rad | Orientation tracking error threshold to detect stop |
| `stop_position_tracking_error` | `1e-5` | m | Position tracking error threshold to detect stop |
| `se2_minimum_time` | `1.0` | s | Minimum execution time (interpolation ramp) for SE2 velocity commands |
| `se2_linear_acceleration_limit` | `0.5` | m/s² | Linear acceleration limit for SE2 velocity commands |
| `se2_angular_acceleration_limit` | `0.5` | rad/s² | Angular acceleration limit for SE2 velocity commands |
| `fault_reset_trigger` | `false` | - | Auto-reset MAJOR/MINOR fault on driver startup |
| `collision_threshold` | `0.02` | m | Minimum link-distance threshold for collision detection |
| `publish_battery_state` | `true` | - | Enable battery state topic |
| `publish_tool_flange_state` | `true` | - | Enable tool flange state topics (left + right) |
