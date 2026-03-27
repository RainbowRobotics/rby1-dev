Client API
==========

These pages cover the high-level C++ client surface used by application code.
Start with ``rb::Robot<T>`` first, then drill into the command handlers,
real-time control structs, and serial stream helper as needed.

.. rubric:: API Pages

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main types
     - Description
   * - :doc:`robot`
     - ``rb::Robot<T>``
     - Main control client for connection, power, servo, state streaming,
       command submission, time sync, and parameter access.
   * - :doc:`robot-command-handler`
     - ``rb::RobotCommandHandler<T>``
     - One-shot command handle for waiting on completion and collecting final
       feedback.
   * - :doc:`robot-command-stream-handler`
     - ``rb::RobotCommandStreamHandler<T>``
     - Streaming command handle for sending multiple requests and reading
       feedback incrementally.
   * - :doc:`control-loop-types`
     - ``rb::ControlInput<T>``, ``rb::ControlState<T>``
     - Data structs exchanged through the ``Robot::Control()`` callback.
   * - :doc:`serial-stream`
     - ``rb::SerialStream``
     - SDK-managed serial device stream outside the gRPC robot client path.

.. toctree::
   :hidden:

   robot
   robot-command-handler
   robot-command-stream-handler
   control-loop-types
   serial-stream
