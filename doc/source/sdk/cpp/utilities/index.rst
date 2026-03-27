Utility API
===========

These pages cover lower-level utilities that sit outside the main
connect-command-feedback workflow. Use them when you need direct Dynamixel
access, master-arm support, UDP transport helpers, or general threading and
timing facilities.

.. rubric:: API Pages

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main types
     - Description
   * - :doc:`dynamixel-bus`
     - ``rb::DynamixelBus``
     - Device-level access to Dynamixel-based peripherals.
   * - :doc:`master-arm`
     - ``rb::upc::MasterArm``
     - Master-arm device integration and local control support.
   * - :doc:`network-utilities`
     - ``rb::UdpClient``, ``UdpIPv4Client``, ``UdpIPv6Client``, ``UdpServer``
     - Lower-level UDP transport types used by the real-time path.
   * - :doc:`threading-and-time-utilities`
     - ``rb::EventLoop``, ``Thread``, ``TimeWatch``
     - Task scheduling, thread control, and timing measurement helpers.

.. toctree::
   :hidden:

   dynamixel-bus
   master-arm
   network-utilities
   threading-and-time-utilities
