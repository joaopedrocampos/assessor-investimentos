# Failure cases: Tork, CTM and 3R Cedar II

The three failed in different ways: Tork through mediocre results without scale, CTM through illiquidity and 3R Cedar II through large, repeated losses. All three left visible signs in public data before the outcome. Research as of 26/10/2026.

| Fund | Outcome | What went wrong | Warning sign visible beforehand |
| --- | --- | --- | --- |
| [Tork Capital](https://braziljournal.com/tork-capital-fecha-fundos-em-meio-a-ambiente-hostil-para-gestores-de-acoes/) | Manager shut down in Apr/2026 with about R$ 600 mi | Years in the 3rd and 4th quartiles vs peers; insufficient assets; new products raised under R$ 20 mi | Bad quartile over 12 to 60 months; -25% in 2021 vs -12% for the Ibovespa |
| [CTM Investimentos](https://www.infomoney.com.br/?p=2194998) | Three funds closed to redemptions on 23/07/2023 | About 39.7% of CTM Estratégia in a single illiquid stock (Energisa MT); 20.56% stake in Mobly | Concentration and stakes above 20% were already visible in CVM portfolio data |
| [3R Cedar II LB](https://gorila.com.br/produtos-de-investimento/fundos/3r-cedar-ii-lb-fia) | Assets fell below R$ 1 mi in 2026 | Three straight years far below the index (-10.8% in 2023, -24.6% in 2024, -8.7% in 2025 with the Ibovespa at +34%) | Among the 10 worst over every period by early 2025 ([survey](https://bpmoney.com.br/?p=346930)) |

At CTM, the manager proposed moving about 38% of CTM Hedge, in illiquid stocks, into a closed fund lasting up to 2 years ([InfoMoney](https://www.infomoney.com.br/?p=2201503)). The outcome of the 14/08/2023 shareholder meeting was not confirmed.

Tork is a different case: [Tork FC FIA](https://gorila.com.br/produtos-de-investimento/fundos/tork-fc-de-fia) beat the Ibovespa in most years between 2019 and 2025. The problem was trailing peers and lacking the scale to keep the firm running. A bot managing its owner's money has no such business risk, but the lesson about prolonged underperformance holds.

## Rules that would have reduced the damage

- **Per-stock cap:** CTM had almost 40% in one name.
- **Liquidity limit:** every position must be exitable in a few sessions using a fraction of average daily volume.
- **Portfolio drawdown stop:** cut exposure and ask for human review after a large drop from peak.
- **Underperformance review:** pause new buys if the strategy falls well below the Ibovespa over 12 months.
- **Volatility filter:** avoid swings like 3R Cedar II's +80% and -22%.

Current values for these limits are in `config/risk_limits.yaml`.
