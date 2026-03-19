# codex-dotfile

English below. Español below.

This repository is a Markdown-first operating system for Codex. It gives Codex a shared set of workflows, prompts, rules, roles, contexts, and skills so it can work more consistently across analysis, implementation, testing, audits, and delivery.

It is not an application runtime. There is no app to launch at the root. The value of this repo is the `.codex/` folder and the working conventions around it.

## English

### What This Repository Is

This repo packages a reusable `.codex/` setup that you can keep as a reference or copy into another repository.

Codex reads these files as operating instructions:

- `workflows` define how to analyze, plan, implement, test, audit, prepare a PR, or ship changes.
- `prompts` provide saved slash-style aliases such as `/think`, `/forge`, and `/test`.
- `rules` define safety and delivery constraints.
- `agents` define specialized roles such as `architect`, `backend`, `frontend`, and `doc-planner`.
- `contexts` adjust behavior for research, development, and review.
- `skills` store focused guidance for architecture, testing, security, TypeScript, Docker, and more.

Start with [`.codex/MANUAL.md`](.codex/MANUAL.md). That file is the main entry point.

### How It Works

You do not run special commands from this repo. You ask Codex, in natural language, to follow one of the files inside `.codex/`.

Examples:

```text
Use .codex/workflows/think.md to analyze this feature and create a plan.

code Text

Follow .codex/workflows/forge.md and execute the latest approved plan without committing.

code Text

Use /test to add coverage for this module and keep the change narrow.

The prompt files under .codex/prompts/ are a convenience layer. There is no native slash-command parser in this repo; the aliases are documented prompt expansions that you can reference in chat.
Recommended Flow

For most non-trivial tasks, the intended flow is:

    think for read-only analysis and planning.

    forge for implementation.

    test for focused coverage and regression protection.

    audit for read-only quality, security, and architecture review.

    pr or ship only when you explicitly want Git delivery steps.

What Codex Will Create

For larger tasks, Codex is expected to leave artifacts in .orchestrator/ so the work can be resumed later.

Typical outputs:

    .orchestrator/plans/<timestamp>-think-<slug>/status.md

    .orchestrator/plans/<timestamp>-think-<slug>/investigation.md

    .orchestrator/plans/<timestamp>-think-<slug>/design.md

    .orchestrator/plans/<timestamp>-think-<slug>/plan.md

    .orchestrator/plans/<timestamp>-<slug>/implementation.md

    .orchestrator/audits/<timestamp>-audit/audit-report.md

Safety Model

This setup is intentionally conservative:

    Codex should not commit, push, merge, or delete branches unless you explicitly ask.

    Delivery steps should use Conventional Commits.

    Plans, docs, and implementation logs should stay aligned with the real work.

    If documentation is missing or stale, Codex should record that as a risk instead of guessing.

Repository Map

    .codex/MANUAL.md: main operating manual.

    .codex/workflows/: end-to-end workflows such as think, forge, test, audit, pr, and ship.

    .codex/prompts/: slash-style prompt aliases.

    .codex/rules/: shared safety and operating constraints.

    .codex/agents/: specialized role cards.

    .codex/contexts/: behavior overlays by work mode.

    .codex/skills/: reusable reference packs.

Quick Start

    Copy or adapt the .codex/ directory into your repository.

    Open .codex/MANUAL.md.

    Ask Codex to use one of the workflows or prompt aliases.

    Let Codex write plans and audit artifacts to .orchestrator/ for medium or large tasks.

Español
Qué es este repositorio

Este repo empaqueta una configuración reutilizable de .codex/ que puedes usar como referencia o copiar dentro de otro repositorio.

Codex lee estos archivos como instrucciones de trabajo:

    workflows: definen cómo analizar, planificar, implementar, probar, auditar, preparar un PR o publicar cambios.

    prompts: ofrecen alias tipo slash como /think, /forge y /test.

    rules: definen restricciones de seguridad y entrega.

    agents: definen roles especializados como architect, backend, frontend y doc-planner.

    contexts: ajustan el comportamiento para investigación, desarrollo y review.

    skills: guardan guías concretas para arquitectura, testing, seguridad, TypeScript, Docker y más.

Empieza por .codex/MANUAL.md. Ese archivo es el punto de entrada principal.
Cómo funciona

No tienes que ejecutar comandos especiales de este repo. Le pides a Codex, en lenguaje natural, que siga uno de los archivos de .codex/.

Ejemplos:
code Text

Usa .codex/workflows/think.md para analizar esta feature y crear un plan.

code Text

Sigue .codex/workflows/forge.md y ejecuta el último plan aprobado sin hacer commit.

code Text

Usa /test para añadir cobertura a este módulo y mantener el cambio acotado.

Los archivos de .codex/prompts/ son una capa de conveniencia. Este repo no incluye un parser nativo de slash commands; esos alias documentan expansiones de prompt que puedes reutilizar en el chat.
Flujo recomendado

Para la mayoría de tareas no triviales, el flujo esperado es:

    think: para analizar y planificar sin tocar código de producto.

    forge: para implementar.

    test: para ampliar cobertura y cerrar regresiones.

    audit: para revisar calidad, seguridad y arquitectura en modo read-only.

    pr o ship: solo cuando quieras pasos de entrega en Git de forma explícita.

Qué va a crear Codex

En tareas medianas o grandes, Codex debería dejar artefactos en .orchestrator/ para que el trabajo pueda retomarse después.

Salidas típicas:

    .orchestrator/plans/<timestamp>-think-<slug>/status.md

    .orchestrator/plans/<timestamp>-think-<slug>/investigation.md

    .orchestrator/plans/<timestamp>-think-<slug>/design.md

    .orchestrator/plans/<timestamp>-think-<slug>/plan.md

    .orchestrator/plans/<timestamp>-<slug>/implementation.md

    .orchestrator/audits/<timestamp>-audit/audit-report.md

Modelo de seguridad

Esta configuración es intencionalmente conservadora:

    Codex no debería hacer commit, push, merge ni borrar ramas salvo que se lo pidas de forma explícita.

    Los pasos de entrega deberían usar Conventional Commits.

    Los planes, la documentación y los logs de implementación deben mantenerse sincronizados con el trabajo real.

    Si la documentación falta o está desactualizada, Codex debería registrarlo como riesgo en lugar de inventar.

Mapa del repositorio

    .codex/MANUAL.md: manual principal.

    .codex/workflows/: flujos completos como think, forge, test, audit, pr y ship.

    .codex/prompts/: alias tipo slash.

    .codex/rules/: restricciones compartidas de seguridad y operación.

    .codex/agents/: tarjetas de rol especializadas.

    .codex/contexts/: overlays de comportamiento según el modo de trabajo.

    .codex/skills/: paquetes reutilizables de referencia.

Inicio rápido

    Copia o adapta el directorio .codex/ dentro de tu repositorio.

    Abre .codex/MANUAL.md.

    Pídele a Codex que use uno de los workflows o alias de prompt.

    Deja que Codex escriba planes y auditorías en .orchestrator/ para tareas medianas o grandes.

