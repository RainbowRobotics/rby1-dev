import { execSync } from 'node:child_process'
import { existsSync, readFileSync } from 'node:fs'
import { dirname, join, normalize, relative } from 'node:path'
import { fileURLToPath } from 'node:url'
import { type DefaultTheme } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import deflist from 'markdown-it-deflist'

// Site root on GitHub Pages; override with VP_BASE for local previews.
const base = process.env.VP_BASE ?? '/rby1-dev/'
// The SDK release the API reference is generated from: the tag of the external/rby1-sdk submodule.
const SDK_VERSION =
  process.env.SDK_VERSION ??
  (() => {
    try {
      return execSync('git describe --tags --exact-match', { cwd: join(dirname(fileURLToPath(import.meta.url)), '../../external/rby1-sdk') })
        .toString().trim()
    } catch {
      return 'v0.10.1'
    }
  })()
const SRC = join(dirname(fileURLToPath(import.meta.url)), '..')

type Item = DefaultTheme.SidebarItem

// ── Sidebar helpers ───────────────────────────────────────────────────
// Section landing pages are linked as "/section/" (what VitePress uses as their route), so that
// the sidebar highlight and the previous/next links work on them.
const route = (path: string) => `/${path.replace(/(^|\/)index$/, '$1')}`
const page = (text: string, path: string): Item => ({ text, link: route(path) })
const group = (text: string, items: Item[], collapsed = false): Item => ({ text, items, collapsed })

/** First "# " heading of a page (Markdown escapes removed). */
function titleOf(file: string): string {
  const text = readFileSync(file, 'utf8')
  const m = text.match(/^#\s+(.+)$/m)
  return (m ? m[1] : file.split('/').pop()!.replace(/\.md$/, '')).replace(/\\(.)/g, '$1').replace(/[*`]/g, '').trim()
}

/**
 * Sidebar tree that follows the links of generated index pages, like a Sphinx toctree:
 * an index page lists its children; children inside the same folder tree become nested items.
 */
function linkTree(indexPath: string, depth = 3, seen = new Set<string>(), sectionRoot?: string): Item {
  const file = join(SRC, indexPath)
  seen.add(normalize(file))
  const text = readFileSync(file, 'utf8')
  const root = dirname(file)
  // Children may live in sibling folders of the section (e.g. sdk/python/client/index.md -> ../generated/*.md).
  const section = sectionRoot ?? root
  const children: Item[] = []
  for (const m of text.matchAll(/\]\(((?!https?:|#)[^)#\s]+\.md)(?:#[^)]*)?\)/g)) {
    const target = normalize(join(root, m[1]))
    if (seen.has(target) || !existsSync(target) || !target.startsWith(section)) continue
    seen.add(target)
    const rel = relative(SRC, target)
    if (depth > 1 && /index\.md$/.test(rel)) {
      children.push({ ...linkTree(rel, depth - 1, seen, section), collapsed: true })
    } else {
      children.push(page(titleOf(target), rel.replace(/\.md$/, '')))
    }
  }
  return { text: titleOf(file), link: route(indexPath.replace(/\.md$/, '')), items: children }
}

const safeTree = (indexPath: string, depth?: number): Item =>
  existsSync(join(SRC, indexPath))
    ? linkTree(indexPath, depth)
    : { text: `${indexPath} (run scripts/generate_reference.py)`, link: '/sdk/' }

// ── Sidebars per top menu ─────────────────────────────────────────────
const quickStart: Item[] = [
  group('Getting Started', [page('Overview', 'getting-started/index')]),
  group('First Steps', [
    page('1. E‑Stop Basics', 'getting-started/estop-basics'),
    page('2. Unboxing', 'getting-started/unboxing'),
    page('3. Hotspot & Web UI', 'getting-started/hotspot-and-webui'),
    page('4. External Access Point', 'getting-started/connect-external-ap'),
    page('5. SDK Installation', 'getting-started/sdk-install-and-state'),
    page('6. First Motion', 'getting-started/first-motion'),
  ]),
  group('Reference', [
    page('Network and Ports', 'getting-started/network-and-ports'),
    page('Supported Platforms', 'getting-started/supported-platforms'),
    page('Connection Troubleshooting', 'getting-started/connection-troubleshooting'),
    page('Hello, RB-Y1', 'getting-started/hello_rby1'),
    page('Tutorial Videos', 'getting-started/tutorial_videos'),
  ]),
]

const manual: Item[] = [
  group('Safety', [
    page('Overview', 'precautions/index'),
    page('General', 'precautions/general'),
    page('Power & Battery', 'precautions/power_and_battery'),
    page('Hardware Handling', 'precautions/hardware_handling'),
    page('Control & System', 'precautions/control_and_system'),
    page('Operation', 'precautions/operation'),
  ]),
  group('Hardware', [
    page('Hardware', 'hardware/index'),
    page('Overview & Specifications', 'hardware/overview'),
    page('Mechanical Part', 'hardware/mechanical_part'),
    page('Motor Driver', 'hardware/motor_driver'),
    page('Electrical Part', 'hardware/electrical_part'),
    page('Battery', 'hardware/battery'),
  ]),
  group('Options', [
    page('Gripper', 'options/gripper'),
    page('Leader Arm', 'options/leader_arm'),
    page('Teleoperation & Data Collection', 'options/teleoperation'),
  ]),
  group('Maintenance & Tools', [
    page('Maintenance', 'maintenance/index'),
    page('RPC Updater', 'rpc_management_tools/rpc_updater'),
    page('Log Backup', 'rpc_management_tools/log_backup'),
    page('CAN Checker', 'rpc_management_tools/can_checker'),
    page('FT Sensor Initialization', 'rpc_management_tools/ft_sensor_initialize'),
    page('Bootloader', 'rpc_management_tools/bootloader'),
    page('Parts Detaching', 'maintenance/detaching_guide'),
  ]),
  group('Legal', [page('Open Source License Notices', 'legal/third-party-notices')]),
]

const software: Item[] = [
  group('SDK Guide', [
    page('Software & SDK', 'software/index'),
    page('Software Architecture', 'software/architecture'),
    page('Robot Main Program', 'software/robot_main_program'),
    page('Web UI', 'software/web-ui'),
    page('User PC (UPC)', 'software/upc'),
    page('Units and Frames', 'software/units-and-frames'),
    group('Robot Models', [
      page('Models', 'sdk/models/index'),
      page('Model A', 'sdk/models/generated/model_a'),
      page('Model M', 'sdk/models/generated/model_m'),
      page('Model UB', 'sdk/models/generated/model_ub'),
      page('Hardware Versions', 'sdk/models/hardware-versions'),
    ], true),
    group('Controllers', [
      page('Controllers', 'sdk/controllers/index'),
      page('Command and Control Architecture', 'sdk/controllers/generated/command_and_control_architecture'),
      page('Control Hold Time and Minimum Time', 'sdk/controllers/generated/control_hold_time_and_minimum_time'),
      page('Parameter Reference', 'sdk/controllers/generated/parameter'),
    ], true),
    page('Examples', 'examples/ex'),
    group('Troubleshooting', [
      page('Troubleshooting', 'sdk/troubleshooting/index'),
      page('Fault Diagnosis', 'sdk/troubleshooting/fault-diagnosis'),
      page('Build Issues', 'sdk/troubleshooting/generated/build_issue'),
      page('Error Reporting', 'sdk/troubleshooting/generated/error_reporting'),
      page('FAQ', 'sdk/troubleshooting/generated/faq'),
    ], true),
    page('Glossary', 'software/glossary'),
  ]),
  group('ROS 2', [
    page('ROS 2', 'ros2/index'),
    ...[
      ['Overview', 'overview'], ['Install & Build', 'install_and_build'], ['Driver Parameters', 'config_driver_parameters'],
      ['Examples', 'examples'], ['Key Features', 'key_features'], ['Topics', 'topics'], ['Services', 'services'],
      ['Action Servers', 'action_servers'], ['Command Streams', 'command_streams'], ['Custom Message Types', 'custom_message_types'],
      ['MoveIt 2', 'rby1_moveit2'], ['MoveIt Planner', 'moveit_planner'], ['ros2_control Hardware Interface', 'hardware_interface'],
      ['Package Architecture', 'package_architecture'], ['Bringup', 'bringup'], ['Tools', 'tools'],
      ['Visualization & Robot Description', 'visualization_and_robot_description'], ['UPC Topic Bridge', 'upc_topic_bridge'],
      ['Troubleshooting & Known Issues', 'troubleshooting_and_known_issues'],
    ].map(([t, p]) => page(t, `ros2/ros2_driver/${p}`)),
  ]),
  group('Simulation', [
    page('Simulation', 'simulators/index'),
    page('MuJoCo', 'simulators/mujoco'),
    page('Isaac Sim', 'simulators/isaac_sim'),
  ]),
]

const apiReference: Item[] = [
  page('API Reference', 'sdk/index'),
  { ...safeTree('sdk/python/index.md'), collapsed: false },
  { ...safeTree('sdk/cpp/index.md'), collapsed: true },
  // Modules only: listing all 272 proto types here would put them in the HTML of every API page.
  { ...safeTree('sdk/protos/index.md', 1), collapsed: true },
]

const sidebar: DefaultTheme.SidebarMulti = {}
for (const p of ['/getting-started/']) sidebar[p] = quickStart
for (const p of ['/precautions/', '/hardware/', '/options/', '/maintenance/', '/rpc_management_tools/', '/legal/']) sidebar[p] = manual
for (const p of ['/software/', '/sdk/models/', '/sdk/controllers/', '/sdk/troubleshooting/', '/examples/', '/ros2/', '/simulators/']) sidebar[p] = software
for (const p of ['/sdk/python/', '/sdk/cpp/', '/sdk/protos/']) sidebar[p] = apiReference
// The API landing page (/sdk/) shares its folder prefix with the guide pages above, so match it exactly.
sidebar['/sdk/index'] = apiReference

// ── Top menu (same pattern as the RBQ manual) ────────────────────────
const nav: DefaultTheme.NavItem[] = [
  { text: 'Home', link: '/' },
  { text: 'Quick Start', link: '/getting-started/', activeMatch: '^/getting-started/' },
  {
    text: 'Manual',
    activeMatch: '^/(precautions|hardware|options|maintenance|rpc_management_tools|legal)/',
    items: [
      { text: 'Safety', link: '/precautions/' },
      { text: 'Hardware', link: '/hardware/' },
      { text: 'Options', link: '/options/gripper' },
      { text: 'Maintenance & Tools', link: '/maintenance/' },
    ],
  },
  {
    text: 'Software',
    activeMatch: '^/(software|sdk/models|sdk/controllers|sdk/troubleshooting|examples|ros2|simulators)/',
    items: [
      { text: 'SDK Guide', link: '/software/' },
      { text: 'ROS 2', link: '/ros2/' },
      { text: 'Simulation', link: '/simulators/' },
    ],
  },
  {
    text: 'API Reference',
    activeMatch: '^/sdk/($|index|python/|cpp/|protos/)',
    items: [
      { text: 'Python API', link: '/sdk/python/' },
      { text: 'C++ API', link: '/sdk/cpp/' },
      { text: 'Protobuf (gRPC) API', link: '/sdk/protos/' },
    ],
  },
  { text: 'Download', link: '/downloads' },
  { text: 'Support', link: '/support' },
  {
    // One version is published (the latest); older releases are on GitHub (see README, "배포와 버전").
    text: SDK_VERSION,
    items: [
      { text: 'Supported platforms & compatibility', link: '/getting-started/supported-platforms' },
      { text: `rby1-sdk ${SDK_VERSION} release notes`, link: `https://github.com/RainbowRobotics/rby1-sdk/releases/tag/${SDK_VERSION}` },
      { text: 'Robot software releases', link: 'https://github.com/RainbowRobotics/rby1-release/releases' },
      { text: 'rby1-ros2 releases', link: 'https://github.com/RainbowRobotics/rby1-ros2/releases' },
    ],
  },
]

// ── Edit links: generated pages point to their source ──────────────
// VitePress serializes this function into the page bundle, so it must not use outside variables.
function editUrl({ filePath }: { filePath: string }): string {
  const repo = 'https://github.com/RainbowRobotics/rby1-dev'
  let m: RegExpMatchArray | null
  if (/^sdk\/python\/generated\//.test(filePath)) return 'https://github.com/RainbowRobotics/rby1-sdk/tree/main/python' // docstrings
  if ((m = filePath.match(/^sdk\/(python|cpp)\/(.+)\.md$/))) return `${repo}/edit/dev/doc/source/sdk/${m[1]}/${m[2]}.rst`
  if (/^sdk\/protos\/generated\//.test(filePath)) return `${repo}/tree/dev/doc/source/sdk/protos` // generator input
  return `${repo}/edit/dev/manual/${filePath}`
}

// ── Page metadata: description from the first paragraph, canonical URL, Open Graph ──
const SITE_URL = `https://rainbowrobotics.github.io${base}`
function firstParagraph(relativePath: string): string | undefined {
  const file = join(SRC, relativePath)
  if (!existsSync(file)) return undefined
  const body = readFileSync(file, 'utf8').replace(/^---[\s\S]*?---/, '')
  let text = ''
  for (const block of body.split(/\n\s*\n/)) {
    const t = block.trim()
    if (!t || /^(#|<|:::|!\[|\||```|-|\$\$|\d+\.)/.test(t)) continue
    // Plain text: link text kept, emphasis and code marks removed (identifiers such as rby1_sdk stay intact).
    text += (text ? ' ' : '') + t.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/[*`]/g, '').replace(/\s+/g, ' ')
    if (text.length >= 80) break // a one-line lead-in alone says little: take the next paragraph too
  }
  if (!text) return undefined
  if (text.length <= 200) return text
  const cut = text.slice(0, 200)
  return cut.slice(0, cut.lastIndexOf(' ')) + '…'
}

// Pages kept only to forward old URLs (frontmatter "search: false"): not in the sitemap, not indexed.
const movedPages = new Set<string>()
const pageUrl = (relativePath: string) =>
  SITE_URL + relativePath.replace(/(^|\/)index\.md$/, '$1').replace(/\.md$/, '.html')

// withMermaid: renders ```mermaid blocks (architecture diagrams in the ROS 2 pages).
export default withMermaid({
  base,
  title: 'RB-Y1',
  description: 'RB-Y1 dual-arm mobile manipulator: manual, SDK and API reference',
  // Keep the .html page URLs of the previous site so existing links keep working.
  cleanUrls: false,
  // Generated fragments pulled in with <!--@include-->, not pages of their own.
  // Also the old single-page proto reference and type list (duplicates of the per-type pages).
  srcExclude: ['hardware/generated/**', 'sdk/protos/generated/protos.md', 'sdk/protos/generated/proto_types.md'],
  lastUpdated: true,
  // The Doxygen HTML is a static folder in public/, not a VitePress page.
  ignoreDeadLinks: [/raw-api\//, /^https?:\/\/localhost/],
  head: [['link', { rel: 'icon', href: `${base}rb_logo.png` }]],
  sitemap: {
    hostname: SITE_URL,
    transformItems: (items) => items.filter((item) => !movedPages.has(new URL(item.url, SITE_URL).href)),
  },
  transformPageData(pageData) {
    if (pageData.frontmatter.search === false) movedPages.add(pageUrl(pageData.relativePath))
    const desc = pageData.frontmatter.description ?? firstParagraph(pageData.relativePath)
    if (desc) pageData.description = desc
  },
  transformHead({ pageData }) {
    const url = pageUrl(pageData.relativePath)
    const title = pageData.title ? `${pageData.title} | RB-Y1` : 'RB-Y1'
    if (pageData.frontmatter.search === false) return [['meta', { name: 'robots', content: 'noindex' }]]
    return [
      ['link', { rel: 'canonical', href: url }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: pageData.description || 'RB-Y1 manual' }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { property: 'og:image', content: `${SITE_URL}hero-image.png` }],
    ]
  },
  // Large generated API tables: keep the search index small and the build quick.
  // MathJax for the controller formulas ($$ blocks converted from MyST {math}).
  // pycon: interactive Python sessions in the API docstrings.
  markdown: {
    math: true,
    languageAlias: { pycon: 'python' },
    // Definition lists: enum members in the generated Python API pages.
    config: (md) => {
      md.use(deflist)
    },
    // Same heading ids as the previous (MyST) site, so existing #anchors keep working:
    // lower case, keep letters, digits, "_" and "-", spaces to "-".
    anchor: {
      slugify: (s: string) =>
        s.trim().toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, '').replace(/\s/g, '-'),
    },
  },

  themeConfig: {
    nav,
    sidebar,
    logo: '/rb_logo.png',
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/RainbowRobotics/rby1-sdk' },
      { icon: 'youtube', link: 'https://www.youtube.com/@rainbowrobotics' },
    ],
    editLink: {
      // Generated pages are edited at their source (see README, "생성되는 페이지는 원본을 고칩니다").
      pattern: editUrl,
      text: 'Edit this page on GitHub',
    },
    outline: { level: [2, 3] },
    footer: { copyright: `© 2024-${new Date().getFullYear()} Rainbow Robotics` },
  },
})
