**Serves:** journal TOOL-aGraftedHelix-33

# Spec brief — TOOL-aGraftedHelix-33, adopted mid-run

Tier-1, streams tooling, `order 17`. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states the twelve invariants that bind it.
Read units 15, 16 and 21's acceptance ledgers under `memory/builds/aGraftedHelix/build/` and the
CURRENT `tools/workflows/unattended-build.template.js` before designing. In your OWN return, name the
spec you author in `authored` by its unit id, `TOOL-aGraftedHelix-33`, never by its path.

## What was observed

Run `wf_dff1cb65-954`, the first live use of the spec-commit stage units 15, 16 and 21 built. Four
writers each authored one spec. In `authored`, unit 29's writer returned the id
`TOOL-aGraftedHelix-29`; units 30, 31 and 32's writers returned paths, two repo-relative and one
absolute. The commit stage matched `authored` against unit ids only, so it committed unit 29's spec
alone (commit `43bdf3aef`), reported success, and the hand-out carried an empty `specPath` for 30-32,
whose specs sat untracked. `--plan` then read them MISSING. Nothing refused. The main loop committed
them by hand at `1b53b54b8`.

## What to decide

The stage must place every spec a writer authored, whichever spelling the writer used, and must
REFUSE, naming the entry, when an `authored` entry matches no roster unit by id and no unit's spec
by path (normalised: repo-relative, forward slashes, an absolute path under the repo reduced).
Decide whether to also tighten the writer prompt and `SPEC_SCHEMA` so `authored` asks for ids, and
say why both or one. Mind the class `two-guards-one-question-two-answers`: one normaliser, used by
the commit stage and by the hand-out's path fill-back. Edit the template, re-render the `.js` with
`bash tools/workflows/check-protocol-parity.test.sh --render`, bump the kit once.
