# TOOL-aWeldedTribunal-4 — acceptance ledger

**Serves:** journal TOOL-aWeldedTribunal-4

## What changed

A `RUN INTEGRITY` block in the synthesis prompt of `tools/workflows/tier2-review.js`, carrying the
eight counters the harness already computed and logged to stdout, plus the two sentences that make
them do work. And a refresh of `memory/gotchas/degradation-known-but-unreported.md`, which is the
left-shift the owner ruling allows.

## Each criterion, answered

- **AC1** — every counter in the spec's §4 inventory is interpolated into the block: `lensesDead`,
  `liveResults.length`, `LENSES.length`, `skepticsDead`, `batches.length`, `conflicts.size`,
  `spurious`, `duplicates`. Checked by extracting the block and testing for each. The criterion also
  covers the block's TEXT, and both sentences are present: the do-not-describe-this-run-as-complete
  instruction and the a-zero-is-not-evidence-of-absence clause.
- **AC2** — the observation that the block reaches the RECORD and not only the source is owed by
  this build's own closing review, which runs this harness. **Not yet observed at the time this
  ledger was written**; the closing review is the run that answers it, and this line says so rather
  than claiming it.
- **AC3** — `memory/gotchas/degradation-known-but-unreported.md` now names
  `tools/workflows/tier2-review.js` as a CLOSED instance, names the counter set, explains why
  `conflicts` is in it and `downgrades` is not, and carries the DoD line.
- **AC4** — `node tools/workflows/check-workflow-syntax.js`: `4 workflow script(s) parsed clean`,
  exit 0.
- **AC5** — the `workflow script syntax` leg is `subject = repo`, so the plain bar runs it; green.
  The `tier2-review self-test` leg guards on `tools/workflows/` and is `subject = kit`, so it is owed
  under `GATE_FULL=1 GATE_SELFTESTS=1` and runs at the push boundary.

## What no gate here can check, stated

`memory/DECISIONS.md:116` refused a scanner for this class, and the reasoning holds: a rule that
every returned counter must appear in a prompt string is satisfied by a comment. So AC1 is a
documented check performed by reading the block, and the left-shift is the record. What the record
buys is that the next harness's author is told what the block is FOR, rather than which variables it
happens to hold.

## Evidence

**Evidences:** TOOL-aWeldedTribunal-4
- AC1 — `tools/workflows/tier2-review.js` — the synthesis prompt interpolates all eight counters of the section 4 inventory, and carries both instruction sentences
- AC2 — `memory/builds/aWeldedTribunal/reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md` — the block reached a real record: that report and its three successors each carry a RUN INTEGRITY section with the counters
- AC3 — `memory/gotchas/degradation-known-but-unreported.md` — names this harness as a closed instance, the counter set, and the DoD line
- AC4 — `node tools/workflows/check-workflow-syntax.js` — 4 workflow scripts parsed clean, exit 0
- AC5 — `bash tools/run-gates/run-gates.sh` — the `workflow script syntax` leg is green on the full bar
