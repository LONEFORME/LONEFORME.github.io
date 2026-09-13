# LONEFORME.github.io 协作约定

## 布局宽度（必读）

| 页面类型 | body class | content-inner max-width | 用途 |
|----------|------------|-------------------------|------|
| 首页 / 热点 / 财经 | `layout-wide` | **1560px** | 看板、多列卡片，宽屏要铺满 |
| 文档 / 项目说明等长文 | `layout-read` | **1100px** | 控制阅读行宽 |

**禁止**再把全站 `.content-inner` 写成过小的 `max-width`（例如 1240px）并 `margin: 0 auto` 却不区分页面：宽屏侧栏旁会出现大留白，看板像被缩小。

宽屏多卡网格优先用 `repeat(5, 1fr)` 或 `auto-fit/minmax`，避免「9 张卡只剩末行 1 张」。

分类逻辑在 `_layouts/default.html` 的 `<body class="...">`；样式在 `assets/css/custom.css` 搜 `layout-wide`。

## 财经 / 新闻流水线

- 生成脚本：`scripts/news_digest.py`（定时 Actions）
- A 股新浪字段：`名称,今开,昨收,当前,...`，当前价在 **parts[3]**，勿取 parts[1]
- AI/芯片分类：禁止整站信源一刀切；`ai` 需词边界，避免 said/attention 误伤

## 大文件 / 隐私

- 不把安装包、简历、原片塞进本仓
- 联系方式若需变更，同步 `index.html` / `_layouts/default.html` / README
