# Examples

Each example can be run in a **separate terminal** while the driver is active:
```bash
source install/setup.bash
ros2 run rby1_examples <example_name>
```

| Example | Command | Description |
|---------|---------|-------------|
| `01_power_control` | `ros2 run rby1_examples 01_power_control` | Full power lifecycle: Power ON/OFF, Servo ON/OFF |
| `02_robot_status_monitor` | `ros2 run rby1_examples 02_robot_status_monitor` | Continuously prints state monitor (Motor state, brakes, battery, etc) |
| `03_tool_flange_monitoring` | `ros2 run rby1_examples 03_tool_flange_monitoring` | Continuously prints tool flange data |
| `04_joint_state_monitoring` | `ros2 run rby1_examples 04_joint_state_monitoring` | Prints per-component joint positions in real time |
| `05_gravity_compensation` | `ros2 run rby1_examples 05_gravity_compensation` | Enables/Disable gravity compensation mode |
| `06_zero_pose` | `ros2 run rby1_examples 06_zero_pose` | Moves all joints to 0 rad simultaneously |
| `07_joint_command` | `ros2 run rby1_examples 07_joint_command` | Sends Ready Pose with joint_position(right), joint_impedance(left) |
| `08_cartesian_command` | `ros2 run rby1_examples 08_cartesian_command` | Sends Ready Pose and moves the arms to a target Cartesian pose with cartesian_position(right), cartesian_impedance(left)|
| `09_multi_controls` | `ros2 run rby1_examples 09_multi_controls` | Simultaneous joint + Cartesian control per body part |
| `10_trajectory_joint_command` | `ros2 run rby1_examples 10_trajectory_joint_command` | Streams a pre-computed trajectory via standard FollowJointTrajectory action |
| `11_cancel_control` | `ros2 run rby1_examples 11_cancel_control` | Demonstrates action cancel and `cancel_control` service |
| `12_mobile_base_control` | `ros2 run rby1_examples 12_mobile_base_control` | Drives the mobile base via `cmd_vel`|
| `13_stream_command` | `ros2 run rby1_examples 13_stream_command` | Alternates Zero/Ready poses using regular joint commands over persistent stream with varying wait intervals |
| `14_collision_safety_control` | `ros2 run rby1_examples 14_collision_safety_control` | use collision value in robot.state, Demonstrates that when collision happens, robot automatically moves retreat to initial safe pose.  |

---

> [!IMPORTANT]
> **Two ways to stop control commands (see Example : 11_cancel_control):**
> 1. **Action cancel** — Cancels only the current action goal. The stream remains open, so subsequent commands can continue immediately.
> 2. **`cancel_control` service** — Immediately stops all control commands **and forcibly closes the stream** for safety.
>
> ⚠️ **If you are using stream-based control (e.g., `cmd_vel`, Example 13), calling `cancel_control` will also shut down the stream.**  
> You will need to re-open the stream (`/stream_control state: true`) before sending further commands.  
> If you only want to pause or cancel a specific motion while keeping the stream alive, use the action cancel instead (see Example 13).
>
> If an issue arises, please check the [Troubleshooting & Known Issues](troubleshooting_and_known_issues.md) section to see if there is any relevant information.

> [!NOTE]
> **Simulator Limitation**: Battery voltage, FT sensor, and IMU data read as `0.0` in simulation (no physical hardware).
> **Tool flange topics**: Requires `publish_tool_flange_state: true` in `driver_parameters.yaml`.

