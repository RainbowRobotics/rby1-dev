# RB-Y1 웹 매뉴얼 개발 가이드

RB-Y1 웹 매뉴얼(https://rainbowrobotics.github.io/rby1-dev/)의 소스입니다.
회사의 다른 제품 매뉴얼(협동로봇, RBQ, RB-S100)과 같은 **VitePress** 사이트이며,
Python·C++ API 레퍼런스는 rby1-sdk에서 **Sphinx**로 생성해 Markdown으로 넣습니다.

## 구조

| 경로 | 내용 |
| ---- | ---- |
| `manual/` | VitePress 사이트. 매뉴얼 페이지(`*.md`), 설정(`.vitepress/config.mts`), 테마, 이미지(`public/`) |
| `manual/scripts/generate_reference.py` | 빌드 때 생성되는 페이지: Python/C++ API, proto 페이지, 관절 범위·속도 표, Doxygen HTML |
| `manual/scripts/check_links.py` | 빌드 결과의 페이지 간 링크와 `#앵커`를 검사(CI에서 실행) |
| `doc/source/` | API 생성 원본: Sphinx 소스(`sdk/python`, `sdk/cpp`의 `.rst`)와 proto 페이지 생성 결과(`sdk/protos/generated`) |
| `doc/scripts/` | 관절 표 생성기, proto 페이지 생성기, 배포 스크립트(`publish_site.py`) |
| `external/rby1-sdk` | API를 생성하는 SDK 서브모듈. 태그로 고정(현재 v0.10.1) |
| `.github/workflows/docs.yml` | 모든 push/PR에서 빌드와 링크 검사. 라이브 배포는 dev에서 수동 실행할 때만 |

작업 브랜치는 `dev`입니다. 저장소의 옛 `main`(VitePress 소스, 2025)과 `gh-pages`(옛 빌드)는 더 쓰지 않습니다.

## 빌드

필요: Python 3.10 이상, [uv](https://docs.astral.sh/uv/), Node.js 22, Docker(Doxygen), git.

```bash
git clone -b dev --recurse-submodules https://github.com/RainbowRobotics/rby1-dev.git
cd rby1-dev
uv sync && source .venv/bin/activate
make -C doc html PYTHON=python                 # 결과: manual/.vitepress/dist
python manual/scripts/check_links.py manual/.vitepress/dist /rby1-dev/
```

매뉴얼 페이지만 고칠 때는 생성 단계를 한 번 실행한 뒤 개발 서버를 씁니다.

```bash
make -C doc reference PYTHON=python            # SDK 휠 설치, Doxygen, API·proto·관절 표 생성
cd manual && npm ci && npx vitepress dev       # http://localhost:5173/rby1-dev/
```

## 페이지 추가·수정

- 페이지는 `manual/` 아래 Markdown 파일입니다. URL은 파일 경로와 같습니다(`hardware/overview.md` → `/hardware/overview.html`).
- 사이드바와 상단 메뉴는 `manual/.vitepress/config.mts`에서 관리합니다. 새 페이지는 해당 섹션 사이드바에 추가합니다.
- 경고 상자는 `::: warning` … `:::`, 이미지는 `manual/public/images/`에 두고 `![설명](/images/...)`로 씁니다.
- 매뉴얼은 영어로만 유지합니다.
- 페이지를 옮기거나 합칠 때는 옛 파일을 지우지 말고, 새 위치로 안내하는 짧은 페이지로 남깁니다(frontmatter `search: false`, `sidebar: false`). 외부에서 그 URL로 들어오는 링크가 깨지지 않게 하기 위해서입니다.

### 생성되는 페이지는 원본을 고칩니다

| 사이트 경로 | 고칠 곳 |
| ----------- | ------- |
| `manual/sdk/python/generated/*` (클래스 페이지) | rby1-sdk의 Python 바인딩 docstring (`python/*.cpp`) |
| `manual/sdk/python/*/index`, `manual/sdk/cpp/**` | `doc/source/sdk/python`, `doc/source/sdk/cpp`의 `.rst`. C++ 선언 설명은 rby1-sdk 헤더의 Doxygen 주석 |
| `manual/sdk/protos/generated/*` | 메시지 설명·경고: `doc/source/sdk/protos/command_descriptions.json`, 형식: `doc/scripts/generate_proto_type_pages.py` |
| `manual/hardware/generated/*` | rby1-sdk의 URDF (`models/*/urdf`) |

이 폴더들은 git에 없고 빌드할 때마다 다시 만들어집니다.

## SDK 버전 올리기

```bash
make -C doc html SDK_TAG=v0.11.0 PYTHON=python   # 서브모듈을 태그로 바꾸고 해당 휠로 API 생성
git add external/rby1-sdk && git commit
```

이후의 `make -C doc html`은 서브모듈의 현재 태그를 그대로 씁니다.

proto가 바뀐 경우에는 `make -C doc protoc-doc`(Docker, sudo 불필요)으로 proto 페이지를 다시 만들고, `doc/source/sdk/protos/generated`와 `manual/sdk/protos/index.md`를 커밋합니다.
설명·경고·단위 같은 추가 문구는 생성된 페이지가 아니라 `doc/source/sdk/protos/command_descriptions.json` 또는 `type_notes.json`에 씁니다.
CI는 같은 명령으로 다시 생성해 커밋본과 다르면 실패합니다.

## 배포와 버전

GitHub Actions의 **Docs** 워크플로를 dev 브랜치에서 수동 실행하고 `publish`를 체크하면 `new-gh-pages`의 사이트 루트가 이 빌드로 바뀝니다(`doc/scripts/publish_site.py`).

사이트에는 최신 버전 하나만 둡니다. 한 빌드가 약 360 MB라 GitHub Pages 한도(1 GB) 안에 여러 버전을 둘 수 없고,
VitePress 빌드는 경로(base)가 고정되어 하위 폴더로 옮길 수 없기 때문입니다. 이전 버전의 변경 내용은 각 저장소의 GitHub 릴리스에서 봅니다.
