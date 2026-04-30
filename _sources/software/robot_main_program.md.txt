# Robot Main Program
##
<!-- (Robot PC System Overview) -->

```{note} The diagram below provides an overview of the **Robot Main Program**, which is the core software system responsible for processing commands and controlling the robot's behavior.
```

```{image} ../_static/images/software/robot_main_program/inside-rpc.png
   :alt: inside-rpc
   :align: center
   :width: 600px
   :class: white_bg
```

---
### Hardware

- **Hardware Management**: Manages all hardware components, including motor drivers, sensors, and power systems.

- **Robot State Construction**: Processes data from these components to construct the robot state.

- **Control Output**: Transmits control outputs from the controller to the hardware (motor drivers).

```{image} ../_static/images/software/robot_main_program/inside-rpc-hardware.png
   :alt: inside-rpc-hardware
   :align: center
   :width: 400px
   :class: white_bg
```

---
### Control Manager

```{note} For detailed information on specific controllers, please refer to this link.
```

- **Control Management**: Manages individual controllers and ensures only one control is active at a time.
- **Robot State Utilization**: Takes the robot state from the hardware to produce the appropriate control output.

```{image} ../_static/images/software/robot_main_program/inside-rpc-controller.png
   :alt: inside-rpc-controller
   :align: center
   :width: 400px
   :class: white_bg
```

<br>


### Control Manager States
- **Idle**: Default state, no control output is transmitted.
- **Enabled**: Actively transmits control outputs. If no control is active, the system defaults to a position lock. Only motors ready for movement are activated.
- **Minor Fault**: Represents a minor issue that requires attention but does not cause a shutdown.
- **Major Fault**: Indicates a critical issue leading to power shutdown.

<br>

### Control States
- **Idle**: No control process is occurring.
- **Executing**: A control process is currently running.
- **Switching**: A transition phase when a new control process overrides the active one due to priority.

<br>

### LED States (LED Strip State)

```{note} The following LED statuses refer to the LED strip located on the front of the robot. This strip visually indicates the robot's power, control, and system states, allowing users to easily monitor the current status of the robot.
```

- **Power ON**: Solid white indicates full power, while blinking white indicates partial power.

```{image} ../_static/images/software/robot_main_program/led_white.jpg
   :alt: led_white
   :align: center
   :width: 400px
   :class: white_bg
```

- **Control Manager Enabled**:
   - **Idle**: Blue LED.

```{image} ../_static/images/software/robot_main_program/led_blue.jpg
   :alt: led_blue
   :align: center
   :width: 400px
   :class: white_bg
```

   - **Executing/Switching**: Green LED.

```{image} ../_static/images/software/robot_main_program/led_green.jpg
   :alt: led_green
   :align: center
   :width: 400px
   :class: white_bg
```

- **Fault States**:
   - **Minor Fault**: Blinking red.
   - **Major Fault**: Solid red.

```{image} ../_static/images/software/robot_main_program/led_red.jpg
   :alt: led_red
   :align: center
   :width: 400px
   :class: white_bg
```


---
### Service
<br>

```{image} ../_static/images/software/robot_main_program/inside-rpc-service.png
   :alt: inside-rpc-service
   :align: center
   :width: 600px
   :class: white_bg
```

- The **gRPC** server accepts requests from clients, processes them, and returns appropriate responses.

- For available services and RPC methods, refer to the corresponding proto file.
