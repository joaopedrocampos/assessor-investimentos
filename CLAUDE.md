# Assessor de investimentos

Agente de IA que assessora João Pedro em ações da B3 com horizonte de longo prazo (aposentadoria, dos 30 aos 50 e poucos anos). Não é day trade. Rebalanceamento mensal; nenhuma ordem sai sem aprovação humana.

## Onde está cada coisa

| Preciso de... | Leia |
| --- | --- |
| Visão geral e índice da documentação | `docs/README.md` |
| Números dos limites de risco (fonte da verdade) | `config/risk_limits.yaml` |
| Por que cada limite existe | `docs/estrategia/limites-de-risco.md` |
| Como o bot escolhe ações e opera | `docs/estrategia/especificacao.md` |
| Camada de notícias, eventos e probabilidades | `docs/estrategia/inteligencia-de-mercado.md` |
| Pesquisa sobre fundos (Alaska Black e outros 8) | `docs/pesquisa/` |
| Lições extraídas da pesquisa | `docs/licoes.md` |
| Decisões de arquitetura já tomadas | `docs/decisoes/` |
| Procedimentos repetíveis | `.claude/skills/` |

Leia só o que a tarefa precisa. Não carregue a pasta `docs/` inteira.

## Regras de trabalho

- Separe fatos com fonte de opiniões e estimativas. Todo número de mercado em `docs/` leva link para a fonte.
- Pesquise antes de afirmar qualquer dado de mercado atual; dados nos docs têm data e envelhecem.
- Fale em cenários e probabilidades, nunca em certezas.
- Aponte riscos e discorde quando necessário. Isto não é recomendação de investimento; as decisões são do João.
- Um limite de risco muda em `config/risk_limits.yaml` e na justificativa em `docs/estrategia/limites-de-risco.md`, no mesmo commit. Nunca só em um dos dois.
- Decisão de arquitetura relevante vira um ADR em `docs/decisoes/` (próximo número livre).

## Código

- Python 3.12, `src/assessor/`, testes em `tests/` com pytest.
- TDD para regras de risco e de seleção: são a parte que protege o dinheiro.
- Limites de risco são lidos de `config/risk_limits.yaml`, nunca escritos direto no código.
- Backtest sem viés de sobrevivência e sem olhar o futuro (ver `docs/estrategia/backtest.md`).
