# Hardware Versions

Each robot model is built in several hardware versions (v1.0, v1.1, ...). The version changes the URDF, some joint ranges and some parts.
Use the URDF that matches your robot.

## Check the version of your robot

- **SDK**: `robot.get_robot_info().robot_model_version` (for example `v1.2`) and `robot_model_name`.
- **Web UI**: the **Dashboard** shows **Model** and **Model Version** at the bottom (see [Web UI](../../software/web-ui.md#dashboard)).

```python
import rby1_sdk as rby

robot = rby.create_robot("192.168.30.1:50051", "a")  # your address and model
robot.connect()
info = robot.get_robot_info()
print(info.robot_model_name, info.robot_model_version)
```

## Versions and URDF files

The URDF files are in the `models` folder of rby1-sdk (links to v0.10.1):

| Model | Hardware versions | URDF files |
| --- | --- | --- |
| Model A | v1.0, v1.1, v1.2 | [`model_v1.0.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1a/urdf/model_v1.0.urdf), [`model_v1.1.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1a/urdf/model_v1.1.urdf), [`model_v1.2.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1a/urdf/model_v1.2.urdf) |
| Model M | v1.0, v1.1, v1.2, v1.3 | [`model_v1.0.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1m/urdf/model_v1.0.urdf), [`model_v1.1.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1m/urdf/model_v1.1.urdf), [`model_v1.2.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1m/urdf/model_v1.2.urdf), [`model_v1.3.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1m/urdf/model_v1.3.urdf) |
| Model UB | v1.0 (the only version; the robot reports `v1.0`) | [`model.urdf`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/models/rby1ub/urdf/model.urdf) |

The MuJoCo models are in `models/<model>/mujoco/` with the same version suffixes (`model_v1.2.xml`, ...).
`model.urdf` of Model A and Model M is an older file; prefer the versioned file.

To compute kinematics and dynamics with the model that the robot itself uses, call `robot.get_dynamics()`:
it loads the URDF from the robot.

## Differences between versions

| **Section** | **Version 1.0** | **Version 1.1** | **Version 1.2** | **Version 1.3** (Model M only) |
| --- | --- | --- | --- | --- |
| **WY2 Motor** | Relative encoder + limit sensor | Absolute encoder | Absolute encoder | Absolute encoder |
| **Wrist Joint Config** | Yaw + Pitch + Yaw | Yaw + Pitch + Yaw | Yaw + Pitch + Yaw | Yaw + Pitch + Roll |
| **F/T Sensor** | F/T sensor + Tool Flange | Integrated F/T sensor + Tool Flange | Integrated F/T sensor + Tool Flange | None (see note below) |
| **Gripper** | Current Gripper | Redesigned Gripper | Redesigned Gripper | Redesigned Gripper |
| **Brake Material** | SUS | SK5 | SK5 | SK5 |
| **Neck Joint** (`head_0`, `head_1`) | Dynamixel 2-DOF (RS485) | Dynamixel 2-DOF (RS485) | High precision reducer 2-DOF (CAN, RB protocol) | High precision reducer 2-DOF (CAN, RB protocol) |
| **Head brakes** | No | No | Yes | Yes |
| **`head_0` range** | -30° ~ 30° | -30° ~ 30° | -90° ~ 90° | -90° ~ 90° |
| **`head_1` range** | -20° ~ 90° | -20° ~ 90° | -90° ~ 90° | -90° ~ 90° |

**Note on F/T sensors:** the F/T sensor row follows the original hardware table, which lists no F/T sensor for v1.3.
Whether a wrist F/T sensor is fitted depends on the configuration of your robot; confirm it with your robot's specification or Rainbow Robotics.
The robot core reads a right and a left F/T sensor on every version, so all versions report
`ft_sensor_right` and `ft_sensor_left` in the robot state. These fields do not show that a sensor is fitted.

Only these URDF files have `FT_sensor_R` and `FT_sensor_L` links: Model A `model_v1.0.urdf`, Model M `model_v1.0.urdf`
and Model UB `model.urdf` (also the older `model.urdf` of Model A and Model M).
The v1.1 and v1.2 URDFs do not have them. In the Model M `model_v1.3.urdf`, the joints to these links are commented out.

All joint ranges per version are in the joint tables of [Model A](generated/model_a.md#joint-range-and-speed-limits) and
[Model M](generated/model_m.md#joint-range-and-speed-limits).

---

Verified against: rby1-sdk v0.10.1 `models/rby1a/urdf/model_v1.0.urdf` … `model_v1.2.urdf`, `models/rby1m/urdf/model_v1.0.urdf` …
`model_v1.3.urdf` (`FT_sensor_R`/`FT_sensor_L` links in the v1.0 files only, commented out in v1.3; head joint limits), `models/rby1ub/urdf/model.urdf` (`FT_sensor_R`/`FT_sensor_L` links), `protos/rb/api/robot_info.proto`
(`robot_model_version`), `include/rby1-sdk/robot.h` (`GetDynamics`); the robot core hardware setup of Model A and Model M
(head on a Dynamixel bus for v1.0/v1.1, CAN RB motors with brakes for v1.2/v1.3; right and left F/T sensor nodes on every version)
and its version string (`v1.0` when the build defines no model version, as for Model UB). The WY2 motor, brake material and gripper rows, and the sensor type and tool flange text in the F/T sensor row, are from the original hardware table and were not checked against code.
