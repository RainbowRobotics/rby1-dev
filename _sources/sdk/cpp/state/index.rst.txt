State & Metadata API
====================

These pages cover live state snapshots, static robot metadata, control-manager
state, and structured logs. Use this category when you are reading what the
robot is doing rather than composing what it should do next.

.. rubric:: API Pages

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main types
     - Description
   * - :doc:`control-manager-state`
     - ``rb::ControlManagerState``
     - Control-manager mode and fault state summary.
   * - :doc:`robot-info`
     - ``rb::RobotInfo`` and related metadata structs
     - Static model, device, and joint metadata returned by
       ``GetRobotInfo()``.
   * - :doc:`robot-state`
     - ``rb::RobotState<T>`` and related state structs
     - Live measurements, targets, tool-flange state, and FT sensor data.
   * - :doc:`log`
     - ``rb::Log``
     - Structured log records and streamed log callbacks.

.. toctree::
   :hidden:

   control-manager-state
   robot-info
   robot-state
   log
