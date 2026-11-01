**Serves:** research TOOL-dFurnishedOrders-61

# Round-9 fix brief — dFurnishedOrders, what the checks found in the round-9 promotion

## The prompt

Fix the finding listed in the brief below, in the promoted spec it names.

## The brief

### Goal

The round-9 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-59-spec-audit-round1.md`)
promoted its minors into unit 61, which the disposal stage authored. The main loop then ran
`python tools/check-spec-tokens.py`, which printed one line on it; the hygiene gate is green. Fix it and nothing
else. Unit 61 is new and uncommitted, so it stays `rev-1` and owes no §9 line. Every rule of the spec brief
`memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md` still binds.

### Items

- **R1 · a path the checker cannot find (`[path]`).** TOOL-dFurnishedOrders-61 spells the install-prefix path
  `{prefix}/roles/kit.toml` in backticks (around its lines 109 and 371), which the checker reads as an untracked repo
  path. Spell it under the `<target>/…` placeholder the earlier specs use, or describe it in words, as unit 48's fix
  did for `{prefix}/check-wiring.sh`; keep the meaning exact.

### Acceptance

`python tools/check-spec-tokens.py` prints no line naming a `memory/builds/dFurnishedOrders/spec/` file, run by the
main loop on the real tree after you return.

### Gates

The memory-hygiene gate's checks 2, 12 and 25, which your role admits, in a throwaway clone under your scratch path
with every spec of the folder committed there; the main loop re-runs the spec-token check.

### Non-goals

Any new unit or new design, and any edit outside `memory/builds/dFurnishedOrders/spec/`. You commit nothing and
render no index: the main loop commits once after you return.
