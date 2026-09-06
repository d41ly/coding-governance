# The owner's prompt — the self-check gates are broken, rebuild them and keep them off adopters

**Serves:** research TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-5

Handed to `/unattended --prompt` on 2026-09-06, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is recorded here verbatim. The bytes travel rather than
the reference: the build folder is the authorization and may not point at a file the run can edit.

## Verbatim

> Some of this repo's _self-test gates_ are broken - they run for hours and can often hang, freezing
> unattended builds. Two concurrent builds were stalled by gate bars hanging for 9h and 6h. Review
> the currently existing tooling self-check tests and:
>
> * Rebuild them from scratch to run in a reasonable amount of time.
> * Make sure that self-checks do NOT ship to the repo adopters (or ship strictly OPT-IN and do not
>   execute on a full bar by default) - adopters do not need to modify this kit, so self-checks are
>   not required there.

## What was derivable, and therefore not asked

The one owner turn this path allows was NOT taken, because nothing disqualifying was missing.
`memory/guides/BUILD-METHOD.md` M2 names ACCEPTANCE and GATES as the two gaps a run may not close for
itself, and both fall out of the prose plus the tree:

- **Acceptance** is observable from the artifacts the prompt names — a bar's held report, an emitted
  adopter manifest, a declared budget with a verdict against it, and an arm inventory compared across
  a rebuild.
- **Gates** are this repo's own bar, which already grades every one of those surfaces.
- **The one genuine fork the prompt contains it resolves itself**: "do NOT ship … (or ship strictly
  OPT-IN …)" delegates the choice. It is taken in unit 3 and marked there.

What was NOT derivable and is therefore stated as an assumption rather than a decision: "a reasonable
amount of time" carries no figure. This build reads it as a DECLARED budget per suite that reds on
breach, in the shape `tools/unattended/run-unattended-gates.sh` already uses, rather than as a single
global number nobody could defend. A wrong reading here costs a re-declaration, not a rebuild.

## Scope note the owner is owed

"Rebuild them from scratch" is taken at its word for the suites that hold the cost, and NOT read as a
line-by-line rewrite of all 46k tracked lines of self-test. The measured cause is structural — process
creation, not test logic — so a rebuild that preserves every arm and changes how arms are executed is
both the cheaper and the more faithful reading. Unit 6 records the arm-inventory comparison that makes
"preserved" checkable rather than claimed, and the wrap-up names every suite left on the old harness.
