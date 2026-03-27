# Model UB
##

```{note} The most accurate information regarding the model can be found in the 
<a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.4.1/models/rby1t5/urdf/model.urdf"
target="_blank" rel="noopener noreferrer">
URDF files under the models directory
</a> 
of the Rainbow Robotics SDK repository. It is highly recommended to refer to this source for the latest updates and details.
```

<br>

```{image} /_static/images/model/model_ub/model_ub.png
   :alt: Model UB
   :align: center
   :width: 400px
   ```

---
### Degrees of Freedom (DOF)
<br>

- Total DOF: 23

---

### Joint Names
<br>

The joint names of the T5 model are as follows:

- **Wheels**: `right_wheel`, `left_wheel`
- **Torso**: `torso_0`, `torso_1`, `torso_2`, `torso_3`, `torso_4`
- **Right Arm**: `right_arm_0`, `right_arm_1`, `right_arm_2`, `right_arm_3`, `right_arm_4`, `right_arm_5`, `right_arm_6`
- **Left Arm**: `left_arm_0`, `left_arm_1`, `left_arm_2`, `left_arm_3`, `left_arm_4`, `left_arm_5`, `left_arm_6`
- **Head**: `head_0`, `head_1`

---
### Mobility Indexes
<br>

The indexes related to mobility are as follows:

- **Right Wheel Index**: 0
- **Left Wheel Index**: 1

---
### Body Indexes
<br>

The indexes related to the body parts are as follows:

- **Torso Indexes**: 2, 3, 4, 5, 6
- **Right Arm Indexes**: 7, 8, 9, 10, 11, 12, 13
- **Left Arm Indexes**: 14, 15, 16, 17, 18, 19, 20

---
### Head Indexes
<br>

The indexes related to the head parts are as follows:

- **Head Indexes**: 21, 22

---
### Brake and Motor Information
<br>

#### Components Without Brakes

The following components do not have brakes:

- Wheels: `right_wheel`, `left_wheel`
- Head: `head_0`, `head_1`
- Right Arm: `right_arm_6`
- Left Arm: `left_arm_6`

<br>

#### Components Without Physical Brake Buttons

The following components have brakes but do not have physical buttons for releasing them (can only be released electronically):

- Torso: `torso_2`, `torso_3`, `torso_4`
- Right Arm: `right_arm_4`, `right_arm_5`
- Left Arm: `left_arm_4`, `left_arm_5`

<br>

#### Components With Physical Brake Buttons

The following components have brakes and include physical buttons for releasing them:

- Torso: `torso_0`, `torso_1`
- Right Arm: `right_arm_0`, `right_arm_1`, `right_arm_2`, `right_arm_3`
- Left Arm: `left_arm_0`, `left_arm_1`, `left_arm_2`, `left_arm_3`

---
### Motor Types
<br>

The motor types for each component are as follows:

- Dynamixel Motors: Used in the Head (`head_0`, `head_1`)
- RBMotors: Used in all other components (Torso, Wheels, Right Arm, Left Arm)


---
### Parameter Lists
<br>


| Parameter Name | Default Value |	Min Value | Max Value | Unit |
| -------------- | ------------- | ---------- | --------- | ---- |
|`robot_model_name`                                                 | "rby1t5"                                          |  -   |   -  |     |	
|`model_name`	                                                     | ""                                                |      |   -  |  -  |
|`battery_config` (type, cutoff_voltage, fully_charged_voltage, ...)| [0, 44.7, 58.6, 1123.0, -61.587, 1.0168, -0.0045] |	 -  |   -  |     |
|`power_command.timeout`                                            | 1.0                                               | 0.0  | 10.0 | sec |
|`servo_on_command.timeout`                                         | 15.0                                              |	0.0 | 30.0 | sec |
|`servo_on_command.new_data_timeout`                                | 3.0                                               | 0.0  |	10.0 | sec |
|`gravity`                                                          | [0, 0, -9.8]                                      |	 -  |   -  | m/s²|
|`default.velocity_limit_scaling`                                   | 1.0                                               |	0.01|	 1.5 |	  |
|`default.acceleration_limit_scaling`                               | 1.0                                               |	0.01|	 1.5 |	  |
|`default.linear_acceleration_limit`                                | 5.0                                               |	0.01|	10.0 |     |
|`default.angular_acceleration_limit`                               | 1.0                                               |	0.01|	 5.0 |	  |
|`default.optimal_control_command.velocity_tracking_gain`           | 0.1                                               |	1e-5|	 1.0 |     |
|`default.optimal_control_command.stop_cost`                        | 1e-3                                              |	1e-6|	 1e9 |     |
|`default.se2_velocity_command.acceleration_limit`                  | [1.0, 5.0, 99.0]                                  |	 -  |	  -  |     |
|`jog_command.one_step_size`                                        | 0.087266463 (5°)          | 0.017453293 (1°) | 0.17453293 (10°) | rad |
|`jog_command.canceling_time`                                       | 0.1                                               | 1e-3 | 10.0 | sec |
|`joint_position_command.cutoff_frequency`                          | 15.0                                              | 1e-3 | 100.0| Hz  |
|`joint_position_command.canceling_time`                            | 0.1	                                             | 1e-3 | 1.0  | sec |
|`joint_position_command.torque_saturation_time`                    | 0.1	                                             | 1e-3 | 1.0  | sec |
|`cartesian_command.cutoff_frequency`                               | 15.0                                              | 1e-3 | 100.0| Hz  |
|`cartesian_command.canceling_time`                                 | 0.1	                                             | 1e-3 | 1.0  | sec |
|`cartesian_command.torque_saturation_time`                         | 0.1	                                             | 1e-3 | 1.0  | sec |
|`impedance_control_command.torque_saturation_time`                 | 0.1	                                             | 1e-3 | 1.0  | sec |
|`optimal_control_command.torque_saturation_time`                   | 0.1	                                             | 1e-3 | 1.0  | sec |
|`stop_command.canceling_time`                                      | 0.1	                                             | 1e-3 | 1.0  | sec |
|`stop_command.torque_saturation_time`                              | 0.1	                                             | 1e-3 | 1.0  | sec |
|`joint_velocity_command.canceling_time`                            | 0.1	                                             | 1e-3 | 1.0  | sec |
|`joint_velocity_command.torque_saturation_time`                    | 0.1	                                             | 1e-3 | 1.0  | sec |
|`se2_velocity_command.canceling_time`                              | 0.1                                               | 1e-3 | 1.0  | sec |

---
### Example Usage in Python
<br>

```python
# Set parameters using the dot notation, following the provided examples
robot.set_parameter("default.acceleration_limit_scaling", "0.8")
robot.set_parameter("joint_position_command.cutoff_frequency", "5")
robot.set_parameter("cartesian_command.cutoff_frequency", "5")
robot.set_parameter("default.linear_acceleration_limit", "5")
```