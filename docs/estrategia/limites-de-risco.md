# Limites de risco: por que cada um existe

Os números ficam em `config/risk_limits.yaml`; este arquivo guarda a justificativa. Para um horizonte de 20 anos, sobreviver às quedas grandes importa mais que escolher a melhor ação: depois de -57%, é preciso +133% só para voltar ao ponto de partida.

| Regra (chave no YAML) | Lição de origem |
| --- | --- |
| `posicao.peso_max_por_acao` | Alaska (até 16% numa ação), CTM (≈ 40%) |
| `posicao.peso_max_por_setor` | Infrad, Alaska (varejo e educação) |
| `liquidez.*` | CTM travou resgates com ações ilíquidas |
| `volatilidade.alvo_anual_max` | Alaska e 3R Cedar II oscilaram demais |
| `drawdown.*` | Alaska (-57% em 2024), 3R Cedar II |
| `fatores.exposicao_max_sensivel_juros_domesticos` | Alaska em 2024 e em 26/10/2026 |
| `fatores.reduzir_antes_de_eleicoes` | Alaska em 2026: quedas em maio e no pós-eleição |
| `carteira.reserva_renda_fixa_min` / `carteira.reserva_renda_fixa_max` | Opportunity mantém cerca de 15% em títulos públicos |
| `subdesempenho.*` | Tork e 3R Cedar II ficaram anos abaixo sem revisão |
| `universo.permite_opcoes` / `permite_alavancagem` | Alaska usa derivativos sem limite e perdeu em todas as frentes em 2024 |
| `execucao.aprovacao_humana_obrigatoria` | O bot é assessor; as decisões são do João |

## Como mudar um limite

1. Rodar o backtest com o valor novo e com o antigo.
2. Alterar o YAML e, se a justificativa mudar, esta tabela, no mesmo commit.
3. Registrar no commit o motivo e o resultado do backtest.
