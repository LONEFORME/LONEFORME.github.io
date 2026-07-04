#!/usr/bin/env python3
"""News Digest - 抓取 RSS 新闻并用 AI 总结，生成网站页面"""

import feedparser
import json
import os
import sys
import requests
from datetime import datetime

log = lambda msg: print(msg, flush=True)

UA = "Mozilla/5.0 (compatible; NewsDigest/1.0; +https://loneforme.github.io)"

RSS_FEEDS = [
    {"url": "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=zh-CN&gl=CN&ceid=CN:zh-Hans", "name": "Google 新闻"},
    {"url": "https://www.bbc.co.uk/zhongwen/simp/index.xml", "name": "BBC 中文"},
    {"url": "https://hnrss.org/frontpage", "name": "Hacker News"},
]

API_URL = "https://opencode.ai/zen/go/v1/chat/completions"
API_KEY = os.environ.get("OPENCODE_GO_API_KEY")
MODEL = "deepseek-v4-flash"
MAX_ARTICLES_PER_FEED = 5
MAX_TOTAL = 20


def fetch_rss(url, timeout=20):
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": UA})
        r.raise_for_status()
        feed = feedparser.parse(r.content)
        entries = []
        for entry in feed.entries[:MAX_ARTICLES_PER_FEED]:
            title = entry.get("title", "").strip()
            link = entry.get("link", "")
            if title and link:
                entries.append({"title": title, "link": link})
        return entries
    except Exception as e:
        log(f"  [ERROR] 抓取失败: {e}")
        return []


def summarize_news(news_items, api_key):
    if not api_key:
        log("[ERROR] OPENCODE_GO_API_KEY 未设置")
        return None

    news_text = "\n".join(f"- {item['title']}" for item in news_items)
    links_text = "\n".join(f"- [{item['title']}]({item['link']})" for item in news_items)

    system_prompt = "用中文总结以下新闻，按主题分类，每类1-2句话。直接输出摘要，不要链接，不要推理过程。"

    try:
        resp = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"总结以下今日新闻：\n\n{news_text}\n\n原始链接：\n{links_text}"}
                ],
                "max_tokens": 8192,
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
            log(f"  Body: {resp.text[:500]}")
        return None


def main():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    log(f"[INFO] 开始抓取新闻 - {date_str}")

    all_news = []
    for feed in RSS_FEEDS:
        log(f"[INFO] 抓取: {feed['name']}...")
        entries = fetch_rss(feed["url"])
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

    links = "\n".join(f"- [{item['title']}]({item['link']})" for item in news)

    if news:
        log(f"[INFO] 调用 AI 总结 API ...")
        summary = summarize_news(news, API_KEY)
        if not summary:
            log(f"[INFO] API 返回为空，使用原始列表")
            summary = ""
    else:
        log(f"[INFO] 无新闻数据，生成空页面")
        summary = "暂无新闻数据。\n"

    page = f"""---
layout: default
title: 新闻摘要
---

# 今日热点摘要

> 自动抓取 · AI 摘要 · 每日更新

---

{summary}

---

## 原文链接

{links}

---

*生成时间: {date_str}*
*数据来源: Google 新闻、BBC 中文、Hacker News*
"""

    with open("news.md", "w", encoding="utf-8") as f:
        f.write(page)
    log(f"[INFO] 已生成 news.md ({len(page)} 字符)")


if __name__ == "__main__":
    main()
