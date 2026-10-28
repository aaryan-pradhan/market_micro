# Dataset

One-minute OHLCV bars for two NSE stocks, downloaded from Yahoo Finance with `code/fetch_data.py` on 28 Oct 2026.
Yahoo keeps only about 30 days of one-minute history, so **these files, not the script, are the dataset of record**.

| File | Stock | Role | Rows | Days |
|---|---|---|---|---|
| `RELIANCE_1m.csv` | Reliance Industries (`RELIANCE.NS`) | liquid | 6,858 | 19 |
| `KSCL_1m.csv` | Kaveri Seed Company (`KSCL.NS`) | illiquid | 6,524 | 19 |

Sample: 30 Sep 2026 – 28 Oct 2026, 09:15–15:29 IST as served by Yahoo.

## Columns

| Column | Meaning |
|---|---|
| `timestamp` | start of the minute, IST (`+05:30`) |
| `Open`, `High`, `Low`, `Close` | prices in INR |
| `Volume` | shares traded in the minute |

## Known quirks (handled in `code/asmm/data.py`)

- Yahoo omits 15:16–15:27 and prints a catch-up bar at 15:28. The study uses 09:15–15:14 (360 bars a day).
- A minute with no bar means no trade. The study carries the close forward and treats the minute as having no fill.
