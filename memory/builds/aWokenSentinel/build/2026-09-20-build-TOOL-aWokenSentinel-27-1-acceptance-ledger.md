# TOOL-aWokenSentinel-27 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-27

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite. The pass verified with the direct checks the spec's section 7 names for it: the three
meta-gate checkers run as plain commands, each once at the tip of unit 21's pass (`98c3d290`, the
commit whose subject carries `TOOL-aWokenSentinel-21`, checked out detached under `%TEMP%/ws27`),
once at this unit's base (`b7a1f062`, the working tree before any edit) and once at this unit's
tip (the working tree with the three enrolments in place), with their output redirected to files
under the session scratchpad and grepped there, never read through `tail`; and the greps of AC1,
AC2 and AC3 over the working tree at both ends. Those stand in for the `testsuite counts (every
bar self-test prints one)`, `codebase-map coverage + freshness` and `govkit selfcheck` legs, which
run the same checkers once at the close, and for `every held leg is budgeted, every budget row
resolves`, `memory hygiene` and `spec tokens`, which nothing here moves. No spec fold was owed:
the design built as written at rev-1, and the one prose choice the spec left open — where the
dossier's sentence sits, since the dossier has no paragraph headed as a suites paragraph — was
taken as the end of the paragraph naming the harness this suite exercises.

**Evidences:** TOOL-aWokenSentinel-27
- AC1 — `bash tools/check-testsuite-counts.sh` at `98c3d290` exited 1 and printed one line, `TESTSUITE-COUNTS FAILED — a self-test pins a floor but does not print the agreed count line, or never compares the two, so nothing reads the pin: tools/workflows/unattended-build.test.sh wants echo "PASS ($n assertions)" and a comparison against it`; at the base `b7a1f062` the same line, exit 1; at the tip exit 0 with no output naming `unattended-build`. `grep -cE '^\[ "\$st" = 0 \] && echo "PASS \(\$n assertions\)"$' tools/workflows/unattended-build.test.sh` printed `1` at the tip and `0` at the base; `grep -n` placed the line at 1296 and `exit $st` at 1297, so the line sits above the terminal exit and the after-exit self-read's range is unchanged. The two tail lines evaluated alone by `bash -c` printed `PASS (293 assertions)` under `st=0` and nothing under `st=1`, the list's status not stopping the line after it. `bash -n` exited 0 and the file carries no CR byte. OBSERVED; the leg is observed at --close.
- AC2 — `python3 tools/codebase-map/test_codebase_map.py` at `98c3d290` exited 1 and printed `UNCLAIMED (new key? claim it in a feature dossier, or FOUNDATION.md for shared substrate; baseline.toml is reserved for the initial backfill): {'gate-legs': ['unattended-build self-test']}`; at the base the same; at the tip exit 0 with six `ok` rows and no `UNCLAIMED` or `FAIL` token. `python tools/codebase-map/gen_map.py --check` at the tip exited 0. `grep -c '"unattended-build self-test"' memory/map/features/review-harnesses.md` printed `1` at the tip and `0` at the base. `gen_map.py --write` reported writing all three generated files; `git diff --numstat` shows `generated/MAP.md` moved by one row, `UNCLAIMED` to `review-harnesses`, and `inventories.json` and `symbols.json` byte-identical to the base, because the key was already in the inventory from unit 21's leg row and no symbol moved. The claim sits in the dossier whose `[paths].globs` is `tools/workflows/*`, the owner of the suite. OBSERVED; the leg is observed at --close.
- AC3 — `python tools/govkit/govkit.py selfcheck` at `98c3d290` exited 1 and printed `govkit: gate leg 'unattended-build self-test' has no row in tools/govkit/subject-pins.tsv — a NEW leg reds until its subject is on the record, because an unpinned leg is one whose side of the bar nobody chose. Regenerate with `python tools/govkit/govkit.py selfcheck --write`` and `govkit: 1 problem(s)`; at the base the same; at the tip exit 0 with `0 unclaimed` and no `unattended-build` token. The row was written by `python tools/govkit/govkit.py selfcheck --write`, never by hand. `grep -c '^unattended-build self-test<TAB>kit<TAB>selftests$' tools/govkit/subject-pins.tsv` printed `1` at the tip and `0` at the base. `git diff --numstat 98c3d290 -- tools/govkit/subject-pins.tsv` printed `1 0`, one insertion and no deletion, so no other row moved. OBSERVED; the leg is observed at --close.

## What this ledger does not evidence

No gate leg, hygiene leg, spec-token leg, lexicon leg or `*.test.sh` suite ran inside this pass;
every one is `--close`'s and each row above says so. The `PASS` line was never seen to print from
a suite run: `compliant()` grades the emitting line's presence and the pass observed that presence
and the line's behaviour in isolation, and the whole-suite reading — the count it prints beside
`FLOOR_ASSERTIONS=293` — is the close's under `run-selftests.sh --kit tools/workflows`. No
identifier was minted, so no lexicon query was owed. The `--dispatch` verb refused the first
declaration for naming `memory/LIVE.md`, a generated index a sibling pass already holds a row on;
the write set was re-declared without the two generated indexes, the way units 25 and 26
declared theirs. The build README's authored roster row for this unit moved `PLANNED` to
`CLOSED` beside the spec header; this pass touched no sibling's row.
