Command Builder API
===================

These pages cover the classes in ``robot_command_builder.h``. Open the
top-level envelope and composition builders first, then drill into the
subsystem and primitive builders that actually hold command parameters.

.. rubric:: Envelope & Composition Builders

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main type
     - Description
   * - :doc:`command-header-builder`
     - ``rb::CommandHeaderBuilder``
     - Shared command metadata such as control hold time.
   * - :doc:`robot-command-builder`
     - ``rb::RobotCommandBuilder``
     - Outermost command envelope passed into ``Robot::SendCommand()``.
   * - :doc:`whole-body-command-builder`
     - ``rb::WholeBodyCommandBuilder``
     - Whole-robot stop and real-time bootstrap commands.
   * - :doc:`component-based-command-builder`
     - ``rb::ComponentBasedCommandBuilder``
     - Composition layer for body, head, and mobility subcommands.
   * - :doc:`body-command-builder`
     - ``rb::BodyCommandBuilder``
     - Body-level command or split torso-and-arms composition.
   * - :doc:`body-component-based-command-builder`
     - ``rb::BodyComponentBasedCommandBuilder``
     - Body-level composition for separate left-arm, right-arm, and torso
       commands.

.. rubric:: Subsystem Builders

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main type
     - Description
   * - :doc:`arm-command-builder`
     - ``rb::ArmCommandBuilder``
     - Arm-scoped command wrapper.
   * - :doc:`torso-command-builder`
     - ``rb::TorsoCommandBuilder``
     - Torso-scoped command wrapper.
   * - :doc:`head-command-builder`
     - ``rb::HeadCommandBuilder``
     - Head joint-position command wrapper.
   * - :doc:`mobility-command-builder`
     - ``rb::MobilityCommandBuilder``
     - Wheel-joint and planar-base command wrapper.

.. rubric:: Primitive Builders

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main type
     - Description
   * - :doc:`joint-position-command-builder`
     - ``rb::JointPositionCommandBuilder``
     - Joint-space point-to-point motion primitive.
   * - :doc:`joint-group-position-command-builder`
     - ``rb::JointGroupPositionCommandBuilder``
     - Joint-space motion primitive for a named subset of joints.
   * - :doc:`joint-impedance-control-command-builder`
     - ``rb::JointImpedanceControlCommandBuilder``
     - Joint-space impedance-control primitive.
   * - :doc:`impedance-control-command-builder`
     - ``rb::ImpedanceControlCommandBuilder``
     - Task-space impedance-control primitive around one target transform.
   * - :doc:`cartesian-command-builder`
     - ``rb::CartesianCommandBuilder``
     - Cartesian target-tracking primitive with stop thresholds.
   * - :doc:`cartesian-impedance-control-command-builder`
     - ``rb::CartesianImpedanceControlCommandBuilder``
     - Cartesian impedance primitive with nullspace and joint-limit terms.
   * - :doc:`joint-velocity-command-builder`
     - ``rb::JointVelocityCommandBuilder``
     - Joint-velocity command primitive.
   * - :doc:`se2-velocity-command-builder`
     - ``rb::SE2VelocityCommandBuilder``
     - Planar-base velocity command primitive.
   * - :doc:`jog-command-builder`
     - ``rb::JogCommandBuilder``
     - Named-joint jogging command primitive.
   * - :doc:`stop-command-builder`
     - ``rb::StopCommandBuilder``
     - Explicit stop command primitive.
   * - :doc:`real-time-control-command-builder`
     - ``rb::RealTimeControlCommandBuilder``
     - Real-time control bootstrap primitive with a UDP port.
   * - :doc:`gravity-compensation-command-builder`
     - ``rb::GravityCompensationCommandBuilder``
     - Gravity-compensation enable or disable primitive.
   * - :doc:`optimal-control-command-builder`
     - ``rb::OptimalControlCommandBuilder``
     - Optimal-control request primitive.

.. toctree::
   :hidden:

   command-header-builder
   robot-command-builder
   whole-body-command-builder
   component-based-command-builder
   body-command-builder
   body-component-based-command-builder
   arm-command-builder
   torso-command-builder
   head-command-builder
   mobility-command-builder
   joint-position-command-builder
   joint-group-position-command-builder
   joint-impedance-control-command-builder
   impedance-control-command-builder
   cartesian-command-builder
   cartesian-impedance-control-command-builder
   joint-velocity-command-builder
   se2-velocity-command-builder
   jog-command-builder
   stop-command-builder
   real-time-control-command-builder
   gravity-compensation-command-builder
   optimal-control-command-builder
