import{_ as o,c as t,a5 as a,o as r}from"./chunks/framework.Bl9iQvl_.js";const p=JSON.parse('{"title":"Build Issue","description":"","frontmatter":{"outline":"deep"},"headers":[],"relativePath":"docs/development/troubleshooting/build-issue.md","filePath":"docs/development/troubleshooting/build-issue.md"}'),s={name:"docs/development/troubleshooting/build-issue.md"};function i(n,e,l,c,d,h){return r(),t("div",null,e[0]||(e[0]=[a(`<h1 id="build-issue" tabindex="-1">Build Issue <a class="header-anchor" href="#build-issue" aria-label="Permalink to &quot;Build Issue&quot;">​</a></h1><h2 id="cmake-preset-error" tabindex="-1">CMake Preset Error <a class="header-anchor" href="#cmake-preset-error" aria-label="Permalink to &quot;CMake Preset Error&quot;">​</a></h2><h3 id="problem" tabindex="-1"><strong>Problem</strong>: <a class="header-anchor" href="#problem" aria-label="Permalink to &quot;**Problem**:&quot;">​</a></h3><p>An error occurs when running CMake with the <code>--preset</code> option: &quot;The source directory does not exist.&quot;</p><h3 id="error-message" tabindex="-1"><strong>Error Message</strong>: <a class="header-anchor" href="#error-message" aria-label="Permalink to &quot;**Error Message**:&quot;">​</a></h3><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>user@hostname:~/project-directory$ cmake --preset conan-release
CMake Error: The source directory &quot;/home/user/project-directory/conan-release&quot; does not exist.
Specify --help for usage, or press the help button on the CMake GUI.
</code></pre></div><h3 id="solution" tabindex="-1"><strong>Solution</strong>: <a class="header-anchor" href="#solution" aria-label="Permalink to &quot;**Solution**:&quot;">​</a></h3><h4 id="check-cmake-version" tabindex="-1">Check CMake Version: <a class="header-anchor" href="#check-cmake-version" aria-label="Permalink to &quot;Check CMake Version:&quot;">​</a></h4><ul><li>This error is often caused by using an older CMake version. Ensure that your CMake version is 3.23 or higher.</li></ul><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>cmake --version
</code></pre></div><ul><li>If the version is outdated, refer to the <a href="./../getting-started/installation.html">installation process</a> in the <strong>CMake installation</strong> section to upgrade to the latest version.</li></ul><hr><p>In most cases, the issue can be resolved by following the above steps. If the problem persists, review the following items.</p><h4 id="additional-checks" tabindex="-1">Additional Checks: <a class="header-anchor" href="#additional-checks" aria-label="Permalink to &quot;Additional Checks:&quot;">​</a></h4><ul><li><strong>Preset Path</strong>: Make sure you are running the CMake command from the project&#39;s root directory.</li><li><strong>Preset Name</strong>: Verify that the preset name defined in the <code>CMakePresets.json</code> file is correct.</li><li><strong>Git Submodule</strong>: Ensure that the submodules are properly initialized when cloning the project.</li></ul><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre><code>git submodule update --init --recursive
</code></pre></div><h4 id="references" tabindex="-1">References: <a class="header-anchor" href="#references" aria-label="Permalink to &quot;References:&quot;">​</a></h4><ul><li>For more detailed information, refer to the <a href="https://docs.conan.io/2/examples/tools/cmake/cmake_toolchain/build_project_cmake_presets.html" target="_blank" rel="noreferrer">Building Projects Using CMake Presets</a> documentation.</li></ul>`,18)]))}const m=o(s,[["render",i]]);export{p as __pageData,m as default};
