# Fix brief — TOOL-dFoldedAudit-1: the banned literal and the adopter's budget

**Serves:** research TOOL-dFoldedAudit-1

## The brief

### Goal
Clear the last divergence so unit 1 can apply its saved patch and close. The stopped builder's return is `build/2026-11-02-build-TOOL-dFoldedAudit-1-11-stopped-dispatch.md`. Commit nothing; the main loop commits.

### Items
1. §4 "The verbs carrier", the fence: replace `python tools/policy/policy.py get review.spec-audit.disposal` with `policy.py get review.spec-audit.disposal`, the spelling `tools/workflows/REVIEW-PROTOCOL.template.md:133` already uses. `tools/check-install-prefix.sh:266` bans the literal in that file and allows no waiver.
2. §7: add the leg `install-prefix (shipped surface)`, spelled as `tools/gate-legs.json` spells it.
3. §4 Files touched: add `memory/guides/SESSION-KICKOFF.md`, whose `last-audit` the pass commit re-stamps with a delta line, because `memory/guides/BUILD-METHOD.md` is on the manifest's watch list.
4. The parity block's Budget clause also runs in adopters, because `kit/dogfood doc parity` is a kit `[[gate_leg]]` at `tools/memory-tree/kit.toml:246-249`. The render has 155 bytes of headroom and 18 `{{MEMORY_ROOT}}` sites, so an adopter whose memory root is 9 characters longer goes past the ceiling and has no fix. Make the clause unable to red for that reason, by the smallest change: it may grade the byte count of a render at this repository's own memory root, or run only where the root is `memory`. State the choice in §4 and keep it observable by the arm, with a case proving a longer root does not red.

### Acceptance
TOOL-dFoldedAudit-1 carries a rev bump and a §9 line, its status cell stays INPROGRESS, and each item has its observation.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No change to M4's target text beyond what item 4 needs, no code, no write outside this one spec.
