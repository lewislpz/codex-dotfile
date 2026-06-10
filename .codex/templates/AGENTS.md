# Agentic Development

<!-- codex-workflow:start -->
For non-trivial work in this repository:

1. Read `.codex/MANUAL.md` and `.codex/config.json`.
2. Follow `.codex/rules/global.md`, `.codex/rules/agent-security.md`, and `.codex/rules/control-plane.md`.
3. Select the matching procedure from `.codex/workflows/`.
4. Use `.orchestrator/` workspaces for resumable plans, audits, evidence, and checkpoints.
5. Apply risk gates from `.codex/rules/risk-gates.md`.
6. Never commit, push, merge, release, or perform destructive actions without explicit user authorization.
7. After modifying `.codex/`, run `bash .codex/scripts/verify-control-plane.sh`.
<!-- codex-workflow:end -->
