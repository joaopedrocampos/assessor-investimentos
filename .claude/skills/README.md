# Skills do projeto

Skill é um procedimento repetível que exige julgamento. Conhecimento vai para `docs/`; regra verificável vai para código ou `config/`.

## Quando criar uma skill

- O mesmo procedimento já foi feito pelo menos duas vezes nas conversas.
- Ele tem passos que o Claude erra ou esquece sem orientação (fontes certas, armadilhas, formato de saída).
- Não dá para resolver com um script ou um teste.

Cada skill é criada uma de cada vez e testada antes de entrar: rodar a tarefa sem a skill, ver onde falha, escrever a skill para corrigir isso e rodar de novo.

## Candidatas

| Skill | Gatilho | Já se repetiu? |
| --- | --- | --- |
| `pesquisando-fundo` | Analisar um fundo de ações novo para a base de pesquisa | Sim, 9 vezes em 26/10/2026 |
| `analisando-evento-de-mercado` | Um evento político ou econômico relevante acontece | Ainda não |
| `revisando-carteira` | Revisão semanal ou mensal da carteira contra os limites | Ainda não |
| `avaliando-acao` | Avaliar se uma ação entra na carteira | Ainda não |

Formato: `.claude/skills/<nome>/SKILL.md`, com `name` e `description` no frontmatter. A descrição diz só quando usar ("Use when..."), nunca resume o procedimento.
