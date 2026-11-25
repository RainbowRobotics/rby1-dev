.. _python_api:

Python API Reference
====================

.. note::

   This reference is generated from **rby1-sdk** |sdk_version|
   (``pip install rby1-sdk``). Names that changed in v0.10.0
   (``break_engage`` → ``brake_engage``, ``MasterArm`` → ``LeaderArm``) are
   listed under their current names.

.. currentmodule:: rby1_sdk

Overview of the Python SDK reference, grouped by client entry points,
command builders, feedback payloads, submodules, and utilities.

.. list-table::
   :header-rows: 1
   :widths: 20 34 46

   * - Section
     - Main types
     - Description
   * - :doc:`client/index`
     - ``Robot_*``, ``Model_*``, ``RobotState_*``
     - Robot entry points and model-specific control/state classes.
   * - :doc:`builders/index`
     - ``*CommandBuilder``
     - Command composition helpers for body, arm, torso, head, and mobility.
   * - :doc:`feedback/index`
     - ``*CommandFeedback``
     - Feedback/result payloads returned by submitted commands.
   * - :doc:`modules/index`
     - ``math``, ``upc``, ``dynamics``
     - Core Python modules exposed by the SDK.
   * - :doc:`utilities/index`
     - ``DynamixelBus``, print helpers
     - Utility helpers and print configuration.

.. toctree::
   :hidden:
   :maxdepth: 2

   client/index
   builders/index
   feedback/index
   modules/index
   utilities/index
