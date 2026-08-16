#!/usr/bin/env bash
# Fixture self-test for check-testsuite-counts.sh — every refusal armed by a POSITIVE assertion
# naming its own failure text, each paired with a green control. A check that was never reached is
# silent for the same reason a passing one is.
#
#   bash tools/check-testsuite-counts.test.sh    # "PASS (N assertions)" + exit 0 = good
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
st=0; n=0
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }

cd "$TMP" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t
mkdir -p tools memory/project
cp "$HERE/check-testsuite-counts.sh" tools/
SCRIPT="$TMP/tools/check-testsuite-counts.sh"
run() { bash "$SCRIPT" 2>&1; }

# A COMPLIANT suite: the agreed count line plus a pinned floor.
mk_ok()  { printf 'FLOOR_ASSERTIONS=3\necho "PASS ($n assertions)"\n' > "$1"; }
# SILENT: no count at all, which is the state 12 of 27 suites were in when the leg was written.
mk_bad() { printf 'echo done\n' > "$1"; }
# A floor pinned with nothing printing a count to compare it against.
mk_floor_only() { printf 'FLOOR_ASSERTIONS=3\necho done\n' > "$1"; }

manifest() { # one argv entry per named suite
  { echo '['
    sep=""
    for f in "$@"; do printf '%s  { "name": "%s", "argv": ["bash", "%s"] }\n' "$sep" "$f" "$f"; sep=","; done
    echo ']'
  } > tools/gate-legs.json
}
: > memory/project/testsuite-count-waivers.txt

# ---- GREEN CONTROL first. Every red arm below is worthless if a conforming tree is not silent.
mk_ok tools/a.test.sh; manifest tools/a.test.sh
out=$(run); rc=$?
same "a conforming tree exits 0" "$rc" "0"
same "a conforming tree prints nothing" "$out" ""

# ---- a suite printing NO count, and not waived.
mk_bad tools/b.test.sh; manifest tools/a.test.sh tools/b.test.sh
out=$(run)
hit "$out" "a self-test on the bar prints no executed assertion count against a floor, so a block of its arms could be stranded past an exit and the suite would still report success: tools/b.test.sh"
same "and it exits non-zero" "$(run >/dev/null 2>&1; echo $?)" "1"

# ...WAIVED, it is silent — that is what lets the leg land green over a real tree and ratchet.
printf 'tools/b.test.sh\n' > memory/project/testsuite-count-waivers.txt
same "a waived suite is silent" "$(run)" ""

# ---- a STALE waiver: the suite now complies, so the row hides nothing and must red. Without this
# ---- the list only ever grows, which is the opposite of a ratchet.
mk_ok tools/b.test.sh
hit "$(run)" "a testsuite-count waiver names a suite that now complies, so the list has stopped shrinking and the row hides nothing: tools/b.test.sh"

# ---- a waiver naming a suite the manifest does not run at all.
mk_bad tools/b.test.sh
printf 'tools/b.test.sh\ntools/ghost.test.sh\n' > memory/project/testsuite-count-waivers.txt
hit "$(run)" "a testsuite-count waiver names a suite the gate manifest does not run, so it waives nothing and outlives what it was written for: tools/ghost.test.sh"

# ---- a floor with no count line to compare it to. Distinct message, because the fix is different.
: > memory/project/testsuite-count-waivers.txt
mk_floor_only tools/c.test.sh; manifest tools/a.test.sh tools/c.test.sh
hit "$(run)" "a self-test pins a floor but does not print the agreed count line, so nothing compares the floor to anything: tools/c.test.sh"

# ---- THE DERIVED-POPULATION ARM. Adding a suite to the manifest reds the leg with NO edit to the
# ---- leg itself; a hand-kept list would have stayed green and that is the defect being prevented.
manifest tools/a.test.sh
same "one compliant suite, silent" "$(run)" ""
mk_bad tools/d.test.sh; manifest tools/a.test.sh tools/d.test.sh
hit "$(run)" "tools/d.test.sh"

# ---- a manifest naming a suite that is not on disk must NOT be skipped silently.
manifest tools/a.test.sh tools/gone.test.sh
hit "$(run)" "the gate manifest names a self-test this leg cannot read, and skipping it silently removes it from the population: tools/gone.test.sh"

# ---- an EMPTY population is a refusal, not a pass. This is the vacuous-selector shape the leg
# ---- exists to prevent, applied to the leg itself.
manifest
hit "$(run)" "the gate manifest names no *.test.sh, so this leg would grade an empty population"

FLOOR_ASSERTIONS=12
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
