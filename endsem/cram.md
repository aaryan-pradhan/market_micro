---
title: "Endsem Cram Sheet: Only What to Memorize"
geometry: margin=1.6cm
fontsize: 10pt
header-includes:
  - \usepackage[most]{tcolorbox}
---

**How this works.** Each section starts with the likely exam question. Then come mnemonic tables. Read the mnemonic, then say each line aloud from the letter. Orange boxes hold the formulas, each with its trick. The sections are in order of exam chance.

| Rank | Must memorize | Master mnemonic |
|---|---|---|
| 1 | Glosten-Milgrom quotes and spread | Buy High, Sell Low gets the plus |
| 2 | Kyle price impact and profit | Units decide, three halves finish |
| 3 | Easley-O'Hara sizes and price path | Few: Fork. Many: Mix. |
| 4 | Amihud measure and findings | Ratio first, then average |
| 5 | Chordia regression and conclusion | Together, own trades widen, market trades tighten |
| 6 | Lesmond and LOT | The no-trade band |
| 7 | Spirals: loop, triggers, scores | X is at most W over m. +1 is always bad. |
| 8 | Predatory trading | OLIPS. Sell with them, then buy from them. |

**The five information models in order: "The dealer WOBLS."**

| Letter | Paper | What it adds |
|---|---|---|
| W | Bagehot (1971) | Words only, no equation |
| O | Copeland and Galai (1983) | Quotes are free Options |
| B | Glosten and Milgrom (1985) | The dealer learns by Bayes rule |
| L | Kyle (1985) | A strategic insider, and price impact Lambda |
| S | Easley and O'Hara (1987) | Trade Size and event uncertainty |

\newpage

# 1. Glosten and Milgrom (1985): very high chance

**Likely question:** Find the bid, the ask and the spread.

**Rule to say first:** "The ask is $E[V\mid\text{buy}]$. The bid is $E[V\mid\text{sale}]$." The quotes are regret free. The dealer has zero profit.

**Symbols to write first:** $\theta=\Pr(V_L)$ ("$\theta$ for trouble"). $\mu$ = the share of informed traders. Uninformed traders buy or sell with probability 0.5 each.

::: {.box title="Glosten and Milgrom: one grid gives every formula"}
Draw this grid. The columns are the two values. The rows are the two trades.

$$\begin{array}{l|cc|c}
 & V_L\ (\theta) & V_H\ (1-\theta) & \text{Sum}\\ \hline
\text{Buy}\to\text{ask} & \theta(1-\mu) & (1-\theta)(1+\mu) & R_B\\
\text{Sale}\to\text{bid} & \theta(1+\mu) & (1-\theta)(1-\mu) & R_S
\end{array}$$

**Sign trick: "Buy High, Sell Low gets the plus."** The cells Buy-$V_H$ and Sale-$V_L$ get $1+\mu$. The other two cells get $1-\mu$.

1. Ask = the Buy-row weighted average of $V_L$ and $V_H$.
2. Bid = the Sale-row weighted average.
3. $\Pr(B)=\tfrac12 R_B=\tfrac12[1+\mu(1-2\theta)]$. $\Pr(S)=\tfrac12R_S$.
4. New $\theta$ after a buy = $\theta(1-\mu)/R_B$.
5. Spread, "4 coins, mu, range, over the two sums": $s=\dfrac{4\,\theta(1-\theta)\,\mu\,(V_H-V_L)}{R_B\,R_S}$. With $\theta=\tfrac12$, $s=\mu(V_H-V_L)$.
6. Check: $\Pr(B)\,a+\Pr(S)\,b$ = prior mean (martingale).

Example to recite: $V_H=110$, $V_L=90$, $\theta=0.3$, $\mu=0.4$. Buy row 0.18, 0.98 (sum 1.16). Sale row 0.42, 0.42 (sum 0.84). Ask 106.897. Bid 100. Spread 6.897. $\Pr(B)=0.58$. Check: $0.58(106.897)+0.42(100)=104$.
:::

**Findings: "ZLMS."**

| Letter | Finding |
|---|---|
| Z | A zero-profit dealer puts the adverse-selection cost into the spread |
| L | Beliefs and quotes are updated (learning) after each trade |
| M | Prices are a martingale: the best forecast of the next price is today's price |
| S | The market is semi-strong efficient |

**Trap:** the slides switch the meaning of $\theta$, and equation 4.28 is wrong. Always state $\theta=\Pr(V_L)$.

# 2. Kyle (1985): very high chance

**Likely question:** Derive or explain the price impact $\lambda$ and the insider's profit.

**Setup to write:** $v\sim N(p_0,\sigma_0^2)$. Noise $y\sim N(0,\sigma_y^2)$. The insider sends $x$. The dealer sees only $z=x+y$. Price $p=\mu+\lambda z$. Here $\mu$ is an intercept, not the informed share.

**Proof in four moves: "Insider, Dealer, Meet, Hide."**

| Move | What happens |
|---|---|
| Insider | Maximize $x(v-\mu-\lambda x)$. So $x=(v-\mu)/2\lambda$, and $\beta=1/2\lambda$ |
| Dealer | $\lambda=\mathrm{Cov}(v,z)/\mathrm{Var}(z)=\beta\sigma_0^2/(\beta^2\sigma_0^2+\sigma_y^2)$ |
| Meet | Put $\beta=1/2\lambda$ in. Then $\lambda^2\sigma_y^2=\sigma_0^2/4$ |
| Hide | $\beta^2\sigma_0^2=\sigma_y^2$: the insider's order is exactly as loud as the noise |

::: {.box title="Kyle: units decide, three halves finish"}
**Units trick.** $\sigma_0$ is in price. $\sigma_y$ is in shares.
$\lambda$ is price per share, so it is $\sigma_0/\sigma_y$. $\beta$ is shares per price, so it is $\sigma_y/\sigma_0$. Profit is price times shares, so it is $\sigma_0\sigma_y$.

**Three halves.**

1. $\lambda\beta=\tfrac12$, so the 2 sits under $\lambda$: $\;\lambda=\dfrac{\sigma_0}{2\sigma_y}$, $\;\beta=\dfrac{\sigma_y}{\sigma_0}$.
2. Expected insider profit $=\tfrac12\sigma_0\sigma_y$.
3. Variance left after trading $=\tfrac12\sigma_0^2$.

**Who pays:** the noise traders lose $\lambda\sigma_y^2=\tfrac12\sigma_0\sigma_y$, which is the insider's profit. The dealer earns zero.

**Trade order:** $x=\beta(v-p_0)$, then $z=x+y$, then $p=p_0+\lambda z$, then the realized profit is $x(v-p)$.

Example to recite: $p_0=100$, $\sigma_0=10$, $\sigma_y=1000$, $v=110$, $y=-400$. $\lambda=0.005$, $\beta=100$, $x=1000$, $z=600$, $p=103$. Realized profit 7000. Expected profit 5000. Variance left 50.
:::

**What changes what: "Profit likes both. Lambda likes only information."**

| Rise in | $\lambda$ | Profit | Why |
|---|---|---|---|
| $\sigma_0$ (private information) | Up | Up | More to hide, so the market is less liquid |
| $\sigma_y$ (noise) | Down | Up | More cover, so the market is deeper |

**Findings (slide 32):** noise hides the insider's information from the dealer. Liquidity traders pay the insider. With many periods, the insider splits the order into small pieces.

# 3. Easley and O'Hara (1987): high chance

**Likely question:** Explain trade size, the separating and pooling equilibria, and the price path after a block.

**Three letters: "Alpha Arrives, Delta Decides, Mu Many."**

| Letter | Meaning |
|---|---|
| $\alpha$ | The probability that an information event arrives |
| $\delta$ | The probability that the signal is low (bad news) |
| $\mu$ | The share of traders who are informed after an event |
| $\alpha\mu$ | The chance that a random trader is informed |

**Two equilibria: "Few informed: Fork. Many informed: Mix."**

| Point | Separating (Fork) | Pooling (Mix) |
|---|---|---|
| When | Few informed traders | Many informed traders |
| The informed trade | Large size only | Both sizes |
| Small quotes | $a_1=b_1=V^{\ast}$, no spread | Spread on small trades too |
| Large quotes | Spread | Spread |

::: {.box title="Easley and O'Hara: two weights, U and I"}
**I (informed) = the tree in time order:** event, then signal, then informed. Sellers: $I_S=\alpha\delta\mu$. Buyers: $I_B=\alpha(1-\delta)\mu$.
**U (uninformed) = "wants large, times is uninformed":** $U_S=X_S^2(1-\alpha\mu)$.

1. $V^{\ast}=\delta\underline{V}+(1-\delta)\bar{V}$.
2. Large bid, pulled down by the informed share: $b_2=V^{\ast}-\dfrac{I}{U+I}(V^{\ast}-\underline{V})$.
3. Large ask, pulled up: $a_2=V^{\ast}+\dfrac{I}{U+I}(\bar{V}-V^{\ast})$.
4. Separation, "the size ratio must beat the crowd ratio": $\dfrac{B^2}{B^1}\ge\dfrac{U_B+I_B}{U_B}=1+\dfrac{\alpha\mu(1-\delta)}{X_B^2(1-\alpha\mu)}$.
5. Slide form of the bid: $b_2=V^{\ast}-\dfrac{\sigma_v^2}{\bar{V}-\underline{V}}\cdot\dfrac{\alpha\mu}{X_S^2(1-\alpha\mu)+\delta\alpha\mu}$, with $\sigma_v^2=\delta(1-\delta)(\bar{V}-\underline{V})^2$ ("coin times range squared").

Example to recite: $\bar{V}=110$, $\underline{V}=90$, $\delta=\alpha=0.5$, $\mu=0.4$, $X=0.25$. $V^{\ast}=100$, $U=0.2$, $I=0.1$, share $=1/3$. Bid 96.667. Ask 103.333. Small 100. Separation needs $B^2/B^1\ge1.5$. A small trade after the block prices at 97.391.
:::

**Price path after a block sale: "Known event: stuck. Unsure event: bounce part way."**

| Time | Event known (Fig 1) | Event uncertain (Fig 2) |
|---|---|---|
| $t$ | Small trade at $V^{\ast}$ | Small trade at $V^{\ast}$ |
| $t+1$ | Block sale, price falls to $b_2$ | Block sale, price falls to $b_2$ |
| $t+2$ | Small trade says nothing new, price stays at $b_2$ | Small trade makes "no event" likelier, price recovers part way, still below $V^{\ast}$ |

**Findings (slide 47): "BQIO."**

| Letter | Finding |
|---|---|
| B | Block trades move prices because of informed trading |
| Q | Quantity is correlated with private information |
| I | Informed traders prefer to trade larger amounts at any given price |
| O | Optimal pricing depends on quantity |

\newpage

# 4. Amihud (2002): high chance

**Likely question:** Give the measure, compare it with others, and state the findings.

::: {.box title="Amihud: ratio first, then average"}
$$ILLIQ_{iy}=\frac{1}{D_{iy}}\sum_{d=1}^{D_{iy}}\frac{\lvert R_{iyd}\rvert}{VOLD_{iyd}}$$
Divide each day's absolute return by that day's dollar volume. Then average over the days. A higher ILLIQ means less liquid.
Amivest is upside down: $\sum VOLD/\sum\lvert R\rvert$. A higher Amivest means more liquid.

Example to recite: returns $0.02,-0.01,0.03$, volumes 10, 5, 10 (million). Ratios 0.002, 0.002, 0.003. ILLIQ 0.002333. Amivest $25/0.06=416.67$.
Surprise example: $P=D/r$. $5/0.10=50$, then $5/0.125=40$, so the return now is $-20\%$.
:::

**Is it valid? "Kyle plus fixed cost."** $ILLIQ=-292+247.9\lambda+49.2\psi$, $R^2=0.30$. Both slopes are positive.

**Method: "NYSE 63 to 97, 408 months, Fama-MacBeth."** CRSP data. Shumway (1997) delisting adjustment. Characteristics from year $y-1$.

**Findings: "Expected = Extra return later. Unexpected = Ugly return now. Small firms feel it most."**

| Finding | Statement |
|---|---|
| Cross-section | ILLIQ has a positive, significant effect on returns, even with beta and size |
| Expected illiquidity | Higher expected market illiquidity gives a higher ex-ante excess return |
| Unexpected illiquidity | Unexpected illiquidity lowers the contemporaneous return |
| Small firms | Both effects are stronger for small firms (flight to liquidity) |

# 5. Chordia, Roll and Subrahmanyam (2000): high chance

**Likely question:** Explain commonality, the regression and the conclusion.

**Seven reasons for commonality: "PVIVP + F + I."** The first five are inventory reasons and read the same both ways.

| Letter | Reason (slide 5) |
|---|---|
| P | Price swings: market-wide trading responds to large price moves |
| V | Volume: trading volume changes dealer inventories together |
| I | Interest rates: they set the cost of carrying inventory |
| V | Volatility: inventory risk has a market-wide part |
| P | Program trading: it puts common pressure on many inventories |
| F | Funds: institutional funds with similar styles trade alike |
| I | Information: a few large traders may know about many stocks |

**Data: "92, 1169, 254, \$2."** NYSE (ISSM) 1992, 1,169 stocks, 254 trading days, prices below \$2 removed.

::: {.box title="Chordia: five measures and the regression"}
"Quoted uses the Mid. Effective uses the trade price, with a 2. Depth is the only one where higher is better."

QSPR $=P_A-P_B$. PQSPR $=(P_A-P_B)/P_M$. DEP $=(Q_A+Q_B)/2$. ESPR $=2\lvert P_t-P_M\rvert$. PESPR $=2\lvert P_t-P_M\rvert/P_t$.

Regression: $DL_{j,t}=\alpha_j+\beta_jDL_{M,t}+\varepsilon_{j,t}$, with $DL_t=(L_t-L_{t-1})/L_{t-1}$.
"0.69, and 69 to 85": the same-day coefficient is 0.69, and 69 to 85 percent of the coefficients are positive. Same day beats lag and lead.

Example to recite: bid 99.80, ask 100.20, buy at 100.10, depth 600 and 400. QSPR 0.40, PQSPR 0.004, DEP 500, ESPR 0.20, PESPR 0.002.
:::

**Test 3: own trades and market trades.**

| Variable | Effect on spread | Reason |
|---|---|---|
| Stock's own number of trades | Up | Asymmetric information |
| Market volume | Down | Inventory: balanced uninformed trading |
| Trade size | Up (spread and depth) | Block pressure or information |

**Conclusion: "Together. Own trades widen. Market trades tighten."**

# 6. Lesmond (2005) and LOT: high chance

**Likely question:** Compare Lesmond, Chordia and Amihud. Explain LOT.

**LOT: "the no-trade band."** A trader trades only if the news is worth more than the cost. Inside the band $[\alpha_1,\alpha_2]$, nobody trades, so the observed return is zero. Many zero-return days mean a high cost.

::: {.box title="LOT"}
$LOT=\alpha_2-\alpha_1$ (the round-trip cost).
Observed return: $R^{\ast}-\alpha_2$ above the band, 0 inside, $R^{\ast}-\alpha_1$ below.
Example to recite: $\alpha_1=-0.010$, $\alpha_2=0.015$, LOT 2.5%. True 0.025 gives 0.010. True 0.007 gives 0. True $-0.018$ gives $-0.008$.
:::

**Findings: "Across: LOT 'n' Roll. Within: LOT, then Amihud. Politics beats law."**

| No. | Finding |
|---|---|
| 1 | Across countries, the price-based LOT and Roll measures work best |
| 2 | Within a country, LOT works best, then Amihud |
| 3 | Weak political and legal institutions give higher liquidity costs |
| 4 | More political risk adds 10 bp (LOT) and 1.9% price impact (Amihud) |
| 5 | Political risk matters more than legal-information risk |

**Compare the three measures: "Spread, Impact, Band."**

| Paper | Measure | Data needed | Use |
|---|---|---|---|
| Chordia (2000) | Spreads and depth | Quotes and trades | Commonality in liquidity |
| Amihud (2002) | $\lvert R\rvert$ per dollar volume | Daily return and volume | Illiquidity is priced |
| Lesmond (2005) | LOT, the zero-return band | Daily returns only | Emerging markets without quotes |

\newpage

# 7. Spirals: Topic 3, high chance

**Likely question:** Explain liquidity spirals and their triggers. Identify spirals from spread and price data.

**Two liquidities: "Market liquidity belongs to the Asset. Funding liquidity belongs to the Trader."**

::: {.box title="Funding constraint"}
$X\le W/m$. **W falls: Loss spiral. m rises: Margin spiral.**
Spiral example: $W=10$, $m=10\%$, $X=100$, loan 90. A 3% fall gives $W'=7$. At 10% the trader holds 70 (sells 27). At 14% the trader holds 50 (sells 20 more). Total: 47 of 97 sold.
:::

**The loop (slide 7): "Lose, Can't fund, Sell, Price drops, then Lose more and Pay more margin."**

| Step | What happens |
|---|---|
| 1 | Initial losses |
| 2 | Funding problems for speculators |
| 3 | Reduced positions |
| 4 | Prices move away from fundamentals |
| 5 | Losses on existing positions (loss spiral) and higher margins (margin spiral), back to step 2 |

**Triggers: "LFVF."** First **L**oss. **F**unding shock. **V**olatility shock. **F**orced sale.

**Five features of liquidity (slide 5): "Dry, Common, Volatile, Flees, Follows."**

| Feature | Statement | Reason |
|---|---|---|
| Dry | Liquidity can suddenly dry up | Financiers raise margins when volatility changes |
| Common | Liquidity has commonality across securities | The same speculators supply liquidity everywhere |
| Volatile | Liquidity is related to volatility | Volatile assets need higher margins |
| Flees | Flight to quality | Scarce capital goes to low-margin assets |
| Follows | Liquidity moves with the market | Funding falls when the market falls |

**Margins (slide 6): "4 before, 12 on Black Monday."** About 4% before 1987, above 12% in October 1987, and up again in every crisis (LTCM 1998, subprime 2007 to 2008).

::: {.box title="Spiral scores (Jain, Mishra and McInish 2013): +1 is always bad"}
Band = last year's mean $\pm$ half a standard deviation. Both tests must hold, otherwise the score is 0.

**Illiquidity spiral (spread):** +1 if $s_t>s_{t-1}$ and $s_t>\bar{s}+0.5\sigma_s$. $-1$ if $s_t<s_{t-1}$ and $s_t<\bar{s}-0.5\sigma_s$.
**Loss spiral (price):** +1 if $P_t<P_{t-1}$ and $P_t<\bar{M}-0.5\sigma_P$. $-1$ if $P_t>P_{t-1}$ and $P_t>\bar{M}+0.5\sigma_P$.
**Spiral measure** = the sum of the last 10 days' scores.

Example to recite: spread 0.95, yesterday 0.90, mean 0.80, sd 0.20, upper limit 0.90, so +1. Price 95, yesterday 97, mean 100, sd 8, lower limit 96, so +1. Seven +1, one $-1$, two 0 give a sum of 6.
:::

**Valuation: "Spirals shrink multiples."** The loss spiral lowers P/B and P/E. The illiquidity spiral lowers P/E, and P/B with controls. The $R^2$ is small. Data: CRSP S&P 500, 1982 to 2010, 476 firms.

# 8. Predatory trading: Topic 4, high chance

**Likely question:** Explain predatory trading and price overshooting.

**Four ways liquidity vanishes market-wide: "Prey, Betray, Pressure, Spiral."** Predatory trading. Broken cooperation. Selling pressure. Funding spirals.

**Definition:** trading that exploits another trader's need to sell. Predators sell with the distressed trader, then buy back. **"Sell with them, then buy from them."**

**Five results: "OLIPS."**

| Letter | Result |
|---|---|
| O | The price overshoots |
| L | The distressed trader gets a lower liquidation value |
| I | The market is illiquid exactly when liquidity is most needed |
| P | A trader can profit by triggering another's crisis |
| S | The crisis spills over across traders and markets |

**When predation pays: "Illiquid and Big."** The market is illiquid, and the distressed position is large relative to others' capacity.

::: {.box title="Predation example: 116, 100, 110"}
Price change $=\lambda\times$ shares. Two traders hold 8 each and both sell: 16 shares, so the price falls from 116 to 100. The predator buys back 10 alone: the price ends at 110. Overshoot $=110-100=10$.
More predators: the overshoot shrinks (3.3, 0.8, 0.2). "Competition eats predation."
:::

**Episodic crises (Carlin, Lobo, Viswanathan 2007): "RHEC."**

| Letter | Meaning |
|---|---|
| R | Repeated game: traders cooperate and supply liquidity to each other |
| H | High stakes: today's gain beats future cooperation, so cooperation breaks |
| E | Episodic: illiquidity comes in sudden episodes |
| C | Contagion: a breakdown hits all linked markets |

**Shkilko et al. (2012): "Longs lead, shorts follow."** Long sellers drive intraday declines. Short sellers make them worse, and switch from supplying to demanding liquidity.

::: {.box title="Large reversal: two sigma down, 90 to 110 back"}
Decline: $\ell\le-2\sigma_i$. Rebound by the close: $0.9\lvert\ell\rvert\le R_{close}-\ell\le1.1\lvert\ell\rvert$.
Example: $\sigma_i=1\%$, $\ell=-2\%$. The day must end between $-0.2\%$ and $+0.2\%$.
:::

**Market-wide phenomena: one cause each.**

| Phenomenon | Cause |
|---|---|
| Commonality | Common funding limits (Chordia) |
| Dry-up | Margin spiral |
| Flight to quality | Scarce funding |
| Overshooting | Predatory trading |
| Episodic illiquidity | Broken cooperation |
| Large reversal | Temporary selling pressure |

\newpage

# 9. Medium and low chance: one line each

**Copeland and Galai (1983): "Ask is a Call, Bid is a Put."** The dealer writes a free call at $P_A$ and a free put at $P_B$ to informed traders.

::: {.box title="Copeland and Galai"}
Maximize $(1-\pi_I)G_U-\pi_IL_I$: "Gain from the Uninformed, Lose to the Informed."
Symmetric case: $h=\pi_I\Delta$. Example: $\Delta=10$, $\pi_I=0.2$, so ask 102, bid 98, spread 4.
:::

**Findings: "PV up, ADC down."** The spread rises with Price and Variance. It falls with Activity, Depth and Continuity. **Limit:** one period only.

**Bagehot (1971): "2-2-1."** Two gains (market gain, trading gain). Two traders (informed, uninformed). One balance (the spread).

**Ince (2022): "ASI, only I survives."** Illiquidity = Alpha + Systematic + Idiosyncratic. Only the idiosyncratic part predicts returns once tiny stocks are removed.

**Stoll (2000): "Time or Price; Stoll pays the Price."** Friction is the price paid for immediacy. Real friction uses resources. Informational friction moves wealth to the informed. Stoll uses **half**-spreads, so Chordia's spread $=2\times$ Stoll's.

**Stoll signs: "Volume and Price shrink it. Variance grows it."**

**Inventory vs information models.**

| Point | Inventory | Information |
|---|---|---|
| Dealer's problem | Unbalanced inventory | Better-informed customers |
| Spread source | Inventory cost and risk | Loss to informed traders |
| Price effect | Temporary | Permanent |

::: {.box title="Roll (1984): the bounce shares one sign, with a minus"}
$P_t=V_t+\tfrac S2Q_t$. Neighbouring changes share only $-Q_{t-1}^2$, so $\mathrm{Cov}=-S^2/4$.
$S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$. Example: Cov $=-0.0625$, so $S=0.5$.
Limits: fails if Cov > 0. Assumes no information in trades and a constant spread.
:::

**Basic lists.**

| Mnemonic | List |
|---|---|
| I Want Deep Rivers | Liquidity: Immediacy, Width, Depth, Resiliency |
| Please Bring Dad's Huge Avocado, Very Fresh | Traders: Proprietary, Brokers, Dealers, Hedgers, Arbitrageurs, Value investors, Front runners |
| Let Traders Invest Very Profitably | Market quality: Liquidity, Transaction cost, Informative prices, Volatility, trading Profits |
| PIP | Why trade: Profit, Information, Price discovery |
