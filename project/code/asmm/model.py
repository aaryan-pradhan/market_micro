"""Avellaneda-Stoikov (2008) closed-form quoting rules.

Units: time in minutes, prices in INR, inventory in shares,
sigma in INR/sqrt(min), k in 1/INR, A in fills/min, gamma in 1/INR.
"""
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Params:
    sigma: float    # mid-price volatility
    A: float        # fill intensity at zero distance
    k: float        # decay of fill intensity with distance


def fill_intensity(delta, p: Params):
    """lambda(delta) = A exp(-k delta)."""
    return p.A * np.exp(-p.k * delta)


def reservation_price(s, q, tau, gamma, p: Params):
    """r = s - q gamma sigma^2 tau, with tau = T - t the time left."""
    return s - q * gamma * p.sigma**2 * tau


def spread_components(tau, gamma, p: Params):
    """(inventory-risk term, market-making edge term) of the total optimal spread."""
    inventory = gamma * p.sigma**2 * tau
    edge = (2.0 / gamma) * np.log1p(gamma / p.k)
    return inventory, edge


def optimal_spread(tau, gamma, p: Params):
    """Total spread delta_a + delta_b = gamma sigma^2 tau + (2/gamma) ln(1 + gamma/k)."""
    inventory, edge = spread_components(tau, gamma, p)
    return inventory + edge


def as_quotes(s, q, tau, gamma, p: Params):
    """AS bid and ask, centred on the reservation price.

    Distances from the mid are floored at 0 so a quote never crosses the mid
    (the model's delta >= 0 constraint).
    """
    r = reservation_price(s, q, tau, gamma, p)
    half = optimal_spread(tau, gamma, p) / 2
    bid = np.minimum(r - half, s)
    ask = np.maximum(r + half, s)
    return bid, ask


def symmetric_quotes(s, half_spread):
    """Benchmark: fixed half-spread around the mid, blind to inventory."""
    return s - half_spread, s + half_spread
