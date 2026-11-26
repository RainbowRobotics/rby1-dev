# Driver Parameters

The driver reads its parameters from `rby1_driver/config/driver_parameters.yaml`.
The workspace is built with `--symlink-install`, so an edit to this file needs no rebuild. Restart the driver to apply it.

## Launch arguments

```bash
ros2 launch rby1_driver rby1_ros2_driver.launch.py
ros2 launch rby1_driver rby1_ros2_driver.launch.py robot_ip:=192.168.30.1:50051 model:=a
ros2 launch rby1_driver rby1_ros2_driver.launch.py params_file:=/path/to/my.yaml namespace:=rby1
```

| Launch argument | Default | Description |
|---|---|---|
| `params_file` | `config/driver_parameters.yaml` | The parameter file below |
| `namespace` | `rby1` | Namespace of the node and of every topic, service and action |
| `robot_ip`, `model` | the file's values | Given on the command line, they override the file |

## driver_parameters.yaml

These are all the keys of the file in rby1-ros2 v1.0.0.

| Parameter | Default | Unit | Description |
|-----------|---------|------|-------------|
| `robot_ip` | `"127.0.0.1:50051"` | - | Robot address and gRPC port. For the simulator keep `127.0.0.1:50051` or `localhost:50051` |
| `model` | `"m"` | - | `"a"` (RB-Y1 A) or `"m"` (RB-Y1 M). Must match the robot or the simulator image |
| `stream_command_hz` | `30.0` | Hz | How often `cmd_vel` is expected. Each `cmd_vel` message is carried out for 1.1 × 1/`stream_command_hz` (about 37 ms at 30 Hz) |
| `joint_position_command_cutoff_frequency` | `15.0` | Hz | **Written to the robot at connect** (robot parameter `joint_position_command.cutoff_frequency`): the joint position command filter |
| `cartesian_command_cutoff_frequency` | `15.0` | Hz | **Written to the robot at connect** (`cartesian_command.cutoff_frequency`): the Cartesian command filter |
| `default_acceleration_limit_scaling` | `1.0` | - | **Written to the robot at connect** (`default.acceleration_limit_scaling`): scales the acceleration limits of commands that give none, 0 to 1 |
| `default_velocity_limit_scaling` | `1.0` | - | **Written to the robot at connect** (`default.velocity_limit_scaling`): scales the velocity limits of commands that give none, 0 to 1 |
| `default_linear_acceleration_limit` | `20.0` | m/s² | **Written to the robot at connect** (`default.linear_acceleration_limit`): linear acceleration limit of Cartesian commands |
| `default_angular_acceleration_limit` | `10.0` | rad/s² | **Written to the robot at connect** (`default.angular_acceleration_limit`): angular acceleration limit of Cartesian commands |
| `se2_minimum_time` | `1.0` | s | Interpolation ramp of a `cmd_vel` (SE2 velocity) command |
| `se2_linear_acceleration_limit` | `0.5` | m/s² | Linear acceleration limit of `cmd_vel` commands |
| `se2_angular_acceleration_limit` | `0.5` | rad/s² | Angular acceleration limit of `cmd_vel` commands |
| `collision_threshold` | `0.02` | m | Link distance below which a posture is reported as a collision. The driver only reports it; it does not stop the robot ([Key Features](key_features.md#predictive-collision-checking)) |
| `control_manager_unlimited` | `false` | - | `true` enables the Control Manager in unlimited mode, also for a plain `CMD_ENABLE`. See the warning below |
| `publish_battery_state` | `true` | - | Publish `battery_state` |
| `publish_tool_flange_state` | `true` | - | Publish the tool flange IMU and wrench topics. The flange status (connected, voltage, switch) is always in `robot_state` |

::: warning Six values are stored on the robot
The six parameters marked **Written to the robot at connect** are sent to the robot with the SDK's `SetParameter` each time the driver connects.
The robot keeps them in its own database, so they stay in effect after the driver exits, also for SDK programs and the Web UI.
The defaults are the robot's own shipped values. Drivers before 2026-10-26 wrote other values (cutoff 4.71 Hz and 1.5 Hz,
linear acceleration 1.0 m/s²); the first connection of the v1.0.0 driver replaces them.
If you change these values, every later user of the robot gets them too.
:::

::: danger control_manager_unlimited
With `control_manager_unlimited: true` the Control Manager is enabled without checking the joint limits.
Use it only to move a joint that stopped just outside its limit back inside, then set it back to `false`.
While it is on, nothing stops a command at the joint limits at enable time. Keep the E-Stop within reach.
:::

## Values fixed in the driver

These are not parameters. They are constants in `rby1_driver/include/default_parameters.hpp`, each with its reason.
To change one, edit that file and rebuild.

| Value | Setting |
|---|---|
| State loop period | 0.01 s (100 Hz, the rate the robot gives its state) |
| State loss timeout | 1.0 s: the driver stops when state reads keep failing this long |
| `minimum_time` of a command that leaves it at 0 | 2.0 s |
| Cartesian velocity limits of a command that gives none | 1.5 m/s, 4.712388 rad/s |
| Acceleration scaling of a command that gives none | 1.0 |
| Joint impedance of a command that gives none | stiffness 100 N·m/rad, damping ratio 1.0, torque limit 10 N·m |
| Control hold time of streamed commands | 1e6 s: a streamed command holds its part until the channel is closed |
| Control hold time of a `cmd_vel` command | 1.0 s |
| Idle close of a stream channel | 60 s, only for a channel that never got a command |
| Reopen gap after a stream closes | 0.3 s |

## Keys of earlier driver versions

Driver versions before v1.0.0 used the keys below. v1.0.0 does not declare them, and the driver ignores them if they are in the file.

| Old key | In v1.0.0 |
|---|---|
| `get_state_period` | Fixed at 0.01 s (100 Hz) in the driver |
| `minimum_time` | Fixed default 2.0 s; set `minimum_time` per command in [`JointCommand` / `CartesianCommand`](custom_message_types.md) |
| `stream_hz` | Replaced by `stream_command_hz` (for `cmd_vel`) |
| `angular_velocity_limit`, `linear_velocity_limit`, `acceleration_limit` | Fixed defaults; set them per command |
| `stop_orientation_tracking_error`, `stop_position_tracking_error` | Fields of the `Rby1CartesianCommand` goal |
| `fault_reset_trigger` | Removed. On a motion command the driver resets a Control Manager fault, major or minor, and enables the Control Manager by itself ([Safety & Fault Management](key_features.md#safety--fault-management)) |

Verified against: rby1-ros2 v1.0.0 `rby1_driver/config/driver_parameters.yaml`, `rby1_driver/src/rby1_ros2_driver.cpp` (`init_parameter`), `rby1_driver/include/default_parameters.hpp`, `rby1_driver/src/command_builder.cpp`, `Doc/manual/02_driver.md`.
