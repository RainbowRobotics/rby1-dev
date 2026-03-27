CartesianCommandBuilder
=======================

``rb::CartesianCommandBuilder`` expresses a Cartesian tracking request. It can
hold one or more task-space targets plus optional joint-position targets and
stop thresholds for tracking error.

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
     - Hold Cartesian targets and stop conditions for tracking tasks.

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
   * - ``SetMinimumTime(...)``
     - Set the requested minimum execution time.
     - Useful for time-scaled motion.
   * - ``SetStop*TrackingError(...)``
     - Set thresholds that abort on excessive tracking error.
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
     - Minimum execution time for the Cartesian motion.
   * - ``AddTarget(..., T, linear_velocity_limit, angular_velocity_limit, acceleration_limit_scaling)``
     - ``SE(3)``, ``m/s``, ``rad/s``, Dimensionless
     - ``T`` carries translation in meters. ``acceleration_limit_scaling`` is a
       normalized scaling factor with documented range ``(0, 1]``.
   * - ``AddJointPositionTarget(..., target_position, velocity_limit, acceleration_limit)``
     - ``rad``, ``rad/s``, ``rad/s^2``
     - Auxiliary joint-space posture bias and optional per-joint limits.
   * - ``SetStopPositionTrackingError(value)``
     - ``m``
     - Stop threshold on translational tracking error.
   * - ``SetStopOrientationTrackingError(value)``
     - ``rad``
     - Stop threshold on rotational tracking error.
   * - ``SetStopJointPositionTrackingError(value)``
     - ``rad``
     - Stop threshold on per-joint position tracking error.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::CartesianCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-builder`
- :doc:`torso-command-builder`
- :doc:`body-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``kinematic_calibration2.cpp``
