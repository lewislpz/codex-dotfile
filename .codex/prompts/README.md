# Slash Prompts

Este entorno no expone un parser nativo de slash commands. Aqui se usa una convencion simple:

- cada alias `/nombre` corresponde a un archivo en `.codex/prompts/nombre.md`
- cada archivo contiene la expansion recomendada del prompt
- puedes invocarlos escribiendo el alias en tu mensaje y pidiendole a Codex que use ese prompt guardado

Ejemplos de uso:

```text
Usa /think para analizar esta feature: login con Google.
```

```text
Usa /forge sobre el ultimo plan aprobado y no hagas commit.
```

```text
Usa /resume para continuar el trabajo desde el ultimo PLAN_PATH.
```

## Aliases Disponibles

- `/think`: analisis y plan sin tocar codigo de producto
- `/forge`: implementacion guiada por plan
- `/test`: matriz de pruebas y TDD
- `/audit`: auditoria read-only
- `/pr`: entrega en rama con push y enlace de PR, solo si lo pides
- `/ship`: merge o release, solo si lo pides
- `/resume`: retomar el ultimo plan o auditoria activa

## Regla Practica

Si mas adelante conectas un launcher real de slash commands, estos archivos ya te sirven como fuente de verdad para la expansion de cada alias.
