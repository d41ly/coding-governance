# TOOL-dRankedPlan-34 — a disposition record is dated by its first appearance under any name, so a rename does not refresh it

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 5 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-34-deviation-341.md](../build/2026-10-27-build-TOOL-dRankedPlan-34-deviation-341.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-34-deviation-342.md](../build/2026-10-27-build-TOOL-dRankedPlan-34-deviation-342.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) | spec-audit | TOOL-dRankedPlan-35 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-36 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 19 to 29
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`) confirmed
**finding 26 at HIGH**, item **H4**. `TOOL-dRankedPlan-24` S1 dates each disposition record by `git log
--diff-filter=A -1 --format=%H -- <path>`, and keeps it when the newest transition is a proper ancestor
of that commit. A path-limited log reports a renamed record as added at the rename commit. The finder's
scratch-repository probe committed a record, then a transition, then a `git mv` of the record, and the
reader kept it. So a disposition written for the first `plan.exit` and renamed after the B6 move
releases the revised plan's second crossing with no new owner act. That is the defect unit 24 exists to
close, and units 25 and 26 inherit it. History shows 29 renames under `memory/builds/*/build/`. This
unit dates a record by its first appearance under any name, the oldest add along `--follow`, the rule
the kit library's `read_first_commit_date` already follows. It repairs `TOOL-dRankedPlan-24`, so it
sits one order above it.

## 2. Scope (IN)

- **S1** — The date. `read_first_appearance(repo, path)` in `tools/loop/ratify.py` runs `git log
  --follow --diff-filter=A --format=%H -- <path>` and returns its last line, the oldest commit that
  added the record under any of its names. It returns `None` when the log prints nothing.
  `read_item_disposition` (`TOOL-dRankedPlan-24` S1) dates each record by it and keeps its rule: a
  record is kept when the newest transition's commit is a proper ancestor of that date. A record with
  no date is not kept. This supersedes unit 24 S1's `git log --diff-filter=A -1 --format=%H -- <path>`
  and the `added =` line of its §4 "The bound". Observed by AC1, AC2 and AC3.
- **S2** — The plants. `reader-bound` (`TOOL-dRankedPlan-24` S3) gains two cases. In `renamed-stale`, a
  record committed before the newest transition is `git mv`'d after it, and it is not kept. In
  `renamed-fresh`, a record committed after the newest transition is `git mv`'d later, and it is kept.
  A new plant, `terminal-reentry-renamed`, runs `terminal-reentry` with the first `terminal` record
  `git mv`'d after the B6 move. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- Which of several kept records governs: `TOOL-dRankedPlan-35`'s.
- A record that landed through a merge, and a record never committed (findings 13 and 27):
  `TOOL-dRankedPlan-37`'s items, over S1's date.
- Moving the date into `tree_lib.py`. `read_adding_commits` there reads with `--no-renames`
  (`tools/memory-tree/tree_lib.py:316`), which makes a rename an add, the defect this unit closes.

### Edges

- **consumes-from** `TOOL-dRankedPlan-24` — `read_item_disposition`, its bound and its `reader-bound` and `terminal-reentry` plants, whose date S1 replaces; without them there is no reader to date
- **hands-off** `TOOL-dRankedPlan-37` — `read_first_appearance`, over which that unit's items for findings 13 and 27 add the merge-delivered case and the uncommitted record's own hold line
- **hands-off** `TOOL-dRankedPlan-43` — S1's `--follow` date, which that unit replaces with a rename-only walk so a near-copy is dated by its own add (spec audit of units 30 to 37, id 19)
- **hands-off** `TOOL-dRankedPlan-45` — the `reader-bound` rename cases, beside which that unit's item for finding 36 plants the replace-in-one-commit case (spec audit of units 30 to 37)
- **hands-off** `TOOL-dRankedPlan-61` — S1's render rule, which this unit's function makes owed: carry `memory/map/generated/symbols.json` into this unit's Files touched and `codebase-map coverage + freshness`, `recall floor` and `recall floor arms` onto its leg line, in this unit's pass (spec audit of units 46 to 52, id 22)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-24` S1 and §4 "The bound" spell `git log --diff-filter=A -1 --format=%H -- <path>`
  with no `--follow`. The audit's appendix row for id 26 records the scratch probe: the rename commit
  came back as the add, and the reader kept the record.
- `read_first_commit_date` (`tools/unattended/lib-unattended.sh:1731-1734`) dates a record by `git log
  --follow --diff-filter=A --format=%cs -- "$_fd_p" | tail -1`. Its port at
  `tools/drift-audit/drift_report.py:2785-2795` says why: "the OLDEST add along `--follow`, so a
  rotation does not re-date an archive".
- `tree_lib.read_adding_commits` (`tools/memory-tree/tree_lib.py:302-325`) also returns the oldest add,
  but with `--no-renames`, so a renamed path is added again under its new name.

### The date after this unit

| The record's history | Unit 24 S1's date | S1's date | Kept after a transition T |
|---|---|---|---|
| added after T | the add | the add | yes |
| added before T, `git mv`'d after T | the rename | the add before T | no |
| added after T, `git mv`'d later | the rename | the add after T | yes |
| added before T, deleted, added again after T | the second add | the first add | no |
| never committed | none | none | no |

A record deleted and re-added under one path takes its first add, as the shared reader in `tree_lib.py`
does, so the two readers agree on that case.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_first_appearance` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest read_first_appearance --as py.function` answered OK |
| `terminal-reentry-renamed` | `ratify.py` fixture plant | none |

### Rollout

Live at landing. A record that has never been renamed keeps the date unit 24 gave it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Freshness by absence: keep a record whose path is absent at the newest transition's commit.** A
  record renamed after T has a new path absent at T, so absence keeps it. That is this finding's
  defect, which the skeptic's corrected fix for finding 13 does not address.
- **Content identity: keep a record whose blob is absent at T.** A rename that edits one byte makes a
  new blob and keeps the stale act. `--follow` tracks a rename by similarity, so an edited rename keeps
  its first add.

## 5. Production-readiness checklist

- security — narrows: a renamed owner act no longer releases a later crossing.
- perf / scale — one `git log --follow` per disposition record naming the item, a handful per move.
- error / empty / loading states — a record with no add commit is not kept, and the caller holds as for
  no fresh record.
- observability — the plants print which record the reader kept.
- risks — `--follow` reads one path per call and detects a rename by similarity. A rename that rewrites
  more than half the record is read as a new add, which keeps it. Such a rewrite is an edit of the
  owner's words, so the record is read as the edit's act.
- testing — the two new `reader-bound` cases and the renamed re-entry plant, red and green.
- migration — none.
- user docs — N/A — no surface changes.

## 6. Acceptance criteria

- **AC1** — When the plant `reader-bound` runs its `renamed-stale` case, `read_item_disposition`
  returns `None`.
  Red when: a record renamed after the newest transition is kept.
- **AC2** — When the `renamed-fresh` case runs, `read_item_disposition` returns the renamed record at
  its new path.
  Red when: a rename makes a fresh record stale.
- **AC3** — When `python ratify.py --fixture --plant terminal-reentry-renamed` runs, `ratify.py tFix`
  under `terminal-command` exits 1 after the B6 move and the rename, and exits 0 printing `ratified —
  terminal-command` once a second `terminal` record is committed.
  Red when: the first crossing's renamed record ratifies the second.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the `renamed-stale` and `renamed-fresh` cases of `reader-bound` and the `terminal-reentry-renamed` plant, staged by a date read with `git log --diff-filter=A -1` and no `--follow` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 19 to 29, finding 26 (HIGH,
  item H4), repairing `TOOL-dRankedPlan-24`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-43`, the hands-off edge to `TOOL-dRankedPlan-45`, each the reciprocal of that promoted unit's own edge (spec audit of units 30 to 37, `reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-61`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.

## 10. Reuse audit

The rule reused is `read_first_commit_date`'s oldest add along `--follow`
(`tools/unattended/lib-unattended.sh:1731`, ported at `tools/drift-audit/drift_report.py:2785`), lifted
into the loop kit's one disposition reader, which unit 24 already owns. The shared reader
`tree_lib.read_adding_commits` (`tools/memory-tree/tree_lib.py:302`) is not reused, because its
`--no-renames` is the defect. `python tools/codebase-map/reuse_lookup.py "the commit that first added a
file following renames"` ranked name stems only (`build_commit`, `add_health_event`,
`add_scratch_worktree`), so no existing Python seam fits beyond the rule cited. The recall query
returned PLAY-dOrderedCharter-47, which grades a record by its adding commit's ancestry, and this
audit's H4 item, and they agree.

Recall terms used: `python tools/memory-recall/query.py "how is a record's adding commit found when it was renamed" --terms "diff-filter=A follow rename first appearance adding commit read_adding_commits no-renames disposition freshness"`
