---
outline: deep
---

# Kinematic Calibration

This process describes how to align the zero position of the joints of a two-armed robot with the URDF reference.

- Preparation

This process can only be performed on a robot that has undergone approximate zero-point alignment.

The process includes moving the arms freely with gravity compensation. If the gravity compensation torque is significantly different from the required value, the robot may perform unsafe movements.

- Step 1

Use the code from [example/gravity_compensation](https://github1s.com/RainbowRobotics/rby1-sdk/blob/main/examples/gravity_compensation.cpp) to activate gravity compensation mode on both arms. If the mode works correctly, a person should be able to move the robot's arms freely.

- Step 2

Fix the provided calibration kit to both arms and run the [example/get_robot_state](https://github1s.com/RainbowRobotics/rby1-sdk/blob/main/examples/get_robot_state.cpp) code.

- Step 3

Collect joint position data in various postures (more than 20) and save the data.

- Step 4

Run the [example/kinematic_calibration](https://github1s.com/RainbowRobotics/rby1-sdk/blob/main/examples/kinematic_calibration.cpp) code. The deviation between the current robot's zero position and the URDF reference will be displayed using the collected data and pre-defined calibration kit information.

- Step 5

Move the robot to the position obtained from the previous step and perform a zero-point reset. For instructions on resetting the zero point, refer to [Zero-Point Reset Method](#).