# Supported Platforms

Where the RB-Y1 software runs, and which versions this site documents.

## Python SDK (rby1-sdk 0.10.1)

`pip install rby1-sdk==0.10.1` installs a prebuilt wheel on these platforms:

| OS | CPU | Requirement | Python |
| --- | --- | --- | --- |
| Linux | x86_64 | glibc 2.35 or later (Ubuntu 22.04, 24.04 or newer) | 3.10 – 3.13 |
| Linux | aarch64 (ARM64), for example the UPC | glibc 2.35 or later (for example JetPack 6, based on Ubuntu 22.04) | 3.10 – 3.13 |
| Windows | x64 | 64-bit Python | 3.10 – 3.13 |
| macOS | Apple Silicon (arm64) | macOS 14 or later | 3.10 – 3.13 |

- Python 3.10 or later is required (`requires_python >=3.10, <4.0`).
- The SDK depends on `numpy` 2.x (`>=2.0.1, <3.0.0`).
- There is no wheel for Linux with glibc older than 2.35 (for example Ubuntu 20.04 or JetPack 5),
  Intel Macs, 32-bit systems or Python 3.14. On these, `pip` falls back to the source package, which needs
  CMake, Conan and a C++ compiler, and may fail. Use a supported platform, or build the SDK from source
  ([C++ build guide](../sdk/cpp/build-and-link.md)).

Check the installed version:

```bash
python -c "import rby1_sdk; print(rby1_sdk.__version__)"
```

## C++ SDK

The C++ SDK is built from source with CMake and Conan. See [Build and Link](../sdk/cpp/build-and-link.md).

## ROS 2 (rby1-ros2 v1.0.0)

| Item | Supported |
| --- | --- |
| ROS 2 | Humble on Ubuntu 22.04 (recommended), Jazzy on Ubuntu 24.04 |
| SDK | rby1-sdk 0.10.x or later, C++ SDK built from source (`RBY1_SDK_PATH`) |

See [ROS 2 Install & Build](../ros2/ros2_driver/install_and_build.md).

## Simulator (rby1-sim Docker image)

- Images for x86_64 (amd64) and ARM64 (arm64) hosts.
- One tag per robot software version, model and hardware version, for example `0.10.6-a_v1.2`.
  The newest tags on Docker Hub are for robot software 0.10.6.

See [MuJoCo](../simulators/mujoco.md).

## Versions of the robot

Check what your robot runs:

- **Robot software (core) version**: `robot.get_robot_info().version` in the SDK.
  The `robot_version` field is deprecated and holds the model name, not the software version.
- **Model and hardware version**: `robot.get_robot_info().robot_model_name` and `robot_model_version`.
- **SDK version on your PC**: `rby1_sdk.__version__`.

A compatibility table between SDK versions and robot software versions is not published.
Check the release notes of the robot software and of rby1-sdk before you update one of them,
and update the robot software with the [RPC Updater](../rpc_management_tools/rpc_updater.md).

---

Verified against: PyPI `rby1-sdk` 0.10.1 JSON (wheel files `cp310`–`cp313` × `manylinux_2_35_x86_64`,
`manylinux_2_35_aarch64`, `win_amd64`, `macosx_14_0_arm64`/`15_0`/`26_0`; `requires_python <4.0,>=3.10`;
`numpy<3.0.0,>=2.0.1`), checked 2026-11-26; rby1-sdk v0.10.1 `pyproject.toml`, `python/rby1_sdk/__init__.py`
(`__version__`), `python/robot_info.cpp` (`version`, `robot_version` deprecated, `robot_model_name`, `robot_model_version`);
rby1-ros2 v1.0.0 `README.md`; Docker Hub `rainbowroboticsofficial/rby1-sim` tags (amd64 and arm64, newest 0.10.6),
checked 2026-11-26.
