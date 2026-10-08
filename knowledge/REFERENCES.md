# References — material that lives in other repos

Pointers only, nothing is copied. Paths are relative to the sibling folders in
`c:\Users\dell\Documents\GitHub\`. Checked 2026-10-08. Read the live file, not a
remembered summary. If a pointer breaks, fix it here.

## Sibling repos

| Repo | Local folder | Status when checked | Use for |
|---|---|---|---|
| bank-portfolio-pilot (bpp) | `bank-portfolio-pilot` | ⚠️ **Local checkout is stale**: HEAD `8d7ce5c` (2026-06-22). GitHub `main` is `40c1516` (2026-09-22) and holds Units 04–13 (signal engine, candles, scheduler, macro/geo flows). **`git pull` there before reading.** | Positions, ledger/FIFO, IL signal engine, candle research |
| trading-copilot-brain | `trading-copilot-brain-22092026` | Up to date, `main` @ `284bdd0` (2026-10-08) | Candle pipeline, algorithms, Schwab FIFO P&L, research method (short-term, US, long-only) |
| Claude-Code-Project-Configuration | `Claude-Code-Project-Configuration` | Template library | Methodology; this repo was cloned from `1-the-template/` |
| hunt-app | `hunt-app` | Running | Trader UI reference only (Electron cockpit for the brain) |

Not relevant: `AditaGoldPowerBi`, `invoice-inbox-project`, `trading-copilot-brain_13072026` (older brain clone).

Shared infrastructure: bpp and the brain use the **same Supabase instance** (`oqsdcxmtvymfuczmgvha`, schemas `public`, `bcmagic`, `bpp`; brain's Spec 136 adds `schwab`). The Supabase MCP in Claude Code reaches it.

## By area (the six areas from the 2026-10-08 call)

### 1. Position data — what is held, where, how much
- bpp: `context/specs/01-supabase-schema.md`, `03-holdings-reconciler.md`, `04-transaction-ingest-v2.md`, `05-holdings-refresh.md`; `context/architecture.md` (schema, invariants, action types); `supabase/migrations/005–010*.sql`; `data/ticker_mapping_import.csv`; `samples/` (one real export per broker); `docs/05-execution/open-issues.md` (27 known issues).
- Live (bpp schema, 2026-10-08): 7 accounts, 78 holdings rows, 74 lots, 991 transactions, 405 broker snapshots, 39 ticker mappings. Held mix: ~12 TASE mutual funds, 2 bonds, ~20 other TASE instruments, ~30 US stocks/ETFs, 1 option.

### 2. Ticker data — prices and candles
- bpp: `docs/03-infrastructure/candle-provider-research.md` (providers compared, costs, eliminated list); `context/progress-tracker.md` → "Resolved → Candle provider decision (2026-06-25)"; `context/specs/10-candle-push-receiver.md` and `12-candle-expansion.md` (TradingView Pine alert → n8n → `bpp.candles`); `candles/` (raw TradingView exports).
- Live (`bpp.candles`, 2026-10-08): only **4 index tickers** (TA125, TA35, TA90, TABANK) × 1d/4h/1h, source TradingView. No per-security candles exist anywhere yet. 1h/4h history expires (~7 weeks / ~5 months) unless refreshed.
- brain: `context/reference/supabase-schema.md` (candles / candles_historical / candles_complete; `build_higher_tf_for_ticker`, `calculate_indicators_candles`); `context/reference/process-flows.md` §3 (candle pipeline); `code_utils/candle_fetch.py`.
- This repo: `knowledge/2026-10-08-tase-data-research.md` (hybrid TASE daily + sampled 15-min idea — unverified).

### 3–5. Algorithms — yes/no gate, scanner, fine-tune
- brain (short-term, but the closest worked example of a gate/scanner/refine pipeline): `context/reference/pipeline.md`, `rulebook.md`, `strategy-library.md`; `code_agents/trend_hierarchy.py`, `code_utils/level_calculator.py`, `pattern_detector.py`, `regime.py`.
- bpp (long-term, Claude-driven): `signal_engine/claude_caller.py` (prompts), `candle_digest.py`, `data_loader.py`; `context/specs/09-signal-engine.md`, `13-signal-engine-improvements.md`. Live: 123 signal runs, 2026-06-25 → 2026-10-08, output ADD / HOLD / REDUCE / SELL.
- Macro/geo context feeding bpp signals: `flows/IL Macro Intelligence.json`, `flows/IL Geopolitical Intelligence.json`; tables `bpp.il_macro`, `bpp.il_geopolitical` (77 rows each).

### 6. P&L by FIFO
- brain: `context/specs/136-schwab-fifo-trade-engine.md` — the "FIFO, already built" piece, and it addresses the exact Schwab file problems raised on the call (no fill times, no reference number; merges Transactions + Order Status files). Check the spec's status block before relying on it.
- bpp: `bpp.lots`, `bpp.lot_allocations`, `bpp.link_sell_to_lots()`, view `bpp.trades` (IL brokers). Live: `lot_allocations` has **0 rows** on 2026-10-08, so realized P&L has not been produced yet there — verify.

### Research method
- brain: `research/RESEARCH-RUNBOOK.md` (Hebrew; reusable recipe for external-research rounds; the 2026-08-22 payload in that folder is crypto/US market data, not reusable here).

## Skills elsewhere that touch this domain
- `/run_il_banks` (global skill, source in brain `docs/13-skills/`) fires the bpp holdings-refresh webhook.
