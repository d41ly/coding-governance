#!/usr/bin/env bash
# Adopt the codebase-map kit into a project. Run it BY PATH from anywhere, after copying this kit
# dir into the target repo and filling map_extractors.py:
#
#   <kit-dir>/adopt-codebase-map.sh --scaffold
#
# The kit dir's NAME is fixed (`codebase-map` — the gate template resolves the kit by it), but its
# PREFIX under the repo root is free: `<root>/codebase-map/` and `<root>/tools/codebase-map/` are
# both supported, matching map_lib.resolve_root.
#
# Steps: conf (copy example if absent) -> extractors sanity -> python scaffold (map tree +
# FOUNDATION skeleton + seeded baseline + generated artifacts) -> gate template copied to
# GATE_FILE -> gate executed once (expect PASS on the freshly seeded tree).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)" || exit 2
# ROOT is the repo containing the KIT, not the repo containing the cwd. Anchoring on the script's
# own location is what lets it be run by path from anywhere, and is the same anchor map_lib uses.
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)" || exit 2
# The kit's path under that root, asked of git rather than derived by trimming "$ROOT" off "$HERE":
# MSYS and symlinks spell the same directory two ways, which is why the old check used `-ef`.
KIT_REL="$(cd "$HERE" && git rev-parse --show-prefix)" || exit 2
KIT_REL="${KIT_REL%/}"
cd "$ROOT" || exit 2
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

# Only the kit dir's NAME is load-bearing (the gate template resolves the kit by it); the prefix is
# free. The kit must also be INSIDE the repo, not be the repo root itself.
[ -n "$KIT_REL" ] || {
  echo "the kit dir is the repo root itself ($ROOT) — copy the kit in as a directory named codebase-map/"; exit 1; }
case "$KIT_REL" in
  codebase-map|*/codebase-map) ;;
  *) echo "the kit dir must be NAMED codebase-map (found: $KIT_REL) — the gate template resolves it by that name; any prefix above it is fine"; exit 1;;
esac

if [ ! -f "$ROOT/.codebase-map.conf" ]; then
  cp "$HERE/.codebase-map.conf.example" "$ROOT/.codebase-map.conf"
  # Stamp the digest command with THIS install's prefix, so the created conf is right by
  # construction rather than right if the adopter remembers. Keyed on the KEY name, never on the
  # example's value, so the two cannot drift. Temp-file rewrite, not `sed -i`: BSD sed (macOS)
  # needs an argument to -i and GNU sed refuses one. Only ever touches a file just copied from the
  # example, so there is no user edit to clobber.
  if sed "s|^MAP_DIFF_CMD=.*|MAP_DIFF_CMD=\"python $KIT_REL/map_diff.py\"|" \
       "$ROOT/.codebase-map.conf" > "$ROOT/.codebase-map.conf.new"; then
    mv "$ROOT/.codebase-map.conf.new" "$ROOT/.codebase-map.conf"
  else
    rm -f "$ROOT/.codebase-map.conf.new"
    echo "note: could not stamp MAP_DIFF_CMD — set it to \"python $KIT_REL/map_diff.py\" by hand."
  fi
  echo "created .codebase-map.conf from the example — EDIT IT (MAP_ROOT, GATE_FILE), then re-run."
  echo "MAP_DIFF_CMD was stamped for this install prefix: python $KIT_REL/map_diff.py"
  exit 1
fi
. "$ROOT/.codebase-map.conf"
# CR-strip: a CRLF-committed conf on Linux keeps \r in sourced values (MSYS masks this)
MAP_ROOT="$(printf '%s' "${MAP_ROOT:-}" | tr -d '\r')"
GATE_FILE="$(printf '%s' "${GATE_FILE:-}" | tr -d '\r')"

[ -f "$HERE/map_extractors.py" ] || {
  cp "$HERE/map_extractors.template.py" "$HERE/map_extractors.py"
  echo "created $KIT_REL/map_extractors.py from the template — declare your inventories"
  echo "(see $KIT_REL/INVENTORY-DERIVATION.md), then re-run."
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
echo "  1. git add $KIT_REL/ .codebase-map.conf $GATE ${MAP_ROOT:-memory/map}/ && commit."
echo "  2. Verify your test suite collects the gate (it now enforces on every run/CI)."
echo "  3. Add the map section to your kickoff manifest (see MANIFEST-TEMPLATE.md) and the"
echo "     DoD line to your governance doc/CLAUDE.md."
echo "  4. Claim as you touch: the baseline only shrinks."
