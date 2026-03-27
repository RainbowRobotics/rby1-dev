Feedback
========

``rb::Feedback`` is the smallest common base for the command-feedback tree. It
mainly provides the validity flag used by all derived feedback objects.

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
     - Provide shared validity semantics for the feedback hierarchy.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``valid() const``
     - Check whether the feedback object contains a valid parsed payload.
     - Use this before drilling into child accessors on derived classes.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::Feedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`command-feedback`
- :doc:`robot-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp`` and ``stop_command.cpp`` are the natural places where the
  feedback tree eventually appears.
