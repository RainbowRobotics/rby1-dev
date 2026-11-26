# Fault Diagnosis

The Control Manager in the robot software runs every motion command. When it detects a problem, it stops the commands and goes to a fault state.
This page explains the states, the causes of each fault, where to find the reason, and how to recover.

## Control Manager states

| State | Meaning | Motion commands | Default LED |
| --- | --- | --- | --- |
| `Idle` | Not enabled. This is the state after boot and after a fault reset. | Refused (the SDK shows finish code `InitializationFailed`, see [Command finish codes](#finish-codes)) | White, blinking until all power is on |
| `Enabled` | Ready. Holds the joints and runs commands. | Accepted | Blue; green while a command runs |
| `MinorFault` | A command or the hardware readiness failed. All commands were stopped; the power stays on. | Refused (the SDK shows finish code `ControlManagerIdle`) | Red, blinking |
| `MajorFault` | A motor, power or state error. All commands were stopped and the robot software turned the power off. | Refused (the SDK shows finish code `ControlManagerIdle`) | Red |

`Unknown` appears in the SDK only when no state has been received.

The Control Manager also reports a **control state**: `Idle` (no command runs), `Executing` (commands run) or `Switching` (a new command waits to start).

Read the states with the SDK:

```python
import rby1_sdk as rby

robot = rby.create_robot("192.168.30.1:50051", "a")  # your address and model
robot.connect()
cm = robot.get_control_manager_state()
print(cm.state, cm.control_state)
```

To watch the state continuously, pass a callback with two parameters to `start_state_update()`: `cb(robot_state, control_manager_state)`.

## Enable fails {#enable-fails}

`enable_control_manager()` returns `False` and the state stays `Idle` (or a fault state). The log tells you why. Look for lines that start with `[ControlManager::Enable]`:

| Log message (shortened) | Cause | What to do |
| --- | --- | --- |
| `The current state is in fault mode (Minor or Major Fault). Expected state is Idle` | A fault was not reset. | Reset the fault first (see [Recover](#recover)). |
| `Not ready for send command, check hardware state` | The hardware is not ready for commands, for example the power or the servos are off. | Turn the power and the servos on, then try again. |
| `Robot state check exceeded the timeout limit of 500ms` | The robot software did not receive a recent robot state. | Check the power, then restart the robot if it repeats. |
| `Joint <index> (<name>) position <value> is below the lower limit` or `exceeds the upper limit` | A joint is outside its position limit. | Move the joint back into its range. See the [FAQ](./faq.md). |

Only the joints whose servos are on when you enable are controlled. Turn on the servos of all joints you want to command before you enable.

## Causes of a MinorFault

The Control Manager goes to `MinorFault` while it is `Enabled` when:

| Log message | Cause |
| --- | --- |
| `[ControlManager] Hardware is not ready for receiving command` | The hardware stopped accepting commands. |
| `[ControlManager] Control state check result: ...` | A running command found an invalid state (the message gives the details). |
| `[ControlManager] Control execution timeout: Control execution time limit exceeded` | A command took too long to compute in one control cycle. |

All commands end, and the target of each joint is set to its current position. The power stays on.

## Causes of a MajorFault

The Control Manager goes to `MajorFault` while it is `Enabled` when:

| Log message | Cause |
| --- | --- |
| `[ControlManager] RobotState Update Timeout` | No robot state for 200 ms. |
| `[ControlManager] Joint <i> <name> JAM ERROR` | The motor driver reports a jam (blocked joint). |
| `[ControlManager] Joint <i> <name> CUR ERROR` | The motor driver reports over-current. |
| `[ControlManager] Joint <i> <name> BIG ERROR` | The motor driver reports a BIG error. |
| `[ControlManager] Joint <i> <name> INPUT ERROR` | The motor driver reports an input error. |
| `[ControlManager] Joint <i> <name> TEMPERATURE ERROR` | The joint temperature reading is above 120. |
| `[ControlManager] Tracking error <i> <name> (target position: ..., position: ...)` | A torso or arm joint is more than 0.2 rad (about 11.5°) away from its target, for example after a collision. |
| `[ControlManager] Joint <i> <name> 'power' is down` | A joint lost power after enabling. |
| `[ControlManager] Joint <i> <name> 'ready' is down` | A joint stopped being ready after enabling, for example its servo was turned off. |
| `[ControlManager] Power state <i> is changed during enable state` | A power device was turned on or off while enabled. |

Then the robot software:

1. ends all commands,
2. turns the power off (`[ControlManager] Major Fault Reaction Started...`),
3. saves the robot states recorded before the fault to a fault log file and logs `[RobotApp] Robot states have been saved: [logs/fault-<time>.csv]`.

::: warning
JAM, CUR, BIG, INPUT and TEMPERATURE errors can mean a hardware problem or a collision.
Find the cause before you enable the robot again. If the same error repeats, stop using the robot and contact support with the fault log (see [Error Reporting](./error_reporting.md)).
:::

## Read the logs

- **Robot log:** read it in the Web UI, or with the SDK examples [15_log](../../examples/ex.md) (`robot.get_last_log(count)`) and [16_log_stream](../../examples/ex.md) (`robot.start_log_stream(callback, rate)`).
- **Fault log:** each `MajorFault` creates one CSV file. List and download the files with [17_fault_log](../../examples/ex.md):

  ```python
  files = robot.get_fault_log_list()
  print(files)
  with open("fault.csv", "wb") as f:
      robot.download_file(files[0], f)  # pick the file of the fault time from the list
  ```

- **All logs:** to collect every log of the robot PC (RPC), use [Log Backup](../../rpc_management_tools/log_backup.md).

### Fault log format

The file starts with comment lines (`#`): the fault time, the robot model, the SDK version of the robot software, the log duration, the joint names, and the codes of the state columns:

- power states: `0` Unknown, `1` Power On, `2` Power Off
- Control Manager state: `0` Idle, `1` Enabled, `2` Minor Fault, `3` Major Fault
- control state: `0` Idle, `1` Executing, `2` Switching

Then one row per sample with these columns:

| Column | Content |
| --- | --- |
| `timestamp` | Time in seconds. |
| `power_<device>` | State of each power device. |
| `control_manager_state`, `control_state` | The codes above. |
| `<joint>_state` | Motor state bits of the joint. On Rainbow motors, bit 8 is JAM, bit 9 over-current, bit 10 BIG, bit 11 INPUT. |
| `<joint>_pos`, `<joint>_vel`, `<joint>_cur`, `<joint>_tq` | Measured position, velocity, current and torque. |
| `<joint>_target_pos`, `<joint>_target_vel`, `<joint>_target_fb_gain`, `<joint>_target_ff_tq` | Command sent to the joint: target position, target velocity, feedback gain and feed-forward torque. |

Example: find the joints with a motor error bit set and the first time it happened.

```python
import pandas as pd

df = pd.read_csv("fault.csv", comment="#")
for col in [c for c in df.columns if c.endswith("_state") and c not in ("control_manager_state", "control_state")]:
    bits = df[col].astype("int64")
    hit = df[((bits >> 8) & 0xF) != 0]
    if not hit.empty:
        print(col, "first error at", hit["timestamp"].iloc[0])
```

## Recover {#recover}

1. **Find the cause** in the log (see the tables above) and remove it: clear an obstacle, let a hot joint cool down, move a joint back into its range.
2. **Wait for the fault reaction to finish** after a `MajorFault`. A reset is refused with `Reset denied: fault reaction is still active.` until the fault log is saved.
3. **Reset the fault.** The state goes back to `Idle`.
4. **Turn the power and the servos on** again; a `MajorFault` turned the power off.
5. **Enable the Control Manager.**

```python
import rby1_sdk as rby

robot = rby.create_robot("192.168.30.1:50051", "a")  # your address and model
robot.connect()

if robot.get_control_manager_state().state in (
    rby.ControlManagerState.State.MinorFault,
    rby.ControlManagerState.State.MajorFault,
):
    robot.reset_fault_control_manager()

robot.power_on(".*")
robot.servo_on(".*")
robot.enable_control_manager()
```

This is the same sequence as `initialize_robot()` in the SDK example `00_helper.py`.

::: warning
Turning the servos on and enabling the Control Manager makes the robot hold its joints with the motors. Keep the E-Stop within reach and keep people away from the robot while you recover.
Do not reset and enable again and again without finding the cause.
:::

Other notes:

- `reset_fault_control_manager()` is refused while the state is `Enabled` (`Reset denied: system is currently in 'Enabled' state.`).
- `disable_control_manager()` is refused while a command is running (`There are still active controls`). Cancel the command first with `cancel_control()` or `handler.cancel()`.

## Command finish codes {#finish-codes}

When a command ends, its feedback has a finish code (`rby1_sdk.RobotCommandFeedback.FinishCode`).

::: warning The SDK shows a shifted finish code
The robot software (checked up to version 0.11.0) has no `Canceled` code. It sends its own code number, and the SDK reads that number with its own list, which has `Canceled` at position 2.
From `Preempted` on, every code is shifted by one. Use the first column of the table below, not the name alone, to find the reason.
The table was derived by reading the code. It was not checked on a robot or a simulator.
:::

| Finish code in the SDK | Reason in the robot software |
| --- | --- |
| `Ok` | The command finished normally. |
| `Canceled` | The command was preempted or canceled: another command with a higher priority took over the same joints; the new command was refused because a running command on the same joints has the same or a higher priority (see the [FAQ](./faq.md)); or the command was canceled with `cancel_control()` or `handler.cancel()`. |
| `Preempted` | The command could not be initialized. The robot log has the details (`Control initialization failed`). |
| `InitializationFailed` | The Control Manager is `Idle`. Enable it first. |
| `ControlManagerIdle` | The Control Manager is in `MinorFault` or `MajorFault`. Recover first. |
| `ControlManagerFault` | The command was still open when the Control Manager was no longer `Enabled`. |
| `Unknown` | The Control Manager stopped all commands because of a fault. Check the Control Manager state and the log. |
| `UnexpectedState` | Not sent by the robot software. |

Verified against: robot core `core/control/control_manager.cpp` (`Enable`, `Disable`, `ResetFault`, `SetControl`, fault checks in the control loop), `core/control/control_manager.h` (states, `kTemperatureErrorThreshold`), `core/robots/robot_app_base.cpp` (major fault reaction and fault CSV format), `core/modules/default_led.cpp` (LED colors); rby1-sdk v0.10.1 `include/rby1-sdk/control_manager_state.h`, `python/robot.cpp` (`get_control_manager_state`, `reset_fault_control_manager`, `get_fault_log_list`, `download_file`, `start_state_update`, `get_last_log`), `python/robot_command_feedback.cpp` (finish codes), `protos/rb/api/robot_command.proto` (`FinishCode`), `src/robot_command_feedback.cpp` (cast of the received code), `examples/python/00_helper.py`, `examples/python/17_fault_log.py`; robot core v0.11.0 `core/control/control_interface.h` (`FinishCode`), `core/service/srv_robot_command.cpp` (cast to the protocol code).
