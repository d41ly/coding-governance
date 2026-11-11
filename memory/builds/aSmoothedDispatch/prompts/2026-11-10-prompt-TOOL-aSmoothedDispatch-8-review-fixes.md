# Promotion brief — aSmoothedDispatch: the closing review's six findings and one carried gap, batched

**Serves:** research TOOL-aSmoothedDispatch-8

## The brief

### Goal
The closing diff review, `memory/builds/aSmoothedDispatch/reviews/2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1.md`, ended CLEAN WITH FIXES and CONVERGED. It has no blocker and no high: three medium items and two low items, holding six confirmed findings. The build method's severity rule (M4) promotes every confirmed finding at a DIFF exit, with mediums and lows batched into ONE unit. That unit is this one. It also carries the held-suite guard gap unit 6's builder found, which the review graded medium. Read the review record's Items section whole; each item states its location, defect, fix and left-shift gate. Units 1 to 7 are CLOSED and their specs stay frozen, so where an item names a CLOSED spec's text (spec 7 at its evidence row and quoted overlay), this unit's spec records the correction and does not edit that spec.

### Items
1. Item 1 (medium): the `gov-spec-writer` house overlay, its rendered agent file and the `--spec` docstring in `tools/check-spec-tokens.py` describe the row shape the checker prints on exit 1, which is `spec-tokens: <spec path> [<kind>]` per miss, then the `unwaived hit(s)` summary. The overlay also says a `spec-tokens: REFUSING` line or an exit 1 with no row is a checker refusal to report. A `spec-tokens self-test` arm runs `--spec` on a planted red spec and greps stdout for the row prefix read from the overlay itself.
2. Item 2 (medium): `tools/unattended/unattended.test.sh` gains the review's three arms for the refusing half of unit 4's admit predicate: own plus foreign hit, a stale waiver row, and a stub checker exiting 1 with no summary. Each is staged RED by deleting its clause from the predicate.
3. Item 3 (medium): the same suite's unit 4 cache arm asserts that call 2 re-ran the checker. New arms cover an edited tracked file, a new commit, a second slug, a refused dispatch run twice, and a missing fingerprint script that prints `spec-token cache off` and writes no key. Each is staged RED by dropping its key component.
4. Item 4 (low): the same suite gains the no-value `--writes` arms: flag next, end of argv and whitespace only, each hitting the empty-path refusal. It also gets the second carriage-return arm that unit 1's spec S3 named.
5. Item 5 (low): `renderRouteContext` in `tools/hooks/scratch-guard.js` reads dispatch rows only when no card-routed unit is buildable, as `checkRouted` step 9b does. A `scratch-guard self-test` arm with a buildable card unit and a buildable dispatched unit asserts no dispatch-row line.
6. Carried gap (medium): the `scratch-guard self-test` leg's guard in `tools/gate-legs.json` names the unattended kit, whose driver its D-AC6 row reads.

### Acceptance
Each item's arm is observed RED on its stated break and GREEN restored, at the close by the main loop. The overlay's quoted row prefix matches a real red `--spec` run's stdout. The scratch-guard leg's guard names `{prefix}/unattended/`.

### Gates
unattended kit self-test, spec-tokens self-test, scratch-guard self-test, roles render wiring, memory hygiene, spec tokens, lexicon naming predicates, kit epoch, kit version markers; then the full bar once.

### Non-goals
Any behaviour change to units 1 to 7 beyond item 5's read order; edits to CLOSED specs; new bug-class records, since all four classes the review names exist.

### Limitations
Kit versions move through the lander's `mint`, not by hand. The builder runs no gate or suite; arms are observed at the close.
