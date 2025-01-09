---
title: Control Hold Time and Minimum Time
outline: deep
---
# Control Hold Time and Minimum Time

## Control State Transition
<figure>
    <img src="/images/robot-control-state-transitions.png" alt="missing" />
</figure>

## Control Hold Time
Control Hold Time defines the duration for which the robot maintains the target (position/velocity) after reaching it.
### How It Works
- When a control command is sent, the robot moves toward the target while considering constraints such as speed and acceleration limits.
- Once the target is reached, the robot maintains the target state for the duration of the Control Hold Time. 
- After the Control Hold Time expires, the control ends, and the robot transitions to the ControlFinished state.

## Minimum Time
Minimum Time represents the minimum duration required for the robot to reach the target state.
### How It Works
- Larger values: The robot reaches the target more slowly.
- Smaller values: The robot reaches the target more quickly.
- Constraints: If Minimum Time is set faster than the hardware specifications or speed/acceleration limits allow, the robot may not reach the target within that time, and the actual time to reach the target will naturally increase.

## Common Mistake
One common mistake is setting the Control Hold Time too short, especially in **Stream Mode**. As shown in the diagram, the control remains active only until the **ControlFinished** state is reached. If the Control Hold Time is too short and the stream cycle is too long, the stream may expire, causing the control to end prematurely.

To better understand how Control Hold Time affects each mode, let’s examine its impact:

### Once Mode
- A single control command is sent, and the robot moves toward the target.
- Once the target is reached, the robot maintains the state (position/velocity) for the duration of the Control Hold Time.
#### Impact
- If the Control Hold Time is too short, the robot may not maintain the target long enough to complete its intended task.
- A well-configured Control Hold Time ensures the robot holds its target state as needed before transitioning to the **ControlFinished** state.

### Stream Mode
- Commands are sent continuously, allowing dynamic updates to the target while the control remains active.  
#### Impact
- If the Control Hold Time is too short and the stream cycle is too long, the control may prematurely transition to the **ControlFinished** state, causing the stream to expire.
- A properly configured Control Hold Time ensures the robot remains active between stream updates, preventing interruptions.

#### Examples
- If the Control Hold Time is set to **1 second**, and no new input is received within 1 second, the control transitions to the finished state.
- If the Control Hold Time is set to **100 seconds**, and the stream cycle operates every 1 second, the target can be updated dynamically, maintaining continuous control.
