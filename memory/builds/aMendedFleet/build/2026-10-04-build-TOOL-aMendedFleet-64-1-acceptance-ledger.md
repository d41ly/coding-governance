# TOOL-aMendedFleet-64 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-64

**Evidences:** TOOL-aMendedFleet-64
- AC1 — `python tools/govkit/govkit.py selfcheck --fix` — in a `git clone --local` of the unit's tip under `%TEMP%`/af64, with this unit's `govkit.py` committed in it: plain `selfcheck` exit 0 and `bash tools/check-kit-versions.sh` clean first; the `KIT_UNATTENDED_VERSION=` number alone set to `9.99` made the version gate exit 1 naming `check-unattended.sh`, `check-pass-order.sh` and `check-brief-recorded.sh`; `selfcheck --fix` then rewrote 24 carriers, exited 0, the version gate read `clean — 16 declared carrier(s)` and exit 0, and `git grep -l` for `gov:kit unattended@1.61` over `tools/` excluding `*.test.sh` printed nothing. Staged break: with the same-line clause replaced by `num = None` the fix rewrote 21 and the version gate exited 1 with three `KIT_UNATTENDED_VERSION != 9.99` lines
- AC2 — `tools/workflows/drift-audit-code.js` — the reset clone's `KIT_DRIFT_AUDIT_VERSION` set to 1.23 and `selfcheck --fix` run: `grep -n "version: '"` printed `3:  version: '1.23',` and `bash tools/check-kit-versions.sh` exited 0. Staged break: the carrier pattern list cut to the entry's own pattern left line 3 at `1.22` and the version gate at exit 1
- AC3 — `tools/workflows/tier2-review.js` — the reset clone's `version: '` number in `tools/workflows/tier2-review.template.js` set to 1.29 and `selfcheck --fix` run: line 3 of the rendered file carried 1.29 in the `version:` field, the `tier2-review@` alias and the `review-harness@` marker, the template's alias moved too (rev-3), and `git diff --quiet` over the four other harnesses exited 0. Staged break: the ownership clause loosened to "no other registry marker" exited that diff 1, with `unattended-unit.js` and `unattended-build.template.js` among four other harness files rewritten
- AC4 — `git status --porcelain` — a second `selfcheck --fix` in the AC1 clone printed `govkit: fix total 0 carrier(s) rewritten` and its porcelain output was byte-equal (`cmp`) to the first run's; `check-pass-order.sh` converted with `unix2dos` before the first run kept 549 CR bytes over 549 lines after it, and `git diff --stat` showed one changed line in it. Staged break: reading without `newline=""` left that file with 0 CR bytes
- AC5 — `python tools/govkit/govkit.py selfcheck` — after AC1's edit and before any fix it exited 1 with 21 check 5c lines naming `gov:kit unattended@1.61` against 9.99, and `git status --porcelain` listed only `tools/unattended/unattended.sh`. Staged break: `main` passing `fix=True` made the plain verb exit 0 and dirty 21 files
- AC6 — `govkit: fix` — the AC1 run printed one `govkit: fix <path> · unattended 1.61 -> 9.99` line per rewritten carrier, then `govkit: fix unattended moved · next: bash tools/unattended/adopt-unattended.sh`; `python tools/govkit/govkit.py selfcheck --bogus` exited 2 with `selfcheck takes no arguments except --write and --fix`
- AC7 — `USAGE` — `grep -n "selfcheck \[--write\] \[--fix\]" tools/govkit/govkit.py` hit the `USAGE` text's first verb line

## The suite arm

S7's arm, `check_fix_carriers` in `tools/govkit/selftest.py`, ran only as a slice — the module
imported and that one function called — in the worktree (9 of 9 ok) and in the clone with the
same-line clause staged out (3 FAIL, the first being the same-line copy). The govkit selftest, the
refusal join, `gen_map.py --check` and the lexicon, line-length, kit-version and kit-epoch legs are
owed at the close.
