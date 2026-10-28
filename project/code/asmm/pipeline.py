"""Compute every result the report uses, once, for one stock."""
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from . import calibration, data, diagnostics, replay, simulate
from .config import GAMMA, GAMMAS
from .model import Params


@dataclass
class StockResult:
    name: str
    bars: pd.DataFrame
    calib: pd.DataFrame
    test: pd.DataFrame
    # calibration (on calibration days)
    params: Params
    ask_curve: calibration.FillCurve
    bid_curve: calibration.FillCurve
    daily_params: pd.DataFrame
    # assumption diagnostics and liquidity (all days)
    acf: pd.Series
    vr: pd.Series
    shape: dict
    profile: pd.DataFrame
    volume_minute: pd.Series
    amihud: pd.Series
    roll: pd.Series
    summary: dict
    # model world
    mc_as: simulate.MCResult
    mc_sym: simulate.MCResult
    mc_ci: tuple
    sweep: pd.DataFrame
    # real world
    replay_paths: dict
    replay_test: pd.DataFrame          # out-of-sample days
    replay_all: pd.DataFrame           # every day, robustness
    extra: dict = field(default_factory=dict)


def gamma_sweep(p: Params, n: int = 2_000) -> pd.DataFrame:
    rows = []
    for g in GAMMAS:
        a, s = simulate.compare(p, g, n=n)
        rows.append(dict(
            gamma=g,
            ce_as=simulate.certainty_equivalent(a.wealth, g),
            ce_sym=simulate.certainty_equivalent(s.wealth, g),
            mean_as=a.wealth.mean(), mean_sym=s.wealth.mean(),
            std_as=a.wealth.std(), std_sym=s.wealth.std(),
            varq_as=a.q_T.var(), varq_sym=s.q_T.var(),
            half_spread=a.half_spread,
        ))
    return pd.DataFrame(rows).set_index("gamma")


def run(name: str) -> StockResult:
    bars = data.load(name)
    calib, test = data.split(bars)
    params, ask, bid = calibration.calibrate(calib)
    daily = calibration.calibrate_daily(bars, ask.delta)

    mc_as, mc_sym = simulate.compare(params, GAMMA)
    ci = simulate.ce_difference_ci(mc_as.wealth, mc_sym.wealth, GAMMA)

    paths_test = replay.run_days(test, params, GAMMA)
    paths_all = replay.run_days(bars, params, GAMMA)

    return StockResult(
        name=name, bars=bars, calib=calib, test=test,
        params=params, ask_curve=ask, bid_curve=bid, daily_params=daily,
        acf=diagnostics.autocorrelation(bars),
        vr=diagnostics.variance_ratio(bars),
        shape=diagnostics.return_shape(bars),
        profile=diagnostics.intraday_profile(bars),
        volume_minute=diagnostics.volume_by_minute(bars),
        amihud=diagnostics.amihud_daily(bars),
        roll=diagnostics.roll_spread_daily(bars),
        summary=diagnostics.summary(bars),
        mc_as=mc_as, mc_sym=mc_sym, mc_ci=ci,
        sweep=gamma_sweep(params),
        replay_paths=paths_test,
        replay_test=replay.day_summary(paths_test),
        replay_all=replay.day_summary(paths_all),
    )


def hero_day(r: StockResult):
    """Test day where the symmetric dealer's inventory strays furthest (the clearest contrast)."""
    t = r.replay_test
    return t[t.strategy == "symmetric"].sort_values("max_abs_q").iloc[-1]["day"]


def assumption_scorecard(r: StockResult) -> dict:
    """The numbers behind the holds / bends / breaks verdicts."""
    sig = r.profile["sigma"]
    return dict(
        fit_r2=min(r.ask_curve.r2, r.bid_curve.r2),
        k_ratio=r.bid_curve.k / r.ask_curve.k,
        A_ratio=r.bid_curve.A / r.ask_curve.A,
        acf1=r.acf.loc[1],
        vr15=r.vr.loc[15],
        drift_t=r.shape["drift_t"],
        kurtosis=r.shape["excess_kurtosis"],
        sigma_ratio=sig.max() / sig.min(),
        k_cv=r.daily_params["k"].std() / r.daily_params["k"].mean(),
    )


def acf_band(r: StockResult) -> float:
    n = len(calibration.price_changes(r.bars))
    return 1.96 / np.sqrt(n)
