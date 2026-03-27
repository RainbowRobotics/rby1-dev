RobotCommandHandler
===================

``rb::RobotCommandHandler<T>`` is the one-shot command handle returned by
``Robot::SendCommand()``. It is the simplest way to wait for completion, cancel
the request, or retrieve the resulting feedback object.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class template``
   * - Primary role
     - Track one submitted command until completion and expose its feedback.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``Get()`` and ``GetStatus()``
     - Retrieve the final feedback object or the current command status.
     - Use ``GetStatus()`` while polling.
   * - ``Wait()`` and ``WaitFor(...)``
     - Block until the command finishes.
     - ``WaitFor(...)`` is the timed variant.
   * - ``IsDone()`` and ``Cancel()``
     - Check for completion or cancel an in-flight command.
     - Cancellation affects the underlying execution request.

.. rubric:: Numeric Parameters & Returns

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Method
     - Unit / encoding
     - Notes
   * - ``WaitFor(timeout_ms)``
     - ``ms``
     - Timeout used while waiting for one-shot command completion.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RobotCommandHandler
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot`
- :doc:`robot-command-stream-handler`
- :doc:`../feedback/robot-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp`` uses the one-shot command path.
- ``stop_command.cpp`` is a compact example of submitting one command and
  waiting for it to finish.
