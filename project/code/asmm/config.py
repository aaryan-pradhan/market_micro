"""Every constant the study depends on, in one place."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # project/
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "report" / "figures"
TAB_DIR = ROOT / "report" / "tables"

# Stocks: file stem -> label used in figures and tables.
STOCKS = {"RELIANCE": "RELIANCE (liquid)", "KSCL": "KSCL (illiquid)"}

# Session. Yahoo drops the 15:16-15:27 bars and prints a catch-up bar at 15:28,
# so the study uses the clean 09:15-15:14 window: T = 360 one-minute bars.
SESSION_START = "09:15"
SESSION_END = "15:14"
T = 360                     # minutes per session (the model's horizon)

N_CALIB_DAYS = 10           # first 10 days calibrate, the rest are the out-of-sample test

# Risk aversion (1/INR). GAMMA is the headline value, GAMMAS the sensitivity sweep.
GAMMA = 0.005
GAMMAS = [0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05]

# Fill-curve fit: use quote distances whose fill probability lies in this band.
FIT_P_BAND = (0.02, 0.98)

# Monte Carlo (the base paper's design: Bernoulli fills, common random numbers).
MC_PATHS = 10_000
MC_DT = 0.02                # minutes per step, keeps lambda*dt small (< 0.04)
MC_SEED = 2026
BOOTSTRAP = 2_000
