# Error Reporting

Report problems so that we can fix them. Which channel to use depends on the problem; the [Support](../../../support.md) page has the full list.

| Problem | Where to report |
| --- | --- |
| A bug in the SDK: wrong behavior, a crash, a wrong API description | [rby1-sdk GitHub Issues](https://github.com/RainbowRobotics/rby1-sdk/issues) |
| Questions, and runtime errors you want to discuss with other users | [rby1-sdk GitHub Discussions](https://github.com/RainbowRobotics/rby1-sdk/discussions) |
| Hardware faults, repairs, firmware, or anything that needs your robot's serial number or private data | E-mail `rby.support@rainbow-robotics.com` |

GitHub Issues and Discussions are public. Do not post serial numbers, IP addresses of your network or other private data there; use e-mail for these.

## Before you report

Collect this information. It lets us reproduce the problem without asking you again.

- **Robot:** model (A, M or UB) and hardware version (for example v1.2).
- **Versions:** the robot software version and the SDK version. In Python:

  ```python
  import rby1_sdk as rby

  print("SDK on this PC:", rby.__version__)
  robot = rby.create_robot("192.168.30.1:50051", "a")  # your address and model
  robot.connect()
  info = robot.get_robot_info()
  print("Robot software:", info.version, "| SDK on the robot:", info.sdk_version)
  print("Robot model:", info.robot_model_name, info.robot_model_version)
  ```

- **Steps:** what you did, what you expected and what happened. Attach the smallest code that shows the problem.
- **Control Manager state and log:** the state when the problem happened and the related log lines. See [Fault Diagnosis](../fault-diagnosis.md).
- **Fault log:** if the Control Manager went to `MajorFault`, the fault log file (`fault-*.csv`) of that time. Download it with the [17_fault_log](../../../examples/ex.md) example.
- **Robot logs:** for problems that are hard to describe, the logs from [Log Backup](../../../rpc_management_tools/log_backup.md).

::: tip
Your reports help us improve the SDK and the robot software. Thank you.
:::

Verified against: rby1-sdk v0.10.1 `python/rby1_sdk/__init__.py` (`__version__`), `python/robot_info.cpp` (`version`, `sdk_version`, `robot_model_name`, `robot_model_version`), `examples/python/17_fault_log.py`; robot core `core/robots/robot_app_base.cpp` (fault log file name).
