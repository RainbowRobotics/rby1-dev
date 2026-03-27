Threading & Time Utilities
==========================

These helper classes provide task scheduling, thread management, and lightweight
timing measurements. They are lower-level building blocks that sit beneath the
main robot client APIs.

.. rubric:: Headers

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Type
     - Header
   * - ``rb::EventLoop``
     - ``#include <rby1-sdk/base/event_loop.h>``
   * - ``rb::Thread``
     - ``#include <rby1-sdk/base/thread.h>``
   * - ``rb::TimeWatch``
     - ``#include <rby1-sdk/base/time_util.h>``

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type or method group
     - Purpose
     - Notes
   * - ``rb::EventLoop``
     - Queue one-shot or cyclic work, pause execution, and wait for tasks.
     - Use in support utilities rather than high-level robot control.
   * - ``rb::Thread``
     - Configure thread name, affinity, and OS priority before running work.
     - Useful when timing behavior matters.
   * - ``rb::TimeWatch``
     - Record elapsed time measurements.
     - Handy in profiling and timing-sensitive utilities.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::EventLoop
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::Thread
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::TimeWatch
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`network-utilities`
- :doc:`../client/robot`

.. rubric:: Examples

- ``real_time_control_command.cpp`` is the most relevant example whenever
  execution timing matters.
