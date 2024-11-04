import{_ as t,c as d,o as e,a3 as r}from"./chunks/framework.o8T5S5EX.js";const o="/rby1-dev/assets/blueprint1.BevBsdtU.png",f=JSON.parse('{"title":"Mechanical Part","description":"","frontmatter":{"title":"Mechanical Part","outline":"deep"},"headers":[],"relativePath":"docs/introduction/hw/mechanical-part.md","filePath":"docs/introduction/hw/mechanical-part.md"}'),a={name:"docs/introduction/hw/mechanical-part.md"},i=r('<h1 id="mechanical-part" tabindex="-1">Mechanical Part <a class="header-anchor" href="#mechanical-part" aria-label="Permalink to &quot;Mechanical Part&quot;">​</a></h1><blockquote><p>⚠️ <strong>Note:</strong> This robot is a research platform, and rapid improvements are constantly being made. While most of the information provided is accurate, we recommend double-checking for the most up-to-date details. For further inquiries, feel free to contact us at <strong><a href="mailto:rby.support@rainbow-robotics.com" target="_blank" rel="noreferrer">rby.support@rainbow-robotics.com</a></strong> or discuss on our GitHub Discussions page at <a href="https://github.com/RainbowRobotics/rby1-sdk/discussions" target="_blank" rel="noreferrer">rby1-sdk Discussions</a>.</p></blockquote><h2 id="motor-specifications" tabindex="-1">Motor Specifications <a class="header-anchor" href="#motor-specifications" aria-label="Permalink to &quot;Motor Specifications&quot;">​</a></h2><p>The table provides details of each motor&#39;s gear type, motor power, maximum measurable current, speed, and range of motion. For example, the R/LWH model has a planetary gear system and uses a 200W motor. Other systems utilize harmonic gears, and the movement range and maximum speed vary according to each axis.</p><table><thead><tr><th></th><th>Gear Type</th><th>Motor Power</th><th>Max. measurable current/ Limit current</th><th>Max Speed</th><th>Range</th></tr></thead><tbody><tr><td>R/LWH</td><td>Planetary</td><td>200W</td><td>150 RPM (1.5m/s)</td><td>Infinite</td><td></td></tr><tr><td>AR</td><td>Harmonic</td><td>250(450)W</td><td>53/46 A</td><td>120°/s</td><td>-20° ~ 20°</td></tr><tr><td>AP</td><td>Harmonic</td><td>250(450)W</td><td>53/46 A</td><td>120°/s</td><td>-60° ~ 70°</td></tr><tr><td>KN</td><td>Harmonic</td><td>250(450)W</td><td>53/46 A</td><td>120°/s</td><td>-140° ~ 45°</td></tr><tr><td>HP</td><td>Harmonic</td><td>200(280)W</td><td>26/23 A</td><td>180°/s</td><td>-45° ~ 90°</td></tr><tr><td>HR</td><td>Harmonic</td><td>200(280)W</td><td>26/23 A</td><td>180°/s</td><td>-30° ~ 30°</td></tr><tr><td>HY</td><td>Harmonic</td><td>200(280)W</td><td>26/23 A</td><td>180°/s</td><td>-90° ~ 90°</td></tr><tr><td>R/LSP</td><td>Harmonic</td><td>80(180)W</td><td>26/14 A</td><td>180°/s</td><td>-135° ~ 135°</td></tr><tr><td>R/LSR</td><td>Harmonic</td><td>80(180)W</td><td>26/14 A</td><td>180°/s</td><td>R : -180° ~ 4°<br> L : -4° ~ 180°</td></tr><tr><td>R/LSY</td><td>Harmonic</td><td>80(180)W</td><td>26/14 A</td><td>180°/s</td><td>-120° ~ 120°</td></tr><tr><td>R/LELB</td><td>Harmonic</td><td>50(75)W</td><td>8/7 A</td><td>180°/s</td><td>-150° ~ 0°</td></tr><tr><td>R/LWY1</td><td>Harmonic</td><td>30(95)W</td><td>8/7 A</td><td>360°/s</td><td>-360° ~ 360°</td></tr><tr><td>R/LWP</td><td>Harmonic</td><td>30(95)W</td><td>8/7 A</td><td>360°/s</td><td>-100° ~ 115°</td></tr><tr><td>R/LWY2</td><td>Harmonic + Pulley</td><td>45W</td><td>8/7 A</td><td>360°/s</td><td>-170° ~ 170°</td></tr></tbody></table><h2 id="torque-specifications" tabindex="-1">Torque Specifications <a class="header-anchor" href="#torque-specifications" aria-label="Permalink to &quot;Torque Specifications&quot;">​</a></h2><p>This table details the torque performance of various motor types. It includes continuous torque, repeated peak torque, and momentary peak torque in Newton-meters (Nm). Additionally, the table specifies the gear ratio, output speed in degrees per second (deg/s), motor encoder resolution in bits, transmission error in arcseconds, stiffness in Newton-meters per radian (Nm/rad), and the motor torque constant in Newton-meters per Ampere (Nm/A).</p><table><thead><tr><th>Type</th><th>AR, AP, KN</th><th>HP, HR, HY</th><th>R/L SP, R/L SR, R/L SY</th><th>R/L ELB</th><th>R/L WY1, R/L WP, R/L WY2</th></tr></thead><tbody><tr><td>Continuous Torque (Nm)</td><td>250</td><td>125</td><td>65</td><td>35</td><td>14</td></tr><tr><td>Repeated Peak Torque (Nm)</td><td>433</td><td>204</td><td>70</td><td>36</td><td>36</td></tr><tr><td>Momentary Peak Torque (Nm)</td><td>841</td><td>369</td><td>143</td><td>70</td><td>70</td></tr><tr><td>Output Speed (deg/s)</td><td>120</td><td>180</td><td>180</td><td>180</td><td>360</td></tr><tr><td>Motor Encoder Resolution (bit)</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td></tr><tr><td>Transmission Error (arcsec)</td><td>~50</td><td>~50</td><td>~50</td><td>~50</td><td>~50</td></tr><tr><td>Stiffness (Nm/rad)</td><td>110,000</td><td>50,000</td><td>14,000</td><td>6,100</td><td>6,100</td></tr><tr><td>Motor Torque Constant (Nm/A)</td><td>0.15</td><td>0.10</td><td>0.10</td><td>0.10</td><td>0.05</td></tr></tbody></table><h2 id="robot-dimensions" tabindex="-1">Robot Dimensions <a class="header-anchor" href="#robot-dimensions" aria-label="Permalink to &quot;Robot Dimensions&quot;">​</a></h2><p>The diagrams show the front and side views of the robot with detailed measurements. The total height of the robot is 1470 mm, and the arm span is 566.67 mm, with a 140-degree range of motion. The base dimensions are 662.62 mm in length and 580 mm in width. These measurements provide an understanding of the physical space the robot occupies, as well as its potential reach and movement range.</p><blockquote><p>⚠️ <strong>Note:</strong> Physical limits and control limits may differ. For detailed operation ranges, please refer to the <a href="https://github.com/RainbowRobotics/rby1-sdk/tree/main/models/rby1a/urdf" target="_blank" rel="noreferrer">URDF files</a>.</p></blockquote><figure style="text-align:center;"><img src="'+o+'" alt="Robot Dimensions" style="width:100%;margin:auto;"></figure>',12),s=[i];function n(c,m,h,l,p,u){return e(),d("div",null,s)}const g=t(a,[["render",n]]);export{f as __pageData,g as default};
