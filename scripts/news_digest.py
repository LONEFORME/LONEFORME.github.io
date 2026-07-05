#!/usr/bin/env python3
"""News Digest - 抓取 RSS 新闻并用 AI 总结，生成网站页面"""

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

步骤1：审查内容 — 优先采用权威媒体（新华社、人民日报、央视、BBC等），剔除明显不实信息。
步骤2：按主题分类（时政、科技AI、电脑硬件、财经、国际、社会），每类精选最多5条。
步骤3：输出以下格式，每篇末尾标注来源。

格式：
### 分类名
- **日期** | **标题** | 内容摘要 [来源: XXX]

要求：
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

    if news:
        log(f"[INFO] 调用 AI 总结 API ...")
        summary = summarize_news(news, API_KEY)
        if not summary:
            log(f"[INFO] API 返回为空")
            summary = "暂无摘要。"
    else:
        summary = "暂无新闻数据。\n"

    page = f"""---
layout: default
title: 新闻摘要
---

# 今日热点摘要

> AI 精选 · 来源可溯 · 每日更新

---

{summary}

---

*生成时间: {date_str}*
"""

    with open("news.md", "w", encoding="utf-8") as f:
        f.write(page)
    log(f"[INFO] 已生成 news.md ({len(page)} 字符)")


if __name__ == "__main__":
    main()
