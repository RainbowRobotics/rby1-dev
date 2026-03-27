CommandHeaderFeedback
=====================

``rb::CommandHeaderFeedback`` adds header-level completion data on top of the
base feedback type. It sits beneath every command-feedback branch.

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
     - Provide the shared ``finished()`` flag for all command feedback objects.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``finished() const``
     - Check whether the associated command header reached completion.
     - This is a coarse completion signal shared by derived feedback types.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::CommandHeaderFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`feedback`
- :doc:`command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
