# ADR 0002: English as the repo language

Date: 27/10/2026 · Status: accepted

## Context

The repo started in Portuguese. Code, libraries, API docs and the installed skills (Matt Pocock, Superpowers) are in English, so the repo was drifting into a mix (`peso_max_por_acao` in YAML next to `load_risk_limits` in Python). Portuguese text also uses more tokens than the same text in English, which matters for an agent that reads docs and news every day. Claude's reasoning quality is similar in both languages, so quality was not the deciding factor.

## Decision

- Code, docs, config keys, skills and commit messages are in English.
- Brazilian market terms stay in Portuguese (Selic, CDI, Ibovespa, Copom, fato relevante, tickers), defined in `docs/glossary.md`.
- Sources in Portuguese are read as-is; conclusions are written in English.
- Chat with João stays in Portuguese.
- The language of the advisor's reports to João is a setting (`config/advisor.yaml`), defaulting to English.

## Consequences

- Translating cost little at this stage (12 docs). It would cost much more later.
- The Python package is `advisor`; the repo name `assessor-investimentos` is kept.
