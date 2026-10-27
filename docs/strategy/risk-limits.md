# Risk limits: why each one exists

The numbers live in `config/risk_limits.yaml`; this file holds the rationale. Over a 20-year horizon, surviving large drawdowns matters more than picking the best stock: after -57%, it takes +133% just to get back to even.

| Rule (YAML key) | Lesson it comes from |
| --- | --- |
| `portfolio.min_stocks` / `portfolio.max_stocks` | Consistent funds hold about 20 stocks |
| `position.max_weight_per_stock` | Alaska (up to 16% in one stock), CTM (≈ 40%) |
| `position.max_weight_per_sector` | Infrad, Alaska (retail and education) |
| `liquidity.*` | CTM froze redemptions holding illiquid stocks |
| `volatility.max_annual_target` | Alaska and 3R Cedar II swung too much |
| `drawdown.*` | Alaska (-57% in 2024), 3R Cedar II |
| `factors.max_exposure_domestic_rate_sensitive` | Alaska in 2024 and on 26/10/2026 |
| `factors.reduce_before_elections` | Alaska in 2026: drops in May and after the election |
| `portfolio.fixed_income_reserve_min` / `portfolio.fixed_income_reserve_max` | Opportunity keeps about 15% in government bonds |
| `underperformance.*` | Tork and 3R Cedar II spent years below without review |
| `universe.allow_options` / `universe.allow_leverage` / `universe.allow_bdr` | Alaska used derivatives without limits and lost on every front in 2024 |
| `universe.max_net_debt_to_ebitda` | Vokin and the quality filters of the consistent funds |
| `execution.*` | The bot is an advisor; João makes the decisions |

## How to change a limit

1. Run the backtest with the new and the old value.
2. Change the YAML and, if the rationale changes, this table, in the same commit.
3. Record the reason and the backtest result in the commit message.
