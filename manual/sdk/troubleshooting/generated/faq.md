# FAQ

### Q: When I press the enable button in the control, nothing happens, and the control mode remains in the `idle` state. What could be the cause, and how can I resolve it?

**A:**
This issue may occur when the robot is near a joint limit. If a joint is beyond its limit when you turn the servos on, the Control Manager cannot switch to `Enabled`.
For other reasons, see [Fault Diagnosis](../fault-diagnosis.md#enable-fails).

To resolve this:

1. Find the joint that is out of range. The Control Manager logs it when enabling fails, for example:
   `[ControlManager::Enable] Joint <index> (right_arm_3) position <value> is below the lower limit <limit>. Enabling process aborted.`
   Read the log in the Web UI, or with the SDK log examples (`15_log.py`, `16_log_stream.py`).
2. Turn the power off and move that joint slightly back into its range with the physical brake release button.
3. Turn the power on, enable the servos and enable the Control Manager again.

::: warning
When a brake is released, the joint is free and the links above it can fall under their own weight.
Before you press the brake release button, support the link by hand (two people for the torso joints `torso_*` and for `right_arm_0`–`right_arm_2` and `left_arm_0`–`left_arm_2`),
release the button before you let go, and keep hands out of pinch points. See [Precautions](../../../precautions/hardware_handling.md).
:::

---
### Q: How can I integrate arm commands with wheel navigation?

**A:**
The Control Manager runs several commands at the same time as long as they use different joints. A command is blocked only by a running command that uses one of the same joints (see the next question).
The arms and torso (the body) and the wheels (the mobility) are different joints, so you can drive the mobile base and move the arms together.

Put both in one command with `ComponentBasedCommandBuilder`: `set_body_command()` for the arms and torso, `set_mobility_command()` for the wheels.

```python
import numpy as np
import rby1_sdk as rby

rc = rby.RobotCommandBuilder().set_command(
    rby.ComponentBasedCommandBuilder()
    .set_body_command(
        rby.BodyComponentBasedCommandBuilder().set_right_arm_command(
            rby.JointPositionCommandBuilder()
            # right_arm_0 ... right_arm_6, the ready pose of 31_multi_controls.py
            .set_position(np.deg2rad([0.0, -5.0, 0.0, -120.0, 0.0, 70.0, 0.0]))
            .set_minimum_time(3.0)
        )
    )
    .set_mobility_command(
        rby.SE2VelocityCommandBuilder()
        .set_command_header(rby.CommandHeaderBuilder().set_control_hold_time(1.0))
        .set_minimum_time(3.0)
        .set_velocity([0.1, 0.0], 0.0)  # linear [m/s], angular [rad/s]
    )
)
# robot: connected, servos on, Control Manager enabled (see initialize_robot in 00_helper.py)
handler = robot.send_command(rc)
```

You can also send the body command and the mobility command as two separate commands, with `send_command()` or with two command streams.
For working mobility code, see [37_mobile_test.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/37_mobile_test.py).

::: warning
This moves the right arm and drives the mobile base. Clear the floor and the space around the robot and keep the E-Stop within reach.
On Model A the Y component of an SE(2) velocity command is ignored.
:::

::: info `WholeBodyCommandBuilder` is not for this
In SDK v0.10.1 a whole-body command can only hold a stop command or a real-time control command. It cannot hold arm or mobility commands.
:::

---
### Q: What happens when I send a set command to only some joints, while the rest of the joints continue moving?

**A:**
The Control Manager compares the joints of the new command with the joints of the commands that are running:

- **No shared joints:** the new command starts and runs at the same time as the running commands.
- **Shared joints, higher priority:** the new command is accepted. The running command that uses those joints is asked to stop and is preempted. Then the new command starts.
- **Shared joints, same or lower priority:** the new command is refused and is preempted.

In SDK v0.10.1 a preempted command shows the finish code `Canceled`, not `Preempted`. See [Command finish codes](../fault-diagnosis.md#finish-codes).

The priority is an integer from 0 to 999; values outside this range are clamped. A higher number is a higher priority.
The default priority of `send_command()` and `create_command_stream()` is 1.
For an example with overlapping commands and priorities, see [31_multi_controls.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/31_multi_controls.py).

---
### Q: What is the difference between `send_command` and `create_command_stream`?

**A:**

- `robot.send_command(builder, priority=1)` sends one command. It returns a handler that you can wait on (`get()`, `wait()`) or cancel. Use it for single motions, for example a move to a waypoint.
- `robot.create_command_stream(priority=1)` opens a command stream. You then call `stream.send_command(builder)` as often as you need, and each new command updates the running one. Use it when you send new targets continuously, for example in teleoperation or when you follow a trajectory in your own loop.

Examples: [32_command_stream.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/32_command_stream.py) and [33_cartesian_command_stream.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/33_cartesian_command_stream.py).

---
### Q: What is the meaning of `send_command().get()`?

**A:**
`send_command()` returns a command handler. Its `get()` method blocks until the command is finished and returns the command feedback.
Check `finish_code` in the feedback: `rby1_sdk.RobotCommandFeedback.FinishCode.Ok` means the command finished normally.

---
### Q: What happens when a stream is canceled?

**A:**
The command of the stream finishes. While no other command uses those joints, the Control Manager holds them at the last target position it sent.

---
### Q: How can I receive sensor feedback while in a stream?

**A:**
To read the robot state once, use `get_state()`. To receive the robot state continuously, use `start_state_update(callback, rate)`; the SDK then calls your callback with each new state.
Reading the state does not interfere with a command stream.

For examples, see [03_robot_state.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/03_robot_state.py) and [04_robot_state_stream.py](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/04_robot_state_stream.py).

---
### Q: The leader arm teleoperation example (`35_leader_arm_teleop_with_monitor`) does not run. What could be the cause, and how can I resolve it?

**A:**
This example runs on the user PC (UPC) and does not run in simulation. Check the following:

- The leader arm is connected to the UPC with its cable, as in [Connect the leader arm](../../../options/leader_arm.md#connect-the-leader-arm).
- The wiring on the UPC bypass port matches your leader arm kit. This manual does not document the jumper position for that port. Ask [support](../../../support.md) for it.
- The program can open the USB serial devices. Run it with `sudo`, or set the udev rule below.

The SDK opens the leader arm at `/dev/rby1_leader_arm`. If that device does not exist, it uses the older name `/dev/rby1_master_arm`. The gripper is at `/dev/rby1_gripper`.
These names are symbolic links that a udev rule creates for the U2D2 USB-serial adapters.

If you don't want to use `sudo` every time you run the program, follow the steps below.

::: warning
You change the udev rules for the U2D2 adapters at your own risk.
The rules match each adapter by its serial number (`ATTRS{serial}`). If you change or mistype the serial number, the device link (`/dev/rby1_leader_arm` or `/dev/rby1_gripper`) is not created and the leader arm or the gripper stops working.
Back up the rules file before you change it.
:::

1. **Back up the existing udev rules file**:

   ```bash
   sudo cp /etc/udev/rules.d/99-u2d2.rules /etc/udev/rules.d/99-u2d2.rules.bak
   ```

2. **Open the udev rules file**:

   ```bash
   sudo nano /etc/udev/rules.d/99-u2d2.rules
   ```

3. **The file looks like this**. Keep the serial numbers and the link names that are already in your file. Older UPC images use `rby1_master_arm` instead of `rby1_leader_arm`.

   ```bash
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_gripper"
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_leader_arm"
   ```

4. **Add `MODE` and `RUN` to each line** to allow access without `sudo`:

   ```bash
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_gripper", MODE="0666", RUN+="/bin/chmod 666 /sys/bus/usb-serial/devices/%k/latency_timer"
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_leader_arm", MODE="0666", RUN+="/bin/chmod 666 /sys/bus/usb-serial/devices/%k/latency_timer"
   ```

5. **Reload the udev rules**:

   ```bash
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

6. **Check that the devices are listed**:

   ```bash
   ls -l /dev/rby1_*
   ```

   You should see `rby1_gripper` and `rby1_leader_arm` (or `rby1_master_arm`).

7. **If the devices do not show up, restore the backup**:

   ```bash
   sudo cp /etc/udev/rules.d/99-u2d2.rules.bak /etc/udev/rules.d/99-u2d2.rules
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

Verified against: rby1-sdk v0.10.1 `protos/rb/api/whole_body_command.proto`, `python/robot_command_builder.cpp`, `python/robot.cpp` (`send_command`, `create_command_stream`, `start_state_update`), `include/rby1-sdk/upc/device.h`, `examples/python/31_multi_controls.py`, `37_mobile_test.py`, `35_leader_arm_teleop_with_monitor.py`; robot core `core/control/control_manager.cpp` (`SetControl`, priority clamp and joint mask check), `core/control/control_manager.h` (`kDummyControlPriority`).
