MobilityCommandFeedback
=======================

``rb::MobilityCommandFeedback`` is the feedback branch for mobility commands.
It exposes leaf feedback for joint-velocity and planar-base velocity requests.

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
     - Hold the feedback branch for one mobility command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``joint_velocity_command() const``
     - Access the joint-velocity feedback leaf.
     - Valid for wheel-joint velocity commands.
   * - ``se2_velocity_command() const``
     - Access the planar-base velocity feedback leaf.
     - Valid for SE2 base commands.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::MobilityCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`component-based-command-feedback`
- :doc:`joint-velocity-command-feedback`
- :doc:`se2-velocity-command-feedback`

.. rubric:: Examples

Examples in rby1-sdk v0.10.1 read only the top-level ``finish_code()`` of ``RobotCommandFeedback``; none reads this feedback type directly. The matching command is sent in `37_mobile_test.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/37_mobile_test.cpp>`__.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
