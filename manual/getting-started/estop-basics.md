# E‑Stop Basics

## E-Stop
- E‑Stop types: E-Stop button, Remote E‑Stop

::: warning
The package includes both an E-Stop button and a remote controller.  
Both are safety tools that cut off power. For details, see [Shutdown Methods](../hardware/electrical_part.md#shutdown-methods).

Before operation, make sure the E-Stop button is reset to its normal position if it has been pressed.
:::

![Remote E-Stop](/images/getting-started/remote_emo.jpg)

![E-Stop button](/images/getting-started/emo.jpg)

## Before the first power‑on
Read this page before you power the robot on for the first time. The next pages power the robot, enable its servos and move it.

- Keep the E‑Stop button or the remote controller in your hand during all first tests.
- Check that the E‑Stop button is released (turn it to reset it) before you power on.
- Clear the space around the robot: the zero‑pose motion moves the torso and both arms.
- After the first power‑on, press the E‑Stop once and check that the robot stops, before any teleoperation, SDK control or navigation.

See also [Precautions](../precautions/general.md) and [Shutdown Methods](../hardware/electrical_part.md#shutdown-methods).

## What happens when the E‑Stop is pressed
- The 48 V power to the actuators is cut and the joint brakes engage. The robot PC (RPC) keeps running, so the Web UI and the SDK stay connected.
- The robot state reports the E‑Stop as pressed (`emo_states` in the SDK robot state).
- While the E‑Stop is pressed, **POWER ON** fails and the log shows `EMO Error: Please check EMO Switch`.

## Recovering after an E‑Stop
1. Make sure the cause of the stop is removed and the area around the robot is clear.
2. Release the E‑Stop button (turn it to reset it).
3. In the Web UI, turn the power on again (**POWER ON**).
4. Enable the servos again.
5. Enable the Control Manager. If its state shows **Fault**, press **Reset** first, then **Enable**.

To pause a motion without cutting power, use the **SOFT STOP** button at the top of the Web UI.

<!-- TODO (owner): confirm whether the remote E‑Stop receiver needs a reset after it is used, and the LED indicators. -->
