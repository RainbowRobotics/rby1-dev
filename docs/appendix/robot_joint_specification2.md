

# Robot Joint Specification

![Kinematic structure of RB-Y1 and name of the joint.](/images/robot_joint_spec.png)
*Figure 1: Kinematic structure of RB-Y1 and name of the joint.*


| **Type**| [**32**](#type-32) | [**25**](#type-25) | [**20**](#type-20) | [**17**](#type-17) | [**14N**](#type-14) | [**14C**](#type-14c) |
|-----------------------------------|--------|--------|--------|--------|---------|---------|
| **Continuous Torque(Nm)**         | 250    | 125    | 100    | 65     | 35      | 14      |
| **Repeated Peak Torque(Nm)**      | 433    | 204    | 107    | 70     | 36      | 36      |
| **Momentary Peak Torque(Nm)**     | 841    | 369    | 191    | 143    | 70      | 70      |
| **Gear Ratio**                    | 101:1  | 101:1  | 101:1  | 101:1  | 101:1   | 100:1   |
| **Output Speed(°/s)**             | 120    | 180    | 180    | 180    | 180     | 360     |
| **Motor Encoder Resolution(bit)** | 14     | 14     | 14     | 14     | 14      | 14      |
| **Transmission Error(arcsec)**    | ~50    | ~50    | ~50    | ~50    | ~50     | ~50     |
| **Stiffness(Nm/rad)**             | 110000 | 50000  | 25000  | 14000  | 6100    | 6100    |
| **Motor Torque(Nm/A)**        | 0.15   | 0.1    | 0.1    | 0.1    | 0.09    | 0.05    |


## Joint Types

### Type 32

- Ankle Roll
- Ankle Pitch

### Type 25

- Knee Pitch
- Hip Roll
- Hip Pitch
- Hip Yaw

### Type 20

- Shoulder Pitch (R and L)
- Shoulder Roll (R and L)

### Type 17

- Shoulder Yaw (R and L)

### Type 14N

- Elbow Pitch (R and L)

### Type 14C

- Wrist Yaw1 (R and L)
- Wrist Yaw2 (R and L)
- Wrist Yaw3 (R and L)