# Parameter Reference

## 1. Battery & Power
<br>


### `battery_config`
Defines how the Status of Charge (`SoC`) is calculated.

- Type: `array<double>` (size = 7)  
- Format: [type, cutoff_voltage, fully_charged_voltage, coeff_0, coeff_1, coeff_2, coeff_3]

| Field | Description |
|------|------|
| type | 0: Voltage-based automatic calculation<br>1: Fixed manual level (test mode) |
| cutoff_voltage | Voltage corresponding to 0% (V) |
| fully_charged_voltage | Voltage corresponding to 100% (V) |
| coeff_0 ~ coeff_3 | Coefficients of a 3rd-order polynomial for voltage-to-percentage conversion |

- Formula: percent = coeff_3V^3 + coeff_2V^2 + coeff_1*V + coeff_0


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
Specifies the power-off targets when a Major Fault occurs.

- Type: `string (regex)`
- Default: `".*"`

> ⚠️ Internally applied as `"48v|" + pattern`  
> → 48V is always included in the power-off target


---
## 2. Command Timeout / State Validation
<br>


### Preset Position
<br>


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
<br>


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
## 3. Dynamics
<br>


### `gravity`
Gravity acceleration vector used in dynamics computation.

- Type: `array<double, 3>`
- Default: `[0, 0, -9.8]`
- Unit: `m/s²`

> Used for gravity term calculation and gravity compensation torque.


---
## 4. Limit Scaling
<br>


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
## 5. Acceleration Limits
<br>



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

## 6. Tracking Error
<br>


### `default.cartesian_command.stop_position_tracking_error`
Position tracking error threshold used to determine completion of a Cartesian Command.


- Type: `double`
- Default: `0.005`
- Range: `1e-4 ~ 0.1`
- Unit: `mm`

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
Position tracking error threshold used to determine completion of a Cartesian Command.

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
- Default: `0.005`
- Range: `1e-4 ~ 1.0`
- Unit: `mm`


---

## 7. Motion Filtering & Canceling

Common concepts applied across multiple commands.
<br>


### `cutoff_frequency`
Low-pass filter (LPF) cutoff frequency

- Higher value → faster response (less smooth)  
- Lower value → smoother motion (slower response)

- Type: `double`
- Default: `15`
- Range: `1e-3 ~ 100`
- Unit: `Hz`

---

### `canceling_time`
Time constant for smooth deceleration when canceling a command

- Type: `double`
- Default: `0.1`
- Range: `1e-3 ~ 1.0`
- Unit: `sec`

---

### Applied To

- `jog_command`
- `joint_position_command`
- `joint_group_position_command`
- `joint_impedance_control_command`
- `cartesian_command`
- `cartesian_impedance_control_command`
- `optimal_control_command`
- `joint_velocity_command`
- `se2_velocity_command`
- `stop_command`

---

## 8. Jog Control
<br>


### `jog_command.one_step_size`
Joint angle step size for one-step mode in Jog Command.

- Type: `double`
- Default: `0.087 rad (≈ 5°)`
- Range: `0.017453293 ~ 0.17453293 (1° ~ 10°)`
- Unit: `rad`


---

## 9. SE2 Base Control
<br>


### `default.se2_velocity_command.acceleration_limit`
Default acceleration limit used by SE2 Velocity Command.

- Type: `array<double,3>`
- Default: `[1.0, 5.0, 99.0]`
- Order: `[angular, linear.x, linear.y]`

This defines the acceleration ramp limit toward the target angular and linear base velocities.


---
## 10. Optimal Control
<br>


### `default.optimal_control_command.stop_cost`
Cost threshold used to determine convergence of an Optimal Control Command.

- Type: `double`
- Default: `1e-3`
- Range: `1e-6 ~ 1e9`

The command is considered converged when: last_cost < stop_cost

---

## 11. Safety & Stability
<br>


### `manipulability_threshold`
Manipulability threshold used to detect singularity risk during control.

- Type: `double`
- Default: `1e4`
- Range: `1e2 ~ 1e10`

If the current manipulability value exceeds this threshold, the command fails due to a singularity condition.

---

### `real_time_control.max_timeout_count`
Maximum number of consecutive communication timeouts allowed in Real-Time Control.

- Type: `int`
- Default: `10`
- Range: `1~500`

If the number of consecutive timeouts reaches this value, control is safely terminated (finish = true).
