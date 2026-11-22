# Topic 5: Basic Concepts Discussed in Class

These notes are a short revision of the basic concepts from before the midsem. They come from the midsem notes of this course and from Harris, "Trading and Exchanges".

| Part | Main question |
|---|---|
| Microstructure | How does trading form a price? |
| Traders | Who trades and why? |
| Orders and market design | How do trades take place? |
| Liquidity | How easy is it to trade? |
| Cost | What does a trade really cost? |
| Volatility | Why do prices move? |
| Roll | How can we find the spread from prices alone? |

## 1. What market microstructure is

- **Definition:** It studies how the process and rules of trading affect prices, costs, volume and traders' behaviour.
- **Classical view:** Price equals value. Trading has no cost.
- **Microstructure view:** Price can differ from value because of cost, inventory, information and market rules.

Madhavan (2000) divides the subject into four areas.

1. Price formation and price discovery.
2. Market design.
3. Transparency.
4. Links to other areas of finance.

**Price discovery** is the process by which new information enters the price. Informed traders make prices informative. Uninformed traders make the market possible, and they pay for price discovery.

## 2. Who trades

| Group | Types | Why they trade |
|---|---|---|
| Utilitarian traders | Investors, borrowers, hedgers, asset exchangers and gamblers | They need a service other than profit from trading |
| Informed traders | Value traders, news traders, technical traders and arbitrageurs | They know or estimate value better |
| Parasitic traders | Order anticipators and bluffers | They profit from the orders of others |
| Dealers | Market makers and specialists | They sell immediacy and earn the spread |
| Futile traders | Traders who wrongly think that they have an edge | They expect a profit but lose |
| Agents | Brokers | They trade for clients and earn commission |

- **Buy side:** These firms and people buy the services of the exchange.
- **Sell side:** Dealers, brokers and broker-dealers sell those services.
- **Zero-sum game:** Relative to the market average, the gain of one trader is the loss of another.

## 3. Orders

| Order | Instruction | Benefit | Risk |
|---|---|---|---|
| Market | Trade now at the best available price | It is almost sure to execute | The price is uncertain |
| Limit | Trade at this price or better | The price is controlled | It may not execute |
| Marketable limit | A limit order that can execute now | It gives immediacy with a price cap | It may execute only partly |
| Stop | Become active when the price reaches a trigger | It limits a loss | The final price may be worse |

- **Liquidity demand:** A market order takes liquidity.
- **Liquidity supply:** A waiting limit order gives liquidity.
- **Adverse selection of limit orders:** A waiting order is most likely to execute when the news is against it.

## 4. Market design

| Point | Call market | Continuous market |
|---|---|---|
| When trades happen | At fixed times | At any time |
| Price | One price that maximizes volume | A different price for each trade |
| Immediacy | No | Yes |
| Strength | It pools orders and discovers price well | It is fast and flexible |
| Weakness | Traders must wait | Limit orders face more adverse selection |

| Point | Quote-driven market | Order-driven market |
|---|---|---|
| Counterparty | A dealer | Another trader |
| Price comes from | Dealer quotes | Rules that match orders |
| Liquidity comes from | Dealer capital | Limit orders |
| Example | Bond and currency dealers | NSE order book |

- **Pre-trade transparency:** Traders can see quotes and depth before they trade.
- **Post-trade transparency:** Traders can see prices and sizes after trades happen.
- **Circuit breaker:** It halts trading after a large move. Indian index limits are 10, 15 and 20 percent.

## 5. Liquidity

Liquidity is the ability to trade a large size, quickly, at low cost, when you want to.

| Dimension | Question | Measure |
|---|---|---|
| Immediacy | How fast can I trade? | Time to execution |
| Width | How much does a small trade cost? | Quoted and effective spread |
| Depth | How much can I trade at a given cost? | Shares at the quotes and in the book |
| Resiliency | How fast does the price recover? | Speed of return after a shock |

**Worked example:** Axis Bank has a bid of 664.40 for 453 shares. Its ask is 664.55 for 714 shares.

1. The quoted spread is $664.55-664.40=0.15$.
2. The mid price is $(664.55+664.40)/2=664.475$.
3. The proportional quoted spread is $0.15/664.475=0.000226$, which is 0.0226 percent.
4. The depth is $(714+453)/2=583.5$ shares.

> **Exam:** Volume is activity. Liquidity is the ease of trading. A crash can have high volume and low liquidity.

## 6. Transaction costs

| Kind | Cost | Meaning |
|---|---|---|
| Explicit | Commission | Payment to the broker |
| Explicit | Fees and taxes | Payments to the exchange and the government |
| Implicit | Spread | Cost of immediacy |
| Implicit | Price impact | The order moves the price against the trader |
| Implicit | Delay | The price moves before the trade is done |
| Implicit | Missed trade | The profit is lost because the order did not execute |

The spread has three economic parts.

1. **Order processing cost:** It pays for systems and labour.
2. **Inventory cost:** It pays for the risk of holding a position.
3. **Adverse selection cost:** It pays for losses to informed traders.

## 7. Inventory models and information models

| Point | Inventory models | Information models |
|---|---|---|
| Problem of the dealer | Unbalanced inventory | Better-informed customers |
| Source of the spread | Cost and risk of inventory | Expected loss to informed traders |
| Effect of a trade | Temporary | Permanent |
| Price change after a buy | It reverses | It stays, because beliefs changed |
| Is risk aversion needed? | In the Stoll and Ho-Stoll models | No |
| Main papers | Garman, Amihud-Mendelson, Stoll, Ho-Stoll, O'Hara-Oldfield | Bagehot, Copeland-Galai, Glosten-Milgrom, Kyle, Easley-O'Hara |

> **Exam:** An information spread exists even with zero processing cost, zero inventory cost and a risk-neutral dealer.

## 8. Volatility

| Point | Fundamental volatility | Transitory volatility |
|---|---|---|
| Cause | News about value | Demand for liquidity by uninformed traders |
| Life | Permanent | Temporary |
| Price pattern | Random walk | Reversal |
| Serial correlation | Near zero | Negative |
| Example | An earnings surprise | Bid-ask bounce or a large forced sale |

- **News traders:** They add fundamental volatility by moving the price to its new value.
- **Value traders:** They reduce transitory volatility by trading against a wrong price.
- **Bid-ask bounce:** Trades move between bid and ask even when value does not change.

## 9. Roll (1984): the spread from prices

### 9.1 Setup

- **A1:** The mid value follows $V_t=V_{t-1}+\varepsilon_t$. The news term $\varepsilon_t$ has mean zero, has variance $\sigma^2$ and is independent over time.
- **A2:** The spread $S$ is constant.
- **A3:** The trade sign $Q_t$ is +1 for a buy and -1 for a sell, each with probability one half.
- **A4:** Trade signs are independent over time and independent of news. So trades carry no information.

### 9.2 Derivation

**Step 1: Write the trade price.**

$$P_t=V_t+\frac{S}{2}Q_t$$

**Step 2: Subtract the previous price.**

$$\Delta P_t=\varepsilon_t+\frac{S}{2}(Q_t-Q_{t-1})$$

**Step 3: Find the variance of the sign change.** Each sign has variance 1 and the two signs are independent by A3 and A4.

$$E[(\Delta Q_t)^2]=1+1=2$$

**Step 4: Find the variance of the price change.** News is independent of signs by A4.

$$\mathrm{Var}(\Delta P_t)=\sigma^2+\frac{S^2}{4}(2)=\sigma^2+\frac{S^2}{2}$$

**Step 5: Multiply two neighbouring sign changes.**

$$\Delta Q_t\Delta Q_{t-1}=Q_tQ_{t-1}-Q_tQ_{t-2}-Q_{t-1}^2+Q_{t-1}Q_{t-2}$$

**Step 6: Take the expectation.** The three products of different signs have mean zero. The square has mean 1.

$$E[\Delta Q_t\Delta Q_{t-1}]=0-0-1+0=-1$$

**Step 7: Find the covariance.** The news terms drop out by A1 and A4.

$$\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})=\frac{S^2}{4}(-1)=-\frac{S^2}{4}$$

**Step 8: Solve for the spread.** Multiply by -4 and take the square root.

$$S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$$

**Worked example:** The covariance is -0.0625. The spread is $2\sqrt{0.0625}=0.5$.

### 9.3 Limits

- **Positive covariance:** The formula has no real answer.
- **No information:** The model ignores adverse selection.
- **Constant spread:** Real spreads change during the day.

> **Exam:** The negative covariance comes from the bid-ask bounce. Keep the minus sign inside the root.
