# TOOL-dBoundRoles-66 — the round-1 audit of unit 64, its 23 minors: skip lines by a pinned predicate, loops swept by class, unit terms tied to their arms, absence checks on joined prose, and the observation's failure path staged

**Status:** CLOSED · rev-4 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 37 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 |
| [2026-10-26-build-TOOL-dBoundRoles-65-round7-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-65-round7-fix-return.md) | research | TOOL-dBoundRoles-65 |
| [2026-10-26-build-TOOL-dBoundRoles-66-deviation-661.md](../build/2026-10-26-build-TOOL-dBoundRoles-66-deviation-661.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-66-deviation-662.md](../build/2026-10-26-build-TOOL-dBoundRoles-66-deviation-662.md) | deviation | — |
| [2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md](../build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md) | journal | TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-11-24-build-TOOL-dBoundRoles-66-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dBoundRoles-66-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-TOOL-dBoundRoles-66-deviation-663.md](../build/2026-11-24-build-TOOL-dBoundRoles-66-deviation-663.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-65-round7-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-65-round7-fix-brief.md) | research | TOOL-dBoundRoles-65 |
| [2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-brief.md) | journal | TOOL-dBoundRoles-65 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md) | journal | TOOL-dBoundRoles-43 TOOL-dBoundRoles-50 TOOL-dBoundRoles-56 TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-69 |
| [2026-11-23-prompt-TOOL-dBoundRoles-66-2-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dBoundRoles-66-2-spec-writer.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-60-spec-fix-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-60-spec-fix-brief.md) | journal | TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-69 |
| [2026-11-24-prompt-TOOL-dBoundRoles-66-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-66-build-brief.md) | journal | — |
| [2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-65 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted spec 64
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-64-spec-audit-round1.md`) exited
CONVERGED with no blocker. It confirmed 24 findings: one HIGH, 11 MEDIUM and 12 LOW. Id 11, the HIGH, is
`TOOL-dBoundRoles-65`'s. BUILD-METHOD M4 promotes every minor, batched into one unit, because they do not
split into two disjoint write sets by M6 (§4 "Why one unit"). This unit takes all 23: report ids 1 to 24
less id 11. Each id is its own scope item, even where the report merged several ids into one item.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 2, 10, 18 | unit 64 §4, S33, AC8; both floored roles suites read | S1, S2, S3 |
| M2 | 8, 19 | unit 64 §4 Evidence, §7, AC7; the spawn guard's floor | S4, S5 |
| M3 | 3 | unit 64 AC2; the spawn guard's unit-50 term | S6 |
| M4 | 1 | unit 64 §6, AC1, AC9, AC19 | S7 |
| M5 | 12 | unit 64 S28, AC18; unit 63 S16 | S8 |
| M6 | 16 | unit 64 S1, S16, S23, §1, §3, AC1, AC11, AC16; unit 60 S24 | S9 |
| M7 | 22 | unit 64 S18, AC13; unit 63 S12 | S10 |
| M8 | 23 | unit 64 S18, §5; unit 63 S12, §5 | S11 |
| L1 | 24 | unit 64 §4, AC8 | S12 |
| L2 | 20 | unit 64 AC2, §4; the spawn guard's comparison line | S13 |
| L3 | 4 | unit 64 AC18; unit 63 S11, §4 Evidence | S14 |
| L4 | 5 | unit 64 AC5, AC8, AC13; unit 61 AC2; unit 62 §5; unit 63 S8, §5 | S15 |
| L5 | 6 | unit 64 §4, AC2, AC7, AC9; the spawn guard's floor comment | S16 |
| L6 | 7, 13 | unit 64 §4 Evidence | S17, S18 |
| L7 | 9 | unit 64 §4 Evidence; the spawn guard's floor | S19 |
| L8 | 14 | unit 64 S12, S33, §4 Inventory, AC8; the adopter suite's floor comment | S20 |
| L9 | 15 | unit 64 §8 F2, §10 | S21 |
| L10 | 17 | unit 62 §7 | S22 |
| L11 | 21 | unit 64 §4 "How an item closes", AC15, AC23 | S23 |

## 2. Scope (IN)

- **S1** — id 2. Spec 64's §4 "The executed-count rule" defines a skip line once. It is a line of a
  floored roles suite matching `^[[:space:]]*(echo|printf) "[Ss][Kk][Ii][Pp] `. Spec 64's AC8 and S33 read
  that predicate in place of "every line printing a skip, case-folded". On the adopter suite it matches
  the six skip echoes of arms 6, 11 and 20, at `tools/roles/adopt-roles.test.sh@a8b141b6:239`, `:241`,
  `:623`, `:625`, `:994` and `:996`. Observed by AC1.
- **S2** — id 10. The predicate's should-match set on the spawn guard's suite is its skip echo
  `skip no-regress byte arm`, at `tools/hooks/agent-cap.test.sh@97439f99:589`, which unit 25 moves into
  `tools/roles/spawn-guard.test.sh` (spec 25's S5). The other three echoes the audit named,
  `skip rule0: pair arm`, `skip rule0: MSYS-mount deny arm` and `skip no-regress property arm`, left the
  suite with TOOL-dFairHearing-16, for `tools/workflows/spec-audit-optin.test.sh@fd149d71:381` and
  `:437` and `tools/workflows/check-verifier-fanout.test.sh@1d211b61:1892`, suites no unit of this build
  floors. Spec 64's AC8 asserts all seven lines of both suites on the real files. Observed by AC1.
- **S3** — id 18. Each suite's floor comparison line, the one reading `-ge "$FLOOR_ASSERTIONS"`, is
  outside the skip-line population, and spec 64's §4 says so by name. On the adopter suite that line is
  `tools/roles/adopt-roles.test.sh@a8b141b6:1330`, which prints "a block of arms was skipped". Spec
  64's AC8 asserts the predicate matches neither suite's comparison line. Observed by AC1.
- **S4** — id 8. Spec 64's §4 Evidence second bullet states the class, not an instance list. A loop
  counts when it is a `for` or `while` loop of the spawn guard's suite whose body calls an asserting
  helper or echoes an ok or FAIL line. The asserting helpers are the suite's six functions whose body
  raises `pass` or `fail`: `check`, `run_pack`, `run_limit_call`, `run_spawn`, `run_harness` and
  `run_effort`, read at `29acd2d77` (§4 Evidence). The bullet
  gives the sweep, `grep -nE '^[[:space:]]*(for|while) '`, then the instances in the suite unit 25
  moves, at `tools/hooks/agent-cap.test.sh@97439f99`: lines 391, 436, 530 and 716 (PINNED, measured
  2026-11-22 at `29acd2d77`). On the built tree the spawn guard's `FLOOR_ASSERTIONS` equals E
  re-counted over that class. Where unit 64's pass counted fewer, this pass raises the floor and corrects
  the term that fell short. Observed by AC2.
- **S5** — id 19. Spec 64's two §7 `New arm:` lines carry the close's independent bound. The printed n
  less the recorded E is at least 0, and at most the assertions of the arms named on
  `# out of the floor:` lines. A gap above that is red at the close. Spec 64's AC7 stays the pass's
  static check, because no pass can observe the close's run (spec 64 §8 F2). Observed by AC3.
- **S6** — id 3. Spec 64's AC2 holds no scratch-shell half that sets the executed count to the floor less
  a term. It takes a per-term check in its place. A probe counts the assertions of unit 50's arm in the
  spawn guard's suite by §4's rule and requires the `+<n> ... (TOOL-dBoundRoles-50)` term's n to equal
  that count. The arm is the section that opens at the `# ---- ` header comment naming
  `TOOL-dBoundRoles-50` and runs to the next `# ---- ` header, the suite's own arm delimiter. Where unit
  50's arm carries no such header, this pass writes one. Where the term differs from the count, it
  corrects the term and the floor. The early-exit staging stays on spec 64's §7 `New arm:` line.
  Observed by AC4.
- **S7** — id 1. Spec 64's §6 states one rule: every absence check over spec prose runs on the bullet or
  paragraph with its lines joined and its whitespace collapsed, in AC3's form. AC1, AC9 and AC19 are
  restated in that form. AC19 reads spec 63's §10 paragraph joined, instead of a line grep. Observed by
  AC5.
- **S8** — id 12. Spec 64's S28 and AC18 search by value, bare token included:
  `git grep -nE '(handoff\.py)?:102[5-8]([^0-9]|$)' -- memory/builds/dBoundRoles/spec`, with the lines of
  specs 63, 64 and 66 set aside. Spec 63's S16 Readers clause accounts for every hit, or says why a hit
  is not a reader. At `29acd2d77`, with those three specs set aside, the grep prints no bare-token hit:
  its hits are spec 59's S1 bullet and AC lines and spec 69's S16 bullet, each spelled `handoff.py:<n>`
  (DERIVED, re-run at the pass). Observed by AC6.
- **S9** — id 16. Spec 60's S24 names `TOOL-dBoundRoles-50` beside unit 58 for the spawn guard's suite.
  It names `TOOL-dBoundRoles-60` and `TOOL-dBoundRoles-61`, with no condition, for the adopter suite. It
  holds no "carries every earlier unit". Spec 64's S1, S16 and S23, its §1 "Lands on" column and its
  unit-60 consumes-from edge name S24. AC1, AC11 and AC16 extract S24. Where unit 64's pass left S24 in
  the old shape, this pass bumps spec 60. Observed by AC7.
- **S10** — id 22. Spec 64's AC13 gains a staged half. The observation probe of spec 63's S12 runs once
  with its imported module name deliberately wrong. It must exit non-zero, and afterwards no registered
  worktree may be the run's own path, compared through `derive_key` of
  `tools/branch-reconcile/branch_reconcile.py` with `os.path.realpath` on both sides. Spec 64's S18 and
  spec 63's S12 state that a hard kill skips both a shell trap and a `finally` clause. Their recovery is
  the next run's first step: take away every entry under the observation's root that the porcelain list
  marks `prunable`. Observed by AC8.
- **S11** — id 23. The cleanup acts only on what the observation owns. Spec 63's S12 takes away its own
  run's path by git's forced worktree removal, which is safe because that run created it. S10's recovery
  step reaches only entries under the observation's root that the porcelain list marks `prunable`. No
  other entry is ever passed to git's worktree removal. `git worktree prune`, which acts on every
  session's stale entries, is not run. Spec 64's S18 states the same clause in place of "takes away and
  prunes any that does". Spec 64's and spec 63's §5 security lines price it: the probe takes away only a
  worktree it created, or a stale entry under its own root. The literal root is the operand that id 11's
  comparison needs, and it is `TOOL-dBoundRoles-65`'s S2, because report items H1 and M8 share the root;
  this item writes no second copy. Observed by AC9.
- **S12** — id 24. Spec 64's §4 states AC8's population and its join key. The population is the lines
  S1's predicate selects. Comments and heredoc or docstring bodies are never skip lines: the adopter
  suite's comment lines 16, 26, 38, 91, 92, 96, 103, 230, 606, 791 and 989
  (`tools/roles/adopt-roles.test.sh@a8b141b6`), and the spawn guard's heredoc text "is skipped, never
  followed" (`tools/hooks/agent-cap.test.sh@97439f99:137` and `:249`). The join key: each
  `# out of the floor: <arm>` line carries the exact label its skip echo prints, up to the echo's em
  dash, such as `skip no-regress byte arm`, `SKIP arm 11` or `SKIP arm 20`, and that label is matched
  as a substring of the echo. Observed by AC1.
- **S13** — id 20. Spec 64's §4 and AC2 name `pass` as the counter the spawn guard's comparison reads,
  the suite's own counter (`tools/hooks/agent-cap.test.sh@97439f99:43`). A run that fails an assertion is red on
  `fail` already. The synthetic-value half is gone by S6's edit, so one edit closes ids 3 and 20.
  Observed by AC4.
- **S14** — id 4. Spec 64's AC18 also reads spec 63's S11 bullet and its §4 Evidence bullet about spec 53.
  Every spec-53 line number they cite must be one that S8's grep prints for spec 53 at this pass. Where
  either cites a stale line, this pass bumps spec 63. Observed by AC6.
- **S15** — id 5. Three scope halves of spec 64 gain their criteria. AC5 requires spec 61's AC2, or its
  S1 or §7, to name `gov-orienter`, `R2` and the outer `check_arm`. AC8 requires spec 62's §5 risks line
  to name the overcount beside the undercount. AC13 requires spec 63's S8 and its §5 security line to
  name the forced cleanup on every exit. Where a text lacks its half, this pass bumps that spec.
  Observed by AC10.
- **S16** — id 6. Spec 64's §4 "The executed-count rule" pins the base line's grammar: the spawn guard's
  floor comment opens `# <N> (TOOL-dBoundRoles-43)`, the number before any unit id. A first-bare-number
  read therefore returns N, and AC2, AC7 and AC9 read that grammar. The adopter suite's comment already
  opens `# 10, then`. The built spawn guard's comment takes the grammar. Observed by AC11.
- **S17** — id 7. Spec 64's §4 Evidence cites spec 52's wrapped Rollout claim at lines 102-103 at
  `5906fb79b`. Observed by AC12.
- **S18** — id 13. Spec 64's §4 Evidence last bullet reads that spec 59 carries no "How an item closes"
  and that specs 58 and 60 are the route's sources. It holds no "only specs 58 and 60 carry". Observed by
  AC12.
- **S19** — id 9. Spec 64's §4 Evidence second bullet gives the spawn guard's suite no
  `check_spec_audit` site count. It says the helper and its sites left that suite with
  TOOL-dFairHearing-16 for `tools/workflows/spec-audit-optin.test.sh`, where
  `grep -c '^[[:space:]]*check_spec_audit '` counts 54 (PINNED, `29acd2d77`) under its own floor, and that
  the suite unit 25 moves calls it from no site, so no term of E rests on it (§8 F3). Where unit 64's
  pass counted `check_spec_audit` sites into the spawn guard's E, S4's correction takes them out.
  Observed by AC12 and AC2.
- **S20** — id 14. One form for floor status, by §8 F2. The adopter suite's floor comment above
  `FLOOR_ASSERTIONS` holds no "Arm 6 is NOT in the floor", no "arm 11 is out of the floor, as arm 6
  is", no "arm 20 and arm 6's added payload are out of the floor" and no "on its SKIP path, out of the
  floor" (`tools/roles/adopt-roles.test.sh@a8b141b6:91`, `:94`, `:102` and `:103`). Arms 11 and 20 are
  each named on a `# out of the floor: SKIP arm <n>` line, and arm 6 keeps the floor lowering on its own
  skip lines. Spec 64's S12 and S33 state that rewrite, and AC8 gains a half: the floor comment holds no
  `NOT in the floor|out of the floor` outside `# out of the floor:` lines (§8 F4). Spec 64's §4
  Inventory says this build introduces the prefix. Observed by AC13.
- **S21** — id 15. Spec 64's §8 F2 and §10 cite `TOOL-aWokenSentinel-19` as the static-count precedent:
  commit `c5a31443a`, `tools/unattended/adopt-unattended.test.sh@cf6bb292:847-854`, a lower bound at
  about ten percent headroom. They say why this unit pins at E with no headroom, citing the hand-counted
  exact pins of `tools/hooks/scratch-guard.test.sh#FLOOR_ASSERTIONS`, the running total at
  `scratch-guard.test.sh@1bae0749:1859-1905`. Neither credits `TOOL-aDeferredBar-9`, an open ask, with a
  floor. F2's pick stands. Observed by AC14.
- **S22** — id 17. Spec 62's §7 spawn-guard `New arm:` line names `FLOOR_ASSERTIONS` set to the executed
  count, its comment carrying unit 43's base, the terms of units 50 and 58 and the out-of-floor arms. It
  is staged by an early exit before unit 50's case, and holds no "kept or minted". Observed by AC15.
- **S23** — id 21. Spec 64's §4 "How an item closes" pins the AMENDED ledger line:
  `- AC<n> — amended rev-<latest> (rev-<a>, rev-<b>) — <observation with a backticked token>`, the latest
  revision first and directly after the em dash. `tools/memory-tree/deviation_join.py#LEDGER`
  reads one revision per line, so the join addresses the latest bump only. Each earlier bump stays
  visible through the join's revision arm. Spec 64's AC15 and AC23 run that regex over unit 60's AC15
  line, and this unit's own AMENDED answers take the same grammar. Observed by AC16.

## 3. Non-goals (OUT)

- Id 11, the HIGH: `TOOL-dBoundRoles-65`. That unit also owns the literal observation root, the operand
  of its comparison (S11).
- Rewording specs 1 to 65 beyond what an item changes; spec 64's §4 "How an item closes" is the one
  route.
- Floors in any suite other than the roles adopter suite and the spawn guard's suite.
- The report's left-shift gates: the should-match and should-not-match checklist entry, the class-form
  Evidence entry, the guard-shares-state entry, the synthetic-staged-red entry, the joined-absence entry,
  the by-value inventory entry, the restated-list entry, the observed-by arm entry, the shared-registry
  cleanup entry, the population-and-join entry, the scope-half criterion entry, the pinned-grammar entry,
  the Evidence-command entry, the old-form retirement entry, the closed-precedent entry and the
  shipped-parser entry. No clause of this build names them; each item's criterion is its regression.

### Edges

- **consumes-from** `TOOL-dBoundRoles-64` — S1, S12, S16, S18, S23, S28, S33, §1, §3, §4, §5, §6, §7, §8 F2, §10 and the floors, comments and ledger answers its pass left, which every item restates or completes (ids 1 to 10 and 12 to 24 of the round-1 audit of unit 64)
- **consumes-from** `TOOL-dBoundRoles-63` — S8, S11, S12, S16, §4 Evidence, §5, §10 and the observation probe, which S7, S8, S10, S11, S14 and S15 restate or stage (ids 1, 4, 5, 12, 22 and 23)
- **consumes-from** `TOOL-dBoundRoles-62` — the §5 risks line and the §7 spawn-guard `New arm:` line, which S15 and S22 restate (ids 5 and 17)
- **consumes-from** `TOOL-dBoundRoles-61` — AC2, S1 and §7, which S15 has unit 64's AC5 read (id 5)
- **consumes-from** `TOOL-dBoundRoles-60` — S24 and its ledger's AC15 answer, which S9 restates and S23 parses (ids 16 and 21)
- **consumes-from** `TOOL-dBoundRoles-50` — its spawn-guard arm, whose assertions S6 counts against the term naming it (ids 3 and 20)
- **hands-off** `TOOL-dBoundRoles-69` — S4, S8, S10, S11, S12, S20, AC1, AC2, AC8, AC9, AC13, AC16, AC17, §4 and the spawn guard's floor this unit's pass leaves, which unit 69 restates or corrects: the pinned loop class and predicate, the printed worktree operand, the hard-kill recovery, the citations and ledger criteria read through the revision list (ids 2, 13, 3, 8, 22, 12, 16, 6, 23, 19, 5, 11, 17 and 18 of the round-1 audit of units 65 and 66)

## 4. Design

### Why one unit

M4 admits two units only when the minors split into two disjoint write sets by M6. They do not. Every
item writes spec 64: S1 to S7, S12, S13 and S16 to S23 restate its own text, and S8 to S11, S14 and S15
restate the clauses it wrote into specs 60 to 63. M6 clause 1 refuses any split. The suite items S4, S6,
S16 and S20 also write the two floored suites that S1 to S3 and S12 read as acceptance input, which
clause 2 refuses.

### How an item closes

Spec 64's §4 "How an item closes" is the route, with S23's grammar. Each item states the built tree's end
state. The pass does what is missing, or records that a landed unit already left it. Where an item
changes another unit's criterion or scope item, the pass bumps that unit's spec FIRST with a §9 line
naming this unit (BUILD-METHOD M2, READY), and that unit's ledger answers the criterion
`amended rev-<n>`, rewriting any earlier answer in place.

### Where each item lands at order 37

Every other unit has built, unit 64 included, so its pass has written the floors, the comments and the
ledger answers these items correct. `TOOL-dBoundRoles-65` shares order 37 and writes specs 63 and 64 too.
`--dispatch` sequences the two (§4 Rollout). This unit's criteria read only its own clauses, and S10's
staged half imports `branch_reconcile` itself, so it holds whichever of the two lands first.

### The skip-line predicate and the join

```python
import re
SKIP = re.compile(r'^[ \t]*(echo|printf) "[Ss][Kk][Ii][Pp] ')
OUT = re.compile(r'^# out of the floor: (.+?)\s*$')
def label(line):          # the printed text up to the em dash
    return line.split('"', 1)[1].split(' — ', 1)[0]
```

A skip line that lowers `FLOOR_ASSERTIONS` on the same line needs no `# out of the floor:` line. Every
other skip line's label is the payload of exactly one such line, and every such line's payload is a
substring of some skip echo. The comparison line never matches, because its echo opens `FAIL`. The block
shows the design's shape; the pass fits it to spec 64's AC8.

### The per-term count

The unit-50 arm is the section from its `# ---- ` header to the next. Its count applies §4's table of spec
64 to that section alone: one per assertion call, the list length for a loop over a literal list, and k
per call for a helper asserting k times. The term's n must equal that count. Unlike the scratch-shell
half it replaces, this can fail: a term of 6 over an arm executing 5 floored assertions reds it.

### Evidence

Re-read at HEAD `29acd2d77` on 2026-11-22; each code line is pinned to the blob it was read at:

- `tools/roles/adopt-roles.test.sh@a8b141b6:239` and `:241` echo `SKIP arm 6` and lower the floor on
  the same line. `:623` and `:625` echo `SKIP arm 11`, and `:994` and `:996` echo `SKIP arm 20`
  (TOOL-aGuardedEffort-1), and those four lower nothing. `:1330` is the comparison, whose echo opens
  `FAIL` and holds "skipped". `:91-112` is the floor comment, opening `# 10, then`, with "Arm 6 is NOT in
  the floor" at `:91`, "arm 11 is out of the floor, as arm 6 is" at `:94`, "arm 20 and arm 6's added
  payload are out of the floor" at `:102` and "on its SKIP path, out of the floor" at `:103`;
  `FLOOR_ASSERTIONS=88` is at `:113`, after the terms of units 14, 2 and 1 of this build.
- `tools/hooks/agent-cap.test.sh@97439f99:43` is `pass=0; fail=0`. The helpers raising `pass` or
  `fail` are defined at `:288` (`check`), `:336` (`run_pack`), `:420` (`run_limit_call`), `:661`
  (`run_spawn`), `:681` (`run_harness`) and `:816` (`run_effort`). `check_spec_audit`, `js`, `jso`,
  `msg`, `check_cap` and `check_spawn` are not in the file: TOOL-dFairHearing-16 moved rules 0, 2 and 5
  and their arms to `tools/workflows/`. Arms open at `# ---- ` header comments, such as `:297` and
  `:319`. The one skip echo is at `:589`, and `:137` and `:249` are heredoc text. Of the sweep's 17
  lines (PINNED, `29acd2d77`), the shell loops 391, 436, 530 and 716 echo ok or FAIL or call a helper,
  and 530's body echoes `FAIL` alone.
- `tools/memory-tree/deviation_join.py#LEDGER` is the regex, `deviation_join.py@bdb5a3d1:588-609` is
  the revision arm and `:610-620` is the ledger arm, one member per matching line.
- `tools/memory-tree/check-memory-hygiene.sh@c2fc4073:3643` classifies a first line holding a backtick
  as an observation. `memory/HYGIENE.md@b76a74c0:814` gives `- AC2 — amended rev-<n> — ...`.
- `tools/unattended/adopt-unattended.test.sh@cf6bb292:847-854` derives its floor of 78 from a static
  count of 87 at about ten percent headroom (`TOOL-aWokenSentinel-19`, commit `c5a31443a`).
  `tools/hooks/scratch-guard.test.sh@1bae0749:1859-1905` is a running total of hand-counted raises,
  309 at `462d20f3` and 401 at `29acd2d77` (PINNED, `scratch-guard.test.sh@1bae0749:1905`).
  `memory/backlog/TOOL.md@558bbfee:71` shows `TOOL-aDeferredBar-9` OPEN.
- At `5906fb79b`, spec 52's Rollout wraps "writes" at line 102 and "no file this unit writes" at line
  103. `### How an item closes` heads specs 43, 44, 50, 51, 58, 60 and 63 there.
- At `29acd2d77`, spec 60's S24 names units 52, 53 and 58 and no unit 50, 60 or 61. Spec 62's §7
  spawn-guard `New arm:` line reads "kept or minted". Spec 63's S12 names no `prunable` and no hard
  kill. Each is cited by its label, since units 64 and 65 revise those specs before this pass.
- In a scratch repository on git 2.54, git's forced worktree removal of an entry whose directory was gone
  (porcelain `prunable`) exited 0 and cleared the entry, so S10's recovery needs no global prune.

### Inventory

Minted: none. The `# ---- ` header S6 may write follows the suite's existing delimiter.

### Migration

None: no stored data changes. The ledger answers this unit writes are lines this build's passes own.

### Rollout

Live at landing, at order 37, after unit 64 at order 36. `TOOL-dBoundRoles-65` holds order 37, and its
Files touched names specs 63 and 64 and their ledgers too. The declared write sets intersect, so
`--dispatch` refuses the second pass while the first is open (M6 clause 1).

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`, the floor comment's out-of-floor lines for arms 11 and 20 (S20)
- `tools/roles/spawn-guard.test.sh`, the floor, its comment's base grammar, its terms and the unit-50 arm
  header (S4, S6, S16; S19 only through S4's correction)
- the specs of units 50, 60, 61, 62, 63 and 64, rev bumps, named here for the dispatch write set
- the acceptance ledgers of units 60, 61, 62, 63 and 64 and this unit's own, the AMENDED answers and the
  counts, named here for the dispatch write set

### Alternatives rejected

- **Two units.** §4 "Why one unit".
- **The report's option (a) for id 14, extending the prose form.** §8 F2.
- **Counting statically the assertions above an inserted exit, for ids 3 and 20.** The skeptic judged it
  as near to true by construction as the half it replaces: any floored assertion after the cut makes it
  hold.
- **The independent bound on AC7.** No pass can observe the close's run (spec 64 §8 F2), so it sits on the
  §7 lines the close observes (S5).

## 5. Production-readiness checklist

- security — no new write path. S10's staged run makes only the worktree S12 already makes, under the
  observation's own root, and S11 confines every cleanup to entries that root owns.
- perf / scale — greps, extraction probes, one staged observation and a count read from two suites' source.
- error / empty / loading states — a floor above the executed count reds the suite naming both figures; a
  probe that imports a wrong module exits non-zero.
- observability — the ledgers record each corrected count beside the loop inventory that produced it.
- risks — a hand count can still be wrong either way. S5's bound at the close catches an undercount
  larger than the out-of-floor arms, and an overcount reds the suite naming both figures.
- testing — AC1 to AC17 by extraction probes, a rewrap probe, a staged observation and a count of source;
  the arms of spec 64's §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe applies §4's `SKIP` predicate to both floored roles suites, it matches
  the two `SKIP arm 6` echoes, the two `SKIP arm 11` echoes, the two `SKIP arm 20` echoes and the
  spawn-guard echo S2 names. It
  matches no comment line, no docstring line and neither comparison line holding `-ge "$FLOOR_ASSERTIONS"`.
  Each matched echo that does not lower `FLOOR_ASSERTIONS` on its own line has its label on exactly one
  `# out of the floor:` line, and each such line's payload is a substring of a matched echo. Spec 64's §4,
  S33 and AC8 state the predicate, the population and the join.
  Red when: the predicate selects the comparison line or a comment, so AC8 reds a correct tree, or a
  hidden out-of-floor arm passes the join.
- **AC2** — When a `python -c` probe lists each line of the spawn guard's suite matching
  `^[[:space:]]*(for|while) ` whose body, up to its `done`, calls one of S4's helpers or echoes ok or FAIL,
  every listed line appears with its iteration count in this unit's ledger line for AC2, and
  `FLOOR_ASSERTIONS` equals the E that line records. Spec 64's §4 Evidence holds the sweep command and
  the instances S4 lists.
  Red when: an asserting loop is missing from the count, so the floor sits below what the suite executes.
  figure: DERIVED from source at the pass; PINNED in the ledger at that pass's commit.
  cost: a read of each loop's body, minutes.
- **AC3** — When a `python -c` probe reads spec 64's two §7 `New arm:` lines, each states the close's
  bound on the printed n less the recorded E, naming `# out of the floor:` arms as its ceiling, and spec
  64's AC7 holds no close-time comparison.
  Red when: the only check on E is the figure the same pass wrote.
- **AC4** — When a `python -c` probe counts the assertions of the section opening at the `# ---- ` header
  naming `TOOL-dBoundRoles-50` in the spawn-guard suite unit 25 adds (its path in S2 and Files touched),
  the count equals the n of the `(TOOL-dBoundRoles-50)` term above `FLOOR_ASSERTIONS`. Spec 64's AC2,
  joined, holds no "less that term" and names `pass`, and the suite's comparison line reads `$pass`.
  Red when: the unit-50 term differs from its arm's executed share and every criterion stays green.
- **AC5** — When a `python -c` probe reads spec 64's §6, it states the joined-prose absence rule once, and
  AC1, AC9 and AC19 each name the joined form. On a scratch copy of spec 63 with "carries every unit
  before 58" rewrapped across a line break, the restated AC1 check still reports the phrase, and the same
  holds for AC19's phrase in spec 63's §10.
  Red when: a retired phrase wrapped across a line passes a line grep.
  fixture: a scratch copy of spec 63 under the run's scratch directory.
- **AC6** — When a `python -c` probe runs S8's `git grep -nE` with the lines of specs 63, 64 and 66 set
  aside, spec 63's S16 Readers clause names every remaining hit's unit and line, or a reason it is not a
  reader. Every spec-53 line number that spec 63's S11 bullet and its §4 Evidence bullet cite is one the
  grep prints for spec 53. Spec 64's S28 and AC18 hold the same regex.
  Red when: an inventory reads complete and omits a citation written as a bare token.
- **AC7** — When a `python -c` probe extracts spec 60's S24, joined, it names `TOOL-dBoundRoles-50`,
  `TOOL-dBoundRoles-60` and `TOOL-dBoundRoles-61`, holds no "carries every earlier unit" and no condition
  on unit 61. Spec 64's S1, S16, S23, AC1, AC11 and AC16 each name S24.
  Red when: a restated per-suite list survives in one copy while its twin is fixed.
- **AC8** — When the observation probe of spec 63's S12 runs with its imported module name deliberately
  wrong, it exits non-zero, and a `python -c` probe over `git worktree list --porcelain -z`, comparing
  through `branch_reconcile.derive_key` with `os.path.realpath` on both sides, finds no entry equal to
  the run's own path. Spec 64's S18 and spec 63's S12 name the hard kill and the `prunable` recovery.
  Red when: a probe with no trap and no `finally` leaves its worktree registered after a failed import.
  cost: one worktree checkout of this repository, seconds.
- **AC9** — When a `python -c` probe extracts spec 63's S12, spec 64's S18 and both specs' §5 security
  lines, joined, S12 and S18 confine cleanup to the run's own path and to `prunable` entries under the
  observation's root, neither holds "takes away and prunes any that does", neither instructs a
  `git worktree prune`, and both §5 lines name the scope of what the probe may take away.
  Red when: the cleanup can force-remove another session's live worktree.
- **AC10** — When a `python -c` probe extracts spec 64's AC5, AC8 and AC13, AC5 names `gov-orienter` and
  `R2`, AC8 names spec 62's §5 overcount, and AC13 names spec 63's S8 and §5. On the built tree spec 61's
  AC2 or S1 names `gov-orienter`, `R2` and `check_arm`, spec 62's §5 risks line names the overcount, and
  spec 63's S8 and §5 security line name the forced cleanup on every exit.
  Red when: a scope half stays stale while every criterion is green.
- **AC11** — When a `python -c` probe reads the first comment line above `FLOOR_ASSERTIONS` in the
  spawn-guard suite unit 25 adds, it matches `^# [0-9]+ \(TOOL-dBoundRoles-43\)`, and that number plus
  every `+<n>` term equals the floor. Spec 64's §4 states the grammar.
  Red when: a compliant spelling puts the unit id first, so a first-bare-number read returns 43.
- **AC12** — When a `python -c` probe reads spec 64's §4 Evidence, it cites spec 52 at `102-103`, holds no
  "only specs 58 and 60 carry", names the review kit's spec-audit opt-in suite (its path in S19) as
  where `check_spec_audit`'s sites went, and gives the spawn guard's suite no `check_spec_audit` site
  count.
  Red when: an Evidence line a builder re-checks names a wrong line, a false census or a short count.
- **AC13** — When a `python -c` probe reads the comment block above `FLOOR_ASSERTIONS` in the roles
  adopter suite (its path in S1 and Files touched), it holds a `# out of the floor: SKIP arm 11` line
  and a `# out of the floor: SKIP arm 20` line, and no match of `NOT in the floor|out of the floor`
  outside `# out of the floor:` lines. Spec 64's
  §4 Inventory says this build introduces the prefix.
  Red when: the comment states one arm's floor status two ways.
- **AC14** — When a `python -c` probe extracts spec 64's §8 F2 and §10, joined, both name
  `TOOL-aWokenSentinel-19` and `c5a31443a`, F2 cites the hand-counted `FLOOR_ASSERTIONS` of the
  scratch-guard suite (its path in S21) by a blob-pinned line or by symbol, and neither credits
  `TOOL-aDeferredBar-9` with a floor.
  Red when: a resolved fork rests on a precedent that never happened.
- **AC15** — When a `python -c` probe reads spec 62's `New arm:` line on the spawn-guard suite unit 25
  adds, it holds no "kept or minted" and names `TOOL-dBoundRoles-50` or "unit 50".
  Red when: spec 62's arm declaration contradicts its own bumped scope.
- **AC16** — When a `python -c` probe runs `LEDGER` from `tools/memory-tree/deviation_join.py` over
  unit 60's AC15 ledger line, it matches at the revision whose §9 line names `TOOL-dBoundRoles-64`, with
  any earlier revision in parentheses after it. Spec 64's §4 "How an item closes" states the grammar, and
  its AC15 and AC23 run that regex.
  Red when: a token-first or two-revision line gives the deviation join no member, or the wrong one.
- **AC17** — When a `python -c` probe reads the `**Evidences:**` blocks of units 60 to 64, no criterion
  label is answered twice in one block, and each criterion this unit changed answers
  `amended rev-` at the revision whose §9 line names `TOOL-dBoundRoles-66`, in S23's grammar.
  Red when: an amendment adds a second answer beside the first.

## 7. Gates

`roles adopter self-test` · `spawn-guard self-test` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`spawn-guard self-test` is the spawn guard's suite, the leg unit 25's pass renamed at `00a96bb43`. No arm
moves here: the floor and comment corrections are re-observed by spec 64's
two `New arm:` lines, carrying the bound S5 adds.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause, so veto 1 discards
  (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1
  set. widens: none · relaxes: none
- **F2 — The adopter suite's floor status: the existing prose form, or the line grammar (id 14)?**
  Options: (a) extend the prose, and have AC8 read arm names from the floor comment's "out of the floor"
  phrases; (b) keep the `# out of the floor: <arm>` lines, rewrite the prose at
  `tools/roles/adopt-roles.test.sh@a8b141b6:91-103` into them, and have AC8 grep for the old form. (a) leaves AC8
  parsing free prose, where "NOT in the floor" beside "+1 for arm 6" already states arm 6's status two
  ways. (b) gives one form a probe can join to the skip echoes (S12). Both stay in the file S20 writes.
  RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the most feature-rich survivor. widens: none · relaxes: none
- **F3 — Id 9's count, once its helper left the suite (S19, AC12)?** TOOL-dFairHearing-16 moved
  `check_spec_audit` and its sites to `tools/workflows/spec-audit-optin.test.sh`, which carries its own
  floor, and the suite unit 25 moves calls it from no site (§4 Evidence). Options: (a) S19 has spec
  64's Evidence give the spawn guard's suite no `check_spec_audit` count and name where the sites went,
  and AC12 checks both; (b) keep the figure 54 and point it at the review kit's suite; (c) retire S19.
  (b) books a count of a suite no unit of this build floors into the spawn guard's Evidence, the false
  census id 9 exists to refuse, and (c) drops an item whose stale claim still sits in spec 64. RESOLVED
  (agent, 2026-11-22, delegated): (a), rung 3, the survivor that keeps id 9's item and its criterion's
  number. widens: none · relaxes: AC12 no longer requires the figure 54
- **F4 — The adopter suite's arm 20, absent at base, states its floor status in prose too (S20,
  AC13)?** At `29acd2d77` arm 20 skips without lowering the floor, and the comment says "arm 20 and arm
  6's added payload are out of the floor" and "on its SKIP path, out of the floor", which AC13's
  `NOT in the floor|is out of the floor` misses. Options: (a) keep that pattern, leaving arm 20's status
  stated twice and AC13 green on that break; (b) add `are`, catching `:102` but not `:103`; (c)
  `NOT in the floor|out of the floor` outside `# out of the floor:` lines, catching every prose
  statement in the block, the form unit 69's S18 later takes to the whole file. (a) keeps AC13 green on
  the break it names, and (b) leaves one prose statement of arm 6's payload. RESOLVED (agent,
  2026-11-22, delegated): (c), rung 3, the most feature-rich survivor. widens: S20 rewrites two more
  prose lines of the same comment and adds the arm-20 line · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the 11 MEDIUM and 12 LOW findings of the round-1 audit of unit 64,
  each id its own item, in one unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-69, the minors batch of the round-1 audit of units 65 and 66; nothing else moved.
- rev-3 · 2026-11-22 · S1 S2 S3 S4 S8 S12 S13 S19 S20 S21 S23 · §4 · AC1 AC2 AC12 AC13 AC14 AC16 · §8
  F2 F3 F4 · §10 · re-grounded at HEAD `29acd2d77` by
  `2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-brief`. TOOL-dFairHearing-16 moved rules 0, 2 and 5
  out of `tools/hooks/agent-cap.test.sh`, so its skip echoes fall from four to one (S2), its asserting
  helpers are `check`, `run_pack`, `run_limit_call`, `run_spawn`, `run_harness` and `run_effort` and its
  asserting loops 391, 436, 530 and 716 at `@97439f99` (S4), its counter sits at `:43` (S13), and
  `check_spec_audit`'s sites now live in `tools/workflows/spec-audit-optin.test.sh` (S19, AC12, F3).
  The adopter suite grew arm 20, a skip with no lowering, so its echoes are six and S20 and AC13 cover
  arm 20's prose too (F4); its comparison sits at `@a8b141b6:1330` and its floor comment at `:91-112`.
  S8's grep prints no bare-token hit at HEAD. The Evidence citations are re-pointed to blob-pinned
  lines: `LEDGER` by symbol, the hygiene classifier at `@c2fc4073:3643`, HYGIENE's line at
  `@b76a74c0:814`, the adopter e2e floor at `@cf6bb292:847-854`, scratch-guard's running total at
  `@1bae0749:1859-1905`, and the backlog row at `@558bbfee:71`. `tools/roles/spawn-guard.test.sh`, its
  floor and its `# out of the floor:` lines are units 25's and 64's, checked against spec 25's S5 and
  spec 64's S12 and S33, not HEAD; sibling-spec clauses are cited by label.
- rev-4 · 2026-11-24 · §7 · the leg line and the sentence below it name `spawn-guard self-test`, as
  `tools/gate-legs.json` does since TOOL-dBoundRoles-25's `00a96bb43`, by
  `2026-11-24-prompt-TOOL-dBoundRoles-60-spec-fix-brief`; no scope item or criterion moved.

## 10. Reuse audit

The seams are the units' own and the tree's: spec 64's "How an item closes" route and executed-count rule,
the suites' `# ---- ` arm delimiter and `FLOOR_ASSERTIONS` comment,
`tools/memory-tree/deviation_join.py#LEDGER`, which AC16 runs rather than re-derives, and
`tools/branch-reconcile/branch_reconcile.py`'s `derive_key`, the comparison `TOOL-dBoundRoles-65` adopts,
which AC8 imports. Each is extended, not rebuilt.
`python tools/codebase-map/reuse_lookup.py "a criterion predicate selects the skip lines a test suite prints and joins each to a floor comment"`
ranked `skip`, `check_line`, `render_line`, `parse_conf_line` and `unfenced_lines`, none a selector of a
suite's skip echoes, so no existing seam fits beyond those named. The recall query's hits include
`TOOL-aSparedSpawn-21`, an open ask for `tools/memory-tree/check-arms.py` to compare a floored suite's
floor against its executed lines, which that file does not yet do (it grades `fail` branches), and
`TOOL-dDerivedDocket-49`, which derived a floor from a block's own assertion lines because a pass runs
no suite, the rule spec 64 follows.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion select lines of a suite by a pinned predicate with should-match and should-not-match controls" --terms "skip line predicate floor comment out of the floor executed count loop sweep ledger amended rev deviation join absence check joined lines"`
