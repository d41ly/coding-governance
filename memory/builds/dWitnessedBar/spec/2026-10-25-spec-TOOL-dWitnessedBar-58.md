# TOOL-dWitnessedBar-58 — the hook's inherited-base export observed where the knob is still visible: the stub bar's environment and the runner's decline, with every leg proven blind to it

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 33 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 |
| [2026-10-25-build-TOOL-dWitnessedBar-58-round3-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-58-round3-fix-return.md) | research | TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-58-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-58-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-58-round3-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-58-round3-fix-brief.md) | research | TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 |
| [2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 52 to 57
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md`)
confirmed finding **id 12 at HIGH**, its item **H1**, alone in that item. `TOOL-dWitnessedBar-56` S5 and
AC4 observe the hook's `GATE_BASE_FROM=inherited` export through "a fixture leg printing its
environment". `TOOL-dWitnessedBar-40` S2 has the runner read the knob once and unset it before any leg
starts, as it unsets `GATE_RUN_ID` (`tools/run-gates/run-gates.sh:2623`). On a correct unit-40 build no
leg can ever see the knob, so AC4 is always red, and the easy way to green it is to drop the unset,
which leaks the knob into every leg. This unit takes the report's fix: the export is observed at the
runner boundary, where the knob is still visible, and the leg-side observation is turned round into a
guard that the unset holds. It repairs `TOOL-dWitnessedBar-56`.

## 2. Scope (IN)

- **S1** — The export at the stub boundary. `.githooks/pre-push.test.sh` gains an arm on the
  inherited-green fixture of its `IR AC4` block (`:1397-1405`), whose push takes the branch at
  `.githooks/pre-push:2123-2127`. The bar is a stub named by `GOV_GATE_CMD` that writes
  `${GATE_BASE_FROM-unset}` to a file under the fixture's git dir, the capture the docs arms already
  make for the docs knob (the stub at `:1823`, read at `:1856` and `:1966`). The file reads
  `inherited`. On the moved-remote fixture of the same block (`:1409`), whose decision is FULL, with the caller's environment setting
  `GATE_BASE_FROM=inherited`, the file reads `unset`. Observed by AC1.
- **S2** — The decline at the runner boundary. `tools/run-gates/run-gates.evidence.test.sh` gains an arm
  that runs the real runner in a clean scratch clone, scoped, with `GATE_BASE=<sha>` and
  `GATE_BASE_FROM=inherited`, over a fixture manifest whose one leg writes `${GATE_BASE_FROM-unset}` to a
  file. After the run, `<common-dir>/gate-verdict/` holds no `.scoped` file for the tree, the run
  record's `base_from` row carries the third field `inherited` that `TOOL-dWitnessedBar-56` S10 adds, and
  the leg's file reads `unset`. Observed by AC2.
- **S3** — The criterion it replaces. Unit 56's AC4 is answered by S1 and S2: at the close the main loop
  writes unit 56's AC4 line in its acceptance ledger in the OBSERVED form, carrying
  `GATE_BASE_FROM=inherited` and naming this unit's AC1 and AC2 and report id 12. Observed by AC3.

## 3. Non-goals (OUT)

- The export, the clear and the class line of the two knobs: `TOOL-dWitnessedBar-40` S2 and
  `TOOL-dWitnessedBar-56` S9.
- The third field of `base_from`: `TOOL-dWitnessedBar-56` S10. This unit reads it.
- The other bar callers' scrub of the knob: `TOOL-dWitnessedBar-60`, id 28's unit.
- The report's left-shift text, a bug-class checklist entry and a spec-audit check on env-knob criteria:
  each is a gate no clause of this build names. S2's leg-side `unset` is the regression gate for this
  instance.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-56` — S9's clear and S10's `inherited` field of `base_from`, which S1 and S2 observe, and its AC4, which S3 answers
- **consumes-from** `TOOL-dWitnessedBar-40` — S2's read-once-and-unset of `GATE_BASE_FROM`, the scoped decline and the hook's export, which S2's leg file proves hold
- **hands-off** `TOOL-dWitnessedBar-63` — S1's stub, written to a suite scratch file as `docstub` writes, AC2's positive twin and its second staged break, and the floor raise that chains with unit 60's (ids 1, 14, 34)

## 4. Design

### Evidence

- `unset GATE_RUN_ID`, "read above, removed here, before any leg starts" (`run-gates.sh:2618-2623`);
  unit 40 S2 puts `GATE_BASE_FROM` under the same rule.
- The inherited-green branch exports `GATE_BASE` and runs `RUNLOG_DECISION=scoped`
  (`.githooks/pre-push:2123-2127`); unit 40 S2 adds `GATE_BASE_FROM=inherited` beside `GATE_BASE` there.
- The hook suite stubs the bar with `GOV_GATE_CMD` under `GOV_GATE_CMD_TEST=1`
  (`.githooks/pre-push.test.sh:121`, `:150`); a stub is not the runner, so it unsets nothing.
- `base_from` is written once per run record (`run-gates.sh:3485`).

### The three boundaries

| Where the knob is read | What it holds on an inherited-green push | Observed by |
|---|---|---|
| the bar command's own environment (a stub) | `inherited` | S1 |
| the runner, before any leg | `inherited`, then unset | S2: no `.scoped`, `base_from … inherited` |
| a leg the runner starts | nothing | S2: the leg's file reads `unset` |

### Inventory

Minted: nothing by name; two suite arms and the evidence suite's floor raise.

### Migration

None.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-56`, in the parallel group of order 33 with
`TOOL-dWitnessedBar-60`.

### Files touched (estimate)

- `.githooks/pre-push.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`

### Alternatives rejected

- **Keep the leg-side observation and drop unit 40's unset.** It is the leak unit 56's S9 inert class
  exists to prevent, and it turns a correct build red.
- **Observe the export by reading the hook's source for the `export` line.** A grep cannot tell a
  branch that runs from one that does not; the stub reads the environment the bar really receives.

## 5. Production-readiness checklist

- security — S2 makes "no leg inherits the knob" a red-able observation rather than an assumption.
- perf / scale — one stub push and one scratch-clone runner run, seconds.
- error / empty / loading states — a stub file that is absent fails the arm, never passes it.
- observability — the arms print the value each boundary read.
- risks — none beyond the fixtures' upkeep.
- testing — AC1 to AC3 by fixture; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `.githooks/pre-push` runs over the `IR AC4` inherited-green fixture with `GOV_GATE_CMD`
  naming the capturing stub, the stub's file reads `inherited`; over the moved-remote fixture with the
  caller setting `GATE_BASE_FROM=inherited`, it reads `unset`.
  Red when: the hook omits the export on the inherited-green branch, or lets a caller's value through to
  a FULL bar.
  fixture: the hook suite's own `IR` fixtures, built by the suite.
- **AC2** — When the runner runs scoped over S2's one-leg fixture manifest in a clean scratch clone, with
  `GATE_BASE_FROM=inherited`,
  `ls <common-dir>/gate-verdict/` shows no `.scoped` file for the tree, `grep -P '^base_from\t'` over the
  run record prints a row ending `inherited`, and the fixture leg's file reads `unset`.
  Red when: the runner's unset is dropped, so the leg reads `inherited`; or the decline writes a
  `.scoped` record.
  fixture: a scratch clone under `%TEMP%/<short-name>`; the tree holds none.
- **AC3** — When `grep -rn 'TOOL-dWitnessedBar-58' memory/builds/dWitnessedBar/build/` runs at the close,
  it names unit 56's AC4 ledger line carrying `GATE_BASE_FROM=inherited` under
  `**Evidences:** TOOL-dWitnessedBar-56`.
  Red when: unit 56's AC4 is recorded observed by the in-leg reading this unit replaces.

## 7. Gates

`pre-push self-test` · `run-gates evidence` · `memory hygiene`

New arm: .githooks/pre-push.test.sh · covers AC1 · the inherited-green stub capture and the FULL decision with a caller-set knob, staged red by deleting the hook's `GATE_BASE_FROM` export · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC2 · the scoped inherited run with an env-capturing leg, staged red by deleting the runner's `unset GATE_BASE_FROM` · FLOOR_ASSERTIONS raised by these assertions

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-56`'s clause. Unit 56 carries none,
  being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 52 to 57, id 12
  (HIGH, item H1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.

## 10. Reuse audit

The seams are the hook suite's `IR` inherited-green fixtures (`.githooks/pre-push.test.sh:1397-1409`) and
its stub capture of an exported knob (`:1823`, the docs arms' stub), plus the runner's existing
read-once-and-unset pattern (`run-gates.sh:2623`) that S2 now observes from a leg.
`python tools/codebase-map/reuse_lookup.py "observe an environment knob the hook exports to the bar"`
ranked `export` (memory-recall), `enumerate_exports` and `write_bar_green`, none a capture of a bar's
environment, so no existing seam fits beyond the two fixtures named, which were found by reading the
suite.

Recall terms used: `python tools/memory-recall/query.py "where does a bar caller scrub the knobs the pre-push hook clears" --terms "BAR_SCRUBBED_KNOBS PM_SCRUB _gknobs GATE_DOCS_BASE gates-green trusted gate-bar-green inherited knob scrub parity"`
