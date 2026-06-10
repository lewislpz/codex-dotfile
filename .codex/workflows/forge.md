---
description: Full implementation workflow for executing an approved plan with logs and verification.
---

# Forge Workflow

Use this workflow when the user wants implementation, not just analysis.

## Preconditions

- Require an explicit workspace path when the user provides one.
- Otherwise use `python3 .codex/scripts/control.py select-workspace .orchestrator/plans`; never select by recency alone.
- If no plan exists, create `investigation.md`, `design.md`, and `plan.md` first in the same workspace before coding.

## Setup

1. Resolve `PLAN_PATH` from the user-provided path or `control.py select-workspace`.
2. Ensure these files exist or are created:
   - `status.md`
   - `investigation.md`
   - `design.md`
   - `plan.md`
   - `implementation.md`
3. If the workspace is a Git repo and the user explicitly wants branch isolation, create a feature branch. Otherwise continue on the current branch.
4. Run `.codex/scripts/validate-plan.sh "$PLAN_PATH"` and stop on failure.
5. Confirm `status.md` declares `status: approved` or `status: in_progress`.
6. Record the implementation actor with `python3 .codex/scripts/control.py record-implementation`.
7. If approved, transition to `in_progress` with `.codex/scripts/transition-workspace.sh`.

## Phase 1: Context Refresh

- Re-read the relevant parts of the plan.
- Load source-of-truth docs if they exist.
- Re-scan the touched modules before editing.

## Phase 2: Execute Tasks

For each unchecked task in `plan.md`:

1. Confirm the owned files and expected result.
2. Decide whether to do it locally or delegate with `.codex/templates/delegation-contract.json`.
3. Implement the change.
4. Run the listed verification command.
5. Update `implementation.md` with what changed and what passed.
6. Mark the task complete in `plan.md`.
7. Create a checkpoint with `.codex/scripts/checkpoint.sh`.

## Phase 3: Verify The Whole Slice

After task execution:
- run the narrowest meaningful test/build checks
- satisfy the gate in `.codex/rules/risk-gates.md`
- update docs if the target repository maintains docs for changed behavior
- confirm there are no unchecked tasks left in `plan.md`
- bind the verified Git working tree and allowed paths; when Git is unavailable, bind the verified source roots
- transition to `completed` with `.codex/scripts/transition-workspace.sh`; direct status edits are forbidden

## Final Response

Report:
1. files changed
2. verification performed
3. remaining risks or follow-ups
4. whether the tree is ready for a manual `pr` or `ship` step

## Rules

- Do not commit, push, or merge unless the user explicitly asks for delivery.
- Classify failures before retrying and stop after three materially different failed repair attempts.
- Keep `implementation.md` and `plan.md` in sync with reality.
