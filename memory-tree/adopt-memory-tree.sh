#!/usr/bin/env bash
# Scaffold an empty, hygiene-passing structured memory tree from .memory-tree.conf.
# For a NEW project. (A project MIGRATING an existing docs tree does that once as its own landing —
# see README.md "Adopting into an existing tree"; the tree shape below is the target either way.)
#
#   memory-tree/adopt-memory-tree.sh --scaffold
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
DISCIPLINES="architecture deployment blocks design performance"
FAMILIES="architecture:ARCH deployment:DEPLOY blocks:BLOCK design:DES performance:PERF"
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
M="$MEMORY_ROOT"
HERE="$(cd "$(dirname "$0")" && pwd)"
FAMILY_of() { local p; for p in $FAMILIES; do case "$p" in "$1:"*) echo "${p#*:}"; return;; esac; done; }

[ "${1:-}" = "--scaffold" ] || { echo "usage: $0 --scaffold"; exit 2; }
[ -e "$M" ] && { echo "$M/ already exists — refusing to overwrite. Remove it or migrate manually."; exit 1; }

mkdir -p "$M/project/journal"
# root index + rules
[ -f "$HERE/HYGIENE.template.md" ] && cp "$HERE/HYGIENE.template.md" "$M/HYGIENE.md" || echo "# ${M}/ retention & hygiene" > "$M/HYGIENE.md"
{ echo "# $M/ — project memory index"; echo
  echo "Structured, machine-linted project memory. Shape + rules: [HYGIENE.md](HYGIENE.md). Generated tree: [TREE.md](TREE.md)."; echo
  echo "## Disciplines"; echo
  for d in $DISCIPLINES; do echo "- [$d/]($d/) — decisions \`$(FAMILY_of "$d")-<slug>-<seq>\`, per-feature builds/."; done
  echo; echo "## Cross-discipline"; echo; echo "- [project/](project/) — session machinery: MEMORY.md, IN-FLIGHT.md, journal/, notes."
} > "$M/README.md"
# project/
printf '# %s/project/ — session machinery\n\n- MEMORY.md — memory-note index (one line per note).\n- IN-FLIGHT.md — session ledger.\n- journal/ — per-session journals.\n' "$M" > "$M/project/README.md"
printf '# Memory Index\n\n> One line per durable note.\n' > "$M/project/MEMORY.md"
printf '# In-flight ledger\n\nOne row per in-flight session — node · slug · branch · streams · status.\n\n| Node | Branch | Streams | Slug · ids | Status |\n|------|--------|---------|------------|--------|\n' > "$M/project/IN-FLIGHT.md"
printf '# legacy-files.txt — recording files kept under historical names (permanent C5 exemption). Empty = strict.\n' > "$M/project/legacy-files.txt"
printf '# curation-debt.txt — index files pending slimming (exempt from checks 6/7/8 while listed). Empty = fully strict.\n' > "$M/project/curation-debt.txt"
touch "$M/project/journal/.gitkeep"
# disciplines
for d in $DISCIPLINES; do
  fam=$(FAMILY_of "$d")
  mkdir -p "$M/$d"
  { echo "# $M/$d/"; echo; echo "Decision log \`$fam-<slug>-<seq>\`, backlog, per-feature builds/. Shape: [../HYGIENE.md](../HYGIENE.md)."; } > "$M/$d/README.md"
  printf '# %s decisions — index\n\n> One line per decision, append-only. Detail in decisions/.\n' "$d" > "$M/$d/DECISIONS.md"
  printf '# %s backlog\n\n> Mutable. Each row leads with one status token (OPEN…WONTDO).\n' "$d" > "$M/$d/BACKLOG.md"
done
# Stage the tree FIRST so the generator (git ls-files) sees the files, then generate + re-stage TREE.md.
git add "$M" >/dev/null 2>&1 || true
bash "$HERE/gen-memory-tree.sh" --write
git add "$M" >/dev/null 2>&1 || true

echo "Scaffolded $M/ ($(echo $DISCIPLINES | wc -w) disciplines) — staged."
echo "Next:"
echo "  1. git add $M/ && commit."
echo "  2. Copy .memory-tree.conf.example to the repo root as .memory-tree.conf (already read if present)."
echo "  3. Wire the gate: add 'bash memory-tree/check-memory-hygiene.sh' to CI + your local gate runner;"
echo "     add a pre-commit fast leg calling it with --staged on staged $M/** paths."
echo "  4. Verify: bash memory-tree/check-memory-hygiene.sh ; echo \$?   (expect 0)"
