**Serves:** research TOOL-dGroundRules-23

# Divergence brief — TOOL-dGroundRules-23, the descriptor guard reds aScoutedSeam's live spec

## The prompt

> Its builder built the join, probed it green, then handed TOOL-dGroundRules-23 back as a DIVERGENCE with nothing committed: S4's guard addition of the census kits' descriptors puts `{prefix}/roles/kit.toml` under the `policy fixtures` guard, which reds the `[guards]` arm of `tools/check-spec-tokens.py` on TOOL-aScoutedSeam-1 (SPECCED), whose §4 touches `tools/roles/kit.toml` and whose §7 lacks the leg. The main loop measured the whole set with every S4 addition applied in a scratch clone: that one hit, `policy fixtures <- tools/roles/kit.toml`, and no other.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-23.md` to the run's ruling (a), the option that keeps the guard on every census descriptor, matching TOOL-dGroundRules-20 §8 F1. Author only: no product code, no commit, no gate.

### Items
1. A §8 fork, RESOLVED (agent, 2026-10-24, delegated) citing ER:388 and the precedent of TOOL-dGroundRules-20 §8 F1 and TOOL-dGroundRules-18 §8 F2: S4 keeps `{prefix}/govkit/entries/` and every census kit's descriptor, and the unit also writes one waiver row keyed `policy fixtures <- tools/roles/kit.toml` in `memory/project/spec-token-waivers.txt` (reason naming TOOL-aScoutedSeam-1 and this unit's guard widening; 33 to 34 rows) and a deviation record `memory/builds/dGroundRules/build/2026-10-24-build-TOOL-dGroundRules-23-deviation-75.md` carrying `**Bound:**`, `**Tier:**`, `**Reason:**` and `**Surface:**` per `memory/HYGIENE.md` "Deviation records", whose follow-through is ask TOOL-dGroundRules-110, which already asks aScoutedSeam's TOOL-1 §7 to carry `policy fixtures`; no new ask. The commit's `Decided:` trailer carries `widens: memory/project/spec-token-waivers.txt` and `relaxes: spec-token-waivers shrink-only count`. Stopping at `entries/` and handing the rest to TOOL-dGroundRules-32 is refused: that unit would meet the same hit, and a descriptor change in between would go unguarded.
2. §4's files touched adds the waiver registry and the deviation record, and `memory/guides/SESSION-KICKOFF.md` if absent (the kickoff manifest watches `tools/gate-legs.json`); §7 adds `spec tokens (a spec's own names resolve)` if absent.
3. §1 and §4 cite the `{prefix}/govkit` exempt row of `tools/govkit/registry.toml` by its content rather than `:296`, which now names another row.
4. §4's pseudocode notes that a `ships = false` row carrying `kit` or `installed` is already refused by `budgets.read_cap_census`, so the join's own `ships = false` loop is unreachable and the case observes that refusal as its WRONG.
5. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's probes stand: the join built green on 26 shipped rows, and its RED probes for AC1 and AC2 named the rows.

### Reuse
TOOL-dGroundRules-20's waiver rows and deviation-74 are the template.
