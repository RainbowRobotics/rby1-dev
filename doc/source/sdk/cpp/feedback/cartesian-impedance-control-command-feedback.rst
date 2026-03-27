CartesianImpedanceControlCommandFeedback
========================================

``rb::CartesianImpedanceControlCommandFeedback`` is the leaf feedback type for
Cartesian impedance requests.

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
     - Report set-point, remaining time, and manipulability for a Cartesian
       impedance command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``set_position() const``
     - Read the current set-position reference.
     - Useful when analyzing the commanded impedance target.
   * - ``remain_time() const``
     - Read the remaining commanded execution time.
     - Useful while tracking long motions.
   * - ``manipulability() const``
     - Read the reported manipulability value.
     - Useful for task-space feasibility inspection.

.. rubric:: Returned Values & Units

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Accessor
     - Unit / encoding
     - Notes
   * - ``set_position()``
     - ``rad``
     - Joint-space setpoint vector used by the internal controller.
   * - ``remain_time()``
     - ``s``
     - Estimated remaining settling time.
   * - ``manipulability()``
     - Dimensionless
     - Manipulability index from the Cartesian impedance path.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::CartesianImpedanceControlCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-feedback`
- :doc:`torso-command-feedback`

.. rubric:: Examples

- ``gravity_compensation.cpp``
