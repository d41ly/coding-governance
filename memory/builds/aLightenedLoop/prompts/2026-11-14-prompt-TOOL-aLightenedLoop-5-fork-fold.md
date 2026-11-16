**Serves:** research TOOL-aLightenedLoop-5

# Fork fold — TOOL-aLightenedLoop-5: the owner's §8 answers for this unit only

## The prompt

> Unit 5 F1: "(a) Accept, say so in header (Recommended)"
> Unit 5 F2: "(b) On, env kill switch"

Item 3 is the pre-commit hook's refusal, not an owner answer.

## The brief

### Goal
Fold this unit's owner answers into its spec's §8 as RESOLVED, and carry it through §4, §6 and the other sections it touches: a rev bump and a §9 line.

### Items
1. TOOL-aLightenedLoop-5 F1 → option (a). Accept the fault path, and state in `stop-guard.js`'s header that a cache hit does not reproduce a fault.
2. TOOL-aLightenedLoop-5 F2 → option (b). Default on, with the environment kill switch `STOP_GUARD_LIVENESS_CACHE=off`, which restores today's spawn on every Stop. Add an acceptance criterion that observes the switch.
3. Hygiene check 12 refused this spec at the opening commit: "acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF: 2026-08-15 -- AC2". Give AC2 a backticked witness, the command or file whose output observes it.

### Acceptance
This spec's §8 has no unresolved item, and it carries a rev bump and a §9 line naming this record. `python tools/check-spec-tokens.py --spec <path>` exits 0 on it.

### Gates
The spec-token check and memory hygiene, as the role's gates.

### Non-goals
Only this unit's spec changes. No other spec, and no code.

### Limitations
The build brief's limitations hold: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`.

### Reuse
The seams each spec's §10 already names.
