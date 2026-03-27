ComponentBasedCommandFeedback
=============================

``rb::ComponentBasedCommandFeedback`` is the top-level feedback branch for
component-based commands. It provides access to body, head, and mobility
feedback children.

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
     - Hold the component-based branch of the feedback tree.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``body_command() const``
     - Access the body feedback subtree.
     - Valid when the command included body content.
   * - ``head_command() const``
     - Access the head feedback subtree.
     - Valid when the command included head motion.
   * - ``mobility_command() const``
     - Access the mobility feedback subtree.
     - Valid when the command included a mobility path.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::ComponentBasedCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-feedback`
- :doc:`body-command-feedback`
- :doc:`head-command-feedback`
- :doc:`mobility-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``mobility_command.cpp``
