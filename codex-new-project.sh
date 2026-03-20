#!/usr/bin/env bash

set -euo pipefail

script_dir="$(
  cd "$(dirname "${BASH_SOURCE[0]}")" && pwd
)"

usage() {
  cat <<'EOF'
Usage:
  ./codex-new-project <project-name>

Example:
  ./codex-new-project my-new-project

This creates a new project folder in the current directory and copies:
  - .codex
  - AGENTS.md
  - GUIDELINES.md
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 1
fi

project_name="$1"
destination="$PWD/$project_name"

if [[ -e "$destination" ]]; then
  echo "Destination already exists: $destination" >&2
  exit 1
fi

mkdir "$destination"
cp -R "$script_dir/.codex" "$destination/.codex"
cp "$script_dir/AGENTS.md" "$destination/AGENTS.md"
cp "$script_dir/GUIDELINES.md" "$destination/GUIDELINES.md"

echo "Project scaffold created in: $destination"
