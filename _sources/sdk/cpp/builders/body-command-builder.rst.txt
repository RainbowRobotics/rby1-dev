BodyCommandBuilder
==================

``rb::BodyCommandBuilder`` holds one body-scoped command. It can wrap one
primitive body command directly or hold a split torso-and-arms composition
through ``BodyComponentBasedCommandBuilder``.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_command_builder.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Hold one body-level command mode beneath the component-based tree.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - converting constructors
     - Construct from a body primitive or from
       ``BodyComponentBasedCommandBuilder``.
     - Supports joint, cartesian, impedance, gravity, and optimal-control modes.
   * - ``SetCommand(...)``
     - Replace the active body command mode.
     - Use before embedding in ``ComponentBasedCommandBuilder``.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::BodyCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`component-based-command-builder`
- :doc:`body-component-based-command-builder`
- :doc:`cartesian-command-builder`
- :doc:`optimal-control-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``optimal_control.cpp``
