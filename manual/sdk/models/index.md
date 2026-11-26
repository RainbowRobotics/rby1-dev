# Models

RB-Y1 comes in three models. They share the arms and the head; the base and the torso differ.
Pick the model name that matches your robot when you create the robot object in the SDK.

| Model | Base | Torso | DOF | SDK model name | `robot_model_name` |
| --- | --- | --- | --- | --- | --- |
| [Model A](./generated/model_a.md) | Differential drive, 2 wheels | 6 joints (`torso_0` … `torso_5`) | 24 | `"a"` | `rby1a` |
| [Model M](./generated/model_m.md) | Mecanum, 4 wheels | 6 joints (`torso_0` … `torso_5`) | 26 | `"m"` | `rby1m` |
| [Model UB](./generated/model_ub.md) | None (upper body) | 2 joints (`torso_hp`, `torso_5`) | 18 | `"ub"` | `rby1ub` |

```python
import rby1_sdk as rby

robot = rby.create_robot("192.168.30.1:50051", "a")  # "a", "m" or "ub"
robot.connect()
print(robot.get_robot_info().robot_model_name)       # check that the model matches
print(robot.model().robot_joint_names)               # joint names in index order
```

- [Hardware Versions](./hardware-versions.md): versions v1.0 to v1.3, how to check yours, and the URDF file of each version.
- [Units and Frames](../../software/units-and-frames.md): units, the base frame and the link names used in commands.
- Joint ranges and speeds of all models are also in [Overview & Specifications](../../hardware/overview.md).

---

Verified against: rby1-sdk v0.10.1 `include/rby1-sdk/model.h` (`A`, `M`, `UB`), `python/rby1_sdk/__init__.py` (`create_robot`),
`python/robot.cpp` (`model`, `get_robot_info`); robot core `core/robots/rby1{a,m,ub}/parameters.h` (`robot_model_name`).
