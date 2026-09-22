#!/usr/bin/env bash
# extract-arms.test.sh — the four states `tools/lib/extract-arms.sh` can report, each armed.
#
# THE SUBJECT IS A SAFETY PROPERTY, WHICH IS WHY IT GETS ARMS AT ALL. `extract-arms.sh` is not a gate
# leg; it is the thing that decides whether a rebuilt suite still grades what it used to. A wrong
# answer from it does not red a bar, it CERTIFIES a port that lost arms — so a wrong answer is
# strictly worse than no answer, and the case for arming it is stronger than for most legs, not
# weaker.
#
# AND IT HAD A WRONG ANSWER. The extractor guarded the empty inventory and nothing else, so a suite
# printing 14 readable lines against 289 executed assertions came back as a confident 14-arm
# inventory at exit 0 — 4.8% coverage, and a port dropping the other 275 would have diffed empty.
# `tools/memory-tree/check-memory-hygiene.test.sh` is that suite; it costs 918 s to run, so the arm
# below reproduces the SHAPE in a three-line fixture rather than paying for the instance.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "extract-arms.test: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2
. "$ROOT/tools/lib/lib-selftest.sh"

TOOL="$ROOT/tools/lib/extract-arms.sh"
[ -f "$TOOL" ] || { echo "extract-arms.test: no extractor at $TOOL"; exit 2; }

SELFTEST_FLOOR=9

# Each fixture is a SUITE the extractor will run. They are three lines each because the extractor
# reads output and nothing else — the cheapest possible subject for a tool whose input is a suite.
build_fixtures() {
  cp "$TOOL" extract-arms.sh || return 2

  # the good shape: one readable line per assertion, and a total that agrees
  printf '#!/usr/bin/env bash\necho "ok   beta"\necho "ok   alpha"\necho "PASS (2 assertions)"\n' > good.sh
  # the harness spelling, with its width clause, and a label carrying the structural glyphs
  printf '#!/usr/bin/env bash\necho "ok    control \xc2\xb7 a short subject passes"\necho "ok    the second"\necho "----"\necho "PASS (2 arms, width 4)"\n' > harness.sh
  # a suite whose own word precedes the verdict, which is the fifth idiom the survey found
  printf '#!/usr/bin/env bash\necho "arm ok    prefixed"\necho "arm ok    also prefixed"\necho "PASS (2 assertions)"\n' > prefixed.sh
  # timings beside the verdict, which would otherwise make the inventory move every run
  printf '#!/usr/bin/env bash\necho "ok   timed one   1.4s"\necho "ok   timed two   12s"\necho "PASS (2 assertions)"\n' > timed.sh
  # NO per-arm line at all
  printf '#!/usr/bin/env bash\necho "everything is fine"\necho "PASS (2 assertions)"\n' > silent.sh
  # readable lines, but far fewer than the suite says it ran: the 4.8% shape
  printf '#!/usr/bin/env bash\necho "ok   one"\necho "ok   two"\necho "PASS (10 assertions)"\n' > partial.sh
  # readable lines, no total of any kind: coverage cannot be checked either way
  printf '#!/usr/bin/env bash\necho "ok   one"\necho "ok   two"\necho done\n' > nototal.sh
  # RED, but still a comparable population — a failing suite has an inventory too
  printf '#!/usr/bin/env bash\necho "ok    kept"\necho "FAIL  lost \xe2\x80\x94 expected rc 0"\necho "FAIL (1 of 2 arms, width 1)"\nexit 1\n' > red.sh
}
build_fixture build_fixtures || exit 2

X='bash extract-arms.sh'

arm "control · a suite whose lines and total agree yields its inventory" 0 "2 arm(s)" \
    'true' "$X good.sh --out inv.txt"

arm "and the inventory is SORTED, so two runs of the same suite compare equal" 0 "alpha" \
    'true' "$X good.sh | head -1"

arm "the harness spelling is read, width clause and all" 0 "its own total 2" \
    'true' "$X harness.sh --out inv.txt"

arm "a suite's own word before the verdict is absorbed, not counted as the label" 0 "prefixed" \
    'true' "$X prefixed.sh | head -1"

arm "a timing beside the verdict is stripped, or the inventory moves every run" 0 "timed one" \
    'true' "$X timed.sh"

# The harness's OWN summary satisfies the arm grammar -- `FAIL (1 of 2 arms, width 1)` -- so
# before the exclusion landed this arm reported THREE, and a red suite's inventory differed from
# the same suite green. An inventory that moves with the verdict compares nothing.
arm "a RED suite has a comparable inventory, its summary not counted as an arm" 0 "2 arm(s)" \
    'true' "$X red.sh --out inv.txt"

# ---------------------------------------------------------------- the three refusals
arm "a suite with NO per-arm line is UNEXTRACTABLE, never an empty inventory" 3 \
    "printed no per-arm verdict line" \
    'true' "$X silent.sh"

arm "a suite printing FEWER readable lines than it ran is PARTIAL, not a confident fraction" 5 \
    "reports 10 executed assertion(s) and printed 2 line(s)" \
    'true' "$X partial.sh"

arm "a suite reporting no total at all is UNVERIFIABLE, because coverage cannot be checked" 4 \
    "but reports no executed total" \
    'true' "$X nototal.sh"

run_arms extract-arms.test.sh
