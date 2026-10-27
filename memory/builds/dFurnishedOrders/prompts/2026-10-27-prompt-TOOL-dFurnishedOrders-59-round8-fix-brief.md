**Serves:** research TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60

# Round-8 fix brief — dFurnishedOrders, what the checks found in the round-8 promotions

## The prompt

Fix the findings listed in the brief below, in the promoted specs they name.

## The brief

### Goal

The round-8 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md`)
promoted its findings into units 59 and 60, which the disposal stage authored. The main loop then ran
`python tools/check-spec-tokens.py` (three lines) and the memory-hygiene gate (check 25) over them. Fix each in the
spec it names and nothing else. Units 59 and 60 are new and uncommitted, so they stay `rev-1` and owe no §9 line.
Every rule of the spec brief
`memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md` still binds.

### Items

- **R1 · retirements with no Readers clause (hygiene check 25).** TOOL-dFurnishedOrders-59's S1, S4 and S5 and
  TOOL-dFurnishedOrders-60's S2 and S10 each read as retiring a named thing and carry no `**Readers:**` clause.
  Where an item truly retires a name (a key, a function, a leg, a file, a flag, a row), give it a `**Readers:**`
  clause in the grammar the check states (`by name:` and the readers that spell the name, then `by value:` and the
  readers of its value, or `NO VALUE READERS` and a reason), each reader found by `git grep` over the tree. Where it
  does not, reword it so a retirement verb does not sit beside a backticked name.
- **R2 · a suite named as an acceptance observation (`[bar]`).** Both specs name `tools/govkit/selftest.py` in a
  criterion. Rewrite each criterion to observe the unit's own code directly (the function on a staged break, a
  scratch fixture, a probe the pass runs), and keep or add the suite on a `New arm:` line in §7.
- **R3 · a path the checker cannot find (`[path]`).** TOOL-dFurnishedOrders-60 spells `tools/check-spec-tokens\.py`
  with a regex escape inside backticks. Spell the path plainly, or move the regex out of the path-shaped token.

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
