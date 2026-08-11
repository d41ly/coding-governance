---
slug: aTimedTurnstile
node: a
opened: 2026-08-11
streams: tooling
roster: TOOL
ids: TOOL-aTimedTurnstile-5
---

# aTimedTurnstile — the merge bar stops being the sum of its legs

Node `a` · opened 2026-08-11 · streams tooling.

`tools/run-gates.sh` runs 47 legs one at a time, so the bar costs the sum of everything it checks:
382.1s warm, 607.3s cold in a fresh worktree, 335.2s for the real runner with its one guard-skip.
The measurement that opened this build found the shape behind that number — 29 of the 47 legs are
SELF-TESTS holding 96.7% of the wall, while the 18 legs that actually check this repo's state cost
12.7s combined — and found that the heavy legs are already hermetic, each isolating itself in a
`mktemp -d` scratch repo. Nothing stopped them running together except the runner.

This build makes them run together. A scratchpad prototype completed all 47 legs in 79.9s at width 8
with `fails=0`, which is the number this unit is built to reproduce.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node a · opened 2026-08-11 · streams tooling · ids TOOL-aTimedTurnstile-5

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aTimedTurnstile-2 — diff-scope the self-test legs, keep the push boundary full](spec/2026-08-11-spec-TOOL-aTimedTurnstile-2.md) | INPROGRESS | rev-1 | 2026-08-11 |
| [TOOL-aTimedTurnstile-5 — run the merge bar's legs concurrently](spec/2026-08-11-spec-TOOL-aTimedTurnstile-5.md) | INPROGRESS | rev-3 | 2026-08-11 |
<!-- /gen:build-index -->

### The specs

| Spec | Item | Tier | Edit site | One-liner |
|------|------|------|-----------|-----------|
| [TOOL-aTimedTurnstile-5](spec/2026-08-11-spec-TOOL-aTimedTurnstile-5.md) | the bounded pool | 2 | `tools/run-gates.sh` + its sibling self-test | Legs run through a bounded worker pool, report in manifest order, and dispatch longest-first from a cache the runner writes itself. |

### What this build does NOT do

Widening `guard` coverage to the 29 self-tests is `TOOL-aTimedTurnstile-2` and is held for an owner
decision, because guards honoured at the push boundary would make the authoritative run diff-scoped
while `AGENTS.md` calls that run the full bar. Making individual legs cheaper is
`TOOL-aTimedTurnstile-3`, and it only becomes the binding constraint after this unit lands, since the
floor stops being the sum and becomes the longest leg under load.
