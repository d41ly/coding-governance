# DEPL-cMendedVintage-19 — a row's role is re-resolved at every schema, so a role move is reported

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-prompt-DEPL-cMendedVintage-19-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-19-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-6` §4 Migration says an adopter's two stale engine rows "report as withdrawn with
an order written to the outbox". The engine cannot produce that: `withdrawn` is the grid cell
`("equal", "absent")` at `tools/govkit/govkit.py:5379`, `t_state` is decided by whether gov's source
blob exists at `to_commit` (`classify_row`, `:5781` and `:5787`), and that unit keeps both records
tracked in gov's tree. Meanwhile the role re-resolution at `:6331` is gated on `schema < 2`, so a
schema-3 row keeps `engine` and takes the full `table` disposition against a rule that now declares
`project-owned` and supplies no bytes. Re-resolve at every schema and report the move.

## 2. Scope (IN)

- **S1** The re-resolution block at `tools/govkit/govkit.py:6331` loses its `schema < 2` guard and runs
  for every schema, against the descriptor's current resolution for that row's kit. Observed by AC1.
- **S2** A row whose recorded role and current resolution DISAGREE takes a new `role-moved`
  disposition instead of the recorded role's table row: the run reports the old role, the new role and
  the path, writes nothing for that row, and does not count it as a change. A disagreement is a
  descriptor transition, not a byte question. Observed by AC2 and AC3.
- **S3** The `r.fail` at `:6325`'s sibling — the schema-1 disagreement refusal — is kept for
  `schema < 2` alone, because a schema-1 role is UNTRUSTED for a different reason and refusing is
  still correct there. S2's disposition is the schema-2-and-up answer, and the two are written as two
  branches rather than one widened one. Observed by AC4.
- **S4** `tools/govkit/matrix.py` gains one arm built on an AGED receipt rather than a fresh install:
  a schema-3 receipt carrying an `engine` row, a descriptor edited to claim that destination as
  `project-owned`, then `update`, asserting the reported disposition. Observed by AC2.

## 3. Non-goals (OUT)

- No automatic rewrite of the row's `role` field. Recording the new role is a receipt write for a
  transition the operator has not acknowledged, and the whole point of reporting is that gov stops
  acting on a rule it can no longer honour.
- No withdrawal, no deletion, no order. `DEPL-cMendedVintage-6` §4 asks for an outbox order; this unit
  reports on the run instead, because an order is a durable artifact and a role move is resolved by
  the operator's next `apply`, which rewrites the row.
- No change to `VERDICT_GRID`, to `classify_row`, or to what `withdrawn` means. The finding is that a
  spec paragraph named a cell the engine cannot reach; the answer is a new disposition, not a new cell
  in a grid every other disposition reads.
- No closure of `DEPL-dPolishedVitrine-1`'s other two clauses. That row asks for three things — the
  re-resolution, the PINNED re-adopt named when a stamp is withheld, and `adopt`'s evidence printed
  apart from its key. This unit takes the first only, and the row stays OPEN for the rest.

### Edges

- **consumes-from** `DEPL-cMendedVintage-6` — that unit makes the descriptor move that creates the
  transition this unit reports. Without it the engine-to-`project-owned` move has no instance in this
  build and the arm in S4 would be grading a hypothetical.
- **hands-off** external — the two live adopters see the report on their first update after both
  units land; the disposition of their stale rows is theirs.

## 4. Design

### What the engine does today, read from source

| the row | `role` recorded | descriptor now says | what `update` does |
|---|---|---|---|
| gov's fixture record, schema 3 | `engine` | `project-owned` | `UPDATE_ROLE["engine"]` is `table`, so the full verdict table runs |
| the same row, at `schema < 2` | `engine` | `project-owned` | re-resolved at `:6331`, disagreement refused |

`UPDATE_ROLE["project-owned"]` is `skip` (`:5438`), so the NEW rule supplies nothing to compare
against and the OLD rule's table is what runs. An adopter's renamed-away copy then grades `missing`
and is restored, which is the clobber `DEPL-cMendedVintage-6` exists to stop, surviving that unit
because the row's role never moved.

### Why a disposition rather than a refusal

`schema < 2` refuses because a schema-1 role is UNTRUSTED — the receipt is known to stamp roles its
descriptor contradicts, so neither answer may be acted on. A schema-3 disagreement is different: both
answers are trustworthy and they describe two different vintages. That is a transition with a correct
handling, and refusing a whole run over a correctly recorded history would wedge exactly the adopters
this build is trying to unwedge. S3 keeps the two branches apart so a later reader does not merge
them into one behaviour that is wrong for one of the two reasons.

### Inventory

| identifier | kind | where |
|---|---|---|
| `role-moved` | verdict token | `tools/govkit/govkit.py`, the `tally` slot and the summary line |

No function, flag or file is minted. The token follows the `pins-moved` spelling the same tally
already carries.

### Migration

An adopter's first `update` after this lands reports one `role-moved` line per row whose descriptor
role changed, and writes nothing for those rows. Their receipts are unchanged until they run `apply`,
which rewrites the row with the current role — the verb that was always the one to record a
descriptor transition. No receipt field changes shape and no schema moves.

### Rollout

Lands directly. The new branch is reachable only where a recorded role and a current resolution
disagree, which is a state no target is in until a descriptor moves a destination between roles.
`DEPL-cMendedVintage-6` is the first such move in this build, which is why this unit is sequenced
after it.

### Alternatives rejected

- **Leave the guard and correct `DEPL-cMendedVintage-6`'s Migration paragraph.** That is a fold, and
  the finding is at HIGH because the paragraph is not merely wrong prose: the transition it describes
  does not happen, so the unit ships a descriptor move whose engine-side effect nobody has measured.
- **Rewrite the row's `role` in place on the update.** `update` would then be recording a descriptor
  transition without the operator's `apply`, and a row rewritten silently is a provenance claim
  nobody made.
- **Widen the schema-1 refusal to every schema.** It reds every run of every adopter mid-transition,
  with the remedy being the verb this build exists to stop recommending.
- **Add a `withdrawn` path for a role move, matching the spec's paragraph.** `withdrawn` means gov's
  source is gone, and it drives deletion under `--write-withdrawals`. Reusing it for a role move puts
  a deletion path behind a descriptor edit.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the guard removed, the two branches split, the new disposition and its tally |
| `tools/govkit/matrix.py` | the aged-receipt arm |
| `memory/backlog/DEPL.md` | `DEPL-dPolishedVitrine-1`'s first clause struck, the row left OPEN for the other two |

## 5. Production-readiness checklist

- security — the re-resolution reads gov's own descriptors through `target_context` and
  `resolve_entry`, which the `schema < 2` branch already calls. No new input and no new write.
- perf / scale — one `resolve_entry` per claimed kit per run, on every schema instead of on schema 1.
  The call is already made for every kit the run acts on, so the cost is a cache read in the common
  case and is measured at build time rather than pinned here.
- error / empty / loading states — a row whose kit is not in `descs` skips the re-resolution exactly
  as today; a row the descriptor no longer resolves at all keeps its recorded role and takes the
  existing unclaimed-source path.
- observability — one `role-moved` line per row naming both roles and the path, and a tally slot so a
  run with many of them reports a count rather than a wall.
- risks — the sharp one is scale: un-gating the re-resolution puts a descriptor resolution on every
  row of every run, and a target with 95 rows across a dozen kits is the case to measure. If the
  build-time reading finds it costly, the resolution is memoised per kit, which is a local change and
  not a scope change. Second: splitting the branches leaves two behaviours for one disagreement, and
  S3 is written so the split is deliberate rather than discovered.
- testing — AC1 through AC4; the aged-receipt fixture in S4 is the one shape every criterion in
  `DEPL-cMendedVintage-6` §6 could not reach, because each of those starts from a fresh install.
- migration — §4; one report per moved row, resolved by the operator's next `apply`.
- user docs — `WIRE-INTO-PROJECT.md`'s update section gains one sentence on what a `role-moved` line
  means and that `apply` is what clears it.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target holds a schema-3 receipt whose row records `engine` and
  whose descriptor still resolves `engine`, `python tools/govkit/govkit.py update --target <fixture>`
  reports that row exactly as it does at BASE.
  Red when: the un-gated re-resolution changes the disposition of rows that did not move, which would
  make every ordinary run take a new path.
  fixture: a scratch fixture target under the run's scratch root; this repo keeps no `.governance/`
  receipt and can host no criterion in this section.
- **AC2** — When that fixture's descriptor is edited to claim the row's destination as
  `project-owned` and `python tools/govkit/govkit.py update --target <fixture> --write` runs, the run
  reports `role-moved` naming both roles and the path, and the file on disk is byte-identical
  afterwards.
  Red when: the guard is left at `schema < 2`, so the row keeps `engine`, takes the table disposition
  and is restored from gov's bytes over the target's own copy.
- **AC3** — When that same run finishes, the fixture's receipt row still records `engine` and the run
  counted no change for it.
  Red when: the disposition rewrites the role, which records a transition the operator's `apply` never
  performed.
- **AC4** — When a schema-1 fixture receipt carries the same disagreement and
  `python tools/govkit/govkit.py update --target <fixture>` runs, the run still refuses with the
  message at `tools/govkit/govkit.py:6325`'s sibling branch.
  Red when: the two branches are merged, so an untrusted schema-1 role takes the reporting path and
  the run acts on a role the receipt is known to get wrong.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/matrix.py` · a schema-3 receipt with an `engine` row and a descriptor edited to
claim that destination as `project-owned`, asserted to report and not to write · the
`tools/govkit/refusal_join.py` `BRANCH_PIN` floor is re-derived in the same commit if the branch split
moves the live count.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "restore a snapshot entry whose kit key no rollback loop
selects"` was this promoted set's probe and returned no seam; its ranked rows are name-token
neighbours on `kit` and `key`, one of which — `resolve_entry` in `tools/govkit/govkit.py` at fan-in 1
— is the function this unit actually reuses, reached by reading rather than by rank. The seam is the
`schema < 2` block at `tools/govkit/govkit.py:6331` itself: it already calls `target_context`,
`resolve_entry` and the `writes`-then-`unlanded` lookup this unit needs, so un-gating it is a guard
change and not a new resolution path. The recall probe returned the record that owns the gap:
`DEPL-dPolishedVitrine-1` in `memory/backlog/DEPL.md:60`, OPEN, which states that `update` keeps a
schema-3 row's role and asks for re-resolution at every schema. The spec set cited it nowhere before
this unit, which is what the review found.

Recall terms used: `--terms "govkit rollback snapshot attributes receipt row kit orphan restore
touched_kits claimed verify outcome regenerate"`, with the question "what decided how govkit rollback
selects snapshot entries by kit and what owns the synthetic attributes row".
