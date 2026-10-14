# TOOL-dTracedLedger-1 — check 23's reds at origin/main ebce889c7, traced and routed to owners

**Status:** CLOSED · rev-1 · 2026-10-14 · node d · Tier-1 · base ebce889c · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dTracedLedger-1-pairs.py](../build/2026-10-14-build-TOOL-dTracedLedger-1-pairs.py) | research | — |
| [2026-10-14-build-TOOL-dTracedLedger-1-research-check-23-reds.md](../build/2026-10-14-build-TOOL-dTracedLedger-1-research-check-23-reds.md) | research | — |
| [2026-10-14-prompt-TOOL-dTracedLedger-1-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dTracedLedger-1-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dTracedLedger-1-brief.md](../prompts/2026-10-14-prompt-TOOL-dTracedLedger-1-brief.md) | research | — |
| [2026-10-14-prompt-TOOL-dTracedLedger-1-spec-input.md](../prompts/2026-10-14-prompt-TOOL-dTracedLedger-1-spec-input.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Record why 37 check-23 rows reached origin/main `ebce889c7` past the merge bar, and hand each row's
fix to the build that owns it as an ask. The rows belong to two HELD runs of node `a`, so the fix is
routed rather than made, and no other build's records are edited.

## 2. Scope (IN)

- **S1** — A research record that states the reproduction, the first-parent bisect landing for
  every row, the attribution against the remote tip `2a9d8191` the push went over, each owner's run
  state, and the row classes. It is
  `build/2026-10-14-build-TOOL-dTracedLedger-1-research-check-23-reds.md`. Observed by AC2.
- **S2** — The read-only pairs instrument the record names,
  `build/2026-10-14-build-TOOL-dTracedLedger-1-pairs.py`. Observed by AC2.
- **S3** — Two asks with their dispositions in this build's `BACKLOG.md`: TOOL-dTracedLedger-2 for
  aSparedSpawn's 36 rows and TOOL-dTracedLedger-3 for aOrientedCast's one, each naming its rows by
  class and pointing at the owner's folder. Observed by AC3.
- **S4** — The build opened: `README.md`, the brief, the slot-contract row and the
  kickoff-manifest re-stamp, with the generated views regenerated. Observed by AC3.
- **S5** — No path under `memory/builds/aSparedSpawn/` or `memory/builds/aOrientedCast/` moves.
  Observed by AC1.

## 3. Non-goals (OUT)

- No edit to any line of aSparedSpawn's or aOrientedCast's specs, ledgers, `RUN.md` or `BACKLOG.md`.
  The ledger rewrites are the owners' work, asked for in TOOL-dTracedLedger-2 and -3.
- No `tools/` change. The two observations the record leaves unfiled stay unfiled here: the
  fork-starved run that dropped check 17's line, and the token arm's one-letter containment join.
- No fix to check 17's stale `memory/gotchas/INDEX.md`, which dRedressedBar's unit 7 owns.
- No acceptance ledger: check 23 grades CLOSED Tier-2 specs only
  (`tools/memory-tree/check-memory-hygiene.sh` line 3089), and this unit is Tier-1.
- No merge to main and no push.

### Edges

none

## 4. Design

The unit is records only, and every record is already written. The research record carries the
evidence and the asks carry the remedies, so each owner reads one ask row and follows its `seen`
pointer to the line at `ebce889c7`.

The asks live in this build's `BACKLOG.md`, not in the owners'. The owner's opening message asked
for aSparedSpawn's `BACKLOG.md`, and that request has no legal form for this session. An ask is
written by a session holding the id's own slug, in `builds/<that slug>/BACKLOG.md`
(`tools/memory-tree/README.md` line 214), and filing one elsewhere is verdict `V1`, "an ask's id
slug is not the build folder it is filed in" (line 268). The generator refused the first attempt
with that verdict. Each ask therefore ends with a pointer to the owner's folder, and
TOOL-dTracedLedger-2 and -3 are ask ids, not spec ids.

Reuse, recorded per seam:

| Seam | What this unit takes from it |
|---|---|
| aSparedSpawn's `- <id> · filed <date> · …` rows | the ask row, its `seen` and `accept` clauses |
| TOOL-aHoistedPass-39, `aHoistedPass/BACKLOG.md` line 42 | a check-23 ask, classed by shape |
| `f079464e2`, which opened dRedressedBar | the opening set: README, brief, slot-contract row |
| check 23's extractors, `check-memory-hygiene.sh` lines 2999 and 3050-3089 | the pairs instrument |

The pairs instrument mirrors the ledger extractor (the `alledger` stream from line 2999) and the
spec extractor (the acceptance-criteria scan around line 3075). It joins tokens per bullet where the
gate's form arm reads the first line only, so it classes rows and never grades them. It writes
nothing, and the record says so.

### Files touched (estimate)

- `memory/builds/dTracedLedger/`: its README, BACKLOG, the two build records, three prompts and
  this spec
- `memory/guides/SESSION-KICKOFF.md` (the manifest re-stamp, committed at `1a172f139`)
- `memory/project/readme-contract.txt`
- `memory/LIVE.md`, `memory/ledger/2026-10.md` and `memory/backlog/TOOL.md`, generated

## 5. Acceptance criteria

- **AC1** — When `git diff --stat ebce889c7..HEAD` runs, it lists no path in aSparedSpawn's or
  aOrientedCast's build folder.
  Red when: any line of either owner's spec, ledger, run record or backlog moved in this build.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, it names no
  TOOL-dTracedLedger id, and its check-23 lines name the same 37 rows as a run at base ebce889c7.
  Red when: check 21 cannot resolve the research record's Serves id, a record of this build trips
  any check, or the check-23 row set differs from the base's.
  figure: 37 is PINNED, measured at base ebce889c7 on 2026-10-14; the base run re-derives it.
  cost: two full hygiene runs, one of them in a detached worktree at the base.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --check` runs, it prints no
  build-index VERDICT line.
  Red when: TOOL-dTracedLedger-2 or -3 is filed outside this build's folder, which is verdict V1,
  or a generated view is stale against the build's records.

## 6. Gates

`memory hygiene` · `build README slot contract` · `kickoff-manifest ratchet` · `line length` · `recall floor` · `recall floor arms`

`memory hygiene` is red at the base on check 17 and the 37 check-23 rows, and this unit adds none.
`recall floor` and `recall floor arms` are owed because their `memory/` guard covers every path in
the estimate.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-14 · initial draft.
