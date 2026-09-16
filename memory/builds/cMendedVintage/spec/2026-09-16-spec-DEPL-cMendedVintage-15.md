# DEPL-cMendedVintage-15 — the synthesized attributes entry is restorable, and no orphan line names it

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 25

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`apply` stamps the `.gitattributes` receipt row with the synthetic kit id `(govkit)`
(`tools/govkit/govkit.py:4626` and `:8246`), which no registry entry claims. Both consumers of a
snapshot entry's `kit` key reject that value: the restore loop selects
`[x for x in snap_rows if x["kit"] == eid]` inside `for eid in touched_kits` over claimed ids
(`tools/govkit/govkit.py:7504` and `:7569`), and `orphan_kits` (`:6730`) sweeps every snapshot entry
whose kit is not in `claimed`. Give the entry a restore stage that reaches it, and take it out of the
orphan sweep.

## 2. Scope (IN)

- **S1** The snapshot entry `DEPL-cMendedVintage-10` S2 takes for `.gitattributes` carries
  `kit = "(govkit)"` explicitly, spelled at the site that builds it rather than inherited from a
  neighbouring row, so the entry agrees with the receipt row `apply` writes at
  `tools/govkit/govkit.py:4626`. Observed by AC1.
- **S2** The rollback pass gains one kit-independent restore stage over snapshot entries whose
  `origin` is `"attributes"`, placed after the `for eid in touched_kits` loop and reached whenever
  that loop rolled any kit back. It performs the same index-and-worktree restore the per-kit loop
  performs and reports under the same three lists. Observed by AC2.
- **S3** `orphan_kits` at `tools/govkit/govkit.py:6730` excludes the synthetic id, so a run that
  rewrote the pin block prints no `verify (govkit): NOT VERIFIED` line at `:7714`. The exclusion is
  written against the one synthetic id this engine mints and refuses to generalise to "any id with
  parentheses". Observed by AC3.
- **S4** `tools/govkit/matrix.py` shape 5 gains one arm over a target with a written pin block and one
  kit staged to fail verify, asserting both halves at once: the pre-run `.gitattributes` bytes return,
  and the run's output carries no `NOT VERIFIED` line naming a kit the registry does not claim.
  Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- No change to what `apply` stamps. `(govkit)` is the id two write sites already spell and a receipt
  already on disk carries it; renaming it would be a receipt migration for a string.
- No generalised synthetic-id namespace, no `kit` sentinel table, no `is_synthetic` predicate. One id
  exists, one exclusion closes it, and a namespace invented for a population of one is plumbing.
- No restore of an `attributes` entry on a run that rolled nothing back. The stage is reached from
  inside the rollback pass, so a clean run never enters it.
- No change to the `pins` classification arm, to `lf_pin_block`, or to where gov's block sits in the
  target's file. Those are `DEPL-cMendedVintage-10`'s and `DEPL-dSettledRoster-1`'s.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — that unit creates the snapshot entry and the write
  whose rollback this unit makes reachable. Without it there is no entry to restore and no run that
  rewrites the block, so this unit has no subject.
- **hands-off** external — nothing else in this build reads the rollback pass's per-origin stages.

## 4. Design

### Why the per-kit loop cannot be widened instead

The obvious smaller edit is to add `(govkit)` to `touched_kits`. It is wrong for a reason worth
writing down: every consumer of that list treats a member as a CLAIMED kit. `:7722` computes
`not_run = [e for e in claimed if e not in touched_kits]`, the baseline loop at `:7504` demands a
baseline per member and refuses when one is missing (`:7515`), and the verify pass runs each member's
`[check]`. A synthetic id has no descriptor, no baseline and no check, so widening the list buys one
restore and three new refusals. The second stage is the smaller change to the code that has to be
correct.

### The stage, and where it sits

| # | site | what it does |
|---|---|---|
| 1 | `for eid in touched_kits` at `tools/govkit/govkit.py:7504` | the per-kit restore, unchanged |
| 2 | immediately after that loop | the `origin == "attributes"` restore, run when the loop rolled anything back |
| 3 | `orphan_kits` at `:6730` | the synthetic id filtered out of the population it builds |

Site 2 is after site 1 because the decision to roll back is the per-kit loop's, and the attributes
block is not any one kit's: it is rendered from every claimed kit's `[[lf_pin]]`, so restoring it for
one rolled-back kit and not another is not a state that exists. The rule is therefore all-or-nothing
and it is stated rather than derived — a run that rolled ANY kit back puts the block back, because
the block gov wrote describes a claimed set the run no longer stands behind.

### Inventory

| identifier | kind | where |
|---|---|---|
| `_attr_snap` | local list in `_cmd_update` | the `origin == "attributes"` entries, beside `snap_rows` |
| `SYNTHETIC_KIT` | module-level constant | `tools/govkit/govkit.py`, the one id `apply` stamps, read by `:4626`, `:6730` and `:8246` |

`SYNTHETIC_KIT` is minted rather than left as three string literals because the exclusion in S3 and
the two write sites must agree, and three copies of a sentinel is how they stop agreeing. The
lexicon cell for a module-level Python constant is `py.const`, which declares `UPPER` and no verb
table.

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
| `tools/govkit/govkit.py` | the constant, the explicit `kit` on the snapshot entry, the second restore stage, the orphan filter |
| `tools/govkit/matrix.py` | one shape-5 arm |

## 5. Production-readiness checklist

- security — the restore writes only paths the snapshot recorded, through the same index and
  worktree calls the per-kit loop already uses. No new path class and no target-supplied value.
- perf / scale — one extra list comprehension per run and, on a rollback only, one `update-index`
  plus one `checkout-index` for a single path.
- error / empty / loading states — a run with no `attributes` entry skips the stage; a run that rolled
  nothing back never reaches it; a restore that git refuses takes the same failure reporting
  `DEPL-cMendedVintage-2` builds for the per-kit loop.
- observability — the restored path is reported in the same `restored` list the order prints, so the
  block appears in the rollback record rather than being restored silently.
- risks — the sharp one is the all-or-nothing rule: a run that rolls back one kit of six restores a
  block the other five still want. That is correct and it is also surprising, so §4 states it and the
  order names the path. Second: a future second synthetic id would need its own decision, which is
  why S3 refuses to generalise the filter.
- testing — AC1 through AC3 against scratch fixture targets. Gov keeps no `.governance/` receipt of
  its own, so no criterion here is observable against this repo.
- migration — none; §4 states why.
- user docs — `WIRE-INTO-PROJECT.md`'s rollback paragraph gains one sentence saying the pin block
  comes back with any rollback.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target with a written pin block is taken through
  `python tools/govkit/govkit.py update --target <fixture> --write` and the run's snapshot is read,
  the `.gitattributes` entry carries `kit` equal to the value the receipt row at
  `tools/govkit/govkit.py:4626` spells.
  Red when: the entry is built with whatever `kit` the enclosing row carries, so the snapshot and the
  receipt disagree and the new stage selects nothing.
  fixture: a scratch fixture target built under the run's scratch root with `intake` then `apply`;
  this repo carries no receipt of its own and can host no criterion in this section.
- **AC2** — When one kit's `[check]` is staged green-to-red on that fixture and
  `python tools/govkit/govkit.py update --target <fixture> --write` rolls it back, the fixture's
  `.gitattributes` holds the bytes it held before the run.
  Red when: the restore is left inside the per-kit loop, where no `eid` equals the synthetic id, so
  the run reports a successful rollback with gov's new block still on disk.
- **AC3** — When that same run's output is read, no line matching `NOT VERIFIED` names a kit absent
  from the fixture's `install.json` claimed set.
  Red when: the orphan filter is written against the literal parentheses rather than against the
  minted constant, so a later rename of the synthetic id restores the spurious line.
  figure: DERIVED — the claimed set is read from the fixture's receipt at observation time.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/matrix.py` · a shape-5 target with a written pin block and one kit staged to
fail verify, asserting both the returned bytes and the absent orphan line · no assertion floor to
move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

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
