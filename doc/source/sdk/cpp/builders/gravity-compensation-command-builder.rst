GravityCompensationCommandBuilder
=================================

``rb::GravityCompensationCommandBuilder`` toggles gravity compensation on or
off for the selected body, torso, or arm path.

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
     - Represent a gravity-compensation enable or disable request.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetCommandHeader(...)``
     - Attach shared header metadata.
     - Uses :doc:`command-header-builder`.
   * - ``SetOn(...)``
     - Enable or disable gravity compensation.
     - This is the main payload.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::GravityCompensationCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-builder`
- :doc:`torso-command-builder`
- :doc:`body-command-builder`

.. rubric:: Examples

- ``gravity_compensation.cpp``
