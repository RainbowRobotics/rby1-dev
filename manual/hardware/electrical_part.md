# Electrical Part

## Power System

<img :src="$withBase('/images/hardware/electronical_part/power-system1.png')" alt="power-system1" class="center white-bg" style="width:200px">

### Input Source

- The system operates using either a **battery** or an **external power source (SMPS)**.
- The **SMPS** (Switched-Mode Power Supply) requires a **back-EMF** protection device to safeguard against voltage spikes.

### Power Distribution

- Power cables run inside the lower body, so little wiring is visible.
- From there, power goes to each part of the body.
- The internal routing also protects the cables.

### Shutdown Methods

How the E-Stop works depends on whether the robot has a Safety Control Board (SCB). The SCB is installed only in KC-certified v1.2 robots. For the SCB version, see [Shutdown Methods (SCB Installed)](#shutdown-methods-scb-installed).

#### Robots without SCB

- **E-Stop button (EMO)**
   - A physical emergency switch on the backpack that cuts off power to the modules.
   - Keep it within reach while the robot operates.

- **Wireless E-Stop remote**
   - Works like the E-Stop button.

::: warning Important
Both the E-Stop button (EMO) and the wireless E-Stop remote cut off the power from the PDU to the terminal board. This is a hardware-level shutdown.
:::

::: warning Caution
You can also disconnect the input power behind the front cover (see [Disconnect the Battery for Long-Term Storage](../precautions/power_and_battery.md#disconnect-the-battery-for-long-term-storage)).
Use this for packing or long-term storage.
It cuts all power at once. Shut down in the normal order first (see [Shutdown Order](../precautions/power_and_battery.md#shutdown-order)).
:::

<img :src="$withBase('/images/hardware/electronical_part/power_system2.png')" alt="power_system2" class="center rounded-img" style="width:600px">

### Power System (SCB Installed)

::: warning Important
SCB (Safety Control Board) is installed only in KC-certified version 1.2 robots.
:::

The robot power system is structured as follows:

- **Battery → PDU → SCB → Terminal Board → Each Module**

The SCB is responsible for safety-related power control, including emergency stop handling.

<img :src="$withBase('/images/hardware/electronical_part/power_system3.png')" alt="emo_shutdown" class="center rounded-img" style="width:600px">

### Shutdown Methods (SCB Installed)

- **E-Stop button (EMO)**
   - A physical emergency switch on the backpack that cuts off power to the modules.
   - Keep it within reach while the robot operates.
   - When the E-Stop button is pressed:
      - The 48V power from SCB to the Terminal Board is cut off
      - As a result, all downstream modules lose power immediately

<img :src="$withBase('/images/hardware/electronical_part/emo_shutdown.png')" alt="emo_shutdown" class="center rounded-img" style="width:600px">

- **Wireless E-Stop remote**
   - A wireless emergency stop that works like the E-Stop button.
   - Use it when you are away from the robot.
   - When the button on the remote is pressed:
      - The receiver receives and validates the signal
      - The PDU cuts off the 48V power supplied to the SCB
      - As a result, all downstream modules lose power immediately

<img :src="$withBase('/images/hardware/electronical_part/remote_control_shutdown.png')" alt="remote_control_shutdown" class="center rounded-img" style="width:600px">

---
### Backpack

The backpack holds the robot's control unit and its external connections.

- **External power**: 24 V, 12 V and 5 V outputs, 8 A each. Bypass ports connect the tool flange to the control unit.
- **User PC (UPC) ports**: 2 USB, 2 Ethernet and 1 HDMI. The two Ethernet ports have different speeds: the UPC port supports **10 Gbps** and the other port **1 Gbps**.
- **Controls**: the antennas, the power buttons and the E-Stop button (EMO).

#### External Power Specifications

| Voltage |	Current Capacity |
| ------- | ---------------- |
| 24V     |	8A               |
| 12V     |	8A               |
| 5V      |	8A               |

<img :src="$withBase('/images/hardware/electronical_part/backpack.png')" alt="backpack" class="center white-bg" style="width:600px">

The robot's body is designed to distribute power and communication to each critical module for smooth operation.

**Key Components Installed in the Body:**

- **Robot PC (RPC)**: UP Xtreme i12. It runs the robot software and controls the joints.
- **User PC (UPC)**: Jetson AGX Orin. It runs your programs.
- **E-Stop button (EMO)**: cuts the robot power at once.
- **PDU** (Power Distribution Unit): Manages power distribution.
- **OLED**: Displays robot status.
- **LED** Strip: Visual robot status indicator.
- **Pan-Tilt Mount**: For mounting vision devices.

---
### User PC (UPC) and Robot PC (RPC)

- The **UPC** is a **Jetson AGX Orin Module 64G** on a **carrier board (AverMedia D315)**. It runs your programs.

- The **RPC** is an **UP Xtreme i12** with a **12th Gen Intel® Core™** processor. It runs the robot software that controls the joints.

<img :src="$withBase('/images/hardware/electronical_part/rpc-upc.png')" alt="rpc-upc" class="center white-bg" style="width:600px">

#### Robot PC (RPC)
The RPC (UP Xtreme i12) gets its power from a DC-DC converter in the PDU. Its power switch is on the top of the robot. A 4-channel M.2 CAN module in the RPC connects it to the joints (see [Communication System Overview [CAN]](#communication-system-overview-can)).

#### User PC (UPC)
The UPC (Jetson AGX Orin) can be replaced with another PC if necessary. It also gets its power from a DC-DC converter in the PDU. Its power switch is on the top of the body. The UPC controls the gripper; connect the communication module that matches your gripper (see [Gripper](../options/gripper.md)).

---
### PDU (Power Distribution Unit)

The PDU has around 20 connectors, and incorrect wiring can lead to operational issues. Special caution is necessary when handling the PDU, particularly around its DC-DC converters, as they can become very hot during operation.

::: warning Important
Be cautious not to touch the DC-DC converters while the power is on, as they can become hot.
:::

<img :src="$withBase('/images/hardware/electronical_part/pdu.png')" alt="pdu" class="center rounded-img" style="width:400px">

---
### Terminal Board and Fuse Information

The Terminal Board inside the robot contains four fuses:

- Fuse types: 5x20mm
- Ratings: 15A fuses

Replace a fuse only with one of the same type and rating.

<img :src="$withBase('/images/hardware/electronical_part/terminal-fuse.png')" alt="terminal-fuse" class="center white-bg" style="width:400px">

<img :src="$withBase('/images/hardware/electronical_part/terminal_board.png')" alt="terminal_board" class="center white-bg" style="width:400px">

---
### Cable Connection Board

This board manages the power and signal connections between the robot's modules.

<img :src="$withBase('/images/hardware/electronical_part/cable-connection-board.png')" alt="cable-connection-board" class="center white-bg" style="width:600px">

---
### Tool Flange Connection

The tool flange has two connectors. Connector A is for users: it provides a 6-line bypass to the UPC. Connector B connects to the tool flange board, which the RPC controls. The tool flange also features an I/O interface, supporting direct connections to the robot’s force/torque (F/T) sensor or gripper. Additionally, the Direct Teaching Button allows users to manually guide the robot’s movements.

<img :src="$withBase('/images/hardware/electronical_part/connection-info.png')" alt="connection-info" class="center white-bg" style="width:600px">

---
### Communication System Overview [CAN]

::: info Note
Users cannot access these CAN channels. Only the robot PC (RPC) uses them.
:::

The RPC has **4 CAN channels**:

| Channel | Devices |
| --- | --- |
| `can0` (right arm) | `right_arm_0` – `right_arm_6`, right tool flange, right F/T sensor |
| `can1` (left arm) | `left_arm_0` – `left_arm_6`, left tool flange, left F/T sensor |
| `can2` (torso) | `torso_0` – `torso_5` (Model UB: its torso joints) |
| `can3` (wheel) | wheels, PDU, SCB, and on Model A/M v1.2 and v1.3 robots `head_0` and `head_1` |

On v1.0 and v1.1 robots, the head uses Dynamixel actuators on a serial bus, not CAN. Model UB always uses Dynamixel actuators for the head, in every version.
Model M v1.3 has no F/T sensors.
The [CAN Checker](../rpc_management_tools/can_checker.md) tool uses the same channel names.

Data:

- The motor drivers send their status and the joint encoder values over CAN.

Command flow:

- Your program on the UPC sends commands to the RPC over **Ethernet**.
- The RPC processes the commands and drives the joints over CAN.

<img :src="$withBase('/images/hardware/electronical_part/can.png')" alt="can" class="center rounded-img" style="width:600px">

---
### Communication System Overview [LAN & BYPASS]

<img :src="$withBase('/images/hardware/electronical_part/communication_system.png')" alt="communication_system" class="center rounded-img" style="width:200px">

#### Access through the UPC
- Your programs on the UPC communicate with the RPC over LAN.
- The UPC sends the commands that control RB-Y1 to the RPC.

#### RPC to mobile base
- The RPC is connected to the mobile base over LAN.
- It receives sensor data such as LiDAR, for example for collision avoidance.

#### Bypass Connection:
- A direct hardware link exists between the body and the tool flange (TF).
- This connection allows communication for devices like grippers.

#### Peripheral Devices:
- The user can connect additional devices, such as USB-to-serial converters, for extended functionality.
