# codex-dotfile

This repository is a Markdown-first operating system for Codex. It provides a shared set of workflows, prompts, rules, roles, contexts, and skills so Codex can work consistently across analysis, implementation, testing, audits, and delivery.

It is not an application runtime. There is no app to launch at the repository root. The value of this repo is the `.codex/` directory and the working conventions around it.

## What This Repository Is

This repo packages a reusable `.codex/` setup that you can keep as a reference or copy into another repository.

Codex reads these files as operating instructions:

- `workflows` define how to analyze, plan, implement, test, audit, prepare a PR, or ship changes
- `prompts` provide saved slash-style aliases such as `/think`, `/forge`, and `/test`
- `rules` define safety and delivery constraints
- `agents` define specialized roles such as `architect`, `backend`, `frontend`, and `doc-planner`
- `contexts` adjust behavior for research, development, and review
- `skills` store focused guidance for architecture, testing, security, TypeScript, Docker, and more

Start with [`.codex/MANUAL.md`](.codex/MANUAL.md). That file is the main entry point.

## How It Works

You do not run special commands from this repo. You ask Codex, in natural language, to follow one of the files inside `.codex/`.

Examples:

```text
Use .codex/workflows/think.md to analyze this feature and create a plan.
```

```text
Follow .codex/workflows/forge.md and execute the latest approved plan without committing.
```

```text
Use /test to add coverage for this module and keep the change narrow.
```

The files under `.codex/prompts/` are a convenience layer. There is no native slash-command parser in this repo; the aliases are documented prompt expansions you can reuse in chat.

When a prompt alias is invoked, Codex should load the matching file in `.codex/prompts/`. If that prompt points to a workflow, Codex should open the corresponding workflow in `.codex/workflows/` and follow it as the source of truth for execution.

## Recommended Flow

For most non-trivial tasks, the intended flow is:

1. `think` for read-only analysis and planning
2. `forge` for implementation
3. `test` for focused coverage and regression protection
4. `audit` for read-only quality, security, and architecture review
5. `pr` or `ship` only when you explicitly want Git delivery steps

## What Codex Will Create

For larger tasks, Codex is expected to leave artifacts in `.orchestrator/` so the work can be resumed later.

Typical outputs:

- `.orchestrator/plans/<timestamp>-think-<slug>/status.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/investigation.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/design.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/plan.md`
- `.orchestrator/plans/<timestamp>-<slug>/implementation.md`
- `.orchestrator/audits/<timestamp>-audit/audit-report.md`

## Safety Model

This setup is intentionally conservative:

- Codex should not commit, push, merge, or delete branches unless you explicitly ask
- delivery steps should use Conventional Commits
- plans, docs, and implementation logs should stay aligned with the real work
- if documentation is missing or stale, Codex should record that as a risk instead of guessing

## Repository Map

- `.codex/MANUAL.md`: main operating manual
- `.codex/workflows/`: end-to-end workflows such as `think`, `forge`, `test`, `audit`, `pr`, and `ship`
- `.codex/prompts/`: slash-style prompt aliases
- `.codex/rules/`: shared safety and operating constraints
- `.codex/agents/`: specialized role cards
- `.codex/contexts/`: behavior overlays by work mode
- `.codex/skills/`: reusable reference packs

## Quick Start

1. Copy or adapt the `.codex/` directory into your repository.
2. Open `.codex/MANUAL.md`.
3. Ask Codex to use one of the workflows or prompt aliases.
4. Let Codex write plans and audit artifacts to `.orchestrator/` for medium or large tasks.
