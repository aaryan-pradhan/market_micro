# O'Hara & Oldfield (1986) in plain words

Past paper: Midsem 2024 Q5.

1. How does the market maker's risk aversion affect how he sets prices?
2. How does his utility function measure profit over an infinite time horizon?
3. How does he set the ask and bid when he takes limit orders into account?

---

## 1. The words you need

**Market maker (dealer).** One person or firm who always stands ready to buy from and sell to the public. In this model there is only one.

**Ask.** The price at which the market maker sells to the public.

**Bid.** The price at which the market maker buys from the public.

**Spread.** Ask minus bid. It is his reward for providing the service of being always available to trade.

**Placement of the spread.** Where the bid and ask sit, high or low. Two dealers can both have a spread of ₹2: one quoting 98–100 and the other 101–103. The spread is the same size, but the placement is different.

**Inventory.** The number of shares he holds right now. If the public sells to him, his inventory goes up. If the public buys from him, it goes down.

**Limit order.** An order that says "trade only at this price or better." For example: "buy 100 shares, but only if the price is ₹98 or lower." It waits until that price is available.

**Market order.** An order that says "trade right now at whatever the current price is." It does not wait.

**Known versus uncertain orders.** In this model the market maker **sees the limit orders before he sets his prices**, so he knows them for sure. Market orders arrive **during** the period, so he can only guess how many will come. That makes them uncertain.

**Risk-neutral.** Someone who cares only about the average outcome. Getting ₹100 for sure feels the same to him as a 50/50 chance of ₹0 or ₹200.

**Risk-averse.** Someone who dislikes uncertainty. He prefers the sure ₹100 to the 50/50 gamble, even though both average ₹100.

**Utility function.** A way of turning money into "happiness" or satisfaction. For a risk-averse person each extra rupee adds a little less happiness than the one before. The first ₹1,000 of profit matters more to him than the jump from ₹50,000 to ₹51,000.

**Marginal utility.** How much happiness one more rupee adds right now. It is **high when profit is low** (money is badly needed) and **low when profit is high** (you already have plenty).

**von Neumann–Morgenstern utility.** The standard name for this kind of utility function. The decision maker picks the choice with the highest *expected* (average) happiness.

**Trading day and trading intervals.** Each day is split into several short periods (the slides call the number of periods "n"). He sets new prices at the start of each period.

**Infinite horizon.** The business never has a planned end date. He expects to keep making markets day after day, forever.

**Discount factor.** A number between 0 and 1 that makes future days count a little less than today. Happiness a year from now matters, but less than happiness today.

**Settlement and the overnight (repurchase) market.** All trades are settled at the end of each day. If he ends the day **short** (he has sold shares he does not own), he borrows them overnight and pays a fee. If he ends the day **long** (holding shares), he lends them out overnight and earns that fee.

**Value function.** A score for "how good tomorrow and all future days will be, given the inventory I carry into tomorrow, if I keep acting sensibly." It lets him judge today's decisions by their effect on the future too.

---

## 2. The story of the model in plain words

At the **start of each period** the market maker:

1. looks at the limit orders already waiting (he knows exactly how many buyers and sellers there are at each price),
2. forms a guess about how many market orders will arrive at each possible price,
3. sets his ask and bid using both pieces of information.

**During the period**, he fills every limit order that matches his prices and every market order that arrives.

**At the end of the period**, he counts his inventory. Then the next period starts with new limit orders.

**At the end of the day**, trades settle. He pays or earns the overnight fee depending on his inventory, and he carries that inventory into tomorrow.

He does this forever, and he chooses his prices to make his **total discounted happiness over all future days** as large as possible.

---

## 3. What was new compared with earlier models

- **Both limit and market orders.** Most earlier papers, including Garman, Amihud–Mendelson, Stoll and Ho–Stoll, only had market orders.
- **Discrete time.** He decides in separate periods, not continuously.
- **Infinite horizon with daily payoffs.** Ho–Stoll had a fixed end date on which everything was sold off. Here there is no end date and no forced sell-off, and he is "paid" (gets his profit and its happiness) every day, not only at the end.
- **Only his trading account counts.** Ho–Stoll also included the dealer's other wealth; this model does not.
- **Two uncertainties.** He is unsure about how many market orders will come, and about what his inventory will be worth.

---

## 4. Answering the three parts of the question

### (a) How does risk aversion affect pricing?

His spread is made of **three parts**:

1. **A part set by the known limit orders.** He knows these for sure, so this part involves no guessing.
2. **A part for the expected market orders.** This is the adjustment he would make even if he were risk-neutral, based on the *average* number of market orders he expects.
3. **A risk adjustment.** This part exists only because he is risk-averse. It reflects his discomfort with not knowing how many market orders will arrive and what his inventory will be worth.

The surprising finding is that **the risk adjustment can be positive or negative**. So a risk-averse market maker may set a **smaller** spread than a risk-neutral one.

In simple terms, the reason is this. A risk-averse person cares most about avoiding bad days. Some kinds of surprise order flow make his bad days worse; to protect himself from those he widens his prices. Other kinds of surprise order flow bring extra profit on days when he already has plenty, and he values that extra profit less. Whether the protective push outweighs the other depends on the situation. When it does not, his spread ends up narrower than a risk-neutral dealer's.

Risk aversion therefore changes **both the size of the spread and the actual bid and ask prices**.

### (b) How does the utility function measure profit over an infinite horizon?

- He does not just add up his rupees. Each day, he turns **that day's total trading profit** into happiness using his utility function.
- Because he is risk-averse, a steady profit every day gives him more happiness than the same average profit that swings wildly between good and bad days.
- He then adds up the happiness from **every future day**, with each day counting a little less than the day before (the discount factor).
- His goal is to set bid and ask prices so that this **total discounted happiness** is as large as possible.
- There is no final date, so he never has to dump his inventory at the end. Instead, the **value function** tells him how good or bad it is to carry a given inventory into tomorrow. Each day's decision therefore balances **today's profit** against **tomorrow's position**.

### (c) How does he set the ask and bid, given limit orders?

Think of each price as a balance between two things:

- **Today's cash.** A higher ask earns more per share sold but attracts fewer buyers. A lower bid costs less per share bought but attracts fewer sellers.
- **The inventory he ends the day with.** Every share he buys or sells changes the inventory he carries into tomorrow, and the value function tells him whether that is good or bad.

Limit orders help because they are **known**. He can see exactly how many shares will trade at each price he might choose, so the limit-order part of his decision involves no risk. Only the market-order part is a guess, and that is where the risk adjustment comes in.

**Inventory affects both prices together:**

- If he is holding **too many shares**, one more share is worth less to him. He lowers **both** the bid and the ask, so he buys less and sells more.
- If he is holding **too few shares**, or is short, he raises **both** prices.

This is what the paper means by "inventory has a pervasive influence." It affects **where** the spread sits, and through his risk attitude it also affects **how wide** it is.

---

## 5. Short exam summary

- Model: one risk-averse market maker, with both limit orders (known) and market orders (uncertain), in discrete periods over an infinite number of days.
- Goal: maximise the total discounted happiness from each day's trading profit.
- Spread = limit-order part + expected-market-order part + risk adjustment.
- The risk adjustment can go either way, so a risk-averse dealer's spread may be **smaller** than a risk-neutral dealer's.
- Inventory affects both the **placement** and the **size** of the spread.

The full version with the formulas is in `inventory_models.html#oo`.
