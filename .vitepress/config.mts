import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/rby1-dev/',
  title: "RB-Y1 Dev",
  description: "Rainbow Robotics Y1 - Documentation",
  sitemap: {
    hostname: 'https://rainbowrobotics.github.io/rby1-dev/'
  },
  head: [
    ["meta", { name: "theme-color", content: "#729b1a" }],
    ["link", { rel: "icon", href: "/logo.png", type: "image/svg+xml" }],
    ["meta", { name: "description", content: "Comprehensive documentation for the RB-Y1 robot from Rainbow Robotics." }],
    ["meta", { name: "keywords", content: "RB-Y1, Rainbow Robotics, robot SDK, robotics documentation" }],
    ["meta", { name: "author", content: "Han-Sol Kang" }],
    ["meta", { name: "robots", content: "index, follow" }],
    ["meta", { property: "og:title", content: "RB-Y1 Dev Documentation" }],
    ["meta", { property: "og:description", content: "Detailed documentation for developers working with the RB-Y1 robot." }],
    ["meta", { property: "og:type", content: "website" }],
  ],
  markdown: {
    math: true
  },
 
  themeConfig: {
    logo: "/logo.png",
    socialLinks: [
      { icon: "github", link: "https://github.com/RainbowRobotics/rby1-sdk" },
      { icon: "youtube", link: "https://www.youtube.com/@rainbowrobotics/videos" },
    ],
    footer: {
      message: 'rby1-sdk Released under the Apache License 2.0.',
      copyright: '© Copyright 2024 Rainbow Robotics. All Rights Reserved.'
    },
    search: {
      provider: 'local',
      options: {
        _render(src, env, md) {
          const html = md.render(src, env)
          if (env.frontmatter?.search === false) return ''
          if (env.relativePath.startsWith('ko')) return ''
          return html
        }
      }
    },
    nav: [
      { text: "Home", link: "/" },
      { text: "Documentations", link: "/docs/introduction/hello-rby1/" },
      { text: "Simulators", link: "/docs/simulators/" },
      { text: "RPC Management Tools", link: "/docs/rpc-release/" },
      // { text: "Support", link: "/docs/support/"},
    ],

    sidebar: [
      {
        text: "Introduction", 
        collapsed: false,
        items:[
          {text: "Hello, RB-Y1", link: "/docs/introduction/hello-rby1/"},
        ],
      },

      {
        text: "Hardware",
        collapsed: false,
        items: [
          {text: "Overview", link: "/docs/introduction/hw/overview.md"},
          {text: "Mechanical Part", link: "/docs/introduction/hw/mechanical-part.md"},
          {text: "Electrical Part", link: "/docs/introduction/hw/electrical-part.md"}
        ]
      },
      {
        text: "Software",
        collapsed: false,
        items: [
          {text: "Software-Architecture", link: "/docs/introduction/sw/software-architecture.md"},
          {text: "Robot Main Program", link: "/docs/introduction/sw/robot-main-program"},
        ]
      },
      {text: "Options",
        collapsed: false,
        items: [
          {text: "Gripper", link: "/docs/introduction/options/gripper.md"},
          {text: "Master-Arm", link: "/docs/introduction/options/master-arm.md"},
        ]
      },
      {
        text: "Getting Started",
        collapsed: false,
        items: [
          {text: "Installation", link: "/docs/development/getting-started/installation"},
          {text: "Access Information", link: "/docs/development/getting-started/access-information"},
          {text: "Quick Start Guide", link: "/docs/development/getting-started/quick-start-guide"},
        ]
      },  
      {text: "RBY1-SDK",
        collapsed: false,
        items: [
          {text: "Model", link: "/docs/development/rby1-sdk/models/A", items:[
            {text: "A", link: "/docs/development/rby1-sdk/models/A"},
          ]},
          {text: "Prameters", link: "/docs/development/rby1-sdk/parameters"},
          {text: "Robot and Command", link: "/docs/development/rby1-sdk/robot-and-command"},
          {text: "Protos", link: "/docs/development/rby1-sdk/protos/protos-v0.3.0", items:[
            {text: "v0.3.0", link: "/docs/development/rby1-sdk/protos/protos-v0.3.0"},
            {text: "Before v0.2.0", link: "/docs/development/rby1-sdk/protos/protos-before-v0.2.0"}, 
          ]},
          {text: "Controllers", link: "/docs/development/rby1-sdk/controllers/command-and-control-architecture.md", items:[
            {text: "Command and Control Architecture", link: "/docs/development/rby1-sdk/controllers/command-and-control-architecture.md"},
            {text: "Control Hold Time and Minimum Time", link: "/docs/development/rby1-sdk/controllers/control-hold-time-and-minimum-time"}, 
          ]},
        ]
      },  
      {
        text: "Examples",
        collapsed: false,
        items: [
          { text: "C++ Examples", link: "/docs/examples/cpp-examples.md"},
          { text: "Python Examples", link: "/docs/examples/python-examples.md"},
        ],
      },
      {text: "Trobuleshooting",
        collapsed: false,
        items: [
          {text: "Build Issue", link: "/docs/development/troubleshooting/build-issue"},
          {text: "Error Reporting", link: "/docs/development/troubleshooting/error-reporting"},
          {text: "Robot Detaching Guide", link: "/docs/development/troubleshooting/robot_detaching_guide"},
          {text: "FAQ", link: "/docs/development/troubleshooting/faq"}
        ]
      },  
    ],
  },
});
