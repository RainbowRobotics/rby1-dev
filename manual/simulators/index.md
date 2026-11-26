# Simulation

Run the robot software against a simulated RB-Y1. The SDK and the ROS 2 driver connect to a simulator the same way they connect to the real robot:
over gRPC, at `localhost:50051` instead of the robot's address, with the model of the simulator image (`a`, `m`).
Test new programs in a simulator before you run them on the robot.

<div class="link-cards">

- [**MuJoCo**](mujoco.md)<br>Docker image with the robot software and a MuJoCo model. Every model and version.

- [**Isaac Sim**](isaac_sim.md)<br>RB-Y1 in NVIDIA Isaac Sim, with the robot software in the same container.

</div>
