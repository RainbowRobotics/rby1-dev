CommandFeedback
===============

``rb::CommandFeedback`` is the shared base for every command result object. It
provides access to the header feedback shared by all branches of the tree.

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
     - Provide access to the shared command-header feedback for derived types.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``command_header() const``
     - Access the embedded ``CommandHeaderFeedback``.
     - This is the shared base-level accessor for the whole tree.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::CommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`command-header-feedback`
- :doc:`robot-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
