# Leader Arm

The **leader arm** is an option for teleoperation. Earlier documents and SDK versions call it the *master arm*.

Every joint of the leader arm is motorized, unlike passive devices. It has the same joint configuration as the RB-Y1 arms, so you can map it to the robot at the task level or at the joint level. It is scaled to about 65% of the RB-Y1 arm, so it fits in a smaller workspace.

<img :src="$withBase('/images/options/leader_arm/leader_arm0.png')" alt="Leader arm with two arms and handles" class="center white-bg" style="width:400px">

<div>

<iframe src="https://www.youtube.com/embed/A6h2GSoIjt8" allowfullscreen loading="lazy"></iframe>

</div>

## Specifications

| Item | Value |
| --- | --- |
| Joints | 14 (7 per arm, same configuration as the RB-Y1 arms) |
| Handles | 2 (one per arm), each with a button and a trigger |
| Actuators | Dynamixel, Protocol 2.0, 2 Mbps |
| Connection | user PC (UPC), device `/dev/rby1_leader_arm` |
| Power | robot 12 V power line |
| Robot model | `models/leader_arm/model.urdf` in rby1-sdk |

## Handle and redundancy

The leader arm has redundant degrees of freedom, so you can do the same task in different postures. Press and hold the button to move the leader arm by hand: it is then gravity-compensated. Release the button to hold the current pose.

<div style="text-align: center;">
  <video width="400" controls autoplay loop muted>
    <source :src="$withBase('/videos/options/leader_arm/leader_arm_redundancy.mp4')" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

Each handle has a **button** and a **trigger**. While you press the button, the robot follows the leader arm. When you release it, the robot holds its position (position lock). The **trigger** controls the gripper.

<div style="text-align: center;">
  <video width="400" controls autoplay loop muted>
    <source :src="$withBase('/videos/options/leader_arm/leader_arm_trigger_button.mp4')" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

<img :src="$withBase('/images/options/leader_arm/leader_arm5.png')" alt="Leader arm handle with the button and the trigger" class="center white-bg" style="width:600px">

## Tripod

The leader arm is mounted on a tripod. You can move it and adjust its height and angle to control the robot from different positions.

<img :src="$withBase('/images/options/leader_arm/leader_arm4.jpg')" alt="Leader arm on its tripod" class="center white-bg" style="width:400px">

<img :src="$withBase('/images/options/leader_arm/leader_arm6.png')" alt="Leader arm tripod adjusted for height and angle" class="center white-bg" style="width:600px">

## Connect the leader arm

1. Connect the leader arm to the UPC with its cable.
2. On the UPC, check that the device exists:

   ```bash
   ls /dev/rb*
   ```

   You should see `/dev/rby1_leader_arm`. Older UPC images use the name `/dev/rby1_master_arm`; the SDK falls back to it when `/dev/rby1_leader_arm` does not exist and prints a warning. This check shows that the USB-to-RS485 converter is present. It does not show that the leader arm itself answers.
3. If you get a permission error, see the udev steps in the [FAQ](../sdk/troubleshooting/generated/faq.md).
4. Run the state check example. It turns on the 12 V power, controls the leader arm motors and shows the leader arm joint states. It sends no motion command to the robot. Keep people and objects clear of the leader arm while it runs.

   ```bash
   # In an rby1-sdk checkout; the example loads ../../models/leader_arm/model.urdf
   cd rby1-sdk/examples/python
   python 20_leader_arm_state_check.py --address 192.168.30.1:50051 --model m
   ```

   Use `--model a` for Model A.

For teleoperation with the leader arm, see [Teleoperation & Data Collection](teleoperation.md).

## SDK

- Python: `rby1_sdk.upc.LeaderArm`; C++: `rb::upc::LeaderArm` (`include/rby1-sdk/upc/leader_arm.h`). `MasterArm` is a deprecated alias.
- Examples in rby1-sdk v0.10.1: <a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/20_leader_arm_state_check.py" target="_blank" rel="noopener noreferrer">20_leader_arm_state_check.py</a>,
  <a href="https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/35_leader_arm_teleop_with_monitor.py" target="_blank" rel="noopener noreferrer">35_leader_arm_teleop_with_monitor.py</a>
  (C++ versions with the same numbers are in `examples/cpp/`).

Verified against: rby1-sdk v0.10.1 `include/rby1-sdk/upc/leader_arm.h`, `include/rby1-sdk/upc/device.h`, `src/upc/device.cpp`, `include/rby1-sdk/base/dynamixel_bus.h`, `examples/python/20_leader_arm_state_check.py`, `examples/python/35_leader_arm_teleop_with_monitor.py`.
