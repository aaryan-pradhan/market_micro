# Market Microstructure Endsem: Start Here

The exam is on Monday, 23 November 2026, from 3:00 PM to 5:00 PM. It carries 25 percent of the grade. Check your room on the admit card.

## 1. Syllabus and notes

| Syllabus item | Notes | Priority | Time |
|---|---|---|---|
| Theories under information-based models | [Topic 1](1-information-based-models.md) | 1 | 75 minutes |
| Liquidity measures and applications (Lesmond, Chordia, Amihud) | [Topic 2](2-liquidity-measures.md) | 2 | 50 minutes |
| Triggers of extreme illiquidity | [Topic 3](3-extreme-illiquidity.md) | 3 | 35 minutes |
| Market-wide liquidity phenomena | [Topic 4](4-market-wide-liquidity.md) | 4 | 35 minutes |
| Basic concepts discussed in class | [Topic 5](5-basic-concepts.md) | 5, least important | 10 minutes |
| Written practice | Section 7 of this page | Last | 35 minutes |

The total is 4 hours.

## 2. What will probably be asked

This is my prediction. I did not find an old endsem paper. It uses the syllabus, the slides and the two old midsem papers.

The 2025 midsem had 6 questions for 40 marks in 2 hours. Two were numericals and the rest asked you to explain or compare. The 2024 midsem had 7 questions for 50 marks.

| Chance | Likely question | Where |
|---|---|---|
| Very high | Find the bid, ask and spread in Glosten and Milgrom | Topic 1, section 5 |
| Very high | Derive or explain Kyle's price impact and insider profit | Topic 1, section 6 |
| High | Explain trade size, separating and pooling in Easley and O'Hara | Topic 1, section 7 |
| High | Compare Lesmond, Chordia and Amihud, with the use of each measure | Topic 2, sections 2, 3 and 5 |
| High | Explain liquidity spirals and their triggers | Topic 3, sections 3 and 5 |
| High | Identify illiquidity and loss spirals from spread and price data | Topic 3, section 6 |
| High | Explain predatory trading and price overshooting | Topic 4, section 1 |
| Medium | Explain commonality and market-wide illiquidity | Topic 2, section 2 and Topic 4, section 5 |
| Medium | Explain the option view of Copeland and Galai | Topic 1, section 4 |
| Medium | Explain episodic crises or the test for price reversals | Topic 4, sections 2 and 3 |
| Low | Compare inventory and information models | Topic 5, section 9 |
| Low | Explain Bagehot, Ince or Stoll's friction | Topic 1, section 3 and Topic 2, sections 4 and 6 |
| Low | Derive Roll's spread | Topic 5, section 10 |

## 3. What to do

1. Read the topics in the priority order.
2. Write each Glosten-Milgrom and Kyle step by hand.
3. Solve each worked example again without looking.
4. Learn every paper as question, method, formula, finding and limitation.
5. Draw the spiral, the event tree and the overshooting figure from memory.
6. In the exam, define every symbol first.
7. In the exam, end every numerical with one sentence of meaning.

## 4. What not to do

- **Inventory models:** Do not study their derivations again. The comparison table in Topic 5 is enough.
- **Basic concepts:** Do not spend more than 10 minutes on Topic 5. Topics 1 to 4 are all very important.
- **Large tables:** Do not learn every number. Learn the sign and the meaning.
- **New papers:** Do not read other papers from the course outline.
- **Slide errors:** Do not copy a marked slide error. Use the corrected step in the notes.
- **Spread formulas:** Do not mix Stoll's half-spreads with Chordia's full spreads.
- **Symbols:** Do not mix the two meanings of $\mu$. It is the informed share in Glosten-Milgrom. It is an intercept in Kyle.

## 5. What you must finish

If time is short, finish these eight things first.

1. Glosten-Milgrom formulas and example.
2. Kyle formulas and example.
3. Easley-O'Hara equilibria and the block sale path.
4. Amihud formula and findings.
5. Chordia regression and conclusion.
6. Lesmond findings and the LOT idea.
7. The two spiral scores and the spiral diagram.
8. Predatory trading conditions and figure.

## 6. The whole course in five lines

1. Informed traders create a spread and a price impact.
2. Liquidity measures tell us how large these costs are.
3. Funding limits turn a small loss into extreme illiquidity.
4. Common funding and strategic selling spread illiquidity across the market.
5. Illiquidity lowers prices and raises the return that investors demand.

## 7. Formulas to write from memory

**Copeland and Galai:** The dealer maximizes expected gain less expected loss.

$$\max_{P_A, P_B}\left[(1-\pi_I)G_U-\pi_I L_I\right]$$

**Glosten and Milgrom:** Here $\theta$ is the probability of the low value.

$$a=\frac{\theta(1-\mu)V_L+(1-\theta)(1+\mu)V_H}{1+\mu(1-2\theta)}$$

$$b=\frac{\theta(1+\mu)V_L+(1-\theta)(1-\mu)V_H}{1-\mu(1-2\theta)}$$

$$s=\frac{4\theta(1-\theta)\mu(V_H-V_L)}{1-(1-2\theta)^2\mu^2}$$

**Kyle:** The price is linear in order flow.

$$p=p_0+\frac{\sigma_0}{2\sigma_y}z$$

$$x=\frac{\sigma_y}{\sigma_0}(v-p_0)$$

$$E[\pi_I]=\frac{\sigma_0\sigma_y}{2}$$

**Easley and O'Hara:** This is the bid for a large trade under separation.

$$b_2=V^{\ast}-\frac{\sigma_v^2}{\bar{V}-\underline{V}}\cdot\frac{\alpha\mu}{X_S^2(1-\alpha\mu)+\delta\alpha\mu}$$

**Chordia:** Commonality means a positive slope.

$$DL_{j,t}=\alpha_j+\beta_jDL_{M,t}+\varepsilon_{j,t}$$

**Amihud:** Average the daily ratios.

$$ILLIQ=\frac{1}{D}\sum_{d=1}^{D}\frac{\lvert R_d\rvert}{VOLD_d}$$

**Lesmond:** LOT is the round-trip cost.

$$LOT=\alpha_2-\alpha_1$$

**Roll:** The bounce gives negative covariance.

$$S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$$

**Funding limit:** Capital and margin limit the position.

$$X\le\frac{W}{m}$$

**Spirals:** Score each day as +1, 0 or -1. The band is the previous year's mean plus or minus half a standard deviation. Add 10 days.

$$Spiral_{10}=\sum_{k=0}^{9}Score_{t-k}$$

**Predatory trading:** In the slide example, 16 shares are sold with $\lambda=1$. The price falls from 116 to 100. The predator buys back 10 shares, and the price recovers to 110. The overshoot is 10.

## 8. How far to trust these notes

- **Slides:** The notes cover the four endsem decks. Slide numbers are in the headings.
- **Slide images:** Each section ends with the official slides it uses, as PNGs from `slides/`. Title slides are left out. In Topic 5, only the slides that the notes cover are shown.
- **Lesmond (2005):** It is not in the slides and the full paper is behind a paywall. Topic 2 says where each part comes from.
- **Amihud's findings:** The slide is blank, so Topic 2 points to the midsem notes for them.
- **Stars:** A ⭐ in each topic marks what to know without notes.
- **Scope:** The notes explain only what is on the slides. Lesmond (2005) is the one exception, because the syllabus names it.
- **Chart readings:** Numbers read from charts are marked as approximate.
- **Worked examples:** The examples are for practice. They are not results of the papers.
