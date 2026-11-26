# First Motion

Move the robot with the SDK for the first time, and check that the E-Stop stops it.
You run three Python examples from the rby1-sdk repository:

1. `01_hello_rby1.py`: connect and print the robot information. The robot does not move.
2. `23_zero_pose.py`: power on, enable the servos and the Control Manager, and move to the zero pose.
3. `24_demo_motion.py`: a demo of joint, Cartesian, impedance and optimal-control commands.

Between steps 2 and 3 you test the E-Stop.

::: danger Before you start
- Do [Hotspot & Web UI](hotspot-and-webui.md) first, including **Finish** (Control Manager back in the standard mode).
  The robot should stand in the zero pose.
- Hold the E-Stop button or the remote controller during every step on this page. See [E‑Stop Basics](estop-basics.md).
- Clear at least the reach of both arms and the torso around the robot. Keep people out of this area.
- `23_zero_pose.py` and `24_demo_motion.py` turn on **all** power rails and **all** servos by default.
:::

## Get the examples

Install the SDK as in [SDK Installation](sdk-install-and-state.md), then get the examples of the same version:

```bash
git clone --branch v0.10.1 https://github.com/RainbowRobotics/rby1-sdk.git
cd rby1-sdk/examples/python
```

In the commands below, replace `192.168.12.1:50051` with your robot address
([Network and Ports](network-and-ports.md)) and `a` with your model (`a`, `m` or `ub`).

## 1. Connect: `01_hello_rby1.py`

```bash
python 01_hello_rby1.py --address 192.168.12.1:50051 --model a
```

It prints `Hello, RB-Y1!` and the robot information. If it prints `Failed to connect to the robot.`,
see [Connection Troubleshooting](connection-troubleshooting.md).

## 2. Zero pose: `23_zero_pose.py`

::: warning The robot moves
The torso and both arms move to the zero pose (all joint angles 0) over at least 10 seconds.
:::

```bash
python 23_zero_pose.py --address 192.168.12.1:50051 --model a
```

The example does the following (`00_helper.py`, `initialize_robot`):

1. Turns on the power rails that match `--power` (default `.*`, all rails).
2. Turns on the servos that match `--servo` (default `.*`, all joints).
3. Resets the Control Manager if it is in `MinorFault` or `MajorFault`.
4. Enables the Control Manager in the standard mode (joint limits are checked).
5. Sends a joint position command to the torso and both arms.

The head and the wheels do not move.

## 3. Test the E-Stop

Do this test with the robot standing still in the zero pose.

1. Press the E-Stop button (or button 1 on the remote controller).
2. Check that the 48 V power is cut:
   - In the Web UI, the **EMO** card at the top shows **Pressed**, and **Power** in the status bar is no longer blue.
   - The Control Manager goes to **Major Fault**, because the power changed while it was enabled.
3. Check from the SDK that the robot reports the E-Stop:

   ```python
   import rby1_sdk as rby

   robot = rby.create_robot("192.168.12.1:50051", "a")
   if not robot.connect():
       raise SystemExit("Cannot connect")
   print([emo.state for emo in robot.get_state().emo_states])  # expect EMOState.State.Pressed
   print(robot.get_control_manager_state().state)               # expect State.MajorFault
   ```

4. Release the E-Stop (turn the button to reset it).
5. Run `23_zero_pose.py` again. It resets the fault, powers on, enables the servos and the Control Manager,
   and holds the zero pose.

::: warning
When the E-Stop cuts the power, `right_arm_6`, `left_arm_6` and the wheels have no brakes.
The wrists can turn under load, and the mobile base can roll on a slope. See [E‑Stop Basics](estop-basics.md).
:::

If the robot does not stop, or the E-Stop is not reported, do not continue. Contact Rainbow Robotics support
([Error Reporting](../sdk/troubleshooting/generated/error_reporting.md)).

## 4. Demo motion: `24_demo_motion.py`

::: danger The robot moves fast and through a large space
The demo moves the torso and both arms through many poses, with joint, Cartesian, impedance,
optimal-control and mixed commands. Clear the space around the robot and keep the E-Stop in your hand.
:::

::: warning The demo changes robot parameters
At the start the demo calls `robot.set_parameter(...)`, which saves the values on the robot.
It sets `joint_position_command.cutoff_frequency` and `cartesian_command.cutoff_frequency` to 5 Hz
(factory default 15 Hz) and keeps them after the demo ends. To restore the defaults:

```python
robot.factory_reset_parameter("joint_position_command.cutoff_frequency")
robot.factory_reset_parameter("cartesian_command.cutoff_frequency")
```
:::

::: info Model UB
The demo sends 6-joint torso commands, written for Model A and Model M. Model UB has a 2-joint torso:
do not run this demo on Model UB.
:::

```bash
python 24_demo_motion.py --address 192.168.12.1:50051 --model a
```

It first moves to a ready pose, runs the demos one after another and ends with `end of demo`.

To stop a running motion:

- **CANCEL CONTROL** at the top of the Web UI, or `robot.cancel_control()` in the SDK
  (example `26_cancel_control.py`), cancels the running command. The power stays on.
- The E-Stop cuts the 48 V power to the actuators.

## 5. Finish

1. Run `23_zero_pose.py` to return to the zero pose.
2. Disable the Control Manager (Web UI **Control Disable**, or `robot.disable_control_manager()`).
3. Turn off the power rails.

See [Power & Battery](../precautions/power_and_battery.md) for the full shut-down procedure.

## Next steps

- [Examples](../examples/ex.md): more SDK examples, by topic.
- [ROS 2](../ros2/index.md): drive the robot from ROS 2.
- [Simulation](../simulators/index.md): try commands on a simulated robot first.
- [Leader Arm](../options/leader_arm.md): teleoperation with the leader arm.

---

Verified against: rby1-sdk v0.10.1 `examples/python/00_helper.py`, `01_hello_rby1.py`, `23_zero_pose.py`,
`24_demo_motion.py`, `26_cancel_control.py`, `python/robot.cpp` (`set_parameter` writes to the robot database by default,
`factory_reset_parameter`), `python/robot_state.cpp`, `python/control_manager_state.cpp`;
robot core `core/robots/rby1a/parameters.h` (cutoff frequency defaults), `core/control/control_manager.cpp`
(power change while enabled → `MajorFault`), `core/robots/rby1a/robot_hardware.cpp` (brakes closed on E-Stop);
Web UI `rby1-web/rby1-frontend/src/components/NavigatorDrawer.vue`, `DashboardComponents/RpcStatusCards.vue`; `sdk/models/generated/model_*.md` (joints without brakes).
