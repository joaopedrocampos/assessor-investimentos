# Market intelligence layer

The bot acts as a long-term advisor: it does not try to guess events, it compares what the market is pricing with the actual probability and warns when risk is asymmetric. The 25/10/2026 election is the example: the market priced an opposition win, Lula won with 51.79% and the Ibovespa fell 13.88% the next day, with a circuit breaker ([InfoMoney](https://www.infomoney.com.br/mercados/ibovespa-hoje-bolsa-de-valores-ao-vivo-26102026/)).

## Principle: the AI reads and compares, the data provides the numbers

A language model has a knowledge cutoff and gets historical numbers wrong with confidence. So probabilities come from a database the bot queries (RAG), and the AI interprets, classifies and finds similar cases.

## The three layers

1. **Historical memory (event base):** every relevant event since 2002, with what the market expected, what happened and how the Ibovespa, dollar, interest-rate futures and sectors reacted at D+1, D+5 and D+30. Indexed with embeddings to retrieve analogous cases.
2. **Daily updates:** an agent collects news, economic data and moves by large investors, classifies events and updates the scenario view.
3. **Probabilistic reasoning:** scenarios with probabilities, compared with what is in the price (stocks, yield curve, option volatility). The output is alerts and suggestions within the risk limits.

## Events for the historical base

| Type | Examples |
| --- | --- |
| Presidential elections | 2002, 2006, 2010, 2014, 2018, 2022, 2026 |
| Political crises | Impeachment (2016), Joesley Day (2017) |
| External shocks | 2008 crisis, pandemic (2020), US tariffs (2025), Middle East war (2026) |
| Monetary policy | Selic hiking and cutting cycles, surprise Copom decisions |
| Fiscal | Changes to the fiscal framework, spending packages |

## Daily data sources

| Category | Sources |
| --- | --- |
| News | RSS and APIs from Valor, InfoMoney, Reuters, Bloomberg Línea |
| Companies | Fatos relevantes and financial statements at the CVM (open data, DFP/ITR) |
| Economy | Central Bank (Selic, Boletim Focus, SGS series), IBGE (IPCA, GDP), B3 yield curve |
| Large investors | Fund portfolios at the CVM, managers' monthly letters, US 13F filings |
| Expectations | Election polls, prediction markets, analyst consensus |
| Prices | Ibovespa, dollar, country risk (CDS), option implied volatility |

## What the advisor delivers

- **Weekly summary:** base scenario, main risks, the week's agenda and likely effect on the portfolio.
- **Alerts:** when a relevant event happens or when the gap between price and probability gets large.
- **Adjustment suggestions:** always within the risk limits, with the reason and the historical cases used.
- **Human approval:** no order goes out without João's approval.

Report language is set in `config/advisor.yaml`.

## Calibration and limits

- **Prediction log:** every probability given is stored and later compared with what happened (Brier score). If the bot's "70%" calls do not happen close to 70% of the time, it is not calibrated.
- **Few examples:** only 7 presidential elections since 2002. Probability ranges will be wide.
- **Regime change:** rates, foreign flows and rules change between cycles. Older cases count for less.
- **Markets react to surprise:** what moves the price is the gap between the outcome and what was already priced, not the event itself.
