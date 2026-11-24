# KICK-dKeptSession-43 — acceptance ledger

**Serves:** journal KICK-dKeptSession-43

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `76369ef3c`.
AC1 to AC4 ran through the unit's own fixture CLI, `bash actions-free.fixture.sh --plant <case>` in the
hooks kit, one plant at a time, each building its own scratch repository under a short temp
directory; neither hooks suite was run. The three new `check_free_line` rows of the scratch-guard
suite and the agent-cap suite's new rule 9 row were probed alone over that fixture output, copied
into a scratch script, never by running the suite: all four held, and the same four patterns over
lines shaped as `KICK-dKeptSession-8`'s arm prints them, a throw naming the skipped line as neither
an instance key nor `none`, each red (DERIVED, that probe). AC5 and AC6 ran as the spec's own
commands. The unit adds no function, so `python tools/codebase-map/gen_map.py --check` exits 0 and
the symbol map does not move; `python tools/lexicon/lexicon.py` exits 1 on verb offenders over its
pin at the base, every one of them in a file this unit does not touch.

The spec's text predates `KICK-dKeptSession-8`'s landing at `2cbf82b43`; what landed reads as the
spec's sections 1, 2 and 4 cite it: `tools/hooks/scratch-guard.js#readItemPointer` with one
`unborn)` pattern, `tools/hooks/scratch-guard.js#checkFreeAction` and its unarmed answers,
`tools/hooks/scratch-guard.js#runFreeAction`'s refusal, rule 9 in `tools/hooks/agent-cap.js#main`
printing `agent-cap: rule 9 unarmed — <why>`, the fixture's twelve plants and its
`write_fixture_card`, and the suite's `FLOOR_ASSERTIONS` pin of 430 (PINNED at base `76369ef3c`). No
suite arm greps unit 8's malformed message, so S3's new message strands none. Section 4's budget
table carries unit 8's estimates, `r` 208 s and 393 s (PINNED, that spec's section 4); the rows
landed at `r` 197.0 s and 389.9 s (PINNED, the budgets file at base `76369ef3c`), so each row is
re-priced from its landed `r` by the table's own rule, the row's value or 1.5 `r` rounded up,
whichever is higher.

Owed to the close: every leg the spec's section 7 names, the scratch-guard and agent-cap suites whole,
and the two `New arm:` lines' RED-first observations: the scratch-guard suite's three
`KICK-dKeptSession-43` rows staged against unit 8's arm, which parses the skipped line as malformed
and refuses it, and the agent-cap suite's `item-skipped` row staged against the same arm, which
throws.

**Evidences:** KICK-dKeptSession-43
- AC1 — `item-skipped` under the stub's `read-only-probes` wrote `item — skipped: no loop kit position.py resolves in this tree · at <HEAD sha8>`: the Bash `echo x > f` to `scratch-guard.js` exited 0 printing `scratch-guard: actions.free unarmed — item pointer skipped: no loop kit position.py resolves in this tree` (DERIVED, that run).
- AC2 — the same plant's Bash `git commit -m x` exited 0 with the same line (DERIVED, that run).
- AC3 — `item-malformed` wrote `item — ??? · at <HEAD sha8>`: the Bash `echo x > f` exited 2 printing `BLOCKED by scratch-guard: the actions.free arm threw (item pointer malformed: item — ??? · at <HEAD sha8>) and fails closed on a Bash.` (DERIVED, that run).
- AC4 — the `item-skipped` plant's `Agent` payload to `agent-cap.js` exited 0 printing `agent-cap: rule 9 unarmed — item pointer skipped: no loop kit position.py resolves in this tree` (DERIVED, that run).
- AC5 — the spec's `node -e` over `readItemPointer` printed `{"skipped":"no boundary was read","at":"1a2b3c4d"} {"skipped":"a · at b","at":"unborn"} {"malformed":"item — skipped: · at 1a2b3c4d","at":"1a2b3c4d"}`, and `grep -c 'unborn)' scratch-guard.js` printed 1 (DERIVED, that probe). A second probe read an instance key, `none` and `x y` as unit 8's AC10 does, and a whitespace-only why as malformed (DERIVED, that probe).
- AC6 — `grep -c 'item pointer skipped' README.md` in the hooks kit printed 2 (DERIVED, that probe).
- S6 — `item-skipped` ran in 0.91 s and `item-malformed` in 0.46 s by direct CLI (DERIVED, that run). `scratch-guard self-test` reads `r` 198.4 s and 298, over its 296; `agent-cap self-test` reads `r` 390.8 s, 1.5 `r` is 587, and its 590 stands; neither reaches its leg's ceiling of 490 or 1800 (PINNED, the leg manifest at base `76369ef3c`). `FLOOR_ASSERTIONS` reads 433 (DERIVED, 430 plus the 3 rows).
- seen-red — `agent-cap self-test` — red `45016a2c4` — green `45016a2c4` — `item-skipped`: a skipped item pointer parsed as malformed, as unit 8's arm
- seen-red — `scratch-guard self-test` — red `f6a0d7aaf` — green `f6a0d7aaf` — `item-skipped`: a skipped item pointer parsed as malformed, as unit 8's arm
