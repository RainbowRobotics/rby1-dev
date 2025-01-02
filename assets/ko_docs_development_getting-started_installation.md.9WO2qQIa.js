import{_ as e,c as n,a2 as t,o}from"./chunks/framework.Dpo7o-4l.js";const u=JSON.parse('{"title":"Installation","description":"","frontmatter":{"outline":"deep"},"headers":[],"relativePath":"ko/docs/development/getting-started/installation.md","filePath":"ko/docs/development/getting-started/installation.md"}'),s={name:"ko/docs/development/getting-started/installation.md"};function l(r,a,i,p,d,c){return o(),n("div",null,a[0]||(a[0]=[t(`<h1 id="installation" tabindex="-1">Installation <a class="header-anchor" href="#installation" aria-label="Permalink to &quot;Installation&quot;">​</a></h1><p>이 문서는 Rainbow Robotics SDK를 시작하는 데 필요한 하드웨어 및 소프트웨어 준비 단계를 안내합니다.</p><h2 id="hardware-preparation" tabindex="-1">Hardware Preparation <a class="header-anchor" href="#hardware-preparation" aria-label="Permalink to &quot;Hardware Preparation&quot;">​</a></h2><p>TBD</p><h2 id="software-installation" tabindex="-1">Software Installation <a class="header-anchor" href="#software-installation" aria-label="Permalink to &quot;Software Installation&quot;">​</a></h2><h3 id="requirements" tabindex="-1">Requirements <a class="header-anchor" href="#requirements" aria-label="Permalink to &quot;Requirements&quot;">​</a></h3><ul><li><strong>Supported OS:</strong> Ubuntu 22.04</li><li><strong>C++ Package Manager:</strong> Conan</li><li><strong>Build Tool:</strong> CMake &gt;= 3.30</li><li><strong>Python Package Manager:</strong> Poetry</li></ul><h3 id="cmake-설치" tabindex="-1">CMake 설치 <a class="header-anchor" href="#cmake-설치" aria-label="Permalink to &quot;CMake 설치&quot;">​</a></h3><p>CMake 버전 확인 및 설치 과정</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code># 현재 설치된 CMake 버전 확인
cmake --version

# CMake 버전이 3.30보다 낮다면, 기존 버전 삭제
sudo apt remove --purge cmake
sudo apt autoremove

# 최신 버전 설치
sudo snap install cmake --classic

# 설치된 CMake 버전 확인
cmake --version
</code></pre></div><h3 id="conan-설치" tabindex="-1">Conan 설치 <a class="header-anchor" href="#conan-설치" aria-label="Permalink to &quot;Conan 설치&quot;">​</a></h3><p>Conan이 이미 설치되어 있다면 이 단계를 생략할 수 있음.</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code># Conan 설치
pip install conan

# Conan 프로필 감지
conan profile detect --force
</code></pre></div><h3 id="poetry-설치" tabindex="-1">Poetry 설치 <a class="header-anchor" href="#poetry-설치" aria-label="Permalink to &quot;Poetry 설치&quot;">​</a></h3><p>Poetry가 이미 설치되어 있다면 이 단계를 생략할 수 있음.</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>curl -sSL https://install.python-poetry.org | python3 -
source ~/.profile

# Check
poetry --version
</code></pre></div><h3 id="sdk-설치" tabindex="-1">SDK 설치 <a class="header-anchor" href="#sdk-설치" aria-label="Permalink to &quot;SDK 설치&quot;">​</a></h3><p>Rainbow Robotics SDK를 설치하고 빌드하는 단계</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code># SDK 클론 및 서브모듈 초기화
git clone --recurse-submodules git@github.com:RainbowRobotics/rby1-sdk.git
</code></pre></div><h4 id="c-usage" tabindex="-1">C++ Usage <a class="header-anchor" href="#c-usage" aria-label="Permalink to &quot;C++ Usage&quot;">​</a></h4><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code># 의존성 패키지 설치
cd rby1-sdk
conan install . -s build_type=Release -b missing -of build

# CMake 프리셋 생성
cmake --preset conan-release -D BUILD_EXAMPLES=ON

# 빌드 수행
cmake --build --preset conan-release
</code></pre></div><h4 id="python-usage" tabindex="-1">Python Usage <a class="header-anchor" href="#python-usage" aria-label="Permalink to &quot;Python Usage&quot;">​</a></h4><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>cd rby1-sdk

# 관련 패키지 설치
poetry install

pip install .

# 가상환경 실행
poetry shell
</code></pre></div><h3 id="예제-프로그램-실행" tabindex="-1">예제 프로그램 실행 <a class="header-anchor" href="#예제-프로그램-실행" aria-label="Permalink to &quot;예제 프로그램 실행&quot;">​</a></h3><p>설치된 SDK를 사용하여 예제 프로그램을 실행</p><blockquote><p>⚠️ <strong>IMPORTANT WARNING</strong>: 실행 전 반드시 주변환경을 확인하세요.</p></blockquote><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code># C++ 예제 프로그램 실행
./build/examples/example_demo_motion [RPC IP]:50051

# poetry shell 상태에서
# demo_motion.py의 ROBOT_ADDRESS를 반드시 확인
python examples_python/demo_motion.py 
</code></pre></div>`,27)]))}const b=e(s,[["render",l]]);export{u as __pageData,b as default};
