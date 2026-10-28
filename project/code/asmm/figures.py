"""Every figure in the report. One function per figure, named after its PDF.

Each function takes {stock name: StockResult} and writes report/figures/<name>.pdf.
Figures are grouped in the order the paper tells its story.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from scipy import stats

from . import model, pipeline
from .calibration import price_changes
from .config import GAMMA, N_CALIB_DAYS, STOCKS, T
from .style import (AS, AS_DARK, AS_LIGHT, BUY, DIVERGING, FULL, GRID_LINE, INK, INK2, MUTED,
                    SELL, STOCK, STRATEGY, SYM, label_end, panel, save)

LETTERS = "abcdefghij"


def _clock(ax, every=60):
    """Minute-of-session axis labelled as IST clock time."""
    ticks = np.arange(0, T + 1, every)
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{9 + (15 + m) // 60}:{(15 + m) % 60:02d}" for m in ticks])
    ax.set_xlim(0, T)


def _stock_legend(ax, res, loc="upper right"):
    ax.legend([Line2D([], [], color=STOCK[n], lw=1.6) for n in res],
              [STOCKS[n] for n in res], loc=loc)


def _strategy_legend(ax, loc="upper left", **kw):
    ax.legend([Line2D([], [], color=c, lw=1.6) for _, c in STRATEGY.values()],
              [lab for lab, _ in STRATEGY.values()], loc=loc, **kw)


def _legend_on_top(fig, handles, labels, top=0.9, ncol=None):
    """Lay out the panels, then put one shared legend in the band above them."""
    fig.tight_layout(rect=(0, 0, 1, top))
    fig.legend(handles, labels, loc="upper center", ncol=ncol or len(labels), bbox_to_anchor=(0.5, 1.0))


def _stock_handles(res):
    return [Line2D([], [], color=STOCK[n], lw=1.6) for n in res], [STOCKS[n] for n in res]


def _strategy_handles(kind="line"):
    if kind == "patch":
        return [Patch(color=c) for _, c in STRATEGY.values()], [lab for lab, _ in STRATEGY.values()]
    return [Line2D([], [], color=c, lw=1.6) for _, c in STRATEGY.values()], [lab for lab, _ in STRATEGY.values()]


# ---------------------------------------------------------------- 3. Data

def fig_price_paths(res):
    fig, axes = plt.subplots(len(res), 1, figsize=(FULL, 3.9), sharex=True)
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        y = r.bars["Close"].to_numpy()
        x = np.arange(len(y))
        days = r.bars["day"].unique()
        split = N_CALIB_DAYS * T
        ax.axvspan(0, split, color="#f3f2ee", lw=0, zorder=0)
        ax.plot(x, y, color=STOCK[n], lw=0.8)
        for j in range(1, len(days)):
            ax.axvline(j * T, color=GRID_LINE, lw=0.4, zorder=0)
        ax.set_ylabel("Price (INR)")
        ax.margins(x=0)
        panel(ax, LETTERS[i], STOCKS[n])
        ax.text(split / 2, 0.04, "calibration window", transform=ax.get_xaxis_transform(),
                ha="center", color=INK2, fontsize=7.5)
        ax.text((split + len(y)) / 2, 0.04, "out-of-sample test window",
                transform=ax.get_xaxis_transform(), ha="center", color=INK2, fontsize=7.5)
    ticks = np.arange(len(days)) * T + T / 2
    axes[-1].set_xticks(ticks[::2])
    axes[-1].set_xticklabels([d.strftime("%d %b") for d in days[::2]])
    axes[-1].grid(axis="x", visible=False)
    fig.align_ylabels()
    save(fig, "data_price_paths")



def fig_intraday_volume(res):
    fig, ax = plt.subplots(figsize=(FULL, 2.5))
    for n, r in res.items():
        v = r.volume_minute * 100
        ax.plot(v.index, v, color=STOCK[n], lw=0.4, alpha=0.35)
        smooth = v.rolling(9, center=True, min_periods=1).mean()
        ax.plot(smooth.index, smooth, color=STOCK[n], lw=1.6)
        label_end(ax, smooth.index[-1], smooth.iloc[-1], n, STOCK[n])
    ax.axhline(100 / T, color=MUTED, lw=0.8, ls="--")
    ax.text(T * 0.5, 100 / T, "uniform (1/360)", color=INK2, fontsize=7.5, va="bottom", ha="center")
    _clock(ax)
    ax.set_ylabel("Share of daily volume (%)")
    ax.set_ylim(bottom=0)
    _stock_legend(ax, res, loc="upper center")
    save(fig, "data_intraday_volume")


def fig_intraday_sigma(res):
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.5))
    for n, r in res.items():
        p = r.profile
        x = p.index + 7.5
        axes[0].plot(x, p["sigma"] / p["sigma"].mean(), "-o", ms=3, color=STOCK[n])
        axes[1].plot(x, p["traded"] * 100, "-o", ms=3, color=STOCK[n])
    axes[0].axhline(1, color=MUTED, lw=0.8, ls="--")
    axes[0].set_ylabel(r"$\sigma$ / session average")
    panel(axes[0], "a", r"Volatility by time of day (constant-$\sigma$ assumption)")
    axes[1].set_ylabel("Minutes with a trade (%)")
    panel(axes[1], "b", "Trading activity by time of day")
    for ax in axes:
        _clock(ax, 90)
    _legend_on_top(fig, *_stock_handles(res), top=0.88)
    save(fig, "data_intraday_sigma")


def fig_return_distribution(res):
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.6))
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        dp = price_changes(r.bars).to_numpy()
        tick = np.min(np.abs(dp[np.abs(dp) > 1e-9]))            # NSE price tick
        width = tick * max(1, round(np.std(dp) / tick / 3))    # whole ticks per bin, no aliasing
        lim = np.quantile(np.abs(dp), 0.999)
        edges = (np.arange(-np.ceil(lim / width), np.ceil(lim / width) + 1) + 0.5) * width
        ax.hist(dp, bins=edges, density=True, color=STOCK[n], alpha=0.8, rwidth=0.85)
        xs = np.linspace(-lim, lim, 400)
        ax.plot(xs, stats.norm.pdf(xs, dp.mean(), dp.std()), color=INK, lw=1.1)
        ax.set_yscale("log")
        ax.set_ylim(0.3 / (len(dp) * width), 3)
        ax.set_xlabel("One-minute price change (INR)")
        panel(ax, LETTERS[i], STOCKS[n])
        ax.text(0.98, 0.95, f"excess kurtosis {r.shape['excess_kurtosis']:.1f}",
                transform=ax.transAxes, ha="right", va="top", color=INK2, fontsize=7.5)
    axes[0].set_ylabel("Density (log scale)")
    _legend_on_top(fig, [Patch(color=MUTED), Line2D([], [], color=INK, lw=1.1)],
                   ["empirical (bins of whole ticks)", "normal with the same mean and s.d."], top=0.88)
    save(fig, "data_return_distribution")


def fig_qq(res):
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    for n, r in res.items():
        dp = price_changes(r.bars).to_numpy()
        z = np.sort((dp - dp.mean()) / dp.std())
        th = stats.norm.ppf((np.arange(1, len(z) + 1) - 0.5) / len(z))
        idx = np.unique(np.linspace(0, len(z) - 1, 1500).astype(int))
        ax.plot(th[idx], z[idx], "o", ms=2.2, color=STOCK[n], alpha=0.8, label=STOCKS[n])
    lim = 4.2
    ax.plot([-lim, lim], [-lim, lim], color=INK, lw=0.9)
    ax.set_xlim(-lim, lim)
    ax.set_xlabel("Normal quantile")
    ax.set_ylabel("Standardised price change")
    ax.legend(loc="upper left")
    save(fig, "data_qq")


def fig_autocorrelation(res):
    fig, ax = plt.subplots(figsize=(FULL, 2.4))
    width = 0.36
    for j, (n, r) in enumerate(res.items()):
        x = r.acf.index + (j - 0.5) * width
        ax.bar(x, r.acf.values, width=width * 0.92, color=STOCK[n], label=STOCKS[n])
    band = max(pipeline.acf_band(r) for r in res.values())
    ax.axhspan(-band, band, color="#efeee9", zorder=0)
    ax.axhline(0, color=INK2, lw=0.6)
    ax.set_xticks(range(1, 11))
    ax.set_xlabel("Lag (minutes)")
    ax.set_ylabel("Autocorrelation of price changes")
    ax.text(10.4, band, "95% band", color=INK2, fontsize=7, va="bottom", ha="right")
    ax.legend(loc="lower right")
    save(fig, "diag_autocorrelation")


def fig_variance_ratio(res):
    fig, ax = plt.subplots(figsize=(FULL, 2.4))
    for n, r in res.items():
        ax.plot(r.vr.index, r.vr.values, color=STOCK[n], lw=1.6)
        label_end(ax, r.vr.index[-1], r.vr.values[-1], f"{n}  VR(30) = {r.vr.values[-1]:.2f}", STOCK[n])
    ax.axhline(1, color=MUTED, lw=0.8, ls="--")
    ax.text(1.5, 1.0, "random walk", color=INK2, fontsize=7.5, va="bottom")
    ax.set_xlim(1, 38)
    ax.set_xlabel("Horizon $h$ (minutes)")
    ax.set_ylabel(r"Variance ratio $\mathrm{VR}(h)$")
    save(fig, "diag_variance_ratio")


def fig_liquidity(res):
    fig, axes = plt.subplots(1, 3, figsize=(FULL, 2.4))
    for n, r in res.items():
        days = np.arange(len(r.amihud))
        axes[0].plot(days, r.amihud.values, "-o", ms=2.5, color=STOCK[n])
        axes[1].plot(days, r.roll.values, "-o", ms=2.5, color=STOCK[n])
        nt = 1 - r.bars.groupby("day")["traded"].mean()
        axes[2].plot(days, nt.values * 100, "-o", ms=2.5, color=STOCK[n])
    axes[0].set_yscale("log")
    panel(axes[0], "a", "Amihud ILLIQ")
    axes[0].set_ylabel(r"$|R|$ per INR crore")
    panel(axes[1], "b", "Roll spread")
    axes[1].set_ylabel("INR")
    panel(axes[2], "c", "No-trade minutes")
    axes[2].set_ylabel("% of minutes")
    for ax in axes:
        ax.set_xlabel("Trading day")
    _legend_on_top(fig, *_stock_handles(res), top=0.86)
    save(fig, "data_liquidity")


# ---------------------------------------------------------------- 4. Calibration

def fig_fill_curves(res):
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.9), sharey=True)
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        for c, marker, face, side in ((r.ask_curve, "o", STOCK[n], "ask"), (r.bid_curve, "s", "white", "bid")):
            u = c.used
            ax.plot(c.delta[u], c.lam[u], marker, ms=3.4, mfc=face, mec=STOCK[n], mew=0.8, ls="none",
                    label=f"{side} side (data)")
            ax.plot(c.delta[~u & (c.lam > 0)], c.lam[~u & (c.lam > 0)], marker, ms=3, mfc="white",
                    mec=MUTED, mew=0.6, ls="none")
        p = r.params
        xs = np.linspace(0, r.ask_curve.delta.max(), 200)
        ax.plot(xs, model.fill_intensity(xs, p), color=INK, lw=1.1, label=r"fit $Ae^{-k\delta}$")
        ax.set_yscale("log")
        ax.set_xlabel(r"Quote distance from mid $\delta$ (INR)")
        panel(ax, LETTERS[i], STOCKS[n])
        r2 = min(r.ask_curve.r2, r.bid_curve.r2)
        ax.text(0.97, 0.95, f"$A$ = {p.A:.2f} / min\n$k$ = {p.k:.2f} / INR\n$R^2 \\geq$ {r2:.3f}",
                transform=ax.transAxes, ha="right", va="top", color=INK, fontsize=7.5, linespacing=1.4)
    axes[0].set_ylabel(r"Fill intensity $\lambda(\delta)$ per minute")
    axes[0].legend(loc="lower left")
    fig.tight_layout()
    save(fig, "calib_fill_curves")


def fig_fill_residuals(res):
    fig, ax = plt.subplots(figsize=(FULL, 2.2))
    for n, r in res.items():
        for c, marker, face in ((r.ask_curve, "o", STOCK[n]), (r.bid_curve, "s", "white")):
            u = c.used
            resid = np.log(c.lam[u]) - (np.log(c.A) - c.k * c.delta[u])
            ax.plot(c.delta[u], resid, marker, ms=3, mfc=face, mec=STOCK[n], mew=0.8, ls="-",
                    lw=0.6, color=STOCK[n])
    ax.axhline(0, color=INK2, lw=0.6)
    ax.set_xlabel(r"$\delta$ (INR)")
    ax.set_ylabel(r"$\ln\lambda$ residual")
    _stock_legend(ax, res, loc="upper center")
    save(fig, "calib_fill_residuals")


def fig_calibration_stability(res):
    fig, axes = plt.subplots(1, 3, figsize=(FULL, 2.4))
    keys = [("sigma", r"$\sigma$ (INR/$\sqrt{\mathrm{min}}$)"), ("A", r"$A$ (fills/min)"), ("k", r"$k$ (1/INR)")]
    for n, r in res.items():
        dp = r.daily_params
        x = np.arange(len(dp))
        for ax, (key, _) in zip(axes, keys):
            ax.plot(x, dp[key], "-o", ms=2.5, color=STOCK[n], lw=1)
            ax.axhline(getattr(r.params, key), color=STOCK[n], lw=0.8, ls="--", alpha=0.8)
    for i, (ax, (_, lab)) in enumerate(zip(axes, keys)):
        ax.axvspan(-0.5, N_CALIB_DAYS - 0.5, color="#f3f2ee", zorder=0)
        panel(ax, LETTERS[i], lab)
        ax.set_xlabel("Trading day")
    h, lab = _stock_handles(res)
    _legend_on_top(fig, h + [Line2D([], [], color=MUTED, ls="--", lw=0.8)],
                   lab + ["calibration-window estimate"], top=0.86)
    save(fig, "calib_stability")


# ---------------------------------------------------------------- 5. The model at NSE parameters

def fig_quotes_vs_inventory(res):
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.9), sharey=True)
    q = np.linspace(-5, 5, 201)
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        for tau, alpha, tag in ((T, 1.0, "09:15"), (T / 2, 0.45, "12:15")):
            bid, ask = model.as_quotes(0.0, q, tau, GAMMA, r.params)
            rp = model.reservation_price(0.0, q, tau, GAMMA, r.params)
            ax.fill_between(q, bid, ask, color=AS, alpha=0.12 * alpha, lw=0)
            ax.plot(q, ask, color=AS, alpha=alpha, lw=1.4)
            ax.plot(q, bid, color=AS, alpha=alpha, lw=1.4)
            ax.plot(q, rp, color=AS_DARK, alpha=alpha, lw=1.0, ls="--")
            ax.text(q[0] - 0.2, ask[0], f"ask {tag}", color=INK2, fontsize=7, va="center", ha="right")
            ax.text(q[-1] + 0.2, bid[-1], f"bid {tag}", color=INK2, fontsize=7, va="center", ha="left")
        ax.axhline(0, color=INK2, lw=0.6)
        ax.annotate("long: ask pinned at the mid\n(constraint $\\delta^a \\geq 0$)", (3.2, 0), xytext=(1.2, 2.6),
                    fontsize=7, color=INK2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
        ax.set_xlim(-7.6, 7.6)
        ax.set_xlabel("Inventory $q$ (shares)")
        panel(ax, LETTERS[i], STOCKS[n])
    axes[0].set_ylabel("Quote minus mid (INR)")
    axes[0].legend([Line2D([], [], color=AS), Line2D([], [], color=AS_DARK, ls="--", lw=1)],
                   ["bid / ask", "reservation price"], loc="lower left")
    fig.tight_layout()
    save(fig, "model_quotes_vs_inventory")


def fig_spread_decomposition(res):
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.6), sharey=True)
    t = np.arange(T + 1)
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        inv, edge = model.spread_components(T - t, GAMMA, r.params)
        edge = np.full_like(inv, edge)
        ax.fill_between(t, 0, edge, color=AS_LIGHT, lw=0, label="market-making edge  $(2/\\gamma)\\ln(1+\\gamma/k)$")
        ax.fill_between(t, edge, edge + inv, color=AS, alpha=0.85, lw=0,
                        label="inventory-risk premium  $\\gamma\\sigma^2(T-t)$")
        ax.axhline(r.roll.mean(), color=INK, lw=1, ls="--")
        ax.text(T - 5, r.roll.mean(), "market's Roll spread", ha="right", va="bottom", color=INK, fontsize=7)
        _clock(ax, 90)
        panel(ax, LETTERS[i], STOCKS[n])
    axes[0].set_ylabel("Optimal total spread (INR)")
    axes[0].legend(loc="upper right", fontsize=7)
    fig.tight_layout()
    save(fig, "model_spread_decomposition")


def fig_skew_heatmap(res):
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.7), sharey=True)
    t = np.arange(T + 1)
    q = np.arange(-15, 16)
    vmax = max(15 * GAMMA * r.params.sigma**2 * T for r in res.values())
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        tt, qq = np.meshgrid(t, q)
        skew = model.reservation_price(0.0, qq, T - tt, GAMMA, r.params)
        im = ax.pcolormesh(t, q, skew, cmap=DIVERGING, vmin=-vmax, vmax=vmax, shading="auto", rasterized=True)
        ax.contour(t, q, skew, levels=[-2, -1, -0.5, 0.5, 1, 2], colors=INK, linewidths=0.4)
        _clock(ax, 90)
        ax.grid(False)
        ax.set_xlabel("Time of day")
        panel(ax, LETTERS[i], STOCKS[n])
    axes[0].set_ylabel("Inventory $q$")
    cb = fig.colorbar(im, ax=axes, shrink=0.9, pad=0.02)
    cb.set_label("Reservation price minus mid (INR)")
    cb.outline.set_visible(False)
    save(fig, "model_skew_heatmap")


# ---------------------------------------------------------------- 6. Monte Carlo

def fig_mc_inventory_paths(res):
    fig, axes = plt.subplots(len(res), 2, figsize=(FULL, 4.2), sharex=True, sharey=True)
    minutes = np.arange(T + 1)
    for i, (n, r) in enumerate(res.items()):
        for j, (key, mc) in enumerate((("as", r.mc_as), ("symmetric", r.mc_sym))):
            ax = axes[i, j]
            lab, col = STRATEGY[key]
            ax.plot(minutes, mc.q_paths[:40].T, color=col, lw=0.45, alpha=0.45, rasterized=True)
            lo, hi = np.percentile(mc.q_paths, [5, 95], axis=0)
            ax.plot(minutes, lo, color=col, lw=1.2)
            ax.plot(minutes, hi, color=col, lw=1.2)
            ax.axhline(0, color=INK2, lw=0.6)
            panel(ax, LETTERS[2 * i + j], f"{n}: {lab}")
            _clock(ax, 120)
        axes[i, 0].set_ylabel("Inventory $q$")
    fig.tight_layout()
    save(fig, "mc_inventory_paths")


def fig_mc_terminal(res):
    fig, axes = plt.subplots(2, len(res), figsize=(FULL, 4.2))
    for j, (n, r) in enumerate(res.items()):
        ax = axes[0, j]
        lim = int(np.percentile(np.abs(r.mc_sym.q_T), 99.5)) + 1
        bins = np.arange(-lim, lim + 2) - 0.5
        ax.hist(r.mc_sym.q_T, bins=bins, color=SYM, alpha=0.55, density=True)
        ax.hist(r.mc_as.q_T, bins=bins, color=AS, alpha=0.75, density=True)
        ax.set_xlabel("Terminal inventory $q_T$")
        panel(ax, LETTERS[j], f"{n}: terminal inventory")
        ax.text(0.97, 0.95, f"Var: AS {r.mc_as.q_T.var():.1f}\n       sym {r.mc_sym.q_T.var():.1f}",
                transform=ax.transAxes, ha="right", va="top", fontsize=7.5, color=INK)

        ax = axes[1, j]
        w = np.r_[r.mc_as.wealth, r.mc_sym.wealth]
        bins = np.linspace(*np.percentile(w, [0.5, 99.5]), 70)
        ax.hist(r.mc_sym.wealth, bins=bins, color=SYM, alpha=0.55, density=True)
        ax.hist(r.mc_as.wealth, bins=bins, color=AS, alpha=0.75, density=True)
        ax.set_xlabel("Terminal wealth $W_T$ (INR)")
        panel(ax, LETTERS[2 + j], f"{n}: terminal wealth")
    axes[0, 0].set_ylabel("Density")
    axes[1, 0].set_ylabel("Density")
    _legend_on_top(fig, *_strategy_handles("patch"), top=0.93)
    save(fig, "mc_terminal_distributions")


def fig_mc_gamma(res):
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.6))
    for n, r in res.items():
        s = r.sweep
        axes[0].plot(s.index, s.ce_as - s.ce_sym, "-o", ms=3, color=STOCK[n])
        axes[1].plot(s.index, s.varq_sym / s.varq_as, "-o", ms=3, color=STOCK[n])
    axes[0].axhline(0, color=INK2, lw=0.6)
    panel(axes[0], "a", "Certainty-equivalent gain of AS (INR)")
    panel(axes[1], "b", r"Var($q_T$) reduction factor, sym / AS")
    for ax in axes:
        ax.set_xscale("log")
        ax.axvline(GAMMA, color=MUTED, lw=0.8, ls="--")
        ax.set_xlabel(r"Risk aversion $\gamma$ (1/INR)")
    axes[1].set_yscale("log")
    h, lab = _stock_handles(res)
    _legend_on_top(fig, h + [Line2D([], [], color=MUTED, ls="--", lw=0.8)], lab + [r"headline $\gamma$"], top=0.86)
    save(fig, "mc_gamma_sensitivity")


def fig_mc_frontier(res):
    fig, ax = plt.subplots(figsize=(FULL, 2.8))
    for n, r in res.items():
        s = r.sweep
        ax.plot(s.std_as, s.mean_as, "-o", ms=3.5, color=STOCK[n], label=f"{n}: AS across $\\gamma$")
        ax.plot(s.std_sym, s.mean_sym, "s", ms=4, mfc="white", mec=STOCK[n], ls=":", color=STOCK[n],
                label=f"{n}: symmetric at the same spread")
        for g in ((s.index[0], s.index[-1]) if n == list(res)[0] else ()):
            ax.annotate(f"$\\gamma$={g:g}", (s.std_as[g], s.mean_as[g]), xytext=(5, 4),
                        textcoords="offset points", fontsize=7, color=INK2)
    ax.set_xscale("log")
    ax.set_xlabel("Standard deviation of terminal wealth (INR, log scale)")
    ax.set_ylabel("Mean terminal wealth (INR)")
    handles, labels = ax.get_legend_handles_labels()
    _legend_on_top(fig, handles, labels, top=0.82, ncol=2)
    save(fig, "mc_frontier")


# ---------------------------------------------------------------- 7. Historical replay

def fig_replay_day(res, n, zoom=40):
    """One test day in four views: the day, a zoom on the quotes, inventory, PnL."""
    r = res[n]
    day = pipeline.hero_day(r)
    a, s = r.replay_paths["as"][day], r.replay_paths["symmetric"][day]
    t = np.arange(len(a))
    peak = int(np.argmax(a["q"].abs().to_numpy()))           # zoom where AS skews hardest
    z0 = int(np.clip(peak - zoom // 2, 0, len(a) - zoom))
    z = slice(z0, z0 + zoom)

    fig = plt.figure(figsize=(FULL, 6.6))
    gs = fig.add_gridspec(4, 1, height_ratios=[1.7, 1.7, 1.1, 1.1], hspace=0.55)
    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])
    ax2 = fig.add_subplot(gs[2], sharex=ax0)
    ax3 = fig.add_subplot(gs[3], sharex=ax0)

    ax0.plot(t, a["mid"], color=INK, lw=0.8)
    ax0.plot(t[a["buy"]], a["mid"][a["buy"]], "^", ms=2.6, color=BUY, alpha=0.8)
    ax0.plot(t[a["sell"]], a["mid"][a["sell"]], "v", ms=2.6, color=SELL, alpha=0.8)
    ax0.axvspan(z0, z0 + zoom, color=AS, alpha=0.08, lw=0)
    ax0.set_ylabel("INR")
    ax0.legend([Line2D([], [], color=INK, lw=0.8),
                Line2D([], [], marker="^", color=BUY, ls="none", ms=4),
                Line2D([], [], marker="v", color=SELL, ls="none", ms=4)],
               ["mid (close)", "AS buys (bid filled)", "AS sells (ask filled)"], loc="best", ncol=3, fontsize=7)
    panel(ax0, "a", f"{STOCKS[n]}, {day:%d %b %Y}: the whole session (shaded: zoom below)")
    _clock(ax0)

    tz = t[z]
    ax1.fill_between(tz, a["bid"][z], a["ask"][z], color=AS, alpha=0.14, lw=0, step="post")
    ax1.step(tz, a["ask"][z], where="post", color=AS, lw=1.0, label="AS ask / bid")
    ax1.step(tz, a["bid"][z], where="post", color=AS, lw=1.0)
    ax1.step(tz, a["reservation"][z], where="post", color=AS_DARK, lw=1.0, ls="--", label="reservation price")
    ax1.plot(tz, a["mid"][z], "-o", color=INK, lw=0.8, ms=2, label="mid")
    b, sl = a["buy"].to_numpy()[z], a["sell"].to_numpy()[z]
    ax1.plot(tz[b], a["bid"].shift(1)[z][b], "^", ms=5, color=BUY)
    ax1.plot(tz[sl], a["ask"].shift(1)[z][sl], "v", ms=5, color=SELL)
    ax1.set_xlim(tz[0], tz[-1])
    ax1.set_xticks(tz[::10])
    ax1.set_xticklabels([f"{9 + (15 + m) // 60}:{(15 + m) % 60:02d}" for m in tz[::10]])
    ax1.set_ylabel("INR")
    lo_, hi_ = np.nanmin(a["bid"][z]), np.nanmax(a["ask"][z])
    ax1.set_ylim(lo_ - 0.45 * (hi_ - lo_), hi_ + 0.05 * (hi_ - lo_))
    ax1.legend(loc="lower center", ncol=3, fontsize=7)
    panel(ax1, "b", f"Zoom: {zoom} minutes of AS quotes; markers show fills at the quoted price")

    for key, frame in (("symmetric", s), ("as", a)):
        ax2.step(t, frame["q"], where="post", color=STRATEGY[key][1], lw=1.1)
        ax3.plot(t, frame["pnl"], color=STRATEGY[key][1], lw=1.1)
        label_end(ax3, t[-1], frame["pnl"].iloc[-1], f"{frame['pnl'].iloc[-1]:+.0f}", STRATEGY[key][1])
    for ax in (ax2, ax3):
        ax.axhline(0, color=INK2, lw=0.6)
    ax2.set_ylabel("$q$")
    panel(ax2, "c", "Inventory")
    _strategy_legend(ax2, loc="lower right", bbox_to_anchor=(1, 1), ncol=2, fontsize=7)
    ax3.set_ylabel("INR")
    panel(ax3, "d", "Marked-to-market PnL")
    _clock(ax3)
    fig.align_ylabels()
    save(fig, f"replay_day_{n.lower()}")


def fig_replay_inventory(res):
    fig, axes = plt.subplots(len(res), 2, figsize=(FULL, 4.2), sharex=True, sharey="row")
    for i, (n, r) in enumerate(res.items()):
        for j, key in enumerate(("as", "symmetric")):
            ax = axes[i, j]
            lab, col = STRATEGY[key]
            for frame in r.replay_paths[key].values():
                ax.step(np.arange(len(frame)), frame["q"], where="post", color=col, lw=0.8, alpha=0.6)
            ax.axhline(0, color=INK2, lw=0.6)
            panel(ax, LETTERS[2 * i + j], f"{n}: {lab}, every test day")
            _clock(ax, 120)
        axes[i, 0].set_ylabel("Inventory $q$")
    fig.tight_layout()
    save(fig, "replay_inventory_paths")


def fig_replay_daily_pnl(res):
    fig, axes = plt.subplots(1, len(res), figsize=(FULL, 2.9), sharey=False)
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        t = r.replay_test.pivot(index="day", columns="strategy", values="pnl")
        y = np.arange(len(t))[::-1]
        ax.hlines(y, t["as"], t["symmetric"], color=GRID_LINE, lw=2)
        ax.plot(t["symmetric"], y, "o", ms=5, color=SYM)
        ax.plot(t["as"], y, "o", ms=5, color=AS)
        ax.axvline(0, color=INK2, lw=0.6)
        ax.set_yticks(y)
        ax.set_yticklabels([d.strftime("%d %b") for d in t.index])
        ax.grid(axis="y", visible=False)
        ax.set_xlabel("Daily PnL (INR)")
        panel(ax, LETTERS[i], STOCKS[n])
    _legend_on_top(fig, [Line2D([], [], marker="o", color=c, ls="none") for _, c in STRATEGY.values()],
                   [lab for lab, _ in STRATEGY.values()], top=0.9)
    save(fig, "replay_daily_pnl")


def fig_pnl_decomposition(res):
    parts = [("capture", "Spread\ncapture"), ("adverse", "Adverse\nselection"),
             ("carry", "Inventory\ncarry"), ("pnl", "Total\nPnL")]
    fig, axes = plt.subplots(1, len(res), figsize=(FULL, 2.8), sharey=True)
    for i, (ax, (n, r)) in enumerate(zip(axes, res.items())):
        m = r.replay_test.groupby("strategy")[[p for p, _ in parts]].mean()
        se = r.replay_test.groupby("strategy")[[p for p, _ in parts]].sem()
        x = np.arange(len(parts))
        for j, key in enumerate(("as", "symmetric")):
            col = STRATEGY[key][1]
            ax.bar(x + (j - 0.5) * 0.38, m.loc[key], width=0.36, color=col,
                   yerr=se.loc[key], error_kw=dict(ecolor=INK2, lw=0.7, capsize=2))
        ax.axhline(0, color=INK2, lw=0.6)
        ax.set_xticks(x)
        ax.set_xticklabels([lab for _, lab in parts], fontsize=7.5)
        ax.grid(axis="x", visible=False)
        panel(ax, LETTERS[i], STOCKS[n])
    axes[0].set_ylabel("INR per day (mean $\\pm$ s.e.)")
    _legend_on_top(fig, *_strategy_handles("patch"), top=0.9)
    save(fig, "replay_pnl_decomposition")


def fig_model_vs_reality(res):
    """Risk reduction factor (symmetric / AS) in the model world vs on real data."""
    rows = []
    for n, r in res.items():
        t = r.replay_test.groupby("strategy")
        abs_qT = t["q_T"].apply(lambda v: v.abs().mean())
        rows += [
            (n, "s.d. of PnL", r.mc_sym.wealth.std() / r.mc_as.wealth.std(),
             t["pnl"].std()["symmetric"] / t["pnl"].std()["as"]),
            (n, "mean $|q|$ during the day", r.mc_sym.mean_abs_q.mean() / r.mc_as.mean_abs_q.mean(),
             t["mean_abs_q"].mean()["symmetric"] / t["mean_abs_q"].mean()["as"]),
            (n, "mean $|q_T|$ at the close", np.abs(r.mc_sym.q_T).mean() / np.abs(r.mc_as.q_T).mean(),
             abs_qT["symmetric"] / abs_qT["as"]),
        ]
    fig, ax = plt.subplots(figsize=(FULL, 2.6))
    y = np.arange(len(rows))[::-1]
    for yi, (n, metric, mc, real) in zip(y, rows):
        ax.hlines(yi, min(mc, real), max(mc, real), color=GRID_LINE, lw=2)
        ax.plot(mc, yi, "D", ms=5, mfc="white", mec=STOCK[n], mew=1.2)
        ax.plot(real, yi, "o", ms=6, color=STOCK[n])
    ax.axvline(1, color=INK2, lw=0.8)
    ax.set_xscale("log")
    ax.set_xlim(0.8, 25)
    ax.set_xticks([1, 2, 3, 5, 10, 20])
    ax.set_xticklabels(["1 (no gain)", "2", "3", "5", "10", "20"])
    ax.minorticks_off()
    ax.set_yticks(y)
    ax.set_yticklabels([f"{n}: {m}" for n, m, *_ in rows], fontsize=7.5)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("Risk reduction factor: symmetric / AS (log scale)")
    ax.legend([Line2D([], [], marker="D", mfc="white", mec=INK2, ls="none"),
               Line2D([], [], marker="o", color=INK2, ls="none")],
              ["model world (Monte Carlo)", "real NSE minutes (replay)"],
              loc="center left", bbox_to_anchor=(0.08, 0.5))
    save(fig, "summary_model_vs_reality")


def fig_market_vs_model_spread(res):
    fig, ax = plt.subplots(figsize=(FULL, 2.6))
    names = list(res)
    x = np.arange(len(names))
    w = 0.2
    series = [
        ("Roll (1984) effective spread", lambda r: r.roll.mean(), "#b9b8b2"),
        ("Mean one-minute high-low range", lambda r: r.summary["range_mean"], MUTED),
        ("AS optimal spread, 12:15", lambda r: model.optimal_spread(T / 2, GAMMA, r.params), AS),
        ("AS optimal spread, 09:15", lambda r: model.optimal_spread(T, GAMMA, r.params), AS_DARK),
    ]
    for j, (lab, f, col) in enumerate(series):
        vals = [f(res[n]) for n in names]
        bars = ax.bar(x + (j - 1.5) * w, vals, width=w * 0.92, color=col, label=lab)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.2f}", ha="center", va="bottom", fontsize=7, color=INK2)
    ax.set_xticks(x)
    ax.set_xticklabels([STOCKS[n] for n in names])
    ax.grid(axis="x", visible=False)
    ax.set_ylabel("Spread (INR)")
    ax.legend(loc="upper left", fontsize=7)
    save(fig, "summary_market_vs_model_spread")


ALL = [fig_price_paths, fig_intraday_volume, fig_intraday_sigma, fig_return_distribution, fig_qq,
       fig_autocorrelation, fig_variance_ratio, fig_liquidity,
       fig_fill_curves, fig_fill_residuals, fig_calibration_stability,
       fig_quotes_vs_inventory, fig_spread_decomposition, fig_skew_heatmap,
       fig_mc_inventory_paths, fig_mc_terminal, fig_mc_gamma, fig_mc_frontier,
       fig_replay_inventory, fig_replay_daily_pnl, fig_pnl_decomposition,
       fig_model_vs_reality, fig_market_vs_model_spread]


def make_all(res):
    for f in ALL:
        f(res)
    for n in res:
        fig_replay_day(res, n)
