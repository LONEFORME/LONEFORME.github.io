"""Fetch genuine OHLC bars for the static market dashboard."""

import json
import math
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/data/market-history.json"
MARKETS = {
    "sh000001": "上证指数",
    "sz399001": "深证成指",
    "sz399006": "创业板指",
    "sh000688": "科创50",
    "hkHSTECH": "恒生科技",
    "hkHSI": "恒生指数",
}
PERIODS = ("hour", "day", "week", "month")


def normalize_bars(rows, period, source):
    """Discard malformed candles; never synthesize OHLC from quote snapshots."""
    bars = {}
    for row in rows:
        try:
            if isinstance(row, dict):
                stamp = row["day"]
                values = [float(row[key]) for key in ("open", "high", "low", "close")]
                volume = float(row.get("volume", 0))
            else:
                stamp = row[0]
                values = [float(row[i]) for i in (1, 3, 4, 2)]
                volume = float(row[5]) if len(row) > 5 else 0
            opening, high, low, close = values
            if not all(math.isfinite(v) and v > 0 for v in values):
                continue
            if low > min(opening, close) or high < max(opening, close) or low > high:
                continue
            if period == "hour":
                # Sina timestamps are market-local Beijing time.
                time = int(datetime.fromisoformat(stamp + "+08:00").timestamp())
                # Sina intraday volume is in shares; Tencent daily volume is in lots.
                volume /= 100
            else:
                datetime.strptime(stamp, "%Y-%m-%d")
                time = stamp
            if not math.isfinite(volume) or volume < 0:
                volume = 0
            bars[time] = dict(time=time, open=opening, high=high, low=low,
                              close=close, volume=volume)
        except (ValueError, TypeError, KeyError, IndexError):
            continue
    return {"source": source, "bars": [bars[t] for t in sorted(bars)]}


def fetch_period(code, period):
    if period == "hour":
        if not code.startswith(("sh", "sz")):
            return None
        response = requests.get(
            "https://quotes.sina.cn/cn/api/jsonp_v2.php/var/"
            "CN_MarketDataService.getKLineData",
            params={"symbol": code, "scale": 60, "ma": "no", "datalen": 240},
            headers={"Referer": "https://finance.sina.com.cn",
                     "User-Agent": "Mozilla/5.0"}, timeout=18)
        response.raise_for_status()
        match = re.search(r"\(\s*(\[.*\])\s*\)", response.text, re.S)
        if not match:
            raise ValueError("No hourly bars in response")
        return normalize_bars(json.loads(match.group(1)), period, "新浪财经")
    response = requests.get(
        "https://web.ifzq.gtimg.cn/appstock/app/fqkline/get",
        params={"param": f"{code},{period},,,{640 if period == 'day' else 180},qfq"},
        headers={"User-Agent": "Mozilla/5.0"}, timeout=18)
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise ValueError(payload.get("msg", "K-line request failed"))
    node = payload.get("data", {}).get(code, {})
    return normalize_bars(node.get(period) or node.get("qfq" + period) or [],
                          period, "腾讯证券")


def refresh(output=OUTPUT):
    output = Path(output)
    try:
        previous = json.loads(output.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        previous = {"markets": {}}
    markets = {}
    for code, name in MARKETS.items():
        old = previous.get("markets", {}).get(code, {})
        markets[code] = {"name": name, "periods": dict(old.get("periods", {}))}

    jobs = [(code, period) for code in MARKETS for period in PERIODS
            if period != "hour" or code.startswith(("sh", "sz"))]

    def run(job):
        code, period = job
        try:
            data = fetch_period(code, period)
            if data and len(data["bars"]) >= 2:
                data["fetchedAt"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                return code, period, data, None
            return code, period, None, "insufficient bars"
        except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
            return code, period, None, str(exc)

    with ThreadPoolExecutor(max_workers=6) as pool:
        for code, period, data, error in pool.map(run, jobs):
            if data:
                markets[code]["periods"][period] = data
                print(f"[kline] {code} {period}: {len(data['bars'])} bars")
            else:
                print(f"[kline] {code} {period}: kept previous data ({error})")
    if not any(market["periods"] for market in markets.values()):
        raise RuntimeError("No usable OHLC data; keeping the existing snapshot")
    result = {"schemaVersion": 1, "markets": markets}
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".tmp")
    temporary.write_text(json.dumps(result, ensure_ascii=False, separators=(",", ":")),
                         encoding="utf-8")
    temporary.replace(output)
    return result


if __name__ == "__main__":
    refresh()
