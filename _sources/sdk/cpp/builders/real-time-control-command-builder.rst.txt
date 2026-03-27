RealTimeControlCommandBuilder
=============================

``rb::RealTimeControlCommandBuilder`` bootstraps the real-time control channel.
Its main job is to carry the UDP port used by the real-time path.

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
     - Represent the real-time control bootstrap request.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetPort(...)``
     - Set the UDP port used by the real-time control path.
     - This is the main payload of the primitive.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetPort(port)``
     - UDP port number
     - Network endpoint configuration, not a physical unit.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RealTimeControlCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`whole-body-command-builder`
- :doc:`../client/control-loop-types`

.. rubric:: Examples

- ``real_time_control_command.cpp``
