# Gripper

The standard gripper is sold as an option. It uses one Dynamixel XM430-W210 actuator per gripper.
The gripper was redesigned in v1.1 (see [Robot Model Version](../sdk/models/generated/model_version.md)).

<img :src="$withBase('/images/options/gripper/rby_gripper_info.png')" alt="Gripper drawing with front and side dimensions" class="center white-bg" style="width:600px">

## Specifications

| Item | Value |
| --- | --- |
| Actuator | Dynamixel XM430-W210 |
| Stroke | 100 mm |
| Finger speed | 40 mm/s |
| Weight | 530 g |
| Size (L x W x H) | 126 x 55 x 133 mm |
| Mounting | 2 x M4 tapped holes, depth 7 mm, 30 mm apart |

The drawing shows a height of 152.7 mm from the mounting face to the fingertips.

## Communication and power

| Item | Value |
| --- | --- |
| Device on the user PC (UPC) | `/dev/rby1_gripper` (U2D2 USB-to-RS485 converter) |
| Protocol | Dynamixel Protocol 2.0 |
| Baud rate | 2 Mbps |
| Dynamixel ID | right gripper: 0, left gripper: 1 |
| Operating mode at power on | Current control |
| Supply voltage | 12 V (the SDK example sets the tool flange output to 12 V) |

::: warning
Set the tool flange output to **12 V** for this gripper. The Max Voltage Limit of the gripper actuator is 16 V. Do not set the tool flange output to 24 V.
:::

The default Dynamixel settings are shown below. The example image shows the left gripper (ID 1).

<img :src="$withBase('/images/options/gripper/rby1_gripper_dynamixel_parameters.png')" alt="Dynamixel control table of the gripper: XM430-W210, ID 1, 2 Mbps, Protocol 2.0, current control" class="center white-bg" style="width:600px">

## Wiring

The gripper connects to the body's I/O port through the bypass port on the wrist. Wire it as shown below to use the U2D2 converter installed in the PDU: UPC DP to BP0, UPC DN to BP1.

<img :src="$withBase('/images/options/gripper/rby_gripper_io_connection.png')" alt="Gripper wiring from the wrist bypass port to the U2D2 in the PDU" class="center white-bg" style="width:600px">

The device name `/dev/rby1_gripper` comes from a udev rule on the UPC (see the udev steps in the [FAQ](../sdk/trobuleshooting/generated/faq.md)).

## Control from the SDK

With the default settings above, you can use the gripper code in the leader arm teleoperation example without changes:
<a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/35_leader_arm_teleop_with_monitor.py" target="_blank" rel="noopener noreferrer">examples/python/35_leader_arm_teleop_with_monitor.py</a> (class `Gripper`) and
<a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/35_leader_arm_teleop_with_monitor.cpp" target="_blank" rel="noopener noreferrer">examples/cpp/35_leader_arm_teleop_with_monitor.cpp</a>.

The example turns on the 12 V power, sets the tool flange output to 12 V, opens `/dev/rby1_gripper` at 2 Mbps, and finds the open and closed limits of both grippers (homing) before it moves them.

::: warning
Homing moves both grippers to their open and closed limits. Keep your fingers and objects out of the grippers when you start the example.
:::
