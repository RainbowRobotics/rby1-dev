# Command Streams

Continuous control goes over the driver's command streams: `stream_joint`, `stream_cartesian`, `cmd_vel` and `follow_joint_trajectory`.
The driver has **five channels**, one per part: `right_arm`, `left_arm`, `torso`, `head` and `mobile`.
Each channel is its own SDK command stream, so one part keeps moving while another is commanded (for example, head commands during an arm trajectory).

## Open and close channels

`stream_control` opens and closes channels by name. Name the channels you will command, comma-separated. Empty or `all` means every channel.

```bash
ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: true, parameters: 'right_arm, left_arm, head'}"
ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: true}"                          # every channel
ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: false, parameters: 'head'}"     # the arm channels stay open
ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: false}"                         # every channel
```

The answer lists what happened, for example `Stream channels opened: right_arm, left_arm; already open: head.`
An unknown channel name is refused.

## Rules

- **Opening holds the part.** The first command on a body channel just opened is the driver's own: the part is held where it is measured.
  The `mobile` channel gets no such command. A channel whose servo is off cannot be opened; the call then fails and opens nothing.
- **Not during gravity compensation.** Opening is refused while gravity compensation is on (`Failed to activate stream control: Gravity compensation is active.`).
- **A command needs its channel.** With any channel open, a command for a part whose channel is closed is refused, and the answer names the channel to open.
  This applies to trajectories, `robot_joint` / `robot_cartesian` and `stream_joint` / `stream_cartesian` alike.
  A trajectory uses the channels of the parts it names: a right-arm trajectory needs `right_arm` only.
  With no channel open at all, the stream commands are refused (`Stream is not active`).
- **`cmd_vel` needs the `mobile` channel.** `cmd_vel` is a topic, so there is no answer. Without an open `mobile` channel the driver ignores each message and logs `cmd_vel received but stream channel 'mobile' is not open` (at most once per second).
- **A commanded channel stays open.** A channel that got no command within 60 s of being opened is closed again with `[STREAM TIMEOUT]`.
  A channel that was commanded once stays open until `stream_control` closes it, or until `cancel_control`, a fault, power off or servo off closes it.
  Its last command holds its part (control hold time 1e6 s) until then.
- **Reopen gap.** `stream_control` waits until 0.3 s have passed since a stream was last closed, because a stream opened right after closing one takes commands the robot ignores.
- **`cmd_vel`.** Each message is carried out for 1.1 × 1/`stream_command_hz` (about 37 ms at 30 Hz), with a control hold time of 1 s. See the warning in [Topics](topics.md#subscribers).

::: warning A stopped client leaves its channels open
If a streaming node is killed, the channels it opened stay open, and the last command keeps holding each part.
Other command sources are refused until the channels are closed:
```bash
ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: false}"
```
:::

## Trajectories (`follow_joint_trajectory`)

- Trajectories run per part. Trajectories on different parts run at the same time.
- A trajectory that names a part already running **replaces** that part's trajectory (`Preempted by a new trajectory on the same part`).
- A cancel stops the channels of the parts it names and no other.
- A trajectory is **refused, and every running trajectory is stopped**, when it is invalid: no points, a part whose channel is closed,
  or a first waypoint that a joint cannot reach in its time within its velocity limit. The stopped parts hold their last waypoint.
- If three waypoints in a row cannot be sent, the goal is aborted.

## `stream_cartesian`

The driver solves the joints for each target with the SDK's IK and streams them.
A step that needs more than a joint's acceleration limit within `minimum_time` is refused (`[STREAM REJECTED] ... exceeds limit`) **and stops the arm** where it is measured; the channel stays open.
Stream small steps from where the arm is.

Verified against: rby1-ros2 v1.0.0 `rby1_driver/src/control_stream.cpp`, `rby1_driver/include/default_parameters.hpp`, `Doc/manual/02_driver.md` (Command streams).
