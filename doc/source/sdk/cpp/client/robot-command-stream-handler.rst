RobotCommandStreamHandler
=========================

``rb::RobotCommandStreamHandler<T>`` keeps a command stream open so multiple
commands can be sent over the same stream. Use it when one-shot submission is
too restrictive or when feedback must be requested incrementally.

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
     - Send commands through a persistent stream and request feedback on demand.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SendCommand(...)``
     - Push one command into the open stream.
     - The payload still uses :doc:`../builders/robot-command-builder`.
   * - ``RequestFeedback(...)``
     - Pull feedback from the stream.
     - Use after one or more streamed commands have been sent.
   * - ``Wait()`` and ``WaitFor(...)``
     - Block until the stream has completed or terminated.
     - ``WaitFor(...)`` is the timed variant.
   * - ``IsDone()`` and ``Cancel()``
     - Check stream completion or cancel the stream.
     - Useful when the producer side must shut down early.

.. rubric:: Numeric Parameters & Returns

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Method
     - Unit / encoding
     - Notes
   * - ``SendCommand(..., timeout_ms)``
     - ``ms``
     - Feedback-receive timeout for the streamed command, not the full command
       execution duration.
   * - ``RequestFeedback(timeout_ms)``
     - ``ms``
     - Timeout for requesting in-flight controller feedback.
   * - ``WaitFor(timeout_ms)``
     - ``ms``
     - Timed wait for the stream itself to finish.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::RobotCommandStreamHandler
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot`
- :doc:`robot-command-handler`
- :doc:`../feedback/robot-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp`` is the easiest place to compare one-shot submission
  against a longer-lived command path.
