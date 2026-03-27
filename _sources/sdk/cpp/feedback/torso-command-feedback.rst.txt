TorsoCommandFeedback
====================

``rb::TorsoCommandFeedback`` exposes the leaf feedback object for the active
torso-scoped command mode.

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
     - Hold the feedback branch for one torso command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``joint_position_command() const`` and
       ``joint_group_position_command() const``
     - Access joint-space torso feedback.
     - Use the accessor matching the submitted primitive.
   * - ``cartesian_command() const`` and
       ``cartesian_impedance_control_command() const``
     - Access task-space torso feedback.
     - Valid when the torso was driven in Cartesian space.
   * - ``impedance_control_command() const``,
       ``joint_impedance_control_command() const``,
       ``gravity_compensation_command() const``,
       ``optimal_control_command() const``
     - Access the remaining torso leaves.
     - Covers compliance, compensation, and optimization paths.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::TorsoCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`body-component-based-command-feedback`
- :doc:`joint-group-position-command-feedback`
- :doc:`optimal-control-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``optimal_control.cpp``
