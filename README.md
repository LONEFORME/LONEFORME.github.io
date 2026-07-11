# LONEFORME.github.io

> 个人网站 · 嵌入式开发 / ROS2 / 激光雷达 SLAM / 计算机视觉

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-已部署-222?logo=githubpages)](https://loneforme.github.io)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-CC342D?logo=jekyll)](https://jekyllrb.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](#许可证)

---

## 📋 关于本站

这是我（**LONEFORME**）的个人技术网站，专注于**机器人感知与导航**方向。站点托管于 GitHub Pages，使用 Jekyll 静态站点生成器构建。

访问地址：**[loneforme.github.io](https://loneforme.github.io)**

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🏠 **个人主页** | 技术标签、精选项目、联系方式展示 |
| 📂 **项目展示** | ROS2 驱动、SLAM 建图、视觉识别、无人机方案 |
| 📖 **技术文档** | 硬件驱动与 SLAM 搭建教程 |
| 📰 **热点新闻** | AI 自动抓取 RSS 并汇总每日新闻（GitHub Actions 定时更新） |
| 🌓 **暗色/亮色主题** | 一键切换，自动记忆偏好 |

---

## 📦 站点结构

```
LONEFORME.github.io/
├── _layouts/
│   └── default.html               # 主页面布局（含主题切换）
├── _includes/
│   └── card-mini.html             # 迷你卡片组件
├── assets/css/
│   └── custom.css                 # 自定义样式
├── docs/                          # 技术文档
│   ├── unitree_l1.md              # 宇树 L1 + Point-LIO 建图方案
│   └── leishen_n10p.md            # 镭神 N10P + SLAM Toolbox 方案
├── scripts/
│   └── news_digest.py             # 新闻摘要自动化脚本（RSS + AI 总结）
├── .github/workflows/
│   └── news-digest.yml            # 每日新闻自动更新工作流
├── _config.yml                    # Jekyll 站点配置
├── index.html                     # 首页
├── projects.md                    # 项目页面
├── docs.md                        # 文档页面
└── news.md                        # 热点新闻页面（自动生成）
```

---

## 🔧 本地运行

```bash
# 克隆仓库
git clone https://github.com/LONEFORME/LONEFORME.github.io.git
cd LONEFORME.github.io

# 安装依赖
bundle install

# 启动本地开发服务器
bundle exec jekyll serve

# 浏览器访问 http://localhost:4000
```

---

## 🤖 新闻自动更新

站点内置新闻摘要自动化系统：

- **`scripts/news_digest.py`** — 从 9 个 RSS 信源抓取新闻，AI 分类总结
- **GitHub Actions** — 每天 UTC 00:00（北京时间 08:00）自动运行
- **功能**：头条焦点区、分类 Tab 切换、彩色标签、来源徽章+国旗、新闻摘要弹窗
- **降级机制**：AI API 不可用时自动回退到 RSS 原始数据展示

---

## 🔗 相关项目

| 项目 | 描述 |
|------|------|
| [N100](https://github.com/LONEFORME/N100) | ROS2 激光雷达驱动 + Point-LIO / SLAM Toolbox |
| [ZCodeProject](https://github.com/LONEFORME/ZCodeProject) | 综合视觉识别系统 |
| [xiyue-drone](https://github.com/LONEFORME/xiyue-drone) | 2025 年电赛无人机方案 |
| [3d-models](https://github.com/LONEFORME/3d-models) | 3D 打印模型库 |

---

## 📬 联系方式

- ✉️ **Email**: [lonefasf@qq.com](mailto:lonefasf@qq.com)
- 💬 **QQ**: 2641881852
- 💻 **GitHub**: [@LONEFORME](https://github.com/LONEFORME)

---

## 📄 许可证

MIT License

---

<p align="center">© 2026 LONEFORME</p>
