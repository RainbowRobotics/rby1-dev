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

- ``mobility_command.cpp``
