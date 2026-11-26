RobotCommandBuilder
===================

``rb::RobotCommandBuilder`` is the outermost command envelope passed into
``Robot::SendCommand()`` and ``RobotCommandStreamHandler::SendCommand()``. It
wraps one top-level command path: whole-body, component-based, or jog.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_command_builder.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Hold the top-level command tree submitted through the client.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``RobotCommandBuilder()`` and converting constructors
     - Construct the envelope directly from one top-level builder.
     - Supports whole-body, component-based, and jog paths.
   * - ``SetCommand(...)``
     - Replace the active top-level command.
     - Use before submission if the envelope is reused.

.. rubric:: Building a Command

Builders nest. A body joint position command is wrapped as
``RobotCommandBuilder`` → ``ComponentBasedCommandBuilder`` → body command.
To command parts of the body separately, use
``BodyComponentBasedCommandBuilder`` for the body command; each part then
takes its own builder. The snippet below is shortened from
``examples/cpp/00_helper.cpp`` (``MoveJ()``). ``torso``, ``right_arm`` and
``left_arm`` are ``Eigen::VectorXd`` joint positions in ``rad`` (6 or 2 torso
values depending on the model, 7 per arm).

.. code-block:: cpp

   using namespace rb;

   auto body = BodyComponentBasedCommandBuilder()
       .SetTorsoCommand(JointPositionCommandBuilder().SetMinimumTime(5.0).SetPosition(torso))
       .SetRightArmCommand(JointPositionCommandBuilder().SetMinimumTime(5.0).SetPosition(right_arm))
       .SetLeftArmCommand(JointPositionCommandBuilder().SetMinimumTime(5.0).SetPosition(left_arm));

   auto handler = robot->SendCommand(
       RobotCommandBuilder().SetCommand(ComponentBasedCommandBuilder().SetBodyCommand(body)),
       1 /* priority */);
   const auto feedback = handler->Get();

The intermediate types (``TorsoCommandBuilder``, ``ArmCommandBuilder``,
``BodyCommandBuilder``) are created implicitly from the builder you pass.

.. warning::

   Sending a command moves the robot. Clear the area around the robot and keep
   the E-Stop within reach.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RobotCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`whole-body-command-builder`
- :doc:`component-based-command-builder`
- :doc:`jog-command-builder`

.. rubric:: Examples

- `23_zero_pose.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/23_zero_pose.cpp>`__: one component-based command sent with ``SendCommand()``.
- `31_multi_controls.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/31_multi_controls.cpp>`__: overlapping commands sent with different priorities.
- `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__: many command types in sequence.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
