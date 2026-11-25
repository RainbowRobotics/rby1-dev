import { defineConfig, type DefaultTheme } from 'vitepress'

// Site root on GitHub Pages; override with VP_BASE for local previews.
const base = process.env.VP_BASE ?? '/rby1-dev/'
// The API reference is a Sphinx build published under <base>api/ (see doc/).
// It is not part of this VitePress app, so links to it use target _self (plain page loads).
// VitePress adds `base` to these site-relative links itself.
const api = (path: string) => `${process.env.API_URL ?? '/api/'}${path}`
const SDK_VERSION = process.env.SDK_VERSION ?? 'v0.10.1'

const apiItems = (lang: 'en' | 'ko'): DefaultTheme.NavItemWithLink[] => [
  { text: lang === 'ko' ? 'Python API' : 'Python API', link: api('sdk/python/index.html'), target: '_self' },
  { text: 'C++ API', link: api('sdk/cpp/index.html'), target: '_self' },
  { text: 'Protobuf (gRPC) API', link: api('sdk/protos/index.html'), target: '_self' },
]

const versionNav: DefaultTheme.NavItemWithChildren = {
  text: SDK_VERSION,
  items: [{ text: `${SDK_VERSION} (latest)`, link: '/' }],
}

function sidebar(prefix: string, ko: boolean): DefaultTheme.Sidebar {
  const t = (en: string, kr: string) => (ko ? kr : en)
  return [
    {
      text: t('Getting Started', '시작하기'),
      items: [
        { text: t('1. E‑Stop Basics', '1. 비상정지(E‑Stop)'), link: `${prefix}getting-started/estop-basics` },
        { text: t('3. Hotspot & Web UI', '3. 핫스팟과 Web UI'), link: '/getting-started/hotspot-and-webui' },
        { text: t('5. SDK Installation', '5. SDK 설치'), link: '/getting-started/sdk-install-and-state' },
      ],
    },
    {
      text: t('Hardware', '하드웨어'),
      items: [{ text: t('Overview', '개요'), link: '/hardware/overview' }],
    },
    {
      text: t('Simulation', '시뮬레이션'),
      items: [{ text: 'MuJoCo', link: '/simulators/mujoco' }],
    },
    {
      text: 'ROS 2',
      items: [{ text: t('Install & Build', '설치와 빌드'), link: '/ros2/ros2_driver/install_and_build' }],
    },
    {
      text: t('API Reference', 'API 레퍼런스'),
      items: apiItems(ko ? 'ko' : 'en'),
    },
  ]
}

export default defineConfig({
  base,
  title: 'RB-Y1',
  description: 'RB-Y1 dual-arm mobile manipulator: manual, SDK and API reference',
  // Keep the .html page URLs of the previous site so existing links keep working.
  cleanUrls: false,
  lastUpdated: true,
  // Sample build: pages that are not migrated yet are linked but absent.
  ignoreDeadLinks: true,
  head: [['link', { rel: 'icon', href: `${base}rb_logo.png` }]],

  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Quick Start', link: '/getting-started/estop-basics' },
          {
            text: 'Manual',
            items: [
              { text: 'Hardware', link: '/hardware/overview' },
              { text: 'Simulation', link: '/simulators/mujoco' },
              { text: 'ROS 2', link: '/ros2/ros2_driver/install_and_build' },
            ],
          },
          { text: 'API Reference', items: apiItems('en') },
          { text: 'Download', link: 'https://github.com/RainbowRobotics/rby1-release/releases' },
          { text: 'Support', link: 'https://github.com/RainbowRobotics/rby1-sdk/discussions' },
          versionNav,
        ],
        sidebar: sidebar('/', false),
      },
    },
    ko: {
      label: '한국어',
      lang: 'ko',
      link: '/ko/',
      themeConfig: {
        nav: [
          { text: '홈', link: '/ko/' },
          { text: '빠른 시작', link: '/ko/getting-started/estop-basics' },
          {
            text: '매뉴얼',
            items: [
              { text: '하드웨어', link: '/hardware/overview' },
              { text: '시뮬레이션', link: '/simulators/mujoco' },
              { text: 'ROS 2', link: '/ros2/ros2_driver/install_and_build' },
            ],
          },
          { text: 'API 레퍼런스', items: apiItems('ko') },
          { text: '다운로드', link: 'https://github.com/RainbowRobotics/rby1-release/releases' },
          { text: '기술지원', link: 'https://github.com/RainbowRobotics/rby1-sdk/discussions' },
          versionNav,
        ],
        sidebar: sidebar('/ko/', true),
        outline: { label: '이 페이지' },
        docFooter: { prev: '이전', next: '다음' },
      },
    },
  },

  themeConfig: {
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
