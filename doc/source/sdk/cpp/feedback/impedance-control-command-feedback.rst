ImpedanceControlCommandFeedback
===============================

``rb::ImpedanceControlCommandFeedback`` is the leaf feedback type for the
task-space impedance command path.

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
     - Report task-space tracking error for an impedance-control command.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``TrackingError``
     - Carry the task-space tracking error.
     - Returned by the main accessor on this page.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``tracking_error() const``
     - Read the task-space tracking error record.
     - Primary diagnostic accessor for compliance tracking quality.

.. rubric:: Returned Values & Units

.. list-table::
   :header-rows: 1
   :widths: 32 18 50

   * - Accessor or field
     - Unit / encoding
     - Notes
   * - ``TrackingError::position_error``
     - ``m``
     - Translational error magnitude.
   * - ``TrackingError::rotation_error``
     - ``rad``
     - Rotational error magnitude.
   * - ``tracking_error()``
     - ``TrackingError``
     - Bundles the two task-space error magnitudes above.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::ImpedanceControlCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-feedback`
- :doc:`torso-command-feedback`

.. rubric:: Examples

- ``gravity_compensation.cpp``
