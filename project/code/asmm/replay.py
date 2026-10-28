"""Historical replay: run a quoting rule over real NSE minutes.

At the end of minute t the dealer sees close_t (the mid proxy) and posts a
bid and an ask for minute t+1. The ask sells one share if minute t+1's high
reaches it; the bid buys one share if its low reaches it. Any inventory
left at the end of the session is marked at the final close.

PnL splits exactly into three parts (per minute, summed over the day):
  spread capture   = sell (ask - s_t) + buy (s_t - bid)       edge earned vs the mid when quoting
  adverse selection= (buy - sell) (s_{t+1} - s_t)             the mid moving against a fresh fill
  inventory carry  = q_t (s_{t+1} - s_t)                      price risk on the position already held
"""
import numpy as np
import pandas as pd

from .config import T
from .model import Params, as_quotes, symmetric_quotes, reservation_price


def run_day(g: pd.DataFrame, p: Params, gamma: float, strategy: str,
            half_spread: float | None = None) -> pd.DataFrame:
    """Minute-by-minute record for one day: mid, quotes, fills, inventory, cash, PnL."""
    s = g["Close"].to_numpy()
    hi = g["High"].to_numpy()
    lo = g["Low"].to_numpy()
    n = len(s)
    q = np.zeros(n)
    x = np.zeros(n)
    bid = np.full(n, np.nan)
    ask = np.full(n, np.nan)
    r = np.full(n, np.nan)
    buy = np.zeros(n, bool)
    sell = np.zeros(n, bool)
    capture = np.zeros(n)
    adverse = np.zeros(n)
    carry = np.zeros(n)

    for t in range(n - 1):
        tau = T - t
        if strategy == "as":
            bid[t], ask[t] = as_quotes(s[t], q[t], tau, gamma, p)
            r[t] = reservation_price(s[t], q[t], tau, gamma, p)
        else:
            bid[t], ask[t] = symmetric_quotes(s[t], half_spread)
            r[t] = s[t]
        buy[t + 1] = lo[t + 1] <= bid[t]          # NaN (no trade) compares False
        sell[t + 1] = hi[t + 1] >= ask[t]
        q[t + 1] = q[t] + buy[t + 1] - sell[t + 1]
        x[t + 1] = x[t] - buy[t + 1] * bid[t] + sell[t + 1] * ask[t]
        move = s[t + 1] - s[t]
        capture[t + 1] = sell[t + 1] * (ask[t] - s[t]) + buy[t + 1] * (s[t] - bid[t])
        adverse[t + 1] = (int(buy[t + 1]) - int(sell[t + 1])) * move
        carry[t + 1] = q[t] * move

    return pd.DataFrame({
        "mid": s, "bid": bid, "ask": ask, "reservation": r,
        "buy": buy, "sell": sell, "q": q, "cash": x, "pnl": x + q * s,
        "capture": capture.cumsum(), "adverse": adverse.cumsum(), "carry": carry.cumsum(),
    }, index=g.index)


def run_days(d: pd.DataFrame, p: Params, gamma: float) -> dict[str, dict]:
    """Replay every day for AS and the symmetric benchmark.

    The benchmark's half-spread is AS's average quoted half-spread on the
    same day, so the two differ only in where the quotes sit, not how wide.
    """
    out = {"as": {}, "symmetric": {}}
    for day, g in d.groupby("day"):
        a = run_day(g, p, gamma, "as")
        h = float(np.nanmean(a["ask"] - a["bid"]) / 2)
        out["as"][day] = a
        out["symmetric"][day] = run_day(g, p, gamma, "symmetric", half_spread=h)
    return out


def day_summary(paths: dict[str, dict]) -> pd.DataFrame:
    """One row per (strategy, day): final PnL, terminal and peak inventory, fills, spread."""
    rows = []
    for strategy, days in paths.items():
        for day, r in days.items():
            rows.append(dict(
                strategy=strategy, day=day,
                pnl=r["pnl"].iloc[-1],
                capture=r["capture"].iloc[-1],
                adverse=r["adverse"].iloc[-1],
                carry=r["carry"].iloc[-1],
                q_T=r["q"].iloc[-1],
                max_abs_q=r["q"].abs().max(),
                mean_abs_q=r["q"].abs().mean(),
                fills=int(r["buy"].sum() + r["sell"].sum()),
                half_spread=float(np.nanmean(r["ask"] - r["bid"]) / 2),
            ))
    return pd.DataFrame(rows)
