**Serves:** research TOOL-dGroundRules-2

# Divergence brief — TOOL-dGroundRules-2, AC4's typo probe matches the `budgets.*` row

## The prompt

> Its builder handed TOOL-dGroundRules-2 back as a DIVERGENCE: §6 AC4 probes `policy.py get budgets.enforse` and wants a refusal naming `catalogue.toml`, but §2 S4 binds `read_catalogue_row` to unit 1's name rule, where a final `*` segment matches any one segment, and unit 1's catalogue carries the v2 row `budgets.*`. So the typo resolves to that row and is never "not a catalogue key".

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-2.md` to the run's ruling (a): AC4 probes a key that no catalogue name or pattern matches, and S4 with unit 1's wildcard rule stands. Author only: no product code, no commit, no gate.

### Items
1. §6 AC4 probes a key no catalogue row matches, exact or wildcard, chosen by reading `tools/policy/catalogue.toml` at HEAD (for example `runtime.agents-in-flite` or `budgetz.enforce`); verify the choice with an in-process `policy.resolve_row(policy.load_catalogue(...), ...)` call returning no row, and keep the rest of AC4 as written.
2. §8 F3 gains one sentence: a near-miss under a wildcard row (`budgets.enforse` against `budgets.*`) resolves to that row by unit 1's name rule, so refusing it is not this unit's mechanism; it belongs with the `budgets.*` census (TOOL-dGroundRules-9), which a later unit owns and this run parks for the owner.
3. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on this spec; AC4's key resolves to no catalogue row at HEAD; every `**Carries:**` and `**Derived:**` line, backticked token, the H1 and the §8 RESOLVED marks survive.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
Any other spec; product code; the spec's status cell, which stays `DEFERRED`; a criterion naming a gate leg, a `*.test.sh` run or the bar.

### Limitations
Ruling (b), a near-miss under `budgets.*` refused by the caps census, was set aside for this unit: unit 2 is ordered before unit 9, so a reader that depends on the census would depend on a unit sequenced after it (BUILD-METHOD M2, ordering axis).

### Reuse
Unit 1's `resolve_row` and `load_catalogue` in `tools/policy/policy.py` are the probe.
