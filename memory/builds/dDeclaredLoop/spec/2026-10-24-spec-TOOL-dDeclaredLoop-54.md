# TOOL-dDeclaredLoop-54 — a terminal set declared per level, and the termination rule run over each table with its own

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 35 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-54-deviation-541.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-54-deviation-541.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 5 at HIGH**, its item **H5**, alone in that item. `TOOL-dDeclaredLoop-33` S2
requires every state of the build, feature and unit tables to reach a terminal state.
`TOOL-dDeclaredLoop-13` declares feature and unit states ending at `deployed`, but
`TOOL-dDeclaredLoop-15`'s `terminal` list holds only build terminals and is not keyed by level. So every
feature and unit state fails the rule over gov's own composition, and `TOOL-dDeclaredLoop-33` AC10 (exit
0 over this repository) cannot pass unless a builder quietly exempts two of three tables. This unit takes
the report's first fix. It repairs `TOOL-dDeclaredLoop-33`.

## 2. Scope (IN)

- **S1** — Per-level terminal sets in `[states]` of `tools/loop/loop.toml`: `feature-terminal =
  ["deployed"]` and `unit-terminal = ["deployed"]`, each member a state of that level's list; the build
  level keeps `terminal`, `TOOL-dDeclaredLoop-15`'s, unchanged. Observed by AC1.
- **S2** — One reader, `read_terminal_set(level)` in `tools/loop/loop_table.py`, returning `terminal` for
  `build` and `<level>-terminal` otherwise, and refusing a level with no declared set, naming it.
  Observed by AC1, AC2.
- **S3** — `TOOL-dDeclaredLoop-15` S2's refusal of a terminal in any row's `from` applies to every level
  through the reader; its refusal of a terminal also listed among open states stays the build level's,
  because the feature and unit levels declare their states as one list. Observed by AC2.
- **S4** — `TOOL-dDeclaredLoop-33` S2's rule reads each table's terminal set through
  `read_terminal_set(level)` and walks reverse reachability per level, an empty set still a finding.
  This supersedes S2's single terminal set. Observed by AC3.

## 3. Non-goals (OUT)

- A unit's state when its build is withdrawn: the build table's terminal ends the build, and the unit
  table models a unit's own steps, which end at `deployed`.
- The termination rule's other arms and the leg: `TOOL-dDeclaredLoop-33`'s, and the leg's guard is
  id 55, unit `TOOL-dDeclaredLoop-55`.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-33` — `check_termination`'s `terminal` rule in `tools/loop/termination.py`, which this unit runs per level
- **consumes-from** `TOOL-dDeclaredLoop-15` — `terminal` in `[states]` and the terminal refusals in `check_transition_tables`, which this unit keys by level
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 44 and 45: this pass keeps the loop transition tables and loop termination legs green, and its arm runs under the loop selftest leg that unit adds

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-13` §4 "Data model": `feature = ["decomposed", "designed", "built", "tested",
  "deployed"]` and `unit = ["designed", "built", "tested", "deployed"]` in `[states]`.
- `TOOL-dDeclaredLoop-15` §4 "The terminal set": `terminal = ["landed", "withdrawn", "superseded",
  "incomplete", "deferred", "retired", "refused", "merged", "answered"]`, the build's nine.

### Data model

```toml
[states]
terminal = ["landed", "withdrawn", ...]        # build level, TOOL-dDeclaredLoop-15
feature-terminal = ["deployed"]
unit-terminal = ["deployed"]
```

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_table.py`
- `tools/loop/termination.py`

### Alternatives rejected

- **Limiting the rule to the build table.** The feature and unit tables would carry a termination claim
  no check makes, which is the false claim the finding names.
- **Re-keying `terminal` as a table of levels.** It moves a key `TOOL-dDeclaredLoop-15` and its readers
  spell; two additive keys change nothing that reads today.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — three reverse walks instead of one, over tables of at most twenty rows.
- error / empty / loading states — a level with no declared set is a named refusal, never a pass.
- observability — the rule's finding names the level.
- risks — a new level added later must declare its set, which S2's refusal enforces.
- testing — AC1 to AC3 as probes and plants; the arm under §7, observed at the close.
- migration — none.
- user docs — the terminal section of `help/loop.md`, `TOOL-dDeclaredLoop-15`'s, names the per-level sets.

## 6. Acceptance criteria

- **AC1** — When a probe calls `read_terminal_set` for `build`, `feature` and `unit`, it returns the nine
  build terminals, `["deployed"]` and `["deployed"]`.
  Red when: the feature or unit level has no declared set and reads the build's.
- **AC2** — When `python loop_table.py --fixture --plant unit-terminal-from` plants a unit row
  leaving `deployed`, the check exits 1 naming it; with `--plant level-no-terminal`, a level whose set is
  absent, it exits 1 naming the level.
  Red when: the from-terminal refusal reads only the build level.
- **AC3** — When `python termination.py check` runs over gov's composition on the built tree,
  its `terminal` rule passes for all three tables.
  Red when: the feature and unit states are walked toward the build's terminals and every one is a finding.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC3 · the terminal rule per level over a planted composition, staged against `TOOL-dDeclaredLoop-33`'s single build set · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Per-level sets, or the rule limited to the build table?** Options: (a) a set per level; (b) the
  build table only, the others stated derived. (b) leaves the composition's termination claim unchecked
  on two of three tables. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 5 (HIGH, item H5).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dDeclaredLoop-15`'s `terminal` key and refusals, and `TOOL-dDeclaredLoop-13`'s
`[states]` and `loop_table.py`; the unit adds two keys and one reader there. `python
tools/codebase-map/reuse_lookup.py "terminal states declared per level of a transition table"` ranked
declaration readers of other files (`declares`, `declared_list`, `declared_scalar`) and `plan_state`, none
a state table; the loop kit is not indexed at base.

Recall terms used: terminal set level feature unit deployed states termination reverse reachability transition table
