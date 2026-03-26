JointImpedanceControlCommandBuilder
===================================

``rb::JointImpedanceControlCommandBuilder`` expresses joint-space impedance
control. It adds stiffness, damping, and torque limits around a joint-position
target.

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
     - Hold a joint-space impedance-control request.

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
     - This is the nominal reference trajectory.
   * - ``SetStiffness(...)``, ``SetDampingRatio(...)``, ``SetTorqueLimit(...)``
     - Configure the impedance behavior.
     - These shape the compliance response.
   * - ``SetMinimumTime(...)``, ``SetVelocityLimit(...)``,
       ``SetAccelerationLimit(...)``
     - Attach timing and motion limits.
     - Useful for bounded transients.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 32 18 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetMinimumTime(minimum_time)``
     - ``s``
     - Minimum execution time.
   * - ``SetPosition(position)``
     - ``rad``
     - Joint-space target position vector.
   * - ``SetVelocityLimit(velocity_limit)``
     - ``rad/s``
     - Per-joint velocity limits.
   * - ``SetAccelerationLimit(acceleration_limit)``
     - ``rad/s^2``
     - Per-joint acceleration limits.
   * - ``SetStiffness(stiffness)``
     - ``Nm/rad``
     - Diagonal joint-space stiffness values.
   * - ``SetTorqueLimit(torque_limit)``
     - ``Nm``
     - Per-joint torque saturation limits.
   * - ``SetDampingRatio(damping_ratio)``
     - Dimensionless
     - Ratio used to derive the damping matrix.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointImpedanceControlCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-builder`
- :doc:`torso-command-builder`
- :doc:`body-command-builder`

.. rubric:: Examples

- ``gravity_compensation.cpp``
