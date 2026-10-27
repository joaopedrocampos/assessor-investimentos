# Investment advisor

AI agent that advises João Pedro on long-term investing in B3 (Brazilian) stocks. Horizon: retirement, from his 30s to his early 50s. Not day trading. Monthly rebalancing; no order is sent without human approval.

## Where things are

| I need... | Read |
| --- | --- |
| Overview and docs index | `docs/README.md` |
| Brazilian market terms kept in Portuguese | `docs/glossary.md` |
| Risk limit numbers (source of truth) | `config/risk_limits.yaml` |
| Why each risk limit exists | `docs/strategy/risk-limits.md` |
| How the bot picks stocks and operates | `docs/strategy/specification.md` |
| News, historical events and probabilities layer | `docs/strategy/market-intelligence.md` |
| Fund research (Alaska Black and 8 others) | `docs/research/` |
| Lessons drawn from the research | `docs/lessons.md` |
| Architecture decisions already made | `docs/decisions/` |
| Repeatable procedures | `.claude/skills/` |

Read only what the task needs. Do not load all of `docs/`.

## Language

- The repo is in English: code, docs, config keys, skills, commit messages.
- Brazilian market terms stay in Portuguese (Selic, CDI, Ibovespa, Copom, fato relevante, tickers). See `docs/glossary.md`.
- Sources are often in Portuguese; read them as-is and write conclusions in English.
- Chat with João is in Portuguese. The language of the advisor's reports to him is set in `config/advisor.yaml`.

## Working rules

- Separate sourced facts from opinions and estimates. Every market figure in `docs/` links to its source.
- Search before stating any current market figure; numbers in the docs are dated and go stale.
- Speak in scenarios and probabilities, never certainties.
- Point out risks and disagree when warranted. This is not investment advice; João makes the decisions.
- A risk limit changes in `config/risk_limits.yaml` and in its rationale in `docs/strategy/risk-limits.md` in the same commit. A test enforces this.
- A significant architecture decision becomes an ADR in `docs/decisions/` (next free number).

## Code

- Python 3.12, package in `src/advisor/`, tests in `tests/` with pytest.
- TDD for risk and selection rules: they are the part that protects the money.
- Risk limits are read from `config/risk_limits.yaml`, never hard-coded.
- Backtests have no survivorship bias and no look-ahead (see `docs/strategy/backtest.md`).
