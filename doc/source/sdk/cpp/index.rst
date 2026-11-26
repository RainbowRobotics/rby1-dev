.. _cpp_api:

C++ API Reference
=================

This reference is generated from the public headers in
`include/rby1-sdk <https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/include/rby1-sdk>`__
of **rby1-sdk** |sdk_version|. Names that changed in v0.10.0 are listed under
their current names: ``Robot::BreakEngage()`` / ``BreakRelease()`` became
``BrakeEngage()`` / ``BrakeRelease()``, and ``rb::upc::MasterArm`` became
``rb::upc::LeaderArm``.

Each section page lists its classes. Each class page starts with a short
member summary, followed by the full generated declarations.

To build the C++ SDK and link it into your project, start with
:doc:`build-and-link`. For first-connection checks with the robot, see
`SDK Installation and Read State <../../getting-started/sdk-install-and-state.md>`_.
For runnable programs, see :doc:`cpp-examples`.

.. list-table::
   :header-rows: 1
   :widths: 20 34 46

   * - Section
     - Main types
     - Description
   * - :doc:`client/index`
     - ``rb::Robot<T>``, command handlers, control-loop structs
     - High-level client entry points for connecting to a robot, streaming
       state, and sending commands.
   * - :doc:`builders/index`
     - ``RobotCommandBuilder`` and all subsystem or primitive builders
     - Command-composition classes for body, arm, torso, head, mobility, and
       real-time control requests.
   * - :doc:`feedback/index`
     - ``RobotCommandFeedback`` and child feedback classes
     - Result and progress objects returned from submitted commands.
   * - :doc:`state/index`
     - ``RobotState<T>``, ``RobotInfo``, ``ControlManagerState``, ``Log``
     - Live state snapshots, static metadata, faults, and structured log
       records.
   * - :doc:`models/index`
     - model descriptors, ``rb::dyn::*``, ``rb::math::*``
     - Compile-time model descriptors, rigid-body dynamics, Lie-group math,
       and solver helpers.
   * - :doc:`utilities/index`
     - ``DynamixelBus``, ``LeaderArm``, UDP, threading, and timing helpers
     - Lower-level hardware utilities, protocol-facing helpers, and runtime
       support classes.
   * - :doc:`cpp-examples`
     - ``examples/cpp`` in rby1-sdk
     - The numbered example programs, what each one does, and whether it moves
       the robot.
   * - :doc:`full-api`
     - raw Doxygen site
     - Full generated symbol list outside the curated reference pages.

.. toctree::
   :hidden:
   :maxdepth: 2

   build-and-link
   client/index
   builders/index
   feedback/index
   state/index
   models/index
   utilities/index
   cpp-examples
   full-api