---
slug: dTieredTribunal
node: d
opened: 2026-08-25
streams: tooling
roster: TOOL
ids: TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-2 TOOL-dTieredTribunal-3 TOOL-dTieredTribunal-4
---

# dTieredTribunal — one review harness for every review kind a build needs

## The problem this build exists to solve
`BUILD-METHOD.md` M4 forbids `tier2-review.js` on a spec — it reviews DIFFS, and a spec is not code —
so every spec audit is driven by a script authored from scratch in the session that needs it. That is
the MAJORITY kind: 82 of this corpus's 156 records are `spec-audit` against 73 `diff-review`.
A hand-written driver re-loses the harness's trust accounting — the integer verdict join, the
dead-lens and dead-skeptic counters, unverified-is-not-refuted, the synth-death hole — each a defect
that shipped once and survives only as a comment. The loss is measured: of three agent-spawning
pipelines in `tools/workflows/`, only `tier2-review.js` carries any of it, and the bar is green over
all three. It shows as ABSENCE, not a crash: a field a program emits appears in 77–88% of records,
one a document asks a human to remember in 5–27%.

## Expected improvements

- `TOOL-dTieredTribunal-1` — a diff review's confirmed-blocker count becomes a value the harness
  returns. The M4 spec-audit loop keeps hand-typing until P1 is ratified.
- `TOOL-dTieredTribunal-2` — the fold class enters `memory/gotchas/`, so the checklist a reviewer is
  handed can name it.
- `TOOL-dTieredTribunal-3` — the two drift-audit siblings stop reporting a clean bill for a run whose
  lenses all died.
## Detriments if this is not built

- A drift audit whose every lens died still returns a clean bill, over a green bar.
- A disagreeing repeat verdict keeps resolving to whichever arrived first.
- A diff review's blocker count keeps resting on a number a human retyped.
- The fold class stays invisible to `gotchas.py`, which is the only thing that emits it.
## Build-level rules
- **This session delivers RESEARCH ONLY.** No spec, no kit edit, no rule edit. The owner narrows the
  proposal set before anything is specced. Settled at kickoff, all three forks.
  **RESOLVED (agent, 2026-08-26, delegated)** — the no-spec half is superseded; the rest still binds.
  No narrowing arrived, so the standing mandate carried it. The criterion had two parts: no
  governance-carrier edit, AND ranked RECOMMENDED or named as a cheaper substitute. Carrier-freeness
  alone qualified nothing, and every proposal the criterion refused is parked below. This run edited
  no governance carrier.
- **Scope is both halves**: the single review pass AND the round/convergence loop M4 and M8 describe.
- **`BUILD-METHOD.md` M4/M8 and `REVIEW-PROTOCOL.md` are in scope as PROPOSALS**, not as edits.
- **Any design fits the caps the hook actually resolves.** File constants in `tools/hooks/agent-cap.js`.
- **The headline goal is NOT delivered.** One engine for every review kind is P1, and P1 is parked.
- **CORRECTION to the problem slot, recorded here because M3 reserves that slot from this run.** It
  says a hand-written driver re-loses four things and only `tier2-review.js` carries any. Two are
  wrong: both siblings DO assign ids in the orchestrator and DO treat a missing verdict as unverified.
  `TOOL-dTieredTribunal-3` §4 is the derived inventory and is the sentence to trust.
- **Node split.** The folder and its ids are node `d`'s; the specs say `node a` because a node `a`
  session authored them under this build's slug and the mandate.
## Parked decisions
- **`TOOL-aDeclaredBound-6`** and **`TOOL-aBoundedVerdict-20`** are OPEN and untouched here.
- **P1 against P9 — the owner turn this build turns on.** P1 is the subject descriptor that IS this
  build's goal; it makes M4's "Not the harness" rule false, so M3 veto 2 reserves it. P9 is the
  record-shape gate the research names as its substitute. They park together because building P9
  alone pre-empts the call on the stronger mechanism.
- **P3, P4, P5, P7, P10 and P11** were each refused by the criterion above and each has a row in this
  build's run-state file carrying the question, the options seen and the reason. Read them there:
  prose here would be a second copy. P5 is the one worth the owner's attention first — it is the only
  lever that reaches a hand-rolled inline driver, which no shipped engine can.
- **P6** is the rule-edit half of whichever option the owner picks, so it rides that turn. **P8** is
  refused by prior art in the research record.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dTieredTribunal-1` | 2 | the harness READS the blocker count it already asks for, and instructs the verdict line |
| 1 | `TOOL-dTieredTribunal-2` | 1 | the fold writes text nobody reviews, and that class is not in the catalogue |
| 2 | `TOOL-dTieredTribunal-3` | 2 | the two drift-audit harnesses gain the trust accounting their sibling already carries |

The owner's narrowing did not arrive with the invocation, so the standing mandate carried it. The
criterion is stated in full in Build-level rules above and has two parts, because carrier-freeness
alone qualified nothing. Every proposal it refused has a row under Parked decisions, and the P1
against P9 fork is additionally parked in this build's run-state file, which is what M9 derives the
owner's turn from.

<!-- /roster:units -->


<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node d · opened 2026-08-25 · streams tooling
ids TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-2 TOOL-dTieredTribunal-3 TOOL-dTieredTribunal-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dTieredTribunal-1 — the harness READS the blocker count it already asks for, and instructs the verdict line](spec/2026-08-26-spec-dTieredTribunal-1.md) | 1 | 2 | SPECCED | rev-4 | 2026-08-26 |
| [TOOL-dTieredTribunal-2 — the fold writes text nobody reviews, and that class is not in the catalogue](spec/2026-08-26-spec-dTieredTribunal-2.md) | 1 | 1 | SPECCED | rev-4 | 2026-08-26 |
| [TOOL-dTieredTribunal-3 — the two drift-audit harnesses gain the trust accounting their sibling already carries](spec/2026-08-26-spec-dTieredTribunal-3.md) | 2 | 2 | SPECCED | rev-4 | 2026-08-26 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dTieredTribunal-1`, `TOOL-dTieredTribunal-2` | yes |
| 2 | `TOOL-dTieredTribunal-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
