# TOOL-aWokenSentinel-24 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-24

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite. The pass verified with the direct checks the spec's section 7 names for it: the helper run
from a sourced copy of `tools/unattended/resume-tick.test.sh`'s prologue (lines 1 to 194 with the
`HERE=` line pinned at the kit dir, assembled under the session scratchpad as `r24/prologue.sh`,
scratch under `r24/tmp` and the fixture repo under `%TEMP%/rt24`) over the tick at the tip and over
two staged copies made by one `sed` each; the tip copy run over a fresh fixture through the
prologue's own `run_tick_over`; the greps of AC3 over the working tree and over `git show` of the
file at `c8aaeb90`, the commit whose subject carries `TOOL-aWokenSentinel-18`; and the U13 and U18
arm blocks run ALONE from the same prologue for the floor's derivation. Those stand in for the
`unattended kit gate`, `lexicon naming predicates`, `memory hygiene`, `spec tokens` and
`install-prefix` legs, which run once at the close. One spec fold was owed and taken as rev-2
before the code: the suite's assertion helper is `check_same`, not `same`, and each arm's own
calls-count line is the helper's first assertion spelled twice, so the arms give it up.

**Evidences:** TOOL-aWokenSentinel-24
- AC1 — `build_tick_without_conf_block` over the tick at the tip printed three `ok` lines (`BLOCK copy keeps both read_bound_key calls`, `BLOCK copy holds no CONF= line`, `BLOCK copy holds no source line`) and `grep -c '^read_bound_key '` over the copy printed `2`; over a tick copy whose `. "$CONF"` line was re-spelled `source "$CONF"` (the copy holding 1 `source` line and 0 dot-source lines) the calls `check_same` printed `FAIL BLOCK copy keeps both read_bound_key calls: expected [2], got [0]` with the other two `ok`; over a tick copy with a third `read_bound_key` line inserted above `CONF=` (3 calls in the copy) it printed `FAIL BLOCK copy keeps both read_bound_key calls: expected [2], got [3]`. OBSERVED, probe log `r24/probe.log`; the legs are observed at --close.
- AC2 — the tip copy the helper made, with the lib and the driver beside it, run as `bash <out> --repo <fixture>` over a fresh fixture through `run_tick_over` printed `rc=2`, `read_bound_key was called with CONF unset` counted `1` on stderr, `declares no` lines `0`, launchers under the sidecar `0`. OBSERVED; the legs are observed at --close.
- AC3 — `grep -c 'build_tick_without_conf_block' resume-tick.test.sh` printed `4` at the tip (the header comment, the definition, spec 13's NOTE arm and spec 18's refusal arm) and `grep -cE "sed '/\^CONF=/" resume-tick.test.sh` printed `1`; over `git show c8aaeb90:tools/unattended/resume-tick.test.sh`, the tip of unit 18's pass, the first printed `0` and the second `2`; `git ls-tree 830c46e8 -- tools/unattended/resume-tick.test.sh` printed no row, so the file does not exist there and the pre-unit-18 reading is taken at `TOOL-aWokenSentinel-18`'s commit as the criterion says. OBSERVED; the legs are observed at --close.
- checkers — `bash -n tools/unattended/resume-tick.test.sh` exited 0 and the file carries no CR byte (`grep -c $'\r'` printed `0`); `python3 tools/lexicon/lexicon.py --suggest build_tick_without_conf_block --as sh.function` printed `OK`. The U13 block run alone counted `pass=29 fail=0` and the U18 block `pass=12 fail=0` (41 `ok` lines, log `r24/blocks.log`), so the suite's executed count moves 104 to 108 and `FLOOR_ASSERTIONS` 94 to 97, which the whole suite observes at the close and this pass did not. OBSERVED; the legs are observed at --close.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, lexicon leg, install-prefix leg or `*.test.sh` suite ran
inside this pass; every one is `--close`'s and each row above says so. The whole-suite reading of
the raised floor is the close's, as is the executed count of the eight arm blocks this pass did not
run. The tick was not touched, so the anchors the helper reads are unit 13's as committed. The
build README's authored roster row for this unit moved `PLANNED` to `CLOSED` beside the spec
header; sibling rows were not touched. `memory/LIVE.md` and `memory/ledger/2026-09.md` were not
declared: `--dispatch` refused `memory/LIVE.md` as a path unit 16's still-open row holds, and no
unit pass of this build has moved either file, so the declaration was retried without them.
