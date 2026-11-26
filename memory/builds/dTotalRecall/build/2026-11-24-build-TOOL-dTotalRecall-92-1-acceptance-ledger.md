# TOOL-dTotalRecall-92 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-92
**Caused-by:** TOOL-dTotalRecall-92

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-3 over
base `2988984364d575b97c63c56bcbce3c2c4099acb6` on node a, 2026-11-24. §7's legs are the close's, and §7 declares no new
arm. The probes are §4's fences, the first bash fence of unit 81 §4, the two probe fences of units 90 and 93 §4, the
script of unit 79 §4 with §4's block spliced in, the fence probe of unit 88 §4 and the strings of units 82 to 84 §4,
each extracted from the spec to a file under the scratch directory and run from the repository root by its path.

Built: S10's record, `2026-11-24-build-TOOL-dTotalRecall-87-deviation-1014`, and S23's docstring paragraph. Every other
item holds as read, so no other record is owed and none is written; S11 restores nothing, S12 moves nothing and S13
clears nothing.

S1: the read beside unit 81's AC2 line, whose ledger is `2026-11-22-build-TOOL-dTotalRecall-81-1-acceptance-ledger.md`
(DERIVED 2026-11-24, `pass_of 67` at the base and that line):

```text
pass_of 67        56390bab8cce52668b940893b8378621df78e4b7
unit 81 driver    56390bab8cce52668b940893b8378621df78e4b7
```

The main loop's read, copied from "The p79 read, as run" of `2026-11-24-prompt-TOOL-dTotalRecall-92-build-brief.md`
(DERIVED 2026-11-24, that run):

```text
p79 at b226b424244234634176b2011cb5daf87357bcb3
p79 rc=0
p79 cost 16 s
```

S4 and S17, the span derivation as corrected, over the block of unit 78's AC1 answer (DERIVED 2026-11-24, these runs).
Each run that exits 0 first prints `unresolved` for units 8, 37, 14, 15 and 26:

| Input | Printed (DERIVED 2026-11-24) |
|---|---|
| the block and `$LIVE` | `span 22 22 checks 9 closed-by 3`, `span live live checks 9 closed-by OPEN`, `spans 2`, exit 0 |
| the block alone | the first of those, `spans 1`, exit 0; unit 79's own script prints the same |
| its last unit, 84, made red, and `$LIVE` | `span 84 84 checks none-printed closed-by sep` before `live` |
| the same with no `sep` line | `span 84 live checks 9 closed-by OPEN`, the folded span |
| unit 69's verdict line deleted | `red population 72 read 71`, exit 1 |
| that line spelled `rc = 0` | `red unplaced` with the line, then that population red, exit 1 |

Unit 79's AC1 answer shows `live` in a span of its own, so it folded nothing and no record of unit 79 is owed.

S10, the two resolvers over one conf value, run again in a scratch tree (DERIVED 2026-11-24, that probe); the six rows of
§4 "The precedent" hold:

| Value | `runlog_lib` | `tree_lib` |
|---|---|---|
| `docs/memory/` | `docs/memory` | `docs/memory` |
| `/memory` | `memory` | refused |
| `docs\memory` | refused | `docs/memory` |
| `docs/me:mory` | refused | as spelled |
| `./docs//memory` | as spelled | `docs/memory` |
| a root with outer spaces | as spelled | stripped |
| `.` | `.` | refused |

S14, the `quoted` lines of the tip scan name
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-2-2-acceptance-ledger.md`,
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-71-1-acceptance-ledger.md` and
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-82-1-acceptance-ledger.md`, and no other. The
anchored read printed no path, and its liveness 151 (DERIVED 2026-11-24, both reads at the tip).

S16, the mechanism: the driver dispatches strictly in sequence inside one order value
(`tools/workflows/unattended-build.js@67ffd1289:78`), by the comparator at
`tools/workflows/unattended-build.js@67ffd1289:692`, so the door's next free `<n>` is read after the previous pass's
commit.

S23, handed to the close's left-shift step: the four definitions of the name, in `tools/loop/loop_lib.py`,
`tools/memory-recall/selftest.py`, `tools/memory-tree/tree_lib.py` and `tools/runlog/runlog_lib.py`.

**Evidences:** TOOL-dTotalRecall-92
- AC1 — `pass_of 67` — printed `56390bab8cce52668b940893b8378621df78e4b7`, which `56390bab8cce` abbreviates, exit 0; unit 81's AC2 answer records `driver 56390bab8cce52668b940893b8378621df78e4b7`, the same sha, the two in the first block above (DERIVED 2026-11-24, that run).
- AC2 — `grep -c "pass_of 999" 2026-10-26-spec-TOOL-dTotalRecall-81.md` — printed 4, the `git grep` for `red 999 no pass commit` one line, unit 81's AC1 answer, and `has_deviation memory/builds/dTotalRecall/build 81 'audit-77 id 11 '` 0. With no token it printed 1 for unit 59, and with `spec changed at` 1 for unit 70, so the zero is no unmovable probe (DERIVED 2026-11-24, these commands).
- AC3 — `pass_of 999` — printed `red 999 no pass commit` and returned 1 at the base (DERIVED 2026-11-24, that run).
- AC4 — `span live live checks 9 closed-by OPEN` — is the last span line with `$LIVE` appended, at `spans 2`, one more than the `spans 1` without it. `has_deviation memory/builds/dTotalRecall/build 79 'audit-77 id 3 '` printed 0, unit 79's answer having folded nothing (DERIVED 2026-11-24, these runs).
- AC5 — `p79 rc=` — the brief hands `p79 at b226b424244234634176b2011cb5daf87357bcb3` and `p79 rc=0`, with no failure line beneath, and `pass_of 79` printed that sha. Unit 79's line beside it is `base79 rc=0`, read at `07760b416cb73f8040eda7d29f6076d66fbce473`. The status is zero, and `has_deviation memory/builds/dTotalRecall/build 79 'audit-77 id 5 '` printed 0 (DERIVED 2026-11-24, the main loop's read and these commands).
- AC6 — `python record_causes.py --fixture --plant kept-home-trailing-root` — exited 0 with no `record causes: RED ` line and no compare line; `read at docs/memory/project/census-kept-paths.txt` and `registered at docs/memory/project/census-kept-paths.txt`, one home. Unit 87's AC2 answer records the same two lines green (DERIVED 2026-11-24, that run).
- AC7 — `s1 s1-999 999 '' 57 "$SCRATCH/s82.txt"` — printed `s1-999 red 999 no pass commit`. None of units 82, 83 and 84 recorded an empty S1: their AC1 lines hold `56390bab8cce52668b940893b8378621df78e4b7` with 1, `206422580b7363ab9582e37ffe7de7c25773a721` with 1 and `254057fa6d5bbc19cd48329737487c88a10b0085` with 0, so each recorded a line and no cause is owed (DERIVED 2026-11-24, that run and the three ledgers).
- AC8 — `malformed` — led no line of the tip scan, which exited 0 over 150 records at this pass's base and over 151 with its own (DERIVED 2026-11-24, both scans). The scratch folder of AC22 printed one for a record with its Risk line taken out.
- AC9 — `p79 cost` — the brief hands `p79 cost 16 s`, one add, one read and one remove. §4's two counts over unit 78's block each printed 72, so each population unit leads one verdict line there and no second sweep is owed (DERIVED 2026-11-24, the main loop's read and these counts).
- AC10 — `has_deviation memory/builds/dTotalRecall/build 87 'audit-77 id 16 '` — printed 0 at the base and 1 after the pass; the After of `2026-11-24-build-TOOL-dTotalRecall-87-deviation-1014` names `runlog_lib`, `design_lib` and `./docs//memory` (DERIVED 2026-11-24, both runs).
- AC11 — `--diff-filter=A` — its form of the listing printed 150 paths at the base and the deleted form none, with rename detection off none either, so nothing is restored; the tip scan printed no `dup` line (DERIVED 2026-11-24, these commands).
- AC12 — `last-body-change` — is in the fourth of seven bullets; `measure_slot_sizes` printed `[('## Build-level rules', 1681)]` and the limits file the cap 1800, so the sentence stays where unit 88 put it (DERIVED 2026-11-24, both commands).
- AC13 — `git worktree list --porcelain` — printed 113 `worktree` lines and none matching, and no entry of the common directory starts `mc` or `gate-mc` (DERIVED 2026-11-24, both reads).
- AC14 — `quoted` — the three paths S14 above lists are every such line, and the anchored read printed no path. No write-once read of units 79 to 88 skipped a record: units 79, 81, 83, 84, 85 and 86 each record that theirs listed nothing before any write, unit 80's predicate listed nothing, unit 82's table owed none, unit 88's S19 read listed none, and unit 87 wrote none and read none. The ledger of unit 82 that the scan quotes names a roster record and rests no decision on it (DERIVED 2026-11-24, those ledgers).
- AC15 — `untracked` — led no line of the tip scan, at the base or at the tip. Unit 80 caused no record of `TOOL-dTotalRecall-69` or `TOOL-dTotalRecall-76`: none (DERIVED 2026-11-24, the scan's `by` lines).
- AC16 — `shared-n` — led no line of the tip scan. `git grep -n "DISPATCH IS STRICTLY SEQUENTIAL, including" -- tools/workflows/unattended-build.js` and `git grep -n "units.slice().sort" -- tools/workflows/unattended-build.js` printed one line each, at `tools/workflows/unattended-build.js@67ffd1289:78` and `tools/workflows/unattended-build.js@67ffd1289:692`, the file's lines the same at the base (DERIVED 2026-11-24, these commands).
- AC17 — `red population` — printed over the block with unit 69's verdict line deleted, exit 1, and over the block whole the script exited 0 (DERIVED 2026-11-24, both runs).
- AC18 — `grep -c "Unit 84 may" 2026-10-26-spec-TOOL-dTotalRecall-83.md` — printed 1, and the tip scan's one `by` line for `TOOL-dTotalRecall-74` is caused by `PLAY-dClosedLoop-2`, so units 83 and 84 each caused none (DERIVED 2026-11-24, that command and the scan).
- AC19 — `git ls-files --error-unmatch kit.toml legacy_ledger.py` — exited 0, as it did for each of the three carriers from the root, and each of unit 88's AC3 greps printed nothing, exit 1 (DERIVED 2026-11-24, these commands).
- AC20 — `last-body-change` — is in the rules slot's fourth bullet, and unit 88 §4's fence probe printed a mid-line count of 0 over spec 74 and of 1 over spec 76 (DERIVED 2026-11-24, that probe).
- AC21 — `tempfile.mkdtemp(prefix="rc-")` — is the shape, the one call unit 88's AC15 python prints, its prefix length 3; unit 88's cited call, `tools/govkit/govkit.py@67ffd1289:5195`, carries the longer prefix `govkit-6b-`, ten characters, and stands only as govkit's prefixed call. The report's `prefix='kg'` is in no file under `tools/` (DERIVED 2026-11-24, these reads).
- AC22 — `dup` — led one line over the scratch folder of two records of unit 59 whose Evidence differs by one byte, beside a `by` line counting 2, and no line of the tip scan (DERIVED 2026-11-24, both scans).
- AC23 — `python -c "import tree_lib; d = tree_lib.resolve_memory_root.__doc__; print([n in d for n in ('runlog_lib', 'loop_lib', 'memory-recall')])"` — printed `[True, True, True]`. `git grep -n "def resolve_memory_root(" -- tools` printed four lines: `def resolve_memory_root(tree):` in `tools/loop/loop_lib.py`, `def resolve_memory_root() -> str:` in `tools/memory-recall/selftest.py`, `def resolve_memory_root(conf: dict) -> str:` in `tools/memory-tree/tree_lib.py` and `def resolve_memory_root(root) -> str:` in `tools/runlog/runlog_lib.py` (DERIVED 2026-11-24, both commands).
- AC24 — `read_at` — as corrected, printed `653bed738685c8d41ee71fbf740a5e3654bdd703 2 is absent` for each of the two needles, where unit 81's printed 0 and 2. An empty file and a file of blank lines each printed `red no needle in` with its path and exited 1. §4's needle scan printed `blocks 14` and no other line (DERIVED 2026-11-24, these runs).
