# Operation

## Direct Teaching Buttons

::: danger WARNING
When the Control Manager is enabled and the control state is idle (solid blue status LED), pressing a Direct Teaching button on a wrist lets you move that arm by hand. If you press the buttons on **both** wrists at the same time, the torso is also released and moves together with the arms. The upper body can then move in a way you do not expect and hit or trap you.

- Press the buttons on both wrists at the same time only when you intend to move the torso.
- Keep your body out of the space under and beside the arms and torso while the buttons are pressed.
:::

<img :src="$withBase('/images/safety_and_precautions/operations_safety/direct_teaching.png')" alt="Direct Teaching buttons on the left and right wrists, circled" class="center white-bg" style="width:60%">

---
## Releasing the Torso Brakes

::: danger WARNING
When you release the torso brakes with the brake button on the torso or in the Web UI, the torso is no longer held. Depending on the posture, it can move under gravity, and the robot can lose balance or tip over. This can cause serious injury.

Before you release a torso brake:
- Move the robot to a posture with the upper body above the mobile base, such as the zero pose.
- Support the torso so that it cannot fall, and keep your body out of its path.
- Release only the joints you need. In the Web UI **Control Panel**, select them in the **Brake** card and press **RELEASE** (newer Web UI versions ask you to confirm).
- Operate brakes with the power on and the servos of those joints off. Newer Web UI versions refuse brake commands while those servos are on.
- When you are done, press **ENGAGE** before you turn the servos on again.
:::

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/operations_safety/brake_webui.png')" alt="Brake card in the Web UI with torso_0 to torso_5 selected and the RELEASE button highlighted" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/operations_safety/brake_button.png')" alt="Brake button on the torso, marked with a red box" class="white-bg">

</div>

</div>

---
## Joints Without a Brake

::: danger WARNING
Not every joint has a brake. After an E-Stop, a power off or a servo off, joints without a brake are not held. They can turn under gravity or when pushed, and the mobile base can roll.

Joints without a brake (Model A and Model M):
- the wheel joints of the mobile base,
- `right_arm_6` and `left_arm_6`,
- `head_0` and `head_1` on robot model versions 1.0 and 1.1.

To check your robot, read `has_brake` for each joint from `robot.get_robot_info().joint_infos`, or run the SDK example [`08_check_firmware_version.py`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/08_check_firmware_version.py).
:::

---
## Pinch Points on the Robot

::: warning CAUTION
Fingers and hands can be caught between moving links of the arms, between an arm and the torso, between torso links, and between the gripper fingers.

- Keep your hands out of the gaps between links while the robot moves or while you move it by hand with the Direct Teaching buttons.
- Do not put your fingers between the gripper fingers while the gripper is powered.
:::

---
## Pinch Points on the Leader Arm

::: warning CAUTION
When you operate the leader arm, fingers or hands can be caught between its joints.

- Keep your hands clear of all joint gaps during operation.
- Keep a safe distance from moving parts while the robot is active.
:::

<img :src="$withBase('/images/safety_and_precautions/operations_safety/leader_arm.png')" alt="Three leader arm joints where fingers can be caught, marked with red boxes" class="white-bg" style="width:100%">
