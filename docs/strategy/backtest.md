# Backtest plan

The strategy should only get real money if it passes the backtest across good and bad periods, including 2015, 2020, 2024 and the 26/10/2026 session.

## Criteria

- **Period:** 2012 to 2026, covering recession (2015–16), pandemic (2020), high rates (2024) and elections (2014, 2018, 2022, 2026).
- **No survivorship bias:** include stocks that delisted or went bankrupt (e.g. Americanas, Oi) on the dates they existed.
- **No look-ahead:** use only financial statements already published at each date, respecting the disclosure lag.
- **Real costs:** brokerage, exchange fees, spread and tax.
- **Benchmarks:** Ibovespa, CDI and Alaska Black itself.
- **Metrics:** annual return, max drawdown, recovery time, volatility, Sharpe ratio and share of 3-year windows above the Ibovespa.
- **Robustness:** vary parameters (10 or 20 stocks, 8% or 12% cap) and check the result does not hinge on fine-tuning.

## Roadmap

- [ ] Choose the data source and build the price and financials base since 2012
- [ ] Implement the risk filters reading `config/risk_limits.yaml` (with tests)
- [ ] Implement the selection score
- [ ] Run the backtest and tune the limits
- [ ] Build the historical event base (`market-intelligence.md`)
- [ ] Confirm the non-resident account and MetaTrader 5 access with the broker
- [ ] Run 3 months on a demo account with manual order approval
- [ ] Start with a small amount and scale only if live behavior matches the backtest
