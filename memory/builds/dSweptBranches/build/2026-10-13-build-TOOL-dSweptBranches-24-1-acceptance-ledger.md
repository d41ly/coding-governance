# Acceptance ledger — TOOL-dSweptBranches-24

**Serves:** journal TOOL-dSweptBranches-24

Built on `b7be73e4`, inline, promoted at the follow-up's closing review. The stubbed arm was written
first and observed red against unit 21's reaper; then the backstop's gone disjunct was staged out on
a copy, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-24
- AC1 — `test_backstop_outcomes_are_each_classified` — red against unit 21's `render_kill` (no `backstopped` count, and only the MSYS message on a doubly refused member); green with the fix, the killed line reading `backstopped 3` and the error carrying both messages
- AC2 — `test_backstop_outcomes_are_each_classified` — with the gone disjunct staged out of `run_kill`, the not-found member read as an error (`[2, 3]` against `[3]`); restored, green: landed in neither list, gone in `already_gone`, denied in `errors`. `test_msys_signal_is_backstopped_by_winpid` now also asserts `backstopped`
- AC3 — `test_live_tree_dies_completely` — the spawn line read `whole` after 0.9 s on a normal run, and `NOT whole (bound -1s)` with the bound forced to -1 and the grandchild hidden from the census; the whole suite passed 74 of 74
- AC4 — `grep -n "erratum" memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-21.md` — finds the line recording AC1 as observed by hand

## Rev-2, from the close's bar

The bar redded three legs on this build's own lines. `lexicon naming predicates` and `lexicon
wiring` read 1070 offenders over the pin of 1068: the two nested `stub_run` stubs, now `run_stub`;
`lexicon.py` exits 0. `harness arms` read unit 23's two `check_old_render || exit 1` sites unpinned;
both occurrences are pinned, and `check-arms.py --check` exits 0. `memory hygiene` check 12 read three
consumes-from edges with no hands-off back; specs 5, 19 and 21 now declare them.

## Owed at the close

The `process-monitor census selftest` leg runs in the close's bar.
