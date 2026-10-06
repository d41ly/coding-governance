**Serves:** journal TOOL-aGraftedHelix-35..36

# Spec brief — TOOL-aGraftedHelix-35 and -36, promoted by the rotated run's closing review

The source of both units is the rotated run's closing diff review,
`memory/builds/aGraftedHelix/reviews/2026-10-06-review-TOOL-aGraftedHelix-29-closing-diff-round1.md`.
Read each section a unit names WHOLE, including its Fix and Left-shift lines. Where a skeptic judged
a fix UNSOUND (ids 6, 10, 11, 14 and 18), the record gives the skeptic's corrected fix: build that
one, never the finder's. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states twelve shared invariants that bind
both units, but its interface section describes code as it was planned. Read the CURRENT code, which
34 built units and three reconciling merges have moved since. No spec audit is run (the opt-in is the
owner's alone). The claim refusals are checks 107 to 111. Spec `order` values: 35 is 19, 36 is 20.
Unit 36 is built after unit 35 because their write sets overlap (`gotchas.py`, the build harness
template, the unattended skill): its spec must read 35's spec and not undo it.

The owner's mandate for this run binds both: nothing is backlogged, and every discovery made while
building joins the build.

## TOOL-aGraftedHelix-35 — Tier-2 — H1 (id 1), closing M1 (id 18) with it

Unit 29 made the review harness read the by-design block at the subject's base. On the spec-audit
route, the audit still merges a second checklist, the spec commit's `--for-diff HEAD~1..HEAD`. That
checklist reads its by-design block at the spec commit's PARENT, which sits inside the build, after
the run's pinned base. `renderChecklistUnion` then keeps every by-design entry of either input, so a
ruling added earlier in the run can exempt the specs being audited. That is the H1 class on a route
unit 29 left open. Close it at the union: no by-design entry reaches an audit unless it stood at the
run's pinned base. Say whether the spec commit's own checklist keeps its by-design block for any
other reader, and if it does, give that reader the base as well. M1 is the same defect at its binding
grade: the fix discharges both ids, and the spec says so.

## TOOL-aGraftedHelix-36 — Tier-2 — the batched minors (M2 to M7, L1 to L3)

One unit, by the owner's promote-every-finding ruling: each item fixed as its section's Fix line
states (or the skeptic's corrected fix where the record judges the finder's unsound), and each
left-shifted as its Left-shift line states.

- **M2** (ids 2, 9 and 17): `--for-diff` misses a renamed invariant's old path.
- **M3** (id 7): the unattended skill never passes `base` to the spec audit, so unit 29's pin is dead
  plumbing on the shipped caller.
- **M4** (ids 8 and 19): unit 31's settle claim-write retry was handed to the orchestrator and never
  disposed of.
- **M5** (id 10): for the shipped junction install, the check-wiring note's guard compares the
  install with itself.
- **M6** (ids 11 and 14): the pathless-commit ban reports no count, misses `git -C` and mid-literal
  forms, and reds on comments.
- **M7** (id 15): the product half of unit 34's `run_bounded` race fix has no arm that can fail.
- **L1** (id 6): the push-main-active guard checks, then acts.
- **L2** (id 16): the re-cut seams lost the topology instrument, and the hoist rule has no standing
  check.
- **L3** (id 20): the README roster row for unit 34 still states rev-1's filing mechanism. Rewrite it
  to the mechanism the unit built.
