# Install & Build

These steps follow the README of [rby1-ros2 v1.0.0](https://github.com/RainbowRobotics/rby1-ros2).

::: info Note
Install in the system environment. With conda or miniforge, Python and CMake path conflicts break the build.
:::

## 1. Install ROS 2

Humble on Ubuntu 22.04 (recommended) or Jazzy on Ubuntu 24.04. The commands below say `humble`; on Jazzy write `jazzy`.
See the [ROS 2 installation guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html).

## 2. Build the C++ SDK

The driver links the **C++** rby1-sdk; the Python package from `pip install rby1-sdk` is not enough.
Build the SDK from source as described in [Build & Link](../../sdk/cpp/build-and-link.md).

`rby1_driver` and `rby1_hardware` find the SDK through the environment variable `RBY1_SDK_PATH`:
the SDK source tree with its build in `build/` (headers in `include/rby1-sdk`, library in `build/src`).
The build stops with a message if it is not set.

```bash
export RBY1_SDK_PATH=$HOME/rby1-sdk    # where you cloned and built the SDK
```

## 3. Get the source and install the dependencies

```bash
mkdir -p rby1_ros2_ws/src
cd rby1_ros2_ws/src
git clone https://github.com/RainbowRobotics/rby1-ros2.git
cd ..

source /opt/ros/humble/setup.bash
sudo rosdep init        # once per PC; "already initialized" is fine
rosdep update
rosdep install --from-paths src --ignore-src -y
```

`rosdep` installs the apt packages the workspace declares: MoveIt 2, `ros2_control` with its controllers, and
`librealsense2` (for the camera publisher in `rby1_tools`, see [Tools](tools.md)). No MoveIt source build is needed.

For an Intel RealSense camera (optional), install the camera's udev rules so a normal user can open it.
The ROS package does not bring them:

```bash
sudo curl -sSL https://raw.githubusercontent.com/IntelRealSense/librealsense/v2.56.5/config/99-realsense-libusb.rules \
     -o /etc/udev/rules.d/99-realsense-libusb.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```

## 4. Set up the environment

Add these lines to the end of `~/.bashrc`, then run `source ~/.bashrc`:

```bash
export RBY1_SDK_PATH=$HOME/rby1-sdk
source /opt/ros/humble/setup.bash
```

If other robots or PCs on the same network run ROS 2, choose a free `ROS_DOMAIN_ID` (0 to 101) and set it in every
terminal that talks to the driver, for example `export ROS_DOMAIN_ID=77`.

::: tip Using the UPC from a PC on the RPC's wireless network
ROS 2 does not reach the user PC (UPC) through the robot PC (RPC) on its own. If your PC is on the RPC's wireless network (AP)
and you want to use nodes that run on the UPC, set up the [UPC Topic Bridge](upc_topic_bridge.md) first (RPC 0.11.0 or later).
:::

## 5. Build

```bash
cd rby1_ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## 6. Start the driver and check it

::: danger The driver connects to the real robot
The examples and MoveIt launches you start after the driver move the robot.
Check that `robot_ip` is your robot's address, test in the simulator first, and keep the E-Stop within reach.
The driver also writes six robot parameters at connect ([Driver Parameters](config_driver_parameters.md)).
:::

```bash
ros2 launch rby1_driver rby1_ros2_driver.launch.py robot_ip:=<robot IP>:50051 model:=a
ros2 node list    # /rby1/rby1_ros2_driver
```

Give `model:=a` or `model:=m` to match your robot. The driver's own parameters are in [Driver Parameters](config_driver_parameters.md).

To try it without a robot, start the [MuJoCo simulator](../../simulators/mujoco.md) and use `robot_ip:=localhost:50051`.
Give the same model as the simulator image (`model:=a` for an `a_v1.2` image). Model UB images cannot be used with the driver.
Then continue with the [Examples](examples.md). To start the driver together with MoveIt, the camera or the gripper, see [Bringup](bringup.md).
