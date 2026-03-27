RobotCommandBuilder
===================

``rb::RobotCommandBuilder`` is the outermost command envelope passed into
``Robot::SendCommand()`` and ``RobotCommandStreamHandler::SendCommand()``. It
wraps one top-level command path: whole-body, component-based, or jog.

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
     - Hold the top-level command tree submitted through the client.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``RobotCommandBuilder()`` and converting constructors
     - Construct the envelope directly from one top-level builder.
     - Supports whole-body, component-based, and jog paths.
   * - ``SetCommand(...)``
     - Replace the active top-level command.
     - Use before submission if the envelope is reused.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RobotCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`whole-body-command-builder`
- :doc:`component-based-command-builder`
- :doc:`jog-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``stop_command.cpp``
