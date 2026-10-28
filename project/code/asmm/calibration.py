"""Estimate sigma, A and k from 1-minute bars.

Fill proxy: a quote placed at distance delta from this minute's close is
filled if next minute's high (ask side) or low (bid side) reaches it. If
order arrivals are Poisson with rate lambda, P(fill in one minute) =
1 - exp(-lambda), so lambda(delta) = -ln(1 - p(delta)). Regressing
ln lambda on delta gives ln A (intercept) and -k (slope).
"""
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .config import FIT_P_BAND
from .model import Params


@dataclass
class FillCurve:
    delta: np.ndarray       # quote distances (INR)
    p: np.ndarray           # fill probability per minute
    lam: np.ndarray         # implied Poisson intensity per minute
    used: np.ndarray        # mask of points inside FIT_P_BAND
    A: float
    k: float
    r2: float


def excursions(d: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """(next high - close, close - next low) for every minute that has a next minute.

    NaN (next minute had no trade) compares False below, i.e. counts as no fill.
    """
    nxt = d.groupby("day")[["High", "Low"]].shift(-1)
    has_next = d.groupby("day")["minute"].shift(-1).notna()
    up = (nxt["High"] - d["Close"])[has_next].to_numpy()
    down = (d["Close"] - nxt["Low"])[has_next].to_numpy()
    return up, down


def delta_grid(d: pd.DataFrame, n: int = 60) -> np.ndarray:
    up, down = excursions(d)
    top = np.nanquantile(np.r_[up, down], 0.99)
    return np.linspace(0.0, top, n)


def fill_curve(exc: np.ndarray, grid: np.ndarray) -> FillCurve:
    p = np.array([np.mean(exc >= x) for x in grid])   # NaN >= x is False
    lo, hi = FIT_P_BAND
    used = (p > lo) & (p < hi)
    lam = -np.log1p(-np.clip(p, 0, 1 - 1e-12))
    y = np.log(lam[used])
    slope, intercept = np.polyfit(grid[used], y, 1)
    resid = y - (intercept + slope * grid[used])
    r2 = 1 - resid @ resid / np.sum((y - y.mean()) ** 2)
    return FillCurve(grid, p, lam, used, float(np.exp(intercept)), float(-slope), float(r2))


def price_changes(d: pd.DataFrame) -> pd.Series:
    """One-minute mid-price changes, never across days."""
    return d.groupby("day")["Close"].diff().dropna()


def calibrate(d: pd.DataFrame, grid: np.ndarray | None = None):
    """Params plus the ask-side and bid-side fill curves.

    A and k average the two sides (the model uses one curve for both).
    """
    grid = delta_grid(d) if grid is None else grid
    up, down = excursions(d)
    ask, bid = fill_curve(up, grid), fill_curve(down, grid)
    sigma = float(price_changes(d).std())
    params = Params(sigma=sigma, A=(ask.A + bid.A) / 2, k=(ask.k + bid.k) / 2)
    return params, ask, bid


def calibrate_daily(d: pd.DataFrame, grid: np.ndarray) -> pd.DataFrame:
    """One calibration per day, for the stability figure."""
    rows = []
    for day, g in d.groupby("day"):
        p, ask, bid = calibrate(g, grid)
        rows.append(dict(day=day, sigma=p.sigma, A=p.A, k=p.k, r2=min(ask.r2, bid.r2)))
    return pd.DataFrame(rows).set_index("day")
