# Robot Main Program
##
<!-- (Robot PC System Overview) -->

::: info The diagram below provides an overview of the **Robot Main Program**, which is the core software system responsible for processing commands and controlling the robot's behavior.

:::

![inside-rpc](/images/software/robot_main_program/inside-rpc.png)

---
### Hardware

- **Hardware Management**: Manages all hardware components, including motor drivers, sensors, and power systems.

- **Robot State Construction**: Processes data from these components to construct the robot state.

- **Control Output**: Transmits control outputs from the controller to the hardware (motor drivers).

![inside-rpc-hardware](/images/software/robot_main_program/inside-rpc-hardware.png)

---
### Control Manager

::: info For detailed information on specific controllers, please refer to this link.

:::

- **Control Management**: Manages individual controllers and ensures only one control is active at a time.
- **Robot State Utilization**: Takes the robot state from the hardware to produce the appropriate control output.

![inside-rpc-controller](/images/software/robot_main_program/inside-rpc-controller.png)

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

::: info The following LED statuses refer to the LED strip located on the front of the robot. This strip visually indicates the robot's power, control, and system states, allowing users to easily monitor the current status of the robot.

:::

- **Power ON**: Solid white indicates full power, while blinking white indicates partial power.

![led_white](/images/software/robot_main_program/led_white.jpg)

- **Control Manager Enabled**:
   - **Idle**: Blue LED.

![led_blue](/images/software/robot_main_program/led_blue.jpg)

   - **Executing/Switching**: Green LED.

![led_green](/images/software/robot_main_program/led_green.jpg)

- **Fault States**:
   - **Minor Fault**: Blinking red.
   - **Major Fault**: Solid red.

![led_red](/images/software/robot_main_program/led_red.jpg)

---
### Service

![inside-rpc-service](/images/software/robot_main_program/inside-rpc-service.png)

- The **gRPC** server accepts requests from clients, processes them, and returns appropriate responses.

- For available services and RPC methods, refer to the corresponding proto file.
