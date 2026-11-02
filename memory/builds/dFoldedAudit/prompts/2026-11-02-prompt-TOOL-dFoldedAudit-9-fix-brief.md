# Fix brief — dFoldedAudit: the M3 sweep and the M2 cross-read over units 9 to 15

**Serves:** research TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15

## The brief

### Goal
Resolve every open fork in units 9 and 15, carry the flagged seams, and cross-read the seven specs so none disagrees with another before the first build pass. The writers' returns are at `memory/builds/dFoldedAudit/build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md`. Commit nothing; the main loop commits.

### Items
1. TOOL-dFoldedAudit-9 §8: F1 RESOLVED to (a), F2 RESOLVED to (a). The main loop has already parked F2's decision row. Mark each `RESOLVED (agent, 2026-11-02, delegated)` in the shape `memory/TEMPLATE-SPEC.md` states.
2. TOOL-dFoldedAudit-15 §8: F1 is the FACT-QUESTION, RESOLVED to (c) by its stated probe. F2 RESOLVED to (b). F3 RESOLVED to (a), overruling that spec's recommendation: the owner-accepted brief's item 1 names M4's text, `tools/unattended/VERBS.template.md` and the protocol as this build's carriers, so aligning them is its stated change and M3's veto 2 does not reach them. Rewrite §3 and §4 to (a).
3. As a result unit 15 also writes, in its one batch: the `--record-round` refusal list in `tools/unattended/VERBS.template.md` and its render, gaining units 11 and 15's changes; the `--plan` bullet unit 13 left; `rev` in the `/build` Skill; and M4's first verdict test in `tools/memory-tree/BUILD-METHOD.template.md` and its render, so it states the case unit 10 adds. M4 stands at 30565 of 30720 bytes; measure the render and stay under. Add `memory/guides/SESSION-KICKOFF.md` to its write set. Turn units 11 and 13's `hands-off external` lines for these into `hands-off` edges to unit 15. M6's `--dispatch` sentence stays parked and is not written.
4. TOOL-dFoldedAudit-14's Edges line reads `hands-off external` while naming TOOL-dFoldedAudit-9. Make it `hands-off` so the pair joins.
5. TOOL-dFoldedAudit-10's fixture C and TOOL-dFoldedAudit-11's fixture R declare no cutoff, and unit 13 ships first and refuses `local` and `--sibling` rows under a blank cutoff. Give each fixture conf `SPEC_FOLD_CUTOFF="2000-01-01"`. Unit 11's `write_chain_fixture` move to rev-3 stays as its spec says.
6. `tools/check-spec-tokens.py` reports TOOL-dFoldedAudit-10: Files touched names `tools/unattended/lib-unattended.sh`, which trips the guard of leg `routed-commits selftest`, absent from §7. Add the leg. Then check every sibling touching that file the same way.
7. Accept TOOL-dFoldedAudit-14's F1 as written; no change.
8. Run M2's cross-read over the seven specs on its four axes. Fix each disagreement in exactly ONE spec, rev bump and §9 line naming what disagreed.

### Acceptance
Every folded spec carries a rev bump and a §9 line, and the return lists each by rev with each axis's result. `unattended.sh --plan dFoldedAudit` reads READY for all seven once committed.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass. Hygiene checks 5, 12 and 25 in a scratch clone.

### Non-goals
A choice beyond these rulings is reported, not decided. No code, no write outside this build's `spec/`.
