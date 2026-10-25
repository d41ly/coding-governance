# TOOL-dWitnessedBar-85 — each liveness variant seen red on each key adds to the canary's count, so the restated floor sees a variant that is no longer there

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 44 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 79 to 84
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. Id 17 shares that item and takes
`TOOL-dWitnessedBar-86`.

`TOOL-dWitnessedBar-82` S1 restates `FLOOR_ASSERTIONS` so that a deleted arm reads below the floor,
and its §1, S2 and New-arm line count the variants of `TOOL-dWitnessedBar-79` and
`TOOL-dWitnessedBar-80` among the arms it protects. Those variants add nothing to `a`. Each one only
decides whether unit 66 S2's single assertion is counted, and a suite that runs no length variant
still sees the tail variant red, so that assertion is counted once and `a` does not move. The floor
therefore cannot see the length variant or the tail variant go missing, and 82 AC2's second clone
cannot print `below the pinned floor` on a correct build.

This unit makes each variant count. On every key, a variant seen red adds one to `a`, and the floor
is restated over those counts. It repairs `TOOL-dWitnessedBar-82` and builds one step after it
(order 44).

## 2. Scope (IN)

- **S1** — The variants count. In the per-key liveness loop of
  `tools/run-gates/run-gates.gov.test.sh`, each variant, the length variant `${_rg_v:1}` of unit 79 and
  the tail variant `${_rg_v%?}x` of unit 80, adds one to `a` for each `<key>:<var>` pair of
  `CANARY_KEYS` on which it is seen red. Seen red means both of unit 74 S2's one-line counts are one
  and `check_canary_keys` on its mutant prints exactly `<var>`. A variant not seen red on a key adds
  nothing there and prints its own reason, as units 79 and 80 S3 state. Unit 66 S2's assertion keeps
  the gating units 74 and 76 give it. The loop's added count is therefore two for every pair, four
  with today's two pairs. Observed by AC1.
- **S2** — The floor is restated over the counted variants. This unit's builder states
  `FLOOR_ASSERTIONS` absolutely, at the count the suite executes on a passing run at this pass, by
  `TOOL-dWitnessedBar-82` S1's counting rule. The comment naming `TOOL-dWitnessedBar-85` as the unit
  that stated it is the one line directly above `FLOOR_ASSERTIONS=<n>`, in place of the owner line
  that sat there, and the assignment line carries nothing after the number. Observed by AC2.

## 3. Non-goals (OUT)

- The staged reds that show a missing variant reads below the floor, and the answers to the coverage
  claims of units 79, 80 and 82, which are `TOOL-dWitnessedBar-86`'s for id 17.
- The last restatement of the floor and the owner the close derives. `TOOL-dWitnessedBar-88` adds an
  arm at order 45, restates the floor after this unit, and fixes where every owner comment sits.
- A counter per variant kept apart from `a`. The suite has one count and one floor
  (`tools/run-gates/run-gates.gov.test.sh:91`, `:459`), and a second count would be a second floor.
- The report's left-shift text, a checklist entry that an arm a floor protects adds to the floor's
  counter itself, and its promotion into the spec template's New-arm guidance. The template is a
  governance carrier, which BUILD-METHOD M3's veto 2 withholds from this run. S1 is the regression
  this unit builds, and it runs on every bar.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-79` — the length variant and its seen-red test, on whose success S1 adds one per key (id 1)
- **consumes-from** `TOOL-dWitnessedBar-80` — the tail variant and its seen-red test, on whose success S1 adds one per key (id 1)
- **consumes-from** `TOOL-dWitnessedBar-82` — S1's restatement rule and the floor it states, which S2 restates over the counted variants (id 1)
- **consumes-from** `TOOL-dWitnessedBar-84` — S14's restated floor and its visited counts, which S2 counts and restates after (id 1)
- **hands-off** `TOOL-dWitnessedBar-86` — the per-variant count, whose staged absence unit 86 observes below the floor and records against the claims of units 79, 80 and 82 (ids 1 and 17)
- **hands-off** `TOOL-dWitnessedBar-88` — the restated floor and its owner line, which unit 88 restates again as the last unit adding a gov-canary arm and reads with `grep -B1` (ids 1, 11, 14 and 22)
- **hands-off** `TOOL-dWitnessedBar-89` — S1's per-variant increments, AC1's `-ge 0` clone and S2's owner line, which unit 89 isolates, widens with the no-tail clone and restates without the history comments (ids 4, 13 and 16 of the round-1 spec audit of units 85 to 88)

## 4. Design

### Evidence

- `tools/run-gates/run-gates.gov.test.sh:91` sets `a=0`, `:94` holds `FLOOR_ASSERTIONS=16`, and `:459`
  fails only when `a` is below the floor. `a` moves only through explicit increments, as the report's
  id 1 and id 17 skeptics read.
- `:92-93` hold the `TOOL-aShardedFloor-2` comment above the constant, and `:95` holds
  `# Raised 15 -> 16 by TOOL-dDerivedDocket-23` below it, read on 2026-10-25.
- `tools/check-testsuite-counts.sh:94` reads the floor with `grep -qE '^FLOOR_ASSERTIONS=[0-9]+$'`, so
  a comment after the number on that line fails the `testsuite counts (every bar self-test prints one)`
  leg.
- `spec/2026-10-25-spec-TOOL-dWitnessedBar-79.md` S3 and `spec/2026-10-25-spec-TOOL-dWitnessedBar-80.md`
  S3 each say a failing variant "leaves unit 66 S2's assertion uncounted", and neither adds to `a`.
  `spec/2026-10-25-spec-TOOL-dWitnessedBar-84.md` S14 adds to `a` only for its two visited counts.
- `build_commit` (`tools/unattended/lib-unattended.sh:1186`) is the one answer to which commit is a
  unit's pass, as `TOOL-dWitnessedBar-62` S16 rules; AC1 and AC2 locate this unit's pass with it.

### Inventory

Minted: the per-variant increments of S1 and the restated value of `FLOOR_ASSERTIONS` with its owner
line. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 44. Order 44 holds `TOOL-dWitnessedBar-84` and `TOOL-dWitnessedBar-86`.
Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js:76`, `:607-612`), so unit 84 builds and restates the floor
before this unit, and unit 86 records after it. `TOOL-dWitnessedBar-88` builds at order 45 and is the
last to restate.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Strike the variants from unit 82's protected list and leave them uncounted, the report's second
  option.** A deleted variant would then be seen only by the grep counts of 79 AC3 and 80 AC3, which
  run once at the close, and a later edit that drops a variant would land with the bar green.
- **Count each variant once, not once per key.** A loop that runs a variant on one key of two would
  still add one, so a shortened loop would read as coverage.
- **Have unit 82 count the variants in its own pass.** Unit 82 is specced and audited without that
  item, and the disposal rule forbids folding a finding into it.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none: one increment per variant per key, on a branch the loop already takes.
- error / empty / loading states — a variant not seen red adds nothing, so its absence and its
  failure both read below the floor.
- observability — the floor's owner line names this unit at its pass.
- risks — a builder who adds the increment before the seen-red test counts a variant that failed;
  AC1's `-ge 0` clone catches it, because the count would not fall.
- testing — AC1 and AC2 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — With `tools/unattended/lib-unattended.sh` sourced,
  `build_commit cdfbd1cf..HEAD TOOL-dWitnessedBar-85 memory/builds/dWitnessedBar "$GENERATED_INDEXES" "$SHARED_RECORDS"`
  names this unit's pass commit, the two values read from `.unattended.conf`. In a scratch clone
  checked out there, the arm's printed assertion count exceeds the count it prints in a clone checked
  out at that commit's first parent by twice the number of words in `${CANARY_KEYS[*]}`. In a clone
  of the pass commit whose suite copy has `check_cr_reached` compare the byte count with `-ge 0`, the
  arm prints `below the pinned floor` with an executed count at least that number of words below the
  floor.
  Red when: a variant adds to `a` whether or not it was seen red, or adds once for every key together.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  figure: every count is DERIVED at observation time; the word count reads 2 today.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — In the scratch clone of AC1's pass commit,
  `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1` prints a comment naming
  `TOOL-dWitnessedBar-85` and no other unit id,
  `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$' tools/run-gates/run-gates.gov.test.sh` prints 1, and the arm
  prints `PASS (<n> assertions)` with `<n>` equal to that value.
  Red when: the counted variants sit above the floor, or the owner line sits where `grep -B1` cannot
  read it.
  fixture: the scratch clone of AC1.
  figure: both numbers are DERIVED at observation time.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `testsuite counts (every bar self-test prints one)` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`). `testsuite counts (every bar self-test prints one)` reads the assignment
line S2 writes.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · the per-variant count in the liveness loop, staged red by a scratch suite whose `check_cr_reached` compares the count with `-ge 0` (the length variant adds nothing on either key and `below the pinned floor` prints) · FLOOR_ASSERTIONS restated absolutely by S2, and again by `TOOL-dWitnessedBar-88` at order 45

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 82 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How does the floor come to see a missing variant (id 1)?** Options: (a) each variant seen red
  on each key adds one to `a`, and the floor is restated over it, the report's first option; (b) the
  variants leave unit 82's protected list, and 82 AC2's second clone deletes an arm that does count,
  the report's second option. (b) leaves a variant's absence visible only to a close-time grep, so a
  later edit drops it with the bar green, and it satisfies fewer of the report's stated claims. (a) is
  the more feature-rich survivor. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 79 to 84, id 1
  (HIGH, item H1, shared with id 17).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.

## 10. Reuse audit

The seam is the suite's own count and floor, `a` and `FLOOR_ASSERTIONS` in
`tools/run-gates/run-gates.gov.test.sh` (`:91`, `:94`, `:459`), and `TOOL-dWitnessedBar-76`'s per-key
liveness loop, given one increment per variant; the restatement follows `TOOL-dWitnessedBar-82` S1's
rule, and the pass commit is `build_commit`'s answer.
`python tools/codebase-map/reuse_lookup.py "assert a pinned count of executed assertions against a floor"`
ranked `counts`, `measure_typed_counts`, `build_counted_values` and `check_count_sources`, none this
suite's floor, so no existing seam fits beyond the count and loop named above.

Recall terms used: `python tools/memory-recall/query.py "how does a gate's assertion floor see a liveness variant that is no longer there" --terms "canary liveness variant counted FLOOR_ASSERTIONS restated floor owner deleted arm seen red increment"`
