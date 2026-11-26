# Services

All service names are relative to the driver's namespace, `rby1` by default (for example, `/rby1/stream_control`).

| Service | Type | Description |
|---------|------|-------------|
| `robot_power` | `rby1_msgs/StateOnOff` | Power on/off. `parameters`: `"all"`, or a power device such as `"48v"`. On the simulator every name is treated as `all` |
| `robot_servo` | `rby1_msgs/StateOnOff` | Servo on/off. `parameters`: `"all"`, or joint/part names. Servo off also cancels control and disables the Control Manager |
| `tool_flange_power` | `rby1_msgs/StateOnOff` | Tool flange output voltage, both flanges. `state: true` with `parameters` `"12"`/`"12v"` or `"24"`/`"24v"`; `state: false` switches the output off. Any other value is refused |
| `gravity_compensation` | `rby1_msgs/GravityCompensation` | Gravity compensation on/off per part (`torso`, `right_arm`, `left_arm`) |
| `cancel_control` | `std_srvs/Trigger` | Stops every command at once **and closes every stream channel** |
| `get_cartesian_pose` | `rby1_msgs/GetCartesianPose` | The transform of `target_link` in `ref_link`, from the SDK's model |
| `control_manager_command` | `rby1_msgs/ControlManagerCommand` | Send `CMD_ENABLE` / `CMD_DISABLE` / `CMD_RESET` / `CMD_UNLIMIT` to the Control Manager |
| `stream_control` | `rby1_msgs/StateOnOff` | Open (`state: true`) or close (`state: false`) the stream channels named in `parameters`: `right_arm`, `left_arm`, `torso`, `mobile`, `head`, comma-separated. Empty or `all` means every channel. See [Command Streams](command_streams.md) |
| `hardware_control` | `rby1_msgs/StateOnOff` | Claim (`state: true`) or release (`state: false`) the control right for a `ros2_control` controller manager ([ros2_control Hardware Interface](hardware_interface.md)) |
| `set_trajectory_impedance` | `rby1_msgs/SetTrajectoryImpedance` | Joint impedance on or off for the torso and each arm, for `follow_joint_trajectory` and `stream_joint`: stiffness per joint, damping ratio and torque limit (100 N·m/rad, 1.0 and 10 N·m when left out) |

Examples:

```bash
ros2 service call /rby1/tool_flange_power rby1_msgs/srv/StateOnOff "{state: true, parameters: '12'}"
ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: true, parameters: 'mobile'}"
ros2 service call /rby1/control_manager_command rby1_msgs/srv/ControlManagerCommand "{command: 1}"
```

::: warning
`robot_power` and `robot_servo` switch power and motors on the real robot, and `tool_flange_power` powers what is attached to the tool flanges.
Before you call them, check that nothing and nobody is in the robot's reach and that the E-Stop is within reach.
:::

## `ControlManagerCommand` constants

| Constant | Value | Description |
|----------|-------|-------------|
| `CMD_NONE` | `0` | No operation |
| `CMD_ENABLE` | `1` | Enable the Control Manager (position hold). Enables in unlimited mode when the parameter `control_manager_unlimited` is `true` |
| `CMD_DISABLE` | `2` | Cancel control, then disable the Control Manager (transition to IDLE) |
| `CMD_RESET` | `3` | Reset a MAJOR/MINOR fault |
| `CMD_UNLIMIT` | `4` | Enable the Control Manager, ignoring its range of motion limits |

::: danger CMD_UNLIMIT
`CMD_UNLIMIT` enables the Control Manager without checking the joint limits.
Use it only to move a joint that stopped just outside its limit back inside (for example with `06_zero_pose`), then disable and enable normally.
:::

## Two ways to stop a command

- **Action cancel** stops only the goal it was sent for. The stream channels stay open, so the next command goes out at once.
- **`cancel_control`** stops every command at once **and closes every stream channel**. After it, open the channels again with `stream_control` before you send `cmd_vel` or stream commands.

Example `11_cancel_control` shows both. Whether a channel is open is reported in the `robot_state` topic as `robot_stream_state` (`true` while any channel is open).

## `robot_joint` and `robot_cartesian` while a channel is open

With no stream channel open, `robot_joint` and `robot_cartesian` are single commands: the robot reports their end, and the result carries its `finish_code`.

::: warning
**With any stream channel open**, these actions go out on the parts' channels instead:
- The goal ends after the command's `minimum_time` (the longest of the parts'), without the robot's report of arrival. Check arrival on `joint_overall_states`.
- A part whose channel is closed is refused (`Stream: stream channel 'right_arm' is not open ...`).
:::

## `set_trajectory_impedance` while a trajectory runs

`set_trajectory_impedance` is refused only while a `follow_joint_trajectory` goal is executing, so that a trajectory does not switch control mode midway.
Send it when the trajectory is done. If a stream channel is open, the driver sends the next upper-body command on a new stream in the new mode; you do not need to close and reopen the stream.

Verified against: rby1-ros2 v1.0.0 `rby1_driver/src/power.cpp` (`tool_flange_control`), `rby1_driver/src/control_stream.cpp` (`stream_control_callback`, `set_trajectory_impedance_callback`), `rby1_msgs/srv/*.srv`, `Doc/manual/02_driver.md`.
