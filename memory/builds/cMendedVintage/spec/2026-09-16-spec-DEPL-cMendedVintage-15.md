# DEPL-cMendedVintage-15 — the synthesized attributes entry is restorable, and no orphan line names it

**Status:** CLOSED · rev-4 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-15-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-15-acceptance-ledger.md) | journal | DEPL-cMendedVintage-10 |
| [2026-09-16-prompt-DEPL-cMendedVintage-15-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-15-2-build-brief.md) | journal | — |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |

<!-- /gen:spec-records -->

## 1. Goal

**rev-1's premise is false at BASE, and rev-2 says so before anything else.** rev-1 was drafted
against a PREDICTION of what `DEPL-cMendedVintage-10` would ship: a snapshot entry stamped with the
synthetic kit id
`(govkit)`,
which no registry entry claims, rejected by both consumers of a snapshot entry's `kit` key. What
`-10` actually landed one commit before this unit ran is the same repair by a different mechanism —
the entry is attributed to NO kit at all, the restore loop reaches it by `origin`, and the orphan
sweep is scoped to `origin == "table"`. Rev-1's three code changes are therefore already in the tree
in another spelling, and re-applying any of them would be a second answer to one question.

What was NOT in the tree is any execution of it. `-10` recorded its own AC4 OWED because no fixture
could produce a pin block and a green-to-red kit at once, so every line of that repair was built and
unobserved — which is the state this unit's own audit note calls a mechanism nobody has seen move.
So the goal of rev-2 is the one thing rev-1's premise did not cover: OBSERVE both halves on a single
run, and leave a gate behind that reds if either is undone.

## 2. Scope (IN)

- **S1** *(DISCHARGED AT BASE, by `-10`, not by this unit.)* The snapshot entry for
  `.gitattributes` carries `kit = None` rather than the synthetic id, with its reason on the site
  that builds it: carrying the id would put a kit no registry entry claims into the population the
  orphan sweep reports on. Verified as landed rather than re-written. Observed by AC1.
- **S2** *(DISCHARGED AT BASE, by `-10`.)* The per-kit restore loop selects
  `x["kit"] == eid or x["origin"] == "attributes"`, so the entry is reached by every rolled-back
  kit rather than by a stage after the loop. The all-or-nothing rule rev-1 argued for holds either
  way, and a second restore of one path is idempotent: the same pre-run index entry, put back again.
  Observed by AC2.
- **S3** *(DISCHARGED AT BASE, by `-10`.)* The orphan sweep is scoped to `origin == "table"`, the
  only origin it was ever about — a RECEIPT row attributed to a kit the receipt's own list does not
  claim. Scoping by origin rather than excluding one id is what rev-1 asked for and stronger than it:
  it needs no sentinel to stay correct if the id is ever renamed. Observed by AC3.
- **S4** *(THIS UNIT'S ONLY CODE.)* `tools/govkit/selftest.py` gains one arm group beside the
  `-14` rollback block: a second scratch gov whose rolled-back kit also declares an `[[lf_pin]]`,
  a target whose block is tampered inside the marker pair so the run rewrites it, and one
  `update --write` asserting both halves at once — the pre-run `.gitattributes` bytes return, and no
  `NOT VERIFIED` line names a kit the receipt does not claim. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- No change to what `apply` stamps. `(govkit)` is the id two write sites already spell and a receipt
  already on disk carries it; renaming it would be a receipt migration for a string.
- No generalised synthetic-id namespace, no `kit` sentinel table, no `is_synthetic` predicate. One id
  exists, one exclusion closes it, and a namespace invented for a population of one is plumbing.
- No repair of the THIRD consumer this unit's own fixture surfaced. The per-kit version-delta table
  groups RECEIPT rows by `kit`, so a target with a pin block prints
  `(govkit)                     gov side unresolvable — no comparison is possible`
  on every `update`. It is a noise row, not a false verdict and not a restore that cannot run, it
  predates this whole build, and closing it means either changing what `apply` stamps — the non-goal
  directly above — or a second filter in a report this unit was not scoped to touch. Recorded in the
  ledger instead of widened into here.
- No restore of an `attributes` entry on a run that rolled nothing back. The landed selection sits
  inside the per-kit rollback branch, so a clean run never reaches it, and the fixture asserts that
  it was reached by requiring `rolled back 1` before it compares any bytes.
- No change to the `pins` classification arm, to `lf_pin_block`, or to where gov's block sits in the
  target's file. Those are `DEPL-cMendedVintage-10`'s and `DEPL-dSettledRoster-1`'s.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — that unit creates the snapshot entry, the write, AND
  (contrary to rev-1's prediction) the restore and the sweep scope that make it reachable. What it
  could not do is execute any of it, so what this unit consumes is an unobserved mechanism rather
  than a defect. Without that unit there is no entry, no run that rewrites the block, and no subject.
- **hands-off** `TOOL-cMendedVintage-10` — this unit's four NARROWING declarations are the live
  instance that wedged the driver, and that unit exists to stop a superseded declaration holding a
  pass open forever. Nothing it changes reaches this unit's code; what it consumes is the record
  this unit left, not its mechanism.
- **hands-off** external — nothing else in this build reads the rollback pass's per-origin stages.

## 4. Design

### Why rev-1's own alternative is what shipped, and why that is fine

rev-1 rejected "bind the entry to the kits whose pins produced the block" for needing an ordering
rule. `-10` shipped neither that nor rev-1's after-the-loop stage: it left the entry unattributed and
made the per-kit loop's SELECTION origin-aware. The all-or-nothing rule survives — any rolled-back
kit restores the block — and the ordering objection never arises, because there is nothing to order:
the second restore writes the same pre-run index entry the first one did. rev-1's argument against
widening `touched_kits` still holds and is still the reason no synthetic id is in that list; what
changed is that the entry is reached without being in any kit-keyed population at all.

### The fixture, which is the whole of this unit

| # | piece | why it is shaped that way |
|---|---|---|
| 1 | a SECOND scratch gov, not an `[[lf_pin]]` on the `-14` roll gov | pinning that gov puts a `.gitattributes` under every `-14` arm, all written against a target with none |
| 2 | the pin declared on the kit that ROLLS BACK | the run must both write the block and enter the restore stage, and one kit doing both is the shortest fixture that reaches it |
| 3 | the block tampered INSIDE the marker pair, then committed | the `pins` arm reads `pins-moved` only against a block that differs from a fresh render; an untouched target reads `current`, writes nothing, and AC2 then passes over an absence |
| 4 | both halves asserted from ONE run | each alone is satisfied by an incoherent engine — the block comes back while a line still calls it an orphan, or the line goes quiet while the block stays staged |

### Inventory

No new identifier, in either file. The arm adds no `def`: it reuses `build_verify_gov`,
`build_verify_target`, `build_kit14`'s existing `extra` parameter, `settle`, `read_bytes14`,
`read_text14`, `run_in_gov` and `gout`, all already in scope beside the `-14` block, and it locates
the block through the engine's own `marker_pair` and `find_block` rather than by sniffing for a line.
That is deliberate beyond laziness: the standing ban this build has now tripped twice landed both
times in a test-side helper nobody thought to check, and an arm that defines nothing cannot trip it.

### Migration

None. No receipt field changes shape, and a receipt already carrying an `attributes` row with
`kit: "(govkit)"` is read by the new stage exactly as by the old one. A target whose rollback already
failed to restore its block is not repaired by this unit — nothing knows which those are — and the
repair is the operator's next `update --write`, which rewrites the block from the current pin set.

### Rollout

Lands directly and is reachable only inside a rollback that already happened. There is no flag: the
current behaviour is a restore that silently does not run, and a default-OFF gate over a fix for
"this does nothing" would be a gate over an absence.

### Alternatives rejected

- **Bind the entry to the kits whose `[[lf_pin]]` produced the block.** The block is one region
  rendered from many kits, so binding it to N kits means N restores of one file, each undoing the
  last. The review record that raised this offered it as one of two shapes; it is the one that needs
  an ordering rule the other does not.
- **Drop the entry from the snapshot and re-render the block on rollback.** Re-rendering produces the
  block for the CURRENT claimed set, which is what the run just wrote. The snapshot exists precisely
  because the pre-run bytes are not derivable.
- **Leave `orphan_kits` alone and let the line print.** It is a `NOT VERIFIED` line naming a kit that
  does not exist, on every run that rewrites the block. A durable false alarm on a correct run is how
  a verify report stops being read.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/selftest.py` | one arm group beside the `-14` rollback block |
| `WIRE-INTO-PROJECT.md` | one paragraph in the rollback-orders section |

rev-1 estimated `tools/govkit/govkit.py` and `tools/govkit/matrix.py`. Neither is touched: the engine
change was already landed by `-10`, and the arm went where its fixture builders already live rather
than into a file that would have had to grow a second copy of them.

## 5. Production-readiness checklist

- security — nothing here reaches production bytes: rev-2 ships no engine change. The property this
  unit ASSERTS about `-10`'s code is that the restore writes only paths the snapshot recorded,
  through the same index and worktree calls the per-kit loop already uses.
- perf / scale — the engine cost is `-10`'s and is one extra disjunct in a selection already being
  evaluated. This unit's own cost is one more scratch install and one more `update` in a suite that
  already builds several, paid only where that suite runs.
- error / empty / loading states — a run with no `attributes` entry skips the stage; a run that rolled
  nothing back never reaches it; a restore that git refuses takes the same failure reporting
  `DEPL-cMendedVintage-2` builds for the per-kit loop.
- observability — the restored path is reported in the same `restored` list the order prints, so the
  block appears in the rollback record rather than being restored silently.
- risks — the sharp one is the all-or-nothing rule: a run that rolls back one kit of six restores a
  block the other five still want. That is correct and it is also surprising, so §4 states it, the
  order names the path, and rev-2 puts it in the operator runbook. Second: the sweep's scope is an
  ORIGIN rather than an id, so a future synthetic id inherits the right answer instead of needing a
  new exclusion — which is why rev-2 records the landed shape as stronger than rev-1's.
- testing — AC1 through AC3 against scratch fixture targets. Gov keeps no `.governance/` receipt of
  its own, so no criterion here is observable against this repo.
- migration — none; §4 states why.
- user docs — `WIRE-INTO-PROJECT.md`'s rollback-orders section gains one paragraph: the pin block
  comes back with ANY kit's rollback, why, and what the operator does about a block restored out from
  under five kits that still wanted it.

## 6. Acceptance criteria

- **AC1** — *(rewritten at rev-2; rev-1 asserted the opposite of what shipped.)* When the fixture's
  snapshot entry for `.gitattributes` is read, its `kit` is `None` and the restore reaches it by
  `origin` rather than by that key — asserted through the two OBSERVABLE consequences, since the
  snapshot is a run-local structure no verb prints: the entry is restored (AC2) and it is not swept
  (AC3).
  Red when: the entry is attributed to any kit id at all, in which case one of the two arms below
  fires — a claimed id would make the sweep silent and the restore doubled, and an unclaimed one
  brings back the spurious line.
  fixture: a scratch target built under the run's scratch root by the real `apply`; this repo keeps
  no receipt of its own and can host no criterion in this section.
- **AC2** — When one kit's `[check]` is staged green-to-red on a fixture whose block this run
  rewrote, and `update --target <fixture> --write` rolls that kit back, the fixture's
  `.gitattributes` holds the bytes it held before the run.
  Red when: the restore selection is keyed on `x["kit"] == eid` alone, where no `eid` matches an
  unattributed entry, so the run reports a successful rollback with gov's new block still on disk.
- **AC3** — When that same run's output is read, no line matching `NOT VERIFIED` names a kit absent
  from the fixture's `install.json` claimed set.
  Red when: the sweep is not scoped by origin, in which case the unattributed entry is swept and the
  run prints a `NOT VERIFIED` line for `(no kit)` on every run that rewrites the block.
  figure: DERIVED — the claimed set is read from the fixture's receipt at observation time.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a second rollback fixture whose rolled-back kit declares an
`[[lf_pin]]`, asserting the returned bytes, the reported restore and the absent orphan line · no
assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-17 · **Written by the build pass, before its code, because rev-1's premise did not
  survive contact with the tree.** `-10` landed the repair one commit earlier by a different
  mechanism than rev-1 predicted, so S1, S2 and S3 are recorded DISCHARGED AT BASE with the shape
  actually in the tree, and the goal is re-stated as the one thing left: executing it. S4 moves from
  `tools/govkit/matrix.py` to `tools/govkit/selftest.py`, where the rollback fixture builders it
  needs already live — putting it in the matrix would have meant a second copy of them, and §12's
  build-once rule points the other way. AC1 is rewritten: it asserted a `kit` value that is the
  opposite of what shipped, and now asserts the unattributed entry through its two observable
  consequences. §3 gains a non-goal for a third consumer the fixture surfaced. §4's site table and
  inventory are replaced — no constant is minted and no `def` is added.
- rev-3 · 2026-09-17 · **The other half of rev-2's own amendment, named by the bug-class checklist
  after the commit.** `amendment-leaves-its-other-half-standing` was an anchored class on this diff
  and it had three live instances, all of them clauses that only made sense while rev-1's engine
  change was still this unit's to write: the §3 edge said this unit makes the rollback reachable,
  a non-goal described a restore stage that was never built, and §5's security and perf bullets
  priced an engine change rev-2 does not ship. All three now describe the landed code and say whose
  it is. Editorial: no criterion, scope item or gate moves.

- rev-4 · 2026-09-17 · §3 · RECIPROCAL EDGE, no scope or criterion changed. `TOOL-cMendedVintage-10`
  was adopted mid-build naming this unit, and the edge was never written back; hygiene check 12 reds
  on a handoff one author declared and the other never saw. The `hands-off external` bullet stays
  and is still true of the rollback stages it speaks about — the new edge is about this unit's
  dispatch record, which is a different subject.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "restore a snapshot entry whose kit key no rollback loop
selects"` returned no seam: its ranked rows are name-token neighbours on the stem `kit` — `kit_rel`
and `kit_dir` in the codebase-map kit, `parse_cell_key` in lexicon — none of which restores anything,
and it named `.sh` as an unscanned layer. So the seam is govkit's own and was read from source: the
per-kit restore block at `tools/govkit/govkit.py:7569` supplies the index-and-worktree calls this
stage reuses verbatim, and `origin` is already the field the landed branch at `:7627` discriminates
on, so the discriminator this unit needs exists rather than being minted. The recall probe returned
the record that owns the shape: the `DEPL-dSealedTally-1` round-1 spec audit found the sibling defect
in the same block — a per-entry tail running for every snapshot entry regardless of origin — which is
why this unit adds a stage rather than widening the loop.

Recall terms used: `--terms "govkit rollback snapshot attributes receipt row kit orphan restore
touched_kits claimed verify outcome regenerate"`, with the question "what decided how govkit rollback
selects snapshot entries by kit and what owns the synthetic attributes row".

**rev-2's own audit, over the thing rev-1 did not have to find: a fixture.** The reuse was read from
source rather than searched for, because the seam is one file over. `build_verify_gov`,
`build_verify_target` and `build_kit14` in `tools/govkit/selftest.py` already build a scratch gov
whose kit goes green-to-red across an `update`, and `build_kit14` already takes an `extra` parameter
that appends descriptor rows — so declaring an `[[lf_pin]]` on the rolled-back kit is a dict key, not
a builder. The matrix's shape 5 has no such fixture and no builder for one; putting the arm there
would have meant a second implementation of three functions that already exist, which is the
alternative §12 names by name. Nothing new was written, which is why §4's inventory is empty.
