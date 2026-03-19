# Guia Intuitiva De Uso

Esta carpeta `.codex/` convierte el repositorio en un sistema de trabajo para Codex. No se usa con comandos especiales: se usa pidiendole a Codex lo que quieres hacer en lenguaje natural.

Tambien tienes prompts guardados en [`.codex/prompts/README.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/README.md) con alias estilo slash como `/think`, `/forge`, `/test`, `/audit`, `/pr`, `/ship` y `/resume`.

## Idea Rapida

- `think`: analizar y planear sin tocar codigo de producto
- `forge`: implementar una tarea o ejecutar un plan aprobado
- `test`: crear o ampliar tests con enfoque TDD
- `audit`: hacer una auditoria read-only
- `pr`: preparar entrega en rama
- `ship`: fusionar o publicar, solo si lo pides explicitamente

## Como Pedir Las Cosas

Usa prompts directos y concretos. Ejemplos:

```text
Usa .codex/workflows/think.md para analizar esta feature y crear un plan.
```

```text
Sigue .codex/workflows/forge.md y ejecuta el ultimo plan aprobado.
```

```text
Haz una auditoria read-only con .codex/workflows/audit.md.
```

```text
Usa .codex/workflows/test.md para cubrir este modulo con tests.
```

## Alias Slash Guardados

No hay parser nativo de slash commands en este entorno, pero si una convencion util:

- `/think` -> [`.codex/prompts/think.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/think.md)
- `/forge` -> [`.codex/prompts/forge.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/forge.md)
- `/test` -> [`.codex/prompts/test.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/test.md)
- `/audit` -> [`.codex/prompts/audit.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/audit.md)
- `/pr` -> [`.codex/prompts/pr.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/pr.md)
- `/ship` -> [`.codex/prompts/ship.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/ship.md)
- `/resume` -> [`.codex/prompts/resume.md`](/Users/lewis/0-dev/active/codex-dotfile/.codex/prompts/resume.md)

Ejemplos:

```text
Usa /think para analizar esta feature y crear un plan.
```

```text
Usa /forge sobre el ultimo plan aprobado y no hagas commit.
```

## Flujo Recomendado

1. Empieza con `think` si la tarea no esta clara.
2. Revisa el plan en `.orchestrator/plans/...`.
3. Usa `forge` para implementar.
4. Usa `test` si faltan pruebas o quieres cerrar regresiones.
5. Usa `pr` o `ship` solo al final y solo si realmente quieres pasos de Git.

## Que Va A Crear Codex

En tareas medianas o grandes, Codex puede crear:

- `.orchestrator/plans/<fecha>-<slug>/investigation.md`
- `.orchestrator/plans/<fecha>-<slug>/design.md`
- `.orchestrator/plans/<fecha>-<slug>/plan.md`
- `.orchestrator/plans/<fecha>-<slug>/implementation.md`
- `.orchestrator/audits/<fecha>-audit/`

Esto sirve para dejar trazabilidad y poder retomar trabajo despues.

## Consejos Para Pedir Mejor

- Di el objetivo: que quieres conseguir.
- Di el alcance: que archivos, modulo o feature afecta.
- Di las restricciones: sin tocar Git, sin refactor grande, con tests, etc.
- Si ya hay un plan, indica la ruta exacta.

Ejemplo:

```text
Usa .codex/workflows/forge.md para implementar el plan en
.orchestrator/plans/2026-03-19-auth-fix/plan.md sin hacer commit y validando con tests.
```

## Regla Practica

Si quieres pensar, pide `think`.
Si quieres construir, pide `forge`.
Si quieres validar, pide `test` o `audit`.
Si quieres entregar cambios en Git, pide `pr` o `ship`.
