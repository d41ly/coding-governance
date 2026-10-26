**Serves:** research TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30

# Round-1 fix brief — dFurnishedOrders, what the checks found in the round-1 promotions

## The prompt

Fix the four findings listed in the brief below, in the promoted specs they name.

## The brief

### Goal

The round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
promoted its findings into units 22 to 30, which the disposal stage authored. The main loop then ran
`python tools/check-spec-tokens.py`, which printed four lines on those specs; the hygiene gate is green. Fix each
finding in the spec it names and nothing else. Units 29 and 30 are new and uncommitted, so they stay `rev-1` and owe
no §9 line. Every rule of the spec brief
`memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md` still binds.

### Items

- **R1 · suites named as acceptance observations (`[bar]`).** TOOL-dFurnishedOrders-29's §6 names
  `tools/runlog/selftest.py` and `tools/roles/adopt-roles.test.sh`, and TOOL-dFurnishedOrders-30's §6 names
  `tools/workflows/unattended-build.test.sh`. Rewrite each criterion to observe the unit's own code directly (the
  function or checker on a staged break, a scratch fixture, a probe the pass runs), and keep or add the suite on a
  `New arm:` line in §7.
- **R2 · a hand-off token the receiver never names (`[handoff]`).** TOOL-dFurnishedOrders-4 hands `render_slot`,
  `ORDER_SLOTS` and the `--for-names` lookup to unit 29, and unit 29 never names `--for-names`: name it in unit 29's
  item that bounds that lookup's reader (its S24, as unit 4's bullet says), in backticks.

### Acceptance

`python tools/check-spec-tokens.py` prints no line naming a `memory/builds/dFurnishedOrders/spec/` file, run by the
main loop on the real tree after you return.

### Gates

The memory-hygiene gate's checks 2, 12 and 25, which your role admits, in a throwaway clone under your scratch path
with every spec of the folder committed there; the main loop re-runs the spec-token check.

### Non-goals

Any new unit or new design, and any edit outside `memory/builds/dFurnishedOrders/spec/`. You commit nothing and
render no index: the main loop commits once after you return.
