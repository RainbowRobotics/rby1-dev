Build & Link
============

The C++ SDK is built from source. This page follows the rby1-sdk |sdk_version|
README and ``CMakeLists.txt``.

.. rubric:: Requirements

- C++17 compiler (GCC on Linux), CMake, Python 3 with ``pip``
- `Conan 2 <https://conan.io/>`_ for the dependencies (gRPC, Protobuf, Eigen, ...)

.. rubric:: 1. Get the source and the dependencies

.. code-block:: bash

   pip install conan
   git clone --recurse-submodules --branch v0.10.1 https://github.com/RainbowRobotics/rby1-sdk.git
   cd rby1-sdk
   conan install . -s build_type=Release -b missing -of build

``--branch v0.10.1`` checks out the release this reference documents. Without
it you get the default branch, which can be newer than this reference.

On ``aarch64`` (for example the UPC), set the compiler first:
``export CC=/usr/bin/aarch64-linux-gnu-gcc``.

.. rubric:: 2. Configure, build and install

Choose the install location with ``CMAKE_INSTALL_PREFIX`` when you configure.
Without it, CMake uses its default prefix (``/usr/local`` on Linux), and the
install step needs ``sudo``. A prefix in your home directory needs no ``sudo``.

With CMake 3.23 or later:

.. code-block:: bash

   cmake --preset conan-release -D BUILD_EXAMPLES=ON -D CMAKE_INSTALL_PREFIX=$HOME/.local
   cmake --build --preset conan-release
   cmake --build --preset conan-release --target install

With an older CMake:

.. code-block:: bash

   cd build
   cmake .. -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=./conan_toolchain.cmake \
            -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=ON \
            -DCMAKE_INSTALL_PREFIX=$HOME/.local
   cmake --build .
   make install

Build options (``-D<option>=ON|OFF``):

.. list-table::
   :header-rows: 1
   :widths: 30 12 58

   * - Option
     - Default
     - Effect
   * - ``BUILD_EXAMPLES``
     - ``OFF``
     - Build the programs in ``examples/cpp`` (for example ``01_hello_rby1``).
   * - ``BUILD_LIB_STATIC``
     - ``OFF``
     - Build a static library instead of a shared one. The installed CMake
       package does not look up the private dependencies (gRPC, Protobuf,
       OSQP, tinyxml2, ...), so a project that links the installed static
       library must provide them itself. Use the default shared library unless
       you need static linking.
   * - ``INSTALL_MODELS``
     - ``ON``
     - Install the robot models (URDF) to ``share/rby1-sdk/models``.

.. rubric:: 3. Use the SDK in your project

The install step exports the CMake package ``rby1-sdk`` with the target
``rby1-sdk::rby1-sdk``. The package needs Eigen 3 (``find_dependency(Eigen3)``);
on Ubuntu install it with ``sudo apt install libeigen3-dev`` if your project
does not provide it.

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.18)
   project(my_rby1_app LANGUAGES CXX)

   set(CMAKE_CXX_STANDARD 17)
   find_package(rby1-sdk CONFIG REQUIRED)

   add_executable(my_rby1_app main.cpp)
   target_link_libraries(my_rby1_app PRIVATE rby1-sdk::rby1-sdk)

.. code-block:: cpp

   // main.cpp
   #include <iostream>
   #include "rby1-sdk/model.h"
   #include "rby1-sdk/robot.h"

   int main() {
     // Robot address and gRPC port; "localhost:50051" reaches a simulator on this computer.
     auto robot = rb::Robot<rb::y1_model::A>::Create("localhost:50051");
     robot->Connect();
     std::cout << robot->GetRobotInfo().robot_version << std::endl;
   }

If the SDK is installed to a non-default prefix, pass it to your project with
``-DCMAKE_PREFIX_PATH=<prefix>`` (for example ``-DCMAKE_PREFIX_PATH=$HOME/.local``).
The SDK is a shared library by default. If your program cannot find
``librby1-sdk.so`` at run time, add ``<prefix>/lib`` to ``LD_LIBRARY_PATH``, or
run ``sudo ldconfig`` after installing to a system prefix.

.. rubric:: Next steps

- :doc:`client/robot` for the client API.
- :doc:`cpp-examples` for runnable programs.
- `Build Issues <../trobuleshooting/generated/build_issue.md>`_ if the build fails.
