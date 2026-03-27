Robot
=====

.. currentmodule:: rby1_sdk

This section groups the primary robot entry points and model-specific classes.
Use it when you need to connect to a robot, fetch state, or work with a
particular model variant.

Each robot model has different degrees of freedom and basic structures, 
so separate classes are provided for each model. For more information about the models, refer to `this page <../../models/index.html>`_.

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   create_robot
   create_robot_a
   create_robot_m
   create_robot_ub

Robot A
~~~~~~~

.. autosummary::
   :toctree: ../generated
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
   :toctree: ../generated
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
   :toctree: ../generated
   :nosignatures:

   Model_UB
   Robot_UB
   Robot_UB_CommandHandler
   Robot_UB_CommandStreamHandler
   Robot_UB_ControlState
   Robot_UB_ControlInput
   RobotState_UB
