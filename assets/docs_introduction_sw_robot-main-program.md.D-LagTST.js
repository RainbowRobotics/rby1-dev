import{_ as o,c as r,a5 as e,o as a}from"./chunks/framework.Bl9iQvl_.js";const s="/rby1-dev/assets/inside-rpc.CFOnnjv2.png",n="/rby1-dev/assets/inside-rpc-hardware.BDJUteZ8.png",i="/rby1-dev/assets/inside-rpc-controller.D_P_QKNR.png",l="/rby1-dev/assets/inside-rpc-service.CfP0x3gS.png",f=JSON.parse('{"title":"Robot Main Program","description":"","frontmatter":{"title":"Robot Main Program","outline":"deep"},"headers":[],"relativePath":"docs/introduction/sw/robot-main-program.md","filePath":"docs/introduction/sw/robot-main-program.md"}'),c={name:"docs/introduction/sw/robot-main-program.md"};function g(d,t,u,h,m,p){return a(),r("div",null,t[0]||(t[0]=[e('<h1 id="robot-main-program-robot-pc-system-overview" tabindex="-1">Robot Main Program (Robot PC System Overview) <a class="header-anchor" href="#robot-main-program-robot-pc-system-overview" aria-label="Permalink to &quot;Robot Main Program (Robot PC System Overview)&quot;">​</a></h1><blockquote><p>ℹ️ <strong>Note</strong>: The diagram below provides an overview of the <strong>Robot Main Program</strong>, which is the core software system responsible for processing commands and controlling the robot&#39;s behavior.</p></blockquote><figure style="text-align:center;"><img src="'+s+'" alt="Robot Main Program Overview" style="width:100%;margin:auto;"></figure><h2 id="hardware" tabindex="-1">Hardware <a class="header-anchor" href="#hardware" aria-label="Permalink to &quot;Hardware&quot;">​</a></h2><ul><li><strong>Hardware Management</strong>: Manages all hardware components, including motor drivers, sensors, and power systems.</li><li><strong>Robot State Construction</strong>: Processes data from these components to construct the <strong>robot state</strong>.</li><li><strong>Control Output</strong>: Transmits control outputs from the controller to the hardware (motor drivers).</li></ul><figure style="text-align:center;"><img src="'+n+'" alt="Hardware" style="width:70%;margin:auto;"></figure><h2 id="control-manager" tabindex="-1">Control Manager <a class="header-anchor" href="#control-manager" aria-label="Permalink to &quot;Control Manager&quot;">​</a></h2><blockquote><p>🔗 <strong>Note</strong>: For detailed information on specific controllers, please refer to <a href="https://rainbowrobotics.github.io/rby1-dev/docs/development/rby1-sdk/controllers.html" target="_blank" rel="noreferrer">this link</a>.</p></blockquote><ul><li><strong>Control Management</strong>: Manages individual controllers and ensures only one control is active at a time.</li><li><strong>Robot State Utilization</strong>: Takes the robot state from the hardware to produce the appropriate control output.</li></ul><figure style="text-align:center;"><img src="'+i+'" alt="Controller" style="width:70%;margin:auto;"></figure><h3 id="control-manager-states" tabindex="-1">Control Manager States <a class="header-anchor" href="#control-manager-states" aria-label="Permalink to &quot;Control Manager States&quot;">​</a></h3><ul><li><strong>Idle</strong>: Default state, no control output is transmitted.</li><li><strong>Enabled</strong>: Actively transmits control outputs. If no control is active, the system defaults to a position lock. Only motors ready for movement are activated.</li><li><strong>Minor Fault</strong>: Represents a minor issue that requires attention but does not cause a shutdown.</li><li><strong>Major Fault</strong>: Indicates a critical issue leading to power shutdown.</li></ul><h3 id="control-states" tabindex="-1">Control States <a class="header-anchor" href="#control-states" aria-label="Permalink to &quot;Control States&quot;">​</a></h3><ul><li><strong>Idle</strong>: No control process is occurring.</li><li><strong>Executing</strong>: A control process is currently running.</li><li><strong>Switching</strong>: A transition phase when a new control process overrides the active one due to priority.</li></ul><h3 id="led-states-led-strip-state" tabindex="-1">LED States (LED Strip State) <a class="header-anchor" href="#led-states-led-strip-state" aria-label="Permalink to &quot;LED States (LED Strip State)&quot;">​</a></h3><blockquote><p>💡 <strong>Note</strong>: The following LED statuses refer to the LED strip located on the front of the robot. This strip visually indicates the robot&#39;s power, control, and system states, allowing users to easily monitor the current status of the robot.</p></blockquote><ul><li><strong>Power ON</strong>: Solid white indicates full power; blinking white indicates partial power.</li><li><strong>Control Manager Enabled</strong>: <ul><li><strong>Idle</strong>: Blue LED.</li><li><strong>Executing/Switching</strong>: Green LED.</li></ul></li><li><strong>Fault States</strong>: <ul><li><strong>Minor Fault</strong>: Blinking red.</li><li><strong>Major Fault</strong>: Solid red.</li></ul></li></ul><h2 id="service" tabindex="-1">Service <a class="header-anchor" href="#service" aria-label="Permalink to &quot;Service&quot;">​</a></h2><figure style="text-align:center;"><img src="'+l+'" alt="Service" style="width:100%;margin:auto;"></figure><ul><li>The <strong>gRPC server</strong> accepts requests from clients, processes them, and returns appropriate responses.</li><li>For available services and RPC methods, refer to the corresponding proto file.</li></ul>',20)]))}const v=o(c,[["render",g]]);export{f as __pageData,v as default};
