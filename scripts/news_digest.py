#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日新闻抓取与智能分类摘要生成脚本
- 聚合各大权威 RSS 源（英超与五大联赛、科技AI、宏观财经、时政国际）
- 智能分类归纳为 4 大平衡核心板块
- 生成现代化带分类频道 Tab、往期时间线速查与悬浮大容量简述的 news.md
- 自动维护 30 天历史档案
"""

import os
import re
import sys
import requests
import feedparser
from datetime import datetime, timedelta

try:
    import zhconv
    def to_simplified(text):
        if not text:
            return ""
        return zhconv.convert(text, 'zh-cn')
except ImportError:
    def to_simplified(text):
        return text

UA = "Mozilla/5.0 (compatible; NewsDigest/1.0; +https://loneforme.github.io)"

RSS_FEEDS = [
    # ⚽ 足球与英超权威专栏
    {"url": "https://feeds.bbci.co.uk/sport/football/premier-league/rss.xml", "name": "BBC 英超专栏"},
    {"url": "https://www.skysports.com/rss/12040", "name": "天空体育(转会中心)"},
    {"url": "https://www.skysports.com/rss/11661", "name": "天空体育(英超)"},
    {"url": "https://www.theguardian.com/football/premierleague/rss", "name": "卫报(英超深度)"},
    # 🇨🇳 国内官方权威媒体
    {"url": "http://www.people.com.cn/rss/politics.xml", "name": "人民网(时政)"},
    {"url": "http://www.people.com.cn/rss/world.xml", "name": "人民网(国际)"},
    {"url": "http://www.people.com.cn/rss/scitech.xml", "name": "人民网(科技)"},
    {"url": "https://www.chinanews.com.cn/rss/scroll-news.xml", "name": "中国新闻网(滚动)"},
    # 🌐 国际权威媒体
    {"url": "https://www.bbc.co.uk/zhongwen/simp/index.xml", "name": "BBC 中文"},
    {"url": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "name": "纽约时报"},
]

API_URL = "https://opencode.ai/zen/go/v1/chat/completions"
API_KEY = os.environ.get("OPENCODE_GO_API_KEY")
MODEL = "deepseek-v4-flash"
MAX_ARTICLES_PER_FEED = 8
MAX_TOTAL_PER_SECTION = 6
MAX_AGE_DAYS = 30

SOURCE_NAME_MAP = {
    "people.com.cn": "人民网",
    "xinhuanet.com": "新华网",
    "chinanews.com.cn": "中国新闻网",
    "skysports.com": "天空体育",
    "theguardian.com": "卫报",
    "bbc.com": "BBC",
    "bbc.co.uk": "BBC",
    "nytimes.com": "纽约时报",
    "cbsnews.com": "CBS News",
    "npr.org": "NPR",
}

# ===== 来源 → 国旗/样式映射 =====
SOURCE_FLAG_MAP = {
    "人民网": "🇨🇳", "新华网": "🇨🇳", "中国新闻网": "🇨🇳", "央视网": "🇨🇳",
    "BBC": "🇬🇧", "BBC 英超专栏": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "天空体育": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "天空体育(转会中心)": "🔄", "天空体育(英超)": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "卫报": "🇬🇧", "卫报(英超深度)": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "纽约时报": "🇺🇸", "CBS News": "🇺🇸", "NPR": "🇺🇸",
}

SOURCE_CSS_MAP = {
    "人民网": "source-cn", "新华网": "source-cn", "中国新闻网": "source-cn",
    "BBC": "source-bbc", "BBC 英超专栏": "source-bbc",
    "天空体育": "source-skysports", "天空体育(转会中心)": "source-skysports", "天空体育(英超)": "source-skysports",
    "卫报": "source-theathletic", "卫报(英超深度)": "source-theathletic",
    "纽约时报": "source-nytimes",
    "CBS News": "source-cbs",
}

# ===== 3 大核心综合板块定义 (财经已独立到 finance.md) =====
SECTIONS_CONFIG = [
    {
        "id": "zuqiu",
        "title": "英超与足球风云 (赛况战术 · 转会焦点)",
        "tab_name": "⚽ 英超与足球风云",
        "flag": "⚽",
        "tag_class": "cat-zuqiu",
        "tag_label": "⚽ 足球专栏",
    },
    {
        "id": "keji",
        "title": "科技创新 & AI 算力",
        "tab_name": "🤖 科技 & AI",
        "flag": "🤖",
        "tag_class": "cat-keji",
        "tag_label": "🤖 科技前沿",
    },
    {
        "id": "shizheng",
        "title": "时政要闻 & 国际动态",
        "tab_name": "🏛️ 时政与国际",
        "flag": "🏛️",
        "tag_class": "cat-shizheng",
        "tag_label": "🏛️ 时政要闻",
    },
]


def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {msg}", flush=True)


def source_to_flag(source):
    return SOURCE_FLAG_MAP.get(source, "🌐")


def source_to_css(source):
    return SOURCE_CSS_MAP.get(source, "")


def normalize_source(raw_source, title="", link=""):
    for domain, clean_name in SOURCE_NAME_MAP.items():
        if domain in link or domain in raw_source:
            return clean_name
    for kw, clean_name in [("人民网", "人民网"), ("新华", "新华网"), ("中新", "中国新闻网"),
                            ("BBC", "BBC"), ("纽约时报", "纽约时报"), ("CBS", "CBS News"),
                            ("天空体育", "天空体育"), ("卫报", "卫报")]:
        if kw in raw_source or kw in title:
            return clean_name
    return raw_source[:15] if raw_source else "综合"


def normalize_date(raw_date):
    if not raw_date:
        return datetime.now().strftime("%Y-%m-%d")
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(raw_date.strip(), fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    m = re.search(r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', raw_date)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.now().strftime("%Y-%m-%d")


def clean_title(title):
    s = re.sub(r'<[^>]+>', '', title).strip()
    s = re.sub(r'\s*[-–—]\s*(人民网|新华网|中国新闻网|BBC|纽约时报|CBS News|天空体育|卫报).*$', '', s)
    return s


def is_recent(date_str):
    if not date_str:
        return True
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return datetime.now() - dt <= timedelta(days=MAX_AGE_DAYS)
    except ValueError:
        return True


def parse_publisher(title):
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
                title, publisher = parse_publisher(title)
                title = to_simplified(clean_title(title))
                src = normalize_source(publisher if publisher else source_name, title, link)
                date = normalize_date(published)
                raw_sum = entry.get("summary", entry.get("description", ""))
                clean_sum = re.sub(r'<[^>]+>', '', raw_sum).strip()
                clean_sum = re.sub(r'\s+', ' ', clean_sum)
                clean_sum = to_simplified(clean_sum)
                if is_recent(date):
                    entries.append({
                        "title": title,
                        "link": link,
                        "date": date,
                        "source": src,
                        "summary": clean_sum[:350]
                    })
                else:
                    log(f"  [SKIP] 过旧文章 ({date}): {title[:40]}")
        return entries
    except Exception as e:
        log(f"  [ERROR] 抓取失败: {e}")
        return []


def classify_item(item):
    """智能归类到四大核心板块之一"""
    text = (item.get("title", "") + " " + item.get("summary", "") + " " + item.get("source", "")).lower()

    # 1. 足球 / 英超 / 转会
    football_keywords = [
        "英超", "转会", "足球", "bbc 英超", "天空体育", "卫报", "阿森纳", "曼城", "利物浦", "曼联",
        "切尔西", "热刺", "皇马", "巴萨", "拜仁", "尤文", "国米", "米兰", "巴黎", "多特", "西甲",
        "意甲", "德甲", "法甲", "欧冠", "欧联", "世界杯", "亚冠", "中超", "战报", "赛况", "战术",
        "arsenal", "man city", "manchester", "liverpool", "chelsea", "tottenham", "spurs",
        "konsa", "villa", "reijnders", "rashford", "jones", "cherif", "garlick", "root",
        "cricket", "football", "premier league", "transfer", "signing", "striker", "midfielder",
        "defender", "goalkeeper", "manager", "fifa", "uefa"
    ]
    for kw in football_keywords:
        if kw in text:
            return "zuqiu"

    # 2. 科技 & AI
    tech_keywords = [
        "科技", "scitech", "ai", "人工智能", "大模型", "算力", "芯片", "半导体", "机器人", "具身智能",
        "算法", "网络安全", "方班", "攻防", "开源", "航天", "航空", "无人机", "卫星", "科普", "生物",
        "医药", "meta", "openai", "google", "apple", "microsoft", "nvidia", "intel", "amd",
        "deepseek", "chatgpt", "claude", "algorithm", "tech", "quantum"
    ]
    for kw in tech_keywords:
        if kw in text:
            return "keji"

    # 3. 财经 & 宏观
    finance_keywords = [
        "财经", "经济", "人民币", "中间价", "汇率", "外汇", "股市", "a股", "美股", "港股", "个股",
        "大盘", "指数", "低开", "高开", "涨停", "跌停", "关税", "贸易", "美加", "供应链", "航运",
        "核电", "能源", "光伏", "储能", "央行", "加息", "降息", "美联储", "通胀", "cpi", "gdp",
        "资产", "证券", "债券", "金融", "投资", "税收", "tariff", "trade", "inflation", "market",
        "economy", "financial", "stock"
    ]
    for kw in finance_keywords:
        if kw in text:
            return "caijing"

    # 4. 默认归入时政
    return "shizheng"


def _esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&#39;"))


def _date_short(date_str):
    return date_str[-5:] if len(date_str) >= 5 else date_str


def build_archive_chips(date_only):
    """扫描 archive/ 目录生成往期历史速查条"""
    archive_dir = "archive"
    archive_files = []
    if os.path.exists(archive_dir):
        for fname in sorted(os.listdir(archive_dir), reverse=True):
            if fname.startswith("news-") and fname.endswith(".md"):
                fdate = fname.replace("news-", "").replace(".md", "")
                archive_files.append(fdate)

    chips_html = '<div class="archive-chips-bar">\n'
    chips_html += '  <span class="archive-chips-title">\n'
    chips_html += '    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>\n'
    chips_html += '    往期速查:\n'
    chips_html += '  </span>\n'
    chips_html += f'  <a href="{{{{ "/news" | relative_url }}}}" class="archive-chip active">⚡ 今日 ({_date_short(date_only)})</a>\n'

    # 列出以往4天
    added = 0
    for fdate in archive_files:
        if fdate != date_only and added < 4:
            chips_html += f'  <a href="{{{{ "/archive/news-{fdate}" | relative_url }}}}" class="archive-chip">📅 {_date_short(fdate)}</a>\n'
            added += 1

    chips_html += '  <a href="{{ "/archive" | relative_url }}" class="archive-chip archive-chip-more">📁 历史档案室 →</a>\n'
    chips_html += '</div>\n'
    return chips_html


def build_page_html(categorized_map, date_only):
    """生成完整的美观新闻页面 HTML"""
    total_count = sum(len(items) for sec in SECTIONS_CONFIG for items in [categorized_map.get(sec["id"], [])])

    # 1. 复合 Header 控制台 (标题 + 频道 Tab + 往期历史入口)
    header_html = f'''<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">📰 热点新闻速览</h1>
      <p class="news-main-desc">每日聚合全球英超足球、前沿科技与国际时政焦点（电脑端悬浮即览深度特稿 · 手机端自适应浏览）</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>{date_only} 今日更新</span>
    </div>
  </div>

  <div class="news-nav-composite">
    <div class="news-channel-bar">
      <button class="channel-btn active" onclick="filterNewsChannel('all', this)">
        <span>🌟 全部动态</span>
        <span class="channel-count">{total_count}</span>
      </button>
'''
    for sec in SECTIONS_CONFIG:
        sec_id = sec["id"]
        sec_count = len(categorized_map.get(sec_id, []))
        header_html += f'''      <button class="channel-btn" onclick="filterNewsChannel('{sec_id}', this)">
        <span>{sec["tab_name"]}</span>
        <span class="channel-count">{sec_count}</span>
      </button>\n'''

    header_html += '''      <button class="channel-btn" onclick="filterNewsChannel('source', this)">
        <span>🌐 媒体信源</span>
      </button>
    </div>

    <a href="{{ "/archive" | relative_url }}" class="archive-btn-compact" title="翻阅往期历史档案">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>往期归档</span>
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </a>
  </div>
</div>
'''

    # 2. 头条焦点区
    all_sorted = []
    for sec in SECTIONS_CONFIG:
        all_sorted.extend(categorized_map.get(sec["id"], []))

    hero_html = ""
    if all_sorted:
        featured = all_sorted[0]
        sub_items = all_sorted[1:4]

        featured_sum = _esc(featured.get("summary") or featured["title"])
        featured_title = _esc(featured["title"])
        featured_date = _date_short(featured["date"])
        featured_cat = featured.get("cat_id", "zuqiu")
        featured_tag_label = "⚽ 足球专栏" if featured_cat == "zuqiu" else "🔥 焦点头条"

        hero_html += '<div class="news-hero">\n'
        hero_html += '  <div class="news-hero-badge">🔥 今日头条焦点</div>\n'
        hero_html += f'  <a class="hero-featured-card" href="{featured["link"]}" target="_blank" rel="noopener" data-cat="{featured_cat}" data-summary="{featured_sum}" data-title="{featured_title}" data-date="{featured_date}" data-source="{featured["source"]}">\n'
        hero_html += f'    <div class="hero-featured-body">\n'
        hero_html += f'      <div class="hero-featured-meta">\n'
        hero_html += f'        <span class="news-cat-tag cat-{featured_cat}">{featured_tag_label}</span>\n'
        hero_html += f'        <span class="source-badge {source_to_css(featured["source"])}">{source_to_flag(featured["source"])} {featured["source"]}</span>\n'
        hero_html += f'        <span class="hero-featured-date">{featured_date}</span>\n'
        hero_html += f'      </div>\n'
        hero_html += f'      <h2 class="hero-featured-title">{featured["title"]}</h2>\n'
        hero_html += f'    </div>\n'
        hero_html += f'    <span class="hero-featured-arrow">→</span>\n'
        hero_html += f'  </a>\n'

        if sub_items:
            hero_html += '  <div class="hero-sub-grid">\n'
            for s_item in sub_items:
                s_sum = _esc(s_item.get("summary") or s_item["title"])
                s_title = _esc(s_item["title"])
                s_date = _date_short(s_item["date"])
                s_cat = s_item.get("cat_id", "keji")
                hero_html += f'    <a class="hero-sub-card" href="{s_item["link"]}" target="_blank" rel="noopener" data-cat="{s_cat}" data-summary="{s_sum}" data-title="{s_title}" data-date="{s_date}" data-source="{s_item["source"]}">\n'
                hero_html += f'      <div class="hero-sub-meta">\n'
                hero_html += f'        <span class="news-cat-tag cat-{s_cat}">🔥 焦点</span>\n'
                hero_html += f'        <span class="source-badge {source_to_css(s_item["source"])}">{source_to_flag(s_item["source"])} {s_item["source"]}</span>\n'
                hero_html += f'      </div>\n'
                hero_html += f'      <p class="hero-sub-title">{s_item["title"]}</p>\n'
                hero_html += f'    </a>\n'
            hero_html += '  </div>\n'
        hero_html += '</div>\n'

    # 3. 三大核心板块结构化展示
    grid_html = '<div class="news-grid">\n'
    for sec in SECTIONS_CONFIG:
        sec_id = sec["id"]
        items = categorized_map.get(sec_id, [])
        if not items:
            continue
        grid_html += f'  <div class="news-category">\n'
        grid_html += f'    <div class="news-category-header">\n'
        grid_html += f'      <span class="category-flag">{sec["flag"]}</span>\n'
        grid_html += f'      <span class="news-category-title">{sec["title"]}</span>\n'
        grid_html += f'      <span class="news-category-count">{len(items)} 条</span>\n'
        grid_html += f'    </div>\n'

        for it in items:
            it_sum = _esc(it.get("summary") or it["title"])
            it_title = _esc(it["title"])
            it_date = _date_short(it["date"])
            src_css = source_to_css(it["source"])
            flag = source_to_flag(it["source"])

            grid_html += f'        <a class="news-item" href="{it["link"]}" target="_blank" rel="noopener" data-cat="{sec_id}" data-summary="{it_sum}" data-title="{it_title}" data-date="{it_date}" data-source="{it["source"]}">\n'
            grid_html += f'          <span class="news-cat-tag {sec["tag_class"]}">{sec["tag_label"]}</span>\n'
            grid_html += f'          <span class="source-badge {src_css}">{flag} {it["source"]}</span>\n'
            grid_html += f'          <span class="news-item-date">{it_date}</span>\n'
            grid_html += f'          <span class="news-item-title">{it["title"]}</span>\n'
            grid_html += f'        </a>\n'
        grid_html += f'  </div>\n'
    grid_html += '</div>\n'

    return header_html + hero_html + grid_html


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

    log(f"[INFO] 去重后共 {len(unique)} 条")

    # 智能分类并分配板块
    categorized_map = {"zuqiu": [], "keji": [], "caijing": [], "shizheng": []}
    for it in unique:
        cat_id = classify_item(it)
        it["cat_id"] = cat_id
        if len(categorized_map[cat_id]) < MAX_TOTAL_PER_SECTION:
            categorized_map[cat_id].append(it)

    # 打印各分类数量
    for cat_id, items in categorized_map.items():
        log(f"  [分类统计] {cat_id}: {len(items)} 条")

    content_html = build_page_html(categorized_map, date_only)

    page = f"""---
layout: default
title: 热点新闻
---

{content_html}

---

<p class="news-updated">🕐 更新于 {date_only}</p>
"""

    with open("news.md", "w", encoding="utf-8") as f:
        f.write(page)
    log(f"[INFO] 已生成 news.md")

    # 生成每日存档
    os.makedirs("archive", exist_ok=True)
    archive_file = f"archive/news-{date_only}.md"
    archive_page = f"""---
layout: default
title: 新闻存档 - {date_only}
---

<h1>📰 新闻存档 - {date_only}</h1>
<p class="page-subtitle">每日自动聚合 · 来源可溯 · <a href="{{{{ site.url }}}}/news" class="archive-back-link">← 返回最新新闻</a></p>

{content_html}

---

<p class="news-updated">🕐 发布于 {date_str}</p>
"""
    with open(archive_file, "w", encoding="utf-8") as f:
        f.write(archive_page)
    log(f"[INFO] 已生成存档 {archive_file}")

    # 清理旧存档（保留最近30天）
    archive_dir = "archive"
    if os.path.exists(archive_dir):
        for fname in os.listdir(archive_dir):
            if fname.startswith("news-") and fname.endswith(".md"):
                try:
                    fdate = fname.replace("news-", "").replace(".md", "")
                    fdatetime = datetime.strptime(fdate, "%Y-%m-%d")
                    if datetime.now() - fdatetime > timedelta(days=30):
                        os.remove(os.path.join(archive_dir, fname))
                        log(f"[INFO] 清理旧存档: {fname}")
                except ValueError:
                    pass

    # 生成存档索引
    archive_files = []
    if os.path.exists(archive_dir):
        for fname in sorted(os.listdir(archive_dir), reverse=True):
            if fname.startswith("news-") and fname.endswith(".md"):
                fdate = fname.replace("news-", "").replace(".md", "")
                archive_files.append(fdate)

    cards_html = ""
    for fdate in archive_files:
        is_today = " (今日)" if fdate == datetime.now().strftime("%Y-%m-%d") else ""
        cards_html += f"""  <a href="{{{{ site.url }}}}/archive/news-{fdate}" class="archive-day-card">
    <div class="archive-day-header">
      <span class="archive-day-date">📅 {fdate}{is_today}</span>
      <span class="archive-day-count">每日热点速览</span>
    </div>
    <p class="archive-day-headline">点击进入查看该日聚合的国内外权威要闻、深度事件简述与信源回顾。</p>
    <div class="archive-day-footer">
      <span>9 个国内外权威信源</span>
      <span>进入阅读 →</span>
    </div>
  </a>\n"""

    archive_index = f"""---
layout: default
title: 新闻历史档案室
---

<h1>📁 新闻历史档案室</h1>
<p class="page-subtitle">每日热点自动归档 · 往期资讯回溯 · <a href="{{{{ site.url }}}}/news" class="archive-back-link">← 返回今日最新新闻</a></p>

<div class="archive-timeline-grid">
{cards_html}</div>

<div style="text-align: center; margin: 40px 0 20px;">
  <a href="{{{{ site.url }}}}/news" class="card-link" style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 24px; font-size: 14px;">
    <span>⚡ 返回今日最新新闻</span>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
  </a>
</div>
"""
    with open("archive/index.md", "w", encoding="utf-8") as f:
        f.write(archive_index)
    log(f"[INFO] 已生成 archive/index.md")


if __name__ == "__main__":
    main()