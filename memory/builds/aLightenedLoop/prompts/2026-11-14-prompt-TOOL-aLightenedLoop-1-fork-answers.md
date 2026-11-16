**Serves:** research TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-5

# Fork answers — aLightenedLoop's §8 forks, resolved by the owner on 2026-11-14

## The prompt

> Unit 1 F1: "A: stamp, staged only + override (Recommended)"
> Unit 3 F1: "(a) No scoping here (Recommended)"
> Unit 5 F1: "(a) Accept, say so in header (Recommended)"
> Unit 5 F2: "(b) On, env kill switch"

## The brief

### Goal
Fold each owner answer into its spec's §8 as RESOLVED, and carry it through §4, §6 and the other sections it touches: a rev bump and a §9 line per spec.

### Items
1. TOOL-aLightenedLoop-1 F1 → option A. The stamp of §4 S2 is consulted under `--staged` only. The owner's override of the charter's `[class]` practice is recorded at `memory/builds/aLightenedLoop/build/2026-11-14-build-TOOL-aLightenedLoop-1-override-1.md`; cite it from §8, and keep the `memory/DECISIONS.md` row the option names in the unit's files-touched.
2. TOOL-aLightenedLoop-3 F1 → option (a). No scoping in this unit: remove scoping from Scope and Acceptance, mark S7 out of scope, and record the incremental per-spec checker as a follow-up ask for the wrap-up. The README roster row is the main loop's to correct.
3. TOOL-aLightenedLoop-5 F1 → option (a). Accept the fault path, and state in `stop-guard.js`'s header that a cache hit does not reproduce a fault.
4. TOOL-aLightenedLoop-5 F2 → option (b). Default on, with the environment kill switch `STOP_GUARD_LIVENESS_CACHE=off`, which restores today's spawn on every Stop. Add an acceptance criterion that observes the switch.

### Acceptance
Each folded spec's §8 has no unresolved item. Each carries a rev bump and a §9 line naming this record. `python tools/check-spec-tokens.py --spec <path>` exits 0 on each.

### Gates
The spec-token check and memory hygiene, as the role's gates.

### Non-goals
No other change to the specs. No code.

### Limitations
The build brief's limitations hold: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`.

### Reuse
The seams each spec's §10 already names.
