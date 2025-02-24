---
title: Model M
outline: deep
---

# Model M Overview

> :bulb: **Note:** The most accurate information regarding the model can be found in the [URDF files under the models directory](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.4.1/models/rby1m/urdf/model.urdf) of the Rainbow Robotics SDK repository. It is highly recommended to refer to this source for the latest updates and details.

## Model Name
**M**

## Degrees of Freedom (DOF)
- **Total DOF**: 26

## Joint Names

The joint names of the M model are as follows:

- **Wheels**: `wheel_fr`, `wheel_fl`, `wheel_rr`, `wheel_rl`
- **Torso**: `torso_0`, `torso_1`, `torso_2`, `torso_3`, `torso_4`, `torso_5`
- **Right Arm**: `right_arm_0`, `right_arm_1`, `right_arm_2`, `right_arm_3`, `right_arm_4`, `right_arm_5`, `right_arm_6`
- **Left Arm**: `left_arm_0`, `left_arm_1`, `left_arm_2`, `left_arm_3`, `left_arm_4`, `left_arm_5`, `left_arm_6`
- **Head**: `head_0`, `head_1`

## Mobility Indexes
The indexes related to mobility are as follows:

- **Wheel FR(Front-Right) Index**: 0
- **Wheel FL(Front-Left) Index**: 1
- **Wheel RR(Rear-Right) Index**: 2
- **Wheel RL(Rear-Left) Index**: 3

## Body Indexes
The indexes related to the body parts are as follows:

- **Torso Indexes**: 4, 5, 6, 7, 8, 9
- **Right Arm Indexes**: 10, 11, 12, 13, 14, 15, 16
- **Left Arm Indexes**: 17, 18, 19, 20, 21, 22, 23

## Head Indexes
The indexes related to the head parts are as follows:
- **Head Indexes**: 24, 25

## Brake and Motor Information
### Components Without Brakes
The following components do not have brakes:
- **Wheels**: `wheel_fr`, `wheel_fl`, `wheel_rr`, `wheel_rl`
- **Head**: `head_0`, `head_1`
- **Right Arm**: `right_arm_6`
- **Left Arm**: `left_arm_6`

### Components Without Physical Brake Buttons
The following components have brakes but do not have physical buttons for releasing them (can only be released electronically):
- **Torso**: `torso_3`, `torso_4`, `torso_5`
- **Right Arm**: `right_arm_4`, `right_arm_5`
- **Left Arm**: `left_arm_4`, `left_arm_5`

### Components With Physical Brake Buttons
The following components have brakes and include physical buttons for releasing them:
- **Torso**: `torso_0`, `torso_1`, `torso_2`
- **Right Arm**: `right_arm_0`, `right_arm_1`, `right_arm_2`, `right_arm_3`
- **Left Arm**: `left_arm_0`, `left_arm_1`, `left_arm_2`, `left_arm_3`

## Motor Types
The motor types for each component are as follows:
- **Dynamixel Motors**: Used in the Head (`head_0`, `head_1`)
- **RBMotors**: Used in all other components (Torso, Wheels, Right Arm, Left Arm)


## Parameter Lists

| Parameter Name                                                        | Default Value                | Min Value          | Max Value          | Unit   |
|-----------------------------------------------------------------------|------------------------------|--------------------|--------------------|--------|
| `robot_model_name`                                                    | "rby1m"                      | -                  | -                  |        |
| `model_name`                                                          | ""                           | -                  | -                  |        |
| `battery_config` *(type, cutoff_voltage, fully_charged_voltage, ...)*  | [0, 44.7, 58.6, 1123.0, -61.587, 1.0168, -0.0045] | -  | -                  |        |
| `soft_stop_enabled`                                                   | 0                            | 0                  | 1                  |        |
| `power_command.timeout`                                               | 1.0                          | 0.0                | 10.0               | sec    |
| `servo_on_command.timeout`                                            | 15.0                         | 0.0                | 30.0               | sec    |
| `servo_on_command.new_data_timeout`                                   | 3.0                          | 0.0                | 10.0               | sec    |
| `gravity`                                                             | [0, 0, -9.8]                 | -                  | -                  | m/s²   |
| `default.velocity_limit_scaling`                                      | 1.0                          | 0.01               | 1.5                |        |
| `default.acceleration_limit_scaling`                                  | 1.0                          | 0.01               | 1.5                |        |
| `default.linear_acceleration_limit`                                   | 5.0                          | 0.01               | 10.0               |        |
| `default.angular_acceleration_limit`                                  | 1.0                          | 0.01               | 5.0                |        |
| `default.optimal_control_command.velocity_tracking_gain`              | 0.1                          | 1e-5               | 1.0                |        |
| `default.optimal_control_command.stop_cost`                           | 1e-3                         | 1e-6               | 1e9                |        |
| `default.se2_velocity_command.acceleration_limit`                     | [1.0, 5.0, 99.0]             | -                  | -                  |        |
| `jog_command.one_step_size`                                           | 0.087266463 (5°)             | 0.017453293 (1°)   | 0.17453293 (10°)   | rad    |
| `jog_command.canceling_time`                                          | 0.1                          | 1e-3               | 10.0               | sec    |
| `joint_position_command.cutoff_frequency`                             | 15.0                         | 1e-3               | 100.0              | Hz     |
| `joint_position_command.canceling_time`                               | 0.1                          | 1e-3               | 1.0                | sec    |
| `joint_position_command.torque_saturation_time`                       | 0.1                          | 1e-3               | 1.0                | sec    |
| `cartesian_command.cutoff_frequency`                                  | 15.0                         | 1e-3               | 100.0              | Hz     |
| `cartesian_command.canceling_time`                                    | 0.1                          | 1e-3               | 1.0                | sec    |
| `cartesian_command.torque_saturation_time`                            | 0.1                          | 1e-3               | 1.0                | sec    |
| `impedance_control_command.torque_saturation_time`                    | 0.1                          | 1e-3               | 1.0                | sec    |
| `optimal_control_command.torque_saturation_time`                      | 0.1                          | 1e-3               | 1.0                | sec    |
| `stop_command.canceling_time`                                         | 0.1                          | 1e-3               | 1.0                | sec    |
| `stop_command.torque_saturation_time`                                 | 0.1                          | 1e-3               | 1.0                | sec    |
| `joint_velocity_command.canceling_time`                               | 0.1                          | 1e-3               | 1.0                | sec    |
| `joint_velocity_command.torque_saturation_time`                       | 0.1                          | 1e-3               | 1.0                | sec    |
| `se2_velocity_command.canceling_time`                                 | 0.1                          | 1e-3               | 1.0                | sec    |


## Example Usage in Python

```python
# Set parameters using the dot notation, following the provided examples
robot.set_parameter("default.acceleration_limit_scaling", "0.8")
robot.set_parameter("joint_position_command.cutoff_frequency", "5")
robot.set_parameter("cartesian_command.cutoff_frequency", "5")
robot.set_parameter("default.linear_acceleration_limit", "5")
```