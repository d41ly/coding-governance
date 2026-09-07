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

SELFTEST_FLOOR=41

# The fixture is a MINIMAL repo the runner can root itself in: two suites it can execute, a manifest
# with one held leg, and a declaration that covers it. Every arm below starts from this green state
# and stages exactly one break into it, which is the only way a refusal can be attributed.
build_repo() {
  mkdir -p tools/run-gates || return 2
  git init -q . >/dev/null 2>&1 || return 2
  git config user.email t@t && git config user.name t || return 2
  cp "$RUNNER" tools/run-gates/run-selftests.sh || return 2

  printf '#!/usr/bin/env bash\necho "suite ok"\nexit 0\n' > tools/suite-ok.sh
  printf '#!/usr/bin/env bash\necho "FAIL something"\nexit 1\n' > tools/suite-red.sh
  printf '#!/usr/bin/env bash\nsleep 3\nexit 0\n' > tools/suite-slow.sh
  # THE WALL ARM'S PAIR. Its margins have to be SECONDS or the arm is a coin flip: the wall and
  # the per-suite bound both expire near the same instant otherwise, and whichever wins decides
  # whether the row renders WALL or TIMEOUT. A 5s first suite puts the wall 5s clear of the start
  # and 5s clear of the second suite's own bound.
  printf '#!/usr/bin/env bash\nsleep 5\nexit 0\n' > tools/suite-mid.sh
  printf '#!/usr/bin/env bash\nsleep 30\nexit 0\n' > tools/suite-long.sh

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
    printf '# sweep-ceiling-factor: 2\n'
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

# ---------------------------------------------------------------- the run, and its liveness
arm "a --kit filter matching nothing REFUSES, because an unknown filter and a clean sweep look alike" 2 \
    "so this run graded NOTHING at all" \
    'true' "$R --kit tools/nowhere"

arm "a population whose every suite passes reports GREEN and says none of it runs on the bar" 0 \
    "self-tests GREEN" \
    'true' "$R"

arm "a suite that fails reds the run" 1 "self-tests RED" \
    "sed -i 's|bash tools/suite-ok.sh|bash tools/suite-red.sh|' $B" \
    "$R"

arm "a suite that overruns its declared budget reds and NAMES the number it broke" 1 \
    "OVER BUDGET" \
    "sed -i 's|free one\t60|free one\t1|; s|bash tools/suite-ok.sh|bash tools/suite-slow.sh|' $B" \
    "$R"

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
' >> $B && git add -A"     "$R"

# ---------------------------------------------------------------- --sweep, TOOL-aPooledSweep-1
# The pool answers ONE question and issues no cost verdict, so every arm here reads the sweep
# verdict and none of them reads a budget. The budget arms above still read the serial mode.
arm "--sweep over a green population exits 0 and SAYS it graded no cost" 0 \
    "NO cost verdict was issued" \
    'true' "$R --sweep"

arm "--sweep prints the width pair it chose BEFORE the first verdict, so the invariant is checkable" 0 \
    "(outer " \
    'true' "$R --sweep"

arm "--sweep reds on a failing suite and prints that suite's OWN output beneath its row" 1 \
    "FAIL something" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t60\tbash tools/suite-red.sh|' $B" \
    "$R --sweep"

# A suite past its bound did not FAIL and did not finish, and rendering it as either loses that.
# suite-slow.sh sleeps 3s; a budget of 1 derives a 2s bound.
arm "a suite past its derived bound is TIMEOUT, distinguishable from both ok and FAIL" 1 \
    "TIMEOUT" \
    "sed -i 's|free one\t60\tbash tools/suite-ok.sh|free one\t1\tbash tools/suite-slow.sh|' $B" \
    "$R --sweep"

# The wall borrowed from run-gates.sh --print-profile was 10800s against a population declaring
# 13600s for one suite, so it would have killed every real sweep for arriving on time. The
# arithmetic is now a refusal rather than a comment.
arm "a run wall BELOW the largest per-suite bound REFUSES rather than killing the run on time" 2 \
    "would be killed before its" \
    'true' "SELFTEST_WALL=5 $R --sweep"

arm "a declaration with no sweep-ceiling-factor REFUSES rather than backgrounding unbounded suites" 2 \
    "declares no sweep-ceiling-factor" \
    "grep -v 'sweep-ceiling-factor' $B > tmp.b && mv tmp.b $B" \
    "$R --sweep"

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
arm "each pooled suite gets its own TMPDIR, so a mktemp inside it cannot collide with a sibling" 1 \
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
# THE FIXTURE IS BUILT FOR MARGIN. Budget 5 x factor 2 = a 10s per-suite bound; outer 1 makes two
# waves, so a 10s wall clears the refusal. The first suite sleeps 5s and finishes well inside its
# own bound; the second sleeps 30s, so its own bound would not expire until ~16s. The wall lands at
# 10s -- five seconds clear of both, which is what keeps this arm from being a coin flip.
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

run_arms run-selftests.test.sh
