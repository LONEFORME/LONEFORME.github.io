# LONEFORME.github.io 协作约定

## 布局宽度（必读）

| 页面类型 | body class | content-inner max-width | 用途 |
|----------|------------|-------------------------|------|
| 首页 / 热点 / 财经 / 项目 / 飞行演示 / 3D | `layout-wide` | **1560px** | 看板、卡片、播放器 |
| 文档 / 说明长文 | `layout-read` | **1100px** | 控制阅读行宽 |

**禁止**再把全站 `.content-inner` 写成过小的 `max-width`（例如 1240px）并 `margin: 0 auto` 却不区分页面：宽屏侧栏旁会出现大留白，看板像被缩小。

同类网格问题一并避免：

| 场景 | 错误做法 | 正确做法 |
|------|----------|----------|
| 9 张行情卡 | auto-fill 宽屏 4 列末行 1 张 | 宽屏 **5 列**（5+4） |
| 6 张项目卡 | auto-fill 宽屏 5 列剩 1 张 | 宽屏 **3 列**（3+3） |
| 4 张板块卡 | 超宽单行拉伸 | 宽屏 **2×2** |
| 视频剧场 / 项目橱窗 | 放进 layout-read 1100px | 用 **layout-wide** |

改完可用 `scripts/scan_layout_issues.py` 自检。

分类逻辑在 `_layouts/default.html` 的 `<body class="...">`；样式在 `assets/css/custom.css` 搜 `layout-wide`。

## 财经 / 新闻流水线

- 生成脚本：`scripts/news_digest.py`（定时 Actions）
- A 股新浪字段：`名称,今开,昨收,当前,...`，当前价在 **parts[3]**，勿取 parts[1]
- AI/芯片分类：禁止整站信源一刀切；`ai` 需词边界，避免 said/attention 误伤

## 大文件 / 隐私

- 不把安装包、简历、原片塞进本仓
- 联系方式若需变更，同步 `index.html` / `_layouts/default.html` / README
