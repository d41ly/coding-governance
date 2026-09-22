# Pre-wiring predicate run — TOOL-dRetiredFork-10

**Serves:** journal TOOL-dRetiredFork-10

S4 and §7 both require a candidate gate predicate to be run over the real tree BEFORE it is wired,
printing hits AND near-misses. This is that run. It did not confirm the design — it REFUTED it, and
that is recorded here rather than smoothed over.

## What was tested

The spec's S2 prescribed anchoring the population on a BASENAME rather than a rooted path prefix.
The candidate was therefore a `workflows/` basename anchor, run against the shipped
`^tools/.*\.js$` filter over gov's actual tree.

## The result

### every *.js git can see: 11

--- review-join
  OLD population (7):
    tools/hooks/scratch-guard.js
    tools/memory-recall/recall-opened.js
    tools/workflows/check-workflow-syntax.js
    tools/workflows/drift-audit-code.js
    tools/workflows/drift-audit-state.js
    tools/workflows/tier2-review.js
    tools/workflows/unattended-build.js
  NEW population (5):
    tools/workflows/check-workflow-syntax.js
    tools/workflows/drift-audit-code.js
    tools/workflows/drift-audit-state.js
    tools/workflows/tier2-review.js
    tools/workflows/unattended-build.js
  NEAR-MISS — in NEW, not in OLD (the widening risk §5 names):
  NEAR-MISS — in OLD, not in NEW (coverage lost):
    tools/hooks/scratch-guard.js
    tools/memory-recall/recall-opened.js

--- verifier-fanout
  OLD population (8):
    tools/hooks/agent-cap.js
    tools/hooks/scratch-guard.js
    tools/memory-recall/recall-opened.js
    tools/workflows/check-workflow-syntax.js
    tools/workflows/drift-audit-code.js
    tools/workflows/drift-audit-state.js
    tools/workflows/tier2-review.js
    tools/workflows/unattended-build.js
  NEW population (5):
    tools/workflows/check-workflow-syntax.js
    tools/workflows/drift-audit-code.js
    tools/workflows/drift-audit-state.js
    tools/workflows/tier2-review.js
    tools/workflows/unattended-build.js
  NEAR-MISS — in NEW, not in OLD (the widening risk §5 names):
  NEAR-MISS — in OLD, not in NEW (coverage lost):
    tools/hooks/agent-cap.js
    tools/hooks/scratch-guard.js
    tools/memory-recall/recall-opened.js

--- what a BLANKET filter-deletion would have admitted (the §3 refutation, re-measured):
    .claude/hooks/agent-cap.js
    .claude/hooks/recall-opened.js
    .claude/hooks/scratch-guard.js

## The verdict

A basename anchor on `workflows/` **narrows** review-join's population from 7 files to 5, dropping
`tools/hooks/scratch-guard.js` and `tools/memory-recall/recall-opened.js`. AC5 requires the
population stay at 7, so S2's mechanism and AC5 cannot both hold.

§5 named the risk as WIDENING — "a basename anchor is wider than a path prefix and may admit a file
the prefix excluded" — and set this run up to catch exactly that. It caught the opposite. The
near-miss columns are empty in the widening direction and hold two files in the losing direction.

**Nothing was admitted that the prefix excluded.** The widening risk §5 anticipated is measured at
zero for both gates, which is worth stating plainly: had this run only checked for the anticipated
failure, it would have come back clean and the design would have shipped two files short.

## What was built instead

A DERIVED prefix — `git rev-parse --show-prefix` from the script's own directory — reproduces the
7-file population exactly while spelling no literal. Parked as a decision the owner has not seen,
because the owner ratified S2 as written and this measurement contradicts it.

The last block above re-measures the §3 refutation as a by-product: deleting the filter outright
admits three `.claude/hooks/` files, one of which is the agent-cap hook whose own ban table trips
the predicate. That refutation still holds.
