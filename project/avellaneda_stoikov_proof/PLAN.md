# The Avellaneda–Stoikov Model: a proof with no step skipped

## Context
Source: the working paper in `../papers/` (§2–3). Reader: a maths undergraduate who has not seen
stochastic control. Purpose: the full derivation of the reservation price and the optimal spread,
self-contained, so neither the deck nor the paper is needed. Delivered as a PDF to the project Drive folder.

## Decisions (intake)
1. Source: text layer yes → work from text; every line rewritten.
2. Purpose: learn from zero (worked RELIANCE numbers, intuition boxes).
3. Assumed knowledge: F1 Taylor, F2 Brownian increments, F3 Poisson arrivals, F4 normal MGF, F5 maximum test.
4. Scope: derivation only; comparative statics, exact (linearised) solution and simulation skipped.
5. Numbers: `verify.py` recomputes every number and identity (VERIFY in book.mk).

## Notation lock
| Item | Lock |
|---|---|
| time left | $(T-t)$, macro `\Tt` |
| half edge | $\frac1\gamma\ln(1+\frac\gamma k)$, macro `\edge` |
| expectations | `\E_t` (all randomness after t), `\E_{dW}`, `\E_Z`, `\E_W` |

## Topic plan
| # | Question / title | Source pages | Needs | Introduces | Status |
|---|---|---|---|---|---|
| 01 | The dealer's problem | §2 | F2 | mid-price, quotes, fill rate, inventory, cash, CARA utility, value function | drafted |
| 02 | The HJB equation | §3.1–3.2 | 01, F1–F3 | dynamic programming principle, HJB equation, jump terms | drafted |
| 03 | Removing cash and the mid-price | §3.3 | 02 | first guess, second guess, Δᵇg, Δᵃg | drafted |
| 04 | The best quote on each side | §3.5 | 03, F5 | first-order condition | drafted |
| 05 | Finding g | §3.4, §3.6 | 03, F4 | frozen-inventory value (the one approximation) | drafted |
| 06 | Reservation price and spread | §3.4–3.5 | 04, 05 | reservation bid/ask/price, inventory-risk premium, market-making edge | drafted |
