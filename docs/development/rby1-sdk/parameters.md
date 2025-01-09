---
title: Parameters
outline: deep
---
# Prameters
## Prameter Lists
| Parameter Name  | Default Value     | Min Value        | Max Value        | Unit   |
|----------------------------------------------------------------------|-------------------|------------------|------------------|--------|
| `power_command.timeout`                                              | 1.0               | 0.0              | 10.0             | sec    |
| `servo_on_command.timeout`                                           | 15.0              | 0.0              | 30.0             | sec    |
| `servo_on_command.new_data_timeout`                                  | 3.0               | 0.0              | 10.0             | sec    |
| `control_threshold`                                                   | 0                 | 0                | 100              |        |
| `idle_to_default_controller_time`                                     | 0.1               | 0.0              | 1e5              | sec    |
| `default.velocity_limit_scaling`                                     | 1.0               | 0.01             | 1.5              |        |
| `default.acceleration_limit_scaling`                                 | 1.0               | 0.01             | 1.5              |        |
| `default.linear_acceleration_limit`                                  | 5.0               | 0.01             | 10.0             |        |
| `default.angular_acceleration_limit`                                 | 1.0               | 0.01             | 5.0              |        |
| `default.optimal_control_command.velocity_tracking_gain`            | 0.1               | 1e-5             | 1.0              |        |
| `default.optimal_control_command.stop_cost`                         | 1e-3              | 1e-6             | 1e9              |        |
| `default.se2_velocity_command.acceleration_limit`                   | 1.0               |5.0               |99.0                |        |
| `jog_command.one_step_size`                                          | 0.087266463(5 deg)       | 0.017453293(1 deg)      | 0.17453293  (10 deg)      | rad    |
| `jog_command.canceling_time`                                         | 0.1               | 1e-3             | 10.0             | sec    |
| `joint_position_command.cutoff_frequency`                            | 15.0              | 1e-3             | 100.0            | Hz     |
| `joint_position_command.canceling_time`                              | 0.1               | 1e-3             | 1.0              | sec    |
| `joint_position_command.torque_saturation_time`                      | 0.1               | 1e-3             | 1.0              | sec    |
| `cartesian_command.cutoff_frequency`                                 | 15.0              | 1e-3             | 100.0            | Hz     |
| `cartesian_command.canceling_time`                                   | 0.1               | 1e-3             | 1.0              | sec    |
| `cartesian_command.torque_saturation_time`                           | 0.1               | 1e-3             | 1.0              | sec    |
| `impedance_control_command.torque_saturation_time`                   | 0.1               | 1e-3             | 1.0              | sec    |
| `optimal_control_command.torque_saturation_time`                     | 0.1               | 1e-3             | 1.0              | sec    |
| `stop_command.canceling_time`                                        | 0.1               | 1e-3             | 1.0              | sec    |
| `stop_command.torque_saturation_time`                                | 0.1               | 1e-3             | 1.0              | sec    |
| `joint_velocity_command.canceling_time`                              | 0.1               | 1e-3             | 1.0              | sec    |
| `joint_velocity_command.torque_saturation_time`                      | 0.1               | 1e-3             | 1.0              | sec    |
| `se2_velocity_command.canceling_time`                                | 0.1               | 1e-3             | 1.0              | sec    |


## Example Usage in Python

```python
# Set parameters using the dot notation, following the provided examples
robot.set_parameter("default.acceleration_limit_scaling", "0.8")
robot.set_parameter("joint_position_command.cutoff_frequency", "5")
robot.set_parameter("cartesian_command.cutoff_frequency", "5")
robot.set_parameter("default.linear_acceleration_limit", "5")
```