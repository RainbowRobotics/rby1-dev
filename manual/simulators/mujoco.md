# MuJoCo

## Explore the RBY1 Simulator!

The RB-Y1 simulator runs the robot software (core) on a MuJoCo model in a Docker container.
The SDK and ROS 2 connect to it over gRPC on port `50051`, the same way they connect to the real robot (see [Connect the SDK or ROS 2](#connect-the-sdk-or-ros-2)).
One image supports both x86 (amd64) and ARM (arm64) hosts, including the user PC (UPC).

👉 <a href="https://hub.docker.com/r/rainbowroboticsofficial/rby1-sim/tags" target="_blank" rel="noopener noreferrer">rainbowroboticsofficial/rby1-sim on Docker Hub</a>

## Choose an image tag

Each tag is `<core version>-<model>_v<hardware version>`. Pick the tag that matches your robot model and version
(check them in the Web UI or with `robot.get_robot_info()`).

| Robot | Tag (core 0.10.6, released 2026-04-06) |
| ----- | -------------------------------------- |
| Model A v1.0 / v1.1 / v1.2 | `0.10.6-a_v1.0` / `0.10.6-a_v1.1` / `0.10.6-a_v1.2` |
| Model M v1.0 / v1.1 / v1.2 / v1.3 | `0.10.6-m_v1.0` / `0.10.6-m_v1.1` / `0.10.6-m_v1.2` / `0.10.6-m_v1.3` |
| Model UB v1.0 | `0.10.6-ub_v1.0` (SDK only: the ROS 2 driver supports Model A and M) |

::: warning
Always give a tag. The image without a tag (`latest`) and the separate `rby1-sim-arm` image are old builds from 2025-03
and do not let you choose the robot model.
:::

## How to Use

1. Install Docker and Docker Compose (if not installed).

   ```bash
   sudo apt update
   sudo apt install -y docker.io docker-compose-v2
   ```

2. Let your user run Docker without `sudo`, then log out and log in again (or reboot) so the group takes effect.
   The commands below run without `sudo`.

   ```bash
   sudo usermod -aG docker $USER
   ```

3. Allow the container to open a window on your display (X11).

   ```bash
   xhost +local:
   ```

4. Create a file named `docker-compose.sim.yaml` with the content below. Replace the tag with the one for your robot.

   ```yaml
   services:
     rby1-sim:
       image: rainbowroboticsofficial/rby1-sim:0.10.6-a_v1.2
       environment:
         - DISPLAY=${DISPLAY}
       volumes:
         - /tmp/.X11-unix:/tmp/.X11-unix
       network_mode: host
   ```

   `network_mode: host` lets the SDK on the same computer connect to the simulator.
   When the host and container networks are isolated (for example, in WSL), publish the gRPC port instead of `network_mode: host`:

   ```yaml
       ports:
         - "50051:50051"
   ```

5. Start the simulator. Docker pulls the image the first time.

   ```bash
   docker compose -f docker-compose.sim.yaml up
   ```

   Without Compose, the same container starts with:

   ```bash
   docker run --rm -it --network host -e DISPLAY=$DISPLAY \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     rainbowroboticsofficial/rby1-sim:0.10.6-a_v1.2
   ```

6. Stop the simulator.

   ```bash
   docker compose -f docker-compose.sim.yaml down
   ```

## Connect the SDK or ROS 2

The simulator's address is `localhost:50051` (or `127.0.0.1:50051`). Give the same model as the image tag (`a`, `m` or `ub`).
From another computer, use the address of the computer that runs the container (see [Network and Ports](../getting-started/network-and-ports.md#simulator)).

```bash
# SDK (Python example from rby1-sdk/examples/python)
python 01_hello_rby1.py --address localhost:50051 --model a

# ROS 2 driver (Model A or M images only)
ros2 launch rby1_driver rby1_ros2_driver.launch.py robot_ip:=localhost:50051 model:=a
```

See [Install & Build](../ros2/ros2_driver/install_and_build.md) for the ROS 2 driver.

Verified against: Docker Hub tags of `rainbowroboticsofficial/rby1-sim` (2026-11-26), rby1-sdk v0.10.1 `examples/python/01_hello_rby1.py` and `python/rby1_sdk/__init__.py` (`create_robot`), rby1-ros2 v1.0.0 `README.md` (simulator, port 50051) and `rby1_driver/src/main.cpp` (models a, m).
