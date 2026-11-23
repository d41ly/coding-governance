#!/usr/bin/env bash
# lib-selftest.test.sh — the arms for <prefix>/lib/lib-selftest.sh. TOOL-aQuenchedHarness-5 S7.
#
# IT DOES NOT USE THE HARNESS TO TEST ITSELF, and that is not squeamishness: half of what must be
# graded here is the harness FAILING correctly, and an arm that fails inside the harness fails the
# suite that contains it. So each case drives the harness in a SUBPROCESS and grades its output and
# exit status from outside — the same shape every other suite in this repo uses on its own subject.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "lib-selftest-test: not a git tree"; exit 2; }
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
FLOOR_ASSERTIONS=38
# RAISED 34 -> 38 by TOOL-dQuietDisk-37 S7: three argument-key assertions and the race arm's built-2 line.

# run_harness <name> <body> [<dir>] -> writes $TMP/<name>.out, returns the harness's exit status; the
# body runs in <dir>, the repository root by default, whose policy a `--template` batch reads
run_harness() {
  local name=$1 body=$2 dir=${3:-$ROOT}
  { printf 'set -u\n. "%s"\n' "$LIB"; printf '%s\n' "$body"; } > "$TMP/$name.sh"
  ( cd "$dir" && bash "$TMP/$name.sh" ) > "$TMP/$name.out" 2>&1
}

FIX='mkfix() { printf "base\n" > subject.txt; mkdir -p sub; }
build_fixture mkfix || exit 2'

# ---- 1. a passing arm passes, and the suite exits 0 --------------------------------------------
run_harness pass "$FIX
arm \"a control arm\" 0 \"base\" \"true\" \"cat subject.txt\"
run_arms t"
rc=$?
[ "$rc" = 0 ] && ok "a suite whose every arm holds exits 0" || nope "a passing suite exited $rc" "$(head -3 "$TMP/pass.out")"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "$bad" = 0 ] && echo "PASS ($n assertions)" || echo "FAIL ($n assertions)"; exit "$bad"; fi
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

# ---- 10. THE FOREIGN-PREFIX PROBE, TOOL-aRepatriatedFork-52 S1. Under FOREIGN_PREFIX_PROBE=1 a
# ----    harness suite runs its FIRST declared arm, says so, and exits with that arm's verdict, so
# ----    the second batch the arm above ran never starts.
FOREIGN_PREFIX_PROBE=1 run_harness probe "$(sed 1,2d "$TMP/batches.sh")"
rc=$?
[ "$rc" = 0 ] && grep -q '^foreign-prefix-probe: stopped after 1 arm$' "$TMP/probe.out" \
  && [ "$(grep -c '^ok    batch' "$TMP/probe.out")" = 1 ] && grep -q '^PASS (1 arms' "$TMP/probe.out" \
  && ok "a probe runs one arm, prints the probe marker and exits before a second batch" \
  || nope "the probe flag did not stop the suite after one arm (exit $rc)" "$(cat "$TMP/probe.out")"

# ---- 11. THE TEMPLATE MODE, TOOL-dQuietDisk-7 S10. Two scratch repositories decide the switch: DEF
# ----    commits no policy, so `tests.fixture-templates` reads its default `shared`, and PC commits
# ----    `per-case`. Each case names its own cache root, so a template a bar's other suites built
# ----    cannot answer for this one. WHAT THIS DOES NOT CHECK: a bar's shared root across suites.
DEF=$TMP/def; PC=$TMP/pc
mkdir -p "$DEF" "$PC/.governance"
printf 'tests.fixture-templates = "per-case"\n' > "$PC/.governance/policy.toml"
printf 'x\n' > "$DEF/README"
for r in "$DEF" "$PC"; do
  git -C "$r" init -q -b main && git -C "$r" -c core.autocrlf=false add -A \
    && git -C "$r" -c core.autocrlf=false -c core.hooksPath= -c commit.gpgsign=false -c user.name=t -c user.email=t@t \
      commit -qm base || { echo "lib-selftest-test: cannot build the switch repositories"; exit 2; }
done
export TMP_IN=$TMP/key.in TMP_RACE=$TMP/race TMP_COST=$TMP/cost TMP_ARGS=$TMP/args
TFIX='mkrepo() { git init -q && git config user.email t@t && printf "base\n" > subject.txt; }
build_fixture --template "" mkrepo || exit 2'

# A clone that copies objects or keeps its remote is the break: each arm asks it of its own clone. An
# unmatched glob stays literal, so `! -d` over the loose-object directories holds only where none exist.
mkdir -p "$TMP/tr.clone"
SELFTEST_TEMPLATE_ROOT=$TMP/tr.clone run_harness tclone "$TFIX"'
arm "no remote"            0 ""     "true" "[ -z \"\$(git remote)\" ]"
arm "objects stay shared"  0 ""     "true" "[ -s .git/objects/info/alternates ] && [ ! -d .git/objects/[0-9a-f][0-9a-f] ] && [ -z \"\$(ls .git/objects/pack)\" ]"
arm "the builder config"   0 "t@t"  "true" "git config user.email"
arm "the committed file"   0 "base" "true" "git show HEAD:subject.txt"
run_arms t' "$DEF"
rc=$?
[ "$rc" = 0 ] && ok "a --template clone keeps no remote, copies no object, and carries the builder's config" \
              || nope "the template clone exited $rc" "$(cat "$TMP/tclone.out")"
grep -qE '^template: [0-9a-f]{8} built$' "$TMP/tclone.out" \
  && ok "and build_fixture --template says once that it built the template" \
  || nope "no 'template: <key8> built' line" "$(cat "$TMP/tclone.out")"

# Two builders colliding on one key: one name, two definitions; and one input byte moved.
run_harness tkey 'mkk() { printf a > f; }
printf "abc\n" > "$TMP_IN"
k1=$(derive_template_key mkk "$TMP_IN") && k1b=$(derive_template_key mkk "$TMP_IN") || exit 2
mkk() { printf b > f; }
k2=$(derive_template_key mkk "$TMP_IN") || exit 2
printf "abd\n" > "$TMP_IN"
k3=$(derive_template_key mkk "$TMP_IN") || exit 2
echo "keys $k1 $k1b $k2 $k3"' "$DEF"
read -r _ k1 k1b k2 k3 < <(grep '^keys ' "$TMP/tkey.out")
[ -n "${k1:-}" ] && [ "$k1" = "${k1b:-}" ] && ok "one builder and one input set give one key twice" \
  || nope "the key is not stable" "$(cat "$TMP/tkey.out")"
[ -n "${k2:-}" ] && [ "$k1" != "$k2" ] && ok "two builders of one name but two definitions never share a key" \
  || nope "a redefined builder kept its key" "$(cat "$TMP/tkey.out")"
[ -n "${k3:-}" ] && [ "$k2" != "$k3" ] && ok "one byte of one input file moves the key" \
  || nope "a changed input kept its key" "$(cat "$TMP/tkey.out")"

# THE BUILDER'S ARGUMENTS KEY ITS TEMPLATE (TOOL-dQuietDisk-37 S4, S7). `mka` writes its first argument,
# so a key that ignored the arguments hands the second caller the first one's value; with none the key
# is the caller's own. Red against the base block, which named the directory by the caller's key alone.
mkdir -p "$TMP/tr.args"
SELFTEST_TEMPLATE_ROOT=$TMP/tr.args run_harness targs 'mka() { printf "%s\n" "$1" > v; }
build_fixture --template "" mka x || exit 2
arm "the x batch" 0 "x" "true" "cat v"
run_arms x
build_fixture --template "" mka y || exit 2
arm "the y batch" 0 "y" "true" "cat v"
run_arms y' "$DEF"
rc=$?
[ "$rc" = 0 ] && grep -q '^ok    the x batch' "$TMP/targs.out" && grep -q '^ok    the y batch' "$TMP/targs.out" \
  && ok "two build_fixture --template batches of one builder with two arguments each grade their own value" \
  || nope "a second argument list was handed the first one's template (exit $rc)" "$(cat "$TMP/targs.out")"
run_harness tdirect 'mka() { printf "%s\n" "${1-none}" > v; }
k=$(derive_template_key mka) || exit 2
a=$(resolve_template "$TMP_ARGS" "$k" mka x 2>/dev/null) && b=$(resolve_template "$TMP_ARGS" "$k" mka y 2>/dev/null) \
  && c=$(resolve_template "$TMP_ARGS" "$k" mka 2>/dev/null) || exit 2
[ "$a" != "$b" ] && echo "paths two $(cat "$a/v") $(cat "$b/v")"
[ "$c" = "$TMP_ARGS/$k/repo" ] && echo "bare keyed"' "$DEF"
grep -qx 'paths two x y' "$TMP/tdirect.out" \
  && ok "two direct resolve_template calls of one key with arguments x and y print two templates, each its own value" \
  || nope "one key with two argument lists resolved one template" "$(cat "$TMP/tdirect.out")"
grep -qx 'bare keyed' "$TMP/tdirect.out" && ok "and a call with no argument still prints <root>/<key>/repo" \
  || nope "a call with no argument moved its key" "$(cat "$TMP/tdirect.out")"

# An exported GIT_DIR reaches none of the three git-running verbs (TOOL-dQuietDisk-36 S4). It names a
# scratch SHA-256 repository with one commit and an origin remote, so a leak moves its HEAD, drops its
# remote, or derives a 64-hex key; the body exports it only after the harness is sourced, and unsets it
# for its own reads of the clone. WHAT THIS DOES NOT CHECK: read_template_mode, which runs no git here.
LEAK=$TMP/leak/scratch; mkdir -p "$LEAK"; printf 's\n' > "$LEAK/s.txt"
git -C "$LEAK" init -q --object-format=sha256 && git -C "$LEAK" -c core.autocrlf=false add -A \
  && git -C "$LEAK" -c core.hooksPath= -c commit.gpgsign=false -c user.name=t -c user.email=t@t commit -qm scratch \
  && git -C "$LEAK" remote add origin "$TMP/leak/origin.git" \
  || { echo "lib-selftest-test: cannot build the scratch SHA-256 repository"; exit 2; }
h0=$(git -C "$LEAK" rev-parse HEAD)
export TMP_LEAK=$TMP/leak
run_harness tleak 'mkg() { git init -q && printf g > g.txt && git -c core.autocrlf=false add -A \
  && git -c core.hooksPath= -c commit.gpgsign=false -c user.name=t -c user.email=t@t commit -qm self; }
k0=$(derive_template_key mkg)
export GIT_DIR=$TMP_LEAK/scratch/.git
k1=$(derive_template_key mkg)
t=$(resolve_template "$TMP_LEAK/root" "$k1" mkg 2>/dev/null)
build_template_clone "$t" "$TMP_LEAK/clone" 2>/dev/null
unset GIT_DIR
echo "clone $(git -C "$TMP_LEAK/clone" remote 2>/dev/null | grep -c .) $(cat "$TMP_LEAK/clone/g.txt" 2>/dev/null)"
echo "keys $k0 $k1"' "$DEF"
[ -n "$h0" ] && [ "$(git -C "$LEAK" rev-parse HEAD 2>/dev/null)" = "$h0" ] && [ "$(git -C "$LEAK" remote 2>/dev/null)" = origin ] \
  && ok "an exported GIT_DIR keeps the scratch repository's HEAD and its origin remote unmoved" \
  || nope "the template cache moved the HEAD or a remote of the repository GIT_DIR names" "$(cat "$TMP/tleak.out")"
grep -qx 'clone 0 g' "$TMP/tleak.out" && ok "and the clone holds the builder's tree and no remote" \
  || nope "the clone under an exported GIT_DIR is not the builder's tree without a remote" "$(cat "$TMP/tleak.out")"
read -r _ lk0 lk1 < <(grep '^keys ' "$TMP/tleak.out")
[[ ${lk0:-} =~ ^[0-9a-f]{40}$ ]] && [ "${lk1:-}" = "$lk0" ] && ok "and the key equals the key derived with GIT_DIR unset" \
  || nope "the key moved under an exported GIT_DIR" "$(cat "$TMP/tleak.out")"

# A racing stage left behind: two shells resolve one key at once in one root. THE BARRIER holds each
# builder until both have entered (TOOL-dQuietDisk-37 S7): each leaves a marker named for its own
# $BASHPID beside the root, never inside it, and builds only once two exist, so both are building at
# once and the second rename meets the `mv -T` collision. A fixed sleep let a racer that forked after
# the first had written `ready` reuse it and never build; `built <n>` is the marker count.
run_harness trace 'mkr() { : > "$TMP_RACE.m.$BASHPID"; local i=0; local -a m
  while m=("$TMP_RACE".m.*); [ "${#m[@]}" -lt 2 ] && [ "$i" -lt 300 ]; do sleep 0.1; i=$((i + 1)); done
  git init -q && printf r > f; }
k=$(derive_template_key mkr) || exit 2
( resolve_template "$TMP_RACE" "$k" mkr > "$TMP_RACE.a" 2>/dev/null ) &
( resolve_template "$TMP_RACE" "$k" mkr > "$TMP_RACE.b" 2>/dev/null ) &
wait
cmp -s "$TMP_RACE.a" "$TMP_RACE.b" && [ -s "$TMP_RACE.a" ] && echo "same template"
echo "built $(ls "$TMP_RACE".m.* 2>/dev/null | wc -l)"
echo "entries $(ls -A "$TMP_RACE" | wc -l) nested $(ls -A "$TMP_RACE/$k" | grep -c "^\.stage-")"' "$DEF"
grep -q '^built 2$' "$TMP/trace.out" && ok "both racers built, so the arm below grades a real collision" \
  || nope "one racer reused the other's template and never built, so no collision was met" "$(cat "$TMP/trace.out")"
grep -q '^built 2$' "$TMP/trace.out" && grep -q '^entries 1 nested 0$' "$TMP/trace.out" \
  && ok "two racing builds leave one key directory, and no stage beside it or inside it" \
  || nope "a racing stage was left behind or renamed over the winner" "$(cat "$TMP/trace.out")"
grep -q '^same template$' "$TMP/trace.out" && ok "and both racers get the same template" \
  || nope "the racers got different templates" "$(cat "$TMP/trace.out")"

# The cache root: a named directory, then a bar's owned gate-work, then the caller's own scratch.
mkdir -p "$TMP/named" "$TMP/gate-work.t/tmp"; : > "$TMP/gate-work.t/owner"
TMP_NAMED=$TMP/named TMP_BAR=$TMP/gate-work.t run_harness troot 'SELFTEST_ROOT=/sr
echo "named $(SELFTEST_TEMPLATE_ROOT=$TMP_NAMED resolve_template_root)"
echo "bar $(SELFTEST_TEMPLATE_ROOT= TMPDIR=$TMP_BAR/tmp resolve_template_root)"
echo "own $(SELFTEST_TEMPLATE_ROOT= TMPDIR=/nowhere resolve_template_root)"' "$DEF"
[ "$(cat "$TMP/troot.out")" = "named $TMP/named
bar $TMP/gate-work.t/templates
own /sr/templates" ] && ok "the cache root is the named directory, else the owned gate-work, else SELFTEST_ROOT" \
  || nope "the cache root resolved elsewhere, so it could outlive the run" "$(cat "$TMP/troot.out")"

# The saving itself: eight cases built per case, init, two configs, add and commit, against eight
# clones of one template, counted as git's trace2 event files; the template's own build is in the count.
run_harness tcost 'mkc() { git init -q --template= && git config user.email t@t && git config user.name t \
  && printf 1 > a && mkdir d && printf 2 > d/b; }
mkdir -p "$TMP_COST/p" "$TMP_COST/c"
for i in 1 2 3 4 5 6 7 8; do mkdir "$TMP_COST/case.$i" && ( cd "$TMP_COST/case.$i" && GIT_TRACE2_EVENT=$TMP_COST/p mkc \
  && GIT_TRACE2_EVENT=$TMP_COST/p git -c core.autocrlf=false add -A \
  && GIT_TRACE2_EVENT=$TMP_COST/p git -c core.hooksPath= -c commit.gpgsign=false commit -qm base ) || exit 2; done
export GIT_TRACE2_EVENT=$TMP_COST/c
t=$(resolve_template "$TMP_COST/root" "$(derive_template_key mkc)" mkc 2>/dev/null) || exit 2
for i in 1 2 3 4 5 6 7 8; do build_template_clone "$t" "$TMP_COST/clone.$i" || exit 2; done
echo "cost $(ls "$TMP_COST/p" | wc -l) $(ls "$TMP_COST/c" | wc -l)"' "$DEF"
read -r _ cp cc < <(grep '^cost ' "$TMP/tcost.out")
[ -n "${cc:-}" ] && [ "$cc" -lt "${cp:-0}" ] && ok "eight clones of one template spend fewer git processes than eight builds ($cc against $cp)" \
  || nope "the cache spent as many git processes as a build per case" "$(cat "$TMP/tcost.out")"

# A reading arm that writes fails the suite under shared, naming the arm and the read checkout.
RBODY="$TFIX"'
arm         "a mutating arm" 0 "" "true" "printf x >> subject.txt"
arm_reading "a reader"       0 "" "true" "cat subject.txt READ_WRITE"
run_arms t'
mkdir -p "$TMP/tr.read"
SELFTEST_TEMPLATE_ROOT=$TMP/tr.read run_harness tread "${RBODY/ READ_WRITE/; printf w > leak.txt}" "$DEF"
rc=$?
[ "$rc" = 1 ] && grep -q '^FAIL  a reading arm wrote into the read checkout .*/read — a reader: ' "$TMP/tread.out" \
  && ok "a reading arm that writes FAILs the suite, naming the arm and the read checkout" \
  || nope "a reading arm's write exited $rc" "$(cat "$TMP/tread.out")"
SELFTEST_TEMPLATE_ROOT=$TMP/tr.read run_harness tread0 "${RBODY/ READ_WRITE/}" "$DEF"
rc=$?
[ "$rc" = 0 ] && ok "and with the write removed the suite passes" || nope "a clean reader exited $rc" "$(cat "$TMP/tread0.out")"

# One suite under --template in both values of the switch: the arm lines must not move.
SBODY="$TFIX
arm         \"green one\" 0 \"base\"       \"true\" \"cat subject.txt\"
arm_reading \"green two\" 0 \"base\"       \"true\" \"cat subject.txt\"
arm         \"the red\"   0 \"NOTPRESENT\" \"true\" \"cat subject.txt\"
arm_reading \"a writer\"  0 \"\"           \"true\" \"printf w > leak.txt\"
run_arms t"
mkdir -p "$TMP/tr.sw"
SELFTEST_TEMPLATE_ROOT=$TMP/tr.sw run_harness tshared "$SBODY" "$DEF"
SELFTEST_TEMPLATE_ROOT=$TMP/tr.sw run_harness tpercase "$SBODY" "$PC"
if diff <(grep -E '^(ok|FAIL)  ' "$TMP/tshared.out" | grep -v 'read checkout') \
        <(grep -E '^(ok|FAIL)  ' "$TMP/tpercase.out") >/dev/null 2>&1 && grep -q '^FAIL  the red' "$TMP/tpercase.out"; then
  ok "the arm lines are identical under shared and per-case, the same arm red in both"
else
  nope "an arm's result moved with the switch" "$(diff "$TMP/tshared.out" "$TMP/tpercase.out" | head -6)"
fi
! grep -q '^template: ' "$TMP/tpercase.out" && grep -q 'read checkout' "$TMP/tshared.out" \
  && ! grep -q 'read checkout' "$TMP/tpercase.out" \
  && ok "per-case builds no template and runs a reading arm in its own copy, as arm does" \
  || nope "per-case still used the template" "$(cat "$TMP/tpercase.out")"

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "lib-selftest-test: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)" || echo "FAILED (lib-selftest, $n assertions)"
exit "$bad"
