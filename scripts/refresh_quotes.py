#!/usr/bin/env python3
"""只刷新 finance.md 里的行情块，不碰新闻、不做翻译。

用途：GitHub Actions 的 schedule 常年延迟（实测 3.5~5.5 小时），新闻一天三次够用，
但汇率/黄金这类连续交易品种需要更勤。本脚本配合 quotes.yml 每小时跑一次，
把「最差情况 4 小时没更新」压到「最差 1 小时」。

用法：
    python scripts/refresh_quotes.py [--dry-run]
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import news_digest as nd  # noqa: E402

BEGIN = "<!-- QUOTES:BEGIN -->"
END = "<!-- QUOTES:END -->"
FINANCE = Path("finance.md")


def build_block() -> str:
    indices = nd.fetch_all_market_indices()
    ticker = nd.build_finance_ticker_html(indices)
    script = nd.build_finance_live_script()
    return f"{BEGIN}\n{ticker}\n\n{script}\n{END}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not FINANCE.exists():
        print("[quotes] 找不到 finance.md，跳过")
        return 0

    src = FINANCE.read_text(encoding="utf-8")
    if BEGIN not in src or END not in src:
        print("[quotes] finance.md 里没有行情块标记，跳过（等下一次完整生成）")
        return 0

    try:
        block = build_block()
    except Exception as exc:  # 网络抖动时不要破坏页面
        print(f"[quotes] 抓取失败，保留原内容：{exc}")
        return 0

    new = re.sub(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        lambda _: block,
        src,
        count=1,
        flags=re.S,
    )

    if new == src:
        print("[quotes] 行情无变化，不写文件")
        return 0

    print(f"[quotes] 已更新行情块 · {datetime.now():%Y-%m-%d %H:%M:%S}")
    if not args.dry_run:
        FINANCE.write_text(new, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
