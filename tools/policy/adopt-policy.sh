#!/usr/bin/env bash
# adopt-policy.sh — scaffold a repository's policy file, and check it against the policy catalogue.
#
#   bash <this kit>/adopt-policy.sh --scaffold [--target <repo>]   # write .governance/policy.toml if absent
#   bash <this kit>/adopt-policy.sh --check [--target <repo>]      # every policy arm over <repo>
#
# <repo> defaults to the git top level of the working directory.
#
# `--scaffold` writes the starter file `policy.py scaffold` prints, and ONLY when no file is there:
# a policy file is the repository's own from its first write, so an existing one is kept byte for
# byte and the script says "kept". `--check` is `check_policy.py --repo <repo>`, whose exit it returns.
#
# The kit dir is this script's own directory, never spelled, so the adopter runs from wherever the
# kit is installed.
#
#   Exit 0 = written, kept or green · 1 = red, or the write failed · 2 = wrong invocation, no
#   repository, or no python.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)" || exit 2
USAGE="usage: bash <this kit>/adopt-policy.sh --scaffold | --check [--target <repo>]"

MODE=""
TARGET=""
while [ $# -gt 0 ]; do
  case "$1" in
    --scaffold|--check) [ -z "$MODE" ] || { echo "$USAGE"; exit 2; }
                        MODE="$1" ;;
    --target) [ $# -ge 2 ] || { echo "$USAGE"; exit 2; }
              TARGET="$2"; shift ;;
    *) echo "$USAGE"; exit 2 ;;
  esac
  shift
done
[ -n "$MODE" ] || { echo "$USAGE"; exit 2; }
if [ -z "$TARGET" ]; then
  TARGET="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "policy: the working directory is in no git repository; name one with --target <repo>"; exit 2; }
fi
[ -d "$TARGET" ] || { echo "policy: --target $TARGET is not a directory"; exit 2; }

# The resolver, INLINE. This kit is copy-installed as a standalone directory, so the shared lib
# does not exist in an adopting repo. The block below is byte-identical to the canonical copy its
# own marker line names, and that copy's self-test reds if any inline copy drifts.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
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

if [ "$MODE" = "--check" ]; then
  "$PY" -B "$HERE/check_policy.py" --repo "$TARGET"
  exit $?
fi

FILE="$TARGET/.governance/policy.toml"
if [ -e "$FILE" ]; then
  echo "kept     $FILE — a policy file is the repository's own, and the scaffold never overwrites it"
  exit 0
fi
mkdir -p "$TARGET/.governance" || exit 1
if "$PY" -B "$HERE/policy.py" scaffold > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"; then
  echo "wrote    $FILE"
  exit 0
fi
rm -f "$FILE.tmp"
echo "policy: the scaffold could not be written to $FILE"
exit 1
