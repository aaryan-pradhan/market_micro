"""One visual language for every figure in the report.

Print-first: white surface, Computer Modern text to match the LaTeX body,
hairline solid grid, thin marks, vector PDF. Colour carries one fixed role
per entity (validated for colour-vision deficiency with the dataviz checker):
strategies are blue/orange, stocks are violet/aqua, buys/sells green/red.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

from .config import FIG_DIR  # noqa: E402

# Roles
AS = "#2a78d6"
SYM = "#eb6834"
STOCK = {"RELIANCE": "#6250d6", "KSCL": "#1baf7a"}
BUY = "#008300"
SELL = "#e34948"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#8a8985"
GRID = "#e8e7e2"
GRID_LINE = "#dcdbd5"     # day separators, dumbbell connectors
AS_LIGHT = "#cfe0f6"
AS_DARK = "#174a8a"
DIVERGING = LinearSegmentedColormap.from_list("div", ["#2a78d6", "#f2f1ee", "#e34948"])

STRATEGY = {"as": ("Avellaneda-Stoikov", AS), "symmetric": ("Symmetric benchmark", SYM)}

FULL = 6.5      # \textwidth in inches (letter, 1 in margins)
HALF = 3.15


def apply():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["cmr10"],
        "mathtext.fontset": "cm",
        "axes.formatter.use_mathtext": True,
        "axes.unicode_minus": False,
        "font.size": 8.5,
        "axes.titlesize": 9,
        "axes.titlelocation": "left",
        "axes.labelsize": 8.5,
        "axes.labelcolor": INK2,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "xtick.color": INK2,
        "ytick.color": INK2,
        "legend.fontsize": 7.5,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#b9b8b2",
        "axes.linewidth": 0.6,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": GRID,
        "grid.linewidth": 0.5,
        "grid.linestyle": "-",
        "lines.linewidth": 1.4,
        "lines.solid_capstyle": "round",
        "patch.linewidth": 0,
        "figure.dpi": 150,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,
    })


def panel(ax, letter: str, title: str = ""):
    """'(a) Title' at the top-left of a panel."""
    ax.set_title(f"({letter}) {title}".rstrip(), color=INK, pad=6)


def label_end(ax, x, y, text, color, dx=4, dy=0, **kw):
    """Direct label at the end of a line, in ink colour (the mark carries the hue)."""
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points",
                va="center", ha="left", color=INK2, fontsize=7.5, **kw)
    ax.plot([x], [y], "o", ms=3, color=color, zorder=5)


def save(fig, name: str):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{name}.pdf")
    plt.close(fig)
