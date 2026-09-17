# DEPL-cMendedVintage-17 — a target whose pins were withdrawn never reaches the empty-marker write

**Status:** CLOSED · rev-4 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-17-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-17-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-17-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-17-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The `pins` arm at `tools/govkit/govkit.py:6386` sets `_om, _cm, _text = ("", "", "")` when the
recomputed pin set is empty, leaves `_span` at `None`, and therefore evaluates `v` to `pins-moved`.
It does not skip. Once `DEPL-cMendedVintage-10` puts a write under that verdict, a target that HAD
pins and whose claimed kits now declare none calls `write_block(cur, "", "", "", "append")` on every
run, and `find_block`'s marker test matches every blank line in the file. Gate the write on a
non-empty pin set and give the withdrawal state its own verdict.

## 2. Scope (IN)

- **S1** The `pins` arm reports a distinct verdict when `_pins` is empty and the target's receipt
  carries an `attributes` row — the pin set was withdrawn, not merely absent — instead of folding that
  state into `pins-moved`. Observed by AC1.
- **S2** `DEPL-cMendedVintage-10`'s write stage runs only for a non-empty recomputed pin set, so the
  empty-marker `write_block` call is unreachable rather than merely unlikely. Observed by AC2.
- **S3** The withdrawal verdict's remedy is the removal of gov's own block: under `--write` the run
  deletes the marked region it previously wrote, leaving the rest of the target's `.gitattributes`
  untouched, and drops the `attributes` receipt row. A block gov wrote for a claim it no longer makes
  is gov's to withdraw. Observed by AC3, and by AC5 on the shape BASE completes at exit 0 over.
- **S4** A target that never declared a pin keeps BASE behaviour exactly: no `attributes` row, no
  verdict, no write. `DEPL-cMendedVintage-10` §8 Q2 reasons about that case and this unit does not
  move it. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `find_block`. Its marker test matching a blank line is a real sharp edge, and it is
  reachable only through a call this unit makes unreachable; hardening a parser against a call that
  no longer exists is work with no observer.
- No withdrawal of a block gov did not write. The receipt's `attributes` row is what says gov owns
  the region; a target with a hand-written `.gitattributes` and no such row is not touched.
- No renormalize on the withdrawal path. `git add --renormalize` after removing a pin would rewrite
  index blobs for a population the target no longer pins, which is a data change nobody asked for.
- No change to `lf_pins` or `lf_pin_block`. The recomputation is correct; what is wrong is the verdict
  the empty result takes.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — that unit introduces the write this unit gates and the
  receipt row this unit's withdrawal path drops. Without it the empty-marker call does not exist and
  this unit has nothing to close.
- **hands-off** `DEPL-cMendedVintage-11` — that unit grades the attributes row's block on `check`. A
  target whose row this unit drops must not then read as a missing block, which is why S3 drops the
  row and the region together rather than either alone.
- **consumes-from** `TOOL-cMendedVintage-10` — that unit's repair is what let this one DECLARE
  `tools/govkit/govkit.py` at all. Until it landed, check 49 refused the declaration on a superseded
  sibling row that could never close. It changes no code this unit reads; what it supplies is the
  ability to start.

## 4. Design

### The reachable population, stated precisely

The state needs all three of: an `attributes` row in the receipt, which only `apply` synthesizes and
only `if pins:` (`tools/govkit/govkit.py:4620`); a claimed set that now declares no `[[lf_pin]]`; and
a run that reaches the `pins` arm. The middle term is the one that happens — a kit dropped from
`receipt["kits"]`, or a kit whose descriptor retired its pin between vintages. It is not
hypothetical and it is not common, which is why it survived both the spec and its first review.

The three outcomes of the shipped call, MEASURED at build time on this unit's own fixture rather
than reasoned about. rev-1's table was wrong in two of its three rows, and the correction makes the
defect worse in the common shape rather than milder.

The term rev-1 missed: a `.gitattributes` that `write_block` produced always ends in a newline, so
`text.split("\n")` always yields a trailing empty field. Every such file already holds ONE blank
line before the target adds any of its own.

| the target's `.gitattributes` holds | `write_block(cur, "", "", "", "append")` does |
|---|---|
| a trailing newline and no other blank line | `find_block` returns that one trailing blank line; the splice replaces it with the empty block's single empty line, so THE FILE IS BYTE-IDENTICAL and the run exits 0 — while the receipt's `attributes` row is rewritten to `mode: spliced`, `patterns: []` and the sha256 of the empty string, and gov's real block stays on disk claimed by nothing |
| a trailing newline and any further blank line | raises `expected exactly one marker pair, found 2 open and 2 close`, mid-run, after the verdict table and after the snapshot; exit 2, and the receipt is not re-stamped |
| no trailing newline at all | appends one blank line; unreachable through any file `apply` or `update` wrote, because both end their write with a newline |

So the red is not bytes landing at an arbitrary blank line. The splice really does fire at an
arbitrary blank line, and because an empty block renders as exactly one empty line, the bytes it
lands there are the bytes already there. What is destroyed is the RECEIPT: a target with an ordinary
`.gitattributes` has its `attributes` row silently rewritten to claim a block that is not there, on
every run, at exit 0. A target whose `.gitattributes` carries one blank line of its own — the shape
a hand-maintained one almost always has — has its update aborted mid-write instead, on every run.

### The verdict, and why a fourth one

`pins-moved` means "gov's block differs from what gov would write now, and `--write` will fix it".
That sentence is false of a withdrawal, where what gov would write now is nothing. A verdict shared
by two states with opposite remedies is the ambiguity the descriptors' outcome probes exist to
resolve, one layer up. The new verdict prints its own line, is counted in its own `tally` slot, and
its read-only preview says the block will be REMOVED rather than rewritten.

### Inventory

| identifier | kind | where |
|---|---|---|
| `pins-withdrawn` | verdict token | `tools/govkit/govkit.py`, the `tally` the `pins` arm writes and the summary that reads it |

No function, flag or file is minted. The token follows the existing `pins-moved` spelling — a noun
then a past participle, hyphenated — rather than introducing a second shape for a sibling verdict.

### Migration

None on disk for any target that pins nothing today. A target in the withdrawal state gets one write
on its next `update --write`, which removes the region and the row; afterwards it is a target with no
`attributes` row, which is the state a target that never pinned is already in. The transition is
one-way and it is the correct direction.

### Rollout

Lands with `DEPL-cMendedVintage-10` and inside the same build, so no adopter ever sees the write stage
without this gate. That sequencing is the whole rollout plan: there is no flag, because the state this
unit closes is one the write stage creates and the two are never separately shipped.

### Alternatives rejected

- **Skip the arm when `_pins` is empty.** The clause in `DEPL-cMendedVintage-10` §5 asserts this is
  what already happens, and it is the sentence the spec audit found false. Making it true by skipping
  leaves gov's stale block on disk forever with nothing reporting it, which trades a raise for a
  silence.
- **Write the block with the markers and an empty body.** An empty marked region is a claim gov is
  not making, and `check` would then grade an empty block as current, which is a green over a
  withdrawal.
- **Refuse the run and tell the operator to run `apply`.** `apply` is the verb this build exists to
  stop recommending, and the remedy is a deletion gov can perform safely on a region it owns.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the verdict, the write gate, the withdrawal path, the summary line |
| `tools/govkit/selftest.py` | the arms §7 names |
| `tools/govkit/refusal_join.py` | nothing, unless the build-time reading finds the `find_block` refusal loses its only caller |

## 5. Production-readiness checklist

- security — the withdrawal deletes only the region between gov's own markers, located by the same
  `find_block` the write uses. Nothing outside that region is read or rewritten.
- perf / scale — one additional emptiness test per run.
- error / empty / loading states — this unit IS the empty-state work. A target with no
  `.gitattributes` and an `attributes` row takes the withdrawal path as a row drop with no file edit;
  a target whose markers are already gone drops the row and reports that it found nothing to remove.
- observability — the new verdict prints its own line naming the count of pins that went away, and
  the read-only preview says REMOVED rather than rewritten, so an operator is never told a rewrite is
  coming when a deletion is.
- risks — the sharp one is S3's deletion: it is the first path on which `update` removes bytes from a
  file the target owns. It is contained to the marked region and it is gated on the receipt row, so
  gov removes only what gov's own record says gov wrote. Second: a target mid-way through dropping
  kits sees the withdrawal and then, on re-adding the kit, a fresh `apply`-style write — which is
  correct and is stated so it is not read as churn.
- testing — AC1 through AC5 against scratch fixture targets. Gov keeps no receipt of its own, so no
  criterion here is observable against this repo.
- migration — §4; one-way and self-completing.
- user docs — `WIRE-INTO-PROJECT.md`'s pin section gains one sentence on what happens when the last
  pinning kit leaves a target.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target holds an `attributes` receipt row and its claimed kits are
  edited to declare no `[[lf_pin]]`, `python tools/govkit/govkit.py update --target <fixture>` reports
  the withdrawal verdict and not `pins-moved`.
  Red when: the empty pin set keeps falling through to `pins-moved`, which is BASE behaviour and the
  state the write stage then acts on.
  fixture: a scratch fixture target under the run's scratch root built with `intake` then `apply`;
  this repo keeps no `.governance/` receipt and can host no criterion in this section.
- **AC2** — When that fixture's `.gitattributes` is given a blank line of the target's own outside
  gov's block — which with the file's own trailing newline makes the two blank lines BASE refuses on
  — and `python tools/govkit/govkit.py update --target <fixture> --write` runs, the run completes and
  no "expected exactly one marker pair" refusal is raised.
  Red when: the write stage is gated on the verdict name rather than on the recomputed pin set, so a
  later verdict rename reopens the empty-marker call.
- **AC3** — When that same `--write` run finishes, gov's marked region is gone from the fixture's
  `.gitattributes`, every line outside it is byte-identical to before the run, and the receipt carries
  no `attributes` row.
  Red when: the region is removed and the row is left, so the next `check` grades a block that is not
  there.
- **AC4** — When `python tools/govkit/govkit.py update --target <fixture> --write` runs against a
  fixture that never declared a pin, the run writes no `.gitattributes`, reports no pin verdict, and
  the file is byte-identical afterwards.
  Red when: the withdrawal path is keyed on the empty pin set alone rather than on the pin set AND
  the receipt row, which makes every unpinned target take a removal path on every run.
- **AC5** — When the withdrawal fixture's `.gitattributes` carries NO blank line of the target's own,
  which is the shape BASE completes at exit 0 over, the same `--write` run leaves no `attributes` row
  in the receipt and removes gov's marked region; the receipt never records a `patterns` list that is
  empty.
  Red when: only the refusing shape is graded. BASE exits 0 on this one and rewrites the row to claim
  the sha256 of the empty string, so a suite that watches exit codes alone reports this target clean
  while its receipt describes a block that is not on disk.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arms: `tools/govkit/selftest.py` · TWO fixture targets whose `attributes` row survives a claimed
set that declares no pin — one carrying a blank line of its own outside gov's block, which is the
shape BASE refuses on, and one carrying none, which is the shape BASE completes at exit 0 over —
each asserted to complete, to leave the surrounding lines untouched, and to end with no `attributes`
row · plus a never-pinned fixture for AC4 · no assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-17 · §4's outcome table replaced by MEASUREMENT. Two of its three rows were wrong:
  the one-blank-line row is byte-identical rather than a splice of foreign bytes, because an empty
  block renders as one empty line over one empty line — what it destroys is the receipt row, at exit
  0; and the no-blank-line row is unreachable, because every writer ends the file with a newline and
  the trailing empty field is itself a blank line. AC2 reworded to name the blank line the target
  supplies rather than a count the trailing newline already half-fills, and AC5 added for the
  exit-0 shape, which is the one that ships silently and which a suite watching exit codes misses.
- rev-3 · 2026-09-17 · rev-2's amendment stops leaving its other half standing. §7's new-arm line
  still asked for "two blank lines planted outside gov's block", which is the wording AC2 had just
  been corrected away from; §5's testing line still counted to AC4; and S3 named no observer for the
  new criterion. No design moved — three sentences that only made sense under the old wording.

- rev-4 · 2026-09-17 · §3 · RECIPROCAL EDGE, no scope or criterion changed. `TOOL-cMendedVintage-10`
  declares a `hands-off` to this unit and this unit declared nothing back; hygiene check 12 reds on a
  handoff one author declared and the other never saw. The edge became a fact when that unit was
  adopted, so recording it completes the record rather than changing the design.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "restore a snapshot entry whose kit key no rollback loop
selects"` was the probe run for this promoted set; it returned no seam, ranked only name-token
neighbours on the stems `kit` and `key`, and named `.sh` as an unscanned layer. The seam this unit
extends was read from source instead: `write_block` and `find_block` in `tools/govkit/govkit.py`
already carry a removal-shaped path — `find_block` returns the inclusive line span of the marked
region, which is exactly what a deletion needs and which the shipped `pins` arm at `:6396` already
computes for its comparison. So S3 removes a region with the locator the arm already built, and
mints no traversal of its own. The recall probe returned `DEPL-cMendedVintage-10`'s own §10, which
records `DEPL-dSettledRoster-1` as the open owner-reserved fork over where gov's block sits; this unit
deletes a region in place and never moves one, so that fork is untouched.

Recall terms used: `--terms "govkit rollback snapshot attributes receipt row kit orphan restore
touched_kits claimed verify outcome regenerate"`, with the question "what decided how govkit rollback
selects snapshot entries by kit and what owns the synthetic attributes row".
