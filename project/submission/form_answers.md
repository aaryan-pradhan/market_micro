# Project submission — Google Form answers

Deadline: **30 Oct 2026, end of day**. Copy each field below into the form.

## Title of the report

Does Optimal Market Making Survive the National Stock Exchange? Calibrating and Testing the Avellaneda–Stoikov Model on Indian Equities

## Names of the students

- Aaryan Pradhan (22CH3FP25)
- Suhani Kumari (22CH3FP16)
- Md Arsh Ansari (22CH3FP20)

## Brief summary of the report

We test whether the Avellaneda–Stoikov (2008) optimal market-making model works on Indian data. Using 19 days of NSE one-minute bars for a liquid stock (RELIANCE) and an illiquid one (KSCL), we check each assumption of the model, calibrate its volatility and fill-intensity parameters, and run the optimal quotes in a 10,000-path Monte Carlo and in an out-of-sample replay on real minutes against a symmetric dealer quoting the same average spread. The model's core assumption holds: fill intensity decays exponentially with quote distance (R² ≥ 0.98). The illiquid stock shows the Roll bid–ask bounce, and intraday volatility is U-shaped rather than constant. On real data the model's inventory control survives: it cuts the standard deviation of daily PnL by 4.8× (RELIANCE) and 7.3× (KSCL). Its profit does not survive: an exact PnL decomposition shows that adverse selection, which the model ignores, absorbs all spread income, and the model's spread is about three times the market's Roll spread. On NSE, Avellaneda–Stoikov works as a risk-control rule, not as a stand-alone source of profit.

## Files to upload

| Form item | File |
|---|---|
| Final report (PDF) | `submission/BM51002_Term_Project_Report.pdf` |
| Dataset (later) | `submission/BM51002_Term_Project_Dataset.zip` (the two CSVs plus `data/README.md`) |
