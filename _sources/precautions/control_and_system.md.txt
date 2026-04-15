# Control & System

## Precautions
<br>

### ⚠️Control via UPC Only (Leader Arm & Gripper)

- The leader arm and gripper are hardware-connected to the UPC (via U2D2).
- Therefore, they cannot be controlled from an external PC via RPC.
- When controlling the leader arm and gripper from an external PC, you must access the UPC remotely and operate them within the UPC environment.


---
### ⚠️Keep the EMO Remote Accessible During Code Execution

- Always keep the EMO remote controller within reach when running control code.
- In case of unexpected behavior, use the EMO remote to immediately stop the robot.

```{image} ../_static/images/saftey_and_precautions/control_and_system/emo.jpg
    :width: 40%
    :align: center
    :class: white_bg
```