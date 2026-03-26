ArmCommandFeedback
==================

``rb::ArmCommandFeedback`` exposes the leaf feedback object for the active
arm-scoped command mode.

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
     - Hold the feedback branch for one arm command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``joint_position_command() const``
     - Access the joint-position feedback leaf.
     - Valid for point-to-point arm motion.
   * - ``cartesian_command() const`` and
       ``cartesian_impedance_control_command() const``
     - Access task-space tracking or impedance feedback.
     - Use the accessor matching the submitted primitive.
   * - ``impedance_control_command() const``,
       ``joint_impedance_control_command() const``,
       ``gravity_compensation_command() const``
     - Access the remaining arm feedback leaves.
     - Covers compliance and compensation paths.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::ArmCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`body-component-based-command-feedback`
- :doc:`joint-position-command-feedback`
- :doc:`cartesian-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``gravity_compensation.cpp``
