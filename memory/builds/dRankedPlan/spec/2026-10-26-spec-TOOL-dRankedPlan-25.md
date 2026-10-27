# TOOL-dRankedPlan-25 — `plan.exit`'s owner disposition counts only for the crossing it was written for

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 5 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-25-deviation-251.md](../build/2026-10-26-build-TOOL-dRankedPlan-25-deviation-251.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-24 TOOL-dRankedPlan-26 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-20 TOOL-dRankedPlan-19 TOOL-dRankedPlan-28 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 5 at HIGH**. It shares item **H4** with findings 21 and 39, which `TOOL-dRankedPlan-24` and
`TOOL-dRankedPlan-26` close. `TOOL-dRankedPlan-10` S4 admits Plan's exit on any disposition record
that names `item.plan.exit` and that `check_disposition_record` admits, and its §3 says a revised plan
"crosses plan.exit again through S4 unchanged". After `TOOL-dRankedPlan-15`'s B6 move back to
`planning`, the first exit's record is still in `build/`, so the revised plan re-enters Design with no
new owner act, under the `request` fallback that every `request` build takes until dWellOiledMachine
lands. This unit bounds `check_plan_exit`'s disposition admission to the current crossing through
`TOOL-dRankedPlan-24`'s reader. It repairs `TOOL-dRankedPlan-10`.

## 2. Scope (IN)

- **S1** — The admission bounded. `check_plan_exit(repo, slug, harness)` (`tools/loop/ratify.py`,
  `TOOL-dRankedPlan-10` S4) takes its disposition record from `read_item_disposition(repo, slug,
  "item.plan.exit")` (`TOOL-dRankedPlan-24` S1), so only a record added after the build's newest
  transition releases the gate. The `met` and `before-placement` admissions are unchanged. This
  supersedes unit 10 S4's "a disposition record … names `item.plan.exit`" and §3's "A revised plan
  crosses `plan.exit` again through S4 unchanged": a revised plan crosses again on a disposition
  written after its B6 move. Observed by AC1 and AC2.
- **S2** — The plants `fallback-reentry` and `codex-reentry` join `ratify.py --fixture --plant <case>`
  (`TOOL-dRankedPlan-10` S7). Each records a first `plan.exit` released by a disposition record, then
  B6 back to `planning`, then a second `plan.exit` move: `fallback-reentry` with no capability table,
  `codex-reentry` with the Codex-shaped row. Observed by AC1 and AC2.
- **S3** — `help/plan.md`'s section "Plan's exit without the intake hook" (`TOOL-dRankedPlan-10` S8)
  says a disposition releases the crossing it follows and no later one. Observed by AC3.

## 3. Non-goals (OUT)

- The bound itself: `TOOL-dRankedPlan-24`'s reader, called and never re-spelled.
- Which Disposition word releases the gate: `TOOL-dRankedPlan-26`'s.
- The driver's hold and release, `TOOL-dRankedPlan-10` S6 through `check_owner_disposition`
  (`TOOL-dDeclaredLoop-31` S6): dDeclaredLoop's owner-gate release, outside this unit.

### Edges

- **consumes-from** `TOOL-dRankedPlan-10` — `check_plan_exit` and its fixture, whose disposition admission S1 re-points; without them there is no gate to bound
- **consumes-from** `TOOL-dRankedPlan-24` — `read_item_disposition`, the one bounded reader S1 calls; without it the bound would be spelled a second time
- **hands-off** `TOOL-dRankedPlan-33` — the `fallback-reentry` and `codex-reentry` plants, which that unit re-runs over the seeded base (spec audit of units 19 to 29, id 21)
- **hands-off** `TOOL-dRankedPlan-35` — `check_plan_exit`'s admission through the reader, where that unit prints a disposition conflict (spec audit of units 19 to 29, id 28)
- **hands-off** `TOOL-dRankedPlan-37` — AC2's second move, spelled `--field harness=codex` by that unit, which observes its harness half at order 18, and the `fallback-reentry` plant it re-runs (spec audit of units 19 to 29, ids 3, 32)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-10` S4 (spec lines 51-56) and §3 last bullet; the audit's appendix rows for ids 5
  and 39 found no recency bound in units 9, 10 and 15.
- `TOOL-dRankedPlan-15` §4 "The flow", steps 3 to 6: B6 to `planning`, the planner's rewrite, the
  ratification "as `plan.ratification` holds the plan's", and `plan.exit`'s second move.
- `TOOL-dRankedPlan-10` §4 "The answer": with no table every harness takes `fallback`, whose only
  release is the owner's disposition.

### The plants

| Plant | Table | First exit | Second exit, no new record | Second exit, new record |
|---|---|---|---|---|
| `fallback-reentry` | none | released by a disposition | exit 1, `plan.exit — held · owner gate · intake not installed` | exit 0, `ratification=intake-not-installed` |
| `codex-reentry` | the Codex-shaped row | released by a disposition | exit 1, the same line | exit 0, `harness=codex` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `fallback-reentry`, `codex-reentry` | `ratify.py` fixture plants | none |

### Rollout

Live at landing. A build at its first crossing behaves as before, since its newest transition is the
move into `planning` and the owner's record follows it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2
- `help/plan.md`: S3's sentence

### Alternatives rejected

- **Bound by the revision number on the B6 trailer.** Only revisions carry it; a backward move by any
  other row would still reuse the old record. The newest transition bounds every re-entry.

## 5. Production-readiness checklist

- security — narrows: each crossing needs its own owner act, which is what the fallback holds for.
- perf / scale — the reader's few `git log` calls per move.
- error / empty / loading states — a stale record reads as none, and the hold line says the gate waits
  for the owner.
- observability — the hold line and the admitted trailer's `ratification=` field.
- risks — an owner who disposed before a B6 must dispose again; the clause asks the revision be
  ratified as the plan is.
- testing — the two re-entry plants, red and green.
- migration — none.
- user docs — `help/plan.md`, S3.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant fallback-reentry` runs, the second move
  `python loop_transition.py record --build tFix --from planning --item item.plan.exit --outcome pass
  --witness <sha>` with no new record exits 1 printing `plan.exit — held · owner gate`, and exits 0 once
  a disposition record is committed after the B6 move.
  Red when: the first crossing's record releases the second.
- **AC2** — When the plant `codex-reentry` runs the same steps, the results are the same and the
  admitted trailer carries `harness=codex`.
  Red when: a Codex-shaped adapter re-enters Design on the old record.
- **AC3** — When `grep -n "crossing it follows" plan.md` runs over the help page, it finds S3's sentence.
  Red when: the page does not say a disposition releases one crossing.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 · the `fallback-reentry` and `codex-reentry` plants under `--fixture`, staged by a `check_plan_exit` that reads every admitted record · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 5 (HIGH, item H4,
  shared with findings 21 and 39), repairing `TOOL-dRankedPlan-10`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-33`, the hands-off edge to `TOOL-dRankedPlan-35`, the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-10` S4's `check_plan_exit`, whose disposition lookup is
re-pointed to `TOOL-dRankedPlan-24` S1's bounded reader; nothing is minted but two plants. No code
exists at base 0689e7fa, where the loop kit is unbuilt. `python tools/codebase-map/reuse_lookup.py
"bound a disposition record lookup to records added after the build's newest transition"` ranked name
stems only, so no existing seam fits beyond the reader this unit consumes. The recall query returned
the audit's H4 item and `TOOL-dRankedPlan-15`'s flow, which agree.

Recall terms used: `python tools/memory-recall/query.py "which disposition record releases a re-entered plan.exit" --terms "disposition record item.plan.exit freshness newest transition B6 revision terminal-command fallback read_transitions"`
