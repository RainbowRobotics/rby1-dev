# Teleoperation & Data Collection

This page shows how to control RB-Y1 with the [leader arm](leader_arm.md) and how to record data. There are three ways:

| Goal | Tool |
| --- | --- |
| Try leader arm teleoperation | SDK example `35_leader_arm_teleop_with_monitor` |
| Record joint positions and play them back | SDK examples `21_record` and `22_replay` |
| Collect datasets and train policies with LeRobot | <a href="https://github.com/RainbowRobotics/rby1-lerobot" target="_blank" rel="noopener noreferrer">rby1-lerobot</a> |

::: danger WARNING
These programs power on the robot and move the arms and the torso.

- Clear the robot's full range of motion of people and objects before you start.
- Keep the E-Stop within reach of the operator, and know where it is.
- Do not exceed the arm payload of 3 kg per arm.
- Before you start, put the leader arm in a safe posture. The teleoperation example moves the robot to a ready pose and then moves the leader arm to the same pose.

See [Precautions](../precautions/index.md) before you operate the robot.
:::

## Before you start

1. Power on the robot PC (RPC) and the user PC (UPC).
2. Check that the UPC can reach the RPC: `ping 192.168.30.1`.
3. Connect the leader arm and check the device (see [Connect the leader arm](leader_arm.md#connect-the-leader-arm)).
4. If you use the grippers, check `/dev/rby1_gripper` (see [Gripper](gripper.md)).
5. Install the SDK on the UPC and get the examples from an rby1-sdk checkout (see [SDK Installation](../getting-started/sdk-install-and-state.md)). The leader arm examples load `models/leader_arm/model.urdf` from the checkout.

## Leader arm teleoperation (SDK example)

Run the example on the UPC, in `examples/python` of the rby1-sdk checkout:

```bash
python 35_leader_arm_teleop_with_monitor.py --address 192.168.30.1:50051 --model m --mode position
```

| Option | Default | Meaning |
| --- | --- | --- |
| `--address` | (required) | Robot address, for example `192.168.30.1:50051` |
| `--model` | `a` | Robot model: `a` or `m` |
| `--mode` | `position` | Robot arm control: `position` or `impedance` |
| `--power` | `.*` | Power lines to turn on (regular expression) |
| `--servo` | `torso_.*\|right_arm_.*\|left_arm_.*` | Joints to servo on (regular expression) |
| `--align-duration` | `4.0` | Seconds to move the leader arm to the ready pose; `0` skips this step |

The example runs in five steps:

1. It connects to the robot, turns on the power and the servos, enables the Control Manager and sets the tool flange output to 12 V.
2. It initializes the leader arm and checks that all its devices answer.
3. **It moves the robot to the ready pose.**
4. It initializes the grippers and finds their limits (homing). The grippers open and close.
5. **It moves the leader arm to the ready pose.**

Then teleoperation starts:

- While you hold the button on a handle, the robot arm on that side follows the leader arm.
- When you release the button, the robot arm holds its position.
- The trigger controls the gripper on that side.

Press `Ctrl+C` to stop. The example ramps the leader arm torque down, stops the robot control, disables the Control Manager and turns off the 12 V power.

## Record and replay

`21_record` saves the robot joint positions at 10 Hz until you press `Ctrl+C`. It writes `recorded.npz` in the current directory. It turns on the power but sends no motion command.

```bash
python 21_record.py --address 192.168.30.1:50051 --model m
```

`22_replay` reads `recorded.npz` and moves the torso and both arms through the recorded positions. It moves to the first position in 5 seconds, then steps through the recording every 0.1 seconds.

```bash
python 22_replay.py --address 192.168.30.1:50051 --model m
```

::: warning
`22_replay` moves the robot. Before you run it, check that the first recorded pose is safe to reach from the current pose and that the area is clear.
:::

## Data collection with LeRobot

<a href="https://github.com/RainbowRobotics/rby1-lerobot" target="_blank" rel="noopener noreferrer">rby1-lerobot</a> is a LeRobot plugin for RB-Y1. It uses the leader arm as the teleoperator and records LeRobot datasets with camera images. Follow its README for installation, camera setup, recording and policy runs.

At the time of writing (rby1-lerobot v0.3.1):

- It requires LeRobot 0.7.0 and Python 3.12 or later.
- It supports robots of hardware version 1.2 or lower.
- It needs the leader arm URDF from an rby1-sdk checkout (`models/leader_arm/model.urdf`); the PyPI wheel does not include it.

Check the README of the release you use for the current requirements.

Verified against: rby1-sdk v0.10.1 `examples/python/21_record.py`, `examples/python/22_replay.py`, `examples/python/35_leader_arm_teleop_with_monitor.py`, `include/rby1-sdk/upc/device.h`; rby1-lerobot v0.3.1 `README.md`.
