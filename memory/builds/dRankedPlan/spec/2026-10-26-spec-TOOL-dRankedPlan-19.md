# TOOL-dRankedPlan-19 — `plan.exit` admits a move only over a witnessed plan record

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 10 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-19-deviation-191.md](../build/2026-10-26-build-TOOL-dRankedPlan-19-deviation-191.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-1-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-20 TOOL-dRankedPlan-28 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 1 at BLOCKER**, item **B1**. `TOOL-dRankedPlan-12` S5 and §8 F2, and `TOOL-dRankedPlan-13`
S9, say `plan.exit` cannot pass while an owed probe is unreturned or a field check refuses, because
"plan.exit needs every reached item's witness" (flow-steps.md:190). The gate that admits Plan's exit
is `TOOL-dRankedPlan-10` S4's `check_plan_exit`, which admits on the ratification answer, the
pre-placement exemption or a disposition record, and never reads `item.plan.record`'s witness. No
unit builds the rule, so unit 12's AC5 names a red that nothing produces. This unit gives the rule
its one owner: `check_plan_exit` refuses every move while `plan_record.py check <slug>` answers
`unwitnessed`, so the field checks units 11 to 13 join into that witness hold the exit. It repairs
`TOOL-dRankedPlan-12`, whose claim it makes true, and so sits one order above it.

## 2. Scope (IN)

- **S1** — The precondition. `check_plan_exit(repo, slug, harness)` (`tools/loop/ratify.py`,
  `TOOL-dRankedPlan-10` S4) first runs `python <memory-tree kit>/plan_record.py check <slug>`
  (`TOOL-dRankedPlan-16` S3), the kit found through the loop kit's inline `resolve_kit_dir` block,
  the route `TOOL-dRankedPlan-13` S8 takes to `plan_fields.py`. On `item.plan.record — witnessed ·
  <path>` it goes on to unit 10's admissions unchanged. On `item.plan.record — unwitnessed · <why>`
  it refuses `plan.exit — held · item.plan.record unwitnessed · <why>`. On any other exit or output,
  or with no memory-tree kit, it refuses `plan.exit — held · item.plan.record unread · <cause>`. The
  precondition holds before every admission: `met`, `before-placement` and a disposition record
  alike. Observed by AC1, AC2 and AC3.
- **S2** — The move. `write_transition`'s call of S1 (`TOOL-dRankedPlan-10` S5) exits 1 on the
  refusal before anything is written, so `loop_transition.py record --item item.plan.exit` is the
  observation, and the driver's plan gate (`TOOL-dRankedPlan-10` S6) reads the same refusal through
  `ratify.py <slug> --exit`, whose `met` line S1 also withholds. Observed by AC1 and AC4.
- **S3** — The plants `plan-record-open-probe`, `plan-record-absent` and `plan-record-unread` join
  `python tools/loop/ratify.py --fixture --plant <case>` (`TOOL-dRankedPlan-9` S7, extended by
  `TOOL-dRankedPlan-10` S7), each over the `claude-adapter` table so the ratification answer is `met`
  and only S1 can hold the move. Observed by AC1, AC2 and AC3.
- **S4** — The claim this unit makes true, stated where its readers look: `TOOL-dRankedPlan-12` S5
  and §8 F2 and `TOOL-dRankedPlan-13` S9 hold through S1, and the rule enforced is
  `item.plan.record`'s witness. `help/plan.md`'s section "Plan's exit without the intake hook"
  (`TOOL-dRankedPlan-10` S8) gains one paragraph: Plan's exit needs the plan record witnessed, and an
  owed probe, a refused field or a missing record holds it whatever the ratification. Observed by AC5.

## 3. Non-goals (OUT)

- The witnesses of the other Plan items. flow-steps.md:190 names "every item the run reached"; the
  reached set is `TOOL-dDeclaredLoop-7`'s `derive_position`, and the dedupe and triage witnesses are
  armed by `TOOL-dRankedPlan-3` at this unit's own order. §8 F2 records the cut.
- Any field check. Probes, read sets, scope, systems, forks and scenario are units 11 to 14's, reached
  through `check_plan_record`, which this unit calls and never edits.
- The ratification answer, the fallback and the disposition lookup: units 9 and 10, and the repairs
  `TOOL-dRankedPlan-25` and `TOOL-dRankedPlan-26` make to them at order 5.

### Edges

- **consumes-from** `TOOL-dRankedPlan-10` — `check_plan_exit` and `write_transition`'s call of it, the gate S1 adds its precondition to; without it no move reads the plan record at all
- **consumes-from** `TOOL-dRankedPlan-16` — `plan_record.py check`, `item.plan.record`'s witness line S1 reads; without it there is no witness to require
- **consumes-from** `TOOL-dRankedPlan-12` — the `Probes owed` check inside `check_plan_fields`, whose refusal on an open probe is the case AC1 drives through the real move
- **consumes-from** `TOOL-dRankedPlan-13` — S9's call of `check_plan_fields` inside `check_plan_record`, which carries the field refusals into the witness S1 reads
- **hands-off** `TOOL-dRankedPlan-33` — S1's witnessed-record precondition and the three `plan-record-*` plants, around which that unit seeds every other plant of the shared fixture (spec audit of units 19 to 29, id 21)
- **hands-off** `TOOL-dRankedPlan-37` — AC2's `pre-placement` variant, which that unit reconciles with unit 10 AC6, and the plants whose memory-tree reads it adds to the `loop selftest` guard (spec audit of units 19 to 29, ids 32, 11)

## 4. Design

### Evidence

- flow-steps.md:190 gives `plan.exit`'s need as "every item the run reached" and its witness as "the
  transition record over the reached items' witnesses"
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`).
- `TOOL-dRankedPlan-10` S4 admits on S3 `met`, on `TOOL-dDeclaredLoop-53` S2's exemption, or on a
  disposition record, and its S5 wires only S4 into `write_transition`; the audit's appendix row for
  id 1 found no other unit building the rule.
- `TOOL-dRankedPlan-16` S3 prints `item.plan.record — witnessed · <path>` or `— unwitnessed · <why>`,
  exit 0 either way, so the gate reads the line, never the exit code alone.
- `TOOL-dRankedPlan-13` S9 has `check_plan_record` call `check_plan_fields`, which carries every
  `FIELD_CHECKS` entry, `TOOL-dRankedPlan-12`'s `Probes owed` among them.

### The order of the checks

```
check_plan_exit(repo, slug, harness)
  witness = run plan_record.py check <slug>         # S1, first, for every crossing
  witness is not "witnessed"   -> held · item.plan.record unwitnessed|unread · <why>
  then TOOL-dRankedPlan-10 S4 as it stands: met | before-placement | disposition | held
```

### The plants

| Plant | Plan record | Probe records | Expected |
|---|---|---|---|
| `plan-record-open-probe` | eleven fields, `Probes owed: verification: the view lists dX first` | none | refused, `unwitnessed · plan field — Probes owed: …`; admitted once a `probe-trigger` and a `probe` record with a `Verdict` are committed |
| `plan-record-absent` | none | none | refused, `unwitnessed`, under `met` and under `pre-placement` |
| `plan-record-unread` | eleven fields | none | the fixture's loop kit resolves no memory-tree kit; refused, `unread` |

The probe records are planted as files in the `fields` form the factory reads, so the plant needs no
`probe.py` and runs `TOOL-dRankedPlan-12` S4's match as written.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `plan-record-open-probe`, `plan-record-absent`, `plan-record-unread` | fixture plants of `ratify.py` | none |

No function is minted: S1 is a precondition inside `check_plan_exit`.

### Rollout

Live at landing. A build in `planning` with no plan record is held at Plan's exit until its planner
writes one, which `item.plan.record` asks of every Plan run.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S3
- `help/plan.md`: S4's paragraph

### Alternatives rejected

- **Units 12 and 13 drop the claim and name another gate.** No other gate reads the plan record
  before Design, so the field checks would hold nothing; the audit's fix names this as the weaker
  option.
- **A second gate beside `check_plan_exit` in `write_transition`.** Two readers of one exit would
  each print half the reason; the precondition belongs in the one gate unit 10 owns.

## 5. Production-readiness checklist

- security — narrows: a move that passed unit 10's admissions is now also refused on an unwitnessed
  record. No new write path.
- perf / scale — one subprocess per `plan.exit` move.
- error / empty / loading states — a missing record, a refusing field and an unresolved kit each
  refuse with their own line; none fails open.
- observability — the refusal names the item and the witness's own reason.
- risks — a build in `planning` opened before the plan kind landed is held until its record exists,
  which is the item the step asks of it.
- testing — the three plants, red and green.
- migration — none.
- user docs — `help/plan.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant plan-record-open-probe` runs, the move
  `python loop_transition.py record --build tFix --from planning --item item.plan.exit --outcome pass
  --witness <sha>` exits 1 printing `plan.exit — held · item.plan.record unwitnessed` and `Probes
  owed`; after the plant commits the trigger and probe records, the same move exits 0.
  Red when: the move reaches `designing` while the declared probe is open, or stays held once it
  returns.
- **AC2** — When the plant `plan-record-absent` runs the same move, it exits 1 printing
  `item.plan.record unwitnessed`, and so does the `pre-placement` variant of the plant.
  Red when: a build with no plan record crosses Plan's exit on `met` or on the exemption.
- **AC3** — When the plant `plan-record-unread` runs the same move, it exits 1 printing
  `item.plan.record unread` and naming the memory-tree kit.
  Red when: an unresolved kit admits the move.
- **AC4** — When `python ratify.py tFix --exit --harness claude-code` runs under the
  `plan-record-absent` plant, it prints no `met` line.
  Red when: the driver's plan gate reads `met` for a build the move refuses.
- **AC5** — When `grep -n "item.plan.record" plan.md` runs over the help page, it finds S4's paragraph
  in the section "Plan's exit without the intake hook".
  Red when: the page does not say the exit needs the plan record witnessed.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 AC4 · the three `plan-record-*` plants under `--fixture`, staged by a `check_plan_exit` that admits on `met` before reading the witness · none

## 8. Open questions

- **F1 — Does the precondition hold for a build `TOOL-dDeclaredLoop-53` exempts from the owner
  gate?** Options: (a) yes, every crossing; (b) only where the owner gate is held. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1: flow-steps.md:190 makes the reached items' witnesses the
  witness of every `plan.exit`, and `TOOL-dDeclaredLoop-53` S2 exempts the owner gate alone.
  widens: none · relaxes: none
- **F2 — Which reached items does the gate read?** Options: (a) `item.plan.record`'s witness, the
  one units 12 and 13 name; (b) every Plan item the run reached, through `derive_position`'s reached
  set and `read_plan_item_witness`. (b) needs the dedupe and triage witnesses `TOOL-dRankedPlan-3`
  arms at this unit's own order, which M6 clause 2 forbids a parallel unit to depend on, and a reached
  set no Plan unit reads yet. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, tie-broken by
  fewer open questions; (b) stays a follow-up beside §3's first bullet. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 1 (BLOCKER, item
  B1), repairing `TOOL-dRankedPlan-12`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-33`, the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-10` S4's `check_plan_exit`, which gains one precondition, read
from `TOOL-dRankedPlan-16` S3's existing witness verb through the kit route `TOOL-dRankedPlan-13` S8
already takes; nothing is minted. No code exists at base 0689e7fa, since the loop kit is
dDeclaredLoop's and unbuilt there. `python tools/codebase-map/reuse_lookup.py "require an item witness
before a step exit transition is admitted"` ranked name stems only (`before`, `step`,
`require_adopted_root`, `wit`); none gates a transition, so no existing seam fits beyond the gate this
unit extends. The recall query returned the audit's B1 item and `TOOL-dRankedPlan-12`'s S5, which
agree with the specs read.

Recall terms used: `python tools/memory-recall/query.py "what must hold before plan.exit admits the move into Design" --terms "plan.exit check_plan_exit plan.record witness probes owed check_plan_record reached items transition"`
