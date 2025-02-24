import{_ as a,c as i,a2 as t,o as l}from"./chunks/framework.3fgD02ok.js";const m=JSON.parse('{"title":"","description":"","frontmatter":{},"headers":[],"relativePath":"rby1-sdk/CHANGELOG.md","filePath":"rby1-sdk/CHANGELOG.md"}'),o={name:"rby1-sdk/CHANGELOG.md"};function r(n,e,s,d,u,h){return l(),i("div",null,e[0]||(e[0]=[t('<h2 id="v0-4-1-2025-02-21" tabindex="-1">v0.4.1 (2025-02-21) <a class="header-anchor" href="#v0-4-1-2025-02-21" aria-label="Permalink to &quot;v0.4.1 (2025-02-21)&quot;">​</a></h2><h3 id="🐛-fixes" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>update pypi version to 0.4.1 due to versioning issue (skip 0.4.0)</li></ul><h2 id="v0-4-0-2025-02-21" tabindex="-1">v0.4.0 (2025-02-21) <a class="header-anchor" href="#v0-4-0-2025-02-21" aria-label="Permalink to &quot;v0.4.0 (2025-02-21)&quot;">​</a></h2><h3 id="♻️-refactor" tabindex="-1">♻️ Refactor <a class="header-anchor" href="#♻️-refactor" aria-label="Permalink to &quot;♻️ Refactor&quot;">​</a></h3><ul><li>update bind_robot and bind_state in python</li><li><strong>demo_motion</strong>: rename waist to torso in demo_motion</li></ul><h3 id="✨-features" tabindex="-1">✨ Features <a class="header-anchor" href="#✨-features" aria-label="Permalink to &quot;✨ Features&quot;">​</a></h3><ul><li>add example for checking firmware version</li><li>Enhance JointInfo to include firmware version and product name</li><li>add python teleoperation example (performance improvements needed)</li><li>add m model (urdf, mjcf) and update motor index for m model</li><li>support mecanum mobile base in dynamics lib</li><li>add api for battery config (#42)</li><li>add api for system time control</li><li>add api to control the led (#40)</li></ul><h3 id="🐛-fixes-1" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-1" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li><strong>robot.h</strong>: add missing break in switch statement</li><li>support model m in python</li><li>bugfix in loader mecanum mobile base</li><li>add ready for command</li><li><strong>robot_state</strong>: add gravity term in robot_state</li><li>change Color (proto message) component type from float to uint32</li></ul><h2 id="v0-3-0-2024-12-20" tabindex="-1">v0.3.0 (2024-12-20) <a class="header-anchor" href="#v0-3-0-2024-12-20" aria-label="Permalink to &quot;v0.3.0 (2024-12-20)&quot;">​</a></h2><h3 id="♻️-refactor-1" tabindex="-1">♻️ Refactor <a class="header-anchor" href="#♻️-refactor-1" aria-label="Permalink to &quot;♻️ Refactor&quot;">​</a></h3><ul><li>remove docs files in protos</li><li>demo_motion</li><li><strong>event_loop</strong>: improve event_loop cyclic_task function</li><li>restructure gain retrieval and return as struct in rby1-sdk</li><li>clean up mobility_command example</li></ul><h3 id="✨-features-1" tabindex="-1">✨ Features <a class="header-anchor" href="#✨-features-1" aria-label="Permalink to &quot;✨ Features&quot;">​</a></h3><ul><li>add CancelControl function to stop ongoing current control</li><li>update demo motion minimum time and velocity limit scaling</li><li><strong>parameter</strong>: add support for temporary parameter setting in SetParameter</li><li>add demo motion example for master arm operation</li><li><strong>model.urdf</strong>: update joint limit(torso_3)</li><li>update joint limit</li><li>update default gain values</li><li>add grpc auto-generated code for web ui</li><li>add motor temperature information</li><li>expand gripper tip collision area</li><li>update functionality for joint position target in cartesian command</li><li>add joint position target to cartesian command (WIP)</li><li>add overloaded constructor to PIDGain and add Python examples for gain set/get</li><li>improve gain management and accessibility</li><li>add head gain example and mutex lock for Dynamixel gain and motro state retrieval</li><li>add examples for setting PID gains and factory reset</li><li>add functionality to set and get pid gains</li><li>add docker-compose.sim.yaml for ARM simulation setup</li><li>add docker-compose.sim.yaml for simulation setup</li><li>break eng/rel + home offset</li><li>proto docs update</li><li>add gripper test (python)</li><li>gripper test for python</li><li>update quick ui + qc ui</li><li>qc gui servo on update</li><li>qc gui update</li><li>teleop + demo motion update + quick ui</li><li>quick ui update(zero + ems)</li><li>impedance update</li><li>quick ui update</li><li>record &amp; replay example update</li></ul><h3 id="🐛-fixes-2" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-2" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>update gripper range detection</li><li>update head current casting after reverting to previous implementation</li><li><strong>dynamixel_bus</strong>: improve motor state reader function</li><li>make joint values realistic (#33)</li><li><strong>robot_command_builder.cpp</strong>: update pybind defaults and include stl header</li><li>update current reading logic for dynamixel</li><li><strong>demo_motion.cpp</strong>: correct typo in demo motion setjointpositiontarget -&gt; addjointpositiontarget</li><li>check done before cancel call</li><li>correct PID gain mapping and remove redundant torque disable call</li><li>align mobility SE2 and joint velocity direction with RPC program for simulator consistency</li><li>update network settings in docker-compose</li><li><strong>master_arm</strong>: fix out of bound access bug</li><li><strong>model.urdf</strong>: Change velocity limits for urdf torso_0, torso_1, and left_arm_5</li><li><strong>dynamixel-bus</strong>: fix bug</li><li>change delay for dynamixel to 100us</li><li>get control manager state in start_state_update cb function</li><li>typo update</li><li>typo</li><li>update teleoperation example</li></ul><h2 id="v0-2-0-2024-10-02" tabindex="-1">v0.2.0 (2024-10-02) <a class="header-anchor" href="#v0-2-0-2024-10-02" aria-label="Permalink to &quot;v0.2.0 (2024-10-02)&quot;">​</a></h2><h3 id="✨-features-2" tabindex="-1">✨ Features <a class="header-anchor" href="#✨-features-2" aria-label="Permalink to &quot;✨ Features&quot;">​</a></h3><ul><li>support dynamics in python</li></ul><h2 id="v0-1-11-2024-09-30" tabindex="-1">v0.1.11 (2024-09-30) <a class="header-anchor" href="#v0-1-11-2024-09-30" aria-label="Permalink to &quot;v0.1.11 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-3" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-3" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>remove unnecessary dependency</li><li>resolve package Python requirement issue</li></ul><h2 id="v0-1-10-2024-09-30" tabindex="-1">v0.1.10 (2024-09-30) <a class="header-anchor" href="#v0-1-10-2024-09-30" aria-label="Permalink to &quot;v0.1.10 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-4" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-4" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>make sdist once</li></ul><h2 id="v0-1-9-2024-09-30" tabindex="-1">v0.1.9 (2024-09-30) <a class="header-anchor" href="#v0-1-9-2024-09-30" aria-label="Permalink to &quot;v0.1.9 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-5" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-5" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>remove build folder before Poetry build</li></ul><h2 id="v0-1-8-2024-09-30" tabindex="-1">v0.1.8 (2024-09-30) <a class="header-anchor" href="#v0-1-8-2024-09-30" aria-label="Permalink to &quot;v0.1.8 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-6" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-6" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>run action on bash</li></ul><h2 id="v0-1-7-2024-09-30" tabindex="-1">v0.1.7 (2024-09-30) <a class="header-anchor" href="#v0-1-7-2024-09-30" aria-label="Permalink to &quot;v0.1.7 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-7" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-7" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li><strong>release.yml</strong>: update ci</li></ul><h2 id="v0-1-6-2024-09-30" tabindex="-1">v0.1.6 (2024-09-30) <a class="header-anchor" href="#v0-1-6-2024-09-30" aria-label="Permalink to &quot;v0.1.6 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-8" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-8" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li><strong>release.yml</strong>: update release action</li></ul><h2 id="v0-1-5-2024-09-30" tabindex="-1">v0.1.5 (2024-09-30) <a class="header-anchor" href="#v0-1-5-2024-09-30" aria-label="Permalink to &quot;v0.1.5 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-9" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-9" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li><strong>release.yml</strong>: fix</li></ul><h2 id="v0-1-4-2024-09-30" tabindex="-1">v0.1.4 (2024-09-30) <a class="header-anchor" href="#v0-1-4-2024-09-30" aria-label="Permalink to &quot;v0.1.4 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-10" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-10" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li><strong>release.yml</strong>: fix path on windows</li></ul><h2 id="v0-1-3-2024-09-30" tabindex="-1">v0.1.3 (2024-09-30) <a class="header-anchor" href="#v0-1-3-2024-09-30" aria-label="Permalink to &quot;v0.1.3 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-11" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-11" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li><strong>release.yml</strong>: use conditions for poetry install</li></ul><h2 id="v0-1-2-2024-09-30" tabindex="-1">v0.1.2 (2024-09-30) <a class="header-anchor" href="#v0-1-2-2024-09-30" aria-label="Permalink to &quot;v0.1.2 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-12" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-12" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li><strong>release.yml</strong>: change poetry path on windows</li></ul><h2 id="v0-1-1-2024-09-30" tabindex="-1">v0.1.1 (2024-09-30) <a class="header-anchor" href="#v0-1-1-2024-09-30" aria-label="Permalink to &quot;v0.1.1 (2024-09-30)&quot;">​</a></h2><h3 id="🐛-fixes-13" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-13" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>fix ci</li></ul><h2 id="v0-1-0-2024-09-30" tabindex="-1">v0.1.0 (2024-09-30) <a class="header-anchor" href="#v0-1-0-2024-09-30" aria-label="Permalink to &quot;v0.1.0 (2024-09-30)&quot;">​</a></h2><h3 id="✨-features-3" tabindex="-1">✨ Features <a class="header-anchor" href="#✨-features-3" aria-label="Permalink to &quot;✨ Features&quot;">​</a></h3><ul><li>update python demo code</li><li>update python demo code</li><li>update self_collision &amp; demo_motion</li><li>proto docs test</li><li>update demo motion2</li><li>update module_test master_arm</li><li>teleoperation example updat</li><li>gripper test update</li><li>update rpc address</li><li>update demo motion</li><li>update example</li><li>update cmakelists</li><li>urdf update</li><li>change input dev name</li><li>add sdk_commit_id (python binding)</li><li>add get/set robot model from/to rpc</li><li>add unlimited mode functionality</li><li>add init protos</li></ul><h3 id="🐛-fixes-14" tabindex="-1">🐛 Fixes <a class="header-anchor" href="#🐛-fixes-14" aria-label="Permalink to &quot;🐛 Fixes&quot;">​</a></h3><ul><li>cast method</li><li>macos test</li><li>add build.py for build wheel</li><li>fix typo</li></ul>',58)]))}const p=a(o,[["render",r]]);export{m as __pageData,p as default};
