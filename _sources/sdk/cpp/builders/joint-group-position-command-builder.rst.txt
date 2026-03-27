JointGroupPositionCommandBuilder
================================

``rb::JointGroupPositionCommandBuilder`` is the subset-joint variant of the
joint-position primitive. It is most useful when the torso or another named
joint group should move without commanding the full joint vector.

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
     - Hold a joint-space target for an explicit named subset of joints.

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
   * - ``SetJointNames(...)`` and ``SetPosition(...)``
     - Define the addressed joint subset and its target positions.
     - The name order defines the value order.
   * - ``SetMinimumTime(...)``
     - Set the requested minimum execution time.
     - Useful for synchronized motion.
   * - ``SetVelocityLimit(...)`` and ``SetAccelerationLimit(...)``
     - Attach optional motion limits.
     - Useful when only a subset of joints moves.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetMinimumTime(minimum_time)``
     - ``s``
     - Minimum execution time for the subset motion.
   * - ``SetPosition(position)``
     - ``rad``
     - Per-joint target positions in the order defined by
       ``SetJointNames(...)``.
   * - ``SetVelocityLimit(velocity_limit)``
     - ``rad/s``
     - Optional per-joint velocity limits for the selected subset.
   * - ``SetAccelerationLimit(acceleration_limit)``
     - ``rad/s^2``
     - Optional per-joint acceleration limits for the selected subset.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointGroupPositionCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`torso-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
