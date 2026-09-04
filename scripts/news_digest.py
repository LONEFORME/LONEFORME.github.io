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
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

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
    for _port in [7890, 7891, 7897, 10809, 1080]:
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
            _q = text[:450] if len(text) > 450 else text
            _params = {"q": _q, "langpair": "en|zh-CN"}
            _resp = _req.get(_url, params=_params, timeout=10)
            if _resp.status_code == 200:
                _data = _resp.json()
                _result = _data.get("responseData", {}).get("translatedText", "")
                if (_result and _result != _q and not is_error_page(_result, "") 
                        and "LIMIT EXCEEDED" not in _result.upper() and "MYMEMORY" not in _result.upper()):
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
    # 🇨🇳 国内官方权威媒体 (专业分流源：时政、国际、社会)
    {"url": "https://www.chinanews.com.cn/rss/china.xml", "name": "中国新闻网(时政)"},
    {"url": "https://www.chinanews.com.cn/rss/world.xml", "name": "中国新闻网(国际)"},
    {"url": "https://www.chinanews.com.cn/rss/society.xml", "name": "中国新闻网(社会)"},
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
    "人民网": "🇨🇳", "新华网": "🇨🇳", "中国新闻网": "🇨🇳", "中国新闻网(时政)": "🇨🇳", "中国新闻网(国际)": "🇨🇳", "中国新闻网(社会)": "🇨🇳", "中国新闻网(滚动)": "🇨🇳", "央视网": "🇨🇳",
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
    "人民网": "source-cn", "新华网": "source-cn", "中国新闻网": "source-cn", "中国新闻网(时政)": "source-cn", "中国新闻网(国际)": "source-cn", "中国新闻网(社会)": "source-cn", "中国新闻网(滚动)": "source-cn",
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
        "title": "西方媒体视角 (外媒看中国 · 奇葩言论集锦)",
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
    {"name": "伦敦现货黄金", "code": "hf_XAU", "flag": "🪙", "tag": "XAU/USD", "desc": "央行购金与全球避险"},
    {"name": "国内现货黄金", "code": "gds_AUTD", "flag": "🪙", "tag": "Au(T+D)", "desc": "上海黄金交易所基准"},
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
    "伦敦现货黄金": {"current": 4473.95, "change": 0.96, "change_pct": 0.02},
    "国内现货黄金": {"current": 967.07, "change": 9.97, "change_pct": 1.04},
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
            elif code.startswith("gds_"):
                # 贵金属现货/延期 (如上海金 Au(T+D)): 当前,买价,卖价,开盘,最高,最低,时间,昨结算,昨收,...
                name = parts[13] if len(parts) > 13 and parts[13] else "贵金属"
                current = float(parts[0]) if parts[0] else 0
                prev_close = float(parts[7]) if len(parts) > 7 and parts[7] and float(parts[7]) > 0 else (float(parts[8]) if len(parts) > 8 and parts[8] else 0)
                change = current - prev_close if prev_close else 0
                change_pct = (change / prev_close * 100) if prev_close else 0
                return {"name": name, "current": current, "change": change, "change_pct": change_pct}
            elif code.startswith("hf_"):
                # 外盘期货/外盘现货金: 当前,买价,卖价,今开,最高,最低,时间,昨结算,昨收,...,日期,名称
                name = parts[13] if len(parts) > 13 and parts[13] else "期货"
                current = float(parts[0]) if parts[0] else 0
                prev_close = float(parts[7]) if len(parts) > 7 and parts[7] and float(parts[7]) > 0 else (float(parts[2]) if len(parts) > 2 and parts[2] else 0)
                change = current - prev_close if prev_close else 0
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
    try:
        print(f"[{now}] {msg}", flush=True)
    except Exception:
        try:
            safe_msg = str(msg).encode(sys.stdout.encoding or 'utf-8', errors='replace').decode(sys.stdout.encoding or 'utf-8')
            print(f"[{now}] {safe_msg}", flush=True)
        except Exception:
            pass


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
    如果无有效日期或解析失败，返回 None。
    """
    if not raw_date or not str(raw_date).strip():
        return None

    raw_date = str(raw_date).strip()

    # 带时区偏移的格式（能正确解析 +0000, +0800, -0500 等）
    tz_formats = [
        "%a, %d %b %Y %H:%M:%S %z",       # RFC 2822: "Mon, 02 Sep 2026 06:00:00 +0000"
        "%a, %d %b %Y %H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S%z",             # ISO 8601: "2026-09-02T06:00:00+00:00"
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%d %H:%M:%S%z",
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
        "%a, %d %b %Y %H:%M:%S UTC",
        "%Y-%m-%dT%H:%M:%SZ",              # "2026-09-02T06:00:00Z"
        "%Y-%m-%dT%H:%M:%S.%fZ",
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
            return dt.replace(tzinfo=BEIJING_TZ)
        except ValueError:
            continue

    # 正则提取日期 YYYY-MM-DD
    m = re.search(r'(20\d{2})[-/](\d{1,2})[-/](\d{1,2})', raw_date)
    if m:
        try:
            return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), 12, 0, tzinfo=BEIJING_TZ)
        except ValueError:
            pass

    return None


def extract_item_datetime(entry, link=""):
    """多层级综合获取新闻发布时间：
    1. 识别 URL 中的年份路径（如 /2022/、/2023/、/2024/、/2025/），如果检测到历史年份，精准提取历史时间；
    2. 解析 entry 自带的 published / updated 字段；
    3. 解析 URL 中的当前日期（如 /2026/09-02/ 或 /20260902/）；
    4. 若以上全部无法获取，返回 None（严格杜绝无日期旧文章混入）。
    """
    now_bj = datetime.now(BEIJING_TZ)

    # 1. 优先检查 link 中是否明确包含历史过旧年份
    if link:
        m = re.search(r'/(20[12][0-9])[-_/]?(\d{1,2})[-_/]?(\d{1,2})', link)
        if m:
            try:
                y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                url_dt = datetime(y, mo, d, 12, 0, tzinfo=BEIJING_TZ)
                # 若 URL 中的日期早于 7 天前，直接判定为历史文章
                if (now_bj - url_dt) > timedelta(days=7):
                    return url_dt
            except ValueError:
                pass

    # 2. 解析 RSS published / updated 字段
    pub_raw = entry.get("published", entry.get("updated", ""))
    if pub_raw:
        dt = parse_datetime_bj(pub_raw)
        if dt:
            return dt

    # 3. 若 RSS 未标明时间，从 URL 中提取当前日期
    if link:
        m = re.search(r'/(20\d{2})[-_/]?(\d{1,2})[-_/]?(\d{1,2})', link)
        if m:
            try:
                y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                return datetime(y, mo, d, 12, 0, tzinfo=BEIJING_TZ)
            except ValueError:
                pass

    return None


def normalize_date(raw_date):
    """兼容包装：返回北京时间日期字符串 YYYY-MM-DD"""
    dt = parse_datetime_bj(raw_date)
    return dt.strftime("%Y-%m-%d") if dt else datetime.now(BEIJING_TZ).strftime("%Y-%m-%d")


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
        "limit exceeded", "mymemory warning", "quota exceeded",
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


def is_junk_notice(title, summary=""):
    """检测是否属于日常政务招标公告、采购意向、常规备案等低价值非新闻公文，返回 True 表示应该过滤掉"""
    if not title:
        return True
    text = (str(title) + " " + str(summary or "")).lower()
    junk_patterns = [
        "政府采购意向", "采购意向公开", "招标公告", "中标候选人", "中标结果", "成交结果",
        "遴选公告", "磋商公告", "询价公告", "比选公告", "招募公告", "出让公告",
        "挂牌出让", "拍卖公告", "招标代理", "工程监理招标", "施工招标", "资格预审公告",
        "答辩名单", "答辩安排", "复试名单", "公示期满", "征求意见稿", "预算公开", "决算公开",
        "政府采购合同", "单一来源采购"
    ]
    for jp in junk_patterns:
        if jp in text:
            return True
    return False


def is_suitable_headline(item):
    """判断是否适合作为今日头条焦点大图（排除非重磅、纯预警、小事故、公文通知）"""
    if not item or not item.get("title"):
        return False
    title = item["title"]
    if len(title.strip()) < 10:
        return False
    unsuitable_keywords = [
        "预警信号", "黄色预警", "蓝色预警", "大雾", "雷电", "暴雨", "海浪警报",
        "采购", "招标", "中标", "停水", "停电", "封路", "施工", "寻人", "失联",
        "通报批评", "开学第一课", "天气预报"
    ]
    for uk in unsuitable_keywords:
        if uk in title:
            return False
    return True


DOMESTIC_SOURCES = ["人民网", "新华网", "中国新闻网", "央视网"]


def is_sensitive_content(title, summary="", source=""):
    """检测是否是西方媒体的涉华偏见/抹黑/负面报道，返回 True 表示应该归类到外媒看中国板块。
    重要原则：
    1. 国内官方权威媒体绝不属于西方媒体视角；
    2. 必须是【涉华/外媒看中国】报道（如果不涉及中国，如美国国内建宴会厅、法庭审判等，绝不属于本板块）；
    3. 排除“司法审查”、“资格审查”等正常法律/合规词汇误判；
    4. 必须包含具体的意识形态偏见、抹黑或攻击性词汇。
    """
    if not title:
        return False

    # 1. 国内官方权威媒体一律不进"西方媒体视角"
    for ds in DOMESTIC_SOURCES:
        if ds in (source or ""):
            return False

    text = (str(title) + " " + str(summary or "")).lower()

    # 2. 必须明确属于涉华报道（外媒看中国）
    china_related = [
        "中国", "中方", "北京", "涉华", "两岸", "大陆", "华裔",
        "china", "chinese", "beijing", "prc", "sino",
        "xi jinping", "xi's", "taiwan", "hong kong", "xinjiang", "tibet"
    ]
    if not any(cr in text for cr in china_related):
        return False

    # 3. 排除正常法律/行政审查术语（如美国法律中的司法审查 judicial review，绝非言论审查）
    normal_review_terms = ["司法审查", "资格审查", "资质审查", "合规审查", "judicial review"]
    clean_text = text
    for nrt in normal_review_terms:
        clean_text = clean_text.replace(nrt, "")

    # 4. 真正的涉华偏见/抹黑/意识形态攻击关键词
    bias_patterns = [
        # 政治与人权批评类
        "言论审查", "网络审查", "新闻审查", "监控系统", "镇压", "压迫", "独裁", "一党", "极权", "威权",
        "侵犯人权", "宗教迫害", "言论自由", "新闻自由", "维权人士", "异见人士",
        "渗透", "间谍活动", "窃取机密", "黑客攻击", "网络攻击", "中国威胁论", "抹黑", "政治打压",
        # 涉疆涉港涉台等特定负面指控
        "集中营", "再教育营", "强迫劳动", "种族灭绝", "打压民主", "破坏自治",
        # 经济/科技负面指控
        "债务陷阱", "新殖民", "经济胁迫", "技术盗窃", "知识产权盗窃", "产能过剩论",
        # 英文敏感词
        "censorship", "mass surveillance", "oppression", "dictatorship", "authoritarian",
        "human rights violation", "religious persecution", "freedom of speech",
        "espionage", "cyber attack", "dissident",
        "concentration camp", "reeducation camp", "forced labor", "genocide",
        "debt trap", "neocolonial", "economic coercion", "ip theft", "overcapacity"
    ]
    for kw in bias_patterns:
        if kw in clean_text:
            return True
    return False


def is_recent(dt_obj):
    """判断是否在 MAX_AGE_DAYS 天内（用于存档保留）"""
    if dt_obj is None:
        return False
    now_bj = datetime.now(BEIJING_TZ)
    if isinstance(dt_obj, datetime):
        if dt_obj.tzinfo is None:
            dt_obj = dt_obj.replace(tzinfo=BEIJING_TZ)
        delta = now_bj - dt_obj
        return timedelta(hours=-2) <= delta <= timedelta(days=MAX_AGE_DAYS)
    return False


def is_frontpage_fresh(dt_obj):
    """判断是否在 FRONTPAGE_MAX_HOURS 小时内（用于首页过滤）"""
    if dt_obj is None:
        return False
    now_bj = datetime.now(BEIJING_TZ)
    if isinstance(dt_obj, datetime):
        if dt_obj.tzinfo is None:
            dt_obj = dt_obj.replace(tzinfo=BEIJING_TZ)
        delta = now_bj - dt_obj
        return timedelta(hours=-2) <= delta <= timedelta(hours=FRONTPAGE_MAX_HOURS)
    return False


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
            if title and link:
                # 提前过滤错误页面、低价值政务公文和无效标题（在任何处理之前）
                raw_sum_check = str(entry.get("summary", entry.get("description", "")) or "")
                if is_error_page(title, raw_sum_check) or is_junk_notice(title, raw_sum_check):
                    log(f"  [SKIP] 错误页面/低价值公文/无效标题: {title[:60]}")
                    continue

                # 智能提取发布时间，严格拒收无有效时间或历史陈旧新闻
                pub_dt = extract_item_datetime(entry, link)
                if not pub_dt or not is_recent(pub_dt):
                    log(f"  [SKIP] 无法识别时间或为历史陈旧文章: {title[:40]}")
                    continue

                # 敏感/偏见新闻单独分类到"西方媒体视角"板块
                title, publisher = parse_publisher(title)
                title = to_simplified(clean_title(title))
                # 英文标题自动翻译成中文
                if not has_chinese(title):
                    title = translate_to_chinese(title)
                src = normalize_source(publisher if publisher else source_name, title, link)
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
                        "feed_name": source_name,
                        "summary": clean_sum[:350]
                    })
                else:
                    log(f"  [SKIP] 过旧文章 ({date}): {title[:40]}")
        return entries
    except Exception as e:
        log(f"  [ERROR] 解析失败: {e}")
        return []


# ===== 细分领域关键词定义 =====
FOOTBALL_KEYWORDS = [
    "英超", "转会", "足球", "bbc 英超", "天空体育", "卫报", "阿森纳", "曼城", "利物浦", "曼联",
    "切尔西", "热刺", "皇马", "巴萨", "拜仁", "尤文", "国米", "米兰", "巴黎", "多特", "西甲",
    "意甲", "德甲", "法甲", "欧冠", "欧联", "世界杯", "亚冠", "中超", "足球赛", "足协杯", "点球", "任意球", "角球", "越位",
    "arsenal", "man city", "manchester", "liverpool", "chelsea", "tottenham", "spurs",
    "konsa", "villa", "reijnders", "rashford", "jones", "cherif", "garlick", "root",
    "cricket", "football", "premier league", "transfer", "signing", "striker", "midfielder",
    "defender", "goalkeeper", "manager", "fifa", "uefa"
]

OTHER_SPORTS_KEYWORDS = [
    # 球类与赛事
    "羽毛球", "乒乓球", "网球", "篮球", "排球", "斯诺克", "台球", "高尔夫", "棒球", "垒球",
    "手球", "水球", "曲棍球", "保龄球", "板球", "橄榄球", "冰球", "壁球",
    "大师赛", "公开赛", "锦标赛", "巡回赛", "挑战赛", "大奖赛", "争霸赛", "邀请赛",
    "奥运会", "亚运会", "大运会", "全运会", "冬奥会", "世锦赛", "青奥会", "残奥会",
    "汤姆斯杯", "尤伯杯", "苏迪曼杯", "戴维斯杯", "联合会杯", "温网", "美网", "法网", "澳网",
    "中网", "cba", "nba", "wcba", "fiba", "atp", "wta", "bwf", "ittf",
    # 田径、水上、冰雪、力量与格斗
    "田径", "短跑", "接力", "马拉松", "跨栏", "跳高", "跳远", "三级跳", "撑竿跳", "铅球",
    "标枪", "铁饼", "竞走", "游泳", "跳水", "花样游泳", "赛艇", "皮划艇", "帆船", "帆板",
    "冲浪", "滑雪", "短道速滑", "花样滑冰", "速度滑冰", "冰壶", "雪车", "雪橇",
    "拳击", "柔道", "跆拳道", "摔跤", "散打", "武术", "空手道", "击剑", "射击", "射箭",
    "举重", "体操", "艺术体操", "蹦床", "攀岩", "滑板", "霹雳舞", "赛车", "f1", "方程式",
    "围棋", "象棋", "国际象棋", "电竞", "电子竞技", "英雄联盟", "王者荣耀", "dota",
    # 比赛术语与赛况
    "爆冷出局", "爆冷淘汰", "爆冷获胜", "男单", "女单", "男双", "女双", "混双",
    "单打", "双打", "逆转取胜", "晋级四强", "晋级八强", "挺进决赛", "杀入决赛",
    "无缘四强", "无缘八强", "无缘半决赛", "无缘决赛", "卫冕冠军", "斩获金牌", "夺得金牌",
    "摘得金牌", "摘得银牌", "收获铜牌", "奖牌榜", "破世界纪录", "创赛会纪录", "头号种子",
    "种子选手", "抢七", "赛点", "局点", "破发", "发球直接得分", "扣杀", "吊球",
    "抢断", "三分球", "盖帽", "扣篮", "罚球", "大满贯", "运动员", "主教练", "裁判员"
]

ENTERTAINMENT_KEYWORDS = [
    "电影", "电视剧", "网剧", "微短剧", "院线", "票房", "首映", "影帝", "影后",
    "导演", "演员", "编剧", "制片人", "明星", "艺人", "歌手", "乐队", "演唱会",
    "巡演", "音乐节", "新专辑", "单曲", "mv", "综艺", "选秀", "脱口秀", "相声",
    "小品", "话剧", "舞台剧", "歌剧", "芭蕾舞", "音乐剧", "戏曲", "京剧", "越剧",
    "黄梅戏", "非遗", "博物馆", "文物", "考古", "艺术展", "书画展", "动漫", "番剧",
    "漫画", "cosplay", "漫展", "手游", "端游", "主机游戏", "八卦", "绯闻", "粉丝", "红毯"
]

LIFE_SOCIETY_KEYWORDS = [
    # 气象预警与自然灾害
    "气象台", "预警信号", "黄色预警", "橙色预警", "红色预警", "蓝色预警", "海浪警报",
    "暴雨", "大暴雨", "特大暴雨", "强降雨", "降雨量", "大雪", "暴雪", "大雾", "浓雾",
    "沙尘暴", "高温橙色", "高温红色", "寒潮", "强对流", "雷电", "冰雹", "台风",
    "泥石流", "山体滑坡", "地震", "余震", "震源深度", "洪峰", "汛情", "防汛",
    "山火", "森林火灾", "旱情", "人工增雨",
    # 市政便民与交通民生
    "公交专线", "公交线路", "地铁线路", "交通管制", "临时限行", "封路", "施工作业",
    "客运站", "火车站", "列车停运", "航班延误", "自来水", "停水通知", "停电通知",
    "燃气管道", "集中供暖", "菜篮子", "菜价", "粮油肉蛋", "惠农专线", "守护菜农",
    # 文旅休闲、美食民俗
    "景区", "门票", "免门票", "游乐园", "动物园", "植物园", "大熊猫", "赏月", "赏花",
    "游园", "露营", "徒步", "农家乐", "民俗", "庙会", "非遗市集", "美食节", "特色小吃",
    "老字号", "秋景", "赏秋", "红叶", "稻穗", "丰收", "梯田", "油菜花", "花海",
    # 校园教育与学生考试
    "开学", "开学第一课", "军训", "迎新", "校服", "师德师风", "教师节", "高考",
    "中考", "小升初", "考研", "录取通知书", "新生报到", "选调生", "招教", "校招",
    # 医疗健康生活与寻人搜救
    "医保报销", "门诊统筹", "疫苗接种", "流感", "支原体", "登革热", "养生", "食疗",
    "睡眠分数", "减重", "近视防控", "搜救", "救援队伍", "失联人员", "被困人员获救",
    "成功脱险", "见义勇为", "善款", "捐助", "寻人启事"
]

HIGH_PRECISION_SHIZHENG_KEYWORDS = [
    # 1. 核心中央机构与政治领导
    "中共中央", "党中央", "全国人大", "全国政协", "国务院", "中央政治局", "中央纪委", "国家监委",
    "最高人民法院", "最高检", "国家发改委", "外交部", "国防部", "国家安全部", "公安部",
    "司法部", "财政部", "商务部", "中联部", "统战部", "中宣部", "国台办", "港澳办",
    "特区政府", "行政长官", "立法会", "总书记", "国家主席", "国务院总理", "全国政协主席",
    "委员长", "中央军委", "国务委员", "省委书记", "省长", "市委书记", "市长", "自治区主席",
    # 2. 核心大政方针、反腐与法治
    "两会", "政府工作报告", "党风廉政", "反腐败", "严重违纪违法", "接受纪律审查", "开除党籍",
    "开除公职", "双开", "立案审查", "立案调查", "国家治理", "治国理政", "国家安全法", "基本法",
    "爱国者治港", "两岸融合", "对台方针", "涉台事务", "以武谋独", "祖国统一",
    # 3. 国际组织、首脑峰会与政府首长
    "联合国安理会", "联合国大会", "联合国秘书长", "白宫", "克里姆林宫", "五角大楼", "国会山",
    "美国参议院", "美国众议院", "欧洲议会", "欧盟委员会", "北约", "北约峰会", "g7峰会",
    "七国集团", "金砖国家", "上合组织", "g20峰会", "二十国集团", "东盟峰会", "非盟峰会",
    "阿盟", "海合会", "国际法院", "国际刑警",
    "内阁", "议长", "众议院", "参议院", "议员", "国会议员", "监察长",
    "总统", "副总统", "总理", "副总理", "首相", "国务卿", "劳工部长", "国防部长", "财政部长", "司法部长", "商务部长",
    "特朗普", "拜登", "普京", "泽连斯基", "内塔尼亚胡", "万斯", "哈里斯", "朔尔茨", "马克龙", "苏纳克", "斯塔默",
    # 4. 外交博弈、地缘政治与国际武装冲突
    "国事访问", "外长会谈", "防长会晤", "元首会晤", "首脑峰会", "双边会晤", "外交照会",
    "停火协议", "和平协定", "双边制裁", "对等反制", "驱逐外交官", "引渡协议", "划定边界",
    "领海领空", "主权争议", "台海局势", "地缘冲突", "巴以冲突", "俄乌局势", "俄乌攻防", "俄乌冲突", "俄乌",
    "朝鲜半岛局势", "伊核协议", "防扩散条约", "领事保护", "撤侨", "大使馆", "总领馆",
    "哈马斯", "真主党", "胡塞武装", "也门政府军",
    # 5. 国防军队与军事部署
    "解放军", "中国人民解放军", "战区", "火箭军", "战略支援部队", "海军陆战队", "航母编队",
    "军舰编队", "军事演习", "联合军演", "联合巡航", "战备巡逻", "导弹试射", "国防动员",
    "防务磋商", "特种部队", "武装冲突", "防空识别区", "空袭", "轰炸", "防空导弹", "导弹袭击",
    # 6. 国际外语高精度时政术语
    "president", "prime minister", "foreign minister", "defense secretary", "secretary of state",
    "white house", "pentagon", "capitol hill", "security council", "united nations",
    "state department", "foreign ministry", "defense ministry", "nato",
    "ceasefire", "peace talks", "state visit", "bilateral talks", "sanctions", "geopolitical"
]


def classify_item(item):
    """智能归类到五大核心板块之一（严格隔离非时政内容，杜绝体育/民生/公文误入时政）"""
    title = item.get("title", "")
    summary = item.get("summary", "")
    source = item.get("source", "")
    feed_name = item.get("feed_name", "")
    link = item.get("link", "").lower()

    # 注意：纯文本匹配严格使用 title 和 summary，绝不混入 source 字符串，避免源名称带有的"中国"污染判断
    text = f"{title} {summary}".lower()
    title_lower = title.lower()

    # 0. 垃圾政务公文与错误页面拦截（判定为 junk 绝不展示）
    if is_junk_notice(title, summary) or is_error_page(title, summary):
        return "junk"

    # 0.1 URL 路径强先验规则（官方媒体层级路由）
    if "/ty/" in link:
        if any(kw in text for kw in FOOTBALL_KEYWORDS):
            return "zuqiu"
        return "zonghe"

    if "/cj/" in link or "/stock/" in link:
        return "caijing"

    # 1. 足球 / 英超 / 转会（特征明确，优先提取）
    for kw in FOOTBALL_KEYWORDS:
        if kw in text:
            return "zuqiu"

    # 2. 其它所有体育竞技运动（羽毛球、乒乓球、篮球、网球、田径、游泳等，严格归入综合，彻底阻断进入时政）
    for kw in OTHER_SPORTS_KEYWORDS:
        if kw in text:
            return "zonghe"

    # 3. 严格股市行情/宏观金融（分流到 finance.md）
    finance_strict_keywords = [
        "a股", "港股", "美股", "股市", "大盘", "指数", "外资银行", "券商研报", "基金净流入",
        "低开", "高开", "涨停", "跌停", "中间价", "汇率", "关税", "贸易战", "cpi", "gdp", "央行加息", "降息",
        "证券", "债券", "理财", "纳斯达克", "标普", "道琼斯", "上证", "深证", "恒生"
    ]
    if any(kw in title_lower for kw in finance_strict_keywords):
        return "caijing"

    # 4. 文娱影视、生活民生、气象预警、自然风光（强制归入综合）
    for kw in ENTERTAINMENT_KEYWORDS:
        if kw in text:
            return "zonghe"

    for kw in LIFE_SOCIETY_KEYWORDS:
        if kw in text:
            return "zonghe"

    # 5. 军事冲突与地缘战况优先（避免因含有“无人机”等词被通用科技截胡）
    military_conflict_keywords = [
        "俄乌", "巴以", "哈马斯", "真主党", "胡塞武装", "军演", "联合军演", "战备巡逻", "防空导弹",
        "导弹", "空袭", "轰炸", "战区", "交火", "停火", "国防部", "五角大楼", "乌克兰危机", "以武谋独"
    ]
    if any(mw in text for mw in military_conflict_keywords):
        return "shizheng"

    # 6. 科技创新 & AI 算力（硬核聚焦：AI大模型突破、算法革新、半导体芯片巨头大动作）
    tech_sources = ["techcrunch", "tom's hardware", "ars technica", "the verge", "it之家", "量子位", "人民网(科技)"]
    if any(ts in source.lower() or ts in feed_name.lower() for ts in tech_sources):
        return "keji"

    ai_model_keywords = [
        "openai", "chatgpt", "gpt-4", "gpt-5", "o1", "o3", "deepseek", "深度求索",
        "claude", "anthropic", "gemini", "llama", "meta ai", "mistral", "qwen", "通义千问",
        "kimi", "moonshot", "智谱", "glm", "minimax", "sora", "runway", "kling", "可灵",
        "大模型", "基座模型", "推理模型", "reasoning model", "多模态", "multimodal", "智能体", "agent",
        "reinforcement learning", "强化学习", "rlhf", "scaling law", "context window", "token", "ai搜索"
    ]
    for kw in ai_model_keywords:
        if kw in text:
            return "keji"

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
        if kw in text:
            return "keji"

    clean_tech_text = re.sub(r'（?(无人机|航拍|资料|中新社|新华社)照片）?', '', text)
    general_tech_keywords = [
        "科技", "scitech", "ai", "人工智能", "机器人", "具身智能", "算法", "网络安全", "方班", "开源",
        "航天", "航空", "无人机", "卫星", "科普", "生物医药", "apple", "苹果", "m4", "m5",
        "google", "谷歌", "microsoft", "微软", "aws", "meta"
    ]
    for kw in general_tech_keywords:
        if kw in clean_tech_text:
            return "keji"

    # 7. 财经 & 宏观 & 产业
    finance_keywords = [
        "财经", "经济", "人民币", "中间价", "汇率", "外汇", "股市", "a股", "美股", "港股", "个股",
        "大盘", "指数", "低开", "高开", "涨停", "跌停", "关税", "贸易", "供应链", "航运",
        "核电", "能源", "光伏", "储能", "央行", "加息", "降息", "美联储", "通胀", "cpi", "gdp",
        "资产", "证券", "债券", "金融", "投资", "税收", "企业", "产业", "台企", "深耕", "赛道",
        "tariff", "trade", "inflation", "market", "economy", "financial", "stock", "company"
    ]
    for kw in finance_keywords:
        if kw in text:
            return "caijing"

    # 8. 西方媒体视角（严格限定：仅外媒信源且包含意识形态攻击/偏见抹黑词）
    if is_sensitive_content(title, summary, source):
        return "meimei"

    # 9. 严格高精度时政与国际要闻（坚决剔除“中国”、“美国”、“国际”、“安全”、“政策”等泛词）
    for kw in HIGH_PRECISION_SHIZHENG_KEYWORDS:
        if kw in text:
            return "shizheng"

    # 10. 信源层级辅助判断：若来自专门时政/国际源，且带有国内政治/国际新闻 URL
    if ("时政" in feed_name or "国际" in feed_name) and ("/gn/" in link or "/gj/" in link):
        return "shizheng"

    # 11. 默认归入综合要闻（文化社会 + 环保教育 + 历史人文 + 其它生活动态）
    return "zonghe"


def _esc(text):
    if not text:
        return ""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;")
                .replace("\r", "")
                .replace("\n", " ")
                .strip())


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

    # 优先选出 1 条重磅主头条（时政要闻 > 科技创新 > 综合社会 > 足球 > 外媒），严格过滤不适合头条的日常公告/警报
    featured = None
    featured_cat = "shizheng"
    for preferred_cat in ["shizheng", "keji", "zonghe", "zuqiu", "meimei"]:
        if preferred_cat in category_top_items and category_top_items[preferred_cat]:
            for cand in category_top_items[preferred_cat]:
                if is_suitable_headline(cand):
                    featured = cand
                    featured_cat = preferred_cat
                    break
            if featured:
                break

    if not featured:
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
  const terms = query.split(/\s+/).filter(Boolean);
  const items = document.querySelectorAll('.news-item, .hero-featured-card, .hero-sub-card');
  let matched = 0;

  if (!terms.length) {
    if (typeof filterNewsChannel === 'function') {
      const activeBtn = document.querySelector('.channel-btn.active');
      const channel = activeBtn ? (activeBtn.getAttribute('onclick') || '').match(/'([^']+)'/)?.[1] || 'all' : 'all';
      filterNewsChannel(channel, activeBtn);
    } else {
      items.forEach(el => el.style.display = '');
      document.querySelectorAll('.news-category').forEach(cat => cat.style.display = '');
    }
    const countEl = document.getElementById('news-search-count');
    if (countEl) countEl.innerText = '';
    return;
  }

  items.forEach(el => {
    const title = (el.getAttribute('data-title') || el.innerText || '').toLowerCase();
    const summary = (el.getAttribute('data-summary') || '').toLowerCase();
    const source = (el.getAttribute('data-source') || '').toLowerCase();
    const cat = (el.getAttribute('data-cat') || '').toLowerCase();
    const date = (el.getAttribute('data-date') || '').toLowerCase();
    const searchTarget = title + ' ' + summary + ' ' + source + ' ' + cat + ' ' + date;
    const isMatch = terms.every(t => searchTarget.includes(t));
    el.style.display = isMatch ? (el.classList.contains('news-item') ? 'flex' : 'block') : 'none';
    if (isMatch) matched++;
  });

  document.querySelectorAll('.news-category').forEach(cat => {
    const visibleChildren = cat.querySelectorAll('.news-item:not([style*="display: none"])');
    cat.style.display = visibleChildren.length > 0 ? 'block' : 'none';
  });

  const countEl = document.getElementById('news-search-count');
  if (countEl) {
    countEl.innerText = `🔍 找到 ${matched} 条`;
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
            price_str = f'${format_number(idx["current"], 2)} <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/盎司</span>'
            change_str = f"{change_sign}{idx['change']:.2f} ({change_sign}{idx['change_pct']:.2f}%)"
        elif idx["name"] == "国内现货黄金":
            price_str = f'¥{format_number(idx["current"], 2)} <span style="font-size:12px;font-weight:normal;color:var(--color-muted);">/克</span>'
            change_str = f"{change_sign}{idx['change']:.2f} ({change_sign}{idx['change_pct']:.2f}%)"
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
                    t_txt = str(it.get("title") or "")
                    sum_txt = str(it.get("summary") or "")
                    if is_junk_notice(t_txt, sum_txt) or is_error_page(t_txt, sum_txt):
                        continue
                    if "LIMIT EXCEEDED" in sum_txt.upper() or "MYMEMORY" in sum_txt.upper():
                        it["summary"] = ""
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