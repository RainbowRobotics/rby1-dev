# Parameter

##

### `battery_config`

- battery_config는 배터리 잔량(level_percent) 계산 방식을 설정하는 7개 요소 배열입니다.
형식: [type, cutoff_voltage, fully_charged_voltage, coeff_0, coeff_1, coeff_2, coeff_3]

1. type
    0: 전압 기반 자동 계산 모드
    1: 수동 잔량 고정 모드 (test)
2. cutoff_voltage
    배터리 0% 기준 전압(V)
3. fully_charged_voltage
    배터리 100% 기준 전압(V)
4. coeff_0 ~ coeff_3
    전압→잔량 변환용 3차 다항식 계수
    계산식: percent = coeff_3*V^3 + coeff_2*V^2 + coeff_1*V + coeff_0

### `soft_stop_enabled`
soft_stop_enabled는 48V 전원 OFF 시 소프트 스톱 시퀀스를 사용할지 결정하는 플래그입니다.
타입: int (0 or 1)
기본값: 0

soft_stop_enabled
48v 전원을 끌 때 감속/안전 정지 루틴 적용 여부를 설정한다.

0: 소프트 스톱 미사용 (일반 전원 OFF)
1: 소프트 스톱 사용

1일 때 48v OFF 명령에서만 아래 순서가 실행됩니다.

1. Position lock 전환
2. 브레이크 체결
3. Gravity compensation 모드 전환
4. 약 0.5초 동안 보상비율을 1.0 -> 0.6으로 감소
5. 48v 전원 OFF


### `power_command.timeout`
전원 제어 명령 실행 후, 대상 전원 상태가 목표 상태(ON/OFF)로 일치할 때까지 대기하는 타임아웃 시간(초).

타입: double
기본값: 1.0
범위: 0.0 ~ 10.0
타임아웃 초과 시: 명령 실패(failed)로 처리


### `preset_position_command.new_data_timeout`
preset_position_command.new_data_timeout는 Preset Position 명령 전에 “관절 상태 데이터가 최신인지” 확인할 때 기다리는 최대 시간(초) 입니다.

Preset Position 실행 전, 대상 관절의 상태 데이터가 최신으로 갱신되기를 대기하는 타임아웃 시간(초).

타입: double
기본값: 3.0
범위: 0.0 ~ 10.0
타임아웃 내 최신 데이터가 안 들어오면: Preset Position 명령 실패(failed)


### `preset_position_command.timeout`
preset_position_command.timeout는 Preset Position 명령을 보낸 뒤, 대상 모터들이 preset 상태(pvl_preset == 0x01)가 될 때까지 기다리는 최대 시간(초) 입니다.

preset_position_command.timeout
Preset Position 명령 실행 후 대상 축의 preset 완료 상태를 확인하는 타임아웃 시간(초).

타입: double
기본값: 5.0
범위: 0.0 ~ 30.0
타임아웃 내 완료되지 않으면: 명령 실패(failed)

### `servo_on_command.timeout`
servo_on_command.timeout는 Servo On 명령 후, 대상 조인트가 준비 상태(is_ready)가 되고 최신 상태 데이터까지 들어올 때까지 기다리는 최대 시간(초) 입니다.

Servo On 실행 후 대상 축이 정상 준비 상태가 될 때까지 대기하는 타임아웃 시간(초).

타입: double
기본값: 15.0
범위: 0.0 ~ 30.0
타임아웃 내 조건 미충족 시: 명령 실패(failed)

### `servo_on_command.new_data_timeout`
servo_on_command.new_data_timeout는 Servo On/Off 명령 전에 대상 조인트의 상태 데이터가 최신으로 들어오는지 확인할 때 기다리는 최대 시간(초) 입니다.

Servo On(및 Servo Off) 실행 전, 대상 축의 상태 데이터 수신이 최신인지 확인하는 타임아웃 시간(초).

타입: double
기본값: 3.0
범위: 0.0 ~ 10.0
타임아웃 내 최신 데이터 미수신 시: 명령 실패(failed)


### `gravity`
gravity는 중력가속도 벡터 설정값입니다.

로봇 동역학 계산에 사용하는 중력가속도 벡터 [gx,gy,gz]를 설정한다. 이 값은 중력항(robot_state.gravity) 계산과 중력보상 feedforward 토크 계산에 반영된다.

타입: std::array<double, 3>
단위: m/s^2
기본값: [0, 0, -9.8]

### `default.acceleration_limit_scaling`
default.acceleration_limit_scaling는 기본 관절 가속도 제한 스케일입니다.

로봇 모델의 관절 가속도 한계값(qddot upper)에 곱해지는 기본 스케일 계수. 주로 최적제어/모션 생성 시 가속도 제한값을 조정하는 데 사용된다.

타입: double
기본값: 1.0
범위: 0.01 ~ 1.5

적용 개념:
기본 가속도 제한 = 조인트 가속도 한계 × default.acceleration_limit_scaling
(요청별 acceleration_limit_scaling이 있으면 여기에 추가로 곱해져 최종 제한이 결정됨)

### `default.angular_acceleration_limit`	
default.angular_acceleration_limit는 Cartesian 계열 명령에서 사용하는 기본 각가속도 제한값입니다.

Cartesian 목표 추종 시 회전(orientation) 축의 기본 각가속도 제한값. 각 타겟에 별도 값이 없으면 이 값을 사용하며, acceleration_limit_scaling이 함께 적용된다.

타입: double
기본값: 10.0
범위: 0.01 ~ 30.0
단위: 보통 rad/s² 기준으로 사용

### `default.cartesian_command.stop_joint_position_tracking_error`
Cartesian Command 종료 판단에 쓰는 조인트 위치 오차 임계값입니다.

Cartesian Command에서 joint position target을 함께 사용할 때, 각 대상 조인트의 위치 오차 |q - q_target|가 이 임계값보다 작아지면 추종 완료 조건으로 본다. 요청에 별도 stop_joint_position_tracking_error 파라미터 값이 없으면 이 기본값을 사용한다.

타입: double
기본값: 0.01
범위: 1e-3 ~ 0.1
단위: rad

### `default.cartesian_command.stop_orientation_tracking_error`	
Cartesian Command 종료 판단에 쓰는 자세(orientation) 추종 오차 임계값입니다.

Cartesian Command에서 목표 자세와 현재 자세의 오차가 이 값보다 작아지면 종료(도달) 조건을 만족한 것으로 판단한다. 요청에 stop_orientation_tracking_error를 따로 주지 않으면 이 기본값을 사용한다.

타입: double
기본값: 0.02
범위: 1e-3 ~ 0.1
단위: rad

### `default.cartesian_command.stop_position_tracking_error`	
Cartesian Command 종료 판단에 쓰는 위치(position) 추종 오차 임계값입니다.

Cartesian Command에서 목표 위치와 현재 위치의 오차가 이 값보다 작아지면 종료(도달) 조건을 만족한 것으로 판단한다. 요청에 stop_position_tracking_error를 따로 주지 않으면 이 기본값을 사용한다.

타입: double
기본값: 0.005
범위: 1e-4 ~ 1.0
단위: m (코드 주석은 mm로 표기돼 있어 문서에서는 단위를 한 번 통일해 두는 걸 권장)

### `default.cartesian_impedance_control_command.stop_joint_position_tracking_error`	

Cartesian Impedance Control에서 조인트 위치 추종 오차(|q - q_target|)의 종료 임계값입니다.
요청에 stop_joint_position_tracking_error가 없으면 이 기본값을 사용합니다.
오차가 임계값 이상이면 미도달, 임계값 미만이면 도달로 판단합니다.

기본값: 0.01
범위: 1e-3 ~ 0.1
단위: rad

### `default.cartesian_impedance_control_command.stop_orientation_tracking_error`	

Cartesian Impedance Control에서 자세(orientation) 추종 오차(orientation_error)의 종료 임계값입니다.
요청에 stop_orientation_tracking_error가 없으면 이 기본값을 사용합니다.
오차가 임계값 이상이면 미도달, 임계값 미만이면 도달로 판단합니다.

기본값: 0.02
범위: 1e-3 ~ 0.1
단위: rad

### `default.cartesian_impedance_control_command.stop_position_tracking_error`	

Cartesian Impedance Control에서 위치(position) 추종 오차(position_error)의 종료 임계값입니다.
요청에 stop_position_tracking_error가 없으면 이 기본값을 사용합니다.
오차가 임계값 이상이면 미도달, 임계값 미만이면 도달로 판단합니다.

기본값: 0.005
범위: 1e-4 ~ 1.0
단위: 코드 주석은 mm로 되어 있지만 계산은 일반적으로 m 기준입니다. 문서 단위는 프로젝트 기준으로 통일 권장.


### `default.linear_acceleration_limit`
Cartesian 계열 명령에서 선형(translation) 가속도 제한의 기본값입니다.
요청에 별도 선형 가속도 제한이 없으면 이 값을 사용합니다.

타입: double
기본값: 20.0
범위: 0.01 ~ 60.0
단위: m/s²

### `default.optimal_control_command.stop_cost`
Optimal Control Command에서 수렴(종료) 판정에 사용하는 cost 임계값입니다.
요청에 stop_cost가 없으면 이 기본값을 사용합니다. last_cost < stop_cost가 되면 수렴으로 간주하고 종료 절차로 들어갑니다.

타입: double
기본값: 1e-3
범위: 1e-6 ~ 1e9


### `default.se2_velocity_command.acceleration_limit`
SE2 Velocity Command에서 사용하는 기본 가속도 제한값입니다. 요청에 acceleration_limit를 따로 넣지 않으면 이 값을 사용합니다.

타입: std::array<double, 3>
기본값: [1.0, 5.0, 99.0]
구성 순서: [angular, linear.x, linear.y]
의미: 베이스의 각속도/선속도 목표로 가는 가속도 램프 제한


### `default.torque_limit_scaling`
로봇 모델의 관절 토크 한계값에 곱해지는 기본 스케일 계수입니다.

타입: double
기본값: 1.0
범위: 0.01 ~ 1.5
의미:
기본 토크 제한 = 모델 토크 한계 × default.torque_limit_scaling

### `default.velocity_limit_scaling`
로봇 모델의 관절 속도 한계값에 곱해지는 기본 스케일 계수입니다.

타입: double
기본값: 1.0
범위: 0.01 ~ 1.5
의미:
기본 속도 제한 = 모델 속도 한계 × default.velocity_limit_scaling

### `jog_command.one_step_size`
JogCommand의 one_step 모드에서 한 번 명령할 때 이동하는 조인트 각도 step 크기입니다.

타입: double
기본값: 0.087266463 (약 5 deg)
범위: 0.017453293 ~ 0.17453293 (1 ~ 10 deg)
단위: rad

### `jog_command.canceling_time`
JogCommand 취소(cancel) 시, 명령을 즉시 끊지 않고 부드럽게 감속해 종료하는 데 사용하는 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 10.0
단위: sec

### `joint_position_command.cutoff_frequency`
Joint Position Command에서 목표 위치/속도 생성 시 적용되는 저역통과필터(LPF) 컷오프 주파수입니다.

타입: double
기본값: 15
범위: 1e-3 ~ 100
단위: Hz
의미: 값이 클수록 더 빠르게 반응(덜 부드러움), 값이 작을수록 더 부드럽지만 응답이 느려짐

### `joint_position_command.canceling_time`
Joint Position Command 취소(cancel) 시, 목표를 즉시 끊지 않고 부드럽게 감쇠하며 종료하는 데 사용하는 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec

### `joint_group_position_command.canceling_time`
Joint Group Position Command 취소 시 목표를 즉시 끊지 않고 부드럽게 감쇠하며 종료하는 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec

### `joint_group_position_command.cutoff_frequency`	
Joint Group Position Command의 목표 생성/추종에 쓰는 저역통과필터(LPF) 컷오프 주파수입니다.

타입: double
기본값: 15
범위: 1e-3 ~ 100
단위: Hz

### `joint_impedance_control_command.canceling_time`
Joint Impedance Control Command 취소 시 부드럽게 종료하기 위한 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec

### `major_fault_power_off_target`
Major Fault 발생 시 PowerOff를 보낼 대상 전원/디바이스를 지정하는 정규식 문자열입니다.

타입: string
기본값: ".*"
의미: Major Fault 반응에서 hardware_->ExecutePowerCommand(power_off_target, kPowerOff)의 타깃 패턴으로 사용
주의:

앱에서 실제 전달은 "48v|" + major_fault_power_off_target 형태라, Major Fault 시 48v는 항상 포함되어 PowerOff 대상이 됩니다.

### `manipulability_threshold`
제어 중 특이점(singularity) 위험 판정에 사용하는 manipulability 임계값입니다.
현재 manipulability 값이 이 임계값을 넘으면 Singularity 상태로 실패 처리합니다.

타입: double
기본값: 1e4
범위: 1e2 ~ 1e10


### `cartesian_command.cutoff_frequency`
Cartesian Command에서 목표/명령을 저역통과필터(LPF)로 평활화할 때 쓰는 컷오프 주파수입니다.

타입: double
기본값: 15
범위: 1e-3 ~ 100
단위: Hz

### `cartesian_command.canceling_time`
Cartesian Command 취소 시 목표를 즉시 끊지 않고 부드럽게 감쇠하며 종료하는 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec

### `cartesian_impedance_control_command.canceling_time`
Cartesian Impedance Control Command 취소 시 부드럽게 종료하기 위한 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec

### `optimal_control_command.cutoff_frequency`
Optimal Control Command에서 목표/명령을 저역통과필터(LPF)로 평활화할 때 쓰는 컷오프 주파수입니다.

타입: double
기본값: 15
범위: 1e-3 ~ 100
단위: Hz

### `real_time_control.max_timeout_count`
Real-Time Control에서 명령 패킷 미수신 timeout을 몇 번까지 허용할지 정하는 최대 카운트입니다.

타입: int
기본값: 10
범위: 1 ~ 500
동작: 연속 timeout 횟수가 이 값 이상이면 제어를 안전 종료(finish = true)합니다.


### `stop_command.canceling_time`
Stop Command 수행 시 목표를 부드럽게 감쇠하며 정지시키는 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec

### `joint_velocity_command.canceling_time`
Joint Velocity Command 취소 시 속도 명령을 부드럽게 줄이며 종료하는 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec

### `se2_velocity_command.canceling_time`
SE2 Velocity Command 취소 시 베이스 속도 명령을 부드럽게 감쇠하며 종료하는 시간 상수입니다.

타입: double
기본값: 0.1
범위: 1e-3 ~ 1.0
단위: sec