#!/usr/bin/env bash
# check-line-length.test.sh — the failing case for every branch the gate carries.
#
# PORTED ONTO `tools/lib/lib-selftest.sh` by TOOL-aQuenchedHarness-6, with the arm inventory
# unchanged — same labels, same staged breaks, same expected verdicts, diffed before and after by
# `bash tools/lib/extract-arms.sh`. Read that harness's header for why the shape is
# declare-then-run rather than run-as-you-go; what is worth knowing HERE is what the port removed.
#
# THE COST WAS NEVER THE GATE, IT WAS THE FIXTURE. Traced at 36 s / 432 lines
# (`memory/builds/aQuenchedHarness/build/2026-09-07-build-TOOL-aQuenchedHarness-5-candidate-test.md`),
# the outer script spawned 31 `python3` — every one of them building a line of repeated characters,
# 18 of those inside a `reset` that ran before every arm. At 773 ms a python spawn on this fleet that
# is ~24 s of the 36 s, spent on strings the shell can build with no process at all. `build_line`
# below is that, in builtins; the line files are built ONCE into the fixture; and each arm now
# copies a snapshot instead of mutating one shared directory.
#
# THE PROPERTY THAT MADE THE OLD SHAPE UNPARALLELISABLE, kept as a warning against restoring it: the
# suite reused ONE scratch repo and `reset` mutated it between arms, so two arms running at once
# landed the second's setup inside the first's subject invocation. Per-arm isolation is what buys the
# pool; the pool is not an optimisation on top of it.
#
# THE HARNESS RUNS SETUP AND THE SUBJECT SEPARATELY, and that is not a style choice. An earlier draft
# ran `sh -c 'setup; gate; cleanup'` and read the rc of the CLEANUP — so every red arm reported 0 and
# the suite would have certified a gate that never fired. Setup happens first, the subject runs
# alone, and its rc is the one compared.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "check-line-length.test: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2
. "$HERE/lib/lib-selftest.sh"

GATE="$ROOT/tools/check-line-length.sh"
[ -f "$GATE" ] || { echo "check-line-length.test: no gate at $GATE"; exit 2; }

# THE SUITE STILL DECLARES ITS OWN ARM COUNT. The floor moved into the harness so eighteen ported
# suites do not carry eighteen copies of the guard, but the NUMBER is this suite's and stays here.
SELFTEST_FLOOR=18

# build_line <char> <n> — <n> copies of <char>, in builtins. `printf -v` and parameter expansion
# cost no process; this one function is where the 31 python spawns went. It is UTF-8 safe by construction:
# the replacement is the argument, so an em dash lands as one character per space.
build_line() { local pad; printf -v pad "%${2}s" ""; printf '%s\n' "${pad// /$1}"; }

# The fixture is the state the old suite's `reset` produced — a subject the gate passes on and a
# declaration naming it — plus every line file the arms need, built once instead of per arm.
build_repo() {
  mkdir -p tools L || return 2
  git init -q . >/dev/null 2>&1 || return 2
  git config user.email t@t && git config user.name t || return 2
  cp "$GATE" tools/check-line-length.sh || return 2
  build_line x 100 > subject.md
  printf 'subject.md\t450\n' > tools/line-length-limits.txt
  build_line y 451 > L/y451
  build_line y 450 > L/y450
  build_line y 300 > L/y300
  build_line y 600 > L/y600
  build_line y 10  > L/y10
  build_line — 400 > L/em400
  printf '%s\n' '```' > L/fence
  # The interpreter dies AFTER the resolver's probe accepted it — the shape a resolver cannot catch.
  printf '#!/usr/bin/env bash\n[ "$1" = "-c" ] && exit 0\nexit 4\n' > deadpy
  chmod +x deadpy
}
build_fixture build_repo || exit 2

arm "control · a short subject passes" 0 "0 over 450" \
    'true' 'bash tools/check-line-length.sh'

# The `want` strings for red arms are each the branch's ENTIRE literal signature up to its first
# interpolation, which the harness meta-gate requires. An arm asserting a readable prefix keeps
# passing after the sentence it was written for is rewritten around it, and the branch quietly loses
# its only proof.
arm "an over-length line reds naming the line and its length" 1 "a subject carries line(s) over its limit of" \
    'cat L/y451 >> subject.md' 'bash tools/check-line-length.sh'

arm "exactly at the limit passes" 0 "0 over 450" \
    'cat L/y450 >> subject.md' 'bash tools/check-line-length.sh'

# ---------------------------------------------------------------- resolution order
arm "the DECLARATION beats the environment" 1 "limit of 200" \
    'printf "subject.md\t200\n" > tools/line-length-limits.txt; cat L/y300 >> subject.md' \
    'LINE_MAX=9999 bash tools/check-line-length.sh'

arm "an UNDECLARED subject honours the environment" 1 "resolved from the environment" \
    'cat L/y300 > other.md' 'LINE_MAX=200 bash tools/check-line-length.sh other.md'

arm "an undeclared subject with no environment falls through to 450" 0 "limit from the default" \
    'cat L/y300 > other.md' 'bash tools/check-line-length.sh other.md'

arm "a POSITIONAL beats the declaration" 1 "resolved from a positional" \
    'cat L/y300 >> subject.md' 'bash tools/check-line-length.sh subject.md 200'

# ---------------------------------------------------------------- the exemption, and its boundary
arm "a long line INSIDE a fence does not red" 0 "0 over 450" \
    '{ cat L/fence; cat L/y600; cat L/fence; } >> subject.md' 'bash tools/check-line-length.sh'

arm "a long line inside a TABLE does red" 1 "characters" \
    '{ printf "| "; cat L/y600; } >> subject.md' 'bash tools/check-line-length.sh'

# ---------------------------------------------------------------- measurement and declaration hygiene
arm "a non-ASCII line is measured in CHARACTERS, not bytes" 0 "0 over 450" \
    'cat L/em400 >> subject.md' 'bash tools/check-line-length.sh'

arm "a row naming an ABSENT path reds as stale" 1 \
    "the declaration names a subject that does not exist, so its row excuses nothing and is stale" \
    'printf "subject.md\t450\ngone.md\t450\n" > tools/line-length-limits.txt' \
    'bash tools/check-line-length.sh'

arm "a NON-NUMERIC limit is a named failure, not a shell error" 1 \
    "the declared line limit for this subject is not a number, so the comparison below would be against text: '" \
    'printf "subject.md\tlots\n" > tools/line-length-limits.txt' \
    'bash tools/check-line-length.sh'

arm "a declaration selecting NO subject is cannot-run" 2 "would grade nothing" \
    'printf "# only a comment\n" > tools/line-length-limits.txt' \
    'bash tools/check-line-length.sh'

# ---------------------------------------------------------------- certify-without-measuring
# THE FOUR ARMS BELOW ARE ONE CLASS: the gate printed `line-length OK … 0 over 0 characters` and
# exited 0 in every one of them. `over` is empty on a clean subject and empty on a crashed scanner,
# and the shell discarded the status that told them apart. Each arm asserts a NON-ZERO verdict, so a
# regression cannot pass by printing the right words.
arm "a non-numeric POSITIONAL limit is a named failure, not a certified zero" 1 \
    "the line limit is not a number, so nothing could be compared against it: '" \
    'cat L/y300 >> subject.md' 'bash tools/check-line-length.sh subject.md abc'

arm "a non-numeric LINE_MAX is a named failure, not a certified zero" 1 \
    "the line limit is not a number, so nothing could be compared against it: '" \
    'cat L/y10 > other.md' 'LINE_MAX=abc bash tools/check-line-length.sh other.md'

# A subject whose every line sits inside a fence measures ZERO lines. Empty-population is the
# vacuity this tree bans by name: the old gate printed OK over a file it graded nothing in.
arm "a subject with NO gradeable line is a dead probe, not a clean verdict" 1 \
    "the scanner reached no gradeable line in this subject, so a clean verdict would certify a measurement that never happened" \
    '{ cat L/fence; cat L/y600; cat L/fence; } > subject.md' 'bash tools/check-line-length.sh'

arm "a scanner that dies mid-run is a named failure, not a certified zero" 1 \
    "the offender scan did not run for this subject, so no line was measured and OK would be a lie" \
    'true' 'LINELEN_PY=$PWD/deadpy bash tools/check-line-length.sh'

# THE INSTALL-DAY PAIR, and the two must land on DIFFERENT verdicts. The kit withholds the
# declaration on purpose — gov's rows name gov's paths, and a row naming an absent path is a stale
# red — so ABSENT is the shape every adopter starts in, and the exit 2 it used to get there was the
# very failure the withholding was made to prevent. Measured in a scratch install before this arm
# existed. Its neighbour above is what stops this one being read as "an empty population is fine".
arm "an ABSENT declaration is NOT ADOPTED at exit 0, not a red install day" 0 \
    "NOT ADOPTED — no declaration at" \
    'rm -f tools/line-length-limits.txt' 'bash tools/check-line-length.sh'

run_arms check-line-length.test.sh
