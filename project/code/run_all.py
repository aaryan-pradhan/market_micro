"""Rebuild every figure, table and number in the report.

    python run_all.py            compute everything (a few minutes), then write outputs
    python run_all.py --cached   reuse the last computation, only redraw figures and tables
"""
import pickle
import sys
import time
from pathlib import Path

from asmm import figures, pipeline, style, tables
from asmm.config import STOCKS

CACHE = Path(__file__).resolve().parent / ".cache" / "results.pkl"


def compute():
    res = {}
    for name in STOCKS:
        t0 = time.time()
        res[name] = pipeline.run(name)
        print(f"{name}: computed in {time.time() - t0:.0f}s")
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_bytes(pickle.dumps(res))
    return res


def main():
    res = pickle.loads(CACHE.read_bytes()) if "--cached" in sys.argv and CACHE.exists() else compute()
    style.apply()
    figures.make_all(res)
    tables.make_all(res)
    print("figures and tables written to report/")


if __name__ == "__main__":
    main()
