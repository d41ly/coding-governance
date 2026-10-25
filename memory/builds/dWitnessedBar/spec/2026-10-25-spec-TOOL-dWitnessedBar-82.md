# TOOL-dWitnessedBar-82 — the gov canary's assertion floor is restated after unit 78, so the arms of units 74 to 81 cannot be deleted with the canary green

**Status:** OPEN · rev-4 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 43 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, report item **H2**. Id 14 shares that item and takes
`TOOL-dWitnessedBar-83`.

The §7 New-arm lines of `TOOL-dWitnessedBar-76`, `-77` and `-78` each read "none, the floor is stated
by `TOOL-dWitnessedBar-73` S15". Unit 73 S15 states `FLOOR_ASSERTIONS` at the count the suite executes
at unit 73's own pass, and unit 73 builds first at order 41. The suite checks the floor only as a
minimum (`tools/run-gates/run-gates.gov.test.sh:459`). So every assertion units 74 to 81 add sits above
the floor: unit 76's per-key loop, unit 78's third and fourth records and its compares, and the
variants of units 79 and 80. Any of them can be deleted with the canary green, while the New-arm lines
certify coverage the floor does not hold.

This unit restates the floor absolutely after unit 78, the last of the round-8 units, and after the
round-9 variants, and observes it red on a deleted arm. It repairs `TOOL-dWitnessedBar-78`, which the
report names as the floor's owner, and builds one step after it (order 43).

## 2. Scope (IN)

- **S1** — The restatement. This unit's builder states `FLOOR_ASSERTIONS` in
  `tools/run-gates/run-gates.gov.test.sh` absolutely, at the count of assertions the built suite
  executes on a passing run at this pass, counted from its source with each loop counted at its
  population, as `TOOL-dWitnessedBar-73` S15 rules. The comment beside it names
  `TOOL-dWitnessedBar-82` as the unit that stated it, and says it counts every arm through order 43.
  Observed by AC1.
- **S2** — The floor is seen red. At the close the main loop runs the arm in two scratch clones of
  the built tree. One suite copy lacks `TOOL-dWitnessedBar-78` S13's fourth-record arm; the other
  lacks `TOOL-dWitnessedBar-79`'s length variant. Each prints the suite's floor line,
  `gov-canary: executed <n> assertions, below the pinned floor <floor>`, and exits non-zero. This
  unit's acceptance ledger records both lines. Observed by AC2.
- **S3** — The New-arm claims are answered. The acceptance ledgers of `TOOL-dWitnessedBar-76`, `-77`
  and `-78` each carry a line naming `FLOOR_ASSERTIONS` and this unit's S1 as the floor that counts
  their arms, in answer to their New-arm lines' citation of unit 73 S15. Observed by AC3.

## 3. Non-goals (OUT)

- Who restates the floor after this unit, and the close's equality of the executed count with the
  floor, which are `TOOL-dWitnessedBar-83`'s for id 14. `TOOL-dWitnessedBar-84` adds arms at order 44
  and restates the floor for them.
- Rewording the New-arm lines of units 76 to 78. Their citation is answered in their ledgers, as
  `TOOL-dWitnessedBar-78` §3 answers units 68 to 73.
- A floor derived from the source at run time. The floor exists to catch a deleted assertion, and a
  floor that moves with the source moves with the deletion.
- The report's left-shift text, a checklist entry that a New-arm line citing a floor names a unit at
  or after its own build position. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-73` — S15's absolute floor and its counting rule, which S1 restates at a later position (id 2)
- **consumes-from** `TOOL-dWitnessedBar-76` — the per-key liveness loop and its New-arm claim, whose assertions S1 counts and whose ledger S3 answers (id 2)
- **consumes-from** `TOOL-dWitnessedBar-77` — its New-arm claim, which S3 answers in its ledger (id 2)
- **consumes-from** `TOOL-dWitnessedBar-78` — its third and fourth records, its compares and its New-arm claim, which S1 counts, S2 deletes in a scratch copy and S3 answers (id 2)
- **hands-off** `TOOL-dWitnessedBar-83` — the restated floor and its comment, whose owner unit 83 derives and whose equality with the executed count it holds at the close (ids 2 and 14)
- **hands-off** `TOOL-dWitnessedBar-84` — the restatement rule, which unit 84 applies again for the arms it adds at order 44 (ids 2 and 21)
- **hands-off** `TOOL-dWitnessedBar-85` — S1's restatement rule and the floor it states, which unit 85 restates over the counted variants (id 1 of the round-1 spec audit of units 79 to 84)
- **hands-off** `TOOL-dWitnessedBar-86` — §1, AC2 and the New-arm claim that the floor protects the variants, which unit 86 observes at this unit's pass and answers in its ledger (id 17 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-88` — S1's restatement rule, AC1 and the §4 figure, which unit 88 locates by `build_commit`, places on one line above the constant and restates (ids 9, 11, 14 and 16 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-89` — S1's counting rule, by which unit 89 restates the floor last under one owner line (id 4 of the round-1 spec audit of units 85 to 88)
- **hands-off** `TOOL-dWitnessedBar-90` — S1's counting rule, by which unit 90 restates the floor under its own owner line (ids 13 of the round-1 spec audit of unit 89)

## 4. Design

### Evidence

- `tools/run-gates/run-gates.gov.test.sh:91-94` holds `a=0` and `FLOOR_ASSERTIONS=16`, with the comment
  "Stated ABSOLUTELY, never as a delta". `:459` fails only when `a` is below the floor, and `:461`
  prints `PASS ($a assertions)`.
- `spec/2026-10-25-spec-TOOL-dWitnessedBar-73.md` S15 states the floor at unit 73's own pass, and its
  AC15 requires the close's `PASS` count to equal it.
- The New-arm lines of units 76, 77 and 78 cite unit 73 S15 for their floor (each spec's §7).
- Orders, read from the status headers on 2026-10-25: units 73, 76 and 77 at 41; unit 78 at 42; units
  79 to 81 at 41. `tools/workflows/unattended-build.js:608-613` sorts by order, then id string, so unit
  73 builds before every unit that adds a gov-canary arm in rounds 8 and 9.
- Specs of this build declaring `New arm: tools/run-gates/run-gates.gov.test.sh`, read on 2026-10-25:
  20, from unit 12 at order 5 to unit 78 at order 42.

### Inventory

Minted: the restated value of `FLOOR_ASSERTIONS` and its comment. No function, plant, flag or file.
Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 43, after `TOOL-dWitnessedBar-78` (42) and the order-41 variants of units
79 and 80. `TOOL-dWitnessedBar-83` shares order 43 and builds after this unit by id string.
`TOOL-dWitnessedBar-84` builds at order 44, adds arms, and restates the floor again for them, so the
value this unit writes is the floor for every pass between order 43 and order 44.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **Have every unit that adds an arm restate the floor in its own pass.** Units 74 to 81 are already
  specced and audited without that item, so the restatement would be folded into their specs, which
  the disposal rule forbids.
- **State the floor as a delta over unit 73's.** The suite's comment requires an absolute statement,
  and a delta over a value that later units move reads as two facts for one number.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none: one constant changes.
- error / empty / loading states — S2 shows the floor line printing on a deleted arm.
- observability — the floor's comment names who stated it, so a later reader knows which unit to
  ask.
- risks — a builder who counts a loop at one iteration under-states the floor; AC1's equality at this
  pass's commit catches it.
- testing — AC1 and AC2 by scratch clone at the close, AC3 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone checked out at this unit's pass commit, the first line of
  `git log --reverse --format='%H %s' -- tools/run-gates/run-gates.gov.test.sh | grep 'TOOL-dWitnessedBar-82'`, the
  arm prints `PASS (<n> assertions)` with `<n>` equal to the value
  `grep '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh` prints in that clone, and the comment
  beside it names `TOOL-dWitnessedBar-82`.
  Red when: the restated floor is below the count executed at this pass, so an arm of units 74 to 81
  can still be deleted with the canary green.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  figure: both numbers are DERIVED at observation time.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — In a scratch clone of the built tree whose suite copy lacks `TOOL-dWitnessedBar-78` S13's
  fourth-record arm, the arm prints a line holding `below the pinned floor` and exits non-zero; a copy
  lacking the `_rg_v:1}` variant does the same. When
  `grep -n 'below the pinned floor' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-82*acceptance-ledger*`
  runs at the close, it prints both lines, each naming the arm the copy lacked.
  Red when: a deleted arm leaves the canary green.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -n 'FLOOR_ASSERTIONS' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[678]*acceptance-ledger*`
  runs at the close, it prints one line in each of the three ledgers naming `TOOL-dWitnessedBar-82`,
  on the line grep prints.
  Red when: a New-arm claim stands answered by a floor stated before its unit built.
  permission: the ledgers are written at the close.

## 7. Gates

`run-gates gov canary` · `memory hygiene` · `recall floor` · `recall floor arms`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`). `recall floor` and `recall floor arms` are owed for the ledgers under
`memory/`.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC2 · the floor restated after unit 78, staged red by a suite copy lacking unit 78 S13's fourth-record arm and by one lacking unit 79's length variant (each reaches `below the pinned floor`) · FLOOR_ASSERTIONS restated absolutely by S1, and again by `TOOL-dWitnessedBar-84` at order 44 for its own arms

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 78 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which unit does this promotion repair, and so where does it sit (id 2)?** Options: (a) unit 78,
  which the report's fix names as the last unit to add gov-canary assertions, order 43; (b) unit 76,
  whose New-arm line the finding cites first, order 42, building after unit 78 by id string. Both
  place the restatement after unit 78. (b) ties with unit 78 at order 42 and builds after it only
  through the id-string tie-break, which the README's build-order region shows as one parallel step.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by fewer open questions.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78, id 2
  (HIGH, item H2, shared with id 14).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-85, TOOL-dWitnessedBar-86 and TOOL-dWitnessedBar-88, promoted by the
  round-1 spec audit of units 79 to 84; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.
- rev-4 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-90, the minors batch of the round-1 spec audit of unit 89; nothing else
  moved.

## 10. Reuse audit

The seam is the suite's own floor, `FLOOR_ASSERTIONS` and its check at
`tools/run-gates/run-gates.gov.test.sh:94` and `:459`, restated under the rule `TOOL-dWitnessedBar-73`
S15 set.
`python tools/codebase-map/reuse_lookup.py "assert a pinned count of executed assertions against a floor"`
ranked `counts`, `measure_typed_counts`, `build_counted_values` and `check_count_sources`, none this
suite's floor, so no existing seam fits beyond the floor named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
