"""Checks that fail if the core logic breaks. Run: python -m pytest tests  (or python tests/test_asmm.py)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from asmm import calibration, model, replay, simulate  # noqa: E402
from asmm.config import T  # noqa: E402

P = model.Params(sigma=0.7, A=1.5, k=2.5)


def test_reservation_price_equals_mid_when_flat():
    assert model.reservation_price(100.0, 0, 200, 0.005, P) == 100.0


def test_quotes_skew_against_inventory():
    bid0, ask0 = model.as_quotes(100.0, 0, 200, 0.005, P)
    bid1, ask1 = model.as_quotes(100.0, 5, 200, 0.005, P)
    assert bid1 < bid0 and ask1 < ask0          # long -> both quotes move down


def test_fill_curve_recovers_known_A_k():
    # Draw excursions with P(exc >= delta) = 1 - exp(-A e^{-k delta}) exactly.
    rng = np.random.default_rng(0)
    u = rng.random(400_000)
    g0 = 1 - np.exp(-P.A)
    exc = np.full(u.size, -1.0)
    ok = u < g0
    exc[ok] = (np.log(P.A) - np.log(-np.log1p(-u[ok]))) / P.k
    fc = calibration.fill_curve(exc, np.linspace(0, 2, 40))
    assert abs(fc.A / P.A - 1) < 0.03 and abs(fc.k / P.k - 1) < 0.03 and fc.r2 > 0.99


def test_symmetric_inventory_variance_matches_skellam():
    # q_T is a difference of two Poisson counts: Var = 2 A e^{-k h} T.
    h = 0.6
    r = simulate.run(P, 0.005, "symmetric", half_spread=h, n=4000, dt=0.05)
    theory = 2 * P.A * np.exp(-P.k * h) * T
    assert abs(r.q_T.var() / theory - 1) < 0.08


def test_replay_pnl_decomposition_is_exact():
    rng = np.random.default_rng(1)
    close = 100 + np.cumsum(rng.normal(0, 0.5, T))
    g = pd.DataFrame({"Close": close, "High": close + rng.exponential(0.4, T),
                      "Low": close - rng.exponential(0.4, T)})
    r = replay.run_day(g, P, 0.005, "as")
    parts = r["capture"] + r["adverse"] + r["carry"]
    assert np.allclose(parts, r["pnl"])


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
