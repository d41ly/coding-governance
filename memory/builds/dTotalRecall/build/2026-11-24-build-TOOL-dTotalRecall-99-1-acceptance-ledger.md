# TOOL-dTotalRecall-99 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-99
**Caused-by:** TOOL-dTotalRecall-99

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-2 over base
`40d07b1bef03ea7b2e6f95f1e9a10b939d140fd1` on node a, 2026-11-25 local, 2026-11-24 UTC, the date its DERIVED marks carry. The pass edits no code and writes no deviation record.
§7's legs are the close's, and §7 declares no new arm. The scan, the fixture and the reds are §4's fences and the probe is
spec 93's, each extracted verbatim into a file under the scratch directory and run from the repository root; the fixture's
two git lines ran each as its own command. The fixture repository was made under the scratch directory and removed after
the run. The scan ran before this ledger was written, over the base's build folder.

The reds (DERIVED 2026-11-24, that run):

| Block | Printed (DERIVED 2026-11-24) | Returned (DERIVED 2026-11-24) |
|---|---|---|
| `outside` | `red scan exit 1`, no scan line before it, `ModuleNotFoundError` on stderr | 1 (DERIVED 2026-11-24) |
| `no folder` | `records 0`, `live 0`, `red scan no records` | 1 (DERIVED 2026-11-24) |
| `unreadable` | `records 2`, `red unreadable memory/builds/dFx/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-22.md UnicodeDecodeError`, `live 1`, `by TOOL-dTotalRecall-2 TOOL-dTotalRecall-2 1`, `red scan exit 1` | 1 (DERIVED 2026-11-24) |
| `silent` | `red scan records, glob 2` | 1 (DERIVED 2026-11-24) |
| `short` | `red scan records, glob 2`, after its stubbed lines | 1 (DERIVED 2026-11-24) |
| `dropped` | `red scan by-sum 1 live 2`, after its stubbed lines | 1 (DERIVED 2026-11-24) |
| `whole` | `scan ok 2 2`, after its stubbed lines | 0 (DERIVED 2026-11-24) |

S4, unit 92's tip criteria graded again from the scan below, which ended `scan ok 151 148` and returned 0 (DERIVED
2026-11-24). The record count moved from §4's pin by `deviation-1014` of unit 87, which unit 92's own pass added. No
deviation record was added between that pass, `2db944436`, and this base, so no line names a later record:

| Unit 92's criterion | The line it names, in the scan below | Unit 92's answer | Grade |
|---|---|---|---|
| AC8 | no `malformed` line | none, exit 0 over 151 records at its tip (its AC8 line, DERIVED 2026-11-24) | green, agrees |
| AC11, the `dup` half | no `dup` line, so none naming a record of unit 59 | none | green, agrees |
| AC15 | no `untracked` line; no `by` line of `TOOL-dTotalRecall-69` or `TOOL-dTotalRecall-76` is caused by `TOOL-dTotalRecall-80` | none, and no record caused by unit 80 | green, agrees |
| AC16 | no `shared-n` line | none | green, agrees |
| AC18 | the one `by` line of `TOOL-dTotalRecall-74` is caused by `PLAY-dClosedLoop-2`, none by `TOOL-dTotalRecall-83` or `TOOL-dTotalRecall-84` | the same line | green, agrees |
| AC22, the tip half | no `dup` line | none | green, agrees |

Unit 92's answers rest on a full read: its ledger's AC8 line gives the scan's exit and its record count at its base and at
its tip, and its AC18 line names a `by` line of that scan. No answer differs and none came from a scan red here, so no
record of unit 92 is owed and none is written.

The scan at the base, whole (DERIVED 2026-11-24, that run):

```text
records 151
live 148
by TOOL-dTotalRecall-1 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-1 2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck 1
by TOOL-dTotalRecall-1 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-1 TOOL-dTotalRecall-1 2
by TOOL-dTotalRecall-100 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-11 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-11 2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-11 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-12 TOOL-dTotalRecall-12 1
by TOOL-dTotalRecall-14 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-15 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-16 TOOL-dTotalRecall-16 1
by TOOL-dTotalRecall-17 TOOL-dTotalRecall-17 1
by TOOL-dTotalRecall-18 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-18 2026-11-05-prompt-TOOL-dTotalRecall-18-owner-forks 1
by TOOL-dTotalRecall-19 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-19 2026-11-05-prompt-TOOL-dTotalRecall-18-owner-forks 1
by TOOL-dTotalRecall-19 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-19 TOOL-dTotalRecall-19 1
by TOOL-dTotalRecall-2 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 2
by TOOL-dTotalRecall-2 2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck 1
by TOOL-dTotalRecall-2 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-2 TOOL-dTotalRecall-2 2
by TOOL-dTotalRecall-20 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-20 2026-11-05-prompt-TOOL-dTotalRecall-18-owner-forks 1
by TOOL-dTotalRecall-21 TOOL-dTotalRecall-21 3
by TOOL-dTotalRecall-22 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-22 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-22 TOOL-dTotalRecall-22 2
by TOOL-dTotalRecall-23 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-23 TOOL-dTotalRecall-23 1
by TOOL-dTotalRecall-24 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-24 TOOL-dTotalRecall-24 1
by TOOL-dTotalRecall-25 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-25 2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-25 TOOL-dTotalRecall-25 1
by TOOL-dTotalRecall-26 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-26 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-3 TOOL-dTotalRecall-3 3
by TOOL-dTotalRecall-36 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-37 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-38 2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1 1
by TOOL-dTotalRecall-38 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-39 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-4 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-4 TOOL-dTotalRecall-4 1
by TOOL-dTotalRecall-40 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-41 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-42 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-43 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-43 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-43 TOOL-dTotalRecall-43 1
by TOOL-dTotalRecall-44 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-45 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-46 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-47 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-48 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-48 TOOL-dTotalRecall-48 1
by TOOL-dTotalRecall-49 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-5 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-5 TOOL-dTotalRecall-5 1
by TOOL-dTotalRecall-50 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-51 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-52 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-53 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-54 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-55 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-56 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-57 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-58 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-59 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-6 TOOL-dTotalRecall-6 2
by TOOL-dTotalRecall-60 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-61 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-62 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-63 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-64 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-65 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-65 TOOL-dTotalRecall-65 1
by TOOL-dTotalRecall-66 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-67 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-68 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-69 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-7 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-70 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-71 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-72 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-73 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-74 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-75 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-76 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-76 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-77 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-78 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-79 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-8 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-8 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-8 TOOL-dTotalRecall-8 1
by TOOL-dTotalRecall-80 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-81 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-82 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-83 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-84 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-85 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-86 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-87 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-87 TOOL-dTotalRecall-92 1
by TOOL-dTotalRecall-88 PLAY-dClosedLoop-2 2
by TOOL-dTotalRecall-89 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-9 2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck 1
by TOOL-dTotalRecall-9 TOOL-dTotalRecall-9 1
by TOOL-dTotalRecall-90 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-91 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-92 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-93 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-94 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-95 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-96 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-97 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-98 PLAY-dClosedLoop-2 1
by TOOL-dTotalRecall-99 PLAY-dClosedLoop-2 1
quoted memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-2-2-acceptance-ledger.md
quoted memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-71-1-acceptance-ledger.md
quoted memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-82-1-acceptance-ledger.md
scan ok 151 148
```

**Evidences:** TOOL-dTotalRecall-99
- AC1 — `tip_check memory/builds/dTotalRecall/build` — returned 0 at the base, its last line `scan ok 151 148`; `ls` listed 151 `*-deviation-*.md` files there (DERIVED 2026-11-24, that run and that count).
- AC2 — `red scan by-sum` — is the dropped scan's last line, and each other block ended in the line and status §4's table gives it, the first table above; no break printed `scan ok` and none returned 0 (DERIVED 2026-11-24, that run).
- AC3 — `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 29 s4'` — printed 0, and with no token 1 for unit 92, so the zero is no unmovable probe. `tip_check` at the base printed `records 151`, `live 148`, the 121 `by` lines of the block above, three `quoted` lines, no `malformed`, `shared-n`, `untracked`, `dup` or `red` line, and `scan ok 151 148`. From it AC8, AC11's `dup` half, AC15, AC16, AC18 and AC22's tip half of unit 92 each grade green, as unit 92 answered each, by the S4 table above; none differs, each answer rested on a full read, and no record follows its pass. `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-99" -- memory/builds/dTotalRecall/build` printed this ledger's block line and no other ledger's once it was written (DERIVED 2026-11-24, these runs).
