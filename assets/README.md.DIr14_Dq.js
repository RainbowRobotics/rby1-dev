import{_ as e,c as o,a2 as t,o as s}from"./chunks/framework.Dpo7o-4l.js";const h=JSON.parse('{"title":"rby1-docs","description":"","frontmatter":{},"headers":[],"relativePath":"README.md","filePath":"README.md"}'),n={name:"README.md"};function c(r,a,d,p,l,i){return s(),o("div",null,a[0]||(a[0]=[t(`<h1 id="rby1-docs" tabindex="-1">rby1-docs <a class="header-anchor" href="#rby1-docs" aria-label="Permalink to &quot;rby1-docs&quot;">​</a></h1><h2 id="install" tabindex="-1">Install <a class="header-anchor" href="#install" aria-label="Permalink to &quot;Install&quot;">​</a></h2><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>git clone --recurse-submodules git@github.com:RainbowRobotics/rby1-docs.git
</code></pre></div><h2 id="docs" tabindex="-1">Docs <a class="header-anchor" href="#docs" aria-label="Permalink to &quot;Docs&quot;">​</a></h2><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>brew install go
go version
go install github.com/pseudomuto/protoc-gen-doc/cmd/protoc-gen-doc@latest
echo &#39;export PATH=$PATH:$HOME/go/bin&#39; &gt;&gt; ~/.zshrc
source ~/.zshrc
protoc-gen-doc --version
cd rby-sdk/protos
 ../../../protoc/bin/protoc -I=. --doc_out=./docs --doc_opt=html,protos.html rb/api/*.proto
 ../../../protoc/bin/protoc -I=. --doc_out=./docs --doc_opt=markdown,protos.md rb/api/*.proto
</code></pre></div><h2 id="requirements" tabindex="-1">Requirements <a class="header-anchor" href="#requirements" aria-label="Permalink to &quot;Requirements&quot;">​</a></h2><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>npm install
</code></pre></div><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>npm run docs:dev
</code></pre></div><h2 id="deploy" tabindex="-1">Deploy <a class="header-anchor" href="#deploy" aria-label="Permalink to &quot;Deploy&quot;">​</a></h2><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>npm run docs:build
cd .vitepress/dist
git push
</code></pre></div><p>배포전 확인</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>npm run docs:preview
</code></pre></div>`,12)]))}const u=e(n,[["render",c]]);export{h as __pageData,u as default};
