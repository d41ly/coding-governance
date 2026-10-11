# TOOL-aPrimedIndex-6 — the pre-push hook scrubs the preflight's skip knob from every bar it runs

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Classify the runner's new `GATE_REGEN_CHECK` knob at the push boundary, so the pre-push suite's H49
arm holds and a caller cannot skip the generated-output preflight on the push that lands
(closing review r1, H2, id 12).

## 2. Scope (IN)

- **S1** — `.githooks/pre-push` adds `GATE_REGEN_CHECK` to `BAR_SCRUBBED_KNOBS`, the knobs it unsets
  for every bar not labelled STUB, with a comment naming why the push bar may not skip it: a skip
  can change the verdict for an output whose leg a guard scopes out (review L4). Observed by AC1 and
  AC2.
- **S2** — The class is left-shifted as a bug-class record, `memory/gotchas/`, anchored on the runner,
  so the next unit adding a runner knob meets the classification duty on its checklist before the
  guarded H49 arm can see it. Observed by AC3.

## 3. Non-goals (OUT)

- The pre-push self-test leg's guard is not widened and the H49 check is not split into its own
  leg: a widened guard makes every live spec touching the runner owe the held leg, and a new leg is
  a meta-gate cascade this mandate does not need. The record in S2 is the left-shift.
- The runner and README text stating the scrub are TOOL-aPrimedIndex-7's, which owns those files.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-3` — the knob being classified.

## 4. Design

`BAR_SCRUBBED_KNOBS` gains one name. The hook's loop already unsets each one for a non-STUB bar and
records it as cleared, and the H49 arm reads the constant with `read_hook_const`, so no reader
changes. The bug-class record follows `memory/gotchas/`'s existing front matter and sections, with
an anchor on the runner path so `gotchas.py --for-paths` selects it; the index is regenerated.

### Files touched (estimate)

- `.githooks/pre-push`
- `memory/gotchas/a-runner-knob-owes-a-push-class.md`
- `memory/gotchas/INDEX.md`

## 5. Production-readiness checklist

- security: the push bar can no longer be told to skip the preflight from the environment.
- perf / scale: N/A — one name in a loop.
- error / empty / loading states: unchanged; an unset knob is a no-op.
- observability: the hook's cleared-knob record names the knob when a caller had set it.
- risks: a STUB bar keeps it, as it keeps every scrubbed knob, which is the hook's own fixtures' need.
- testing: the H49 arm replayed directly, and the scrub observed on a staged break.
- migration: none.
- user docs: the bug-class record; the README line is TOOL-aPrimedIndex-7's.

## 6. Acceptance criteria

- **AC1** — When the H49 arm's `check_knob_classes`, extracted from the pre-push suite, is replayed
  over the runner, it prints nothing; before the edit it printed
  `unclassified-or-twice GATE_REGEN_CHECK (0)`. Red when: the knob is unclassified or classified
  twice.
- **AC2** — When the hook's scrub loop is replayed with `GATE_REGEN_CHECK=0` exported and a non-STUB
  class, the variable is unset afterwards and named in `ENV_CLEARED`. Red when: the variable
  survives the loop.
- **AC3** — When `python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.sh` runs,
  the new class is among the selected items, and `gotchas.py --check` exits 0. Red when: the record
  selects nothing or the index is stale.

## 7. Gates

`memory hygiene` · `pre-push self-test` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from closing review round 1 H2 (id 12).

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` on "unset environment knobs before the push bar runs"
returned only name-stem candidates (`run`, `before`, `run_arms`), so no existing seam fits beyond
the one the closing review names, `BAR_SCRUBBED_KNOBS` in `.githooks/pre-push` with its loop, which
this unit extends by one name. The record follows the shape of the
nearest records under `memory/gotchas/`.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
