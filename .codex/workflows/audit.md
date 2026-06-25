---
description: Read-only audit workflow for code quality, security, and architectural drift.
---

# Audit Workflow

Use this workflow for a structured read-only audit.

## Outcome

Create `.orchestrator/audits/<timestamp>-audit/` with:

- `status.md`
- `1-guidelines-findings.md`
- `2-security-findings.md`
- `3-architecture-findings.md`
- `audit-report.md`

Create `status.md` from `.codex/templates/status.md` with `workflow: audit`,
`status: in_progress`, and the audit risk level.

## Phase 0: Setup

```bash
export AUDIT_PATH=".orchestrator/audits/$(date +'%Y-%m-%d-%H-%M')-audit"
mkdir -p "$AUDIT_PATH"
```

## Phase 1: Guidelines Check

Detect the stack and conventions before judging code:

- load configured docs when present
- inspect stack markers and project-native commands
- sample representative modules, not only easy files
- compare against `.codex/skills/` guidance and local patterns
- distinguish style preferences from maintainability risks

Write `1-guidelines-findings.md`:

```markdown
# Guidelines Findings

## Scope
<files and modules sampled>

## Findings
- Severity: <critical|high|medium|low>
- File: `<path:line>`
- Issue: <concrete observation>
- Impact: <why it matters>
- Recommendation: <specific fix>
```

## Phase 2: Security Check

Review auth, authorization, secrets handling, validation, rate limiting,
dependency posture, permissions, CORS/CSRF where relevant, and risky
configuration.

Write `2-security-findings.md` with concrete evidence. Do not include secrets in
the report. Redact any sensitive values discovered during inspection.

## Phase 3: Architecture And Performance Scan

Look for:

- boundary leaks between UI, domain logic, persistence, and infrastructure
- tight coupling, cyclic dependencies, and contract drift
- unclear ownership or abstractions that hide simple behavior
- missing failure behavior around persistence, external calls, or queues
- likely performance bottlenecks in hot paths, N+1 queries, payload size, or rendering

Write `3-architecture-findings.md` with file references and actionable
recommendations.

## Phase 4: Final Report

Write `audit-report.md`:

```markdown
# Audit Report

## Executive Summary
<health summary and highest-risk theme>

## Prioritized Findings
### Critical
### High
### Medium
### Low

## Recommended Next Steps
<ordered fixes or follow-up /think work>

## Evidence Reviewed
<docs, configs, modules, tests, commands>
```

Execute the required risk gate and transition to `completed` through
`.codex/scripts/transition-workspace.sh` only when the report exists and all audit
phases are accounted for.

## Final Response

Present findings ordered by severity and point to the report path.

## Rules

- This workflow is read-only for product code.
- Writing audit artifacts under `.orchestrator/audits/` is allowed.
- Do not commit, push, mutate source files, or run destructive commands.
- Prefer concrete file evidence over broad claims.
