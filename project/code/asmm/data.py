"""Load the raw 1-minute bars and put each day on a complete minute grid."""
import numpy as np
import pandas as pd

from .config import DATA_DIR, SESSION_START, SESSION_END, T, N_CALIB_DAYS


def load(stock: str) -> pd.DataFrame:
    """Bars for one stock on a full 09:15-15:14 grid (T rows per day).

    A minute with no bar is a minute with no trade: its close is carried
    forward (the mid-price did not move), its high/low stay NaN (no quote
    could be filled) and its volume is 0.
    """
    raw = pd.read_csv(DATA_DIR / f"{stock}_1m.csv", index_col="timestamp", parse_dates=True)
    raw.index = pd.to_datetime(raw.index, utc=True).tz_convert("Asia/Kolkata")
    raw = raw.between_time(SESSION_START, SESSION_END)

    days = []
    for day, g in raw.groupby(raw.index.date):
        grid = pd.date_range(f"{day} {SESSION_START}", periods=T, freq="min", tz=raw.index.tz)
        g = g.reindex(grid)
        g["traded"] = g["Close"].notna()
        g["Close"] = g["Close"].ffill().bfill()
        g["Volume"] = g["Volume"].fillna(0.0)
        g["day"] = pd.Timestamp(day)
        g["minute"] = np.arange(T)
        days.append(g)
    return pd.concat(days)


def split(d: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """(calibration days, out-of-sample test days)."""
    days = d["day"].unique()
    calib = d["day"].isin(days[:N_CALIB_DAYS])
    return d[calib], d[~calib]


def by_day(d: pd.DataFrame):
    """Iterate (day, frame) in date order."""
    return d.groupby("day", sort=True)
