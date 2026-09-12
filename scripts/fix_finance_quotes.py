#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用修正后的新浪解析刷新 finance.md 中的股指数字。"""
import re
import urllib.request
from pathlib import Path


def fetch(code):
    url = f"https://hq.sinajs.cn/list={code}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://finance.sina.com.cn",
    })
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw = resp.read()
    text = raw.decode("gbk", errors="replace")
    m = re.search(r'="([^"]+)"', text)
    if not m:
        raise SystemExit(f"no data {code}: {text[:80]}")
    parts = m.group(1).split(",")
    name = parts[0]
    open_p = float(parts[1])
    prev = float(parts[2])
    cur = float(parts[3])
    ch = cur - prev
    pct = ch / prev * 100 if prev else 0
    print(f"{code}: {name} open={open_p:.2f} prev={prev:.2f} current={cur:.2f} {ch:+.2f} ({pct:+.2f}%)")
    return name, cur, ch, pct, ch >= 0


def fmt(n, d=2):
    return f"{n:,.{d}f}"


def main():
    path = Path(__file__).resolve().parent.parent / "finance.md"
    text = path.read_text(encoding="utf-8")
    mapping = [
        ("sh000001", "000001.SH"),
        ("sz399001", "399001.SZ"),
        ("sz399006", "399006.SZ"),
        ("sh000688", "000688.SH"),
    ]
    for code, code_tag in mapping:
        name, cur, ch, pct, up = fetch(code)
        m = re.search(
            rf'(<span class="ticker-code">{re.escape(code_tag)}</span>[\s\S]*?)'
            rf'<span class="ticker-price ticker-(?:up|down)">([^<]+)</span>\s*'
            rf'<span class="ticker-change (?:up|down)">([^<]+)</span>',
            text,
        )
        if not m:
            print("SKIP", code_tag)
            continue
        block = m.group(0)
        new_block = re.sub(
            r'<span class="ticker-price ticker-(?:up|down)">[^<]+</span>',
            f'<span class="ticker-price ticker-{"up" if up else "down"}">{fmt(cur)}</span>',
            block,
            count=1,
        )
        arrow = "▲" if up else "▼"
        sign = "+" if up else ""
        new_block = re.sub(
            r'<span class="ticker-change (?:up|down)">[^<]+</span>',
            f'<span class="ticker-change {"up" if up else "down"}">{arrow} {sign}{pct:.2f}%</span>',
            new_block,
            count=1,
        )
        text = text.replace(block, new_block)
        print("updated", code_tag)

    path.write_text(text, encoding="utf-8")
    print("finance.md refreshed ->", path)


if __name__ == "__main__":
    main()
