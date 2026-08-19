#!/usr/bin/env bash
# adopt-playbook.sh — render the governance charter into a target, and verify it later.
#
#   bash tools/playbook/adopt-playbook.sh --target <repo>            # write the region
#   bash tools/playbook/adopt-playbook.sh --target <repo> --check    # assert it still matches
#   bash tools/playbook/adopt-playbook.sh --selftest                 # the engine's own arms
#
# This is the shape every other adopter in this repo has, which is why the playbook entry no longer
# carries a `why_no_adopter` reason: installation stopped being a copy an operator finishes by hand.
#
# `--check` asserts TWO things with SEPARATE messages, because they are two questions: that the
# rendered region still equals a fresh render, and that no placeholder survived it. A target whose
# descriptor declares nothing for a key renders a region that is perfectly in sync and still tells
# the agent to invoke a placeholder's name.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)

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

PY_BIN=$(resolve_python "${PLAYBOOK_PY:-}") || exit 2

# The verbs this shim accepts, spelled here rather than only in the engine, so a reader of the
# adopter can see that `--check` exists without opening the Python. The engine parses argv itself;
# this case is a declaration, not a second parser.
case " $* " in
  *" --selftest "*) : ;;   # the engine's arms, over its own temp fixtures — no target is read
  *" --check "*)    : ;;   # assert the region still matches a fresh render, and that none survived
  *)                : ;;   # write the region
esac

exec "$PY_BIN" "$HERE/render_playbook.py" "$@"
