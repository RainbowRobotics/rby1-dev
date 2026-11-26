// Default VitePress theme with the Rainbow Robotics colors shared by the other product manuals
// (rb_cobot_docs, RBQ, RB-S100).
import DefaultTheme from 'vitepress/theme'
import { withBase } from 'vitepress'
import type { Theme } from 'vitepress'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Raw HTML in pages (e.g. <video> sources from public/) needs the site base: :src="$withBase('/videos/...')".
    app.config.globalProperties.$withBase = withBase
  },
} satisfies Theme
