# Parameter Reference

Robot parameters are settings stored on the robot PC (RPC). They set limits, timeouts, filters and network options of the robot software.
All three models (A, M and UB) use the same parameters; only the value of `robot_model_name` differs.

## Read and set parameters

You can change parameters with the SDK or in the Web UI (**Settings** → **Parameters**, see [Web UI](../../../software/web-ui.md#settings)).

- **Names** use dots, for example `joint_position_command.cutoff_frequency`. Always give the full name with its prefix.
  A name without its prefix (for example `cutoff_frequency`) does not exist, and `set_parameter()` returns `False`.
- **Values** are passed as text in JSON format:
  - numbers: `"5"`, `"0.8"`
  - arrays: `"[0, 0, -9.8]"`
  - strings need quotes inside the text: `"\"RBY1_HOTSPOT\""`
- **Range**: a number outside the range of the parameter is refused, and `set_parameter()` returns `False`.
- **Storage**: by default (`write_db=True`) the new value is saved in the parameter database of the RPC and stays after a restart.
  With `write_db=False` the value is used only until the robot software restarts or until you call `reset_parameter()`.

```python
import rby1_sdk as rby

robot = rby.create_robot("192.168.30.1:50051", "a")  # your address and model
robot.connect()

for name, type_code in robot.get_parameter_list():   # type: 0 int, 1 double, 2 string, 3/4/5 array of 3/6/7 doubles
    print(name, robot.get_parameter(name))

robot.set_parameter("joint_position_command.cutoff_frequency", "5")        # saved permanently
robot.set_parameter("default.velocity_limit_scaling", "0.5", write_db=False)  # until restart
robot.reset_parameter("default.velocity_limit_scaling")       # back to the value saved in the database
robot.factory_reset_parameter("joint_position_command.cutoff_frequency")  # back to the default below
```

| Call | Effect |
| --- | --- |
| `get_parameter_list()` | Names and types of all parameters |
| `get_parameter(name)` | Current value as JSON text |
| `set_parameter(name, value, write_db=True)` | Set a value (see above) |
| `reset_parameter(name)` / `reset_all_parameters()` | Discard values set with `write_db=False`; read the saved values again |
| `factory_reset_parameter(name)` / `factory_reset_all_parameters()` | Set the default value and save it |

`reset_parameter_to_default()` and `reset_all_parameters_to_default()` are deprecated names of the factory reset calls.
C++ uses the same calls in CamelCase (`SetParameter`, `GetParameterList`, ...).
See the SDK example `05_parameter.py` ([Examples](../../../examples/ex.md)).

::: warning
Most parameters take effect while the robot runs. Lower limits make the robot slower; higher limits (scaling above 1.0, higher cutoff frequencies)
make it faster and less smooth. Test new values with the robot in a clear area and the E-Stop within reach.
:::

Parameters marked **Read at boot** below take effect only after the robot software restarts.

---

## 1. Robot and model

### `robot_model_name`
Model of the robot software: `"rby1a"`, `"rby1m"` or `"rby1ub"`. Do not change it.
At boot the robot software compares it with its own model; if they differ, it resets **all** parameters to the defaults.

- Type: `string`

### `model_name`
Name of a custom robot model (URDF) used for kinematics and dynamics on the robot. **Read at boot.**

- Type: `string`
- Default: `""` (the built-in model)

The robot software loads `<model_name>.urdf` from the models folder of the RPC. Add a model with `robot.import_robot_model(name, urdf_text)`.
If the file does not exist, the built-in model is used and the log shows a warning.

---

## 2. Battery & Power

### `battery_config`
Defines how the State of Charge (SoC) is calculated.

- Type: `array<double>` (size = 7)
- Format: `[type, cutoff_voltage, fully_charged_voltage, coeff_0, coeff_1, coeff_2, coeff_3]`
- Default: `[0, 46.0, 56.0, 25558.048, -1530.144, 30.294, -0.198]`

| Field | Description |
|------|------|
| type | 0: Voltage-based automatic calculation<br>1: Fixed manual level (test mode) |
| cutoff_voltage | Voltage corresponding to 0% (V) |
| fully_charged_voltage | Voltage corresponding to 100% (V) |
| coeff_0 ~ coeff_3 | Coefficients of a 3rd-order polynomial for voltage-to-percentage conversion |

Formula, with the battery voltage $V$:

$$
\text{percent} = c_3 V^3 + c_2 V^2 + c_1 V + c_0
$$

The value belongs to the battery pack of your robot. Do not copy it from another robot.

---
### `soft_stop_enabled`
Determines whether a soft stop sequence is applied when turning off 48V power.

- Type: `int (0 or 1)`
- Default: `0`

| Value | Description |
|------|------|
| 0 | Immediate power OFF |
| 1 | Soft stop enabled |

Soft stop sequence:
1. Switch to Position Lock
2. Engage brake
3. Enable Gravity Compensation
4. Reduce compensation ratio (1.0 → 0.6 over ~0.5 sec)
5. Turn off 48V power

---
### `power_command.timeout`
Maximum time to wait for the power state to reach the target (ON/OFF).

- Type: `double`
- Default: `1.0`
- Range: `0.0 ~ 10.0`
- Unit: `sec`

> If exceeded → command is marked as **failed**

---
### `major_fault_power_off_target`
Specifies the power-off targets when a Major Fault occurs. **Read at boot.**

- Type: `string (regex)`
- Default: `".*"`

> Internally applied as `"48v|" + pattern`
> → 48V is always included in the power-off target

---
### `boot.power_on_target`
Power rails that the robot software turns on at boot. Available from robot software 0.11.0. **Read at boot.**

- Type: `string (regex over the rail names 5v, 12v, 24v, 48v)`
- Default: `""` (nothing is turned on at boot)

Example: `"\"5v|12v\""`. This turns on power only; it does not turn on the servos or move the robot.

---
## 3. Command Timeout / State Validation

### Preset Position

### `preset_position_command.new_data_timeout`
Maximum time to wait for fresh joint state data before executing the command.

- Type: `double`
- Default: `3.0 sec`
- Range: `0.0 ~ 10.0`
- Unit: `sec`

### `preset_position_command.timeout`
Maximum time to wait for the preset state to be reached.

- Type: `double`
- Default: `5.0 sec`
- Range: `0.0 ~ 30.0`
- Unit: `sec`

> Timeout → command fails

---
### Servo On

### `servo_on_command.new_data_timeout`
Maximum time to wait for fresh state data before executing Servo On/Off.

- Type: `double`
- Default: `3.0 sec`
- Range: `0.0 ~ 10.0`
- Unit: `sec`

### `servo_on_command.timeout`
Maximum time to wait for the joint to become ready after Servo On.

- Type: `double`
- Default: `15.0 sec`
- Range: `0.0 ~ 30.0`
- Unit: `sec`

> Timeout → command fails

---
## 4. Dynamics

### `gravity`
Gravity acceleration vector used in dynamics computation, in the base frame (see [Units and Frames](../../../software/units-and-frames.md)).

- Type: `array<double, 3>`
- Default: `[0, 0, -9.8]`
- Unit: `m/s²`

> Used for gravity term calculation and gravity compensation torque.

---
### `friction_compensation_enabled`
Adds a friction compensation torque to the arm joints. Available from robot software 0.11.0.

- Type: `int (0 or 1)`
- Default: `0` (off)

The torque is computed from the measured joint velocity with a viscous and Coulomb friction model.
The model was identified on hardware version v1.2 arms. The torso and the joints of Model UB's torso are not compensated.

### `friction_compensation_gain`
Scale of the friction compensation torque.

- Type: `double`
- Default: `1.0`
- Range: `0.5 ~ 1.1`

---
## 5. Limit Scaling

### `default.acceleration_limit_scaling`
Scaling factor applied to joint acceleration limits.

- Type: `double`
- Default: `1.0`
- Range: `0.01 ~ 1.5`

Applied concept: acceleration limit = joint acceleration limit × default.acceleration_limit_scaling

If a request-specific acceleration_limit_scaling is provided, the final acceleration limit is computed as:
joint acceleration limit × default.acceleration_limit_scaling × request.acceleration_limit_scaling

---
### `default.velocity_limit_scaling`
Scaling factor applied to joint velocity limits.

- Type: `double`
- Default: `1.0`
- Range: `0.01 ~ 1.5`

Applied concept: velocity limit = joint velocity limit × default.velocity_limit_scaling

If a request-specific velocity_limit_scaling is provided, the final velocity limit is computed as:
joint velocity limit × default.velocity_limit_scaling × request.velocity_limit_scaling

---
### `default.torque_limit_scaling`
Scaling factor applied to joint torque limits.

- Type: `double`
- Default: `1.0`
- Range: `0.01 ~ 1.5`

Applied concept: torque limit = joint torque limit × default.torque_limit_scaling

---
## 6. Acceleration Limits

### `default.linear_acceleration_limit`
Default linear acceleration limit used by Cartesian-type commands.

- Type: `double`
- Default: `20.0`
- Range: `0.01 ~ 60.0`
- Unit: `m/s²`

---

### `default.angular_acceleration_limit`
Default angular acceleration limit used by Cartesian-type commands.

- Type: `double`
- Default: `10.0`
- Range: `0.01 ~ 30.0`
- Unit: `rad/s²`

---

## 7. Tracking Error

### `default.cartesian_command.stop_position_tracking_error`
Position tracking error threshold used to determine completion of a Cartesian Command.

- Type: `double`
- Default: `0.005` (5 mm)
- Range: `1e-4 ~ 1.0`
- Unit: `m`

If the position error is smaller than this threshold, the target is considered reached.

---

### `default.cartesian_command.stop_orientation_tracking_error`
Orientation tracking error threshold used to determine completion of a Cartesian Command.

- Type: `double`
- Default: `0.02`
- Range: `1e-3 ~ 0.1`
- Unit: `rad`

If the orientation error is smaller than this threshold, the target is considered reached.

---

### `default.cartesian_command.stop_joint_position_tracking_error`
Joint position tracking error threshold used to determine completion of a Cartesian Command.

- Type: `double`
- Default: `0.01`
- Range: `1e-3 ~ 0.1`
- Unit: `rad`

If |q - q_target| is smaller than this threshold, the target is considered reached.

---

### `default.cartesian_impedance_control_command.stop_joint_position_tracking_error`

Joint position tracking error threshold used to determine completion of a Cartesian Impedance Control command.

- Type: `double`
- Default: `0.01`
- Range: `1e-3 ~ 0.1`
- Unit: `rad`

---

### `default.cartesian_impedance_control_command.stop_orientation_tracking_error`

Orientation tracking error threshold used to determine completion of a Cartesian Impedance Control command.

- Type: `double`
- Default: `0.02`
- Range: `1e-3 ~ 0.1`
- Unit: `rad`

---

### `default.cartesian_impedance_control_command.stop_position_tracking_error`

Position tracking error threshold used to determine completion of a Cartesian Impedance Control command.

- Type: `double`
- Default: `0.005` (5 mm)
- Range: `1e-4 ~ 1.0`
- Unit: `m`

---

## 8. Motion Filtering & Canceling

Two kinds of parameters exist for several commands. Each command has its own parameter; set it with the full name from the table.

- **`<command>.cutoff_frequency`**: low-pass filter (LPF) cutoff frequency of the command target.
  A higher value gives a faster response (less smooth); a lower value gives smoother motion (slower response).
- **`<command>.canceling_time`**: time for a smooth deceleration when the command is canceled.

| Parameter | Default | Range | Unit |
| --- | --- | --- | --- |
| `joint_position_command.cutoff_frequency` | 15 | 1e-3 ~ 100 | Hz |
| `optimal_control_command.cutoff_frequency` | 15 | 1e-3 ~ 100 | Hz |
| `cartesian_command.cutoff_frequency` | 15 | 1e-3 ~ 100 | Hz |
| `joint_group_position_command.cutoff_frequency` | 15 | 1e-3 ~ 100 | Hz |
| `jog_command.canceling_time` | 0.1 | 1e-3 ~ 10.0 | sec |
| `joint_position_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |
| `cartesian_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |
| `stop_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |
| `joint_velocity_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |
| `se2_velocity_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |
| `joint_impedance_control_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |
| `cartesian_impedance_control_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |
| `joint_group_position_command.canceling_time` | 0.1 | 1e-3 ~ 1.0 | sec |

There is no `cutoff_frequency` for the other commands, and no `optimal_control_command.canceling_time`.

---

## 9. Jog Control

### `jog_command.one_step_size`
Joint angle step size for one-step mode in Jog Command.

- Type: `double`
- Default: `0.087266463 rad (5°)`
- Range: `0.017453293 ~ 0.17453293 (1° ~ 10°)`
- Unit: `rad`

---

## 10. SE2 Base Control

### `default.se2_velocity_command.acceleration_limit`
Default acceleration limit used by SE2 Velocity Command.

- Type: `array<double,3>`
- Default: `[1.0, 5.0, 99.0]`
- Order: `[angular, linear.x, linear.y]`
- Unit: `rad/s²` (angular), `m/s²` (linear)

This defines the acceleration ramp limit toward the target angular and linear base velocities.

---
## 11. Optimal Control

### `default.optimal_control_command.stop_cost`
Cost threshold used to determine convergence of an Optimal Control Command.

- Type: `double`
- Default: `1e-3`
- Range: `1e-6 ~ 1e9`

The command is considered converged when: last_cost < stop_cost.
See [Command and Control Architecture](command_and_control_architecture.md#optimal-control) for the other convergence settings of the command.

---

## 12. Safety & Stability

### `manipulability_threshold`
Manipulability threshold used to detect singularity risk during control.

- Type: `double`
- Default: `1e4`
- Range: `1e2 ~ 1e10`

If the current manipulability value exceeds this threshold, the command fails due to a singularity condition.

---

### `real_time_control.max_timeout_count`
Maximum number of consecutive control cycles without a new packet from your program in Real-Time Control.

- Type: `int`
- Default: `10`
- Range: `1 ~ 500`
- Unit: control cycles of 2 ms (default 10 = 20 ms; maximum 500 = 1 s)
- Available from robot software 0.10.2

In every 2 ms cycle without a new packet, the robot software **applies the last received command again**,
including its feedforward torque. When the count reaches this value, real-time control ends: each joint holds its
current position with zero feedforward torque, and the command finishes.

::: warning
During the timeout the last command, including its torque, keeps acting on the robot. A large value lets a stopped
or stalled program keep driving the robot for up to 1 s. Keep the value small and send packets every cycle.
:::

---

## 13. Network

These parameters are used by the robot PC (RPC) Wi‑Fi. The Web UI sets them in **Settings** → **RPC Hotspot** and **RPC WiFi Settings**
(see [Web UI](../../../software/web-ui.md#settings)). New hotspot values are used the next time the hotspot starts.

| Parameter | Type | Default | Values | Available from |
| --- | --- | --- | --- | --- |
| `hotspot.ssid` | string | `"RBY1"` | Hotspot network name | 0.5.0 |
| `hotspot.password` | string | factory password (see [Hotspot & Web UI](../../../getting-started/hotspot-and-webui.md)) | 8 to 63 characters | 0.5.0 |
| `hotspot.band` | string | `"2.4"` | `"2.4"` or `"5"` (GHz) | 0.11.0 |
| `hotspot.channel` | int | `0` | `0` = automatic, up to 196 | 0.11.0 |
| `hotspot.ht` | int | `1` | `1` = use 802.11n (and 802.11ac on 5 GHz) | 0.11.0 |
| `hotspot.width` | int | `0` | Channel width in MHz: `0` = automatic, 20, 40, 80 (5 GHz) | 0.11.0 |
| `wifi.band` | string | `"auto"` | Band used when the RPC joins your Wi‑Fi network: `"auto"`, `"2.4"` or `"5"` | 0.11.0 |

---

Verified against: robot core v0.11.0 `core/robots/rby1a/parameters.h` (names, defaults, ranges; `rby1m` and `rby1ub` differ only in
`robot_model_name`), `core/base/parameters.h` (dot names, JSON values, `write_db`, range check, reset and factory reset),
`core/robots/rby1a/robot_app.cpp` (`robot_model_name` check at boot, `model_name`, `boot.power_on_target`,
`major_fault_power_off_target` read at boot), `core/robots/robot_app_base.cpp` (`SetupDynamicsModel`),
`core/control/control_manager.cpp` (friction compensation), `core/control/impl/rt.h` (real-time timeout),
`core/service/srv_robot_command_builder.cpp` (5 mm comment); rby1-sdk v0.10.1 `src/robot.cpp` (`SetParameter` JSON),
`python/robot.cpp` (parameter calls and the `hotspot.ssid` example), `protos/rb/api/parameter.proto` (type codes),
`include/rby1-sdk/model.h` (`kControlPeriod = 0.002`), `examples/python/05_parameter.py`.
