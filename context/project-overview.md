# Long Stocks IL — "ניהול מסחר" (trading management)

> **Status: configured, not yet planned.** This file records what was *stated*
> (2026-10-08 call, `knowledge/2026-10-08-sharon-einat-call-summary.md`).
> Anything marked **[open]** is undecided and belongs to the planning session.
> Nothing here is a design.

## Overview

A long-term trading system for a single investor: hold positions over the long
term and know **when to add, when to reduce, when to replace**. It sits between
two existing systems — more sophisticated than `bank-portfolio-pilot` (portfolio
direction from index candles and macro news), and long-horizon where
`trading-copilot-brain` is short-term intraday. Closely related to the Israeli
bank side (bpp). See `knowledge/REFERENCES.md` for what already exists.

## Goals (as stated)

1. Know the positions: what is held, where, how much.
2. Have price data per ticker (candle tables) from a transparent, reliable source.
3. Decide when to increase / reduce / replace a position.
4. Know profit and loss by FIFO.

## The six areas (as stated — not yet turned into units)

1. **Position data** — what is held, where, how much.
2. **Ticker data** — price/candle tables; the challenge is finding a transparent
   data source. Daily candles needed, especially for Israeli securities
   (funds, ETFs/תעודות סל); weekly and monthly candles to be added.
3. **Yes/No gate algorithm.**
4. **Scanner algorithm** — raises a flag (danger / opportunity zone) on large
   timeframes: monthly, weekly, daily.
5. **Fine-tune algorithm** — runs *only after* the scanner flags, on 4-hour and
   1-hour timeframes. The split is deliberate: it keeps noise out of decisions.
6. **Profit & Loss by FIFO** — described as technical and already developed in the past.

## Stated constraints

- Data budget: willing to pay a subscription of about **$50–100/month** if needed.
- Sites previously noted for data: Funder (פאנדר), Maya (מאיה, TASE).
- Behavioral analysis of the trader is **deferred**; the aim for now is an
  all-inclusive data file, not deciding what to do with it.

## Scope

### In scope (stated)
- The six areas above.

### Out of scope / inherited defaults — **[open] confirm in planning**
- No automated order execution (recommendations only) — inherited from both neighbors.
- **Long positions only, no shorts ever — decided 2026-10-08.**
- Whether US holdings are in scope (the project name says IL; the held portfolio is mixed) — **[open]**.

## Success criteria

**[open]** — to be written in the planning session.
