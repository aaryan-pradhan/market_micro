"""Download NSE 1-minute bars from Yahoo Finance into project/data/ (yfinance keeps ~30 days of 1-min history)."""
from datetime import date, timedelta
from pathlib import Path
import pandas as pd, yfinance as yf

DATA = Path(__file__).resolve().parents[1] / "data"
TICKERS = {"RELIANCE.NS": "RELIANCE", "KSCL.NS": "KSCL"}

for yt, name in TICKERS.items():
    parts, end = [], date.today() + timedelta(days=1)
    start = end - timedelta(days=29)
    while start < end:  # Yahoo serves at most 8 days of 1-min bars per request
        stop = min(start + timedelta(days=7), end)
        parts.append(yf.Ticker(yt).history(start=start, end=stop, interval="1m", auto_adjust=False))
        start = stop
    d = pd.concat(parts).tz_convert("Asia/Kolkata").between_time("09:15", "15:29")
    d = d[~d.index.duplicated()].sort_index()[["Open", "High", "Low", "Close", "Volume"]]
    d.index.name = "timestamp"
    d.to_csv(DATA / f"{name}_1m.csv")
    print(f"{name}: {len(d)} bars, {d.index.normalize().nunique()} days, {d.index[0]} -> {d.index[-1]}")
