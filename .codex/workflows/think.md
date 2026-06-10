---
description: Read-only analysis workflow for investigation, design, and implementation planning.
---

# Think Workflow

Use this workflow when the user wants analysis, architecture, or a concrete plan without product code changes.

## Outcome

Create a workspace in `.orchestrator/plans/<timestamp>-think-<slug>/` with:
- `status.md`
- `investigation.md`
- `design.md`
- `plan.md`

## Phase 0: Setup

```bash
export PLAN_PATH=".orchestrator/plans/$(date +'%Y-%m-%d-%H-%M')-think-<slug>"
mkdir -p "$PLAN_PATH"
```

Create `status.md` with phases `Investigation`, `Design`, and `Plan`.
Create it from `.codex/templates/status.md` with `workflow: think`, `status: draft`, and an explicit risk level.

## Phase 1: Investigation

1. Load configured documentation candidates in order.
2. If they are missing, fall back to local docs, config files, and the source tree.
3. Detect the stack, architecture pattern, conventions, and relevant modules.
4. Write `investigation.md` covering:
   - request summary
   - current state
   - reuse opportunities
   - risks and edge cases
   - recommendation

## Phase 2: Design

Write `design.md` covering:
- architecture impact
- file/module boundaries
- contracts or schemas if needed
- dependency changes if any
- testing strategy

If frontend work is involved, separate logic, presentation, and state concerns explicitly.

## Phase 3: Plan

Write `plan.md` as an ordered checklist of atomic tasks.

Each task must include:
- target file or module
- concrete action
- verification command or check

Keep tasks small enough to complete and verify independently.

Before finishing:

1. validate the workspace with `.codex/scripts/validate-plan.sh`
2. transition to `awaiting_approval` with `.codex/scripts/transition-workspace.sh`
3. leave `approved_by: pending` until the user explicitly approves execution

## Final Response

Tell the user:
1. what you found
2. the recommended design
3. the execution plan
4. that product code was not modified

## Rules

- Do not edit product code in this workflow.
- Writing under `.orchestrator/plans/` is allowed.
- Do not create branches, commits, or pushes here.
