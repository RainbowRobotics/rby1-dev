JointVelocityCommandBuilder
===========================

``rb::JointVelocityCommandBuilder`` is the joint-space velocity primitive for
mobility or other velocity-mode command paths.

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
     - Hold a joint-velocity target plus optional timing and acceleration data.

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
   * - ``SetVelocity(...)``
     - Set the target joint velocity vector.
     - This is the main payload.
   * - ``SetMinimumTime(...)`` and ``SetAccelerationLimit(...)``
     - Set timing and acceleration limits.
     - Useful for smooth velocity transitions.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetMinimumTime(minimum_time)``
     - ``s``
     - Minimum ramp duration toward the target velocity.
   * - ``SetVelocity(velocity)``
     - ``rad/s``
     - Per-joint target velocities.
   * - ``SetAccelerationLimit(acceleration_limit)``
     - ``rad/s^2``
     - Per-joint acceleration limits for the ramp.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointVelocityCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`mobility-command-builder`
- :doc:`se2-velocity-command-builder`

.. rubric:: Examples

- ``mobility_command.cpp``
