# Docs

Knowledge base for the advisor. One subject per file; risk numbers live in `config/risk_limits.yaml`.

## Summary

It is possible to build a bot that uses what worked across the 9 funds studied, but not one that copies Alaska Black: that fund relies on judgment and on bets with no risk limits, which produced -57.2% in 2024, +67.6% in 2025 and a sharp drop in the post-election session of 26/10/2026.

- **What to copy:** value and quality selection (Atmos, Dynamo, Vokin), a 15-to-20-stock portfolio and a long horizon.
- **What to avoid:** bets that depend on the same factor (Alaska Black), illiquid positions (CTM) and years of underperformance without review (Tork, 3R Cedar II).
- **What the bot adds:** hard limits per stock, sector, liquidity and factor, a portfolio stop, and risk reduction before elections.

## Index

| File | Contents |
| --- | --- |
| `glossary.md` | Brazilian market terms kept in Portuguese |
| `research/methodology.md` | How the 9 funds were chosen and the research limitations |
| `research/alaska-black.md` | Alaska Black portfolio, phases and process (2016–Oct 2026) |
| `research/consistent-funds.md` | Atmos, Dynamo Cougar and Vokin |
| `research/recent-winners.md` | Infrad Master and Opportunity Ações |
| `research/failure-cases.md` | Tork, CTM and 3R Cedar II |
| `research/comparison.md` | The 9 funds side by side |
| `lessons.md` | Six patterns, and what becomes code vs. stays judgment |
| `strategy/specification.md` | Universe, selection, routine and technical architecture |
| `strategy/risk-limits.md` | Rationale for each risk limit |
| `strategy/market-intelligence.md` | News, historical events and probabilities |
| `strategy/backtest.md` | Backtest criteria and roadmap |
| `decisions/` | Architecture decision records |

Research done on 26/10/2026. Market data goes stale: check the date before using a number. Dates are written DD/MM/YYYY.

This is technical research material, not investment advice.
