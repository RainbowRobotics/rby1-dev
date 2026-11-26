# Control & System

## E-Stop Within Reach

::: danger WARNING
Code, teleoperation or a Web UI command can move the robot in an unexpected way. If you cannot stop it at once, it can hit you or others.

- Keep the E-Stop button (EMO) on the robot or the **Remote E-Stop** (wireless remote controller) within reach whenever the robot is powered and you run control code.
- If the robot moves unexpectedly, press the E-Stop.
- See [E-Stop Basics](../getting-started/estop-basics.md) for what the E-Stop does and how to recover.
:::

<img :src="$withBase('/images/safety_and_precautions/control_and_system/emo.jpg')" alt="Remote E-Stop (wireless remote controller) with buttons 1, 2 and 3 held in front of the robot; the front LED is red" class="center white-bg" style="width:40%">

---
## The Web UI Stop Buttons Are Not an E-Stop

::: danger WARNING
The Web UI has two stop buttons at the top of the screen. Both are software commands that travel over the network. If the connection is slow or lost, they do not reach the robot.

- **CANCEL CONTROL** cancels the current motion command. The power stays on.
- **ESTOP** cancels the current motion command and turns off all power lines.
- Neither button replaces the E-Stop button (EMO) or the Remote E-Stop (wireless remote controller). Keep one of them within reach.
:::

---
## Unlimit Mode

::: danger WARNING
In **Unlimit** mode the Control Manager does not check the joint operating range, so commands can move joints outside their limits. The robot can hit itself or reach poses that cause damage or injury.

Unlimit mode is enabled by any of these:
- the **Unlimit** button in the **Control Manager** card of the Web UI (also used by the Unpacking wizard),
- `robot.enable_control_manager(unlimited_mode_enabled=True)` in the Python SDK (C++: `EnableControlManager(true)`),
- `CMD_UNLIMIT` in the ROS 2 `control_manager_command` service (see [Services](../ros2/ros2_driver/services.md)),
- the ROS 2 driver while its parameter `control_manager_unlimited` is `true`: `CMD_ENABLE`, servo-on and motion or stream commands all enable the Control Manager in Unlimit mode when it is not already enabled.

Use Unlimit mode only when a procedure asks for it, such as unpacking. Afterwards, press **Disable**, then **Enable**, to go back to the standard mode before you use the SDK, teleoperation or ROS 2 (see [Connect to Hotspot & Check Web UI](../getting-started/hotspot-and-webui.md)). With ROS 2, also check that `control_manager_unlimited` is `false`. If it is `true`, the next ROS 2 servo-on or motion command enables Unlimit mode again after you disable the Control Manager. The driver reads this parameter only at startup, so restart the driver after you change it.
:::

---
## Connection Loss and Control Hold Time

::: danger WARNING
When your program stops sending commands (crash, network loss), the robot keeps its last command for the **Control Hold Time**. For velocity commands this means the robot **keeps moving** at the last velocity for that time, then stops.

- Keep the Control Hold Time of velocity commands short: a few times your stream period.
- See [Control Hold Time and Minimum Time](../sdk/controllers/generated/control_hold_time_and_minimum_time.md).
:::

---
## Control the Leader Arm and Gripper from the UPC

::: info NOTICE
The leader arm and the gripper are connected to the user PC (UPC) through a U2D2 (RS-485 to USB) device. They cannot be controlled from an external PC through the robot PC (RPC).

- To control the leader arm and the gripper from an external PC, connect to the UPC remotely and run your program on the UPC.
- See [User PC (UPC)](../software/upc.md) for how to reach the UPC, and [Leader Arm](../options/leader_arm.md) and [Gripper](../options/gripper.md).
:::
