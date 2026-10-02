import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '电赛无人机全栈技术知识库',
  description: '机器人感知与导航 · 嵌入式系统 · 激光雷达 SLAM · 计算机视觉 · 电赛无人机全栈工程',
  lang: 'zh-CN',
  base: '/drone/',
  srcDir: 'drone-src',
  outDir: 'drone',
  cleanUrls: true,
  ignoreDeadLinks: true,
  markdown: {
    math: true,
    lineNumbers: true
  },
  themeConfig: {
    siteTitle: '🚁 无人机全栈知识库',
    nav: [
      { text: '🧭 知识库首页', link: '/' },
      { text: '🏠 个人主页', link: 'https://loneforme.github.io/' },
      { text: '📂 精选项目', link: 'https://loneforme.github.io/projects' },
      { text: '🧊 3D 预览', link: 'https://loneforme.github.io/3d-viewer.html' },
      { text: 'GitHub', link: 'https://github.com/LONEFORME' }
    ],
    sidebar: [
      {
        text: '🚁 六大核心技术模块',
        collapsed: false,
        items: [
          { text: '🧭 知识库总览 (Index)', link: '/' },
          { text: '01 硬件底座与电气规范', link: '/01_硬件底座与电气规范' },
          { text: '02 飞控系统与控制算法', link: '/02_飞控系统与控制算法' },
          { text: '03 室内自主定位与避障', link: '/03_室内自主定位与避障' },
          { text: '04 机器视觉与目标检测', link: '/04_机器视觉与目标检测' },
          { text: '05 路径规划与自主决策', link: '/05_路径规划与自主决策' },
          { text: '06 合规交互与机械结构', link: '/06_合规交互与机械结构' }
        ]
      },
      {
        text: '🏆 赛题指南与上手实战',
        collapsed: false,
        items: [
          { text: '01 电赛无人机入门指南', link: '/guides/01_电赛无人机方向入门指南' },
          { text: '02 全栈开发路径与实战指南', link: '/guides/02_电赛无人机全栈开发学习路径与实战指南' },
          { text: '03 新生零基础成长路线与实战指引', link: '/guides/03_大一新生零基础成长路线与实战指引' },
          { text: '04 锡月无人机上手方案', link: '/guides/04_锡月无人机上手方案' },
          { text: '05 凌霄无人机上手方案', link: '/guides/05_凌霄无人机上手方案' }
        ]
      }
    ],
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索知识库',
            buttonAriaLabel: '搜索知识库'
          },
          modal: {
            noResultsText: '无法找到相关结果',
            resetButtonTitle: '清除查询条件',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭'
            }
          }
        }
      }
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/LONEFORME' }
    ],
    footer: {
      message: '电赛无人机与全栈工程技术知识库 · 遵循 PolyForm Noncommercial 1.0.0 许可',
      copyright: 'Copyright © 2026 LONEFORME (旧梦如常)'
    }
  }
})
