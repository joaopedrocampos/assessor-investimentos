# Plano de backtest

A estratégia só deve receber dinheiro real se passar no backtest em períodos bons e ruins, incluindo 2015, 2020, 2024 e o pregão de 26/10/2026.

## Critérios

- **Período:** 2012 a 2026, cobrindo recessão (2015–16), pandemia (2020), juros altos (2024) e eleições (2014, 2018, 2022, 2026).
- **Sem viés de sobrevivência:** incluir ações que saíram da bolsa ou faliram (ex.: Americanas, Oi) nas datas em que existiam.
- **Sem olhar o futuro:** usar só os balanços já publicados em cada data, respeitando o atraso de divulgação.
- **Custos reais:** corretagem, emolumentos, spread e imposto.
- **Comparar com:** Ibovespa, CDI e o próprio Alaska Black.
- **Métricas:** retorno anual, maior queda, tempo de recuperação, volatilidade, índice de Sharpe e percentual de janelas de 3 anos acima do Ibovespa.
- **Teste de robustez:** variar os parâmetros (10 ou 20 ações, teto de 8% ou 12%) e conferir se o resultado não depende de um ajuste fino.

## Roadmap

- [ ] Escolher a fonte de dados e montar a base de preços e balanços desde 2012
- [ ] Implementar os filtros de risco lendo `config/risk_limits.yaml` (com testes)
- [ ] Implementar a pontuação de seleção
- [ ] Rodar o backtest e ajustar os limites
- [ ] Montar a base de eventos históricos (`inteligencia-de-mercado.md`)
- [ ] Confirmar com a corretora a conta de não residente e o acesso ao MetaTrader 5
- [ ] Operar 3 meses em conta demo com aprovação manual das ordens
- [ ] Começar com valor pequeno e aumentar só se o comportamento real bater com o backtest
