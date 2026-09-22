# TOOL-aScouredKit-36 — a lens carries a budget and writes its file FIRST

**Status:** CLOSED · rev-1 · 2026-08-31 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Stop a single review lens from running unbounded and returning nothing, which blocks its whole
workflow and discards every hour it spent.

## 2. Scope (IN)

- S1. Every lens brief in the shipped Tier-2 harnesses states a tool-call budget and instructs the
  lens to record an unanswered question rather than exceed it.
- S2. Every lens brief instructs WRITE-FIRST-THEN-APPEND: create the writeup early and incomplete,
  add to it as you learn.
- S3. The brief carries the incident that bought the rule, with its numbers, so a future reader
  cannot mistake it for style.
- S4. It is stated plainly in the code that this is a BRIEF and not a gate, and why no gate is
  possible here.

## 3. Non-goals (OUT)

- A mechanical timeout. A workflow script cannot time out its own `agent()` call; there is no
  hook and no harness seam that can. Claiming otherwise would be the exact defect this build spent
  three review rounds finding.
- Changing the fan-out or concurrency caps, which are a different control and already enforced.
- `tier2-review.js`, whose lenses receive a diff or a spec rather than a whole tree and did not
  exhibit the failure. Left alone deliberately rather than edited for symmetry.

## 4. Design

A completeness lens ran **2 hours 10 minutes** against siblings that finished in **twelve minutes**,
made 75 tool calls, and was killed having written **nothing** to disk. Two independent defects
produced that, and only together do they make it expensive:

**No budget.** Charter §7 says cost is a verdict — every suite declares a wall-clock ceiling, and
one arriving without a ceiling reds by that fact. The shipped harnesses declare ceilings for their
GATE LEGS and none for their AGENTS. The lens went off building end-to-end adopter fixtures nobody
asked it for, which was defensible work and unbounded.

**No write-first discipline.** The brief said "write your writeup and return ONLY the structured
object", which an agent naturally satisfies at the END. So a lens killed at any point before its
last act leaves zero evidence. Two hours of real work was discarded — and it HAD found something:
the deployment it built confirmed two of this build's own blocker fixes end-to-end at a foreign
prefix, which had to be re-derived by hand from its leftover fixture before that fixture was removed.

The second is the load-bearing half. A budget makes overrun less likely; write-first changes what
overrun COSTS, from everything to nothing.

### Alternatives rejected

Enforcing the budget in the harness. There is no seam: `agent()` returns when it returns, and the
orchestrator cannot interrupt it. Stating a bound that nothing checks would be a ceiling nobody
enforces, which this repo names as its own defect class. So the brief says outright that it is the
only control there is.

## 5. Production-readiness checklist

- security — N/A, prose in a prompt.
- perf / scale — this IS the perf unit; it bounds the worst case.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a lens that runs out of budget now records the unanswered
  question, which is a state the brief previously had no words for.
- observability — a killed lens leaves a partial writeup rather than nothing. That is the whole fix.
- risks — an agent may ignore a brief. Nothing prevents that and §3 says so; the alternative is no
  control at all.
- testing + left-shift gates — `node tools/workflows/check-workflow-syntax.js` ·
  `bash tools/workflows/check-verifier-fanout.sh` · `bash tools/check-kit-versions.sh`.
- migration / rollback — prompt text only; no artifact or return shape moves.
- user docs — the brief is the doc.

## 6. Acceptance criteria

- **AC1** — When `tools/workflows/drift-audit-code.js` and `drift-audit-state.js` are read, each
  lens brief states a tool-call budget AND instructs write-first-then-append.
- **AC2** — When `node tools/workflows/check-workflow-syntax.js` runs, all three scripts parse.
- **AC3** — When `bash tools/workflows/check-verifier-fanout.sh` runs, it is clean — the edit is
  prose inside a template literal and must not disturb the fan-out the hook proves bounded.
- **AC4** — When `bash tools/check-kit-versions.sh` runs, it is green.

## 7. Gates

`workflow syntax` · `verifier fan-out` · `kit version markers` · the full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · built. The incident is recorded in the briefs themselves rather than only
  here, because the reader who needs it is the next lens, not the next spec reader.

## 10. Reuse audit

No new seam: the text is added to the existing `COMMON` block each harness already prepends to every
lens brief, so one edit per harness reaches every lens. `tier2-review.js` composes its briefs
differently and is excluded by §3 for a stated reason rather than by oversight.
