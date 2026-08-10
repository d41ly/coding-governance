#!/usr/bin/env bash
# merge-rows.sh — resolve a python launcher and exec this kit's merge driver with it.
#
#   git config merge.rows.driver 'bash <kit>/merge-rows.sh %O %A %B %P'
#
# WHY THIS FILE EXISTS. `merge-rows.py` is the row-keyed three-way driver for the authored indexes
# (`DECISIONS.md`, `backlog/*.md`). Git execs a `merge.<driver>.driver` command line itself and never
# goes through a gate runner, so nothing can substitute a resolved launcher into it — the launcher
# has to be resolved HERE. Naming one literally is the Microsoft-Store-stub failure the resolver
# exists for, and the invocation ban in `tools/lib/resolve-python.test.sh` refuses it repo-wide.
#
# WHY IT IS NOT `tools/lib/pyrun.sh`. That shim SOURCES the canonical resolver from a sibling, which
# only works inside the governance repo. A copy-installed kit is a standalone directory: `../lib/`
# does not exist in an adopting repo, so an adopter wiring the driver named a shim they never
# received. Git then execs a command that cannot start, and a driver that never starts never writes
# `%A` — so git reports CONFLICT and leaves the path holding OURS-ONLY content with NO conflict
# markers. Silent content loss on an append-only record. This file closes that by travelling INSIDE
# the kit and carrying the resolver inline, which is the established rule for every copy-installed
# kit file; `tools/lib/` remains gov-internal and ships nothing.
#
# NO `cd`. Git invokes a merge driver with the cwd at the top of the working tree and hands it
# `%O %A %B` relative to that, so moving the cwd can only break paths that are already correct.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does not
# exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh and
# tools/lib/resolve-python.test.sh reds if any copy drifts.
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
PY=$(resolve_python) || exit 2
exec "$PY" "$HERE/merge-rows.py" "$@"
