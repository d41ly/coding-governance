# TOOL-dScopedBuild-27 — the push leg under `warn-and-ask` prints its ask lines and writes no `BACKLOG.md`; the Build exit files them

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 6 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**, report item **H3**. `TOOL-dScopedBuild-3` AC2 and
`TOOL-dScopedBuild-9` AC3 call `check_routed_commits`, the push leg, under `warn-and-ask` and expect
one ask row added to the fixture's `BACKLOG.md`. Unit 3 S4, unit 9 S2 and `TOOL-dScopedBuild-14` S6
with its §8 F2 file asks at the Build exit alone, because a pre-push hook must not write the tree it
pushes, and unit 14's table says the push leg prints `ask ·` lines only. A correct build cannot pass
either criterion, and a builder chasing them would make the push write `BACKLOG.md`.

This unit restates both criteria's `warn-and-ask` half: the push prints and writes nothing, over
every `BACKLOG.md` of the fixture, and a sliced Build exit files exactly one ask per finding. It
lands on units 3 and 9, and builds one step after the later of them, unit 9 (order 6).

## 2. Scope (IN)

- **S1** — The push writes no ask. Under `warn-and-ask`, `check_routed_commits` prints one
  `ask · build.scope · <subject> · accept <accept>` line per finding and leaves every tracked and
  untracked `BACKLOG.md` under the fixture's memory root byte for byte as it was. This supersedes
  unit 3 AC2's clause "and `write_gate_asks` adds one ask row naming it to the fixture build's
  `BACKLOG.md`" and unit 9 AC3's clause "with one ask row in the fixture's `BACKLOG.md`"; each
  criterion's other clauses stand. Observed by AC1 and AC2.
- **S2** — The exit files them. Over the same two fixtures, `check_build_exit` sliced from
  `tools/unattended/unattended.sh`, as unit 3 AC9 slices it, under `warn-and-ask` returns 0 and
  stages exactly one ask row per finding through `write_gate_asks` (unit 14 S6), each row naming its
  unit, which the ask generator reads back. Observed by AC3.
- **S3** — Units 3 and 9 answered. Each unit's acceptance ledger answers its superseded criterion
  with a note naming `TOOL-dScopedBuild-27 S1`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Changing where asks are filed. Unit 14 §8 F2 ruled the exit, and this unit only restates the two
  criteria that contradicted it.
- The dedupe key `write_gate_asks` reuses an open ask by, id 50 of the same audit, which
  `TOOL-dScopedBuild-35` S32 takes.
- The left-shift checklist entry the report names. No clause of this build names it.
- Rewording units 3 and 9; each clause is superseded by name.

### Edges

- **consumes-from** `TOOL-dScopedBuild-3` — AC2's fixture and its `warn-and-ask` clause, and AC9's slice of `check_build_exit`, which S1 and S2 restate (id 3)
- **consumes-from** `TOOL-dScopedBuild-9` — AC3's map-adopting fixture and its `warn-and-ask` clause, which S1 and S2 restate (id 3)
- **consumes-from** `TOOL-dScopedBuild-14` — S6's `write_gate_asks`, the one exit-time filer S2 observes, and S2's `render_gate_outcome`, whose `ask ·` lines S1 reads
- **hands-off** `TOOL-dScopedBuild-36` — S1's no-write read, AC1's and AC2's fixtures and §7's planted red, which that unit's S1 to S3 restate with `read_backlog_state` (id 11)
- **hands-off** `TOOL-dScopedBuild-39` — S2's and AC3's fixture, which that unit's S22 makes the two trees `routed_commits.build_fixture` builds (id 9)

## 4. Design

### Evidence

- Unit 14 §4 "The three values, where each is read" puts the push's `warn-and-ask` at "leg green,
  ask lines printed" and the exit's at "asks filed by `write_gate_asks`", and says "The ask is filed
  at the exit alone (§8 F2)" (`memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-14.md:150-155`).
- Unit 3 S4 files "one ask per pair, at the Build exit (TOOL-dScopedBuild-14 S6, its §8 F2)", and unit
  9 S2 has `write_gate_asks` file "at the Build exit".
- `routed_commits.build_fixture` (`tools/memory-tree/routed_commits.py:403-404`) is the fixture both
  criteria build; S1 reads its memory root whole, so an arm writing any other `BACKLOG.md` is seen.

### The observation

```
before = {p: bytes(p) for p in fixture memory root's **/BACKLOG.md}
check_routed_commits(...)   under warn-and-ask   -> rc 0, one ask · line per finding
after  = same read                               -> after == before            (S1)
check_build_exit sliced, warn-and-ask            -> rc 0, one staged ask row per finding   (S2)
```

### Inventory

Minted: nothing in product code. Two selftest arms and one driver-suite arm, and the ledger notes of
S3. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 6, one step after unit 9 (order 5) and after unit 3 (order 4), so both fixtures exist.
It ties with `TOOL-dScopedBuild-29` and `TOOL-dScopedBuild-8` at order 6. All three write
`tools/memory-tree/routed_commits.py`, so their write sets intersect and BUILD-METHOD M6 sequences
them within the step rather than running them concurrently.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`: the selftest arms of S1
- `tools/unattended/unattended.test.sh`: the sliced exit of S2

### Alternatives rejected

- **Let the push leg write the row under `warn-and-ask`.** Unit 14 §8 F2 rejected it: a pre-push hook
  would write the tree it is pushing.
- **Assert only the build's own `BACKLOG.md`.** An arm writing another build's file would pass; S1
  reads every one under the memory root.

## 5. Production-readiness checklist

- security — no new write path; S1 asserts the push has none.
- perf / scale — two byte reads of the fixture's backlogs per arm.
- error / empty / loading states — a fixture with no finding prints the `clean` line and no ask.
- observability — S1's arm names the first `BACKLOG.md` whose bytes moved.
- risks — none beyond the two fixtures' own.
- testing — AC1 and AC2 in the routed-commits selftest, AC3 in the driver suite.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `check_routed_commits` runs on unit 3 AC2's fixture under `warn-and-ask`, it exits 0,
  prints one `ask · build.scope · TOOL-tFix-1` line, and every `BACKLOG.md` under the fixture's memory
  root reads the same bytes after as before.
  Red when: the push leg writes or stages any `BACKLOG.md`, or prints no ask line.
  fixture: unit 3 AC2's, built by `routed_commits.build_fixture`.
- **AC2** — When `check_routed_commits` runs on unit 9 AC3's map-adopting fixture under
  `warn-and-ask`, it exits 0, prints the `feat · touched and still graced` finding as an `ask ·` line,
  and every `BACKLOG.md` under the fixture's memory root is unchanged.
  Red when: the touch join's warn-and-ask half writes a row at the push.
  fixture: unit 9 AC3's.
- **AC3** — When `check_build_exit` is sliced from `unattended.sh` and run over each of the two
  fixtures under `warn-and-ask`, it returns 0 and stages exactly one ask row per finding naming its
  unit, which `ASKS_CMD` reads back; a second run over the same tip stages none.
  Red when: the exit files no ask, or files one per run.
  fixture: the driver suite's slug fixture with `ASKS_CMD` declared, as unit 14 AC7 builds it.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 · the two fixtures under `warn-and-ask` with every `BACKLOG.md` read before and after, staged by having the push call the filer · none

New arm: tools/unattended/unattended.test.sh · covers AC3 · the sliced exit over both fixtures and a rerun at the same tip, staged by skipping `write_gate_asks` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause.
  It lands on two units, so (b) would split two clauses for one restated half. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set. widens: none
  · relaxes: none
- **F2 — Which unit does this promotion repair, for its order?** Options: (a) unit 3, order 5; (b)
  unit 9, order 6. At order 5 it would tie with unit 9 and could not read unit 9's fixture, which S1
  and S2 restate. RESOLVED (agent, 2026-11-01, delegated): (b), rung 3, the one survivor that builds
  after both units it lands on. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 3
  (HIGH, item H3).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-36 and TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 9, 11).

## 10. Reuse audit

The seams are the two criteria's own fixtures, `routed_commits.build_fixture`
(`tools/memory-tree/routed_commits.py:403`) and unit 9 AC3's map-adopting shape, and unit 3 AC9's
slice of `check_build_exit`; S2 observes `write_gate_asks` (unit 14 S6) and adds no filer.
`python tools/codebase-map/reuse_lookup.py "assert a push leg writes no backlog file while printing
ask lines"` ranked `write`, `legs`, `write_text`, `leg` and `check_line`, none a no-write assertion
over a fixture's backlogs, so no existing seam fits beyond the fixtures named.

Recall terms used: `python tools/memory-recall/query.py "may the push leg write a backlog ask row" --terms "warn-and-ask write_gate_asks pre-push hook BACKLOG.md ask lines Build exit routed-commits push leg"`
