#!/usr/bin/env bash
# adopt-drift-audit.sh — wire the drift-audit kit into a project.
#
# gov:kit drift-audit@1.0
#
# Run from anywhere INSIDE the target repo AFTER copying this kit dir to the repo root as
# `drift-audit/`:
#
#   drift-audit/adopt-drift-audit.sh            # seed the project layer + render the Skill
#   drift-audit/adopt-drift-audit.sh --check    # verify the rendered Skill still matches the kit
#
# Steps: require .memory-tree.conf (owned by the memory-tree kit; refuse, never create) -> seed
# drift_signals.py from the template IF ABSENT (never overwrite: the pins are measured project
# state) -> render .claude/skills/drift-audit/SKILL.md from SKILL.template.md -> report next steps.
#
# `--check` is the merge-bar arm: the rendered Skill must still match what the template plus the
# adopter's conf produce. It renders to a temp file and diffs, so a hand-edited Skill reds instead of
# silently outliving the kit it came from.
#
#   Exit 0 = adopted / in sync · 1 = out of sync or unusable · 2 = wrong invocation or not a repo.
set -u

MODE="${1:-}"
case "$MODE" in
  ""|--check) ;;
  *) echo "usage: $0 [--check]"; exit 2 ;;
esac

KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(git -C "$KIT_DIR" rev-parse --show-toplevel 2>/dev/null)" || { echo "drift-audit: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

CONF="$ROOT/.memory-tree.conf"
if [ ! -f "$CONF" ]; then
  cat >&2 <<'EOF'
drift-audit: .memory-tree.conf not found.

It is owned by the memory-tree kit, so this kit refuses rather than creating a second declaration of
the corpus root. Adopt memory-tree first, or write the minimum stub:

  MEMORY_ROOT=memory
  DISCIPLINES="<your disciplines>"
EOF
  exit 1
fi

# CR-strip: a CRLF-committed conf keeps \r in sourced values on Linux (MSYS masks this).
MEMORY_ROOT="$(tr -d '\r' < "$CONF" | sed -n 's/^MEMORY_ROOT=//p' | head -1)"
MEMORY_ROOT="${MEMORY_ROOT:-memory}"

SKILL_DIR="$ROOT/.claude/skills/drift-audit"
SKILL_OUT="$SKILL_DIR/SKILL.md"
TEMPLATE="$KIT_DIR/SKILL.template.md"
[ -f "$TEMPLATE" ] || { echo "drift-audit: SKILL.template.md missing from the kit"; exit 1; }

# The kit dir's name as the adopter sees it, so the rendered Skill's commands are copy-pasteable.
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh
# and tools/lib/resolve-python.test.sh reds if any copy drifts.
#
# This site spelled `python` BARE, which is why V5's migration missed it: the idiom ban matches
# `command -v`, and a bare launcher name carries no such marker. On a python3-only host — or one
# where the MS-Store stub answers for python3 — this line produced an empty KIT_REL and the
# `--check` leg then reported drift on a Skill that had never changed.
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
DA_PY=$(resolve_python) || exit 2
KIT_REL="$("$DA_PY" -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]).replace(os.sep,'/'))" "$KIT_DIR" "$ROOT")"
[ -n "$KIT_REL" ] || { echo "drift-audit: could not derive the kit path — refusing to render a Skill with an empty command prefix"; exit 2; }

render() { # -> stdout; LF only (the rendered Skill is pinned LF in .gitattributes)
  sed -e "s|{{KIT_DIR}}|$KIT_REL|g" -e "s|{{MEMORY_ROOT}}|$MEMORY_ROOT|g" "$TEMPLATE" | tr -d '\r'
}

if [ "$MODE" = "--check" ]; then
  [ -f "$SKILL_OUT" ] || { echo "drift-audit: $SKILL_OUT not rendered — run $0"; exit 1; }
  TMP="$(mktemp)"; trap 'rm -f "$TMP"' EXIT
  render > "$TMP"
  if ! diff -q <(tr -d '\r' < "$SKILL_OUT") "$TMP" >/dev/null 2>&1; then
    echo "drift-audit: $SKILL_OUT is out of sync with SKILL.template.md + .memory-tree.conf"
    echo "  re-render with: $0"
    diff <(tr -d '\r' < "$SKILL_OUT") "$TMP" | head -20
    exit 1
  fi
  # The project layer must exist for the report to run at all; --check is where a half-adoption shows.
  [ -f "$KIT_DIR/drift_signals.py" ] || { echo "drift-audit: drift_signals.py missing — the report cannot run"; exit 1; }
  echo "drift-audit: in sync (skill rendered from template, project layer present)"
  exit 0
fi

# Seed the project layer ONCE. Never overwrite: PINS are measured project state, and re-seeding a
# repo that already tuned them would silently reset every ratchet to the template's zeros.
if [ -f "$KIT_DIR/drift_signals.py" ]; then
  echo "drift-audit: drift_signals.py already present — left untouched"
else
  cp "$KIT_DIR/drift_signals.template.py" "$KIT_DIR/drift_signals.py"
  echo "drift-audit: seeded drift_signals.py from the template — FILL IT before trusting the report"
fi

mkdir -p "$SKILL_DIR"
render > "$SKILL_OUT"
echo "drift-audit: rendered $SKILL_OUT"

cat <<EOF

Next:
  1. Fill $KIT_REL/drift_signals.py — PRODUCT_GLOBS at minimum.
  2. Run:  python $KIT_REL/drift_report.py
  3. Seed PINS at the values you just measured, not at zero, then re-run with --check (expect 0).
  4. Wire the --check arm into your gate manifest so a regression reds.
EOF
