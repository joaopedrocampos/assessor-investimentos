# Lessons

The bot should copy the selection discipline of the consistent funds and avoid what hurt Alaska Black most: the absence of risk limits. Six patterns show up across the sample (details in `research/`).

1. **Correlation is the hidden risk.** Alaska Black lost 57% in 2024 because stocks, options, FX and rates all depended on the same scenario. Measuring factor exposure (rates, dollar, domestic consumption) matters more than counting stocks.
2. **Cap the damage of each mistake.** Atmos states its worst pick never cost more than 2% of the portfolio. That is a per-position risk limit, not a weight limit.
3. **Liquidity decides whether you can get out.** CTM froze redemptions with almost 40% in one illiquid stock. Each position's size must fit the traded volume.
4. **Even the best have bad years.** Dynamo, Atmos and Vokin spent 2 to 5 years below the index. The bot must survive that without blowing up and without being switched off at the worst moment.
5. **One good year proves nothing.** Infrad beat the index by 46 points in 2025 and by little in other years. Evaluate strategies across several periods.
6. **Long underperformance calls for review.** Tork and 3R Cedar II spent years below without changing course.

## What becomes code and what does not

| Codifiable | Requires judgment |
| --- | --- |
| Liquidity and market-cap filters | Quality of company management |
| Valuation filters (P/E, EV/EBITDA, margin of safety) | Fair value of each company (discounted cash flow) |
| Quality filters (ROIC, net debt/EBITDA) | Whether a drop is market overreaction or a broken thesis |
| Caps per stock, sector and factor | Reading the political and regulatory scenario |
| Portfolio drawdown stop and volatility target | When to hedge with dollars or rates |
| Risk reduction before scheduled events (elections) | Choosing themes such as infrastructure |
| Periodic rebalancing | Strategy changes |

An AI agent reading financial statements, letters and news can support the judgment side, but the final call on changing rules stays with João.
