# DEPL-aPrimedIndex-1 — govkit's verdict reader runs the target's runner with its generated-output preflight skipped

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams deployer · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-DEPL-aPrimedIndex-1-1-acceptance-ledger.md](../build/2026-10-11-build-DEPL-aPrimedIndex-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-6-1-build-brief.md) | journal | TOOL-aPrimedIndex-6 TOOL-aPrimedIndex-7 TOOL-aPrimedIndex-8 |

<!-- /gen:spec-records -->

## 1. Goal

Keep `govkit apply` comparing legs when a target's tree holds a stale generated output. The runner's
new preflight exits 2 before any leg line, and apply's two verdict reads then parse an empty map,
with which apply can certify an install it never compared (closing review r1, H1, id 7).

## 2. Scope (IN)

- **S1** — `read_gate_verdicts` runs the target's runner with `GATE_REGEN_CHECK=0` in its
  environment, so both the baseline and the after read get one verdict per leg, and a stale output
  reads as its own freshness leg's red. Observed by AC1.
- **S2** — The govkit self-test gains an arm driving `read_gate_verdicts` over a fixture runner that
  refuses unless the knob reaches it. Observed by AC2.

## 3. Non-goals (OUT)

- No empty-map guard on the after read. The review offered one as optional; the knob closes the
  trigger this build added, and a guard is a refusal policy for the deployer to decide.
- The run-gates README's list of bar entry points gains govkit apply in TOOL-aPrimedIndex-7, which
  owns that file in this build.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-3` — the preflight and the knob that skips it.

## 4. Design

One keyword argument on the existing `subprocess.run` in `read_gate_verdicts`:
`env=dict(os.environ, GATE_REGEN_CHECK="0")`, with a comment saying why. The knob is inert for this
reader's purpose: apply compares legs, and every output the preflight checks is also a leg.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

## 5. Production-readiness checklist

- security: N/A — the same command runs; one variable is added to its environment.
- perf / scale: each read skips a check of about a minute on node `a`.
- error / empty / loading states: unchanged; the reader's existing guards still read the map.
- observability: unchanged.
- risks: a target whose runner predates the knob ignores it, which is the behaviour before this build.
- testing: the new self-test arm, and a direct call observed on a staged break.
- migration: none.
- user docs: N/A — the README line is TOOL-aPrimedIndex-7's.

## 6. Acceptance criteria

- **AC1** — When `read_gate_verdicts` is called directly over a fixture target whose runner prints
  `GATE ok    fixture leg` only when `GATE_REGEN_CHECK=0` reaches it and otherwise exits 2, it returns
  that leg as green. Red when: the call returns an empty map, as it does with the `env` argument
  removed.
- **AC2** — When the new self-test arm's block is executed alone, with the suite's `check` and
  `govkit_module` helpers, it records no failure; with the `env` argument removed from the reader it
  records one. Red when: the arm passes against the reader without the knob.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a fixture runner that exits 2 with no leg line unless the knob reaches it · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from closing review round 1 H1 (id 7).

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` on "run the target's gate runner and parse its leg verdict
lines" returned only name-stem candidates (`parse`, `run`, `legs`), so no existing seam fits beyond
the function the closing review names, `read_gate_verdicts` in `tools/govkit/govkit.py`, which this
unit extends by one argument. The fixture follows
the self-test's existing `govkit_module()` direct-call arms.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
