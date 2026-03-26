RobotCommandFeedbackParser
==========================

``rb::RobotCommandFeedbackParser`` is the low-level parser helper that fills a
``RobotCommandFeedback`` object from a lower-level message payload.

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
     - Parse the raw command-feedback message into the structured feedback tree.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``Parse(...)``
     - Populate a ``RobotCommandFeedback`` instance from a lower-level message.
     - Useful in lower-level tooling or custom protocol integration.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RobotCommandFeedbackParser
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-feedback`

.. rubric:: Examples

- ``rtcomm_protocol.cpp`` is the closest lower-level example context.
