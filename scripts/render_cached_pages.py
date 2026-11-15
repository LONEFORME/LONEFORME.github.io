"""Rebuild the dashboards from cached news, fetching only market data."""

import re
from datetime import datetime
from pathlib import Path

import news_digest as nd


def main():
    existing = Path("news.md").read_text(encoding="utf-8")
    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) 抓取更新", existing)
    if not match:
        raise RuntimeError("Cannot determine original news capture time")
    captured = match.group(1)
    date_only = captured[:10]
    items = nd.load_daily_cache(date_only)
    if not items:
        raise RuntimeError("No cached news; leaving pages intact")
    items.sort(key=lambda item: item.get("published_dt") or
               datetime.min.replace(tzinfo=nd.BEIJING_TZ), reverse=True)
    captured_dt = datetime.strptime(captured, "%Y-%m-%d %H:%M").replace(tzinfo=nd.BEIJING_TZ)
    fresh = [item for item in items if item.get("published_dt") and
             0 <= (captured_dt - item["published_dt"]).total_seconds() <= 86400]
    categorized = {section["id"]: [] for section in nd.SECTIONS_CONFIG}
    categorized["caijing"] = []
    for item in fresh or items:
        category = nd.classify_item(item)
        if category in categorized and len(categorized[category]) < nd.MAX_TOTAL_PER_SECTION:
            categorized[category].append(item)
    content = nd.build_page_html(categorized, date_only, crawled_time=captured)
    page = f"""---
layout: default
title: 热点新闻
---

{content}

<p class="news-updated">抓取更新于 {captured}（北京时间）· 最近 24 小时精选动态 · 往期请查阅历史归档</p>
"""
    Path("news.md").write_text(page, encoding="utf-8")
    nd.generate_finance_page(categorized["caijing"],
                             datetime.now(nd.BEIJING_TZ).strftime("%Y-%m-%d %H:%M"),
                             date_only)


if __name__ == "__main__":
    main()
