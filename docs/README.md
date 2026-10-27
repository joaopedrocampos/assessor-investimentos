# Documentação

Base de conhecimento do assessor. Cada arquivo cobre um assunto; os números de risco ficam em `config/risk_limits.yaml`.

## Resumo

Dá para construir um bot que aproveite o que funcionou em 9 fundos estudados, mas não um que copie o Alaska Black: o fundo depende de julgamento e de apostas sem limite de risco, que geraram -57,2% em 2024, +67,6% em 2025 e uma queda forte no pregão pós-eleição de 26/10/2026.

- **O que copiar:** seleção por valor e qualidade (Atmos, Dynamo, Vokin), carteira de 15 a 20 ações e horizonte longo.
- **O que evitar:** apostas que dependem do mesmo fator (Alaska Black), posições ilíquidas (CTM) e anos seguidos de subdesempenho sem revisão (Tork, 3R Cedar II).
- **O que o bot acrescenta:** limites rígidos por ação, setor, liquidez e fator, stop da carteira e redução de risco antes de eleições.

## Índice

| Arquivo | Conteúdo |
| --- | --- |
| `pesquisa/metodologia.md` | Como os 9 fundos foram escolhidos e as limitações da pesquisa |
| `pesquisa/alaska-black.md` | Carteira, fases e processo do Alaska Black (2016–out/2026) |
| `pesquisa/fundos-consistentes.md` | Atmos, Dynamo Cougar e Vokin |
| `pesquisa/campeoes-recentes.md` | Infrad Master e Opportunity Ações |
| `pesquisa/casos-de-erro.md` | Tork, CTM e 3R Cedar II |
| `pesquisa/comparativo.md` | Os 9 fundos lado a lado |
| `licoes.md` | Seis padrões e o que vira código ou fica no julgamento |
| `estrategia/especificacao.md` | Universo, seleção, rotina e arquitetura técnica |
| `estrategia/limites-de-risco.md` | Justificativa de cada limite de risco |
| `estrategia/inteligencia-de-mercado.md` | Notícias, eventos históricos e probabilidades |
| `estrategia/backtest.md` | Critérios de backtest e próximos passos |
| `decisoes/` | ADRs com as decisões de arquitetura |

Pesquisa feita em 26/10/2026. Dados de mercado envelhecem: confira a data antes de usar um número.

Este material é uma base técnica para pesquisa, não recomendação de investimento.
