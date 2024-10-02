import{_ as n,c as t,a1 as e,o as r}from"./chunks/framework.Bff2UY46.js";const i="/rby1-dev/assets/mermaid-robot-command.DsUrisxV.png",a="/rby1-dev/assets/mermaid-wholebody-command.mPn8R2As.png",s="/rby1-dev/assets/mermaid-component_based.BPX2ktgH.png",m="/rby1-dev/assets/mermaid-body-component.CKcxBeBZ.png",l="/rby1-dev/assets/mermaid-controller.D1W5nYTf.png",C=JSON.parse('{"title":"Controllers","description":"","frontmatter":{"title":"Controllers","outline":"deep"},"headers":[],"relativePath":"docs/development/rby1-sdk/controllers.md","filePath":"docs/development/rby1-sdk/controllers.md"}'),d={name:"docs/development/rby1-sdk/controllers.md"};function c(p,o,h,g,u,_){return r(),t("div",null,o[0]||(o[0]=[e('<h1 id="controllers" tabindex="-1">Controllers <a class="header-anchor" href="#controllers" aria-label="Permalink to &quot;Controllers&quot;">​</a></h1><h2 id="overview" tabindex="-1">Overview <a class="header-anchor" href="#overview" aria-label="Permalink to &quot;Overview&quot;">​</a></h2><p>The robot commands are divided into three main types:</p><ol><li><strong>WholeBodyCommand</strong>: Controls the entire robot with 24 degrees of freedom (DOF) in a single command.</li><li><strong>ComponentBasedCommand</strong>: Controls the body of the robot with 20 DOF, either using the entire body at once or split into components.</li><li><strong>JogCommand</strong>: Controls smaller, individual movements, typically used for fine adjustments.</li></ol><figure><img src="'+i+'" alt="Robot Command Diagram" style="margin:auto;"></figure><hr><h3 id="wholebodycommand" tabindex="-1">WholeBodyCommand <a class="header-anchor" href="#wholebodycommand" aria-label="Permalink to &quot;WholeBodyCommand&quot;">​</a></h3><p>This command controls all the major components of the robot, including arms, torso, and legs. It supports various controllers for managing the full body of the robot. The primary use case is for synchronized movements where multiple parts of the robot are involved. This command sends a <strong>24 DOF</strong> control signal all at once.</p><figure><img src="'+a+'" alt="WholeBody Command Diagram" style="margin:auto;width:60%;align:center;"></figure><h3 id="componentbasedcommand" tabindex="-1">ComponentBasedCommand <a class="header-anchor" href="#componentbasedcommand" aria-label="Permalink to &quot;ComponentBasedCommand&quot;">​</a></h3><p>The <strong>ComponentBasedCommand</strong> is responsible for controlling the core components of the robot, such as the <strong>Mobility</strong>, <strong>Body</strong>, and <strong>Head</strong>. It provides a flexible architecture for handling different sections of the robot individually. Each of these components can be controlled using specialized commands, allowing precise control over the robot&#39;s movement and actions. This structure typically supports multiple controllers to handle specific parts of the robot efficiently.</p><figure><img src="'+s+'" alt="Component Based Command Diagram" style="margin:auto;"></figure><hr><h3 id="bodycommand-structure" tabindex="-1">BodyCommand Structure <a class="header-anchor" href="#bodycommand-structure" aria-label="Permalink to &quot;BodyCommand Structure&quot;">​</a></h3><p>The <strong>BodyCommand</strong> allows for detailed control of the robot&#39;s body and arms. It is divided into <strong>BodyComponentBasedCommand</strong>, under which <strong>TorsoCommand</strong> and <strong>ArmCommand</strong> exist. The arms can be controlled individually through <strong>LeftArmCommand</strong> and <strong>RightArmCommand</strong>, providing finer control over each arm.</p><p>In the diagram below, the <strong>Controller</strong> nodes follow the structure defined in the <a href="#controllers">Controllers</a> section, where each <strong>Controller</strong> node represents the available controllers for joint position, Cartesian motion, impedance control, gravity compensation, and optimal control.</p><figure><img src="'+m+'" alt="Body Component Command Diagram" style="margin:auto;"></figure><hr><h3 id="controllers-1" tabindex="-1">Controllers <a class="header-anchor" href="#controllers-1" aria-label="Permalink to &quot;Controllers&quot;">​</a></h3><p>The following controllers are used throughout different commands like <strong>WholeBodyCommand</strong>, <strong>ComponentBasedCommand</strong>, and their subcommands.</p><ul><li><strong>JointPositionController</strong>: Manages the position of each joint.</li><li><strong>CartesianController</strong>: Controls the Cartesian position of the robot.</li><li><strong>ImpedanceController</strong>: Allows control of force and motion, useful for interactions with the environment.</li><li><strong>GravityCompensationController</strong>: Compensates for gravitational forces, making the robot more energy-efficient during holding positions.</li><li><strong>OptimalController</strong>: Controls the robot&#39;s motion using an optimization equation.</li></ul><figure><img src="'+l+`" alt="Controller Diagram" style="margin:auto;"></figure><h2 id="examples" tabindex="-1">Examples <a class="header-anchor" href="#examples" aria-label="Permalink to &quot;Examples&quot;">​</a></h2><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre><code>def example_joint_position_command_1(robot):
    print(&quot;joint position command example 1&quot;)

    # Initialize joint positions
    q_joint_waist = np.zeros(6)
    q_joint_right_arm = np.zeros(7)
    q_joint_left_arm = np.zeros(7)

    # Set specific joint positions
    q_joint_right_arm[1] = -90 * D2R
    q_joint_left_arm[1] = 90 * D2R

    rc = RobotCommandBuilder().set_command(
        ComponentBasedCommandBuilder().set_body_command(
            BodyComponentBasedCommandBuilder()
            .set_torso_command(
                JointPositionCommandBuilder()
                .set_minimum_time(minimum_time)
                .set_position(q_joint_waist)
            )
            .set_right_arm_command(
                JointPositionCommandBuilder()
                .set_minimum_time(minimum_time)
                .set_position(q_joint_right_arm)
            )
            .set_left_arm_command(
                JointPositionCommandBuilder()
                .set_minimum_time(minimum_time)
                .set_position(q_joint_left_arm)
            )
        )
    )

    rv = robot.send_command(rc, 10).get()

    if rv.finish_code != RobotCommandFeedback.FinishCode.Ok:
        print(&quot;Error: Failed to conduct demo motion.&quot;)
        return 1

    return 0


def example_joint_position_command_2(robot):
    print(&quot;joint position command example 2&quot;)

    # Define joint positions
    q_joint_waist = np.array([0, 30, -60, 30, 0, 0]) * D2R
    q_joint_right_arm = np.array([-45, -30, 0, -90, 0, 45, 0]) * D2R
    q_joint_left_arm = np.array([-45, 30, 0, -90, 0, 45, 0]) * D2R

    # Combine joint positions
    q = np.concatenate([q_joint_waist, q_joint_right_arm, q_joint_left_arm])

    # Build command
    rc = RobotCommandBuilder().set_command(
        ComponentBasedCommandBuilder().set_body_command(
            BodyCommandBuilder().set_command(
                JointPositionCommandBuilder()
                .set_position(q)
                .set_minimum_time(minimum_time)
            )
        )
    )

    rv = robot.send_command(rc, 10).get()

    if rv.finish_code != RobotCommandFeedback.FinishCode.Ok:
        print(&quot;Error: Failed to conduct demo motion.&quot;)
        return 1

    return 0
</code></pre></div>`,24)]))}const b=n(d,[["render",c]]);export{C as __pageData,b as default};
