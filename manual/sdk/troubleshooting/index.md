# Troubleshooting

Start here when something does not work. The sections below cover connection problems. The other pages cover the rest:

- [Fault Diagnosis](./fault-diagnosis.md): the Control Manager does not enable, goes to a fault, or a command fails.
- [Build Issues](./generated/build_issue.md): building the SDK from source fails.
- [FAQ](./generated/faq.md): commands, priorities, streams and the leader arm.
- [Error Reporting](./generated/error_reporting.md): what to send when you ask for help.

## SDK cannot connect

`robot.connect()` returns `False`, or the examples print "Failed to connect robot".

1. **Check the address.** The SDK connects to the robot PC (RPC) on port **50051**. Use the address that matches your network:

   | Your PC is on | Address |
   | --- | --- |
   | The robot hotspot ([Hotspot & Web UI](../../getting-started/hotspot-and-webui.md)) | `192.168.12.1:50051` |
   | Your Wi-Fi network ([External Access Point](../../getting-started/connect-external-ap.md)) | `<IP shown in the Web UI>:50051` |
   | The user PC (UPC) inside the robot | `192.168.30.1:50051` |
   | The same PC as a simulator ([Simulation](../../simulators/index.md)) | `localhost:50051` |

2. **Check the network.** Ping the robot. If the ping fails, check that your PC is on the same subnet, try a wired connection or another cable, and check the firewall of your PC.

   ```bash
   ping 192.168.12.1
   ```

3. **Check that the robot software is running.** Test the port. If the ping works but the port is closed, the robot software on the RPC is not running yet; wait until boot is finished, or restart the robot.

   ```bash
   nc -vz 192.168.12.1 50051
   ```

4. **Check the SDK on your PC.** Activate the Python environment in which you installed `rby1-sdk`, and check the version:

   ```bash
   python -c "import rby1_sdk; print(rby1_sdk.__version__)"
   ```

5. **Check the model argument.** The second argument of `create_robot()` (or `--model` in the examples) must match your robot: `a`, `m` or `ub`.

## SDK and robot software versions

After you connect, compare the SDK version on your PC with the versions on the robot:

```python
import rby1_sdk as rby

robot = rby.create_robot("192.168.12.1:50051", "a")  # your address and model
robot.connect()
info = robot.get_robot_info()
print("SDK on this PC:", rby.__version__)
print("Robot software:", info.version, "| SDK on the robot:", info.sdk_version)
```

If a function of the SDK fails although the connection works, a version difference can be the cause. Update the SDK on your PC or the robot software ([RPC Updater](../../rpc_management_tools/rpc_updater.md)) so that they match, and include both versions when you [report the problem](./generated/error_reporting.md).

## Cannot reach the Web UI

- Join the robot hotspot again and check the SSID and the password. See [Hotspot & Web UI](../../getting-started/hotspot-and-webui.md).
- On an external network, check the IP address of the robot in the network settings ([External Access Point](../../getting-started/connect-external-ap.md)).

Verified against: robot core `core/main.cpp` (gRPC server on `0.0.0.0:50051`); rby1-sdk v0.10.1 `python/robot.cpp` (`connect`, `get_robot_info`), `python/robot_info.cpp`, `python/rby1_sdk/__init__.py` (`create_robot` models `a`, `m`, `ub`, `__version__`), `examples/python/00_helper.py`.
