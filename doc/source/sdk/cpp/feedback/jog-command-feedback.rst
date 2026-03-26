JogCommandFeedback
==================

``rb::JogCommandFeedback`` is the leaf feedback type for named-joint jog
commands.

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
     - Expose the target joint name for a jog feedback leaf.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``target_joint_name() const``
     - Read the joint name associated with the jog result.
     - Useful when logs or tools handle jog requests generically.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JogCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-feedback`

.. rubric:: Examples

- ``module_test/*`` utilities are the closest reference points for jog-like
  service workflows.
