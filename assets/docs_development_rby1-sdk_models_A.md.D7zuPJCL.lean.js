import{_ as o,c as t,a2 as r,o as a}from"./chunks/framework.3fgD02ok.js";const g=JSON.parse('{"title":"Model","description":"","frontmatter":{"title":"Model","outline":"deep"},"headers":[],"relativePath":"docs/development/rby1-sdk/models/A.md","filePath":"docs/development/rby1-sdk/models/A.md"}'),d={name:"docs/development/rby1-sdk/models/A.md"};function s(l,e,n,i,c,h){return a(),t("div",null,e[0]||(e[0]=[r('<h1 id="a-model-overview" tabindex="-1">A Model Overview <a class="header-anchor" href="#a-model-overview" aria-label="Permalink to &quot;A Model Overview&quot;">​</a></h1><blockquote><p>💡 <strong>Note:</strong> The most accurate information regarding the model can be found in the <a href="https://github.com/RainbowRobotics/rby1-sdk/blob/main/models/rby1a/urdf/model.urdf" target="_blank" rel="noreferrer">URDF files under the models directory</a> of the Rainbow Robotics SDK repository. It is highly recommended to refer to this source for the latest updates and details.</p></blockquote><h2 id="model-name" tabindex="-1">Model Name <a class="header-anchor" href="#model-name" aria-label="Permalink to &quot;Model Name&quot;">​</a></h2><p><strong>A</strong></p><h2 id="degrees-of-freedom-dof" tabindex="-1">Degrees of Freedom (DOF) <a class="header-anchor" href="#degrees-of-freedom-dof" aria-label="Permalink to &quot;Degrees of Freedom (DOF)&quot;">​</a></h2><ul><li><strong>Total DOF</strong>: 24</li></ul><h2 id="joint-names" tabindex="-1">Joint Names <a class="header-anchor" href="#joint-names" aria-label="Permalink to &quot;Joint Names&quot;">​</a></h2><p>The joint names of the A model are as follows:</p><ul><li><strong>Wheels</strong>: <code>right_wheel</code>, <code>left_wheel</code></li><li><strong>Torso</strong>: <code>torso_0</code>, <code>torso_1</code>, <code>torso_2</code>, <code>torso_3</code>, <code>torso_4</code>, <code>torso_5</code></li><li><strong>Right Arm</strong>: <code>right_arm_0</code>, <code>right_arm_1</code>, <code>right_arm_2</code>, <code>right_arm_3</code>, <code>right_arm_4</code>, <code>right_arm_5</code>, <code>right_arm_6</code></li><li><strong>Left Arm</strong>: <code>left_arm_0</code>, <code>left_arm_1</code>, <code>left_arm_2</code>, <code>left_arm_3</code>, <code>left_arm_4</code>, <code>left_arm_5</code>, <code>left_arm_6</code></li><li><strong>Head</strong>: <code>head_0</code>, <code>head_1</code></li></ul><h2 id="mobility-indexes" tabindex="-1">Mobility Indexes <a class="header-anchor" href="#mobility-indexes" aria-label="Permalink to &quot;Mobility Indexes&quot;">​</a></h2><p>The indexes related to mobility are as follows:</p><ul><li><strong>Right Wheel Index</strong>: 0</li><li><strong>Left Wheel Index</strong>: 1</li></ul><h2 id="body-indexes" tabindex="-1">Body Indexes <a class="header-anchor" href="#body-indexes" aria-label="Permalink to &quot;Body Indexes&quot;">​</a></h2><p>The indexes related to the body parts are as follows:</p><ul><li><strong>Torso Indexes</strong>: 2, 3, 4, 5, 6, 7</li><li><strong>Right Arm Indexes</strong>: 8, 9, 10, 11, 12, 13, 14</li><li><strong>Left Arm Indexes</strong>: 15, 16, 17, 18, 19, 20, 21</li></ul><h2 id="head-indexes" tabindex="-1">Head Indexes <a class="header-anchor" href="#head-indexes" aria-label="Permalink to &quot;Head Indexes&quot;">​</a></h2><p>The indexes related to the head parts are as follows:</p><ul><li><strong>Head Indexes</strong>: 22, 23</li></ul><h2 id="brake-and-motor-information" tabindex="-1">Brake and Motor Information <a class="header-anchor" href="#brake-and-motor-information" aria-label="Permalink to &quot;Brake and Motor Information&quot;">​</a></h2><h3 id="components-without-brakes" tabindex="-1">Components Without Brakes <a class="header-anchor" href="#components-without-brakes" aria-label="Permalink to &quot;Components Without Brakes&quot;">​</a></h3><p>The following components do not have brakes:</p><ul><li><strong>Wheels</strong>: <code>right_wheel</code>, <code>left_wheel</code></li><li><strong>Head</strong>: <code>head_0</code>, <code>head_1</code></li><li><strong>Right Arm</strong>: <code>right_arm_6</code></li><li><strong>Left Arm</strong>: <code>left_arm_6</code></li></ul><h3 id="components-without-physical-brake-buttons" tabindex="-1">Components Without Physical Brake Buttons <a class="header-anchor" href="#components-without-physical-brake-buttons" aria-label="Permalink to &quot;Components Without Physical Brake Buttons&quot;">​</a></h3><p>The following components have brakes but do not have physical buttons for releasing them (can only be released electronically):</p><ul><li><strong>Torso</strong>: <code>torso_3</code>, <code>torso_4</code>, <code>torso_5</code></li><li><strong>Right Arm</strong>: <code>right_arm_4</code>, <code>right_arm_5</code></li><li><strong>Left Arm</strong>: <code>left_arm_4</code>, <code>left_arm_5</code></li></ul><h3 id="components-with-physical-brake-buttons" tabindex="-1">Components With Physical Brake Buttons <a class="header-anchor" href="#components-with-physical-brake-buttons" aria-label="Permalink to &quot;Components With Physical Brake Buttons&quot;">​</a></h3><p>The following components have brakes and include physical buttons for releasing them:</p><ul><li><strong>Torso</strong>: <code>torso_0</code>, <code>torso_1</code>, <code>torso_2</code></li><li><strong>Right Arm</strong>: <code>right_arm_0</code>, <code>right_arm_1</code>, <code>right_arm_2</code>, <code>right_arm_3</code></li><li><strong>Left Arm</strong>: <code>left_arm_0</code>, <code>left_arm_1</code>, <code>left_arm_2</code>, <code>left_arm_3</code></li></ul><h2 id="motor-types" tabindex="-1">Motor Types <a class="header-anchor" href="#motor-types" aria-label="Permalink to &quot;Motor Types&quot;">​</a></h2><p>The motor types for each component are as follows:</p><ul><li><strong>Dynamixel Motors</strong>: Used in the Head (<code>head_0</code>, <code>head_1</code>)</li><li><strong>RBMotors</strong>: Used in all other components (Torso, Wheels, Right Arm, Left Arm)</li></ul>',31)]))}const _=o(d,[["render",s]]);export{g as __pageData,_ as default};
