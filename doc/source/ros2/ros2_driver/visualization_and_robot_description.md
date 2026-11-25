# Visualization & Robot Description 

## RBY1 Description

You can use the robot's basic TF structure and state publisher through the commands below. When implementing features related to rby1, please use the model files from the corresponding package.

- **Parameters**:
  - `model_name` : `rby1a`, `rby1m`
  - `model_version`
    - `rby1a` : `1.0`, `1.1`, `1.2`
    - `rby1m` : `1.0`, `1.1`, `1.2`, `1.3`

```bash
source install/setup.bash
ros2 launch rby1_description rby1_state_publisher.launch.py model:=a version:=1_1
```

1. If you launch this command, you can see the following window:

```{image} ../../_static/images/ros2/state_checker_guide_1.png
    :width: 100%
    :align: center
    :class: white_bg
```

2. Click 'Add', and add plugins `TF` and `RobotModel`:

```{image} ../../_static/images/ros2/state_checker_guide_2.png
    :width: 100%
    :align: center
    :class: white_bg
```


3. Click 'Fixed Frame' and set to `base`:

```{image} ../../_static/images/ros2/state_checker_guide_3.png
    :width: 100%
    :align: center
    :class: white_bg
```


4. Click 'RobotModel', and select Topics -> `/robot_description`:

```{image} ../../_static/images/ros2/state_checker_guide_4.png
    :width: 100%
    :align: center
    :class: white_bg
```


5. You can now control the robot model using the joint state publisher GUI:

```{image} ../../_static/images/ros2/state_checker_guide_5.png
    :width: 100%
    :align: center
    :class: white_bg
```