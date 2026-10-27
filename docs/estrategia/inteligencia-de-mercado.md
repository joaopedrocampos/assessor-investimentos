# Camada de inteligência de mercado

O bot funciona como assessor de longo prazo: não tenta adivinhar eventos, mas compara o que o mercado está precificando com a probabilidade real e avisa quando existe risco assimétrico. A eleição de 25/10/2026 é o exemplo: o mercado precificava vitória da oposição, Lula venceu com 51,79% e o Ibovespa caiu 13,88% no dia seguinte, com circuit breaker ([InfoMoney](https://www.infomoney.com.br/mercados/ibovespa-hoje-bolsa-de-valores-ao-vivo-26102026/)).

## Princípio: a IA lê e compara, os dados dão os números

Um modelo de linguagem tem data de corte e erra números históricos com confiança. Por isso as probabilidades vêm de uma base de dados consultada pelo bot (RAG), e a IA interpreta, classifica e busca casos parecidos.

## As três camadas

1. **Memória histórica (base de eventos):** cada evento relevante desde 2002, com o que o mercado esperava, o que aconteceu e a reação do Ibovespa, dólar, juros futuros e setores em D+1, D+5 e D+30. Indexada por embeddings para busca de casos análogos.
2. **Atualização diária:** um agente coleta notícias, dados econômicos e movimentos de grandes investidores, classifica os eventos e atualiza a visão de cenário.
3. **Raciocínio em probabilidades:** cenários com probabilidade, comparados com o que está no preço (bolsa, curva de juros, volatilidade das opções). A saída são alertas e sugestões dentro dos limites de risco.

## Eventos para a base histórica

| Tipo | Exemplos |
| --- | --- |
| Eleições presidenciais | 2002, 2006, 2010, 2014, 2018, 2022, 2026 |
| Crises políticas | Impeachment (2016), Joesley Day (2017) |
| Choques externos | Crise de 2008, pandemia (2020), tarifas dos EUA (2025), guerra no Oriente Médio (2026) |
| Política monetária | Ciclos de alta e corte da Selic, decisões do Copom fora do esperado |
| Fiscal | Mudanças de arcabouço fiscal, pacotes de gastos |

## Fontes de dados diárias

| Categoria | Fontes |
| --- | --- |
| Notícias | RSS e APIs de Valor, InfoMoney, Reuters, Bloomberg Línea |
| Empresas | Fatos relevantes e balanços na CVM (dados abertos, DFP/ITR) |
| Economia | Banco Central (Selic, boletim Focus, séries do SGS), IBGE (IPCA, PIB), curva de juros da B3 |
| Grandes investidores | Carteiras de fundos na CVM, cartas mensais de gestores, relatórios 13F nos EUA |
| Expectativas | Pesquisas eleitorais, mercados de previsão, consenso de analistas |
| Preços | Ibovespa, dólar, risco-país (CDS), volatilidade implícita das opções |

## O que o assessor entrega

- **Resumo semanal:** cenário base, principais riscos, agenda da semana e efeito provável na carteira.
- **Alertas:** quando um evento relevante acontece ou quando a diferença entre preço e probabilidade fica grande.
- **Sugestões de ajuste:** sempre dentro dos limites de risco, com o motivo e os casos históricos usados.
- **Aprovação humana:** nenhuma ordem sai sem o João aprovar.

## Calibração e limites

- **Registro de previsões:** cada probabilidade dada fica gravada e é comparada depois com o que aconteceu (Brier score). Se os "70%" do bot não acontecem perto de 70% das vezes, ele não está calibrado.
- **Poucos exemplos:** só 7 eleições presidenciais desde 2002. As faixas de probabilidade serão largas.
- **Mudança de regime:** juros, fluxo estrangeiro e regras mudam entre ciclos. Casos antigos valem menos.
- **Mercado reage à surpresa:** o que move o preço é a diferença entre o resultado e o que já estava precificado, não o evento em si.
