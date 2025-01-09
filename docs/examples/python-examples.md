---
title: Python Examples  
outline: deep
---
# Python Examples

Here is a list of available Python example programs for the Rainbow Robotics SDK. Explore each example by clicking on the corresponding link.

> :warning: **Important Warning**: This documentation is based on the **main branch** of the SDK repository. The **dev branch** may include additional features that are currently in development. However, since these features are not fully tested, we are not responsible for any issues arising from using the dev branch. Use it with caution.

> :information_source: **Note**: Unfortunately, there is no teleoperation example provided in the Python examples. If you are looking for a teleoperation example, please refer to the C++ examples.  
> Keep in mind that the **Master Arm** and **Gripper** are controlled primarily by **Dynamixel**, not through our SDK, and most of the code used is from ROBOTIS.  
> A simple example for the gripper is available in the **dev branch** under `examples/python/module_test`. However, this example has not been officially released and is not recommended for use (as of October 17, 2024).



## Available Python Examples
- [01_hello_rby1.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/01_hello_rby1.py): A simple "Hello, RB-Y1" example to get started.
- [02_power.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/02_power.py): Power control example.
- [03_robot_state.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/03_robot_state.py): Robot state retrieval example.
- [04_robot_state_stream.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/04_robot_state_stream.py): Streaming robot state data.
- [05_collisions.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/05_collisions.py): Example of collision checking.
- [09_demo_motion.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/09_demo_motion.py): Basic robot motion control example.  
  > :warning: **Warning**: This demo executes large and faster movements compared to the C++ version. Ensure the surroundings are clear and secure before running this example.
- [command_stream.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/command_stream.py): Command streaming example.
- [ft_sensor.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/ft_sensor.py): Example of force/torque sensor integration.
- [log.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/log.py): Example demonstrating logging functionalities.
- [robot_info.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/robot_info.py): Retrieve robot information.
- [robot_model.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/robot_model.py): Access robot model data.
- [robot_state.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/robot_state.py): Another example for retrieving robot state.
- [send_robot_command.py](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python/send_robot_command.py): Example of sending commands to the robot.
- ...

For more details, visit the full Python examples directory:  
**[GitHub Python Examples](https://github.com/RainbowRobotics/rby1-sdk/tree/main/examples/python)**
