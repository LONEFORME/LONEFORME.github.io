#!/usr/bin/env python3
"""News Digest - 抓取 RSS 新闻并用 AI 总结，生成网站页面"""

import feedparser
import json
import os
import sys
import requests
from datetime import datetime

RSS_FEEDS = [
    {"url": "https://rsshub.app/36kr/news/latest", "name": "36氪"},
    {"url": "https://rsshub.app/thepaper/latest", "name": "澎湃新闻"},
    {"url": "https://rsshub.app/zhihu/daily", "name": "知乎日报"},
    {"url": "https://rsshub.app/huxiu/article", "name": "虎嗅"},
]

API_URL = "https://opencode.ai/zen/go/v1/chat/completions"
API_KEY = os.environ.get("OPENCODE_GO_API_KEY")
MODEL = "deepseek-v4-flash"
MAX_ARTICLES_PER_FEED = 5
MAX_TOTAL = 20


def fetch_rss(url, timeout=20):
    try:
        feed = feedparser.parse(url)
        entries = []
        for entry in feed.entries[:MAX_ARTICLES_PER_FEED]:
            title = entry.get("title", "").strip()
            link = entry.get("link", "")
            if title and link:
                entries.append({"title": title, "link": link})
        return entries
    except Exception as e:
        print(f"  [ERROR] {e}", file=sys.stderr)
        return []


def summarize_news(news_items, api_key):
    if not api_key:
        print("[ERROR] OPENCODE_GO_API_KEY 未设置", file=sys.stderr)
        return None

    news_text = "\n".join(f"- {item['title']}" for item in news_items)
    links_text = "\n".join(f"- [{item['title']}]({item['link']})" for item in news_items)

    system_prompt = "你是一个新闻编辑。请用中文总结以下新闻，按主题分类（如科技、财经、时政），每类1-2句话，Markdown格式，保持客观简洁。最后附上原始链接列表。"

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
                "max_tokens": 3000,
                "temperature": 0.3
            },
            timeout=120
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[ERROR] API 调用失败: {e}", file=sys.stderr)
        if "resp" in dir():
            print(f"  Status: {resp.status_code}", file=sys.stderr)
        return None


def main():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[INFO] 开始抓取新闻 - {date_str}")

    all_news = []
    for feed in RSS_FEEDS:
        print(f"[INFO] 抓取: {feed['name']}...")
        entries = fetch_rss(feed["url"])
        print(f"  获取 {len(entries)} 条")
        all_news.extend(entries)

    seen = set()
    unique = []
    for item in all_news:
        key = item["title"][:60]
        if key not in seen:
            seen.add(key)
            unique.append(item)

    news = unique[:MAX_TOTAL]
    print(f"[INFO] 去重后共 {len(news)} 条")

    summary = summarize_news(news, API_KEY)
    if not summary:
        summary = "今日暂无摘要。\n"
        for item in news:
            summary += f"- [{item['title']}]({item['link']})\n"

    page = f"""---
layout: default
title: 新闻摘要
---

# 今日热点摘要

> 自动抓取 · AI 摘要 · 每日更新

---

{summary}

---

*生成时间: {date_str}*
"""

    with open("news.md", "w", encoding="utf-8") as f:
        f.write(page)
    print(f"[INFO] 已生成 news.md ({len(page)} 字符)")


if __name__ == "__main__":
    main()
