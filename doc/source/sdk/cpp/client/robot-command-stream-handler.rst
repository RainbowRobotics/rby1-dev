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

.. rubric:: Streaming Commands

Shortened from ``examples/cpp/32_command_stream.cpp``. The loop sends a new
body joint position target through one open stream every cycle. Each command
carries a control hold time (see :doc:`../builders/command-header-builder`).
``Model`` is the model descriptor, for example ``rb::y1_model::A``.

.. code-block:: cpp

   using namespace rb;

   auto stream = robot->CreateCommandStream(10 /* priority */);
   for (int t = 0; t < 10000; ++t) {
     Eigen::VectorXd q = Eigen::VectorXd::Zero(Model::kBodyIdx.size());
     q(q.size() - 3) = M_PI / 4.0 * std::sin(2.0 * M_PI * t * 0.001 / 5.0);

     stream->SendCommand(RobotCommandBuilder().SetCommand(
         ComponentBasedCommandBuilder().SetBodyCommand(
             JointPositionCommandBuilder()
                 .SetCommandHeader(CommandHeaderBuilder().SetControlHoldTime(1.0))
                 .SetMinimumTime(3)
                 .SetPosition(q))));
     std::this_thread::sleep_for(std::chrono::microseconds(500));
   }
   stream->Cancel();  // Also call Cancel() when the user stops the program early.

.. warning::

   This loop moves the robot. Clear the area around the robot and keep the
   E-Stop within reach.

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

- `32_command_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/32_command_stream.cpp>`__: opens a stream and sends joint position commands in a loop.
- `33_cartesian_command_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/33_cartesian_command_stream.cpp>`__: streams Cartesian targets and calls ``RequestFeedback()``.
- `22_replay.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/22_replay.cpp>`__: replays recorded positions through a stream.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
