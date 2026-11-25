.. meta::
   :description: RB-Y1 Dual-Arm Mobile Manipulator — Developer & Expert Manual
   :keywords: Rainbow Robotics, RB-Y1, dual-arm, manipulator, SDK, real-time control, robotics

.. title:: RB-Y1 Developer Manual

===============================
RB-Y1 Developer & Expert Manual
===============================

.. image:: _static/images/brand/hero-image.png
   :alt: RB-Y1
   :align: center
   :width: 800px

Designed for **developers**, this manual covers the RB-Y1 dual-arm mobile manipulator——its real-time software stack, 
APIs, setup workflows, and integration guidelines. The RB-Y1 provides *two 7-DoF arms* for coordinated manipulation, high-precision 
actuation and sensing, and a modular architecture suitable for research and production environments.

.. note::
   **Audience** — This documentation targets **robotics developers, integrators, and researchers** who require low-level access, deterministic behavior, and clear contracts between hardware, control, and client applications.

What’s in this manual
---------------------

.. grid:: 1 2 2 4
   :gutter: 3

   .. grid-item-card:: Getting Started
      :link: getting-started/index
      :link-type: doc

      E‑Stop, unboxing, hotspot and Web UI, first SDK connection.

   .. grid-item-card:: Safety
      :link: precautions/index
      :link-type: doc

      Precautions to read before operating the robot.

   .. grid-item-card:: Hardware
      :link: hardware/index
      :link-type: doc

      Specifications, joint limits, electrical system, battery and options.

   .. grid-item-card:: Software & SDK
      :link: software/index
      :link-type: doc

      Architecture, robot models, controllers, examples and troubleshooting.

   .. grid-item-card:: API Reference
      :link: sdk/index
      :link-type: doc

      Python, C++ and Protobuf (gRPC) APIs of rby1-sdk |sdk_version|.

   .. grid-item-card:: ROS 2
      :link: ros2/index
      :link-type: doc

      The ROS 2 driver, MoveIt 2 integration, topics and services.

   .. grid-item-card:: Simulation
      :link: simulators/index
      :link-type: doc

      MuJoCo and Isaac Sim simulators.

   .. grid-item-card:: Maintenance
      :link: maintenance/index
      :link-type: doc

      Software update, log backup, diagnostics and part replacement.

System highlights
-----------------

- **Dual-arm manipulation** — Two 7-DoF arms enable simultaneous, complex tasks.
- **Precision & stability** — High-precision actuators/encoders for accurate, repeatable motion.
- **Modular design** — Scalable structure adaptable to varied requirements.
- **Real-time control & integration** — Deterministic communication/control, clean integration points
  to higher-level systems and policies.

Before you begin
----------------

- **Safety first** — Before the first power‑on, read :doc:`getting-started/estop-basics` and the
  :doc:`Safety <precautions/index>` pages, and follow your site safety policies.
- **Environment** — Ensure a supported Linux/Windows development host with real-time requirements
  where applicable.
- **Network** — Confirm access via RB-Y1 hotspot or your site network (:doc:`getting-started/hotspot-and-webui`).
- **SDK** — Install the SDK and verify state streaming (`rby1-sdk <https://github.com/RainbowRobotics/rby1-sdk>`_), (:doc:`getting-started/sdk-install-and-state`).

Support & licensing
-------------------

- **License** — *rby1-sdk* is released under **Apache 2.0** and incorporates
  third-party software. See :doc:`legal/third-party-notices` for attribution
  and license information.
- **Issues & help** — Use your support channel or contact your Rainbow Robotics representative with
  logs, repro steps, and software versions.

——

*© 2024-2025 Rainbow Robotics. All rights reserved.*

.. toctree::
   :hidden:
   :maxdepth: 2

   getting-started/index
   precautions/index
   hardware/index
   software/index
   sdk/index
   ros2/index
   simulators/index
   maintenance/index
