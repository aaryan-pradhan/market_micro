---
title: "Endsem Cram Sheet (20 minutes)"
geometry: margin=1.5cm
fontsize: 10pt
header-includes:
  - |
    ```{=latex}
    \usepackage{tikz}
    \usetikzlibrary{arrows.meta,positioning,calc}
    \tikzset{n/.style={draw,rounded corners,fill=white,inner sep=3pt,font=\small,align=center},e/.style={-{Stealth},thick},p/.style={font=\footnotesize,fill=white,inner sep=1pt}}
    ```
---

# 1. Information-based models

## Bagehot (1971)

A market gain comes when the whole market rises, so everybody gains. A trading gain comes from trading better than others, so not everybody gains. The dealer loses to informed traders. The spread lets the dealer recover these losses from uninformed traders.

## Copeland and Galai (1983)

**Assumptions.** There is one period. There is a single risk-neutral dealer. Traders are informed or uninformed (liquidity traders). Traders arrive with given probabilities.

**Symbols.** $\pi_I$ is the probability that an informed trader arrives. $\pi_{BL}$, $\pi_{SL}$ and $\pi_{NL}$ are the probabilities that an uninformed trader buys, sells or does not trade.

If the true price $P>P_A$, the informed trader buys, and the dealer loses $P-P_A$. If $P<P_B$, the informed trader sells, and the dealer loses $P_B-P$.

Expected loss to an informed trader:
$$L_I=\int_{P_A}^{\infty}(P-P_A)f(P)\,dP+\int_0^{P_B}(P_B-P)f(P)\,dP$$

Expected gain from an uninformed trader:
$$G_U=\pi_{BL}(P_A-P)+\pi_{SL}(P-P_B)+\pi_{NL}(0)$$

The dealer chooses $P_A$ and $P_B$ to maximize expected profit, which must be at least zero:
$$\max_{P_A,P_B}\ (1-\pi_I)G_U-\pi_IL_I\ \ge0$$

The ask is a free call option, and the bid is a free put option, that the dealer gives to the informed trader.

**Limitations.** There is only a single period. New information is assumed to be revealed instantly.

**Findings.** The spread rises with the price level and the return variance. The spread falls with market activity, depth and continuity.

## Glosten and Milgrom (1985)

Trading is sequential: one trader arrives at a time and trades one unit. The dealer is competitive and earns zero expected profit. $\theta$ is the probability of good news ($V_H$). $\mu$ is the share of informed traders. An uninformed trader buys with probability $\gamma^B$ and sells with probability $\gamma^S$.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[n] (r) at (0,0) {Nature};
\node[n,fill=green!10] (H) at (2.8,1.8) {$V_H$ (good)};
\node[n,fill=red!10] (L) at (2.8,-1.8) {$V_L$ (bad)};
\node[n] (HI) at (5.8,2.7) {Informed};
\node[n] (HU) at (5.8,0.9) {Uninformed};
\node[n] (LU) at (5.8,-0.9) {Uninformed};
\node[n] (LI) at (5.8,-2.7) {Informed};
\draw[e] (r) -- node[p,above left]{$\theta$} (H);
\draw[e] (r) -- node[p,below left]{$1-\theta$} (L);
\draw[e] (H) -- node[p,above]{$\mu$} (HI);
\draw[e] (H) -- node[p,below]{$1-\mu$} (HU);
\draw[e] (L) -- node[p,above]{$1-\mu$} (LU);
\draw[e] (L) -- node[p,below]{$\mu$} (LI);
\node[anchor=west,font=\small] (a) at (7.3,2.7) {\textbf{BUY} for sure: $\theta\mu$};
\node[anchor=west,font=\small] (b) at (7.3,0.9) {buy $\theta(1-\mu)\gamma^B$,\quad sell $\theta(1-\mu)\gamma^S$};
\node[anchor=west,font=\small] (c) at (7.3,-0.9) {buy $(1-\theta)(1-\mu)\gamma^B$,\quad sell $(1-\theta)(1-\mu)\gamma^S$};
\node[anchor=west,font=\small] (d) at (7.3,-2.7) {\textbf{SELL} for sure: $(1-\theta)\mu$};
\draw[e] (HI)--(a); \draw[e] (HU)--(b); \draw[e] (LU)--(c); \draw[e] (LI)--(d);
\end{tikzpicture}
\end{center}
```

Add the buy leaves and the sell leaves of the tree:
$$P(B)=\theta\mu+(1-\mu)\gamma^B,\qquad P(S)=(1-\theta)\mu+(1-\mu)\gamma^S$$

Bayes rule is $P(A\mid B)=P(A\cap B)/P(B)$. So
$$P(V_H\mid B)=\frac{\theta\mu+\theta(1-\mu)\gamma^B}{\theta\mu+(1-\mu)\gamma^B},\qquad P(V_H\mid S)=\frac{\theta(1-\mu)\gamma^S}{(1-\theta)\mu+(1-\mu)\gamma^S}$$

$P(V_L\mid B)=1-P(V_H\mid B)$ and $P(V_L\mid S)=1-P(V_H\mid S)$. Note that $P(V_H\mid S)$ is **not** $1-P(V_H\mid B)$.

The ask and the bid are the expected values given the trade:
$$a=E[V\mid B]=V_HP(V_H\mid B)+V_LP(V_L\mid B),\qquad b=E[V\mid S]=V_HP(V_H\mid S)+V_LP(V_L\mid S)$$

With $\gamma^B=\gamma^S=0.5$, the spread is
$$s=a-b=\frac{4\theta(1-\theta)\mu(V_H-V_L)}{1-(1-2\theta)^2\mu^2}$$

When $\theta=0.5$, this becomes $s=\mu(V_H-V_L)$. So the spread rises with $\mu$, the share of insiders. The spread is positive even with zero cost and zero profit, so it is pure adverse selection.

## Kyle (1985)

It is a batch auction, not sequential trading. All orders clear at a single price. The base model has one period; it extends to many periods.

| Item | Formula |
|---|---|
| Asset value | $v\sim N(p_0,\sigma_0^2)$ |
| Noise trader demand | $y\sim N(0,\sigma_y^2)$ |
| Total demand ($x$ is the insider's demand) | $z=x(v)+y$ |
| Price function ($\lambda$ is inverse liquidity) | $p(z)=\lambda z+\mu$ |
| Insider's profit | $\pi_I=x(v-p)$ |
| Optimal insider demand | $x=(v-\mu)/2\lambda$ |
| Linear insider strategy | $x=\alpha+\beta v$, with $\alpha=-\mu/2\lambda$ and $\beta=1/2\lambda$ |
| Insider sensitivity | $\beta^\ast=\sigma_y/\sigma_0$ |
| Price intercept | $\mu^\ast=p_0$ |
| Inverse liquidity | $\lambda^\ast=\sigma_0/2\sigma_y$ |
| Conditional variance | $\mathrm{Var}(v\mid z)=\sigma_0^2/2$ |
| Insider's expected profit | $E(\pi_I)=\sigma_y\sigma_0/2$ |
| Liquidity traders' expected loss | $E(\pi_L)=\lambda\sigma_y^2=\sigma_y\sigma_0/2$ |

**Derivation.** The insider's expected profit is $E(\pi_I)=E[x(v-\lambda(x+y)-\mu)]=x(v-\lambda x-\mu)$. Set $dE(\pi_I)/dx=0$, which gives $x=(v-\mu)/2\lambda$. The dealer sets the price to the expected value given the order flow:
$$p(z)=E(v\mid z)=p_0+\frac{\beta(z-\alpha-\beta p_0)\sigma_0^2}{\sigma_y^2+\beta^2\sigma_0^2}$$

Here $\alpha$ is the intercept, and $\beta$ is how much the insider's demand changes when the asset value changes. Matching the two gives $\lambda^\ast$, $\mu^\ast$ and $\beta^\ast$.

The noise traders pay for the insider's profit. Half of the private information enters the price.

## Easley and O'Hara (1987)

Traders trade different quantities. There is no transaction cost. Trading is sequential, as in Glosten and Milgrom. There are several competitive, risk-neutral market makers. There is dual uncertainty: (i) does a trader actually have new private information, and (ii) if new information exists, is it good or bad?

**Symbols.** $\alpha$ is the probability that an information event occurred. $\delta$ is the probability that the signal is low, given an event, so $P(L)=\delta$ and $P(H)=1-\delta$. $\mu$ is the fraction of informed traders. $\underline V=E(V\mid s=L)$ and $\bar V=E(V\mid s=H)$, with $\bar V>\underline V$. The initial unconditional value is $V^\ast=\delta\underline V+(1-\delta)\bar V$. Sizes are $0<B^1<B^2$ (small and large buy) and $0<S^1<S^2$ (small and large sell). $X_B^i$ is the fraction of uninformed traders who want to trade quantity $B^i$, and $X_S^i$ is the same for $S^i$. In equilibrium, each dealer's expected profit is zero; dealers keep in mind the quantity and the other dealers.

**Separating equilibrium.** The informed trader trades only the large quantity. The dealer sees a large quantity, guesses that the trader may be informed, and adjusts the price to lower losses. So the market separates informed and uninformed traders. Small trades get $V^\ast$. Large trades get:
$$b_2^\ast=V^\ast-\frac{\sigma_v^2}{\bar V-\underline V}\left[\frac{\alpha\mu}{X_S^2(1-\alpha\mu)+\delta\alpha\mu}\right],\qquad a_2^\ast=V^\ast+\frac{\sigma_v^2}{\bar V-\underline V}\left[\frac{\alpha\mu}{X_B^2(1-\alpha\mu)+\alpha\mu(1-\delta)}\right]$$

**Pooling equilibrium.** The informed trader trades both quantities. The dealer cannot guess the type from the size, so the dealer cannot separate by size, and both sale sizes are priced below $V^\ast$.

**Spread with cost $C$** (transaction cost and risk premium). The dealer sees only the side and size of the trade:
$$A=E[V\mid \text{buy}]+C,\qquad B=E[V\mid \text{sell}]-C,\qquad S=A-B=E[V\mid\text{buy}]-E[V\mid\text{sell}]+2C$$

**Price path: small trade, then a large sell, then a small trade.**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\begin{scope}
\draw[-{Stealth}] (0,0)--(5.5,0) node[right,font=\small]{time};
\draw[-{Stealth}] (0,0)--(0,3.2) node[above,font=\small]{price};
\draw[dashed] (0,2.6)--(5,2.6) node[right,font=\small]{$V^\ast$};
\draw[dashed] (0,0.8)--(5,0.8) node[right,font=\small]{$b_2$};
\draw[very thick,blue] (1,2.6)--(2.5,0.8)--(4.2,0.8);
\foreach \x/\y in {1/2.6,2.5/0.8,4.2/0.8} \fill[blue] (\x,\y) circle (2.5pt);
\node[below,font=\small] at (1,0) {small}; \node[below,font=\small] at (2.5,0) {large sell}; \node[below,font=\small] at (4.2,0) {small};
\node[font=\small\bfseries] at (2.7,3.6) {Trader uncertainty only};
\end{scope}
\begin{scope}[xshift=8.5cm]
\draw[-{Stealth}] (0,0)--(5.5,0) node[right,font=\small]{time};
\draw[-{Stealth}] (0,0)--(0,3.2) node[above,font=\small]{price};
\draw[dashed] (0,2.6)--(5,2.6) node[right,font=\small]{$V^\ast$};
\draw[dashed] (0,0.8)--(5,0.8) node[right,font=\small]{$b_2$};
\draw[very thick,red] (1,2.6)--(2.5,0.8)--(4.2,1.6);
\foreach \x/\y in {1/2.6,2.5/0.8,4.2/1.6} \fill[red] (\x,\y) circle (2.5pt);
\node[right,font=\scriptsize,align=left] at (4.25,1.6) {partial\\recovery};
\node[below,font=\small] at (1,0) {small}; \node[below,font=\small] at (2.5,0) {large sell}; \node[below,font=\small] at (4.2,0) {small};
\node[font=\small\bfseries] at (2.7,3.6) {Trader + event uncertainty};
\end{scope}
\end{tikzpicture}
\end{center}
```

With trader uncertainty only, the small trade after the block says nothing new, so the price stays at $b_2$. With event uncertainty too, a small trade makes "no event" more likely, so the price recovers part of the way but stays below $V^\ast$.

**Findings.** Trade size carries information. Informed traders prefer large trades. Large trades get worse prices.

\newpage

# 2. Liquidity measures

## Chordia, Roll and Subrahmanyam (2000): commonality

**Liquidity dimensions.** (i) Tightness or width is the spread. (ii) Depth is the quantity at the quote. (iii) Immediacy is how quickly a trade can be executed. (iv) Resiliency is how quickly the market recovers to the original price.

**Causes of commonality.** (i) Trading activity, (ii) trading volume, (iii) carrying costs (interest rates), (iv) volatility, (v) program trading, (vi) institutional funds, and (vii) asymmetric information.

**Five measures.** The mid price is $P_M=(P_A+P_B)/2$, and $P_t$ is the transaction price.

| Measure | Formula |
|---|---|
| Quoted spread | $P_A-P_B$ |
| Proportional quoted spread | $(P_A-P_B)/P_M$ |
| Depth | $\tfrac12(Q_A+Q_B)$ |
| Effective spread | $2\lvert P_t-P_M\rvert$ |
| Proportional effective spread | $2\lvert P_t-P_M\rvert/P_t$ |

The daily percentage change in a measure is $DL_t=(L_t-L_{t-1})/L_{t-1}$.

**Regression 1 (market).** $DL_{j,t}=\alpha_j+\beta_jDL_{M,t}+\varepsilon_{j,t}$. A positive $\beta_j$ means that each stock's liquidity moves with the market. This is commonality.

**Regression 2 (market and industry).** $DL_{j,t}=\alpha_j+\beta_{j,M}DL_{M,t}+\beta_{j,I}DL_{I,t}+\varepsilon_{j,t}$. It shows which factor, market or industry, contributes.

**Regression 3 (what drives it).** Inventory risk and asymmetric information make the number of trades and the trade size important.
$$DL_{j,t}=\alpha_j+\beta_{j,S}DS_{j,t}+\beta_{j,T}DT_{j,t}+\beta_{j,M}DV_{M,t}+\beta_{j,I}DV_{I,t}+\varepsilon_{j,t}$$

$DS_{j,t}$ is the percent change in the average dollar trade size of stock $j$ on day $t$. $DT_{j,t}$ is the change in the number of trades. $DV_{M,t}$ is the change in total market dollar volume, excluding $j$. $DV_{I,t}$ is the change in total industry dollar volume, excluding $j$.

**Signs.** General trading activity lowers the spread. Informed trading raises the spread. The number of trades $DT$ raises the spread. Market volume $DV_M$ lowers the spread. Trade size $DS$ raises the spread and the depth. Industry volume $DV_I$ lowers depth.

## Amihud (2002): illiquidity ratio

$$ILLIQ_{iy}=\frac{1}{D_{iy}}\sum_{d=1}^{D_{iy}}\frac{\lvert R_{iyd}\rvert}{VOLD_{iyd}}$$

Here $i$ is the stock, $y$ the year and $d$ the trading day. $R_{iyd}$ is the daily return, $VOLD_{iyd}$ is the daily dollar volume traded, and $D_{iy}$ is the number of trading days. A higher ILLIQ means more illiquidity and less liquidity.

**Check against detailed measures.** $ILLIQ_{iy}=-292+247.9\lambda_i+49.2\psi_i$, where $\lambda_i$ is Kyle's lambda (inverse liquidity) and $\psi_i$ is the fixed cost. Both slopes are positive, so the simple ratio agrees with the detailed measures.

**Fama-MacBeth regression.**
$$R_{imy}=k_{0my}+\sum_{j=1}^{J}k_{jmy}X_{ji,y-1}+U_{imy}$$

$R_{imy}$ is the return of stock $i$ in month $m$ of year $y$. $X_{ji,y-1}$ is characteristic $j$ of stock $i$ in the last year ($y-1$): illiquidity, company size and beta. $J$ is the number of characteristics, and $U_{imy}$ is the residual. Returns rise with ILLIQ, so people demand more return from illiquid stocks.

## Ince (2022)

Illiquidity has three parts: a normal level (alpha), systematic illiquidity, and idiosyncratic illiquidity, which depends only on the stock. Systematic illiquidity matters only for very small stocks and disappears when they are removed. Idiosyncratic illiquidity predicts future returns.

## Stoll (2000): friction

Friction is the cost or difficulty that investors face. Time friction is the time needed to trade. Price friction is the cost of immediacy; Stoll uses price friction.

$$s=a_0+a_1\log V+a_2\sigma^2+a_3\log MV+a_4\log P+a_5\log N+e$$

$V$ is daily dollar volume, $\sigma^2$ the return variance, $MV$ the market value, $P$ the closing price and $N$ the number of trades per day. The spread $s$ is half the proportional quoted spread: $s=\tfrac12\times(A-B)/P$. The spread rises with $\sigma^2$ (and with $\log MV$ and $\log N$ on NYSE). The spread falls with $\log V$ and $\log P$.

## Lesmond (2005): emerging markets

Many emerging markets have no bid and ask data, so cost is estimated from daily prices. The LOT measure says an investor trades only when the value of information beats the cost. So the price does not move (a zero return) inside a band. The selling cost is $\alpha_1<0$ and the buying cost is $\alpha_2>0$. The round-trip cost is $LOT=\alpha_2-\alpha_1$.

**Findings.** Across countries, the price-based measures LOT and Roll work better than volume-based ones. Within a country, LOT works best, and Amihud less so. Countries with weak political and legal institutions have higher liquidity costs.

\newpage

# 3. Extreme illiquidity

Market liquidity is how easily an asset can be bought or sold. Funding liquidity is how easily traders can obtain funds. Brunnermeier and Pedersen (2009) show that they feed each other through margin requirements. In extreme market events, margin requirements rise.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[n,fill=gray!15] (A) at (-6.3,1.6) {Initial\\losses};
\node[n,fill=orange!15] (B) at (-2.6,1.6) {Funding\\problems};
\node[n,fill=orange!15] (C) at (1.2,1.6) {Reduced\\positions};
\node[n,fill=orange!15] (D) at (5.2,1.6) {Prices move away\\from fundamentals};
\node[n,fill=red!10] (F) at (1.2,-0.9) {Losses on existing positions (\textbf{loss spiral})};
\node[n,fill=red!10] (E) at (1.2,-2.4) {Higher margins (\textbf{margin spiral})};
\draw[e] (A)--(B); \draw[e] (B)--(C); \draw[e] (C)--(D);
\draw[e] (D.south) |- (F.east); \draw[e] (D.south) |- (E.east);
\draw[e] (F.west) -| ($(B.south)+(-0.4,0)$);
\draw[e] (E.west) -| ($(B.south)+(0.4,0)$);
\end{tikzpicture}
\end{center}
```

**How to measure a spiral (Jain, Mishra and McInish 2013).** Each day gets a score of $-1$, 0 or $+1$, and $+1$ is always bad. The band is last year's average plus or minus half its standard deviation. Both conditions must hold; otherwise the score is 0.

**(i) Spread method (illiquidity spiral).**

- $S=+1$ if the current spread is above the previous day's spread **and** above last year's average spread $+\tfrac12\sigma$.
- $S=-1$ if the current spread is below the previous day's spread **and** below last year's average spread $-\tfrac12\sigma$.
- $S=0$ if neither holds.

A score of $+1$ means the spread rose, so liquidity fell. A score of $-1$ means the spread fell, so liquidity rose.

**(ii) Price method (loss spiral).**

- $P=+1$ if the current price is below the previous price **and** below last year's midpoint $-\tfrac12\sigma$.
- $P=-1$ if the current price is above the previous price **and** above last year's midpoint $+\tfrac12\sigma$.
- $P=0$ if neither holds.

Each score is summed over 10 days: $S_{spiral,10}=\sum_{t=0}^{9}S_{spiral,t}$, and the same for prices. Both spirals lower firm valuation (P/E and price to book).

**Features of liquidity.** Liquidity can suddenly dry up. Many assets become illiquid together. Volatile assets are less liquid. Capital flees to quality. Liquidity falls when the market falls.

# 4. Market-wide liquidity

**Predatory trading (Brunnermeier and Pedersen 2005).** A large trader is forced to sell. Other strategic traders sell at the same time, and then buy back later at a low price. So the price overshoots, the distressed trader gets less, and the market is illiquid exactly when liquidity is needed. Predation pays when the market is illiquid and the distressed position is big. More predators competing reduce the overshoot.

**Episodic crises (Carlin, Lobo and Viswanathan 2007).** Traders meet again and again, so they usually cooperate and give liquidity to each other. When the stakes become high, the gain from predating today beats the value of future cooperation. Cooperation breaks down, and a sudden liquidity crisis follows. This can spread to other markets.

**Price pressure (Shkilko, Van Ness and Van Ness 2012).** On days with a large intraday fall that reverses, long sellers who demand liquidity drive most of the fall. Short sellers add to the fall but come second. A large reversal is a fall of at least $2\sigma_i$ that recovers 90 to 110 percent by the close.

**Liquidity spirals.** The loss spiral and the margin spiral from Topic 3 also spread illiquidity across the whole market.
