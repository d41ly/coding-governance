# TOOL-dTotalRecall-100 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-100
**Caused-by:** TOOL-dTotalRecall-100

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-2 over
base `ace443fc3f526435139d522485f7c324f4177b9b` on node a, 2026-11-25 local. The pass edits no code, restores no record,
removes no worktree and writes no deviation record. §7's legs are the close's, and §7 declares no new arm. The probes are
§4's fences, the amended scan made by splicing §4's python fence into unit 99's, beside the fences of units 81, 89, 90,
92, 93, 95, 97 and 98 §4. Each was extracted verbatim from its spec into a file under the scratch directory and run from
the repository root, `PY` being the launcher the scan resolves. The fixture repository was made under the scratch
directory and removed after the run.

The fixture (DERIVED 2026-11-25, that run), every block as §4 pins it:

| Block | Printed (DERIVED 2026-11-25) |
|---|---|
| `pair` | one `dup` line naming `-591` and `-592`, and `scan ok 2 2` |
| `malformed` | one `malformed` line ending `Risk is missing`, and `scan ok 1 1` |
| `corrected` | no `dup` line, and `scan ok 3 2` |
| `superseded` | `malformed-superseded` naming `-591`, no `malformed` line, and `scan ok 2 1` |
| `free` | `restored` naming `-deviation-2`, taken out at `022207d4817e`, as `-deviation-3`, then `f9ba13854f1d735e979f4d1aaa8614ac6ef24fef` twice |
| `again` | `held`, ending `bytes-present` |
| `join` | `read 3` alone |
| `shared` | `read 4` and two `malformed:` lines, each `shares deviation-1 with` the other |

The scan at the base printed the same block, line for line, as `2026-11-24-build-TOOL-dTotalRecall-99-1-acceptance-ledger.md`
holds, by `diff` (DERIVED 2026-11-25), so no line moved with the amendment over a folder where no record is malformed.

S2, `scan_edits` (DERIVED 2026-11-25, that run). Every trailer is `none`, so no pass made one and no record is owed:

| Commit | `Pass:` | Records it modified |
|---|---|---|
| `9773de4ad99bcce909475f685de8168f0f67c1e3` | none | `2026-11-22-build-TOOL-dTotalRecall-8-deviation-83` |
| `1c944a4ac572c8afda1d5bc94a807c208c048486` | none | `2026-11-22-build-TOOL-dTotalRecall-1-deviation-15` |
| `f070230a554c0a19a7f77d6378508167ab7733f8` | none | `2026-10-26-build-TOOL-dTotalRecall-2-deviation-21`, `2026-10-26-build-TOOL-dTotalRecall-23-deviation-231`, `2026-10-26-build-TOOL-dTotalRecall-8-deviation-81` |

S8 to S11, unit 89's two fences run at the base (DERIVED 2026-11-25, that run; the red reads' lines follow the walk's):

```text
s1-59 206422580b7363ab9582e37ffe7de7c25773a721 1 `absorbs` is absent
0
0
p83 39ffc882ed18d2f5234fe4b86739ca4175a1d656
rec memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md before-p83 9443f6b3d152b71fd88e9e9d1e8f01c5ab6536d8
rec memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md before-p83 9443f6b3d152b71fd88e9e9d1e8f01c5ab6536d8
rec memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md at-or-after-p83 9443f6b3d152b71fd88e9e9d1e8f01c5ab6536d8
rec memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md red ancestry rc=128
rec memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md ungraded p83 red 83 no pass commit
rec memory/builds/dTotalRecall/build/none-deviation-0.md at-or-after-p83 untracked
s1-999 red 999 no pass commit
1
0
```

S13, the main loop's `check_swept`, run at `07de92e8f` and handed in the brief
`2026-11-25-prompt-TOOL-dTotalRecall-100-build-brief.md`. Run again by the builder at the base over the same lines of unit
78's AC1 block, it printed the same (DERIVED 2026-11-25, both runs). No line is `unswept`, so no second sweep is owed:

```text
none 8 no pass commit
none 37 no pass commit
none 14 no pass commit
none 15 no pass commit
none 26 no pass commit
population 72 swept 67
```

The zero is no unmovable count. Over a scratch copy of that block with unit 69's verdict deleted and unit 70's status made
a bare 1, it printed `unswept` for units 69 and 70 at their passes and `population 72 swept 65` (DERIVED 2026-11-25, that run).

S18, the five lines the cite scan prints, all of spec 91, beside the text `git show f7011dd6f:skills/session-kickoff/manifest-check.sh`
gives at each first-cited line (DERIVED 2026-11-25, that command):

| Cite of spec 91, as spelled there | The line's text at that blob |
|---|---|
| `skills/session-kickoff/manifest-check.sh@f7011dd6f:236` | `ROOT=$(git rev-parse --show-toplevel 2>/dev/null)`, else the not-a-repository error and `exit 2` |
| `skills/session-kickoff/manifest-check.sh@f7011dd6f:2656` | `fail 5 "watched files changed since last-audit with no re-stamp at/after the change:` |
| `skills/session-kickoff/manifest-check.sh@f7011dd6f:2527-2570` | `BLOCK_OK=1` |
| `skills/session-kickoff/manifest-check.sh@f7011dd6f:2618-2644` | `SKIP_RANGE=0` |
| `skills/session-kickoff/manifest-check.sh@f7011dd6f:2359` | the `1)` arm, `carries no kickoff-manifest marker` and `exit 0` |

Each holds what spec 91 cites it for, as do the four bare lines that spec names beside the first, each an `exit 2`
(DERIVED 2026-11-25, the same blob).

**Evidences:** TOOL-dTotalRecall-100
- AC1 — `malformed-superseded` — led one line of the `superseded` block, with no `malformed` line and `scan ok 2 1`; the `malformed` block printed one `malformed` line. `tip_check memory/builds/dTotalRecall/build` printed no `malformed` line and ended `scan ok 151 148`, exit 0, at the base and again after this ledger was written (DERIVED 2026-11-25, those runs).
- AC2 — `scan_edits` — listed the three commits and five records of the S2 table above, the three §4 pins, and nothing from `tools/`; with `-m` the same three commits. No commit's trailer names a unit, so `has_deviation memory/builds/dTotalRecall/build <unit> 'audit-89 id 23 s2'` is owed at 0 for every unit, and printed 0 for units 1, 2, 8, 23 and 92, the four edited units and the restoring one (DERIVED 2026-11-25, these runs).
- AC3 — `dup` — led one line of the `pair` block and none of the `corrected` block, which ended `scan ok 3 2`; the scan over the build folder printed none, so no pair of unit 92 is made one again (DERIVED 2026-11-25, those runs).
- AC4 — `has_deviation --paths memory/builds/dTotalRecall/build 69 'audit-77 id 23 s4'` — listed no record and printed 0, so none is withdrawn; with no token it listed unit 69's roster record and 1. `c5_input` over unit 80's ledger printed `p69 rc=0` and `p69 unplaced 0`, the placed status line (DERIVED 2026-11-25, these runs).
- AC5 — `grep -c 'kickoff-manifest:'` — printed 1 over `memory/guides/SESSION-KICKOFF.md` at `f7011dd6fc390d088e0d790c5e6c6901fd20edd6`, the commit `pass_of 69` printed, the line `<!-- kickoff-manifest: v1.5 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->`; a misspelled marker printed 0. `has_deviation memory/builds/dTotalRecall/build 69 'audit-89 id 7 s5'` printed 0, and unit 96's GREEN answer stands (DERIVED 2026-11-25, these commands).
- AC6 — `has_deviation memory/builds/dTotalRecall/build 59` — with the string printed 0, at most 1; with no token it printed 1, the roster record (DERIVED 2026-11-25, both runs).
- AC7 — `key59 memory/builds/dTotalRecall/build` — printed `key59 0 0` and no `missing` line, so no record is named unowed. `grep -l 'Caused-by:.. TOOL-dTotalRecall-100'` over unit 59's one record listed nothing, exit 1; with `PLAY-dClosedLoop-2` for the cause it listed it (DERIVED 2026-11-25, these commands).
- AC8 — `has_deviation --paths` — printed for unit 59 the one path `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md`, and the walk one line for it, `before-p83`; the red reads printed what §4 pins, the block above (DERIVED 2026-11-25, that run).
- AC9 — `at-or-after-p83 untracked` — is what `check_ancestry` printed with `HEAD` over a none-deviation-0.md of the build folder (DERIVED 2026-11-25, that run).
- AC10 — `ungraded p83 red 83 no pass commit` — is what `check_ancestry` printed given that red line. `has_deviation memory/builds/dTotalRecall/build 89 'audit-89 id 31 s10'` printed 0 and with no token 1: unit 89 answered that arm green over a `pass_of 83` sha, with no counted record and no red or ungraded line, so no record is owed (DERIVED 2026-11-25, these runs and unit 89's ledger).
- AC11 — `has_deviation --paths memory/builds/dTotalRecall/build 59` — printed one `rec` line, the path AC8's walk line names and no other; with the string it printed no `rec` line and 0, and with `pass(59)` and the string the same, so the walk misses no counted path (DERIVED 2026-11-25, these runs).
- AC12 — `write_free_restores 462d20f3..HEAD` — printed nothing, at the base and after the pass, and the tree stayed unchanged; `deleted_records` over the range printed nothing beside its liveness of 151, so no path is absent and none is restored under a free `<n>`. Unit 92's pass `2db944436b369b9b5861d681ce6e2682052d1ccd` modified no record. The fixture's `free` and `again` blocks printed what §4 pins (DERIVED 2026-11-25, these runs).
- AC13 — `check_swept "$SWEEP"` — printed the block above, at the base: no `unswept` line, its `none` lines units 8, 37, 14, 15 and 26, exactly the population's specs not CLOSED, each DEFERRED, and `population 72 swept 67`, the rest (DERIVED 2026-11-25, the main loop's run, this one and the spec headers).
- AC14 — `git worktree list --porcelain` — printed 114 `worktree` lines, none ending `/gate-mc92` or `/gate-mc100`, and no entry of the common directory's 81 is named either, so nothing was removed (DERIVED 2026-11-25, both reads).
- AC15 — `scan_cells` — printed `cells 10 edges 3` alone, and over the planted copies a `run` line for each planted needle and the same counts. Unit 92's scan printed `blocks 14` alone, and with the scratch spec a `run` line and `blocks 15` (DERIVED 2026-11-25, these runs).
- AC16 — `memory/builds/dTotalRecall/spec/*.md` — under §4's predicate read 0 for each of the 24 specs of units 77 to 100; of the other 67 it read above 0 for two, unit 70's at 3 and unit 76's at 1, its liveness and the two frozen specs named (DERIVED 2026-11-25, that run).
- AC17 — `grep -n "units.slice().sort" tools/workflows/unattended-build.js` — printed `692:const ordered = units.slice().sort(function (x, y) {`, the one line, and the cite scan printed no line of spec 90 (DERIVED 2026-11-25, both commands).
- AC18 — `git show` — gives the texts of the S18 table above at each first-cited line; the cite scan printed no line of spec 89 and five of spec 91, each pinned at `f7011dd6f`, and over the scratch file it printed both bare cites (DERIVED 2026-11-25, these commands).
- AC19 — `has_deviation memory/builds/dTotalRecall/build 88 'audit-77 id 1 '` — printed 0, the count unit 89's AC3 recorded, and with no token 2. Over the scratch folder it printed 0 where `audit-77 id 1` printed 1. The grep for a bare token over the folder's records listed nothing, exit 1, and listed the scratch file (DERIVED 2026-11-25, these runs).
- AC20 — `read_shared . memory/builds/dTotalRecall/build` — printed `read 151` alone, the number `git ls-files` lists there, before this ledger was written and again after; the scan printed no `untracked` line, and the fixture's `shared` block two `malformed:` lines (DERIVED 2026-11-25, these runs).
