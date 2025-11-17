.. _python_api:

Python API Reference
====================

.. currentmodule:: rby1_sdk

Robot
-----

Each robot model has different degrees of freedom and basic structures, 
so separate classes are provided for each model. For more information about the models, refer to `this page <../../models/index.html>`_.

.. autosummary::
   :toctree: generated
   :nosignatures:

   create_robot
   create_robot_a
   create_robot_m
   create_robot_ub

Robot A
~~~~~~~

.. autosummary::
   :toctree: generated
   :nosignatures:

   Model_A
   Robot_A
   Robot_A_CommandHandler
   Robot_A_CommandStreamHandler
   Robot_A_ControlState
   Robot_A_ControlInput
   RobotState_A

Robot M
~~~~~~~

.. autosummary::
   :toctree: generated
   :nosignatures:

   Model_M
   Robot_M
   Robot_M_CommandHandler
   Robot_M_CommandStreamHandler
   Robot_M_ControlState
   Robot_M_ControlInput
   RobotState_M

Robot UB
~~~~~~~~

.. autosummary::
   :toctree: generated
   :nosignatures:

   Model_UB
   Robot_UB
   Robot_UB_CommandHandler
   Robot_UB_CommandStreamHandler
   Robot_UB_ControlState
   Robot_UB_ControlInput
   RobotState_UB

Robot Command
-------------

Robot Command Builder
~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated
   :nosignatures:

   RobotCommandBuilder
   CommandHeaderBuilder
   WholeBodyCommandBuilder
   ComponentBasedCommandBuilder
   HeadCommandBuilder
   MobilityCommandBuilder
   BodyCommandBuilder
   BodyComponentBasedCommandBuilder
   TorsoCommandBuilder
   ArmCommandBuilder
   StopCommandBuilder
   SE2VelocityCommandBuilder
   JogCommandBuilder
   JointVelocityCommandBuilder
   ImpedanceControlCommandBuilder
   CartesianImpedanceControlCommandBuilder
   CartesianCommandBuilder
   GravityCompensationCommandBuilder
   OptimalControlCommandBuilder
   JointImpedanceControlCommandBuilder
   JointGroupPositionCommandBuilder
   JointPositionCommandBuilder

Robot Command Feedback
~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated
   :nosignatures:

   Feedback
   CommandHeaderFeedback
   CommandFeedback
   RobotCommandFeedback
   WholeBodyCommandFeedback
   ComponentBasedCommandFeedback
   HeadCommandFeedback
   MobilityCommandFeedback
   BodyCommandFeedback
   BodyComponentBasedCommandFeedback
   TorsoCommandFeedback
   ArmCommandFeedback
   StopCommandFeedback
   SE2VelocityCommandFeedback
   JogCommandFeedback
   JointVelocityCommandFeedback
   ImpedanceControlCommandFeedback
   CartesianImpedanceControlCommandFeedback
   CartesianCommandFeedback
   GravityCompensationCommandFeedback
   OptimalControlCommandFeedback
   JointImpedanceControlCommandFeedback
   JointGroupPositionCommandFeedback
   JointPositionCommandFeedback

Modules
-------

.. autosummary::
   :toctree: generated
   :recursive:
   :nosignatures:

   math
   upc
   dynamics

Utilities
---------

.. autosummary::
   :toctree: generated
   :nosignatures:

   set_printoptions
   printoptions
   DynamixelBus