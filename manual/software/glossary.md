# Glossary

Terms used across this manual, in alphabetical order.

| Term | Meaning |
| --- | --- |
| **Base** (`base`) | The root link of the robot model. Its frame has x forward, y left and z up. See [Units and Frames](units-and-frames.md#base-frame). |
| **Body** | The torso and both arms. A body command controls these joints (`model.body_idx`). |
| **Brake** | Holds a joint when its motor is off. Some joints have a release button; others are released only in software. See the [model pages](../sdk/models/index.md). |
| **CANCEL CONTROL** | Web UI button that cancels the running command (`cancel_control()`). The power stays on. |
| **Cartesian command** | A command that moves a link (for example `ee_right`) to a pose given in another link's frame (for example `base`). |
| **Command** | A request to move the robot, built with the SDK builders (`RobotCommandBuilder`). See [Command and Control Architecture](../sdk/controllers/generated/command_and_control_architecture.md). |
| **Command stream** | A command channel that stays open, so your program can update the target many times (`create_command_stream()`). |
| **Component** | A part of the robot that a component-based command addresses: mobility, body (torso, right arm, left arm) and head. |
| **Control Hold Time** | How long a command stays active after it reaches its target. See [Control Hold Time and Minimum Time](../sdk/controllers/generated/control_hold_time_and_minimum_time.md). |
| **Control Manager** | The part of the robot software that runs commands. States: Idle, Enabled, Minor Fault, Major Fault. See [Robot Main Program](robot_main_program.md). |
| **Control period** | 2 ms: the cycle of the robot software and of real-time control. |
| **E-Stop** (EMO) | The emergency stop button on the robot. Pressing it cuts the 48 V power to the actuators in hardware. See [E‑Stop Basics](../getting-started/estop-basics.md). |
| **`ee_right`, `ee_left`** | The end-effector links of the right and left arm. |
| **Finish code** | Why a command ended: `Ok`, `Canceled`, `Preempted`, ... With robot software up to 0.11.0, the SDK shows most codes shifted by one name (a preempted or refused command shows `Canceled`). See [Fault Diagnosis](../sdk/troubleshooting/fault-diagnosis.md#finish-codes). |
| **F/T sensor** | Force/torque sensor at the wrist. Whether Model M v1.3 has one is not confirmed; see [Hardware Versions](../sdk/models/hardware-versions.md#differences-between-versions). |
| **gRPC** | The protocol of the robot software API, on port 50051. The SDK uses it. See the [Protobuf API Reference](../sdk/protos/index.md). |
| **Gripper** | Optional two-finger gripper controlled from the UPC. See [Gripper](../options/gripper.md). |
| **Hardware version** | Build version of a model (v1.0 to v1.3). See [Hardware Versions](../sdk/models/hardware-versions.md). |
| **Hotspot** | The Wi‑Fi network that the RPC opens while the HOTSPOT button is pressed in (default SSID `RBY1`, RPC address `192.168.12.1`). |
| **Joint names** | Names such as `torso_1`, `right_arm_2`, `head_0`. See [Units and Frames](units-and-frames.md#joint-order). |
| **Leader arm** | A pair of small arms that an operator moves to teleoperate the robot. Older documents call it *master arm*. See [Leader Arm](../options/leader_arm.md). |
| **LeRobot** | Open-source robot learning framework. RB-Y1 support is in [rby1-lerobot](https://github.com/RainbowRobotics/rby1-lerobot). See [Teleoperation & Data Collection](../options/teleoperation.md). |
| **Minimum Time** | The shortest time a command takes to reach its target. |
| **Mobility** | The wheels of Model A and Model M. Model UB has none. |
| **Model A, M, UB** | The three robot models: differential base, mecanum base, upper body only. See [Robot Models](../sdk/models/index.md). |
| **Parameter** | A setting stored on the RPC, for example `default.velocity_limit_scaling`. See [Parameter Reference](../sdk/controllers/generated/parameter.md). |
| **Power rails** | The robot power outputs `5v`, `12v`, `24v` and `48v`. `power_on(".*")` turns on all of them. |
| **Priority** | An integer sent with a command (default 1). A higher priority takes over joints from a running command. See [Robot Main Program](robot_main_program.md#control-manager). |
| **Real-time control** | Control at 500 Hz over UDP, where your program sends joint targets and torques every 2 ms (`robot.control()`). |
| **Robot PC (RPC)** | The computer inside the robot that runs the robot software, the gRPC server and the Web UI. |
| **Robot software** (core) | The program on the RPC. Its version is shown as **RPC** in the Web UI Dashboard. |
| **RPC Updater** | The tool that installs a new robot software version on the RPC. See [RPC Updater](../rpc_management_tools/rpc_updater.md). |
| **SDK** | rby1-sdk, the C++ and Python library to control the robot (`rby1_sdk` in Python). |
| **SE2 velocity** | A planar velocity of the mobile base: `[vx, vy]` in m/s and a yaw rate in rad/s. |
| **Servo** | A joint motor that is on and holds or moves the joint. `servo_on()` turns servos on. |
| **Simulator** | The robot software running with a simulated robot (MuJoCo or Isaac Sim). See [Simulation](../simulators/index.md). |
| **Tool flange** | The interface at the end of each arm, with switchable 12 V / 24 V output. |
| **Unlimit** | Enables the Control Manager even when a joint is outside its range (the range check at enable is skipped). Use it only to bring a joint back into its range. |
| **URDF / MJCF** | Robot model files: URDF for kinematics and dynamics, MJCF for MuJoCo. They are in the `models` folder of rby1-sdk. |
| **User PC (UPC)** | The computer inside the robot for your own programs (Jetson AGX Orin). See [User PC (UPC)](upc.md). |
| **Web UI** | The browser interface on the RPC at port 5173. See [Web UI](web-ui.md). |
| **Zero pose** | All joint angles at 0: the robot stands straight. |

---

Verified against: the pages linked above; rby1-sdk v0.10.1 `include/rby1-sdk/model.h`, `include/rby1-sdk/robot.h`;
robot core `core/robots/rby1a/robot_hardware.cpp` (power rail names), `core/control/control_manager.h` (states).
