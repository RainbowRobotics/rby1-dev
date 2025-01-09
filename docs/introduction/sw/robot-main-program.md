---
title: Robot Main Program
outline: deep
---

# Robot Main Program (Robot PC System Overview)

> :information_source: **Note**: The diagram below provides an overview of the **Robot Main Program**, which is the core software system responsible for processing commands and controlling the robot's behavior.

<figure style="text-align: center">
    <img src="/images/inside-rpc.png" alt="Robot Main Program Overview" style="width:100%;margin:auto;" />
</figure>

## Hardware
- **Hardware Management**: Manages all hardware components, including motor drivers, sensors, and power systems.
- **Robot State Construction**: Processes data from these components to construct the **robot state**.
- **Control Output**: Transmits control outputs from the controller to the hardware (motor drivers).

<figure style="text-align: center">
    <img src="/images/inside-rpc-hardware.png" alt="Hardware" style="width:70%;margin:auto;" />
</figure>

## Control Manager
> :link: **Note**: For detailed information on specific controllers, please refer to [this link](https://rainbowrobotics.github.io/rby1-dev/docs/development/rby1-sdk/controllers.html).

- **Control Management**: Manages individual controllers and ensures only one control is active at a time.
- **Robot State Utilization**: Takes the robot state from the hardware to produce the appropriate control output.

<figure style="text-align: center">
    <img src="/images/inside-rpc-controller.png" alt="Controller" style="width:70%;margin:auto;" />
</figure>

### Control Manager States
- **Idle**: Default state, no control output is transmitted.
- **Enabled**: Actively transmits control outputs. If no control is active, the system defaults to a position lock. Only motors ready for movement are activated.
- **Minor Fault**: Represents a minor issue that requires attention but does not cause a shutdown.
- **Major Fault**: Indicates a critical issue leading to power shutdown.

### Control States
- **Idle**: No control process is occurring.
- **Executing**: A control process is currently running.
- **Switching**: A transition phase when a new control process overrides the active one due to priority.

### LED States (LED Strip State)
> :bulb: **Note**: The following LED statuses refer to the LED strip located on the front of the robot. This strip visually indicates the robot's power, control, and system states, allowing users to easily monitor the current status of the robot.

- **Power ON**: Solid white indicates full power; blinking white indicates partial power.
- **Control Manager Enabled**:
  - **Idle**: Blue LED.
  - **Executing/Switching**: Green LED.
- **Fault States**:
  - **Minor Fault**: Blinking red.
  - **Major Fault**: Solid red.

## Service
<figure style="text-align: center">
    <img src="/images/inside-rpc-service.png" alt="Service" style="width:100%;margin:auto;" />
</figure>

- The **gRPC server** accepts requests from clients, processes them, and returns appropriate responses.
- For available services and RPC methods, refer to the corresponding proto file.
