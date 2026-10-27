# Especificação do bot

O bot é uma estratégia de valor e qualidade, com 15 a 20 ações da B3, rebalanceamento mensal e limites de risco rígidos que o Alaska Black não tem. Todos os números são pontos de partida para o backtest, não valores comprovados. Os valores dos limites estão em `config/risk_limits.yaml`.

## Universo de ações

- Ações da B3 acima do volume médio diário e do valor de mercado mínimos definidos em `config/risk_limits.yaml`.
- Sem BDRs, opções ou alavancagem na primeira versão.

## Seleção (pontuação mensal)

Cada ação recebe uma nota de 0 a 100 combinando:

| Critério | Medida | Peso inicial |
| --- | --- | --- |
| Valor | P/L, EV/EBITDA e dividend yield, comparados com o setor | 40% |
| Qualidade | ROIC, margem e estabilidade dos lucros | 35% |
| Saúde financeira | Dívida líquida/EBITDA abaixo do teto (exceto bancos) | 15% |
| Momento | Retorno de 12 meses excluindo o último mês | 10% |

O bot sugere as melhores notas que passarem nos limites de risco (`limites-de-risco.md`).

## Rotina

1. **Diário:** atualizar preços, checar stop da carteira e limites. Só vende fora do calendário se um limite for violado.
2. **Mensal:** recalcular notas, gerar a carteira-alvo e a lista de ordens.
3. **Aprovação:** o João aprova as ordens antes do envio.
4. **Execução:** ordens limitadas, divididas em partes quando a posição for grande para o volume.
5. **Registro:** cada decisão fica gravada com o motivo, para auditoria e para o agente explicar o que fez.

## Arquitetura técnica

| Componente | Opção sugerida |
| --- | --- |
| Dados de mercado e fundamentos | brapi.dev ou yfinance; dados abertos da CVM (DFP/ITR) para balanços |
| Armazenamento | PostgreSQL ou SQLite com histórico de preços e fundamentos |
| Motor de estratégia | Python (pandas), regras lidas de `config/` |
| Backtest | vectorbt ou backtrader |
| Execução | MetaTrader 5 via corretora brasileira, biblioteca oficial `MetaTrader5` |
| Agendamento | cron ou AWS Lambda + EventBridge |
| Camada de agente | LLM que lê cartas, fatos relevantes e notícias e sinaliza riscos para revisão; não envia ordens sozinho (`inteligencia-de-mercado.md`) |
| Alertas | E-mail ou Telegram para ordens, limites violados e stop |

## Pendência regulatória

O João mora na Alemanha. Confirmar com a corretora se é possível operar na B3 como não residente (Resolução 4.373) e com um contador como fica a tributação nos dois países.
