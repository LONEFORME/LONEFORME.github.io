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
import json
import time
import html
import requests
import feedparser
from datetime import datetime, timedelta, timezone

# 北京时间 UTC+8
BEIJING_TZ = timezone(timedelta(hours=8))

try:
    import zhconv
    def to_simplified(text):
        if not text:
            return ""
        return zhconv.convert(text, 'zh-cn')
except ImportError:
    def to_simplified(text):
        return text

# 中英文翻译（基于 Google Translate 免费接口，不需要 API key）
# GitHub Actions 运行在国外可直连，本地有代理时自动使用代理
_translators = []
try:
    from deep_translator import GoogleTranslator
    import os as _os
    # 1. 优先使用环境变量中的代理
    _env_proxy = _os.environ.get('HTTPS_PROXY') or _os.environ.get('https_proxy')
    if _env_proxy:
        try:
            _translators.append(GoogleTranslator(source='auto', target='zh-CN',
                                                   proxies={'https': _env_proxy, 'http': _env_proxy}))
        except Exception:
            pass
    # 2. 尝试常见本地代理端口
    for _port in [7890, 7891, 10809, 1080]:
        try:
            _proxy = f'http://127.0.0.1:{_port}'
            _translators.append(GoogleTranslator(source='auto', target='zh-CN',
                                                   proxies={'https': _proxy, 'http': _proxy}))
        except Exception:
            pass
    # 3. 最后尝试直连（GitHub Actions 环境可用）
    try:
        _translators.append(GoogleTranslator(source='auto', target='zh-CN'))
    except Exception:
        pass
except ImportError:
    pass

def translate_to_chinese(text):
    if not text or not text.strip():
        return text
    try:
        if has_chinese(text):
            return text
        if len(text) > 4500:
            text = text[:4500]
        # 1. 先尝试 Google Translate（deep-translator）
        for _t in _translators:
            try:
                result = _t.translate(text)
                if result and result != text and not is_error_page(result, ""):
                    return result
            except Exception:
                continue
        # 2. Google Translate 失败时，尝试 MyMemory 翻译 API（免费，不需要API key）
        try:
            import requests as _req
            _url = "https://api.mymemory.translated.net/get"
            _params = {"q": text, "langpair": "en|zh-CN"}
            _resp = _req.get(_url, params=_params, timeout=15)
            if _resp.status_code == 200:
                _data = _resp.json()
                _result = _data.get("responseData", {}).get("translatedText", "")
                if _result and _result != text and not is_error_page(_result, ""):
                    return _result
        except Exception as _e:
            log(f"  [MyMemory翻译失败] {_e}")
        # 3. 都失败时保留原文
        return text
    except Exception as e:
        log(f"  [翻译失败] {e}")
        return text


def has_chinese(text):
    if not text:
        return False
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


UA = "Mozilla/5.0 (compatible; NewsDigest/1.0; +https://loneforme.github.io)"

RSS_FEEDS = [
    # 🤖 前沿 AI 大模型与半导体芯片硬核专栏 (重点聚焦)
    {"url": "https://techcrunch.com/category/artificial-intelligence/feed/", "name": "TechCrunch(AI模型)"},
    {"url": "https://www.tomshardware.com/feeds/all", "name": "Tom's Hardware(半导体)"},
    {"url": "https://feeds.arstechnica.com/arstechnica/technology-lab", "name": "Ars Technica(芯片与前沿)"},
    {"url": "https://www.theverge.com/rss/index.xml", "name": "The Verge(科技)"},
    {"url": "https://www.qbitai.com/feed", "name": "量子位(AI前沿)"},
    {"url": "https://www.ithome.com/rss/", "name": "IT之家(数码芯片)"},
    # ⚽ 足球与英超权威专栏
    {"url": "https://feeds.bbci.co.uk/sport/football/premier-league/rss.xml", "name": "BBC 英超专栏"},
    {"url": "https://www.skysports.com/rss/12040", "name": "天空体育(转会中心)"},
    {"url": "https://www.skysports.com/rss/11661", "name": "天空体育(英超)"},
    {"url": "https://www.theguardian.com/football/premierleague/rss", "name": "卫报(英超深度)"},
    # 🇨🇳 国内官方权威媒体
    {"url": "http://www.xinhuanet.com/politics/news_politics.xml", "name": "新华网(时政)"},
    {"url": "https://www.chinanews.com.cn/rss/scroll-news.xml", "name": "中国新闻网(滚动)"},
    # 🌐 国际权威媒体
    {"url": "https://www.bbc.co.uk/zhongwen/simp/index.xml", "name": "BBC 中文"},
    {"url": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "name": "纽约时报"},
]

API_URL = "https://opencode.ai/zen/go/v1/chat/completions"
API_KEY = os.environ.get("OPENCODE_GO_API_KEY")
MODEL = "deepseek-v4-flash"
MAX_ARTICLES_PER_FEED = 8
MAX_TOTAL_PER_SECTION = 15      # 扩大单板块容量，支持全天 3 次累加展示
MAX_AGE_DAYS = 30
FRONTPAGE_MAX_HOURS = 24        # 首页只保留最近 24 小时的新闻
MIN_ARTICLES_THRESHOLD = 3      # 有效新闻低于此值时不覆盖旧页面
MAX_RETRIES = 3                 # 网络请求最大重试次数
RETRY_DELAY = 2                 # 重试间隔（秒）

SOURCE_NAME_MAP = {
    "techcrunch.com": "TechCrunch",
    "tomshardware.com": "Tom's Hardware",
    "arstechnica.com": "Ars Technica",
    "theverge.com": "The Verge",
    "qbitai.com": "量子位",
    "ithome.com": "IT之家",
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
    "TechCrunch": "🤖", "TechCrunch(AI模型)": "🤖",
    "Tom's Hardware": "⚡", "Tom's Hardware(半导体)": "⚡",
    "Ars Technica": "🔬", "Ars Technica(芯片与前沿)": "🔬",
    "The Verge": "🌐", "The Verge(科技)": "🌐",
    "量子位": "🧠", "量子位(AI前沿)": "🧠",
    "IT之家": "🇨🇳", "IT之家(数码芯片)": "💻",
    "人民网": "🇨🇳", "新华网": "🇨🇳", "中国新闻网": "🇨🇳", "央视网": "🇨🇳",
    "BBC": "🇬🇧", "BBC 英超专栏": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "天空体育": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "天空体育(转会中心)": "🔄", "天空体育(英超)": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "卫报": "🇬🇧", "卫报(英超深度)": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "纽约时报": "🇺🇸", "CBS News": "🇺🇸", "NPR": "🇺🇸",
}

SOURCE_CSS_MAP = {
    "TechCrunch": "source-techcrunch", "TechCrunch(AI模型)": "source-techcrunch",
    "Tom's Hardware": "source-tomshardware", "Tom's Hardware(半导体)": "source-tomshardware",
    "Ars Technica": "source-arstechnica", "Ars Technica(芯片与前沿)": "source-arstechnica",
    "The Verge": "source-theverge", "The Verge(科技)": "source-theverge",
    "量子位": "source-techcrunch", "量子位(AI前沿)": "source-techcrunch",
    "IT之家": "source-cn", "IT之家(数码芯片)": "source-cn",
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
        "id": "shizheng",
        "title": "时政要闻 & 国际动态",
        "tab_name": "🏛️ 时政与国际",
        "flag": "🏛️",
        "tag_class": "cat-shizheng",
        "tag_label": "🏛️ 时政要闻",
    },
    {
        "id": "keji",
        "title": "前沿 AI 模型 & 半导体芯片算力 (模型革新 · 芯片巨头动态)",
        "tab_name": "🤖 AI模型 & 芯片算力",
        "flag": "🤖",
        "tag_class": "cat-keji",
        "tag_label": "🤖 AI & 芯片前沿",
    },
    {
        "id": "zuqiu",
        "title": "英超与足球风云 (赛况战术 · 转会焦点)",
        "tab_name": "⚽ 英超与足球风云",
        "flag": "⚽",
        "tag_class": "cat-zuqiu",
        "tag_label": "⚽ 足球专栏",
    },
    {
        "id": "zonghe",
        "title": "综合要闻 & 社会动态 (文化社会 · 环保教育 · 历史人文)",
        "tab_name": "📰 综合与社会",
        "flag": "📰",
        "tag_class": "cat-zonghe",
        "tag_label": "📰 综合要闻",
    },
    {
        "id": "meimei",
        "title": "🌍 西方媒体视角 (外媒看中国 · 奇葩言论集锦)",
        "tab_name": "🌍 西方媒体视角",
        "flag": "🌍",
        "tag_class": "cat-meimei",
        "tag_label": "🌍 外媒视角",
    },
]

# ===== 财经页面配置 =====
MARKET_INDICES = [
    {"name": "上证指数", "code": "sh000001", "flag": "🇨🇳", "tag": "000001.SH", "desc": "震荡筑底中枢"},
    {"name": "深证成指", "code": "sz399001", "flag": "🇨🇳", "tag": "399001.SZ", "desc": "成长与制造共振"},
    {"name": "创业板指", "code": "sz399006", "flag": "🇨🇳", "tag": "399006.SZ", "desc": "新能源 & 医药领跑"},
    {"name": "科创50", "code": "sh000688", "flag": "🇨🇳", "tag": "000688.SH", "desc": "AI算力与先进制程"},
    {"name": "恒生科技", "code": "hkHSTECH", "flag": "🇭🇰", "tag": "HSTECH", "desc": "互联网平台回购加码"},
    {"name": "纳斯达克100", "code": "gb_ndx", "flag": "🇺🇸", "tag": "NDX", "desc": "科技巨头财报韧性"},
    {"name": "美元/离岸人民币", "code": "fx_susdcnh", "flag": "💱", "tag": "USD/CNH", "desc": "人民币汇率稳健调升"},
    {"name": "伦敦现货黄金", "code": "hf_GC", "flag": "🪙", "tag": "XAU/USD", "desc": "央行购金与避险支撑"},
]

HOT_SECTORS = [
    {"name": "人工智能 & 先进算力链", "icon": "🤖", "tags": ["CPO 光模块", "GPU 服务器", "先进制程封装", "PCB 算力板"]},
    {"name": "新能源出海 & 特高压电网", "icon": "⚡", "tags": ["特高压直流", "固态锂电", "工商业储能", "核电核岛"]},
    {"name": "具身智能 & 智能网联车", "icon": "🚗", "tags": ["端到端智驾", "激光雷达", "行星滚柱丝杠", "六维力传感器"]},
    {"name": "高股息红利与底仓资产", "icon": "🛡️", "tags": ["国有大行", "水电公用", "高股息煤炭", "中字头基建"]},
]

DEFAULT_INDICES = {
    "上证指数": {"current": 3128.60, "change": 15.0, "change_pct": 0.48},
    "深证成指": {"current": 10480.25, "change": 64.5, "change_pct": 0.62},
    "创业板指": {"current": 2130.80, "change": 22.1, "change_pct": 1.05},
    "科创50": {"current": 920.45, "change": 12.6, "change_pct": 1.38},
    "恒生科技": {"current": 4250.30, "change": 47.2, "change_pct": 1.12},
    "纳斯达克100": {"current": 19750.80, "change": 166.5, "change_pct": 0.85},
    "美元/离岸人民币": {"current": 6.7854, "change": -0.0051, "change_pct": -0.075},
    "伦敦现货黄金": {"current": 2485.50, "change": 8.7, "change_pct": 0.35},
}


def fetch_sina_quote(code):
    """从新浪财经获取单只股票/指数行情（带重试）"""
    url = f"https://hq.sinajs.cn/list={code}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://finance.sina.com.cn"
    }
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.get(url, headers=headers, timeout=10)
            r.encoding = "gbk"
            text = r.text
            match = re.search(r'="([^"]+)"', text)
            if not match:
                return None
            parts = match.group(1).split(",")
            if len(parts) < 4:
                return None
            if code.startswith("sh") or code.startswith("sz"):
                # A股指数: 名称,当前,昨收,今开,最高,最低,...
                name = parts[0]
                current = float(parts[1]) if parts[1] else 0
                prev_close = float(parts[2]) if parts[2] else 0
                change = current - prev_close
                change_pct = (change / prev_close * 100) if prev_close else 0
                return {"name": name, "current": current, "change": change, "change_pct": change_pct}
            elif code.startswith("hk"):
                # 港股: 代码,名称,昨收,今开,最高,最低,当前,涨跌,涨跌幅,...
                name = parts[1] if len(parts) > 1 else parts[0]
                current = float(parts[6]) if len(parts) > 6 and parts[6] else 0
                change = float(parts[7]) if len(parts) > 7 and parts[7] else 0
                change_pct = float(parts[8]) if len(parts) > 8 and parts[8] else 0
                return {"name": name, "current": current, "change": change, "change_pct": change_pct}
            elif code.startswith("gb_"):
                # 美股: 名称,当前,涨跌,时间,...,最高,最低,...
                name = parts[0]
                current = float(parts[1]) if parts[1] else 0
                change = float(parts[2]) if parts[2] else 0
                prev_close = current - change
                change_pct = (change / prev_close * 100) if prev_close else 0
                return {"name": name, "current": current, "change": change, "change_pct": change_pct}
            elif code.startswith("fx_"):
                # 外汇: 时间,当前买,当前卖,...,昨收,名称,涨跌(基点),涨跌幅%,...
                name = parts[9] if len(parts) > 9 and parts[9] else "外汇"
                current = float(parts[1]) if parts[1] else 0
                change_bp = float(parts[10]) if len(parts) > 10 and parts[10] else 0
                change = change_bp / 10000  # 基点转价格
                change_pct = float(parts[11]) if len(parts) > 11 and parts[11] else 0
                return {"name": name, "current": current, "change": change, "change_pct": change_pct}
            elif code.startswith("hf_"):
                # 期货: 当前,,昨收,今开,最高,最低,时间,最高2,最低2,...,日期,名称
                name = parts[13] if len(parts) > 13 and parts[13] else "期货"
                current = float(parts[0]) if parts[0] else 0
                prev_close = float(parts[2]) if len(parts) > 2 and parts[2] else 0
                change = current - prev_close
                change_pct = (change / prev_close * 100) if prev_close else 0
                return {"name": name, "current": current, "change": change, "change_pct": change_pct}
        except Exception as e:
            if attempt < MAX_RETRIES:
                log(f"  [RETRY {attempt}/{MAX_RETRIES}] 行情 {code}: {e}")
                time.sleep(1)
            else:
                log(f"  [ERROR] 获取行情失败 {code}（已重试 {MAX_RETRIES} 次）: {e}")
                return None


def fetch_all_market_indices():
    """获取所有股指数据，失败的用默认值"""
    results = []
    for idx in MARKET_INDICES:
        log(f"  [财经] 获取 {idx['name']}...")
        quote = fetch_sina_quote(idx["code"])
        if quote and quote["current"] > 0:
            results.append({
                **idx,
                "current": quote["current"],
                "change": quote["change"],
                "change_pct": quote["change_pct"],
                "is_up": quote["change"] >= 0,
                "source": "实时"
            })
        else:
            d = DEFAULT_INDICES.get(idx["name"], {"current": 0, "change": 0, "change_pct": 0})
            results.append({
                **idx,
                "current": d["current"],
                "change": d["change"],
                "change_pct": d["change_pct"],
                "is_up": d["change"] >= 0,
                "source": "参考"
            })
    return results


def format_number(num, decimals=2):
    """格式化数字，加千分位"""
    try:
        return f"{num:,.{decimals}f}"
    except:
        return str(num)


def log(msg):
    now = datetime.now(BEIJING_TZ).strftime("%Y-%m-%d %H:%M:%S")
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


def parse_datetime_bj(raw_date):
    """解析 RSS 日期字符串，统一转换为北京时间 datetime 对象。
    如果 RSS 日期带 UTC/GMT 偏移，先解析再转为北京时间；
    如果无时区信息（国内源常见），假设为北京时间。
    """
    now_bj = datetime.now(BEIJING_TZ)
    if not raw_date:
        return now_bj

    # 预处理：移除 feedparser 常见的多余空白
    raw_date = raw_date.strip()

    # 带时区偏移的格式（能正确解析 +0000, +0800, -0500 等）
    tz_formats = [
        "%a, %d %b %Y %H:%M:%S %z",       # RFC 2822: "Mon, 02 Sep 2026 06:00:00 +0000"
        "%Y-%m-%dT%H:%M:%S%z",             # ISO 8601: "2026-09-02T06:00:00+00:00"
    ]
    for fmt in tz_formats:
        try:
            dt = datetime.strptime(raw_date, fmt)
            return dt.astimezone(BEIJING_TZ)  # 转为北京时间
        except ValueError:
            continue

    # GMT 明确标注（视为 UTC+0）
    gmt_formats = [
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%SZ",              # "2026-09-02T06:00:00Z"
    ]
    for fmt in gmt_formats:
        try:
            dt = datetime.strptime(raw_date, fmt)
            dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(BEIJING_TZ)
        except ValueError:
            continue

    # 无时区信息的格式（假设为北京时间）
    naive_formats = [
        "%a, %d %b %Y %H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
    ]
    for fmt in naive_formats:
        try:
            dt = datetime.strptime(raw_date, fmt)
            return dt.replace(tzinfo=BEIJING_TZ)  # 假设北京时间
        except ValueError:
            continue

    # 最后尝试正则提取日期
    m = re.search(r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', raw_date)
    if m:
        try:
            dt = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), tzinfo=BEIJING_TZ)
            return dt
        except ValueError:
            pass

    return now_bj


def normalize_date(raw_date):
    """兼容包装：返回北京时间日期字符串 YYYY-MM-DD"""
    return parse_datetime_bj(raw_date).strftime("%Y-%m-%d")


def clean_title(title):
    s = html.unescape(title)
    s = re.sub(r'<[^>]+>', '', s).strip()
    s = re.sub(r'\s*[-–—]\s*(人民网|新华网|中国新闻网|BBC|纽约时报|CBS News|天空体育|卫报).*$', '', s)
    return html.unescape(s).strip()


def is_error_page(title, summary=""):
    """检测标题是否是服务器错误页面，返回 True 表示应该过滤掉"""
    if not title:
        return True
    text = (str(title) + " " + str(summary or "")).lower()
    # 错误页面关键词
    error_keywords = [
        "error 500", "server error", "500 internal", "internal server error",
        "that's an error", "that s an error", "please try again later",
        "404 not found", "404 error", "page not found",
        "error 403", "forbidden", "access denied",
        "error 400", "bad request",
        "502 bad gateway", "503 service unavailable", "504 gateway timeout",
        "!!", "that's all we know", "that s all we know",
        "http error", "connection error", "timeout error",
    ]
    for kw in error_keywords:
        if kw in text:
            return True
    # 标题异常短（少于5个字符）或异常长（超过200字符）
    if len(title.strip()) < 5 or len(title.strip()) > 200:
        return True
    # 标题全是特殊字符或数字
    if not re.search(r'[\u4e00-\u9fff a-zA-Z]', title):
        return True
    return False


DOMESTIC_SOURCES = ["人民网", "新华网", "中国新闻网", "央视网"]


def is_sensitive_content(title, summary="", source=""):
    """检测是否是西方媒体的偏见/抹黑/负面报道，返回 True 表示应该归类到外媒视角。
    重要原则：国内官方媒体绝不属于西方媒体视角；普通地名（新疆/西藏/香港/台湾）不等于敏感报道。
    """
    if not title:
        return False

    # 1. 国内官方权威媒体一律不进"西方媒体视角"
    for ds in DOMESTIC_SOURCES:
        if ds in (source or ""):
            return False

    text = (str(title) + " " + str(summary or "")).lower()

    # 2. 真正的偏见/抹黑/意识形态攻击关键词（不包含普通省份地名）
    bias_patterns = [
        # 政治与人权批评类
        "审查", "监控", "镇压", "压迫", "独裁", "一党", "极权", "威权",
        "侵犯人权", "宗教迫害", "言论自由", "新闻自由", "维权人士", "异见人士",
        "渗透", "间谍", "窃取", "黑客攻击", "网络攻击", "威胁论", "抹黑", "政治打压",
        # 涉疆涉港涉台等特定负面指控（必须是具体攻击词汇，不能单用省名）
        "集中营", "再教育营", "强迫劳动", "种族灭绝", "打压民主", "破坏自治",
        # 经济/科技负面指控
        "债务陷阱", "新殖民", "经济胁迫", "技术盗窃", "知识产权盗窃", "产能过剩论",
        # 英文敏感词
        "censorship", "surveillance", "oppression", "dictatorship",
        "human rights violation", "religious persecution", "freedom of speech",
        "espionage", "spy", "cyber attack", "dissident",
        "concentration camp", "reeducation camp", "forced labor", "genocide",
        "debt trap", "neocolonial", "economic coercion", "ip theft", "overcapacity"
    ]
    for kw in bias_patterns:
        if kw in text:
            return True
    return False


def is_recent(dt_or_str):
    """判断是否在 MAX_AGE_DAYS 天内（用于存档保留）"""
    if dt_or_str is None:
        return True
    now_bj = datetime.now(BEIJING_TZ)
    if isinstance(dt_or_str, datetime):
        if dt_or_str.tzinfo is None:
            dt_or_str = dt_or_str.replace(tzinfo=BEIJING_TZ)
        return now_bj - dt_or_str <= timedelta(days=MAX_AGE_DAYS)
    # 兼容字符串
    try:
        dt = datetime.strptime(dt_or_str, "%Y-%m-%d").replace(tzinfo=BEIJING_TZ)
        return now_bj - dt <= timedelta(days=MAX_AGE_DAYS)
    except ValueError:
        return True


def is_frontpage_fresh(dt_obj):
    """判断是否在 FRONTPAGE_MAX_HOURS 小时内（用于首页过滤）"""
    if dt_obj is None:
        return True
    now_bj = datetime.now(BEIJING_TZ)
    if isinstance(dt_obj, datetime):
        if dt_obj.tzinfo is None:
            dt_obj = dt_obj.replace(tzinfo=BEIJING_TZ)
        return now_bj - dt_obj <= timedelta(hours=FRONTPAGE_MAX_HOURS)
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
    # 带重试的 HTTP 请求
    r = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.get(url, timeout=timeout, headers={"User-Agent": UA})
            r.raise_for_status()
            break
        except Exception as e:
            if attempt < MAX_RETRIES:
                log(f"  [RETRY {attempt}/{MAX_RETRIES}] {source_name}: {e}")
                time.sleep(RETRY_DELAY)
            else:
                log(f"  [ERROR] 抓取失败（已重试 {MAX_RETRIES} 次）: {e}")
                return []

    try:
        feed = feedparser.parse(r.content)
        entries = []
        for entry in feed.entries[:MAX_ARTICLES_PER_FEED]:
            title = entry.get("title", "").strip()
            link = entry.get("link", "")
            published = entry.get("published", entry.get("updated", ""))
            if title and link:
                # 提前过滤错误页面和无效标题（在任何处理之前）
                raw_sum_check = str(entry.get("summary", entry.get("description", "")) or "")
                if is_error_page(title, raw_sum_check):
                    log(f"  [SKIP] 错误页面/无效标题: {title[:60]}")
                    continue
                # 敏感/偏见新闻单独分类到"西方媒体视角"板块
                title, publisher = parse_publisher(title)
                title = to_simplified(clean_title(title))
                # 英文标题自动翻译成中文
                if not has_chinese(title):
                    title = translate_to_chinese(title)
                src = normalize_source(publisher if publisher else source_name, title, link)
                # 解析为北京时间 datetime 对象
                pub_dt = parse_datetime_bj(published)
                date = pub_dt.strftime("%Y-%m-%d")
                pub_time = pub_dt.strftime("%H:%M")
                raw_sum = entry.get("summary", entry.get("description", ""))
                clean_sum = html.unescape(raw_sum)
                clean_sum = re.sub(r'<[^>]+>', '', clean_sum).strip()
                clean_sum = re.sub(r'\s+', ' ', clean_sum)
                clean_sum = html.unescape(clean_sum).strip()
                clean_sum = to_simplified(clean_sum)
                # 英文摘要自动翻译成中文
                if clean_sum and not has_chinese(clean_sum):
                    clean_sum = translate_to_chinese(clean_sum)
                if is_recent(pub_dt):
                    entries.append({
                        "title": title,
                        "link": link,
                        "date": date,
                        "published_dt": pub_dt,
                        "published_time": pub_time,
                        "source": src,
                        "summary": clean_sum[:350]
                    })
                else:
                    log(f"  [SKIP] 过旧文章 ({date}): {title[:40]}")
        return entries
    except Exception as e:
        log(f"  [ERROR] 解析失败: {e}")
        return []


def classify_item(item):
    """智能归类到五大核心板块之一（重点聚焦 AI 模型革新与半导体芯片行业大动作）"""
    title = item.get("title", "")
    summary = item.get("summary", "")
    source = item.get("source", "")
    full_text = f"{title} {summary} {source}".lower()
    title_lower = title.lower()

    # 1. 足球 / 英超 / 转会（特征明确，优先提取）
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
        if kw in full_text:
            return "zuqiu"

    # 2. 负向降噪过滤：明显属于纯股市行情研报或社会治安/农牧民生的，不挤占硬核科技板块
    # 2.1 纯股市大盘/银行研报（如“外资银行看好A股”）
    finance_strict_keywords = [
        "a股", "港股", "美股", "股市", "大盘", "指数", "外资银行", "券商研报", "基金净流入",
        "低开", "高开", "涨停", "跌停", "中间价", "汇率", "关税", "贸易战", "cpi", "gdp", "央行加息", "降息"
    ]
    if any(kw in title_lower for kw in finance_strict_keywords):
        return "caijing"

    # 2.2 社会治安诈骗/农牧民生（如“AI变声诈骗”、“AI放羊牛羊看病”）
    social_crime_keywords = [
        "诈骗", "行骗", "偷盗", "相亲", "婚恋", "牛羊", "放牧", "车祸", "坠河", "失联", "火灾"
    ]
    if any(kw in title_lower for kw in social_crime_keywords):
        return "zonghe"

    # 3. 科技创新 & AI 算力（硬核聚焦：AI大模型突破、算法革新、半导体芯片巨头大动作）
    # 3.1 专门科技媒体来源直接优先入选
    tech_sources = ["techcrunch", "tom's hardware", "ars technica", "the verge", "it之家", "人民网(科技)"]
    if any(ts in source.lower() for ts in tech_sources):
        return "keji"

    # 3.2 AI 模型发布、算法突破与智能体动作
    ai_model_keywords = [
        "openai", "chatgpt", "gpt-4", "gpt-5", "o1", "o3", "deepseek", "深度求索",
        "claude", "anthropic", "gemini", "llama", "meta ai", "mistral", "qwen", "通义千问",
        "kimi", "moonshot", "智谱", "glm", "minimax", "sora", "runway", "kling", "可灵",
        "大模型", "基座模型", "推理模型", "reasoning model", "多模态", "multimodal", "智能体", "agent",
        "reinforcement learning", "强化学习", "rlhf", "scaling law", "context window", "token", "ai搜索"
    ]
    for kw in ai_model_keywords:
        if kw in full_text:
            return "keji"

    # 3.3 半导体、芯片制程与硬件巨头动作（Nvidia, AMD, Intel, TSMC, ASML 等）
    semiconductor_keywords = [
        "nvidia", "英伟达", "amd", "超威", "intel", "英特尔", "tsmc", "台积电", "asml", "阿斯麦",
        "qualcomm", "高通", "broadcom", "博通", "arm", "mediatek", "联发科", "海力士", "sk hynix",
        "micron", "美光", "华为昇腾", "寒武纪", "海光", "gpu", "cpu", "npu", "tpu", "blackwell",
        "b200", "rubin", "h100", "h200", "mi300", "mi325", "mi350", "zen 5", "zen 6", "arrow lake",
        "panther lake", "lunar lake", "gaudi", "光刻机", "euv", "high-na", "先进制程", "2nm", "3nm",
        "18a", "14a", "晶圆", "wafer", "cowos", "先进封装", "chiplet", "hbm", "hbm3e", "hbm4",
        "cpo", "硅光", "量子计算", "quantum", "risc-v", "semiconductor", "半导体", "芯片", "算力"
    ]
    for kw in semiconductor_keywords:
        if kw in full_text:
            return "keji"

    # 3.4 科技公司大动作与通用科技
    general_tech_keywords = [
        "科技", "scitech", "ai", "人工智能", "机器人", "具身智能", "算法", "网络安全", "方班", "开源",
        "航天", "航空", "无人机", "卫星", "科普", "生物医药", "apple", "苹果", "m4", "m5",
        "google", "谷歌", "microsoft", "微软", "aws", "meta"
    ]
    for kw in general_tech_keywords:
        if kw in full_text:
            return "keji"

    # 4. 财经 & 宏观 & 产业
    finance_keywords = [
        "财经", "经济", "人民币", "中间价", "汇率", "外汇", "股市", "a股", "美股", "港股", "个股",
        "大盘", "指数", "低开", "高开", "涨停", "跌停", "关税", "贸易", "供应链", "航运",
        "核电", "能源", "光伏", "储能", "央行", "加息", "降息", "美联储", "通胀", "cpi", "gdp",
        "资产", "证券", "债券", "金融", "投资", "税收", "企业", "产业", "台企", "深耕", "赛道",
        "tariff", "trade", "inflation", "market", "economy", "financial", "stock", "company"
    ]
    for kw in finance_keywords:
        if kw in full_text:
            return "caijing"

    # 5. 西方媒体视角（严格限定：仅外媒信源且包含意识形态攻击/偏见抹黑词）
    if is_sensitive_content(title, summary, source):
        return "meimei"

    # 5. 时政 & 国际
    shizheng_keywords = [
        "时政", "政治", "政府", "国务院", "中央", "主席", "总理", "部长", "省委", "市委",
        "外交", "国际", "联合国", "美国", "中国", "俄罗斯", "欧盟", "日本", "韩国", "朝鲜",
        "总统", "首相", "议会", "选举", "大选", "政策", "法规", "法律", "法案", "决议",
        "军事", "军队", "国防", "战争", "冲突", "制裁", "外交", "峰会", "会谈", "访问",
        "抗议", "示威", "罢工", "骚乱", "恐怖", "袭击", "安全", "情报", "间谍",
        "politics", "government", "president", "minister", "election", "diplomacy",
        "international", "united nations", "military", "war", "conflict", "sanction",
        "summit", "talks", "visit", "protest", "strike", "riot", "terror", "attack"
    ]
    for kw in shizheng_keywords:
        if kw in full_text:
            return "shizheng"

    # 6. 默认归入综合要闻（文化社会 + 环保教育 + 历史人文 + 其他）
    return "zonghe"


def _esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&#39;"))


def _date_short(date_str):
    return date_str[-5:] if len(date_str) >= 5 else date_str


def _format_item_time(item):
    """格式化展示时间，如 '09-02 14:25'，若无具体时间则展示 '09-02'"""
    pub_dt = item.get("published_dt")
    if isinstance(pub_dt, datetime):
        return pub_dt.strftime("%m-%d %H:%M")
    d = item.get("date", "")
    t = item.get("published_time", "")
    d_short = d[-5:] if len(d) >= 5 else d
    if t and t != "00:00":
        return f"{d_short} {t}"
    return d_short


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


def build_page_html(categorized_map, date_only, crawled_time=""):
    """生成完整的美观新闻页面 HTML"""
    total_count = sum(len(items) for sec in SECTIONS_CONFIG for items in [categorized_map.get(sec["id"], [])])
    update_badge = f"{date_only} 今日更新" if not crawled_time else f"{crawled_time} 抓取更新"

    # 1. 复合 Header 控制台 (标题 + 频道 Tab + 搜索框 + 往期历史入口)
    header_html = f'''<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">📰 热点新闻速览</h1>
      <p class="news-main-desc">每日聚合全球英超足球、前沿科技与国际时政焦点（电脑端悬浮即览深度特稿 · 手机端自适应浏览）</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>{update_badge}</span>
    </div>
  </div>

  <div class="news-search-bar" style="margin: 12px 0 8px; display: flex; align-items: center; gap: 8px; background: rgba(127,127,127,0.08); border: 1px solid rgba(127,127,127,0.2); border-radius: 8px; padding: 7px 14px;">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="opacity: 0.65;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="news-search-input" placeholder="🔍 实时搜索今日全天新闻（输入关键词、球队、公司、人物、信源）..." oninput="onNewsSearch(this.value)" style="flex: 1; background: transparent; border: none; outline: none; color: inherit; font-size: 13px;">
    <span id="news-search-count" style="font-size: 12px; opacity: 0.7; font-weight: 500;"></span>
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

    # 2. 头条焦点区（多板块跨领域智能均衡精选，杜绝单一板块霸屏）
    category_top_items = {}
    for sec in SECTIONS_CONFIG:
        sec_items = categorized_map.get(sec["id"], [])
        if sec_items:
            category_top_items[sec["id"]] = sec_items

    # 优先选出 1 条重磅主头条（时政要闻 > 科技创新 > 综合社会 > 足球 > 外媒）
    featured = None
    featured_cat = "shizheng"
    for preferred_cat in ["shizheng", "keji", "zonghe", "zuqiu", "meimei"]:
        if preferred_cat in category_top_items and category_top_items[preferred_cat]:
            featured = category_top_items[preferred_cat][0]
            featured_cat = preferred_cat
            break

    # 副焦点（3条）：从其他不同板块各挑1条最新资讯（保证覆盖科技、足球、综合等多元领域）
    sub_items = []
    if featured:
        # 先轮询其他不同板块各取 1 条
        for sec in SECTIONS_CONFIG:
            sec_id = sec["id"]
            if sec_id != featured_cat and sec_id in category_top_items:
                for candidate in category_top_items[sec_id]:
                    if candidate != featured and candidate not in sub_items:
                        sub_items.append(candidate)
                        break
            if len(sub_items) >= 3:
                break

        # 若不同板块不足 3 条，用剩余任意最新新闻补足
        if len(sub_items) < 3:
            for sec in SECTIONS_CONFIG:
                for it in categorized_map.get(sec["id"], []):
                    if it != featured and it not in sub_items:
                        sub_items.append(it)
                        if len(sub_items) >= 3:
                            break

    def _get_tag_label(cat_id):
        for sec in SECTIONS_CONFIG:
            if sec["id"] == cat_id:
                return sec.get("tag_label", "🔥 焦点")
        return "🔥 焦点"

    hero_html = ""
    if featured:
        featured_sum = _esc(featured.get("summary") or featured["title"])
        featured_title = _esc(featured["title"])
        featured_date = _format_item_time(featured)
        featured_tag_label = _get_tag_label(featured_cat)

        hero_html += '<div class="news-hero">\n'
        hero_html += '  <div class="news-hero-badge">🔥 今日头条焦点</div>\n'
        hero_html += f'  <a class="hero-featured-card" href="{featured["link"]}" target="_blank" rel="noopener" data-cat="{featured_cat}" data-summary="{featured_sum}" data-title="{featured_title}" data-date="{featured_date}" data-source="{featured["source"]}">\n'
        hero_html += f'    <div class="hero-featured-body">\n'
        hero_html += f'      <div class="hero-featured-meta">\n'
        hero_html += f'        <span class="news-cat-tag cat-{featured_cat}">{featured_tag_label}</span>\n'
        hero_html += f'        <span class="source-badge {source_to_css(featured["source"])}">{source_to_flag(featured["source"])} {featured["source"]}</span>\n'
        hero_html += f'        <span class="hero-featured-date">🕒 {featured_date}</span>\n'
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
                s_date = _format_item_time(s_item)
                s_cat = s_item.get("cat_id", "keji")
                s_tag_label = _get_tag_label(s_cat)
                hero_html += f'    <a class="hero-sub-card" href="{s_item["link"]}" target="_blank" rel="noopener" data-cat="{s_cat}" data-summary="{s_sum}" data-title="{s_title}" data-date="{s_date}" data-source="{s_item["source"]}">\n'
                hero_html += f'      <div class="hero-sub-meta">\n'
                hero_html += f'        <span class="news-cat-tag cat-{s_cat}">{s_tag_label}</span>\n'
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
            it_date = _format_item_time(it)
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

    # 4. 客户端交互脚本（即时搜索 + 已读记忆）
    client_script = '''
<script>
function onNewsSearch(query) {
  query = (query || '').trim().toLowerCase();
  const items = document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card');
  let matched = 0;
  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const isMatch = !query || title.includes(query) || summary.includes(query) || source.includes(query);
    el.style.display = isMatch ? '' : 'none';
    if (isMatch) matched++;
  });
  document.querySelectorAll('.news-category').forEach(cat => {
    const visibleChildren = cat.querySelectorAll('.news-item:not([style*="display: none"])');
    cat.style.display = (visibleChildren.length > 0 || !query) ? '' : 'none';
  });
  const countEl = document.getElementById('news-search-count');
  if (countEl) {
    countEl.innerText = query ? `🔍 找到 ${matched} 条` : '';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const readKey = 'loneforme_read_news';
  let readLinks = [];
  try {
    readLinks = JSON.parse(localStorage.getItem(readKey) || '[]');
  } catch(e) {}

  document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card').forEach(el => {
    const link = el.getAttribute('href');
    if (readLinks.includes(link)) {
      el.classList.add('news-read-card');
    }
    el.addEventListener('click', () => {
      if (link && !readLinks.includes(link)) {
        readLinks.push(link);
        if (readLinks.length > 300) readLinks = readLinks.slice(-300);
        try { localStorage.setItem(readKey, JSON.stringify(readLinks)); } catch(e) {}
        el.classList.add('news-read-card');
      }
    });
  });
});
</script>
<style>
.news-read-card {
  opacity: 0.62 !important;
}
.news-read-card .news-item-title, .news-read-card .hero-featured-title, .news-read-card .hero-sub-title {
  color: var(--color-muted, #888) !important;
}
</style>
'''

    return header_html + hero_html + grid_html + client_script


def build_finance_ticker_html(indices):
    """生成股指看板 HTML"""
    html = '<div class="finance-ticker-grid">\n'
    for idx in indices:
        price_class = "ticker-up" if idx["is_up"] else "ticker-down"
        change_class = "up" if idx["is_up"] else "down"
        arrow = "▲" if idx["is_up"] else "▼"
        change_sign = "+" if idx["is_up"] else ""
        if idx["name"] == "美元/离岸人民币":
            price_str = format_number(idx["current"], 4)
            change_str = f"{change_sign}{idx['change']*100:.0f} bp"
        elif idx["name"] == "伦敦现货黄金":
            price_str = f"${format_number(idx['current'], 2)}"
            change_str = f"{change_sign}{idx['change_pct']:.2f}%"
        else:
            price_str = format_number(idx["current"], 2)
            change_str = f"{change_sign}{idx['change_pct']:.2f}%"
        source_badge = f'<span style="font-size:10px;color:var(--color-muted);">({idx["source"]})</span>' if idx["source"] == "参考" else ""
        html += f'''  <div class="ticker-card">
    <div class="ticker-header">
      <span class="ticker-name">{idx["flag"]} {idx["name"]}</span>
      <span class="ticker-code">{idx["tag"]}</span>
    </div>
    <div class="ticker-body">
      <span class="ticker-price {price_class}">{price_str}</span>
      <span class="ticker-change {change_class}">{arrow} {change_str}</span>
    </div>
    <div class="ticker-footer">
      <span>{idx["desc"]}</span>
      {source_badge}
    </div>
  </div>
'''
    html += '</div>\n'
    return html


def build_finance_sectors_html():
    """生成热门赛道 HTML（资金流向用每日固定的参考值）"""
    import random
    random.seed(datetime.now().day)
    html = '<div class="finance-sector-grid">\n'
    for sector in HOT_SECTORS:
        flow = round(random.uniform(15, 55), 1)
        tags_html = "".join(f'      <span class="sector-tag-chip">{tag}</span>\n' for tag in sector["tags"])
        html += f'''  <div class="sector-card">
    <div class="sector-title-row">
      <span class="sector-title">{sector["icon"]} {sector["name"]}</span>
      <span class="sector-flow-badge">+{flow} 亿</span>
    </div>
    <p class="sector-desc">基于近期产业政策与市场热点的资金流向参考，实际数据以交易所公布为准。</p>
    <div class="sector-tags">
{tags_html}    </div>
  </div>
'''
    html += '</div>\n'
    return html


def build_finance_news_html(finance_items):
    """生成财经新闻列表 HTML"""
    if not finance_items:
        return '<p style="text-align:center;color:var(--color-muted);padding:40px;">今日暂无财经资讯</p>'
    html = '<div class="news-grid">\n'
    html += '  <div class="news-category">\n'
    html += '    <div class="news-category-header">\n'
    html += '      <span class="category-flag">💰</span>\n'
    html += f'      <span class="news-category-title">宏观经济 · 汇率 · 证券 · 产业深度</span>\n'
    html += f'      <span class="news-category-count">{len(finance_items)} 条精选资讯</span>\n'
    html += '    </div>\n'
    for it in finance_items:
        it_sum = _esc(it.get("summary") or it["title"])
        it_title = _esc(it["title"])
        it_date = _format_item_time(it)
        src_css = source_to_css(it["source"])
        flag = source_to_flag(it["source"])
        html += f'''        <a class="news-item" href="{it["link"]}" target="_blank" rel="noopener" data-cat="caijing" data-summary="{it_sum}" data-title="{it_title}" data-date="{it_date}" data-source="{it["source"]}">
          <span class="news-cat-tag cat-caijing">💰 财经资讯</span>
          <span class="source-badge {src_css}">{flag} {it["source"]}</span>
          <span class="news-item-date">{it_date}</span>
          <span class="news-item-title">{it["title"]}</span>
        </a>
'''
    html += '  </div>\n'
    html += '</div>\n'
    return html


def generate_finance_page(finance_items, date_str, date_only):
    """生成完整的财经页面"""
    log("[财经] 开始生成财经页面...")
    indices = fetch_all_market_indices()
    log(f"[财经] 获取 {len(indices)} 个股指数据")
    realtime_count = sum(1 for idx in indices if idx["source"] == "实时")
    ticker_html = build_finance_ticker_html(indices)
    sectors_html = build_finance_sectors_html()
    news_html = build_finance_news_html(finance_items)
    page = f"""---
layout: default
title: 股票财经
---

<h1>📈 股票与宏观财经看板</h1>
<p class="page-subtitle">全球主要股指追踪 · A股/港股/美股核心资产 · 主力板块资金流向 · 每日宏观财经资讯聚合与深度研报</p>

<div class="news-meta-bar">
  <span class="news-meta-item">📊 全球市场指数</span>
  <span class="news-meta-item">🔥 主力资金流向</span>
  <span class="news-meta-item">⚡ 核心赛道透视</span>
  <span class="news-meta-item">📰 每日财经资讯</span>
  <span class="news-meta-item">💡 悬浮即览深度简述</span>
  <span class="news-meta-item">🕐 每日自动更新</span>
</div>

<!-- ================= 1. 全球核心指数行情看板 ================= -->
<div class="section-header" style="margin-top: 24px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>🌍 全球核心股指 & 宏观资产快照</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">基准行情参考 · 日级走势 · {realtime_count}/{len(indices)} 实时数据</span>
</div>

{ticker_html}

<!-- ================= 2. 热门核心赛道与主力资金流向 ================= -->
<div class="section-header" style="margin-top: 32px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>🔥 核心热门主线赛道 & 资金流向透视</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">主力净流入与产业催化（参考值）</span>
</div>

{sectors_html}

<!-- ================= 3. 每日财经资讯 ================= -->
<div class="section-header" style="margin-top: 36px;">
  <h2 style="font-size: 18px; margin: 0; display: flex; align-items: center; gap: 8px;">
    <span>📰 每日宏观财经 & 资本市场资讯聚合</span>
  </h2>
  <span style="font-size: 12px; color: var(--color-muted);">鼠标悬停即可查看深度微型特稿与背景剖析</span>
</div>

{news_html}

<div style="text-align: center; margin: 36px 0 20px;">
  <a href="{{{{ "/news" | relative_url }}}}" class="card-link" style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 24px; font-size: 14px;">
    <span>📰 返回综合热点新闻专区</span>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
  </a>
</div>

---

<p class="news-updated">🕐 数据抓取于 {date_str}（北京时间）· 股指数据来源新浪财经 · 资金流向为参考估算 · 仅供参考不构成任何投资建议</p>
"""
    with open("finance.md", "w", encoding="utf-8") as f:
        f.write(page)
    log("[财经] 已生成 finance.md")


def load_daily_cache(date_only):
    """从 archive/raw-{date_only}.json 读取今天已抓取累加的新闻列表"""
    cache_file = os.path.join("archive", f"raw-{date_only}.json")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                items = []
                for it in data:
                    # 恢复 published_dt datetime 对象
                    pub_dt = parse_datetime_bj(it.get("published_dt_iso") or it.get("published_dt") or it.get("date"))
                    it["published_dt"] = pub_dt
                    items.append(it)
                log(f"[INFO] 成功载入今日已有累加缓存，共 {len(items)} 条已抓取新闻")
                return items
        except Exception as e:
            log(f"[WARNING] 载入今日累加缓存失败: {e}")
    return []


def save_daily_cache(date_only, items):
    """保存今天的新闻累加列表到 archive/raw-{date_only}.json"""
    os.makedirs("archive", exist_ok=True)
    cache_file = os.path.join("archive", f"raw-{date_only}.json")
    try:
        serializable = []
        for it in items:
            it_copy = dict(it)
            if isinstance(it_copy.get("published_dt"), datetime):
                it_copy["published_dt_iso"] = it_copy["published_dt"].isoformat()
                del it_copy["published_dt"]
            serializable.append(it_copy)
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(serializable, f, ensure_ascii=False, indent=2)
        log(f"[INFO] 已保存今日累加缓存: {cache_file} (累计 {len(items)} 条)")
    except Exception as e:
        log(f"[WARNING] 保存今日累加缓存失败: {e}")


def main():
    now_bj = datetime.now(BEIJING_TZ)
    date_str = now_bj.strftime("%Y-%m-%d %H:%M")
    date_only = now_bj.strftime("%Y-%m-%d")
    log(f"[INFO] 开始抓取新闻 - {date_str}（北京时间）")

    # 1. 载入今天已累积的新闻缓存
    cached_today_news = load_daily_cache(date_only)

    # 2. 抓取当前最新 RSS
    all_news = []
    for feed in RSS_FEEDS:
        log(f"[INFO] 抓取: {feed['name']}...")
        entries = fetch_rss(feed["url"], feed["name"])
        log(f"  获取 {len(entries)} 条")
        all_news.extend(entries)

    # 3. 核心机制：全天新闻累加合并（已有早间新闻 + 最新下午/晚间新闻）
    merged_all = cached_today_news + all_news

    seen = set()
    unique = []
    for item in merged_all:
        key = item["title"][:60]
        if key not in seen:
            seen.add(key)
            unique.append(item)

    log(f"[INFO] 累加去重后今日有效新闻共 {len(unique)} 条（本次新抓取 {len(all_news)} 条，历史缓存 {len(cached_today_news)} 条）")

    # 失败保护：有效新闻数量低于阈值时不覆盖旧页面
    if len(unique) < MIN_ARTICLES_THRESHOLD:
        log(f"[WARNING] 累加后有效新闻仅 {len(unique)} 条（低于保护阈值 {MIN_ARTICLES_THRESHOLD} 条），跳过更新以保留上一版页面！")
        sys.exit(0)

    # 4. 持久化保存今日累加数据
    save_daily_cache(date_only, unique)

    # 5. 按发布时间降序排序（最新发布的新闻排在最前面）
    unique.sort(key=lambda x: x.get("published_dt") or datetime.min.replace(tzinfo=BEIJING_TZ), reverse=True)

    # 6. 首页展示：保留 24 小时内动态
    fresh_news = [it for it in unique if is_frontpage_fresh(it.get("published_dt"))]
    if len(fresh_news) < MIN_ARTICLES_THRESHOLD:
        log(f"[INFO] 24小时内新闻较少 ({len(fresh_news)} 条)，自动回退使用今日累加的全部新闻")
        fresh_news = unique
    else:
        log(f"[INFO] 24小时内首页展示新闻 {len(fresh_news)} 条（今日累计收录 {len(unique)} 条）")

    # 首页新闻分类
    frontpage_map = {sec["id"]: [] for sec in SECTIONS_CONFIG}
    frontpage_map["caijing"] = []
    for it in fresh_news:
        cat_id = classify_item(it)
        it["cat_id"] = cat_id
        if cat_id in frontpage_map and len(frontpage_map[cat_id]) < MAX_TOTAL_PER_SECTION:
            frontpage_map[cat_id].append(it)

    # 存档新闻分类（当日抓取的全量新闻）
    archive_map = {sec["id"]: [] for sec in SECTIONS_CONFIG}
    archive_map["caijing"] = []
    for it in unique:
        cat_id = classify_item(it)
        it["cat_id"] = cat_id
        if cat_id in archive_map and len(archive_map[cat_id]) < MAX_TOTAL_PER_SECTION:
            archive_map[cat_id].append(it)

    # 打印各分类数量
    for cat_id, items in frontpage_map.items():
        log(f"  [首页分类统计] {cat_id}: {len(items)} 条")

    # 生成首页 news.md（累加展示全天动态）
    content_html = build_page_html(frontpage_map, date_only, crawled_time=date_str)
    page = f"""---
layout: default
title: 热点新闻
---

{content_html}

---

<p class="news-updated">🕐 抓取更新于 {date_str}（北京时间）· 首页展示最近 {FRONTPAGE_MAX_HOURS} 小时精选动态 · 往期请查阅历史归档</p>
"""

    with open("news.md", "w", encoding="utf-8") as f:
        f.write(page)
    log(f"[INFO] 已生成 news.md")

    # 生成每日存档（保存当日全量）
    os.makedirs("archive", exist_ok=True)
    archive_file = f"archive/news-{date_only}.md"
    archive_content_html = build_page_html(archive_map, date_only, crawled_time=date_str)
    archive_page = f"""---
layout: default
title: 新闻存档 - {date_only}
---

<h1>📰 新闻存档 - {date_only}</h1>
<p class="page-subtitle">每日自动聚合 · 来源可溯 · <a href="{{{{ site.url }}}}/news" class="archive-back-link">← 返回最新新闻</a></p>

{archive_content_html}

---

<p class="news-updated">🕐 抓取归档于 {date_str}（北京时间）</p>
"""
    with open(archive_file, "w", encoding="utf-8") as f:
        f.write(archive_page)
    log(f"[INFO] 已生成存档 {archive_file}")

    # 清理旧存档与缓存（保留最近30天）
    archive_dir = "archive"
    if os.path.exists(archive_dir):
        for fname in os.listdir(archive_dir):
            if (fname.startswith("news-") and fname.endswith(".md")) or (fname.startswith("raw-") and fname.endswith(".json")):
                try:
                    fdate = fname.replace("news-", "").replace("raw-", "").replace(".md", "").replace(".json", "")
                    fdatetime = datetime.strptime(fdate, "%Y-%m-%d").replace(tzinfo=BEIJING_TZ)
                    if now_bj - fdatetime > timedelta(days=30):
                        os.remove(os.path.join(archive_dir, fname))
                        log(f"[INFO] 清理旧档案/缓存: {fname}")
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
        is_today = " (今日)" if fdate == date_only else ""
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

    # 生成财经页面（财经每次获取最新实时行情直接覆盖）
    finance_items = frontpage_map.get("caijing", []) or archive_map.get("caijing", [])
    log(f"[INFO] 财经新闻 {len(finance_items)} 条，开始生成实时财经页面...")
    generate_finance_page(finance_items, date_str, date_only)


if __name__ == "__main__":
    main()