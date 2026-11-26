---
layout: home

hero:
  name: RB-Y1
  text: 레인보우로보틱스 양팔 모바일 매니퓰레이터
  tagline: 개발자와 시스템 통합 담당자를 위한 매뉴얼, SDK, API 레퍼런스입니다.
  image:
    src: /hero-image.png
    alt: RB-Y1
  actions:
    - theme: brand
      text: 빠른 시작
      link: /ko/getting-started/estop-basics
    - theme: alt
      text: 하드웨어
      link: /hardware/overview
    - theme: alt
      text: API 레퍼런스
      link: /sdk/index

features:
  - icon: 🛑
    title: 빠른 시작
    details: 비상정지부터 개봉, 핫스팟·Web UI, SDK 설치까지 순서대로 안내합니다.
    link: /ko/getting-started/estop-basics
    linkText: 시작하기
  - icon: 🦺
    title: 안전
    details: 로봇을 운용하기 전에 읽어야 할 주의사항입니다.
    link: /precautions/index
    linkText: 주의사항
  - icon: 🦾
    title: 하드웨어
    details: 사양, 관절 범위·속도 한계, 옵션과 유지보수입니다.
    link: /hardware/index
    linkText: 하드웨어
  - icon: 🧭
    title: SDK 가이드
    details: 구조, 로봇 모델, 컨트롤러, 예제, 문제 해결입니다.
    link: /software/index
    linkText: SDK 가이드
  - icon: 📚
    title: API 레퍼런스
    details: rby1-sdk의 Python, C++, Protobuf(gRPC) API입니다.
    link: /sdk/index
    linkText: API 레퍼런스
  - icon: 🤖
    title: ROS 2
    details: rby1-ros2 드라이버, MoveIt 2 연동, 토픽과 서비스입니다.
    link: /ros2/index
    linkText: ROS 2
  - icon: 🛠️
    title: 유지보수·도구
    details: 소프트웨어 업데이트, 로그 백업, CAN·F/T 센서 점검, 부품 교체입니다.
    link: /maintenance/index
    linkText: 유지보수
  - icon: 🧪
    title: 시뮬레이션
    details: Docker에서 MuJoCo 모델로, 또는 Isaac Sim에서 로봇 소프트웨어를 실행합니다.
    link: /simulators/index
    linkText: 시뮬레이터
---

## 시작하기 전에

- **안전.** 처음 전원을 켜기 전에 [비상정지](/ko/getting-started/estop-basics)와 [안전](/precautions/index) 페이지를 읽고, 현장의 안전 규정을 따르십시오.
- **네트워크.** RB‑Y1 핫스팟이나 현장 네트워크로 연결합니다([핫스팟과 Web UI](/getting-started/hotspot-and-webui)).
- **SDK.** [rby1-sdk](https://github.com/RainbowRobotics/rby1-sdk)를 설치하고 로봇 상태를 읽을 수 있는지 확인합니다([SDK 설치](/getting-started/sdk-install-and-state)).

## 주요 특징

- **양팔 조작.** 7자유도 팔 두 개로 복잡한 작업을 동시에 수행합니다.
- **정밀도와 안정성.** 고정밀 구동기와 엔코더로 정확하고 반복 가능한 동작을 냅니다.
- **모듈형 설계.** 다양한 요구에 맞게 구성할 수 있습니다.
- **실시간 제어와 연동.** 결정적인 통신·제어와 상위 시스템·정책과의 명확한 연동 지점을 제공합니다.

## 지원과 라이선스

- **라이선스.** rby1-sdk는 Apache 2.0으로 배포되며 제3자 소프트웨어를 포함합니다. [오픈소스 라이선스 고지](/legal/third-party-notices)를 참고하십시오.
- **기술지원.** [GitHub Discussions](https://github.com/RainbowRobotics/rby1-sdk/discussions)에 문의하거나, 로그·재현 절차·소프트웨어 버전을 rby.support@rainbow-robotics.com으로 보내 주십시오.

[영어 매뉴얼](/)이 기준 문서입니다. 한국어 번역은 현재 일부 페이지만 제공합니다.
