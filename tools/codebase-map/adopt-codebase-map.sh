#!/usr/bin/env bash
# Adopt the codebase-map kit into a project. Run from anywhere INSIDE the target repo AFTER
# copying this kit dir to the repo root as `codebase-map/` and filling map_extractors.py:
#
#   codebase-map/adopt-codebase-map.sh --scaffold
#
# Steps: conf (copy example if absent) -> extractors sanity -> python scaffold (map tree +
# FOUNDATION skeleton + seeded baseline + generated artifacts) -> gate template copied to
# GATE_FILE -> gate executed once (expect PASS on the freshly seeded tree).
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
HERE="$(cd "$(dirname "$0")" && pwd)"
PY="${MAP_PY:-python}"

[ "${1:-}" = "--scaffold" ] || { echo "usage: $0 --scaffold   (MAP_PY=python3 to override the launcher)"; exit 2; }

# -ef (same device+inode), not a string compare: MSYS/symlinks spell the same dir differently
[ "$HERE" -ef "$ROOT/codebase-map" ] || {
  echo "kit dir must live at <repo-root>/codebase-map/ (found: $HERE) — the gate template resolves it by that name"; exit 1; }

if [ ! -f "$ROOT/.codebase-map.conf" ]; then
  cp "$HERE/.codebase-map.conf.example" "$ROOT/.codebase-map.conf"
  echo "created .codebase-map.conf from the example — EDIT IT (MAP_ROOT, GATE_FILE), then re-run."
  exit 1
fi
. "$ROOT/.codebase-map.conf"
# CR-strip: a CRLF-committed conf on Linux keeps \r in sourced values (MSYS masks this)
MAP_ROOT="$(printf '%s' "${MAP_ROOT:-}" | tr -d '\r')"
GATE_FILE="$(printf '%s' "${GATE_FILE:-}" | tr -d '\r')"

[ -f "$HERE/map_extractors.py" ] || {
  cp "$HERE/map_extractors.template.py" "$HERE/map_extractors.py"
  echo "created codebase-map/map_extractors.py from the template — declare your inventories"
  echo "(see codebase-map/INVENTORY-DERIVATION.md), then re-run."
  exit 1; }

# Idempotent: an already-scaffolded map reconverges via --write (re-renders generated/ so a bumped
# version marker lands) instead of the gen_map.py --scaffold refuse-if-present wedge on re-run.
if [ -f "${MAP_ROOT:-memory/map}/FOUNDATION.md" ]; then
  "$PY" "$HERE/gen_map.py" --write || exit 1
else
  "$PY" "$HERE/gen_map.py" --scaffold || exit 1
fi

# Seed the affordance grace list ONCE (seed-if-absent): a fresh scaffold gets `exempt = []`; a repo
# re-adopting from a pre-affordance kit version gets its existing dossiers graced — green by
# construction either way. NOT re-seeded when present: the list is shrink-only, so re-seeding a
# repo with a real (non-exempt) violation would mask it.
if [ ! -f "${MAP_ROOT:-memory/map}/affordance-exempt.toml" ]; then
  "$PY" "$HERE/gen_map.py" --seed-affordance-baseline || exit 1
fi

GATE="${GATE_FILE:-tests/test_codebase_map.py}"
if [ -f "$GATE" ]; then
  echo "gate already present at $GATE — left untouched"
else
  mkdir -p "$(dirname "$GATE")"
  cp "$HERE/test_codebase_map.template.py" "$GATE"
  echo "gate installed at $GATE"
fi

echo "--- running the gate once (standalone mode) ---"
"$PY" "$GATE" || { echo "gate FAILED on the freshly seeded tree — fix before committing"; exit 1; }

echo "Adopted. Next:"
echo "  1. git add codebase-map/ .codebase-map.conf $GATE ${MAP_ROOT:-memory/map}/ && commit."
echo "  2. Verify your test suite collects the gate (it now enforces on every run/CI)."
echo "  3. Add the map section to your kickoff manifest (see MANIFEST-TEMPLATE.md) and the"
echo "     DoD line to your governance doc/CLAUDE.md."
echo "  4. Claim as you touch: the baseline only shrinks."
