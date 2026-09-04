# Build brief — TOOL-dRetiredFork-19

**Serves:** journal TOOL-dRetiredFork-19

## What the unit is

`TOOL-dRetiredFork-12` S1 was corrected to `placeholders = ["KIT_DIR"]` because `TOOL_ROOT` cannot
be rendered by the unattended adopter and an unresolved `{{TOOL_ROOT}}` brace would ship to every
adopter. But §4 Data model still reads "Two tokens only", §10 still asserts the pair, and §5 still
says "its two tokens" — and §4 Data model is the section a builder implements from. So following
the spec still ships the brace.

## What this pass does

1. S1/S2 — rewrite `TOOL-dRetiredFork-12` §4 Data model, §10 seam sentence and §5's user-docs row.
2. S3 — build the gate: for every `[[files]]` rule declaring `placeholders`, assert each token is
   substituted by that kit's own adopter, resolved from the descriptor's `[adopt]` argv. One
   direction only: declared subset-of substituted.
3. S5 — run the candidate over the whole tree BEFORE wiring, recording hits AND near-misses.
   ALREADY SUSPECTED: `tools/unattended/kit.toml` declares EIGHT placeholders while
   `adopt-unattended.sh:222-228` substitutes seven. `AUTH_PARAM` may be a live violation, and §4
   Migration says such a repair is its own commit before the gate is wired.
4. S4 — stage `TOOL_ROOT` into a `placeholders` list, observe the RED naming token and adopter,
   revert.
5. S6 — the leg declares a ceiling in `tools/gate-legs.json` and carries its
   `memory/project/testsuite-count-waivers.txt` row if its suite prints no count.

## Ratified forks, folded

F1 — the gate reads the adopter TEXTUALLY, not by running it, and states that limit in its own
header, because a structural check reading as a semantic one is the class §7 names.
F2 — the reverse direction (substituted but undeclared) is REPORTED, never gated.

## What a new leg also owes, learned the hard way earlier in this run

A new gate-legs key must be CLAIMED in a `memory/map/features/` dossier and the map artifacts
regenerated, or `codebase-map coverage` reds. A new tool under `tools/` must be declared in
`tools/govkit/registry.toml`.

## Acceptance

AC1-AC6, run rather than asserted.
