import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import market_history as mh


class MarketHistoryTests(unittest.TestCase):
    def test_ohlc_order_validation_sort_and_duplicate(self):
        rows = [
            ["2026-11-12", "10", "12", "13", "9", "100"],
            ["2026-11-11", "9", "10", "11", "8", "80"],
            ["2026-11-12", "10", "11", "13", "9", "120"],
            ["2026-11-13", "10", "12", "11", "9", "100"],
            ["2026-11-14", "NaN", "12", "13", "9", "100"],
        ]
        bars = mh.normalize_bars(rows, "day", "test")["bars"]
        self.assertEqual([b["time"] for b in bars], ["2026-11-11", "2026-11-12"])
        self.assertEqual(bars[-1]["close"], 11)
        self.assertEqual(bars[-1]["high"], 13)
        self.assertEqual(bars[-1]["volume"], 120)

    def test_hour_timestamp_is_beijing_time(self):
        row = {"day": "2026-11-13 10:30:00", "open": "10", "close": "11",
               "high": "12", "low": "9", "volume": "NaN"}
        bar = mh.normalize_bars([row], "hour", "test")["bars"][0]
        self.assertEqual(bar["time"], 1794537000)
        self.assertEqual(bar["volume"], 0)

    def test_intraday_volume_is_converted_to_lots(self):
        row = {"day": "2026-11-13 10:30:00", "open": "10", "close": "11",
               "high": "12", "low": "9", "volume": "1500"}
        self.assertEqual(mh.normalize_bars([row], "hour", "test")["bars"][0]["volume"], 15)

    def test_failed_refresh_retains_original_snapshot_and_timestamp(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "history.json"
            previous = {"markets": {"sh000001": {"name": "上证指数", "periods": {
                "day": {"fetchedAt": "2026-11-12T00:00:00+00:00", "source": "test",
                        "bars": [{"time": "2026-11-12", "open": 10, "close": 11,
                                  "high": 12, "low": 9}]}}}}}
            target.write_text(json.dumps(previous), encoding="utf-8")
            with patch.object(mh, "fetch_period", side_effect=ValueError("offline")), patch("builtins.print"):
                result = mh.refresh(target)
            self.assertEqual(result["markets"]["sh000001"]["periods"],
                             previous["markets"]["sh000001"]["periods"])

    def test_no_data_failure_does_not_create_fake_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "history.json"
            with patch.object(mh, "fetch_period", return_value={"bars": []}), patch("builtins.print"):
                with self.assertRaises(RuntimeError):
                    mh.refresh(target)
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
