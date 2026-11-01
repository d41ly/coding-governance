**Serves:** research TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42

# Round-3 fix brief — dFurnishedOrders, what the checks found in the round-3 promotions

## The prompt

Fix the findings listed in the brief below, in the promoted specs they name.

## The brief

### Goal

The round-3 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`)
promoted its findings into units 38 to 42, which the disposal stage authored. The main loop then ran
`python tools/check-spec-tokens.py`, which printed 32 lines on units 39, 40, 41 and 42; the hygiene gate is green.
Fix each in the spec it names and nothing else. Units 38 to 42 are new and uncommitted, so they stay `rev-1` and owe
no §9 line. Every rule of the spec brief
`memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md` still binds.

### Items

- **R1 · paths the checker cannot find (`[path]`).** A backticked repo-shaped path in a spec must be tracked at
  HEAD. Unit 39 names `tools/lib/run_bounded.py`; unit 40 names `scripts/run.test.sh`,
  `.claude/workflows/drift-audit-code.js` and `.claude/workflows/mine.test.sh`; unit 41 names
  `tools/govkit/steps/retired_dispatch_args.py`, `scripts/govkit/registry.toml`, `scripts/run.js`,
  `vendor/x/kit.toml`, `scripts/recall/kit.toml`, `scripts/recall/x.test.sh`, `scripts/check-wiring.sh`,
  `scripts/mine.test.sh`, `scripts/drift-audit/drift_signals.py`, `scripts/drift-audit/selftest.py` and
  `scripts/gov/workflows/kit.toml`; unit 42 names `memory/notes/x.md` and `tools/roles/role-schema.toml`. For a
  file this build or a parent will CREATE, keep the full path in §2, §4 and Files touched and cite it by its basename
  elsewhere. For a fixture path inside a scratch adopter, spell it under a placeholder root the checker does not read
  as a repo path (`<fixture>/scripts/run.js`, say), or describe it in words; never as a bare repo path.
- **R2 · suites named as acceptance observations (`[bar]`).** Unit 40 names `scripts/run.test.sh`, `mine.test.sh`
  and `.claude/workflows/mine.test.sh`; unit 41 names `scripts/recall/x.test.sh`, `scripts/mine.test.sh`,
  `scripts/drift-audit/selftest.py` and `.githooks/pre-push.runlog.test.sh`. Where the name is a fixture adopter's
  file, R1's placeholder spelling clears it. Where a criterion runs a real suite, rewrite it to observe the unit's
  own code directly (the function or checker on a staged break, a scratch fixture, a probe the pass runs), and keep
  or add the suite on a `New arm:` line in §7.

### Acceptance

`python tools/check-spec-tokens.py` prints no line naming a `memory/builds/dFurnishedOrders/spec/` file, run by the
main loop on the real tree after you return.

### Gates

The memory-hygiene gate's checks 2, 12 and 25, which your role admits, in a throwaway clone under your scratch path
with every spec of the folder committed there; the main loop re-runs the spec-token check.

### Non-goals

Any new unit or new design, and any edit outside `memory/builds/dFurnishedOrders/spec/`. You commit nothing and
render no index: the main loop commits once after you return.
