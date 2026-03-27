CartesianCommandFeedback
========================

``rb::CartesianCommandFeedback`` is the leaf feedback type for Cartesian
tracking commands.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_command_feedback.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Report tracking errors, remaining time, and manipulability for a
       Cartesian command.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``TrackingError``
     - Carry task-space tracking error data.
     - Used by the error accessor methods on this page.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``se3_pose_tracking_errors() const`` and
       ``joint_position_tracking_errors() const``
     - Read task-space and joint-space error signals.
     - Use to understand why a command stopped or slowed.
   * - ``remain_time() const``
     - Read the remaining commanded execution time.
     - Useful while tracking long motions.
   * - ``manipulability() const``
     - Read the reported manipulability value.
     - Useful for task-space feasibility inspection.

.. rubric:: Returned Values & Units

.. list-table::
   :header-rows: 1
   :widths: 32 18 50

   * - Accessor or field
     - Unit / encoding
     - Notes
   * - ``TrackingError::position_error``
     - ``m``
     - Translational task-space tracking error magnitude.
   * - ``TrackingError::orientation_error``
     - ``rad``
     - Rotational tracking error magnitude.
   * - ``se3_pose_tracking_errors()``
     - ``TrackingError`` list
     - Per-target task-space error records.
   * - ``joint_position_tracking_errors()``
     - ``rad``
     - Per-joint position tracking error magnitudes.
   * - ``remain_time()``
     - ``s``
     - Estimated remaining time to reach the target set.
   * - ``manipulability()``
     - Dimensionless
     - Python binding docs describe this as a manipulability index.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::CartesianCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-feedback`
- :doc:`torso-command-feedback`
- :doc:`body-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
