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

# ---- THE SECOND KIT'S PATHS ARE DERIVED, never typed. `--attribute` forwards through
# ---- `run-unattended-gates.sh`, whose own `--kit` filter names that kit's directory, so the
# ---- fixture needs a suite under it — and the comment above applies with full force: a second kit
# ---- path spelled here is a NEW literal, and the install-prefix checker is a shrink-only BAN.
# ---- `git ls-files` names the file, and the directory falls out of it.
U=$(git -C "$ROOT" ls-files --full-name -- '*run-unattended-gates.sh' | head -1)
[ -n "$U" ] || { echo "run-selftests.test: no tracked run-unattended-gates.sh to derive from"; exit 2; }
UDIR=$(dirname -- "$U")
# This script's own repo-relative path, derived the same way the runner derives its own.
RUNNER_REL="$(git -C "$(dirname -- "$RUNNER")" rev-parse --show-prefix 2>/dev/null)$(basename -- "$RUNNER")"

# ---- THE BASE THE DEFAULT MODE IS PINNED TO, an immutable sha rather than a moving ref.
# ---- `TOOL-dDerivedDocket-1` added `--attribute` on the promise that the no-flag mode's stdout and
# ---- exit are UNCHANGED, and the parity arm below is that promise rather than an assertion of it.
# ---- IF YOU CHANGE THE DEFAULT MODE'S OUTPUT ON PURPOSE: re-pin this line in the same commit and
# ---- say so in the message. A red here means the mode the flag agreed not to touch has moved, and
# ---- the arm cannot tell a deliberate move from an accidental one — only you can.
ATTR_BASE=fb07ca25

SELFTEST_FLOOR=69

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

  # ---------------------------------------------------------------- the attribution fixture
  # TOOL-dDerivedDocket-1. TWO COMMITS, and that is the whole shape: commit one is R, the baseline
  # `--attribute` measures against, and commit two is L, which is what the working tree holds. Every
  # arm below passes `HEAD~1` as R and mutates L if it needs to.
  #
  # ONE SUITE PER CONDITION, each with its OWN row, because `--kit` filters on a substring of the
  # argv — so `--kit tools/attr/<file>.sh` selects exactly that suite and no arm pays for the rest.
  # A shared suite mutated per arm would make every arm's cost the population's cost.
  #
  # THE NAMES BELOW MUST STAY MUTUALLY NON-PREFIXING, because a substring filter is exactly the
  # id-matched-as-a-substring shape: `deadl.sh` must not select `deadl9.sh`, and `both.sh` must not
  # select `deadboth.sh` — the `.sh` and the `/` in front are what keep each one alone today. A
  # filter that matched two suites would move the counts, and one that matched none REFUSES, so
  # either mistake is loud; a new suite named as another's prefix is the way to make it quiet.
  #
  # THE ROWS ARE NOT IN L'S DECLARATION. They sit in `rows.txt` and each attribution arm appends
  # them, which leaves the declaration the arms above this line read BYTE-IDENTICAL: the derived
  # run-wall arm computes its number from the budgets present, so two extra rows would red an arm
  # that has nothing to do with this flag.
  mkdir -p tools/attr "$UDIR" || return 2
  attr_suite() { # file · body line...
    local f=$1; shift
    { printf '#!/usr/bin/env bash\n'; printf '%s\n' "$@"; } > "tools/attr/$f"
  }
  # R's versions.
  attr_suite inherit.sh   'echo "FAIL arm A"' 'exit 1'
  attr_suite both.sh      'echo "FAIL arm A"' 'exit 1'
  attr_suite fixed.sh     'echo "FAIL arm F"' 'exit 1'
  attr_suite deadl.sh     'echo "arm ran"' 'exit 0'
  # The count line is deliberate: KF14's DEAD PROBE is "non-zero exit and no FAIL line", WITH or
  # WITHOUT one, and a rule that also demanded the count be absent reads this suite as clean.
  attr_suite deadl9.sh    'echo "PASS (2 arms, width 1)"' 'exit 0'
  attr_suite over.sh      'exit 0'
  attr_suite deadr.sh     'exit 3'
  attr_suite deadboth.sh  'exit 3'
  attr_suite absent.sh    'exit 0'
  # Slow enough on the R side that a short outer bound can kill the run mid-measurement, which is
  # the only way to observe that a killed run caches nothing.
  attr_suite cache.sh     'sleep 4' 'exit 0'
  attr_suite variant-deadr-fail.sh 'echo "FAIL arm A"' 'exit 1'
  printf '#!/usr/bin/env bash\necho "the delegated suite ran"\nexit 0\n' > "$UDIR/attr-u.sh"

  {
    printf 'attr inherit\t60\tbash tools/attr/inherit.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr both\t60\tbash tools/attr/both.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr fixed\t60\tbash tools/attr/fixed.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr deadl\t60\tbash tools/attr/deadl.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr deadl9\t60\tbash tools/attr/deadl9.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr over\t1\tbash tools/attr/over.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr deadr\t60\tbash tools/attr/deadr.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr deadboth\t60\tbash tools/attr/deadboth.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr cache\t60\tbash tools/attr/cache.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
    printf 'attr unattended\t60\tbash %s/attr-u.sh\tmeasured 2s on node t 2026-09-20, x1.5\n' "$UDIR"
    # LAST, and deliberately excluded from R's declaration below: this is the row that tests the
    # `absent` path, where the baseline declares no such suite at all.
    printf 'attr absent\t60\tbash tools/attr/absent.sh\tmeasured 2s on node t 2026-09-20, x1.5\n'
  } > tools/attr/rows.txt

  # THE DELEGATING WRAPPER, copied so the forwarding arm exercises the real file rather than a
  # description of it. Its `--checks` half is never reached under `--attribute`, which defaults the
  # half selector to the self-tests, so none of those checkers has to exist here.
  cp "$ROOT/$U" "$U" || return 2

  # THE RUNNER AS OF BASE, for the byte-parity arm. An unreachable sha writes nothing and the arm's
  # own liveness line refuses rather than comparing against an empty file.
  git -C "$ROOT" show "$ATTR_BASE:$RUNNER_REL" > tools/attr/base-runner.sh 2>/dev/null || : > tools/attr/base-runner.sh

  {
    printf '#!/usr/bin/env bash\n'
    printf 'set -u\n'
    # AN ABSENT BASE RUNNER IS A REFUSAL, not a comparison against an empty file: two empty strings
    # are equal, which would certify byte-parity while measuring nothing at all.
    printf '[ -s tools/attr/base-runner.sh ] || { echo "nope: no BASE runner in the fixture"; exit 1; }\n'
    # DURATIONS NORMALISED ON BOTH SIDES. The serial mode prints each suite's seconds, so an
    # unnormalised comparison is a coin flip on a loaded box and would red for the clock.
    printf 'norm() { sed -E "s/[0-9]+s/Ns/g"; }\n'
    printf 'a=$(%s --kit tools/suite-ok.sh 2>&1); ra=$?\n' "$R"
    printf 'b=$(bash tools/attr/base-runner.sh --kit tools/suite-ok.sh 2>&1); rb=$?\n'
    printf '[ "$ra" = "$rb" ] || { echo "nope: exit $ra against $rb"; exit 1; }\n'
    printf 'if [ "$(printf "%%s\\n" "$a" | norm)" = "$(printf "%%s\\n" "$b" | norm)" ]; then\n'
    printf '  echo "default mode matches the BASE runner, exit $ra"\n'
    printf 'else\n'
    printf '  echo "nope: the default mode diverged from the BASE runner"\n'
    printf '  diff <(printf "%%s\\n" "$a" | norm) <(printf "%%s\\n" "$b" | norm) | head -20\n'
    printf '  exit 1\n'
    printf 'fi\n'
  } > tools/attr/parity.sh

  {
    printf '#!/usr/bin/env bash\n'
    printf 'set -u\n'
    printf 'b=$(git worktree list | wc -l)\n'
    printf '%s --attribute HEAD~1 --kit tools/attr/cache.sh >/dev/null 2>&1\n' "$R"
    printf 'a=$(git worktree list | wc -l)\n'
    printf '[ "$b" = "$a" ] && echo "worktree count unchanged $a" || { echo "nope: $b -> $a"; exit 1; }\n'
  } > tools/attr/wtcount.sh

  # ---- COMMIT ONE: R. Its declaration carries every attribution row EXCEPT `attr absent`.
  grep -v '^attr absent' tools/attr/rows.txt >> "$B" || return 2
  git add -A >/dev/null 2>&1 || return 2
  git commit -q -m 'the baseline R' >/dev/null 2>&1 || return 2

  # ---- COMMIT TWO: L. The declaration goes back to exactly what the arms above expect, and the
  # ---- suites take their working-tree behaviour.
  grep -v '^attr ' "$B" > tmp.b && mv tmp.b "$B" || return 2
  attr_suite inherit.sh  'echo "FAIL arm A"' 'echo "FAIL arm B"' 'exit 1'
  attr_suite fixed.sh    'echo "arm ran"' 'exit 0'
  attr_suite deadl.sh    'exit 3'
  attr_suite deadl9.sh   'echo "PASS (2 arms, width 1)"' 'exit 3'
  attr_suite over.sh     'sleep 3' 'exit 0'
  attr_suite deadr.sh    'echo "arm ran"' 'exit 0'
  attr_suite absent.sh   'echo "FAIL arm Z"' 'exit 1'
  attr_suite cache.sh    'exit 0'
  git add -A >/dev/null 2>&1 || return 2
  git commit -q -m 'the working tree L' >/dev/null 2>&1 || return 2
}
build_fixture build_repo || exit 2

# The one setup every attribution arm shares: L's declaration gains the rows R already carries.
ATTR_ROWS="cat tools/attr/rows.txt >> $B"


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

# THE WALL MUST STOP THE DISPATCH, not merely kill what is running. Pointing the watchdog's kill at
# the workers -- which is correct -- removed the only thing that ended the run, because the runner
# used to be the thing being killed. Reproduced at 16 s, 17 s and 23 s against a 10 s wall before
# the guard went in.
arm "the wall STOPS the dispatch, so a suite it never reached is reported UNRUN rather than killed" 1 \
    "NEVER RUN and are UNGRADED" \
    "sed -i 's|\t60\t|\t5\t|g; s|bash tools/suite-ok.sh|bash tools/suite-long.sh|g' $B && sed -i 's|suite-ok.sh|suite-mid.sh|g' $LEGS && printf 'three\t5\tbash tools/suite-long.sh\tmeasured 5s on node t 2026-09-07, x1.5\nfour\t5\tbash tools/suite-long.sh\tmeasured 5s on node t 2026-09-07, x1.5\n' >> $B && git add -A" \
    "SELFTEST_WALL=10 SELFTEST_OUTER_WIDTH=1 $R --sweep"

# THE DERIVED WALL IS THE RUN'S STRUCTURAL CEILING, not a multiple of its worst suite. `largest x
# waves` assumed every wave was as slow as the slowest member, which over the real population is
# 2x to 15x the true maximum -- and a backstop that can never fire is not one.
arm "the derived run wall is the bounded work over the pool, printed so it can be checked" 0 \
    "run wall 140s" \
    "sed -i '0,/\t60\t/{s|\t60\t|\t10\t|}' $B" \
    "SELFTEST_OUTER_WIDTH=1 $R --sweep"

# ---------------------------------------------------------------- --attribute, TOOL-dDerivedDocket-1
# THE QUESTION THIS FLAG ANSWERS is not "did the suite fail" but "did it fail BEFORE this tree
# touched anything". Every arm below runs one fixture suite against `HEAD~1`, and each stages the
# ONE condition it is written for. The fixture's two commits are what make that possible: the arm
# can differ at L, at R, or on both sides, which no single-commit fixture can express.

# S2/AC1. Without the normaliser, A's line carries the scratch worktree's path at R and the working
# tree's at L, compares unequal, and the INHERITED failure reads NEW — which passes the blame for a
# pre-existing failure to the unit that merely ran next.
arm "--attribute separates a failure the BASELINE already had from one only this tree has" 1 \
    "NEW 1 · INHERITED 1 · FIXED 0" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/inherit.sh"

arm "the INHERITED member line NAMES the failure, so a reader can file it rather than re-diagnose it" 1 \
    "INHERITED  FAIL arm A" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/inherit.sh"

arm "the NEW member line names the failure this tree is actually answerable for" 1 \
    "NEW        FAIL arm B" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/inherit.sh"

# S5/AC3. The no-flag loop sets st=1 whenever a suite exits non-zero, and inheriting that is the
# whole defect: it fails every unit for failures filed against other units.
arm "a failure present on BOTH sides is INHERITED and EXITS 0 — inheriting a red is not causing one" 0 \
    "verdict clean" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/both.sh"

arm "that inherited-only suite reads NEW 0, so the token and the counts agree" 0 \
    "NEW 0 · INHERITED 1 · FIXED 0" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/both.sh"

# S3/AC2. An abort produces an EMPTY failure set, which is indistinguishable from a clean run by
# set membership alone — green by absence, and KF14's blocker.
arm "a suite that ABORTS at L with no FAIL line is a DEAD PROBE, never an empty failure set" 1 \
    "DEAD PROBE at L" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/deadl.sh"

arm "a DEAD PROBE at L is EXCLUDED from the attributed count and reds the verdict" 1 \
    "attributed 0 of 1 suite(s)" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/deadl.sh"

arm "the summary counts that dead side separately, so a reader can tell it from a new failure" 1 \
    "DEAD L 1 · DEAD R 0 · OVER 0 · verdict red" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/deadl.sh"

# AC9. The count line is the trap: a rule that also required it to be ABSENT would read a suite
# that printed its count and then died as an empty set.
arm "a suite that prints its COUNT line and then dies is still a DEAD PROBE at L" 1 \
    "DEAD PROBE at L" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/deadl9.sh"

# S1/AC5. A symmetric difference folds FIXED into NEW, which reds a unit for repairing something.
arm "a failure present at R and GONE at L is FIXED, and the exit status is unaffected by it" 0 \
    "FIXED      FAIL arm F" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/fixed.sh"

# F4/AC10. Charter §7 says a runner REDS on a cost breach, and the mode every self-test unit
# verifies with is the last place to quietly suspend that.
arm "an L-side budget breach still REDS under --attribute, and names the number it broke" 1 \
    "OVER BUDGET at L" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/over.sh"

arm "that breach is reported APART from NEW, which reads 0, so the two causes never blur" 1 \
    "NEW 0 · INHERITED 0 · FIXED 0 · DEAD L 0 · DEAD R 0 · OVER 1 · verdict red" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/over.sh"

# F5/AC12. A dead R is the baseline being broken, which is exactly the state the unit that FIXES it
# starts from — so failing the run on it leaves that unit unable ever to verify its own fix.
arm "a DEAD PROBE at R alone never reds the run, or the unit fixing that abort could not verify it" 0 \
    "DEAD R 1 · OVER 0 · verdict clean" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/deadr.sh"

arm "that dead baseline is REPORTED rather than silently treated as a clean one" 0 \
    "DEAD PROBE at R" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/deadr.sh"

arm "an L failure over a DEAD R reads NEW and never INHERITED — a dead side has no members" 1 \
    "NEW        FAIL arm A" \
    "$ATTR_ROWS && cp tools/attr/variant-deadr-fail.sh tools/attr/deadr.sh" \
    "$R --attribute HEAD~1 --kit tools/attr/deadr.sh"

arm "a suite dead on BOTH sides reds, or a consumer passes with its own arms never executed" 1 \
    "DEAD L 1 · DEAD R 1" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/deadboth.sh"

# S3. A suite the baseline never declared has no R-side set at all, which reads the same way a dead
# R does: everything at L is this tree's own.
arm "a suite the BASELINE does not declare reads 'absent' at R, and all of its L failures are NEW" 1 \
    " absent" \
    "$ATTR_ROWS" \
    "$R --attribute HEAD~1 --kit tools/attr/absent.sh"

# S4/AC4. The cache is the only reason "each suite once per unit" is affordable across twelve
# units, and the only dangerous way to build it is to write it before the R run returns.
# These three arms need a `timeout` binary for the kill; without one the setup fails LOUDLY as ERR.
arm "a KILLED R run caches nothing, so the next run measures the baseline FRESH" 0 \
    " fresh" \
    "$ATTR_ROWS && timeout -k 1 2 $R --attribute HEAD~1 --kit tools/attr/cache.sh >/dev/null 2>&1; true" \
    "$R --attribute HEAD~1 --kit tools/attr/cache.sh"

arm "a COMPLETED R run is served from the cache next time, which is what bounds the doubled cost" 0 \
    " cached" \
    "$ATTR_ROWS && $R --attribute HEAD~1 --kit tools/attr/cache.sh >/dev/null 2>&1; true" \
    "$R --attribute HEAD~1 --kit tools/attr/cache.sh"

arm "a cached run adds NO worktree entry at all, so the cache is a real saving and not a re-run" 0 \
    "worktree count unchanged" \
    "$ATTR_ROWS && $R --attribute HEAD~1 --kit tools/attr/cache.sh >/dev/null 2>&1; true" \
    'bash tools/attr/wtcount.sh'

# AC8. The flag is additive or it is nothing: every consumer of the no-flag mode predates it.
arm "the DEFAULT mode is byte-identical to the runner at BASE, so no attribution path runs without the flag" 0 \
    "default mode matches the BASE runner" \
    'true' \
    'bash tools/attr/parity.sh'

# S6/F2/AC6. The delegating wrapper must forward the flag AND say what it did not attribute — a
# half that runs unattributed and says nothing is the silence this repo keeps filing.
arm "the unattended wrapper FORWARDS --attribute to its self-test half" 0 \
    "attributed 1 of 1 suite(s)" \
    "$ATTR_ROWS" \
    "bash $U --attribute HEAD~1"

arm "and it STATES that its checks half is not attributed, rather than leaving it to be inferred" 0 \
    "the --checks half is NOT attributed" \
    "$ATTR_ROWS" \
    "bash $U --attribute HEAD~1"

# The refusals. An unresolvable baseline must refuse before running anything: running L and calling
# every failure NEW is the worst of both answers.
arm "an --attribute value naming no commit REFUSES before running a single suite" 2 \
    "names no commit in this repository" \
    "$ATTR_ROWS" \
    "$R --attribute deadbeefdeadbeef --kit tools/attr/both.sh"

# A knob accepted and ignored leaves the operator believing a baseline they never got — the same
# shape this file already arms for SELFTEST_WALL and SELFTEST_OUTER_WIDTH.
arm "--attribute combined with a mode that runs nothing REFUSES rather than silently ignoring the flag" 2 \
    "cannot be combined with" \
    'true' \
    "$R --attribute HEAD~1 --list"

arm "a bare --attribute with no value REFUSES instead of spinning on a shift that cannot happen" 2 \
    "needs a commit-ish" \
    'true' \
    "$R --attribute"

run_arms run-selftests.test.sh
