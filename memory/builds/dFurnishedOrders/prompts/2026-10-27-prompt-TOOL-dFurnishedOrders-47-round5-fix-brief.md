**Serves:** research TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49

# Round-5 fix brief — dFurnishedOrders, what the checks found in the round-5 promotions

## The prompt

Fix the findings listed in the brief below, in the promoted specs they name.

## The brief

### Goal

The round-5 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md`)
promoted its findings into units 47 to 49, which the disposal stage authored. The main loop then ran
`python tools/check-spec-tokens.py` (five lines, on units 48 and 49) and the memory-hygiene gate (check 25, on units
47 and 48). Fix each in the spec it names and nothing else. Units 47 to 49 are new and uncommitted, so they stay
`rev-1` and owe no §9 line. Every rule of the spec brief
`memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md` still binds.

### Items

- **R1 · retirements with no Readers clause (hygiene check 25).** TOOL-dFurnishedOrders-47's S2 and
  TOOL-dFurnishedOrders-48's S6, S11 and S23 each retire a named thing and carry no `**Readers:**` clause. Give each
  one, in the grammar the check states: `**Readers:**` then `by name:` and the readers that spell the name, then
  `by value:` and the readers of its value, or `NO VALUE READERS` and a reason. Find every reader with `git grep`
  over the tree. Where an item does not in fact retire a name, reword it so it does not read as a retirement.
- **R2 · paths the checker cannot find (`[path]`).** TOOL-dFurnishedOrders-48 names `a/govkit/registry.toml`,
  `b/govkit/registry.toml`, `{prefix}/check-wiring.sh` and `{prefix}/scratch-kit/kit.toml`. Spell each fixture or
  install-prefix path under the `<target>/…` placeholder the earlier specs use, or describe it in words.
- **R3 · a suite named as an acceptance observation (`[bar]`).** TOOL-dFurnishedOrders-49 names
  `tools/lib/resolve-python.test.sh` in a criterion. Rewrite it to observe the unit's own code directly (the
  function on a staged break, a scratch fixture, a probe the pass runs), and keep or add the suite on a `New arm:`
  line in §7.

### Acceptance

`python tools/check-spec-tokens.py` prints no line naming a `memory/builds/dFurnishedOrders/spec/` file, and the
hygiene gate's check 25 prints no FAILED line naming one, both run by the main loop on the real tree after you
return.

### Gates

The memory-hygiene gate's checks 2, 12 and 25, which your role admits, in a throwaway clone under your scratch path
with every spec of the folder committed there; the main loop re-runs the spec-token check.

### Non-goals

Any new unit or new design, and any edit outside `memory/builds/dFurnishedOrders/spec/`. You commit nothing and
render no index: the main loop commits once after you return.
