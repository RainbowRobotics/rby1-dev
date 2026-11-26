WholeBodyCommandBuilder
=======================

``rb::WholeBodyCommandBuilder`` selects a whole-robot command mode. It is the
compact path used for stop commands and for bootstrapping the real-time control
channel.

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
     - Hold one whole-body command beneath ``RobotCommandBuilder``.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - converting constructors
     - Construct directly from ``StopCommandBuilder`` or
       ``RealTimeControlCommandBuilder``.
     - The whole-body path only supports these two primitive modes.
   * - ``SetCommand(...)``
     - Replace the active whole-body primitive.
     - Reconfigure an existing builder instance.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::WholeBodyCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-builder`
- :doc:`stop-command-builder`
- :doc:`real-time-control-command-builder`

.. rubric:: Examples

No C++ example in rby1-sdk v0.10.1 uses this builder directly. ``Robot::Control()`` sends a whole-body real-time control command internally; see `34_real_time_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp>`__.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
