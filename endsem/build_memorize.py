"""Build memorize.pdf: the five topic notes word for word, plus memory boxes.

The notes are not changed. This script copies them, adds hook boxes, proof
maps and formula boxes at fixed headings, and runs pandoc.
Run from endsem/: python3 build_memorize.py
"""
import re
import subprocess

FILES = [
    "1-information-based-models.md",
    "2-liquidity-measures.md",
    "3-extreme-illiquidity.md",
    "4-market-wide-liquidity.md",
    "5-basic-concepts.md",
]


def hook(title, body):
    return f'::: {{.hook title="{title}"}}\n{body.strip()}\n:::\n'


def pmap(body):
    return f"::: map\n{body.strip()}\n:::\n"


def fbox(title, body):
    return f'::: {{.box title="{title}"}}\n{body.strip()}\n:::\n'


HEADER = r"""---
title: "Market Microstructure Endsem: Notes with Memory Tricks"
geometry: margin=1.8cm
fontsize: 10pt
header-includes:
  - \usepackage[most]{tcolorbox}
---

**How to use this PDF.** The text is the five topic notes, word for word. Three kinds of box are added to them.

- A blue **Hook** box gives a trick to remember a list, a number or an equation.
- A green **Proof map** box comes just before a long proof. It gives the whole proof as a few moves, with no intermediate steps. Read the map first. Then read the full proof under it.
- An orange **Formula** box holds the formulas that you need for numericals.

The last page collects every formula box on one sheet.

**Read first:** Topic 1, Section 7 (Easley and O'Hara), and all of Topic 2. You have not read these yet.

""" + hook("The whole course in five sentences", r"""
1. Informed traders make the dealer charge a spread, and their trades move the price. This is Topic 1.
2. Liquidity measures tell us how large these trading costs are. This is Topic 2.
3. Limits on funding can turn a small loss into extreme illiquidity. This is Topic 3.
4. Common funding and strategic selling spread illiquidity across the whole market. This is Topic 4.
5. Illiquidity lowers prices and raises the return that investors demand. This is in Topics 2 and 3.

Remember the chain: **Inform, Measure, Fund, Spread across, Price.**
""")

MERMAID = {
    "1-information-based-models.md": r"""
**The tree of events (from the slide diagram):**

1. Before trading, an information event happens with probability $\alpha$. No event happens with probability $1-\alpha$.
2. After an event, the signal is low with probability $\delta$. It is high with probability $1-\delta$.
3. After a low signal, the informed share $\mu$ of traders sells.
4. After a high signal, the informed share $\mu$ of traders buys.
5. With no event, all traders are uninformed.
""",
    "3-extreme-illiquidity.md": r"""
**The loop (from the slide diagram):**

1. Initial losses cause funding problems for speculators.
2. Funding problems force speculators to reduce their positions.
3. Reduced positions push prices away from fundamentals.
4. Prices away from fundamentals cause higher margins. This is the margin spiral.
5. Prices away from fundamentals also cause losses on existing positions. This is the loss spiral.
6. Both spirals lead back to funding problems, so the loop starts again.
""",
}

# (file, heading prefix, "after" or "before", text)
INSERTS = [
    # ---------------- Topic 1 ----------------
    ("1", "## 2. The five theories", "after", hook("The five theories: the dealer WOBLS", r"""
Each model adds one new thing. The first letters spell **WOBLS**, so remember that "the dealer wobbles".

- **W**ords: Bagehot (1971) gives the idea in words only, with no equation.
- **O**ption: Copeland and Galai (1983) treat the quotes as free options.
- **B**ayes: Glosten and Milgrom (1985) let the dealer learn from each trade by Bayes rule.
- **L**ambda: Kyle (1985) lets a strategic insider choose the order size, and the price impact is $\lambda$.
- **S**ize: Easley and O'Hara (1987) let traders choose between two sizes.

The years climb through odd numbers: 71, 83, 85, 85, 87. The two 1985 papers are twins. Glosten and Milgrom is sequential with one unit per trade. Kyle is a batch auction with a chosen size.
""")),
    ("1", "## 3. Bagehot", "after", hook("Bagehot: 2-2-1", r"""
Remember **2-2-1**.

- There are **two gains**. The market gain can be earned by everyone. The trading gain cannot be earned by everyone.
- There are **two traders**. The dealer loses to the informed trader. The dealer recovers that loss from the uninformed trader.
- There is **one balance**. The spread balances the loss and the gain.
""")),
    ("1", "### 4.1 The idea", "after", hook("Copeland and Galai: Ask is a Call, Bid is a Put", r"""
The ask is a free call option with strike $P_A$. The informed trader exercises it, by buying, when the true price $P$ is above $P_A$.

The bid is a free put option with strike $P_B$. The informed trader exercises it, by selling, when $P$ is below $P_B$.

The objective is **"Gain from the Uninformed, Lose to the Informed"**: $(1-\pi_I)G_U-\pi_I L_I$. Each term is weighted by the probability of its own trader type.
""")),
    ("1", "### 4.4", "after", pmap(r"""
1. The informed trader uses the free options. So the expected loss $L_I$ is the expected payoff of the call at $P_A$ plus the expected payoff of the put at $P_B$.
2. The uninformed trader pays half the spread on each trade. So the gain is $G_U=\pi_{BL}(P_A-P_0)+\pi_{SL}(P_0-P_B)$.
3. The dealer weights each part by the chance of that trader type. Then the dealer chooses $P_A$ and $P_B$ to maximize $(1-\pi_I)G_U-\pi_I L_I$.
4. A wider spread lowers the option loss and raises the gain per uninformed trade. But a wider spread also drives uninformed traders away. This stops the spread from growing without limit.
5. Competition pushes the profit to zero. In the symmetric example, this gives the half-spread $h=\pi_I\Delta$.
""")),
    ("1", "### 4.6", "after", hook("Findings: PV up, ADC down", r"""
The spread rises with the **P**rice level and the **V**ariance of the return. The spread falls with market **A**ctivity, **D**epth and **C**ontinuity.

There are two limitations. The model has only one period. The information is revealed at once by the trade.
""")),
    ("1", "## 5. Glosten and Milgrom", "before", fbox("Formulas: Copeland and Galai", r"""
Use this for the symmetric example. The value is $P_0\pm\Delta$ with equal chance. The quotes are $P_0\pm h$. Every uninformed trader trades, so $\pi_{BL}=\pi_{SL}=0.5$.

1. The gain from an uninformed trader is $G_U=h$.
2. The loss to an informed trader is $L_I=\Delta-h$.
3. Zero profit means $(1-\pi_I)h=\pi_I(\Delta-h)$. This gives $h=\pi_I\Delta$.

The example has $\Delta=10$ and $\pi_I=0.2$. So $h=2$, the ask is 102, the bid is 98, and the spread is 4.
"""))
    ,
    ("1", "### 5.1 The idea", "after", hook("Glosten and Milgrom: quote what you would believe after the trade", r"""
The ask is $E[V\mid\text{buy}]$. The bid is $E[V\mid\text{sale}]$. The dealer quotes what they would believe after the trade, so they never regret the quote. This is why the quotes are called regret free.

Remember **"tilt, then normalise"**. Start from the prior. A buy multiplies the good state by $(1+\mu)$ and the bad state by $(1-\mu)$. A sale swaps the two. Then divide by the sum.

Remember **"$\theta$ for trouble"**: $\theta=\Pr(V_L)$. Write this in the first line of your answer, because the slides switch its meaning.
""")),
    ("1", "### 5.6", "after", pmap(r"""
1. In the good state, all insiders buy and half of the uninformed buy. So a buy has probability $\tfrac12(1+\mu)$. In the bad state, only half of the uninformed buy. So a buy has probability $\tfrac12(1-\mu)$.
2. Bayes rule multiplies the prior by these likelihoods. The $\tfrac12$ cancels. After a buy, the weights are $\theta(1-\mu)$ on $V_L$ and $(1-\theta)(1+\mu)$ on $V_H$. After a sale, the weights are $\theta(1+\mu)$ and $(1-\theta)(1-\mu)$.
3. Each quote is the weighted average of the two values. The buy weights add to $1+\mu(1-2\theta)$, and the sale weights add to $1-\mu(1-2\theta)$:
$$a=\frac{\theta(1-\mu)V_L+(1-\theta)(1+\mu)V_H}{1+\mu(1-2\theta)},\qquad b=\frac{\theta(1+\mu)V_L+(1-\theta)(1-\mu)V_H}{1-\mu(1-2\theta)}$$
4. The ask minus the bid gives the spread:
$$s=\frac{4\theta(1-\theta)\mu(V_H-V_L)}{1-(1-2\theta)^2\mu^2}$$
When $\theta=0.5$, the spread is $s=\mu(V_H-V_L)$.
5. The spread is positive with zero cost and zero profit. So the whole spread is adverse selection.
""") + hook("The spread formula in words", r"""
The spread is **4 times the coin, times the insider share, times the range, divided by the product of the two denominators**.

The coin is $\theta(1-\theta)$. The product of the two denominators is $1-(1-2\theta)^2\mu^2$.

With a fair coin, $\theta=0.5$, the spread is simply the insider share times the range.
""")),
    ("1", "### 5.8", "before", fbox("Formulas: Glosten and Milgrom. Learn one grid, and read every formula off it", r"""
**Step 1: draw the grid.** The columns are the two values with their priors. The rows are the two trades.

$$\begin{array}{l|cc|c}
 & V_L\ \ (\text{prior }\theta) & V_H\ \ (\text{prior }1-\theta) & \text{Row sum}\\ \hline
\text{Buy (gives the ask)} & \theta(1-\mu) & (1-\theta)(1+\mu) & R_B=1+\mu(1-2\theta)\\
\text{Sale (gives the bid)} & \theta(1+\mu) & (1-\theta)(1-\mu) & R_S=1-\mu(1-2\theta)
\end{array}$$

**Step 2: fill the signs with one rule.** The state that agrees with the trade gets $1+\mu$. The other state gets $1-\mu$. A buy agrees with good news, so $V_H$ gets the plus. A sale agrees with bad news, so $V_L$ gets the plus.

The plus signs sit on **Buy-High** and **Sale-Low**. Remember it as **"Buy High, Sell Low gets the plus"**. In trading this is the worst rule there is. Here it is exactly right, and that is why it sticks.

**Step 3: read every formula off the grid.**

1. **Ask** = the average of $V_L$ and $V_H$ with the Buy row as weights: $a=(\text{left}\cdot V_L+\text{right}\cdot V_H)/R_B$.
2. **Bid** = the same average with the Sale row: $b=(\text{left}\cdot V_L+\text{right}\cdot V_H)/R_S$.
3. **Probability of a buy** = half the Buy row sum: $\Pr(B)=\tfrac12R_B$. **Probability of a sale** = half the Sale row sum: $\Pr(S)=\tfrac12R_S$. The two row sums add to 2, so the halves add to 1.
4. **New $\theta$ after a buy** = the left cell of the Buy row over its sum: $\theta(1-\mu)/R_B$. Use it to draw the next grid.
5. **Spread** = **"4 coins, mu, range, over the two row sums"**:
$$s=\frac{4\cdot\theta(1-\theta)\cdot\mu\cdot(V_H-V_L)}{R_B\cdot R_S}$$
The coin is $\theta(1-\theta)$. When $\theta=\tfrac12$, both row sums are 1, so $s=\mu(V_H-V_L)$.
6. **Check:** $\Pr(B)\,a+\Pr(S)\,b$ must equal the prior mean. This is the martingale property.

**Example.** $V_H=110$, $V_L=90$, $\theta=0.3$, $\mu=0.4$. The Buy row is $0.18,\ 0.98$, with sum 1.16. The Sale row is $0.42,\ 0.42$, with sum 0.84.
Ask $=(0.18\cdot 90+0.98\cdot 110)/1.16=106.897$. Bid $=(0.42\cdot 90+0.42\cdot 110)/0.84=100$. $\Pr(B)=0.58$.
Spread $=4(0.21)(0.4)(20)/(1.16\cdot 0.84)=6.72/0.9744=6.897$. Check: $0.58(106.897)+0.42(100)=104$, the prior mean.
""")),
    ("1", "### 5.8", "after", hook("Findings: ZLMS", r"""
- **Z**ero profit: the dealer puts the adverse-selection cost into the spread.
- **L**earning: beliefs and quotes update with each trade.
- **M**artingale: the best forecast of the next price is the present price.
- **S**emi-strong efficiency: public information cannot predict the future price better.

Compare with Copeland and Galai. Their spread comes from expected gains and losses. The Glosten and Milgrom spread comes from beliefs given each trade.
""")),
    ("1", "### 6.1", "after", hook("Kyle: the insider hides perfectly, and everything is a half", r"""
At the equilibrium, the insider's order has the **same variance as the noise**: $\beta^2\sigma_0^2=\sigma_y^2$. So half of the order flow is information, and half of the information enters the price.

- $\lambda=\dfrac{\sigma_0}{2\sigma_y}$. Remember **"information over twice the noise"**.
- $\beta=\dfrac{\sigma_y}{\sigma_0}$. Remember **"flip $\lambda$ and drop the 2"**.
- $E[\pi_I]=\dfrac{\sigma_0\sigma_y}{2}$. Remember **"multiply the two, then halve"**.
""")),
    ("1", "### 6.4", "after", pmap(r"""
1. **The insider responds.** The expected profit is $x(v-\mu-\lambda x)$. Setting the derivative to zero gives $x=(v-\mu)/2\lambda$. So the insider's slope is $\beta=1/2\lambda$.
2. **The dealer responds.** The price is the regression of $v$ on the order flow $z$. So $\lambda=\mathrm{Cov}(v,z)/\mathrm{Var}(z)=\beta\sigma_0^2/(\beta^2\sigma_0^2+\sigma_y^2)$.
3. **The two responses meet.** Putting $\beta=1/2\lambda$ into the dealer's rule gives $\lambda^2\sigma_y^2=\sigma_0^2/4$. So $\lambda=\sigma_0/2\sigma_y$, $\beta=\sigma_y/\sigma_0$ and $\mu=p_0$.
4. **The insider hides.** With these values, $\beta^2\sigma_0^2=\sigma_y^2$. So the order flow has variance $2\sigma_y^2$, and the variance left after trading is $\sigma_0^2/2$.
5. **The noise traders pay.** The insider earns $\sigma_0\sigma_y/2$ on average. The noise traders lose $\lambda\sigma_y^2=\sigma_0\sigma_y/2$. The dealer earns zero.
""")),
    ("1", "### 6.5", "after", hook("What changes what: profit likes both, lambda likes only information", r"""
- When $\sigma_0$ rises, $\lambda$ rises and the insider's profit rises. There is more private information, so the market is less liquid.
- When $\sigma_y$ rises, $\lambda$ falls and the insider's profit rises. More noise hides the insider, so the market is deeper.
""")),
    ("1", "### 6.7", "before", fbox("Formulas: Kyle. The units write the formulas, and three halves finish them", r"""
**Trick 1: the units tell you which way up each ratio goes.** $\sigma_0$ is measured in price. $\sigma_y$ is measured in shares.

- $\lambda$ is the price change per share. Price over shares is $\sigma_0/\sigma_y$.
- $\beta$ is the number of shares per unit of price gap. Shares over price is $\sigma_y/\sigma_0$.
- The profit is price times shares. So it is built from $\sigma_0\sigma_y$.
- The variance left is a price squared. So it is built from $\sigma_0^2$.

You never have to remember which one is on top. The units decide it.

**Trick 2: three halves.** The only extra thing to remember is where the halves go.

1. $\lambda\cdot\beta=\tfrac12$. This comes from the insider's best response, $\beta=1/2\lambda$. The insider trades only half as hard as the price impact allows. So the 2 sits under $\lambda$: $\lambda=\dfrac{\sigma_0}{2\sigma_y}$ and $\beta=\dfrac{\sigma_y}{\sigma_0}$.
2. The expected profit is half of price times shares: $E[\pi_I]=\tfrac12\sigma_0\sigma_y$.
3. The variance left after trading is half of the prior variance: $\mathrm{Var}(v\mid z)=\tfrac12\sigma_0^2$.

**Trick 3: what the noise traders lose, the insider wins.** The noise loss is $\lambda\sigma_y^2=\tfrac12\sigma_0\sigma_y$, which is the same number as the profit. The dealer earns zero.

**The trade itself, in the order it happens.**

1. The insider sends $x=\beta(v-p_0)$.
2. The dealer sees the order flow $z=x+y$.
3. The dealer sets the price $p=p_0+\lambda z$.
4. The realized profit is $x(v-p)$.

**Example.** $p_0=100$, $\sigma_0=10$, $\sigma_y=1000$, $v=110$, $y=-400$. Then $\lambda=10/2000=0.005$ and $\beta=1000/10=100$. Check: $\lambda\beta=0.5$. The order is $x=100(10)=1000$. The flow is $z=600$. The price is $p=100+0.005(600)=103$. The realized profit is $1000(110-103)=7000$. The expected profit is $\tfrac12(10)(1000)=5000$. The variance left is $\tfrac12(100)=50$.
""")),
    ("1", "### 7.2", "after", hook("Three Greek letters: Alpha Arrives, Delta Decides, Mu Many", r"""
- $\alpha$ is the chance that an information event **arrives** before the day.
- $\delta$ is the chance that the signal is **low**, which is bad news.
- $\mu$ is the share of traders who are informed **after an event**.

The key product is $\alpha\mu$. It is the chance that a random trader is informed. So $1-\alpha\mu$ is the chance that a random trader is uninformed.
""")),
    ("1", "### 7.4", "after", hook("Two equilibria: few informed means Fork, many informed means Mix", r"""
**Separating (few informed, a fork).** The informed trade only the large size. So small trades are safe, and $a_1=b_1=V^{\ast}$. Only large trades carry a spread.

**Pooling (many informed, a mix).** The informed trade both sizes. The dealer cannot tell the types apart. So both sizes carry a spread.
""")),
    ("1", "### 7.5", "after", pmap(r"""
1. Two groups sell large. The uninformed sellers have weight $X_S^2(1-\alpha\mu)$, and they are worth $V^{\ast}$ on average. The informed sellers, after an event and a low signal, have weight $\alpha\delta\mu$, and they are worth $\underline{V}$.
2. The large bid is the weighted average of these two values. This is the Glosten and Milgrom rule again:
$$b_2=\frac{X_S^2(1-\alpha\mu)\,V^{\ast}+\alpha\delta\mu\,\underline{V}}{X_S^2(1-\alpha\mu)+\alpha\delta\mu}$$
3. Writing $V^{\ast}-\underline{V}$ with the variance $\sigma_v^2$ turns this into the slide's form:
$$b_2^{\ast}=V^{\ast}-\frac{\sigma_v^2}{\bar{V}-\underline{V}}\cdot\frac{\alpha\mu}{X_S^2(1-\alpha\mu)+\delta\alpha\mu}$$
The large ask is the same, with buyers, $X_B^2$ and $(1-\delta)$ in place of $\delta$.
4. Separation holds only if the informed buyer prefers the large size: $B^2(\bar{V}-a_2)\ge B^1(\bar{V}-V^{\ast})$. This gives
$$\frac{B^2}{B^1}\ge 1+\frac{\alpha\mu(1-\delta)}{X_B^2(1-\alpha\mu)}$$
If this fails, the informed also trade small, and the result is pooling.
""") + hook("The large bid in words: pulled down by the informed share", r"""
Call the uninformed large sellers $U$ and the informed large sellers $I$. Then the large bid is
$$b_2=V^{\ast}-\frac{I}{U+I}\,(V^{\ast}-\underline{V})$$
In words, **the bid starts at $V^{\ast}$ and is pulled toward the bad value by the informed share of the large sellers.** This is the same as the slide's formula. The $\delta$ inside $I$ and the $(1-\delta)$ inside $V^{\ast}-\underline{V}$ multiply to the $\sigma_v^2/(\bar{V}-\underline{V})$ on the slide.
""")),
    ("1", "### 7.8", "after", hook("Price path: known event means stuck, unsure event means bounce part way", r"""
At time $t$, a small trade happens at $V^{\ast}$. At $t+1$, a block sale pushes the price down to $b_2$.

- If the event is **known** (Figure 1), a small trade at $t+2$ says nothing new. So the price **stays** at $b_2$.
- If the event is **uncertain** (Figure 2), only the uninformed trade small. So a small trade makes "no event" more likely. The price **recovers part way**, but it stays below $V^{\ast}$.
""")),
    ("1", "### 7.10", "before", fbox("Formulas: Easley and O'Hara. Two weights, U and I, give everything", r"""
**Trick 1: the informed weight is the tree, read in time order.** First an event arrives ($\alpha$). Then the signal is decided ($\delta$ for low). Then the informed trade ($\mu$). Multiply down the branch:

- Informed large **sellers**: $I_S=\alpha\cdot\delta\cdot\mu$.
- Informed large **buyers**: $I_B=\alpha\cdot(1-\delta)\cdot\mu$.

**Trick 2: the uninformed weight is "wants large, times is uninformed".**

- Uninformed large sellers: $U_S=X_S^2\cdot(1-\alpha\mu)$.
- Uninformed large buyers: $U_B=X_B^2\cdot(1-\alpha\mu)$.

Here $1-\alpha\mu$ is the chance that a random trader is uninformed.

**Trick 3: every quote is "start at $V^{\ast}$, then get pulled by the informed share".**

1. $V^{\ast}=\delta\underline{V}+(1-\delta)\bar{V}$. This is the plain expected value.
2. Large bid: $b_2=V^{\ast}-\dfrac{I_S}{U_S+I_S}(V^{\ast}-\underline{V})$. It is pulled **down** toward the bad value.
3. Large ask: $a_2=V^{\ast}+\dfrac{I_B}{U_B+I_B}(\bar{V}-V^{\ast})$. It is pulled **up** toward the good value.
4. Small quotes (separating): nobody informed trades small, so the pull is zero, and $a_1=b_1=V^{\ast}$.

**Trick 4: separation means "the size ratio must beat the crowd ratio".**
$$\frac{B^2}{B^1}\ \ge\ \frac{U_B+I_B}{U_B}=1+\frac{\alpha\mu(1-\delta)}{X_B^2(1-\alpha\mu)}$$
Why: in a large trade, the informed buyer's profit per share shrinks to the uninformed share $U_B/(U_B+I_B)$ of the small-trade profit. So the large size must be big enough to make up for it.

**Trick 5: the variance is "coin times range squared".** $\sigma_v^2=\delta(1-\delta)(\bar{V}-\underline{V})^2$. The coin $\delta(1-\delta)$ is the same kind of coin as $\theta(1-\theta)$ in Glosten and Milgrom.

**Small trade after a block sale.** Take the three state weights after the block sale. Multiply each by the chance that the trader is uninformed: $1-\mu$ after an event, and 1 with no event. Then average the values with these weights.

**Example.** $\bar{V}=110$, $\underline{V}=90$, $\delta=\alpha=0.5$, $\mu=0.4$, $X=0.25$. Then $V^{\ast}=100$, $1-\alpha\mu=0.8$, $U=0.25(0.8)=0.2$ and $I=0.5(0.5)(0.4)=0.1$. The informed share is $0.1/0.3=1/3$.
Large bid $=100-\tfrac13(10)=96.667$. Large ask $=100+\tfrac13(10)=103.333$. Small quotes are 100. Separation needs $B^2/B^1\ge 0.3/0.2=1.5$.
""")),
    ("1", "### 7.10", "after", hook("Findings: BQIO", r"""
- **B**lock trades move prices, because of informed trading.
- **Q**uantity is correlated with private information.
- **I**nformed traders prefer larger amounts at any given price.
- **O**ptimal pricing depends on quantity. Prices of large trades show a higher probability of informed trading.
""")),
    ("1", "## 8.", "after", hook("Recognize the model from one word", r"""
- The word "option" points to Copeland and Galai.
- The words "regret free", "Bayes" or "sequential" point to Glosten and Milgrom.
- The words "batch", "strategic" or "order flow" point to Kyle.
- The words "size", "block" or "event uncertainty" point to Easley and O'Hara.
""")),

    # ---------------- Topic 2 ----------------
    ("2", "## 1. Background", "before", hook("Five papers: CALIS", r"""
Each paper answers one question. The first letters spell **CALIS**.

- **C**hordia (2000) asks whether liquidity moves together. The answer is yes, which is commonality.
- **A**mihud (2002) asks whether illiquidity is priced. The answer is yes: illiquid stocks pay higher returns.
- **L**esmond (2005) asks which measure works in emerging markets. LOT and Roll work best across countries.
- **I**nce (2022) asks which part of illiquidity is priced. The idiosyncratic part predicts returns.
- **S**toll (2000) asks what causes friction. Friction has a real part and an informational part.
""")),
    ("2", "### 2.2", "after", hook("Seven reasons: PVIVP, plus F, plus I", r"""
The first five letters read the same both ways, like a palindrome. All five are **inventory** reasons.

- **P**rice swings make market-wide trading respond.
- **V**olume drives dealer inventories together.
- **I**nterest rates set the cost of carrying inventory.
- **V**olatility gives inventory risk a market part.
- **P**rogram trading puts common pressure on many inventories.

Then come two more. **F**unds: institutional funds with similar styles trade alike. **I**nformation: a few large traders may know about many stocks.
""")),
    ("2", "### 2.4", "after", hook("Data: 92, 1169, 254, two dollars", r"""
Remember four numbers in order. The data is NYSE (ISSM) for the year **1992**. There are **1,169** stocks. There are **254** trading days. Stock-days with a price below **\$2** are deleted.
""")),
    ("2", "### 2.5", "after", hook("Five measures: quoted uses the mid, effective uses the trade price and has a 2", r"""
The quoted spreads use the mid quote. The effective spreads use the trade price, and they carry a factor of 2.

Depth is the **only** measure where a higher value means **more** liquid.
""")),
    ("2", "### 2.8", "after", hook("Test 1: one number, 0.69, and one range, 69 to 85", r"""
The quoted-spread coefficient on the same day is **0.69**. So a 1 percent change in the market spread goes with a 0.69 percent change in the stock's spread.

Between **69 and 85** percent of stocks have a positive coefficient. The same-day coefficient is much larger than the lag and the lead.
""")),
    ("2", "### 2.12", "after", hook("Conclusion: together, own trades widen, market trades tighten", r"""
1. **Together.** The liquidity of individual stocks moves together.
2. **Own trades widen.** A stock's spread rises with its own number of trades. This is asymmetric information.
3. **Market trades tighten.** The spread falls with market-wide trading. That trading is mostly uninformed and balances inventory.
""")),
    ("2", "## 3. Amihud", "before", fbox("Formulas: Chordia, Roll and Subrahmanyam", r"""
1. Quoted spread: QSPR $=P_A-P_B$.
2. Proportional quoted spread: PQSPR $=(P_A-P_B)/P_M$.
3. Depth: DEP $=(Q_A+Q_B)/2$.
4. Effective spread: ESPR $=2\lvert P_t-P_M\rvert$.
5. Proportional effective spread: PESPR $=2\lvert P_t-P_M\rvert/P_t$.
6. Daily change: $DL_t=(L_t-L_{t-1})/L_{t-1}$.
7. Test 1: $DL_{j,t}=\alpha_j+\beta_jDL_{M,t}+\varepsilon_{j,t}$.

Example: the bid is 99.80, the ask is 100.20, a buy happens at 100.10, and the depth is 600 at the bid and 400 at the ask. Then QSPR $=0.40$, $P_M=100$, PQSPR $=0.004$, DEP $=500$, ESPR $=0.20$ and PESPR $=0.002$.
""")),
    ("2", "### 3.2", "after", hook("ILLIQ: absolute return per dollar, ratio first, then average", r"""
For each day, divide the absolute return by the dollar volume. Then take the average of these daily ratios over the year. Do not divide the average return by the average volume.

A higher ILLIQ means **less** liquid. Amivest is the upside-down cousin: total volume over total absolute return. A higher Amivest means **more** liquid.
""")),
    ("2", "### 3.4", "after", hook("Data: NYSE 63 to 97, 408 months, Fama-MacBeth", r"""
The data is NYSE stocks from 1963 to 1997, from CRSP. Returns are adjusted for delisting (Shumway 1997). The characteristics come from year $y-1$.

Fama-MacBeth has three steps. Run one cross-section regression each month. Save the coefficients. Average them over the 408 months, and test the average against zero.
""")),
    ("2", "### 3.5", "after", hook("Findings: Expected means Extra return later, Unexpected means Ugly return now", r"""
- **Expected** market illiquidity raises the expected excess return later.
- **Unexpected** illiquidity raises the required return at once. So the price $D/r$ falls, and the return now is negative.
- Both effects are stronger for **small** firms. This is the flight to liquidity.
""")),
    ("2", "## 4. Ince", "before", fbox("Formulas: Amihud", r"""
1. ILLIQ is the yearly average of the daily ratio $\lvert R_d\rvert/VOLD_d$. Always state the unit.
2. Amivest $=\sum VOLD_d/\sum\lvert R_d\rvert$.
3. A surprise in illiquidity: with a dividend $D$ forever, the price is $P=D/r$. A higher $r$ lowers the price now.

Example: returns $0.02,-0.01,0.03$ and volumes 10, 5 and 10 million dollars. The ratios are $0.002,0.002,0.003$. ILLIQ $=0.002333$ per million dollars. Amivest $=25/0.06=416.67$.
Surprise example: $D=5$. At $r=10\%$, $P=50$. At $r=12.5\%$, $P=40$. The return now is $-20\%$.
""")),
    ("2", "### 4.1", "after", hook("Ince: ASI, and only I survives", r"""
Monthly firm illiquidity has three parts: **A**lpha (a constant for the firm), **S**ystematic (moves with the market) and **I**diosyncratic (specific to the firm).

The systematic premium disappears once very small stocks are removed. The idiosyncratic part predicts returns.
""")),
    ("2", "### 5.4", "after", hook("LOT: the no-trade band", r"""
An investor trades only if the value of the news beats the trading cost. Inside the band $[\alpha_1,\alpha_2]$, nobody trades, so the observed return is **zero**.

So **many zero-return days mean a high cost**. The width of the band is the round-trip cost: $LOT=\alpha_2-\alpha_1$.
""") + pmap(r"""
1. The true return follows the market model: $R^{\ast}_{jt}=\beta_jR_{mt}+\varepsilon_{jt}$.
2. Below the band, the observed return is $R^{\ast}-\alpha_1$. Inside the band, it is 0. Above the band, it is $R^{\ast}-\alpha_2$.
3. Maximum likelihood over the three kinds of days picks $\alpha_1$, $\alpha_2$, $\beta$ and the error variance.
4. The selling cost $-\alpha_1$ plus the buying cost $\alpha_2$ gives the round-trip cost $LOT=\alpha_2-\alpha_1$.
""")),
    ("2", "### 5.5", "after", hook("Findings: across countries LOT and Roll, within a country LOT then Amihud", r"""
1. Across countries, the price-based measures LOT and Roll work best.
2. Within a country, LOT works best, and Amihud works to a lesser extent.
3. Weak political and legal institutions mean a higher liquidity cost.
4. More political risk adds 10 basis points of cost by LOT and 1.9 percent of price impact by Amihud.
5. Politics beats law: political risk looks stronger than the information risk from legal institutions.
""")),
    ("2", "## 6. Stoll", "before", fbox("Formulas: LOT", r"""
1. $LOT=\alpha_2-\alpha_1$.
2. The observed return is $R^{\ast}-\alpha_2$ above the band, $R^{\ast}-\alpha_1$ below it, and 0 inside it.

Example: $\alpha_1=-0.010$ and $\alpha_2=0.015$. So LOT $=0.025$, or 2.5 percent. A true return of 0.025 is observed as 0.010. A true return of 0.007 is observed as 0. A true return of $-0.018$ is observed as $-0.008$.
""")),
    ("2", "### 6.1", "after", hook("Two views of friction: time or price, and Stoll pays the price", r"""
Friction can be seen as time (Lippman and McCall) or as price (Demsetz). Stoll uses the price view. Friction is the price concession paid for immediacy.
""")),
    ("2", "### 6.3", "after", hook("Signs: volume and price shrink it, variance grows it, MV and N flip by market", r"""
- $\log V$ has a negative sign, because inventory is easier to unload.
- $\sigma^2$ has a positive sign, because of inventory risk.
- $\log P$ has a negative sign, because a fixed cost is spread over a higher price.
- $\log MV$ and $\log N$ are positive on NYSE and AMSE, and negative on Nasdaq.

The adjusted $R^2$ is 0.77 for NYSE and AMSE, and 0.65 for Nasdaq.
""")),
    ("2", "### 6.4", "after", hook("Two kinds of friction: real and informational", r"""
**Real** friction uses up resources: labour, systems, and capital to bear inventory risk. **Informational** friction moves wealth from the less informed to the better informed.
""") + fbox("Formulas: Stoll", r"""
1. Stoll uses **half**-spreads. The quoted half-spread is $S=(A-B)/2$. The effective half-spread is $ES=\lvert P-M\rvert$.
2. Chordia uses **full** spreads. So Chordia's effective spread is 2 times Stoll's.
""")),

    # ---------------- Topic 3 ----------------
    ("3", "### 2.1", "after", hook("Market liquidity belongs to the asset, funding liquidity belongs to the trader", r"""
Market liquidity asks whether an asset can be sold easily near its true value. Funding liquidity asks whether a trader can get money to hold a position. Each one feeds the other, so they can form a spiral.
""")),
    ("3", "### 2.2", "after", hook("X is at most W over m", r"""
Own capital must pay the margin share $m$ of the position. So $mX\le W$, which gives $X\le W/m$.

- When $W$ falls, the top of the fraction shrinks. This is the **loss spiral**.
- When $m$ rises, the bottom of the fraction grows. This is the **margin spiral**.
""")),
    ("3", "## 3.", "after", hook("Five features: Dry, Common, Volatile, Flees, Follows", r"""
1. **Dry:** liquidity can suddenly dry up.
2. **Common:** many securities become illiquid together.
3. **Volatile:** volatile assets are less liquid.
4. **Flees:** in a flight to quality, risky assets lose more liquidity.
5. **Follows:** liquidity falls when the market falls.

The same five are the findings of the spiral paper in Topic 4.
""")),
    ("3", "## 4. Extreme market events", "after", hook("Margins rise exactly when the market needs traders", r"""
Margins were about 4 percent before 1987. They went above 12 percent on Black Monday. In every later crisis (1989, 1990 to 1991, the Asian crisis, LTCM in 1998, subprime in 2007 to 2008), margins rose again.
""")),
    ("3", "### 5.1", "after", hook("Four triggers: LFVF", r"""
- **L**oss: a first loss.
- **F**unding shock: lenders cut credit.
- **V**olatility shock: financiers cannot tell news from illiquidity, so they raise margins.
- **F**orced sale: a large trader must unwind, and others may predate.
""")),
    ("3", "### 5.2", "after", pmap(r"""
1. A trader suffers a loss.
2. The loss causes a funding problem.
3. The trader must sell, so prices move away from fundamentals.
4. Lower prices cause more losses on the remaining positions. This is the loss spiral.
5. Higher volatility makes financiers raise margins. This is the margin spiral.
6. Both spirals make the funding problem worse, so the loop starts again, stronger each time.
""")),
    ("3", "## 6. Empirical measure", "before", fbox("Formulas: the spiral numbers", r"""
1. The position is $X=W/m$, and the loan is $X-W$.
2. After a price fall of $f$, the position is worth $X(1-f)$. The new capital is $W'=X(1-f)-\text{loan}$.
3. The loss-spiral sale is $X(1-f)-W'/m$. The margin-spiral sale is $W'/m-W'/m'$.

Example: $W=10$ and $m=10\%$, so $X=100$ and the loan is 90. A 3 percent fall makes the position 97 and $W'=7$. At a 10 percent margin, the trader may hold 70, so they sell 27. At a 14 percent margin, they may hold 50, so they sell 20 more. In total, 47 of 97 are sold after a 3 percent fall.
""")),
    ("3", "## 6. Empirical measure", "after", hook("Spiral scores: +1 is always bad", r"""
For spreads, bad means **up**. For prices, bad means **down**. So the inequalities point opposite ways in the two measures.

Two tests must both hold. First, the value moves against yesterday. Second, the value is beyond the band, which is last year's mean plus or minus **half** a standard deviation. Otherwise the score is 0.

Add the scores of the last 10 days. A large positive sum means the stock is in a spiral.
""")),
    ("3", "## 7. Data", "before", fbox("Formulas: spiral scores", r"""
1. The spread score is +1 if $s_t>s_{t-1}$ and $s_t>\bar{s}+0.5\sigma_s$. It is $-1$ if $s_t<s_{t-1}$ and $s_t<\bar{s}-0.5\sigma_s$. Otherwise it is 0.
2. The price score is +1 if $P_t<P_{t-1}$ and $P_t<\bar{M}-0.5\sigma_P$. It is $-1$ if $P_t>P_{t-1}$ and $P_t>\bar{M}+0.5\sigma_P$. Otherwise it is 0.
3. The spiral measure is the sum of the scores over the last 10 days.
""")),
    ("3", "### 9.1", "after", hook("Valuation: spirals shrink multiples", r"""
The loss spiral lowers both price to book (PTBV) and P/E in all six models. The illiquidity spiral lowers P/E in all three models, and it lowers PTBV once controls are added.

The effects are significant, but the $R^2$ is tiny, so they explain little.
""")),

    # ---------------- Topic 4 ----------------
    ("4", "## 1. Predatory trading", "before", hook("Four ways liquidity vanishes: Prey, Betray, Pressure, Spiral", r"""
- **Prey:** others trade against a distressed trader. This is predatory trading (Brunnermeier and Pedersen 2005).
- **Betray:** cooperation among traders breaks down (Carlin, Lobo and Viswanathan 2007).
- **Pressure:** sellers demand liquidity together (Shkilko, Van Ness and Van Ness 2012).
- **Spiral:** funding liquidity and market liquidity feed each other (Brunnermeier and Pedersen 2009).
""")),
    ("4", "### 1.4", "after", hook("Five results: OLIPS", r"""
- The price **O**vershoots.
- The distressed trader gets a **L**ower liquidation value.
- The market is **I**lliquid exactly when liquidity is most needed.
- A trader can **P**rofit by triggering another trader's crisis.
- The crisis **S**pills over across traders and markets.

Remember **"sell with them, then buy from them"**. Predators sell first, in the same direction, and buy back later. Predation pays when the market is **illiquid** and the distressed position is **big** relative to others' buying capacity.
""")),
    ("4", "### 1.8", "before", fbox("Formulas: the predation example", r"""
1. The price change is $\lambda$ times the number of shares traded.
2. The overshoot is the final price minus the lowest price.

Example: each of the two traders holds 8, and the speed is $A=20$. Both sell at speed 10, so the selling ends at 5.8. Together they sell 16 shares, so the price falls from 116 to 100. The predator buys back 10 shares alone at speed 20, so this ends at 6.3. The final price is 110. So the overshoot is $110-100=10$.
""")),
    ("4", "### 1.8", "after", hook("More predators, less overshoot: competition eats predation", r"""
With 3, 9 and 27 traders, the overshoot shrinks to about 3.3, 0.8 and 0.2. More predators also start buying back earlier.
""")),
    ("4", "### 2.2", "after", hook("Episodic crises: RHEC", r"""
- **R**epeated game: traders cooperate, because predating today loses future cooperation.
- **H**igh stakes: when the stakes are high, today's gain beats the future loss, so cooperation breaks.
- **E**pisodic: so illiquidity comes in sudden episodes.
- **C**ontagion: cooperation across markets makes crises rarer, but a breakdown then hits all markets.
""")),
    ("4", "### 3.1", "after", hook("Shkilko: longs lead, shorts follow", r"""
Intraday price declines are driven mostly by **long sellers**. Short sellers make declines somewhat worse, and they switch from providing liquidity to demanding it. But their effect is second to that of the long sellers.
""")),
    ("4", "### 3.2", "after", hook("Large reversal: two sigma down, 90 to 110 percent back", r"""
The price first falls by at least two standard deviations: $\ell\le-2\sigma_i$. Then, by the close, it recovers between 90 and 110 percent of the fall: $0.9\lvert\ell\rvert\le R_{close}-\ell\le 1.1\lvert\ell\rvert$.
""")),
    ("4", "## 4. Spirals", "before", fbox("Formulas: Shkilko reversal", r"""
1. The decline condition is $\ell\le-2\sigma_i$.
2. The rebound condition is $0.9\lvert\ell\rvert\le R_{close}-\ell\le 1.1\lvert\ell\rvert$.

Example: $\sigma_i=1\%$ and the low is $\ell=-2\%$. The smallest rebound is 1.8, so the close is $-0.2\%$. The largest rebound is 2.2, so the close is $+0.2\%$. The day must end between $-0.2\%$ and $+0.2\%$.
""")),
    ("4", "### 4.3", "after", hook("The spiral findings are the five features again", r"""
Remember **Dry, Common, Volatile, Flees, Follows** from Topic 3. These are the five findings on slide 20.
""")),

    # ---------------- Topic 5 ----------------
    ("5", "## 1.", "after", hook("Kissell's five foci and the three reasons to trade", r"""
Kissell's five foci are **Venues, Discovery, Spreads, Intraday, Costs**. Microstructure studies trading venues, price discovery, spreads and quotes, intraday behaviour and transaction costs.

The three reasons to trade spell **PIP**: Profit, Information and Price discovery.
""")),
    ("5", "## 3.", "after", hook("Seven trader types: Please Bring Dad's Huge Avocado, Very Fresh", r"""
**P**roprietary traders, **B**rokers, **D**ealers, **H**edgers, **A**rbitrageurs, **V**alue investors and **F**ront runners.
""")),
    ("5", "## 5.", "before", fbox("Formulas: the Axis Bank example", r"""
1. The spread is the ask minus the bid: $664.55-664.40=0.15$.
2. The mid price is the average: $664.475$.
3. The proportional spread is $0.15/664.475=0.0226$ percent.
4. The depth is $(714+453)/2=583.5$ shares.
""")),
    ("5", "## 5.", "after", hook("Liquidity dimensions: I Want Deep Rivers", r"""
**I**mmediacy asks how fast you can trade. **W**idth is the spread, the cost of a small trade. **D**epth asks how much you can trade at a price. **R**esiliency asks how fast the price recovers after a large trade.
""")),
    ("5", "## 7.", "after", hook("Market quality: Let Traders Invest Very Profitably", r"""
The five measures are **L**iquidity, **T**ransaction cost, **I**nformative prices, **V**olatility and trading **P**rofits.
""")),
    ("5", "## 8.", "after", hook("Volatility: fundamental is forever, transitory is temporary", r"""
Total volatility is fundamental volatility plus transitory volatility. Fundamental volatility comes from news, and it is permanent. Transitory volatility comes from impatient uninformed traders, and value traders push the price back.
""")),
    ("5", "## 10.", "after", hook("Roll: the bounce shares one sign, with a minus", r"""
Two neighbouring price changes share only $Q_{t-1}$. It enters them with opposite signs. So $\mathrm{Cov}=-(S/2)^2$, and $S=2\sqrt{-\mathrm{Cov}}$.
""") + pmap(r"""
1. The trade price is the value plus or minus half the spread: $P_t=V_t+\tfrac{S}{2}Q_t$.
2. The price change is the news plus the change in the bounce: $\Delta P_t=\varepsilon_t+\tfrac{S}{2}(Q_t-Q_{t-1})$.
3. In the covariance of two neighbouring changes, only the shared term $-Q_{t-1}^2$ survives. So $\mathrm{Cov}=-S^2/4$.
4. Solving gives $S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$. The variance is $\sigma^2+S^2/2$.
""")),
]

FOOTER = r"""
\newpage

# Last look: every formula on one sheet

""" + fbox("All formulas for numericals", r"""
- **Copeland and Galai:** maximize $(1-\pi_I)G_U-\pi_IL_I$. In the symmetric case, $h=\pi_I\Delta$.
- **Glosten and Milgrom** ($\theta=\Pr(V_L)$): draw the grid. "Buy High, Sell Low gets the plus." The Buy row is $\theta(1-\mu),\ (1-\theta)(1+\mu)$, and the Sale row is $\theta(1+\mu),\ (1-\theta)(1-\mu)$. The ask and the bid are the row averages. $\Pr(B)$ is half the Buy row sum. The spread is $4\cdot\theta(1-\theta)\cdot\mu\cdot\Delta V/(R_B R_S)$, which is $\mu\Delta V$ when $\theta=\tfrac12$.
- **Kyle:** the units set each ratio, and three halves finish them. $\lambda\beta=\tfrac12$, so $\lambda=\sigma_0/2\sigma_y$ and $\beta=\sigma_y/\sigma_0$. The profit is $\tfrac12\sigma_0\sigma_y$, which equals the noise traders' loss. The variance left is $\tfrac12\sigma_0^2$. The price is $p=p_0+\lambda z$.
- **Easley and O'Hara:** $I_S=\alpha\delta\mu$ (the tree in time order) and $U_S=X_S^2(1-\alpha\mu)$. Then $b_2=V^{\ast}-\frac{I}{U+I}(V^{\ast}-\underline{V})$, and the ask is the mirror image. The small quotes are $V^{\ast}$. Separation needs $B^2/B^1\ge(U_B+I_B)/U_B$: the size ratio must beat the crowd ratio.
- **Chordia:** QSPR $=A-B$. PQSPR divides it by $P_M$. DEP $=(Q_A+Q_B)/2$. ESPR $=2\lvert P_t-P_M\rvert$. PESPR divides it by $P_t$. Test 1 is $DL_{j,t}=\alpha_j+\beta_jDL_{M,t}+\varepsilon$, with $\beta\approx 0.69$.
- **Amihud:** ILLIQ is the average of $\lvert R_d\rvert/VOLD_d$, ratio first. Amivest $=\sum VOLD/\sum\lvert R\rvert$.
- **Lesmond:** $LOT=\alpha_2-\alpha_1$. **Stoll:** half-spreads $(A-B)/2$ and $\lvert P-M\rvert$.
- **Roll:** $S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$, and $\mathrm{Var}(\Delta P)=\sigma^2+S^2/2$.
- **Funding:** $X\le W/m$. **Spiral scores:** +1, $-1$ or 0 against the band of mean plus or minus half a standard deviation. +1 is bad. Add the last 10 days.
- **Predation:** the price change is $\lambda$ times the shares. The path is 116, then 100, then 110, so the overshoot is 10.
- **Shkilko:** $\ell\le-2\sigma_i$ and $0.9\lvert\ell\rvert\le R_{close}-\ell\le 1.1\lvert\ell\rvert$.
""")


def build_file(num, path):
    text = open(path).read().replace("⭐", r"$\star$").replace(r"\gt", ">").replace(r"\lt", "<")
    blocks = iter(re.findall(r"```mermaid.*?```", text, flags=re.S))
    for b in blocks:
        text = text.replace(b, MERMAID[path])
    text = re.sub(r"^(!\[[^\]]*\]\([^)]*\))\s*$", r"\1{width=75%}", text, flags=re.M)
    lines = text.split("\n")
    out = []
    mine = [i for i in INSERTS if i[0] == num]
    used = set()
    for line in lines:
        for k, (_, prefix, where, body) in enumerate(mine):
            if line.startswith(prefix.replace("⭐", r"$\star$")) or \
               line.replace(r"$\star$ ", "").startswith(prefix):
                if where == "before":
                    out += ["", body, ""]
                    used.add(k)
        out.append(line)
        for k, (_, prefix, where, body) in enumerate(mine):
            if line.startswith(prefix) or line.replace(r"$\star$ ", "").startswith(prefix):
                if where == "after":
                    out += ["", body, ""]
                    used.add(k)
    missing = [mine[k][1] for k in range(len(mine)) if k not in used]
    assert not missing, f"{path}: headings not found: {missing}"
    return "\n".join(out)


if __name__ == "__main__":
    parts = [HEADER]
    for n, f in enumerate(FILES, 1):
        parts += ["\n\\newpage\n", build_file(str(n), f)]
    parts.append(FOOTER)
    open("memorize.md", "w").write("\n".join(parts))
    subprocess.run(["pandoc", "memorize.md", "--lua-filter", "box.lua",
                    "--pdf-engine=tectonic", "-o", "memorize.pdf"], check=True)
