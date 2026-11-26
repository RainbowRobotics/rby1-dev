# General

## No Collision Detection for External Obstacles

::: danger WARNING
The robot does not detect collisions with people or objects around it. A moving arm, torso or mobile base can hit a person and cause serious injury.

- Clear the area around the robot of people and obstacles before you start a motion.
- Keep a safe distance from the robot while it moves.
- Keep the E-Stop within reach (see [Control & System](control_and_system.md#e-stop-within-reach)).
:::

Self-collision (between the robot's own links) is **reported, not prevented**. The robot state reports the closest link distances (`collisions`), but the robot does **not** stop by itself. To stop on a close distance, your application must watch this value and send a stop command. See [`27_collisions.py`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/python/27_collisions.py).

---
## Weight, Payload and Transport

::: danger WARNING
The robot is heavy: Model A weighs 131 kg and Model M weighs 170 kg. Lifting or tipping it by hand can cause serious injury.

- Do not try to lift the robot by hand.
- This manual does not describe lifting points or a transport procedure. Contact Rainbow Robotics support (see [Support](../support.md)) before you lift, ship or move the robot without driving it.
- Do not exceed the arm payload of **3 kg per arm**. Weight per part and the payload are listed in [Overview](../hardware/overview.md#technical-specifications).
:::

---
## Mobile Base

::: danger WARNING
The mobile base can drive at up to 1.5 m/s (see [Overview](../hardware/overview.md#general-specifications)). The wheels have no brake. A collision with the moving base, or a base that rolls away, can cause serious injury.

- The wheel joints have no brake. After an E-Stop, a power off or a servo off, the wheels are not held, and the robot can roll on a slope or when it is pushed. Operate and park the robot on a level floor.
- Disconnect the charger before you drive (see [Power & Battery](power_and_battery.md#disconnect-the-charger-before-driving-the-mobile-base)).
- Velocity commands keep the base moving for the Control Hold Time when your program stops sending them (see [Control & System](control_and_system.md#connection-loss-and-control-hold-time)).
:::

---
## Sharp Edges Under the Mecanum Mobile Base

::: warning CAUTION
The lower inner area of the mecanum mobile base can have sharp parts. Touching them can cause cuts or puncture wounds.

- Take extra care around this area when you handle the robot.
- Wear protective gloves when you handle the robot.
:::

<img :src="$withBase('/images/saftey_and_precautions/general_safety/mecanum_wheel.png')" alt="Hand reaching under the edge of the mecanum mobile base, marked as a sharp-edge hazard area" class="center white-bg" style="width:40%">

---
## Test in Simulation Before the Real Robot

::: warning CAUTION
A program that has not been tested can move the robot in an unexpected way and hit people or objects.

- Test new motions in a simulator before you run them on the real robot.
- See [Simulators](../simulators/index.md) for installation and usage.
:::

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/saftey_and_precautions/general_safety/model_a.png')" alt="RB-Y1 Model A in the simulator" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/saftey_and_precautions/general_safety/model_m.png')" alt="RB-Y1 Model M in the simulator" class="white-bg">

</div>

</div>
