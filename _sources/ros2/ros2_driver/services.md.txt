# Services

| Service | Type | Description |
|---------|------|-------------|
| `robot_power` | `rby1_msgs/StateOnOff` | Power ON/OFF. `parameters`: `"all"`, `"48v"`, `"5v"`, etc. |
| `robot_servo` | `rby1_msgs/StateOnOff` | Servo ON/OFF. `parameters`: `"all"`, joint/part names |
| `tool_flange_power` | `rby1_msgs/StateOnOff` | Set tool flange voltage. `parameters`: `"12v"`, `"24v"`, `"48v"` (ON) or `""` (OFF) |
| `gravity_compensation` | `rby1_msgs/GravityCompensation` | Enable/disable gravity compensation per body part |
| `cancel_control` | `std_srvs/Trigger` | Cancel all active motion commands immediately |
| `get_cartesian_pose` | `rby1_msgs/GetCartesianPose` | Query Cartesian transform between two links |
| `control_manager_command` | `rby1_msgs/ControlManagerCommand` | Send `CMD_ENABLE` / `CMD_DISABLE` / `CMD_RESET` to the Control Manager |
| `stream_control` | `rby1_msgs/StateOnOff` | Enable/disable persistent streaming mode with 10-minute hold times (`state=true` to enable, `state=false` to disable) |
| `hardware_control` | `rby1_msgs/StateOnOff` | Claim (`state=true`) or release (`state=false`) hardware control rights for direct controller managers |
| `set_trajectory_impedance` | `rby1_msgs/SetTrajectoryImpedance` | Enable or disable impedance control mode for the trajectory execution action server (`follow_joint_trajectory`) |

## `ControlManagerCommand` constants

| Constant | Value | Description |
|----------|-------|-------------|
| `CMD_NONE` | `0` | No operation |
| `CMD_ENABLE` | `1` | Enable the Control Manager (start position hold) |
| `CMD_DISABLE` | `2` | Disable the Control Manager (transition to IDLE) |
| `CMD_RESET` | `3` | Reset MAJOR/MINOR fault and return to IDLE |
| `CMD_UNLIMIT` | `4` | Enable the Control Manager, ignoring its range of motion limits. |


> [!IMPORTANT]
> - ⚠️ **Calling `cancel_control` while using stream-based control will also close the stream.** After `cancel_control`, you must re-open the stream before sending further `cmd_vel` commands. To cancel only the current motion without closing the stream, use the action cancel (see Example 13).
> - The current stream open/close state is reflected in the `robot_state` topic as `robot_stream_state` (`bool`).

> [!WARNING]
> **Behavior of `robot_joint` and `robot_cartesian` Actions under Active Stream:**
> When persistent streaming is active (`stream_control` is `true`), the single joint (`robot_joint`) and Cartesian (`robot_cartesian`) commands are also routed through the command stream (`stream_handler_`).
> - In this mode, these actions will return a success (`succeed`) status **immediately** after sending the command, without waiting for the robot to reach the target position or providing intermediate feedback.
> - Therefore, target completion checking must be done independently by monitoring the joint state topics.
>
> **Joint/Cartesian Action Behavior Characteristics When Persistence Stream is Enabled:**
> - When `robot_joint` and `robot_cartesian` action commands are sent while the persistence stream is turned on, those commands are transmitted through the stream channel.
> - In this case, it **returns immediately** without waiting for the robot to reach the target position; therefore, the client side must monitor whether the target has been reached via a separate joint status topic.
>
> ⚙️ = controlled by the corresponding flag in `driver_parameters.yaml`

> [!WARNING]
> **Impedance configuration during active stream control:**
> The robot command stream fixes the control mode configuration (e.g. position control vs impedance control) of the command instances when the stream is first opened.
> - Therefore, you cannot configure trajectory impedance while persistent stream control is active (`stream_control` is `true`).
> - The `/set_trajectory_impedance` service will **fail** and return `success: false` if called under an active stream.
> - To apply trajectory impedance changes, you must first deactivate the stream (call `/stream_control` with `state: false`), configure the impedance via `/set_trajectory_impedance`, and then reactivate the stream (call `/stream_control` with `state: true`).

