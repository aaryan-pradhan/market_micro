"""Microstructure diagnostics: do the model's assumptions hold, and how liquid is the stock?"""
import numpy as np
import pandas as pd
from scipy import stats

from .calibration import price_changes


# --- Mid-price: is it an arithmetic Brownian motion? ------------------------

def autocorrelation(d: pd.DataFrame, max_lag: int = 10) -> pd.Series:
    """Autocorrelation of 1-minute price changes, pairs never straddle two days."""
    dp = d.groupby("day")["Close"].diff()
    out = {}
    for lag in range(1, max_lag + 1):
        lagged = dp.groupby(d["day"]).shift(lag)
        ok = dp.notna() & lagged.notna()
        out[lag] = np.corrcoef(dp[ok], lagged[ok])[0, 1]
    return pd.Series(out, name="acf")


def variance_ratio(d: pd.DataFrame, horizons=range(1, 31)) -> pd.Series:
    """VR(h) = Var(h-minute change) / (h * Var(1-minute change)); 1 under a random walk."""
    var1 = price_changes(d).var()
    out = {}
    for h in horizons:
        dh = d.groupby("day")["Close"].diff(h).dropna()
        out[h] = dh.var() / (h * var1)
    return pd.Series(out, name="vr")


def return_shape(d: pd.DataFrame) -> dict:
    dp = price_changes(d)
    z = (dp - dp.mean()) / dp.std()
    return dict(
        mean=dp.mean(),
        drift_t=dp.mean() / (dp.std() / np.sqrt(len(dp))),
        excess_kurtosis=stats.kurtosis(z),
        skew=stats.skew(z),
        jb_p=stats.jarque_bera(z).pvalue,
    )


# --- Are sigma and order flow constant through the day? --------------------

def intraday_profile(d: pd.DataFrame, bucket: int = 15) -> pd.DataFrame:
    """Per time-of-day bucket: sigma, share of daily volume, share of minutes traded."""
    b = (d["minute"] // bucket) * bucket
    dp = d.groupby("day")["Close"].diff()
    vol_share = d["Volume"] / d.groupby("day")["Volume"].transform("sum")
    return pd.DataFrame({
        "sigma": dp.groupby(b).std(),
        "volume_share": vol_share.groupby(b).sum() / d["day"].nunique(),
        "traded": d["traded"].groupby(b).mean(),
    })


def volume_by_minute(d: pd.DataFrame) -> pd.Series:
    """Average share of the day's volume traded in each minute."""
    share = d["Volume"] / d.groupby("day")["Volume"].transform("sum")
    return share.groupby(d["minute"]).mean()


# --- Liquidity measures from the course syllabus ----------------------------

def amihud_daily(d: pd.DataFrame) -> pd.Series:
    """Amihud (2002) ILLIQ per day: |daily return| / INR volume, scaled to per INR crore."""
    g = d.groupby("day")
    ret = (g["Close"].last() / g["Close"].first() - 1).abs()
    inr_volume = (d["Close"] * d["Volume"]).groupby(d["day"]).sum()
    return ret / (inr_volume / 1e7)


def roll_spread_daily(d: pd.DataFrame) -> pd.Series:
    """Roll (1984) spread per day: 2 sqrt(-Cov(dp_t, dp_{t-1})); NaN when the covariance is positive."""
    out = {}
    for day, g in d.groupby("day"):
        dp = g["Close"].diff()
        c = dp.cov(dp.shift(1))
        out[day] = 2 * np.sqrt(-c) if c < 0 else np.nan
    return pd.Series(out, name="roll")


def summary(d: pd.DataFrame) -> dict:
    """One row of the descriptive-statistics table."""
    days = d["day"].nunique()
    inr_volume = (d["Close"] * d["Volume"]).sum() / days
    return dict(
        days=days,
        price=d["Close"].mean(),
        inr_volume_cr=inr_volume / 1e7,
        no_trade_share=1 - d["traded"].mean(),
        sigma=price_changes(d).std(),
        range_mean=(d["High"] - d["Low"]).mean(),
        amihud=amihud_daily(d).mean(),
        roll=roll_spread_daily(d).mean(),
    )
