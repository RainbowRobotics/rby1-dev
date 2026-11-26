# E‑Stop Basics

Read this page before you power the robot on for the first time. The next pages power the robot,
enable its servos and move it.

## Ways to stop the robot

| Control | What it does | Depends on the network |
| --- | --- | --- |
| **E-Stop button** (EMO) on the robot | Cuts the 48 V power to the actuators in hardware | No |
| **Remote controller** (wireless E-Stop), button 1 | Same as the E-Stop button | No |
| Web UI **ESTOP** (top bar) | Software stop: cancels the running command, then sends a power-off command for all power rails | Yes |
| Web UI **CANCEL CONTROL** (top bar), or `robot.cancel_control()` in the SDK | Cancels the running command. The power stays on; the robot holds its position while the Control Manager is enabled. The command does not resume. | Yes |

::: warning Important
The package includes an E-Stop button and a remote controller. Both cut the power in hardware.
For details, see [Shutdown Methods](../hardware/electrical_part.md#shutdown-methods).

The Web UI **ESTOP** button is not an emergency stop: it only works while your PC, the network and the robot
software respond. Always keep the E-Stop button or the remote controller within reach.
:::

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/getting-started/remote_emo.jpg')" alt="Remote controller (wireless E-Stop)" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/getting-started/emo.jpg')" alt="E-Stop button" class="white-bg">

</div>

</div>

## Before the first power‑on

- Keep the E‑Stop button or the remote controller in your hand during all first tests.
- Check that the E‑Stop button is released (turn it to reset it) before you power on.
- Clear the space around the robot: the zero‑pose motion moves the torso and both arms.
- After the first power‑on, press the E‑Stop once and check that the robot stops, before any teleoperation,
  SDK control or navigation. [First Motion](first-motion.md#3-test-the-e-stop) shows how.

See also [Safety](../precautions/index.md) and [Shutdown Methods](../hardware/electrical_part.md#shutdown-methods).

## What happens when the E‑Stop is pressed

- The 48 V power to the actuators is cut. The robot PC (RPC) keeps running, so the Web UI and the SDK stay connected.
- The brakes engage on the torso and arm joints that have brakes.
- `right_arm_6`, `left_arm_6` and the wheels have **no brakes**. The wrists can turn under load,
  and the mobile base can roll on a slope. See the brake tables in [Model A](../sdk/models/generated/model_a.md)
  and [Model M](../sdk/models/generated/model_m.md).
- If the Control Manager was enabled, it goes to **Major Fault**.
- The robot state reports the E‑Stop as pressed (`emo_states` in the SDK robot state, the **EMO** card in the Web UI).
- While the E‑Stop is pressed, power on fails: the Web UI system bar shows **Power** in orange and the log shows
  `EMO Error: Please check EMO Switch`.

## Recovering after an E‑Stop

1. Make sure the cause of the stop is removed and the area around the robot is clear.
2. Release the E‑Stop button (turn it to reset it).
3. In the Web UI, turn the power on again.
4. Enable the servos again.
5. Enable the Control Manager. If its state shows **Fault**, press **Control Reset** first, then **Control Enable**.

---

Verified against: robot core `core/robots/rby1a/robot_hardware.cpp` (E-Stop: brakes closed on torso and arm motors,
48 V off; `EMO Error` message), `core/control/control_manager.cpp` (power change while enabled → Major Fault);
Web UI `NavigatorDrawer.vue` (**CANCEL CONTROL**, **ESTOP**, Control Enable / Reset), `rby1-backend` `routers/power.py`
(`estop`: `cancel_control` then `power_off(".*")`; `soft_stop`: `cancel_control`), `UnpackingStepper.vue`
(remote button 1, Power orange), `RpcStatusCards.vue`; `sdk/models/generated/model_a.md`, `model_m.md` (joints without brakes).
