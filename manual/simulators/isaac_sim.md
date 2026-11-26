# Isaac Sim

This page explains how to run the RB-Y1 in NVIDIA Isaac Sim and connect `rby1-sdk` or the ROS 2 driver to it.

- Related repository: <a href="https://github.com/RainbowRobotics/rby1-sim-isaac" target="_blank" rel="noopener noreferrer">RBY1 Isaac Sim on GitHub</a>

<img :src="$withBase('/images/simulator/isaac_sim/isaac_sim.png')" alt="" class="center white-bg" style="width:80%">

## How the SDK connects

In SDK mode (`docker/run_sdk.sh`) the container runs Isaac Sim and the robot software (rby1 core, `app_main isaac`) together:

```
rby1-sdk / ROS 2 driver  --gRPC :50051-->  rby1 core (app_main isaac)  --UDP 5006 / 5005-->  Isaac Sim
```

Your program connects to the core at `localhost:50051` over gRPC, exactly as it connects to a real robot.
The UDP ports `5005` and `5006` are used between the core and Isaac Sim inside the simulator; your program does not use them.

## Requirements

* NVIDIA GPU + driver
* [Docker](https://docs.docker.com/engine/install/)
* [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/RainbowRobotics/rby1-sim-isaac.git
cd rby1-sim-isaac
```

### 2. Run

| Script | Robot control | Robot UDP bridge | `app_main isaac` (rby1 core) |
|--------|---------------|------------------|------------------|
| `docker/run.sh` | Built-in standalone PD trajectory | Disabled by default | Not started |
| `docker/run_sdk.sh` | rby1-sdk / rby1 core commands | Enabled | Started automatically |

#### SDK mode

Runs Isaac Sim and the rby1 core, so the SDK and the ROS 2 driver can control the robot.

```bash
./docker/run_sdk.sh --image 0.11.0-a_v1.2-isaac6.2.0   # Model A v1.2
./docker/run_sdk.sh --image 0.11.0-m_v1.2-isaac6.2.0   # Model M v1.2
./docker/run_sdk.sh --image 0.11.0-a_v1.2-isaac6.2.0 --gripper --gripper-name rb_gripper   # with the gripper
HEADLESS=1 ./docker/run_sdk.sh --image 0.11.0-a_v1.2-isaac6.2.0                            # no GUI window
```

The default launch uses the robot without a gripper. Arguments after `--image` are passed to the simulation:
`--gripper --gripper-name <name>` mounts a gripper. `HEADLESS=1` runs without windows, which keeps the simulation close to real time.
The other run options are in the [repository README](https://github.com/RainbowRobotics/rby1-sim-isaac#run-options).

#### Standalone mode

Runs Isaac Sim only. The robot follows the built-in PD trajectory; no rby1 core is started, and the SDK cannot connect.

```bash
./docker/run.sh --image 0.11.0-a_v1.2-isaac6.2.0   # Model A v1.2
./docker/run.sh --image 0.11.0-m_v1.2-isaac6.2.0   # Model M v1.2
```

### 3. Connect the SDK or ROS 2

With `run_sdk.sh` running, connect to `localhost:50051` with the model of the image (`a` or `m`):

```bash
# SDK (Python example from rby1-sdk/examples/python)
python 01_hello_rby1.py --address localhost:50051 --model a

# ROS 2 driver
ros2 launch rby1_driver rby1_ros2_driver.launch.py robot_ip:=localhost:50051 model:=a
```

::: tip
The core listens on port `50051` of the host (the container uses the host network).
Do not run the [MuJoCo simulator](mujoco.md) or another core on the same PC at the same time.
:::

## Supported images

Each image loads the robot model matching its tag, so no extra flag is needed.

| Tag | Model | Isaac Sim | rby1 core |
|-----|-------|-----------|-----------|
| `0.11.0-a_v1.2-isaac6.2.0` (recommended) | Model A v1.2 | 6.2.0 | 0.11.0 |
| `0.11.0-m_v1.2-isaac6.2.0` (recommended) | Model M v1.2 | 6.2.0 | 0.11.0 |
| `0.10.7-a_v1.2-isaac6.1.0-r1` | Model A v1.2 | 6.1.0 | 0.10.7, rebuild 1 |
| `0.10.7-m_v1.2-isaac6.1.0-r1` | Model M v1.2 | 6.1.0 | 0.10.7, rebuild 1 |
| `0.10.7-a_v1.2-isaac6.1.0` | Model A v1.2 | 6.1.0 | 0.10.7 |
| `0.10.7-m_v1.2-isaac6.1.0` | Model M v1.2 | 6.1.0 | 0.10.7 |
| `0.10.7-a_v1.2` | Model A v1.2 | 5.1.0 | 0.10.7 |
| `0.10.7-m_v1.2` | Model M v1.2 | 5.1.0 | 0.10.7 |

Docker Hub also has `0.11.0-m_v1.3-isaac6.2.0`; the repository README does not list it yet.

::: warning Isaac Sim 5.1 images on RTX 5090
The Isaac Sim 5.1 images (`0.10.7-a_v1.2`, `0.10.7-m_v1.2`) crash in the RTX renderer at startup on an RTX 5090 with driver 615.71, also headless.
Use the Isaac Sim 6.x images there.
:::

## Docker image tag convention

```
rainbowroboticsofficial/rby1-sim-isaac:<version>-<model>_v<model_version>[-isaac<isaac_version>][-r<rebuild>]

rainbowroboticsofficial/rby1-sim-isaac:0.11.0-a_v1.2-isaac6.2.0      # Model A v1.2, Isaac Sim 6.2.0
rainbowroboticsofficial/rby1-sim-isaac:0.10.7-a_v1.2-isaac6.1.0-r1   # Model A v1.2, Isaac Sim 6.1.0, rebuild 1
rainbowroboticsofficial/rby1-sim-isaac:0.10.7-a_v1.2                 # Model A v1.2, Isaac Sim 5.1.0
```

`-r<rebuild>`: the same release and Isaac Sim version, rebuilt with a newer rby1 core.

## UDP ports

The container uses the host network (`--network=host`), so these ports are open on the host.

| Port | Direction | Description |
|------|-----------|-------------|
| `5005/udp` | Isaac Sim → rby1 core | Robot state |
| `5006/udp` | rby1 core → Isaac Sim | Robot command |
| `5007/udp` | User code → Isaac Sim | Gripper command |
| `5008/udp` | Isaac Sim → User code | Gripper state |

## Gripper example

`examples/gripper_example.py` controls the gripper with the same code in the simulator and on the real robot.
The `SimDynamixelBus` class in `src/sim_gripper_bridge.py` provides the same interface as `rby1_sdk.DynamixelBus`; `--sim` selects it.

**In Isaac Sim**: start the simulator with a gripper mounted, then run the example on the host:

```bash
./docker/run_sdk.sh --image 0.11.0-a_v1.2-isaac6.2.0 --gripper --gripper-name rb_gripper
cd examples
pip install numpy
python3 gripper_example.py --sim
```

**On the real robot**: run the example on the UPC, where the gripper's USB is plugged in. It needs `rby1-sdk` installed there (`rby1_sdk.DynamixelBus` on the UPC's gripper device).

::: danger
On the real robot the gripper fingers move. Keep fingers and objects out of the gripper, and keep the E-Stop within reach.
:::

## License

See the [repository](https://github.com/RainbowRobotics/rby1-sim-isaac) for its license terms.

Verified against: rby1-sim-isaac main `README.md` (pushed 2026-11-05), `docker/run_sdk.sh`, `examples/gripper_example.py`; Docker Hub tags of `rainbowroboticsofficial/rby1-sim-isaac` (2026-11-26); rby1-sdk v0.10.1 `examples/python/01_hello_rby1.py`.
