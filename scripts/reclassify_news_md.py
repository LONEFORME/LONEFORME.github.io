#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用最新 classify_item 规则重排 news.md 中的分类（不重新抓取）。"""
import re
import sys
import types
from pathlib import Path

for _mod in ("requests", "feedparser", "zhconv"):
    if _mod not in sys.modules:
        sys.modules[_mod] = types.ModuleType(_mod)
_dt = types.ModuleType("deep_translator")
_dt.GoogleTranslator = object
sys.modules["deep_translator"] = _dt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from news_digest import classify_item, SECTIONS_CONFIG, _esc

CAT_META = {s["id"]: s for s in SECTIONS_CONFIG}
# 财经不在 news 页展示，落到综合
FALLBACK = {
    "junk": None,
    "caijing": "zonghe",
    "keji": "keji",
    "zuqiu": "zuqiu",
    "shizheng": "shizheng",
    "zonghe": "zonghe",
    "meimei": "meimei",
}

ITEM_RE = re.compile(
    r'<a class="news-item" href="(?P<href>[^"]+)"[^>]*?'
    r'data-cat="(?P<cat>[^"]*)"[^>]*?'
    r'data-summary="(?P<summary>[^"]*)"[^>]*?'
    r'data-title="(?P<title>[^"]*)"[^>]*?'
    r'data-date="(?P<date>[^"]*)"[^>]*?'
    r'data-source="(?P<source>[^"]*)"[^>]*?'
    r'>(?P<body>.*?)</a>',
    re.S,
)

HEADER_RE = re.compile(
    r'(<div class="news-category">\s*'
    r'<div class="news-category-header">.*?<span class="news-category-count">)(\d+)( 条</span>)',
    re.S,
)


def make_item_html(item, cat_id):
    meta = CAT_META[cat_id]
    return (
        f'<a class="news-item" href="{item["href"]}" target="_blank" rel="noopener" '
        f'data-cat="{cat_id}" data-summary="{_esc(item["summary"])}" '
        f'data-title="{_esc(item["title"])}" data-date="{_esc(item["date"])}" '
        f'data-source="{_esc(item["source"])}">\n'
        f'          <span class="news-cat-tag {meta["tag_class"]}">{meta["tag_label"]}</span>\n'
        f'          {item["source_badge"]}\n'
        f'          <span class="news-item-date">{_esc(item["date"])}</span>\n'
        f'          <span class="news-item-title">{_esc(item["title"])}</span>\n'
        f'        </a>'
    )


def section_html(cat_id, items):
    meta = CAT_META[cat_id]
    parts = [
        '  <div class="news-category">',
        '    <div class="news-category-header">',
        f'      <span class="category-flag">{meta["flag"]}</span>',
        f'      <span class="news-category-title">{meta["title"]}</span>',
        f'      <span class="news-category-count">{len(items)} 条</span>',
        '    </div>',
    ]
    for it in items:
        parts.append("        " + make_item_html(it, cat_id))
    parts.append('  </div>')
    return "\n".join(parts)


def extract_source_badge(body: str) -> str:
    m = re.search(r'<span class="source-badge[^"]*">.*?</span>', body, re.S)
    return m.group(0).strip() if m else '<span class="source-badge">🌐</span>'


def main():
    path = Path("news.md")
    text = path.read_text(encoding="utf-8")
    items = []
    for m in ITEM_RE.finditer(text):
        summary = (
            m.group("summary")
            .replace("&quot;", '"')
            .replace("&#39;", "'")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&amp;", "&")
        )
        title = (
            m.group("title")
            .replace("&quot;", '"')
            .replace("&#39;", "'")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&amp;", "&")
        )
        old_cat = m.group("cat")
        new_raw = classify_item({
            "title": title,
            "summary": summary,
            "source": m.group("source"),
            "feed_name": m.group("source"),
            "link": m.group("href"),
        })
        new_cat = FALLBACK.get(new_raw, new_raw)
        if new_cat is None:
            continue
        if new_cat not in CAT_META:
            new_cat = "zonghe"
        items.append({
            "href": m.group("href"),
            "title": title,
            "summary": summary,
            "date": m.group("date"),
            "source": m.group("source"),
            "old_cat": old_cat,
            "new_cat": new_cat,
            "source_badge": extract_source_badge(m.group("body")),
        })
        if old_cat != new_cat:
            print(f"[MOVE] {old_cat} -> {new_cat}: {title[:50]}")

    # 保持时间顺序（输入已是时间序）
    by_cat = {sid: [] for sid in CAT_META}
    for it in items:
        by_cat[it["new_cat"]].append(it)

    start = text.find('<div class="news-grid">')
    end = text.find('</div>\n', text.rfind('  </div>', start))
    # 找 news-grid 的闭合：最后一个 </div> 前的 category 块结束
    # 更稳妥：从 news-grid 到 JS 过滤脚本前
    js_idx = text.find("<script>", start)
    if start < 0 or js_idx < 0:
        print("cannot locate news-grid", file=sys.stderr)
        sys.exit(1)
    # news-grid 包含所有 category；闭合 div 在 script 前
    before = text[:start]
    after = text[js_idx:]
    # after 之前应有 </div> 关闭 news-grid
    tail_match = re.search(r'(\s*</div>\s*)$', text[start:js_idx])
    grid_close = tail_match.group(1) if tail_match else "\n</div>\n"

    # 同步纠正首页 hero 子卡的分类标签
    def _fix_hero(m):
        attrs = m.group(0)
        title_m = re.search(r'data-title="([^"]*)"', attrs)
        sum_m = re.search(r'data-summary="([^"]*)"', attrs)
        src_m = re.search(r'data-source="([^"]*)"', attrs)
        href_m = re.search(r'href="([^"]*)"', attrs)
        if not title_m:
            return attrs
        title = title_m.group(1).replace("&quot;", '"').replace("&amp;", "&")
        summary = (sum_m.group(1) if sum_m else "").replace("&quot;", '"').replace("&amp;", "&")
        source = src_m.group(1) if src_m else ""
        href = href_m.group(1) if href_m else ""
        raw = classify_item({
            "title": title, "summary": summary, "source": source,
            "feed_name": source, "link": href,
        })
        cat = FALLBACK.get(raw, "zonghe")
        if cat not in CAT_META:
            cat = "zonghe"
        meta = CAT_META[cat]
        attrs = re.sub(r'data-cat="[^"]*"', f'data-cat="{cat}"', attrs)
        # 标签在卡片内部，由调用方整体替换
        return attrs

    def _fix_hero_block(m):
        block = m.group(0)
        attrs = _fix_hero(m)
        cat_m = re.search(r'data-cat="([^"]*)"', attrs)
        cat = cat_m.group(1) if cat_m else "zonghe"
        meta = CAT_META[cat]
        block = re.sub(r'data-cat="[^"]*"', f'data-cat="{cat}"', block)
        block = re.sub(
            r'<span class="news-cat-tag cat-[^"]+">[^<]+</span>',
            f'<span class="news-cat-tag {meta["tag_class"]}">{meta["tag_label"]}</span>',
            block,
            count=1,
        )
        return block

    before = re.sub(
        r'<a class="hero-sub-card"[\s\S]*?</a>',
        _fix_hero_block,
        before,
    )

    sections = "\n".join(section_html(sid, by_cat[sid]) for sid in CAT_META if by_cat[sid])
    new_grid = '<div class="news-grid">\n' + sections + grid_close
    path.write_text(before + new_grid + after, encoding="utf-8")
    print("done:", {k: len(v) for k, v in by_cat.items()})


if __name__ == "__main__":
    main()
