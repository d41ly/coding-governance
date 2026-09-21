# cMendedVintage — the acceptance ledger for unit 11

**Serves:** journal DEPL-cMendedVintage-11

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real engine against
scratch fixture targets at the shell — once against the pre-change binary and once after — so every
criterion here is answered by a fixture and none by a suite.*

## The one thing worth reading twice

**The defect is live and it was reproduced before a line was written.** A fixture target installed
with a kit declaring an `[[lf_pin]]`, then stripped of gov's whole marked region from its
`.gitattributes`, exited 0 from `check` with no finding anywhere in its output. The receipt still
claimed the block. Nothing graded the claim, because the drift loop opened by skipping every row
whose role was not `merged`.

**The spec was right that this is a one-line gate and not a new comparator**, and that was checked
rather than assumed: the digest `apply` records is taken over the marker-inclusive text
`lf_pin_block` returns, and the loop's extractor slices the same marker-inclusive span and hashes it
after stripping CR. The two agree with no second normalization written anywhere, which is why the
change is a gate, two counters and a guard.

**Six things the spec asked for were measured wrong and are amended at rev-3**, each logged on its
own §9 line. The two worth naming here are the ones that would have shipped a red arm. S4 asked for
the role in the DRIFT message; inserting it before the block id flips
`DRIFT: gov block 'govkit:branch-guard'`
which a shipped arm asserts verbatim, so the role rides after the id instead. And AC1 asked for a
fixture built from "a kit declaring an `[[lf_pin]]`" and for the verb to exit 0 — the obvious
selection, `memory-recall`, drags in `memory-tree`, whose three undischarged holes make `check` exit
1 for reasons that have nothing to do with a pin block, so the criterion was unanswerable on it. The
fixture selects `run-gates` instead: no dependency, no hole, three pins.

**The guard the spec scoped to one role is role-blind in the code.** A `merged` row carrying no
`block_sha256` had exactly the same false-accusation failure, printing `expected None` against a
target that tampered with nothing. One guard above the role branch is the same line count as one
below it and leaves no sibling caller broken.

**The brief's prediction about `DEPL-cMendedVintage-17` holds, measured.** A target whose pins that
unit withdraws leaves no `attributes` row in the receipt and no marked region in the file, so this
loop has nothing to grade and reports nothing. The two halves agree. The fixture takes the second of
the two shapes that unit dispatches on — a kit dropped from the receipt's `kits` — which needs no
second gov vintage.

**One finding about a landed verb, and it is CLEARABLE.** `adopt` over a target that holds no gov
block synthesizes an `attributes` row whose digest is gov's RECOMPUTED block, so under this change
that target now reds `REMOVED` where it silently exited 0 before. That is the truthful verdict — the
block really is absent — and the remedy exists: `update --write` classifies the same row
`pins-moved` and writes the block back, after which `check` exits 0. Measured end to end. It is the
§3 ordering promise arriving through `adopt` rather than through an edit, and it needs no repair
here.

**Evidences:** DEPL-cMendedVintage-11

*Every token below sits on its own bullet's FIRST physical line, deliberately: hygiene check 23
joins an answer's backticked tokens to the criterion's per PHYSICAL line, so a token pushed onto a
continuation belongs to no line and its criterion grades as answered by nothing.*

- AC1 — OBSERVED — `python tools/govkit/govkit.py check --target <fixture>` — an untouched fixture
  exits 0 and prints the new note reporting the pin block intact. `[[lf_pin]]` is what the fixture's
  selection declares. AMENDED rev-3 for the selection, logged at §9: the criterion's
  own kit could not answer its own exit code. RED-WHEN asserted positively rather than left as
  prose — an edit appended OUTSIDE the marker pair is not drift and the target still reads intact,
  which is what distinguishes a span extractor from one handed the whole file.
- AC2 — OBSERVED — `govkit:lf-pins` — one line edited strictly BETWEEN the markers fails the verb,
  names the block and the file, and the DRIFT line names the role that spoke. Deleting the whole
  region fails with the REMOVED wording and no DRIFT. The tamper-after-the-close-marker shape is
  asserted as its own arm, going the other way: the block is byte-identical there and intact is the
  right answer, which is why the failing arm tampers inside the pair. AMENDED rev-3 for where the
  role rides in the message.
- AC3 — OBSERVED — `block_sha256` — a receipt whose row has the key REMOVED is reported ungradeable
  by name and the run exits 0. The RED-WHEN is asserted as its own arm: a row whose digest is
  present and EMPTY is still graded and still reds, so the guard is testing the key and not the
  value. AMENDED rev-3: an ungradeable row leaves the graded population rather than standing at
  `0/1`.
- AC4 — OBSERVED — `merged blocks: 1/1 intact` — a fixture carrying both roles prints that string
  unchanged beside the separate pin-block note, and `merged blocks: 2/2` appears nowhere. Measured a
  second time on a target shaped like the suite's own merged-block fixture, which turns out to carry
  an `attributes` row too, so the false `2/2` sentence was reachable by the shipped arms and is not.
  figure: DERIVED from the run's own output.

## OWED

- **The gate-side encoding of AC1 through AC4.** Sixteen `[-11]` arms landed in this unit's write
  set and only the govkit self-test suite can execute them. That suite is a merge-bar leg and no
  gate, suite or bar ran in this pass. They are NOT asserted by construction: the block's own source
  was extracted from the shipped file verbatim, dedented, and executed against stubs for the five
  names the suite supplies, and all sixteen passed. What is owed is the suite RUN — that the block
  still passes in the suite's own scope, with the suite's own `tmp`, and that the three sibling arms
  it sits beside are still green. Owed to the bar the main loop runs once every unit is terminal.
- **The three shipped arms this change could have flipped were measured directly, not owed.** A
  target installed with the kit those arms use carries an `attributes` row alongside its `merged`
  one, so the shared-counter hazard was live. Under the change the outside-edit arm still finds
  `merged blocks:` with no DRIFT, the inside-edit arm still finds
  `DRIFT: gov block 'govkit:branch-guard'`
  and the marker-deletion arm still finds `REMOVED`.
- **No other unit's owed criterion is discharged here.** The `DEPL-cMendedVintage-17` edge was
  measured, but it is this unit's own §3 edge rather than one of that unit's criteria, and it
  agreed.
