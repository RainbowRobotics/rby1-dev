# Command and Control Architecture

### Overview

A robot command (`RobotCommandBuilder`) holds exactly one of three command types:

1. **WholeBodyCommand**: stops the robot or runs real-time control. It does not hold motion controllers.
2. **ComponentBasedCommand**: sends commands to the `mobility`, `body` and `head` components. Each component gets its own controller.
3. **JogCommand**: moves one joint by a small step, typically used for fine adjustments.

All values are in SI units (rad, rad/s, m, N·m). See [Units and Frames](../../../software/units-and-frames.md).

<img :src="$withBase('/images/sdk/command_and_control_architecture/mermaid_robot_command.png')" alt="mermaid_robot_command" class="center rounded-img" style="width:600px">

---
### WholeBodyCommand

A WholeBodyCommand holds one of two commands:

- **StopCommand** (`StopCommandBuilder`): stops the running commands and holds the robot.
- **RealTimeControlCommand**: starts real-time control, in which your program sends joint targets and torques over UDP every 2 ms.
  The SDK sends this command for you when you call `robot.control(callback)`; see the C++ [control loop types](../../cpp/client/control-loop-types.md).

It applies to all joints of the model: 24 for Model A, 26 for Model M and 18 for Model UB.

---
### ComponentBasedCommand

The **ComponentBasedCommand** controls the components of the robot separately: **Mobility** (wheels), **Body** (torso and both arms) and **Head**.
Set only the components you want to move.

<img :src="$withBase('/images/sdk/command_and_control_architecture/mermaid_component_based.png')" alt="mermaid_component_based" class="center rounded-img" style="width:600px">

---
### BodyCommand Structure

The **BodyCommand** either controls the whole body (torso and both arms) with one controller, or holds a **BodyComponentBasedCommand**.
The BodyComponentBasedCommand has a **TorsoCommand**, a **RightArmCommand** and a **LeftArmCommand**, each with its own controller.

<img :src="$withBase('/images/sdk/command_and_control_architecture/mermaid_body_component.png')" alt="mermaid_body_component" class="center rounded-img" style="width:600px">

---
### Controllers

The table shows which controller (command) each component accepts. The Python builder of each command has the same name with `Builder` added,
for example `JointPositionCommandBuilder`.

| Command | Mobility | Body | Torso | Right / left arm | Head |
| --- | :-: | :-: | :-: | :-: | :-: |
| `JointPositionCommand` | | ✓ | ✓ | ✓ | ✓ |
| `JointGroupPositionCommand` | | | ✓ | | |
| `JointVelocityCommand` | ✓ | | | | |
| `SE2VelocityCommand` | ✓ | | | | |
| `CartesianCommand` | | ✓ | ✓ | ✓ | |
| `ImpedanceControlCommand` | | | ✓ | ✓ | |
| `JointImpedanceControlCommand` | | ✓ | ✓ | ✓ | |
| `CartesianImpedanceControlCommand` | | ✓ | ✓ | ✓ | |
| `GravityCompensationCommand` | | ✓ | ✓ | ✓ | |
| `OptimalControlCommand` | | ✓ | ✓ | | |

- **JointPositionCommand**: moves joints to target positions.
- **JointGroupPositionCommand**: moves the joints you list by name to target positions.
- **JointVelocityCommand**, **SE2VelocityCommand**: drive the wheels by joint velocity, or the base by a planar velocity (x, y, yaw).
- **CartesianCommand**: moves links to target poses.
- **ImpedanceControlCommand**, **CartesianImpedanceControlCommand**, **JointImpedanceControlCommand**: control motion with a stiffness, so the robot yields to contact.
- **GravityCompensationCommand**: compensates for gravity, so the joints can be moved by hand.
- **OptimalControlCommand**: solves an optimization problem for link poses, the center of mass and joint positions (below).

#### Optimal control

The robot software computes the joint velocity $\dot{\mathbf{q}}$ that minimizes a weighted sum of squared errors every control cycle:

$$
\min_{\dot{\mathbf{q}}}\;
\sum_{i=0}^{n-1}\left\lVert W_{1,i}\left(J_i\dot{\mathbf{q}}-\log\left(T^{-1}_{i,\text{cur}}T_{i,\text{ref}}\right)\right)\right\rVert^2
+ \left\lVert W_2\left(\dot{\mathbf{q}}-(\mathbf{q}_{\text{ref}}-\mathbf{q}_{\text{cur}})\right)\right\rVert^2
+ \left\lVert W_3\,\dot{\mathbf{q}}\right\rVert^2
$$

subject to the joint velocity limits

$$
\dot{\mathbf{q}}_{lb}\le\dot{\mathbf{q}}\le\dot{\mathbf{q}}_{ub}
$$

with

$$
W_{1,i} = \mathrm{diag}(w_{o,i},w_{o,i},w_{o,i},w_{p,i},w_{p,i},w_{p,i}),\qquad
W_{2} = \mathrm{diag}(w_{0},w_{1},\cdots,w_{dof-1})
$$

- $T_{i,\text{ref}}$ is a Cartesian target (`add_cartesian_target(ref_link, link, T, translation_weight, rotation_weight)`), $w_{o,i}$ and $w_{p,i}$ its rotation and translation weights.
- $\mathbf{q}_{\text{ref}}$ and $w_j$ are joint position targets and weights (`add_joint_position_target(joint_name, q, weight)`).
- A center-of-mass target (`set_center_of_mass_target`) adds a term of the same form.
- $W_3$ is a small fixed weight that keeps the solution small in the joint space.

The formula above is a simplified form; the robot software also scales the errors with `set_error_scaling()` and the control period.

**When the command ends.** The cost is the size of the remaining target error. The command converges when

- the cost is below the stop cost (`set_stop_cost()`, default from the parameter
  [`default.optimal_control_command.stop_cost`](parameter.md#defaultoptimal_control_commandstop_cost)), or
- the smoothed cost changes by less than `set_min_delta_cost()` in `set_patience()` consecutive control cycles
  (only when you set a minimum delta cost; without a patience value, the first such cycle ends the command).

See the SDK example `24_demo_motion.py` for weights and limits that work on the robot.

---
### Example

The example below moves the torso and both arms with joint position commands.
It is written for Model A and Model M (a 6-joint torso); on Model UB the torso has 2 joints.
The complete demo with more commands is the SDK example `24_demo_motion.py` ([Examples](../../../examples/ex.md)).

::: danger WARNING
This program powers on the robot, turns on the servos and moves the torso and both arms.
Clear the robot's full range of motion of people and objects, and keep the E-Stop within reach.
Try it in the [simulator](../../../simulators/index.md) first.
:::

```python
import numpy as np
import rby1_sdk as rby

ADDRESS = "192.168.30.1:50051"  # your robot address
MODEL = "a"                     # "a" or "m"
D2R = np.pi / 180               # degrees to radians
MINIMUM_TIME = 2.0              # seconds

robot = rby.create_robot(ADDRESS, MODEL)
if not robot.connect():
    raise SystemExit("Cannot connect to the robot")
if not robot.is_power_on(".*"):
    robot.power_on(".*")
if not robot.is_servo_on(".*"):
    robot.servo_on(".*")
if robot.get_control_manager_state().state in (
    rby.ControlManagerState.State.MinorFault,
    rby.ControlManagerState.State.MajorFault,
):
    robot.reset_fault_control_manager()
if not robot.enable_control_manager():
    raise SystemExit("Cannot enable the Control Manager")

model = robot.model()
torso = np.array([0, 30, -60, 30, 0, 0]) * D2R           # len(model.torso_idx) == 6
right_arm = np.array([-45, -30, 0, -90, 0, 45, 0]) * D2R  # len(model.right_arm_idx) == 7
left_arm = np.array([-45, 30, 0, -90, 0, 45, 0]) * D2R    # len(model.left_arm_idx) == 7

rc = rby.RobotCommandBuilder().set_command(
    rby.ComponentBasedCommandBuilder().set_body_command(
        rby.BodyComponentBasedCommandBuilder()
        .set_torso_command(
            rby.JointPositionCommandBuilder().set_minimum_time(MINIMUM_TIME).set_position(torso)
        )
        .set_right_arm_command(
            rby.JointPositionCommandBuilder().set_minimum_time(MINIMUM_TIME).set_position(right_arm)
        )
        .set_left_arm_command(
            rby.JointPositionCommandBuilder().set_minimum_time(MINIMUM_TIME).set_position(left_arm)
        )
    )
)

feedback = robot.send_command(rc, 10).get()  # 10 is the command priority
if feedback.finish_code != rby.RobotCommandFeedback.FinishCode.Ok:
    print("Motion failed:", feedback.finish_code)
```

To send all body joints in one command, use `BodyCommandBuilder().set_command(JointPositionCommandBuilder().set_position(q))`
with `q` of length `len(model.body_idx)` (20 for Model A and M, 16 for Model UB), in index order.

---

Verified against: rby1-sdk v0.10.1 `protos/rb/api/robot_command.proto`, `whole_body_command.proto` (only `stop_command` and `real_time_control_command`),
`component_based_command.proto`, `body_command.proto`, `body_component_based_command.proto`, `torso_command.proto`, `arm_command.proto`,
`head_command.proto`, `mobility_command.proto` (controllers per component), `include/rby1-sdk/model.h` (DOF and indexes),
`include/rby1-sdk/math/optimal_control.h` (cost terms), `include/rby1-sdk/robot_command_builder.h` (`OptimalControlCommandBuilder`),
`python/robot_command_builder.cpp`, `examples/python/00_helper.py`, `examples/python/24_demo_motion.py`;
robot core `core/service/srv_optimal_control_command.cpp` (convergence check).
