Command Feedback API
====================

These pages cover the classes in ``robot_command_feedback.h``. Read the
top-level feedback pages first, then drill into the composite or primitive
feedback class that matches the command path you sent.

.. rubric:: Base & Composite Feedback

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main type
     - Description
   * - :doc:`feedback`
     - ``rb::Feedback``
     - Common validity flag shared by all feedback objects.
   * - :doc:`command-header-feedback`
     - ``rb::CommandHeaderFeedback``
     - Header-level completion status.
   * - :doc:`command-feedback`
     - ``rb::CommandFeedback``
     - Shared base for all command result objects.
   * - :doc:`robot-command-feedback`
     - ``rb::RobotCommandFeedback``
     - Top-level status, finish code, and root feedback tree.
   * - :doc:`whole-body-command-feedback`
     - ``rb::WholeBodyCommandFeedback``
     - Composite feedback for whole-body stop and real-time bootstrap requests.
   * - :doc:`component-based-command-feedback`
     - ``rb::ComponentBasedCommandFeedback``
     - Composite feedback for body, head, and mobility child commands.
   * - :doc:`body-command-feedback`
     - ``rb::BodyCommandFeedback``
     - Composite feedback for a body-level command or split body composition.
   * - :doc:`body-component-based-command-feedback`
     - ``rb::BodyComponentBasedCommandFeedback``
     - Composite feedback for separate left-arm, right-arm, and torso child
       commands.
   * - :doc:`arm-command-feedback`
     - ``rb::ArmCommandFeedback``
     - Feedback wrapper for an arm-scoped command.
   * - :doc:`torso-command-feedback`
     - ``rb::TorsoCommandFeedback``
     - Feedback wrapper for a torso-scoped command.
   * - :doc:`head-command-feedback`
     - ``rb::HeadCommandFeedback``
     - Feedback wrapper for a head command.
   * - :doc:`mobility-command-feedback`
     - ``rb::MobilityCommandFeedback``
     - Feedback wrapper for mobility commands.

.. rubric:: Primitive Feedback

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main type
     - Description
   * - :doc:`stop-command-feedback`
     - ``rb::StopCommandFeedback``
     - Leaf result for a stop command.
   * - :doc:`realtime-control-command-feedback`
     - ``rb::RealtimeControlCommandFeedback``
     - Leaf result for the real-time bootstrap command.
   * - :doc:`se2-velocity-command-feedback`
     - ``rb::SE2VelocityCommandFeedback``
     - Leaf result for a planar-base velocity command.
   * - :doc:`jog-command-feedback`
     - ``rb::JogCommandFeedback``
     - Leaf result for a jog command.
   * - :doc:`joint-velocity-command-feedback`
     - ``rb::JointVelocityCommandFeedback``
     - Leaf result for a joint-velocity command.
   * - :doc:`joint-position-command-feedback`
     - ``rb::JointPositionCommandFeedback``
     - Progress values for a joint-position command.
   * - :doc:`joint-group-position-command-feedback`
     - ``rb::JointGroupPositionCommandFeedback``
     - Progress and joint-index data for a joint-group command.
   * - :doc:`cartesian-command-feedback`
     - ``rb::CartesianCommandFeedback``
     - Tracking errors and manipulability data for a Cartesian command.
   * - :doc:`cartesian-impedance-control-command-feedback`
     - ``rb::CartesianImpedanceControlCommandFeedback``
     - Impedance-tracking data for a Cartesian impedance command.
   * - :doc:`gravity-compensation-command-feedback`
     - ``rb::GravityCompensationCommandFeedback``
     - Leaf result for a gravity-compensation command.
   * - :doc:`impedance-control-command-feedback`
     - ``rb::ImpedanceControlCommandFeedback``
     - Tracking error data for an impedance-control command.
   * - :doc:`joint-impedance-control-command-feedback`
     - ``rb::JointImpedanceControlCommandFeedback``
     - Set-point and error data for a joint-impedance command.
   * - :doc:`optimal-control-command-feedback`
     - ``rb::OptimalControlCommandFeedback``
     - Solver cost data for an optimal-control command.

.. rubric:: Parsing Utility

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main type
     - Description
   * - :doc:`robot-command-feedback-parser`
     - ``rb::RobotCommandFeedbackParser``
     - Parser that fills a ``RobotCommandFeedback`` object from a lower-level
       message.

.. toctree::
   :hidden:

   feedback
   command-header-feedback
   command-feedback
   robot-command-feedback
   whole-body-command-feedback
   component-based-command-feedback
   body-command-feedback
   body-component-based-command-feedback
   arm-command-feedback
   torso-command-feedback
   head-command-feedback
   mobility-command-feedback
   stop-command-feedback
   realtime-control-command-feedback
   se2-velocity-command-feedback
   jog-command-feedback
   joint-velocity-command-feedback
   joint-position-command-feedback
   joint-group-position-command-feedback
   cartesian-command-feedback
   cartesian-impedance-control-command-feedback
   gravity-compensation-command-feedback
   impedance-control-command-feedback
   joint-impedance-control-command-feedback
   optimal-control-command-feedback
   robot-command-feedback-parser
