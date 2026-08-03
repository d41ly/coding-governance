# Review brief — TOOL-aGuardedTally-1 spec, pre-code adversarial pass

Target spec: `C:/projects/coding-governance/memory/tooling/builds/2026-08-03-TOOL-aGuardedTally/spec/2026-08-03-spec-aGuardedTally-1.md`
Repo root: `C:/projects/coding-governance`. Base `57d9b54`.

## What is under review

The spec's DESIGN. Nothing is built. It modifies `tools/workflows/tier2-review.js` (lines 121-128
and ~164), adds `tools/gate-lint/`, and edits `parallel-coding-governance.template.md`.

## The defect being fixed, so you do not re-report it

`tier2-review.js:121-128` does `finderResults.filter(Boolean)` then, on an empty finding list,
returns `note: 'clean: 0 findings'`. A dead agent returns `null` and is dropped silently, so an
all-dead run is indistinguishable from an all-clean one. Observed live 2026-08-03: a review returned
`{"confirmed":[],"note":"clean: 0 findings"}` with `agents_done: 0`, four `ENOTFOUND` errors, and a
journal holding four `started` lines and zero `result` lines.

## Where a review earns its tokens here

1. **Is the three-way distinction in §4 actually sufficient?** Are there states it still collapses —
   a lens that returns a malformed object, a lens that returns `{findings: []}` after an internal
   error, a partially-drained batch in the verify stage?
2. **S2 (the refuted path) is specified in one sentence.** Is that enough to build from, and does the
   AC4 phrasing ("no verdict comes back") cover the batched-skeptic shape where one agent returns
   verdicts for five findings and covers only three?
3. **Does the fix change any caller's behaviour?** §5 claims the only consumers are orchestrator
   prose. Verify that against the repo.
4. **AC5 demands mutation-verification.** Is it specified precisely enough that a builder cannot
   satisfy it by asserting on already-clean input?
5. **Is S3's template prose actually project-agnostic**, or does it smuggle inCMS specifics?
6. **§8 Fork 1** asks whether the inCMS-local `tier2-review-indexed.js` should be folded back as
   canonical. Is the recommendation right?

## Output contract

Cite findings by spec section (`S1`..`S4`, `AC1`..`AC5`, `§4`, `§5`, `§8`) or `file:line`. Skeptics
default to refute. Rank confirmed findings by severity, name the section each folds into, and state
explicitly whether every lens actually ran — a prior run of this harness family reported a hard zero
because all its agents had died.
