# Observations — aClearedLedger: each ask's accept line, each suite the units gave to the main loop, and each new arm seen red

**Serves:** journal TOOL-aClearedLedger-1 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 TOOL-aClearedLedger-11 TOOL-aClearedLedger-12 TOOL-aClearedLedger-13 TOOL-aClearedLedger-14 TOOL-aClearedLedger-15 TOOL-aClearedLedger-16

The main loop's own record, written at the close for review round 1's item H1: no unit pass runs a
suite, so each suite, leg and red-first observation the specs gave to the main loop was run here, on
a frozen clone under the node's temp directory, and is written down here rather than asserted.
Every run was one whole run of the suite's own argv; no slice was run. The raw outputs stay on node a
under the session's temp `nm16out` folder and are not tracked.

## The asks' accept lines

| Ask | Run, on a clone at | What it printed |
|---|---|---|
| TOOL-aNimbleMend-16 | the gate guard's suite, `48ee864e3` | `216 passed, 0 failed`, no line opening `FAIL parity:` (PINNED 2026-11-13) |
| TOOL-aNimbleMend-17 | the scratch guard's suite, `1b75a3b0e` | `385 passed, 0 failed`, no `S-AC2`, `S-AC3`, `S-AC5` or `S-AC8` FAIL line (PINNED 2026-11-13) |
| TOOL-aNimbleMend-18 | the spec-token suite, `7cbe4a220` | `PASS (253 assertions)`, no `arm FAIL` line naming parity (PINNED 2026-11-13) |
| TOOL-aNimbleMend-19 | the hygiene self-test, `ab84f0372` | exit 0, `PASS (731 assertions)` (PINNED 2026-11-13) |
| TOOL-aNimbleMend-20 | the policy fixtures leg, `7d58d947e` | `922 assertion(s) executed · 0 wrong` (PINNED 2026-11-13) |
| TOOL-aNimbleMend-23 | the `red-fix-join` plant, `1e516f5af` | `PASS red-fix-join — 19 cases` (PINNED 2026-11-13) |
| TOOL-aNimbleMend-25, -26 | the two lint commands, `8db6f4bef` | exit 0 and `0 red`, disposed in this build's backlog |
| TOOL-aNimbleMend-21 | five `--staged` hygiene runs, `8db6f4bef` | no `unbound variable` line; cured by TOOL-aWitnessedCrash-1, disposed in the backlog |
| TOOL-aNimbleMend-24 | the practice catalogue and the protocol's section 12 | the owner's two rulings, written by units 1 and 2 |
| TOOL-aNimbleMend-22 | two timing rounds, `1e516f5af` | parked in the backlog: the node was never quiet |

## The suites at the tip of each later unit

| Unit | Run, on a clone at | What it printed |
|---|---|---|
| TOOL-aClearedLedger-11 | gate guard, spec tokens, the spec-tokens leg | `PASS (230 assertions)`, `PASS (257 assertions)`, no `[bar]` row (PINNED 2026-11-14) |
| TOOL-aClearedLedger-12 | gate guard, `a56c07711` | `PASS (234 assertions)` (PINNED 2026-11-14) |
| TOOL-aClearedLedger-13 | gate guard, spec tokens, template size, the leg, `64673441a` | `PASS (237 assertions)`, `PASS (257 assertions)`, one red arm A25b, no `[bar]` row (PINNED 2026-11-14) |
| TOOL-aClearedLedger-14 | gate guard, spec tokens, the leg, `998b627aa` | `PASS (239 assertions)`, `PASS (257 assertions)`, no `[bar]` row (PINNED 2026-11-14) |
| TOOL-aClearedLedger-16 | gate guard, spec tokens, the leg, `5ac43b14d` | `PASS (243 assertions)`, `PASS (257 assertions)`, no `[bar]` row (PINNED 2026-11-14) |

The template size suite's arm A25b is red at the build's base as well: the suite at `8db6f4bef`
exits 1 on that arm alone. Its fixture copies the charter, which measures over the cap the arm
plants, at the base and here. It predates this build and is left for a later one.

## Each new arm, seen red

Each break was staged on its own clone of the named tip, and the suite was run whole. The green side
is the same suite unbroken at that tip, in the tables above.

| Unit | Break staged | Red line |
|---|---|---|
| 3 | the hook's bound raised above every planted ceiling | `FAIL D6 … (exit 0, want 2)` lines |
| 3 | an over-bound bare-script leg added to the manifest | `FAIL parity:` |
| 3 | the hook's word list without `fixture` | `FAIL the suite's direct-check bound and words` |
| 5 | a row at the bound admitted | `arm FAIL  direct-check: six staged rows did not derive` |
| 5 | rule 2 dropped from `check_bar` | `arm FAIL  direct-check: the staged leg's three spellings` |
| 5 | the module's word list without `fixture` | `arm FAIL  direct-check: this suite's bound and word list differ` |
| 6 | the marker-block range out of `derive_engreads` | `FAIL the override derivation read EXAMPLE_INSIDE_KEY` |
| 6 | the cache-figure fold out of `extract_hs_lines` | `FAIL the scoped runs do not partition` |
| 9 | every trailer commit counted as a fix | `FAIL missing: build-records: PASS red-fix-join` |
| 11 | arms 1 to 14, five breaks of the hook | each named arm's `FAIL D6` line, and no other arm |
| 11 | the lint's five breaks | five distinct `arm FAIL  direct-check` lines |
| 12 | the guard put back to the all-digits test | the four appended-output arms, `230 passed, 4 failed` (PINNED 2026-11-14) |
| 13 | the hook's three breaks | `FAIL D6 the leg behind python3 -m pdb`, `FAIL D6 a kept gap: a 2>&1 ahead of the flag`, `FAIL D6 a kept gap: a glued variable prefix` |
| 13 | the lint's five breaks | each break's own wrapper spellings named as no hit |
| 13 | the refusal clause removed, then put back to its old wording | `arm FAIL  A25c`, then `arm FAIL  A25d` |
| 14 | the hook put back to blob `77894998` | both quoted-operator allow arms, `237 passed, 2 failed` (PINNED 2026-11-14) |
| 14 | the drop test removed | the quoted `>` arm, `238 passed, 1 failed` (PINNED 2026-11-14) |
| 15 | the hook put back to blob `07723a18`, at `5ac43b14d` | `FAIL D6 a quoted > opening a glued target after >` and `after 2>`, `241 passed, 2 failed` (PINNED 2026-11-14) |
| 16 | the keep-as-word test weakened to `!redir || q >= 0`, at `5ac43b14d` | unit 16's two arms `FAIL D6 the leg with a quoted target glued to >` and `to 2>`, with unit 15's two, `239 passed, 4 failed` (PINNED 2026-11-14) |

## At the close

Pass legs ran after every unit's pass commit. Units 2, 4, 7, 9, 13, 14, 15 and 16 were green on the
first run; the reds of the others were each on one leg, fixed by a records or red-fix commit, and only
the red leg's own command was run again after it. The bar runs once, after this record's commit.
The review closed at round 4: its confirmed count rose over round 3's, so units 15 and 16, which
carry round 4's findings, were built from their specs and read by no fifth round.
