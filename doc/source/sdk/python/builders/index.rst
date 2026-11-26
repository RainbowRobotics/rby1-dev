Robot Command Builders
======================

.. currentmodule:: rby1_sdk

Builders compose command payloads. Start here when you need to assemble
structured commands for body, arm, head, torso, mobility, or whole-body control.

.. rubric:: How builders nest

``Robot_*.send_command()`` and the command stream take a
``RobotCommandBuilder``. It holds one of three command paths:

.. code-block:: text

   RobotCommandBuilder
   ├── ComponentBasedCommandBuilder      (one command per component)
   │   ├── set_body_command(...)         BodyCommandBuilder, or any body-capable builder,
   │   │   │                             or BodyComponentBasedCommandBuilder:
   │   │   ├── set_torso_command(...)     TorsoCommandBuilder or a torso-capable builder
   │   │   ├── set_right_arm_command(...) ArmCommandBuilder or an arm-capable builder
   │   │   └── set_left_arm_command(...)  ArmCommandBuilder or an arm-capable builder
   │   ├── set_mobility_command(...)     MobilityCommandBuilder, SE2VelocityCommandBuilder
   │   │                                 or JointVelocityCommandBuilder
   │   └── set_head_command(...)         HeadCommandBuilder or JointPositionCommandBuilder
   ├── WholeBodyCommandBuilder           (StopCommandBuilder)
   └── JogCommandBuilder

Pass a leaf builder (``JointPositionCommandBuilder``, ``CartesianCommandBuilder``,
``JointImpedanceControlCommandBuilder``, ...) directly where the tree accepts
it; the SDK converts it to the intermediate builder (``ArmCommandBuilder``,
``TorsoCommandBuilder``, ``BodyCommandBuilder``, ``MobilityCommandBuilder``,
``HeadCommandBuilder``). The example below is shortened from ``movej()`` in
``examples/python/00_helper.py``:

.. code-block:: python

   body = (rby.BodyComponentBasedCommandBuilder()
           .set_torso_command(rby.JointPositionCommandBuilder().set_minimum_time(5).set_position(torso))
           .set_right_arm_command(rby.JointPositionCommandBuilder().set_minimum_time(5).set_position(right_arm)))
   robot.send_command(
       rby.RobotCommandBuilder().set_command(
           rby.ComponentBasedCommandBuilder().set_body_command(body)), 1).get()

.. rubric:: Two impedance builders

- ``ImpedanceControlCommandBuilder``: impedance in task space. The robot
  computes a wrench from the 6D pose error of one link
  (``set_translation_weight``, ``set_rotation_weight``).
- ``CartesianImpedanceControlCommandBuilder``: takes Cartesian pose targets,
  solves for joint targets first (optimal control / inverse kinematics), then
  tracks them with joint-space impedance (``set_joint_stiffness``, damping
  ratio, torque limit).

.. rubric:: All builders

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   RobotCommandBuilder
   CommandHeaderBuilder
   WholeBodyCommandBuilder
   ComponentBasedCommandBuilder
   HeadCommandBuilder
   MobilityCommandBuilder
   BodyCommandBuilder
   BodyComponentBasedCommandBuilder
   TorsoCommandBuilder
   ArmCommandBuilder
   StopCommandBuilder
   SE2VelocityCommandBuilder
   JogCommandBuilder
   JointVelocityCommandBuilder
   ImpedanceControlCommandBuilder
   CartesianImpedanceControlCommandBuilder
   CartesianCommandBuilder
   GravityCompensationCommandBuilder
   OptimalControlCommandBuilder
   JointImpedanceControlCommandBuilder
   JointGroupPositionCommandBuilder
   JointPositionCommandBuilder
