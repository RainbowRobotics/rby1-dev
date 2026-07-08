(troubleshooting)=
# Troubleshooting & Known Issues

## Issue: MoveIt Known Issues

### ⚠️ Warning: `Missing gripper_finger_r2_joint` / `gripper_finger_l2_joint`

```
[WARN] The complete state of the robot is not yet known. Missing gripper_finger_r2_joint
```

**Cause**: `gripper_finger_r2_joint` and `gripper_finger_l2_joint` are **mimic joints** (linked to `r1`/`l1` via `<mimic>` in the URDF) and are not registered in `ros2_control`. The `joint_state_broadcaster` does not publish state for them, so MoveIt's planning scene monitor raises this warning.

**Impact**: **None** — motion planning and execution for all controlled joints works correctly. This warning can be safely ignored.

#### ⚠️ Hardware Control Handoff

When `ros2 launch rby1_moveit_* demo.launch.py` is launched with real hardware, the `RBY1SystemHardware` plugin calls `/hardware_control state:=true` to take exclusive control from the driver. During this period, direct action commands sent to the driver (e.g. `robot_joint`) will be rejected. Control is returned to the driver when MoveIt is shut down (`Ctrl+C`).

## Issue: Control Commands Rejected After Trajectory Stream Interruptions

* **Symptom**: 
  If a stream-based trajectory control node (e.g., using persistent trajectory streams) is suddenly terminated or killed mid-operation, the driver's stream state remains active. Until this stream mode is explicitly closed, the driver will reject all other incoming joint or Cartesian motion commands, resulting in errors.
  
* **Resolution**: 
  You must manually disable the streaming state by calling the `/stream_control` service with `state: false` in a separate terminal. This terminates the lingering stream and restores normal control capabilities.

  ```bash
  ros2 service call /stream_control rby1_msgs/srv/StateOnOff "{state: false}"
  ``` 

## Issue: Driver Shutdown on Startup due to Collision

* **Symptom**:
  If you launch the driver while the robot is already in a collision state (especially common when launching in simulation where default/initial joint states overlap), the driver will detect the collision and immediately log a FATAL error and terminate for safety.
  
* **Resolution**:
  Temporarily decrease the `collision_threshold` parameter in `driver_parameters.yaml` (e.g. to a very small value or `0.0`), launch the driver safely, command the robot joints to move to a safe, non-colliding pose, and then restore `collision_threshold` to its original value.

## Issue: Client-Side Warnings `Ignoring unexpected goal/result response`

* **Symptom**:
  When running sequential Python examples (e.g., `13_stream_command`), the terminal outputs warnings like `Ignoring unexpected goal response. There may be more than one action server for the action 'robot_joint'` or `Ignoring unexpected result response`.
  This occurs because:
  1. Persistent streaming makes the action server return success immediately. If the client completes the goal before the Python client-side state machine processes the goal acceptance, a race condition occurs.
  2. Standard blocking calls like `time.sleep()` prevent the ROS 2 executor thread from spinning, causing DDS status updates to accumulate and get processed out of order during the next goal spin.

* **Resolution**:
  1. The C++ driver has been updated to introduce a 50ms delay (`std::this_thread::sleep_for(std::chrono::milliseconds(50))`) before completing streaming commands to ensure the client-side state machine is ready.
  2. In your sequential Python nodes, avoid using standard `time.sleep()`. Instead, implement a non-blocking spin-sleep function (e.g., `rclpy.spin_once` in a loop) to keep draining the DDS network queue:
