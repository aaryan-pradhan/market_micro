# Topic 5: Basic Concepts Discussed in Class

These notes follow the midsem decks: "1. Introduction of Market Microstructure", "1.1 Exchanges", "1.1 Orders and Trades" and "2.1 Sources of Volatility".

This is the least important topic. Read it once after Topics 1 to 4. A ⭐ marks what to know without notes.

## 1. What market microstructure is

The introduction slides list what microstructure covers.

| No. | Area | Example or detail |
|---|---|---|
| 1 | Trading rules | |
| 2 | Physical layouts | The NSE NEAT trading system |
| 3 | Information systems | The systems that present and communicate information |
| 4 | Interaction | How market participants interact |
| 5 | Safeguards | Price bands, circuit breakers and trading halts |

**Textbook definition (Kissell, 2014):** Market microstructure studies financial markets and how they operate. It focuses on five things.

| No. | Focus |
|---|---|
| 1 | The structure of exchanges and trading venues, both displayed and dark |
| 2 | The price discovery process |
| 3 | The determinants of spreads and quotes |
| 4 | Intraday trading behaviour |
| 5 | Transaction costs |

**Why we trade:** The slides give three reasons.

| No. | Reason |
|---|---|
| 1 | Profit |
| 2 | Information |
| 3 | Price discovery |

![intro slide 2](slides/intro/intro-02.png)

![intro slide 3](slides/intro/intro-03.png)

![intro slide 5](slides/intro/intro-05.png)

## 2. Dimensions of a market

| No. | Dimension | What it means |
|---|---|---|
| 1 | Trading platform | It can be manual or fully automated. Speed, market integration and stabilizing mechanisms matter |
| 2 | Information flow mechanism | It decides how information reaches traders |
| 3 | Traders' interaction | It decides how traders meet and trade |
| 4 | Regulatory mechanism | It sets the rules |
| 5 | Imperfections | Transaction cost and information asymmetry are the two imperfections |

![intro slide 7](slides/intro/intro-07.png)

## 3. ⭐ Traders and participants

**Types of traders:** The slides list seven types.

| No. | Type |
|---|---|
| 1 | Proprietary traders |
| 2 | Brokers or agency traders |
| 3 | Dealers |
| 4 | Hedgers |
| 5 | Arbitrageurs |
| 6 | Value investors |
| 7 | Front runners |

The exchanges deck adds these facts from Harris.

| Who or what | Fact |
|---|---|
| Zero-sum game | Trading is zero-sum when gains and losses are measured relative to the market average |
| Brokers | They are agents who arrange trades for their clients |
| Patient traders | They get better prices than impatient traders, because they search longer for good terms |
| Speculators | They trade to profit from information about future prices |
| Dealers | They lose to well-informed speculators, because they end up on the wrong side of the trade |
| Bluffers | They sometimes fool uninformed traders into trading unwisely |
| Investors and borrowers | Investors move money from the present to the future. Borrowers do the opposite |
| Hedgers | They trade to manage financial risks |
| Asset exchangers | They trade one asset for another that they value more |
| Gamblers | They trade to entertain themselves |
| Arbitrageurs | They make sure that prices do not differ much across markets |
| Sell side | Dealers and brokers provide exchange services to the buy side |

![intro slide 8](slides/intro/intro-08.png)

![intro slide 9](slides/intro/intro-09.png)

![exchanges slide 4](slides/exchanges/exchanges-04.png)

![exchanges slide 5](slides/exchanges/exchanges-05.png)

![exchanges slide 6](slides/exchanges/exchanges-06.png)

![exchanges slide 7](slides/exchanges/exchanges-07.png)

## 4. ⭐ Basic terms

| Term | Meaning |
|---|---|
| Bid | The best price to sell at |
| Ask | The best price to buy at |
| Mid quote | The average of the best bid and the best ask |
| Spread | The best ask minus the best bid |
| BBO | The best bid and offer |
| NBBO | The national best bid and offer |
| Price impact | How much an order moves the price |
| Uptick | A price above the last price |
| Downtick | A price below the last price |
| Zero tick | The same price as the last price |

| Point | Block deal | Bulk deal |
|---|---|---|
| Size | One trade of at least 5,00,000 shares or at least Rs 10 crore | At least 0.5 percent of a company's listed shares |
| When | A separate window, from 8:45 to 9:00 AM or from 2:05 to 2:20 PM | Normal hours |
| Who can see it | Retail investors cannot see it | Everyone can see it |

**Worked example (the Axis Bank slide):** The bid is 664.40 for 453 shares. The ask is 664.55 for 714 shares.

| Step | Measure | Working | Result |
|---|---|---|---|
| 1 | Spread | $664.55-664.40$ | 0.15 |
| 2 | Mid price | $(664.55+664.40)/2=1328.95/2$ | 664.475 |
| 3 | Proportional spread | $0.15/664.475=0.000226$ | 0.0226 percent |
| 4 | Depth | $(714+453)/2=1167/2$ | 583.5 shares |

![intro slide 10](slides/intro/intro-10.png)

![intro slide 11](slides/intro/intro-11.png)

![intro slide 12](slides/intro/intro-12.png)

![intro slide 20](slides/intro/intro-20.png)

![orders slide 9](slides/orders/orders-09.png)

## 5. ⭐ Liquidity dimensions

The 2025 midsem asked for the four dimensions of liquidity, so they were taught in class.

| Dimension | Question |
|---|---|
| Immediacy | How fast can I trade? |
| Width | How much does a small trade cost? This is the spread. |
| Depth | How much can I trade at a given price? |
| Resiliency | How fast does the price recover after a large trade? |

## 6. Orders

| Order | Instruction | Role |
|---|---|---|
| Market | Trade now at the best price available | It takes liquidity and pays the spread |
| Limit | Trade only at the limit price or better | It provides liquidity |
| Stop | Activate the order when the price reaches the stop price | A sell stop is a safety net for a long position |

| Order | Risk | What it means |
|---|---|---|
| Market | Poor price | It fills quickly, but sometimes at a poor price. Its price impact depends on available liquidity |
| Limit | Execution uncertainty | The price can move away, so the trader fails to trade |
| Limit | Adverse selection | The order fills when informed traders know that it is mispriced. This causes ex post regret |

![intro slide 21](slides/intro/intro-21.png)

![intro slide 23](slides/intro/intro-23.png)

![orders slide 2](slides/orders/orders-02.png)

![orders slide 3](slides/orders/orders-03.png)

![orders slide 4](slides/orders/orders-04.png)

![orders slide 5](slides/orders/orders-05.png)

![orders slide 6](slides/orders/orders-06.png)

![orders slide 7](slides/orders/orders-07.png)

## 7. Market design

| Design | What it means |
|---|---|
| Continuous market | Trades happen at any time during the session |
| Call market | Orders are collected and executed together at one time. NSE uses a call auction in its pre-open session |
| Quote-driven market | Dealers quote prices, and traders trade with dealers |
| Order-driven market | Rules match buy and sell orders directly |
| Circuit breaker | It halts trading after a large market move |

**Market quality** has five measures.

| No. | Measure |
|---|---|
| 1 | Liquidity |
| 2 | Transaction cost |
| 3 | Informative prices |
| 4 | Volatility |
| 5 | Trading profits |

![intro slide 24](slides/intro/intro-24.png)

![intro slide 25](slides/intro/intro-25.png)

![intro slide 26](slides/intro/intro-26.png)

![intro slide 30](slides/intro/intro-30.png)

## 8. ⭐ Volatility

Prices change for two reasons. New information arrives about values. Impatient traders also demand liquidity.

| Point | Fundamental volatility | Transitory volatility |
|---|---|---|
| Cause | Unanticipated changes in values | Trading by impatient uninformed traders |
| Life | Permanent | Temporary, because prices revert to value |
| Example | Earnings news | Bid-ask bounce and large uninformed orders |
| Who causes it | Informed traders move the price to the new value | Uninformed orders push the price away from value |
| Who ends it | Not applicable | Value traders and arbitrageurs push the price back |

| Point | What it says |
|---|---|
| Total volatility | Fundamental volatility plus transitory volatility |
| Dealers | They infer information from order flow. This creates the adverse selection part of the spread. Price changes from this part add to fundamental volatility |
| Bid-ask bounce | Market buyers trade at the ask and market sellers trade at the bid. So the price jumps without any news |

![volatility slide 2](slides/volatility/volatility-02.png)

![volatility slide 3](slides/volatility/volatility-03.png)

![volatility slide 4](slides/volatility/volatility-04.png)

![volatility slide 5](slides/volatility/volatility-05.png)

![volatility slide 6](slides/volatility/volatility-06.png)

![volatility slide 7](slides/volatility/volatility-07.png)

![volatility slide 8](slides/volatility/volatility-08.png)

![volatility slide 9](slides/volatility/volatility-09.png)

![volatility slide 10](slides/volatility/volatility-10.png)

## 9. ⭐ Inventory models and information models

| Point | Inventory models | Information models |
|---|---|---|
| Problem of the dealer | Unbalanced inventory | Better-informed customers |
| Source of the spread | Cost and risk of inventory | Expected loss to informed traders |
| Effect of a trade on price | Temporary | Permanent |
| Main papers | Garman, Amihud-Mendelson, Stoll, Ho-Stoll, O'Hara-Oldfield | Bagehot, Copeland-Galai, Glosten-Milgrom, Kyle, Easley-O'Hara |

## 10. ⭐ Roll (1984): the spread from prices

**Assumptions:**

| No. | Assumption |
|---|---|
| A1 | The value follows a random walk: $V_t=V_{t-1}+\varepsilon_t$. The news $\varepsilon_t$ has mean 0 and variance $\sigma^2$, and is independent over time |
| A2 | The spread $S$ is constant |
| A3 | The trade sign $Q_t$ is +1 for a buy and -1 for a sale, each with probability one half |
| A4 | Trade signs are independent over time and independent of news |

| Fact | Working | Why |
|---|---|---|
| $E[Q_t]=0$ | $\frac{1}{2}(1)+\frac{1}{2}(-1)$ | A3 |
| $E[Q_t^2]=1$ | $Q_t^2=1$ for both signs | A3 |
| $E[Q_tQ_{t-k}]=0$ for $k\ge 1$ | $E[Q_t]E[Q_{t-k}]=0\cdot 0$ | A4 |
| $E[\varepsilon_tQ_s]=0$ | $E[\varepsilon_t]E[Q_s]=0$ | A4 |

| Step | What we do |
|---|---|
| 1 | Write the trade price |
| 2 | Take the price change |
| 3 | Find the variance |
| 4 | Find the covariance |
| 5 | Solve for the spread |

**Step 1: Write the trade price.** A buy pays half a spread above value. A sale gets half a spread below value.

$$P_t=V_t+\frac{S}{2}Q_t$$

**Step 2: Take the price change.**

| Line | Expression | Why |
|---|---|---|
| 1 | $\Delta P_t=P_t-P_{t-1}$ | Definition |
| 2 | $=(V_t-V_{t-1})+\frac{S}{2}(Q_t-Q_{t-1})$ | Step 1 at $t$ and $t-1$ |
| 3 | $=\varepsilon_t+\frac{S}{2}\Delta Q_t$ | A1, and $\Delta Q_t=Q_t-Q_{t-1}$ |

$$\Delta P_t=\varepsilon_t+\frac{S}{2}(Q_t-Q_{t-1})$$

**Step 3: Find the variance.**

| Line | Expression | Why |
|---|---|---|
| 1 | $E[(\Delta Q_t)^2]=E[Q_t^2]-2E[Q_tQ_{t-1}]+E[Q_{t-1}^2]$ | Expand the square |
| 2 | $=1-0+1=2$ | Facts table |
| 3 | $\mathrm{Var}(\Delta P_t)=\mathrm{Var}(\varepsilon_t)+\frac{S^2}{4}E[(\Delta Q_t)^2]$ | The cross term is 0, since news is independent of signs |
| 4 | $=\sigma^2+\frac{S^2}{4}(2)$ | A1 and line 2 |

$$\mathrm{Var}(\Delta P_t)=\sigma^2+\frac{S^2}{2}$$

**Step 4: Find the covariance.**

| Line | Expression | Why |
|---|---|---|
| 1 | $\Delta P_{t-1}=\varepsilon_{t-1}+\frac{S}{2}(Q_{t-1}-Q_{t-2})$ | Step 2 one period earlier |
| 2 | News terms add 0 | $\varepsilon_t$ and $\varepsilon_{t-1}$ are independent of each other and of all signs |
| 3 | $\mathrm{Cov}=\frac{S^2}{4}E[(Q_t-Q_{t-1})(Q_{t-1}-Q_{t-2})]$ | Both means are 0, so the covariance is the mean of the product |
| 4 | $=\frac{S^2}{4}(E[Q_tQ_{t-1}]-E[Q_tQ_{t-2}]-E[Q_{t-1}^2]+E[Q_{t-1}Q_{t-2}])$ | Multiply out the four terms |
| 5 | $=\frac{S^2}{4}(0-0-1+0)$ | Facts table. Only the shared term $-Q_{t-1}^2$ survives |
| 6 | $=-\frac{S^2}{4}$ | Arithmetic |

$$\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})=-\frac{S^2}{4}$$

**Step 5: Solve for the spread.**

| Line | Expression | Why |
|---|---|---|
| 1 | $-\mathrm{Cov}=\frac{S^2}{4}$ | Multiply Step 4 by -1 |
| 2 | $S^2=-4\,\mathrm{Cov}$ | Multiply by 4 |
| 3 | $S=2\sqrt{-\mathrm{Cov}}$ | Take the positive root, since $S\gt 0$ |

$$S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$$

**Example:** The covariance is -0.0625.

| Step | Working | Result |
|---|---|---|
| 1 | $-\mathrm{Cov}=0.0625$ | 0.0625 |
| 2 | $\sqrt{0.0625}$ | 0.25 |
| 3 | $S=2(0.25)$ | 0.5 |

**Limits:**

| No. | Limit |
|---|---|
| 1 | The formula fails when the sample covariance is positive, since the root of a negative number is not real |
| 2 | It assumes that trades carry no information |
| 3 | It assumes a constant spread |

![volatility slide 11](slides/volatility/volatility-11.png)

![volatility slide 12](slides/volatility/volatility-12.png)

![volatility slide 13](slides/volatility/volatility-13.png)

![volatility slide 14](slides/volatility/volatility-14.png)

![volatility slide 15](slides/volatility/volatility-15.png)
