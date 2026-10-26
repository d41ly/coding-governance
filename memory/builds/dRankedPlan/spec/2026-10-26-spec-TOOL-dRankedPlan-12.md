# TOOL-dRankedPlan-12 — `plan.record` declaring the probes owed before Design

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 9 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0380@1e2f59a7 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-11 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

The night pass made testing a program with two ways in, placed at a boundary or raised by a role,
whose record returns to the asking item (point 2,
`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:132-145`), and
dPlacedRequest builds that program (TOOL-dPlacedRequest-7). Nothing lets the planner say, in the plan
it hands Design, which claims must be tested before Design starts: until the role templates carry
the `probe` outcome, "probes are placed, never raised"
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:669`). This unit
gives `plan.record`'s record (I3, TOOL-dRankedPlan-16) a `Probes owed` field (shared interface I17):
each probe the plan owes, raised through `probe.py trigger` with `item.plan.record` as its asker, and
the plan record's check refusing, so `plan.exit` cannot pass, while an owed probe has no returned
`probe` record.

## 2. Scope (IN)

- **S1** — The field: `- **Probes owed:** none`, or entries joined by `; `, each `<kind>: <question>`,
  `<kind>` one of `verification`, `reproduction` or `experiment`, the closed set `probe.py pin
  --kind` takes (TOOL-dPlacedRequest-7 S4), and `<question>` the claim to test, the probe's subject.
  The check in `tools/memory-tree/plan_fields.py` (TOOL-dRankedPlan-13 S1), listed in `FIELD_CHECKS`
  as `Probes owed`, refuses a kind outside the set, an empty question or a repeated question, naming
  each. Observed by AC1.
- **S2** — The raise: `python tools/memory-tree/plan_fields.py probes <slug> --trigger` runs, for
  each entry no `probe-trigger` record of the build answers (S4's match), `python <loop>/probe.py
  trigger --cause raised --asker item.plan.record --subject <question> --build <slug>`
  (TOOL-dPlacedRequest-7 S3), found through `backlog.resolve_kit_dir`
  (`tools/memory-tree/backlog.py:1758`), and prints the trigger's own line: the opened record, or
  `probe — not opened · <key>: <why>` when `probe.raise` refuses the cause. An entry already
  answered is not triggered again. With no loop kit it exits 2 naming it. Observed by AC2 and AC3.
- **S3** — The state: `python tools/memory-tree/plan_fields.py probes <slug>` prints one line per
  entry, `probe owed — <kind> · <question> · <trigger record|not triggered> · <probe record|open> ·
  <verdict|->`, the list the runner of `item.probe.pin` reads each entry's `--kind` from. Observed by
  AC4.
- **S4** — The check's second half, the owed-before-Design rule: an entry is returned when a
  `probe-trigger` record of the build carries `Asker: item.plan.record` and `Subject` equal to the
  entry's question, and a `probe` record whose `Trigger` names that trigger record carries a
  `Verdict` (TOOL-dPlacedRequest-7 S6's fields), both read through the record-file factory's reader
  (PLAY-dOrderedCharter-7 S7). The check refuses each entry not returned, naming it `not triggered`
  with the remedy `plan_fields.py probes <slug> --trigger`, or `open`; and an entry whose `probe`
  record's `Kind` differs from its declared kind, naming both. Any verdict returns the entry: a probe
  gates nothing past the item that asked (flow-steps.md:641), and its record is the planner's input
  on re-entry. Observed by AC4.
- **S5** — The gate at `plan.exit`. S4 is part of `plan_fields.py check`, which TOOL-dRankedPlan-13
  S9 joins to the plan-record schema check, `item.plan.record`'s witness; `plan.exit` needs every
  reached item's witness (flow-steps.md:190), so it cannot pass while a declared probe is unreturned.
  Observed by AC5.
- **S6** — The declaration: the memory-tree kit's `loop` `requires_if` row (TOOL-dRankedPlan-11 S5)
  names `probe.py`'s subprocess run in its `why`. NOT OBSERVED by a criterion: `govkit selfcheck`
  grades the row at the close.
- **S7** — The plants `probes-shape`, `probes-trigger`, `probes-refused`, `probes-state` and
  `probes-schema` join `plan_fields.py --fixture`, run by the `plan-fields selftest` leg, with a stub
  `probe.py` that records each argv and writes or refuses the trigger record as planted. Observed by
  AC1 to AC5.
- **S8** — `help/plan.md`'s section "The plan record's intent fields" (TOOL-dRankedPlan-13 S11) gains
  `Probes owed`: its grammar, `probes --trigger`, what returns an entry, and what `probe.raise`'s
  values do to a planner-raised probe. Observed by AC6.

## 3. Non-goals (OUT)

- The probe program: its items, `probe.py`'s verbs, the `probe` and `probe-trigger` record kinds and
  the four `probe.*` keys are TOOL-dPlacedRequest-7's, called here.
- Pinning, designing, running and judging a probe: the program's items after `item.probe.trigger`.
- A new trigger cause: the planner's declaration raises through the closed set's `raised` (§8 F1).
- The `probe` outcome on the role templates: dFurnishedOrders' `cl-dClosedLoop-0206`, beside which
  this field stays the plan's own record of what it owes.
- Firing the raise at `plan.record`'s outcome: the executor's, dWellOiledMachine's; S4's refusal names
  the verb until then.

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `record-kind.plan`, the plan record whose `Probes owed` field this unit defines
- **consumes-from** `TOOL-dRankedPlan-13` — `plan_fields.py`, the module, its `FIELD_CHECKS` table, its fixture and the schema check join this unit's field rides
- **consumes-from** `TOOL-dRankedPlan-11` — `requires_if`, the memory-tree kit's `loop` row whose `why` S6 extends
- **consumes-from** external — dPlacedRequest: `probe.py trigger`, the `probe` and `probe-trigger` record kinds and their fields, and `probe.raise` (TOOL-dPlacedRequest-7 S3, S4, S6, S9); the record-file factory's reader (PLAY-dOrderedCharter-7 S7); each DEFERRED at base and re-grounded on its landed code
- **hands-off** external — dWellOiledMachine's executor runs `plan_fields.py probes <slug> --trigger` at `plan.record`'s outcome and launches the program's items `next` returns
- **hands-off** `TOOL-dRankedPlan-19` — the `Probes owed` check, whose refusal that unit makes hold `plan.exit` through the plan record's witness (round-1 spec audit, id 1)
- **hands-off** `TOOL-dRankedPlan-29` — the `Probes owed` check's entry split, which that unit's S39 corrects (round-1 spec audit, id 49)

## 4. Design

### Evidence

- `probe.points` stands in the catalogue at base with default `[]`
  (`tools/policy/catalogue.toml:679-683`), and TOOL-dPlacedRequest-7 §4's refusal table refuses the
  `point` cause when `--at` is not in it; `probe.raise` defaults to `roles-and-owner` (:686-689) and
  refuses `raised` only under `owner-only` and `off`.
- TOOL-dPlacedRequest-7 S3's causes are the closed set `point`, `owner`, `observation`, `raised` and
  `reproduction`, held as `[[trigger-cause]]` rows of `tools/loop/loop.toml`.
- The `probe-trigger` record carries `Cause`, `Asker`, `Subject`, `At` and `Key`; the `probe` record
  `Sha`, `Kind`, `Question`, `Losing`, `Asker`, `Trigger`, `Verdict` and `Writer`
  (TOOL-dPlacedRequest-7 S6 and §4 "The records").

### The field and its state

```
- **Probes owed:** verification: does the card keep its route after a compaction?; experiment: which of two triage rule sets labels more asks?

probe owed — verification · does the card keep its route after a compaction? · 2026-10-27-build-TOOL-dX-1-probe-trigger-1 · 2026-10-27-build-TOOL-dX-1-probe-1 · confirmed
probe owed — experiment · which of two triage rule sets labels more asks? · not triggered · open · -
```

### Under each value of `probe.raise`

| Value | `--trigger` | The check, until the entry returns |
|---|---|---|
| `roles-and-owner` | opens the probe | `open` |
| `owner-only` | `probe — not opened · probe.raise: …` | `not triggered`; the owner may raise it with `--cause owner` and the same subject, which S4 matches |
| `off` | `probe — not opened · probe.raise: …` | `not triggered`; the plan record is amended to leave the entry out |

S4 matches on the asker and the subject, not the cause, so an owner-raised probe answers the entry
the planner declared.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `Probes owed` | plan record field | none |
| `check_probes_owed` | function in `plan_fields.py` | `py.function`, asked at the pass |
| `probes`, `--trigger` | verb and flag of `plan_fields.py` | none |
| plants `probes-shape`, `probes-trigger`, `probes-refused`, `probes-state`, `probes-schema` | fixture cases | none |

### Migration

None: no plan record exists before TOOL-dRankedPlan-16 lands the kind.

### Rollout

Live at landing for every plan record checked after it; a plan owing `none` is unaffected.

### Files touched (estimate)

- `tools/memory-tree/plan_fields.py`: S1 to S4, S7's plants
- `tools/memory-tree/kit.toml`: S6's `why`
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION`
- `help/plan.md`: S8

### Alternatives rejected

- **Trigger inside `check`.** A check that writes records answers differently on its second run;
  `--trigger` is the one writing verb, and the check names it as its remedy.
- **The plan record lists trigger record names.** The trigger's file name is minted by the probe
  program; S4 derives the join from the asker and the subject both records already carry.

## 5. Production-readiness checklist

- security — `--trigger` writes only through `probe.py trigger`, the program's own door, with an argv
  list; the question reaches it as one argument, never through a shell.
- perf / scale — one record read per owed probe; a plan owes few.
- error / empty / loading states — `none` owes nothing; a refused cause and a missing loop kit each
  print their cause; a re-run triggers nothing already answered.
- observability — S3's line per entry, and the trigger's own line per raise.
- risks — the factory's reader call and the trigger record's subject field are re-grounded on the
  landed kits; two entries with one question are refused by S1, so S4's match is one-to-one.
- testing — S7's five plants, red and green.
- migration — none.
- user docs — `help/plan.md`, S8.

## 6. Acceptance criteria

- **AC1** — When `python plan_fields.py --fixture --plant probes-shape` runs `check tFix --field
  "Probes owed"` over `verification: does X hold?; guess: y; reproduction: ; verification: does X
  hold?`, it exits 1 naming the kind `guess`, the empty question and the repeated question; over
  `none` it exits 0.
  Red when: a kind outside the three, or an empty question, passes.
- **AC2** — When the plant `probes-trigger` runs `probes tFix --trigger` over two entries, the stub
  `probe.py` records two calls, each `trigger --cause raised --asker item.plan.record --subject <the
  entry's question> --build tFix`; run again, it records none.
  Red when: an entry is triggered twice, or with another cause or asker.
- **AC3** — When the plant `probes-refused` sets the stub to refuse `raised` as `probe.raise:
  owner-only` does, `probes tFix --trigger` prints `probe — not opened · probe.raise` and `check tFix
  --field "Probes owed"` exits 1 naming the entry `not triggered` and `plan_fields.py probes tFix
  --trigger`; after the plant writes an owner-caused trigger and a `probe` record with `Verdict:
  confirmed` for that subject, the check exits 0.
  Red when: a refused raise reads as owed-and-met, or an owner-raised probe does not answer the entry.
- **AC4** — When the plant `probes-state` holds one entry with a trigger record and no `probe` record,
  one with both and `Verdict: refuted`, and one whose `probe` record says `Kind: experiment` against a
  declared `verification`, `probes tFix` prints `open`, `refuted` and the third's records, and the
  check exits 1 naming the first as `open` and the third's two kinds, not the second.
  Red when: an open probe passes, a refuted one refuses, or a kind mismatch passes.
- **AC5** — When the plant `probes-schema` runs the plan-record schema check over AC4's open entry, it
  fails naming `Probes owed` from `plan_fields.py check`; once the probe returns, it passes.
  Red when: the schema check, and with it `plan.exit`, passes while a declared probe is open.
  fixture: the schema check's module is TOOL-dRankedPlan-16's, joined by TOOL-dRankedPlan-13 S9.
- **AC6** — When `grep -n "Probes owed" plan.md` runs over the help page, it finds S8's text naming
  `--trigger` and `probe.raise`.
  Red when: the page does not describe the field.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck`

New arm: tools/memory-tree/plan_fields.py · covers AC1 AC2 AC3 AC4 AC5 · the five `probes-*` plants under the `plan-fields selftest` leg, staged by an open probe the check passes · none

## 8. Open questions

- **F1 — Which trigger cause does a planner-declared probe raise with?** Options: (a) `point` with
  `--at item.plan.exit`, the brief's proposed I17; (b) `raised` with `--asker item.plan.record`; (c)
  `owner`; (d) a new `[[trigger-cause]]` row `plan`. (a) loses: `point` is refused while `--at` is not
  in `probe.points`, whose default is `[]` (`tools/policy/catalogue.toml:679-683`), so under the
  default no declared probe would open. (c) loses: it records an owner request the owner never made.
  (d) needs a refusal rule in `probe.py`, a change to dPlacedRequest's program. RESOLVED (agent,
  2026-10-26, delegated): (b), rung 3, the most feature-rich survivor: the planner is the role raising
  the probe from its own item, `next` returns the program's items while that item waits
  (flow-steps.md:621), and `probe.raise`'s default admits it while its two narrower values hold as
  §4's table says. It refines I17, whose owner this unit is. widens: none · relaxes: none
- **F2 — Is `plan.exit` refused while an owed probe is open?** RESOLVED (agent, 2026-10-26,
  delegated): yes, rung 1: the clause owes the probes "before Design", and S5 refuses through the
  plan-record schema check `plan.exit` needs, not a second gate. widens: none · relaxes: none
- **F3 — Does a probe's verdict gate the plan?** Options: (a) any verdict returns the entry; (b) only
  `confirmed` or `measured` does. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1: "A probe
  gates nothing past the item that asked" (flow-steps.md:641); a refuted claim is the planner's input
  to revise the plan, which the plan record's re-entry carries. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 12, night-pass.md:118-175 (point 2),
  flow-steps.md:180-190 and :604-675, TOOL-dPlacedRequest-7 S3, S4, S6 and S9 and its refusal table,
  and scout A's row 5.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-19`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended: TOOL-dPlacedRequest-7's `probe.py trigger` and its two record kinds, called
through their door and read through the record-file factory, never restated; TOOL-dRankedPlan-13's
`plan_fields.py`, whose `FIELD_CHECKS` table gains one entry and whose schema check join carries the
gate; `backlog.resolve_kit_dir` (`tools/memory-tree/backlog.py:1758`, verified at base) to find the
loop kit. `python tools/codebase-map/reuse_lookup.py "refuse a step exit while a declared probe or
test has no recorded verdict"` ranked name stems (`probe`, `has`, `records`, `declares`); none gates on
a probe record, and no probe program exists at base, matching scout A's row 5 ("Nothing"). Where the
brief and source disagree: I17 proposed `--cause point --at item.plan.exit`, which the catalogue's
`probe.points` default at base refuses (§8 F1). The recall query returned scout A's row 5 and
TOOL-dPlacedRequest-7's spec brief rows; no record decided the cause.

Recall terms used: `python tools/memory-recall/query.py "how does the plan record declare probes owed before Design starts" --terms "probes owed probe.trigger probe record plan.record plan.exit probe.points probe.raise trigger-cause asker verdict"`
