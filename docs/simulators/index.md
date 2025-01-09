---
title: Simulators
outline: false
sidebar: false
prev: false
next: false
---

# 🚀 Explore the RBY1 Simulator!
Now available for both **ARM** and **x86** platforms in a **MuJoCo-based** Docker container.  
👉 [Get Started with ARM](https://hub.docker.com/r/rainbowroboticsofficial/rby1-sim-arm)  
👉 [Get Started with x86](https://hub.docker.com/r/rainbowroboticsofficial/rby1-sim)

## How to Use
- Install Docker Compose (if not installed)

```bash
sudo apt update
sudo apt install -y docker docker-compose-v2
```

- Use `ports` when the host and container networks are isolated (such as in WSL) and `network_mode: host` when the container can directly access the host network.
- For running the simulation, use `rainbowroboticsofficial/rby1-sim` if your system is x86-based, and `rainbowroboticsofficial/rby1-sim-arm` if your system is ARM-based (like our `U-PC`). This ensures compatibility with the underlying architecture of your system.

`docker-compose.sim.yaml`:
```yaml
version: '3.8'
services:
    rby1-sim-arm:
    image: rainbowroboticsofficial/rby1-sim
    environment:
        - DISPLAY=${DISPLAY}
    volumes:
        - /tmp/.X11-unix:/tmp/.X11-unix
    network_mode: host
```
- Use the `docker-compose.sim.yaml` file to start the container:
💡 **Tip**: This command will pull the `rby1-sim` image automatically if it’s not already downloaded.
```bash
docker compose -f docker-compose.sim.yaml up
```
- To stop the container, use:
```bash
docker compose -f docker-compose.sim.yaml down
```

