---
title: "Endsem Cram Sheet"
subtitle: "One picture per model. Every formula, number and finding is read off the picture."
geometry: margin=1.5cm
fontsize: 10pt
header-includes:
  - |
    ```{=latex}
    \usepackage[most]{tcolorbox}
    \usepackage{tikz}
    \usetikzlibrary{arrows.meta,positioning,calc,decorations.pathreplacing}
    \tikzset{n/.style={draw,rounded corners,fill=white,inner sep=3pt,font=\small,align=center},e/.style={-{Stealth},thick},p/.style={font=\footnotesize,fill=white,inner sep=1pt}}
    ```
---

**How to use this sheet.** Each model has one master picture. Learn the picture first. Then read each formula off it, in the order given. Blue boxes are mnemonics. Orange boxes are formulas to write from memory. The letters of each mnemonic are in bold in the list below it.

::: {.hook title="The whole course in five lines"}
1. Informed traders create a spread and a price impact. (Topic 1)
2. Liquidity measures tell us how large these costs are. (Topic 2)
3. Funding limits turn a small loss into extreme illiquidity. (Topic 3)
4. Common funding and strategic selling spread illiquidity across the market. (Topic 4)
5. Illiquidity lowers prices and raises the return that investors demand. (All)
:::

| Chance | Likely question | Section here |
|---|---|---|
| Very high | Bid, ask and spread in Glosten and Milgrom | 1.5 |
| Very high | Kyle's $\lambda$ and the insider's profit | 1.6 |
| High | Trade size, separating and pooling in Easley and O'Hara | 1.7 |
| High | Compare Lesmond, Chordia and Amihud | 2.2, 2.3, 2.5, 2.7 |
| High | Liquidity spirals and their triggers | 3.3, 3.4 |
| High | Spiral scores from spread and price data | 3.5 |
| High | Predatory trading and overshooting | 4.1 |
| Medium | Commonality and market-wide illiquidity | 2.2, 4.5 |
| Medium | Copeland and Galai option view | 1.4 |
| Medium | Episodic crises, large reversals | 4.2, 4.3 |
| Low | Inventory against information, Bagehot, Ince, Stoll, Roll | 1.3, 2.4, 2.6, 5 |

\newpage

# Topic 1: Information-based models

## 1.1 The chain of five models

**Mnemonic: "The dealer WOBLS."** Each model fixes the one before it. The words under each arrow are the weakness that the next model fixes.

```{=latex}
\begin{center}
\begin{tikzpicture}[node distance=0.4cm]
\node[n,font=\footnotesize,fill=gray!10] (W) {\textbf{W}ords\\Bagehot 1971};
\node[n,font=\footnotesize,fill=gray!10,right=of W] (O) {\textbf{O}ptions\\Copeland--Galai 1983};
\node[n,font=\footnotesize,fill=gray!10,right=of O] (B) {\textbf{B}ayes\\Glosten--Milgrom 1985};
\node[n,font=\footnotesize,fill=gray!10,right=of B] (L) {\textbf{L}ambda\\Kyle 1985};
\node[n,font=\footnotesize,fill=gray!10,right=of L] (S) {\textbf{S}ize\\Easley--O'Hara 1987};
\draw[e] (W)--(O); \draw[e] (O)--(B); \draw[e] (B)--(L); \draw[e] (L)--(S);
\node[font=\scriptsize,align=center] at ($(W)!0.5!(O)+(0,-0.9)$) {no\\equation};
\node[font=\scriptsize,align=center] at ($(O)!0.5!(B)+(0,-0.9)$) {one period,\\no learning};
\node[font=\scriptsize,align=center] at ($(B)!0.5!(L)+(0,-0.9)$) {one unit,\\no impact};
\node[font=\scriptsize,align=center] at ($(L)!0.5!(S)+(0,-0.9)$) {one size,\\event assumed};
\end{tikzpicture}
\end{center}
```

| Model | What it adds | What the dealer does | Main result |
|---|---|---|---|
| Bagehot (1971) | Some traders know more | Recovers losses from the uninformed | The spread exists because of information |
| Copeland and Galai (1983) | A profit function | Balances expected gains and losses | The spread is the price of a free option |
| Glosten and Milgrom (1985) | Learning from each trade | Quotes the expected value given the trade | A spread exists with zero cost and zero profit |
| Kyle (1985) | A strategic insider who chooses size | Prices the total order flow | $\lambda=\sigma_0/2\sigma_y$ |
| Easley and O'Hara (1987) | Trade size and event uncertainty | Quotes a price for each size | Size and sequence of trades move prices |

**Words to know.** Fundamental value is what the asset is truly worth ($V$, $v$ or $P$). The dealer **buys at the bid** and **sells at the ask**. An informed trader knows something that the price does not show yet. An uninformed trader (also called a liquidity or noise trader) trades for cash or portfolio needs. Adverse selection means that the dealer loses because the better informed trader picks the profitable side. Risk neutral means caring only about expected profit. The prior is the belief before a trade, and the posterior is the belief after it.

## 1.2 Role of information (slide 2)

::: {.hook title="Mnemonic: CFSR, 'Can't Find Safe Returns'"}
- **C**ost is not enough: the price did not always depend on transaction cost.
- **F**low matters: new information also moves prices.
- **S**uperior traders exist: participants do not have equal information.
- **R**isk is new: adverse selection is a risk to the market maker's wealth.
:::

| Point | Inventory models | Information models |
|---|---|---|
| Dealer's problem | The dealer holds an unwanted position | The trader may know more |
| Reason for the spread | Holding cost, order cost and ruin risk | Adverse selection |
| What a trade changes | The inventory | The belief about value |
| Price effect | Mostly temporary | Permanent, as far as the trade has information |

## 1.3 Bagehot (1971): "The only game in town" (slide 4)

```{=latex}
\begin{center}
\begin{tikzpicture}[node distance=2.6cm]
\node[n,fill=red!10] (I) {Informed traders};
\node[n,fill=yellow!20,right=of I] (D) {\textbf{DEALER}\\supplies liquidity\\to everyone};
\node[n,fill=green!10,right=of D] (U) {Uninformed traders};
\draw[e,red!70!black] (D) -- node[p,above]{dealer loses} (I);
\draw[e,green!50!black] (U) -- node[p,above]{dealer gains} (D);
\node[below=0.3cm of D,font=\small,align=center] {Wider spread: smaller loss to informed, bigger gain from uninformed.\\The spread is the \textbf{balance}.};
\end{tikzpicture}
\end{center}
```

::: {.hook title="Mnemonic: 2-2-1"}
- **Two gains.** The market gain comes when the whole market rises, and everyone can earn it. The trading gain comes from trading better than others, and not everyone can earn it.
- **Two traders.** The dealer loses to informed traders and must recover that loss from uninformed traders.
- **One balance.** The spread balances the two. The average investor loses over time, because of the cost of information.

Bagehot has no equations. In the exam, write the two gains, the two traders and the spread as the balance.
:::

## 1.4 Copeland and Galai (1983): the dealer writes two free options (slides 5 to 11)

**Master picture: the price line.** The informed trader knows the true price $P$. The uninformed trader knows only $P_0$.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm]
\draw[thick,-{Stealth}] (0,0) -- (15,0) node[right]{$P$};
\foreach \x/\lb in {1/0,5/P_B,7.5/P_0,10/P_A} {\draw[thick] (\x,0.15)--(\x,-0.15) node[below]{$\lb$};}
\fill[red!15] (1,0.25) rectangle (5,1.3);
\fill[red!15] (10,0.25) rectangle (14.5,1.3);
\node[font=\small,align=center] at (3,0.78) {informed \textbf{sells}\\(uses the free \textbf{put})\\dealer loses $P_B-P$};
\node[font=\small,align=center] at (12.25,0.78) {informed \textbf{buys}\\(uses the free \textbf{call})\\dealer loses $P-P_A$};
\node[font=\small,align=center] at (7.5,0.78) {informed\\does not trade};
\draw[decorate,decoration={brace,amplitude=4pt,mirror}] (5,-0.7)--(7.5,-0.7) node[midway,below=4pt,font=\small]{uninformed sale: gain $P_0-P_B$};
\draw[decorate,decoration={brace,amplitude=4pt,mirror}] (7.5,-1.5)--(10,-1.5) node[midway,below=4pt,font=\small]{uninformed buy: gain $P_A-P_0$};
\end{tikzpicture}
\end{center}
```

::: {.hook title="Mnemonics: 'Ask is a Call, Bid is a Put' and 'Gain from U, Lose to I'"}
The ask $P_A$ is a free call with strike $P_A$. The informed trader uses it when the true value is above $P_A$. The bid $P_B$ is a free put with strike $P_B$. The informed trader uses it when the true value is below $P_B$.

Every formula is read off the price line: the red areas give $L_I$, and the two braces give $G_U$.
:::

**Model.** One period. A single risk-neutral dealer sets the bid and ask to maximize expected profit. Some fraction of traders has superior information.

**Assumptions: "1 dealer, 2 kinds of knowledge, arrivals, 1 size, instant."** A1: a single risk-neutral dealer. A2: informed traders know the actual price $P$. A3: uninformed traders know only the general price $P_0$. A4: traders arrive with given probabilities, as in inventory models. A5: all trades have the same fixed size. A6: quotes are instantaneous.

**Notation.** $\pi_I$ is the probability that the trader is informed. $\pi_{BL}$, $\pi_{SL}$ and $\pi_{NL}$ are the probabilities that an uninformed trader buys, sells or does not trade. $f(P)$ is the density of the true price.

::: {.box title="Copeland and Galai: five steps read off the price line"}
1. Loss to an informed trader (3.1): $L_I=\int_{P_A}^{\infty}(P-P_A)f(P)\,dP+\int_{0}^{P_B}(P_B-P)f(P)\,dP$. These are the two red areas.
2. Gain from an uninformed trader (3.2): $G_U=\pi_{BL}(P_A-P_0)+\pi_{SL}(P_0-P_B)+\pi_{NL}(0)$. These are the two braces. The slide writes $P$ for $P_0$.
3. Objective: $\max_{P_A,P_B}\,[(1-\pi_I)G_U-\pi_IL_I]$.
4. Participation: $(1-\pi_I)G_U-\pi_IL_I\ge0$. With competition, expected profit is zero.
5. Trade-off: a wider spread makes $L_I$ smaller and earns more per uninformed trade, but it drives uninformed traders away. The last effect stops the spread from growing without limit.

**Example.** The true price is 110 or 90 with equal chance, so $P_0=100$. $\pi_I=0.2$, $\pi_{BL}=\pi_{SL}=0.5$. Quotes are $100\pm h$.

$G_U=0.5h+0.5h=h$. $L_I=0.5(10-h)+0.5(10-h)=10-h$. Zero profit: $0.8h=0.2(10-h)=2-0.2h$, so $h=2$.

**Ask 102, bid 98, spread 4.** Shortcut for the symmetric case: $h=\pi_I\Delta$, where $\Delta=10$.
:::

::: {.hook title="Findings: 'PV up, ADC down'. Limits: 'one period, instant reveal'"}
- Information asymmetry explains the dealer's spread.
- The spread rises with the **P**rice level and the **V**ariance of return.
- The spread falls with market **A**ctivity, **D**epth and **C**ontinuity.
- Limits: the model has only one period, and new information is revealed instantly through the trade.

In the exam, do not stop at the objective function. Explain the sign of each term and the option view.
:::

\newpage

## 1.5 Glosten and Milgrom (1985): the event tree (slides 12 to 24)

**Why it is needed.** Copeland and Galai have one period, and their dealer does not learn. Here the dealer learns from every trade.

**The idea.** A competitive dealer earns zero expected profit. Informed traders sell on bad news and buy on good news. The dealer cannot tell who is who, so the trade itself (a buy or a sale) is a signal. The dealer updates the belief after each trade.

**Assumptions: "Two values, mu insiders, half-half noise, one at a time, zero profit, zero cost."** A1: $V=V_L$ with probability $\theta$, and $V_H$ with probability $1-\theta$. A2: a share $\mu$ are insiders. A3: insiders buy on good news and sell on bad news. A4: a liquidity trader buys or sells with probability 0.5 each. A5: trading is sequential; one trader arrives at a time and trades one unit or none. A6: the dealer is risk neutral and competitive. A7: transaction cost is zero. The profit of insiders equals the loss of liquidity traders.

**Master picture.** Write $\theta=\Pr(V_L)$ first: "$\theta$ for trouble".

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[n] (r) at (0,0) {Nature};
\node[n,fill=red!10] (L) at (2.8,1.8) {$V_L$ (bad)};
\node[n,fill=green!10] (H) at (2.8,-1.8) {$V_H$ (good)};
\node[n] (LI) at (5.8,2.7) {Informed};
\node[n] (LU) at (5.8,0.9) {Uninformed};
\node[n] (HU) at (5.8,-0.9) {Uninformed};
\node[n] (HI) at (5.8,-2.7) {Informed};
\draw[e] (r) -- node[p,above left]{$\theta$} (L);
\draw[e] (r) -- node[p,below left]{$1-\theta$} (H);
\draw[e] (L) -- node[p,above]{$\mu$} (LI);
\draw[e] (L) -- node[p,below]{$1-\mu$} (LU);
\draw[e] (H) -- node[p,above]{$1-\mu$} (HU);
\draw[e] (H) -- node[p,below]{$\mu$} (HI);
\node[anchor=west,font=\small] (a) at (7.3,2.7) {\textbf{SELL} for sure: $\theta\mu$};
\node[anchor=west,font=\small] (b) at (7.3,0.9) {\textbf{BUY} $\tfrac12\theta(1-\mu)$ \quad \textbf{SELL} $\tfrac12\theta(1-\mu)$};
\node[anchor=west,font=\small] (c) at (7.3,-0.9) {\textbf{BUY} $\tfrac12(1-\theta)(1-\mu)$ \quad \textbf{SELL} $\tfrac12(1-\theta)(1-\mu)$};
\node[anchor=west,font=\small] (d) at (7.3,-2.7) {\textbf{BUY} for sure: $(1-\theta)\mu$};
\draw[e] (LI)--(a); \draw[e] (LU)--(b); \draw[e] (HU)--(c); \draw[e] (HI)--(d);
\end{tikzpicture}
\end{center}
```

Multiply along each branch to get each joint probability. An informed sale on good news is impossible, so a sale can come from three branches only.

**Read off the tree.** Add the buy leaves for each value, then double them so the halves go away. This gives the grid.

| | $V_L$ | $V_H$ |
|---|---|---|
| Buy leaves | $\tfrac12\theta(1-\mu)$ | $(1-\theta)\mu+\tfrac12(1-\theta)(1-\mu)=\tfrac12(1-\theta)(1+\mu)$ |
| Sale leaves | $\theta\mu+\tfrac12\theta(1-\mu)=\tfrac12\theta(1+\mu)$ | $\tfrac12(1-\theta)(1-\mu)$ |

::: {.box title="Glosten and Milgrom: the doubled grid gives every formula"}
$$\begin{array}{l|cc|c}
 & V_L\ (\theta) & V_H\ (1-\theta) & \text{Sum}\\ \hline
\text{Buy}\to\text{ask} & \theta(1-\mu) & (1-\theta)(1+\mu) & R_B=1+\mu(1-2\theta)\\
\text{Sale}\to\text{bid} & \theta(1+\mu) & (1-\theta)(1-\mu) & R_S=1-\mu(1-2\theta)
\end{array}$$

**Sign rule: "Buy High, Sell Low gets the plus."** The cells Buy-$V_H$ and Sale-$V_L$ get $1+\mu$, because the informed trade sits there. The other two cells get $1-\mu$.

1. $\Pr(B)=\tfrac12R_B=0.5[1+\mu(1-2\theta)]$ (4.27). $\Pr(S)=\tfrac12R_S=1-\Pr(B)$.
2. Posteriors (Bayes): each cell over its row sum. $\Pr(V_L\mid B)=\dfrac{\theta(1-\mu)}{R_B}$, $\Pr(V_H\mid B)=\dfrac{(1-\theta)(1+\mu)}{R_B}$, $\Pr(V_L\mid S)=\dfrac{\theta(1+\mu)}{R_S}$, $\Pr(V_H\mid S)=\dfrac{(1-\theta)(1-\mu)}{R_S}$.
3. Ask (4.29): $a=\dfrac{\theta(1-\mu)V_L+(1-\theta)(1+\mu)V_H}{R_B}$. Bid (4.30): $b=\dfrac{\theta(1+\mu)V_L+(1-\theta)(1-\mu)V_H}{R_S}$.
4. Distance form: $a=V_L+(V_H-V_L)\Pr(V_H\mid B)$ and $b=V_L+(V_H-V_L)\Pr(V_H\mid S)$.
5. Spread (4.31), **"4 coins, mu, range, over the two sums"**: $s=\dfrac{4\theta(1-\theta)\mu(V_H-V_L)}{R_BR_S}=\dfrac{4\theta(1-\theta)\mu(V_H-V_L)}{1-(1-2\theta)^2\mu^2}$.
6. Special case $\theta=0.5$: both sums are 1, so $s=\mu(V_H-V_L)$.
7. New $\theta$ after a buy $=\Pr(V_L\mid B)$. Draw the next grid with it.
8. Check (martingale): $\Pr(B)\,a+\Pr(S)\,b=$ the prior mean.
:::

**Spread proof map (Step 8 of the notes).** Let $k=1-2\theta$. Subtract the two distance forms, so the $V_L$ terms cancel. The numerator is $(1+\mu)(1-\mu k)-(1-\mu)(1+\mu k)=2\mu-2\mu k=2\mu(1-k)=2\mu(2\theta)=4\theta\mu$. The denominator is $(1+\mu k)(1-\mu k)=1-\mu^2k^2$. Multiply by $(V_H-V_L)(1-\theta)$.

**Bayes rule (slides 21 to 23), "Posterior = Prior times Likelihood over Marginal".** (3.10) $\Pr(D)=\Pr(D\mid E)\Pr(E)+\Pr(D\mid E^c)\Pr(E^c)$. (3.11) $\Pr(D,E)=\Pr(E\mid D)\Pr(D)=\Pr(D\mid E)\Pr(E)$. (3.12) $\Pr(E\mid D)=\Pr(D\mid E)\Pr(E)/\Pr(D)$. (3.13) Put 3.10 into the denominator. (3.14) Read it in words. Here $\Pr(E)$ is the prior, $\Pr(D\mid E)$ the likelihood, $\Pr(D)$ the marginal likelihood and $\Pr(E\mid D)$ the posterior.

**Regret-free quotes (slide 15).** A quote is regret free if it is still fair after the trade. Ask $=E[V\mid B]$ (4.23). Bid $=E[V\mid S]$ (4.24).

**General form (slide 16).** If uninformed traders buy with probability $\gamma^B$ and sell with $\gamma^S$, then $\Pr(B)=(1-\mu)\gamma^B+(1-\theta)\mu$ and $\Pr(S)=(1-\mu)\gamma^S+\theta\mu$.

::: {.box title="Glosten and Milgrom example to recite"}
$V_H=110$, $V_L=90$, $\theta=0.3$, $\mu=0.4$. Prior mean $0.3(90)+0.7(110)=104$. $\mu(1-2\theta)=0.16$.

Buy row $0.18,\ 0.98$, sum 1.16. Sale row $0.42,\ 0.42$, sum 0.84. $\Pr(B)=0.58$, $\Pr(S)=0.42$.

Ask $=(16.2+107.8)/1.16=124/1.16=$ **106.897**. Bid $=(37.8+46.2)/0.84=84/0.84=$ **100**. Spread **6.897**.

Spread formula check: $4(0.21)(0.4)(20)/(1.16\times0.84)=6.72/0.9744=6.897$. Martingale check: $0.58(106.897)+0.42(100)=104$.

After a buy: new $\theta=0.18/1.16=0.1552$. New ask 108.541, new bid 104. Both quotes move up after a buy.
:::

::: {.hook title="Findings: SBQ-DME, 'Simple, Beliefs, Quotes, Difference, Martingale, Efficient'"}
- **S**imple description: the model explains the adverse selection cost, and the dealer puts it in the spread to avoid losses.
- **B**eliefs change: information affects the beliefs of the dealer.
- **Q**uotes change: the dealer updates quotes by learning from the arrival of trades.
- **D**ifference from Copeland and Galai: their spread is a function of expected gains and losses. This spread comes from beliefs given each trade.
- **M**artingale: the price is a martingale with respect to the dealer's information. The best forecast of the next price is the present price.
- **E**fficient: the market is semi-strong efficient. Public information cannot predict the future price better.

Conclusion: $s>0$ with zero cost and zero profit, so this spread is pure adverse selection. The spread rises with $\mu$.
:::

**Slide errors.** The slides switch the meaning of $\theta$: slides 14, 16 and 17 use it for good news, and slides 18, 20 and equation 4.27 use it for bad news. Always write $\theta=\Pr(V_L)$ in your first line. Equation 4.28 prints $\Pr(V_L\mid B)$ as $(1-\theta)(1-\mu)/[1-\mu(1-2\theta)]$, which is wrong in this notation.

**Exam order.** Draw the tree. Then write $\Pr(B)$, the posterior, the ask, the bid and the spread. Finish with one line of meaning.

\newpage

## 1.6 Kyle (1985): the timeline (slides 25 to 32)

**Why it is needed.** The Glosten and Milgrom insider trades one unit and ignores price impact. Kyle's insider chooses the size strategically.

**Players: "One insider, noise, competitive dealers, one batch."** One risk-neutral informed trader knows how the order moves the price. Noise traders trade a random amount. Market makers are competitive and risk neutral. A batch auction clears all orders at one price, so the bid-ask spread is not relevant. There is one period and one risky security.

**Master picture.**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.95cm]
\draw[very thick,-{Stealth}] (0,0) -- (16,0) node[right]{time};
\foreach \x/\lb in {1.5/1,5.5/2,9.5/3,13.5/4} {\fill (\x,0) circle (3pt); \node[above=4pt,font=\small\bfseries] at (\x,0) {\lb};}
\node[n,fill=red!10,below=0.4cm] at (1.5,0) {Insider sees\\$v\sim N(p_0,\sigma_0^2)$\\sends\\$x=\beta(v-p_0)$};
\node[n,fill=gray!10,below=0.4cm] at (5.5,0) {Noise traders\\send\\$y\sim N(0,\sigma_y^2)$};
\node[n,fill=yellow!20,below=0.4cm] at (9.5,0) {Dealer sees only\\$z=x+y$\\sets\\$p=p_0+\lambda z$};
\node[n,fill=green!10,below=0.4cm] at (13.5,0) {$v$ is revealed\\insider profit\\$\pi_I=x(v-p)$};
\end{tikzpicture}
\end{center}
```

**Assumptions A1 to A6.** A1: $v\sim N(p_0,\sigma_0^2)$, known only to the insider. A2: $y\sim N(0,\sigma_y^2)$, independent of $v$. A3: the insider knows $v$ but not $y$ and submits $x(v)$. A4: the dealer sees only $z=x+y$ and sets $p(z)$. A5: competition gives zero expected profit, so $p=E[v\mid z]$. A6: the price rule is linear, $p(z)=\lambda z+\mu$ (4.4). Here $\mu$ is an intercept, not the insider share. $\lambda$ is inverse liquidity: a lower $\lambda$ means lower price impact.

**Proof map: "Insider, Dealer, Meet, Hide".**

| Move | Steps | What happens |
|---|---|---|
| Insider | 1 to 4 | $\pi_I=x(v-p)$ (4.3). $E[\pi_I]=x(v-\lambda x-\mu)$ (4.5). Derivative: $v-2\lambda x-\mu=0$, second derivative $-2\lambda<0$. So $x=(v-\mu)/2\lambda$ (4.6), which is $x=a+\beta v$ with $a=-\mu/2\lambda$ and $\beta=1/2\lambda$ (4.7) |
| Dealer | 5 to 7 | $z=a+\beta v+y$. Mean $a+\beta p_0$, variance $\beta^2\sigma_0^2+\sigma_y^2$, covariance with $v$ is $\beta\sigma_0^2$. Normal rule: $E[v\mid z]=p_0+\frac{\beta\sigma_0^2}{\sigma_y^2+\beta^2\sigma_0^2}(z-a-\beta p_0)$ (4.8). Slope: $\lambda=\frac{\beta\sigma_0^2}{\sigma_y^2+\beta^2\sigma_0^2}$ |
| Meet | 6 to 8 | Put $\beta=1/2\lambda$: $\lambda\sigma_y^2+\frac{\sigma_0^2}{4\lambda}=\frac{\sigma_0^2}{2\lambda}$, so $\lambda^2\sigma_y^2=\sigma_0^2/4$, so $\lambda^\ast=\sigma_0/2\sigma_y$ (4.11). Intercept: $\mu=p_0+\mu/2-p_0/2$, so $\mu^\ast=p_0$ (4.10). Then $\beta^\ast=\sigma_y/\sigma_0$ and $a^\ast=-p_0\sigma_y/\sigma_0$ |
| Hide | 9 to 11 | $\beta^2\sigma_0^2=\sigma_y^2$: the insider is exactly as loud as the noise. So $\mathrm{Var}(z)=2\sigma_y^2$ and $\mathrm{Var}(v\mid z)=\sigma_0^2-\beta^2\sigma_0^4/2\sigma_y^2=\sigma_0^2/2$. Profit $E[\pi_I]=\sigma_0^2/4\lambda=\sigma_y\sigma_0/2$ (4.13). Noise loss $E[y(p-v)]=\lambda\sigma_y^2=\sigma_y\sigma_0/2$ (4.14) |

::: {.box title="Kyle: units decide, three halves finish"}
**Units.** $\sigma_0$ is in price. $\sigma_y$ is in shares. $\lambda$ is price per share, so it is $\sigma_0/\sigma_y$. $\beta$ is shares per price, so it is $\sigma_y/\sigma_0$. Profit is price times shares, so it is $\sigma_0\sigma_y$.

**Three halves.**

1. $\lambda\beta=\tfrac12$, so the 2 sits under $\lambda$: $\lambda=\dfrac{\sigma_0}{2\sigma_y}$, $\beta=\dfrac{\sigma_y}{\sigma_0}$, $x=\dfrac{\sigma_y}{\sigma_0}(v-p_0)$.
2. Expected insider profit $=\tfrac12\sigma_0\sigma_y$.
3. Variance left after trading $=\tfrac12\sigma_0^2$. Half of the private information enters the price in one period.

**Who pays.** Noise traders lose $\lambda\sigma_y^2=\tfrac12\sigma_0\sigma_y$, which is the insider's profit. The dealer's expected net profit is zero.

**Example.** $p_0=100$, $\sigma_0=10$, $\sigma_y=1000$, $v=110$, $y=-400$.

$\lambda=10/2000=0.005$. $\beta=1000/10=100$. Check $\lambda\beta=0.5$. $x=100(10)=1000$. $z=1000-400=600$. $p=100+0.005(600)=103$.

Realized profit $1000(110-103)=7000$. Expected profit $0.5(1000)(10)=5000$. Variance left $100/2=50$.
:::

::: {.hook title="Four questions Kyle answers (slide 26): 'How fast, how valuable, how noisy, how liquid'"}
- How **fast** does private information enter the price? Half of it in one period.
- How **valuable** is private information to the insider? $E[\pi_I]=\sigma_y\sigma_0/2$.
- How does **noise** trading affect price volatility? More noise lowers the price impact $\lambda$.
- What decides the **liquidity** of a market? $\lambda=\sigma_0/2\sigma_y$: private information against noise.
:::

**What changes what: "Profit likes both. Lambda likes only information."**

| Rise in | $\lambda$ | Insider profit | Meaning |
|---|---|---|---|
| $\sigma_0$ | Up | Up | More private information makes the market less liquid |
| $\sigma_y$ | Down | Up | More noise hides the insider and makes the market deeper |

::: {.hook title="Findings (slide 32): 'Hide, Pay, Split'"}
- **Hide.** Order flow from liquidity traders hides the insider's information. A large random buy makes the dealer raise the price.
- **Pay.** Liquidity traders fund the insider's profit. The dealer's net loss is zero.
- **Split.** With many periods, the insider splits the order into small pieces, and the size of the pieces changes over time.
:::

**Slide errors.** Equation 4.9 has no minus sign on $a^\ast$; the minus is needed, because $a=-\mu/2\lambda$. Slide 28 says the dealer optimizes profit; in Kyle, competition forces zero expected profit. Slide 32 says noise distorts the information "available to informed traders"; the insider already knows $v$, so the noise hides it from the dealer.

\newpage

## 1.7 Easley and O'Hara (1987): the event tree with sizes (slides 33 to 47)

**Why it is needed.** Earlier sequential models used one fixed size and assumed that information exists.

::: {.hook title="What is new (slides 33 and 34): 'Extend, Same, Sizes, Dual, Study, Message'"}
- **Extend:** it extends the sequential model of Glosten and Milgrom.
- **Same** dealers: competitive and risk neutral, and their quotes change with trades.
- **Sizes:** traders can trade different quantities.
- **Dual** uncertainty: the dealer does not know whether information exists, nor its direction.
- **Study:** price movements, trade size and the spread of information.
- **Message:** the size and the sequence of trades both move prices and pass information.
:::

**Letters: "Alpha Arrives, Delta Decides (low), Mu Many informed."**

**Master picture.** Each node shows what happens next. The leaves show who sends a large sale. $V^\ast=\delta\underline V+(1-\delta)\bar V$ is the value with no news.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[n] (r) at (0,0) {Before\\trading};
\node[n,fill=orange!15] (E) at (3,1.6) {Event};
\node[n,fill=gray!10] (O) at (3,-2.4) {No event\\value $V^\ast$};
\node[n,fill=red!10] (Lo) at (6.2,2.6) {Low signal\\value $\underline V$};
\node[n,fill=green!10] (Hi) at (6.2,0.4) {High signal\\value $\bar V$};
\draw[e] (r) -- node[p,above left]{$\alpha$} (E);
\draw[e] (r) -- node[p,below left]{$1-\alpha$} (O);
\draw[e] (E) -- node[p,above left]{$\delta$} (Lo);
\draw[e] (E) -- node[p,below left]{$1-\delta$} (Hi);
\node[anchor=west,font=\small,align=left] (a) at (8.4,2.6) {informed $\mu$: \textbf{SELL LARGE}\\uninformed $1-\mu$: large sale with $X_S^2$};
\node[anchor=west,font=\small,align=left] (b) at (8.4,0.4) {informed $\mu$: \textbf{BUY LARGE}\\uninformed $1-\mu$: large sale with $X_S^2$};
\node[anchor=west,font=\small,align=left] (c) at (8.4,-2.4) {all uninformed:\\large sale with $X_S^2$};
\draw[e] (Lo)--(a); \draw[e] (Hi)--(b); \draw[e] (O)--(c);
\end{tikzpicture}
\end{center}
```

**Read off the tree: the three ways a large sale happens.**

| State | Who sells large | Joint probability |
|---|---|---|
| Event, low | All informed, plus uninformed who want $S^2$ | $\alpha\delta[\mu+(1-\mu)X_S^2]$ |
| Event, high | Only uninformed who want $S^2$ | $\alpha(1-\delta)(1-\mu)X_S^2$ |
| No event | Only uninformed who want $S^2$ | $(1-\alpha)X_S^2$ |
| **Sum** | | $\Pr(S^2)=X_S^2(1-\alpha\mu)+\alpha\delta\mu$ |

Sum step: the $X_S^2$ terms give $\alpha\delta(1-\mu)+\alpha(1-\delta)(1-\mu)+(1-\alpha)=\alpha(1-\mu)+1-\alpha=1-\alpha\mu$.

::: {.box title="Easley and O'Hara: two weights, U and I, give everything"}
**I (informed) = the tree in time order:** event, then signal, then informed. Sellers $I_S=\alpha\delta\mu$. Buyers $I_B=\alpha(1-\delta)\mu$.

**U (uninformed) = "wants large, times is uninformed":** $U_S=X_S^2(1-\alpha\mu)$ and $U_B=X_B^2(1-\alpha\mu)$. Here $1-\alpha\mu$ is the chance that a random trader is uninformed.

1. Large bid: uninformed sales are worth $V^\ast$, and informed sales are worth $\underline V$. So $b_2=\dfrac{U_SV^\ast+I_S\underline V}{U_S+I_S}=V^\ast-\dfrac{I_S}{U_S+I_S}(V^\ast-\underline V)$. **Pulled down by the informed share.**
2. Large ask: $a_2=V^\ast+\dfrac{I_B}{U_B+I_B}(\bar V-V^\ast)$. **Pulled up.**
3. Slide form (variance): $V^\ast-\underline V=(1-\delta)(\bar V-\underline V)$ and $\sigma_v^2=\delta(1-\delta)(\bar V-\underline V)^2$ ("coin times range squared"). So $b_2^\ast=V^\ast-\dfrac{\sigma_v^2}{\bar V-\underline V}\cdot\dfrac{\alpha\mu}{X_S^2(1-\alpha\mu)+\delta\alpha\mu}$ and $a_2^\ast=V^\ast+\dfrac{\sigma_v^2}{\bar V-\underline V}\cdot\dfrac{\alpha\mu}{X_B^2(1-\alpha\mu)+(1-\delta)\alpha\mu}$.
4. Small quotes (separating): the informed never trade small, so $a_1=b_1=V^\ast$.
5. Separation, **"the size ratio must beat the crowd ratio"**: the informed buyer needs $B^2(\bar V-a_2)\ge B^1(\bar V-V^\ast)$, so $\dfrac{B^2}{B^1}\ge\dfrac{U_B+I_B}{U_B}=1+\dfrac{\alpha\mu(1-\delta)}{X_B^2(1-\alpha\mu)}$. If it holds, the equilibrium separates. If not, the informed also trade small, and the equilibrium pools.
6. Pooling: a share $\phi_i$ of informed sellers picks size $i$. $b_i=V^\ast-\dfrac{\sigma_v^2}{\bar V-\underline V}\cdot\dfrac{\alpha\mu\phi_i}{X_S^i(1-\alpha\mu)+\delta\alpha\mu\phi_i}$. Both bids are below $V^\ast$, and the informed earn the same profit at both sizes.
7. Spread for size $i$ (slide 44, corrected): $A_i=E[V\mid B^i]+C$, $B_i=E[V\mid S^i]-C$, $S_i=E[V\mid B^i]-E[V\mid S^i]+2C$. The model sets $C=0$.

The large-trade discount rises with $\alpha$, $\mu$ and the variance of value.
:::

**Two equilibria: "Few informed: Fork. Many informed: Mix."**

| Point | Separating (Fork) | Pooling (Mix) |
|---|---|---|
| Size chosen by the informed | Mainly large | Both small and large |
| Number of informed | Relatively few | Many |
| Can the dealer separate types? | Yes, partly by size | No |
| Where is the spread? | Only on large trades | On both sizes |
| Effect on price | Large trades get worse prices | Prices are averaged and may hide the true price |

In pooling, both types choose the same action at the same price with positive probability.

**Assumptions A1 to A9: "Signal, Delta, Values, Alpha, Mu, Many informed, Dealer blind, No cost, Outside demand".** A1: $V$ is random; an information event is a signal $s$, low or high. A2: low with probability $\delta$, $0<\delta<1$. A3: $\underline V=E[V\mid s=L]$, $\bar V=E[V\mid s=H]$, $\bar V>\underline V$. A4: an event happens before the trading day with probability $\alpha$, $0<\alpha\le1$, only between trading days. A5: after an event the expected share of informed trades is $\mu$. A6: informed traders are risk neutral and many, so they compete. A7: the dealer and the uninformed know neither the event nor the signal. A8: no transaction cost and no risk aversion, because the period is short. A9: uninformed demand is given from outside (timing of income and consumption, portfolio needs).

**Market structure.** Two sizes on each side: buyers want $B^1<B^2$, sellers offer $S^1<S^2$. $X_B^i$ and $X_S^i$ are the shares of uninformed who want each size. Trading is sequential in six steps. A trader arrives. The trader asks competing dealers for prices at each quantity. The trader may choose not to trade. An uninformed trader takes the best quote for the desired quantity. An informed trader takes the quote with the highest profit. An indifferent trader picks a dealer at random. Dealers set a price for each of the four quantities at the start of the day, each with zero expected profit.

**Price path after a block sale (slides 45 and 46): "Known event: stuck. Unsure event: bounce part way."**

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
\node[below,font=\small] at (1,0) {$t$}; \node[below,font=\small] at (2.5,0) {$t+1$}; \node[below,font=\small] at (4.2,0) {$t+2$};
\node[font=\small\bfseries] at (2.7,3.6) {Fig.\ 1: event known};
\end{scope}
\begin{scope}[xshift=8.5cm]
\draw[-{Stealth}] (0,0)--(5.5,0) node[right,font=\small]{time};
\draw[-{Stealth}] (0,0)--(0,3.2) node[above,font=\small]{price};
\draw[dashed] (0,2.6)--(5,2.6) node[right,font=\small]{$V^\ast$};
\draw[dashed] (0,0.8)--(5,0.8) node[right,font=\small]{$b_2$};
\draw[very thick,red] (1,2.6)--(2.5,0.8)--(4.2,1.6);
\foreach \x/\y in {1/2.6,2.5/0.8,4.2/1.6} \fill[red] (\x,\y) circle (2.5pt);
\node[right,font=\scriptsize,align=left] at (4.25,1.6) {partial\\recovery};
\node[below,font=\small] at (1,0) {$t$}; \node[below,font=\small] at (2.5,0) {$t+1$}; \node[below,font=\small] at (4.2,0) {$t+2$};
\node[font=\small\bfseries] at (2.7,3.6) {Fig.\ 2: event uncertain};
\end{scope}
\end{tikzpicture}
\end{center}
```

At $t$ a small trade happens at $V^\ast$. At $t+1$ a block sale pushes the price to $b_2$. At $t+2$ a small trade arrives. In Figure 1 it says nothing new, so the price stays low. In Figure 2 a small trade comes only from an uninformed trader, so it makes "no event" more likely, and the price recovers part way but stays below $V^\ast$.

::: {.box title="Easley and O'Hara example to recite"}
$\bar V=110$, $\underline V=90$, $\delta=\alpha=0.5$, $\mu=0.4$, $X_S^2=X_B^2=0.25$.

$V^\ast=100$. $\sigma_v^2=0.25(400)=100$. $\alpha\mu=0.2$. $U=0.25(0.8)=0.2$. $I=0.5(0.5)(0.4)=0.1$. Denominator 0.3. Informed share $1/3$.

Adjustment $(100/20)(0.2/0.3)=3.333$. Large bid **96.667**, large ask **103.333**, small quotes **100**. Separation needs $B^2/B^1\ge0.3/0.2=$ **1.5**.

Small trade after the block: take the large-sale weights $0.1375$ (low), $0.0375$ (high) and $0.125$ (none), total 0.3. Multiply by the chance of an uninformed trader: 0.6, 0.6 and 1. New weights $0.0825$, $0.0225$ and $0.125$, total 0.23.

Price $=[0.0825(90)+0.0225(110)+0.125(100)]/0.23=22.4/0.23=$ **97.391**. It lies between 96.667 and 100: partial recovery.
:::

::: {.hook title="Findings (slide 47): BQIO, 'Blocks Quietly Inform Others'"}
- **B**lock trades: their price effects come from informed trading.
- **Q**uantity matters: trade size is correlated with private information.
- **I**nformed preference: at any given price, informed traders prefer larger amounts.
- **O**ptimal pricing depends on quantity: large-trade prices show a higher probability of informed trading.
:::

**Slide error (slide 44).** The slide prints $B=E[V\mid H]-C$ and $A=E[V\mid L]+C$ with $H$ for informed and $L$ for uninformed. The dealer cannot see the type, so quotes depend only on side and size. Use the corrected forms in item 7 of the box.

## 1.8 Compare the five theories

| Point | Bagehot | Copeland--Galai | Glosten--Milgrom | Kyle | Easley--O'Hara |
|---|---|---|---|---|---|
| Time | No formal model | One period | Sequential | One batch, later many | Sequential |
| Dealer | Loses and recovers | Maximizes profit | Zero profit | Zero profit | Zero profit |
| Informed trader | Not modelled | Takes a free option | Trades one unit | Chooses size strategically | Chooses one of two sizes |
| Dealer learns? | No | No | From direction | From net order flow | From direction, size and sequence |
| Liquidity measure | Spread | Spread | Spread | $1/\lambda$ | Spread at each size |
| Event certain? | Not modelled | Yes | Yes | Yes | No |

::: {.hook title="Recognize the model from one word"}
"Option" means Copeland and Galai. "Regret free", "Bayes" and "sequential" mean Glosten and Milgrom. "Batch", "strategic" and "order flow" mean Kyle. "Size", "block" and "event uncertainty" mean Easley and O'Hara.
:::

\newpage

# Topic 2: Liquidity measures

## 2.1 The five papers

::: {.hook title="Mnemonic: 'Can Any Lender Ignore Stoll?' (Chordia, Amihud, Lesmond, Ince, Stoll)"}
- **C**hordia (2000): does liquidity move together? Spreads and depth. Yes, there is commonality.
- **A**mihud (2002): does illiquidity affect returns? Absolute return per dollar traded. Less liquid stocks must pay higher returns.
- **L**esmond (2005): which measure works in emerging markets? LOT, Roll, Amihud and others. LOT and Roll work best across countries.
- **I**nce (2022): which part of illiquidity is priced? Three parts. The idiosyncratic part predicts returns.
- **S**toll (2000): what causes friction? Seven friction measures. Friction has real and informational parts.
:::

**Words.** Liquidity is the ability to trade a large size, quickly, at low cost, when you want to. Immediacy is trading now. Mid price $P_M=(P_A+P_B)/2$. Price impact is how much a trade moves the price. Commonality means the liquidity of many stocks moves together. A t value above about 2 in absolute value is significant.

**Background (slides 2 and 3): "1986 spread, 2000 together, 2001 level, 2001 systematic".** Amihud and Mendelson (1986) introduced the spread as a proxy for illiquidity. Chordia and others (2000) documented commonality. Chordia and others (2001) studied the cross-sectional relation with the level of illiquidity. Huberman and Halka (2001) found a systematic part of liquidity that changes over time.

## 2.2 Chordia, Roll and Subrahmanyam (2000): "Commonality in liquidity"

**The gap (slide 4).** Earlier studies looked at one stock at a time and gave little attention to common causes. Changes in liquidity are correlated across stocks. Inventory risk and asymmetric information both change liquidity over time. Trading cost and other microstructure effects have common determinants.

::: {.hook title="Seven reasons for commonality (slide 5): 'PVIVP, then F and I'"}
The first five are inventory reasons. "PVIVP" reads the same from both ends.

- **P**rice swings: market-wide trading responds to market-wide price swings.
- **V**olume: volume drives dealer inventory, so desired inventories move together.
- **I**nterest rates: the cost of carrying inventory depends on them.
- **V**olatility: inventory risk depends on volatility, which has a market component.
- **P**rogram trading: it puts common pressure on many inventories at once.
- **F**unds: institutional funds with similar styles trade alike (correlated trading).
- **I**nformation: a small group of large traders may know more about many stocks (asymmetric information).
:::

**Implications (slide 6): "Move, Cost, Crises, Factor, Prices".** Liquidity moves together. Trading costs move together. Liquidity crises can be episodic and global. Trading cost has a common factor (Amihud and Mendelson 1986, Brennan and Subrahmanyam 1996). Liquidity affects asset prices through two channels. The **static** channel is the average cost of trading, so a costly stock must pay a higher return. The **dynamic** channel is the risk that liquidity changes, so a stock with risky liquidity must pay more.

**Data (slides 7 and 8): "92, 1169, 254, \$2".** NYSE transaction data from ISSM for 1992, with 254 trading days and 1,169 stocks, each trading on 10 or more days. Excluded: stocks with splits or stock dividends, certificates, ADRs, non-US firms, Americus Trust, closed-end funds and REITs. A stock-day is deleted if the average price is below \$2. The opening batch and special-settlement trades are removed. The NYSE specialist announces spread and depth some seconds before a trade. Each measure is averaged over all trades of a stock on a day.

**Master picture: the five measures on one quote line.**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm]
\draw[thick] (0,0)--(13,0);
\foreach \x/\lb/\val in {2/bid $P_B$/99.80,6.5/mid $P_M$/100.00,8.75/trade $P_t$/100.10,11/ask $P_A$/100.20} {\draw[thick] (\x,0.15)--(\x,-0.15); \node[above=3pt,font=\small] at (\x,0.1) {\lb}; \node[below=3pt,font=\small] at (\x,-0.1) {\val};}
\draw[decorate,decoration={brace,amplitude=5pt}] (2,0.9)--(11,0.9) node[midway,above=5pt,font=\small]{QSPR $=P_A-P_B=0.40$;\quad PQSPR $=0.40/P_M=0.004$};
\draw[decorate,decoration={brace,amplitude=4pt,mirror}] (6.5,-0.75)--(8.75,-0.75) node[midway,below=5pt,font=\small,align=center]{$\lvert P_t-P_M\rvert=0.10$\\ESPR $=2(0.10)=0.20$\\PESPR $=0.20/100.10=0.002$};
\node[n,fill=blue!8] at (2,-1.6) {$Q_B=600$};
\node[n,fill=blue!8] at (11,-1.6) {$Q_A=400$};
\node[font=\small] at (11,-2.3) {DEP $=(600+400)/2=500$};
\end{tikzpicture}
\end{center}
```

::: {.box title="Chordia: five measures. 'Quoted uses the Mid. Effective has a 2. Depth is the only one where higher is better.'"}
QSPR $=P_A-P_B$ (dollars). PQSPR $=(P_A-P_B)/P_M$ (pure number). DEP $=(Q_A+Q_B)/2$ (shares). ESPR $=2\lvert P_t-P_M\rvert$ (dollars). PESPR $=2\lvert P_t-P_M\rvert/P_t$ (pure number).

PQSPR divides by the mid price. PESPR divides by the trade price. The effective spread is smaller than the quoted spread when the trade is inside the quotes.

Daily change: $DL_t=(L_t-L_{t-1})/L_{t-1}$.
:::

**Cross-sectional statistics (slide 10).** Mean QSPR 0.3162 (median 0.2691). Mean PQSPR 0.0160. Mean DEP 3776 shares. Mean ESPR 0.2245. Mean PESPR 0.0111. Four facts, **"Inside, Skew, Agree, Opposite"**. Effective is below quoted, because many trades happen inside the quotes. The mean is above the median, because a few illiquid stocks pull it up. All spread measures correlate positively (QSPR with PQSPR 0.844, ESPR with PESPR 0.871). Depth correlates negatively with spreads (QSPR with DEP $-0.396$), because a wide spread comes with low depth.

**Daily changes (slide 11).** Mean absolute daily change: DQSPR 0.2396, DPQSPR 0.2408, DDEP 0.7828, DESPR 0.3148, DPESPR 0.3196. Liquidity changes a lot from day to day, and **depth changes the most**.

::: {.box title="Three tests: 'Market, then Market plus Industry, then Who trades'"}
**Test 1 (slides 12 and 13):** $DL_{j,t}=\alpha_j+\beta_jDL_{M,t}+\varepsilon_{j,t}$, plus a lag and a lead of the market change. $\beta_j>0$ is commonality. "Significant" means positive with t above 1.645.

Same-day coefficients: DQSPR **0.690** (t 28.29), DPQSPR 0.791, DDEP 1.373, DESPR 0.280, DPESPR 0.778. Percent positive: 84.86, 84.26, 81.61, 68.61 and 71.00, so **"69 to 85 percent positive"**. Lag and lead are small (DQSPR lag 0.123, lead 0.053).

Meaning of 0.69: a 1 percent change in the market spread goes with a 0.69 percent change in the stock spread. The same day matters much more than the lag or the lead.

**Test 2 (slide 14):** $DL_{j,t}=\alpha_j+\beta_{j,M}DL_{M,t}+\beta_{j,I}DL_{I,t}+\varepsilon_{j,t}$. Both market and industry matter (DQSPR: market 0.264, industry 0.467). The "sum" adds same day, lag and lead. Mean $R^2$ is only about 0.02, so most changes are specific to the firm.

**Test 3 (slides 15 and 16):** $DL_{j,t}=\alpha_j+\beta_SDS_{j,t}+\beta_TDT_{j,t}+\beta_MDV_{M,t}+\beta_IDV_{I,t}+\varepsilon_{j,t}$.

$S$ = average dollar trade size (block pressure or information). $T$ = number of trades (asymmetric information, Jones and others 1994). $V_M$ = market dollar volume without stock $j$ (balanced, uninformed trading). $V_I$ = industry dollar volume without stock $j$. Stealth trading: informed traders break up orders and are most active in medium sizes (Barclay and Warner 1993). Trading frequency is strongly influenced by market and industry.
:::

**Observations (slide 17).**

| Variable | Effect | Why |
|---|---|---|
| Trading in general | Usual view: more trading reduces spreads | Inventory view |
| Number of trades | Strong positive effect on spreads | Informed traders |
| Market volume | Negative, marginal effect on the quoted spread | Balanced, uninformed trading |
| Trade size | Strong positive effect on quoted spread and depth | Block pressure or information |
| Industry volume | Negative, not significant effect on depth | No clear effect |

::: {.hook title="Conclusion (slide 18): 'Together. Own trades widen. Market trades tighten.'"}
1. Liquidity measures of individual stocks move **together** (commonality).
2. A stock's spread rises with its **own** number of transactions (asymmetric information).
3. A stock's spread falls with **market**-wide trading, which is mostly uninformed and balances inventory (inventory risk).

Exam order: meaning, reasons, data, five measures, regression, sign and conclusion. One number is enough: 0.69.
:::

\newpage

## 2.3 Amihud (2002): "Illiquidity and stock returns"

**Master picture: ratio first, then average, then price it.**

```{=latex}
\begin{center}
\begin{tikzpicture}[node distance=0.6cm]
\node[n,fill=blue!8] (a) {Each day $d$:\\$\lvert R_{iyd}\rvert/VOLD_{iyd}$};
\node[n,fill=blue!8,right=of a] (b) {Average over\\the $D_{iy}$ days};
\node[n,fill=orange!15,right=of b] (c) {$ILLIQ_{iy}$\\high = illiquid};
\node[n,fill=green!10,right=of c] (d) {Year $y-1$ value\\prices returns\\in year $y$};
\draw[e] (a)--(b); \draw[e] (b)--(c); \draw[e] (c)--(d);
\node[n,fill=gray!10,below=0.6cm of c] (v) {Valid? Compare with\\Kyle $\lambda$ and fixed cost $\psi$};
\draw[e] (c)--(v);
\end{tikzpicture}
\end{center}
```

**Idea.** A stock is illiquid if a small traded value moves the price a lot. The measure needs only daily returns and volume, with no quote data. Investors demand a higher expected return for an illiquid stock.

::: {.box title="Amihud: the measure, the check and the method"}
$$ILLIQ_{iy}=\frac{1}{D_{iy}}\sum_{d=1}^{D_{iy}}\frac{\lvert R_{iyd}\rvert}{VOLD_{iyd}}$$

It is the average absolute return per dollar traded, a price impact measure. Higher means less liquid.

**Amivest is upside down:** $\sum VOLD/\sum\lvert R\rvert$ (Cooper and others 1985, Khan and Baker 1993). Higher means more liquid.

Do not divide the average return by the average volume. Take each day's ratio first. Always state the unit.

**Example.** Returns $0.02$, $-0.01$ and $0.03$; volumes 10, 5 and 10 million. Ratios 0.002, 0.002 and 0.003. Sum 0.007. ILLIQ $=0.007/3=$ **0.002333 per million dollars**. Amivest $=25/0.06=$ **416.67**.

**Validity (slide 22), "Kyle plus fixed cost":** $ILLIQ_i=-292+247.9\lambda_i+49.2\psi_i$, with t values 12.25, 13.78 and 17.33, and $R^2=0.30$. Both slopes are positive, so the simple measure agrees with the detailed ones.

**Method (slides 23 and 24), "NYSE 63 to 97, CRSP, Fama-MacBeth, 408 months, Shumway, $y-1$":** $R_{imy}=k_{0my}+\sum_jk_{jmy}X_{ji,y-1}+U_{imy}$. Run one cross-section regression each month, save the coefficients, average them over 408 months (1964 to 1997) and test whether the average is zero. Returns are adjusted for delisting (Shumway 1997) to avoid survivorship bias. Characteristics come from year $y-1$, so they are known at the start of year $y$.
:::

::: {.hook title="Findings: 'Expected = Extra return later. Unexpected = Ugly return now. Small firms feel it most.'"}
- Cross-section: expected stock returns rise with illiquidity, even after beta and size.
- Time series: higher **expected** market illiquidity gives a higher ex-ante market excess return.
- **Unexpected** market illiquidity lowers contemporaneous stock returns.
- Both effects are stronger for **small** firms, which fits a flight to liquidity.
- So the stock excess return (the equity premium) partly pays investors for illiquidity.

The findings slide (25) is blank in our deck; these findings come from the paper.
:::

## 2.4 Ince (2022): liquidity components

::: {.hook title="Mnemonic: 'ASI, only I survives'"}
- Monthly illiquidity of a firm is split into **A**lpha (the constant part for that firm), **S**ystematic (moves with the market) and **I**diosyncratic (specific to the firm).
- The systematic premium disappears when very small stocks are removed.
- High idiosyncratic liquidity gives positive future risk-adjusted returns. Low idiosyncratic liquidity gives negative ones.
- Data (slide 34): common stocks on NYSE, Amex and Nasdaq, January 1964 to December 2018, from CRSP.
:::

**Other articles on commonality (slide 28): "Institutions, Incentive, Sentiment, Funding, Forty".** Kamara and others (2008) and Koch and others (2009): correlated trading by institutions. Morck and others (2000): weak incentive to trade individual securities. Huberman and Halka (2001): investor sentiment. Coughenour and Saad (2004) and Hameed and others (2010): funding limits of intermediaries. Karolyi and others (2012): evidence from 40 markets.

## 2.5 Lesmond (2005): "Liquidity of emerging markets"

**Problem.** Many emerging markets lack long records of bids and asks, but trading there can be very costly. So liquidity is estimated from daily prices and volume. Question: which low-frequency measure works across countries and within a country? Setting: summaries say 31 emerging markets (one citing paper says 23), 1987 to 2000, with five measures compared against quoted spreads where available. Journal of Financial Economics, volume 77, pages 411 to 452.

**Master picture: the no-trade band.**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\fill[gray!15] (-1,-2.2) rectangle (1.5,2.2);
\node[font=\small,align=center] at (0.25,1.6) {no-trade band\\observed $R=0$};
\draw[-{Stealth}] (-4.5,0)--(5,0) node[right,font=\small]{true $R^\ast$};
\draw[-{Stealth}] (0,-2.4)--(0,2.6) node[above,font=\small]{observed $R$};
\draw[very thick,blue] (-3.2,-2.2)--(-1,0) -- (1.5,0) -- (3.7,2.2);
\draw[thick] (-1,0.12)--(-1,-0.12) node[above left=3pt,font=\small]{$\alpha_1<0$};
\draw[thick] (1.5,0.12)--(1.5,-0.12) node[below right,font=\small]{$\alpha_2>0$};
\node[font=\small,align=left,anchor=west] at (3.9,1.2) {$R=R^\ast-\alpha_2$\\good news beats\\the buying cost};
\node[font=\small,align=right,anchor=east] at (-3.0,-0.9) {$R=R^\ast-\alpha_1$\\bad news beats\\the selling cost};
\end{tikzpicture}
\end{center}
```

::: {.box title="LOT (Lesmond, Ogden and Trzcinka 1999) in four steps"}
**Idea.** An investor trades only if the value of information exceeds the cost of trading. Otherwise the price does not move. So many zero-return days mean high cost.

Assumptions: A1 the true return follows the market model; A2 selling needs $R^\ast<\alpha_1<0$; A3 buying needs $R^\ast>\alpha_2>0$; A4 the marginal informed investor trades only beyond these limits; A5 the error is normal.

1. True return: $R^\ast_{jt}=\beta_jR_{mt}+\varepsilon_{jt}$.
2. Observed return in three regions: $R^\ast-\alpha_1$ below the band, 0 inside, $R^\ast-\alpha_2$ above. (Read it off the picture.)
3. Maximum likelihood with three parts (falls, zeros, rises) chooses $\alpha_1$, $\alpha_2$, $\beta$ and the error variance.
4. Selling cost $-\alpha_1$, buying cost $\alpha_2$, round trip $LOT=\alpha_2-\alpha_1$.

**Example.** $\alpha_1=-0.010$, $\alpha_2=0.015$, so LOT $=$ **2.5 percent**. A true 0.025 gives an observed 0.010. A true 0.007 gives 0. A true $-0.018$ gives $-0.008$.

The 1999 paper found round-trip costs of 1.2 percent (largest US firms) and 10.3 percent (smallest), 1963 to 1990.

Simpler cousin: the share of zero-return days. Lesmond (2005) found it highly correlated with hand-collected spreads.
:::

**The measures compared.**

| Measure | Formula | Type | Data needed | Main weakness |
|---|---|---|---|---|
| LOT | $\alpha_2-\alpha_1$ | Price based | Daily returns of stock and market | Needs an estimation model |
| Roll | $2\sqrt{-\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})}$ | Price based | Daily prices | Fails when covariance is positive |
| Amihud | Average of $\lvert R\rvert$ over traded value | Price impact | Returns and volume | Fails with zero volume |
| Turnover | Shares traded over shares outstanding | Volume based | Volume and share count | Volume can rise in a crisis while cost also rises |

::: {.hook title="Findings: 'Across: LOT n Roll. Within: LOT, then Amihud. Politics beats law.'"}
1. Across countries, the price-based measures LOT and Roll work better than volume-based measures.
2. Within a country, LOT works best, and Amihud works to a lesser extent.
3. Countries with weak political and legal institutions have significantly higher liquidity cost, "even to the exclusion of legal origin or insider trading enforcement".
4. More political risk goes with **10 basis points** higher cost by LOT and **1.9 percent** higher price impact by Amihud.
5. Political risk appears stronger than the information risk created by legal institutions.
:::

## 2.6 Stoll (2000): "Friction"

::: {.hook title="Mnemonic: 'Time or Price; Stoll pays the Price'"}
- Friction in **time** is the time needed to trade a given amount optimally (Lippman and McCall 1986).
- Friction in **price** is the price concession paid for immediacy (Demsetz 1968). Stoll uses the price view.
- **Real** friction uses real resources: labour, systems and capital to bear inventory risk.
- **Informational** friction moves wealth from less informed to better informed traders.
:::

**The paper (slide 29).** It studies sources of trading friction with seven robust measures from transaction data, on 1,706 NYSE and AMSE stocks and 2,184 Nasdaq stocks. Insights: the size of cost, real against informational friction, and the effect of market structure.

::: {.box title="Stoll: price of immediacy. 'Volume and Price shrink it. Variance grows it. Size and trades flip by market.'"}
$s=a_0+a_1\log V+a_2\sigma^2+a_3\log MV+a_4\log P+a_5\log N+e$, with $s=(A-B)/2P$ the proportional quoted **half**-spread.

December 1997, NYSE/AMSE then Nasdaq: log volume $-0.0010$ and $-0.0012$ (inventory is easier to unload); variance $1.5467$ and $0.4908$ (inventory risk is higher); log market value $+0.0003$ and $-0.0003$ (sign differs); log price $-0.0024$ and $-0.0020$ (fixed cost spread over a higher price); log trades $+0.0003$ and $-0.0011$ (sign differs). Adjusted $R^2$ 0.7731 and 0.6467. January and February 1998 are similar (0.7763/0.6588 and 0.7914/0.6688).

Quoted half-spread $S=(A-B)/2$ (total friction). Effective half-spread $ES=\lvert P-M\rvert$ (total friction on actual trades). Traded spread: "refer to article".

**Trap:** Stoll uses half-spreads and Chordia uses full spreads, so Chordia's effective spread is twice Stoll's.
:::

## 2.7 Compare the three measures from the syllabus

| Paper | Measure | Data needed | Use |
|---|---|---|---|
| Chordia (2000) | Spreads and depth | Quotes and trades | Commonality in liquidity |
| Amihud (2002) | $\lvert R\rvert$ per dollar volume | Daily return and volume | Illiquidity is priced |
| Lesmond (2005) | LOT, the zero-return band | Daily returns only | Emerging markets without quotes |

\newpage

# Topic 3: Triggers of extreme illiquidity

**Overview.** Theory: Brunnermeier and Pedersen (2009) show that market liquidity and funding liquidity feed each other. Evidence: the margin history of S&P 500 futures, where margins jump in a crisis. Measure: Jain, Mishra and McInish (2013) count bad spread days and bad price days over 10 days. Effect: spirals lower firm valuation.

**Words.** A speculator supplies liquidity by buying cheap and selling dear (dealers, hedge funds). A financier lends to the speculator. Margin is the part of a position that the trader pays with own capital; a haircut means the same for a collateral loan. Deleveraging is selling to reduce borrowing. A spiral is a loop in which a bad event causes more of itself. Flight to quality is capital moving from risky to safe assets.

## 3.1 Why extreme cases matter (slide 2)

::: {.hook title="Three principles: 'Key, Trade, No outsiders'"}
1. Liquidity is **key**: a market cannot work well without it.
2. **Trading** should govern change: changes should come from participants' trading.
3. Outside factors should not rule the liquidity of an asset or market.

In an extreme case, funding can decide liquidity. This breaks principle 3, which is why these cases need study.
:::

## 3.2 Brunnermeier and Pedersen (2009): "Market liquidity and funding liquidity"

Review of Financial Studies, volume 22, issue 6, pages 2201 to 2238.

**Main idea.** Traders provide market liquidity, but only when they have funding. Funding (capital and margin) depends on how liquid the assets are. Under some conditions margins are destabilizing, and the two kinds of liquidity reinforce each other. This gives liquidity spirals.

::: {.hook title="Two liquidities: 'Market liquidity belongs to the Asset. Funding liquidity belongs to the Trader.'"}
- Market liquidity: can I sell easily near the true value? It is measured by spread, depth and price impact. It fails when buyers disappear.
- Funding liquidity: can I get money to hold this position? It is measured by margin, haircut and cost of borrowing. It fails when lenders demand more capital.
:::

## 3.3 Master picture: the spiral loop (slide 7)

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[n,fill=gray!15] (A) at (-6.3,1.6) {1. Initial\\losses};
\node[n,fill=orange!15] (B) at (-2.6,1.6) {2. Funding problems\\for speculators};
\node[n,fill=orange!15] (C) at (1.6,1.6) {3. Reduced\\positions};
\node[n,fill=orange!15] (D) at (5.4,1.6) {4. Prices move away\\from fundamentals};
\node[n,fill=red!10] (F) at (1.6,-0.9) {5. Losses on existing positions\\\textbf{loss spiral}: $W$ falls};
\node[n,fill=red!10] (E) at (1.6,-2.6) {6. Higher margins\\\textbf{margin spiral}: $m$ rises};
\draw[e] (A)--(B); \draw[e] (B)--(C); \draw[e] (C)--(D);
\draw[e] (D.south) |- (F.east); \draw[e] (D.south) |- (E.east);
\draw[e] (F.west) -| ($(B.south)+(-0.4,0)$);
\draw[e] (E.west) -| ($(B.south)+(0.4,0)$);
\node[n,fill=yellow!25,font=\normalsize] at (-5.6,-1.8) {$X\le\dfrac{W}{m}$};
\end{tikzpicture}
\end{center}
```

::: {.box title="The funding limit: 'W falls: Loss spiral. m rises: Margin spiral.'"}
Capital needed is $mX$, and it cannot exceed $W$. So $mX\le W$, which gives $X\le W/m$. ($W$ is capital, $m$ the margin rate and $X$ the position in money.)

**Example.** $W=10$, $m=10\%$. First position $10/0.10=100$. Loan $100-10=90$.

A 3 percent price fall: position $97$, capital $97-90=7$.

Old margin: allowed $7/0.10=70$, so the **loss spiral** sells $97-70=27$.

New margin 14 percent: allowed $7/0.14=50$, so the **margin spiral** sells $70-50=20$ more.

Total **47 out of 97**. This selling pushes the price down again.
:::

| Point | Loss spiral | Margin spiral |
|---|---|---|
| What changes | Capital $W$ falls | Margin $m$ rises |
| Cause | Price fall on existing positions | Financier fears volatility and illiquidity |
| Leverage | Trader sells to keep leverage constant | Trader must cut leverage |
| Needs a higher margin? | No | Yes |

::: {.hook title="Triggers: LFVF, 'Lose, Fund, Volatile, Forced'"}
- **L**: a first loss, so speculators lose capital.
- **F**: a funding shock, so lenders cut credit or capital is withdrawn.
- **V**: a volatility shock, so financiers cannot tell news from illiquidity and raise margins.
- **F**: a forced sale, where a large trader must unwind and others may predate (Topic 4).
:::

## 3.4 Five features of liquidity (slide 5)

::: {.hook title="Mnemonic: 'Dry, Common, Volatile, Flees, Follows'"}
- **Dry:** liquidity can suddenly dry up, because financiers are imperfectly informed and raise margins when volatility changes.
- **Common:** many securities become illiquid together, because the same speculators supply liquidity in all of them.
- **Volatile:** volatile assets are less liquid, because they need higher margins.
- **Flees:** flight to quality; risky assets lose more liquidity, because scarce capital moves to low-margin assets.
- **Follows:** liquidity falls when the market falls, because funding conditions move with the market.

This is an easy question. Write each feature with its reason.
:::

**Margins on S&P 500 futures, 1982 to 2008 (slide 6): "4 before, 12 on Black Monday".** About 4 percent from 1982 to 1987. Above 12 percent on 19 October 1987. About 3 percent in calm 1989, then up again in the 1989 mini-crash. About 6.4 percent in the 1990 to 1991 US and Iraq war. About 2 percent in calm 1997, then 3.8 percent in the Asian crisis. About 5.5 percent at the LTCM collapse in 1998. From about 4 to about 5 percent in the 2007 to 2008 subprime crisis. Margins are for exchange members, as a percent of contract value; initial equals maintenance margin for members. **Margins rise when markets are in trouble, so traders lose funding exactly when the market needs them.**

## 3.5 Jain, Mishra and McInish (2013): the two spiral scores

"Identification and valuation implications of financial market spirals", in *Rethinking Valuation and Pricing Models*, from page 471. This is the professor's own paper. Learn the two definitions and the signs.

**Master picture: today must beat yesterday and leave the band.**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\begin{scope}
\fill[gray!15] (0,1.2) rectangle (5,2.2);
\draw[dashed] (0,2.2)--(5,2.2) node[right,font=\small]{$\bar s+0.5\sigma_s$};
\draw (0,1.7)--(5,1.7) node[right,font=\small]{$\bar s$};
\draw[dashed] (0,1.2)--(5,1.2) node[right,font=\small]{$\bar s-0.5\sigma_s$};
\fill (1.5,1.9) circle (2.5pt) node[below,font=\scriptsize]{$s_{t-1}$};
\fill[red] (3.5,2.8) circle (3pt) node[above,font=\scriptsize]{$s_t$: higher and above, $+1$};
\draw[e,red] (1.6,1.95)--(3.4,2.75);
\node[font=\small\bfseries] at (2.5,3.7) {Illiquidity spiral (spread)};
\end{scope}
\begin{scope}[xshift=9cm]
\fill[gray!15] (0,1.2) rectangle (5,2.2);
\draw[dashed] (0,2.2)--(5,2.2) node[right,font=\small]{$\bar M+0.5\sigma_P$};
\draw (0,1.7)--(5,1.7) node[right,font=\small]{$\bar M$};
\draw[dashed] (0,1.2)--(5,1.2) node[right,font=\small]{$\bar M-0.5\sigma_P$};
\fill (1.5,1.5) circle (2.5pt) node[above,font=\scriptsize]{$P_{t-1}$};
\fill[red] (3.5,0.6) circle (3pt) node[below,font=\scriptsize]{$P_t$: lower and below, $+1$};
\draw[e,red] (1.6,1.45)--(3.4,0.65);
\node[font=\small\bfseries] at (2.5,3.7) {Loss spiral (price)};
\end{scope}
\end{tikzpicture}
\end{center}
```

::: {.box title="Spiral scores: '+1 is always bad'"}
The band is last year's mean (or midpoint) plus or minus half a standard deviation. **Both** tests must hold, otherwise the score is 0.

**Illiquidity spiral** (bad = spread up). $S_t=+1$ if $s_t>s_{t-1}$ and $s_t>\bar s+0.5\sigma_s$ (29.2). $S_t=-1$ if $s_t<s_{t-1}$ and $s_t<\bar s-0.5\sigma_s$ (29.1). Otherwise 0 (29.3). Sum: $S_{spiral,10}=\sum_{k=0}^{9}S_{t-k}$ (29.4).

**Loss spiral** (bad = price down). $L_t=+1$ if $P_t<P_{t-1}$ and $P_t<\bar M-0.5\sigma_P$ (29.5). $L_t=-1$ if $P_t>P_{t-1}$ and $P_t>\bar M+0.5\sigma_P$ (29.6). Otherwise 0 (29.7). Sum: $P_{spiral,10}=\sum_{k=0}^{9}L_{t-k}$ (29.8). The slide calls the score P; these notes use $L_t$.

The inequality signs are opposite in the two measures, because bad means higher for spreads and lower for prices.

**Example.** Spread 0.95, yesterday 0.90, mean 0.80, sd 0.20. Upper limit $0.80+0.10=0.90$. Higher than yesterday and above 0.90, so **+1**.

Price 95, yesterday 97, midpoint 100, sd 8. Lower limit $100-4=96$. Lower than yesterday and below 96, so **+1**.

Ten scores 1, 1, 0, 1, 1, $-1$, 1, 0, 1, 1: seven $+1$, one $-1$ and two 0, so the sum is **6**.
:::

**Data (slide 11): "CRSP plus Datastream, S&P 500, 1982 to 2010, 476 firms".** CRSP gives daily closing bid, ask, volume, ticker, close price, market capitalization and PERMCO. Datastream gives price to book, dividend per share, total assets and return on equity, plus the market value and P/E of the S&P 500. Period November 1982 to December 2010. Final sample 476 firms.

**Histograms (slide 12).** Ten-day counts run from $-10$ to 10. Sigma-based illiquidity has two peaks (0 and $-4$). Alternative illiquidity has one peak at $-4$ with a right tail. Both loss measures have two humps near $-5$ and $+5$. Losses and gains come in runs, which is why the loss measures have humps away from zero.

::: {.hook title="Valuation (slide 13): 'Spirals shrink multiples'"}
- The regressions explain price to book (PTBV) and P/E.
- The **loss spiral** lowers both PTBV and P/E in all six models (PTBV $-0.034$, P/E $-0.33$).
- The **illiquidity spiral** lowers P/E in all three models ($-0.37$), and lowers PTBV significantly only after controls are added ($-0.049$ in model 5.3).
- Size: a loss spiral of 10 lowers PTBV by $10(0.034)=0.34$ in model 5.1.
- Caution: $R^2$ is small (0.0002 to 0.06). The effects are significant but explain little of the variation.

Conclusion: financial market spirals have valuation implications.
:::

\newpage

# Topic 4: Market-wide liquidity phenomena

::: {.hook title="Four ways liquidity vanishes market-wide: 'Prey, Betray, Pressure, Spiral'"}
- **Prey:** predatory trading, Brunnermeier and Pedersen (2005). Others trade against a distressed trader.
- **Betray:** episodic crises, Carlin, Lobo and Viswanathan (2007). Cooperation between traders breaks down.
- **Pressure:** price pressure, Shkilko, Van Ness and Van Ness (2012). Sellers demand liquidity together.
- **Spiral:** Brunnermeier and Pedersen (2009). Funding and market liquidity feed each other.
:::

**Words.** A distressed trader is forced to sell. A predator uses the forced sale to profit. Liquidation value is the money from selling a position. Price overshooting means the price moves beyond its new long-run level and then comes back. Front running is trading ahead of a known order. A short sale sells a borrowed share. Contagion is a crisis spreading from one trader or market to another.

## 4.1 Predatory trading: Brunnermeier and Pedersen (2005)

**Definition (slide 2).** Predatory trading exploits an information advantage to profit at the expense of others. It may use non-public information or market dynamics. It benefits the predator unfairly and harms other investors or the market. **Pattern: "Sell with them, then buy from them."** One trader must sell, other traders also sell, and they buy back later.

**Master picture: the price path (slides 9 to 11).**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.8cm,y=0.22cm]
\draw[-{Stealth}] (4,96)--(7.7,96) node[right,font=\small]{time};
\draw[-{Stealth}] (4,96)--(4,121) node[above,font=\small]{price};
\foreach \y in {100,110,116} {\draw (3.95,\y)--(4.05,\y); \node[left,font=\small] at (3.95,\y) {\y};}
\foreach \x in {5,5.8,6.3,7} {\draw (\x,96.5)--(\x,95.5); \node[below,font=\small] at (\x,95.5) {\x};}
\draw[very thick,red] (4.3,116)--(5,116)--(5.8,100)--(6.3,110)--(7.3,110);
\draw[dashed] (5.8,100)--(5.8,96); \draw[dashed] (6.3,110)--(6.3,96);
\node[font=\footnotesize,align=right,anchor=east] at (5.4,103) {both sell 8:\\16 shares, $\lambda=1$,\\price falls 16};
\node[font=\footnotesize,align=left,anchor=west] at (6.35,104) {predator buys\\back 10 alone};
\node[font=\small,anchor=south] at (4.65,116.5) {distress at 5};
\draw[dashed] (5.8,100)--(7.35,100);
\draw[decorate,decoration={brace,amplitude=4pt}] (7.6,110)--(7.6,100) node[midway,right=5pt,font=\small]{overshoot 10};
\end{tikzpicture}
\end{center}
```

::: {.box title="Simulated example: '116, 100, 110'"}
Inputs: supply $S=40$; two strategic traders, one distressed; limit $\bar x=10$; each starts with 8; distress at time 5; final time $T=7$; $\mu=140$; price impact $\lambda=1$; speed without temporary cost $A=20$ per time unit. At time 7 the asset pays off or the market becomes perfectly liquid.

1. Starting price 116 (read from the slide).
2. Two sellers share $A$: each sells at $20/2=10$ per time unit.
3. The distressed trader needs $8/10=0.8$, so selling ends at $5+0.8=5.8$.
4. The predator sells all 8 at the same time. Total sold 16. The price falls $16\times1=16$, to **100**.
5. The predator buys back from 0 to its limit 10, alone at speed 20: $10/20=0.5$, ending at $5.8+0.5=6.3$.
6. New price **110**. Overshoot $110-100=$ **10**.

The predator sells at higher marginal prices and buys back at lower ones.

**More predators (slide 12).** Total holding stays 16. With 3, 9 and 27 traders, the low is about 110, 112.5 and 113.1, and the final price is about 113.3. The overshoot falls (3.3, then 0.8, then 0.2), and predators buy back earlier. **"Competition eats predation."**
:::

::: {.hook title="Five results: OLIPS"}
- **O**: the price overshoots.
- **L**: the distressed trader gets a lower liquidation value.
- **I**: the market is illiquid exactly when liquidity is most needed.
- **P**: a trader can profit by triggering another trader's crisis.
- **S**: the crisis spills over across traders and markets.
:::

**Contribution (slide 3): "Large, Slow, Known".** A new framework of strategic interaction among large traders with market impact. Traders trade continuously and limit their speed to keep temporary impact cost low. Some traders become distressed, and the others know that they need to sell.

**Specific contributions (slide 4): "Introduce, Types, Hard, Hurts".** (a) It introduces predatory trading: strategic behaviour that exploits others' information disadvantage, causes inefficiency and harms market quality. (b) Types: front running, anticipating orders, and trading strategically ahead of a large order. (c) It is hard to identify: a regulator must separate a legitimate strategy from manipulation. (d) It hurts liquidity, price efficiency, stability and investor confidence.

::: {.hook title="Findings (slide 5) and when predation pays: 'Illiquid and Big'"}
A distressed large investor must unwind. Other strategic traders first trade in the same direction. They withdraw liquidity instead of providing it. The liquidation becomes costly and the price overshoots.

Predation is profitable when (1) the market is **illiquid** and (2) the distressed position is **big** relative to the others' buying capacity.

Exam contrast: the normal view says others buy when someone sells cheaply. Predation says they sell first and buy later.
:::

::: {.hook title="Examples (slide 6): 'Every Disclosed Loser Meets Greedy Cruel Competitors'"}
- **E**nron and UBS Warburg (2002): taking Enron's traders without its book was opposed for "predatory trading risk", because the traders knew the book.
- **D**isclosure (IAFE 2001): detailed disclosure of positions can be ruinous for large portfolios.
- **L**TCM as a victim (Business Week 2001): lenders such as Goldman sold the same asset before LTCM could, in 1998.
- **M**eriwether: selling hurricane insurance does not cause a hurricane, but in markets, people who know you sold insurance can make the loss happen.
- **G**reenspan (1 October 1998): a forced LTCM sale would distort prices and hurt creditors, counterparties and others.
- **C**ramer (2002): "When you smell blood in the water, you become a shark."
- **C**redit General (June 1995): it bought a billion pounds sterling and tried to sell for marks; the market evaporated.
:::

**Framework (slides 7 and 8).** A1 continuous time. A2 a riskless bond and a risky asset. A3 supply $S>0$, payoff $v$ at $T$, $E(v)=\mu$. A4 price $p(t)$. A5 $I$ large strategic traders (hedge funds, proprietary desks). A6 long-term investors (pension funds, individuals). A7 strategic traders are risk neutral. A8 they count their own price impact. Position: $x^i(t)=x^i(0)+\int_0^ta^i(\tau)\,d\tau$, where $a^i$ is the trading speed (negative for selling). Limit: $-\bar x\le x^i(t)\le\bar x$, from risk or capital.

## 4.2 Carlin, Lobo and Viswanathan (2007): episodic liquidity crises

**Master picture: a repeated game that breaks when stakes are high.**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm]
\foreach \i/\col/\lb in {1/green!15/cooperate,2/green!15/cooperate,3/green!15/cooperate,4/red!20/PREDATE,5/green!15/cooperate,6/green!15/cooperate} {\node[n,fill=\col,minimum width=1.15cm] (p\i) at (\i*1.9,0) {\scriptsize period \i\\\scriptsize \lb};}
\foreach \i/\j in {1/2,2/3,3/4,4/5,5/6} {\draw[e] (p\i)--(p\j);}
\node[font=\small,align=center,below=0.25cm of p4] {high stakes:\\gain today $>$\\future cooperation};
\node[font=\small,align=center,below=0.25cm of p2] {small stakes: traders\\supply liquidity to each other};
\end{tikzpicture}
\end{center}
```

::: {.hook title="Mnemonic: RHEC, 'Repeated, High stakes, Episodic, Contagion'"}
1. The stage game is a continuous-time trading game over one period, with a pricing equation for price impact.
2. In one period, a trader gains by predating.
3. With many periods (**repeated**), traders meet again and again.
4. They cooperate most of the time and give apparent liquidity to each other.
5. A trader who predates today loses cooperation in the future.
6. Cooperation breaks when stakes are **high**: the gain today exceeds the future loss.
7. Predatory trading starts and causes **episodic** illiquidity.

Across markets: cooperation makes crises less frequent, but a breakdown then hits all those markets (**contagion**).

Cooperation: most of the time, small stakes, traders supply liquidity, the market looks liquid. Predation: sometimes, high stakes, traders sell with the one in need, the market suddenly becomes illiquid.
:::

## 4.3 Shkilko, Van Ness and Van Ness (2012): "Short selling and intraday price pressures"

Financial Management, volume 41, issue 2, pages 345 to 370.

::: {.hook title="Mnemonic: 'Longs lead, shorts follow'"}
- It studies intraday downward price pressure in single stocks.
- Non-short volume that demands liquidity (long sellers) drives most declines.
- Short sellers are also active and make declines somewhat worse. Their selling is more intense in the decline stage of large reversals.
- Short sellers usually provide liquidity, but they switch to demanding it.
- Their effect is second to that of long sellers. This contradicts the view that short sellers destabilize markets on their own.
:::

**Master picture: the large reversal day (slide 15).**

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[-{Stealth}] (0,0)--(8.6,0) node[right,font=\small]{time in the day};
\draw[-{Stealth}] (0,-2.8)--(0,1.2) node[above,font=\small]{cumulative return};
\draw[dashed] (0,-2)--(8,-2) node[right,font=\small]{$-2\sigma_i$};
\draw[very thick,blue] (0,0)--(1.5,-0.8)--(3,-2.4)--(4.8,-1.0)--(8,0.1);
\fill[blue] (3,-2.4) circle (2.5pt) node[below,font=\small]{low $\ell\le-2\sigma_i$};
\fill[blue] (8,0.1) circle (2.5pt);
\node[font=\small,align=left,anchor=west] at (8.2,0.7) {close within the band:\\rebound 90 to 110\% of $\lvert\ell\rvert$};
\end{tikzpicture}
\end{center}
```

::: {.box title="Large reversal: 'Two sigma down, 90 to 110 back'"}
1. Normal movement $\sigma_i$: the average standard deviation of five-minute cumulative returns of stock $i$ over the previous 20 trading days.
2. Decline: $\ell\le-2\sigma_i$, where $\ell$ is the lowest cumulative return of the day.
3. Rebound: $0.9\lvert\ell\rvert\le R_{close}-\ell\le1.1\lvert\ell\rvert$. The rise from the low to the close is the rebound.

**Example.** $\sigma_i=1\%$, so the low must be $-2\%$ or lower. With $\ell=-2$: the smallest rebound 1.8 gives a close of $-0.2\%$; the largest rebound 2.2 gives $+0.2\%$. The day must end between **$-0.2$ and $+0.2$ percent**.

**Slide error:** the figure prints $\ell\ge-2\sigma$. The text needs $\ell\le-2\sigma$.
:::

## 4.4 Spirals again (slides 16 to 20)

This is the same Brunnermeier and Pedersen (2009) loop as in section 3.3. Traders provide market liquidity according to their funding, and capital and margins depend on market liquidity. The trigger is that margin requirements rise in crises (S&P 500 futures in 1987, 1998 and 2007). The loss spiral: losses reduce capital and force sales. The margin and haircut spiral: higher margins reduce allowed leverage and force sales.

**Findings (slide 20): the same "Dry, Common, Volatile, Flees, Follows".** Sudden dry-up happens when financiers are imperfectly informed and fundamental volatility varies over time. Liquidity and fragility move together across assets, because a change in funding affects liquidity supply in all assets. Liquidity is correlated with volatility. Flight to quality arises from the model. Liquidity moves with the market because funding conditions do (the slide cuts off "funding conditions do").

## 4.5 Join the whole topic

::: {.hook title="Seven phenomena, one cause each"}
- **Commonality** (stocks gain and lose liquidity together): Chordia and others, and funding limits.
- **Dry-up** (liquidity vanishes suddenly): margin spiral.
- **Flight to quality** (capital moves to safe assets): scarce funding.
- **Overshooting** (price falls too far and returns): predatory trading.
- **Episodic illiquidity** (calm periods end in short crises): breakdown of cooperation.
- **Contagion** (a crisis spreads): common traders and broken cooperation.
- **Large reversal** (a sharp fall reverses in a day): temporary selling pressure.
:::

| Point | Predation | Broken cooperation | Spiral |
|---|---|---|---|
| Trigger | Another trader must sell | Stakes become high | Loss or margin increase |
| Is the seller forced? | The victim is forced, the predator chooses | The predators choose | All are forced by funding |
| Strategy needed? | Yes | Yes | No |
| Key limit | Position limit of buyers | Value of future cooperation | Capital and margin |

**Exam.** A market-wide question needs three layers. First define commonality. Then give the mechanism. Then give the evidence.

\newpage

# Topic 5: Basic concepts (short)

::: {.box title="Roll (1984): 'the bounce shares one sign, with a minus'"}
Assumptions: A1 $V_t=V_{t-1}+\varepsilon_t$ (random walk); A2 constant spread $S$; A3 $Q_t=\pm1$ with probability one half each; A4 signs independent over time and of news.

1. $P_t=V_t+\tfrac S2Q_t$.
2. $\Delta P_t=\varepsilon_t+\tfrac S2(Q_t-Q_{t-1})$.
3. $\mathrm{Var}(\Delta P_t)=\sigma^2+\tfrac{S^2}{4}\cdot2=\sigma^2+\tfrac{S^2}{2}$.
4. Neighbouring changes share only $-Q_{t-1}^2$, so $\mathrm{Cov}(\Delta P_t,\Delta P_{t-1})=-\tfrac{S^2}{4}$.
5. $S=2\sqrt{-\mathrm{Cov}}$. Example: Cov $=-0.0625$, root 0.25, $S=0.5$.

Limits: it fails when the sample covariance is positive; it assumes trades carry no information; it assumes a constant spread.
:::

| Mnemonic | List |
|---|---|
| I Want Deep Rivers | Liquidity dimensions: **I**mmediacy (how fast), **W**idth (cost of a small trade, the spread), **D**epth (how much at a given price), **R**esiliency (how fast the price recovers) |
| Please Bring Dad's Huge Avocado, Very Fresh | Traders: **P**roprietary, **B**rokers, **D**ealers, **H**edgers, **A**rbitrageurs, **V**alue investors, **F**ront runners |
| Let Traders Invest Very Profitably | Market quality: **L**iquidity, **T**ransaction cost, **I**nformative prices, **V**olatility, trading **P**rofits |
| PIP | Why we trade: **P**rofit, **I**nformation, **P**rice discovery |
| Rules, Rooms, Info, Meet, Safe | What microstructure covers: trading **r**ules, physical layouts (NSE NEAT), **i**nformation systems, how participants **m**eet, **s**afeguards (price bands, circuit breakers, halts) |
| Venues, Discovery, Spreads, Intraday, Costs | Kissell's (2014) five focuses: trading venues (displayed and dark), price discovery, spreads and quotes, intraday behaviour, transaction costs |
| Platform, Info flow, Interaction, Rules, Imperfections | Dimensions of a market. The two imperfections are transaction cost and information asymmetry |

| Point | Fundamental volatility | Transitory volatility |
|---|---|---|
| Cause | Unanticipated changes in values | Trading by impatient uninformed traders |
| Life | Permanent | Temporary, prices revert to value |
| Example | Earnings news | Bid-ask bounce, large uninformed orders |
| Who ends it | Not applicable | Value traders and arbitrageurs |

Total volatility is fundamental plus transitory volatility. Dealers infer information from order flow; this is the adverse selection part of the spread, and its price changes add to fundamental volatility.

| Point | Inventory models | Information models |
|---|---|---|
| Dealer's problem | Unbalanced inventory | Better-informed customers |
| Source of the spread | Cost and risk of inventory | Expected loss to informed traders |
| Effect of a trade on price | Temporary | Permanent |
| Papers | Garman, Amihud--Mendelson, Stoll, Ho--Stoll, O'Hara--Oldfield | Bagehot, Copeland--Galai, Glosten--Milgrom, Kyle, Easley--O'Hara |

**Harris facts.** Trading is zero-sum relative to the market average. Brokers arrange trades for clients. Patient traders get better prices than impatient ones. Speculators trade on information about future prices. Dealers lose to well-informed speculators. Bluffers sometimes fool uninformed traders. Investors move money to the future, and borrowers do the opposite. Hedgers manage risk. Asset exchangers swap one asset for one they value more. Gamblers trade for fun. Arbitrageurs keep prices close across markets. The sell side (dealers, brokers) serves the buy side.

**Terms.** Bid is the best price to sell at, and ask is the best price to buy at. The mid quote is their average; the spread is ask minus bid. BBO is the best bid and offer; NBBO is the national best. Uptick, downtick and zero tick compare with the last price. A block deal is one trade of at least 5,00,000 shares or Rs 10 crore, in a separate window (8:45 to 9:00 AM or 2:05 to 2:20 PM), not visible to retail. A bulk deal is at least 0.5 percent of listed shares, in normal hours, visible to all. Axis Bank example: bid 664.40 (453), ask 664.55 (714). Spread 0.15, mid 664.475, proportional spread 0.0226 percent, depth 583.5.

**Orders.** A market order trades now at the best price; it takes liquidity and risks a poor price. A limit order trades only at the limit or better; it provides liquidity and risks non-execution and adverse selection (ex post regret). A stop order activates at the stop price; a sell stop is a safety net for a long position. Continuous markets trade at any time. Call markets collect orders and execute them together (the NSE pre-open call auction). Quote-driven markets trade with dealers. Order-driven markets match orders by rules. A circuit breaker halts trading after a large move.
