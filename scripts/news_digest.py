#!/usr/bin/env python3
"""News Digest - 抓取 RSS 新闻并用 AI 总结，生成带标签页的网站页面"""

import feedparser
import os
import requests
import re
from datetime import datetime

log = lambda msg: print(msg, flush=True)

UA = "Mozilla/5.0 (compatible; NewsDigest/1.0; +https://loneforme.github.io)"

RSS_FEEDS = [
    # 国内官方权威媒体
    {"url": "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=zh-CN&gl=CN&ceid=CN:zh-Hans", "name": "Google 新闻(时政)"},
    {"url": "http://www.people.com.cn/rss/politics.xml", "name": "人民网(时政)"},
    {"url": "http://www.people.com.cn/rss/world.xml", "name": "人民网(国际)"},
    {"url": "http://www.people.com.cn/rss/scitech.xml", "name": "人民网(科技)"},
    {"url": "https://www.chinanews.com.cn/rss/scroll-news.xml", "name": "中国新闻网(滚动)"},
    # 国际权威媒体
    {"url": "https://www.bbc.co.uk/zhongwen/simp/index.xml", "name": "BBC 中文"},
    {"url": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "name": "纽约时报"},
    {"url": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "name": "纽约时报(国际)"},
    {"url": "https://www.cbsnews.com/latest/rss/main", "name": "CBS News"},
    {"url": "https://feeds.npr.org/1001/rss.xml", "name": "NPR(含AP美联社)"},
    # 科技财经
    {"url": "https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRDZ0FQAQ?hl=zh-CN&gl=CN&ceid=CN:zh-Hans", "name": "Google 新闻(科技)"},
]

API_URL = "https://opencode.ai/zen/go/v1/chat/completions"
API_KEY = os.environ.get("OPENCODE_GO_API_KEY")
MODEL = "deepseek-v4-flash"
MAX_ARTICLES_PER_FEED = 6
MAX_TOTAL = 30


def parse_publisher(title):
    """从标题末尾提取来源，如 '标题 - 人民日报' → ('标题', '人民日报')"""
    m = re.search(r'\s*[-–—]\s*(.+)$', title)
    if m:
        pub = m.group(1).strip()
        t = title[:m.start()].strip()
        if len(pub) < 20 and not pub.startswith("http"):
            return t, pub
    return title, ""


def fetch_rss(url, source_name, timeout=20):
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": UA})
        r.raise_for_status()
        feed = feedparser.parse(r.content)
        entries = []
        for entry in feed.entries[:MAX_ARTICLES_PER_FEED]:
            title = entry.get("title", "").strip()
            link = entry.get("link", "")
            published = entry.get("published", entry.get("updated", ""))
            if title and link:
                clean_title, publisher = parse_publisher(title)
                src = publisher if publisher else source_name
                entries.append({
                    "title": clean_title,
                    "link": link,
                    "date": published[:10] if published else "",
                    "source": src
                })
        return entries
    except Exception as e:
        log(f"  [ERROR] 抓取失败: {e}")
        return []


def summarize_news(news_items, api_key):
    if not api_key:
        log("[ERROR] OPENCODE_GO_API_KEY 未设置")
        if os.environ.get("GITHUB_ACTIONS"):
            log(f"  [DEBUG] API_KEY 前4位: {api_key[:4] if api_key else 'N/A'}")
        return None

    lines = []
    for item in news_items:
        lines.append(f"[{item['date'] or '?'}] [{item['source']}] {item['title']}")
    news_text = "\n".join(lines)
    log(f"[DEBUG] 发送给 API 的文本长度: {len(news_text)} 字符")

    system_prompt = """你是资深新闻编辑。任务：整理以下新闻。

步骤1：审查内容 — 优先采用权威媒体（新华社、人民日报、央视、BBC、纽约时报等），剔除明显不实信息。
步骤2：按主题分类（时政、科技AI、国际、社会、财经、体育、军事、其他），每类精选最多5条。
步骤3：输出以下格式，每篇末尾标注来源。

格式：
### 分类名
- **日期** | **标题** | 详细内容 [来源: XXX]

要求：
- 分类名请从（时政、科技AI、国际、社会、财经、体育、军事、其他）中选
- 每类≤5条
- 日期 YYYY-MM-DD
- 详细内容必须不少于400字，包含：事件背景、核心内容、相关数据、影响分析、专家观点等
- 末尾 [来源: XXX] 标明出处
- 不要链接，不要推理过程"""

    try:
        log(f"[DEBUG] 请求模型: {MODEL}, URL: {API_URL}")
        resp = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": news_text}
                ],
                "max_tokens": 16384,
                "temperature": 0.3
            },
            timeout=120
        )
        log(f"[DEBUG] API 响应状态码: {resp.status_code}")
        if resp.status_code != 200:
            log(f"[DEBUG] API 响应体: {resp.text[:500]}")
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        log(f"[DEBUG] API 返回内容长度: {len(content)} 字符")
        log(f"[DEBUG] API 返回内容前200字: {content[:200]}")
        return content if content.strip() else None
    except Exception as e:
        log(f"[ERROR] API 调用失败: {e}")
        if "resp" in dir():
            log(f"  Status: {resp.status_code}")
            log(f"  响应片段: {resp.text[:300]}")
        return None


def parse_categories(ai_output):
    """Parse AI output into list of (category_name, [item_lines])"""
    categories = []
    current_cat = None
    current_items = []

    for line in ai_output.strip().split("\n"):
        line = line.strip()
        if line.startswith("### "):
            # Save previous category
            if current_cat:
                categories.append((current_cat, current_items))
            current_cat = line[4:].strip()
            current_items = []
        elif line.startswith("- ") and current_cat:
            current_items.append(line)

    if current_cat:
        categories.append((current_cat, current_items))

    return categories


def cat_name_to_id(name):
    """Map Chinese category name to HTML id suffix"""
    mapping = {
        "时政": "shizheng",
        "科技AI": "keji",
        "科技": "keji",
        "国际": "guoji",
        "社会": "shehui",
        "财经": "caijing",
        "体育": "tiyu",
        "军事": "junshi",
        "其他": "qita",
    }
    return mapping.get(name.strip(), "qita")


def cat_name_short(name):
    """Short display name for tab button"""
    mapping = {
        "时政": "时政",
        "科技AI": "科技",
        "科技": "科技",
        "国际": "国际",
        "社会": "社会",
        "财经": "财经",
        "体育": "体育",
        "军事": "军事",
        "其他": "其他",
    }
    return mapping.get(name.strip(), name.strip())


def item_to_html(line):
    """Convert a single markdown item line to news-card HTML"""
    # Pattern: - **DATE** | **TITLE** | SUMMARY [来源: XXX]
    m = re.match(r'-\s+\*\*([^*]+)\*\*\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*(.+?)(?:\s*\[来源:\s*([^\]]+)\])?\s*$', line)
    if m:
        date = m.group(1).strip()
        title = m.group(2).strip()
        detail = m.group(3).strip()
        source = m.group(4).strip() if m.group(4) else ""
        
        # Escape HTML entities for data attribute
        detail_escaped = detail.replace('"', '&quot;').replace("'", '&#39;')
        
        html = f'              <div class="news-card" onclick="showNewsDetail(this)" data-detail="{detail_escaped}" data-title="{title}" data-date="{date}" data-source="{source}">\n'
        html += f'                <div class="news-date-badge">{date}</div>\n'
        html += f'                <div class="news-card-title">{title}</div>\n'
        html += f'                <div class="news-card-summary">{detail[:80]}...</div>\n'
        if source:
            html += f'                <div class="news-card-source">{source}</div>\n'
        html += f'                <div class="news-card-more">点击查看详情 →</div>\n'
        html += f'              </div>\n'
        return html
    
    # Fallback: treat as plain text
    clean = re.sub(r'^\-\s+', '', line)
    return f'              <div class="news-card"><div class="news-card-summary">{clean}</div></div>\n'


def generate_tabbed_html(categories, date_str):
    """Generate horizontal tabbed news HTML with prev/next buttons"""

    tabs = []
    for cat_name, items in categories:
        tab_id = cat_name_to_id(cat_name)
        short_name = cat_name_short(cat_name)
        tabs.append((tab_id, short_name, cat_name, items))

    if not tabs:
        return "<p>暂无新闻数据。</p>"

    total_count = sum(len(items) for _, _, _, items in tabs)

    html = '<div class="news-tabs">\n'

    # Radio inputs MUST be direct children of .news-tabs for CSS ~ selector
    html += '  <input type="radio" name="news-tab" id="tab-all" checked>\n'
    for tab_id, _, _, items in tabs:
        html += f'  <input type="radio" name="news-tab" id="tab-{tab_id}">\n'

    # Tab bar
    html += '  <div class="tab-bar" id="newsTabBar">\n'
    html += f'    <label for="tab-all" class="tab-label">\U0001f4cb \u5168\u90e8 <span class="tab-count">{total_count}</span></label>\n'

    icon_map = {
        "shizheng": "\U0001f3db\ufe0f", "keji": "\U0001f916", "guoji": "\U0001f30d", "shehui": "\U0001f52c",
        "caijing": "\U0001f4b0", "tiyu": "\u26bd", "junshi": "\u2694\ufe0f", "qita": "\U0001f4ce"
    }
    for tab_id, short_name, _, items in tabs:
        icon = icon_map.get(tab_id, "\U0001f4cb")
        html += f'    <label for="tab-{tab_id}" class="tab-label">{icon} {short_name} <span class="tab-count">{len(items)}</span></label>\n'
    html += '  </div>\n\n'

    # Navigation buttons
    html += '  <div class="tab-nav">\n'
    html += '    <button class="tab-nav-btn tab-prev" onclick="switchTab(-1)" title="\u4e0a\u4e00\u4e2a\u5206\u7c7b" aria-label="Previous">\u2039</button>\n'
    html += '    <div class="tab-nav-indicator" id="tabIndicator">\u5168\u90e8</div>\n'
    html += '    <button class="tab-nav-btn tab-next" onclick="switchTab(1)" title="\u4e0b\u4e00\u4e2a\u5206\u7c7b" aria-label="Next">\u203a</button>\n'
    html += '  </div>\n\n'

    # Summary line
    html += f'  <div class="news-summary-line">{date_str} \u00b7 \u5171 {total_count} \u6761\u65b0\u95fb \u00b7 \u70b9\u51fb\u6807\u7b7e\u6216 \u2190 \u2192 \u952e\u5207\u6362</div>\n\n'

    # "All" panel
    html += '  <div class="tab-panel" id="panel-all">\n'
    for _, _, _, items in tabs:
        for item in items:
            html += item_to_html(item)
    html += '  </div>\n\n'

    # Category panels
    for tab_id, short_name, _, items in tabs:
        html += f'  <div class="tab-panel" id="panel-{tab_id}">\n'
        if items:
            for item in items:
                html += item_to_html(item)
        else:
            html += f'    <div class="news-card"><div class="news-card-summary">\u6682\u65e0 {short_name} \u7c7b\u65b0\u95fb\u3002</div></div>\n'
        html += '  </div>\n\n'

    html += '</div>\n'

    # JavaScript for prev/next navigation and modal
    # Build the comma-separated list of tab IDs
    tab_ids = ", ".join('"' + t[0] + '"' for t in tabs)
    html += '''
<script>
(function() {
  const tabIds = ["all", ''' + tab_ids + '''];
  let currentIdx = 0;

  window.switchTab = function(dir) {
    currentIdx = (currentIdx + dir + tabIds.length) % tabIds.length;
    const id = tabIds[currentIdx];
    const radio = document.getElementById("tab-" + id);
    if (radio) {
      radio.checked = true;
      radio.dispatchEvent(new Event("change", { bubbles: true }));
    }
    updateIndicator();
    scrollTabIntoView(id);
  };

  function updateIndicator() {
    const id = tabIds[currentIdx];
    const indicator = document.getElementById("tabIndicator");
    const label = document.querySelector("label[for='tab-" + id + "']");
    if (label && indicator) {
      let text = label.textContent.trim();
      text = text.replace(/\\s*\\d+\\s*$/, "").trim();
      indicator.textContent = text;
    }
  }

  function scrollTabIntoView(id) {
    const label = document.querySelector("label[for='tab-" + id + "']");
    if (label) {
      label.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    }
  }

  document.querySelectorAll(".tab-label").forEach(function(label) {
    label.addEventListener("click", function() {
      const forId = this.getAttribute("for").replace("tab-", "");
      currentIdx = tabIds.indexOf(forId);
      if (currentIdx === -1) currentIdx = 0;
      updateIndicator();
    });
  });

  document.addEventListener("keydown", function(e) {
    if (e.key === "ArrowLeft") { switchTab(-1); e.preventDefault(); }
    if (e.key === "ArrowRight") { switchTab(1); e.preventDefault(); }
    if (e.key === "Escape") { closeNewsModal(); }
  });

  updateIndicator();
})();
</script>

<script>
function showNewsDetail(card) {
  const detail = card.getAttribute("data-detail");
  const title = card.getAttribute("data-title");
  const date = card.getAttribute("data-date");
  const source = card.getAttribute("data-source");
  
  const modal = document.getElementById("newsModal");
  const modalTitle = document.getElementById("modalTitle");
  const modalDate = document.getElementById("modalDate");
  const modalSource = document.getElementById("modalSource");
  const modalContent = document.getElementById("modalContent");
  
  modalTitle.textContent = title;
  modalDate.textContent = date;
  modalSource.textContent = source || "";
  modalContent.textContent = detail;
  
  modal.classList.add("active");
  document.body.style.overflow = "hidden";
}

function closeNewsModal() {
  const modal = document.getElementById("newsModal");
  modal.classList.remove("active");
  document.body.style.overflow = "";
}

document.addEventListener("click", function(e) {
  if (e.target.classList.contains("news-modal-overlay")) {
    closeNewsModal();
  }
});
</script>

<div id="newsModal" class="news-modal-overlay">
  <div class="news-modal">
    <button class="news-modal-close" onclick="closeNewsModal()">✕</button>
    <div class="news-modal-header">
      <span class="news-modal-date" id="modalDate"></span>
      <span class="news-modal-source" id="modalSource"></span>
    </div>
    <h2 class="news-modal-title" id="modalTitle"></h2>
    <div class="news-modal-body" id="modalContent"></div>
  </div>
</div>
'''

    return html
def generate_raw_html(news_items, date_str):
    """Generate simple HTML grid from raw RSS entries (fallback when AI fails)"""
    if not news_items:
        return "<p>暂无新闻数据。</p>"

    html = f'<div class="news-summary-line" style="margin-top: 0;">🕐 {date_str} · 共 {len(news_items)} 条新闻 · 鼠标悬停查看详情 · 点击跳转原文</div>\n\n'
    html += '<div class="news-grid">\n'

    # Group by source
    from_source = {}
    for item in news_items:
        src = item["source"]
        if src not in from_source:
            from_source[src] = []
        from_source[src].append(item)

    for src, items in from_source.items():
        html += f'  <div class="news-category">\n'
        html += f'    <div class="news-category-header">\n'
        html += f'      <span class="news-category-icon">📰</span>\n'
        html += f'      <span class="news-category-title">{src}</span>\n'
        html += f'      <span class="news-category-count">{len(items)}</span>\n'
        html += f'    </div>\n'

        for item in items:
            link = item["link"]
            title = item["title"]
            date = item["date"]
            html += f'    <a class="news-item" href="{link}" target="_blank" rel="noopener">\n'
            if date:
                html += f'      <div class="news-item-date">{date}</div>\n'
            html += f'      <div class="news-item-title">{title}</div>\n'
            html += f'      <div class="news-item-source">{item["source"]}</div>\n'
            html += f'      <div class="news-item-link">查看原文 →</div>\n'
            html += f'    </a>\n'

        html += '  </div>\n'

    html += '</div>\n'
    return html


def main():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_only = datetime.now().strftime("%Y-%m-%d")
    log(f"[INFO] 开始抓取新闻 - {date_str}")

    all_news = []
    for feed in RSS_FEEDS:
        log(f"[INFO] 抓取: {feed['name']}...")
        entries = fetch_rss(feed["url"], feed["name"])
        log(f"  获取 {len(entries)} 条")
        all_news.extend(entries)

    seen = set()
    unique = []
    for item in all_news:
        key = item["title"][:60]
        if key not in seen:
            seen.add(key)
            unique.append(item)

    news = unique[:MAX_TOTAL]
    log(f"[INFO] 去重后共 {len(news)} 条")

    summary = None
    if news:
        log(f"[INFO] 调用 AI 总结 API ...")
        summary = summarize_news(news, API_KEY)
        if not summary:
            log(f"[INFO] AI 返回为空，将使用 RSS 原始数据作为降级方案")
            summary = ""

    # Parse AI output into categories
    if summary and summary.strip():
        categories = parse_categories(summary)
        log(f"[INFO] 解析到 {len(categories)} 个分类 (AI 模式)")
        news_html = generate_tabbed_html(categories, date_str)
        mode = "AI"
    else:
        log(f"[INFO] 使用 RSS 原始数据降级方案 ({len(news)} 条)")
        news_html = generate_raw_html(news, date_str)
        mode = "RSS"
        categories = []  # mark as non-empty so news.md gets written

    # Generate today's news page (news.md)
    if categories or news:
        page = f"""---
layout: default
title: 热点新闻
---

# 📰 热点新闻速览

> {"AI 精选" if mode == "AI" else "RSS 聚合"} · 来源可溯 · 每日更新

{news_html}

---

<p class="news-updated">🕐 更新于 {date_only}</p>
"""

        with open("news.md", "w", encoding="utf-8") as f:
            f.write(page)
        log(f"[INFO] 已生成 news.md ({len(page)} 字符, {mode} 模式)")

        # Generate daily archive page
        os.makedirs("archive", exist_ok=True)
        archive_file = f"archive/news-{date_only}.md"
        archive_page = f"""---
layout: default
title: 新闻存档 - {date_only}
---

# 📰 新闻存档 - {date_only}

> [{date_only} 的新闻回顾]({{ site.url }}/news)

---

{news_html}

---

<p class="news-updated">🕐 发布于 {date_str}</p>
"""
        with open(archive_file, "w", encoding="utf-8") as f:
            f.write(archive_page)
        log(f"[INFO] 已生成存档 {archive_file}")
    else:
        log(f"[WARN] 无任何数据，保留现有 news.md，不覆盖")

    # Clean up archives older than 5 days
    from datetime import timedelta
    archive_dir = "archive"
    if os.path.exists(archive_dir):
        for fname in os.listdir(archive_dir):
            if fname.startswith("news-") and fname.endswith(".md"):
                try:
                    fdate = fname.replace("news-", "").replace(".md", "")
                    fdatetime = datetime.strptime(fdate, "%Y-%m-%d")
                    if datetime.now() - fdatetime > timedelta(days=5):
                        os.remove(os.path.join(archive_dir, fname))
                        log(f"[INFO] 清理旧存档: {fname}")
                except ValueError:
                    pass

    # Generate archive index page
    archive_files = []
    if os.path.exists(archive_dir):
        for fname in sorted(os.listdir(archive_dir), reverse=True):
            if fname.startswith("news-") and fname.endswith(".md"):
                fdate = fname.replace("news-", "").replace(".md", "")
                archive_files.append(fdate)

    archive_index = f"""---
layout: default
title: 新闻存档
---

# 📁 新闻存档

> 过去5天的新闻记录

"""
    for fdate in archive_files[:5]:
        archive_index += f"- 📅 [{fdate}]({{ site.url }}/archive/news-{fdate})\n"
    
    if not archive_files:
        archive_index += "<p>暂无存档。</p>\n"

    with open("archive/index.md", "w", encoding="utf-8") as f:
        f.write(archive_index)
    log(f"[INFO] 已生成 archive/index.md")


if __name__ == "__main__":
    main()
