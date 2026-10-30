# DEPL-dShippedRelease-2 — `deploy.distill` unarmed, recording that it measured nothing

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 8 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0507@e74286a1 whole
**Carries:** node:item.deploy.distill

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

`deploy.distill` confirms that the decision-log rows `build.distill` wrote are in the log at the
landed SHA. `build.distill` is dScopedBuild's and that build holds no spec, so there is nothing to
confirm: an empty join would read as green. This unit builds the item unarmed, as `test.seed` records
an unarmed seed: it writes a line on the landing record saying it measured nothing, is never green,
and routes on to `deploy.recommend` (the owner's FK-4-8).

## 2. Scope (IN)

- **S1** — The verb, `unattended.sh --deploy distill <slug> <sha>`, over `run_deploy_distill(slug, sha,
  root)` in `tools/loop/deploy_items.py` (pin C1). It reads `read_stand_ins`
  (`tools/loop/loop_table.py`, TOOL-dDeclaredLoop-13 S8) for the row `item.build.distill`. With the
  row present it derives the line `distill: unarmed · <reason> · <sha>`, `<reason>` reading `stand-in
  <owner>` from the row, and sets the record's `distill` field to everything after `distill: ` through
  `set_landing_field` (DEPL-dShippedRelease-1 S6). It prints the line and exits 0. Observed by AC1.
- **S2** — Never green: the verb has no green exit. Its one outcome today is `unarmed`, which the
  `item.deploy.distill` row routes to `item.deploy.recommend`, the row's `witness` reading "the
  landing record's line that it measured nothing". `rows-missing` and `confirmed`, the row's two armed
  outcomes (TOOL-dDeclaredLoop-12's transcription of flow-steps:440), are unreachable until the armed
  path of S5 exists. Observed by AC1, AC3.
- **S3** — The read-back, `check_distill_field(record, stand_ins)` in `deploy_items.py`, reached as
  `python deploy_items.py check-distill <sha>`, run by the verb after its write. It reds, exit 1, a
  record whose `distill` value reads anything but `unarmed · …` while the stand-in row holds, which is
  a green with nothing joined, printing `distill — <sha8> · empty join read green`. A `pending` value
  on a record past this item reds the same way. Observed by AC2.
- **S4** — Idempotence: the item is `idempotent` in flow-steps:440. A re-run on a record already
  holding the line writes nothing, `set_landing_field`'s equal-value rule. Observed by AC4.
- **S5** — The one armed behaviour specified here, since no spec of dScopedBuild exists, is what
  happens when the stand-in row is gone. When `read_stand_ins` holds no `item.build.distill` row, the
  verb looks for `read_distill_join` in `deploy_items.py`. It is not there today, so the verb records
  `distill: unarmed · no join reader · <sha>`, prints `NOTE` naming dScopedBuild, and stays never
  green, because a gone row with no reader is still an empty join. Observed by AC5.
- **S6** — The item armed as unarmed: the `[[stand-in]]` row for `item.deploy.distill` leaves
  `tools/loop/loop.toml` in this landing, this unit's own item having a witness, the record's line.
  The row for `item.build.distill` stays, dScopedBuild's. Observed by AC6.
- **S7** — The docs: `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`, and `help/deploy.md` state the verb, the line and that
  `unarmed` is not green. `KIT_UNATTENDED_VERSION` moves. NOT OBSERVED by a criterion: prose, read by
  the memory hygiene leg at the close.

**Build-run preconditions**: `read_stand_ins` and the `item.build.distill` stand-in row
(TOOL-dDeclaredLoop-13 S8), the `item.deploy.distill` row (TOOL-dDeclaredLoop-12 S2),
`set_landing_field` and `read_landing` (DEPL-dShippedRelease-1).

## 3. Non-goals (OUT)

- The armed join, its rows-missing patch and its (build, fork id) key: dScopedBuild's, with no spec to
  cite; §8 F2 names what it must supply.
- `build.distill` itself, and any decision-log writer.
- `deploy.recommend`, the next item: TOOL-dDeclaredLoop-22's.
- Calling the verb in order: `run_deploy_items`, DEPL-dShippedRelease-4's.
- Reading the decision log. An unarmed item reads nothing, so a planted log row changes no output.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing` and `set_landing_field`, the record the line lands on; with no record the verb exits 1 naming `absent`
- **hands-off** external — dScopedBuild supplies `read_distill_join(build, sha)` and deletes the `item.build.distill` stand-in row in one landing, TOOL-dDeclaredLoop-13's arming rule
- **consumes-from** external — TOOL-dDeclaredLoop-13's `read_stand_ins` and -12's `item.deploy.distill` row, specced and unbuilt at this base

## 4. Design

### Evidence

- Nothing at this base writes a decision-log row for a build: `git grep -n "build.distill" -- tools`
  prints nothing at `5d1c82ac`. PINNED at that sha.
- `test.seed`'s grammar is `# unarmed · <reason> · <sha>` (TOOL-dWitnessedBar-15 S2), a line that says
  what was not measured and at which commit; a rerun treats it as absent.
- The route is flow-steps:440 and its note at :448-450; flow-steps:105-109 states the general rule, "A
  command with no tool today is unarmed ... it records that it ran nothing, is never green, and the
  route goes on".
- A stand-in row is `item` and `owner` (TOOL-dDeclaredLoop-13 §4), and `read_stand_ins` is its reader.

### The line

```
distill: unarmed · stand-in dScopedBuild · 4f1c9e2a…
distill: unarmed · no join reader · 4f1c9e2a…
```

The field's value is the text after `distill: `, the shared interface I2. It carries the full SHA, so
a copied line says which landing measured nothing. A `·`-separated grammar with three parts, parsed by
`check_distill_field` and by nothing else.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `run_deploy_distill`, `check_distill_field`, `derive_distill_line` | functions, `deploy_items.py` | `py.function`, each answered OK by `--suggest` at `5d1c82ac` |
| `--deploy distill` | driver verb | none |
| `python deploy_items.py check-distill` | CLI verb | none |
| `distill-unarmed`, `distill-empty-join`, `distill-idempotent`, `distill-no-reader` | fixture cases of `deploy_fixture.py` | none |

### Migration

None. The field exists from DEPL-dShippedRelease-1, written `pending`.

### Rollout

Live with the record. Nothing it does is a gate: the verb has no red route of its own, and S3's red is
a defect in the program, seen at the read-back and by the fixture.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3, S4, S5
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/loop/loop.toml`: S2's witness, S6
- `tools/unattended/unattended.sh`: the verb, `KIT_UNATTENDED_VERSION`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: S7
- `help/deploy.md`: S7

### Alternatives rejected

- **Reading the decision log and reporting zero rows.** Rejected by M3's counter-rule and the clause:
  a read that returns nothing cannot tell "no major forks" from "nothing wrote". Test: the clause's
  planted case, an empty join read green.
- **Omitting the item until dScopedBuild lands.** Rejected: `item.deploy.distill` is an owned node and
  flow-steps:448 says the item runs unarmed. Test: `carries.py --report`'s owned-node list.
- **A new status word on the record, `skipped`.** Rejected: FK-4-8 fixes the reading to `test.seed`'s
  unarmed, and a second word would be a second grammar. Test: TOOL-dWitnessedBar-15 S2's line.

## 5. Production-readiness checklist

- security — N/A: no new write path beyond `set_landing_field`, and the line holds only a row's owner and a SHA.
- perf / scale — one TOML read and one field write per landing.
- error / empty / loading states — a landing with no record exits 1 `absent`; the empty join is the
  whole subject of S3.
- observability — the line is printed and is on the record; `NOTE` names the missing reader.
- risks — a retired row with no reader keeps reading unarmed for ever: S5's `NOTE` is what surfaces it,
  and dScopedBuild's unit owes the reader.
- testing — `deploy_fixture.py`, one case per criterion.
- migration — none.
- user docs — `help/deploy.md`, `memory/guides/UNATTENDED-VERBS.md`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case distill-unarmed` runs `--deploy distill` with the
  `item.build.distill` stand-in row present, it prints `distill: unarmed · stand-in dScopedBuild · <sha>`,
  exits 0, and `read-landing` prints that value on the `distill` line.
  Red when: the item writes nothing, or stops the route.
- **AC2** — When `python deploy_fixture.py --case distill-empty-join` plants a record whose `distill`
  reads `confirmed` over a log with no rows, `python deploy_items.py check-distill <sha>` exits 1 printing
  `empty join read green`; with the verb's own `unarmed` value it exits 0.
  Red when: the planted empty join reads green, the clause's seen-red case.
- **AC3** — When `grep -n "item.deploy.distill" -A12 loop.toml` runs at the pass, the row's `routes` send
  `unarmed` to `item.deploy.recommend` and no route of an `unarmed` outcome reads `transition`.
  Red when: unarmed routes anywhere but on, or the row lacks the outcome.
- **AC4** — When `python deploy_fixture.py --case distill-idempotent` runs the verb twice, the ref's tip
  is the same commit after each.
  Red when: a re-run grows the record's history.
- **AC5** — When `python deploy_fixture.py --case distill-no-reader` removes the `item.build.distill`
  row from the fixture's table, the verb records `unarmed · no join reader` and prints `NOTE` naming
  dScopedBuild.
  Red when: a retired row with no join reads as confirmed.
- **AC6** — When `grep -c 'item = "item.deploy.distill"' loop.toml` runs at the pass, it prints 0, and the
  same count for `item.build.distill` prints 1.
  Red when: the item's stand-in row outlives it, or dScopedBuild's row went with it.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit version markers` · `recall floor` · `recall floor arms`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC4 AC5 · the four `distill-` cases, the failing case `distill-empty-join` staged against `check_distill_field` with the unarmed test removed · none

## 8. Open questions

- **F1 — How does the item know it is unarmed?** Options: (a) the `[[stand-in]]` row for
  `item.build.distill`; (b) a constant in `deploy_items.py`; (c) a policy key. (b) outlives the row
  and (c) is a key no clause names. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, scout A's
  row 2 and shared interface I2; the row is the one fact. widens: none · relaxes: none
- **F2 — What is specified of the armed path, with no spec of dScopedBuild to cite?** Options: (a) as
  far as the stand-in row's retirement, S5, naming the reader dScopedBuild supplies; (b) spec the join
  on (build, fork id) now. (b) is the surface of a later build, which the packet's Non-goals forbid.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, the packet's Non-goals and "Later builds
  named". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 2, flow-steps:105-109, :440 and :448-450,
  shared interface I2, and scout A's row 2.

## 10. Reuse audit

The seams are `read_stand_ins` (TOOL-dDeclaredLoop-13 S8, unbuilt) for the armed test,
`set_landing_field` and `read_landing` (DEPL-dShippedRelease-1) for the write, and `test.seed`'s
unarmed grammar (TOOL-dWitnessedBar-15 S2) for the line. `python tools/codebase-map/reuse_lookup.py
"record that a check measured nothing and never read an empty population as green"` returned name-stem
neighbours (`check`, `population`, `check_line`, `records`); `population` in
`tools/govkit/refusal_join.py` reads a different thing, so no shipped seam fits and the grammar is a
spec-level reuse. Scout A's row 2 holds; its "TOOL-dLinkedLibrary-1:145,169" was not re-read, since
nothing here rests on it. The recall probe's hits were this build's scout record and the re-cut's
stand-in table; neither disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "what does a stand-in row do for an item whose owning build has not landed" --terms "stand-in unarmed distill build.distill test.seed never green decision log rows join"`
