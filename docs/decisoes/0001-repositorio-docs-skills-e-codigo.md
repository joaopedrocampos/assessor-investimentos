# ADR 0001: repositório como fonte da verdade, separando docs, skills, config e código

Data: 27/10/2026 · Status: aceito

## Contexto

A pesquisa inicial nasceu num documento único do Claude Docs. Manter esse documento sincronizado com o projeto do Claude exigia exportar e reenviar a cada mudança. O projeto vai evoluir por anos.

## Decisão

O repositório Git é a fonte da verdade. Cada tipo de conteúdo vai para um lugar:

| Tipo | Onde | Por quê |
| --- | --- | --- |
| Instruções e mapa do projeto | `CLAUDE.md` | Carregado em toda sessão; precisa ser curto |
| Conhecimento (pesquisa, lições, estratégia) | `docs/` | Lido sob demanda; um assunto por arquivo |
| Números que o código aplica (limites de risco) | `config/*.yaml` | Regra mecânica se valida em código, não em prosa |
| Procedimentos repetíveis com julgamento | `.claude/skills/` | Ex.: pesquisar um fundo, analisar um evento de mercado |
| O bot em si | `src/`, `tests/` | Python |

O assessor não é "uma grande skill". Skill é procedimento; conhecimento vai para `docs/`, e regra que pode ser verificada vai para código.

## Consequências

- Atualizar = commit. Sessões novas leem a versão atual.
- O documento original do Claude Docs fica como registro histórico e não é mais atualizado.
- Skills só são criadas quando um procedimento se repete, e são testadas antes de entrar (ver `.claude/skills/README.md`).
