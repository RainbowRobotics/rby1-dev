---
layout: home

hero:
  name: RB-Y1
  text: Rainbow Robotics Dual-Arm Mobile Manipulator
  tagline: Manual, SDK and API reference for developers and integrators.
  image:
    src: /hero-image.png
    alt: RB-Y1
  actions:
    - theme: brand
      text: Quick Start
      link: /getting-started/index
    - theme: alt
      text: Hardware
      link: /hardware/overview
    - theme: alt
      text: API Reference
      link: /sdk/index

features:
  - icon: 🛑
    title: Quick Start
    details: E‑Stop first, then unboxing, hotspot and Web UI, and the SDK.
    link: /getting-started/index
    linkText: Get started
  - icon: 🦺
    title: Safety
    details: Precautions to read before operating the robot.
    link: /precautions/index
    linkText: Read the precautions
  - icon: 🦾
    title: Hardware
    details: Specifications, joint range and speed limits, options and maintenance.
    link: /hardware/index
    linkText: Hardware
  - icon: 🧭
    title: SDK Guide
    details: Architecture, robot models, controllers, examples and troubleshooting.
    link: /software/index
    linkText: SDK guide
  - icon: 📚
    title: API Reference
    details: Python, C++ and Protobuf (gRPC) API of rby1-sdk.
    link: /sdk/index
    linkText: API reference
  - icon: 🤖
    title: ROS 2
    details: The rby1-ros2 driver, MoveIt 2 integration, topics and services.
    link: /ros2/index
    linkText: ROS 2
  - icon: 🛠️
    title: Maintenance & Tools
    details: Software update, log backup, CAN and F/T sensor checks, part replacement.
    link: /maintenance/index
    linkText: Maintenance
  - icon: 🧪
    title: Simulation
    details: Run the robot software on a MuJoCo model in Docker, or in Isaac Sim.
    link: /simulators/index
    linkText: Simulators
---

## Before you begin

- **Safety first.** Before the first power‑on, read [E‑Stop Basics](/getting-started/estop-basics) and the [Safety](/precautions/index) pages, and follow your site safety policies.
- **Network.** Connect through the RB‑Y1 hotspot or your site network ([Hotspot & Web UI](/getting-started/hotspot-and-webui)).
- **SDK.** Install [rby1-sdk](https://github.com/RainbowRobotics/rby1-sdk) and check that you can read the robot state ([SDK Installation](/getting-started/sdk-install-and-state)).

## System highlights

- **Dual‑arm manipulation.** Two 7‑DoF arms for simultaneous, complex tasks.
- **Precision and stability.** High‑precision actuators and encoders for accurate, repeatable motion.
- **Modular design.** A structure that adapts to different requirements.
- **Real‑time control and integration.** Deterministic communication and control, with clean integration points for higher‑level systems and policies.

## Support & licensing

- **License.** rby1-sdk is released under Apache 2.0 and includes third‑party software; see [Open Source License Notices](/legal/third-party-notices).
- **Help.** Ask on [GitHub Discussions](https://github.com/RainbowRobotics/rby1-sdk/discussions) or contact rby.support@rainbow-robotics.com with logs, steps to reproduce and software versions.
