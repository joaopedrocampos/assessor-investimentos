# Lições

O bot deve copiar a disciplina de seleção dos fundos consistentes e evitar o que mais prejudicou o Alaska Black: a falta de limites de risco. Seis padrões aparecem em toda a amostra (detalhes em `pesquisa/`).

1. **Correlação é o risco escondido.** O Alaska Black perdeu 57% em 2024 porque ações, opções, câmbio e juros dependiam do mesmo cenário. Medir a exposição a fatores (juros, dólar, consumo doméstico) é mais importante que contar ações.
2. **Limitar o estrago de cada erro.** A Atmos declara que a pior escolha nunca custou mais de 2% da carteira. Isso é um limite de risco por posição, não de peso.
3. **Liquidez decide se você consegue sair.** A CTM travou resgates com quase 40% em uma ação ilíquida. O tamanho de cada posição precisa caber no volume negociado.
4. **Até os melhores passam anos ruins.** Dynamo, Atmos e Vokin ficaram de 2 a 5 anos abaixo do índice. O bot precisa sobreviver a isso sem quebrar e sem ser desligado no pior momento.
5. **Um ano bom não prova nada.** Infrad ganhou 46 pontos do índice em 2025 e pouco nos outros anos. Avaliar estratégias em vários períodos.
6. **Subdesempenho longo pede revisão.** Tork e 3R Cedar II ficaram anos abaixo sem mudar o rumo.

## O que vira código e o que não vira

| Codificável | Depende de julgamento |
| --- | --- |
| Filtros de liquidez e valor de mercado | Qualidade da gestão das empresas |
| Filtros de valuation (P/L, EV/EBITDA, margem de segurança) | Valor justo de cada empresa (fluxo de caixa descontado) |
| Filtros de qualidade (ROIC, dívida líquida/EBITDA) | Se uma queda é exagero do mercado ou tese quebrada |
| Teto por ação, setor e fator | Leitura de cenário político e regulatório |
| Stop de drawdown da carteira e volatilidade-alvo | Quando proteger a carteira com dólar ou juros |
| Redução de risco antes de eventos com data marcada (eleições) | Escolha de temas como infraestrutura |
| Rebalanceamento periódico | Mudanças de estratégia |

A parte de julgamento pode ser apoiada por um agente de IA lendo balanços, cartas e notícias, mas a decisão final de mudar regras continua com o João.
