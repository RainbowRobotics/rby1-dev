JointPositionCommandBuilder
===========================

``rb::JointPositionCommandBuilder`` is the standard joint-space point-to-point
motion primitive. It sets target position, minimum time, and optional velocity
or acceleration limits.

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
     - Hold a joint-space position target with timing and limit metadata.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetCommandHeader(...)``
     - Attach shared header metadata.
     - Uses :doc:`command-header-builder`.
   * - ``SetPosition(...)``
     - Set the target joint vector.
     - This is the main payload.
   * - ``SetMinimumTime(...)``
     - Set the requested minimum execution time.
     - Useful for time-scaling motion.
   * - ``SetVelocityLimit(...)`` and ``SetAccelerationLimit(...)``
     - Attach optional limits for the motion.
     - Adds optional per-command motion limits.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetMinimumTime(minimum_time)``
     - ``s``
     - Minimum execution time for the motion.
   * - ``SetPosition(position)``
     - ``rad``
     - Per-joint target positions.
   * - ``SetVelocityLimit(velocity_limit)``
     - ``rad/s``
     - Optional per-joint velocity limits.
   * - ``SetAccelerationLimit(acceleration_limit)``
     - ``rad/s^2``
     - Optional per-joint acceleration limits.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointPositionCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-builder`
- :doc:`torso-command-builder`
- :doc:`head-command-builder`

.. rubric:: Examples

- `00_helper.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/00_helper.cpp>`__: ``MoveJ()`` helper used by most examples.
- `23_zero_pose.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/23_zero_pose.cpp>`__: moves the body to the zero pose.
- `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__: joint position steps of the demo sequence.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
