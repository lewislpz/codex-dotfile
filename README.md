# Codex Workflow Kit

A portable workflow layer for doing serious work with Codex without losing the plot.

This repository is not an app, a framework, or a prompt dump. It is a small operating system for agentic development: rules, workflows, role briefs, templates, skills, validation scripts, and evidence trails that help a human and Codex work through real repository changes with less drift.

## The Problem

Most AI coding sessions start well and get messy later:

- the agent forgets why a decision was made
- plans live only in chat history
- "done" means whatever the last message claims
- reviews, tests, and approvals are easy to skip
- another session cannot resume the work cleanly
- every repository reinvents the same instructions

This repo turns that into a repeatable process. It gives Codex a shared way to investigate, plan, implement, verify, audit, and prepare delivery while leaving a local trail that a human can inspect.

## What It Gives You

- **Workflows** for analysis, implementation, testing, audits, PR prep, and shipping.
- **Rules** for security, risk gates, Git safety, control-plane state, and delivery boundaries.
- **Templates** for plans, implementation logs, checkpoints, gate evidence, and delegation contracts.
- **Scripts** that validate workspace state, run gates, bind evidence to Git state, and catch process regressions.
- **Skills** that encode focused engineering judgment without forcing one stack or architecture.
- **Slash-prompt aliases** you can invoke naturally in chat, such as `/think`, `/forge`, and `/audit`.

The point is not ceremony. The point is making larger AI-assisted changes resumable, reviewable, and harder to hand-wave.

## When To Use It

Use this kit when a repository needs more than a one-off prompt:

- feature work that should start with investigation and a plan
- changes where tests, review, or approval matter
- audits that need reproducible evidence
- teams that want consistent Codex behavior across projects
- personal projects where you want future-you to understand what happened

You probably do not need it for a tiny typo fix or a throwaway experiment.

## Quick Start

Copy `.codex/` into the root of a target repository, then run:

```sh
bash .codex/scripts/bootstrap.sh
```

Bootstrap is idempotent. It checks the local environment, creates workflow roots, installs the managed `AGENTS.md` block, updates generated-file exclusions, and validates the package.

Minimum environment:

- Bash
- Python 3.9 or newer
- `rg` / ripgrep
- Git when Git binding or delivery workflows are required

## Daily Workflow

Start with analysis:

```text
Use /think to analyze this feature: add GitHub login.
```

Review the generated plan. When you are ready to execute it:

```text
Use /forge on the approved plan and do not commit.
```

For a read-only health check:

```text
Use /audit to review this repository for security, architecture, and quality risks.
```

For test-focused work:

```text
Use /test to build coverage for this module.
```

Delivery workflows are intentionally manual. Use `/pr` or `/ship` only when you explicitly want Codex to prepare that step. The rules forbid commits, pushes, merges, releases, or destructive actions without explicit user authorization.

## Useful Commands

Validate the whole control plane:

```sh
bash .codex/scripts/verify-control-plane.sh
```

List resumable workspaces:

```sh
bash .codex/scripts/list-workspaces.sh
```

Validate a specific plan workspace:

```sh
bash .codex/scripts/validate-plan.sh .orchestrator/plans/<workspace>
```

Run workflow regression checks:

```sh
bash .codex/scripts/validate-workflows.sh
```

## Repository Layout

```text
.codex/
  agents/       Role briefs for architecture, planning, backend, and frontend work
  contexts/     Behavior overlays for research, implementation, and review
  evals/        Process-regression cases
  prompts/      Natural-language slash prompt aliases
  rules/        Global, security, delivery, and control-plane rules
  schemas/      Machine-readable workspace and config contracts
  scripts/      Validation, gate, checkpoint, binding, bootstrap, and eval commands
  skills/       Focused engineering guidance packs
  templates/    Canonical formats for plans, logs, gates, and delegation
  workflows/    Operating procedures for think, forge, test, audit, pr, and ship
```

Runtime workflow state lives in `.orchestrator/` inside the target repository. That directory is local agent state and should normally stay out of Git.

## How The Control Plane Works

For non-trivial work, Codex creates a workspace under `.orchestrator/plans/` or `.orchestrator/audits/`. The workspace records:

- status and risk level
- investigation notes
- design decisions
- the implementation plan
- task-by-task implementation notes
- checkpoints
- gate receipts
- Git or file bindings

State transitions are handled by scripts instead of hand-edited prose. A completed workspace must satisfy the gates required by its risk level.

Risk levels are deliberately simple:

- **Low**: documentation, copy, and local formatting changes
- **Medium**: application logic, APIs, dependencies, schemas, and behavior changes
- **High**: auth, secrets, destructive migrations, release automation, and production delivery

## Adapting It To A Project

Most project-specific settings belong in:

```text
.codex/config.json
```

Use it for workspace roots, documentation candidates, generated-file exclusions, Git conventions, and risk gates. Keep the reusable workflow package product-neutral; put product rules in the target repository's normal documentation or project-specific skills.

## Maintaining This Kit

After modifying `.codex/`, run:

```sh
bash .codex/scripts/verify-control-plane.sh
```

If you change a workflow or skill, add or update an eval case first so the package can catch the process regression later.

## What This Is Not

- It is not a replacement for human review.
- It is not a CI system.
- It is not a framework for your application code.
- It is not a guarantee that an agent made the right call.

It is a set of rails for doing AI-assisted engineering with more memory, clearer boundaries, and better evidence.
