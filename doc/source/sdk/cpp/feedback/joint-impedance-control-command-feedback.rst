JointImpedanceControlCommandFeedback
====================================

``rb::JointImpedanceControlCommandFeedback`` is the leaf feedback type for
joint-space impedance commands.

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
     - Report set-point and error data for a joint-impedance command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``set_position() const``
     - Read the reference joint-position vector.
     - Useful when inspecting commanded compliance targets.
   * - ``error() const``
     - Read the current joint-space error vector.
     - Useful when diagnosing tracking quality.

.. rubric:: Returned Values & Units

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Accessor
     - Unit / encoding
     - Notes
   * - ``set_position()``
     - ``rad``
     - Joint-space setpoint vector.
   * - ``error()``
     - ``rad``
     - Per-joint position error vector.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointImpedanceControlCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-feedback`
- :doc:`torso-command-feedback`
- :doc:`body-command-feedback`

.. rubric:: Examples

- ``gravity_compensation.cpp``
