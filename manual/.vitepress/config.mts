import { existsSync, readFileSync } from 'node:fs'
import { dirname, join, normalize, relative } from 'node:path'
import { fileURLToPath } from 'node:url'
import { type DefaultTheme } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import deflist from 'markdown-it-deflist'

// Site root on GitHub Pages; override with VP_BASE for local previews.
const base = process.env.VP_BASE ?? '/rby1-dev/'
const SDK_VERSION = process.env.SDK_VERSION ?? 'v0.10.1'
const SRC = join(dirname(fileURLToPath(import.meta.url)), '..')

type Item = DefaultTheme.SidebarItem

// ── Sidebar helpers ───────────────────────────────────────────────────
const page = (text: string, path: string): Item => ({ text, link: `/${path}` })
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
function linkTree(indexPath: string, depth = 3, seen = new Set<string>()): Item {
  const file = join(SRC, indexPath)
  seen.add(normalize(file))
  const text = readFileSync(file, 'utf8')
  const root = dirname(file)
  const children: Item[] = []
  for (const m of text.matchAll(/\]\(((?!https?:|#)[^)#\s]+\.md)(?:#[^)]*)?\)/g)) {
    const target = normalize(join(root, m[1]))
    if (seen.has(target) || !existsSync(target) || !target.startsWith(root)) continue
    seen.add(target)
    const rel = relative(SRC, target)
    if (depth > 1 && /index\.md$/.test(rel)) {
      children.push({ ...linkTree(rel, depth - 1, seen), collapsed: true })
    } else {
      children.push(page(titleOf(target), rel.replace(/\.md$/, '')))
    }
  }
  return { text: titleOf(file), link: `/${indexPath.replace(/\.md$/, '')}`, items: children }
}

const safeTree = (indexPath: string, depth?: number): Item =>
  existsSync(join(SRC, indexPath))
    ? linkTree(indexPath, depth)
    : { text: `${indexPath} (run scripts/generate_reference.py)`, link: '/sdk/index' }

// ── Sidebars per top menu ─────────────────────────────────────────────
const quickStart: Item[] = [
  group('Getting Started', [
    page('Overview', 'getting-started/index'),
    page('Hello, RB-Y1', 'getting-started/hello_rby1'),
    page('Tutorial Videos', 'getting-started/tutorial_videos'),
  ]),
  group('First Steps', [
    page('1. E‑Stop Basics', 'getting-started/estop-basics'),
    page('2. Unboxing', 'getting-started/unboxing'),
    page('3. Hotspot & Web UI', 'getting-started/hotspot-and-webui'),
    page('4. External Access Point', 'getting-started/connect-external-ap'),
    page('5. SDK Installation', 'getting-started/sdk-install-and-state'),
  ]),
]

const manual: Item[] = [
  group('Safety', [
    page('Safety', 'precautions/index'),
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
    page('Electrical Part', 'hardware/electrical_part'),
    page('Battery', 'hardware/battery'),
  ]),
  group('Options', [page('Gripper', 'options/gripper'), page('Leader Arm', 'options/leader_arm')]),
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
    group('Robot Models', [
      page('Models', 'sdk/models/index'),
      page('Model A', 'sdk/models/generated/model_a'),
      page('Model M', 'sdk/models/generated/model_m'),
      page('Model UB', 'sdk/models/generated/model_ub'),
    ], true),
    group('Controllers', [
      page('Controllers', 'sdk/controllers/index'),
      page('Command and Control Architecture', 'sdk/controllers/generated/command_and_control_architecture'),
      page('Control Hold Time and Minimum Time', 'sdk/controllers/generated/control_hold_time_and_minimum_time'),
      page('Parameter Reference', 'sdk/controllers/generated/parameter'),
    ], true),
    page('Examples', 'examples/ex'),
    group('Troubleshooting', [
      page('Troubleshooting', 'sdk/trobuleshooting/index'),
      page('Build Issues', 'sdk/trobuleshooting/generated/build_issue'),
      page('Error Reporting', 'sdk/trobuleshooting/generated/error_reporting'),
      page('FAQ', 'sdk/trobuleshooting/generated/faq'),
    ], true),
  ]),
  group('ROS 2', [
    page('ROS 2', 'ros2/index'),
    ...[
      ['Overview', 'overview'], ['Install & Build', 'install_and_build'], ['Examples', 'examples'],
      ['Visualization & Robot Description', 'visualization_and_robot_description'], ['RBY1 MoveIt2', 'rby1_moveit2'],
      ['Package Architecture', 'package_architecture'], ['Config File', 'config_driver_parameters'],
      ['Key Features', 'key_features'], ['Topics', 'topics'], ['Services', 'services'],
      ['Action Servers', 'action_servers'], ['Custom Message Types', 'custom_message_types'],
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

const sidebarFor = (estopLink = '/getting-started/estop-basics'): DefaultTheme.SidebarMulti => {
  const qs = quickStart.map((g) => ({
    ...g,
    items: g.items?.map((i) => (i.link === '/getting-started/estop-basics' ? { ...i, link: estopLink } : i)),
  }))
  const s: DefaultTheme.SidebarMulti = {}
  for (const p of ['/getting-started/', '/ko/getting-started/']) s[p] = qs
  for (const p of ['/precautions/', '/hardware/', '/options/', '/maintenance/', '/rpc_management_tools/', '/legal/']) s[p] = manual
  for (const p of ['/software/', '/sdk/models/', '/sdk/controllers/', '/sdk/trobuleshooting/', '/examples/', '/ros2/', '/simulators/']) s[p] = software
  for (const p of ['/sdk/index', '/sdk/python/', '/sdk/cpp/', '/sdk/protos/']) s[p] = apiReference
  return s
}

// ── Top menu (same pattern as the RBQ manual) ────────────────────────
const nav = (ko: boolean): DefaultTheme.NavItem[] => {
  const t = (en: string, kr: string) => (ko ? kr : en)
  return [
    { text: t('Home', '홈'), link: ko ? '/ko/' : '/' },
    { text: t('Quick Start', '빠른 시작'), link: ko ? '/ko/getting-started/estop-basics' : '/getting-started/index', activeMatch: '/getting-started/' },
    {
      text: t('Manual', '매뉴얼'),
      activeMatch: '/(precautions|hardware|options|maintenance|rpc_management_tools|legal)/',
      items: [
        { text: t('Safety', '안전'), link: '/precautions/index' },
        { text: t('Hardware', '하드웨어'), link: '/hardware/index' },
        { text: t('Options', '옵션'), link: '/options/gripper' },
        { text: t('Maintenance & Tools', '유지보수·도구'), link: '/maintenance/index' },
      ],
    },
    {
      text: t('Software', '소프트웨어'),
      activeMatch: '/(software|sdk/models|sdk/controllers|sdk/trobuleshooting|examples|ros2|simulators)/',
      items: [
        { text: t('SDK Guide', 'SDK 가이드'), link: '/software/index' },
        { text: 'ROS 2', link: '/ros2/index' },
        { text: t('Simulation', '시뮬레이션'), link: '/simulators/index' },
      ],
    },
    {
      text: t('API Reference', 'API 레퍼런스'),
      activeMatch: '^/sdk/(index|python/|cpp/|protos/)',
      items: [
        { text: 'Python API', link: '/sdk/python/index' },
        { text: 'C++ API', link: '/sdk/cpp/index' },
        { text: 'Protobuf (gRPC) API', link: '/sdk/protos/index' },
      ],
    },
    { text: t('Download', '다운로드'), link: 'https://github.com/RainbowRobotics/rby1-release/releases' },
    { text: t('Support', '기술지원'), link: 'https://github.com/RainbowRobotics/rby1-sdk/discussions' },
    {
      text: SDK_VERSION,
      items: [{ text: t(`${SDK_VERSION} release notes`, `${SDK_VERSION} 릴리스 노트`), link: `https://github.com/RainbowRobotics/rby1-sdk/releases/tag/${SDK_VERSION}` }],
    },
  ]
}

// withMermaid: renders ```mermaid blocks (architecture diagrams in the ROS 2 pages).
export default withMermaid({
  base,
  title: 'RB-Y1',
  description: 'RB-Y1 dual-arm mobile manipulator: manual, SDK and API reference',
  // Keep the .html page URLs of the previous site so existing links keep working.
  cleanUrls: false,
  // Generated fragments pulled in with <!--@include-->, not pages of their own.
  srcExclude: ['hardware/generated/**'],
  lastUpdated: true,
  // The Doxygen HTML is a static folder in public/, not a VitePress page.
  ignoreDeadLinks: [/raw-api\//, /^https?:\/\/localhost/],
  head: [['link', { rel: 'icon', href: `${base}rb_logo.png` }]],
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

  locales: {
    root: { label: 'English', lang: 'en', themeConfig: { nav: nav(false), sidebar: sidebarFor() } },
    ko: {
      label: '한국어',
      lang: 'ko',
      link: '/ko/',
      themeConfig: {
        nav: nav(true),
        sidebar: sidebarFor('/ko/getting-started/estop-basics'),
        outline: { label: '이 페이지', level: [2, 3] },
        docFooter: { prev: '이전', next: '다음' },
      },
    },
  },

  themeConfig: {
    // Only a few pages are translated: the language menu goes to the Korean home page,
    // not to /ko/<same page>, which usually does not exist.
    i18nRouting: false,
    logo: '/rb_logo.png',
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/RainbowRobotics/rby1-sdk' },
      { icon: 'youtube', link: 'https://www.youtube.com/@rainbowrobotics' },
    ],
    editLink: {
      pattern: 'https://github.com/RainbowRobotics/rby1-dev/edit/dev/manual/:path',
      text: 'Edit this page on GitHub',
    },
    outline: { level: [2, 3] },
    footer: { copyright: `© 2024-${new Date().getFullYear()} Rainbow Robotics` },
  },
})
