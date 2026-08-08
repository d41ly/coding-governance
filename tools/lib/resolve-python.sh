#!/usr/bin/env bash
# The one python-launcher resolver, and it RUNS the candidate.
#
# Six scripts used to resolve a launcher by asking whether a name is on PATH. On Windows the
# Microsoft Store ships a `python3` STUB that answers that question and then exits 9009 without
# executing anything, so every one of them could pick a launcher that cannot run. Being on PATH is
# not evidence. Running is.
#
# USAGE — source it, then call it, and let the CALLER halt:
#
#   . "$HERE/../lib/resolve-python.sh"
#   PY=$(resolve_python) || exit 2
#   PY=$(resolve_python "${MAP_PY:-}") || exit 2     # a published per-kit override goes FIRST
#
# It echoes the launcher and returns non-zero; it does not exit. Most callers here run `set -u`
# WITHOUT `set -e`, so a function that merely `return 1`s cannot stop its caller — the value has to
# come back through a substitution the caller can test.
#
# A kit that is COPY-INSTALLED as a standalone directory (`cp -r <gov>/tools/memory-tree
# <project>/memory-tree`) cannot source this file: `../lib/` does not exist in the adopting repo.
# Those scripts carry the block between the markers below INLINE, byte-identical, and
# `resolve-python.test.sh` gates every copy against this one.

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
