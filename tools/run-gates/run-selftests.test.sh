#!/usr/bin/env bash
# run-selftests.test.sh — the failing case for every refusal `run-selftests.sh` carries.
#
# IT LANDED WITHOUT ONE. `TOOL-aQuenchedHarness-4` shipped a runner whose whole job is refusing —
# refusing a declaration that misses a held leg, refusing a row naming an untracked file, refusing a
# filter that matched nothing — and nothing in this tree had ever seen any of those refusals fire.
# Charter §7: a gate you have only ever watched pass is an assertion about nothing. This is that
# arrears, paid by `TOOL-aQuenchedHarness-6`, which added `--rank` to the same file and would
# otherwise have added a fourth unobserved refusal to three.
#
# IT RUNS ON THE HARNESS IT EXISTS BECAUSE OF. `tools/lib/lib-selftest.sh` is this build's own
# product, and a suite written against it here is the second adopter after the ported one — which is
# the only way to find out whether the three verbs fit a subject nobody designed them around.
set -u
# THE FIXTURE KEYS EVERY EVIDENCE ROW ON TAG `t` and the runner short-circuits on GOV_NODE, so an
# inherited `GOV_NODE=a` turned 46 arms red naming node a (aBatchedArm closing review D12) — the
# `fixture-inherits-ambient-machine-state` class; sibling suites scrub with `env -u` for the same
# reason. The one arm that wants GOV_NODE sets it in its own subject.
unset GOV_NODE
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "run-selftests.test: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2
. "$ROOT/tools/lib/lib-selftest.sh"

RUNNER="$ROOT/tools/run-gates/run-selftests.sh"
[ -f "$RUNNER" ] || { echo "run-selftests.test: no runner at $RUNNER"; exit 2; }

# HOISTED ABOVE THE FIXTURE BUILDER so the generated helper below can interpolate them.
# Re-spelling either path inside a printf would add a kit-path literal to this file, and
# the install-prefix checker is a shrink-only BAN rather than a ratchet.
R='bash tools/run-gates/run-selftests.sh'
B='tools/run-gates/selftest-budgets.txt'
LEGS='tools/gate-legs.json'
# THE POOLED EVIDENCE and the fixture's copy of the runner, both DERIVED from the lines above so
# neither adds a carried literal (the install-prefix ban pins this file's count).
E='tools/run-gates/selftest-pooled-evidence.txt'
RC=${R#bash }

# THE FLOOR, RE-DERIVED at TOOL-aBatchedArm-5: 55 at BASE, minus the retired factor-absent arm,
# plus the arms that unit added — both counts are in that unit's acceptance ledger. Raised again
# at the aBatchedArm closing fix by the arms it added; that ledger carries the count.
SELFTEST_FLOOR=108

# The fixture is a MINIMAL repo the runner can root itself in: two suites it can execute, a manifest
# with one held leg, and a declaration that covers it. Every arm below starts from this green state
# and stages exactly one break into it, which is the only way a refusal can be attributed.
build_repo() {
  mkdir -p tools/run-gates || return 2
  git init -q . >/dev/null 2>&1 || return 2
  git config user.email t@t && git config user.name t || return 2
  cp "$RUNNER" tools/run-gates/run-selftests.sh || return 2

  # EVERY COMPLETING SUITE PRINTS THE HARNESS TRAILER `PASS (`, because under parity
  # (TOOL-aBatchedArm-5 S2/S4) a completed exit with no trailer is not a reading and does not
  # match a baseline that has one; the suites that deliberately print none are named as such.
  printf '#!/usr/bin/env bash\necho "PASS (1 assertions)"\nexit 0\n' > tools/suite-ok.sh
  printf '#!/usr/bin/env bash\necho "FAIL something"\nexit 1\n' > tools/suite-red.sh
  printf '#!/usr/bin/env bash\nsleep 3\necho "PASS (1 assertions)"\nexit 0\n' > tools/suite-slow.sh
  # THE WALL ARM'S PAIR. Its margins have to be SECONDS or the arm is a coin flip: the wall and
  # the per-suite bound both expire near the same instant otherwise, and whichever wins decides
  # whether the row renders WALL or TIMEOUT. A 5s first suite puts the wall 5s clear of the start
  # and 5s clear of the second suite's own bound.
  printf '#!/usr/bin/env bash\nsleep 5\necho "PASS (1 assertions)"\nexit 0\n' > tools/suite-mid.sh
  printf '#!/usr/bin/env bash\nsleep 30\nexit 0\n' > tools/suite-long.sh
  # THE WITNESS THAT A SUITE RAN. The refusal arms claim the runner executed nothing, and a
  # suite's stdout cannot show that -- the serial loop swallows it on a pass and the pool files
  # it. A file it leaves behind can.
  printf '#!/usr/bin/env bash\ntouch ran.marker\necho "PASS (1 assertions)"\nexit 0\n' > tools/suite-mark.sh
  # ---- TOOL-aBatchedArm-5's fixtures: the red-by-design shape unit 3's rows have (three FAIL
  # ---- lines, the executed-count trailer, exit 1); a suite that dies at once under `set -u` with
  # ---- no FAIL line and no trailer (the fast-red class the FAIL count exists to catch); and a
  # ---- suite that exits 0 in under a second and prints NOTHING (a completed exit that is not a
  # ---- reading).
  { printf '#!/usr/bin/env bash\n'
    printf 'echo "FAIL one"; echo "FAIL two"; echo "FAIL three"\n'
    printf 'echo "  (81 assertions executed in shard 1/8 against a floor of 78)"\n'
    printf 'exit 1\n'
  } > tools/suite-shard.sh
  printf '#!/usr/bin/env bash\nset -u\necho "$THIS_IS_UNBOUND"\nexit 0\n' > tools/suite-crash.sh
  printf '#!/usr/bin/env bash\nexit 0\n' > tools/suite-quiet.sh
  # ---- the NO-BASELINE SENTINEL shape (aBatchedArm closing D3): a batched group whose expected
  # ---- set is still unwritten prints the refusal, its observed set indented, and the shard's
  # ---- trailer all the same — so by (rc, FAIL, executed) alone it reads as a red-by-design row.
  { printf '#!/usr/bin/env bash\n'
    printf 'echo "FAIL check_emitted: expected set not yet observed — owed at the final pass · call at line 946"\n'
    printf 'echo "    observed: UNATTENDED check 3 FAILED a-signature"\n'
    printf 'echo "  (81 assertions executed in shard 1/8 against a floor of 78)"\n'
    printf 'exit 1\n'
  } > tools/suite-sentinel.sh
  # ---- a suite that OUTLIVES TERM (aBatchedArm closing D8): the wall's TERM is ignored, so the
  # ---- worker's `timeout -k 5` KILLs it after the grace and it exits 137 — a kill with a
  # ---- WALL_BREACHED flag and an rc the WALL branch does not key on.
  printf '#!/usr/bin/env bash\ntrap "" TERM\nfor _ in 1 2 3 4 5 6 7 8 9 10; do sleep 2; done\nexit 0\n' > tools/suite-stubborn.sh

  # THE CHARTER STUB WITH ONE REGISTRY ROW. The runner keys pooled evidence by the charter's §2
  # node TAG, resolved from USERNAME/USER against the registry table at the repo root; a bare
  # `git init` has no charter, so the fixture writes one mapping the current user to tag `t`.
  # AC2's no-row clause is staged by deleting this row.
  printf '# fixture charter\n\n| Tag | Machine/user | Primary tree |\n|-----|---|---|\n| `t` | `%s` | fixture |\n' \
    "${USERNAME:-$USER}" > AGENTS.md
  # THE MARGIN the pooled bound reads beside the runner: floor 1 s, fraction 1.0 — so a bound is
  # `max(budget, reading) + max(1, that)`, which is 2x the larger term, and every seed below is sized
  # against that: a budget-60 row with a 1 s seed bounds at 120 s, the TIMEOUT arm's budget-1 row
  # at 2 s (against a 3 s sleep), the suite-mid arm's budget-4 row at 8 s (against a 5 s sleep).
  printf '# fixture margin: <floor seconds>\t<fraction of max>\n1\t1.0\tfixture\n' > tools/run-gates/ceiling-margin.txt
  # THE SEEDED, TRACKED EVIDENCE, under BOTH tokens the arms produce: `pooled@2x1` by default (W
  # falls to 2 with no run-gates.sh in the fixture, so outer 2, inner 1) and `pooled@1x2` under
  # SELFTEST_OUTER_WIDTH=1. Every row an arm appends at run time is seeded in that arm's setup
  # with tools/seed.sh, under the token it runs at.
  {
    printf '# fixture pooled evidence: seconds monotone; rc, fails, executed the latest reading'"'"'s.\n'
    printf '# <row>\t<condition>\t<node>\t<max seconds>\t<rc>\t<fails>\t<executed>\t<readings>\t<date>\n'
    for _tok in pooled@2x1 pooled@1x2; do
      printf 'held one\t%s\tt\t1\t0\t0\t-\t1\t2026-09-14\n' "$_tok"
      printf 'free one\t%s\tt\t1\t0\t0\t-\t1\t2026-09-14\n' "$_tok"
    done
  } > "$E"
  # seed.sh <row> <token> <secs> <rc> <fails> <executed> — upsert ONE evidence row under tag `t`
  # and stage it, so an arm's setup can size a reading without spelling nine tab fields inline.
  { printf '#!/usr/bin/env bash\n'
    printf 'set -u\n'
    printf 'E=%s\n' "$E"
    printf 'k=$(printf "%%s\\t%%s\\tt\\t" "$1" "$2")\n'
    printf 'grep -vF -- "$k" "$E" > "$E.new"; mv "$E.new" "$E"\n'
    printf 'printf "%%s\\t%%s\\tt\\t%%s\\t%%s\\t%%s\\t%%s\\t1\\t2026-09-14\\n" "$1" "$2" "$3" "$4" "$5" "$6" >> "$E"\n'
    printf 'git add -A >/dev/null 2>&1\n'
  } > tools/seed.sh

  # ONE held leg — `subject: kit` is half of the hold predicate — plus one leg the bar does not
  # hold, so the forward direction has something to find and something to correctly ignore.
  printf '%s\n' '[' \
    '  {"name": "held one", "argv": ["bash", "tools/suite-ok.sh"], "subject": "kit"},' \
    '  {"name": "not held", "argv": ["bash", "tools/suite-ok.sh"], "subject": "repo"}' \
    ']' > tools/gate-legs.json

  {
    printf '# a fixture declaration.\n'
    printf '# port-majority-share: 0.50\n'
    printf '# port-minimum-factor: 3.0\n'
    printf 'held one\t60\t\tworst of 3 readings 10s, x1.5\n'
    printf 'free one\t60\tbash tools/suite-ok.sh\tmeasured 2s on node t 2026-09-07, x1.5\n'
  } > tools/run-gates/selftest-budgets.txt

  # THE ROUND-TRIP SETUP, as a file rather than as an arm string. The capture needs a sed
  # expression, a tab and a newline, and an arm string is eval'd inside a fresh `bash -c` --
  # three quoting layers deep, which is where the first attempt at this arm died.
  {
    printf '#!/usr/bin/env bash\n'
    printf 'set -u\n'
    printf 'B=%s\n' "$B"
    printf 'tag=$(%s --sweep 2>/dev/null |' "$R"
    printf ' sed -n "s/^run-selftests: condition: //p")\n'
    # AN EMPTY CAPTURE IS A REFUSAL, not a row with no tag in it: without this the arm would
    # write an ordinary reading, --rank would rank it, and the arm would red for a reason that
    # has nothing to do with the join it exists to observe.
    printf '[ -n "$tag" ] || { echo "the sweep emitted no condition line"; exit 1; }\n'
    printf 'printf "roundtrip\\t60\\tbash tools/suite-ok.sh\\tmeasured 42s $tag on node t 2026-09-07, x1.5\\n" >> "$B"\n'
    printf 'git add -A >/dev/null 2>&1\n'
  } > tools/roundtrip.sh
  # ---- TOOL-aPooledSweep-3's fixtures: a suite per escape route, and a git that can only fail
  # ---- the one subcommand the fingerprint uses.
  { printf '#!/usr/bin/env bash\n'
    printf 'echo "FAIL tracked-write" >> subject.md\n'
    printf 'echo "FAIL wrote-into-the-checkout"\n'
    printf 'exit 1\n'
  } > tools/suite-dirty.sh
  { printf '#!/usr/bin/env bash\n'
    printf 'echo x > "$(git rev-parse --git-common-dir)/aPooledSweep-probe"\n'
    printf 'echo "FAIL wrote-into-the-git-dir"\n'
    printf 'exit 1\n'
  } > tools/suite-gitdir.sh
  { printf '#!/usr/bin/env bash\n'
    printf '[ -n "${TMPDIR:-}" ] || { echo "FAIL no-tmpdir"; exit 1; }\n'
    printf 'case "$(mktemp -d)" in "$TMPDIR"*) echo "FAIL scratch-under-tmpdir";;'
    printf ' *) echo "FAIL scratch-escaped";; esac\n'
    printf 'exit 1\n'
  } > tools/suite-tmpdir.sh
  # A GIT THAT ANSWERS EVERY SUBCOMMAND THE RUNNER NEEDS AND REFUSES `status`. Deleting the git
  # dir instead would break the runner's own root resolution, so the arm would observe a
  # different refusal than the one it is written for.
  { printf '#!/usr/bin/env bash\n'
    printf 'case "$1" in status) exit 3;; esac\n'
    # THE REAL GIT'S PATH IS RESOLVED AT FIXTURE-BUILD TIME and baked in. Resolving it inside the
    # shim would find the shim, because the arm puts the shim's directory FIRST on PATH.
    printf 'exec %s "$@"\n' "$(command -v git)"
  } > tools/git-nostatus.sh
  # The subject file the dirty suite appends to has to be TRACKED, or --untracked-files=no
  # cannot see it and the arm passes by finding nothing.
  printf 'a tracked subject\n' > subject.md
  git add -A >/dev/null 2>&1 || return 2
}
build_fixture build_repo || exit 2


# ---------------------------------------------------------------- --check, both directions
arm "control · a clean declaration passes --check" 0 "declaration clean" \
    'true' "$R --check"

arm "a HELD leg with no budget row reds, because a suite arriving without one would be exempt by arriving" 1 \
    "these HELD legs carry no budget row" \
    "grep -v '^held one' $B > tmp.b && mv tmp.b $B && git add -A" \
    "$R --check"

arm "a row naming a path git does not track reds" 1 "which git does not track" \
    "printf 'ghost\t60\tbash tools/suite-ghost.sh\tworst of 3 readings 5s, x1.5\n' >> $B" \
    "$R --check"

arm "a row with no argv and no leg of that name reds" 1 "has no argv and no leg of that name" \
    "printf 'orphan\t60\t\tworst of 3 readings 5s, x1.5\n' >> $B" \
    "$R --check"

# ---------------------------------------------------------------- the shard token, TOOL-aBatchedArm-4 S1
# `--shard 1/8` carries a slash and is not a path. The predicate that admits it is a REGEX over the
# whole token; a glob's `[0-9]*` is one digit then anything, so the second arm is the direction the
# glob would have lost: a digit-led directory name is still handed to git and still reds.
arm "a numeric-ratio token such as --shard 1/8 is admitted by --check, because it is not a path" 0 \
    "declaration clean" \
    "for i in 1 2 3 4 5 6 7 8; do printf 'sharded %s\t60\tbash tools/suite-ok.sh --shard %s/8\tmeasured 2s on node t 2026-09-07, x1.5\n' \$i \$i; done >> $B && git add -A" \
    "$R --check"

# ---------------------------------------------------------------- the shard join, TOOL-aBatchedArm-3 S4
# Ported from the gov canary's shard contract, FORWARD half only: a script called with `--shard`
# is called at one arity and every index 1..n is declared once. Seven of eight rows report green on
# their own, which is green-by-absence one row at a time — so the arm above stages the COMPLETE set
# and this one deletes a row from it. The second arm is the half deliberately NOT ported: a suite
# that declares `SHARD_ARITY` and is called whole is a declaration this file is right to carry.
arm "a deleted shard row reds the join NAMING the missing index, rather than seven green rows" 1 \
    "no row for index 5" \
    "for i in 1 2 3 4 6 7 8; do printf 'sharded %s\t60\tbash tools/suite-ok.sh --shard %s/8\tmeasured 2s on node t 2026-09-07, x1.5\n' \$i \$i; done >> $B && git add -A" \
    "$R --check"

arm "a suite that declares SHARD_ARITY and is called WHOLE is not graded by the join" 0 \
    "declaration clean" \
    "printf '#!/usr/bin/env bash\nSHARD_ARITY=2\nexit 0\n' > tools/suite-arity.sh && printf 'whole\t60\tbash tools/suite-arity.sh\tmeasured 2s on node t 2026-09-07, x1.5\n' >> $B && git add -A" \
    "$R --check"

arm "a DIGIT-LED untracked path is still refused by name, so the ratio predicate is a regex and not a glob" 1 \
    "names '1abc/2suite.sh', which git does not track" \
    "printf 'digitled\t60\tbash 1abc/2suite.sh\tmeasured 2s on node t 2026-09-07, x1.5\n' >> $B && git add -A" \
    "$R --check"

# An EMPTY declaration passes BOTH directions by finding nothing in either, which is the vacuity the
# runner's own liveness line exists to refuse.
arm "an EMPTY declaration reds rather than passing both directions by finding nothing" 1 \
    "the declaration is EMPTY, so both directions above passed by finding nothing" \
    "printf '# only a comment\n' > $B && printf '%s\n' '[]' > $LEGS && git add -A" \
    "$R --check"

# ---------------------------------------------------------------- --rank
arm "--rank orders the population and names the set carrying the declared share" 0 \
    "the declared share is carried by the TOP" \
    'true' "$R --rank"

arm "--rank REFUSES a reading whose CONDITION it does not recognise, and computes no share at all" 1 \
    "carry no reading whose CONDITION this verb recognises" \
    "printf 'carried\t60\tbash tools/suite-ok.sh\tcarried verbatim from somewhere else\n' >> $B && git add -A" \
    "$R --rank"

arm "--rank REFUSES when the declaration states no share, rather than defaulting one" 1 \
    "the declaration states no port-majority-share" \
    "grep -v 'port-majority-share' $B > tmp.b && mv tmp.b $B" \
    "$R --rank"

arm "--rank REFUSES a declaration that ranks no row at all" 2 \
    "ranked NO row at all, so this verb graded nothing" \
    "grep '^#' $B > tmp.b && mv tmp.b $B" \
    "$R --rank"

# ---------------------------------------------------------------- the declared mode, TOOL-aBatchedArm-4 S2
# A bare run REFUSES. It used to be the serial default, and the one caller that reported cost read
# only the exit code, so a silent pooled default would have printed GREEN with every budget withheld
# and a silent serial one was a contract nobody had written down. The five arms below that used to
# invoke the runner bare now declare --serial; this one is the refusal, and the marker suite is
# what proves "executes no suite" rather than the runner asserting it.
arm "a run with NO mode REFUSES naming both spellings, and executes no suite" 2 \
    "declares --serial or --pooled" \
    "sed -i 's|bash tools/suite-ok.sh|bash tools/suite-mark.sh|' $B" \
    "( $R; rc=\$?; [ -e ran.marker ] && exit 99; exit \$rc )"

# The refusal sits AFTER --check and --list: both execute nothing and take no mode, and --check is
# the unguarded bar leg, so a refusal above it would red every bar. The control arm at the top of
# this file is the --check half; this is --list.
arm "--list takes no mode and is not refused, because it executes nothing" 0 \
    "declared total" \
    'true' "$R --list"

# ---------------------------------------------------------------- the run, and its liveness
# AND IT SITS BEFORE THE FILTER-LIVENESS REFUSAL, which still fires by name under a declared mode:
# the mode is the invocation's shape, the filter its content, and a wrong filter still reds.
arm "a --kit filter matching nothing REFUSES, because an unknown filter and a clean sweep look alike" 2 \
    "so this run graded NOTHING at all" \
    'true' "$R --serial --kit tools/nowhere"

arm "a population whose every suite passes reports GREEN and says none of it runs on the bar" 0 \
    "self-tests GREEN" \
    'true' "$R --serial"

arm "a suite that fails reds the run" 1 "self-tests RED" \
    "sed -i 's|bash tools/suite-ok.sh|bash tools/suite-red.sh|' $B" \
    "$R --serial"

arm "a suite that overruns its declared budget reds and NAMES the number it broke" 1 \
    "OVER BUDGET" \
    "sed -i 's|free one\t60|free one\t1|; s|bash tools/suite-ok.sh|bash tools/suite-slow.sh|' $B" \
    "$R --serial"

# ---------------------------------------------------------------- the state field is READ
# The run loop used to ignore `$state` entirely, and the emitter used to accept any budget. Together
# that made a row with an empty budget print a GREEN line at 0s for a suite it never executed: the
# empty column collapsed under IFS=tab, argv read back empty, `eval ""` returned 0, and the budget
# comparison errored into "not over budget". Both halves are armed here, in both readers.
arm "a NON-NUMERIC budget is a named refusal in --check, not a row that cannot be graded" 1     "declares a budget that is not a number"     "printf 'lopsided	lots	bash tools/suite-ok.sh	worst of 3 readings 5s, x1.5
' >> $B && git add -A"     "$R --check"

arm "an EMPTY budget column is caught too, rather than collapsing into the argv" 1     "declares a budget that is not a number"     "printf 'hollow		bash tools/suite-ok.sh	worst of 3 readings 5s, x1.5
' >> $B && git add -A"     "$R --check"

arm "the RUN loop refuses a row it cannot resolve instead of printing ok for a suite it never ran" 1     "this row could not be resolved into a runnable suite"     "printf 'hollow		bash tools/suite-ok.sh	worst of 3 readings 5s, x1.5
' >> $B && git add -A"     "$R --serial"

# ---------------------------------------------------------------- --sweep, TOOL-aPooledSweep-1
# The pool answers ONE question and issues no cost verdict, so every arm here reads the sweep
# verdict and none of them reads a budget. The budget arms above still read the serial mode.
arm "--sweep over a green population exits 0 and SAYS it graded no cost" 0 \
    "NO cost verdict was issued" \
    'true' "$R --sweep"

arm "--sweep prints the width pair it chose BEFORE the first verdict, so the invariant is checkable" 0 \
    "(outer " \
    'true' "$R --sweep"

# RE-LABELLED at TOOL-aBatchedArm-5: under parity a suite that exits 1 with one FAIL line and no
# trailer is a MISMATCH against its (0, 0, -) seed, and the row's own output is still printed
# beneath it by the grep S4 preserves — the want-string is that output, unchanged.
arm "--sweep reds a suite whose exit and FAIL count miss its baseline as MISMATCH, and prints that suite's OWN output beneath its row" 1 \
    "FAIL something" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-red.sh|' $B" \
    "$R --sweep"

# A suite past its bound did not FAIL and did not finish, and rendering it as either loses that.
# suite-slow.sh sleeps 3s; a budget of 1 with the fixture's 1 s seed bounds at max(1, 1) + max(1,
# 1.0 x 1) = 2s — the evidence shape (TOOL-aBatchedArm-5 S1), where the factor once gave 1 x 2.
arm "a suite past its evidence bound is TIMEOUT, distinguishable from both ok and MISMATCH" 1 \
    "TIMEOUT" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t1\tbash tools/suite-slow.sh|' $B" \
    "$R --sweep"

# The wall borrowed from run-gates.sh --print-profile was 10800s against a population declaring
# 13600s for one suite, so it would have killed every real sweep for arriving on time. The
# arithmetic is now a refusal rather than a comment; the largest bound it compares against is the
# evidence one, 120s for a budget-60 row with a 1 s seed.
arm "a run wall BELOW the largest per-suite bound REFUSES rather than killing the run on time" 2 \
    "would be killed before its" \
    'true' "SELFTEST_WALL=5 $R --sweep"

# The factor-absent refusal arm that stood here is RETIRED with the `sweep-ceiling-factor:` header
# (TOOL-aBatchedArm-5 S1): nothing derives a bound from a factor any more, so there is no
# absence to refuse. Its successor is the no-reading refusal below.

# The bound is a probed capability. lib-selftest.sh runs UNBOUNDED without it, which is right for
# arms that are seconds long and fatal here, where one hang suppresses every verdict line.
arm "--sweep REFUSES when no timeout binary resolves, instead of running the bound silently inert" 2 \
    "found none of" \
    'true' "SELFTEST_TIMEOUT_BIN=definitely-not-a-binary $R --sweep"

arm "a --sweep filter matching nothing REFUSES, exactly as the serial mode's does" 2 \
    "so this run graded NOTHING at all" \
    'true' "$R --sweep --kit tools/nowhere"

# ---------------------------------------------------------------- the withheld verdict, TOOL-aPooledSweep-2
# The pool's readings are contended by construction, so the budget comparison is WITHHELD rather
# than passed. Withheld is not passed: the count is stated on every run, and the row says so too.
arm "every pooled row carries its cost verdict, and that verdict is 'withheld'" 0 \
    "cost withheld" \
    'true' "$R --sweep"

arm "the sweep STATES how many cost verdicts it withheld, so a green sweep is never budget-clean" 0 \
    "cost verdict(s) WITHHELD under pooled@" \
    'true' "$R --sweep"

arm "the sweep names the SERIAL mode as where a cost verdict comes from" 0 \
    "for a cost verdict, run the serial mode" \
    'true' "$R --sweep"

# ---------------------------------------------------------------- --pooled, TOOL-aBatchedArm-4 S2/S5
# --pooled is the declared spelling of the branch --sweep reaches, so the arms above cover its
# mechanism; these cover the spelling, the pair of verdicts one suite gets under the two modes,
# and the three remedies that now name a mode instead of the bare form (S6).
arm "--pooled over a green population exits 0 and SAYS it graded no cost" 0 \
    "NO cost verdict was issued" \
    'true' "$R --pooled"

# THE PAIR. One suite, one budget, two modes, two verdicts. suite-mid.sh sleeps 5s against a
# budget of 4: --serial grades it OVER BUDGET, --pooled withholds — the bound is max(4, 1 s seed)
# + max(1, 1.0 x 4) = 8s, so the suite finishes and the withholding is the ONLY thing standing
# between it and a verdict. (The factor once gave the same 8 s as 4 x 2; the seed is sized so the
# evidence shape clears the 5 s sleep by the same margin.)
arm "under --serial a breaching suite gets OVER BUDGET, because an uncontended clock can grade it" 1 \
    "OVER BUDGET" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t4\tbash tools/suite-mid.sh|' $B" \
    "$R --serial"

arm "under --pooled the SAME breaching suite is 'cost withheld' and the run is green, not OVER BUDGET" 0 \
    "cost withheld" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t4\tbash tools/suite-mid.sh|' $B" \
    "$R --pooled"

# THE REMEDIES NAME A MODE. Three lines interpolate the runner's own path, so a grep over the
# source could not have caught one still spelling the bare form; each is exercised instead.
arm "the missing-timeout refusal names --serial as the remedy, not the bare form" 2 \
    "Use --serial, which reports each suite" \
    'true' "SELFTEST_TIMEOUT_BIN=definitely-not-a-binary $R --pooled"

arm "a completed pooled run points at --serial for a cost verdict, by its own path" 0 \
    "for a cost verdict, run the serial mode: $R --serial" \
    'true' "$R --pooled"

# RE-CUT at TOOL-aBatchedArm-5 S4 to the parity wording: a pooled RED is a parity red and is not
# told to confirm itself serially; it names the calibrate, by the runner's own path, as what
# takes a repaired suite's new baseline.
arm "a RED pooled run names the calibrate as the remedy for a MISMATCH, by its own path, not a serial re-run" 1 \
    "one calibrate away: $R --pooled --calibrate" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-red.sh|' $B" \
    "$R --pooled"

# --rank sorts by recorded seconds, and a contended reading sorted against serial ones ranks the
# CONDITIONS. Nothing refused one until now: CONDS' second pattern accepts any text after the
# seconds, and a match there is what RANKS a row rather than what refuses it.
arm "--rank REFUSES a pooled reading by name rather than sorting it as a direct one" 1 \
    "carry no reading whose CONDITION this verb recognises" \
    "printf 'contended\t60\tbash tools/suite-ok.sh\tmeasured 42s pooled@8x1 on node t 2026-09-07, x1.5\n' >> $B && git add -A" \
    "$R --rank"

# THE OTHER EDGE. A refusal that also drops the ordinary rows is a blanket, not a predicate, and the
# arm above cannot tell the two apart on its own.
arm "the same file WITHOUT the pooled row still ranks, so the refusal is a predicate not a blanket" 0 \
    "the declared share is carried by the TOP" \
    'true' "$R --rank"

# THE EMITTER AND THE READER, JOINED. The two arms above hand-type the tag on both sides, so they
# observe the refusal and observe nothing about whether it matches what --sweep actually prints.
# This one CAPTURES the tag from a real sweep and feeds that exact string to --rank; a spelling
# drift on either side reds here and nowhere else.
arm "the tag --sweep EMITS is the tag --rank refuses, captured rather than hand-typed" 1 \
    "carry no reading whose CONDITION this verb recognises" \
    'bash tools/roundtrip.sh' \
    "$R --rank"

# ---------------------------------------------------------------- pool safety, TOOL-aPooledSweep-3
# The private TMPDIR is the redirection; the fingerprint is the observation that it held. Neither
# is a sandbox, and the arms below claim no more than that.
# RE-LABELLED at TOOL-aBatchedArm-5: the row is a MISMATCH against its (0, 0, -) seed, and the
# want-string is the suite's own FAIL line, still printed beneath the row.
arm "each pooled suite gets its own TMPDIR, so a mktemp inside it cannot collide with a sibling (a MISMATCH row, its own output beneath)" 1 \
    "FAIL scratch-under-tmpdir" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-tmpdir.sh|' $B" \
    "$R --sweep"

arm "a suite that writes into a TRACKED file reds the sweep as UNSOUND after the pool drains" 1 \
    "THE SWEEP IS UNSOUND" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-dirty.sh|' $B" \
    "$R --sweep"

# S4: a whole-run fingerprint CANNOT attribute, so it must not pretend to. The refusal names the
# serial mode as the tool that can, rather than guessing at a culprit.
arm "the unsound verdict refuses to name a culprit suite and names the serial re-run instead" 1 \
    "Re-run the SERIAL mode, which can" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-dirty.sh|' $B" \
    "$R --sweep"

# THE OTHER EDGE, and the reason the git-common-dir arm was deleted rather than narrowed: that
# directory is written by the bar itself and by every sibling worktree, so a fingerprint over it
# reds on innocent runs. This arm pins that it does not.
arm "a suite writing into the GIT COMMON DIR does not red the sweep, which is why that arm was dropped" 1 \
    "tree fingerprint MATCHED" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-gitdir.sh|' $B" \
    "$R --sweep"

# A CLEAN SWEEP SAYS THE CHECK FIRED. A run where the fingerprint never ran and one where it
# passed are the same silence otherwise.
arm "a clean sweep STATES that the fingerprint matched, rather than being silent about it" 0 \
    "tree fingerprint MATCHED before and after" \
    'true' \
    "$R --sweep"

# LIVENESS. `git status --porcelain` is EMPTY on a clean tree, so emptiness cannot be the test:
# what is asserted is that the command SUCCEEDED, and a failure refuses before any suite runs.
arm "a fingerprint that cannot be TAKEN refuses before running anything, rather than reading clean" 2 \
    "a sweep would be UNGRADED" \
    "mkdir -p shim && cp tools/git-nostatus.sh shim/git && chmod +x shim/git" \
    "PATH=\"\$PWD/shim:\$PATH\" $R --sweep"

# THE INVARIANT AS REACHED, not as printed. The width-pair arm reads what the pool was ASKED for; a
# pool that ran wider than its outer bound would satisfy that arm and break the composite invariant
# the whole re-division rests on. This reads the stamps the pool actually produced.
arm "peak concurrency is REPORTED and never exceeds the outer width the run printed" 0     "peak concurrency"     'true' "$R --sweep"

# ---------------------------------------------------------------- the closing review's fold
# THE WALL, SEEN FIRING. Until now its only arm tested the pre-flight refusal, so the kill path had
# never been observed -- and it was dead twice over: the watchdog SIGTERMed the runner itself
# (`$$` in a backgrounded subshell is the PARENT's pid), and a TERMed worker still writes a verdict
# file, so the WALL branch, which only fired on a MISSING one, was unreachable either way.
#
# THE FIXTURE IS BUILT FOR MARGIN. Budget 5 with a 1 s seed under `pooled@1x2` bounds at max(5, 1)
# + max(1, 1.0 x 5) = 10s per suite (the factor once gave the same 10 s as 5 x 2); outer 1 makes
# two waves, so a 10s wall clears the refusal. The first suite sleeps 5s and finishes well inside
# its own bound; the second sleeps 30s, so its own bound would not expire until ~15s. The wall
# lands at 10s -- five seconds clear of both, which is what keeps this arm from being a coin flip.
arm "the run WALL kills an outstanding suite, renders it WALL, and NAMES it" 1 \
    "run wall killed" \
    "sed -i 's|\t60\t|\t5\t|g; s|bash tools/suite-ok.sh|bash tools/suite-long.sh|g' $B && sed -i 's|suite-ok.sh|suite-mid.sh|g' $LEGS" \
    "SELFTEST_WALL=10 SELFTEST_OUTER_WIDTH=1 $R --sweep"

# A POOL OF ONE IS SERIAL, and the peak figure must say so. It said 2, because the overlap test
# used closed intervals on whole-second stamps and every slot handoff double-counted -- which on
# the real population would have redded the peak guard on every green sweep.
arm "a strictly serial pool reports peak 1, not a handoff double-counted as overlap" 0 \
    "peak concurrency 1 of outer 1" \
    'true' \
    "SELFTEST_OUTER_WIDTH=1 $R --sweep"

# A KNOB WITH A TYPO MUST NOT BE SILENTLY DISCARDED. Both of these used to fall through their case
# arms, leaving the operator believing a bound or a width they never got.
arm "a non-numeric SELFTEST_OUTER_WIDTH REFUSES rather than being silently ignored" 2 \
    "which is not a positive" \
    'true' \
    "SELFTEST_OUTER_WIDTH=abc $R --sweep"

arm "a non-numeric SELFTEST_WALL REFUSES rather than being silently ignored" 2 \
    "which is not a number of seconds" \
    'true' \
    "SELFTEST_WALL=soon $R --sweep"

# THE WALL MUST STOP THE DISPATCH, not merely kill what is running. Pointing the watchdog's kill at
# the workers -- which is correct -- removed the only thing that ended the run, because the runner
# used to be the thing being killed. Reproduced at 16 s, 17 s and 23 s against a 10 s wall before
# the guard went in.
# The appended rows `three` and `four` are SEEDED under the token this arm runs at, `pooled@1x2`,
# because an unevidenced row refuses the whole run by name before anything is dispatched.
arm "the wall STOPS the dispatch, so a suite it never reached is reported UNRUN rather than killed" 1 \
    "NEVER RUN and are UNGRADED" \
    "sed -i 's|\t60\t|\t5\t|g; s|bash tools/suite-ok.sh|bash tools/suite-long.sh|g' $B && sed -i 's|suite-ok.sh|suite-mid.sh|g' $LEGS && printf 'three\t5\tbash tools/suite-long.sh\tmeasured 5s on node t 2026-09-07, x1.5\nfour\t5\tbash tools/suite-long.sh\tmeasured 5s on node t 2026-09-07, x1.5\n' >> $B && bash tools/seed.sh three pooled@1x2 1 0 0 - && bash tools/seed.sh four pooled@1x2 1 0 0 - && git add -A" \
    "SELFTEST_WALL=10 SELFTEST_OUTER_WIDTH=1 $R --sweep"

# THE DERIVED WALL IS THE RUN'S STRUCTURAL CEILING, not a multiple of its worst suite. `largest x
# waves` assumed every wave was as slow as the slowest member, which over the real population is
# 2x to 15x the true maximum -- and a backstop that can never fire is not one. Under the evidence
# shape the bounds are (10 + 10) + (60 + 60) = 140 s over one slot — the same 140 s the factor
# once produced as (10 + 60) x 2, which is why the want-string survived the re-cut unchanged.
arm "the derived run wall is the bounded work over the pool, printed so it can be checked" 0 \
    "run wall 140s" \
    "sed -i '0,/\t60\t/{s|\t60\t|\t10\t|}' $B" \
    "SELFTEST_OUTER_WIDTH=1 $R --sweep"

# ---------------------------------------------------------------- the evidence bound, TOOL-aBatchedArm-5 S1
# Every arm from here to the floor line is that unit's. NONE has been observed RED: owner ruling
# 2026-09-14 (no gate until every unit of the build is built), so each arm's comment states its
# red case from the staged break alone, and the observation is the build's final gate pass.

# THE BOUND IS EVIDENCE. A budget-60 row with a 1 s seed is bounded from the BUDGET: 60 + max(1,
# 60) = 120 s, and the row says which term won and what it read. NOT YET OBSERVED RED — owner
# ruling 2026-09-14; observed at the build's final gate pass. Red when: the bound is budget x
# anything (the factor would print 120 here too, which is why the arm reads the TERM and not only
# the number), or the row names no reading.
arm "a pooled row is bounded from its serial BUDGET when the seeded reading is far below it, and says so" 0 \
    "bounded at 120s: budget won (budget 60s; reading 1s over 1 reading(s) under pooled@2x1 on node t, 2026-09-14)" \
    'true' "$R --pooled"

# A reading ABOVE the budget wins: 200 s seeded against budget 60 bounds at 200 + max(1, 200) =
# 400 s. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the bound stays at the budget's
# 120 s, i.e. the reading is read and ignored.
arm "a pooled row is bounded from its READING when the seeded reading exceeds its budget, and says so" 0 \
    "bounded at 400s: reading won (budget 60s; reading 200s" \
    "bash tools/seed.sh 'free one' pooled@2x1 200 0 0 -" \
    "$R --pooled"

# THE RUN WALL IS DERIVED FROM THE EVIDENCE BOUNDS: (120 + 400) over 2 slots is 260, floored at the
# largest bound, 400. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the wall is the
# budget-derived 120 s, or is not floored at the largest bound.
arm "the run wall is ceil(sum of evidence bounds / outer) floored at the largest evidence bound" 0 \
    "run wall 400s" \
    "bash tools/seed.sh 'free one' pooled@2x1 200 0 0 -" \
    "$R --pooled"

# And the below-the-largest refusal compares against THAT bound. NOT YET OBSERVED RED — owner
# ruling 2026-09-14. Red when: a 300 s wall is accepted over a 400 s evidence bound.
arm "a run wall below the largest EVIDENCE bound refuses, naming that bound" 2 \
    "population is 400s (an evidence bound)" \
    "bash tools/seed.sh 'free one' pooled@2x1 200 0 0 -" \
    "SELFTEST_WALL=300 $R --pooled"

# THE FACTOR IS RETIRED, not merely unread: a `sweep-ceiling-factor:` header staged back into the
# declaration changes nothing. 3 rather than 2, because 60 x 2 is the same 120 the evidence bound
# gives and could not discriminate. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: any
# factor-derived bound (180 s) or wall prints.
arm "a sweep-ceiling-factor header staged back in is IGNORED — the bound and the wall are the evidence ones" 0 \
    "bounded at 120s: budget won" \
    "printf '# sweep-ceiling-factor: 3\n' >> $B" \
    "$R --pooled"

# THE ABSENT MARGIN REFUSES, naming the file: a silent zero-margin default is a bound nobody chose.
# NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the run proceeds with no margin file.
arm "a pooled run with the margin file absent REFUSES naming it, rather than defaulting a headroom" 2 \
    "no margin declared at" \
    "rm tools/run-gates/ceiling-margin.txt" \
    "$R --pooled"

# ---------------------------------------------------------------- the no-reading refusal, S1 / AC2
# A row with no reading under (row, token, node) REFUSES the run — naming the row, the token and
# --calibrate — and executes NOTHING: the marker suite is the row that DOES have a reading, and it
# must not run either. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the run proceeds
# under any bound (rc 99 from the marker: a factor wearing a refusal's name).
arm "a row with NO reading under this token and node REFUSES the pooled run by name, naming --calibrate, and executes no suite" 2 \
    "NO pooled reading under pooled@2x1 on node t" \
    "grep -v '^free one' $E > tmp.e && mv tmp.e $E && sed -i 's|suite-ok.sh|suite-mark.sh|' $LEGS && git add -A" \
    "( $R --pooled; rc=\$?; [ -e ran.marker ] && exit 99; exit \$rc )"

# A reading under a FOREIGN node is no reading here: the key carries the node because unit 3
# measured 47 to 60 s on node `a` against ~2 s elsewhere. NOT YET OBSERVED RED — owner ruling
# 2026-09-14. Red when: a row keyed on node `z` bounds a run on node `t`.
arm "a row evidenced only under a FOREIGN node tag refuses the same way" 2 \
    "NO pooled reading under pooled@2x1 on node t" \
    "sed -i 's|\tt\t|\tz\t|' $E && git add -A" \
    "$R --pooled"

# With the registry row deleted, the node cannot be resolved and the run refuses NAMING THE USER —
# never falling back to a hostname the registry does not know. NOT YET OBSERVED RED — owner ruling
# 2026-09-14. Red when: the run resolves a node from anything but the registry, or runs.
arm "with the charter's registry row deleted, a pooled run refuses naming the user, never a hostname" 2 \
    "no registry row matches user" \
    "grep -v '^| \`t\`' AGENTS.md > tmp.a && mv tmp.a AGENTS.md" \
    "$R --pooled"

# ---------------------------------------------------------------- --calibrate, S2 / AC3, AC8
# The bootstrap grades NOTHING: no OVER BUDGET, no TIMEOUT, no sweep verdict — the subject greps
# for each and exits 99 on a hit, so the arm reds on any verdict as well as on a missing summary.
# NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: a calibration prints a verdict.
arm "--pooled --calibrate runs every selected row under the serial-sum wall and grades nothing, saying so" 0 \
    "calibrated 2 row(s), 0 red, graded none" \
    'true' \
    "( out=\$($R --pooled --calibrate); rc=\$?; printf '%s\n' \"\$out\" | grep -qE 'OVER BUDGET|TIMEOUT|sweep (GREEN|RED)' && exit 99; printf '%s\n' \"\$out\"; exit \$rc )"

# The wall is the serial SUM of the selected budgets, undivided, and it says so. NOT YET OBSERVED
# RED — owner ruling 2026-09-14. Red when: the wall is divided by the width (60) or is any bound.
arm "the calibrate wall is the serial SUM of the selected budgets, undivided, and names the term that won" 0 \
    "run wall 120s = the serial sum (serial sum 120s over 2 budget(s))" \
    'true' "$R --pooled --calibrate"

# SELFTEST_WALL TIGHTENS ONLY. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: a
# SELFTEST_WALL above the sum loosens the wall.
arm "SELFTEST_WALL above the serial sum tightens nothing under --calibrate, and says so" 0 \
    "tightens nothing" \
    'true' "SELFTEST_WALL=999 $R --pooled --calibrate"

# EACH COMPLETED ROW'S READING IS WRITTEN after the closing fingerprint, with its token, tag, rc and
# FAIL count, and the tracked file is changed by a run that still reports MATCHED — the write sits
# outside the fingerprinted window. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the
# file is unchanged (rc 99), or the write landed inside the window and the run reports UNSOUND.
arm "a calibrate over a clean fixture reports the fingerprint MATCHED and has still changed the evidence file" 0 \
    "tree fingerprint MATCHED before and after" \
    'true' \
    "( $R --pooled --calibrate; rc=\$?; git diff --quiet -- $E && exit 99; exit \$rc )"

# The seed is 30 s so a sub-second suite cannot raise it on a slow box; what is asserted is the
# line's shape — row, token, tag, the kept seconds, rc, FAIL count.
arm "a calibrate prints each reading it wrote with its token, tag, rc and FAIL count" 0 \
    "reading free one under pooled@2x1 on node t: 30s (kept at 30s" \
    "bash tools/seed.sh 'free one' pooled@2x1 30 0 0 -" \
    "$R --pooled --calibrate | grep 'rc 0, 0 FAIL, - executed'"

# SECONDS ARE MONOTONE, rc/fails/executed FOLLOW THE LATEST READING. A 50 s seed re-read by the
# red-by-design shard suite (exit 1, 3 FAIL, 81 executed, under a second) keeps 50 s and takes
# the new triple, readings 2. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: seconds
# fall to the new reading, or rc/fails stay at the old ones.
arm "a second calibrate with a LOWER reading and a different rc updates rc, fails and executed and NOT seconds" 0 \
    $'free one\tpooled@2x1\tt\t50\t1\t3\t81\t2\t' \
    "bash tools/seed.sh 'free one' pooled@2x1 50 0 0 - && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-shard.sh|' $B" \
    "$R --pooled --calibrate > /dev/null; cat $E"

# And a HIGHER reading raises them: a 1 s seed re-read by a 3 s sleep is raised. NOT YET OBSERVED
# RED — owner ruling 2026-09-14. Red when: the seconds stay at 1.
arm "a calibrate with a HIGHER reading raises that row's seconds, and prints the raise" 0 \
    "reading free one under pooled@2x1 on node t: " \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-slow.sh|' $B" \
    "$R --pooled --calibrate | grep 'raised from 1s'"

# A ROW THE WALL KILLED WRITES NO READING, IS NAMED, AND REDS THE CALIBRATE. Its seed is removed
# first so the file's silence about it is the observation. NOT YET OBSERVED RED — owner ruling
# 2026-09-14. Red when: a walled row's seconds land in the file (rc 99), or the run is green.
arm "a row the calibrate wall kills writes NO reading, is named, and the calibrate exits RED counting it walled" 1 \
    "calibrated 1 row(s), 0 red, 1 walled, 0 untrailed, graded none" \
    "grep -v '^free one' $E > tmp.e && mv tmp.e $E && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-long.sh|' $B && git add -A" \
    "( SELFTEST_WALL=3 $R --pooled --calibrate; rc=\$?; grep -q '^free one' $E && exit 99; exit \$rc )"

# A COMPLETED EXIT WITH NO TRAILER IS NOT A READING: a suite that exits 0 in under a second and
# prints nothing is `untrailed`, writes nothing, reds the calibrate. NOT YET OBSERVED RED — owner
# ruling 2026-09-14. Red when: the quiet exit is recorded as a reading (rc 99) or the run is green.
arm "a suite that exits 0 with no trailer is UNTRAILED at calibrate: no reading written, the run RED" 1 \
    "calibrated 1 row(s), 0 red, 0 walled, 1 untrailed, graded none" \
    "grep -v '^free one' $E > tmp.e && mv tmp.e $E && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-quiet.sh|' $B && git add -A" \
    "( $R --pooled --calibrate; rc=\$?; grep -q '^free one' $E && exit 99; exit \$rc )"

# A row the header DECLARES trailer-less is read as rc-plus-FAIL, and the gap is printed on the
# row. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the declared row is untrailed.
arm "a row the evidence header declares trailer-less is read as rc-plus-FAIL, and the gap is printed" 0 \
    "declared trailer-less: completion NOT witnessed" \
    "sed -i '1i # no-trailer: free one' $E && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-red.sh|' $B && git add -A" \
    "$R --pooled --calibrate"

# --calibrate OFF --pooled REFUSES naming the pair and executes no suite — three spellings, the
# serial one carrying the marker. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: any
# of them runs a row (rc 99) or writes a reading.
arm "--serial --calibrate REFUSES naming the pair and executes no suite" 2 \
    "--calibrate modifies --pooled and nothing else, and was given with '--serial'" \
    "sed -i 's|bash tools/suite-ok.sh|bash tools/suite-mark.sh|' $B" \
    "( $R --serial --calibrate; rc=\$?; [ -e ran.marker ] && exit 99; exit \$rc )"

arm "--check --calibrate REFUSES naming the pair" 2 \
    "--calibrate modifies --pooled and nothing else, and was given with '--check'" \
    'true' "$R --check --calibrate"

arm "a bare --calibrate REFUSES naming the pair" 2 \
    "--calibrate modifies --pooled and nothing else, and was given with 'no mode'" \
    'true' "$R --calibrate"

# ---------------------------------------------------------------- --reset, S2 / AC10
# Exactly the reset row's seconds are lowered, the calibrate ran that row and NO other (the other
# row is the marker suite), and the decision is printed. NOT YET OBSERVED RED — owner ruling
# 2026-09-14. Red when: the other row ran (rc 99), or the reset ran silently.
arm "--reset <row> narrows the calibrate to that row, runs no other, and prints the decision" 0 \
    "RESET free one under pooled@2x1 on node t: dropped its 500s reading" \
    "bash tools/seed.sh 'free one' pooled@2x1 500 0 0 - && bash tools/seed.sh 'held one' pooled@2x1 500 0 0 - && sed -i 's|suite-ok.sh|suite-mark.sh|' $LEGS && git add -A" \
    "( $R --pooled --calibrate --reset 'free one'; rc=\$?; [ -e ran.marker ] && exit 99; exit \$rc )"

# The reset row's seconds are LOWERED to the new reading — 500 to a sub-second suite's — with
# readings back at 1; the awk reads the row back rather than pinning a took that a slow box can
# move by a second. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the row keeps 500
# (monotone won) or readings is not 1.
arm "--reset lowers exactly that row's seconds to the new reading, readings back at 1" 0 \
    "LOWERED free one" \
    "bash tools/seed.sh 'free one' pooled@2x1 500 0 0 - && bash tools/seed.sh 'held one' pooled@2x1 500 0 0 -" \
    "$R --pooled --calibrate --reset 'free one' > /dev/null; awk -F'\t' '\$1 == \"free one\" && \$4 + 0 < 500 && \$8 == 1 { print \"LOWERED \" \$0 }' $E"

# And NO other row moves. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the other row's
# 500 s is touched.
arm "--reset moves no other row" 0 \
    $'held one\tpooled@2x1\tt\t500\t0\t0\t-\t1\t' \
    "bash tools/seed.sh 'free one' pooled@2x1 500 0 0 - && bash tools/seed.sh 'held one' pooled@2x1 500 0 0 -" \
    "$R --pooled --calibrate --reset 'free one' > /dev/null; cat $E"

# --reset off --calibrate refuses; --reset naming a row the file lacks refuses; each by name.
# NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: either runs silently.
arm "--reset off --calibrate REFUSES by name" 2 \
    "--reset lowers a row's calibrated seconds and is a modifier of --calibrate" \
    'true' "$R --pooled --reset 'free one'"

arm "--reset naming a row the evidence file lacks REFUSES by name" 2 \
    "--reset names 'ghost', and" \
    'true' "$R --pooled --calibrate --reset ghost"

# ---------------------------------------------------------------- the shape gate, S3 / AC9
# `--check` reds a duplicated key, a seven-field row, a foreign-tag row and an orphaned row, each
# naming the line; `--pooled` REFUSES over a file that will not parse rather than defaulting past
# it. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: --check is green over any of the
# four, or --pooled runs past the bad row.
arm "--check reds an evidence row whose (row, token, node) key repeats, naming the line" 1 \
    "the (row, token, node) key repeats" \
    "printf 'free one\tpooled@2x1\tt\t7\t0\t0\t-\t1\t2026-09-14\n' >> $E && git add -A" \
    "$R --check"

arm "--check reds a seven-field evidence row, naming the line" 1 \
    "7 field(s), not 9" \
    "printf 'free one\tpooled@4x2\tt\t7\t0\t0\t-\n' >> $E && git add -A" \
    "$R --check"

arm "--check reds an evidence row whose node is no tag the registry table carries" 1 \
    "no tag the charter's registry table carries" \
    "printf 'free one\tpooled@4x2\tq\t7\t0\t0\t-\t1\t2026-09-14\n' >> $E && git add -A" \
    "$R --check"

arm "--check reds an ORPHAN evidence row naming no declared budget row" 1 \
    "is an ORPHAN" \
    "printf 'nobody\tpooled@2x1\tt\t7\t0\t0\t-\t1\t2026-09-14\n' >> $E && git add -A" \
    "$R --check"

arm "--check over a well-formed evidence file is green and counts its rows" 0 \
    "4 pooled evidence row(s) well-formed" \
    'true' "$R --check"

# ---------------------------------------------------------------- the trailer rule, statically
# aBatchedArm closing review D4: a suite whose only trailer sits behind `[ "$st" = 0 ] &&` is
# UNTRAILED under --pooled the moment it reds, and the calibrate then writes no reading for it.
# --check holds the rule over the rows under each `# pooled-kit:` the evidence header declares.
# Observed RED first on a clone carrying the five kit suites the review named.
arm "--check reds a pooled-kit row whose script prints its trailer only under [ \$st = 0 ], naming the row and the script" 1 \
    "row 'free one': tools/suite-greenonly.sh prints no trailer outside a" \
    "printf '#!/usr/bin/env bash\nst=1\n[ \"\$st\" = 0 ] && echo \"PASS (1 assertions)\"\nexit \$st\n' > tools/suite-greenonly.sh && printf '# pooled-kit: tools/\n' >> $E && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-greenonly.sh|' $B && git add -A" \
    "$R --check"

arm "--check skips a pooled-kit row declared no-trailer and counts what it graded" 0 \
    "trailer arm graded 1 row(s) under pooled-kit tools/ (1 declared no-trailer)" \
    "printf '#!/usr/bin/env bash\nst=1\n[ \"\$st\" = 0 ] && echo \"PASS (1 assertions)\"\nexit \$st\n' > tools/suite-greenonly.sh && printf '# pooled-kit: tools/\n# no-trailer: free one\n' >> $E && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-greenonly.sh|' $B && git add -A" \
    "$R --check"

arm "--check with no pooled-kit declared says the trailer arm graded NOTHING rather than passing silently" 0 \
    "no pooled-kit declared so the trailer arm graded NOTHING" \
    'true' "$R --check"

# ---------------------------------------------------------------- the no-baseline sentinel, D3
# A row printing `expected set not yet observed` has its trailer and its own exit, and is still
# NOT a reading: both rows are made sentinels so a byte-unchanged evidence file is the whole
# assertion (rc 99 otherwise), and the seeded MISMATCH below is the same refusal under --pooled.
arm "--pooled --calibrate reds a row whose output carries the no-baseline sentinel as UNTRAILED and writes no reading" 1 \
    "a group with no expected set is a refusal, not a reading" \
    "sed -i 's|tools/suite-ok.sh|tools/suite-sentinel.sh|g' $B $LEGS && git add -A" \
    "( $R --pooled --calibrate; rc=\$?; git diff --quiet -- $E || exit 99; exit \$rc )"

arm "--pooled renders a sentinel-carrying row MISMATCH even when its (rc, fails, executed) equals the baseline" 1 \
    "a group with no expected set is a refusal, never parity" \
    "bash tools/seed.sh 'free one' pooled@2x1 1 1 1 81 && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-sentinel.sh|' $B" \
    "$R --pooled"

# The row's output outlives the scratch: the `observed:` line the paste is taken from is in the
# kept file, and the row names it. rc 98 if the file lacks it, 99 if the file is absent.
arm "a calibrate keeps each row's output under gate-logs/selftests and names the path on a row that is not ok" 1 \
    "output: " \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-sentinel.sh|' $B && git add -A" \
    "( $R --pooled --calibrate; rc=\$?; f=\$(git rev-parse --git-dir)/gate-logs/selftests/free_one.out; [ -s \"\$f\" ] || exit 99; grep -q '^    observed: ' \"\$f\" || exit 98; exit \$rc )"

# ---------------------------------------------------------------- an unsound calibrate, D7
# The inverse of the `fingerprint MATCHED` arm: a suite that writes into a tracked file makes the
# run UNSOUND, and an unsound calibrate writes NOTHING — the other row's clean reading included.
arm "an UNSOUND calibrate writes no reading at all and says so, leaving the evidence file byte-unchanged" 1 \
    "readings NOT written: this calibrate was unsound" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-dirty.sh|' $B && git add -A" \
    "( $R --pooled --calibrate; rc=\$?; git diff --quiet -- $E || exit 99; exit \$rc )"

# ---------------------------------------------------------------- a kill is not a completion, D8
# A DECLARED trailer-less row that outlives the 3 s wall's TERM is KILLed by the worker's grace
# and exits 137: the WALL branch keys on 143, and the declared-nt clause took any rc as a reading.
# Its seed is removed first so the file's silence about it is the observation (rc 99 otherwise).
arm "a declared trailer-less row killed at rc 137 is KILLED, not read: no reading written, the row named" 1 \
    "is a kill, not a completion — NO reading written" \
    "grep -v '^free one' $E > tmp.e && mv tmp.e $E && sed -i '1i # no-trailer: free one' $E && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-stubborn.sh|' $B && git add -A" \
    "( SELFTEST_WALL=3 $R --pooled --calibrate; rc=\$?; grep -q '^free one' $E && exit 99; exit \$rc )"

# ---------------------------------------------------------------- GOV_NODE is a registry tag, D11
# The write path trusted GOV_NODE verbatim while --check refused the row it wrote; both now read
# the same table. The evidence file is byte-unchanged (rc 99 otherwise) and nothing ran.
arm "GOV_NODE naming no registry tag is REFUSED by the calibrate, naming the table, with the evidence file unchanged" 2 \
    "GOV_NODE is 'zz', which is no tag the charter's" \
    'true' \
    "( GOV_NODE=zz $R --pooled --calibrate; rc=\$?; git diff --quiet -- $E || exit 99; exit \$rc )"

arm "--pooled over an evidence file that will not parse REFUSES naming the file, rather than defaulting past the row" 2 \
    "will not parse" \
    "printf 'free one\tpooled@4x2\tt\t7\t0\t0\t-\n' >> $E && git add -A" \
    "$R --pooled"

# ---------------------------------------------------------------- AC4: --rank is untouched
# Pooled readings live in their own file, never in the budget file's fourth column, so --rank's
# refusal of `pooled@` has nothing to refuse after a calibrate. NOT YET OBSERVED RED — owner
# ruling 2026-09-14. Red when: a calibrate writes a `pooled@` token into the budget file.
arm "--rank still exits 0 after a calibrate, because pooled readings never enter the budget file" 0 \
    "the declared share is carried by the TOP" \
    'true' "$R --pooled --calibrate > /dev/null; $R --rank"

# ---------------------------------------------------------------- parity, S4 / AC11
# A red-by-design row whose (rc, FAIL, executed) MATCHES its baseline is `ok` and the run is GREEN.
# NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: a matching red-by-design row exits 1.
arm "a red-by-design row whose (rc, fails, executed) matches its baseline renders ok ... matched and the run exits 0" 0 \
    "ok (rc 1, 3 FAIL, 81 executed matched)" \
    "bash tools/seed.sh 'free one' pooled@2x1 1 1 3 81 && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-shard.sh|' $B" \
    "$R --pooled"

# One whose triple differs is MISMATCH naming both and the acceptance, exit 1. NOT YET OBSERVED
# RED — owner ruling 2026-09-14. Red when: a mismatching triple exits 0 or names one triple only.
arm "a row whose triple differs from its baseline renders MISMATCH naming both triples and the acceptance, and exits 1" 1 \
    "(rc 1, 3 FAIL, 81 executed) against baseline (rc 1, 2 FAIL, 81 executed); --calibrate to take the new baseline, --reset <row> to lower seconds" \
    "bash tools/seed.sh 'free one' pooled@2x1 1 1 2 81 && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-shard.sh|' $B" \
    "$R --pooled"

# THE FAST RED: exit 1 in under a second on an unbound variable, zero FAIL lines, no trailer,
# against a baseline of three — MISMATCH, never matched. NOT YET OBSERVED RED — owner ruling
# 2026-09-14. Red when: the crash reads as matched, which an rc-only oracle would say.
arm "a row exiting 1 in under a second with zero FAIL lines against a baseline of three is MISMATCH" 1 \
    "(rc 1, 0 FAIL, - executed) against baseline (rc 1, 3 FAIL, 81 executed), and NO trailer in its output" \
    "bash tools/seed.sh 'free one' pooled@2x1 1 1 3 81 && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-crash.sh|' $B" \
    "$R --pooled"

# A trailer-less completion at GRADE against a seeded green row is MISMATCH too. NOT YET OBSERVED
# RED — owner ruling 2026-09-14. Red when: the quiet exit 0 matches (0, 0, -) by numbers alone.
arm "a suite that exits 0 with no trailer is MISMATCH at grade against a seeded green row" 1 \
    "(rc 0, 0 FAIL, - executed) against baseline (rc 0, 0 FAIL, - executed), and NO trailer in its output" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-quiet.sh|' $B" \
    "$R --pooled"

# THE GREEN SUMMARY names every count at zero. NOT YET OBSERVED RED — owner ruling 2026-09-14.
# Red when: any of the five words is absent from a green summary.
arm "a GREEN pooled summary prints killed, walled, unrun, unstarted and mismatched, each 0" 0 \
    "killed 0 · walled 0 · unrun 0 · unstarted 0 · mismatched 0" \
    'true' "$R --pooled"

# EACH NON-COMPLETION OUTCOME COUNTED UNDER ITS OWN WORD, one fixture row staged into each class,
# the run RED on every one. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: the count
# sits under another word, or the run is green.
arm "the summary counts a row killed at its own bound under 'killed'" 1 \
    "killed 1 · walled 0 · unrun 0 · unstarted 0 · mismatched 0" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t1\tbash tools/suite-slow.sh|' $B" \
    "$R --pooled"

arm "the summary counts a row the wall killed under 'walled'" 1 \
    "killed 0 · walled 1 · unrun 0 · unstarted 0 · mismatched 0" \
    "sed -i 's|\t60\t|\t5\t|g; s|bash tools/suite-ok.sh|bash tools/suite-long.sh|g' $B && sed -i 's|suite-ok.sh|suite-mid.sh|g' $LEGS" \
    "SELFTEST_WALL=10 SELFTEST_OUTER_WIDTH=1 $R --pooled"

arm "the summary counts rows the wall never dispatched under 'unrun'" 1 \
    "killed 0 · walled 1 · unrun 2 · unstarted 0 · mismatched 0" \
    "sed -i 's|\t60\t|\t5\t|g; s|bash tools/suite-ok.sh|bash tools/suite-long.sh|g' $B && sed -i 's|suite-ok.sh|suite-mid.sh|g' $LEGS && printf 'three\t5\tbash tools/suite-long.sh\tmeasured 5s on node t 2026-09-07, x1.5\nfour\t5\tbash tools/suite-long.sh\tmeasured 5s on node t 2026-09-07, x1.5\n' >> $B && bash tools/seed.sh three pooled@1x2 1 0 0 - && bash tools/seed.sh four pooled@1x2 1 0 0 - && git add -A" \
    "SELFTEST_WALL=10 SELFTEST_OUTER_WIDTH=1 $R --pooled"

# THE WORKER-DEATH CLASS: an unbound variable under `set -u` inside the fixture's copy of the
# runner's own worker, staged on the line before it makes its scratch directory, so every worker
# dies before its verdict file exists — the class the runner's own `run_sweep_one` comment records.
# Read as `unstarted`, the run RED. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: a
# row with no verdict file and no wall breach reads GREEN or is counted under another word.
arm "a worker dying under set -u before its verdict file is counted under 'unstarted', the run RED" 1 \
    "killed 0 · walled 0 · unrun 0 · unstarted 2 · mismatched 0" \
    "sed -i 's|^    mkdir -p \"\$d/tmp\" \|\| return\$|    : \"\$SELFTEST_STAGED_UNBOUND\"; mkdir -p \"\$d/tmp\" \|\| return|' $RC && grep -q SELFTEST_STAGED_UNBOUND $RC" \
    "$R --pooled"

arm "the summary counts a completed row that missed its baseline under 'mismatched'" 1 \
    "killed 0 · walled 0 · unrun 0 · unstarted 0 · mismatched 1" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-red.sh|' $B" \
    "$R --pooled"

# THE WITHHELD LINE THE KIT RUNNER PARSES SURVIVES parity, because §3's first non-goal keeps the
# cost verdict withheld. NOT YET OBSERVED RED — owner ruling 2026-09-14. Red when: a matched
# red-by-design row is not counted as a withheld cost verdict.
arm "a matched red-by-design row still counts as a WITHHELD cost verdict" 0 \
    "2 cost verdict(s) WITHHELD under pooled@2x1" \
    "bash tools/seed.sh 'free one' pooled@2x1 1 1 3 81 && sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-shard.sh|' $B" \
    "$R --pooled"

run_arms run-selftests.test.sh
