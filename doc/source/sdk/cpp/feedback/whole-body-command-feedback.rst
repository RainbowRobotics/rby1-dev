WholeBodyCommandFeedback
========================

``rb::WholeBodyCommandFeedback`` is the feedback branch for whole-body commands.
It exposes the leaf feedback for stop requests and real-time bootstrap
requests.

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
     - Hold the whole-body branch of the feedback tree.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``stop_command() const``
     - Access the leaf feedback for stop requests.
     - Valid when the whole-body command was a stop.
   * - ``realtime_control_command() const``
     - Access the leaf feedback for real-time bootstrap requests.
     - Valid when the whole-body command opened the RT path.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::WholeBodyCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-feedback`
- :doc:`stop-command-feedback`
- :doc:`realtime-control-command-feedback`

.. rubric:: Examples

Examples in rby1-sdk v0.10.1 read only the top-level ``finish_code()`` of ``RobotCommandFeedback``; none reads this feedback type directly. The matching command is sent in `34_real_time_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp>`__.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
