<div align="center">

# 🌐 LONEFORME 个人网站
### LONEFORME.github.io

*嵌入式开发 · ROS2 · 激光雷达 SLAM · 计算机视觉 · 每日新闻财经*

**访问地址：[loneforme.github.io](https://loneforme.github.io)**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-已部署-222?logo=githubpages)](https://loneforme.github.io)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-CC342D?logo=jekyll)](https://jekyllrb.com)
[![News](https://img.shields.io/badge/每日新闻-自动更新-green.svg)]()
[![Finance](https://img.shields.io/badge/财经看板-实时数据-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue)](#许可证)

</div>

---

## 📑 快速导航

| 分类 | 链接 | 说明 |
|------|------|------|
| 🏠 | [个人主页](https://loneforme.github.io) | 技术标签、精选项目、联系方式 |
| 📂 | [项目展示](https://loneforme.github.io/projects) | ROS2 驱动、SLAM 建图、视觉识别、无人机 |
| 📖 | [技术文档](https://loneforme.github.io/docs) | 硬件驱动与 SLAM 搭建教程 |
| 📰 | [热点新闻](https://loneforme.github.io/news) | AI 自动抓取翻译，每日更新 |
| 📈 | [股票财经](https://loneforme.github.io/finance) | 全球股指、资金流向、财经资讯 |
| 🧊 | [3D 模型查看器](https://loneforme.github.io/3d-viewer) | 在线预览 STL 3D 打印模型 |
| 📁 | [新闻存档](https://loneforme.github.io/archive) | 历史新闻归档，可回溯查阅 |

---

## ✨ 功能特性

### 🏠 个人主页
- 技术标签云、精选项目展示
- 联系方式（Email / QQ / GitHub）
- 暗色/亮色主题一键切换，自动记忆偏好

### 📂 项目展示
- ROS2 驱动开发、激光雷达 SLAM 建图
- 计算机视觉识别、无人机竞赛方案
- 3D 打印模型库（6 大分类，100+ 模型）

### 📖 技术文档
- 宇树 L1 激光雷达 + Point-LIO 建图方案
- 镭神 N10P + SLAM Toolbox 建图方案
- 树莓派 4B 部署指南

### 📰 热点新闻（AI 自动更新）
- **11 个 RSS 信源**：BBC、天空体育、卫报、人民网、中国新闻网、纽约时报等
- **英文自动翻译**：Google Translate + MyMemory 双引擎，无需 API key
- **5 大分类板块**：⚽ 英超足球 / 🤖 科技AI / 🏛️ 时政国际 / 📰 综合社会 / 🌍 西方媒体视角
- **智能过滤**：自动过滤服务器错误页面、无效标题
- **头条焦点区** + 分类 Tab 切换 + 来源徽章+国旗 + 悬浮摘要弹窗
- **30 天历史存档**，可回溯查阅

### 📈 股票财经看板（每日更新）
- **8 大全球股指**：上证指数、深证成指、创业板指、科创50、恒生科技、纳斯达克100、美元/离岸人民币、伦敦现货黄金
- **实时行情数据**（新浪财经 API），失败时自动回退参考值
- **4 大热门赛道**资金流向参考：AI算力、新能源、具身智能、高股息红利
- **每日财经资讯**聚合，与新闻系统联动

### 🧊 3D 模型查看器
- 在线预览 STL 格式 3D 打印模型
- 6 大分类：飞控与无人机 / 摄像头系统 / 小车底盘 / 激光与传感器 / 树莓派相关 / 其他零件
- 100+ 模型，支持旋转、缩放、平移查看

---

## 📦 站点结构

```
LONEFORME.github.io/
├── 📄 页面文件（根目录）
│   ├── index.html              # 🏠 首页
│   ├── projects.md             # 📂 项目展示
│   ├── docs.md                 # 📖 技术文档索引
│   ├── news.md                 # 📰 热点新闻（自动生成）
│   ├── finance.md              # 📈 股票财经（自动生成）
│   ├── 3d-viewer.html          # 🧊 3D 模型查看器
│   └── 404.md                  # ❌ 404 页面
│
├── 🎨 Jekyll 配置
│   ├── _config.yml             # Jekyll 站点配置
│   ├── _layouts/
│   │   └── default.html        # 主页面布局（含主题切换）
│   ├── _includes/
│   │   └── card-mini.html      # 迷你卡片组件
│   └── assets/
│       └── css/custom.css      # 自定义样式
│
├── 📚 内容目录
│   ├── docs/                   # 技术文档
│   │   ├── unitree_l1.md       # 宇树 L1 + Point-LIO 建图
│   │   ├── leishen_n10p.md     # 镭神 N10P + SLAM Toolbox
│   │   └── rpi4_deploy.md      # 树莓派 4B 部署指南
│   ├── models/                  # 3D 打印模型库
│   │   ├── models.json           # 3D 模型数据索引
│   │   ├── 01-飞控与无人机/     # 飞控板、摄像头支架、保护罩等
│   │   ├── 02-摄像头系统/       # 摄像头支架、舵机云台等
│   │   ├── 03-小车底盘/         # 底盘、电机支架、拓展坞等
│   │   ├── 04-激光与传感器/     # 激光雷达支架、定高板等
│   │   ├── 05-树莓派相关/       # 树莓派固定、雷达支架等
│   │   └── 06-其他零件/         # 杂项零件
│   └── archive/                 # 📰 新闻历史存档（30天）
│       ├── index.md             # 存档索引页
│       └── news-YYYY-MM-DD.md  # 每日新闻存档
│
├── 🤖 自动化脚本
│   └── scripts/
│       └── news_digest.py      # 新闻+财经自动生成脚本
│                                # （RSS抓取、英文翻译、智能分类、错误过滤、股指获取）
│
├── ⚙️ GitHub Actions
│   └── .github/workflows/
│       └── news-digest.yml     # 每日自动更新工作流
│                                # （北京时间 08:00 每日 + 15:00 工作日收盘）
│
├── .gitignore
├── .gitattributes
└── README.md
```

---

## 🤖 新闻与财经自动更新系统

### 系统架构

```
RSS 信源（11个）
    ↓
抓取 + 清洗 + 去重
    ↓
英文自动翻译（Google Translate + MyMemory 双引擎）
    ↓
智能分类（5大板块 + 错误页面过滤 + 敏感内容识别）
    ↓
┌─────────────┴─────────────┐
↓                           ↓
生成 news.md              获取股指行情（新浪财经API）
（5大分类板块）                ↓
                        生成 finance.md
                        （股指看板 + 赛道资金 + 财经资讯）
    ↓                           ↓
    └───────────┬─────────────┘
                ↓
        GitHub Actions 自动提交推送
                ↓
        GitHub Pages 自动部署
```

### 更新时间

| 时间（北京时间） | 说明 |
|-----------------|------|
| **每天 08:00** | 每日早盘前更新新闻 + 财经 |
| **工作日 15:00** | A股收盘后更新财经数据 |

### 技术亮点

- **双翻译引擎**：Google Translate 为主，MyMemory 为备用，完全免费无需 API key
- **智能错误过滤**：自动检测并过滤 RSS 源和翻译服务返回的 500/404 错误页面
- **5 大新闻分类**：英超足球 / 科技AI / 时政国际 / 综合社会 / 西方媒体视角
- **8 大全球股指**：A股4大指数 + 恒生科技 + 纳斯达克100 + 离岸人民币 + 黄金
- **30 天存档**：自动维护历史新闻档案，可回溯查阅

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

### 手动运行新闻更新脚本

```bash
# 安装 Python 依赖
pip install feedparser requests zhconv deep-translator

# 运行脚本（生成 news.md + finance.md + archive/）
python scripts/news_digest.py
```

---

## 🔗 相关项目

| 项目 | 描述 |
|------|------|
| [embedded-board-reference](https://github.com/LONEFORME/embedded-board-reference) | 嵌入式开发板参考配置（7款板子一键部署） |
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

<div align="center">

## 📄 许可证

**MIT License**

*© 2026 LONEFORME · Made with ❤️*

</div>
