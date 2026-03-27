RobotCommandFeedback
====================

``rb::RobotCommandFeedback`` is the root of the command-result tree returned by
the client. It exposes top-level execution status and the first branching point
for whole-body, component-based, or jog feedback.

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
     - Hold the root execution status and the top-level child feedback objects.

.. rubric:: Member Types / Enums

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``Status``
     - High-level execution status.
     - Check while polling or after completion.
   * - ``FinishCode``
     - Final completion code.
     - Read this before drilling into branch-specific details.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``status() const`` and ``finish_code() const``
     - Read the top-level execution status and final code.
     - These are the first fields most client code checks.
   * - ``whole_body_command() const``
     - Access the whole-body branch.
     - Valid when the submitted command took the whole-body path.
   * - ``component_based_command() const``
     - Access the component-based branch.
     - Valid when body, head, or mobility commands were composed.
   * - ``jog_command() const``
     - Access the jog branch.
     - Valid when the top-level command was a named-joint jog.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RobotCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`whole-body-command-feedback`
- :doc:`component-based-command-feedback`
- :doc:`jog-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``stop_command.cpp``
