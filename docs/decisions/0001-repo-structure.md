# ADR 0001: the repo is the source of truth, split into docs, skills, config and code

Date: 27/10/2026 · Status: accepted

## Context

The initial research was a single Claude Docs document. Keeping it in sync with the Claude project meant exporting and re-uploading it on every change. The project will evolve for years.

## Decision

The Git repo is the source of truth. Each kind of content has one home:

| Kind | Where | Why |
| --- | --- | --- |
| Instructions and project map | `CLAUDE.md` | Loaded every session; must stay short |
| Knowledge (research, lessons, strategy) | `docs/` | Read on demand; one subject per file |
| Numbers the code enforces (risk limits) | `config/*.yaml` | Mechanical rules are validated in code, not prose |
| Repeatable procedures needing judgment | `.claude/skills/` | E.g. researching a fund, analyzing a market event |
| The bot itself | `src/`, `tests/` | Python |

The advisor is not "one big skill". A skill is a procedure; knowledge goes in `docs/`, and rules that can be checked go in code.

## Consequences

- Updating means committing. New sessions read the current version.
- The original Claude Docs document stays as a historical record and is no longer updated.
- Skills are created only when a procedure repeats, and are tested before they go in (see `.claude/skills/README.md`).
