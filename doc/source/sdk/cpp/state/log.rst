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
     - Carry the time, level, and message of one log record emitted by the robot.

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
   * - ``timestamp``
     - Time of the log record, as ``timespec`` (``tv_sec``, ``tv_nsec``).
     - After ``StartTimeSync()`` has established time sync, the SDK shifts this
       value to the clock of your computer. Otherwise it is the robot time.
   * - ``robot_system_timestamp``
     - Robot PC (RPC) system time of the record, as ``timespec``.
     - Not shifted by time sync.
   * - ``level``
     - Severity of the log record.
     - Compare against the ``Level`` enum.
   * - ``message``
     - Human-readable message text.
     - The main payload most tools display.

.. note::

   In the generated declarations below, ``robot_system_timestamp`` appears
   as a heading ``struct robot_system_timestamp``. It is a plain ``timespec``
   member (``struct timespec robot_system_timestamp {}`` in ``log.h``), not a
   type of its own. ``timestamp`` is shown correctly as
   ``struct timespec timestamp``.

.. rubric:: Detailed Reference

.. doxygenstruct:: rb::Log
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`../client/robot`
- :doc:`robot-state`

.. rubric:: Examples

- `15_log.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/15_log.cpp>`__: ``GetLastLog()``.
- `16_log_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/16_log_stream.cpp>`__: ``StartLogStream()`` and ``StopLogStream()``.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
