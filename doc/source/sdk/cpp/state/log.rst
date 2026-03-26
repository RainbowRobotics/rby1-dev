Log
===

``rb::Log`` is the structured record emitted by the robot log APIs. It is used
by ``GetLastLog()`` and the callback passed into ``StartLogStream()``.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/log.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``struct``
   * - Primary role
     - Carry a log level and message payload emitted by the robot.

.. rubric:: Member Types / Enums

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``Level``
     - Enumerate the severity of the log record.
     - Read this before filtering or displaying messages.

.. rubric:: Public Attributes

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Field
     - Meaning
     - Notes
   * - ``level``
     - Severity of the log record.
     - Compare against the ``Level`` enum.
   * - ``message``
     - Human-readable message text.
     - The main payload most tools display.

.. rubric:: Detailed Reference

.. doxygenstruct:: rb::Log
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`../client/robot`
- :doc:`robot-state`

.. rubric:: Examples

- ``log.cpp`` is the direct example for fetching and streaming ``rb::Log``
  records.
