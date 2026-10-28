"""Monte Carlo in the model's own world, with NSE-calibrated parameters.

Follows the base paper's design: arithmetic Brownian mid-price, Bernoulli
fills with probability lambda(delta) dt per step, and common random
numbers (both strategies see bit-identical draws), so differences come
from the quoting rule alone.
"""
from dataclasses import dataclass

import numpy as np

from .config import T, MC_PATHS, MC_DT, MC_SEED, BOOTSTRAP
from .model import Params, as_quotes, symmetric_quotes, fill_intensity


@dataclass
class MCResult:
    wealth: np.ndarray          # terminal wealth X_T + q_T S_T, per path
    q_T: np.ndarray             # terminal inventory, per path
    half_spread: float          # average quoted half-spread over time and paths
    fills: float                # average number of fills per path
    mean_abs_q: np.ndarray      # time-average |q| over the session, per path
    q_paths: np.ndarray         # inventory each minute, first `keep` paths  (keep, T+1)
    s_paths: np.ndarray         # mid-price each minute, first `keep` paths


def run(p: Params, gamma: float, strategy: str, half_spread: float | None = None,
        n: int = MC_PATHS, dt: float = MC_DT, seed: int = MC_SEED, keep: int = 60) -> MCResult:
    """Simulate one session of length T for `strategy` in {'as', 'symmetric'}."""
    rng = np.random.default_rng(seed)
    steps = int(round(T / dt))
    per_min = int(round(1 / dt))
    s = np.zeros(n)                       # mid relative to its start (prices enter only as differences)
    x = np.zeros(n)
    q = np.zeros(n)
    spread_sum, fills, abs_q = 0.0, np.zeros(n), np.zeros(n)
    q_paths = np.zeros((keep, T + 1))
    s_paths = np.zeros((keep, T + 1))

    for i in range(steps):
        tau = T - i * dt
        if strategy == "as":
            bid, ask = as_quotes(s, q, tau, gamma, p)
        else:
            bid, ask = symmetric_quotes(s, half_spread)
        spread_sum += np.mean(ask - bid) / 2

        # Draw order fixed for both strategies: normal, uniform (bid), uniform (ask).
        z = rng.standard_normal(n)
        u_bid = rng.random(n)
        u_ask = rng.random(n)
        hit_bid = u_bid < fill_intensity(s - bid, p) * dt
        hit_ask = u_ask < fill_intensity(ask - s, p) * dt
        q += hit_bid.astype(float) - hit_ask
        x += np.where(hit_ask, ask, 0.0) - np.where(hit_bid, bid, 0.0)
        fills += hit_bid + hit_ask
        abs_q += np.abs(q) * dt / T
        s = s + p.sigma * np.sqrt(dt) * z

        if (i + 1) % per_min == 0:
            m = (i + 1) // per_min
            q_paths[:, m] = q[:keep]
            s_paths[:, m] = s[:keep]

    return MCResult(x + q * s, q.copy(), spread_sum / steps, float(fills.mean()), abs_q, q_paths, s_paths)


def certainty_equivalent(w: np.ndarray, gamma: float) -> float:
    """CE = -(1/gamma) ln E[exp(-gamma W)], computed stably."""
    a = -gamma * w
    m = a.max()
    return -(m + np.log(np.mean(np.exp(a - m)))) / gamma


def ce_difference_ci(w_as: np.ndarray, w_sym: np.ndarray, gamma: float,
                     reps: int = BOOTSTRAP, seed: int = MC_SEED) -> tuple[float, float]:
    """Paired bootstrap 95% CI for CE(AS) - CE(symmetric)."""
    rng = np.random.default_rng(seed)
    n = len(w_as)
    diffs = np.empty(reps)
    for r in range(reps):
        idx = rng.integers(0, n, n)
        diffs[r] = certainty_equivalent(w_as[idx], gamma) - certainty_equivalent(w_sym[idx], gamma)
    return tuple(np.percentile(diffs, [2.5, 97.5]))


def compare(p: Params, gamma: float, **kw) -> tuple[MCResult, MCResult]:
    """AS first; the symmetric benchmark then quotes AS's realised average half-spread."""
    a = run(p, gamma, "as", **kw)
    s = run(p, gamma, "symmetric", half_spread=a.half_spread, **kw)
    return a, s
