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
      link: /getting-started/estop-basics
    - theme: alt
      text: Hardware
      link: /hardware/overview
    - theme: alt
      text: API Reference
      link: /api/sdk/index.html
      target: _self

features:
  - icon: 🛑
    title: Safety first
    details: How to stop the robot and recover, before the first power-on.
    link: /getting-started/estop-basics
    linkText: E-Stop basics
  - icon: 🔌
    title: Hotspot & Web UI
    details: Power on, enable the servos and the Control Manager, move to the zero pose.
    link: /getting-started/hotspot-and-webui
    linkText: First power-on
  - icon: 🦾
    title: Hardware
    details: Specifications and the joint range and speed limits from the robot model.
    link: /hardware/overview
    linkText: Hardware overview
  - icon: 🐍
    title: SDK (Python / C++)
    details: Install rby1-sdk, connect, and read the robot state.
    link: /getting-started/sdk-install-and-state
    linkText: Install the SDK
  - icon: 🤖
    title: ROS 2
    details: Build the rby1-ros2 driver and connect it to the robot or the simulator.
    link: /ros2/ros2_driver/install_and_build
    linkText: Install & build
  - icon: 🧪
    title: Simulation
    details: Run the robot software on a MuJoCo model in Docker.
    link: /simulators/mujoco
    linkText: MuJoCo simulator
---
