# Build Plan

> **Status: BASIC OUTLINE (2026-10-08).** The whole map in broad strokes, with places for
> decisions along the way. Units will be split, merged, reordered or added as decisions land.
> Nothing is built yet. The thinking behind it is in `docs/02-plan/first-draft-plan.md`.

The ordered list of units that make up this build. Each unit is a single, scoped, verifiable
piece of work: small enough for one focused session, concrete enough that "done" is clear.

This file covers **the WHOLE project**: completed units stay in the table with their result and
date, grouped by phase.

Two rules that keep the map honest:

- **Iterations of one deliverable = ONE unit.** A map that went v1 → v2 → v3 is a single unit
  whose result is the latest version; earlier versions go to `archive/`. A future improvement
  is a NEW unit.
- **Units allocate into `Code/` workflows N:M.** The allocation lives in `Code/README.md`.

## How this outline is meant to be used

- It is **basic on purpose.** Each unit gets its own spec in `context/specs/NN-name.md` only when
  it is about to start (use `/new-spec`), not before.
- **Decision gates (D1 to D6)** mark points where a decision changes what comes next. A unit that
  depends on a gate does not start until the gate is settled and written into
  `docs/01-design/design-doc.md`.
- Anything not decided stays marked **[open]**. A unit may not invent the answer.
- **Changing this plan is normal.** Insert a unit, split one, or move one. Record why in the
  progress tracker.

## Rules for a good unit

- It produces one visible, verifiable result.
- It stays within one system boundary. Do not mix database, workflow and prompt changes in one unit.
- It has a checklist of conditions that must be true before it is complete.
- It can be built in a single focused session without needing decisions that belong in another unit.

## Ordering rules

- **Dependencies first.** Never build on something that does not exist yet.
- **Cheapest risk first.** Test the biggest unknown (the chart source) before building on it.
- **Calculations before Claude.** Supabase produces the summary sheets before any prompt is written.
- **Prove it quietly before it is live.** A trial run with no action taken comes before real use.
- **Security and approvals before functionality.** The shared Supabase instance needs explicit
  approval before any new schema is created.
- **Install dependencies just in time.**

## Decision gates

| Gate | Decision | Needed before | Where it stands |
|---|---|---|---|
| D1 | Universe: Israeli only, or US too. Which brokers and accounts. | 02, 05, 06 | **[open]** |
| D2 | Chart source: which one, at what cost (budget about $50–100 a month). | 06 | **[open]**, settled by unit 02 |
| D3 | Reuse of the older systems: own the positions or read them from bpp; FIFO. | 05, 19 | **[open]**, settled by unit 03 |
| D4 | Statistical figures per ticker; how a ticker's risk is measured; news yes or no. | 08, 09, 13 | **[open]**, settled by unit 01 |
| D5 | Delivery: how the investor receives the list. | 16 | **[open]** |
| D6 | Run schedule: time of day, day of week for the market mood. | 15 | **[open]** |

## Units

Statuses use: Planned / In progress / Complete YYYY-MM-DD.

### Phase A — Settle the ground (decisions and tests, no product code)

| # | Name | What it produces | Depends on | Status |
|---|------|------------------|------------|--------|
| 01 | Settle the blocking questions | Written answers to D1 and D4 (universe, statistical figures, how risk is measured, news yes/no, what the yes/no gate decides). Success criteria first draft. | — | Planned |
| 02 | Chart source test | A short test of candidate sources against the **real holdings**: coverage, history depth, quality for rarely traded items, cost, terms of use. Settles D2. **Desk research is already done** (2026-10-08, `docs/03-infrastructure/data-sources.md`: TASE price list, claim checks, alternatives); this unit is the hands-on part listed there under "Still to do". Do not redo the desk research. | D1 | Planned |
| 03 | Look at the older systems | `git pull` in bank-portfolio-pilot first. A short note of what to reuse, what to leave, and what changes (positions, FIFO, tables). Settles D3. | 01 | Planned |
| 04 | Approvals and architecture | Approval to create a new schema in the shared Supabase instance (or another decision). `context/architecture.md` and `docs/01-design/design-doc.md` filled in from what is settled. | 02, 03 | Planned |

### Phase B — Data foundation (Supabase and ingestion)

| # | Name | What it produces | Depends on | Status |
|---|------|------------------|------------|--------|
| 05 | Instruments and holdings | One master record per instrument (names, type, currency, intraday or daily-only) and the holdings with their purchases. | 04, D1, D3 | Planned |
| 06 | Chart ingestion | Daily, weekly and monthly charts for every holding; 4-hour and 1-hour only for exchange-traded ones. Every row dated "as of" so history is never rewritten. Checked against the live source. | 05, D2 | Planned |
| 07 | Market data ingestion | The index series (and anything that describes the market state) for the weekly read. | 04, D1 | Planned |
| 08 | Recommendations log and audit store | Tables that keep each day's stance and reason per ticker, the weekly market sentiment, the exact summary sheet sent to Claude, the prompt version and the answer. | 04 | Planned |

### Phase C — Calculations (all maths happens in Supabase)

| # | Name | What it produces | Depends on | Status |
|---|------|------------------|------------|--------|
| 09 | Ticker summary sheet | Per ticker: trend, key price levels, the chosen statistical figures. Fixed format. Checked against hand calculations. Check first whether SQL is enough for levels and RSI. | 06, D4 | Planned |
| 10 | Scanner (long charts) | Flags danger and opportunity zones from monthly, weekly and daily charts. | 09 | Planned |
| 11 | Fine-tune (short charts) | Looks at 4-hour and 1-hour charts, only for flagged exchange-traded tickers. | 10 | Planned |
| 12 | Market summary sheet | Weekly summary of the market data, in a fixed format. | 07 | Planned |

### Phase D — Claude (the thinking layer)

| # | Name | What it produces | Depends on | Status |
|---|------|------------------|------------|--------|
| 13 | Weekly market sentiment | Versioned prompt, fixed answer form (JSON), form check, and saved result with reasons. Tested on past weeks. | 08, 12 | Planned |
| 14 | Per-ticker stance | Versioned prompt and fixed answer form: hold, add, reduce or sell all, plus a reason. Reads the ticker sheet, the week's mood and yesterday's stance. Default is "no change". Long only, never a short. Tested on past days. | 08, 10, 11, 13, D4 | Planned |

### Phase E — Run it and prove it

| # | Name | What it produces | Depends on | Status |
|---|------|------------------|------------|--------|
| 15 | n8n workflows | The weekly run and the daily run, exported to git. Retry once, fall back to yesterday, alert if a run does not finish, never publish a half list. | 14, D6 | Planned |
| 16 | Delivery | The list of tickers with stance and reason reaches the investor. | 15, D5 | Planned |
| 17 | Quiet trial | Run for a set number of weeks with no action taken. Compare the advice with what the investor would have done. Judge it against the success criteria from unit 01. | 16 | Planned |

### Phase F — Later (parked on purpose)

These come after the single-ticker stage works. Order is not fixed.

| # | Name | What it produces | Depends on | Status |
|---|------|------------------|------------|--------|
| 18 | News per ticker | News as an input, if D4 says yes. May move earlier into Phase C and D. | D4 | Planned (conditional) |
| 19 | Portfolio view and amounts | The "how much": risk groups, target shares, the gap with a safe zone, cash, comparing tickers, money amounts. | 17 | Planned |
| 20 | Profit and loss by FIFO | Only if the advice or the investor needs it. May reuse earlier work from the older systems. | D3 | Planned (conditional) |
| 21 | Investor behaviour analysis | Postponed in the call. Only the data file is kept for now. | 17 | Planned (postponed) |

## Things to watch along the way

- **The chart source (unit 02) is the biggest unknown.** If it fails, the plan may need a different
  source, a smaller universe, or a different scanner. The desk research found no confirmed source
  yet for 4-hour and 1-hour charts of Israeli securities within the $50–100 a month budget
  (`docs/03-infrastructure/data-sources.md`).
- **Supabase is shared and read-only from here.** Nothing in Phase B starts without approval from unit 04.
- **Scanner in SQL.** If support and resistance or a standard RSI are too awkward in SQL, unit 09
  may need a different place to calculate. That is an architecture decision, not a quiet change.
- **Stance jumping.** If unit 17 shows the advice flipping too often, add rules in unit 14.
- **Early shortcuts.** A small thin run through all the phases on two or three tickers, before
  building everything wide, is an option. **[open]**

_(Every unit gets a spec file in `context/specs/NN-unit-name.md` when it starts. See
`context/specs/README.md`.)_
