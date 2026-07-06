# LONEFORME.github.io

> 个人网站 · 嵌入式开发 / ROS2 / 激光雷达 SLAM

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-已部署-222?logo=githubpages)](https://loneforme.github.io)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-CC342D?logo=jekyll)](https://jekyllrb.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](#许可证)

---

## 📋 关于本站

这是我（**LONEFORME**）的个人技术网站，专注于**机器人感知与导航**方向。站点托管于 GitHub Pages，使用 Jekyll 静态站点生成器构建，记录了我在以下领域的研究与实践：

- ⚡ **ROS2** 机器人操作系统开发
- 📡 **激光雷达驱动**封装与适配
- 🗺️ **SLAM** 建图与导航方案
- 🔧 **嵌入式 Linux** 系统开发
- 🧭 **多传感器融合**技术

访问地址：**[loneforme.github.io](https://loneforme.github.io)**

---

## 🚀 功能特性

| 功能 | 说明 |
|------|------|
| 📂 **项目展示** | ROS2 激光雷达驱动、SLAM 建图方案等开源项目 |
| 📖 **技术文档** | 详细的硬件驱动与 SLAM 搭建教程 |
| 📰 **热点新闻速览** | AI 自动抓取 RSS 并汇总每日新闻（GitHub Actions 定时更新） |
| 🏠 **个人主页** | 技术标签、联系方式、精选项目展示 |

---

## 📦 站点结构

```
LONEFORME.github.io/
├── _layouts/              # Jekyll 布局模板
│   └── default.html       # 主页面布局
├── assets/
│   └── css/
│       └── custom.css     # 自定义样式
├── docs/                  # 技术文档
│   ├── unitree_l1.md      # 宇树 L1 + FAST-LIO2 建图方案
│   └── leishen_n10p.md    # 镭神 N10P + SLAM Toolbox 方案
├── scripts/
│   └── news_digest.py     # 新闻摘要自动化脚本（RSS + AI 总结）
├── .github/workflows/
│   └── news-digest.yml    # 新闻自动更新 GitHub Actions 工作流
├── _config.yml            # Jekyll 站点配置
├── index.md               # 首页
├── projects.md            # 项目页面
├── docs.md                # 文档页面
├── news.md                # 热点新闻页面（自动生成）
└── .gitignore
```

---

## 🔧 本地运行

如果你想在本地运行此站点：

### 前置依赖

- [Ruby](https://www.ruby-lang.org/) (>= 2.7)
- [Jekyll](https://jekyllrb.com/) 和 Bundler

### 步骤

```bash
# 1. 克隆仓库
git clone https://github.com/LONEFORME/LONEFORME.github.io.git
cd LONEFORME.github.io

# 2. 安装依赖
bundle install

# 3. 启动本地开发服务器
bundle exec jekyll serve

# 4. 打开浏览器访问 http://localhost:4000
```

---

## 🤖 新闻自动更新

站点内置了新闻摘要自动化系统：

- **`scripts/news_digest.py`** — Python 脚本，从 RSS 源抓取新闻，使用 AI API 进行摘要与分类
- **GitHub Actions** — 每天定时运行，自动更新 `news.md` 页面
- 支持按主题标签切换（时政、科技 AI、国际、社会、财经等）

---

## 🔗 相关项目

| 项目 | 描述 |
|------|------|
| [📡 宇树 L1 激光雷达 ROS2 驱动](https://github.com/LONEFORME/N100) | Unitree L1 激光雷达 ROS2 封装驱动 |
| [🔭 镭神 N10P ROS2 驱动与 SLAM](https://github.com/LONEFORME/N100) | Leishen 单线激光雷达驱动，集成 SLAM Toolbox 导航方案 |
| [🧭 FAST-LIO2 宇树雷达适配](https://github.com/LONEFORME/N100) | 实时激光雷达-惯性里程计建图，适配宇树 L 系列雷达 |
| [🔄 T265 自动 Boot](https://github.com/LONEFORME/N100) | Intel RealSense T265 追踪相机固件加载脚本 |

---

## 📬 联系方式

- ✉️ **Email**: [lonefasf@qq.com](mailto:lonefasf@qq.com)
- 💬 **QQ**: 2641881852
- 💻 **GitHub**: [@LONEFORME](https://github.com/LONEFORME)

---

## 📄 许可证

本项目采用 **MIT 许可证**。详情请参阅 [LICENSE](LICENSE) 文件。

---

<p align="center">
  用 ❤️ 和 ROS2 构建 · © 2026 LONEFORME
</p>
