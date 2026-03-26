BodyCommandFeedback
===================

``rb::BodyCommandFeedback`` is the body-scoped branch of the feedback tree. It
matches the body-level command modes available under ``BodyCommandBuilder``.

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
     - Hold the body branch of the feedback tree and expose the active leaf.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``body_component_based_command() const``
     - Access the split torso-and-arms subtree.
     - Valid when the body command was decomposed.
   * - ``joint_position_command() const``, ``cartesian_command() const``,
       ``cartesian_impedance_control_command() const``
     - Access the main body motion leaves.
     - Use the accessor that matches the body command mode.
   * - ``joint_impedance_control_command() const``,
       ``gravity_compensation_command() const``,
       ``optimal_control_command() const``
     - Access the remaining body command leaves.
     - Covers compliance, compensation, and optimization paths.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::BodyCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`component-based-command-feedback`
- :doc:`body-component-based-command-feedback`
- :doc:`cartesian-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``optimal_control.cpp``
