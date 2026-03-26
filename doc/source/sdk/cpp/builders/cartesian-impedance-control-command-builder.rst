CartesianImpedanceControlCommandBuilder
=======================================

``rb::CartesianImpedanceControlCommandBuilder`` is the most feature-rich
task-space compliance primitive. It extends the Cartesian command path with
joint limits, joint stiffness, nullspace targets, and reset behavior.

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
     - Hold a Cartesian impedance request with richer task and nullspace data.

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
   * - ``AddTarget(...)`` and ``AddJointPositionTarget(...)``
     - Add task-space and optional joint-space targets.
     - ``AddTarget(...)`` is the main task-space API.
   * - ``AddJointLimit(...)``, ``SetJointStiffness(...)``,
       ``SetJointDampingRatio(...)``, ``SetJointTorqueLimit(...)``
     - Configure nullspace and impedance terms.
     - These are the main additions over ``CartesianCommandBuilder``.
   * - ``SetNullspaceJointTarget(...)`` and ``SetResetReference(...)``
     - Control nullspace bias and reference reset behavior.
     - Useful in long-running Cartesian tasks.
   * - ``SetMinimumTime(...)`` and ``SetStop*TrackingError(...)``
     - Set time and stop thresholds.
     - Covers position, orientation, and joint-position errors.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 34 18 48

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetMinimumTime(minimum_time)``
     - ``s``
     - Minimum execution time.
   * - ``AddTarget(..., T, linear_velocity_limit, angular_velocity_limit, linear_acceleration_limit, angular_acceleration_limit)``
     - ``SE(3)``, ``m/s``, ``rad/s``, ``m/s^2``, ``rad/s^2``
     - ``T`` carries translation in meters. Velocity and acceleration limits are
       internal solver bounds.
   * - ``AddJointPositionTarget(..., target_position, velocity_limit, acceleration_limit)``
     - ``rad``, ``rad/s``, ``rad/s^2``
     - Auxiliary joint target used by the optimization stage.
   * - ``SetNullspaceJointTarget(target_position, weight, k_p, k_d, cost_weight)``
     - ``rad``, Dimensionless, Not specified
     - ``target_position`` is joint-space. ``weight`` and ``cost_weight`` are
       optimization weights. Public docs do not assign units to ``k_p`` or
       ``k_d``.
   * - ``SetStopPositionTrackingError(value)``
     - ``m``
     - Stop threshold on translational error.
   * - ``SetStopOrientationTrackingError(value)``
     - ``rad``
     - Stop threshold on rotational error.
   * - ``SetStopJointPositionTrackingError(value)``
     - ``rad``
     - Stop threshold on joint-position error.
   * - ``SetJointStiffness(stiffness)``
     - ``Nm/rad``
     - Per-joint stiffness values.
   * - ``SetJointTorqueLimit(torque_limit)``
     - ``Nm``
     - Per-joint torque saturation values.
   * - ``SetJointDampingRatio(damping_ratio)``
     - Dimensionless
     - Joint damping ratio used to derive the damping matrix.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::CartesianImpedanceControlCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-builder`
- :doc:`torso-command-builder`
- :doc:`impedance-control-command-builder`

.. rubric:: Examples

- ``gravity_compensation.cpp``
