# Casos de erro: Tork, CTM e 3R Cedar II

Os três falharam de formas diferentes: a Tork por resultado mediano sem escala, a CTM por iliquidez e o 3R Cedar II por quedas grandes e repetidas. Os três deixaram sinais visíveis em dados públicos antes do desfecho. Pesquisa de 26/10/2026.

| Fundo | Desfecho | O que deu errado | Sinal de alerta visível antes |
| --- | --- | --- | --- |
| [Tork Capital](https://braziljournal.com/tork-capital-fecha-fundos-em-meio-a-ambiente-hostil-para-gestores-de-acoes/) | Gestora fechou em abr/2026 com cerca de R$ 600 mi | Anos no 3º e 4º quartis contra outros fundos; patrimônio insuficiente; produtos novos captaram menos de R$ 20 mi | Quartil ruim em 12 a 60 meses; -25% em 2021 contra -12% do Ibovespa |
| [CTM Investimentos](https://www.infomoney.com.br/?p=2194998) | Três fundos fechados para resgate em 23/07/2023 | Cerca de 39,7% do CTM Estratégia em uma só ação ilíquida (Energisa MT); 20,56% de participação na Mobly | Concentração e participações acima de 20% já apareciam nas carteiras da CVM |
| [3R Cedar II LB](https://gorila.com.br/produtos-de-investimento/fundos/3r-cedar-ii-lb-fia) | Patrimônio caiu para menos de R$ 1 mi em 2026 | Três anos seguidos muito abaixo do índice (-10,8% em 2023, -24,6% em 2024, -8,7% em 2025 com o Ibovespa a +34%) | Entre os 10 piores em todos os períodos já no início de 2025 ([levantamento](https://bpmoney.com.br/?p=346930)) |

No caso da CTM, a gestora propôs isolar cerca de 38% do CTM Hedge em ações ilíquidas num fundo fechado de até 2 anos ([InfoMoney](https://www.infomoney.com.br/?p=2201503)). O resultado da assembleia de 14/08/2023 não foi confirmado.

A Tork é um caso diferente: o [Tork FC FIA](https://gorila.com.br/produtos-de-investimento/fundos/tork-fc-de-fia) bateu o Ibovespa na maioria dos anos entre 2019 e 2025. O problema foi ficar atrás dos concorrentes e não ter escala para manter a gestora. Para um bot que opera dinheiro próprio, esse risco de negócio não existe, mas a lição sobre subdesempenho prolongado vale.

## Regras que teriam reduzido o dano

- **Limite por ação:** a CTM tinha quase 40% num papel.
- **Limite de liquidez:** cada posição precisa poder ser zerada em poucos pregões usando uma fração do volume médio diário.
- **Stop de drawdown da carteira:** reduzir exposição e pedir revisão humana após queda grande desde o pico.
- **Revisão por subdesempenho:** pausar novas compras se a estratégia ficar muito abaixo do Ibovespa em 12 meses.
- **Filtro de volatilidade:** evitar oscilações como o +80% e -22% do 3R Cedar II.

Os valores atuais desses limites estão em `config/risk_limits.yaml`.
