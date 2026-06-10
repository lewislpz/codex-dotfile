---
name: subagent-driven-development
description: Use when executing an approved plan and some tasks can be delegated safely to bounded Codex sub-agents.
---

# Sub-Agent Driven Development

Use only when delegation is available and authorized. If it is not, execute the same
bounded task contracts in the main thread.

## Execution Loop

1. Pick the next unchecked task from `plan.md`.
2. Decide whether the task is small enough to do locally or worth delegating.
3. If delegating, create an enforceable contract from `.codex/templates/delegation-contract.json`.
4. Review the result against the plan and boundary rules.
5. Update `implementation.md` and mark the task in `plan.md`.

## Rules

- One sub-agent per task.
- Give one bounded objective, allowed and forbidden paths, acceptance criteria, and verification.
- Keep write scopes disjoint.
- Stop on any scope conflict; never silently broaden ownership.
- Validate returned changed paths with `python3 .codex/scripts/control.py validate-scope`.
- Require an independent reviewer for high-risk delegated changes.
- Require the agent to return summary, files changed, checks run, and unresolved risks.
- Re-review fixes with the same criteria that failed previously.
- Classify failures before retrying and abort after three materially different failed repair attempts.
