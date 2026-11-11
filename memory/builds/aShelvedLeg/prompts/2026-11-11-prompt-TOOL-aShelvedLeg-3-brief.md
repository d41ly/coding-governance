# Brief — aShelvedLeg: unit 2's closing-review minors

**Serves:** research TOOL-aShelvedLeg-3

## The brief

### Goal
The MEDIUM and LOW the closing review of TOOL-aShelvedLeg-2 confirmed are fixed in one batch unit, as M4 promotes them, and each is left-shifted. The findings are in `memory/builds/aShelvedLeg/reviews/2026-11-11-review-TOOL-aShelvedLeg-2-closing-diff-round1.md`. The spec is written with status DEFERRED: by the owner's ruling of 2026-11-11 units 1 and 2 land first and this unit lands later on its own. Its §3 declares **consumes-from** `TOOL-aShelvedLeg-2` and no edge to unit 1.

### Items
1. **The every-bar comments S1 missed (MEDIUM, ids 2 and 3).** `tools/unattended/lib-unattended.sh:2389` says `read_spec_audit_ids` exists "because check 2 runs on every bar", and `tools/unattended/unattended.sh:2997` rests an owner-accepted cost on check 9 asserting the same facts "on the bar". Both checks are `check-unattended.sh`'s, which TOOL-aShelvedLeg-1 held off every automatic bar. Re-derive the population by grep over every script in `tools/unattended/`, not a named-file list, and reword each sentence; where a sentence's argument rested on the bar running the leg, say what bounds it now.
2. **The changed-mode sentence drops its other arms (LOW, ids 1 and 4).** `tools/unattended/README.md:424-426`, `tools/unattended/kit.toml:263-265` and `memory/gotchas/changed-mode-selection-ignores-doc-reads.md` say the leg is selected by the kit's shipped sources "only" or "alone". `run-gates.sh:3071-3077` also runs a held leg with no, unreadable, non-ancestor or foreign last-run record, or one more than `GATE_SELFTESTS_MAX_LAG` commits behind HEAD. Point at that comment rather than restating the rule.
3. **Left-shift.** One `memory/gotchas/` entry for the new class `restated-rule-drops-its-other-arms`; the other two findings' classes exist.

### Acceptance
1. A grep over every file in `tools/unattended/` for every-bar or merge-bar wording on a line about `check-unattended`, check 2, check 9 or the kit gate prints only lines that describe a different leg. At BASE it prints `lib-unattended.sh:2389` and `unattended.sh:2997`.
2. No changed-mode sentence in the three files says "only" or "alone" about the selection.
3. The new gotchas entry passes memory hygiene.

### Gates
memory hygiene · spec tokens · docs · kit version markers · kit epoch · lexicon naming predicates · routed commits name a specced unit · brief-recorded; then the full bar at the lander.

### Non-goals
Behaviour of any script. The changed-mode selection itself.

### Limitations
The spec is written with status DEFERRED: by the owner's ruling of 2026-11-11 units 1 and 2 land first and this unit lands later on its own. Its §3 declares **consumes-from** `TOOL-aShelvedLeg-2` and no edge to unit 1. Comments, docs and records only. `check-unattended.sh` carries raw CR bytes if touched. Kit versions move through the lander's `mint`.

### Reuse
The wording TOOL-aShelvedLeg-2 wrote is the shape.

## Owner confirmation

Asked: Unit 2's review converged with 0 blockers, but promoted 2 more comment-level minors: stale 'runs on every bar' comments at lib-unattended.sh:2389 and unattended.sh:2997, and the changed-mode sentence saying 'only'. The method makes them a unit 3, which means another spec, build and review cycle of about 1 h, with no behaviour change at stake. What now?
Answer: "Land now, 3 later (Recommended)"
