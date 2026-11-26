RealtimeControlCommandFeedback
==============================

``rb::RealtimeControlCommandFeedback`` is the leaf feedback type for the
real-time control bootstrap request.

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
     - Mark the leaf result for the real-time control bootstrap command.

.. rubric:: Public Member Functions

- No type-specific methods are added at this leaf. Use the inherited validity
  and completion checks from the base feedback classes.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RealtimeControlCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`whole-body-command-feedback`

.. rubric:: Examples

Examples in rby1-sdk v0.10.1 read only the top-level ``finish_code()`` of ``RobotCommandFeedback``; none reads this feedback type directly. The matching command is sent in `34_real_time_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp>`__.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
