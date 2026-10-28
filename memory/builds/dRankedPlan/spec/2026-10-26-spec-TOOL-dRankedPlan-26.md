# TOOL-dRankedPlan-26 — a disposition of `ask` or `none` keeps `plan.exit` shut

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 5 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-26-deviation-261.md](../build/2026-10-26-build-TOOL-dRankedPlan-26-deviation-261.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-67 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-20 TOOL-dRankedPlan-19 TOOL-dRankedPlan-28 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 39 at HIGH**. It shares item **H4** with findings 5 and 21, which `TOOL-dRankedPlan-25` and
`TOOL-dRankedPlan-24` close by bounding the lookup to the current crossing. Finding 39 adds the second
half the audit's fix names: `TOOL-dRankedPlan-10` S4's gate and `TOOL-dRankedPlan-9` S4's
`terminal-command` arm release on any record `check_disposition_record` admits, and that check grades
only membership in the item's outcome set, which for an item declaring `outcomes = "dispositions"` is
placement's nine and holds `ask` and `none` (`TOOL-dDeclaredLoop-16` S1, S5). An owner who answers
`ask`, deferring the decision, or `none` would release Plan's exit. This unit names the two holding
words and has both readers refuse a record carrying one. It repairs `TOOL-dRankedPlan-10`.

## 2. Scope (IN)

- **S1** — The words. `HOLDING_DISPOSITIONS = ("ask", "none")` in `tools/loop/ratify.py`, and
  `check_releasing_disposition(fields)`, true when the record's `Disposition`, resolved through
  `resolve_disposition` (`TOOL-dDeclaredLoop-16` S2) so the alias `defer` reads `ask`, is not in it.
  Observed by AC1 and AC3.
- **S2** — The gate. `check_plan_exit` (`TOOL-dRankedPlan-10` S4) refuses when the disposition record
  it took is not releasing, `plan.exit — held · owner gate · disposition <word> holds`, and admits on
  any other admitted word. The record it takes is the newest, so the owner's latest word governs.
  Observed by AC1 and AC2.
- **S3** — The predicate. `read_plan_ratification`'s `terminal-command` arm (`TOOL-dRankedPlan-9` S4)
  answers unratified, `disposition <word> holds`, for a `terminal` record that is not releasing.
  Observed by AC3.
- **S4** — The plants `holding-ask`, `holding-defer` and `holding-none` join `ratify.py --fixture
  --plant <case>`: a fresh disposition for `item.plan.exit` carrying the word, under the `no-table`
  fallback, then a `terminal` one under `terminal-command`. Observed by AC1 to AC3.

## 3. Non-goals (OUT)

- The freshness bound: `TOOL-dRankedPlan-24` and `TOOL-dRankedPlan-25`.
- `item.plan.exit`'s declared outcome set: `TOOL-dDeclaredLoop-12`'s row. S1 holds whichever set it
  declares, since a word outside it never reaches S2.
- Any other gate's reading of a disposition: dDeclaredLoop's owner-gate release
  (`TOOL-dDeclaredLoop-31` S6) and `TOOL-dRankedPlan-4`'s moves keep their own word rules.

### Edges

- **consumes-from** `TOOL-dRankedPlan-10` — `check_plan_exit`, whose disposition admission S2 holds on a holding word; without it there is no gate to hold
- **consumes-from** `TOOL-dRankedPlan-9` — `read_plan_ratification`'s `terminal-command` arm, which S3 holds on a holding word
- **hands-off** `TOOL-dRankedPlan-33` — the `holding-ask` plant, which that unit re-runs over the seeded base (spec audit of units 19 to 29, id 21)
- **hands-off** `TOOL-dRankedPlan-35` — S2's "the owner's latest word governs", which that unit defines by ancestry and holds on a conflict (spec audit of units 19 to 29, id 28)

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-16` S1: the set is `continue`, `amend`, `new`, `patch`, `repeat`, `unit`,
  `breakpoint`, `ask` and `none`; S2 maps `defer` to `ask`; S5 checks membership only.
- `TOOL-dRankedPlan-10` S4 and `TOOL-dRankedPlan-9` S4 each release on a record
  `check_disposition_record` admits. The audit's appendix row for id 39 states that `item.plan.exit`'s
  declared set was not confirmed: UNVERIFIED at base 0689e7fa, where `TOOL-dDeclaredLoop-12`'s rows are
  unbuilt. S1 is correct under either set.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_releasing_disposition` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest check_releasing_disposition --as py.function` answered OK |
| `HOLDING_DISPOSITIONS` | constant, `ratify.py` | none declared |
| `holding-ask`, `holding-defer`, `holding-none` | `ratify.py` fixture plants | none |

### Rollout

Live at landing. `TOOL-dRankedPlan-25` shares `check_plan_exit` at this order and changes which record
is taken; S2 judges the record taken, so the two changes compose in either sequence.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S4

### Alternatives rejected

- **The word filter inside `TOOL-dRankedPlan-24`'s reader.** The reader then skips an `ask` and returns
  an older `amend` the owner has since deferred; the newest word must govern, so the filter judges the
  record the reader returns.
- **An allow-list of releasing words.** The set is dDeclaredLoop's and may grow; the two holding words
  are the ones whose meaning is "not yet".

## 5. Production-readiness checklist

- security — narrows: a deferral can no longer open the gate.
- perf / scale — one comparison per lookup.
- error / empty / loading states — the hold line names the word.
- observability — the hold line and the predicate's unratified reason.
- risks — none beyond the hold the owner asked for.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — `help/plan.md`'s fallback section already says the owner's disposition releases
  the gate; a deferral releasing nothing needs no new reader-facing rule.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant holding-ask` runs, the move `python
  loop_transition.py record --build tFix --from planning --item item.plan.exit --outcome pass --witness
  <sha>` exits 1 printing `disposition ask holds`, and the plant's following `continue` record admits
  it.
  Red when: a deferral releases Plan's exit.
- **AC2** — When the plant `holding-none` runs the same move, it exits 1 printing `disposition none
  holds`.
  Red when: `none` releases the gate.
- **AC3** — When the plant `holding-defer` runs under `terminal-command`, `ratify.py tFix` exits 1
  printing `disposition ask holds`, the alias resolved.
  Red when: an alias of a holding word ratifies.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the three `holding-*` plants under `--fixture`, staged by a `check_plan_exit` that admits any admitted word · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 39 (HIGH, item H4,
  shared with findings 5 and 21), repairing `TOOL-dRankedPlan-10`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-33`, the hands-off edge to `TOOL-dRankedPlan-35`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-10` S4's gate and `TOOL-dRankedPlan-9` S4's arm; the word
resolution reuses `TOOL-dDeclaredLoop-16` S2's `resolve_disposition`, so the alias `defer` is never
spelled here. No code exists at base 0689e7fa. `python tools/codebase-map/reuse_lookup.py "bound a
disposition record lookup to records added after the build's newest transition"` ranked name stems
only, and nothing in the tree judges a disposition word, so no existing seam fits beyond the two
readers this unit extends. The recall query returned the audit's H4 item and `TOOL-dDeclaredLoop-16`'s
S1 set, which agree.

Recall terms used: `python tools/memory-recall/query.py "which disposition record releases a re-entered plan.exit" --terms "disposition record item.plan.exit freshness newest transition B6 revision terminal-command fallback read_transitions"`
