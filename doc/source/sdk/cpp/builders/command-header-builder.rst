CommandHeaderBuilder
====================

``rb::CommandHeaderBuilder`` carries command-level metadata shared by many
primitive builders. In practice it is the place to set hold-time behavior
before embedding a primitive command in a higher-level builder.

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
     - Carry common command-header settings for downstream builders.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``CommandHeaderBuilder()``
     - Construct an empty command header.
     - Typically followed by one setter call.
   * - ``SetControlHoldTime(...)``
     - Set the control hold time attached to a command.
     - Reused by several primitive builder classes.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetControlHoldTime(control_hold_time)``
     - ``s``
     - The hold time is serialized through ``google.protobuf.Duration`` in the
       command header proto.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::CommandHeaderBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-builder`
- :doc:`joint-position-command-builder`
- :doc:`stop-command-builder`

.. rubric:: Examples

- `32_command_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/32_command_stream.cpp>`__: ``SetControlHoldTime()`` on streamed commands.
- `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__: command headers on the demo motions.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
