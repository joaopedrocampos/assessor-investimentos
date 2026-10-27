# Bot specification

The bot is a value-and-quality strategy with 15 to 20 B3 stocks, monthly rebalancing and hard risk limits that Alaska Black lacks. All numbers are starting points for the backtest, not proven values. Limit values live in `config/risk_limits.yaml`.

## Stock universe

- B3 stocks above the minimum average daily volume and market cap set in `config/risk_limits.yaml`.
- No BDRs, options or leverage in the first version.

## Selection (monthly score)

Each stock gets a 0–100 score combining:

| Criterion | Measure | Starting weight |
| --- | --- | --- |
| Value | P/E, EV/EBITDA and dividend yield, relative to sector | 40% |
| Quality | ROIC, margin and earnings stability | 35% |
| Financial health | Net debt/EBITDA below the cap (banks excluded) | 15% |
| Momentum | 12-month return excluding the last month | 10% |

The bot suggests the top scores that pass the risk limits (`risk-limits.md`).

## Routine

1. **Daily:** update prices, check the portfolio stop and limits. Sells off-schedule only if a limit is breached.
2. **Monthly:** recompute scores, build the target portfolio and the order list.
3. **Approval:** João approves orders before they are sent.
4. **Execution:** limit orders, split into parts when the position is large relative to volume.
5. **Logging:** every decision is stored with its reason, for audit and so the agent can explain what it did.

## Technical architecture

| Component | Suggested option |
| --- | --- |
| Market and fundamentals data | brapi.dev or yfinance; CVM open data (DFP/ITR) for financial statements |
| Storage | PostgreSQL or SQLite with price and fundamentals history |
| Strategy engine | Python (pandas), rules read from `config/` |
| Backtest | vectorbt or backtrader |
| Execution | MetaTrader 5 through a Brazilian broker, official `MetaTrader5` library |
| Scheduling | cron or AWS Lambda + EventBridge |
| Agent layer | LLM that reads letters, fatos relevantes and news and flags risks for review; never sends orders on its own (`market-intelligence.md`) |
| Alerts | Email or Telegram for orders, breached limits and stop |

## Open regulatory question

João lives in Germany. Confirm with the broker whether he can trade on B3 as a non-resident (Resolução 4.373), and with an accountant how taxation works in both countries.
