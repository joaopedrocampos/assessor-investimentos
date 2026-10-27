# Project skills

A skill is a repeatable procedure that needs judgment. Knowledge goes in `docs/`; checkable rules go in code or `config/`.

## When to create a skill

- The same procedure has already been done at least twice in conversations.
- It has steps Claude gets wrong or forgets without guidance (right sources, pitfalls, output format).
- It cannot be solved with a script or a test.

Create one skill at a time and test it before it goes in: run the task without the skill, see where it fails, write the skill to fix that, run it again.

## Candidates

| Skill | Trigger | Has it repeated? |
| --- | --- | --- |
| `researching-a-fund` | Analyzing a new equity fund for the research base | Yes, 9 times on 26/10/2026 |
| `analyzing-a-market-event` | A relevant political or economic event happens | Not yet |
| `reviewing-the-portfolio` | Weekly or monthly portfolio review against the limits | Not yet |
| `evaluating-a-stock` | Deciding whether a stock enters the portfolio | Not yet |

Format: `.claude/skills/<name>/SKILL.md`, with `name` and `description` in the frontmatter. The description says only when to use it ("Use when..."), never summarizes the procedure.
