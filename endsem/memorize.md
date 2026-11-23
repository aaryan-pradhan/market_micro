---
title: "Market Microstructure Endsem: Memorize"
subtitle: "The five topic notes, shorter, with hooks, bird's-eye proofs and formula boxes"
geometry: margin=1.7cm
fontsize: 10pt
header-includes:
  - \usepackage[most]{tcolorbox}
---

**How to use this.** It follows `1-` to `5-*.md` in the same order. Nothing new is added, except memory hooks and shorter proofs. Each part has three kinds of block:

- a blue **Hook** box: a mnemonic for a list or an equation you must write from memory,
- a **bird's-eye proof**: the derivation as 3 to 6 moves, without the helper variables,
- an orange **Formulas** box: only what a numerical needs.

**Read first (not yet read):** Topic 1 §5 (Easley and O'Hara) and all of Topic 2.

::: {.hook title="The whole course in five lines"}
1. Informed traders create a spread and a price impact. *(Topic 1)*
2. Liquidity measures tell us how large these costs are. *(Topic 2)*
3. Funding limits turn a small loss into extreme illiquidity. *(Topic 3)*
4. Common funding and strategic selling spread illiquidity across the market. *(Topic 4)*
5. Illiquidity lowers prices and raises the return that investors demand. *(Topics 2 and 3)*

Chain: **Inform $\to$ Measure $\to$ Fund $\to$ Spread across $\to$ Price.**
:::

\newpage

# Topic 1: Information-Based Models

## 1.0 The five theories in one picture

::: hook
**"The dealer WOBLS."** Each model adds one thing:
**W**ords (Bagehot 1971) $\to$ **O**ption (Copeland and Galai 1983) $\to$ **B**ayes (Glosten and Milgrom 1985) $\to$ **L**ambda (Kyle 1985) $\to$ **S**ize (Easley and O'Hara 1987).

Years: 71, then 83, 85, 85, 87. The two 1985 papers are the twins: G-M (sequential, one unit) and Kyle (batch, chosen size).
:::

| Model | Adds | Fixes the earlier weakness | Dealer learns from | Liquidity measure |
|---|---|---|---|---|
| Bagehot (1971) | Some traders know more | First theory, words only | Nothing | Spread |
| Copeland and Galai (1983) | A profit function | Bagehot had no equation | Nothing (one period) | Spread |
| Glosten and Milgrom (1985) | Learning from each trade | C-G has one period, no learning | Direction | Spread |
| Kyle (1985) | Strategic insider chooses size | G-M insider trades one unit, ignores impact | Net order flow | $1/\lambda$ |
| Easley and O'Hara (1987) | Two sizes, event uncertainty | Earlier: one size, information sure to exist | Direction, size, sequence | Spread at each size |

| Point | Inventory models | Information models |
|---|---|---|
| Dealer's problem | Unwanted position | The trader may know more |
| Why a spread | Holding cost, order cost, ruin risk | Adverse selection |
| A trade changes | The inventory | The belief about value |
| Price effect | Mostly temporary | Permanent |

**Role of information (slide 2):** transaction cost alone does not explain prices; information flow moves prices; traders are not equally informed; adverse selection is a new risk to the dealer's wealth.

**Recognize the model from a word:** "option" = C-G. "Regret free", "Bayes", "sequential" = G-M. "Batch", "strategic", "order flow" = Kyle. "Size", "block", "event uncertainty" = E-O.

## 1.1 Bagehot (1971): "The only game in town"

::: hook
**2-2-1.** Two gains (market gain, which everyone can earn; trading gain, which not everyone can). Two traders (informed: the dealer loses; uninformed: the dealer recovers the loss). One balance: the spread.
:::

- The average investor loses over time, because of the cost of information.
- A wider spread cuts the loss to informed traders and raises the gain from uninformed traders.
- No equations. In the exam write the 2-2-1 and the diagram: Informed $\leftarrow$ loses $\leftarrow$ DEALER $\leftarrow$ gains $\leftarrow$ Uninformed.

## 1.2 Copeland and Galai (1983): the free options

::: hook
**Ask = Call, Bid = Put.** The ask is a free call with strike $P_A$: the informed exercise it (buy) when $P>P_A$. The bid is a free put with strike $P_B$: the informed exercise it (sell) when $P<P_B$.

Objective, **"Gain from U, Lose to I"**: $\;(1-\pi_I)\,G_U-\pi_I\,L_I$. Each term is weighted by the probability of its own trader type.
:::

**Assumptions:** one risk-neutral dealer; informed know $P$; uninformed know only $P_0$; arrivals with given probabilities; one fixed size; instant quotes.

**Bird's-eye proof**

1. Loss to an informed trader = expected payoff of the call + expected payoff of the put:
$$L_I=\int_{P_A}^{\infty}(P-P_A)f(P)\,dP+\int_{0}^{P_B}(P_B-P)f(P)\,dP$$
2. Gain from an uninformed trader = the half-spread on each side, times how often that side comes:
$$G_U=\pi_{BL}(P_A-P_0)+\pi_{SL}(P_0-P_B)+\pi_{NL}\cdot 0$$
3. Choose the quotes: $\max_{P_A,P_B}\left[(1-\pi_I)G_U-\pi_I L_I\right]$, subject to $\ge 0$. Competition makes it $=0$.
4. Trade-off: a wider spread lowers $L_I$ and earns more per uninformed trade, **but** drives the uninformed away. That last effect stops the spread from growing without limit.

::: hook
**Findings: "PV up, ADC down."** The spread rises with **P**rice level and **V**ariance of return. It falls with market **A**ctivity, **D**epth and **C**ontinuity.
Limitations: only one period; information is revealed instantly by the trade.
:::

::: box
Example setup: value is $P_0\pm\Delta$ with equal chance, quotes $P_0\pm h$, every uninformed trader trades ($\pi_{BL}=\pi_{SL}=0.5$).

- $G_U=h$ and $L_I=\Delta-h$.
- Zero profit: $(1-\pi_I)h=\pi_I(\Delta-h)$, which gives $h=\pi_I\Delta$.

Notes example: $\Delta=10$, $\pi_I=0.2$, so $h=2$: ask 102, bid 98, spread 4.
(The shortcut $h=\pi_I\Delta$ holds only for this symmetric setup.)
:::

## 1.3 Glosten and Milgrom (1985): learning from each trade

::: hook
**Rule: "Quote what you'd believe after the trade."** Ask $=E[V\mid\text{buy}]$, bid $=E[V\mid\text{sale}]$. This is regret free: the quote is still fair after the trade.

**"Tilt, then normalise."** Start from the prior. A **buy** multiplies the good state by $(1+\mu)$ and the bad state by $(1-\mu)$. A **sale** swaps them. Divide by the sum.

**$\theta$ = Trouble** = $\Pr(V_L)$. Write this in your first line: the slides switch the meaning.
:::

**Assumptions:** $V_L$ with prob $\theta$, $V_H$ with $1-\theta$; share $\mu$ are insiders (buy on good news, sell on bad); uninformed buy or sell 0.5 each; sequential, one unit; dealer risk neutral and competitive (zero profit); zero cost.

**The event tree (draw it first in the exam):**

| Branch | Buy | Sale |
|---|---|---|
| Good news $(1-\theta)$, informed $\mu$ | $(1-\theta)\mu$ | 0 |
| Good news, uninformed $(1-\mu)$ | $0.5(1-\theta)(1-\mu)$ | $0.5(1-\theta)(1-\mu)$ |
| Bad news $\theta$, informed $\mu$ | 0 | $\theta\mu$ |
| Bad news, uninformed $(1-\mu)$ | $0.5\theta(1-\mu)$ | $0.5\theta(1-\mu)$ |

**Bird's-eye proof**

1. **Likelihood of a buy in each state.** In $V_H$: all insiders buy and half the uninformed buy, $\mu+\tfrac{1}{2}(1-\mu)=\tfrac{1}{2}(1+\mu)$. In $V_L$: only half the uninformed buy, $\tfrac{1}{2}(1-\mu)$.
2. **Tilt (Bayes = prior $\times$ likelihood).** The $\tfrac12$ cancels, so after a buy the weights are $\theta(1-\mu)$ on $V_L$ and $(1-\theta)(1+\mu)$ on $V_H$. After a sale: $\theta(1+\mu)$ and $(1-\theta)(1-\mu)$.
3. **Normalise.** The sum of the buy weights is $1+\mu(1-2\theta)$, and $\Pr(B)$ is half of it. For a sale: $1-\mu(1-2\theta)$.
4. **Quotes** = weighted averages:
$$a=\frac{\theta(1-\mu)V_L+(1-\theta)(1+\mu)V_H}{1+\mu(1-2\theta)},\qquad b=\frac{\theta(1+\mu)V_L+(1-\theta)(1-\mu)V_H}{1-\mu(1-2\theta)}$$
5. **Spread.** Write each quote as $V_L+(V_H-V_L)\Pr(V_H\mid\cdot)$. Subtract; $V_L$ cancels. Cross-multiply the two fractions: the numerator $(1+\mu)(1-\mu k)-(1-\mu)(1+\mu k)$ collapses to $2\mu(1-k)=4\theta\mu$, with $k=1-2\theta$.
$$s=\frac{4\theta(1-\theta)\mu(V_H-V_L)}{1-(1-2\theta)^2\mu^2}\qquad\theta=0.5:\; s=\mu(V_H-V_L)$$

::: hook
**Spread formula: "4 times the coin, times insiders, times the range, over the product of the two denominators."**
Coin $=\theta(1-\theta)$. The denominator $1-(1-2\theta)^2\mu^2=(1+\mu k)(1-\mu k)$.
Fair coin ($\theta=0.5$): **spread = insider share $\times$ range.**
:::

**Conclusion:** $s>0$ with zero cost and zero profit, so the spread is pure adverse selection. $s$ rises with $\mu$.

::: box
1. Weights after a **buy**: $w_L=\theta(1-\mu)$, $w_H=(1-\theta)(1+\mu)$. Ask $=\dfrac{w_LV_L+w_HV_H}{w_L+w_H}$.
2. Weights after a **sale**: $w_L=\theta(1+\mu)$, $w_H=(1-\theta)(1-\mu)$. Bid = the same average.
3. $\Pr(B)=0.5[1+\mu(1-2\theta)]$, and $\Pr(S)=1-\Pr(B)$.
4. After a buy, the new $\theta$ is $\Pr(V_L\mid B)=w_L/(w_L+w_H)$. Repeat for the next quotes.
5. Check: $\Pr(B)\,a+\Pr(S)\,b$ = prior mean (martingale).

Example: $V_H=110$, $V_L=90$, $\theta=0.3$, $\mu=0.4$. Prior 104. $\Pr(B)=0.58$. Ask $=(0.18\cdot 90+0.98\cdot 110)/1.16=106.897$. Bid $=(0.42\cdot 90+0.42\cdot 110)/0.84=100$. Spread 6.897. Check: $0.58(106.897)+0.42(100)=104$.
After a buy: new $\theta=0.18/1.16=0.1552$. Ask 108.541, bid 104. Both quotes move up.
:::

::: hook
**Findings, "ZLMS":** **Z**ero-profit dealer puts adverse-selection cost in the spread. **L**earning: beliefs and quotes update with each trade. **M**artingale: the best forecast of the next price is the present price. **S**emi-strong efficient: public information cannot predict the future price better.
Versus C-G: the C-G spread comes from expected gains and losses; the G-M spread comes from beliefs given each trade.
:::

**Slide errors:** $\theta$ changes meaning between slides. Equation 4.28 prints $\Pr(V_L\mid B)$ in the good-news form. Use the tilt rule.

## 1.4 Kyle (1985): the strategic insider

::: hook
**"The insider hides perfectly. Everything is a half."**
At the equilibrium the insider's order has the **same variance as the noise**: $\beta^2\sigma_0^2=\sigma_y^2$. So half of the order flow is information, half of the information enters the price, and $\lambda$ and the profit both carry a $\tfrac12$.

$\lambda=\dfrac{\sigma_0}{2\sigma_y}$: **"Info over twice Noise."** $\quad\beta=\dfrac{\sigma_y}{\sigma_0}$: **flip it, drop the 2.** $\quad E[\pi_I]=\dfrac{\sigma_0\sigma_y}{2}$: **multiply them, halve.**
:::

**Players:** one risk-neutral insider who knows $v$ and counts their own price impact; noise traders with random demand; competitive, risk-neutral market makers; one batch auction (one price, so no spread); one period, one security.

**Assumptions:** $v\sim N(p_0,\sigma_0^2)$; noise $y\sim N(0,\sigma_y^2)$, independent of $v$; the insider knows $v$, not $y$, and sends $x$; the dealer sees only $z=x+y$; zero profit, so $p=E[v\mid z]$; linear rule $p=\mu+\lambda z$ ($\mu$ here is an intercept, not the insider share).

**Bird's-eye proof** (two best responses meet)

1. **Insider's best response.** Expected profit $=x(v-\mu-\lambda x)$, since $E[y]=0$. Set the derivative to zero: $x=\dfrac{v-\mu}{2\lambda}$, so the slope is $\beta=\dfrac{1}{2\lambda}$. *(Second derivative $-2\lambda<0$: a maximum. A higher $\lambda$ means a smaller order.)*
2. **Dealer's best response.** The price is the regression of $v$ on $z$: $\lambda=\dfrac{\mathrm{Cov}(v,z)}{\mathrm{Var}(z)}=\dfrac{\beta\sigma_0^2}{\beta^2\sigma_0^2+\sigma_y^2}$.
3. **Meet.** Put $\beta=1/2\lambda$ into step 2: $\lambda\sigma_y^2+\dfrac{\sigma_0^2}{4\lambda}=\dfrac{\sigma_0^2}{2\lambda}$, so $\lambda^2\sigma_y^2=\dfrac{\sigma_0^2}{4}$:
$$\lambda^{\ast}=\frac{\sigma_0}{2\sigma_y},\qquad\beta^{\ast}=\frac{\sigma_y}{\sigma_0},\qquad\mu^{\ast}=p_0,\qquad x=\frac{\sigma_y}{\sigma_0}(v-p_0)$$
($\mu^{\ast}=p_0$ comes from matching the intercepts.)
4. **The hiding fact.** $\beta^{\ast 2}\sigma_0^2=\sigma_y^2$, so $\mathrm{Var}(z)=2\sigma_y^2$.
5. **Half revealed.** $\mathrm{Var}(v\mid z)=\sigma_0^2-\dfrac{\mathrm{Cov}^2}{\mathrm{Var}(z)}=\sigma_0^2-\dfrac{\beta^2\sigma_0^4}{2\sigma_y^2}=\sigma_0^2-\dfrac{\sigma_0^2}{2}=\dfrac{\sigma_0^2}{2}$.
6. **Who pays.** Insider: $E[\pi_I]=\dfrac{E(v-p_0)^2}{4\lambda}=\dfrac{\sigma_0^2}{4\lambda}=\dfrac{\sigma_0\sigma_y}{2}$. Noise traders lose $E[y(p-v)]=\lambda\sigma_y^2=\dfrac{\sigma_0\sigma_y}{2}$. Dealer: zero.

::: hook
**What changes what: "Profit likes both; lambda likes only info."**
$\sigma_0\uparrow$: $\lambda\uparrow$, profit $\uparrow$ (more private information, less liquid).
$\sigma_y\uparrow$: $\lambda\downarrow$, profit $\uparrow$ (more noise hides the insider, deeper market).
:::

**The four questions (slide 26):** speed of information into the price = half in one period; value of information = $\sigma_y\sigma_0/2$; noise lowers $\lambda$; liquidity is decided by $\lambda=\sigma_0/2\sigma_y$, private information against noise.

::: box
- $\lambda=\sigma_0/(2\sigma_y)$, $\beta=\sigma_y/\sigma_0$, $x=\beta(v-p_0)$
- $z=x+y$, $p=p_0+\lambda z$
- Realized profit $=x(v-p)$. Expected profit $=\sigma_0\sigma_y/2$ (before $v$ is known).
- Remaining variance $=\sigma_0^2/2$

Example: $p_0=100$, $\sigma_0=10$, $\sigma_y=1000$, $v=110$, $y=-400$. $\lambda=0.005$, $\beta=100$, $x=1000$, $z=600$, $p=103$. Realized profit 7000. Expected profit 5000. Remaining variance 50.
:::

**Findings (slide 32):** noise order flow hides the insider's information *from the dealer* (the slide's wording "from informed traders" is wrong); a large random buy makes the dealer raise the price; liquidity traders pay the insider's profit, and the dealer nets zero; with many periods the insider splits the order into small pieces.
**Slide errors:** slide 28 says that the dealer maximizes profit; the dealer actually earns zero. Equation 4.9 drops the minus in $a^{\ast}=-p_0\sigma_y/\sigma_0$.

## 1.5 Easley and O'Hara (1987): size and event uncertainty (NOT YET READ)

**What is new:** extends G-M; competitive, risk-neutral dealers; traders can choose **different sizes**; **dual uncertainty**: the dealer does not know whether information exists, nor its direction. Main message: **the size and the sequence of trades both move prices.**

::: hook
**Three Greek letters, one story: "Alpha Arrives, Delta Decides, Mu Many."**
$\alpha$ = an information event **arrives** (before the day). $\delta$ = the signal is **low** (bad). $\mu$ = the share of traders who are informed **after an event**.
**Key product:** $\alpha\mu$ = the chance that a random trader is informed. So $1-\alpha\mu$ = the chance that they are uninformed.
:::

**Assumptions:**

| No. | Assumption |
|---|---|
| A1 to A3 | Signal low (prob $\delta$) or high; $\underline{V}=E[V\mid L]<\bar{V}=E[V\mid H]$ |
| A4 | Event before the day with prob $\alpha$; events happen only between days |
| A5, A6 | After an event, informed trade a share $\mu$; they are risk neutral and competitive |
| A7 | The dealer and the uninformed see neither the event nor the signal |
| A8, A9 | No cost, no risk aversion (short period); uninformed demand is given from outside (income and consumption timing, portfolio needs) |

Value without news: $V^{\ast}=\delta\underline{V}+(1-\delta)\bar{V}$.

**Market structure:** two sizes on each side, $B^1<B^2$ and $S^1<S^2$; $X^i_B$, $X^i_S$ = the share of uninformed wanting each size. A trader arrives, asks competing dealers for prices at each size, may not trade. The uninformed take the best quote for their size; the informed take the most profitable quote. Dealers set a price schedule for the four quantities at the start of the day; each trade has zero expected profit.

::: hook
**Two equilibria: "Few informed: Fork. Many informed: Mix."**
**Separating** (few informed): the informed go **large only**, so small trades are safe ($a_1=b_1=V^{\ast}$) and the spread is **only on large** trades.
**Pooling** (many informed): the informed use **both sizes**, the dealer cannot tell the types apart, and **both sizes carry a spread**.
:::

**Bird's-eye proof: the large-trade bid (separating)**

1. **Who sells large, and at what value?** Uninformed sellers want $S^2$ with weight $X_S^2(1-\alpha\mu)$. They are worth $V^{\ast}$ on average. Informed sellers (event and low signal) have weight $\alpha\delta\mu$. They are worth $\underline{V}$.
2. **Bid = weighted average** (the G-M rule again):
$$b_2=\frac{X_S^2(1-\alpha\mu)\,V^{\ast}+\alpha\delta\mu\,\underline{V}}{X_S^2(1-\alpha\mu)+\alpha\delta\mu}$$
3. **Pull out $V^{\ast}$:** $b_2=V^{\ast}-\dfrac{\alpha\delta\mu(V^{\ast}-\underline{V})}{X_S^2(1-\alpha\mu)+\alpha\delta\mu}$.
4. **Use the variance.** $V^{\ast}-\underline{V}=(1-\delta)(\bar{V}-\underline{V})$ and $\sigma_v^2=\delta(1-\delta)(\bar{V}-\underline{V})^2$. So $\delta(V^{\ast}-\underline{V})=\sigma_v^2/(\bar{V}-\underline{V})$:
$$b_2^{\ast}=V^{\ast}-\frac{\sigma_v^2}{\bar{V}-\underline{V}}\cdot\frac{\alpha\mu}{X_S^2(1-\alpha\mu)+\delta\alpha\mu},\qquad a_2^{\ast}=V^{\ast}+\frac{\sigma_v^2}{\bar{V}-\underline{V}}\cdot\frac{\alpha\mu}{X_B^2(1-\alpha\mu)+(1-\delta)\alpha\mu}$$
For the ask, the informed buy on a **high** signal, so $(1-\delta)$ replaces $\delta$.
5. **Does separation hold?** The informed buyer must prefer large: $B^2(\bar{V}-a_2)\ge B^1(\bar{V}-V^{\ast})$. This gives
$$\frac{B^2}{B^1}\ge 1+\frac{\alpha\mu(1-\delta)}{X_B^2(1-\alpha\mu)}=\frac{\text{all large buyers' weight}}{\text{uninformed large buyers' weight}}$$
If the large size is big enough, or $\alpha\mu$ small enough, separation holds. Otherwise the informed also trade small, and the result is pooling.

**Conclusion:** the large-trade discount rises with $\alpha$, $\mu$ and the variance of value.

::: hook
**$b_2$ in words: "V-star minus (variance over range) times (informed over all large sellers, without the $\delta$ on top)."**
The quickest way to compute it: skip the formula and take the **weighted average** of step 2.
:::

**Pooling (slide 43):** a share $\phi_i$ of informed sellers uses size $i$: $b_i=V^{\ast}-\dfrac{\sigma_v^2}{\bar{V}-\underline{V}}\cdot\dfrac{\alpha\mu\phi_i}{X^i_S(1-\alpha\mu)+\delta\alpha\mu\phi_i}$. Both bids lie below $V^{\ast}$. The informed must earn the same profit at both sizes.

**Spread at size $i$ (slide 44, corrected):** $A_i=E[V\mid B^i]+C$, $B_i=E[V\mid S^i]-C$, $S_i=E[V\mid B^i]-E[V\mid S^i]+2C$. The model sets $C=0$. (The slide conditions on the trader type. The dealer cannot see the type, only the side and size.)

::: hook
**Price path after a block sale: "Known event: stuck. Unsure event: bounce part way."**
$t$: a small trade at $V^{\ast}$. $t+1$: a block sale pushes the price down to $b_2$.
$t+2$, **event known** (Fig 1): a small trade says nothing new, so the price **stays** at $b_2$.
$t+2$, **event uncertain** (Fig 2): only the uninformed trade small, so a small trade makes "no event" more likely. The price **recovers partly**, but stays below $V^{\ast}$.
:::

::: box
1. $V^{\ast}=\delta\underline{V}+(1-\delta)\bar{V}$. $\sigma_v^2=\delta(1-\delta)(\bar{V}-\underline{V})^2$.
2. Large bid = average of $V^{\ast}$ (weight $X_S^2(1-\alpha\mu)$) and $\underline{V}$ (weight $\alpha\delta\mu$).
3. Large ask = average of $V^{\ast}$ (weight $X_B^2(1-\alpha\mu)$) and $\bar{V}$ (weight $\alpha(1-\delta)\mu$).
4. Small quotes (separating): $a_1=b_1=V^{\ast}$.
5. Separation needs $B^2/B^1\ge 1+\alpha\mu(1-\delta)/[X_B^2(1-\alpha\mu)]$.
6. A small trade after a block: take the three state weights after the block sale, multiply each by the chance that the trader is uninformed ($1-\mu$ after an event, 1 with no event), and average the values.

Example: $\bar{V}=110$, $\underline{V}=90$, $\delta=\alpha=0.5$, $\mu=0.4$, $X=0.25$. $V^{\ast}=100$, $\sigma_v^2=100$, $\alpha\mu=0.2$.
Large bid $=(0.2\cdot 100+0.1\cdot 90)/0.3=96.667$. Large ask $=(0.2\cdot 100+0.1\cdot 110)/0.3=103.333$. Small quotes 100. Separation needs $B^2/B^1\ge 1.5$.
After the block sale, the state weights are $0.1375$ (low), $0.0375$ (high), $0.125$ (no event). Times $0.6,0.6,1$: $0.0825,0.0225,0.125$, total $0.23$. Small-trade price $=(0.0825\cdot 90+0.0225\cdot 110+0.125\cdot 100)/0.23=22.4/0.23=97.391$. It lies between 96.667 and 100: a partial recovery.
:::

::: hook
**Findings (slide 47), "BQIO":** **B**lock trades move prices because of informed trading. **Q**uantity is correlated with private information. **I**nformed traders prefer larger amounts at any given price. **O**ptimal pricing depends on quantity: large-trade prices show a higher probability of informed trading.
:::

\newpage

# Topic 2: Liquidity Measures and Applications (NOT YET READ)

::: hook
**Five papers, five questions: "Together? Priced? Which measure? Which part? What causes it?"**
**C**hordia 2000 (commonality) $\cdot$ **A**mihud 2002 (illiquidity is priced) $\cdot$ **L**esmond 2005 (measures for emerging markets) $\cdot$ **I**nce 2022 (which component is priced) $\cdot$ **S**toll 2000 (friction). **"CALIS."**
:::

| Paper | Question | Measure | Answer |
|---|---|---|---|
| Chordia, Roll, Subrahmanyam (2000) | Does liquidity move together? | Spreads, depth | Yes: commonality |
| Amihud (2002) | Does illiquidity affect returns? | $\lvert R\rvert$ per dollar traded | Illiquid stocks pay higher returns |
| Lesmond (2005) | Which measure works in emerging markets? | LOT, Roll, Amihud, others | LOT and Roll work best across countries |
| Ince (2022) | Which part of illiquidity is priced? | Three parts | The idiosyncratic part predicts returns |
| Stoll (2000) | What causes friction? | Seven friction measures | Real and informational parts |

**Background (slides 2 and 3):** Amihud and Mendelson (1986) introduced the spread as an illiquidity proxy; Chordia et al. (2000) documented commonality; Chordia et al. (2001) studied the cross-section with the level of illiquidity; Huberman and Halka (2001) found a time-varying systematic part of liquidity.

## 2.1 Chordia, Roll and Subrahmanyam (2000): "Commonality in liquidity"

**Gap:** earlier studies looked at one stock at a time. But liquidity changes are correlated across stocks; inventory risk and asymmetric information both change liquidity over time; trading costs have common determinants.

::: hook
**Seven reasons: "PVIVP + F + I."** The first five read the same both ways (a palindrome). They are all **inventory** reasons:
**P**rice swings (market-wide trading responds to them) $\cdot$ **V**olume (drives dealer inventories together) $\cdot$ **I**nterest rates (cost of carrying inventory) $\cdot$ **V**olatility (inventory risk has a market part) $\cdot$ **P**rogram trading (common pressure on many inventories).
Then **F**unds (institutional funds with similar styles trade alike: correlated trading) and **I**nformation (a few large traders may know about many stocks).
:::

**Implications (slide 6):** liquidity co-moves; trading costs co-move; liquidity crises can be episodic and global; trading cost has a common factor (Amihud-Mendelson 1986, Brennan-Subrahmanyam 1996). Two price channels: **static** (average cost, so a costly stock pays more) and **dynamic** (risk that liquidity changes, so a stock with risky liquidity pays more).

::: hook
**Data: "92 $\to$ 1169 $\to$ 254 $\to$ \$2."** NYSE (ISSM) for the year **1992**, **1,169** stocks (each traded on 10 or more days), **254** trading days, stock-days with a price below **\$2** deleted.
Also removed: splits and stock dividends, certificates, ADRs, non-US firms, Americus Trust, closed-end funds, REITs, the opening batch and special-settlement trades. The NYSE specialist announces spread and depth seconds before a trade. Each daily value is the average over that day's trades.
:::

::: hook
**Five measures: "Quoted uses the Mid. Effective uses the Execution price, and has a 2."**
Depth is the **only** one where higher means **more** liquid.
:::

| Symbol | Formula | Unit | Higher means |
|---|---|---|---|
| QSPR | $P_A-P_B$ | Dollars | Less liquid |
| PQSPR | $(P_A-P_B)/P_M$ | Number | Less liquid |
| DEP | $(Q_A+Q_B)/2$ | Shares | **More** liquid |
| ESPR | $2\lvert P_t-P_M\rvert$ | Dollars | Less liquid |
| PESPR | $2\lvert P_t-P_M\rvert/P_t$ | Number | Less liquid |

**Statistics (slides 10 and 11):** effective < quoted (trades happen inside the quotes); mean > median (a few illiquid stocks); spreads correlate positively with each other; depth correlates negatively with spreads. Daily change $DL_t=(L_t-L_{t-1})/L_{t-1}$. Liquidity changes a lot day to day, and **depth changes the most** (mean absolute change 0.78).

**Test 1, market commonality:**
$$DL_{j,t}=\alpha_j+\beta_j\,DL_{M,t}+\varepsilon_{j,t}\qquad(\text{plus a lag and a lead of }DL_M)$$

::: hook
**One number: 0.69.** The quoted-spread same-day coefficient: a 1% change in the market spread goes with a 0.69% change in the stock's spread.
**"69 to 85":** 69 to 85 percent of stocks have a positive coefficient. **Same day beats lag and lead.** Significant means $t>1.645$.
:::

**Test 2, market + industry:** $DL_{j,t}=\alpha_j+\beta_{j,M}DL_{M,t}+\beta_{j,I}DL_{I,t}+\varepsilon_{j,t}$. Both matter (DQSPR: market 0.264, industry 0.467). Mean $R^2\approx 2\%$: most daily change is firm-specific. The common part is still significant, and it cannot be diversified away.

**Test 3, inventory or information:** $DL_{j,t}=\alpha_j+\beta_S DS_{j,t}+\beta_T DT_{j,t}+\beta_M DV_{M,t}+\beta_I DV_{I,t}+\varepsilon_{j,t}$, where $S$ = average dollar trade size, $T$ = number of trades (asymmetric information: Jones et al. 1994; stealth trading in medium sizes: Barclay-Warner 1993), and $V_M$, $V_I$ = market and industry dollar volume without stock $j$.

| Variable | Effect | Explanation |
|---|---|---|
| Own number of trades | Strong **positive** on spreads | Informed traders |
| Market volume | **Negative**, marginal, on quoted spread | Balanced uninformed trading eases inventory |
| Trade size | Strong positive on quoted spread **and** depth | Block pressure or information |
| Industry volume | Negative, not significant, on depth | No clear effect |

::: hook
**Conclusion: "Together. Own trades widen. Market trades tighten."**
1. Liquidity of individual stocks moves together (commonality).
2. A stock's spread rises with its **own** number of transactions (asymmetric information).
3. The spread falls with **market-wide** trading, which is mostly uninformed and balances inventory (inventory risk).

Exam order: meaning, reasons, data, five measures, regression, sign, conclusion.
:::

## 2.2 Amihud (2002): "Illiquidity and stock returns"

**Idea:** a stock is illiquid if a small traded value moves its price a lot. The measure needs only daily returns and volume, no quotes. Investors demand a higher return for illiquid stocks.

::: hook
**ILLIQ: "Absolute return per dollar. Ratio first, then average."**
$$ILLIQ_{iy}=\frac{1}{D_{iy}}\sum_{d=1}^{D_{iy}}\frac{\lvert R_{iyd}\rvert}{VOLD_{iyd}}$$
Higher means **less** liquid. Its cousin, **Amivest** = total volume / total $\lvert R\rvert$ (Cooper et al. 1985; Khan-Baker 1993), is upside down: higher means **more** liquid.
:::

**Is it valid? (slide 22):** $ILLIQ_i=-292+247.9\,\lambda_i+49.2\,\psi_i$, with $R^2=0.30$. Here $\lambda$ = Kyle's price impact (t 13.78) and $\psi$ = the fixed-cost part of the spread (t 17.33). Both slopes are positive, so ILLIQ agrees with the measures from detailed trade data.

::: hook
**Data: "NYSE 63 to 97, 408 months, Fama-MacBeth."** CRSP daily and monthly. Returns adjusted for delisting (Shumway 1997, avoids survivorship bias). Characteristics from year $y-1$, so they are known at the start of year $y$.
$$R_{imy}=k_{0my}+\sum_j k_{jmy}X_{ji,y-1}+U_{imy}$$
Fama-MacBeth in three steps: one cross-section regression each month $\to$ save the coefficients $\to$ average over 408 months and test the average against zero.
:::

::: hook
**Findings: "Expected = Extra return later. Unexpected = Ugly return now. Small firms feel it most."**

- Cross-section: the ILLIQ coefficient is positive and significant, even with beta and size: an **illiquidity premium**.
- Time series: **expected** market illiquidity $\uparrow$ $\to$ expected excess return $\uparrow$. **Unexpected** illiquidity $\uparrow$ $\to$ required return jumps, price $D/r$ falls, so the current return is **negative**.
- Both effects are stronger for **small** firms (flight to liquidity).
- So part of the equity premium pays for illiquidity.

(The findings slide is blank in the deck. These come from the midsem notes.)
:::

::: box
- ILLIQ: compute $\lvert R_d\rvert/VOLD_d$ for **each day**, then average. Do **not** divide the average return by the average volume. State the unit.
- Amivest $=\sum VOLD_d/\sum\lvert R_d\rvert$.

Example: returns $0.02,-0.01,0.03$; volumes 10, 5, 10 (million dollars). Ratios $0.002,0.002,0.003$. ILLIQ $=0.007/3=0.002333$ per million dollars. Amivest $=25/0.06=416.67$.
Surprise: $D=5$ forever. At $r=10\%$, $P=50$. At $r=12.5\%$, $P=40$. The return now is $-20\%$, and the expected return after that is higher.
:::

## 2.3 Ince (2022): which part of illiquidity is priced

::: hook
**"ASI: Alpha, Systematic, Idiosyncratic. Only I survives."**
Monthly firm illiquidity = **A**lpha (constant for the firm) + **S**ystematic (moves with the market) + **I**diosyncratic (firm-specific).
The systematic premium **disappears** once very small stocks are removed. The idiosyncratic part predicts returns: high idiosyncratic liquidity gives positive future risk-adjusted returns, low gives negative ones.
:::

**Data (slide 34):** NYSE, Amex and Nasdaq common stocks, January 1964 to December 2018, CRSP.

**Other commonality articles (slide 28):** correlated institutional trading (Kamara et al. 2008; Koch et al. 2009); weak incentive to trade single securities (Morck et al. 2000); investor sentiment (Huberman-Halka 2001); funding limits of intermediaries (Coughenour-Saad 2004; Hameed et al. 2010); 40 markets (Karolyi et al. 2012).

## 2.4 Lesmond (2005): "Liquidity of emerging markets"

JFE 77, 411 to 452. Not in the slides. The findings come from the abstract and from summaries; the LOT model comes from the 1999 paper.

**Problem:** many emerging markets lack long bid-ask records, but trading there is costly. So estimate liquidity from daily prices and volume. Which low-frequency measure works across countries and within a country? Summaries say 31 emerging markets (one citing paper says 23), 1987 to 2000. It compares the measures with quoted spreads where these exist.

| Measure | Formula | Type | Weakness |
|---|---|---|---|
| LOT | $\alpha_2-\alpha_1$ | Price based | Needs an estimation model |
| Roll | $2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$ | Price based | Fails when Cov > 0 |
| Amihud | mean of $\lvert R\rvert$/value traded | Price impact | Fails with zero volume |
| Turnover | shares traded / shares outstanding | Volume based | Volume can rise in a crisis while cost rises |

**LOT (Lesmond, Ogden, Trzcinka 1999), bird's-eye**

::: hook
**"The no-trade band."** An investor trades only if the value of the news beats the cost. Inside the band $[\alpha_1,\alpha_2]$ nobody trades, so the observed return is **zero**. **Many zero-return days = high cost.** The band's width is the round-trip cost: $LOT=\alpha_2-\alpha_1$.
:::

1. True return: market model, $R^{\ast}_{jt}=\beta_jR_{mt}+\varepsilon_{jt}$, with normal error.
2. Observed return in the three regions:

| True return | Observed | Meaning |
|---|---|---|
| $R^{\ast}<\alpha_1$ (with $\alpha_1<0$) | $R^{\ast}-\alpha_1$ | Bad news beats the selling cost |
| $\alpha_1\le R^{\ast}\le\alpha_2$ | 0 | News too small |
| $R^{\ast}>\alpha_2$ (with $\alpha_2>0$) | $R^{\ast}-\alpha_2$ | Good news beats the buying cost |

3. Maximum likelihood over the three kinds of days (falls, zeros, rises) picks $\alpha_1$, $\alpha_2$, $\beta$ and the error variance.
4. Selling cost $-\alpha_1$, plus buying cost $\alpha_2$, gives the round trip: $LOT=\alpha_2-\alpha_1$.

The 1999 paper found round-trip costs of 1.2% for the largest US firms and 10.3% for the smallest (1963 to 1990). A simpler cousin: the **share of zero-return days**. It correlates highly with hand-collected spreads in emerging markets (Bekaert, Harvey and Lundblad, reporting Lesmond 2005).

::: hook
**Findings: "Across: LOT 'n' Roll. Within: LOT, then Amihud. Bad institutions cost more; politics beats law."**

1. Across countries: price-based LOT and Roll beat volume-based measures.
2. Within a country: LOT works best, Amihud to a lesser extent.
3. Weak political and legal institutions $\to$ significantly higher liquidity cost, "even to the exclusion of legal origin or insider trading enforcement".
4. More political risk: +10 bp cost by LOT, +1.9% price impact by Amihud.
5. Political risk looks stronger than the information risk from legal institutions.
:::

::: box
- $LOT=\alpha_2-\alpha_1$. Observed return $=R^{\ast}-\alpha_2$ above the band, $R^{\ast}-\alpha_1$ below it, 0 inside.

Example: $\alpha_1=-0.010$, $\alpha_2=0.015$. LOT $=0.025$ = 2.5%. True 0.025 gives observed 0.010. True 0.007 gives 0. True $-0.018$ gives $-0.008$.
:::

## 2.5 Stoll (2000): "Friction"

::: hook
**Two views of friction: "Time (Lippman-McCall) or Price (Demsetz). Stoll pays the Price."** Friction = the price concession paid for immediacy.
**Two kinds: Real** (uses labour, systems, capital to bear inventory risk) and **Informational** (wealth moves from the less to the better informed).
:::

**What the paper does:** seven robust friction measures from transaction data; 1,706 NYSE and AMSE stocks and 2,184 Nasdaq stocks; size of cost, real against informational friction, effect of market structure, and relations among the measures and with trading characteristics.

**Price of immediacy:** $s=a_0+a_1\log V+a_2\sigma^2+a_3\log MV+a_4\log P+a_5\log N+e$, where $s=(A-B)/2P$ is the proportional quoted **half**-spread.

::: hook
**Signs: "Volume and Price shrink it. Variance grows it. MV and N flip by market."**
$\log V$: $-$ (inventory easier to unload). $\sigma^2$: $+$ (inventory risk). $\log P$: $-$ (fixed cost spread over a higher price). $\log MV$ and $\log N$: $+$ on NYSE/AMSE, $-$ on Nasdaq.
Adjusted $R^2$: 0.77 NYSE/AMSE, 0.65 Nasdaq (Dec 1997). January and February 1998 are similar.
:::

::: box
- Stoll uses **half**-spreads: quoted $S=(A-B)/2$, effective $ES=\lvert P-M\rvert$. The traded spread: "refer to article".
- Chordia uses **full** spreads, so Chordia's effective spread $=2\times$ Stoll's.
:::

::: box
**Topic 2 numericals (example: bid 99.80, ask 100.20, buy at 100.10, depth 600 bid and 400 ask)**
QSPR $=0.40$. $P_M=100$. PQSPR $=0.40/100=0.004$. DEP $=500$. ESPR $=2(0.10)=0.20$. PESPR $=0.20/100.10=0.002$. The effective spread is smaller because the trade is inside the quotes.
:::

\newpage

# Topic 3: Triggers of Extreme Illiquidity

| Part | Source | Main point |
|---|---|---|
| Theory | Brunnermeier and Pedersen (2009) | Market liquidity and funding liquidity feed each other |
| Evidence | Margins on S&P 500 futures | Margins jump in a crisis |
| Measure | Jain, Mishra and McInish (2013) | Count bad spread days and bad price days over 10 days |
| Effect | Same paper | Spirals lower firm valuation |

**Why extreme cases matter (slide 2):** liquidity is key; trading should govern change; outside factors should not rule liquidity. In a crisis, funding decides liquidity, which breaks the third principle.

## 3.1 Brunnermeier and Pedersen (2009): the two liquidities

::: hook
**"Market liquidity belongs to the Asset. Funding liquidity belongs to the Trader."**
Traders give market liquidity only if they have funding. Funding (capital and margin) depends on how liquid the assets are. Margins can destabilize, so the two reinforce each other: a **spiral**.
:::

| Point | Market liquidity | Funding liquidity |
|---|---|---|
| Question | Can I sell easily near the true value? | Can I get money to hold this position? |
| Measured by | Spread, depth, price impact | Margin, haircut, cost of borrowing |
| Fails when | Buyers disappear | Lenders demand more capital |

::: hook
**"X is at most W over m."** Own capital pays the margin share $m$ of the position, so $mX\le W$, which gives $X\le W/m$.
**W falls = Loss spiral** (the numerator shrinks). **m rises = Margin spiral** (the denominator grows).
:::

## 3.2 Five features of liquidity (slide 5)

::: hook
**"Dry, Common, Volatile, Flees, Follows."**

1. **Dry**: it can suddenly dry up, because imperfectly informed financiers raise margins when volatility changes.
2. **Common**: many securities become illiquid together, because the same speculators supply liquidity in all of them.
3. **Volatile**: volatile assets are less liquid, because they need higher margins.
4. **Flees** (flight to quality): risky assets lose more liquidity, because scarce capital goes to low-margin assets.
5. **Follows** the market: liquidity falls when the market falls, because funding conditions move with the market.

The same five are the B-P findings in Topic 4 (slide 20).
:::

**Margins in crises (slide 6, approximate readings):** about 4% before 1987; above 12% on Black Monday (19 Oct 1987); about 3% in 1989, then the mini-crash raises it; about 6.4% in the 1990 to 1991 Iraq war; about 2% in calm 1997; about 3.8% in the Asian crisis; about 5.5% at LTCM (1998); about 4 to 5% in subprime (2007 to 2008). **Margins rise exactly when the market needs the traders.**

## 3.3 The liquidity spiral (slide 7)

::: hook
**Triggers, "LFVF":** first **L**oss; **F**unding shock (lenders cut credit); **V**olatility shock (financiers cannot tell news from illiquidity, so they raise margins); **F**orced sale (a large trader must unwind, and others may predate).

**Loop: "Lose, Can't fund, Sell, Price drops, then Lose more (loss) and Pay more margin (margin), back to Can't fund."**
:::

1. Initial loss $\to$ 2. funding problem $\to$ 3. reduce positions (deleverage) $\to$ 4. prices move away from fundamentals (market liquidity falls) $\to$ 5. losses on remaining positions (**loss spiral**) and 6. higher margins (**margin spiral**) $\to$ back to 2, stronger each time.

| Point | Loss spiral | Margin spiral |
|---|---|---|
| What changes | $W$ falls | $m$ rises |
| Cause | Price fall on existing positions | Financier fears volatility and illiquidity |
| Leverage | Sell to keep leverage constant | Must cut leverage |
| Needs a higher margin? | No | Yes |

::: box
1. Position $X=W/m$. Loan $=X-W$.
2. After a price fall of $f$: new position value $=X(1-f)$, new capital $W'=X(1-f)-\text{loan}$.
3. Loss-spiral sale $=X(1-f)-W'/m$. Margin-spiral sale $=W'/m-W'/m'$.

Example: $W=10$, $m=10\%$. $X=100$, loan 90. A 3% fall: position 97, $W'=7$. At 10%, allowed 70, so sell 27. At 14%, allowed 50, so sell 20 more. Total **47 of 97** sold after a 3% fall.
:::

## 3.4 Jain, Mishra and McInish (2013): the professor's spiral measures

"Identification and valuation implications of financial market spirals", in *Rethinking Valuation and Pricing Models*, from p. 471. **Learn the two definitions and the signs.**

::: hook
**"+1 is always bad."** For spreads, bad = **up**. For prices, bad = **down**. So the inequalities point opposite ways in the two measures.
**Two tests, both needed:** (1) a move versus yesterday, **and** (2) beyond the band = last year's mean $\pm$ **half** a standard deviation. Otherwise the score is 0.
**Sum the last 10 days.** A large positive sum = in a spiral.
:::

| Measure | +1 when | -1 when |
|---|---|---|
| Illiquidity spiral (spread) | $s_t>s_{t-1}$ **and** $s_t>\bar{s}+0.5\sigma_s$ | $s_t<s_{t-1}$ **and** $s_t<\bar{s}-0.5\sigma_s$ |
| Loss spiral (price) | $P_t<P_{t-1}$ **and** $P_t<\bar{M}-0.5\sigma_P$ | $P_t>P_{t-1}$ **and** $P_t>\bar{M}+0.5\sigma_P$ |

$$S_{spiral,10}=\sum_{k=0}^{9}S_{t-k},\qquad P_{spiral,10}=\sum_{k=0}^{9}L_{t-k}$$

**Data (slide 11):** CRSP daily bid, ask, volume, close, market cap, PERMCO for S&P 500 firms, Nov 1982 to Dec 2010; Datastream for P/B, dividends, total assets, ROE, and the S&P 500 value and P/E. Final sample **476 firms**.

**Histograms (slide 12):** the 10-day counts run from $-10$ to $10$. The loss measures have two humps away from zero, because losses and gains come in runs.

::: hook
**Valuation (slide 13): "Spirals shrink multiples."**
The **loss spiral** lowers both PTBV and P/E in all six models. The **illiquidity spiral** lowers P/E in all three models, and PTBV significantly once controls are added.
Size: a loss spiral of 10 lowers PTBV by $10(0.034)=0.34$ (model 5.1). Caution: $R^2$ is tiny, so the effects are significant but explain little. Conclusion: spirals have valuation implications.
:::

::: box
Spread score: today 0.95, yesterday 0.90, mean 0.80, sd 0.20. Upper limit $0.80+0.10=0.90$. Both $0.95>0.90$ tests hold, so +1.
Price score: today 95, yesterday 97, midpoint 100, sd 8. Lower limit $100-4=96$. Both $95<97$ and $95<96$ hold, so +1.
10-day sum: seven +1, one $-1$, two 0, so the sum is 6.
:::

\newpage

# Topic 4: Market-Wide Liquidity Phenomena

::: hook
**Four ways liquidity vanishes market-wide: "Prey, Betray, Pressure, Spiral."**
**Prey**: predatory trading, others trade against a distressed trader (B-P 2005). **Betray**: cooperation breaks down (Carlin, Lobo, Viswanathan 2007). **Pressure**: sellers demand liquidity together (Shkilko, Van Ness, Van Ness 2012). **Spiral**: funding and market liquidity feed each other (B-P 2009).
:::

## 4.1 Predatory trading: Brunnermeier and Pedersen (2005)

**Definition (slide 2):** exploiting an information advantage (non-public information or market dynamics) to profit at others' expense. It benefits the predator unfairly and harms other investors or the market. **Pattern: one trader must sell; others sell too; they buy back later.**

::: hook
**Five results, "OLIPS":** the price **O**vershoots; the distressed trader gets a **L**ower liquidation value; the market is **I**lliquid exactly when liquidity is most needed; a trader can **P**rofit by triggering another's crisis; the crisis **S**pills over across traders and markets.
:::

**Contribution (slide 3):** strategic interaction among large traders with market impact; traders trade continuously and limit their speed to keep temporary impact cost low; some become distressed, and the others know that they must sell.
**Specific contributions (slide 4):** (a) introduces predatory trading, which causes inefficiency; (b) types: front running, order anticipation, strategic trading ahead of a large order; (c) hard to identify: a regulator must separate a legitimate strategy from manipulation; (d) hurts liquidity, price efficiency, stability and investor confidence.

::: hook
**Findings: "Sell with them, then buy from them."** The normal view: others buy when someone sells cheaply. Predation: they **sell first** in the same direction, withdraw liquidity, the liquidation becomes costly, the price overshoots, and they **buy back later**.
**Profitable when "Illiquid and Big":** the market is illiquid, **and** the distressed position is large relative to the others' buying capacity.
:::

**Examples (slide 6):** Enron and UBS Warburg 2002 (taking the traders without the book: "predatory trading risk"); IAFE 2001 (detailed disclosure can ruin large portfolios); LTCM as victim 1998 (Goldman and other counterparties sold first); Meriwether (selling hurricane insurance doesn't cause a hurricane, but in markets those who know can cause the loss); Greenspan, 1 Oct 1998 (an LTCM forced sale would distort prices for uninvolved parties); Cramer 2002 ("smell blood in the water, become a shark"); Credit General 1995 (a billion pounds sterling, and the market evaporated).

**Framework:** continuous time; a riskless bond and a risky asset with supply $S>0$ paying $v$ at $T$, $E(v)=\mu$; $I$ large strategic traders (risk neutral, count their own impact) and long-term investors.
$$x^i(t)=x^i(0)+\int_0^t a^i(\tau)\,d\tau,\qquad -\bar{x}\le x^i(t)\le\bar{x}$$
Position = start + all trades; the limit comes from risk or capital. $a^i$ = trading speed (negative when selling).

::: box
**Simulated example:** $S=40$, $I=2$ (1 distressed), limit $\bar{x}=10$, each holds 8, distress at $t=5$, $T=7$, $\mu=140$, $\lambda=1$, speed $A=20$.

1. Each seller's speed: $20/2=10$. The distressed trader needs $8/10=0.8$, so the selling ends at 5.8.
2. The predator sells all 8 at the same time, so $8+8=16$ are sold.
3. Price fall $=\lambda\times 16=16$: from **116 to 100**.
4. The predator buys back from 0 to its limit 10, alone at speed 20: $10/20=0.5$, ending at 6.3.
5. New price **110**. **Overshoot $=110-100=10$.**

Rule: price change $=\lambda\times$ shares traded. Overshoot = final price $-$ lowest price.
:::

::: hook
**More predators, less overshoot: "competition eats predation."**
With 3, 9, 27 traders (total holding 16), the lowest price is about 110, 112.5, 113.1 and the final is about 113.3. The overshoot shrinks to about 3.3, 0.8, 0.2. More predators also start buying back earlier.
:::

## 4.2 Carlin, Lobo and Viswanathan (2007): episodic crises

::: hook
**"RHEC": Repeated game, High stakes, Episodic, Contagion.**
In one period, predating pays. In a repeated game, traders cooperate (they give apparent liquidity to each other), because predating today loses future cooperation. When the **stakes are high**, today's gain beats the future loss, so cooperation breaks and predation starts: **episodic** illiquidity. Cooperation across markets makes crises rarer, but a breakdown then hits all of them: **contagion**.
:::

| Point | Cooperation | Predation |
|---|---|---|
| When | Most of the time, small stakes | Sometimes, high stakes |
| Action | Supply liquidity to the one in need | Sell with the one in need |
| Market | Looks liquid | Suddenly illiquid |

## 4.3 Shkilko, Van Ness and Van Ness (2012): "Short selling and intraday price pressures"

Financial Management 41(2), 345 to 370.

::: hook
**"Longs lead, shorts follow."** Intraday declines are driven mostly by **long sellers** (non-short volume that demands liquidity). Short sellers make declines somewhat worse, and they trade more intensely in the decline stage of large reversals. They **switch** from providing liquidity to demanding it. Their effect is **second** to the long sellers', which contradicts the view that short sellers destabilize markets on their own.
:::

::: hook
**Large reversal: "Two sigma down, 90 to 110 back."**
$\sigma_i$ = average sd of 5-minute cumulative returns over the previous 20 days.
Decline: $\ell\le-2\sigma_i$. Rebound by the close: $0.9\lvert\ell\rvert\le R_{close}-\ell\le 1.1\lvert\ell\rvert$.
(The slide figure prints $\ell\ge-2\sigma$. The text needs $\le$.)
:::

::: box
$\sigma_i=1\%$, low $\ell=-2\%$. Smallest rebound $1.8$, so the close is $-0.2\%$. Largest rebound $2.2$, so the close is $+0.2\%$. The day must end between $-0.2\%$ and $+0.2\%$.
:::

## 4.4 Spirals (slides 16 to 20) and the whole topic

Same B-P (2009) loop as Topic 3: funding drives market liquidity; market liquidity drives capital and margins; margins can destabilize. Trigger: margins rise in crises (1987, 1998, 2007). Loss spiral (losses cut capital) and margin or haircut spiral (higher margins cut leverage). **Findings = the five features: "Dry, Common, Volatile, Flees, Follows"**, with dry-up when financiers are imperfectly informed and fundamental volatility varies over time.

| Phenomenon | Explanation |
|---|---|
| Commonality | Chordia et al.; funding limits |
| Dry-up | Margin spiral |
| Flight to quality | Scarce funding |
| Overshooting | Predatory trading |
| Episodic illiquidity | Breakdown of cooperation |
| Contagion | Common traders and broken cooperation |
| Large reversal | Temporary selling pressure |

| Point | Predation | Broken cooperation | Spiral |
|---|---|---|---|
| Trigger | Another must sell | Stakes become high | Loss or margin rise |
| Forced? | Victim forced, predator chooses | Predators choose | All forced by funding |
| Strategy needed? | Yes | Yes | No |
| Key limit | Buyers' position limit | Value of future cooperation | Capital and margin |

**Exam:** a market-wide liquidity answer has three layers: define commonality, then give the mechanism, then give the evidence.

\newpage

# Topic 5: Basic Concepts

**What microstructure covers (slides):** trading rules; physical layouts (NSE NEAT); information systems; how participants interact; safeguards (price bands, circuit breakers, halts).

::: hook
**Kissell (2014), five foci: "Venues, Discovery, Spreads, Intraday, Costs."** Structure of exchanges and venues (lit and dark); price discovery; determinants of spreads and quotes; intraday trading behaviour; transaction costs.
**Why we trade: "PIP":** Profit, Information, Price discovery.
**Dimensions of a market:** platform (manual or automated: speed, integration, stabilizers); information flow; traders' interaction; regulation; imperfections (transaction cost and information asymmetry).
:::

::: hook
**Seven trader types: "Please Bring Dad's Huge Avocado, Very Fresh."**
**P**roprietary traders, **B**rokers (agency), **D**ealers, **H**edgers, **A**rbitrageurs, **V**alue investors, **F**ront runners.
:::

**Harris facts:** trading is zero-sum relative to the market average; brokers are agents; patient traders get better prices; speculators trade on information about future prices; dealers lose to well-informed speculators; bluffers fool the uninformed; investors move money to the future and borrowers to the present; hedgers manage risk; asset exchangers swap assets; gamblers trade for fun; arbitrageurs keep prices aligned across markets; the sell side (dealers, brokers) serves the buy side.

**Basic terms:** bid = best price to sell at; ask = best price to buy at; mid = their average; spread = ask $-$ bid; BBO and NBBO; price impact; uptick, downtick, zero tick.

| Point | Block deal | Bulk deal |
|---|---|---|
| Size | One trade $\ge$ 5,00,000 shares or $\ge$ Rs 10 crore | $\ge$ 0.5% of listed shares |
| When | Separate window: 8:45 to 9:00 AM or 2:05 to 2:20 PM | Normal hours |
| Visible | Not to retail | To everyone |

::: hook
**Liquidity dimensions: "I Want Deep Rivers."** **I**mmediacy (how fast), **W**idth (the spread: cost of a small trade), **D**epth (how much at a price), **R**esiliency (how fast the price recovers after a large trade).
**Market quality, five: "Let Traders Invest Very Profitably."** **L**iquidity, **T**ransaction cost, **I**nformative prices, **V**olatility, trading **P**rofits.
:::

**Orders:** market (trade now; takes liquidity, pays the spread; risk: poor price), limit (at the limit or better; provides liquidity; risks: execution uncertainty and adverse selection, i.e. ex post regret), stop (activates at the stop price; a sell stop protects a long).
**Design:** continuous vs call (NSE pre-open is a call auction); quote-driven (dealers) vs order-driven (rules match orders); circuit breaker (halt after a large move).

**Volatility:** total = fundamental + transitory.

| Point | Fundamental | Transitory |
|---|---|---|
| Cause | Unanticipated value changes (earnings news) | Impatient uninformed trading (bid-ask bounce, big uninformed orders) |
| Life | Permanent | Temporary: prices revert |
| Who ends it | Not applicable | Value traders and arbitrageurs |

Dealers infer information from order flow; this adverse-selection part of the spread adds to **fundamental** volatility. Bid-ask bounce: buyers trade at the ask and sellers at the bid, so the price jumps without news.

**Inventory vs information models:** inventory = unbalanced inventory, cost and risk of inventory, temporary effect (Garman, Amihud-Mendelson, Stoll, Ho-Stoll, O'Hara-Oldfield). Information = better-informed customers, expected loss to the informed, permanent effect (Bagehot, Copeland-Galai, Glosten-Milgrom, Kyle, Easley-O'Hara).

## 5.1 Roll (1984): the spread from prices

::: hook
**"Bounce shares one sign, with a minus."** Two neighbouring price changes share only $Q_{t-1}$, and it enters them with opposite signs. So $\mathrm{Cov}=-(S/2)^2$, and **$S=2\sqrt{-\mathrm{Cov}}$.**
:::

**Assumptions:** value is a random walk, $V_t=V_{t-1}+\varepsilon_t$ (mean 0, variance $\sigma^2$, independent); constant spread $S$; $Q_t=\pm 1$ with prob $\tfrac12$ each; signs are independent over time and of news.

**Bird's-eye proof**

1. Trade price $=$ value $\pm$ half-spread: $P_t=V_t+\tfrac{S}{2}Q_t$.
2. Change: $\Delta P_t=\varepsilon_t+\tfrac{S}{2}(Q_t-Q_{t-1})$.
3. Variance: $\mathrm{Var}(\Delta P_t)=\sigma^2+\tfrac{S^2}{4}\cdot 2=\sigma^2+\tfrac{S^2}{2}$.
4. Covariance: $\tfrac{S^2}{4}E[(Q_t-Q_{t-1})(Q_{t-1}-Q_{t-2})]$. Of the four products, only $-Q_{t-1}^2$ has a nonzero mean ($-1$). So $\mathrm{Cov}=-S^2/4$.
5. Solve: $S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$.

**Limits:** fails if the sample Cov > 0; assumes trades carry no information; assumes a constant spread.

::: box
- $S=2\sqrt{-\mathrm{Cov}}$. Example: Cov $=-0.0625$, so $S=2(0.25)=0.5$.
- Axis Bank: bid 664.40 (453 shares), ask 664.55 (714 shares). Spread 0.15. Mid 664.475. Proportional spread $0.15/664.475=0.0226\%$. Depth $(714+453)/2=583.5$.
:::

\newpage

# Last-look formula sheet

::: box
**C-G:** $\max(1-\pi_I)G_U-\pi_IL_I$. Symmetric case: $h=\pi_I\Delta$.

**G-M** ("tilt, then normalise", $\theta=\Pr(V_L)$): buy weights $\theta(1-\mu),\,(1-\theta)(1+\mu)$; sale weights $\theta(1+\mu),\,(1-\theta)(1-\mu)$.
$s=\dfrac{4\theta(1-\theta)\mu(V_H-V_L)}{1-(1-2\theta)^2\mu^2}$; at $\theta=\tfrac12$, $s=\mu\Delta V$. $\Pr(B)=\tfrac12[1+\mu(1-2\theta)]$.

**Kyle** ("everything halves"): $\lambda=\dfrac{\sigma_0}{2\sigma_y}$, $\beta=\dfrac{\sigma_y}{\sigma_0}$, $p=p_0+\lambda z$, $E\pi_I=\dfrac{\sigma_0\sigma_y}{2}$ = noise loss, $\mathrm{Var}(v\mid z)=\dfrac{\sigma_0^2}{2}$.

**E-O:** $V^{\ast}=\delta\underline{V}+(1-\delta)\bar{V}$. Large bid = average of $V^{\ast}$ [weight $X_S^2(1-\alpha\mu)$] and $\underline{V}$ [weight $\alpha\delta\mu$]. Formula form: $b_2=V^{\ast}-\dfrac{\sigma_v^2}{\bar{V}-\underline{V}}\cdot\dfrac{\alpha\mu}{X_S^2(1-\alpha\mu)+\delta\alpha\mu}$. Small: $V^{\ast}$. Separation: $B^2/B^1\ge 1+\dfrac{\alpha\mu(1-\delta)}{X_B^2(1-\alpha\mu)}$.

**Chordia:** QSPR $=A-B$; PQSPR $/P_M$; DEP $=(Q_A+Q_B)/2$; ESPR $=2\lvert P_t-P_M\rvert$; PESPR $/P_t$. $DL_{j,t}=\alpha_j+\beta_jDL_{M,t}+\varepsilon$; $\beta\approx 0.69$.

**Amihud:** ILLIQ = mean of $\lvert R_d\rvert/VOLD_d$ (ratio first). Amivest $=\sum VOLD/\sum\lvert R\rvert$.

**Lesmond:** $LOT=\alpha_2-\alpha_1$. **Stoll:** half-spreads $(A-B)/2$ and $\lvert P-M\rvert$.

**Roll:** $S=2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$; $\mathrm{Var}(\Delta P)=\sigma^2+S^2/2$.

**Funding:** $X\le W/m$. **Spirals:** score $\pm1$ or 0 against the band (mean $\pm\tfrac12$sd), with +1 bad; sum 10 days.

**Predation:** price change $=\lambda\times$ shares; 116 $\to$ 100 $\to$ 110, overshoot 10.

**Shkilko:** $\ell\le-2\sigma_i$ and $0.9\lvert\ell\rvert\le R_{close}-\ell\le 1.1\lvert\ell\rvert$.
:::
