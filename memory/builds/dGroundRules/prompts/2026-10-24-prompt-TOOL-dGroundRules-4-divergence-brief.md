**Serves:** research TOOL-dGroundRules-4

# Divergence brief — TOOL-dGroundRules-4, the unknown-key plant under `budgets.*` and the lexicon pin

## The prompt

> Its builder handed TOOL-dGroundRules-4 back as a DIVERGENCE: AC11, S9 and the first `New arm:` line plant `[budgets]` `enforse = "warn"` and expect a reason naming `enforse` as no catalogue key, but S1 and S2 tie validate's unknown-key check to `read_catalogue_row`, which matches `budgets.enforse` to the `budgets.*` row (`tools/policy/catalogue.toml:1279`). S11's lexicon pin arithmetic is also short by one, because TOOL-dGroundRules-2's `Refusal.__str__` arrived unpinned.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-4.md` to the run's ruling, the same one TOOL-dGroundRules-2 rev-4 took: the unknown-key plant uses a key no catalogue row matches, and a near-miss under a wildcard row stays the parked census question. Author only: no product code, no commit, no gate.

### Items
1. AC11, S9 and the first `New arm:` line plant an unknown key no catalogue row matches, exact or wildcard: C's `[runtime]` table setting `agents-in-flite = 3`, with a valid V before it, so `get budgets.enforce --explain` reads V with source `last-valid` and a reason naming `agents-in-flite` as matching no catalogue row. Verify with an in-process `policy.read_catalogue_row` call over `tools/policy/catalogue.toml` at HEAD returning no row for `runtime.agents-in-flite`.
2. §8 F6 gains one sentence: a near-miss under a wildcard row (`budgets.enforse` against `budgets.*`) resolves to that row, so refusing it is the parked `budgets.*` census question (RUN.md, 2026-10-23T20:44:00Z), not this unit's mechanism.
3. S11 pins `VERB_OFFENDER_PIN` at the reading this unit leaves, 1213 measured by the builder, and names both arrivals: TOOL-dGroundRules-2's `Refusal.__str__` in `tools/policy/policy.py`, which arrived unpinned, and this unit's `validate`. Re-measure with `python tools/lexicon/lexicon.py` before writing the number.
4. §4's Files touched adds `tools/policy/README.md`: S8's `arm_on_invalid` joins `ARMS`, and TOOL-dGroundRules-16's `adopter-fresh-target` case requires a matching row in that README's "Each arm in an adopter" table.
5. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling.

### Acceptance
`python tools/check-spec-tokens.py` exits 0; the planted key resolves to no catalogue row at HEAD; every `**Carries:**` and `**Derived:**` line, backticked token, the H1 and the §8 RESOLVED marks survive.

### Gates
No gate runs in this pass beyond the lexicon reading item 3 needs; the close runs the spec's §7 legs.

### Non-goals
Any other spec; product code; the spec's status cell, which stays `DEFERRED`; a criterion naming a gate leg, a `*.test.sh` run or the bar.

### Limitations
The builder's other notes stay with the build: `adopter-fresh-target` reports `arm_on_invalid` before the first commit until TOOL-dGroundRules-21 S15, and the `policy fixtures` budget is unmeasured against the strict case.

### Reuse
`read_catalogue_row` and `load_catalogue` in `tools/policy/policy.py` are the probe.
