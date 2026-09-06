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

SELFTEST_FLOOR=13

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

  git add -A >/dev/null 2>&1 || return 2
}
build_fixture build_repo || exit 2

R='bash tools/run-gates/run-selftests.sh'
B='tools/run-gates/selftest-budgets.txt'

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
    "printf '# only a comment\n' > $B && printf '%s\n' '[]' > tools/gate-legs.json && git add -A" \
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

run_arms run-selftests.test.sh
