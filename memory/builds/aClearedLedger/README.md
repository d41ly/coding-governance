---
slug: aClearedLedger
node: a
opened: 2026-11-13
streams: tooling
roster: TOOL
ids: TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-8 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10
status: OPEN
authorized-by: slug
asks: TOOL-aNimbleMend-16..24
---

# aClearedLedger — the nine asks aNimbleMend's close left open, each closed at its cause

## The problem this build exists to solve

aNimbleMend landed green and left asks 16 to 24 open in its backlog. Five are suite reds that
predate it and that every later close must re-attribute: the gate guard's two parity arms, seven
context arms of the scratch guard, the spec-token suite's parity arm, eight lines of the hygiene
self-test and thirty-three wrong assertions of the policy fixtures. One is an unbound variable the
hygiene gate prints under `--staged`. One is four suites past their cost budgets, read on a busy
node. One is a `Red-fix:` commit with no path, which can never be recorded. The last is an owner
call on two sentences about the red-fix lane, ruled on 2026-11-13.

## Expected improvements

- Each of the five suites runs green, fixed at its cause, with no floor raised and no arm waived.
- A `--staged` hygiene run prints no unbound variable, and an arm reds on the old behaviour.
- Four budget rows name a reading taken alone on a quiet node.
- A path-less `Red-fix:` commit has a stated debt and a plant case.
- The charter and the protocol say what the owner ruled.

## Detriments if this is not built

- Every close keeps re-attributing five inherited suite reds, and a new red hides among them.
- A hygiene check may end early under `--staged` with no verdict printed.
- The charter keeps forbidding, at level 0, a lane the protocol allows.

## Build-level rules

- **Classification (M2)**: ten units at open, each MISSING. The roster is provisional until the
  specs are written.
- **Owner rulings, 2026-11-13 (ask 24)**: the `[spec]` practice gains an exception for an inline
  red fix, written at its source `tools/playbook/practices.toml`; the fix's record stays the next
  commit, and the protocol's section 12 says why.
- **Attended.** No run-state file exists; the merge and the push wait for the owner's ask.
- A suite red is fixed at its cause: no floor is raised and no arm is waived to pass a suite.
- Units 6 and 8 both write the hygiene gate, so 8 follows 6. Unit 10 measures the suites the
  others changed, so it comes last.
- Suites run at the main loop on a frozen clone, never inside a role agent's pass.
- Kit versions move through the lander's `mint`, once, after the last unit.
- No spec audit: the owner declined one at kickoff, 2026-11-13.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aClearedLedger-1` | the `[spec]` practice's exception for an inline red fix, at the practice catalogue, with the charter and the role agents re-rendered |
| 2 | `TOOL-aClearedLedger-2` | the protocol's section 12 states that a fix's record is the next commit and why it cannot ride its own fix |
| 3 | `TOOL-aClearedLedger-3` | the gate guard and the leg manifest agree on every suite invocation: the two parity arms of the gate guard's suite |
| 4 | `TOOL-aClearedLedger-4` | the scratch guard's refusal context and the seven context arms of its suite agree |
| 5 | `TOOL-aClearedLedger-5` | the spec-token suite's manifest parity arm matches every suite invocation the manifest declares |
| 6 | `TOOL-aClearedLedger-6` | the hygiene self-test's eight lines: the scoped-run partition over check 26's cache figure, and the conf example's undeclared keys |
| 7 | `TOOL-aClearedLedger-7` | the policy fixtures leg prints no wrong assertion: the guard census, the reader refusal and the recall export cap |
| 8 | `TOOL-aClearedLedger-8` | the acceptance-ledger block of the hygiene gate binds its map under `--staged`, with an arm that reds on the old behaviour |
| 9 | `TOOL-aClearedLedger-9` | what a path-less `Red-fix:` commit owes, stated by the door or the join, with a plant case |
| 10 | `TOOL-aClearedLedger-10` | four suite budget rows re-measured alone on a quiet node, with the ceilings and the pass legs re-derived |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-13 · streams tooling
ids TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-8 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
