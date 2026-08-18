#!/usr/bin/env bash
# check-line-length.test.sh — the failing case for every branch the gate carries.
#
# ONE scratch repo, reused. `git init` measured ~7s on this fleet and the gate roots itself with
# `git rev-parse`, so a repo per arm puts the suite past its own timeout while proving nothing.
#
# THE HARNESS RUNS SETUP AND THE GATE SEPARATELY, and that is not a style choice. An earlier draft
# ran `sh -c 'setup; gate; cleanup'` and read the rc of the CLEANUP — so every red arm reported 0 and
# the suite would have certified a gate that never fired. Setup happens first, the gate runs alone,
# and its rc is the one compared.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
GATE="$ROOT/tools/check-line-length.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

ASSERTIONS=0; FAILED=0
say_ok()   { ASSERTIONS=$((ASSERTIONS+1)); printf 'arm ok    %s\n' "$1"; }
say_fail() { ASSERTIONS=$((ASSERTIONS+1)); FAILED=$((FAILED+1)); printf 'arm FAIL  %s — %s\n' "$1" "$2"; }

W="$TMP/repo"; mkdir -p "$W/tools"
git -C "$W" init -q 2>/dev/null
git -C "$W" config user.email t@t; git -C "$W" config user.name t
cp "$GATE" "$W/tools/check-line-length.sh"

PY=python
line() { "$PY" -c "import sys;sys.stdout.write(sys.argv[1]*int(sys.argv[2])+chr(10))" "$1" "$2"; }

reset() {                      # a subject the gate passes on, and a declaration naming it
  line x 100 > "$W/subject.md"
  printf 'subject.md\t450\n' > "$W/tools/line-length-limits.txt"
  rm -f "$W/other.md"
}

# arm <label> <want-rc> <want-substring> [env] [gate-args...]
arm() {
  local label=$1 wrc=$2 want=$3 envv=$4; shift 4
  local out rc
  if [ -n "$envv" ]; then
    out=$(cd "$W" && env "$envv" bash tools/check-line-length.sh "$@" 2>&1); rc=$?
  else
    out=$(cd "$W" && bash tools/check-line-length.sh "$@" 2>&1); rc=$?
  fi
  if [ "$rc" -eq "$wrc" ] && printf '%s' "$out" | grep -qF "$want"; then say_ok "$label"
  else say_fail "$label" "expected rc $wrc naming '$want', got $rc: $(printf '%s' "$out" | head -2 | tr '\n' ' ')"; fi
}

reset
arm "control · a short subject passes" 0 "0 over 450" ""

reset; line y 451 >> "$W/subject.md"
arm "an over-length line reds naming the line and its length" 1 "is 451 characters" ""

reset; line y 450 >> "$W/subject.md"
arm "exactly at the limit passes" 0 "0 over 450" ""

# ---------------------------------------------------------------- resolution order
reset; printf 'subject.md\t200\n' > "$W/tools/line-length-limits.txt"; line y 300 >> "$W/subject.md"
arm "the DECLARATION beats the environment" 1 "limit of 200" "LINE_MAX=9999"

reset; line y 300 > "$W/other.md"
arm "an UNDECLARED subject honours the environment" 1 "resolved from the environment" "LINE_MAX=200" other.md

reset; line y 300 > "$W/other.md"
arm "an undeclared subject with no environment falls through to 450" 0 "limit from the default" "" other.md

reset; line y 300 >> "$W/subject.md"
arm "a POSITIONAL beats the declaration" 1 "resolved from a positional" "" subject.md 200

# ---------------------------------------------------------------- the exemption, and its boundary
reset; { printf '```\n'; line y 600; printf '```\n'; } >> "$W/subject.md"
arm "a long line INSIDE a fence does not red" 0 "0 over 450" ""

reset; { printf '| '; line y 600; } >> "$W/subject.md"
arm "a long line inside a TABLE does red" 1 "characters" ""

# ---------------------------------------------------------------- measurement and declaration hygiene
reset; line — 400 >> "$W/subject.md"
arm "a non-ASCII line is measured in CHARACTERS, not bytes" 0 "0 over 450" ""

reset; printf 'subject.md\t450\ngone.md\t450\n' > "$W/tools/line-length-limits.txt"
arm "a row naming an ABSENT path reds as stale" 1 "is stale" ""

reset; printf 'subject.md\tlots\n' > "$W/tools/line-length-limits.txt"
arm "a NON-NUMERIC limit is a named failure, not a shell error" 1 "is not a number" ""

reset; printf '# only a comment\n' > "$W/tools/line-length-limits.txt"
arm "a declaration selecting NO subject is cannot-run" 2 "would grade nothing" ""

printf '\n'
if [ "$FAILED" -ne 0 ]; then
  printf 'check-line-length.test.sh FAILED — %d arm(s)\n' "$FAILED"; exit 1
fi
FLOOR_ASSERTIONS=13
if [ "$ASSERTIONS" -lt "$FLOOR_ASSERTIONS" ]; then
  printf 'check-line-length.test.sh FAILED — ran %d assertion(s) against a floor of %d\n' \
    "$ASSERTIONS" "$FLOOR_ASSERTIONS"; exit 1
fi
printf 'PASS (%d assertions)\n' "$ASSERTIONS"
