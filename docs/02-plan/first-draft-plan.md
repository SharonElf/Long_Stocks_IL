# First Draft Plan — Long Stocks IL (in simple words)

> **Status: DRAFT, revised after the first planning talk (2026-10-08).**
> Nothing here is final. Nothing is built yet.
> Anything marked **[open]** is not decided yet.
> This is not yet copied into `context/project-overview.md`, `context/architecture.md`
> or `context/build-plan.md`.
>
> **Revision 2 (same day):** the investor changed three things.
> 1. Risk is judged **per ticker**, not for the portfolio. The portfolio view and the
>    "how much" are moved to a **next stage** (section 8).
> 2. Market sentiment is read **once a week**.
> 3. Each ticker gets its own **statistical figures**, and possibly **news**.

## 0. The idea in one minute

Every day, after the market closes, the system researches **each ticker** the investor holds.
It looks at that ticker's own trend and gives it one stance:
**hold, add, reduce, or sell all**, with a reason.

Once a week, the system also reads the **mood of the whole market**. That mood is background
for every ticker's decision.

For now the system does **not** say how much to add or reduce. That comes later.

The system only gives advice. It never buys or sells by itself.

## 1. How we are planning

We plan **backwards**, starting from what the investor wants to receive:

1. What does the investor get at the end?
2. What decisions must that support?
3. What question does each decision ask?
4. What data answers each question, and how good must it be?
5. Where can we get that data, what does it cost, and can we trust it?
6. How does it run: where it is stored, where it is calculated, how it is sent, how often?
7. **Only at the end:** look at the two older systems (bank-portfolio-pilot and
   trading-copilot-brain) and reuse what already fits.

The six areas from the 2026-10-08 call are used as a double-check at the end. They are not the
starting point. Links to the older systems are in `knowledge/REFERENCES.md`.

## 2. What the investor receives

A list of every ticker held. Each line has a stance and a reason.

| Stance | Meaning |
|---|---|
| Hold | Do nothing. |
| Add | The ticker looks good enough to buy more. |
| Reduce | The ticker looks weak enough to sell some. |
| Sell all | Close the whole position. |

- **No amounts for now.** "Add" and "reduce" say *what* and *why*, not *how much*.
- **"Replace" is not its own answer.** That choice belongs to the investor.
- **Long only, no shorts ever.** "Sell all" is the lowest the system can go. It never advises
  selling something the investor does not own. **(Decided.)**
- We only need data for things the investor already holds. We do not search the market for new ideas.
- The exact look of the list is left for later.
- Advice only, no automatic orders. (Comes from the older systems; still to confirm.)

## 3. How the system thinks (draft)

**The ticker is what matters.** Each ticker is researched on its own, and its own trend decides.

**Once a week: the market mood**

```
Look at the whole market (a few index charts + what describes the market state)
  → Claude writes a short "market sentiment" with reasons
  → saved, and used as background for every ticker that week
```

**Every day: for each ticker**

```
1. Long charts (monthly, weekly, daily)  → what is the trend? any danger or opportunity zone?
2. Statistical figures for the ticker    → numbers that describe how it behaves
3. News for the ticker (?)               → only if we decide news is an input
4. Something flagged?                    → then look at short charts (4 hours, 1 hour)
5. Claude reads all of it, plus this week's market mood and yesterday's stance
                                         → stance + reason
```

What each part is for:

| Part | Its job |
|---|---|
| Long charts and scanner | Show the ticker's trend and raise a flag at danger zones and opportunity zones. |
| Short charts (fine-tune) | Sharpen the timing, but only after the scanner flagged something. This keeps small noise out of the decisions. |
| Statistical figures | Describe the ticker in numbers. Which figures: **[open]**. |
| News | Possible extra input for the ticker. Yes or no: **[open]**. |
| Weekly market mood | Background. It shapes how cautious or bold the ticker's stance is. How exactly: **[open]**. |
| Yesterday's stance | Keeps the advice steady. The default is "no change". A change needs new evidence. |

### Points we already agreed

- **Risk belongs to the ticker,** judged from the ticker's own trend. How risk is measured: **[open]**.
- **Market sentiment is weekly.** Which day and time: **[open]**.
- **Tickers are checked every day,** because news and big moves can change things fast.
  Time of day: **[open]**.
- **Amounts are left out for now.**
- **Claude works out the stances; the system calculates the inputs.**

## 4. The data we need

### Must have

1. **Holdings and trades.** What is held, where, how much, and each purchase (needed to know the cost).
2. **Charts (candles) for each ticker.** Daily, weekly and monthly for all of them.
   4-hour and 1-hour only for things traded on an exchange.
3. **Statistical figures for each ticker.** Which ones: **[open]**.
4. **Whole-market data,** read weekly. A few index charts, plus anything that describes the market state.
5. **The weekly market sentiment.** Claude's output, with the reasons kept.
6. **A log of every recommendation.** Each day, each ticker: the stance, the reason. We need it to
   explain the "why", to avoid changing our mind too often, and to check later whether the advice was good.

### Helpful

7. **One record per instrument.** Its names and numbers at the broker and at the data source, its
   type, its currency, and whether it has live prices during the day or only one price per day.
8. **Prices and exchange rates,** to value the holdings.

### Only if needed

9. **News per ticker.** Only if we decide news is an input. **[open]**
10. **Profit and loss by FIFO** (first bought, first sold). It is one of the six areas. We do not yet
    know if the daily advice needs it.

### Moved to the next stage

- The table that says which risk group each holding belongs to.
- Target shares per risk group.
- Amounts to add or reduce.

**Suggested order for going through them:** items 1, 2 and 4 first (they cost the most and carry
the most risk). Then 3 and 5 (the thinking inputs). Then 6 and 7. Then 8 to 10.
Each item gets its own talk: how important it is and what to do with it.

## 5. Problems and choices still to settle

- **Changing the advice too often.** If Claude re-judges every ticker every day, the stances can jump
  around and become noise. The plan so far: Claude sees yesterday's stance and keeps it unless there is
  new evidence. Any extra rule (for example, limits on how far a stance can jump in one day): **[open]**.
- **Explainable and repeatable.** The investor must be able to follow why a stance was given.
  The same inputs should not give different answers on different runs.
- **Some things have no price during the day.** Classic mutual funds and bonds publish one price a
  day. They can be checked on monthly, weekly and daily charts, but never on 4-hour or 1-hour charts.
  We treat this as a natural limit. To confirm.
- **The chart data source is the biggest risk.** The research about the Tel Aviv exchange (TASE) in
  `knowledge/` has not been checked. Charts built from 15-minute samples are unreliable for things
  that trade rarely. We need a short test of the data source against the real holdings **before**
  building anything.
- **Which tickers does Claude look at each day?** Every ticker, or only the flagged ones? The
  scanner checks all of them either way. **[open]**

## 6. How it will run (draft)

The investor said: the "conductor" is **n8n**, the "brain" is the **Claude API**, and
**all the calculations are done in Supabase (the database) before anything is sent to Claude.**

**Weekly run: market mood**

```
Weekly timer
 → fetch index data
 → Supabase calculates the market "summary sheet"
 → Claude: market sentiment + reasons
 → Supabase checks the answer is in the right form
 → save it
```

**Daily run: each ticker**

```
Timer fires after the market closes
 → fetch fresh charts and prices (and news, if we decide to use it)
 → Supabase calculates a "summary sheet" for each ticker
   (trend, key price levels, statistical figures)
 → scanner checks the long charts of every ticker
 → short-chart fine-tune only for flagged tickers
 → Claude, one call per ticker, all at the same time:
   reads the ticker sheet + this week's market mood + yesterday's stance
   → stance + reason
 → Supabase checks the answer is in the right form
 → save to the recommendations log → tell the investor
```

Rules for the design:

- **n8n only conducts.** It starts the run, fetches data, calls Claude, chooses the path, and sends
  the message. It holds no business rules.
- **Claude never does maths and never reads raw charts.** It reads a fixed-format summary sheet.
- **Claude does not remember anything between calls.** So each call includes yesterday's stance and
  reason, and the latest market mood, taken from the database. The default is "no change".
- **Steady answers come from the design,** not from settings. (The newest models do not allow
  the "temperature" setting.) We get steadiness by anchoring to yesterday and by checking in the database.
- **Claude answers in a fixed form (JSON).** We check the form before saving.
- **When something goes wrong:**
  - Bad answer → try once more → if still bad, keep yesterday's stance and send an alert.
  - Never publish a half-finished list.
  - Re-running a day replaces that day's record.
  - Alert if a run has not finished by a set time.
  - Handle the cases where the API refuses or times out.
- **Everything can be checked and replayed.** Every day we save the exact summary sheet sent to
  Claude, the prompt version, and the answer. Every number is calculated "as of a date", and old
  history is never recalculated in place.
- **Prompts are versioned in git.** Each logged recommendation says which prompt version made it.
  The n8n workflow files are also exported to git.
- **Cost is not the problem.** It is one market call a week plus one call per ticker per day.

Things to check:

- Some calculations (finding support and resistance levels, a standard RSI) are awkward in plain SQL.
  We must check what else Supabase offers before putting the scanner in the database.
- The Supabase instance is **shared** with the older projects. A new schema there needs explicit
  approval. Until then, Supabase is read-only from this project.
- With one call per ticker, the tickers are not compared with each other. That is fine for now, because
  the whole-portfolio view is the next stage.

## 7. Open questions

These came from the progress tracker. The right column shows where we are:

| # | Question | Where we are |
|---|---|---|
| 1 | How does this relate to bpp? Own the positions or read them? Replace its signals? | **Postponed** to the last step (look at the older systems). |
| 2 | Israeli holdings only, or also US? | **[open]**. Also decides currency handling and which indexes. |
| 3 | Funds and bonds have no price during the day. Is that OK? | Leaning yes. To confirm. |
| 4 | Where do we get the charts? | **[open]**. Test first, then choose. |
| 5 | Rules, Claude, or a mix? | Partly answered: Claude judges each ticker, the system calculates the inputs. Style of the yes/no gate and the scanner: **[open]**. |
| 6 | How often, and how is it delivered? | Tickers daily, market mood weekly. Delivery channel (Telegram, a report, other) **[open]**. |
| 7 | Do we need profit and loss by FIFO? | **Postponed** to the last step. |
| 8 | Which tools and where do they run? | **Drafted** (section 6): n8n + Claude API + Supabase, calculations in Supabase. A new schema in the shared database needs approval. |
| 9 | Who does what? | **[open]**. The call names Sharon and Einat. |
| 10 | What does success look like? | **[open]** |

New questions from the revision:

- **How is a ticker's risk measured?** From its trend alone, or also from other figures?
- **Which statistical figures** do we compute for each ticker?
- **News per ticker: yes or no?** If yes, from where, and does it need to be read by Claude?
- **How does the weekly market mood change a ticker's stance?** For example, does it make "add" harder in a weak market?
- Is risk versus reward **only price levels**, or also company numbers and valuation?
- Does "the whole market" mean Israeli indexes only, or US as well?
- What does the **yes/no gate** actually decide? Our guess: a permission check on the investor's side
  ("am I able and allowed to act today?"). The investor must confirm.
- Does the list cover only long-term holdings, or every position?
- Should Claude judge every ticker every day, or only the flagged ones?

## 8. Next stage (parked on purpose)

The investor said the portfolio as a whole matters less than the single ticker, so these are
left for later. The first draft had worked out some of them, and they are kept here so they are not lost.

- **How much to add or reduce.** Likely counted in percentage points of the portfolio, then turned
  into a money amount on the day.
- **Risk groups.** A table that says which holding is in which group (low, medium, high). The
  investor will supply it. Only firm point so far: bonds are low risk. The order of stocks versus
  ETFs (including leveraged ETFs, sector ETFs, תעודות סל and mutual funds) comes with that table.
- **Target share per group.** Example from the call: low 22% / medium 60% / high 18%. The investor
  said the real table is "a little more complicated". What is the complication? **[open]**
- **The gap between real and target shares,** and a **safe zone** inside which the system says nothing.
- **Where cash belongs** in the groups.
- **Comparing tickers with each other,** so the portfolio stays consistent.

## 9. Ideas (not decisions)

- When the risk groups come back, base them on a **riskiness score** per ticker, so a holding can move
  to a higher group when it becomes more volatile. The per-ticker risk read from this stage could feed it.
- A **fast path** for big overnight moves, if "once a day after close" turns out to be too slow.
- Analysis of the investor's own behaviour is **postponed** (from the call). For now the aim is one
  complete data file.

## 10. Limits we were given (from the call)

- Budget for data: about **$50–100 per month**.
- Sites already mentioned as data sources: Funder (פאנדר) and Maya (מאיה, the TASE site).
- We need daily, weekly and monthly charts for each security, especially for Israeli funds and
  ETFs/תעודות סל.

## 11. What happens next

1. Go through each data item in section 4: how important it is and what to do with it.
   Start with the new ones: statistical figures and news.
2. Settle the open questions in section 7, starting with the universe (Q2), news, and how risk is
   measured per ticker.
3. Only then compare with the older systems. First run `git pull` in `bank-portfolio-pilot`,
   because the local copy is out of date.
4. Move what is settled into `context/project-overview.md`, `context/architecture.md`,
   `docs/01-design/design-doc.md` and `context/build-plan.md`.
5. Later: plan the next stage (section 8).
