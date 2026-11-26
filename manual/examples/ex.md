# Examples

The SDK repository has numbered example programs in Python and C++. This page lists the examples of **rby1-sdk v0.10.1**, the SDK version this manual documents. The links open the files at the `v0.10.1` tag, so they match the installed `rby1-sdk==0.10.1` wheel.

- Python: [`examples/python`](https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/examples/python)
- C++: [`examples/cpp`](https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/examples/cpp)

::: danger Examples that move the robot
Many examples power on the robot, turn the servos on, enable the Control Manager and move the arms, the torso or the mobile base.
Before you run an example marked **Yes** in the table below:

- Read [Precautions](../precautions/general.md) and [E-Stop Basics](../getting-started/estop-basics.md), and keep the E-Stop within reach.
- Clear the space around the robot. Examples marked **CAUTION** in their file header make large or fast motions, or drive the mobile base.
- Read the header of the file first. It states the motion, the arguments and the limits of the example.
- Try the example in the [simulator](../simulators/index.md) first when it supports it.
:::

## Run an example

### Python

Install the SDK and get the examples of the same version:

```bash
pip install rby1-sdk==0.10.1
git clone --branch v0.10.1 https://github.com/RainbowRobotics/rby1-sdk.git
cd rby1-sdk/examples/python
```

Run the examples from `examples/python`. Most of them import `00_helper.py` from the same folder.
Every example prints its arguments with `--help`. A typical call is:

```bash
python 03_robot_state.py --address 192.168.30.1:50051 --model a --power '.*'
```

| Argument | Meaning |
| --- | --- |
| `--address` | `<robot IP>:50051`. Use the robot PC (RPC) address `192.168.30.1` from the user PC (UPC), the hotspot address `192.168.12.1` from a laptop on the robot hotspot, or `localhost:50051` for a simulator on the same PC. |
| `--model` | Robot model: `a`, `m` or `ub`. |
| `--power` | Regular expression of the power devices to turn on, for example `'.*'` for all. |
| `--servo` | Regular expression of the joints to turn the servos on, for example `'.*'` for all. |

### C++

Build the SDK from source with `BUILD_EXAMPLES=ON` as described in the SDK [README](https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1#c):

```bash
cmake --preset conan-release -D BUILD_EXAMPLES=ON
cmake --build --preset conan-release
```

Each example becomes an executable named `example_<file name>` in the `examples/cpp` folder of the build directory, for example `example_03_robot_state`.
The examples in `examples/cpp/dynamics` become `example_dynamics_<name>`; they only compute dynamics and do not connect to a robot.

```bash
./example_03_robot_state --address 192.168.30.1:50051 --model a --power ".*"
```

## Example list

- **Moves the robot**: **Yes** means the example sends motion commands. **CAUTION** means the file header has a CAUTION block.
- **Simulator**: **No** means the file header says the example does not run in simulation. **Yes** means the header has no such note; not every example has been tested in each simulator.

::: info Python and C++ numbers differ in two places
The numbers match between Python and C++ except for these files: number 04 is the robot state stream in Python but the parameter example in C++, number 05 is the reverse, and 38 and 39 have `rpc_` in the Python file names only.
:::

| No. | Python | C++ | What it does | Moves the robot | Simulator |
| --- | --- | --- | --- | --- | --- |
| 00 | [00_helper.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/00_helper.py) | [00_helper.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/00_helper.cpp) | Helper functions used by other examples: power on, servo on, reset a Control Manager fault, enable the Control Manager, and `movej` for joint moves. Not run directly. | — | — |
| 01 | [01_hello_rby1.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/01_hello_rby1.py) | [01_hello_rby1.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/01_hello_rby1.cpp) | Connects to the robot and prints the robot information. | No | Yes |
| 02 | [02_robot_model_setting.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/02_robot_model_setting.py) | [02_robot_model_setting.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/02_robot_model_setting.cpp) | Downloads the robot model (URDF), saves a custom model to the robot and selects it. **Changes a robot setting**; the new model is used after a reboot. | No | Yes |
| 03 | [03_robot_state.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/03_robot_state.py) | [03_robot_state.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/03_robot_state.cpp) | Turns on the selected power devices and prints the current robot state once. | No | Yes |
| 04 | [04_robot_state_stream.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/04_robot_state_stream.py) | [04_parameter.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/04_parameter.cpp) | Python: receives the robot state as a stream. C++: reads and sets robot parameters (see 05). | No | Yes |
| 05 | [05_parameter.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/05_parameter.py) | [05_robot_state_stream.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/05_robot_state_stream.cpp) | Python: lists, resets and sets robot parameters. **Changes a robot setting**: it leaves `joint_position_command.cutoff_frequency` at `1`, so note the value it prints first and set it back. C++: receives the robot state as a stream. | No | Yes |
| 06 | [06_state_tool_flange.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/06_state_tool_flange.py) | [06_state_tool_flange.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/06_state_tool_flange.cpp) | Turns on the 48 V tool flange supply if needed and prints the left and right tool flange states. | No | Yes |
| 07 | [07_power.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/07_power.py) | [07_power.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/07_power.cpp) | Turns on the power devices that match `--device`. | No | Yes |
| 08 | [08_check_firmware_version.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/08_check_firmware_version.py) | [08_check_firmware_version.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/08_check_firmware_version.cpp) | Prints the motor information: name, brake, product name and firmware version. | No | Yes |
| 09 | [09_get_pid_gain.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/09_get_pid_gain.py) | [09_get_pid_gain.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/09_get_pid_gain.cpp) | Reads the motor PID gains. | No | No |
| 10 | [10_set_pid_gain.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/10_set_pid_gain.py) | [10_set_pid_gain.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/10_set_pid_gain.cpp) | Changes the PID gains of selected joints and then restores them. Disable the Control Manager first. CAUTION: the factory gains are tuned; wrong gains can cause accidents. | No | No |
| 11 | [11_factory_default_pid_gain.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/11_factory_default_pid_gain.py) | [11_factory_default_pid_gain.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/11_factory_default_pid_gain.cpp) | Sets the PID gains to the factory default values. The header recommends not to use it. | No | No |
| 12 | [12_led.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/12_led.py) | [12_led.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/12_led.cpp) | Controls the robot LED. | No | Yes |
| 13 | [13_set_system_time.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/13_set_system_time.py) | [13_set_system_time.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/13_set_system_time.cpp) | Reads and sets the robot system time and time zone. | No | No |
| 14 | [14_wifi.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/14_wifi.py) | [14_wifi.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/14_wifi.cpp) | Sets up the Wi-Fi connection of the robot PC (RPC). **Changes the network**; the change can take 1–2 minutes. Check the new IP address on the OLED of the backpack. | No | No |
| 15 | [15_log.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/15_log.py) | [15_log.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/15_log.cpp) | Prints the most recent robot log entries. | No | Yes |
| 16 | [16_log_stream.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/16_log_stream.py) | [16_log_stream.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/16_log_stream.cpp) | Receives robot log entries as a stream. | No | Yes |
| 17 | [17_fault_log.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/17_fault_log.py) | [17_fault_log.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/17_fault_log.cpp) | Lists the fault log files and downloads the first one as `fault.csv`. See [Fault Diagnosis](../sdk/trobuleshooting/fault-diagnosis.md). | No | Yes |
| 18 | [18_dynamics_modeling.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/18_dynamics_modeling.py) | [18_dynamics_modeling.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/18_dynamics_modeling.cpp) | Builds a two-link dynamics model and computes forward kinematics. No robot needed. | No | — |
| 19 | [19_dynamics_robot.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/19_dynamics_robot.py) | [19_dynamics_robot.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/19_dynamics_robot.cpp) | Gets the dynamics model from the robot and computes forward kinematics and inverse dynamics. | No | Yes |
| 20 | [20_leader_arm_state_check.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/20_leader_arm_state_check.py) | [20_leader_arm_state_check.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/20_leader_arm_state_check.cpp) | Runs on the user PC (UPC). Turns on the 12 V supply and reads the leader arm joints, torque and current. | Leader arm only | No |
| 21 | [21_record.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/21_record.py) | [21_record.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/21_record.cpp) | Turns the power on and records the joint positions until you stop it, then saves them (`recorded.npz` in Python). | No | Yes |
| 22 | [22_replay.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/22_replay.py) | [22_replay.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/22_replay.cpp) | Replays the positions recorded by 21 on the torso and both arms. | Yes | Yes |
| 23 | [23_zero_pose.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/23_zero_pose.py) | [23_zero_pose.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/23_zero_pose.cpp) | Moves the robot to the zero pose. | Yes | Yes |
| 24 | [24_demo_motion.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/24_demo_motion.py) | [24_demo_motion.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp) | Runs joint position, Cartesian, impedance, optimal control and mixed command demos in sequence. | Yes, CAUTION | Yes |
| 25 | [25_wiggle_motion.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/25_wiggle_motion.py) | [25_wiggle_motion.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/25_wiggle_motion.cpp) | Moves to the ready pose and moves the torso joints in a continuous circle with joint impedance control until Ctrl+C. | Yes, CAUTION | Yes |
| 26 | [26_cancel_control.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/26_cancel_control.py) | [26_cancel_control.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/26_cancel_control.cpp) | Moves to the zero pose, starts a second motion and cancels it after 2 s. | Yes | Yes |
| 27 | [27_collisions.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/27_collisions.py) | [27_collisions.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/27_collisions.cpp) | Monitors the self-collision distance during a motion and sends a stop command when the links get too close. | Yes | Yes |
| 28 | [28_cartesian_impedance_control.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/28_cartesian_impedance_control.py) | [28_cartesian_impedance_control.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/28_cartesian_impedance_control.cpp) | Joint move, Cartesian command, then Cartesian impedance control of the right arm. | Yes | Yes |
| 29 | [29_joint_impedance_control.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/29_joint_impedance_control.py) | [29_joint_impedance_control.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/29_joint_impedance_control.cpp) | Joint impedance control of both arms toward the zero position. | Yes | Yes |
| 30 | [30_joint_group_command.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/30_joint_group_command.py) | [30_joint_group_command.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/30_joint_group_command.cpp) | Joint group position command. Available on the torso only. | Yes | No |
| 31 | [31_multi_controls.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/31_multi_controls.py) | [31_multi_controls.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/31_multi_controls.cpp) | Sends overlapping body and arm commands with different priorities and prints each finish code. | Yes | Yes |
| 32 | [32_command_stream.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/32_command_stream.py) | [32_command_stream.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/32_command_stream.cpp) | Streams body joint position commands through a command stream. | Yes, CAUTION | Yes |
| 33 | [33_cartesian_command_stream.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/33_cartesian_command_stream.py) | [33_cartesian_command_stream.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/33_cartesian_command_stream.cpp) | Streams right arm Cartesian targets through a command stream. | Yes, CAUTION | Yes |
| 34 | [34_real_time_control.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/34_real_time_control.py) | [34_real_time_control.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp) | Real-time control with your own controller instead of command builders. Moves to a target pose and waits until Ctrl+C. | Yes | Yes |
| 35 | [35_leader_arm_teleop_with_monitor.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/35_leader_arm_teleop_with_monitor.py) | [35_leader_arm_teleop_with_monitor.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/35_leader_arm_teleop_with_monitor.cpp) | Runs on the user PC (UPC). Teleoperation: the robot arms and grippers follow the leader arm and its triggers. | Yes | No |
| 36 | [36_brake_test.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/36_brake_test.py) | [36_brake_test.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/36_brake_test.cpp) | Releases the brake of one joint (`--joint`), waits briefly and engages it again. The joint can move under gravity. Do not use it on torso joints or with `".*"`. | Yes (brake release), CAUTION | Yes |
| 37 | [37_mobile_test.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/37_mobile_test.py) | [37_mobile_test.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/37_mobile_test.cpp) | Moves to a ready pose and drives the mobile base with velocity commands. On Model A the Y component of SE(2) commands is ignored. | Yes (mobile base), CAUTION | Yes |
| 38 | [38_rpc_serial_device.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/38_rpc_serial_device.py) | [38_serial_device.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/38_serial_device.cpp) | Lists the serial devices on the robot PC (RPC). | No | No |
| 39 | [39_rpc_serial_communication.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/39_rpc_serial_communication.py) | [39_serial_communication.cpp](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/39_serial_communication.cpp) | Opens a serial device on the robot PC (RPC) and reads from it. CAUTION: devices that send data as soon as they connect can overload the RPC. | No | No |

::: tip Newer examples
The `main` and `dev` branches of rby1-sdk can contain newer examples that are not in v0.10.1. They may need a newer SDK and robot software than this manual describes.
:::

Verified against: rby1-sdk v0.10.1 `examples/python/*.py` and `examples/cpp/*.cpp` file headers, `examples/cpp/CMakeLists.txt`, `examples/cpp/dynamics/CMakeLists.txt`, `CMakeLists.txt` (`BUILD_EXAMPLES`), `README.md` (C++ build).
