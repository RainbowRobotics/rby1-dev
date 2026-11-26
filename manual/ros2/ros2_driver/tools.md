# Tools

`rby1_tools` carries what sits on the robot besides the robot itself: a camera publisher, the gripper and the 2D LiDARs.

```bash
ros2 launch rby1_tools camera.launch.py                        # RealSense camera
ros2 launch rby1_tools gripper.launch.py                       # gripper model on TF + virtual driver
ros2 launch rby1_tools lidar.launch.py                         # the front LiDAR pair (on the UPC)
```

## Camera

`realsense_publisher` reads an Intel RealSense through librealsense directly (no realsense-ros) and publishes its images, its camera model and its place on the robot on TF.

```bash
ros2 launch rby1_tools camera.launch.py                          # config/camera/realsense.yaml
ros2 launch rby1_tools camera.launch.py rviz:=true               # with RViz
ros2 launch rby1_tools camera.launch.py mount:=head_tilted       # another place on the robot (add it to camera_mount.yaml first)
ros2 launch rby1_tools camera.launch.py camera_name:=desk mount:=none   # a second camera, on no link
```

| Launch argument | Default | Description |
|---|---|---|
| `camera` | `realsense` | The kind of camera. Only `realsense` for now |
| `camera_name` | `camera` | First part of the topics and frames: `/<camera_name>/...`, `<camera_name>_link` |
| `config` | `config/camera/<camera>.yaml` | Settings file: `serial`, `width`, `height`, `fps`, `use_rgb`, `use_depth`, `use_ir`, `use_point_cloud`, `align_depth_to_color`, `compressed`, exposure |
| `mount` | `head_default` | Where the camera sits: a name in `config/camera/camera_mount.yaml`; `none`: on no link |
| `rviz` | `false` | RViz with the image and the frames |

| Topic / frame | Type | When |
|---|---|---|
| `/<camera_name>/rgb/raw` (or `/rgb/compressed`) | `sensor_msgs/Image` (`CompressedImage`) | colour, by default |
| `/<camera_name>/rgb/info` | `sensor_msgs/CameraInfo` | always |
| `/<camera_name>/depth/raw`, `/depth/info` | `Image`, `CameraInfo` | `use_depth` (depth `16UC1` in mm) |
| `/<camera_name>/ir_left/...`, `/ir_right/...` | `Image`, `CameraInfo` | `use_ir` |
| `/<camera_name>/point_cloud` | `sensor_msgs/PointCloud2` | `use_point_cloud` |
| TF `<parent> → <camera_name>_link` | static | `mount` not `none` (`head_default`: on `link_head_2`) |

- **Setup**: needs `ros-$ROS_DISTRO-librealsense2` (installed by `rosdep`; without it the camera node is not built) and the udev rules from [Install & Build](install_and_build.md#3-get-the-source-and-install-the-dependencies).
- **Placing the camera**: `camera_mount.yaml` holds one entry per place, `<name>: {parent, xyz (m), rpy (rad)}`. There is no automatic camera-to-robot calibration: measure the values, then check them in RViz.
- **Marker detector**: not part of this repository. A detector that publishes `/rby1/marker_<id>/pose` (`geometry_msgs/PoseStamped`) works with the planner's scene tools.

## Gripper

The driver does not drive the grippers, and the robot model up to v1.2 ends at the tool frames.
`gripper.launch.py` starts the gripper model (TF and RViz) and its parts in the planning scene by flag, and always `gripper_driver`, which takes the gripper's commands and reports its fingers.

- `virtual: true` (default): nothing moves; the reported fingers go where they are told.
- `virtual: false`: the real gripper, through the SDK's Dynamixel bus (`/dev/rby1_gripper`).

```bash
ros2 launch rby1_tools gripper.launch.py                                 # model on TF + virtual driver
ros2 launch rby1_tools gripper.launch.py scene:=true                     # and its parts in the planning scene (needs a move_group)
ros2 launch rby1_tools gripper.launch.py virtual:=false                  # the real gripper (on the UPC, with the RB-Y1 driver running)
ros2 launch rby1_tools gripper.launch.py model:=false joint_states_topic:=/joint_states   # RB-Y1 M v1.3
ros2 topic pub --once -w 1 /rby1/right_gripper/grasp std_msgs/msg/Bool "{data: true}"     # close
ros2 topic pub --once -w 1 /rby1/right_gripper/grasp std_msgs/msg/Bool "{data: false}"    # open
ros2 topic echo /rby1/right_gripper/state
```

::: danger The real gripper moves at start
With `virtual: false`, run the launch on the PC the gripper's USB is plugged into (the UPC), with the RB-Y1 driver running and the robot powered.
The gripper driver first switches both tool flange outputs to 12 V through the driver's `tool_flange_power`,
then runs each motor to both ends of its travel (homing): **the fingers move**. Keep fingers and objects out of the gripper.
The real gripper is built only where `RBY1_SDK_PATH` is set.
:::

| Launch argument | Default | Description |
|---|---|---|
| `model` | `true` | The gripper's URDF on TF under `ee_right` / `ee_left`. Not for an M v1.3, whose URDF has the gripper |
| `scene` | `false` | The gripper's parts in the planning scene (needs a `move_group`) |
| `virtual` | the settings' (`true`) | `true` or `false` |
| `hands` | `right,left` | `right`, `left`, or both |
| `joint_states_topic` | `/gripper/joint_states` with `model`, else none | Where the finger joint states go; `/joint_states` on an M v1.3 |
| `driver_namespace` | `rby1` | Namespace of the RB-Y1 driver (for `tool_flange_power`) |

| Topic | Type | Direction | Content |
|---|---|---|---|
| `/rby1/<hand>_gripper/command` | `std_msgs/Float64` | in | Each finger's opening in m: 0 closed to 0.05 open |
| `/rby1/<hand>_gripper/grasp` | `std_msgs/Bool` | in | `true` closes, `false` opens |
| `/rby1/<hand>_gripper/state` | `sensor_msgs/JointState` | out | The fingers' opening |

Settings (`config/gripper/gripper_driver.yaml`), mount (`config/gripper/gripper_mount.yaml`).
If the motors do not answer (`Dynamixel id ... does not answer`), switch the flange on by hand and start again:

```bash
ros2 service call /rby1/tool_flange_power rby1_msgs/srv/StateOnOff "{state: true, parameters: '12'}"
```

## LiDAR

`lidar_publisher` turns the UDP packets of the Richbeam LakiBeam1 2D LiDARs on the mobile base into `sensor_msgs/LaserScan`, and places each sensor on TF. No vendor driver is needed.
Run it on the PC the sensors send to: the UPC (192.168.30.2). The front left sensor (192.168.30.10) sends to port 2367, the front right one (192.168.30.11) to 2368.

```bash
ros2 launch rby1_tools lidar.launch.py                    # the front pair
ros2 launch rby1_tools lidar.launch.py front_right:=false # the front left one only
ros2 launch rby1_tools lidar_calibrate.launch.py          # once, with lidar.launch.py stopped: where the sensors sit
```

| Topic / frame | Type | Content |
|---|---|---|
| `/<lidar_name>/scan` | `sensor_msgs/LaserScan` | One full turn per message (`lidar_front_left`, `lidar_front_right`), with `merge: false` |
| `/lidar_merged/scan` | `sensor_msgs/LaserScan` | All sensors as one 360° scan in `base`, with `merge: true` in `config/lidar/lidar.yaml` |
| TF `<parent> → <lidar_name>_link` | static | Where the sensor sits (`parent`, `xyz`, `rpy` in `lidar.yaml`) |

- The sensor places in `lidar.yaml` are reference values, not measured on your robot. Measure them, or run `lidar_calibrate.launch.py` once and copy the printed `xyz` / `rpy` in. It finds x, y and yaw against a reference sensor.
- **No scans**: check that the sensor answers (`ping`), where it sends (`curl http://<sensor_ip>/api/v1/sensor/overview`, field `host`), and that its packets reach this PC (`sudo tcpdump -n -i any -c 3 udp and host <sensor_ip>`).

Verified against: rby1-ros2 v1.0.0 `rby1_tools/launch/*.launch.py`, `rby1_tools/config/`, `Doc/manual/07_tools.md`, README (RealSense udev rules).
