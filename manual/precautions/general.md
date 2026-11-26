# General

## Precautions

### ⚠️Risk of Injury from Sharp Edges on the Mecanum Mobile Base

- When lifting or handling the robot, take extra care around the lower inner area of the mecanum mobile base, as it may contain sharp components.
- Direct contact with these areas may cause cuts or puncture injuries.
- It is recommended to wear protective gloves when handling the robot.

![](/images/saftey_and_precautions/general_safety/mecanum_wheel.png)

---
### ⚠️No External Obstacle Collision Detection

- The robot does not provide collision detection for external obstacles.
- Always ensure that the surrounding environment is clear of obstacles before operation.
- Maintain a safe distance from the robot while it is moving.
- Self-collision (between the robot's own links) is **reported, not prevented**: the robot state reports the closest link distances (`collisions`), but the robot does **not** stop by itself. To stop on a close distance, your application must watch this value and send a stop command (see [`27_collisions.py`](https://github.com/RainbowRobotics/rby1-sdk/blob/main/examples/python/27_collisions.py)).

---
### ⚠️Perform Simulation Before Real Robot Testing

- It is strongly recommended to perform tests in a simulator environment before running the robot in real-world conditions.
- Simulation allows you to verify motions in advance and helps prevent unexpected or unsafe behavior.
- Please refer to the simulator setup guide for installation and usage instructions. ([Explore the RBY1 Simulator!](/simulators/simulators))

![](/images/saftey_and_precautions//general_safety/model_a.png)

![](/images/saftey_and_precautions/general_safety/model_m.png)
