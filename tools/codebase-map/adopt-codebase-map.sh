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
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh
# and tools/lib/resolve-python.test.sh reds if any copy drifts.
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# MAP_PY is this kit's published override (named in its usage line below and in
# WIRE-INTO-PROJECT.md), so it is the first candidate. Its old bare-`python` default was the
# weakest of the three detectors: on a python3-only host it named a launcher that does not exist.
PY=$(resolve_python "${MAP_PY:-}") || exit 2

[ "${1:-}" = "--scaffold" ] || { echo "usage: $0 --scaffold   (MAP_PY=python3 to override the launcher)"; exit 2; }   # gov:literal-python — inside a usage string

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
