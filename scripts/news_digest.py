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
        return None

    lines = []
    for item in news_items:
        lines.append(f"[{item['date'] or '?'}] [{item['source']}] {item['title']}")
    news_text = "\n".join(lines)

    system_prompt = """你是资深新闻编辑。任务：整理以下新闻。

步骤1：审查内容 — 优先采用权威媒体（新华社、人民日报、央视、BBC、纽约时报等），剔除明显不实信息。
步骤2：按主题分类（时政、科技AI、国际、社会、财经、体育、军事、其他），每类精选最多5条。
步骤3：输出以下格式，每篇末尾标注来源。

格式：
### 分类名
- **日期** | **标题** | 内容摘要 [来源: XXX]

要求：
- 分类名请从（时政、科技AI、国际、社会、财经、体育、军事、其他）中选
- 每类≤5条
- 日期 YYYY-MM-DD
- 摘要40-60字，概括核心内容
- 末尾 [来源: XXX] 标明出处
- 不要链接，不要推理过程"""

    try:
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
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return content if content.strip() else None
    except Exception as e:
        log(f"[ERROR] API 调用失败: {e}")
        if "resp" in dir():
            log(f"  Status: {resp.status_code}")
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
        summary = m.group(3).strip()
        source = m.group(4).strip() if m.group(4) else ""
        
        html = f'              <div class="news-card">\n'
        html += f'                <span class="news-date-badge">{date}</span>\n'
        html += f'                <div class="news-card-title">{title}</div>\n'
        html += f'                <div class="news-card-summary">{summary}</div>\n'
        if source:
            html += f'                <span class="news-card-source">{source}</span>\n'
        html += f'              </div>\n'
        return html
    
    # Fallback: treat as plain text
    clean = re.sub(r'^\-\s+', '', line)
    return f'              <div class="news-card"><div class="news-card-summary">{clean}</div></div>\n'


def generate_tabbed_html(categories, date_str):
    """Generate the full tabbed news HTML"""
    
    # Build tab IDs
    tabs = []
    for cat_name, items in categories:
        tab_id = cat_name_to_id(cat_name)
        short_name = cat_name_short(cat_name)
        tabs.append((tab_id, short_name, cat_name, items))
    
    if not tabs:
        return "<p>暂无新闻数据。</p>"
    
    # Count total items
    total_count = sum(len(items) for _, _, _, items in tabs)
    
    html = '<div class="news-tabs">\n'
    
    # Tab bar (sticky)
    html += '  <div class="tab-bar">\n'
    
    # "全部" tab (default selected)
    html += f'    <input type="radio" name="news-tab" id="tab-all" checked>\n'
    html += f'    <label for="tab-all" class="tab-label">📋 全部 <span class="tab-count">{total_count}</span></label>\n'
    
    # Category tabs
    icon_map = {
        "shizheng": "🏛️", "keji": "💻", "guoji": "🌍", "shehui": "👥",
        "caijing": "💰", "tiyu": "⚽", "junshi": "⚔️", "qita": "📎"
    }
    for tab_id, short_name, _, items in tabs:
        icon = icon_map.get(tab_id, "📋")
        html += f'    <input type="radio" name="news-tab" id="tab-{tab_id}">\n'
        html += f'    <label for="tab-{tab_id}" class="tab-label">{icon} {short_name} <span class="tab-count">{len(items)}</span></label>\n'
    
    html += '  </div>\n\n'
    
    # Summary line
    html += f'  <div class="news-summary-line">🕐 上次更新: {date_str} · 共 {total_count} 条新闻 · 点击上方标签切换分类</div>\n\n'
    
    # "全部" panel
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
            html += f'    <div class="news-card"><div class="news-card-summary">暂无 {short_name} 类新闻。</div></div>\n'
        html += '  </div>\n\n'
    
    html += '</div>\n'
    
    return html


def main():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
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
            log(f"[INFO] API 返回为空")
            summary = ""
    
    # Parse AI output into categories and generate tabbed HTML
    if summary and summary.strip():
        categories = parse_categories(summary)
        log(f"[INFO] 解析到 {len(categories)} 个分类")
        news_html = generate_tabbed_html(categories, date_str)
    else:
        news_html = "<p>暂无新闻数据。</p>\n"
        news_html += f'<div class="news-summary-line">🕐 生成时间: {date_str}</div>\n'

    page = f"""---
layout: default
title: 新闻摘要
---

# 今日热点摘要

{news_html}

---

<div class="news-updated">
  🛜 AI 每日精选 · 来源可溯 · {date_str} 更新
</div>
"""

    with open("news.md", "w", encoding="utf-8") as f:
        f.write(page)
    log(f"[INFO] 已生成 news.md ({len(page)} 字符)")


if __name__ == "__main__":
    main()
