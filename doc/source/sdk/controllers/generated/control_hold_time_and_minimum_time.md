# Control Hold Time and Minimum Time
##

### Control State Transition

```{image} /_static/images/sdk/control_hold_time_and_minimum_time/robot_control_state_transitions.png
   :alt: robot_control_state_transitions.png
   :align: center
   :width: 600px
   :class: rounded-img
```

---
### Control Hold Time

Control Hold Time defines the duration for which the robot maintains the target (position/velocity) after reaching it.

Set it in the command header, for example `rby1_sdk.CommandHeaderBuilder().set_control_hold_time(0.3)` (seconds; C++: `CommandHeaderBuilder().SetControlHoldTime(0.3)`).
If it is not set, the hold time is **0 s**.

```{warning}
For velocity commands (`SE2VelocityCommand` for the mobile base and `JointVelocityCommand`), "maintaining the target" means
**the robot keeps moving at the last target velocity** for the whole Control Hold Time, and only then decelerates to a stop.
If your program stops sending commands (crash, network loss), the robot keeps moving for that time.
Keep the hold time for velocity commands short: a few times the stream period.
```

<br>

#### How It Works (Control Hold Time)

- When a control command is sent, the robot moves toward the target while considering constraints such as speed and acceleration limits.
- Once the target is reached, the robot maintains the target state for the duration of the Control Hold Time.
- After the Control Hold Time expires, the control ends, and the robot transitions to the ControlFinished state.

---
### Minimum Time

Minimum Time represents the minimum duration required for the robot to reach the target state.

<br>

#### How It Works (Minimum Time)

- Larger values: The robot reaches the target more slowly.
- Smaller values: The robot reaches the target more quickly.
- Constraints: If Minimum Time is set faster than the hardware specifications or speed/acceleration limits allow, the robot may not reach the target within that time, and the actual time to reach the target will naturally increase.

---
## Common Mistake

One common mistake is setting the Control Hold Time too short, especially in **Stream Mode**. As shown in the diagram, the control remains active only until the **ControlFinished** state is reached. If the Control Hold Time is too short and the stream cycle is too long, the stream may expire, causing the control to end prematurely.

To better understand how Control Hold Time affects each mode, let’s examine its impact:

<br>

### Once Mode

- A single control command is sent, and the robot moves toward the target.
- Once the target is reached, the robot maintains the state (position/velocity) for the duration of the Control Hold Time.

#### Impact in Once Mode

- If the Control Hold Time is too short, the robot may not maintain the target long enough to complete its intended task.
A well-configured Control Hold Time ensures the robot holds its target state as needed before transitioning to the **ControlFinished** state.

### Stream Mode

- Commands are sent continuously, allowing dynamic updates to the target while the control remains active.

#### Impact in Stream Mode

- If the Control Hold Time is too short and the stream cycle is too long, the control may prematurely transition to the **ControlFinished** state, causing the stream to expire.
- A properly configured Control Hold Time ensures the robot remains active between stream updates, preventing interruptions.

#### Examples

- If the Control Hold Time is set to 1 second, and no new input is received within **1 second**, the control transitions to the finished state.
- If the stream sends a new command every **0.1 s**, a Control Hold Time of about **0.3 s** keeps the control active between updates and tolerates a late or lost message,
  while the robot stops shortly after the stream stops.
- Do not use a long hold time (for example, tens of seconds) to keep a stream alive. With velocity commands the robot would keep moving for that long if the stream stops.