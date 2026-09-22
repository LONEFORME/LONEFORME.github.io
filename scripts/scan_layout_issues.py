#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描站点 CSS 中容易导致“中间被缩小 / 末行大片空白”的同类问题。"""
from pathlib import Path
import re

css = Path("assets/css/custom.css").read_text(encoding="utf-8")

print("=== content max-width blocks ===")
for m in re.finditer(r'([^{}]{0,80}\.(?:content-inner|news-grid|card-grid|finance-ticker-grid|finance-sector-grid|theater-container)[^{}]*)\{([^}]+)\}', css):
    sel = " ".join(m.group(1).split())
    body = m.group(2)
    flags = []
    if re.search(r'max-width:\s*\d{3,4}px', body):
        flags.append(re.search(r'max-width:\s*[^;]+', body).group(0))
    if 'margin: 0 auto' in body or 'margin:0 auto' in body:
        flags.append('centered')
    if re.search(r'grid-template-columns', body):
        flags.append(re.search(r'grid-template-columns:\s*[^;]+', body).group(0).strip())
    if flags:
        print(f"- {sel}")
        for f in flags:
            print(f"    {f}")

print("\n=== auto-fill minmax (could leave leftover slots) ===")
for i, line in enumerate(css.splitlines(), 1):
    if 'auto-fill' in line and 'minmax' in line:
        print(f"  L{i}: {line.strip()}")

print("\n=== fixed width px > 400 (not media queries) ===")
for i, line in enumerate(css.splitlines(), 1):
    if re.search(r'(width|min-width):\s*[4-9]\d{2}px', line) and 'max-width:' not in line:
        print(f"  L{i}: {line.strip()}")

print("\n=== body/layout classes expected ===")
layout = Path("_layouts/default.html").read_text(encoding="utf-8")
print("layout-wide/read in default.html:", 'layout-wide' in layout and 'layout-read' in layout)
for p in ["index.html", "news.md", "finance.md", "projects.html", "docs.md", "videos.md", "3d-viewer.html"]:
    path = Path(p)
    if not path.exists():
        # try without ext
        continue
    t = path.read_text(encoding="utf-8", errors="replace")[:500]
    print(f"{p}: front/layout hint ok" if t.startswith("---") or t.startswith("<!") else f"{p}: check")
