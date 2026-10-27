# Recent winners: Infrad Master and Opportunity Ações

Infrad looks like a thematic bet that paid off hugely in one year; Opportunity looks like a consistent process that only matched the index in 2025. Being one year's champion says little about the next. Research as of 26/10/2026.

| Year | Infrad Master | Opportunity Ações | Ibovespa |
| --- | --- | --- | --- |
| 2021 | did not exist | -0.4% | -11.9% |
| 2022 | did not exist | -17.0% | +4.7% |
| 2023 | +18.6% to +25.6% (from Sep) | +45.9% | +22.3% |
| 2024 | -8.3% | +26.8% | -10.4% |
| 2025 | +79.9% | +35.7% | +34.0% |
| 2026 (to Oct) | +32.3% | not confirmed | +26.7% |

Sources: [ETFs Brasil – Infrad](https://www.etfsbrasil.com.br/fundos/52085530000183), [Gorila – Opportunity](https://gorila.com.br/produtos-de-investimento/fundos/opportunity-acoes-fia-bdr-nivel-i), [Mais Retorno – Ibovespa](https://maisretorno.com/indice/ibov). Sources disagree in some years (Gorila shows Infrad 2025 at +70%).

## Infrad Master (Radar Gestora)

- **Thesis:** infrastructure focus, with only 3 years of history (first NAV Sep/2023). Topped the 2025 ranking ([BP Money](https://bpmoney.com.br/?p=388914)).
- **Risk:** volatility of 26–27% a year vs 19.5% for the Ibovespa. Largest drawdown 21.8%, and -13.1% in May 2026 alone.
- **Skill or timing:** beat the index by 2 points in 2024, 46 points in 2025 and 5.6 points in 2026. Almost all the edge came from one year. The stock-level portfolio was not found.

## Opportunity Ações

- **Thesis:** utilities and education, with significant stakes in PetroReconcavo, Alupar and Equatorial ([InvestNews](https://investnews.com.br/negocios/movimentos-do-opportunity-daniel-dantas/amp/)).
- **Allocation (Sep/26):** 33.9% abroad, 28.9% in local stocks, 14.7% in government bonds, 8% in BDRs ([Mais Retorno](https://maisretorno.com/fundo/opportunity-acoes-fif-acoes-rl/carteira)). The foreign diversification and the fixed-income slice reduce risk.
- **Skill or timing:** history since 2017; beat the index in 2021, 2023 and 2024 and lost in 2022. In 2025 the standout was size (R$ 22 bi), not return.

## Lessons for the bot

- **Thematic cap:** no sector or theme above a fixed ceiling. A theme can return 80% in a year and drop 13% in a month.
- **Volatility target:** if portfolio volatility exceeds the target, the bot shrinks positions.
- **Reserve:** keep a fixed fixed-income slice, like Opportunity's ~15% in government bonds.
- **Judge the average, not the best year:** in the backtest, compare against the Ibovespa year by year.
- **Human judgment:** choosing the theme and reading regulation and politics, which decide outcomes in infrastructure.
