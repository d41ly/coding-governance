---
slug: aPrimedIndex
node: a
opened: 2026-10-11
streams: tooling+deployer
roster: TOOL+DEPL
ids: DEPL-aPrimedIndex-1 TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 TOOL-aPrimedIndex-5 TOOL-aPrimedIndex-6 TOOL-aPrimedIndex-7 TOOL-aPrimedIndex-8 TOOL-aPrimedIndex-9 TOOL-aPrimedIndex-10
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
- Units 5 to 8 are closing review r1's promotions (M4): one per HIGH, and the minors in two batches
  over disjoint write sets. All four write disjoint files, and the inline author sequences them.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aPrimedIndex-1` | every generated output a bar leg grades declares its write and check commands in its kit's descriptor |
| 2 | `TOOL-aPrimedIndex-2` | one runner verb rewrites every declared output in stage order, and a second names each stale one |
| 3 | `TOOL-aPrimedIndex-3` | the runner refuses to start a bar while a declared output is stale, before it queues for the host |
| 4 | `TOOL-aPrimedIndex-4` | the lander regenerates the declared outputs over its merged tree and lands them with the merge |
| 5 | `DEPL-aPrimedIndex-1` | govkit's verdict reader runs the target's runner with its generated-output preflight skipped |
| 6 | `TOOL-aPrimedIndex-6` | the pre-push hook scrubs the preflight's skip knob from every bar it runs |
| 7 | `TOOL-aPrimedIndex-7` | the regen verb's and the runner's review minors, batched |
| 8 | `TOOL-aPrimedIndex-8` | the lander's review minors, batched, and the fixture that names a unit |
| 9 | `TOOL-aPrimedIndex-9` | the lexicon render proves freshness alone |
| 10 | `TOOL-aPrimedIndex-10` | the in-place landing checks the allow record against what it pushed |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 10 unit(s) · node a · opened 2026-10-11 · streams tooling+deployer
ids DEPL-aPrimedIndex-1 TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 TOOL-aPrimedIndex-5 TOOL-aPrimedIndex-6 TOOL-aPrimedIndex-7 TOOL-aPrimedIndex-8 TOOL-aPrimedIndex-9 TOOL-aPrimedIndex-10

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPrimedIndex-1 — every generated output a bar leg grades declares its write and check commands in its kit's descriptor](spec/2026-10-11-spec-TOOL-aPrimedIndex-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPrimedIndex-2 — one runner verb rewrites every declared output in stage order, and a second names each stale one](spec/2026-10-11-spec-TOOL-aPrimedIndex-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aPrimedIndex-3 — the runner refuses to start a bar while a declared output is stale, before it queues for the host](spec/2026-10-11-spec-TOOL-aPrimedIndex-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aPrimedIndex-4 — the lander regenerates the declared outputs over its merged tree and lands them with the merge](spec/2026-10-11-spec-TOOL-aPrimedIndex-4.md) | 3 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [DEPL-aPrimedIndex-1 — govkit's verdict reader runs the target's runner with its generated-output preflight skipped](spec/2026-10-11-spec-DEPL-aPrimedIndex-1.md) | 4 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPrimedIndex-6 — the pre-push hook scrubs the preflight's skip knob from every bar it runs](spec/2026-10-11-spec-TOOL-aPrimedIndex-6.md) | 4 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPrimedIndex-7 — the regen verb's and the runner's review minors, batched](spec/2026-10-11-spec-TOOL-aPrimedIndex-7.md) | 4 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPrimedIndex-8 — the lander's review minors, batched, and the fixture that names a unit](spec/2026-10-11-spec-TOOL-aPrimedIndex-8.md) | 4 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPrimedIndex-9 — the lexicon render proves freshness alone](spec/2026-10-11-spec-TOOL-aPrimedIndex-9.md) | 5 | 1 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPrimedIndex-10 — the in-place landing checks the allow record against what it pushed](spec/2026-10-11-spec-TOOL-aPrimedIndex-10.md) | 6 | 1 | INPROGRESS | rev-1 | 2026-10-11 |
<!-- /gen:build-units -->

Records: 15 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-aPrimedIndex-1 TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-10 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 TOOL-aPrimedIndex-6 TOOL-aPrimedIndex-7 TOOL-aPrimedIndex-8 TOOL-aPrimedIndex-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPrimedIndex-1` | no |
| 2 | `TOOL-aPrimedIndex-2` | no |
| 3 | `TOOL-aPrimedIndex-3`, `TOOL-aPrimedIndex-4` | yes |
| 4 | `DEPL-aPrimedIndex-1`, `TOOL-aPrimedIndex-6`, `TOOL-aPrimedIndex-7`, `TOOL-aPrimedIndex-8` | yes |
| 5 | `TOOL-aPrimedIndex-9` | no |
| 6 | `TOOL-aPrimedIndex-10` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
