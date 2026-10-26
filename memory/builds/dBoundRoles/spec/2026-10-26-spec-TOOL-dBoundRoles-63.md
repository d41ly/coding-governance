# TOOL-dBoundRoles-63 — the round-1 audit of units 59 and 60, its 19 minors: a floor sum that counts its base, criteria that can fail on the text they retire, observations on a tree that imports, and write sets that name every file

**Status:** DEFERRED · rev-4 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 35 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-61-round5-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-61-round5-fix-return.md) | research | TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 |
| [2026-10-26-build-TOOL-dBoundRoles-63-deviation-631.md](../build/2026-10-26-build-TOOL-dBoundRoles-63-deviation-631.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-63-deviation-632.md](../build/2026-10-26-build-TOOL-dBoundRoles-63-deviation-632.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-61-round5-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-61-round5-fix-brief.md) | research | TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 |
| [2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted specs 59 and 60
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md`) confirmed
two HIGH findings, promoted as `TOOL-dBoundRoles-61` (id 19) and `TOOL-dBoundRoles-62` (id 21), and 12
MEDIUM and 7 LOW. BUILD-METHOD M4 batches the minors into one unit: they do not split into two disjoint
write sets by M6 (§4 "Why one unit"). This unit takes all 19, report ids 2 to 18, 20 and 22 less ids 19
and 21, each its own scope item even where the report merged several into one item. Id 1 was refuted by
the audit.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 2, 10, 15, 22 | unit 60 S24, AC15, §4 Evidence | S1, S2, S3, S4 |
| M2 | 9 | unit 59 S1, §4 "The slice" | S5 |
| M3 | 3 | unit 60 AC4 | S6 |
| M4 | 4 | unit 60 AC14 | S7 |
| M5 | 5 | unit 60 S19, AC11 | S8 |
| M6 | 13 | unit 60 S19, AC11 | S9 |
| M7 | 16 | unit 60 §4 Files touched | S10 |
| M8 | 17 | unit 59 AC4 | S11 |
| M9 | 20 | unit 60 §4, S12, S19, S23, AC6, AC11, AC14 | S12 |
| L1 | 6 | unit 60 S1 | S13 |
| L2 | 7 | unit 59 S4 | S14 |
| L3 | 8 | unit 60 S26 | S15 |
| L4 | 11 | unit 59 AC4 | S16 |
| L5 | 12 | unit 60 §4 Evidence | S17 |
| L6 | 14 | unit 59 S4, AC4 | S18 |
| L7 | 18 | unit 59 §4 Files touched | S19 |

## 2. Scope (IN)

- **S1** — id 2. 60 AC15 and S24 state the sum per suite as the base term, the first bare number in the
  comment above `FLOOR_ASSERTIONS`, plus every `+<n>` term, equal to the floor. Observed by AC1.
- **S2** — id 10. For `tools/roles/spawn-guard.test.sh` the base term is the one unit 62 S2 writes, which
  carries every unit before 58, so unit 58's terms are never asked to equal that floor alone. Observed by
  AC1.
- **S3** — id 15. 60 §4 Evidence's last bullet reads that the base 10 plus the `+<n>` terms of
  `tools/roles/adopt-roles.test.sh:73-80` sum to `FLOOR_ASSERTIONS=50`. Observed by AC2.
- **S4** — id 22. Before the pass records 60 AC15, it runs S1's sum over the base blob of the adopter suite
  and records the reading in unit 60's ledger: the base term plus the terms print 50, equal to the floor.
  Observed by AC3.
- **S5** — id 9. 59 S1 and §4 "The slice" read the slice's exit status, and a non-zero exit fails the case
  naming the role and the slice's stderr. Unit 61's S4 makes that bump of spec 59 and its S1 builds the
  check; this pass records that, or makes what is missing. Observed by AC4.
- **S6** — id 3. 60 AC4 also requires that `grep -n 'writes no file this unit writes'` over spec 52 prints
  nothing, and that 52's §4 Rollout names `TOOL-dBoundRoles-26` as a writer of
  `tools/roles/adopt-roles.test.sh`. Where unit 60's pass left the phrase, this pass makes 60 S7's bump of
  spec 52. Observed by AC5.
- **S7** — id 4. 60 AC14's S34 half reads 54's AC1 bullet with its lines joined, and asserts it holds no
  `ten at` and no typed count of overlays. Where 54's AC1 still holds one, this pass makes 60 S34's bump of
  spec 54. Observed by AC6.
- **S8** — id 5. 60 S19 drops "This pass observes both arms". AC11 observes each of 54's and 55's arm
  criteria by a direct probe in the form unit 49 AC1 uses: govkit's self-test module imported as a library
  from S12's worktree, no suite run, the staged break written into the worktree's copy. Observed by AC7.
- **S9** — id 13. The same bump of spec 60 has S19 rewrite the §5 testing lines of specs 54 and 55: each
  arm is observed at its unit's own pass and on S12's worktree, not at the close. AC11 gains a half:
  `grep -n 'arm of §7 at the close'` over specs 54 and 55 prints nothing. Where unit 60's pass left either
  line, this pass makes that bump. Observed by AC8.
- **S10** — id 16. 60 §4 Files touched names the specs of units 45, 48 and 50 among the specs its pass may
  bump. Observed by AC9.
- **S11** — id 17. 59 AC4 takes the skeptic's corrected form. A probe extracts two bullets of spec 53: S1,
  from `**S1**` through the end of its Readers clause, and the §4 Evidence bullet citing the read set. Each
  names `parse_read_key`, and the S1 bullet holds no match of `handoff\.py:1025($|[^0-9])`. The citations
  of the `ap.error` refusal at spec 53's lines 26 and 76, and its §1 Goal text, stay. Where unit 59's pass
  left a match in 53's S1 bullet, this pass makes 59 S4's bump of spec 53. Observed by AC10.
- **S12** — id 20. 60 §4 "Where each item lands" observes on a detached worktree, not on a `git archive`
  extraction, so govkit's self-test module finds its repository at import. The commit is
  `git log -1 --format=%H -S derive_overlay_expected -- tools/govkit/selftest.py`, the one that took the
  function out, and its subject must name `TOOL-dBoundRoles-19`. `git worktree add --detach` checks out its
  parent under a short `%TEMP%` path, and `git worktree remove` takes it away after. An observation whose
  module does not import there fails, naming the import error. 60's S12, S19, S23, AC6, AC11 and AC14 read
  "the worktree of §4" for "the archived tree". Observed by AC11.
- **S13** — id 6. 60 S1 drops its exclusion-pathspec wording and keeps the literal `-F` match; S2 alone
  scopes the probe. Observed by AC12.
- **S14** — id 7. 59 S4 has unit 53's ledger answer AC1 and AC2 in the OBSERVED form, re-observed under the
  folded helper, because 59's bump leaves their text as it is (§8 F2). Where unit 59's pass wrote
  `amended rev-<n>` for either, this pass re-observes that criterion and writes the OBSERVED answer in its
  place. Observed by AC13.
- **S15** — id 8. 60 S26 gains the clause 60 S11 carries for spec 49: where unit 58's pass left 45's AC1
  bullet without `gov-builder`, this pass makes that bump. Observed by AC9.
- **S16** — id 11. 59 AC4 also requires that the Readers line of 53's S1 names no bare
  `handoff.py:1025`, the citation 59 S4 retires there. Observed by AC10.
  **Readers:** by name: `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md:45`, 53's
  Readers line, the one spelling this item clears. A git grep for the citation also prints 53's line 41
  inside the S1 bullet, which S11 clears, its ap.error citations at lines 26 and 76, which S11 keeps, and
  spec 59's lines 27, 52, 60, 82 and 164, which cite the base or state the retirement and stay. by value: NO VALUE READERS — the item moves a
  citation in a spec's prose, which no code reads; the read-set parse it pointed at stays in
  `tools/roles/handoff.py`, and 53 now cites it through `parse_read_key`.
- **S17** — id 12. 60 §4 Evidence's first bullet says the grep was read at the spec commit `13ac01368`,
  where it prints spec 46 line 139, 48 line 176, 50 line 265 and 58 lines 117 and 349 beside spec 60's own;
  its fourth cites `tools/memory-recall/selftest.py:1615` for `desc` and `:1619-1620` for the token loop.
  Observed by AC14.
- **S18** — id 14. 59 S4's §10 clause is an addition: 53's §10 names `roles_lib.parse_read_key` (unit 14
  S4) beside `load_roles` and `check_arm` as the seam the read check folds through. 59 AC4 gains a half:
  `grep -n 'parse_read_key'` over spec 53 prints a §10 line. Where unit 59's pass left 53's §10 without
  it, this pass makes that bump. Observed by AC10.
- **S19** — id 18. 59 §4 Files touched names unit 53's acceptance ledger, the answers of S4, for the
  dispatch write set. Observed by AC15.

## 3. Non-goals (OUT)

- The HIGH findings: `TOOL-dBoundRoles-61` (id 19) and `TOOL-dBoundRoles-62` (id 21).
- Rewording specs 1 to 62 beyond what an item changes; §4 "How an item closes" is the one route.
- The report's left-shift gates: the floor-grammar check, the empty-output checklist, the red-at-base
  criterion check, the line-break spec lint, the pass-run suite lint, the amendment-other-half checklist,
  the write-set hygiene check, the retired-citation checklist, the extracted-tree checklist, the
  two-answers checklist, the check 23 extension, the Evidence re-run lint, the in-place-of checklist and
  the ledger-write check. No clause of this build names them; each item's criterion is its regression.

### Edges

- **consumes-from** `TOOL-dBoundRoles-59` — S1, S4, §4 and AC4, which S5, S11, S14, S16, S18 and S19 restate (ids 7, 9, 11, 14, 17 and 18)
- **consumes-from** `TOOL-dBoundRoles-60` — S1, S19, S24, S26, §4, AC4, AC6, AC11, AC14 and AC15, which S1 to S4, S6 to S10, S12, S13, S15 and S17 restate (ids 2, 3, 4, 5, 6, 8, 10, 12, 13, 15, 16, 20 and 22)
- **consumes-from** `TOOL-dBoundRoles-61` — the exit check and its bump of spec 59, which S5 records rather than rebuilds (ids 9 and 19)
- **consumes-from** `TOOL-dBoundRoles-62` — the spawn guard's floor line and its base term, which S2's sum reads (ids 10 and 21)
- **hands-off** `TOOL-dBoundRoles-64` — S2, S4, S6, S8, S11, S12, S16, §3, §4, §5, §10, AC1, AC3, AC4, AC5, AC11 and AC14, which unit 64 restates: criteria that can fail on the text they retire, the worktree's forced cleanup, the full write set, one AC15 answer, the Readers inventory and the edges (ids 1, 2, 3, 4, 5, 6, 9, 10, 14, 15, 17, 19, 24, 25, 26, 29 and 33 of the round-1 audit of units 61 to 63)
- **hands-off** `TOOL-dBoundRoles-65` — S12 and AC11, which unit 65 restates: the porcelain list compared through `branch_reconcile`'s normalised keys under a literal `dbr63obs` root, with a positive control (id 11 of the round-1 audit of unit 64)
- **hands-off** `TOOL-dBoundRoles-66` — S8, S11, S12, S16, §4 Evidence, §5, §10 and the observation probe, which unit 66 restates or stages: the joined §10 check, the by-value Readers inventory, the hard-kill recovery and the cleanup confined to the probe's own entries (ids 1, 4, 5, 12, 22 and 23 of the round-1 audit of unit 64)
- **hands-off** `TOOL-dBoundRoles-67` — S12's commit, whose parent unit 67 takes as the observation's signature to sweep for leftovers wherever they sit (id 1 of the round-1 audit of units 65 and 66)
- **hands-off** `TOOL-dBoundRoles-68` — S12's commit shape, a `-S` commit that takes a token out, which unit 68's scratch control copies (id 14 of the round-1 audit of units 65 and 66)
- **hands-off** `TOOL-dBoundRoles-69` — S8, S12 and §5, which unit 69 restates: the printed `root:` and `worktree:` lines, the one cleanup rule, the stale-entry recovery and the `dbr63obs` spelling (ids 21, 8, 12, 19 and 9 of the round-1 audit of units 65 and 66)

## 4. Design

### Why one unit

M4 admits two units only when the minors split into two disjoint write sets by M6. They do not. The
spec-59 half (ids 7, 9, 11, 14, 17 and 18) observes `tools/roles/adopt-roles.test.sh` as an acceptance
input in S5, and the spec-60 half writes that file where S1's sum is red on the built tree, which M6
clause 2 refuses. The two halves would also land at different orders, 24 and 34, so they would never build
together.

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a landed
unit already left it. Where an item changes another unit's criterion or scope item, the pass bumps that
unit's spec FIRST with the changed text and a §9 line naming this unit (BUILD-METHOD M2, READY), and that
unit's ledger answers the criterion `amended rev-<n>`, naming the revision (58 §4 "How an item closes").
Where S1's sum is red on the built tree because a raise left no term, the pass adds the term to that
suite's comment.

### Where each item lands at order 35

Every other unit has built, units 61 and 62 included. Unit 19's pass took `derive_overlay_expected` out of
`tools/govkit/selftest.py`, so S8 and S12 observe on the worktree S12 names.

### Evidence

Read at base `462d20f3` on 2026-10-26, and at the spec commit `13ac01368` where a line says so:

- `tools/roles/adopt-roles.test.sh:73` opens `# 10, then +3 for arm 7`; the thirteen `+<n>` terms of
  `:73-80` sum to 40, and `:81` is `FLOOR_ASSERTIONS=50`.
- `tools/govkit/selftest.py:34-47` raises `SystemExit` outside a git repository, `:70` finds `GOV_ROOT` by
  a `.git` entry, and `:195-196` run `rev-parse HEAD` at import. A detached worktree's `.git` file
  satisfies all three.
- Spec 52's §4 Rollout reads that `TOOL-dBoundRoles-26` "writes no file this unit writes"; spec 26 lists
  `tools/roles/adopt-roles.test.sh` under Files touched.
- Spec 54's AC1 wraps `ten at` and `base` across a line break, so `grep -c 'ten at base'` prints 0 today.
- Specs 54 and 55 each read `the arm of §7 at the close` in their §5 testing line.
- Spec 53 cites `handoff.py:1025-1028` at lines 26 and 76, `handoff.py:1025-1026` at line 41, and
  `tools/roles/handoff.py:1025` in its Readers clause at line 45; its §10 names `check_arm` and
  `roles_lib.load_roles` only.
- At `13ac01368`, `git grep -n 'handoff.derive_section_sha' -- memory/builds/dBoundRoles/spec` prints spec
  46 line 139, 48 line 176, 50 line 265 and 58 lines 117 and 349, beside spec 60's own lines.
- `tools/memory-recall/selftest.py:1615` assigns `desc`, `:1617-1618` are comments, and `:1619-1620` are the
  token loop.

### Inventory

Minted: none.

### Migration

None: no stored data changes. S4 and S14 add ledger lines this build's passes own.

### Rollout

Live at landing, at order 35, after every unit it repairs and after units 61 and 62. No other unit holds
order 35.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh` and `tools/roles/spawn-guard.test.sh`, the floor comments, where S1's
  sum is red on the built tree
- the specs of units 45, 52, 53, 54, 55, 59 and 60, rev bumps, named here for the dispatch write set
- the acceptance ledgers of units 53, 59 and 60, the OBSERVED and AMENDED answers S4, S14 and the bumps
  write, named here for the dispatch write set

### Alternatives rejected

- **Two units.** §4 "Why one unit".
- **Keep `git archive` and `git init` inside the extraction.** A fresh repository has no history, so the
  pickaxe of S12 cannot run there, and the module's pin read sees a repository the build never made.
- **Run govkit's self-test suite on the worktree to observe AC11.** A pass runs no self-test suite (M6);
  S8 is the direct form.

## 5. Production-readiness checklist

- security — no new write path; the worktree lives under `%TEMP%` and is removed after.
- perf / scale — greps, probes, one worktree checkout.
- error / empty / loading states — S12 fails an observation whose module does not import, naming the error.
- observability — the ledger records S4's base reading and S12's worktree observations.
- risks — the bumps touch seven converged specs; each moves only the item's text.
- testing — AC1 to AC15 by grep, probe and worktree; this unit adds no arm.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe extracts spec 60's AC15 bullet, it states the sum as the base term plus
  every `+<n>` term, and the same rule run over the roles adopter suite and the spawn guard's suite
  on the built tree prints, per suite, a sum equal to its floor.
  Red when: AC15 sums the `+<n>` terms alone and is red on a correct tree.
- **AC2** — When `grep -n 'base 10'` runs over spec 60, it prints §4 Evidence's last bullet.
  Red when: the Evidence says the terms alone sum to the floor.
- **AC3** — When S1's sum runs over the roles adopter suite as `git show` prints it at base `462d20f3`, it
  prints 50, equal to the floor; with the base term dropped it prints 40.
  Red when: the probe drops the base term and still reads green.
  figure: PINNED 50 and 40, measured at base `462d20f3` on 2026-10-26.
- **AC4** — When a `python -c` probe extracts spec 59's S1 bullet and its `### The slice` subsection, each
  names the exit status, and `grep -n 'gov-nosuch' tools/roles/adopt-roles.test.sh` prints unit 61's call.
  Red when: an empty line from a crashed slice still reads as every key read.
- **AC5** — When `grep -n 'writes no file this unit writes'` runs over spec 52, it prints nothing, and
  `grep -n 'TOOL-dBoundRoles-26'` over spec 52 prints a §4 Rollout line naming
  the roles adopter suite's path.
  Red when: a Rollout keeps a disjointness claim the Files touched contradict.
- **AC6** — When a `python -c` probe joins the lines of spec 54's AC1 bullet, the joined text holds no
  `ten at` and no number of overlays.
  Red when: a typed count survives across a line break.
- **AC7** — When `grep -c 'observes both arms'` runs over spec 60, it prints 0, and a `python -c` probe
  extracting 60's AC11 finds the library import of unit 49 AC1's form and no staged `New arm:` case.
  Red when: a criterion of a pass-run unit needs a suite run.
- **AC8** — When `grep -n 'arm of §7 at the close'` runs over specs 54 and 55, it prints nothing.
  Red when: a §5 line sends the closer to an arm on a deleted check.
- **AC9** — When a `python -c` probe extracts spec 60's Files touched, it names specs 45, 48 and 50, and
  60's S26 bullet holds the clause for a bump unit 58's pass left undone.
  Red when: a pass may write a spec its declared set omits.
- **AC10** — When a `python -c` probe reads spec 53, its S1 bullet through the Readers clause names
  `parse_read_key` and matches no `handoff\.py:1025($|[^0-9])`, its `**Readers:**` line names no
  `handoff.py:1025`, its §4 Evidence read-set bullet and its §10 each name `parse_read_key`, and spec 59's
  AC4 bullet states each of those halves.
  Red when: a stale spelling of the retired citation survives in 53's S1, or 53's §10 omits the seam.
- **AC11** — When `grep -n 'git archive'` runs over spec 60, it prints nothing, its §4 names
  `git worktree add --detach` and `-S derive_overlay_expected`, and that pickaxe on the built tree prints
  one sha whose subject names `TOOL-dBoundRoles-19`.
  Red when: the observation tree cannot import govkit's self-test module.
- **AC12** — When `grep -n 'exclusion pathspec'` runs over spec 60, it prints nothing.
  Red when: S1 and S2 give two command shapes for one probe.
- **AC13** — When a `python -c` probe extracts spec 59's S4, it names no `amended rev-` for 53's AC1 or
  AC2, and unit 53's `**Evidences:**` block answers AC1 and AC2 each with a backticked token.
  Red when: the ledger records as amended a criterion whose text never changed.
- **AC14** — When `grep -n '13ac01368'` runs over spec 60, it prints §4 Evidence's first bullet, and
  `grep -n 'selftest.py:1615-1618'` over spec 60 prints nothing.
  Red when: an Evidence line cites a base or a range the source does not bear out.
- **AC15** — When `grep -n 'acceptance ledger'` runs over spec 59, it prints a §4 Files touched line naming
  unit 53.
  Red when: a pass writes a ledger its declared set omits.

## 7. Gates

`roles adopter self-test` · `agent-cap self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`agent-cap self-test` stands for the spawn guard's suite; unit 25's pass renames it on every live §7
line when it renames the leg. This unit adds no arm: each criterion is a grep or a probe.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause; veto 1 discards (b).
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — 53's AC1 and AC2: OBSERVED answers, or a bump that restates their text (id 7)?** Options: (a) keep
  them OBSERVED, re-observed under the folded helper; (b) restate their text and name them in 53's §9 line,
  so `amended rev-<n>` is true. (b) rewrites two criteria no defect touches, for the record's sake.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, fewest follow-ups. widens: none · relaxes: none
- **F3 — The observation tree: a detached worktree, or `git init` in the extraction (id 20)?** Options: (a)
  `git worktree add --detach` at the parent of the pickaxe's commit; (b) `git archive` plus `git init` and
  one commit. (b) leaves no history for the pickaxe and a repository the module's pin read never saw.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the 12 MEDIUM and 7 LOW findings of the round-1 audit of units 59
  and 60, each id its own item, in one unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-65 and TOOL-dBoundRoles-66, the HIGH promotion and the minors batch of the round-1 audit of unit 64; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-67, TOOL-dBoundRoles-68 and TOOL-dBoundRoles-69, the two HIGH promotions and the minors batch of the round-1 audit of units 65 and 66; nothing else moved.

## 10. Reuse audit

The seams are the units' own: 59's and 60's "How an item closes" route, 58's AMENDED rule, unit 62's floor
line, unit 49 AC1's library import of govkit's self-test module, and git's own worktree and pickaxe, each
extended rather than copied.
`python tools/codebase-map/reuse_lookup.py "observe a deleted function on the tree at the parent of the commit that removed it"`
ranked `tree`, `build_commit`, `load_map_tree` and `resolve_session_tree`, none an observation tree, so no
existing seam fits beyond those named. The recall query's hits are acceptance-ledger records and hygiene
check 23's ledger reader, which the OBSERVED and AMENDED answers already feed.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion observed on the tree before a later unit deleted the code" --terms "worktree detached parent commit pickaxe deleted function archived tree observation criterion amended ledger"`
