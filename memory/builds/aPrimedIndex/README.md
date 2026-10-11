---
slug: aPrimedIndex
node: a
opened: 2026-10-11
streams: tooling
status: INPROGRESS
roster: TOOL
ids: TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4
authorized-by: prompt
---

# aPrimedIndex — no bar starts over a stale generated index

## The problem this build exists to solve

The merge bar grades generated outputs for freshness: the build index (`memory/LIVE.md`, the ledger
and backlog views, the README and spec regions), the gotchas `INDEX.md`, the codebase map, and the
Skills and guides the kits render. Nothing regenerates them before a bar starts, so a session learns
of a stale one when a leg reds an hour in, then regenerates and runs the whole bar again. The
lander's reconcile merge leaves the `merge=ours` indexes stale too. The owner's prose is the
mandate, recorded under [prompts/](prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1.md).

## Expected improvements

- A bar over a stale output refuses before its first leg, naming each stale output and the one
  command that regenerates them all.
- One command regenerates every declared output in dependency order.
- The lander lands the outputs its merge left stale inside that merge.

## Detriments if this is not built

- Bars keep reding an hour in on a stale index and restarting from scratch.
- Every reconciled landing keeps handing the push bar a stale `merge=ours` index.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, authored this run, one mechanism each.
- Order 1, 2, then 3 and 4. Units 3 and 4 write disjoint files but both call unit 2's verb, which is
  their contract, so this inline run sequences them.
- The bar stays read-only on the tree it grades: it refuses and names the remedy, and never
  regenerates in place. The lander, which already writes over its merge, regenerates.
- Ratchets, minted version carriers and node-local evidence are not regenerated: they are not
  derived from the tree alone. Unit 1's spec names each one.
- Kit versions are minted by the lander; no unit bumps one by hand.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aPrimedIndex-1` | OPEN | every generated output a bar leg grades declares its write and check commands in its kit's descriptor |
| 2 | `TOOL-aPrimedIndex-2` | OPEN | one runner verb rewrites every declared output in stage order, and a second names each stale one |
| 3 | `TOOL-aPrimedIndex-3` | OPEN | the runner refuses to start a bar while a declared output is stale, before it queues for the host |
| 4 | `TOOL-aPrimedIndex-4` | OPEN | the lander regenerates the declared outputs over its merged tree and lands them with the merge |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 0 unit(s) · node a · opened 2026-10-11 · streams tooling
ids TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
