#!/usr/bin/env bash
# check-microformats.test.sh — the failing case for every predicate the gate carries.
#
# A gate is not landed until its failing case has been OBSERVED, and a gate with seven predicates
# needs seven observations rather than one. Each arm below feeds a fixture that violates exactly one
# clause and asserts the gate names THAT clause, so a predicate that stops discriminating is caught
# by the arm for the clause it stopped seeing.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
GATE="$ROOT/tools/check-microformats.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

ASSERTIONS=0
FAILED=0
say_ok()   { ASSERTIONS=$((ASSERTIONS+1)); printf 'arm ok    %s\n' "$1"; }
say_fail() { ASSERTIONS=$((ASSERTIONS+1)); FAILED=$((FAILED+1)); printf 'arm FAIL  %s — %s\n' "$1" "$2"; }

# ONE scratch repo, reused. Every arm rewrites charter.md inside it rather than initialising its
# own: `git init` measured ~7s on this node, and fourteen of them put the suite past its own
# timeout while proving nothing a single repo does not.
WORK="$TMP/repo"
mkdir -p "$WORK"
git -C "$WORK" init -q 2>/dev/null
git -C "$WORK" config user.email t@t; git -C "$WORK" config user.name t

# A fixture the gate PASSES on, so each arm breaks exactly one thing.
fixture() {
  local d=$1
  cat > "$d/charter.md" <<'FIX'
Some prose above the block.

<!-- microformats -->
- `committed — <sha> · <branch> · <subject>`
- `gates — GREEN · <leg> · <leg> …`
- `SPEC — [<unit-id>](<path>) · review <ids|none>`
<!-- /microformats -->

Some prose below it.
FIX
}

# arm <label> <expect: ok|red|cannot> <expected-substring> <sed-script-or-empty>
arm() {
  local label=$1 expect=$2 want=$3 script=${4:-}
  local d="$WORK"
  fixture "$d"
  [ -n "$script" ] && sed -i "$script" "$d/charter.md"
  local out rc
  out=$(cd "$d" && bash "$GATE" charter.md 2>&1); rc=$?
  case "$expect" in
    ok)     [ "$rc" -eq 0 ] && say_ok "$label" || say_fail "$label" "expected 0, got $rc: $out" ;;
    red)    if [ "$rc" -eq 1 ] && printf '%s' "$out" | grep -qF "$want"
            then say_ok "$label"; else say_fail "$label" "expected rc 1 naming '$want', got $rc: $out"; fi ;;
    cannot) if [ "$rc" -eq 2 ] && printf '%s' "$out" | grep -qF "$want"
            then say_ok "$label"; else say_fail "$label" "expected rc 2 naming '$want', got $rc: $out"; fi ;;
  esac
}

arm "control · a conforming block passes" ok ""

# --- the could-not-run branch. THREE fence failures, because the anchor is the fence and the arm
# --- for a renamed heading could not be built: the section has no heading to rename.
arm "the fence pair removed is cannot-run, not clean" cannot \
  "not delimited by exactly one fence pair" '/microformats/d'
arm "an unclosed fence is cannot-run" cannot \
  "not delimited by exactly one fence pair" '\|<!-- /microformats -->|d'
arm "a duplicated fence pair is cannot-run" cannot \
  "not delimited by exactly one fence pair" \
  '\|<!-- /microformats -->|a\
<!-- microformats -->\
<!-- /microformats -->'

# --- the anti-vacuity pair
arm "a fenced block with no definition is cannot-run" cannot \
  "encloses no definition line" '/^- `/d'
arm "a derivation missing its sentinel reds" red \
  "lost its frozen sentinel member" 's/^- `committed/- `landed/'

# --- one arm per grammar clause
arm "a second joiner reds on the count" red \
  "joiners rather than exactly one" 's/· <branch> ·/— <branch> ·/'
arm "a field ahead of the joiner reds on POSITION" red \
  "puts a field ahead of its joiner" 's/^- `committed — /- `committed <sha> — /'
arm "a bare parenthesis reds" red \
  "carries a bare parenthesis" 's/· <subject>/· (<subject>)/'
arm "a markdown link does NOT red as a parenthesis" ok "" \
  's/· <subject>/· [<x>](<y>)/'
arm "a colon label reds" red \
  "uses a colon as a label" 's/· <branch>/· branch: <branch>/'
arm "a colon glued to a value does NOT red" ok "" \
  's/· <branch>/· :<port>/'
arm "an upper-case placeholder reds" red \
  "not a lowercase angle-bracket name" 's/<subject>/<SUBJECT>/'

printf '\n'
if [ "$FAILED" -ne 0 ]; then
  printf 'check-microformats.test.sh FAILED — %d arm(s)\n' "$FAILED"
  exit 1
fi
FLOOR_ASSERTIONS=13
if [ "$ASSERTIONS" -lt "$FLOOR_ASSERTIONS" ]; then
  printf 'check-microformats.test.sh FAILED — ran %d assertion(s) against a floor of %d\n' \
    "$ASSERTIONS" "$FLOOR_ASSERTIONS"
  exit 1
fi
printf 'PASS (%d assertions)\n' "$ASSERTIONS"
