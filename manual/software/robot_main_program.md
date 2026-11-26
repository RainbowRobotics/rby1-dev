# Robot Main Program

<!-- (Robot PC System Overview) -->

::: info Note
The diagram below provides an overview of the **Robot Main Program**, which is the core software system on the robot PC (RPC) responsible for processing commands and controlling the robot's behavior.
:::

<img :src="$withBase('/images/software/robot_main_program/inside-rpc.png')" alt="inside-rpc" class="center white-bg" style="width:600px">

---
### Hardware

- **Hardware Management**: Manages all hardware components, including motor drivers, sensors, and power systems.

- **Robot State Construction**: Processes data from these components to construct the robot state.

- **Control Output**: Transmits control outputs from the controller to the hardware (motor drivers).

<img :src="$withBase('/images/software/robot_main_program/inside-rpc-hardware.png')" alt="inside-rpc-hardware" class="center white-bg" style="width:400px">

---
### Control Manager

::: info Note
For the controllers and the commands that use them, see [Controllers](../sdk/controllers/index.md).
:::

- **Control Management**: Runs the commands (controls) you send. Several commands run at the same time when they use different joints,
  for example one command for the right arm and one for the head.
- **Priority**: Every command has a priority (an integer; default `1`, set with `send_command(builder, priority)` or `create_command_stream(priority)`).
  When a new command uses a joint that a running command already uses:
  - if the new priority is **higher**, the new command takes over and the running command ends;
  - if the new priority is **the same or lower**, the new command is refused and ends.

  In both cases the SDK shows the finish code `Canceled` (robot software up to 0.11.0), not `Preempted`.
  See [Command finish codes](../sdk/troubleshooting/fault-diagnosis.md#finish-codes).
- **Robot State Utilization**: Takes the robot state from the hardware to produce the appropriate control output.

<img :src="$withBase('/images/software/robot_main_program/inside-rpc-controller.png')" alt="inside-rpc-controller" class="center white-bg" style="width:400px">

### Control Manager States

| State | How it is entered | Running commands | How to leave it |
| --- | --- | --- | --- |
| **Idle** | After boot, after `disable_control_manager()` or after a fault reset | None. No control output is transmitted. | `enable_control_manager()` |
| **Enabled** | `enable_control_manager()` succeeded | Commands run. If no command runs, the joints hold their position (position lock). Only joints whose servos are on are controlled. | `disable_control_manager()` (refused while a command runs; cancel it first with `cancel_control()`) |
| **Minor Fault** | A command or the hardware readiness failed | All commands are canceled and each joint target is reset to its current position. The power stays on. | `reset_fault_control_manager()` → `Idle`, then `enable_control_manager()` |
| **Major Fault** | A motor, power or state error | All commands are canceled and the robot software turns the power off. | Wait until the fault reaction ends, `reset_fault_control_manager()`, power and servos on, then `enable_control_manager()` |

The causes of each fault, the log messages and the full recovery steps are in [Fault Diagnosis](../sdk/troubleshooting/fault-diagnosis.md).

::: warning
Enabling the Control Manager makes the motors hold the joints. Keep the E-Stop within reach when you enable it or recover from a fault.
:::

### Control States
- **Idle**: No control process is occurring.
- **Executing**: A control process is currently running.
- **Switching**: A transition phase when a new control process overrides the active one due to priority.

### LED States (LED Strip State)

::: info Note
The following LED statuses refer to the LED strip located on the front of the robot. This strip visually indicates the robot's power, control, and system states, allowing users to easily monitor the current status of the robot.
:::

- **Power ON**: Solid white indicates full power, while blinking white indicates partial power.

<img :src="$withBase('/images/software/robot_main_program/led_white.jpg')" alt="led_white" class="center white-bg" style="width:400px">

- **Control Manager Enabled**:
   - **Idle**: Blue LED.

<img :src="$withBase('/images/software/robot_main_program/led_blue.jpg')" alt="led_blue" class="center white-bg" style="width:400px">

   - **Executing/Switching**: Green LED.

<img :src="$withBase('/images/software/robot_main_program/led_green.jpg')" alt="led_green" class="center white-bg" style="width:400px">

- **Fault States**:
   - **Minor Fault**: Blinking red.
   - **Major Fault**: Solid red.

<img :src="$withBase('/images/software/robot_main_program/led_red.jpg')" alt="led_red" class="center white-bg" style="width:400px">

---
### Service

<img :src="$withBase('/images/software/robot_main_program/inside-rpc-service.png')" alt="inside-rpc-service" class="center white-bg" style="width:600px">

- The **gRPC** server (port 50051) accepts requests from clients, processes them, and returns appropriate responses.

- For available services and RPC methods, see the [Protobuf API Reference](../sdk/protos/index.md), for example the
  [RobotCommandService](../sdk/protos/generated/robot_command_service/robotcommandservice.md) and the
  [ControlManagerService](../sdk/protos/generated/control_manager_service/controlmanagerservice.md).

---

Verified against: robot core `core/control/control_manager.h` (states and their effect), `core/control/control_manager.cpp`
(`SetControl`: joint-mask overlap and priority check, `Enable`, `Disable`, `ResetFault`); rby1-sdk v0.10.1 `include/rby1-sdk/robot.h`
(`SendCommand(..., int priority = 1)`, `CreateCommandStream(int priority = 1)`, `EnableControlManager`, `ResetFaultControlManager`, `CancelControl`).
