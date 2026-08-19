#!/usr/bin/env python3
"""News Digest - 抓取 RSS 新闻并用 AI 总结，生成带标签页的网站页面"""

import feedparser
import os
import requests
import re
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime

log = lambda msg: print(msg, flush=True)

UA = "Mozilla/5.0 (compatible; NewsDigest/1.0; +https://loneforme.github.io)"

RSS_FEEDS = [
    # ⚽ 足球与英超权威专栏 (五大联赛赛况与转会中心)
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
MAX_ARTICLES_PER_FEED = 6
MAX_TOTAL = 32
MAX_AGE_DAYS = 30

SOURCE_NAME_MAP = {
    "people.com.cn": "人民网",
    "xinhuanet.com": "新华网",
    "chinanews.com.cn": "中国新闻网",
    "chinanews.com": "中国新闻网",
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

CAT_ICON_MAP = {
    "zuqiu": "⚽", "zhuanhui": "🔄", "keji": "🤖", "caijing": "💰",
    "shizheng": "🏛️", "guoji": "🌍", "junshi": "⚔️", "qita": "📎",
}


def source_to_flag(source):
    return SOURCE_FLAG_MAP.get(source, "🌐")


def source_to_css(source):
    return SOURCE_CSS_MAP.get(source, "")


_DAY_NAMES = {"mon": "Mon", "tue": "Tue", "wed": "Wed", "thu": "Thu", "fri": "Fri", "sat": "Sat", "sun": "Sun"}
_MONTH_NAMES = {"jan": "Jan", "feb": "Feb", "mar": "Mar", "apr": "Apr", "may": "May", "jun": "Jun",
                "jul": "Jul", "aug": "Aug", "sep": "Sep", "oct": "Oct", "nov": "Nov", "dec": "Dec"}
_MONTH_PREFIX2 = {"ja": "Jan", "fe": "Feb", "ma": "Mar", "ap": "Apr", "may": "May", "ju": "Jul",
                  "au": "Aug", "se": "Sep", "oc": "Oct", "no": "Nov", "de": "Dec"}

def _try_fix_date(date_str):
    """Fix common truncated date issues from RSS feeds"""
    s = date_str.strip()
    m = re.match(r'^(\w+),\s*(\d{1,2})\s+(\w{2,})$', s)
    if m:
        dow = m.group(1)
        day = m.group(2).zfill(2)
        mon_raw = m.group(3).lower()[:3]
        if len(mon_raw) == 3 and mon_raw in _MONTH_NAMES:
            s = f"{dow}, {day} {_MONTH_NAMES[mon_raw]} {datetime.now().year}"
        elif len(mon_raw) >= 2 and mon_raw[:2] in _MONTH_PREFIX2:
            s = f"{dow}, {day} {_MONTH_PREFIX2[mon_raw[:2]]} {datetime.now().year}"
    return s

def normalize_date(date_str):
    """Parse various RSS date formats into YYYY-MM-DD string."""
    if not date_str:
        return ""
    date_str = _try_fix_date(date_str.strip())
    if re.match(r'^\d{4}-\d{2}-\d{2}', date_str):
        return date_str[:10]
    if re.match(r'^\d{4}-\d{2}-\d{2}T', date_str):
        return date_str[:10]
    try:
        dt = parsedate_to_datetime(date_str)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    m = re.match(r'^\w+,\s*(\d{1,2})\s+(\w+)\s+(\d{4})$', date_str)
    if m:
        day, mon, year = m.group(1).zfill(2), m.group(2)[:3].title(), m.group(3)
        mon_num = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
        if mon in mon_num:
            return f"{year}-{mon_num[mon]:02d}-{day}"
    log(f"  [WARN] 无法解析日期: {date_str[:40]}")
    return date_str[:10]


def clean_title(title):
    """Remove trailing source suffixes like ' - domain.com' or ' | Some Site'"""
    m = re.search(r'\s*[-–—|]\s*[a-zA-Z0-9][-a-zA-Z0-9.]*\.[a-zA-Z]{2,}\s*$', title)
    if m:
        title = title[:m.start()].strip()
    m = re.search(r'\s*\([^)]*\)\s*$', title)
    if m and len(m.group()) < 30:
        title = title[:m.start()].strip()
    return title


def normalize_source(source_raw, title="", link=""):
    """Clean up source name"""
    s = source_raw.strip()
    if not s:
        return s
    parts = s.lower().split(".")
    if len(parts) >= 2:
        for i in range(len(parts)):
            candidate = ".".join(parts[i:])
            if candidate in SOURCE_NAME_MAP:
                return SOURCE_NAME_MAP[candidate]
    return s


def is_recent(date_str):
    """Check if article date is within MAX_AGE_DAYS. If parse fails, keep it."""
    if not date_str:
        return True
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return datetime.now() - dt <= timedelta(days=MAX_AGE_DAYS)
    except ValueError:
        return True


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
                title, publisher = parse_publisher(title)
                title = clean_title(title)
                src = normalize_source(publisher if publisher else source_name, title, link)
                date = normalize_date(published)
                raw_sum = entry.get("summary", entry.get("description", ""))
                clean_sum = re.sub(r'<[^>]+>', '', raw_sum).strip()
                clean_sum = re.sub(r'\s+', ' ', clean_sum)
                if is_recent(date):
                    entries.append({
                        "title": title,
                        "link": link,
                        "date": date,
                        "source": src,
                        "summary": clean_sum[:300]
                    })
                else:
                    log(f"  [SKIP] 过旧文章 ({date}): {title[:40]}")
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
        "足球赛况": "zuqiu", "足球": "zuqiu", "英超": "zuqiu", "五大联赛": "zuqiu", "英超赛况": "zuqiu",
        "转会风云": "zhuanhui", "转会": "zhuanhui", "英超转会": "zhuanhui", "五大联赛转会": "zhuanhui",
        "科技AI": "keji", "科技": "keji",
        "财经": "caijing", "经济": "caijing",
        "时政": "shizheng", "国际": "guoji", "其他": "qita",
    }
    return mapping.get(name.strip(), "qita")


def cat_name_short(name):
    """Short display name for tab button"""
    mapping = {
        "足球赛况": "足球", "英超": "足球", "五大联赛": "足球",
        "转会风云": "转会", "英超转会": "转会",
        "科技AI": "科技", "科技": "科技",
        "财经": "财经",
        "时政": "时政", "国际": "国际", "其他": "其他",
    }
    return mapping.get(name.strip(), name.strip())


# =====================================================================
#  以下为渲染函数 — 适配新版 UI（头条焦点 + 彩色标签 + 来源徽章 + 国旗）
# =====================================================================

def _esc(text):
    """Escape HTML special characters"""
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&#39;"))


def _date_short(date_str):
    """YYYY-MM-DD → MM-DD"""
    return date_str[-5:] if len(date_str) >= 5 else date_str


def parse_ai_item(line):
    """解析 AI 输出的一行，返回 {date, title, summary, source}"""
    m = re.match(r'-\s+\*\*([^*]+)\*\*\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*(.+?)(?:\s*\[来源:\s*([^\]]+)\])?\s*$', line)
    if m:
        return {
            "date": m.group(1).strip(),
            "title": m.group(2).strip(),
            "summary": m.group(3).strip(),
            "source": m.group(4).strip() if m.group(4) else "",
        }
    clean = re.sub(r'^\-\s+', '', line)
    return {"date": "", "title": clean, "summary": clean, "source": ""}


def build_hero_ai(categories):
    """从 AI 分类数据构建头条焦点区 HTML"""
    # 收集所有条目，取前4条作为头条
    all_items_parsed = []
    for cat_name, items in categories:
        cat_id = cat_name_to_id(cat_name)
        cat_short = cat_name_short(cat_name)
        for item_line in items:
            parsed = parse_ai_item(item_line)
            all_items_parsed.append({**parsed, "cat_id": cat_id, "cat_name": cat_short})

    if not all_items_parsed:
        return ""

    featured = all_items_parsed[0]
    sub_items = all_items_parsed[1:4]

    html = '<div class="news-hero">\n'
    html += '  <div class="news-hero-badge">🔥 头条焦点</div>\n'

    # 主头条（无链接，用 modal）
    detail_esc = _esc(featured["summary"])
    title_esc = _esc(featured["title"])
    html += f'  <div class="hero-featured-card" onclick="showNewsDetail(this)" data-detail="{detail_esc}" data-title="{title_esc}" data-date="{featured["date"]}" data-source="{featured["source"]}">\n'
    html += f'    <div class="hero-featured-img" style="background: linear-gradient(135deg, #1a0a2e 0%, #2d1b4e 30%, #0a1628 100%);">\n'
    html += f'      <span class="hero-featured-emoji">{source_to_flag(featured["source"])}</span>\n'
    html += f'    </div>\n'
    html += f'    <div class="hero-featured-body">\n'
    html += f'      <div class="hero-featured-meta">\n'
    html += f'        <span class="news-cat-tag cat-{featured["cat_id"]}">{featured["cat_name"]}</span>\n'
    css_cls = source_to_css(featured["source"])
    html += f'        <span class="source-badge {css_cls}">{source_to_flag(featured["source"])} {featured["source"]}</span>\n'
    html += f'        <span class="hero-featured-date">{_date_short(featured["date"])}</span>\n'
    html += f'      </div>\n'
    html += f'      <h2 class="hero-featured-title">{featured["title"]}</h2>\n'
    summary_short = featured["summary"][:200]
    if len(featured["summary"]) > 200:
        summary_short += "..."
    html += f'      <p class="hero-featured-summary">{summary_short}</p>\n'
    html += f'    </div>\n'
    html += f'    <span class="hero-featured-arrow">→</span>\n'
    html += f'  </div>\n'

    # 副头条
    if sub_items:
        html += '  <div class="hero-sub-grid">\n'
        for item in sub_items:
            detail_esc2 = _esc(item["summary"])
            title_esc2 = _esc(item["title"])
            css_cls2 = source_to_css(item["source"])
            html += f'    <div class="hero-sub-card" onclick="showNewsDetail(this)" data-detail="{detail_esc2}" data-title="{title_esc2}" data-date="{item["date"]}" data-source="{item["source"]}">\n'
            html += f'      <div class="hero-sub-meta">\n'
            html += f'        <span class="news-cat-tag cat-{item["cat_id"]}">{item["cat_name"]}</span>\n'
            html += f'        <span class="source-badge {css_cls2}">{source_to_flag(item["source"])} {item["source"]}</span>\n'
            html += f'      </div>\n'
            html += f'      <p class="hero-sub-title">{item["title"]}</p>\n'
            html += f'    </div>\n'
        html += '  </div>\n'

    html += '</div>\n'
    return html


def build_hero_rss(news_items):
    """从 RSS 原始数据构建头条焦点区 HTML"""
    if not news_items:
        return ""

    featured = news_items[0]
    sub_items = news_items[1:4]

    html = '<div class="news-hero">\n'
    html += '  <div class="news-hero-badge">🔥 头条焦点</div>\n'

    # 主头条
    summary_esc = _esc(featured.get("summary", "") or featured["title"])
    title_esc = _esc(featured["title"])
    date_short = _date_short(featured["date"])
    css_cls = source_to_css(featured["source"])

    html += f'  <a class="hero-featured-card" href="{featured["link"]}" target="_blank" rel="noopener" data-summary="{summary_esc}" data-title="{title_esc}" data-date="{date_short}" data-source="{featured["source"]}">\n'
    html += f'    <div class="hero-featured-img" style="background: linear-gradient(135deg, #1a0a2e 0%, #2d1b4e 30%, #0a1628 100%);">\n'
    html += f'      <span class="hero-featured-emoji">{source_to_flag(featured["source"])}</span>\n'
    html += f'    </div>\n'
    html += f'    <div class="hero-featured-body">\n'
    html += f'      <div class="hero-featured-meta">\n'
    html += f'        <span class="source-badge {css_cls}">{source_to_flag(featured["source"])} {featured["source"]}</span>\n'
    html += f'        <span class="hero-featured-date">{date_short}</span>\n'
    html += f'      </div>\n'
    html += f'      <h2 class="hero-featured-title">{featured["title"]}</h2>\n'
    html += f'    </div>\n'
    html += f'    <span class="hero-featured-arrow">→</span>\n'
    html += f'  </a>\n'

    # 副头条
    if sub_items:
        html += '  <div class="hero-sub-grid">\n'
        for item in sub_items:
            css_cls2 = source_to_css(item["source"])
            sub_sum_esc = _esc(item.get("summary", "") or item["title"])
            sub_title_esc = _esc(item["title"])
            sub_date_short = _date_short(item["date"])
            html += f'    <a class="hero-sub-card" href="{item["link"]}" target="_blank" rel="noopener" data-summary="{sub_sum_esc}" data-title="{sub_title_esc}" data-date="{sub_date_short}" data-source="{item["source"]}">\n'
            html += f'      <div class="hero-sub-meta">\n'
            html += f'        <span class="source-badge {css_cls2}">{source_to_flag(item["source"])} {item["source"]}</span>\n'
            html += f'      </div>\n'
            html += f'      <p class="hero-sub-title">{item["title"]}</p>\n'
            html += f'    </a>\n'
        html += '  </div>\n'

    html += '</div>\n'
    return html


def render_ai_news_item(parsed, cat_id, cat_name):
    """渲染一条 AI 模式新闻（无链接，点击弹窗）"""
    detail_esc = _esc(parsed["summary"])
    title_esc = _esc(parsed["title"])
    css_cls = source_to_css(parsed["source"])
    flag = source_to_flag(parsed["source"])

    html = f'        <div class="news-item" onclick="showNewsDetail(this)" data-detail="{detail_esc}" data-summary="{detail_esc}" data-title="{title_esc}" data-date="{parsed["date"]}" data-source="{parsed["source"]}">\n'
    html += f'          <span class="news-cat-tag cat-{cat_id}">{cat_name}</span>\n'
    html += f'          <span class="source-badge {css_cls}">{flag} {parsed["source"]}</span>\n'
    html += f'          <span class="news-item-date">{_date_short(parsed["date"])}</span>\n'
    html += f'          <span class="news-item-title">{parsed["title"]}</span>\n'
    # 摘要截取前180字
    summary_show = parsed["summary"][:180]
    if len(parsed["summary"]) > 180:
        summary_show += "..."
    html += f'          <span class="news-item-summary">{summary_show}</span>\n'
    html += f'        </div>\n'
    return html


def render_rss_news_item(item):
    """渲染一条 RSS 模式新闻（有链接，直接跳转，附带悬浮简述）"""
    css_cls = source_to_css(item["source"])
    flag = source_to_flag(item["source"])
    summary_esc = _esc(item.get("summary", "") or item["title"])
    title_esc = _esc(item["title"])
    date_short = _date_short(item["date"])

    html = f'        <a class="news-item" href="{item["link"]}" target="_blank" rel="noopener" data-summary="{summary_esc}" data-title="{title_esc}" data-date="{date_short}" data-source="{item["source"]}">\n'
    html += f'          <span class="source-badge {css_cls}">{flag} {item["source"]}</span>\n'
    html += f'          <span class="news-item-date">{date_short}</span>\n'
    html += f'          <span class="news-item-title">{item["title"]}</span>\n'
    html += f'        </a>\n'
    return html


def generate_source_grouped_panel_ai(categories):
    """AI 模式「全部」面板：按来源分组展示"""
    # 收集所有条目并按来源分组
    from_source = {}
    for cat_name, items in categories:
        cat_id = cat_name_to_id(cat_name)
        cat_short = cat_name_short(cat_name)
        for item_line in items:
            parsed = parse_ai_item(item_line)
            src = parsed["source"] or "综合"
            if src not in from_source:
                from_source[src] = []
            from_source[src].append({**parsed, "cat_id": cat_id, "cat_name": cat_short})

    html = '<div class="news-grid">\n'
    for src, items in from_source.items():
        flag = source_to_flag(src)
        html += f'      <div class="news-category">\n'
        html += f'        <div class="news-category-header">\n'
        html += f'          <span class="category-flag">{flag}</span>\n'
        html += f'          <span class="news-category-title">{src}</span>\n'
        html += f'          <span class="news-category-count">{len(items)} 条</span>\n'
        html += f'        </div>\n'
        for item in items:
            html += render_ai_news_item(item, item["cat_id"], item["cat_name"])
        html += f'      </div>\n'
    html += '    </div>\n'
    return html


def generate_tabbed_html(categories, date_str):
    """AI 模式：头条焦点 + 分类 Tab + 彩色标签 + 来源徽章 + 摘要"""

    tabs = []
    for cat_name, items in categories:
        tab_id = cat_name_to_id(cat_name)
        short_name = cat_name_short(cat_name)
        tabs.append((tab_id, short_name, cat_name, items))

    if not tabs:
        return "<p>暂无新闻数据。</p>"

    total_count = sum(len(items) for _, _, _, items in tabs)

    # === 头条焦点区 ===
    hero_html = build_hero_ai(categories)

    # === Tab 容器 ===
    html = '<div class="news-tabs">\n'

    # Radio inputs (必须直接在 .news-tabs 下)
    html += '  <input type="radio" name="news-tab" id="tab-all" checked>\n'
    for tab_id, _, _, _ in tabs:
        html += f'  <input type="radio" name="news-tab" id="tab-{tab_id}">\n'

    # Tab bar
    html += '  <div class="tab-bar" id="newsTabBar">\n'
    html += f'    <label for="tab-all" class="tab-label">📋 全部 <span class="tab-count">{total_count}</span></label>\n'
    for tab_id, short_name, _, items in tabs:
        icon = CAT_ICON_MAP.get(tab_id, "📋")
        html += f'    <label for="tab-{tab_id}" class="tab-label">{icon} {short_name} <span class="tab-count">{len(items)}</span></label>\n'
    html += '  </div>\n\n'

    # 导航按钮 + 摘要行
    html += '  <div class="tab-nav">\n'
    html += '    <button class="tab-nav-btn tab-prev" onclick="switchTab(-1)" title="上一个分类" aria-label="Previous">‹</button>\n'
    html += '    <div class="tab-nav-indicator" id="tabIndicator">全部</div>\n'
    html += '    <button class="tab-nav-btn tab-next" onclick="switchTab(1)" title="下一个分类" aria-label="Next">›</button>\n'
    html += '  </div>\n\n'
    html += f'  <div class="news-summary-line">{date_str} · 共 {total_count} 条新闻 · 点击标签或 ← → 键切换</div>\n\n'

    # 「全部」面板（按来源分组）
    html += '  <div id="panel-all" class="tab-panel">\n'
    html += generate_source_grouped_panel_ai(categories)
    html += '  </div>\n\n'

    # 各分类面板
    for tab_id, short_name, cat_name, items in tabs:
        html += f'  <div id="panel-{tab_id}" class="tab-panel">\n'
        if items:
            html += '    <div class="news-grid">\n'
            html += f'      <div class="news-category">\n'
            icon = CAT_ICON_MAP.get(tab_id, "📋")
            html += f'        <div class="news-category-header">\n'
            html += f'          <span class="category-flag">{icon}</span>\n'
            html += f'          <span class="news-category-title">{short_name}新闻</span>\n'
            html += f'          <span class="news-category-count">{len(items)} 条</span>\n'
            html += f'        </div>\n'
            for item_line in items:
                parsed = parse_ai_item(item_line)
                html += render_ai_news_item(parsed, tab_id, short_name)
            html += f'      </div>\n'
            html += '    </div>\n'
        else:
            html += f'    <p style="color:var(--color-muted);padding:20px;">暂无 {short_name} 类新闻。</p>\n'
        html += '  </div>\n\n'

    html += '</div>\n'

    # Modal + JS
    html += _modal_and_js(tabs)

    return hero_html + html


def generate_raw_html(news_items, date_str):
    """RSS 降级模式：头条焦点 + 按来源分组 + 国旗徽章"""

    if not news_items:
        return "<p>暂无新闻数据。</p>"

    # === 头条焦点区 ===
    hero_html = build_hero_rss(news_items)

    # === 按来源分组 ===
    from_source = {}
    for item in news_items:
        src = item["source"]
        if src not in from_source:
            from_source[src] = []
        from_source[src].append(item)

    html = '<div class="news-grid">\n'
    for src, items in from_source.items():
        flag = source_to_flag(src)
        html += f'  <div class="news-category">\n'
        html += f'    <div class="news-category-header">\n'
        html += f'      <span class="category-flag">{flag}</span>\n'
        html += f'      <span class="news-category-title">{src}</span>\n'
        html += f'      <span class="news-category-count">{len(items)} 条</span>\n'
        html += f'    </div>\n'
        for item in items:
            html += render_rss_news_item(item)
        html += f'  </div>\n'
    html += '</div>\n'

    return hero_html + html


def _modal_and_js(tabs):
    """生成 Modal HTML 和 Tab 切换 JS（AI 模式专用）"""
    tab_ids = ", ".join('"' + t[0] + '"' for t in tabs)
    return '''
<!-- Modal -->
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

<script>
(function() {
  var tabIds = ["all", ''' + tab_ids + '''];
  var currentIdx = 0;

  window.switchTab = function(dir) {
    currentIdx = (currentIdx + dir + tabIds.length) % tabIds.length;
    var id = tabIds[currentIdx];
    var radio = document.getElementById("tab-" + id);
    if (radio) { radio.checked = true; }
    updateIndicator();
    scrollTabIntoView(id);
  };

  function updateIndicator() {
    var id = tabIds[currentIdx];
    var indicator = document.getElementById("tabIndicator");
    var label = document.querySelector("label[for='tab-" + id + "']");
    if (label && indicator) {
      var text = label.textContent.trim().replace(/\\s*\\d+\\s*$/, "").trim();
      indicator.textContent = text;
    }
  }

  function scrollTabIntoView(id) {
    var label = document.querySelector("label[for='tab-" + id + "']");
    if (label) { label.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" }); }
  }

  document.querySelectorAll(".tab-label").forEach(function(label) {
    label.addEventListener("click", function() {
      var forId = this.getAttribute("for").replace("tab-", "");
      currentIdx = tabIds.indexOf(forId);
      if (currentIdx === -1) currentIdx = 0;
      updateIndicator();
    });
  });

  document.addEventListener("keydown", function(e) {
    if (e.key === "ArrowLeft")  { switchTab(-1); e.preventDefault(); }
    if (e.key === "ArrowRight") { switchTab(1);  e.preventDefault(); }
    if (e.key === "Escape")     { closeNewsModal(); }
  });

  updateIndicator();
})();

function showNewsDetail(card) {
  var detail = card.getAttribute("data-detail");
  var title  = card.getAttribute("data-title");
  var date   = card.getAttribute("data-date");
  var source = card.getAttribute("data-source");
  document.getElementById("modalTitle").textContent   = title;
  document.getElementById("modalDate").textContent    = date;
  document.getElementById("modalSource").textContent  = source || "";
  document.getElementById("modalContent").textContent = detail;
  var modal = document.getElementById("newsModal");
  modal.classList.add("active");
  document.body.style.overflow = "hidden";
}

function closeNewsModal() {
  document.getElementById("newsModal").classList.remove("active");
  document.body.style.overflow = "";
}

document.addEventListener("click", function(e) {
  if (e.target.classList.contains("news-modal-overlay")) { closeNewsModal(); }
});
</script>
'''


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

    if summary and summary.strip():
        categories = parse_categories(summary)
        log(f"[INFO] 解析到 {len(categories)} 个分类 (AI 模式)")
        news_html = generate_tabbed_html(categories, date_str)
        mode = "AI"
    else:
        log(f"[INFO] 使用 RSS 原始数据降级方案 ({len(news)} 条)")
        news_html = generate_raw_html(news, date_str)
        mode = "RSS"
        categories = []

    source_count = len(RSS_FEEDS)
    mode_label = "AI 智能分类" if mode == "AI" else "RSS 聚合"
    mode_badge = "🤖" if mode == "AI" else "📡"

    if categories or news:
        page = f"""---
layout: default
title: 热点新闻
---

<h1>📰 热点新闻速览</h1>
<p class="page-subtitle">每日自动聚合 · 国内外权威媒体 · 来源可溯 · 每日更新</p>

<div class="news-meta-bar">
  <span class="news-meta-item">📡 {source_count} 个信源</span>
  <span class="news-meta-item">{mode_badge} {mode_label}</span>
  <span class="news-meta-item">🕐 每日更新</span>
  <span class="news-meta-item">🔗 来源可溯</span>
</div>

{news_html}

---

<p class="news-updated">🕐 更新于 {date_only}</p>
"""

        with open("news.md", "w", encoding="utf-8") as f:
            f.write(page)
        log(f"[INFO] 已生成 news.md ({len(page)} 字符, {mode} 模式)")

        # 生成每日存档
        os.makedirs("archive", exist_ok=True)
        archive_file = f"archive/news-{date_only}.md"
        archive_page = f"""---
layout: default
title: 新闻存档 - {date_only}
---

<h1>📰 新闻存档 - {date_only}</h1>
<p class="page-subtitle">每日自动聚合 · 来源可溯 · <a href="{{{{ site.url }}}}/news" class="archive-back-link">← 返回最新新闻</a></p>

{news_html}

---

<p class="news-updated">🕐 发布于 {date_str}</p>
"""
        with open(archive_file, "w", encoding="utf-8") as f:
            f.write(archive_page)
        log(f"[INFO] 已生成存档 {archive_file}")
    else:
        log(f"[WARN] 无任何数据，保留现有 news.md，不覆盖")

    # 清理旧存档（保留最近30天历史）
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