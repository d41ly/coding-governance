# TOOL-dDeclaredLoop-61 — every draw row carries a draw id, so two identical parallel draws stay two rows

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 30 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-61-deviation-611.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-61-deviation-611.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 53 at HIGH**, its item **H4**, which it shares with id 38; id 38 is
`TOOL-dDeclaredLoop-62`. A draw row is `draw · <cause> · <item> · <spent>/<total>`
(`TOOL-dDeclaredLoop-30` S3) and carries no unit, sha or time. Two worktrees making the same draw on one
item, each typing the figure its own history saw, append byte-identical lines, and git takes an
identical change on both sides once: two skeptics reproduced a merge at rc 0 holding one draw row. The
budget counts one draw fewer per collision, exactly when parallel worktrees draw on the same thing, and
`TOOL-dDeclaredLoop-49` S2's typed-versus-derived line never fires because one row is left. This unit
makes the row unique, the half of the fix that makes any merge keep both. It repairs
`TOOL-dDeclaredLoop-49`.

## 2. Scope (IN)

- **S1** — The row grammar gains a trailing field, the draw id: `draw · <cause> · <item> ·
  <spent>/<total> · <draw-id>`, the id `<UTC yyyymmddThhmmssZ>-<6 hex>`, the hex from `secrets.token_hex(3)`
  at write time. `record_draw` writes it on a log-record row and on a run-state row alike, and
  `TOOL-dDeclaredLoop-30` S9's copy of a run-state row into a log record keeps it. This amends
  `TOOL-dDeclaredLoop-30` S3's grammar by one field. Observed by AC1, AC3.
- **S2** — `spent` counts rows by draw id: two rows carrying one id are one draw, and a row carrying none
  (written before this unit) counts as its own draw, so no landed record's count moves. This refines
  `TOOL-dDeclaredLoop-49` S1's count. Observed by AC1, AC2.
- **S3** — A draw riding a `Gov-Transition` trailer, `TOOL-dDeclaredLoop-48` S2's `draw=` field, needs no
  id: its commit is its identity, and two such draws are two commits. Observed by AC3.
- **S4** — The fixture case `parallel-append-identical`: two branches off one record each append a draw
  with the same cause, item and typed figure, and merge under the transition-record attribute the tree
  declares, read with `git check-attr merge` on a transition record path and copied into the fixture.
  Observed by AC1.

## 3. Non-goals (OUT)

- Which merge driver `.gitattributes` names for transition records: `TOOL-dDeclaredLoop-62`, which takes
  this unit's id as what keeps two rows apart.
- Rewriting landed rows to carry an id: S2 reads them as they are.
- A checklist entry that every merged append-only record carries a unique field, the finding's
  left-shift: the class is recorded at the close; S4 is this record's identical-rows fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-49` — the build-wide count of draw rows and the typed-figure line, whose rows this unit makes distinct
- **hands-off** `TOOL-dDeclaredLoop-62` — the draw id, the field that keeps two identical draws two lines under any merge driver
- **hands-off** `TOOL-dDeclaredLoop-75` — the one row order and the id's own regex (the round-3 spec audit's ids 14, 33); this pass keeps the `loop budget fixtures` leg green (id 31)

## 4. Design

### Evidence

- The skeptic's reproduction, id 38 and id 53 of the report: two branches each appending
  `draw · review-round · item.a · 2/10` under `merge=union` merged at rc 0 with one such row.
- `TOOL-dDeclaredLoop-49` §4's own example has two worktrees both typing `3/10`, which is the collision.
- A run-state row already opens with a `<ts>`; a log-record row has no such field.

### The row

```
draw · review-round · TOOL-dX · 3/10 · 20261024T153012Z-4fa1c9
```

Six hex digits beside a second-resolution time make a collision need two draws in one second drawing the
same 24 bits, and S2 would then count one draw fewer, the defect's own bound at a rate this unit does not
measure. The id is never compared across builds.

### Files touched (estimate)

- `tools/loop/budget.py`

### Alternatives rejected

- **The drawing commit's sha.** A row is written before its commit exists, so the sha cannot be in it.
- **A worktree name.** Two runs in one worktree, one after the other, draw the same row again.

## 5. Production-readiness checklist

- security — `secrets` draws the hex; no new surface.
- perf / scale — one more field per row.
- error / empty / loading states — a row whose id field is malformed is named by `budget_state` and
  counted as its own draw, never refused.
- observability — `budget_state --explain` prints each row's id.
- risks — two rows with one id are one draw; only a copy carries a repeated id by construction.
- testing — AC1 to AC3 as fixture plants; the arm under §7, observed at the close.
- migration — none: S2 reads id-less rows.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant parallel-append-identical` merges the two branches,
  the merged record holds two draw rows differing only in their draw id, and `budget_state` counts both.
  Red when: the rows carry no id, git takes the identical change once, and one draw is counted.
- **AC2** — When `--plant legacy-rows` reads a record whose three draw rows carry no id, `budget_state`
  answers `open 3/<total>`.
  Red when: id-less rows are skipped or collapsed into one.
- **AC3** — When `--plant id-on-every-home` draws once into a log record, once into a run-state file and
  once on a `Gov-Transition` trailer, the first two rows end in a field matching
  `^[0-9]{8}T[0-9]{6}Z-[0-9a-f]{6}$` and the trailer's `draw=` field carries none.
  Red when: a home writes the old grammar.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/budget.py · covers AC1 AC2 AC3 · the identical-rows merge, legacy rows and the per-home id plants, staged against `TOOL-dDeclaredLoop-30`'s id-less grammar · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 53 (HIGH, item H4, shared
  with id 38).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dDeclaredLoop-30`'s own row writer and reader in `tools/loop/budget.py`; the id is one
field on the grammar that unit owns. `python tools/codebase-map/reuse_lookup.py "unique field on an
appended row so a merge keeps both"` ranked `rows`, `row`, `merge` (`tools/memory-tree/merge-rows.py`),
`field`, `extract_row` and `id_rows`; `merge-rows.py` keys a row by its id or a digest of its text, which
makes an identical row one row, so no existing seam supplies uniqueness and the field is this unit's.

Recall terms used: budget draw row grammar unique id parallel worktree identical append merge union collapse spent
