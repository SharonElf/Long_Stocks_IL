# Data sources — research record (data foundation)

> **Checked 2026-10-08** (desk research, no accounts opened, nothing purchased).
> Purpose: so the research does **not** have to be redone. Read this first. Re-check only
> the items marked **volatile** or **not checked**, at the places named under
> "Where to look". The hands-on tests that are still needed are in "Still to do".
> Related: build plan unit 02 (chart source test), decision gate D2, `knowledge/REFERENCES.md`.

## 1. Bottom line

The pasted TASE research (`knowledge/2026-10-08-tase-data-research.md`) is **not usable as
written**. Its architecture idea is sound (daily history, weekly/monthly built from daily,
4h built from 1h). Its **cost and access assumptions do not hold**:

- The official TASE API for end-of-day history is a **paid monthly subscription**, not free.
- The "free 15-minute delayed prices on the website" and "sample them every 15 minutes" parts
  are **unverified**, and TASE sells the same delayed feed as a paid product.
- It covers ETFs only. Mutual funds and bonds, which the investor holds, were ignored.

No source has yet been **confirmed** to supply per-security 1h/4h candles for Israeli
securities at the budget ($50–100 a month, from the call).

## 2. Claim-by-claim result

| # | Claim in the pasted research | Result | Evidence (see section 6) |
|---|---|---|---|
| C1 | TASE sells an expensive intraday-history product (the "$820" one) | **Confirmed.** "Securities Intraday Quotes - Historical Data", $820 a month, API only. | S1 |
| C2 | Daily history is free or cheap from TASE | **Wrong for the official API.** Securities EoD: current data $100, five years back $250, ten years back $500 (USD a month, internal use, excl. VAT). | S1 |
| C3 | History is free on the TASE website | **Unverified.** Only a 2006 press release says free history from 2000. The current site could not be loaded (JavaScript only). Export options, security types covered, and limits are unknown. | S3 |
| C4 | The website shows 15-minute delayed prices free | **Unverified.** TASE sells the same thing as "Securities Prices - Online (15-minute delay)", $500 a month. | S1 |
| C5 | Sample the website every 15 minutes to build hourly candles | **Unverified and risky.** Terms of use could not be retrieved. bpp's own research flagged the site's internal API as ToS-unclear and fragile. TASE selling this feed makes tolerance of scraping less likely. Sampled candles are also wrong for rarely traded items (the research admits this). | S1, S6 |
| C6 | Weekly from daily, 4h from 1h, hourly volume from differences of cumulative volume | **Sound logic.** The volume trick needs a cumulative-volume field, whose availability was not verified. | — |
| C7 | (not in the research) Mutual funds and bonds | **Ignored by the research.** TASE "Mutual Funds Prices" is $250 a month. "Mutual Funds - Basic" is free but its contents are unknown. | S1 |
| C8 | Maya (מאיה) as a data site, from the call | **Not a price source.** On the price list, MAYA is the *market announcements feed* ($145 a month): company filings and announcements. Relevant to the news question, not to candles. | S1 |
| C9 | Funder (פאנדר), from the call | **Not checked at all.** | — |

## 3. TASE official API price list (2026) — the numbers

Source: S1. Prices are **USD per month, excluding VAT**, a monthly subscription ("Prices are
denominated in U.S dollars and are based on a monthly subscription").
Columns on the list: *internal use*, *internal use for a private client* (a business with
fewer than seven employees, or a private individual), *distribution*, and where it is
available (*Developer Portal API* and/or *data files sent by email, Excel/CSV*).

Extraction note: the PDF text came out scrambled, so numbers were assigned to columns by
their position on the page. Rows with two numbers (internal, distribution) are reliable.
Rows with a single number (marked †) could be in the internal or distribution column;
open the saved PDF to confirm before relying on them.

**Rows relevant to this project**

| Product | Internal | Distribution | API | Email files |
|---|---|---|---|---|
| Securities EoD - Current Data | 100 | 375 | yes | yes |
| Securities EoD - Five years back | 250 | 500 | yes | no |
| Securities EoD - Ten years back | 500 | 1,000 | yes | no |
| Securities Intraday Quotes - Historical Data | 820 † | — | yes | no |
| Securities Prices - Online (15-minute delay) | 500 † (sits in the distribution column) | | yes | no |
| Mutual Funds Prices | 250 | 250 | yes | yes |
| Mutual Fund Holdings | 375 | 750 | yes | no |
| TASE indices EoD - Current Data | 150 † | — | yes | yes |
| TASE indices EoD - Five years back | 250 † | — | yes | no |
| TASE indices EoD - Ten years back | 500 | 1,000 | yes | no |
| Derivatives EoD - Current Data | 75 | 200 | yes | no |
| Extended Bond Data | 50 | 150 | yes | no |
| Bond Amortization Schedule | 500 | 1,000 | yes | no |
| Payments and Corporate Events | 375 | 2,000 | yes | yes |
| Market Announcements feed "MAYA" | 145 | 290 | yes | no |

Not listed here (not relevant): short sales, interested parties, board and management,
"Smart Money" trading activity, index weights and parameters, OTC, company-website data.
The full list is in the saved PDF.

**Free products via the Developer Portal API** (internal use): Securities - Basic,
Mutual Funds - Basic, Indices - Basic, TASE indices online, Derivatives Data - Basic,
Lending Pool - Online Data, OTC Transactions Online, Public Offerings - Online,
TASE Trading and Vacation Schedules.

- What the free "Basic" products return is **not verified** (the docs are behind
  registration). A third-party Python SDK (`tasepy`, S4) wraps four free endpoints
  (Funds, Indices Basic, Indices Online, Securities Basic) and says it has **no
  end-of-day or historical endpoints**. Do not expect candles from the free tier.
- There is **no private-individual price** on the securities, funds or indices rows.

**Fit with the budget ($50–100 a month):** only "Securities EoD - Current Data" ($100)
reaches it, and that is the current day, not history. History starts at $250 a month.
Open question: can history be bought for **one month only** and then dropped? (Ask TASE.)

## 4. Alternatives (what is and is not verified)

| Source | Verified 2026-10-08 | Not verified (taken from bpp's June research, S6) |
|---|---|---|
| **EODHD** | Documents 70 exchanges "as of August 2026". Intraday API: 5-minute and 1-hour bars from October 2020 for "other exchanges", 1-minute "not guaranteed"; 1h history up to 7,200 days; intraday data is delayed and final 2–3 hours after close. Tel Aviv is **not named** in the intraday docs. Third-party pages show EODHD data for Tel Aviv stocks (`.TA`) and Israeli government bonds. | $19.99 a month for all exchanges. About 898 Israeli funds, with Morningstar-style IDs (`0P0000A7DZ.TA`), needing a one-time ID mapping. Bond coverage unknown. Free tier 20 calls a day. |
| **Twelve Data** | Tel Aviv (XTAE) is **end-of-day only** and needs the Pro plan (individual) or Venture (business). So no 1h/4h from here. | Earlier price of $66 a month ("Grow" plan); plan names have changed since. Fund ticker format unknown. |
| TradingView | Offers Tel Aviv data to users (delayed free, real time paid; TradingView blog, S5). | No external data API. bpp already receives 1d/4h/1h candles for **4 index tickers** from TradingView alerts (Pine script → n8n → Supabase), so alerts are a possible lead for per-security 1h/4h. Alert limits and plan cost for this are unknown. |
| Yahoo Finance, Stooq, Alpha Vantage, Financial Modeling Prep, Investing.com | — | bpp eliminated them (no Israeli funds or bonds, broken API, no confirmed Tel Aviv coverage, or scraping only). Yahoo `.TA` stocks and ETFs were not re-tested here. |
| market.tase.co.il internal API | — | bpp: undocumented, ToS unclear, could break any time. |

bpp's doc said TASE pricing was "not public". That is out of date: the public 2026 price
list above exists.

## 5. Not checked, and why

- The TASE website pages are JavaScript-rendered. The fetch tool saw only "Tase Site".
  So the website's real contents, export options, delay labels and **terms of use** were
  not read. Do this in a browser.
- The TASE Developer Portal documentation (field lists, rate limits, licence terms) is
  behind registration. `openapi.tase.co.il` did not resolve from this machine.
- EODHD's exchange symbol list needs an API token, so the Tel Aviv ticker count and the
  fund and ETF coverage were not counted.
- Funder (פאנדר): not looked at.
- Whether the investor's actual holdings are covered by any source: **not tested**.

## 6. Where to look (sources, with the date read)

| ID | What | URL |
|---|---|---|
| S1 | TASE Data Products Price List 2026 (saved: `knowledge/2026-10-08-tase-api-pricelist-2026.pdf`). The 2025 list is at `content.tase.co.il/media/tz1lzp1i/2001_api_pricelist_2025eng.pdf`. | https://content.tase.co.il/media/4imn13pz/2001_api_pricelist_2026_eng.pdf |
| S2 | TASE Data Hub product pages (JavaScript, redirects to the product lobby) | https://www.tase.co.il/he/content/products_lobby/datahub |
| S3 | 2006 press release on free website history from 2000 | https://mondovisione.com/news/tase-launches-new-website-for-the-first-time-all-trading-data-from-the-year-2000-2011124/ |
| S4 | `tasepy` (third-party Python SDK for the free TASE endpoints) | https://pypi.org/project/tasepy/ |
| S5 | TradingView blog on Tel Aviv data | https://www.tradingview.com/blog/en/tel-aviv-stock-exchange-data-is-now-available-to-everyone-16295 |
| S6 | bpp candle provider research, 2026-06-22 (local sibling repo, read-only) | `../bank-portfolio-pilot/docs/03-infrastructure/candle-provider-research.md` |
| S7 | EODHD intraday docs | https://eodhd.com/financial-apis/intraday-historical-data-api |
| S8 | Twelve Data exchange list | https://twelvedata.com/exchanges |

## 7. When to re-check (and what not to redo)

- **Do not redo** C1–C9 above or the section 4 findings unless one of the triggers below fires.
- **Volatile:** TASE prices (the file name carries the year, `2001_api_pricelist_<year>`;
  check each January or before subscribing), EODHD and Twelve Data plan names and prices.
- **Re-check when:** the holdings list or universe changes (D1), a provider is about to be
  chosen (unit 02), or the budget changes.
- If you find a newer price list, add a new dated section here and keep this one.

## 8. Still to do (hands-on, needs the investor or an account)

These settle decision gate D2 and are the real content of build plan unit 02.

1. **Register for a free TASE Data Hub account** and see what Securities - Basic and
   Mutual Funds - Basic actually return (any price fields? history?).
2. **Ask TASE:** can Securities EoD history be bought for one month only; do the licence
   terms ("internal use") cover a personal system.
3. **Read the TASE website terms of use** in a browser, and check what the public pages show
   (delay label, history length, export).
4. **Test EODHD's free tier** (20 calls a day) on the real holdings: an Israeli stock, an ETF,
   a mutual fund, a bond, and a 1-hour request on an Israeli ETF.
5. **Optionally** test the TradingView-alert route for 1h/4h on a few tickers.
6. Record the results here, as a new dated section, and then settle D2.
