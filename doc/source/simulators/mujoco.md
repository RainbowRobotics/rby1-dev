# MuJoCo

## Explore the RBY1 Simulator!

The RB-Y1 simulator runs the robot software (core) on a MuJoCo model in a Docker container.
Connect to it with the SDK or ROS 2 exactly as you would connect to the real robot.
One image supports both x86 (amd64) and ARM (arm64) hosts, including the `U-PC`.

👉 <a href="https://hub.docker.com/r/rainbowroboticsofficial/rby1-sim/tags" target="_blank" rel="noopener noreferrer">rainbowroboticsofficial/rby1-sim on Docker Hub</a>

## Choose an image tag

Each tag is `<core version>-<model>_v<hardware version>`. Pick the tag that matches your robot model and version
(check them in the Web UI or with `robot.get_robot_info()`).

| Robot | Tag (core 0.10.6, released 2026-04-06) |
| ----- | -------------------------------------- |
| Model A v1.0 / v1.1 / v1.2 | `0.10.6-a_v1.0` / `0.10.6-a_v1.1` / `0.10.6-a_v1.2` |
| Model M v1.0 / v1.1 / v1.2 / v1.3 | `0.10.6-m_v1.0` / `0.10.6-m_v1.1` / `0.10.6-m_v1.2` / `0.10.6-m_v1.3` |
| Model UB v1.0 | `0.10.6-ub_v1.0` |

```{warning}
Always give a tag. The image without a tag (`latest`) and the separate `rby1-sim-arm` image are old builds from 2025-03
and do not let you choose the robot model.
```

## How to Use

1. Install Docker and Docker Compose (if not installed).

   ```bash
   sudo apt update
   sudo apt install -y docker.io docker-compose-v2
   ```

2. Allow the container to open a window on your display (X11).

   ```bash
   xhost +local:
   ```

3. Create a file named `docker-compose.sim.yaml` with the content below. Replace the tag with the one for your robot.

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
   When the host and container networks are isolated (for example, in WSL), publish the ports with `ports` instead.

4. Start the simulator. Docker pulls the image the first time.

   ```bash
   docker compose -f docker-compose.sim.yaml up
   ```

   Without Compose, the same container starts with:

   ```bash
   docker run --rm -it --network host -e DISPLAY=$DISPLAY \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     rainbowroboticsofficial/rby1-sim:0.10.6-a_v1.2
   ```

5. Stop the simulator.

   ```bash
   docker compose -f docker-compose.sim.yaml down
   ```
