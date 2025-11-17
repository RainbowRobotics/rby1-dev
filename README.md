# RBY1 Docs 개발 가이드

이 저장소는 RBY1 하드웨어/SDK 문서를 Sphinx로 빌드하기 위한 설정을 담고 있습니다.  
처음 합류한 팀원이 빠르게 시작할 수 있도록 문서 빌드 방법과 README 작성 팁을 정리했습니다.

## TL;DR – 문서 빌드

```bash
make -C doc clean                          # 이전 결과물 제거
make -C doc html SDK_TAG=dev              # dev 버전 HTML 빌드
open doc/build/html/dev/index.html        # macOS 기준 미리보기
xdg-open doc/build/html/dev/index.html    # Ubuntu GNOME 등 데스크톱 환경
```

## 처음 문서 빌드하기

1. **필수 도구 설치**
   - Python 3.10 이상, `make`, `git`, Docker(프로토/도큐젠 생성 시 필요) 를 설치합니다.
   - macOS(Homebrew) 예시:
     ```bash
     brew install python@3.11 git make
     ```
     Docker Desktop은 [공식 설치 가이드](https://docs.docker.com/desktop/mac/install/) 를 따라 설치합니다.
   - Ubuntu/Debian 계열 예시:
     ```bash
     sudo apt update
     sudo apt install -y python3 python3-venv python3-pip make git
     ```
     배포판별 Docker Engine 설치 방법은 [공식 문서](https://docs.docker.com/engine/install/) 를 참고하세요.
2. **저장소 복제 및 서브모듈 초기화**
   ```bash
   git clone git@github.com:RainbowRobotics/rby1-dev.git
   cd rby1-dev
   git submodule update --init --recursive
   ```
3. **가상 환경 구성**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -U pip
   python -m pip install -e .
   ```
   `pyproject.toml` 에 선언된 Sphinx 관련 의존성이 설치됩니다.
4. **처음 빌드 실행**
   ```bash
   make -C doc html SDK_TAG=dev
   ```
   - `SDK_TAG` 를 릴리스 태그(`v0.9.0` 등)로 바꾸면 버전별 HTML이 `doc/build/html/<SDK_TAG>` 에 생성됩니다.
   - 프로토 버전 문서나 Doxygen XML이 없는 경우, Makefile이 Docker를 이용해 자동 생성합니다.

## 기존 환경에서 다시 빌드하기

이미 가상 환경과 의존성이 준비된 상태라면 다음 순서로 최신 문서를 빌드합니다.

```bash
git pull origin main                                 # 최신 변경 사항 반영
git submodule update --init --recursive --checkout   # SDK 갱신
source .venv/bin/activate                             # 기존 가상 환경 재사용
pip install -e . --upgrade                            # (필요 시) 의존성 갱신
make -C doc clean                                     # 이전 산출물 제거
make -C doc html SDK_TAG=dev                          # HTML 재생성
```

`SDK_TAG` 을 원하는 버전으로 바꾸면 동일한 절차로 다른 버전도 곧바로 빌드할 수 있습니다.

## 자주 쓰는 Make 타겟

| 명령 | 설명 |
| --- | --- |
| `make -C doc html SDK_TAG=dev` | dev 태그 기준 전체 HTML 빌드 |
| `make -C doc clean` | Sphinx 빌드 산출물+생성 파일 제거 |
| `make -C doc clean-version SDK_TAG=v0.9.0` | 특정 태그에 해당하는 HTML만 정리 |
| `make -C doc protoc-doc` / `clean-proto` | `.proto` → Markdown 문서 생성/삭제 |
| `make -C doc doxygen-doc` / `clean-doxygen` | C++ Doxygen XML 생성/삭제 |

## 문서 버전 제어 환경 변수

`doc/source/conf.py` 는 아래 환경 변수를 읽어 빌드된 HTML의 버전 선택기와 링크를 구성합니다.

| 변수 | 역할 | 예시 |
| --- | --- | --- |
| `RBY1_SDK_VERSION` | 현재 빌드에 표시할 SDK 버전. `SDK_VERSION` 이 없을 때 사용되며 `make -C doc html SDK_TAG=...` 실행 시 자동으로 같게 설정됩니다. | `RBY1_SDK_VERSION=v0.9.0 make -C doc html` |
| `AVAILABLE_VERSIONS` | 버전 선택기 드롭다운에 표시할 버전 목록. 공백으로 구분합니다. | `AVAILABLE_VERSIONS="v0.8.0 v0.9.0 dev" make -C doc html` |
| `VERSION_BASE_PREFIX` | 호스팅 시 문서 루트 경로. GitHub Pages 등 서브 디렉터리에 배포할 때 사용합니다. | `VERSION_BASE_PREFIX="/docs/sdk/" AVAILABLE_VERSIONS="v0.9.0 dev" make -C doc html` |

일반적으로 `make -C doc html SDK_TAG=v0.9.0` 만 실행해도 동일한 효과를 얻지만, CI 파이프라인이나 커스텀 배포 스크립트에서는 위 값을 직접 지정해 원하는 버전 구조를 만들 수 있습니다.

## README 작성 가이드

문서/컴포넌트별 README는 다음 흐름을 권장합니다.

1. **제목 + 한 줄 요약**: 무엇을 다루는지 1–2줄로 소개합니다.
2. **TL;DR**: 핵심 명령어나 사용 방법을 코드 블록으로 제시합니다.
3. **빠른 시작(Quick Start)**: 설치, 환경 변수, 의존성 등 단계별 절차를 번호 목록으로 정리합니다.
4. **상세 설명**: 구조, 설계 의도, 주의 사항을 소제목으로 나누고 이미지/표를 활용합니다.
5. **트러블슈팅**: 자주 묻는 질문, 로그 확인 방법 등을 FAQ 형식으로 나눕니다.
6. **참고 링크**: SDK/하드웨어 스펙 문서, 관련 이슈나 위키 링크를 걸어둡니다.

예시 스켈레톤:

```markdown
# Motor Driver README

> 브러시리스 모터 드라이버 펌웨어 설정 가이드

## TL;DR
\`\`\`bash
make flash TARGET=motor_driver
\`\`\`

## Quick Start
1. ...
```

## Markdown 빠른 학습 리소스

- [Markdown Guide – Basic Syntax](https://www.markdownguide.org/basic-syntax/) : 가장 널리 쓰이는 문법 표와 예제가 정리되어 있습니다.

위 자료를 참고해 표, 코드 블록, 주석 등을 일관된 스타일로 유지해주세요.
