# TOOL-aWokenSentinel-17 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-17

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite. The pass verified with the direct checks the spec's section 6 names: the new
`TOOL-aWokenSentinel-17` block of `tools/unattended/unattended.test.sh` run ALONE, together with the
extraction block it sits beside, over the suite's sourced prologue from a runner assembled under the
session scratchpad with `HERE` pinned at the kit under test and the fixture's `mktemp -d` rooted at
`%TEMP%/us17`; each staged break as a variant of that runner — the helper reduced to the raw `sed`,
and `SCRIPT` pointed for the one `check_status_one_line` invocation at a driver copy with the lib
beside it, made in binary mode by a scratchpad script; the greps of AC3; and `lexicon.py --suggest`
for the two names, `lexicon.py --check`, `check-install-prefix.sh` and `check-spec-tokens.py` each
run ONCE as the checker, never as the bar. Those stand in for the `unattended kit gate`, `lexicon
naming predicates`, `memory hygiene`, `spec tokens` and `install-prefix (shipped surface)` legs,
which run once at the close. The spec took a rev-3 fold at the pass: its section 4 said the `next`
value is a bare unit id, and the driver prints the roster row's label `<id> — <title>`; the cut holds
because that joiner is an em dash, and no design moved.

**Evidences:** TOOL-aWokenSentinel-17
- AC1 — the block alone over the kit under test, fixture `reset_tree; --preflight tRun; --park tRun --item x --reason y`: `run --status tRun` printed `unattended: tRun · phase RUNNING · witness <sha> · next ARCH-tRun-1 — the unit · parked 1`, and `extract_next "$s17"` printed `ARCH-tRun-1 — the unit`, byte-equal to the awk control `want_unit`. RED against the runner variant whose `extract_next` body is the raw `sed 's/.*· next //'`: `FAIL AC1 extract_next cuts the next field under a parked suffix: expected [ARCH-tRun-1 — the unit], got [ARCH-tRun-1 — the unit · parked 1]`, and the AC2 read-back row red the same way; the suffix-free reader at the extraction block stayed green on the raw sed, which is H2's precondition made visible. OBSERVED; the suite whole is observed at --close.
- AC2 — `check_status_one_line tRun` on the same fixture, called in the main shell with stdout to `$TMP/s17.line`: the `same` passed with `1` and the file held the status line, which `extract_next` cut to `ARCH-tRun-1 — the unit`. RED against a driver copy with `  printf 'x\n'` inserted after the two-line status `printf` (`drv2/`, `lib-unattended.sh` copied beside it): `FAIL --status tRun is one stdout line: expected [1], got [2]`. RED against a copy with the status `printf` deleted (`drv0/`, lib beside it): `FAIL --status tRun is one stdout line: expected [1], got [0]` and the read-back row `expected [ARCH-tRun-1 — the unit], got []`; the copy's shape was asserted by the staging script (`status-printf count: 1 / extra printf: 1` and `0 / 0`), and neither run printed the `kit library is missing` refusal. OBSERVED.
- AC3 — `grep -c 'extract_next' tools/unattended/unattended.test.sh` printed `5` at the tip (definition, the `:1882` reader, the AC1 arm, the AC2 read-back, one comment) and `0` over `git show 12513c25:tools/unattended/unattended.test.sh`; `diff` of the `^want_unit=` line between that blob and the tip printed nothing. OBSERVED.
- AC4 — after `mutate .unattended.conf '/^GATE_BOUND=/d'` the merged `run --status tRun` carried `declares no GATE_BOUND` on its first line (`unattended: NOTE - this project declares no GATE_BOUND, so a declared command is bounded at the kit default of 3600s. …`) and `check_status_one_line tRun` still read `1`; the block's green run is `n=30 st=0` with this arm in it. OBSERVED; a permanent arm, not a one-time probe.
- floor — the block executed 7 assertions (`n-before=23`, `n=30`) over the sourced prologue and the extraction block. `FLOOR_ASSERTIONS` 910 → 917 and `FLOOR_SHARD_2` 714 → 721, region two, derivation in each pin's own comment. The main loop's first green at VERIFYING confirms the executed count; observed at --close.
- checkers — `python tools/lexicon/lexicon.py --suggest extract_next --as sh.function` and `… check_status_one_line …` each printed `OK`; `lexicon.py --check` printed `lexicon OK — 2162 tracked file(s)`; `bash tools/check-install-prefix.sh` printed `install-prefix: clean — 276 shipped files, 11 declared waiver(s), 25 marked fixture line(s), no undeclared root-install spelling` and `carried-prefix clean — 139 recorded file(s), 41 hand-justified, none rising`; `python tools/check-spec-tokens.py` exited 0 with this spec flipped to SPECCED for the run and back, `525 token(s) examined in 13 live spec(s)` and no line naming this unit; `bash -n` over the suite exited 0; `git diff | cat -A` showed no `^M`. OBSERVED; the legs are observed at --close.
