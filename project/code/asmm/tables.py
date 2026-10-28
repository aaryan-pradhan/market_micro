"""LaTeX tables and the numbers macro file, so no number in the report is typed by hand.

Tables go to report/tables/<name>.tex (booktabs rows only; the float and
caption live in the report). Scalars go to report/tables/numbers.tex as
\\newcommand macros, e.g. \\RELIANCEk -> the calibrated k for RELIANCE.
"""
import numpy as np

from . import model, pipeline, simulate
from .config import GAMMA, N_CALIB_DAYS, TAB_DIR, T, MC_PATHS


def _write(name: str, text: str):
    TAB_DIR.mkdir(parents=True, exist_ok=True)
    (TAB_DIR / f"{name}.tex").write_text(text)


def _rows(header: list[str], rows: list[list[str]], align: str) -> str:
    lines = [f"\\begin{{tabular}}{{{align}}}", "\\toprule",
             " & ".join(header) + r" \\", "\\midrule"]
    lines += [" & ".join(r) + r" \\" for r in rows]
    lines += ["\\bottomrule", "\\end{tabular}", ""]
    return "\n".join(lines)


def descriptive(res):
    keys = [("Trading days", "days", "{:.0f}"), ("Mean price (INR)", "price", "{:,.1f}"),
            ("Mean daily traded value (INR crore)", "inr_volume_cr", "{:,.2f}"),
            ("Minutes with no trade (\\%)", "no_trade_share", "{:.1%}"),
            ("$\\sigma$, one-minute price change (INR)", "sigma", "{:.3f}"),
            ("Mean one-minute high--low range (INR)", "range_mean", "{:.3f}"),
            ("Amihud ILLIQ ($|R|$ per INR crore)", "amihud", "{:.2e}"),
            ("Roll spread (INR)", "roll", "{:.3f}")]
    rows = [[lab] + [fmt.format(r.summary[k]).replace("%", "\\%") for r in res.values()] for lab, k, fmt in keys]
    _write("descriptive", _rows(["Statistic"] + list(res), rows, "l" + "r" * len(res)))


def calibration(res):
    rows = []
    for lab, f in [("$\\sigma$ (INR$/\\sqrt{\\text{min}}$)", lambda r: f"{r.params.sigma:.3f}"),
                   ("$A$ (fills per minute), ask / bid", lambda r: f"{r.ask_curve.A:.3f} / {r.bid_curve.A:.3f}"),
                   ("$k$ (per INR), ask / bid", lambda r: f"{r.ask_curve.k:.3f} / {r.bid_curve.k:.3f}"),
                   ("$A$ used (mean of sides)", lambda r: f"{r.params.A:.3f}"),
                   ("$k$ used (mean of sides)", lambda r: f"{r.params.k:.3f}"),
                   ("$R^2$ of log-linear fit, ask / bid", lambda r: f"{r.ask_curve.r2:.3f} / {r.bid_curve.r2:.3f}"),
                   ("Points in fit, ask / bid", lambda r: f"{r.ask_curve.used.sum()} / {r.bid_curve.used.sum()}")]:
        rows.append([lab] + [f(r) for r in res.values()])
    _write("calibration", _rows(["Parameter"] + list(res), rows, "l" + "r" * len(res)))


def scorecard(res):
    sc = {n: pipeline.assumption_scorecard(r) for n, r in res.items()}
    spec = [
        ("Fill intensity is $Ae^{-k\\delta}$", "min $R^2$", "fit_r2", "{:.3f}", "Holds"),
        ("One curve for both sides", "$k_{\\text{bid}}/k_{\\text{ask}}$", "k_ratio", "{:.2f}", "Holds"),
        ("Mid has no drift", "$t$-stat of mean change", "drift_t", "{:+.2f}", "Holds"),
        ("Independent increments", "lag-1 autocorrelation", "acf1", "{:+.3f}", "Bends (illiquid)"),
        ("Random-walk scaling", "VR(15)", "vr15", "{:.2f}", "Bends (illiquid)"),
        ("Gaussian increments", "excess kurtosis", "kurtosis", "{:.1f}", "Bends"),
        ("Constant $\\sigma$ through the day", "max/min 15-min $\\sigma$", "sigma_ratio", "{:.1f}", "Breaks"),
        ("Constant $k$ across days", "coef.\\ of variation of daily $k$", "k_cv", "{:.2f}", "Bends"),
    ]
    rows = [[a, m] + [fmt.format(sc[n][k]) for n in res] + [v] for a, m, k, fmt, v in spec]
    _write("scorecard", _rows(["Assumption", "Statistic"] + list(res) + ["Verdict"], rows, "ll" + "r" * len(res) + "l"))


def monte_carlo(res):
    rows = []
    for n, r in res.items():
        for key, mc in (("AS", r.mc_as), ("Symmetric", r.mc_sym)):
            rows.append([n, key, f"{mc.wealth.mean():.2f}", f"{mc.wealth.std():.2f}",
                         f"{simulate.certainty_equivalent(mc.wealth, GAMMA):.2f}",
                         f"{mc.q_T.var():.1f}", f"{mc.fills:.0f}", f"{mc.half_spread:.3f}"])
    _write("monte_carlo", _rows(["Stock", "Strategy", "Mean $W_T$", "S.d. $W_T$", "CE", "Var$(q_T)$",
                                 "Fills", "Half-spread"], rows, "llrrrrrr"))


def replay(res):
    rows = []
    for n, r in res.items():
        g = r.replay_test.groupby("strategy")
        for key, lab in (("as", "AS"), ("symmetric", "Symmetric")):
            x = g.get_group(key)
            rows.append([n, lab, f"{x.pnl.mean():+.1f}", f"{x.pnl.std():.1f}",
                         f"{x.capture.mean():+.1f}", f"{x.adverse.mean():+.1f}", f"{x.carry.mean():+.1f}",
                         f"{x.mean_abs_q.mean():.2f}", f"{x.max_abs_q.mean():.1f}", f"{x.fills.mean():.0f}"])
    _write("replay", _rows(["Stock", "Strategy", "PnL", "S.d.", "Capture", "Adverse", "Carry",
                            "Mean $|q|$", "Max $|q|$", "Fills"], rows, "llrrrrrrrr"))


def numbers(res):
    """Scalar macros cited in the text."""
    m = {"GammaRA": f"{GAMMA:g}", "Horizon": f"{T}", "CalibDays": f"{N_CALIB_DAYS}", "Paths": f"{MC_PATHS:,}"}
    for n, r in res.items():
        p = r.params
        sc = pipeline.assumption_scorecard(r)
        t = r.replay_test.groupby("strategy")
        a_all = r.replay_all.groupby("strategy")
        lo, hi = r.mc_ci
        m.update({
            f"{n}Days": f"{r.summary['days']}",
            f"{n}TestDays": f"{r.replay_test.day.nunique()}",
            f"{n}Sigma": f"{p.sigma:.3f}", f"{n}A": f"{p.A:.2f}", f"{n}k": f"{p.k:.2f}",
            f"{n}RTwo": f"{sc['fit_r2']:.3f}", f"{n}AcfOne": f"{sc['acf1']:+.3f}", f"{n}VRfifteen": f"{sc['vr15']:.2f}",
            f"{n}SigmaRatio": f"{sc['sigma_ratio']:.1f}", f"{n}Kurt": f"{sc['kurtosis']:.1f}",
            f"{n}Amihud": f"{r.summary['amihud']:.2e}", f"{n}Roll": f"{r.summary['roll']:.2f}",
            f"{n}NoTrade": f"{r.summary['no_trade_share'] * 100:.1f}",
            f"{n}VarqAS": f"{r.mc_as.q_T.var():.1f}", f"{n}VarqSym": f"{r.mc_sym.q_T.var():.1f}",
            f"{n}VarqFactor": f"{r.mc_sym.q_T.var() / r.mc_as.q_T.var():.0f}",
            f"{n}VarqTheory": f"{2 * p.A * np.exp(-p.k * r.mc_as.half_spread) * T:.1f}",
            f"{n}CEAS": f"{simulate.certainty_equivalent(r.mc_as.wealth, GAMMA):.1f}",
            f"{n}CESym": f"{simulate.certainty_equivalent(r.mc_sym.wealth, GAMMA):.1f}",
            f"{n}CEciLo": f"{lo:.1f}", f"{n}CEciHi": f"{hi:.1f}",
            f"{n}MeanAS": f"{r.mc_as.wealth.mean():.1f}", f"{n}MeanSym": f"{r.mc_sym.wealth.mean():.1f}",
            f"{n}HalfSpread": f"{r.mc_as.half_spread:.2f}",
            f"{n}ReplayPnlAS": f"{t.pnl.mean()['as']:+.1f}", f"{n}ReplayPnlSym": f"{t.pnl.mean()['symmetric']:+.1f}",
            f"{n}ReplaySdAS": f"{t.pnl.std()['as']:.1f}", f"{n}ReplaySdSym": f"{t.pnl.std()['symmetric']:.1f}",
            f"{n}ReplaySdFactor": f"{t.pnl.std()['symmetric'] / t.pnl.std()['as']:.1f}",
            f"{n}ReplayAbsqAS": f"{t.mean_abs_q.mean()['as']:.1f}",
            f"{n}ReplayAbsqSym": f"{t.mean_abs_q.mean()['symmetric']:.1f}",
            f"{n}CaptureAS": f"{t.capture.mean()['as']:+.1f}", f"{n}AdverseAS": f"{t.adverse.mean()['as']:+.1f}",
            f"{n}CarryAS": f"{t.carry.mean()['as']:+.1f}",
            f"{n}ReplayCEAS": f"{simulate.certainty_equivalent(t.get_group('as').pnl.to_numpy(), GAMMA):+.1f}",
            f"{n}ReplayCESym": f"{simulate.certainty_equivalent(t.get_group('symmetric').pnl.to_numpy(), GAMMA):+.1f}",
            f"{n}AllSdFactor": f"{a_all.pnl.std()['symmetric'] / a_all.pnl.std()['as']:.1f}",
            f"{n}AllPnlAS": f"{a_all.pnl.mean()['as']:+.1f}", f"{n}AllPnlSym": f"{a_all.pnl.mean()['symmetric']:+.1f}",
            f"{n}SpreadOpen": f"{model.optimal_spread(T, GAMMA, p):.2f}",
            f"{n}SpreadMid": f"{model.optimal_spread(T / 2, GAMMA, p):.2f}",
        })
    text = "% Generated by code/run_all.py. Do not edit.\n" + "".join(
        f"\\newcommand{{\\{k}}}{{{v}}}\n" for k, v in m.items())
    _write("numbers", text)


def make_all(res):
    for f in (descriptive, calibration, scorecard, monte_carlo, replay, numbers):
        f(res)
