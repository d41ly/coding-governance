#!/usr/bin/env bash
# lib-selftest.test.sh — the arms for tools/lib/lib-selftest.sh. TOOL-aQuenchedHarness-5 S7.
#
# IT DOES NOT USE THE HARNESS TO TEST ITSELF, and that is not squeamishness: half of what must be
# graded here is the harness FAILING correctly, and an arm that fails inside the harness fails the
# suite that contains it. So each case drives the harness in a SUBPROCESS and grades its output and
# exit status from outside — the same shape every other suite in this repo uses on its own subject.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "lib-selftest-test: not a git tree"; exit 2; }
cd "$ROOT" || exit 2
LIB="$HERE/lib-selftest.sh"
[ -f "$LIB" ] || { echo "lib-selftest-test: no harness at $LIB"; exit 2; }

TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP" 2>/dev/null' EXIT
n=0; bad=0
ok()   { n=$((n+1)); printf 'ok   %s\n' "$1"; }
nope() { n=$((n+1)); bad=1; printf 'nope %s — %s\n' "$1" "${2:-}"; }

# FLOOR_ASSERTIONS grades whether this SUITE still carries its arms, not whether this box could run
# them. A suite that silently shrinks reports green over a population it stopped grading.
FLOOR_ASSERTIONS=17

# run_harness <name> <body> -> writes $TMP/<name>.out, returns the harness's exit status
run_harness() {
  local name=$1 body=$2
  { printf 'set -u\n. "%s"\n' "$LIB"; printf '%s\n' "$body"; } > "$TMP/$name.sh"
  ( cd "$ROOT" && bash "$TMP/$name.sh" ) > "$TMP/$name.out" 2>&1
}

FIX='mkfix() { printf "base\n" > subject.txt; mkdir -p sub; }
build_fixture mkfix || exit 2'

# ---- 1. a passing arm passes, and the suite exits 0 --------------------------------------------
run_harness pass "$FIX
arm \"a control arm\" 0 \"base\" \"true\" \"cat subject.txt\"
run_arms t"
rc=$?
[ "$rc" = 0 ] && ok "a suite whose every arm holds exits 0" || nope "a passing suite exited $rc" "$(head -3 "$TMP/pass.out")"
grep -q '^PASS (1 arms' "$TMP/pass.out" && ok "and reports its own arm count" || nope "no PASS line with a count" "$(cat "$TMP/pass.out")"

# ---- 2. THE FAILING CASE. Charter section 7: a gate is not landed until this has been observed --
run_harness fail "$FIX
arm \"an arm whose expectation is not met\" 0 \"NOTPRESENT\" \"true\" \"cat subject.txt\"
run_arms t"
rc=$?
[ "$rc" = 1 ] && ok "a suite with a failing arm exits 1" || nope "a failing suite exited $rc" "$(head -3 "$TMP/fail.out")"
grep -q '^FAIL  an arm whose expectation is not met' "$TMP/fail.out" \
  && ok "and NAMES the arm that failed, with what it expected" || nope "the failure did not name its arm" "$(cat "$TMP/fail.out")"

# ---- 3. ISOLATION. The property the whole design exists for: a staged break must not leak into the
# ----    next arm. The suites this harness replaces share ONE mutated fixture directory, so running
# ----    their arms concurrently without this would corrupt them silently.
run_harness iso "$FIX
arm \"stages a break\"      0 \"BROKE\" \"printf 'BROKE\\\\n' > subject.txt\" \"cat subject.txt\"
arm \"must not see it\"     0 \"base\"  \"true\"                              \"cat subject.txt\"
run_arms t"
rc=$?
[ "$rc" = 0 ] && ok "an arm's staged break does not reach the next arm's fixture" \
              || nope "isolation failed" "$(cat "$TMP/iso.out")"

# ---- 4. ORDER STABILITY. Arms execute in whatever order the pool frees a slot; the report is by
# ----    declaration index. A suite whose output moves with the width has byte-pins nobody can trust.
BODY="$FIX
arm \"first\"  0 \"base\" \"true\" \"cat subject.txt\"
arm \"second\" 0 \"base\" \"true\" \"cat subject.txt\"
arm \"third\"  0 \"base\" \"true\" \"cat subject.txt\"
arm \"fourth\" 0 \"base\" \"true\" \"cat subject.txt\"
run_arms t"
SELFTEST_INNER_WIDTH=1 run_harness w1 "$BODY"
SELFTEST_INNER_WIDTH=4 run_harness w4 "$BODY"
if diff <(grep -E '^(ok|FAIL) ' "$TMP/w1.out") <(grep -E '^(ok|FAIL) ' "$TMP/w4.out") >/dev/null 2>&1; then
  ok "the arm lines are byte-identical at width 1 and width 4"
else
  nope "reporting order moved with the width" "$(diff "$TMP/w1.out" "$TMP/w4.out" | head -4)"
fi
# AND THE WIDTH IS REPORTED, so a reader can tell a serial run from a parallel one. This is the ONE
# line that legitimately differs between the two, and asserting it stops a future edit from making
# the widths indistinguishable and calling that byte-stability.
grep -q 'width 1)' "$TMP/w1.out" && grep -q 'width 4)' "$TMP/w4.out" \
  && ok "while the summary names the width each run actually used" \
  || nope "the summary does not report its width" "$(tail -1 "$TMP/w1.out"); $(tail -1 "$TMP/w4.out")"

# ---- 5. THE POOL WIDTH IS READ, NEVER RESOLVED. If this harness resolved the profile row itself,
# ----    it and run-selftests.sh would each apply the same declared width and the product would be
# ----    width squared — 64 concurrent processes at width 8, measured by a spec audit.
grep -q 'SELFTEST_INNER_WIDTH' "$LIB" && ! grep -q 'print-profile\|gate-profiles' "$LIB" \
  && ok "the harness reads SELFTEST_INNER_WIDTH and resolves no profile of its own" \
  || nope "the harness resolves a width itself, which squares the pool" ""

# ---- 6. A WEDGED ARM reds by name and the suite still completes ---------------------------------
run_harness wedge "SELFTEST_ARM_TIMEOUT=3
$FIX
arm \"an arm that wedges\" 0 \"never\" \"true\" \"sleep 60\"
arm \"a healthy arm after it\" 0 \"base\" \"true\" \"cat subject.txt\"
run_arms t"
rc=$?
[ "$rc" = 1 ] && ok "a wedged arm reds rather than hanging the suite" || nope "the wedged suite exited $rc" "$(cat "$TMP/wedge.out")"
grep -q '^ok    a healthy arm after it' "$TMP/wedge.out" \
  && ok "and the arms after it still run — one wedge is not a suite-wide stall" \
  || nope "a wedged arm stopped the suite" "$(cat "$TMP/wedge.out")"

# ---- 7. AN EMPTY POPULATION IS A REFUSAL, never a green line ------------------------------------
run_harness empty 'mkfix() { :; }
build_fixture mkfix || exit 2
run_arms t'
rc=$?
[ "$rc" = 2 ] && ok "a suite that declared no arms REFUSES rather than reporting a clean sweep" \
              || nope "an empty suite exited $rc" "$(cat "$TMP/empty.out")"

# ---- 8. THE SHRINK GUARD. A suite that quietly loses arms reports green over a population it
# ----    stopped grading, which is the failing case every ported suite used to carry itself.
FLOORBODY="$FIX
arm \"one\" 0 \"base\" \"true\" \"cat subject.txt\"
arm \"two\" 0 \"base\" \"true\" \"cat subject.txt\"
run_arms t"
SELFTEST_FLOOR=2 run_harness floor_met "$FLOORBODY"
rc=$?
[ "$rc" = 0 ] && ok "a suite that meets its pinned floor passes" || nope "a met floor exited $rc" "$(cat "$TMP/floor_met.out")"

SELFTEST_FLOOR=3 run_harness floor_short "$FLOORBODY"
rc=$?
[ "$rc" = 1 ] && grep -q 'below the pinned floor of 3' "$TMP/floor_short.out" \
  && ok "a suite that has SHRUNK below its floor reds by name, before running an arm" \
  || nope "a shrunken suite exited $rc without naming its floor" "$(cat "$TMP/floor_short.out")"

# A floor nobody can parse must REFUSE. Falling back to 0 makes an unreadable pin and no pin at all
# report identically, which is the vacuity this tree bans everywhere else.
SELFTEST_FLOOR=lots run_harness floor_junk "$FLOORBODY"
rc=$?
[ "$rc" = 2 ] && ok "an unparseable floor REFUSES rather than silently disabling the guard" \
              || nope "a junk floor exited $rc" "$(cat "$TMP/floor_junk.out")"

# ---- 9. TWO BATCHES. A suite needing a second base fixture calls build_fixture again; before the
# ----    reset landed, batch two silently re-ran batch one's arms against batch two's snapshot.
run_harness batches 'mkfix1() { printf "ONE
" > subject.txt; }
mkfix2() { printf "TWO
" > subject.txt; }
build_fixture mkfix1 || exit 2
arm "batch one arm" 0 "ONE" "true" "cat subject.txt"
run_arms one
build_fixture mkfix2 || exit 2
arm "batch two arm" 0 "TWO" "true" "cat subject.txt"
run_arms two'
rc=$?
[ "$rc" = 0 ] && ok "a second build_fixture starts a second batch rather than replaying the first"               || nope "the second batch exited $rc" "$(cat "$TMP/batches.out")"
grep -q '^PASS (1 arms' "$TMP/batches.out" && [ "$(grep -c '^PASS (1 arms' "$TMP/batches.out")" = 2 ]   && ok "and each batch reports ONE arm, not the running total"   || nope "the batches did not report one arm each" "$(cat "$TMP/batches.out")"
[ "$(grep -c '^ok    batch one arm' "$TMP/batches.out")" = 1 ]   && grep -q '^ok    batch two arm' "$TMP/batches.out"   && ok "and batch one's arm is graded ONCE, not replayed against batch two's fixture"   || nope "batch one leaked into batch two" "$(cat "$TMP/batches.out")"

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "lib-selftest-test: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)" || echo "FAILED (lib-selftest, $n assertions)"
exit "$bad"
