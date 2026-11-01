# TOOL-dScopedBuild-32 — one bar call, `run_gate_bar`, carrying `gates-green`'s knob scrub, for the Build exit and the core run

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 2 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md) | research | TOOL-dScopedBuild-25 TOOL-dScopedBuild-28 TOOL-dScopedBuild-31 TOOL-dScopedBuild-33 TOOL-dScopedBuild-35 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 22 at HIGH**, report item **H8**. `TOOL-dScopedBuild-1` S5's `run_build_exit`
copies the `gates-green` bar call, a pinned run id and `$GATE_CMD` with `GATE_RUN_ID` and
`GATE_ATTRIBUTE`, and leaves out that arm's scrub (`tools/unattended/unattended.sh:11157-11170`),
which unsets `GATE_LEGS`, `GATE_REUSE`, `GATE_REUSE_LINEAGE` and four more knobs before the bar runs.
`TOOL-dScopedBuild-7` S3's `run_build_core` repeats the shape "as `--build-exit` does". A main loop
that exports a `GATE_LEGS` subset or a reuse knob then gets `build-exit: PASS` over a bar that graded
only that subset, since the green record stores neither the manifest nor the reuse mode.

This unit puts the scrub list in one function and the bounded bar call with its exit-3 re-run in
another, which both new callers use, so neither can run the bar unscrubbed. It repairs
`TOOL-dScopedBuild-1` and builds one step after it (order 2).

## 2. Scope (IN)

- **S1** — The scrub. `derive_bar_scrub <label>` in `tools/unattended/unattended.sh` holds the one knob
  list, the line `local _gk _gknobs="GATE_LEGS GATE_REUSE GATE_REUSE_LINEAGE GATE_DOCS_BASE
  GATE_SPAWN_CMD GATE_SPAWN_FLOOR GATE_VERDICT_FAULT" _gset=""` moved verbatim from the `gates-green`
  arm, so the parity arm that cuts it (`tools/unattended/unattended.test.sh:4341`) still reads it. It
  sets the array `GB_SCRUB` to `-u GATE_WALL` and one `-u <knob>` per member, and prints
  `<label> — not honoured from the environment by this bar: <knobs>` naming each set one. The
  `gates-green` arm calls it with `unattended: gates-green` in place of its inline loop and reads
  `GB_SCRUB` where it read `_gscrub`; its decision table, in-place branch and `--decide` call are
  unchanged. Observed by AC1 and AC2.
- **S2** — The call. `run_gate_bar <label> <R> [<legs file>] [-- <env word>...]` in `unattended.sh`
  runs `derive_bar_scrub`, then per try pins a fresh run id and its dir under the git dir's `gate-run/`
  as the arm does (`:11174-11179`), runs `run_orphan_reap`, and runs
  `run_bounded env "${GB_SCRUB[@]}" GATE_RUN_ID=<id> GATE_ATTRIBUTE=<R> [GATE_WALL] [GATE_LEGS=<legs
  file>] <env words> $GATE_CMD`, `GATE_LEGS` set after the scrub and only from the explicit argument.
  It re-runs once on exit 3 with a fresh id, as the arm does (`:11280-11281`), and sets `GB_RC`,
  `GB_ID`, `GB_DIR` and `GB_HEAD`, the HEAD it graded. Observed by AC1.
- **S3** — The callers. Unit 1 S5's `run_build_exit` runs the bar as
  `run_gate_bar "build-exit" "$ASHA"` and hands `GB_RC` and `GB_DIR` to `check_build_exit`; unit 7
  S3's `run_build_core` runs it as `run_gate_bar "build-core" "$R" "<core legs file>" -- GATE_FULL=1`,
  its manifest an argument and never an inherited `GATE_LEGS`. This supersedes unit 1 S5's "runs
  `$GATE_CMD` once with `GATE_RUN_ID` and `GATE_ATTRIBUTE=<R>`" and unit 7 S3's bar line. Observed by
  AC1 and AC3.

## 3. Non-goals (OUT)

- Moving `gates-green`'s own loop into `run_gate_bar`. Its in-place branch checks the prepared merge
  and asks the push boundary to decide on the first try inside the loop (`:11198-11277`); §8 F2 keeps
  it.
- The exit's table and the core run's verdict: units 1 and 7.
- The left-shift driver-suite arm over every bar-running verb the report names beyond AC1's. No
  clause of this build names it.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — S5's `run_build_exit` bar call, which S2 and S3 give the scrub (id 22)
- **hands-off** `TOOL-dScopedBuild-7` — S3's `run_build_core` bar call, spelled `run_gate_bar "build-core" "$R" "<core legs file>" -- GATE_FULL=1`, its core manifest an argument rather than an inherited `GATE_LEGS` (id 22)
- **hands-off** `TOOL-dScopedBuild-37` — S1's `derive_bar_scrub` knob line and AC1's and AC2's knob sets, which that unit restates with `GATE_REGEN_CHECK` (id 22)
- **hands-off** `TOOL-dScopedBuild-39` — S2's `run_gate_bar`, which this unit's builder builds with the slug argument and the backstop `RB_BOUND` that unit's S14 and S15 state, and AC2, which its S10 and S11 complete (ids 7, 16, 15, 31)

## 4. Design

### Evidence

- `unattended.sh:11157-11170`: the scrub list, commented that a green record "stores neither the
  manifest nor the reuse mode, so a GATE_LEGS subset or a GATE_REUSE run inherited from the driver
  would certify the whole bar for this tree".
- `tools/run-gates/run-gates.sh:252` reads `LEGS_FILE=${GATE_LEGS:-...}` from the environment, and
  neither driver file unsets the knobs anywhere else (the report's id 22, confirmed).
- `tools/unattended/unattended.test.sh:4334-4345`: the parity arm cuts `^ *local _gk _gknobs="..."`
  from the driver and asserts every `BAR_SCRUBBED_KNOBS` name is in it, so S1 keeps that line's
  spelling.
- `unattended.sh:11280-11281`: the loop breaks unless the bar exited 3 on the first try.

### The call, after this unit

```
run_gate_bar <label> <R> [<legs file>] [-- <env word>...]
  derive_bar_scrub <label>                         -> GB_SCRUB, the not-honoured line
  try 1, and try 2 only on exit 3:
    pin GB_ID, GB_DIR; run_orphan_reap
    run_bounded env "${GB_SCRUB[@]}" GATE_RUN_ID=GB_ID GATE_ATTRIBUTE=R [GATE_LEGS=<file>] <words> $GATE_CMD
  GB_RC, GB_HEAD
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_bar_scrub`, `run_gate_bar` | shell functions, `unattended.sh` | `sh.function`, OK |
| `GB_SCRUB`, `GB_RC`, `GB_ID`, `GB_DIR`, `GB_HEAD` | shell globals | none |

### Migration

None: no stored data changes.

### Rollout

Built at order 2, one step after unit 1 (order 1), tied with unit 14 and `TOOL-dScopedBuild-33`. Unit
14 also writes `unattended.sh`, so M6 sequences them within the step. Unit 7 (order 9) calls S2.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write`

### Alternatives rejected

- **Copy the scrub into `run_build_exit`.** Three copies of one list, the drift the finding names; a
  fourth caller would copy whichever it read first.
- **Unset the knobs once at the driver's top.** `--close` reads `GATE_SELFTESTS` and the main loop's
  exports on purpose (`:11185-11192`), so a blanket unset would change what the close inherits.

## 5. Production-readiness checklist

- security — deny by default: every bar the new verbs run is the whole manifest unless an argument
  names a file.
- perf / scale — unchanged: one bar, and one re-run on exit 3.
- error / empty / loading states — no `GATE_CMD` stays unit 1's exit 2, before S2 runs.
- observability — the not-honoured line names each knob it unset, with the caller's label.
- risks — the `gates-green` arm's behaviour must not move; AC2 reads its scrub through the same
  parity arm as before.
- testing — AC1 to AC3 in the driver suite.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `GATE_LEGS=<a one-row manifest> GATE_REUSE=1 bash unattended.sh --build-exit tExit`
  runs in the driver suite's fixture, its `GATE_CMD` a stub recording `${GATE_LEGS-unset}` and
  `${GATE_REUSE-unset}`, the stub records `unset unset` and the output holds
  `build-exit — not honoured from the environment by this bar: GATE_LEGS GATE_REUSE`.
  Red when: the exit's bar inherits an exported knob.
  fixture: unit 1 AC5's slug fixture and stub bar.
- **AC2** — When `grep -c '_gknobs="' tools/unattended/unattended.sh` runs on the built tree it prints
  1, and `sed -n 's/^ *local _gk _gknobs="\([^"]*\)".*/\1/p' tools/unattended/unattended.sh` prints
  the seven knob names.
  Red when: a second copy of the list exists, or the parity arm's cut reads nothing.
- **AC3** — When `run_build_core` runs over the same fixture with `GATE_LEGS` exported to another
  file, the stub records the core legs file `derive_core_manifest` wrote and the full-run knob
  `GATE_FULL` at the value 1.
  Red when: the core run grades an inherited manifest.
  permission: observed at the close, after unit 7 is built.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 · the exit and the core run over exported `GATE_LEGS` and `GATE_REUSE` with a recording stub, staged by running the bar without `GB_SCRUB` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 1's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How much of `gates-green`'s bar call is extracted?** Options: (a) the whole loop, with the
  in-place preconditions and the first-try `--decide` moved before it; (b) the scrub list into
  `derive_bar_scrub`, which all three callers use, and the loop into `run_gate_bar` for the two new
  callers, `gates-green` keeping its loop. (a) moves the in-place precondition check out of the exit-3
  re-run, a behaviour change to a landed arm no criterion here observes. RESOLVED (agent,
  2026-11-01, delegated): (b), rung 3, the survivor that closes the finding and moves no landed
  behaviour. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 22
  (HIGH, item H8).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-37 and TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 7, 15, 16, 22, 31).

## 10. Reuse audit

The seam is `gates-green`'s own bar invocation (`tools/unattended/unattended.sh:11157-11281`), its
scrub list extracted rather than copied and its loop shape reused for the two new callers.
`python tools/codebase-map/reuse_lookup.py "run the merge bar with its knobs scrubbed and a pinned run
id"` ranked `run`, `merge`, `run_git`, `run_arms` and `extract_run_facts`, none a bar invocation, so
no existing function fits; the arm's inline block is the seam. The recall probe returned scout A's
row for unit 7 and this audit's item.

Recall terms used: `python tools/memory-recall/query.py "why does gates-green scrub GATE_LEGS before the bar" --terms "GATE_LEGS GATE_REUSE scrub gates-green bar knobs manifest reuse mode green record certify"`
