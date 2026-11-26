# RB-Y1 웹 매뉴얼 개발 가이드

RB-Y1 웹 매뉴얼(https://rainbowrobotics.github.io/rby1-dev/)의 소스입니다.
회사의 다른 제품 매뉴얼(협동로봇, RBQ, RB-S100)과 같은 **VitePress** 사이트이며,
Python·C++ API 레퍼런스는 rby1-sdk에서 **Sphinx**로 생성해 Markdown으로 넣습니다.

## 구조

| 경로 | 내용 |
| ---- | ---- |
| `manual/` | VitePress 사이트. 매뉴얼 페이지(`*.md`), 설정(`.vitepress/config.mts`), 테마, 이미지(`public/`) |
| `manual/scripts/generate_reference.py` | 빌드 때 생성되는 페이지: Python/C++ API, proto 페이지, 관절 범위·속도 표, Doxygen HTML |
| `doc/source/` | API 생성용 Sphinx 소스(`sdk/python`, `sdk/cpp`)와 proto 생성 결과(`sdk/protos/generated`) |
| `doc/scripts/` | 관절 표 생성기, proto 페이지 생성기, 버전별 배포 스크립트(`publish_site.py`) |
| `external/rby1-sdk` | API를 생성하는 SDK 서브모듈. 태그로 고정(현재 v0.10.1) |
| `.github/workflows/docs.yml` | 모든 push/PR에서 빌드. 라이브 배포는 dev에서 수동 실행할 때만 |

## 빌드

필요: Python 3.10 이상, [uv](https://docs.astral.sh/uv/), Node.js 22, Docker(Doxygen), git.

```bash
git clone --recurse-submodules https://github.com/RainbowRobotics/rby1-dev.git
cd rby1-dev
uv sync && source .venv/bin/activate
make -C doc html PYTHON=python          # 결과: manual/.vitepress/dist
```

매뉴얼 페이지만 고칠 때는 생성 단계를 한 번 실행한 뒤 개발 서버를 씁니다.

```bash
python manual/scripts/generate_reference.py   # API·proto·관절 표 생성 (doc/build/doxygen 필요: make -C doc doxygen-doc)
cd manual && npm ci && npx vitepress dev      # http://localhost:5173/rby1-dev/
```

## 페이지 추가·수정

- 페이지는 `manual/` 아래 Markdown 파일입니다. URL은 파일 경로와 같습니다(`hardware/overview.md` → `/hardware/overview.html`).
- 사이드바와 상단 메뉴는 `manual/.vitepress/config.mts`에서 관리합니다. 새 페이지는 해당 섹션 사이드바에 추가합니다.
- 경고 상자는 `::: warning` … `:::`, 이미지는 `manual/public/images/`에 두고 `![설명](/images/...)`로 씁니다.
- 한국어 페이지는 `manual/ko/` 아래 같은 경로에 둡니다.
- 생성되는 폴더(`manual/sdk/python`, `manual/sdk/cpp`, `manual/sdk/protos/generated`, `manual/hardware/generated`)는 직접 고치지 않습니다.

## SDK 버전 올리기

```bash
make -C doc html SDK_TAG=v0.11.0 PYTHON=python   # 서브모듈을 태그로 바꾸고 해당 휠로 API 생성
git add external/rby1-sdk && git commit
```

proto가 바뀐 경우에는 `make -C doc protoc-doc`으로 proto 페이지를 다시 만들고 결과를 커밋합니다.

## 배포

GitHub Actions의 **Docs** 워크플로를 dev 브랜치에서 수동 실행하고 `publish`를 체크하면 `new-gh-pages`에 배포됩니다.
최신 버전은 사이트 루트에, 이전 버전은 `/<버전>/`에 남고 `versions.json`이 갱신됩니다(`doc/scripts/publish_site.py`).

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
