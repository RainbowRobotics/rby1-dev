BodyComponentBasedCommandFeedback
=================================

``rb::BodyComponentBasedCommandFeedback`` is the split body branch that exposes
independent feedback for the left arm, right arm, and torso.

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
     - Hold the split torso-and-arms body feedback branch.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``left_arm_command() const``
     - Access the left-arm feedback subtree.
     - Valid when the split body command addressed the left arm.
   * - ``right_arm_command() const``
     - Access the right-arm feedback subtree.
     - Valid when the split body command addressed the right arm.
   * - ``torso_command() const``
     - Access the torso feedback subtree.
     - Valid when the split body command addressed the torso.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::BodyComponentBasedCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`body-command-feedback`
- :doc:`arm-command-feedback`
- :doc:`torso-command-feedback`

.. rubric:: Examples

Examples in rby1-sdk v0.10.1 read only the top-level ``finish_code()`` of ``RobotCommandFeedback``; none reads this feedback type directly. The matching command is sent in `23_zero_pose.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/23_zero_pose.cpp>`__, `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
