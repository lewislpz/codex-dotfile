# codex-dotfile

English below. Espanol below.

This repository is a Markdown-first operating system for Codex. It gives Codex a shared set of workflows, prompts, rules, roles, contexts, and skills so it can work more consistently across analysis, implementation, testing, audits, and delivery.

It is not an application runtime. There is no app to launch at the root. The value of this repo is the `.codex/` folder and the working conventions around it.

## English

### What This Repository Is

This repo packages a reusable `.codex/` setup that you can keep as a reference or copy into another repository.

Codex reads these files as operating instructions:

- `workflows` define how to analyze, plan, implement, test, audit, prepare a PR, or ship changes
- `prompts` provide saved slash-style aliases such as `/think`, `/forge`, and `/test`
- `rules` define safety and delivery constraints
- `agents` define specialized roles such as `architect`, `backend`, `frontend`, and `doc-planner`
- `contexts` adjust behavior for research, development, and review
- `skills` store focused guidance for architecture, testing, security, TypeScript, Docker, and more

Start with [`.codex/MANUAL.md`](.codex/MANUAL.md). That file is the main entry point.

### How It Works

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

The prompt files under [`.codex/prompts/`](.codex/prompts/README.md) are a convenience layer. There is no native slash-command parser in this repo; the aliases are documented prompt expansions that you can reference in chat.

### Recommended Flow

For most non-trivial tasks, the intended flow is:

1. `think` for read-only analysis and planning
2. `forge` for implementation
3. `test` for focused coverage and regression protection
4. `audit` for read-only quality, security, and architecture review
5. `pr` or `ship` only when you explicitly want Git delivery steps

### What Codex Will Create

For larger tasks, Codex is expected to leave artifacts in `.orchestrator/` so the work can be resumed later.

Typical outputs:

- `.orchestrator/plans/<timestamp>-think-<slug>/status.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/investigation.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/design.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/plan.md`
- `.orchestrator/plans/<timestamp>-<slug>/implementation.md`
- `.orchestrator/audits/<timestamp>-audit/audit-report.md`

### Safety Model

This setup is intentionally conservative:

- Codex should not commit, push, merge, or delete branches unless you explicitly ask
- delivery steps should use Conventional Commits
- plans, docs, and implementation logs should stay aligned with the real work
- if documentation is missing or stale, Codex should record that as a risk instead of guessing

### Repository Map

- [`.codex/MANUAL.md`](.codex/MANUAL.md): main operating manual
- [`.codex/workflows/`](.codex/workflows/think.md): end-to-end workflows such as `think`, `forge`, `test`, `audit`, `pr`, and `ship`
- [`.codex/prompts/`](.codex/prompts/README.md): slash-style prompt aliases
- [`.codex/rules/`](.codex/rules/global.md): shared safety and operating constraints
- [`.codex/agents/`](.codex/agents/architect.md): specialized role cards
- [`.codex/contexts/`](.codex/contexts/development.md): behavior overlays by work mode
- [`.codex/skills/`](.codex/skills/software-architecture/SKILL.md): reusable reference packs

### Quick Start

1. Copy or adapt the `.codex/` directory into your repository.
2. Open [`.codex/MANUAL.md`](.codex/MANUAL.md).
3. Ask Codex to use one of the workflows or prompt aliases.
4. Let Codex write plans and audit artifacts to `.orchestrator/` for medium or large tasks.

## Espanol

### Que Es Este Repositorio

Este repo empaqueta una configuracion reutilizable de `.codex/` que puedes usar como referencia o copiar dentro de otro repositorio.

Codex lee estos archivos como instrucciones de trabajo:

- `workflows` definen como analizar, planificar, implementar, probar, auditar, preparar un PR o publicar cambios
- `prompts` ofrecen alias tipo slash como `/think`, `/forge` y `/test`
- `rules` definen restricciones de seguridad y entrega
- `agents` definen roles especializados como `architect`, `backend`, `frontend` y `doc-planner`
- `contexts` ajustan el comportamiento para investigacion, desarrollo y review
- `skills` guardan guias concretas para arquitectura, testing, seguridad, TypeScript, Docker y mas

Empieza por [`.codex/MANUAL.md`](.codex/MANUAL.md). Ese archivo es el punto de entrada principal.

### Como Funciona

No tienes que ejecutar comandos especiales de este repo. Le pides a Codex, en lenguaje natural, que siga uno de los archivos de `.codex/`.

Ejemplos:

```text
Usa .codex/workflows/think.md para analizar esta feature y crear un plan.
```

```text
Sigue .codex/workflows/forge.md y ejecuta el ultimo plan aprobado sin hacer commit.
```

```text
Usa /test para anadir cobertura a este modulo y mantener el cambio acotado.
```

Los archivos de [`.codex/prompts/`](.codex/prompts/README.md) son una capa de conveniencia. Este repo no incluye un parser nativo de slash commands; esos alias documentan expansiones de prompt que puedes reutilizar en el chat.

### Flujo Recomendado

Para la mayoria de tareas no triviales, el flujo esperado es:

1. `think` para analizar y planificar sin tocar codigo de producto
2. `forge` para implementar
3. `test` para ampliar cobertura y cerrar regresiones
4. `audit` para revisar calidad, seguridad y arquitectura en modo read-only
5. `pr` o `ship` solo cuando quieras pasos de entrega en Git de forma explicita

### Que Va A Crear Codex

En tareas medianas o grandes, Codex deberia dejar artefactos en `.orchestrator/` para que el trabajo pueda retomarse despues.

Salidas tipicas:

- `.orchestrator/plans/<timestamp>-think-<slug>/status.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/investigation.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/design.md`
- `.orchestrator/plans/<timestamp>-think-<slug>/plan.md`
- `.orchestrator/plans/<timestamp>-<slug>/implementation.md`
- `.orchestrator/audits/<timestamp>-audit/audit-report.md`

### Modelo De Seguridad

Esta configuracion es intencionalmente conservadora:

- Codex no deberia hacer `commit`, `push`, `merge` ni borrar ramas salvo que se lo pidas de forma explicita
- los pasos de entrega deberian usar Conventional Commits
- los planes, la documentacion y los logs de implementacion deben mantenerse sincronizados con el trabajo real
- si la documentacion falta o esta desactualizada, Codex deberia registrarlo como riesgo en lugar de inventar

### Mapa Del Repositorio

- [`.codex/MANUAL.md`](.codex/MANUAL.md): manual principal
- [`.codex/workflows/`](.codex/workflows/think.md): flujos completos como `think`, `forge`, `test`, `audit`, `pr` y `ship`
- [`.codex/prompts/`](.codex/prompts/README.md): alias tipo slash
- [`.codex/rules/`](.codex/rules/global.md): restricciones compartidas de seguridad y operacion
- [`.codex/agents/`](.codex/agents/architect.md): tarjetas de rol especializadas
- [`.codex/contexts/`](.codex/contexts/development.md): overlays de comportamiento segun el modo de trabajo
- [`.codex/skills/`](.codex/skills/software-architecture/SKILL.md): paquetes reutilizables de referencia

### Inicio Rapido

1. Copia o adapta el directorio `.codex/` dentro de tu repositorio.
2. Abre [`.codex/MANUAL.md`](.codex/MANUAL.md).
3. Pidele a Codex que use uno de los workflows o aliases de prompt.
4. Deja que Codex escriba planes y auditorias en `.orchestrator/` para tareas medianas o grandes.
