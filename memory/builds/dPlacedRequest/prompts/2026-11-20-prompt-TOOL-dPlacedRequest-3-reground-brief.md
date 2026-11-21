**Serves:** research TOOL-dPlacedRequest-3

# Brief — dPlacedRequest: TOOL-dPlacedRequest-3 re-grounded before its build

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-3 is the next unit to build, and its spec (rev-5) predates what this run has built since: the
probe program (TOOL-dPlacedRequest-7, whose rev-9 F11 routes a role item's `probe` outcome to the stand-in
`stand-in:{prefix}/loop/probe.py` because a route into `item.probe.trigger` is a cross-step route
`tools/loop/loop_table.py#check_transition_tables` refuses), the placement module (units 4, 5, 10 and 14:
`tools/loop/placement.py`), the claim (unit 21: `tools/loop/claim.py` and the driver's `--entry-claim`), the item seeds
and maps (units 8 and 6), and the kickoff card's pockets (unit 9). Re-ground the spec so a builder can build it as
written, before it is dispatched.

### Items

1. F-probe: every place the spec routes an entry item's `probe` outcome to `item.probe.trigger` (its §3 consumes-from edge, its §4 table row and the declaration example, and the open-question text) routes it to `stand-in:{prefix}/loop/probe.py` instead, as TOOL-dPlacedRequest-7 F11 rules for every role item. Record it as a fork in §8 marked `RESOLVED (agent, 2026-11-20, delegated): the probe stand-in, rung 3; TOOL-dPlacedRequest-7 F11 rules it for every role item, and the transition-table check refuses the cross-step route. widens: none · relaxes: none`.
2. Probe the tree for every symbol, item, field, verb and path the spec cites, and amend each that no longer matches: the five entry items' rows as `tools/loop/loop.toml` holds them today (their `seed`, `map` and `unfolds` keys, their actors, owners and routes, and whether TOOL-dPlacedRequest-21 already declared any of them), the placement and claim verbs by their tree names, and the card's pockets section. Where the spec would now re-declare something another unit already landed, say so and narrow the unit to what is left.
3. Replace every line citation with a `path#symbol` citation, and every bare file-stem section reference with its alias tag.
4. If an amendment leaves a real choice the tree cannot settle, decide it by the same rung and record it resolved; leave no fork open.

### Acceptance

Spec 3 at rev-6 carries the resolved probe fork, every amendment the re-grounding found, `path#symbol` citations,
and one §9 line naming this brief; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-3` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the driver's `--check-specs` and the naming
lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays DEFERRED), no spec other than
TOOL-dPlacedRequest-3. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section
number stand before a unit word, and never quote a check's hit literally in prose.
