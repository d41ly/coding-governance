# TOOL-dCalibratedLens-46 — the loop legs' and `tier2-review self-test`'s guards widened in every spelling the leg is declared in, and rendered where the manifest is a render

**Status:** OPEN · rev-1 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 20 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dCalibratedLens-46-deviation-461.md](../build/2026-11-03-build-TOOL-dCalibratedLens-46-deviation-461.md) | deviation | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 22, HIGH, item H4 of the round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`). `TOOL-dCalibratedLens-41` S13
and S27 widened three guards by editing `tools/gate-legs.json` alone. Once TOOL-dWitnessedBar-11
lands that file is a render: `loop measure fixtures` and `loop-review selftest` are `[[gate_leg]]`
rows of `tools/loop/kit.toml` (unit 4 S9, unit 2 S11), and `tier2-review self-test`'s whole row,
guard included, moves into its `[[exempt_leg]]` row of `tools/govkit/registry.toml`. A hand edit is
then refused by the factory's check, or erased by the next render, and the guard that was widened to
close the held-suite-guard-misses-a-sibling-kit class quietly loses its entries. This unit takes the
three guard edits from unit 41, states which declaration each one lands in under each of the two
states the build run can find, and proves the widening survives. It repairs
`TOOL-dCalibratedLens-41`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 41's text (rev-2, id 22): S13 and
  S27 name this unit as their builder, unit 41's Files touched lists no path, and its §3 hands the
  three guards here. Units 2 and 4 hand their rows' guards here in place of unit 41 (each rev-4, r3
  id 22). Observed by AC1.
- **S2** — Which declaration, decided at the pass by `test -f tools/run-gates/leg_factory.py`, and
  the case is named in the pass's commit as a `Decided:` trailer. Factory case: each entry goes in
  the leg's one declaration as TOOL-dWitnessedBar-11 S1 spells it, the `[[gate_leg]]` row of
  `tools/loop/kit.toml` for the two loop legs (its `[gate_leg.gov]` sub-table's `guard` where the
  declaration splits gov's run from an adopter's) and the `tier2-review self-test` `[[exempt_leg]]`
  row of `tools/govkit/registry.toml`; then `python tools/run-gates/leg_factory.py --write` renders
  `tools/gate-legs.json`. Hand case: each entry goes in the leg's row of `tools/gate-legs.json` and
  in every descriptor row that spells a `guard` for the same leg name, because govkit's check 7h
  joins a descriptor and the manifest by name and never compares their guards (the filed ask
  TOOL-aPacedTurnstile-12). Observed by AC1 and AC3.
- **S3** — The `loop-review selftest` entries, the files the plants of units 19, 20, 26, 32, 33, 35,
  42 and 43 import or read: `{prefix}/memory-tree/record_kinds.py`,
  `{prefix}/memory-tree/record-kinds.toml`, `{prefix}/memory-tree/tree_lib.py` and `{prefix}/runlog/`,
  the runlog kit as a directory because `tools/runlog/runlog.py:67-71` imports five of its modules
  (id 28, M13, carried from `TOOL-dCalibratedLens-48`). Observed by AC1.
- **S4** — The `loop measure fixtures` entries, the files the plants of units 29 and 38 run and what
  they load: `{prefix}/roles/handoff.py` and `{prefix}/roles/roles_lib.py`
  (`tools/roles/handoff.py:92`), `{prefix}/memory-tree/tree_lib.py`, `{prefix}/policy/policy.py`,
  `{prefix}/policy/catalogue.toml` (`tools/policy/policy.py:62`) and `{prefix}/policy/budgets.py`
  (`:599`), the last three carrying the `memory.item-budget` default the plants read (id 28).
  Observed by AC1.
- **S5** — The `tier2-review self-test` entries, the hook unit 24's arm runs and what it loads:
  `{prefix}/hooks/agent-cap.js`, `{prefix}/policy/policy-mirror.js` (`tools/hooks/agent-cap.js:465`)
  and `{prefix}/hooks/scratch-guard.js` (`:1465`) (id 28). Observed by AC2.

## 3. Non-goals (OUT)

- The factory itself, and moving any other leg's guard: TOOL-dWitnessedBar-11.
- A gate that reds a spec whose Files touched names a rendered file without its source, the
  finding's left-shift line. `tools/gate-legs.json` is not a render at base, so its population there
  is empty, and the factory's own `--check` reds the hand edit once it is one.
- A gate computing each guarded leg's import closure, id 28's left-shift line. The closure is read
  by hand here, and `--legs-for` observes each entry.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — the `loop-review selftest` row of its S11, whose guard S3 widens; without it there is no row to edit
- **consumes-from** `TOOL-dCalibratedLens-4` — the `loop measure fixtures` row of its S9, whose guard S4 widens
- **consumes-from** `TOOL-dCalibratedLens-41` — S13 and S27, the guard widenings this unit builds in its place
- **consumes-from** external — TOOL-dWitnessedBar-11 (`leg_factory.py`), DEFERRED at base; its absence at the pass selects the hand case of S2

## 4. Design

### Evidence

- `tools/run-gates/leg_factory.py` is absent at `8bec4cef`, and TOOL-dWitnessedBar-11 is DEFERRED
  (`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md:3`); its S1 (`:36-42`)
  puts every manifest key of a leg in one declaration, an `[[exempt_leg]]` row carrying the whole
  row beside its `why`, and its S2 (`:43-47`) makes `--check` exit 1 on any difference.
- `tools/govkit/registry.toml:666-668` at base: the `tier2-review self-test` `[[exempt_leg]]` row
  holds `name` and `why` only, and `tools/gate-legs.json` holds its guard,
  `{prefix}/workflows/` and `{prefix}/memory-tree/gen_build_index.py`.
- `tools/govkit/govkit.py:2530-2700`: check 7h compares a descriptor's `subject`, `chunk`,
  `doc_reads`, `impure`, `reads` and `ceiling` with the manifest's, and never `guard`.
- Unit 4 S9 and AC10 already assume the factory; unit 2 S11 states a hand-written fallback until it
  lands.

### Inventory

No identifier is minted.

### Files touched (estimate)

- `tools/gate-legs.json` — S2 to S5, in either case
- `tools/loop/kit.toml` — S3 and S4, the declaring rows
- `tools/govkit/registry.toml` — S5, in the factory case

### Alternatives rejected

- **Edit `tools/gate-legs.json` alone, as unit 41 did.** It is the defect: right only while the
  factory is absent, and silently undone by its first render.
- **Wait for the factory and widen only then.** The plants land at orders 3 to 14; until then an edit
  to `record_kinds.py` or `agent-cap.js` would skip the suite that runs it.

## 5. Production-readiness checklist

- security — N/A: selector edits.
- perf / scale — the three legs run on more edits, each a cost of seconds.
- error / empty / loading states — a factory present but failing `--check` after the render stops the
  pass; it is never re-rendered away.
- observability — `--legs-for` names the leg for every entry; the commit's `Decided:` trailer names
  the case.
- risks — check 7c classes each entry as kit-relative, since each opens `{prefix}/`.
- testing — AC1 to AC3 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --legs-for` runs after the pass over
  `record_kinds.py`, `record-kinds.toml` and `tree_lib.py` at their kit paths and
  `tools/runlog/extract.py`, each names `loop-review selftest`; over `handoff.py`, `roles_lib.py`,
  `tree_lib.py`, `policy.py`, `catalogue.toml` and `budgets.py`, each names `loop measure fixtures`.
  Red when: a file a loop plant imports still selects no leg that runs the plant.
- **AC2** — When the same query runs over `tools/hooks/agent-cap.js`, `tools/policy/policy-mirror.js`
  and `tools/hooks/scratch-guard.js`, each names `tier2-review self-test`.
  Red when: an edit to the hook or what it loads still skips the suite whose arm runs it.
- **AC3** — In the factory case, when `leg_factory.py --check` runs from its S2 path after the pass,
  it exits 0. In the hand case, when a `python -c` probe reads each of the three legs' guards
  from `tools/gate-legs.json` and from every `tools/*/kit.toml` row of the same name that spells one,
  it prints the same list for each pair.
  Red when: the widening lives in one spelling of a leg and not the other.
  fixture: which case holds is the build run's, decided by S2's probe.

## 7. Gates

`govkit selfcheck` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `tier2-review self-test` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's legs `loop-review selftest` and `loop measure fixtures` (TOOL-dCalibratedLens-2 S11,
TOOL-dCalibratedLens-4 S9) are not in the manifest at base and are named here in prose.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, promoted from id 22 (HIGH, item H4) of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, carrying id 28 (M13) from
  `TOOL-dCalibratedLens-48`; units 41, 2 and 4 amended at the disposal (their rev-2, rev-4 and rev-4).

## 10. Reuse audit

The seams extended are each leg's own declaration and, in the factory case, TOOL-dWitnessedBar-11's
`leg_factory.py --write`, never a second renderer; `--legs-for` of `tools/check-spec-tokens.py` is
the query the criteria use. `python tools/codebase-map/reuse_lookup.py "widen a held suite guard to
the files its plant imports"` ranked name stems only (`corpus_files`, `resolve_kit_file`); none
computes a guard from imports, so the closure was read by hand from each entry file's imports. The
recall probe returned TOOL-dWitnessedBar-11's reuse scout and the filed ask TOOL-aPacedTurnstile-12,
which S2's hand case follows.

Recall terms used: `python tools/memory-recall/query.py "how is a declared gate leg guard widened
when the leg manifest is rendered from declaring rows" --terms "gate leg guard declaring row rendered
manifest leg factory exempt_leg registry hand-written fallback"`
