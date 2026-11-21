# TOOL-dWitnessedBar-85 — each liveness variant seen red on each key adds to the canary's count, so the restated floor sees a variant that is no longer there

**Status:** DEFERRED · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 44 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-85-deviation-851.md](../build/2026-10-25-build-TOOL-dWitnessedBar-85-deviation-851.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-85-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-85-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-85-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-85-reground-spec-writer.md) | journal | — |
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
decides whether its key's compare is counted, unit 66 S2's for `rec_sha` and unit 67 S2's for
`rec_fp`, and a suite that runs no length variant still sees the tail variant red, so each compare
is counted once and `a` does not move. The floor therefore cannot see the length variant or the tail
variant go missing, and 82 AC2's second clone cannot print `below the pinned floor` on a correct build.

This unit makes each variant count. On every key, a variant seen red adds one to `a`, and the floor
is restated for those counts. It repairs `TOOL-dWitnessedBar-82` and builds after
`TOOL-dWitnessedBar-84` within order 44.

## 2. Scope (IN)

- **S1** — The variants count. In the per-key liveness loop of
  `tools/run-gates/run-gates.gov.test.sh`, each `check_key_variant` call, the tail variant
  `${_rg_v%?}x` of unit 80 and the length variant `${_rg_v:1}` of unit 79, adds one to `a` for each
  `<key>:<var>` pair of `CANARY_KEYS` on which it is seen red. Seen red means the call returned 0,
  which `check_key_variant` does only when both of unit 74 S2's one-line counts are one,
  `check_canary_keys` did not return 2, and it printed `<var>` and no other name. The increment sits
  at the loop's top level on the call's status, never inside the `$(...)` the call runs in, where it
  would be lost. A variant not seen red on a key adds nothing there and prints its own reason, as
  units 79 and 80 S3 state. The `rec_sha` and `rec_fp` compares keep the gating units 74, 76 and 79
  give them: a key joins `rgf_seen` only when both its variants were seen red. The loop's added count
  is two for every pair, four over today's pairs (DERIVED: twice the words of `${CANARY_KEYS[*]}`).
  Observed by AC1.
- **S2** — The floor is restated for the counted variants. Since this unit adds increments after
  `TOOL-dWitnessedBar-84`'s restatement, its builder states `FLOOR_ASSERTIONS` absolutely by
  `TOOL-dWitnessedBar-82` S1's rule: the floor read from the file at this pass's base plus S1's
  increments, the only ones this unit adds. Its `# RAISED <old> -> <new> by TOOL-dWitnessedBar-85`
  comment goes on the line directly below the constant, above unit 84's, and that first line names no
  other unit id. The line above the constant is left as it stands: it is the derived owner's line,
  which `TOOL-dWitnessedBar-83` S1 gives to `TOOL-dWitnessedBar-90`. The assignment line carries
  nothing after the number. Observed by AC2.
- **S3** — No code line added. S1's increments ride the lines that already call each variant, so
  the suite's code-line measure and its row in `memory/project/shell-role.txt` are unchanged by this
  pass (§8 F3). Comment lines S2 adds are not code lines. Observed by AC3.

## 3. Non-goals (OUT)

- The staged reds that show a missing variant reads below the floor, and the answers to the coverage
  claims of units 79, 80 and 82, which are `TOOL-dWitnessedBar-86`'s for id 17.
- The derived owner's line above the constant, which `TOOL-dWitnessedBar-83` S1 gives to
  `TOOL-dWitnessedBar-90` (order 47), and the restatements after this unit: `TOOL-dWitnessedBar-88`
  S7 at order 45, `TOOL-dWitnessedBar-89` S10 at order 46 and unit 90's.
- A counter per variant kept apart from `a`. The suite has one count and one floor
  (`tools/run-gates/run-gates.gov.test.sh@612cac75f:243`, `:1315`), and a second count would be a
  second floor.
- Where the visited-count increments of `TOOL-dWitnessedBar-84` S14 sit, which
  `TOOL-dWitnessedBar-89` S7 places once per loop at order 46. S1 leaves them as they landed.
- The report's left-shift text, a checklist entry that an arm a floor protects adds to the floor's
  counter itself, and its promotion into the spec template's New-arm guidance. The template is a
  governance carrier, which BUILD-METHOD M3's veto 2 withholds from this run. S1 is the regression
  this unit builds, and it runs on every bar.
- `TOOL-dWitnessedBar-28`'s gov-canary arm. Unit 28 is not built: it waits on three dOrderedCharter
  changes (asks `TOOL-dWitnessedBar-101` to `-103`) and this run defers it, so S2's floor leaves its
  arm out, and the floor for it waits with unit 28.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-79` — the length variant and its seen-red test, on whose success S1 adds one per key (id 1)
- **consumes-from** `TOOL-dWitnessedBar-80` — the tail variant and its seen-red test, on whose success S1 adds one per key (id 1)
- **consumes-from** `TOOL-dWitnessedBar-82` — S1's restatement rule and the floor it states, which S2 restates over the counted variants (id 1)
- **consumes-from** `TOOL-dWitnessedBar-84` — S14's restated floor and its visited counts, which S2 counts and restates after (id 1)
- **hands-off** `TOOL-dWitnessedBar-86` — the per-variant count, whose staged absence unit 86 observes below the floor and records against the claims of units 79, 80 and 82 (ids 1 and 17)
- **hands-off** `TOOL-dWitnessedBar-88` — S1's per-variant count and S2's restated floor, which unit 88's S17 reason leaves uncounted and its S7 restates after (ids 1, 11, 14 and 22)
- **hands-off** `TOOL-dWitnessedBar-89` — S1's per-variant increments, AC1's `-ge 0` clone and S2's `# RAISED` line, which unit 89 isolates, widens with the no-tail clone and restates without the history comments (ids 4, 13 and 16 of the round-1 spec audit of units 85 to 88)

## 4. Design

### Evidence

Read at `612cac75f` on 2026-11-21; the suite is unchanged there since `e1ad4ef32`.

- `tools/run-gates/run-gates.gov.test.sh@612cac75f:243` sets `a=0`, `:246` holds
  `FLOOR_ASSERTIONS=76` (PINNED 2026-11-21), and `:1315` fails only when `a` is below the floor. `a`
  moves only through explicit increments, as the report's id 1 and id 17 skeptics read.
- `:244-245` hold the `TOOL-aShardedFloor-2` comment above the constant, the line
  `grep -B1 '^FLOOR_ASSERTIONS=' | head -1` prints. `:247` opens unit 84's
  `# RAISED 74 -> 76 by TOOL-dWitnessedBar-84` comment directly below it, above unit 82's at `:250`
  (PINNED 2026-11-21), the placement unit 84's builder return records
  (`2026-11-19-build-TOOL-dWitnessedBar-84-1-builder-return`).
- `tools/check-testsuite-counts.sh#compliant` reads the floor with
  `grep -qE '^FLOOR_ASSERTIONS=[0-9]+$'`, so a comment after the number on that line fails the
  `testsuite counts (every bar self-test prints one)` leg.
- The liveness loop calls `check_key_variant` twice per pair, the tail variant at
  `tools/run-gates/run-gates.gov.test.sh@612cac75f:980` and the length variant at `:982`, each inside
  `$(...)`, with its failure appended to `rgf_whys` on the continuation line. `#check_key_variant`
  returns 0 silent only on S1's seen-red conditions and otherwise prints one reason and returns 1.
  The compares are gated on `rgf_seen` at `:992` and `:995`, and the loop adds to `a` only for its
  visited count at `:989`, unit 84 S14's.
- `spec/2026-10-25-spec-TOOL-dWitnessedBar-79.md` S3 and `spec/2026-10-25-spec-TOOL-dWitnessedBar-80.md`
  S3 each keep a failed variant's `<var>` out of `rgf_seen`, so that key's compare stays uncounted,
  and neither adds to `a`. `spec/2026-10-25-spec-TOOL-dWitnessedBar-84.md` S14 adds to `a` only for
  its two visited counts (PINNED 2026-11-21).
- `#check_cr_reached` tests the value with `[ "${#_cc_v}" -eq 41 ]` and a last-byte CR test. Read as
  `-ge 0`, the count admits every value, so unit 79's length variant, forty bytes ending in CR (79 S1),
  passes on every key while unit 80's tail variant still fails the last-byte test. Unit 74 rev-3 F3
  retired `-ge 0` as unit 74 AC2's break only because that unit's one variant failed both conditions.
- The suite's row in `memory/project/shell-role.txt` equals the file's measured code lines
  (`tools/gate-lint/sh_hygiene.py#measure_code_lines`), unit 84 having widened it to that measure
  (`2026-11-21-build-TOOL-dWitnessedBar-84-widen-23`), and the ledger is shrink-only
  (`tools/gate-lint/kit.toml`, the `shell-role` `[[ledger]]`). A code line S1 adds reds
  `portability (shell lines only shrink)` unless widened (§8 F3).
- `tools/unattended/lib-unattended.sh#build_commit` is the one answer to which commit is a unit's
  pass, as `TOOL-dWitnessedBar-62` S16 rules; AC1 to AC3 locate this unit's pass with it.

### Inventory

Minted: the per-variant increments of S1 and the restated value of `FLOOR_ASSERTIONS` with its
`# RAISED` comment. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 44. Order 44 holds `TOOL-dWitnessedBar-84`, this unit and
`TOOL-dWitnessedBar-86`. Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js@612cac75f:78-82`, `:692-697`), so unit 84 built and restated
the floor first (`e1ad4ef32`), and unit 86 builds after this unit lands, re-grounded over it. Units
88, 89 and 90 restate after, at orders 45 to 47, and unit 90 is the owner that writes the line above
the constant.

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
- **Write S2's comment on the line above the constant.** That line is the derived owner's, unit 90's
  by `TOOL-dWitnessedBar-83` S1, and unit 84 left it as it stood.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none: one increment per variant per key, on a branch the loop already takes.
- error / empty / loading states — a variant not seen red adds nothing, so its absence and its
  failure both read below the floor.
- observability — the floor's `# RAISED` line below the constant names this unit at its pass.
- risks — a builder who adds the increment before the seen-red test counts a variant that failed.
  AC1's `-ge 0` clone catches it: its executed count then falls by the words of
  `${CANARY_KEYS[*]}`, the gated compares alone, not by twice that.
- testing — AC1 to AC3 by scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — With `tools/unattended/lib-unattended.sh` sourced,
  `build_commit cdfbd1cf..HEAD TOOL-dWitnessedBar-85 memory/builds/dWitnessedBar "$GENERATED_INDEXES" "$SHARED_RECORDS"`
  names this unit's pass commit, the two values read from `.unattended.conf`. In a scratch clone
  checked out there, the arm's printed assertion count exceeds the count it prints in a clone checked
  out at that commit's first parent by twice the number of words in `${CANARY_KEYS[*]}`. In a clone
  of the pass commit whose suite copy has `check_cr_reached` read its `-eq 41` as `-ge 0`, the arm
  prints `below the pinned floor`, with an executed count twice that number of words below the count
  the unedited clone prints: on each key the length variant's increment and its key's compare.
  Red when: a variant adds to `a` whether or not it was seen red, or adds once for every key together.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  figure: every count is DERIVED at observation time; the word count reads 2 today.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — In the scratch clone of AC1's pass commit,
  `grep -A1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | tail -1` prints a comment
  naming `TOOL-dWitnessedBar-85` and no other unit id,
  `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1` prints the line it
  prints at the first parent,
  `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$' tools/run-gates/run-gates.gov.test.sh` prints 1, and the arm
  prints `PASS (<n> assertions)` with `<n>` equal to that value.
  Red when: the counted variants sit above the floor, or the comment displaces the owner's line.
  fixture: the scratch clone of AC1.
  figure: both numbers are DERIVED at observation time.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — In the scratch clones of AC1's pass commit and its first parent,
  `python tools/gate-lint/sh_hygiene.py --shell-role --measure . tools/run-gates/run-gates.gov.test.sh`,
  the ledger's own seed, prints the same row, and `git diff <first-parent> <pass> -- memory/project/shell-role.txt`
  prints nothing.
  Red when: S1 adds a code line, so the shrink-only row is widened or reds.
  fixture: the scratch clones of AC1.
  figure: the measure is DERIVED at observation time.
  permission: the probe is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `testsuite counts (every bar self-test prints one)` · `portability (shell lines only shrink)` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh#derive_hold_source`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf@612cac75f:40`). `testsuite counts (every bar self-test prints one)` reads the
assignment line S2 writes, and `portability (shell lines only shrink)` grades S3's unchanged row.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · the per-variant count in the liveness loop, staged red by a scratch suite whose `check_cr_reached` reads its count as `-ge 0` (the length variant adds nothing on either key and `below the pinned floor` prints) · FLOOR_ASSERTIONS restated absolutely by S2 for this unit's increments; the derived owner is `TOOL-dWitnessedBar-90` by `TOOL-dWitnessedBar-83` S1

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
- **F3 — Does S1 add code lines to a suite whose shell-role row sits at its measure (§4 Evidence)?**
  Options: (a) each increment rides the call's existing lines, so the row stands; (b) new lines,
  with the row widened by `ratchet.py widen` and a widen record, two more files touched. (b) widens a
  shrink-only row for no behaviour (a) lacks and adds files the unit does not need. Recommendation
  (a). RESOLVED (agent, 2026-11-21, delegated): (a), the survivor with fewer follow-ups, re-ground
  per 2026-11-19-prompt-TOOL-dWitnessedBar-85-reground-brief.
  widens: none · relaxes: none
- **F4 — How far below must AC1's `-ge 0` clone read?** Rev-2 read "at least" the word count below
  the floor. At `612cac75f` the clone also loses each key's gated compare (§4 Evidence), so a build
  counting a failed variant still reads the word count below, and "at least" cannot see AC1's
  Red-when. Options: (a) keep "at least", which fails that Red-when, so veto 1 discards it; (b) twice
  the word count below the unedited clone's count. Recommendation (b). RESOLVED (agent, 2026-11-21,
  delegated): (b), the one survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 79 to 84, id 1
  (HIGH, item H1, shared with id 17).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.
- rev-3 · 2026-11-21 · §1 · S1 to S3 · §3 · §4 · §5 · AC1 to AC3 · §7 · §8 · §10 · re-grounded at
  `612cac75f` per 2026-11-19-prompt-TOOL-dWitnessedBar-85-reground-brief. S1 counts on
  `check_key_variant`'s status at the loop's top level. S2's comment goes below the constant, the
  owner unit 90. S3 and F3 hold the shell-role row; F4 makes AC1's clone read twice the word count.
  §3 names units 28's and 89's shares and the later restatements; citations blob-pinned.

## 10. Reuse audit

The seam is the suite's own count and floor, `a` and `FLOOR_ASSERTIONS` in
`tools/run-gates/run-gates.gov.test.sh` (`@612cac75f:243`, `:246`, `:1315`), and
`TOOL-dWitnessedBar-76`'s per-key liveness loop with its `check_key_variant` calls, given one
increment per call seen red; the restatement follows `TOOL-dWitnessedBar-82` S1's rule, and the pass
commit is `build_commit`'s answer.
`python tools/codebase-map/reuse_lookup.py "assert a pinned count of executed assertions against a floor"`
ranked `counts`, `compare_counts`, `measure_typed_counts` and `read_count` (PINNED 2026-11-21), none
this suite's floor, so no existing seam fits beyond the count and loop named above.

Recall terms used: `python tools/memory-recall/query.py "how does a gate's assertion floor see a liveness variant that is no longer there" --terms "canary liveness variant counted FLOOR_ASSERTIONS restated floor owner deleted arm seen red increment"`
