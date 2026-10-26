# TOOL-dBoundRoles-64 — the round-1 audit of units 61 to 63, its 32 minors: floors at the executed count naming every unit, a negative case inverting its verdict, criteria failing on the text they retire, no stray worktree, and an edge per bumped spec

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-64-round6-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-64-round6-fix-return.md) | research | TOOL-dBoundRoles-42 |
| [2026-10-26-prompt-TOOL-dBoundRoles-64-round6-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-64-round6-fix-brief.md) | research | TOOL-dBoundRoles-42 |
| [2026-10-26-review-TOOL-dBoundRoles-64-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-64-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted specs 61, 62 and 63
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md`) exited
CONVERGED with no blocker and no high, and confirmed 18 MEDIUM and 14 LOW findings. BUILD-METHOD M4
promotes every one, batched into one unit: they do not split into two disjoint write sets by M6 (§4 "Why
one unit"). This unit takes all 32, report ids 1 to 33 less id 18, which the audit refuted. Each id is its
own scope item, even where the report merged several into one item. S33 is the defect of ids 1 and 19 on
the other floored suite, found while grounding them (§8 F4).

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 1, 19 | unit 62 S2, S3, AC2, AC3; unit 63 S2, AC1; unit 60 AC15; the spawn guard's suite | S1, S2 |
| M2 | 2, 9, 25 | unit 63 S6, AC5; unit 60 AC4; spec 52 §4 Rollout | S3, S4, S5 |
| M3 | 3, 10 | unit 63 S17, AC14; spec 60 §4 Evidence | S6, S7 |
| M4 | 4, 22, 30 | unit 61 S1, S5, §7, AC4; unit 63 AC4; the roles adopter suite | S8, S9, S10 |
| M5 | 11, 31 | unit 62 S2, §5; the spawn guard's suite | S11, S12 |
| M6 | 12 | unit 62 S1 | S13 |
| M7 | 16, 32 | unit 62 S1, AC1, §4, §7; the waiver file | S14, S15 |
| M8 | 20 | unit 62 S3, AC3; unit 61 S4; unit 60 AC15 | S16 |
| M9 | 24 | unit 63 §4 Files touched | S17 |
| M10 | 33 | unit 63 S8, S12, §5, AC11 | S18 |
| L1 | 13 | unit 62 S3 | S19 |
| L2 | 5, 14 | unit 63 S4, AC3; unit 60's ledger | S20, S21 |
| L3 | 6 | unit 63 §4; unit 60's ledger | S22 |
| L4 | 7, 21 | unit 62 S3, AC3; unit 60 AC15; the roles adopter suite | S23, S24 |
| L5 | 8, 23 | unit 61 AC1, §4 "The capture" | S25, S26 |
| L6 | 15, 29 | unit 63 S16 | S27, S28 |
| L7 | 17 | unit 63 §10 | S29 |
| L8 | 26 | unit 63 §3; specs 19, 45, 49, 52, 53, 54 and 55 §3 | S30 |
| L9 | 27 | unit 62 §3; spec 58 §3 | S31 |
| L10 | 28 | unit 62 §4 Evidence, §10 | S32 |
| none | none | the roles adopter suite's arms whose arm lines moved no floor | S33 |

## 2. Scope (IN)

- **S1** — id 1. Spec 62's S2 and S3 and spec 63's S2 name `TOOL-dBoundRoles-50` beside unit 58 among the
  units the spawn guard's floor carries a term for. None of the three says the base "carries every earlier
  unit" or "every unit before 58". Spec 60's AC15, as unit 62 restated it, names units 50 and 58 for the
  spawn guard's suite. Observed by AC1.
- **S2** — id 19. The comment above `FLOOR_ASSERTIONS` in `tools/roles/spawn-guard.test.sh` carries a
  `+<n> for <case> (TOOL-dBoundRoles-50)` term for the floored assertions unit 50's arm adds (spec 50 §7,
  covers AC16), and the floor is raised by it. Spec 62's AC2 and spec 63's AC1 each require that term, so
  an early exit before unit 50's case reds the comparison. Observed by AC2.
- **S3** — id 2. Spec 63's S6 and AC5 read spec 52's §4 Rollout paragraph with its lines joined and its
  whitespace collapsed, in the form 63 AC6 uses for spec 54, and assert that the joined text holds no
  "writes no file this unit writes". Observed by AC3.
- **S4** — id 9. The same joined form stands in spec 60's AC4, the half 63 S6 carries there, in place of
  the grep over wrapped prose. Observed by AC3.
- **S5** — id 25. On the built tree, spec 52's §4 Rollout, joined, holds no such claim and names
  `TOOL-dBoundRoles-26` as a writer of `tools/roles/adopt-roles.test.sh`. Where the passes of units 60 and
  63 left the wrapped claim, this pass makes that bump of spec 52. Observed by AC3.
- **S6** — id 3. Spec 63's AC14 greps spec 60 for the bare token, `grep -nF ':1615-1618'`, which must print
  nothing, and requires spec 60's fourth §4 Evidence bullet to name `:1615` and `:1619-1620`. Observed by
  AC4.
- **S7** — id 10. On the built tree, spec 60's fourth §4 Evidence bullet cites
  `tools/memory-recall/selftest.py:1615` for `desc` and `:1619-1620` for the token loop. Where unit 63's
  pass left the stale range, this pass makes that bump of spec 60. Observed by AC4.
- **S8** — id 4. Spec 61's S1 and §7 state the in-suite arm of §4 "The inverted negative case": the call
  `assert_role_reads gov-nosuch input:question` runs inside a command substitution, and one outer
  `check_arm` passes when the capture holds a FAIL line naming `gov-nosuch` and `KeyError`, and fails on
  anything else, an ok line included. AC2's refused front matter takes the same form with `gov-orienter`
  and `R2`, and the role file is restored after it. Observed by AC5.
- **S9** — id 22. On the built tree, `tools/roles/adopt-roles.test.sh` holds the two inverted cases of S8,
  so the suite stays green on a correct helper and goes red on a helper that reads stdout alone. Where
  unit 61's pass left a bare call that the suite's own `check_arm` counts, this pass rewrites it into that
  form. Observed by AC6.
- **S10** — id 30. Spec 61's S5 states that its `+<n>` term counts only the outer `check_arm` calls, `+2`,
  because the capture's subshell discards the helper's own counter increments. Spec 61's AC4 greps
  `gov-nosuch` for the call, as spec 63's AC4 does, and `TOOL-dBoundRoles-61` for the term. Observed by
  AC5.
- **S11** — id 11. Spec 62's S2 counts EXECUTED assertions by §4 "The executed-count rule": a call site in a
  loop counts once per iteration, and a helper that asserts more than once per call counts that many per
  call, as `check_spec_audit` asserts once per form. On the built tree the spawn guard's floor equals that
  count, and unit 62's ledger records the call-site figure beside the executed figure. Observed by AC7.
- **S12** — id 31. Spec 62's S2 keeps every arm that can announce a skip out of the floor, the house rule
  of `tools/roles/adopt-roles.test.sh:73-74`, and its §5 risks line prices both the undercount from call
  sites and the overcount from a skippable arm. The comment above the spawn guard's floor names each arm it
  leaves out, one `# out of the floor: <arm>` line per arm. Observed by AC8.
- **S13** — id 12. Spec 62's S1 keeps only the base: where unit 43 pinned a floor, that value is the bare
  base term, and the floor line is raised by the terms S2, S11 and S19 name. S1 holds no "keeps the value".
  Where unit 43's pin counted an arm S12 leaves out, the base is that pin less the arm's assertions, and
  the comment says which arm. Observed by AC9.
- **S14** — id 16. Spec 62's §7 leg line names `testsuite counts (every bar self-test prints one)`. Its AC1
  observes the floor's shape through that leg's own predicate, `compliant` in
  `tools/check-testsuite-counts.sh`, called on the suite, rather than by re-grepping its anchor, and
  restated AC15 takes its no-floor red from the same predicate. Observed by AC10.
- **S15** — id 32. On the built tree, `compliant` passes on the spawn guard's suite, so a PASS line in the
  anchored form is present, and `memory/project/testsuite-count-waivers.txt` holds no row naming that suite
  under either path. Spec 62's S1 fallback branch makes 43 S27's waiver half true, and its Files touched
  names the waiver file. Observed by AC10.
- **S16** — id 20. Unit 61 adds the two inverted cases of S8 and their term on every branch its S4 permits:
  the no-code branch edits no helper code and still adds them (§8 F3). So restated AC15's unit-61 entry, in
  spec 62's S3 and AC3 and in spec 60's AC15, holds on every branch, with no condition. Where unit 61's
  pass took that branch without the cases, this pass adds them, the term naming `TOOL-dBoundRoles-61` and
  this unit. Observed by AC11.
- **S17** — id 24. Spec 63's §4 Files touched names the acceptance ledgers of units 45, 53, 54, 59 and 60.
  Observed by AC12.
- **S18** — id 33. Spec 63's S12 takes the observation worktree away with `git worktree remove --force`,
  on every exit of the probe, a failed import included, by a shell trap or a finally clause, at a path
  unique per run under a short `%TEMP%` prefix. S8 and §5 say the same, and AC11 gains a half: after the
  observation, `git worktree list --porcelain` names no path under that prefix. On the built tree no
  worktree under the prefix stays registered; this pass takes away and prunes any that does. Observed by
  AC13.
- **S19** — id 13. Spec 62's S3 history clause names unit 50 beside unit 58 for the spawn guard's suite, so
  the comment it describes claims no coverage it lacks. One edit closes S1, S2 and this item. Observed by
  AC1.
- **S20** — id 5. Spec 63's AC3 gains a tree-level half: unit 60's `**Evidences:**` block holds an AC15
  line carrying the base-blob sum 50 and a backticked `git show 462d20f3:tools/roles/adopt-roles.test.sh`
  token. That line is the one S22 keeps. Observed by AC14.
- **S21** — id 14. That line exists on the built tree. Where unit 63's pass recorded the base reading
  elsewhere or not at all, this pass makes the reading and writes it there. Observed by AC14.
- **S22** — id 6. Spec 63's §4 "How an item closes" states that a later amendment of a criterion rewrites
  the earlier answer in place: unit 60's ledger holds one AC15 line, `amended rev-<m>`, naming the
  revisions of both bumps, unit 62's and unit 63's. This unit's own amendments keep the same rule (§4 "How
  an item closes"). Observed by AC15 and AC23.
- **S23** — id 7. Spec 62's S3 and AC3 and spec 60's AC15 name unit 60 among the units the adopter suite's
  floor carries a term for, for the cases of 60 S36. Observed by AC16.
- **S24** — id 21. On the built tree, the adopter suite's comment holds a `+<n>` term naming
  `TOOL-dBoundRoles-60`. Where unit 60's raise was folded into another unit's term, this pass splits it
  out. Observed by AC16.
- **S25** — id 8. Spec 61's AC1 lists `$TMP_ROOT`, a scratch directory, among the names its driver
  defines. Observed by AC17.
- **S26** — id 23. Spec 61's §4 "The capture" refuses an empty `TMP_ROOT` before the redirect, by
  `: "${TMP_ROOT:?}"`, so a driver that omits it fails naming the variable rather than writing at the
  filesystem root. The helper holds the same guard on the built tree; where unit 61's pass left it out,
  this pass adds it. Observed by AC17.
- **S27** — id 15. Spec 63's S16 Readers clause names spec 52's citation of the read-set parse for the
  `ap.error` refusal as one that stays, as it names 53's citations of that refusal. Observed by AC18.
- **S28** — id 29. The clause accounts for every spec line the grep it names prints outside specs 63 and
  64, each by its unit and line as the grep prints them at this pass, after S30's bumps have moved them.
  Spec 63's S11 and §4 Evidence, where they cite spec 53 by line, take the same lines. Observed by AC18.
- **S29** — id 17. Spec 63's §10 reads "58's and 60's 'How an item closes' route". Observed by AC19.
- **S30** — id 26. Spec 63's §3 gains a **consumes-from** bullet for each of units 19, 45, 49, 52, 53, 54
  and 55, each naming the items of 63 that rest on it. Each of those seven specs gains the mirroring
  **hands-off** bullet naming `TOOL-dBoundRoles-63`, a rev bump with its §9 line. Observed by AC20.
- **S31** — id 27. Spec 62's §3 gains a **consumes-from** bullet for `TOOL-dBoundRoles-58`, naming its
  spawn-guard arms, which S2 floors, and its New arm line, which S4 bumps. Spec 58 gains the mirroring
  **hands-off** bullet, a rev bump with its §9 line. Observed by AC21.
- **S32** — id 28. Spec 62's §4 Evidence and §10 cite `tools/roles/adopt-roles.test.sh:73-80` as the
  comment shape S2 wants. They keep `tools/hooks/scratch-guard.test.sh:1303-1321` only as the shape of the
  comparison line, and say its running-total comment is not that shape. Observed by AC22.
- **S33** — no report id; the defect of ids 1 and 19 on the other floored suite (§8 F4). On the built tree,
  `FLOOR_ASSERTIONS` in `tools/roles/adopt-roles.test.sh` equals its executed count by §4's rule. Where its
  base and named terms fall short, because units' arm lines named no floor (§4 Evidence), one
  `+<n> for the arms of units <ids> whose arm lines moved no floor (TOOL-dBoundRoles-64)` term carries the
  rest. Each skip branch either lowers the floor on its own line, as arm 6 does, or its arm is named on a
  `# out of the floor: <arm>` line. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- Id 18, refuted by the audit as a preference.
- Rewording specs 1 to 63 beyond what an item changes; §4 "How an item closes" is the one route.
- Floors in any suite other than the roles adopter suite and the spawn guard's suite, and the leg rename
  unit 25 owns.
- The report's left-shift gates: the join of `New arm:` lines by suite and order, the check refusing a grep
  already silent at the spec's base, the wrapped-phrase checklist entry, the negative-case checklist entry,
  the executed-count gap check, the keep-against-sum checklist entry, the testsuite-counts-in-§7 check, the
  every-branch checklist entry, the ledger write-set check, the worktree-cleanup checklist entry, the
  two-answers hygiene refusal, the pinned-blob criterion flag, the Readers re-run check, the section
  citation resolver, the reciprocity-join extension, the floor-comment grammar check and the scratch-driver
  checklist entry. No clause of this build names them; each item's criterion is its regression.

### Edges

- **consumes-from** `TOOL-dBoundRoles-61` — S1, S4, S5, §4 "The capture", §7, AC1 and AC4, and the cases its pass built, which S8 to S10, S16, S25 and S26 restate or complete (ids 4, 8, 20, 22, 23 and 30)
- **consumes-from** `TOOL-dBoundRoles-62` — S1 to S3, §3, §4 Evidence, §5, §7, AC1 to AC3 and the spawn guard's floor its pass left, which S1, S2, S11 to S16, S19, S23, S24, S31 and S32 restate or complete (ids 1, 6, 7, 11, 12, 13, 16, 19, 20, 21, 27, 28, 31 and 32)
- **consumes-from** `TOOL-dBoundRoles-63` — S2, S4, S6, S8, S11, S12, S16, §3, §4, §5, §10, AC1, AC3, AC4, AC5, AC11 and AC14, which S1 to S3, S6, S10, S17, S18, S20 to S22 and S27 to S30 restate (ids 1, 2, 3, 4, 5, 6, 9, 10, 14, 15, 17, 19, 24, 25, 26, 29 and 33)
- **consumes-from** `TOOL-dBoundRoles-60` — AC4, AC15, §4 Evidence and its ledger's AC15 answer, which S1, S4, S7, S16, S20 to S23 restate or complete (ids 1, 3, 5, 6, 7, 9, 10, 14, 19, 20 and 21)
- **consumes-from** `TOOL-dBoundRoles-50` — its spawn-guard arm, whose floored assertions S2's term carries (ids 1, 13 and 19)
- **consumes-from** `TOOL-dBoundRoles-43` — its pinned spawn-guard floor and S27's waiver half, which S13 takes as the base and S15 completes (ids 12, 16 and 32)
- **consumes-from** `TOOL-dBoundRoles-58` — its spawn-guard arms and §3, into which S31 writes the hands-off bullet for unit 62 (id 27)
- **consumes-from** `TOOL-dBoundRoles-52` — §4 Rollout and §3, which S5 corrects and S30 extends by the hands-off bullet for unit 63 (ids 25 and 26)
- **consumes-from** `TOOL-dBoundRoles-19` — its commit, at whose parent S18's worktree is checked out, and §3, which S30 extends (ids 26 and 33)
- **consumes-from** `TOOL-dBoundRoles-45` — §3, which S30 extends by the hands-off bullet for unit 63 (id 26)
- **consumes-from** `TOOL-dBoundRoles-49` — its AC1 import form, which S18's probe keeps, and §3, which S30 extends (id 26)
- **consumes-from** `TOOL-dBoundRoles-53` — its citations of the read-set parse, which S28 re-reads, and §3, which S30 extends (ids 26 and 29)
- **consumes-from** `TOOL-dBoundRoles-54` — §3, which S30 extends by the hands-off bullet for unit 63 (id 26)
- **consumes-from** `TOOL-dBoundRoles-55` — §3, which S30 extends by the hands-off bullet for unit 63 (id 26)
- **hands-off** `TOOL-dBoundRoles-65` — S18 and AC13, which unit 65 restates: the worktree check compared through normalised keys under spec 63's named root, with a positive control that must report a planted leftover (id 11 of the round-1 audit of unit 64)
- **hands-off** `TOOL-dBoundRoles-66` — S1, S12, S16, S18, S23, S28, S33, §1, §3, §4, §5, §6, §7, §8 F2, §10 and the floors, comments and ledger answers this unit's pass leaves, which unit 66 restates: one skip predicate and its join, loops swept by class, the unit-50 term tied to its arm, joined absence checks, the staged failed import and the owned cleanup (ids 1 to 10 and 12 to 24 of the round-1 audit of unit 64)
- **hands-off** `TOOL-dBoundRoles-69` — S12, S18, §4 "The executed-count rule" table and §5, which unit 69 restates: the `<label>` payload, S18 citing spec 63's cleanup rule, the stale entry priced and the `dbr63obs` spelling (ids 12, 19, 9 and 17 of the round-1 audit of units 65 and 66)

## 4. Design

### Why one unit

M4 admits two units only when the minors split into two disjoint write sets by M6. They do not. The
spec-61 items (ids 4, 8, 22, 23 and 30) write spec 63's AC4 and the roles adopter suite. The spec-62 items
write spec 63's S2 (id 1) and its ledger answer (id 6), and read the adopter suite's floor as an
acceptance input (ids 7, 20 and 21). The spec-63 items write spec 63 throughout. Every half writes spec 63,
which M6 clause 1 refuses, and the adopter suite is one half's write and another's acceptance input,
which clause 2 refuses.

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a landed
unit already left it. Where an item changes another unit's criterion or scope item, the pass bumps that
unit's spec FIRST with the changed text and a §9 line naming this unit (BUILD-METHOD M2, READY), and that
unit's ledger answers the criterion `amended rev-<n>`, naming the revision (58 §4 "How an item closes").
One line answers one criterion: where the ledger already holds an answer, the amendment rewrites that
line in place and names every revision that changed the criterion, never a second line beside it.

### Where each item lands at order 36

Every other unit has built, units 61, 62 and 63 included. Unit 25 moved the spawn guard's suite to
`tools/roles/spawn-guard.test.sh`, so the items read it there. S30's edge bumps precede S28, whose line
numbers they move.

### The executed-count rule

Both floored roles suites take one rule, so a floor bounds what the suite runs rather than what its source
spells. The count E is read from source, as `tools/hooks/scratch-guard.test.sh` counted its raises by hand
because a pass runs no suite.

| Source shape | Counts toward E |
|---|---|
| one assertion call, or one pass-or-fail branch pair | 1 per execution |
| a call inside a loop over a literal list | 1 per item of the list |
| a call inside a loop over a computed list | the fewest items the list can hold, the comment saying so |
| a helper asserting k times per call | k per call site |
| an arm with a skip branch that lowers the floor on its own line | its assertions, less what the branch lowers |
| any other arm with a skip branch | 0, named on a `# out of the floor: <arm>` line |

`FLOOR_ASSERTIONS` equals E. The comment above it is a bare base term plus `+<n> for <case> (<unit>)`
terms, summing to E. Where the named terms fall short, one term naming this unit carries the rest and
lists the units whose arms it counts. Where they exceed E, the term that overcounts is corrected to the
count, and the comment says which arm it no longer counts. The pass records E and the call-site count per
suite in the ledger. The close's run of each suite prints `PASS (<n> assertions)`; n at or above E is the
arm's green, and the main loop records n beside E.

### The inverted negative case

```bash
# TOOL-dBoundRoles-61: a role slot with no file must FAIL the helper, and this arm passes on that FAIL.
inv=$(assert_role_reads gov-nosuch input:question)
case "$inv" in
  *FAIL*gov-nosuch*KeyError*) check_arm "reads: a missing slot fails the read check" 1 ;;
  *) check_arm "reads: a missing slot fails the read check, got: ${inv:-nothing}" 0 ;;
esac
```

The substitution runs the helper in a subshell, so the helper's own `check_arm` raises `n` and `fail`
there, and the suite counts only the outer arm. The refused-front-matter case takes the same shape over a
copy of the fixture's `gov-orienter.agent.md` with its `reads:` key indented, matching `gov-orienter` and
`R2`, and copies the file back after. The block is the design's shape; the pass fits it to the suite's
labels.

### Evidence

Read at base `462d20f3` on 2026-10-26 for code, and at the spec commit `5906fb79b` for spec lines:

- `tools/roles/adopt-roles.test.sh:51` is `set -u`, `:71` sets `TMP_ROOT`, `:73-80` is the comment whose
  first bare number 10 and thirteen terms sum to `FLOOR_ASSERTIONS=50` at `:81`, and `:83` defines a
  `check_arm` that raises `fail` on any verdict but 1. `:170` and `:172` lower the floor on arm 6's SKIP,
  `:432` and `:434` print arm 11's SKIP with no lowering, and `:715` prints `PASS ($n assertions)`.
- `tools/hooks/agent-cap.test.sh`, the spawn guard's suite before unit 25 moves it, holds no
  `FLOOR_ASSERTIONS`. It calls `check_spec_audit` from 53 sites, and the helper asserts once per form in
  `for form in object string` (`:795-797`). Loops assert at `:883` over six kinds and `:933` over four
  platforms. Skip branches sit at `:891`, `:947`, `:2043` and `:2280`. `:150` prints
  `PASS (${pass:-1} assertions)` under `FOREIGN_PREFIX_PROBE` only.
- `tools/check-testsuite-counts.sh:86-99` is `compliant`: an anchored PASS line, a non-zero floor, and a
  reference to it. The branch below it reds a waiver row naming a suite that complies.
- `memory/project/testsuite-count-waivers.txt:10` lists `tools/hooks/agent-cap.test.sh`;
  `tools/gate-legs.json:1645` names the leg `testsuite counts (every bar self-test prints one)`.
- `tools/hooks/scratch-guard.test.sh:1303-1319` is a running-total comment whose first bare number, 164, is
  a total; `:1320` pins the floor and `:1321` compares.
- Spec 43 line 524 raises the spawn guard's floor; spec 50 line 324 adds a spawn-guard arm, floor field
  `none`; spec 58 line 398 likewise. The build orders are 28, 30 and 32. Spec 62's S2 takes 43's pin as the
  base and its S3 says that base carries every earlier unit.
- The adopter suite's `New arm:` lines in specs 1, 2, 3, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 24, 26,
  38, 41, 43, 45, 47, 48 and 50 name no floor; units 52, 53 and 58 are floored by 60 S24, and units 59, 60
  and 61 name their own raise.
- Spec 52's lines 101-102 wrap "writes" / "no file this unit writes"; its line 28 cites the read-set parse
  for `ap.error`. Spec 60's line 222 cites the bare `:1615-1618`. `tools/memory-recall/selftest.py:1615`
  assigns `desc` and `:1619-1620` hold the token loop.
- Spec 61's §4 "The capture" redirects to `"$TMP_ROOT/reads.err"`, and its AC1 driver defines only
  `check_arm`, `$PY`, `$FX` and `$FXK`. Its S4 permits a branch that edits no code, while its AC4 needs a
  term naming the unit.
- Spec 63's §10 cites "59's and 60's" route; only specs 58 and 60 carry "How an item closes". Spec 60's §3
  declares a consumes-from edge for every spec it bumps; spec 63's §3 names units 59 to 62 only, and spec
  62's names units 60, 61 and 63.

### Inventory

Minted: none. The `# out of the floor:` prefix is a comment convention of the two suites, not an
identifier.

### Migration

None: no stored data changes. The ledger answers this unit writes are lines this build's passes own.

### Rollout

Live at landing, at order 36, after every unit it repairs. No other unit holds order 36.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`, the inverted cases, the `TMP_ROOT` guard and the floor (S9, S16, S24,
  S26, S33)
- `tools/roles/spawn-guard.test.sh`, the floor, its comment and its out-of-floor lines (S2, S11 to S13,
  S15)
- `memory/project/testsuite-count-waivers.txt`, the spawn guard's row where one stands (S15)
- the specs of units 19, 45, 49, 52, 53, 54, 55, 58, 60, 61, 62 and 63, rev bumps, named here for the
  dispatch write set
- the acceptance ledgers of units 60, 61, 62 and 63 and this unit's own, the AMENDED answers, the base
  reading and the executed counts, named here for the dispatch write set

### Alternatives rejected

- **Two units.** §4 "Why one unit".
- **Keep 43's pin and add unit 50's term only.** It closes ids 1 and 19, and leaves the floor at a
  call-site count a loop can outrun (id 11).
- **Take the floor from the close's printed total.** The close runs after every pass, so no pass could
  write the figure its criterion reads (§8 F2).
- **Run either suite to count it.** A pass runs no self-test suite (M6); the rule reads source, and the
  close's run is the observation.

## 5. Production-readiness checklist

- security — no new write path; the observation worktree lives under a unique short `%TEMP%` path and goes
  on every exit.
- perf / scale — greps, probes, a scratch driver and a count read from two suites' source.
- error / empty / loading states — a floor above the executed count reds the suite naming both figures; an
  empty `TMP_ROOT` fails naming the variable.
- observability — the ledgers record each executed count beside its call-site count, and each comment names
  every unit's share and every arm left out.
- risks — a count read by hand can be wrong either way; an overcount reds the suite at the close naming
  both figures, and an undercount leaves the floor a weaker bound, which the main loop's record of n beside
  E shows.
- testing — AC1 to AC23 by grep, probe, scratch shell and scratch driver; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe extracts spec 62's S2 and S3 bullets, spec 63's S2 bullet and spec
  60's AC15 bullet, each names `TOOL-dBoundRoles-50`, spec 60's AC15 names it for the spawn guard's suite,
  and none of the four holds `carries every earlier unit` or `carries every unit before 58`.
  Red when: a base said to carry every earlier unit leaves out unit 50's arm.
- **AC2** — When a `python -c` probe reads the comment above `FLOOR_ASSERTIONS` in the spawn guard's suite
  (its path in S2 and Files touched), its first bare number plus every `+<n>` term equals the floor, and
  one term names `TOOL-dBoundRoles-50`. A scratch shell then evaluates only the suite's floor and
  comparison lines, copied out by `grep`, with the executed count set to the floor less that term: it
  prints the failure line. Spec 62's AC2 and spec 63's AC1 each name `TOOL-dBoundRoles-50`. No suite runs.
  Red when: unit 50's assertions sit outside the floor, so an early exit before them leaves the suite green.
  figure: DERIVED from the file at observation time.
- **AC3** — When a `python -c` probe joins the lines of spec 52's §4 Rollout paragraph and collapses their
  whitespace, the joined text holds no `writes no file this unit writes` and names `TOOL-dBoundRoles-26`
  with the adopter suite's path. The same probe over `git show 5906fb79b` of spec 52 prints the phrase.
  Spec 63's S6 and AC5 and spec 60's AC4 each state the joined form.
  Red when: a grep over wrapped prose reads silent while the claim survives.
- **AC4** — When `grep -nF ':1615-1618'` runs over spec 60, it prints nothing, while the same grep over
  `git show 5906fb79b` of spec 60 prints its line 222. A `python -c` probe finds `:1615` and `:1619-1620`
  in spec 60's fourth §4 Evidence bullet, and the `grep -nF` form in spec 63's AC14.
  Red when: a criterion's grep is silent over the defect it retires.
- **AC5** — When a `python -c` probe extracts spec 61's S1, S5, §7 and AC4, S1 or the `New arm:` line names
  the command substitution and the outer `check_arm`, S5 names `+2`, and AC4 greps `gov-nosuch`, as spec
  63's AC4 does.
  Red when: an in-suite negative case states no verdict inversion and no floor count.
- **AC6** — When a scratch driver defines `check_arm` with its own counter, `$PY`, `$FX`, `$FXK` and
  `$TMP_ROOT` over the roles adopter fixture, and sources the `assert_role_reads` definition and the two
  inverted cases from the roles adopter suite, it prints two ok lines and its counter rises by
  exactly 2. With the helper staged back to reading stdout alone, both lines print FAIL. And
  `grep -n 'gov-nosuch' tools/roles/adopt-roles.test.sh` prints a line inside a `$(` capture.
  Red when: the suite's own `check_arm` counts the expected FAIL, so the suite reds on a correct tree.
  fixture: a scratch repository with the roles kit installed by `build_fixture`'s steps, under `%TEMP%`,
  short-pathed.
- **AC7** — When the pass counts each floored roles suite by §4 "The executed-count rule", unit 62's
  `**Evidences:**` block holds one AC2 line naming the spawn guard's call-site count and its executed count,
  and this unit's block an AC7 line naming both counts for the adopter suite. A `python -c` probe then finds
  each suite's `FLOOR_ASSERTIONS` equal to the executed count recorded for it, and its base plus terms
  equal to the floor.
  Red when: a floor sits at a call-site count while the suite's loops execute more.
  figure: DERIVED from source at the pass; PINNED in the ledger at that pass's commit.
  cost: a read of each suite's loops and helpers, minutes.
- **AC8** — When a `python -c` probe reads each floored roles suite, every line printing a skip, case-folded,
  either lowers `FLOOR_ASSERTIONS` on that line or names an arm that a `# out of the floor:` line names, and
  every such comment line names an arm some skip line prints. Spec 62's S2 names loop iterations and
  skippable arms, and its §5 risks line names the undercount.
  Red when: a skippable arm is counted, so the floor reds where it skips, or the comment hides an arm it
  leaves out.
- **AC9** — When a `python -c` probe extracts spec 62's S1 bullet, it holds no `keeps the value` and names
  unit 43's pinned value as the bare base term, and the spawn guard's comment names `TOOL-dBoundRoles-43` on
  its base.
  Red when: S1 keeps a value S2 raises, so either instruction breaks a criterion.
- **AC10** — When a scratch shell defines `compliant` from its lines in `tools/check-testsuite-counts.sh`
  and calls it on the spawn guard's suite, it returns 0, and on a scratch copy with the `FLOOR_ASSERTIONS`
  line deleted it returns 1. `grep -cE 'agent-cap\.test\.sh|spawn-guard\.test\.sh' memory/project/testsuite-count-waivers.txt`
  prints 0. Spec 62's §7 leg line names `testsuite counts (every bar self-test prints one)`, and its Files
  touched names the waiver file.
  Red when: a PASS line outside the anchored form, or a stale waiver row, passes every gate the spec names.
- **AC11** — When a `python -c` probe extracts spec 61's S4, its no-code branch adds the inverted cases and
  their term; spec 62's S3 and AC3 and spec 60's AC15 name unit 61 for the adopter suite with no condition;
  and `grep -n 'TOOL-dBoundRoles-61' tools/roles/adopt-roles.test.sh` prints a `+<n>` term above
  `FLOOR_ASSERTIONS`.
  Red when: restated AC15 needs a term on a branch unit 61's spec lets close without one.
- **AC12** — When a `python -c` probe extracts spec 63's `### Files touched (estimate)`, it names the
  acceptance ledgers of units 45, 53, 54, 59 and 60.
  Red when: a pass writes a ledger its declared set omits.
- **AC13** — When a `python -c` probe extracts spec 63's S12, it names `git worktree remove --force`, a
  cleanup on every exit and a path unique per run, and spec 63's AC11 holds a
  `git worktree list --porcelain` half. On the built tree, `git worktree list --porcelain` names no path
  under S12's prefix.
  Red when: a staged break or a failed import leaves a registered worktree behind.
- **AC14** — When a `python -c` probe reads unit 60's `**Evidences:**` block, its AC15 line holds `50` and
  a backticked `git show` of the roles adopter suite at base `462d20f3`, and spec 63's AC3 states that half.
  Red when: the base reading 63 S4 requires is never recorded, and AC3 still passes on an immutable blob.
- **AC15** — When a `python -c` probe reads unit 60's `**Evidences:**` block, exactly one line answers AC15,
  it reads `amended rev-` and names the revisions of the bumps of units 62 and 63, and spec 63's §4 "How an
  item closes" states the in-place rewrite.
  Red when: two lines answer one criterion, or one stale line names an earlier revision.
- **AC16** — When a `python -c` probe extracts spec 62's S3 and AC3 and spec 60's AC15, each names
  `TOOL-dBoundRoles-60` for the adopter suite, and `grep -n 'TOOL-dBoundRoles-60' tools/roles/adopt-roles.test.sh`
  prints a `+<n>` term above `FLOOR_ASSERTIONS`.
  Red when: unit 60's raise has no term of its own, so its attribution is lost.
- **AC17** — When a `python -c` probe extracts spec 61's AC1 and its §4 "The capture", AC1 names
  `$TMP_ROOT` among the driver's names and the block holds `TMP_ROOT:?`. A scratch shell running that guard
  line with `TMP_ROOT` empty exits non-zero naming the variable, and `grep -n 'TMP_ROOT:?' tools/roles/adopt-roles.test.sh`
  prints the helper's guard.
  Red when: the driver's redirect lands at the filesystem root and the observation reds for a reason the
  exit check never meets.
- **AC18** — When a `python -c` probe runs `git grep -n 'handoff.py:1025' -- memory/builds/dBoundRoles/spec`,
  sets aside the lines of specs 63 and 64, and reads spec 63's S16 Readers clause, the clause names every
  remaining file's unit and line, spec 52's `ap.error` citation among them.
  Red when: the inventory reads complete and omits a line the grep prints.
- **AC19** — When `grep -n "59's and 60's"` runs over spec 63, it prints nothing, and spec 63's §10 names
  `58's and 60's`.
  Red when: a seam citation points at a section its spec does not carry.
- **AC20** — When a `python -c` probe reads spec 63's `### Edges`, it holds a `**consumes-from**` bullet for
  each of units 19, 45, 49, 52, 53, 54 and 55, and each of those seven specs' `### Edges` holds a
  `**hands-off**` bullet naming `TOOL-dBoundRoles-63`, with a §9 line naming it.
  Red when: a spec that bumps another unit's spec declares no edge to it.
- **AC21** — When a `python -c` probe reads spec 62's `### Edges`, it holds a `**consumes-from**` bullet for
  `TOOL-dBoundRoles-58`, and spec 58's holds a `**hands-off**` bullet naming `TOOL-dBoundRoles-62`, with a
  §9 line naming it.
  Red when: the edge graph misses that unit 62 rewrites spec 58.
- **AC22** — When `grep -n 'adopt-roles.test.sh:73-80'` runs over spec 62, it prints a §4 Evidence line,
  and a `python -c` probe finds that every line of spec 62 naming `scratch-guard.test.sh:1303` also names
  the comparison.
  Red when: the Evidence cites as the shape a comment that fails S2's sum rule.
- **AC23** — When a `python -c` probe reads the `**Evidences:**` blocks of units 60, 61, 62 and 63, no
  criterion label is answered twice in one block, and each criterion this unit changed answers
  `amended rev-` at the revision whose §9 line names `TOOL-dBoundRoles-64`.
  Red when: an amendment adds a second answer beside the first.

## 7. Gates

`roles adopter self-test` · `agent-cap self-test` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

`agent-cap self-test` stands for the spawn guard's suite; unit 25's pass renames it on every live §7 line
when it renames the leg. The two recall legs are owed by the waiver file's guard.

New arm: tools/roles/adopt-roles.test.sh · covers AC6 AC7 · the two inverted negative cases, staged by the helper reading stdout alone, and the floor at the executed count, staged by an early exit before unit 61's cases · `FLOOR_ASSERTIONS` set to the executed count, with terms naming units 60 and 61 and this unit's term for the arms that moved no floor

New arm: tools/roles/spawn-guard.test.sh · covers AC2 AC7 AC8 · the floor comparison, staged by an early exit before unit 50's case · `FLOOR_ASSERTIONS` set to the executed count, its comment carrying the base, the terms of units 50 and 58 and the out-of-floor arms

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause; veto 1 discards (b).
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — The spawn guard's floor: the executed count read from source, or the close's printed total (ids 11
  and 31)?** Options: (a) §4 "The executed-count rule", read by the pass; (b) the `$pass+$fail` total the
  close's run prints, lowered where a skip applies. (b) exists only after every pass, so no pass can write
  the figure, and AC7 could not be observed. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  most feature-rich survivor, as `TOOL-aDeferredBar-9` floored a suite from a static count less its
  host-conditional arms. widens: none · relaxes: none
- **F3 — Unit 61 in restated AC15: required on every branch, or only where its pass added the cases (id
  20)?** Options: (a) a conditional entry; (b) unit 61's no-code branch still adds the two inverted cases and
  their term. (a) leaves the negative case unbuilt on that branch and 61's own AC4 red there; (b) closes
  both. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the most feature-rich survivor. widens: none ·
  relaxes: none
- **F4 — The adopter suite's arms whose arm lines moved no floor: in this unit, or out?** Options: (a) S33
  applies §4's rule to that suite too; (b) a non-goal, left for a later audit. No finding names it, and it
  is the defect of ids 1 and 19 on the suite restated AC15 covers beside the spawn guard's. (a) adds no
  dependency, surface or write path beyond the file S9 already writes. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most feature-rich survivor and the charter's gate-the-class rule. widens:
  none · relaxes: none
- **F5 — The spawn guard's base: unit 43's pin, or a count re-derived at this pass (ids 1, 12 and 13)?**
  Options: (a) 43's pin is the bare base term, and the terms of units 50 and 58 and this unit's catch-up
  term raise it to E; (b) a base re-derived as E less the named terms. Both reach the same floor. (a) keeps
  the floor's history readable, and it is the report's fix for id 12. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, fewest follow-ups. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the 18 MEDIUM and 14 LOW findings of the round-1 audit of units 61
  to 63, each id its own item, in one unit, with S33 for the same class on the adopter suite. Before its
  commit, the round-6 fix brief shortened the H1 by 29 characters so its index row fits the 350 cap, and
  named the adopter suite in prose in AC6 and AC14.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-65 and TOOL-dBoundRoles-66, the HIGH promotion and the minors batch of the round-1 audit of unit 64; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-69, the minors batch of the round-1 audit of units 65 and 66; nothing else moved.

## 10. Reuse audit

The seams are the units' own: 58's and 60's "How an item closes" route, the suites' shrink-only
`FLOOR_ASSERTIONS` convention in the comment shape `tools/roles/adopt-roles.test.sh:73-80` carries, the
`compliant` predicate of `tools/check-testsuite-counts.sh:86-99`, which AC10 calls rather than copies,
the suite's `check_arm` and unit 61's `assert_role_reads`, and git's own worktree, each extended rather
than rebuilt.
`python tools/codebase-map/reuse_lookup.py "a suite floor counts executed assertions inside loops and leaves skipping arms out"`
ranked `skipped`, `counts`, `arm`, `run_arms` and `check_arm`, none a count of a suite's executed
assertions read from source, so no existing seam fits beyond those named. The recall query's hits are
`TOOL-aWokenSentinel-19` and `TOOL-aWokenSentinel-21`, each declaring a floor in a suite that had none,
and `TOOL-aDeferredBar-9`, which floors a suite from a static count less its host-conditional arms, the
precedent §8 F2 follows.

Recall terms used: `python tools/memory-recall/query.py "how does a floored suite count looped assertions and invert an expected failing case" --terms "FLOOR_ASSERTIONS executed count loop iterations skip arm inverted negative case check_arm compliant testsuite counts"`
