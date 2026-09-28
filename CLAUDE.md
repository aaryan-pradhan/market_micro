# CLAUDE.md

Guidance for Claude Code in this repo.

## Purpose

Study repo for **BM51002 Market Microstructure** (IIT Kharagpur, VGSoM, Autumn 2026-27,
Prof Ajay Kumar Mishra). Not code: every "feature" is a revision ledger page.

## Deadline: Mid Term, Tue 29 Sep 2026 (25% of the grade)

Syllabus, verbatim from `course/Syllabus for Mid Term 29.09.2026.txt`:

1. Five Theories discussed under Inventory-Based Models
2. Rolls (1984) article
3. Liquidity Measures- Chordia (2000), Amihud (2002)

The five inventory theories (from `3_inventory_models/2 Inventory model Full.pdf`):

| # | Paper | One-line gist |
|---|---|---|
| 1 | Garman (1976), "Market microstructure" | Monopolist dealer, fixed bid/ask, Poisson buy/sell arrivals λa(pa), λb(pb); no borrowing → gambler's ruin; spread partly to cut failure probability |
| 2 | Amihud & Mendelson (1980), "Dealership market: market-making with inventory" | Prices depend on inventory (birth–death process); bid & ask monotone decreasing in inventory; preferred inventory position; positive spread |
| 3 | Stoll (1978), "The supply of dealer services" | Risk-averse dealer, utility of terminal wealth, 2 periods; costs = holding + order + information; spread linear in risk aversion, trade size, variance; independent of initial inventory |
| 4 | Ho & Stoll (1981), "Optimal dealer pricing under transactions and return uncertainty" | Multi-period DP; Poisson order flow + Brownian portfolio return; spread = risk-neutral part + risk adjustment; spread independent of inventory, but price *placement* depends on it; no closed form |
| 5 | O'Hara & Oldfield (1986), "The microeconomics of market making" | Discrete time, infinite horizon, limit + market orders; spread = known limit orders + risk-neutral adjustment + risk adjustment; risk-averse spread may be *smaller*; inventory affects size and placement |

(The course outline dates Amihud & Mendelson to 1980, the slides say 1978 in one place. Use 1980.)

Roll (1984) is in `4_volatility/2.1 Sources of Volatility.pdf` and cited in
`1_market_structure/1.4 ... Biais, Glosten Spatt 2005.pdf`. Chordia, Roll &
Subrahmanyam (2000) and Amihud (2002) are in `2_liquidity/1.5 ...`. Slide
equations are images, so read the PDF pages visually (Read tool, `pages`), not
through `pdftotext`.

Earlier: Quiz on 11 Sep 2026, same syllabus up to the models covered by 10 Sep.

Grading: 2 quizzes 10%, 2 surprise quizzes 10%, mid term 25%, term project 20%,
end term 25%, assignments 10%.

## Layout

- `course/`: outline, syllabi, `Links.txt` (Drive folders with the articles),
  `Topics Discussed.xlsx`, and the group-project form. The form holds classmates'
  emails and roll numbers, so never commit or publish it.
- `1_market_structure/`: intro, exchanges, orders & trades, Biais–Glosten–Spatt survey.
- `2_liquidity/`: Chordia (2000), Amihud (2002), Ince (2022), Stoll (2000).
- `3_inventory_models/`: the five theories. `partial.pdf` is an earlier cut of `Full.pdf` (Garman through Stoll). Use Full.
- `4_volatility/`: fundamental vs transitory volatility, Roll (1984), Hasbrouck VAR.
- `papers/`: past midsem papers (`midsem_2024.pdf`, `midsem_2025.pdf`) and one solutions page per paper (`midsem_2024.html`, `midsem_2025.html`, all questions solved). Each question on the page has three sections: target reading list (deck + pages, or a ⚠ slides-missing box) → concept summary → solution + takeaway. Add each new question to its paper's page and to `index.html`.
- `index.html`: the entry point that links every ledger page.
- `_template.html`: the ledger page to copy (one worked entry, Roll 1984).

`*.pdf` and `*.xlsx` are gitignored. The slides are the instructor's, so the
public repo gets only the notes. Older Avellaneda–Stoikov material lives in
`../MarketMicrostructure/`.

## Ledger format (copied from dsa-prep)

Source: `../dsa-prep/prob_prep/` (the "prob ledger") and `../dsa-prep/CONTEXT.md`.

**Golden Rules.** Solutions are simple. Proofs are simple. Implementations are simple.
"Simple" means no gaps and plain words, not fewest words: repeating is fine, skipping is not.

**Page.** One self-contained HTML page per syllabus topic, saved in that topic's
folder (e.g. `3_inventory_models/inventory_models.html`). Copy `_template.html`:
it carries the prob-ledger `<style>` block unchanged (Meslo font, colour tokens,
light and dark themes) and KaTeX (`\( \)` inline, `\[ \]` display). Do not
invent new CSS classes. Link the page from `index.html`. Each page can be published
as a private claude.ai artifact.

**Entry** (one per model / paper), in this order:

1. **`.idea` primer box**: define every term the entry uses before the entry needs
   it (for example "bid–ask bounce" or "Poisson arrival rate"). Never assume the
   reader already knows a definition.
2. **Statement**: `.stmt` setup, then a separate **Question:** line saying what the model answers.
3. **Key idea**: the one fact the result rests on, in plain words.
4. **Previous model → why it falls short**: a `.brute` table with 4 rows in this order.
   - `before`: the earlier model or naive approach.
   - `assumes`: the assumption it rests on.
   - `fails at` (row class `dies`): the specific case that breaks it.
   - `therefore` (row class `therefore`): what this model changes.

   This is dsa-prep's "brute force → why it dies". The five inventory theories form a chain, each fixing the previous one.
5. **Solution**: **Setup** (every symbol defined, every assumption numbered A1, A2, …)
   → **Claim** → `ol.pf` numbered steps, one fact per step, each ending in
   `<span class="r"><b>Why:</b> …</span>` that cites a definition, an assumption
   or an earlier step. Show the algebra line by line. Never write "clearly",
   "obviously", "similarly" or "simplifying gives". Put the final answer in
   `.ans`. End with **Conclusion.** … ∎. An inline SVG (`class="fig"`, only the
   `.fig` classes, `viewBox`, `role="img"`, `aria-label`) goes at the end of the
   step it illustrates, and only where it replaces prose.
6. **Exam**: **Gotcha:** a real trap. **Recognize:** the phrase that tells you
   which model a differently worded question is about. Plus the paper's findings
   as a list when the exam asks "what did X find".
7. **⚠ Slide gap** (`.gap`): only when the slide's argument is incomplete or
   wrong. Derive from scratch; the slides are never the standard.

Numerical claims get checked, by hand or with a quick script, before they go on the page.
