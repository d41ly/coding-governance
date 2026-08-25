---
slug: aBatchedTribunal
node: a
opened: 2026-08-09
streams: tooling
roster: TOOL
ids: TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-2 TOOL-aBatchedTribunal-3 TOOL-aBatchedTribunal-4 TOOL-aBatchedTribunal-5 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-7 TOOL-aBatchedTribunal-8
---

# aBatchedTribunal — the review protocol becomes a gate, not a note

`memory/review-workflow-protocol.md` in the upstream inCMS tree is a binding charter rule: **≤5
verify-stage agents TOTAL per review, ≤5 concurrent, batch size grows and agent count does not.**
This repo has a batched harness and had no rule pointing at it, so the first bespoke review written
in this session fanned **one skeptic per finding** and nothing stopped it. That is the whole build:
port the protocol, and make its central number mechanical.

## Units

TWO specs, not four sub-specs. W1–W3 are one mechanism and the rev-1 review moved its centre of
gravity, so splitting that single decision across three specs would have put it in three places to
drift. W4 is a separate spec because it answers a separate document — the closing review.

| Unit | Spec | What it lands |
|---|---|---|
| W1 | `-1` | `memory/guides/REVIEW-PROTOCOL.md`, charter-binding, shipped with the workflows kit's own parity check |
| W2 | `-1` | the verifier-arity rule in `agent-cap.js` (+ `scriptPath`, cap 6 → 5), `check-verifier-fanout.sh` delegating to it, `tier2-review.js` bounded |
| W3 | `-1` | the closing review of `76fcd09..HEAD` re-run through the batched harness — which found the new rule failing OPEN |
| W4 | `-6` | the four rows that review left open; three of them worse than their row said |
| W5 | `-6` | the review of W4 — the new self-test was failing open |
| W6 | `-8` | the epoch gate's endpoint hole; the per-commit trade measured, not guessed |

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBatchedTribunal-1` | 2 | the review protocol becomes a gate, not a note |
| 2 | `TOOL-aBatchedTribunal-6` | 2 | W4: the four rows the closing review left open |
| 3 | `TOOL-aBatchedTribunal-8` | 2 | W6: the epoch gate's endpoint hole, and the trade measured |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node a · opened 2026-08-09 · streams tooling
ids TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-2 TOOL-aBatchedTribunal-3 TOOL-aBatchedTribunal-4 TOOL-aBatchedTribunal-5 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-7 TOOL-aBatchedTribunal-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBatchedTribunal-1 — the review protocol becomes a gate, not a note](spec/2026-08-09-spec-aBatchedTribunal-1.md) | — | 2 | CLOSED | rev-3 | 2026-08-09 |
| [TOOL-aBatchedTribunal-6 — W4: the four rows the closing review left open](spec/2026-08-09-spec-aBatchedTribunal-6.md) | — | 2 | CLOSED | rev-2 | 2026-08-09 |
| [TOOL-aBatchedTribunal-8 — W6: the epoch gate's endpoint hole, and the trade measured](spec/2026-08-09-spec-aBatchedTribunal-8.md) | — | 2 | CLOSED | rev-1 | 2026-08-09 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->