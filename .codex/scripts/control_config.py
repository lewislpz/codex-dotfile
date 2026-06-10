#!/usr/bin/env python3
from __future__ import annotations

import fnmatch
import json
import re
from pathlib import Path
from typing import Any

DEFAULT_CONFIG: dict[str, Any] = {
    "binding_excludes": [
        ".git/**",
        ".orchestrator/**",
        ".next/**",
        ".turbo/**",
        ".codex/evals/results/**",
        "**/.DS_Store",
        "**/__pycache__/**",
        "**/.next/**",
        "**/.turbo/**",
        "**/coverage/**",
        "**/dist/**",
        "**/node_modules/**",
        "coverage/**",
        "dist/**",
        "node_modules/**",
    ],
    "documentation_candidates": ["docs/00-general-docs.md", "README.md"],
    "forbidden_gate_commands": [":", "exit 0", "true"],
    "git": {"primary_branches": ["main", "master"], "remote": "origin"},
    "gates": {
        "low": ["consistency"],
        "medium": ["tests", "review"],
        "high": [
            "threat_model",
            "tests",
            "integration",
            "independent_review",
            "user_approval",
        ],
        "technical": ["consistency", "integration", "tests"],
    },
    "version": 1,
    "workspace_roots": [".orchestrator/plans", ".orchestrator/audits"],
}
GATE_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9_-]*$")


def find_repository_root(start: Path) -> Path:
    resolved = start.resolve()
    if resolved.is_file():
        resolved = resolved.parent
    for candidate in (resolved, *resolved.parents):
        if (candidate / ".codex").is_dir():
            return candidate
    return Path.cwd().resolve()


def load_config(start: Path = Path(".")) -> dict[str, Any]:
    path = find_repository_root(start) / ".codex" / "config.json"
    if not path.exists():
        return DEFAULT_CONFIG
    config = json.loads(path.read_text(encoding="utf-8"))
    return {
        **DEFAULT_CONFIG,
        **config,
        "gates": {**DEFAULT_CONFIG["gates"], **config.get("gates", {})},
        "git": {**DEFAULT_CONFIG["git"], **config.get("git", {})},
    }


def validate_config(start: Path = Path(".")) -> list[str]:
    config = load_config(start)
    errors = []
    if config.get("version") != 1:
        errors.append("config version must be 1")
    for field in (
        "binding_excludes",
        "documentation_candidates",
        "forbidden_gate_commands",
        "workspace_roots",
    ):
        values = config.get(field)
        if not isinstance(values, list) or not values or not all(
            isinstance(value, str) and value for value in values
        ):
            errors.append(f"config field must be a non-empty string list: {field}")
    gates = config.get("gates", {})
    for risk in ("low", "medium", "high"):
        if not isinstance(gates.get(risk), list) or not gates[risk]:
            errors.append(f"config requires gates for risk: {risk}")
    technical = set(gates.get("technical", []))
    declared = set().union(*(set(gates.get(risk, [])) for risk in ("low", "medium", "high")))
    if not technical <= declared:
        errors.append("technical gates must also be declared in a risk policy")
    for gate_name in declared | technical:
        if not isinstance(gate_name, str) or not GATE_NAME_PATTERN.fullmatch(gate_name):
            errors.append(f"invalid gate name: {gate_name}")
    git = config.get("git", {})
    if not git.get("remote") or not git.get("primary_branches"):
        errors.append("config requires Git remote and primary branches")
    return errors


def required_gates(start: Path, risk: str) -> set[str]:
    return set(load_config(start).get("gates", {}).get(risk, []))


def technical_gates(start: Path) -> set[str]:
    return set(load_config(start).get("gates", {}).get("technical", []))


def is_valid_gate_name(gate_name: str) -> bool:
    return bool(GATE_NAME_PATTERN.fullmatch(gate_name))


def is_excluded(path: str, patterns: list[str]) -> bool:
    normalized = path.replace("\\", "/")
    return any(
        fnmatch.fnmatch(normalized, pattern)
        or fnmatch.fnmatch(f"/{normalized}", f"*/{pattern}")
        for pattern in patterns
    )
