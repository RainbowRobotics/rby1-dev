# Bringup

`rby1_bringup` has one launch file that starts the driver and the parts you switch on.

```bash
ros2 launch rby1_bringup bringup.launch.py
```

- **What starts** is set by the `True`/`False` flags at the top of `rby1_bringup/launch/bringup.launch.py`, one line each with a comment. Only `DRIVER` is on by default.
- **What each part starts with** is in `rby1_bringup/config/bringup.yaml`, one section per part, with the arguments of that part's own launch file. An empty value (`""`) means that launch file's default.

With `colcon build --symlink-install` you edit both files in the source tree; restart the launch to apply.

| Flag | Starts | Section in `bringup.yaml` | Page |
|---|---|---|---|
| `DRIVER` (on) | The driver | `driver`: `params_file`, `namespace`, `robot_ip`, `model` | [Driver Parameters](config_driver_parameters.md) |
| `MOVEIT_EXECUTOR` | The MoveIt planner that moves the arms through the driver. **It moves the robot to the ready pose at start** | `moveit_executor`: `rviz`, `target_namespace`, `velocity_scaling`, `minimum_time`, `impedance`, `ready_pose`, `version` | [MoveIt Planner](moveit_planner.md) |
| `MOVEIT_DEMO` | MoveIt with `ros2_control` (not together with the planner) | `moveit_demo`: `package`, `use_fake_hardware` | [MoveIt 2](rby1_moveit2.md) |
| `ROS2_CONTROL` | `ros2_control` with the hardware plugin, without MoveIt (not together with `MOVEIT_DEMO`) | `ros2_control`: `use_fake_hardware` (the robot is `driver.model` and `moveit_executor.version`, both required) | [ros2_control Hardware Interface](hardware_interface.md) |
| `SCENE` | Obstacles loaded into the planning scene | `scene`: `config` | [MoveIt Planner](moveit_planner.md#planning-scene-rby1_moveit_objects) |
| `OBJECTS` | Modules on the robot or fixtures in the planning scene | `objects`: `config` | [MoveIt Planner](moveit_planner.md#planning-scene-rby1_moveit_objects) |
| `CAMERA` | The camera publisher | `camera`: `camera`, `camera_name`, `config`, `mount` | [Tools](tools.md#camera) |
| `GRIPPER` | The gripper on the hands: model on TF, parts in the planning scene, its driver (virtual or real) | `gripper`: `model`, `scene`, `virtual`, `hands`, `mount`, `config` | [Tools](tools.md#gripper) |

::: warning
`MOVEIT_EXECUTOR` moves the robot as soon as it starts, and `GRIPPER` with `virtual: false` moves the gripper fingers at start (homing).
Check the flags and `bringup.yaml` before you launch on a real robot, and keep the E-Stop within reach.
:::

::: warning Set `driver.robot_ip` for `ROS2_CONTROL` and `MOVEIT_DEMO`
With `ROS2_CONTROL` or `MOVEIT_DEMO`, set `driver.robot_ip` in `bringup.yaml` (for example `192.168.30.1:50051`).
With it empty, the driver uses the address in its params file, but the hardware plugin connects to `127.0.0.1:50051`.
:::

Before anything starts, the launch checks the combination and stops with one line when it is wrong:
a missing section, a bad model or address, planner and demo together, a demo package that is not built or is for the other model,
an M v1.3 (`moveit_executor.version: 1.3`) with the gripper's model or scene on, or nothing switched on at all.
The planner is started 3 s after the driver, and the scene, the objects and the gripper scene once `move_group` is up.

Each part in the launch file is its own launch file included with its arguments written out, so a block can be copied or changed as it is.

Verified against: rby1-ros2 v1.0.0 `rby1_bringup/launch/bringup.launch.py`, `rby1_bringup/config/bringup.yaml`, `Doc/manual/01_overview.md` (Bringup).
