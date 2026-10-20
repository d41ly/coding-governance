# Research: aScoutedSeam's principles applied to gov's flow and roles

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 129's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-10-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

**Point 2: applying aScoutedSeam's measured principles to gov's target flow and roles**

**Abbreviations.** `AS/` means `memory/builds/aScoutedSeam/build/` on `origin/main` (`a60b0c7dc`), read with `git show`. `DL/` means `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`. aScoutedSeam's records carry no `[tags]`, so I cite them by § or heading.

I wrote nothing in the tree. My probes ran on a copy under `/tmp/tmp.oOWt1okS0R`, which is now deleted.

## 1. Inventory of every agent call

I derived the population from the step tables, not from the dated matrix. A read-only parse of `DL/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md` found **88 item rows and 22 role items**. `DL/…-layer-roles.md [matrix]` still says 20, because it predates `probe.design` and `probe.experiment`.

Effort comes from `DL/…-systems.md [design-role-shapes]`, lines 450–458 (with RS-2). Where today's code differs, I give it after the slash.

| # | Step · item (flow-steps line) | Role | Input | Output | Read by | Effort, design / code |
|---|---|---|---|---|---|---|
| 1 | entry · `entry.orient` (:77) | orientation scout | tree, leases, card refs, kickoff manifest | the composed card: scope, reading, risks, bug classes | `entry.place`; every work order's card slice | medium / xhigh (`tools/roles/house/policy.toml:9`) |
| 2 | entry · `entry.place` (:78) | orientation scout | request, plan view, design index, open asks | a disposition from a closed set, with reason and evidence; the observations the request claims | `placement.check` (a command), then `entry.claim`, Plan or `probe.trigger` | medium |
| 3 | plan · `plan.triage-judge` (:128) | planner | an intake no rule decides | select, defer, retire or refuse | `plan.triage-rule`'s routes | high |
| 4 | plan · `plan.record` (:129) | planner | intake, triage, duplicates, owner answers | plan record (goal, cut-line, acceptance as observations, parents, reach); research requests; owner questions | owner ratification, then `design.seams` and `design.decompose` | high |
| 5 | `plan.research` (:130), `design.research` (:181) | researcher | the asker's question | research record | the asking item | medium, single |
| 6 | `plan.reason`, `design.reason`, `test.reason` (:134, :185, :293) | planner, architect, tester | the command's score | whether to review, and why | breakpoint routing | the role's effort |
| 7 | design · `design.inventory` (:178) | architect | plan revision; built units | one verdict per built unit | `design.decompose` | high |
| 8 | design · `design.seams` (:179) | reuse scout | plan scope paths, open asks, map/recall, house index (handed) | seams with probe digests | `design.decompose`; the spec writer's work order; the card's `**Reuse:**` | medium |
| 9 | design · `design.decompose` (:180) | architect | plan record, seams, inventory | features, units with order and write sets, interfaces, forks | `design.overlaps`, `design.unit-spec` | high |
| 10 | design · `design.unit-spec` (:183) | spec writer, one per unit | unit row, interfaces, seams, overlaps | spec at its SHA; forks; overlap acknowledgements | `design.ready`, spec audit, builder, closing review | high |
| 11 | breakpoint · `review.lens`, spec or design-audit preset (:472) | reviewer ×5 | pinned specs, lens brief, checklist share, byDesign, prior findings | findings | `review.refute` | medium |
| 12 | breakpoint · `review.lens`, diff preset (closing, gate and landing reviews) | reviewer ×5 | the range, `specs`/`context`, checklist share | findings | `review.refute` | high |
| 13 | `review.refute` (:473) | skeptic, at most 5 batches | findings | one verdict per finding | `review.report` | high on diff, medium on spec (`policy.toml:14,18`) |
| 14 | `review.report` (:474) | synthesizer | verdicts | report, one disposition per confirmed finding | `review.dispose` (a command) | high / medium |
| 15 | `review.fold` (:476) | spec writer | confirmed findings on unbuilt specs | folded specs; class records | next round, or `design.ready` | high |
| 16 | build · `build.unit-pass` (:229) | builder, one per unit | spec at its SHA, write set, acceptance commands, bug classes (`DL/…-flow-roles.md [steps]` Build) | `committed` or `diverged` | `build.acceptance` (executor), `build.scope`, closing review | high / xhigh (`policy.toml:12`) |
| 17 | test · `test.attribute` (:289) | tester | own and mixed reds, labels, diff, specs | one judgment per red | routes to Build or Design | medium |
| 18 | probe · `probe.design` (:522) | tester | claim and subject at a pinned SHA, cold | commands | `probe.run` | medium |
| 19 | probe · `probe.experiment` (:523) | researcher | the pinned question | corpus, variants, judge | `probe.run`, then `probe.judge` | medium |
| 20 | the experiment's blind judge (flow-steps:536) | not named (aScoutedSeam used `gov-skeptic`) | one case, every arm under rotated labels | grades per arm | the scorer | not declared |
| 21 | adopt · `adopt.decisions` (:596) | reviewer, as two raters | candidates from `adopt.census` | a route per candidate | reconstructed decision records | not declared |
| 22 | the cycle (`[cycle]` 2–3) | prompt writer | the item's resolved work order | the task prompt | the executor, which wraps and spawns it | medium |
| 23 | expansions | deployer, maintainer, the Loop Review lens | landed units; readings; metrics | notes, filings, proposals | Plan's triage | medium |

**Missing from the flow:** aScoutedSeam's stage 2, the diff-time reuse check. No item in `[build]` runs it.

## 2. Classification

| Kind | Calls | Principles | Status |
|---|---|---|---|
| **Coverage** | 7, 8, 11, 12, 13, 14, 15, 17, 21; the claimed observations of 2; the bug classes of 1 | P1–P6 and P11 | **MEASURED only for 8** (it is M1c: P8 sketch, census, MUST cap; `AS/…-1-7` and `AS/…-1-9`) **and for the missing diff check** (P1–P7, P9). Every other row is TRANSFER. |
| **Creation** | 4, 9, 10, 16, 18, 19, 22; the research call 5; the card of 1 | P8 builds the population; P7 applies to the inputs | TRANSFER |
| **Single-item judgement** | the disposition of 2, 3, 6, 20 | P3's closed verdicts, P13 | TRANSFER |

Two notes on this:
- **The design already has P3 rows in places.** Calls 7, 13, 14, 15 and 17 already have "every X has one verdict" computed-join witnesses (flow-steps :178, :473–:476, :289). What the design lacks is P2/P4/P5 on `review.lens`.
- **P13's fenced block is superseded** by the design's schema-forced return (`[cycle]` 5). The part that survives is "count unparsed replies before reading a score", and it belongs to the scorer factory.

## 3. Listers for the coverage calls

| Call | Deterministic lister | Where | Probe |
|---|---|---|---|
| Missing diff check; reuse half of 12 | `extract_units` / `render_units` | `AS/…-1-10-d1v2.py:44,85`. Not built in gov: `map_diff.py` has no `--added-units` (`tools/codebase-map/map_diff.py:1-6`); it is specced as TOOL-aScoutedSeam-3 S8 | on `73b80ed31`: **36 units** |
| 11 and 12, bug classes | `gotchas.py --for-diff` / `--for-paths` | `tools/memory-tree/gotchas.py:7-8` | same range: "43 class(es) selected by an anchor + 6 universal" |
| 12, gate review, legs a path set trips | `check-spec-tokens.py --legs-for -` | `tools/check-spec-tokens.py:550` | 201 path-to-leg lines; "70 of 140 legs carry no guard" |
| 11, 12 and 16: ACs, write set | `AC_LABEL`, `extract_acceptance`, `extract_files_touched` | `tools/check-spec-tokens.py:269,428,443` | AC labels in 1312 of 1322 specs |
| 11, 12 and 16: S-items | **None in gov.** Searched `tools/**/*.py` for `**S`, `S\d`, `scope item`. `review_replay.py:68` only matches addresses. The nearest is `SPEC_ITEM` in `AS/…-1-13-system.py:142` (diff lines only) | — | `- **S<n>**` lines in 1093 of 1322 specs, so a regex lister is viable |
| 13, 14, 15 | the findings list, and the report's dispositions | inside the harness | already joined |
| 17 | `test.route`'s reds (a command, in the design) | design only | — |
| 7 | built units | `gen_build_index.py` (`--build`, `--json`) | — |
| 21 | `adopt.census` | design only | — |
| 2, claimed observations | **None.** The agent enumerates them (P8) | — | — |
| 8 | **Half.** The house index is a lister of seams, not of needs. The plan record's scope and acceptance could list the needs; `AS/…-1-11` "Where else it applies" calls that untested | — | — |

## 4. Edges (the priority)

"Carried today" means in v2's typed returns and work orders.

| Edge | What N commits to | Rows N+1 must answer | Carried today? | Status |
|---|---|---|---|---|
| **E1** `design.seams` → missing diff check → closing review | MUST seams | per MUST: `used`, `bypassed` or `not-applicable`; a bypassed MUST is also a duplicate, becoming a fold or fix unit | **No.** There is no item. The diff preset has no reuse lens (`tools/workflows/tier2-review.template.js:705-731`), and v2 keeps it that way (`DL/…-review-system.md [lenses]`, :134). `gov-diff-reviewer` reads only `input:diff, input:spec?` (`tools/roles/agents/gov-diff-reviewer.agent.md:7`) | **MEASURED**, 13 → 20 of 23 |
| E2 `design.seams` → `design.decompose` | MUST/SHOULD seams, constraints, census lines | per seam: assigned to unit X, or rejected with a reason | **No.** Seams arrive as P29 `claimed` content with no duty to dispose each one; decompose's witness is a roster schema (flow-steps:180) | TRANSFER |
| E3 `design.decompose` → `design.unit-spec` | assigned seams, interfaces, overlaps | §10: one row per assigned seam (extended, or rejected with a reason); interfaces honoured; overlaps acknowledged | **Partial.** Overlaps are acknowledged (:183). §10 holds one seam or "no existing seam fits" (`memory/TEMPLATE-SPEC.md:290-300`), and check 12 cannot see whether it is true (gap-design-05) | TRANSFER |
| E4 `plan.record` → `design.decompose` | acceptance observations, cut-line | per observation: covered by unit(s), out of scope, or deferred | **No** join exists | TRANSFER |
| E5 `design.unit-spec` → `build.unit-pass` | S-items, ACs, MUST seams, bug classes | ACs are re-run by the executor (witnessed, which beats rows). Per S-item: done, deferred or n/a. Per MUST: used, bypassed or n/a | **Partial.** ACs are witnessed. The builder's work order holds no seams (`[steps]` Build), the reuse line is per unit, not per seam (:229), and the builder reads `input:spec, card:route?` only (`tools/roles/agents/gov-builder.agent.md:7`). Builder rows are claimed by the author, so they need E1 or E6 to verify them | TRANSFER |
| **E6** build → closing review | S-items, ACs, MUSTs, the diff's own units | met, missed or bypassed per item, plus one row per unit (P2) | **No.** Specs reach the panel as `specs`/`context` prose. The finder schema holds `findings` only (`tier2-review.template.js:561-584`), and the prompt says "If nothing real, return findings: []" (:1136-1140) | MUST half MEASURED (it is E1); S-item and AC half TRANSFER |
| E7 checklist → `review.lens` | bug classes | per class: hit, clear or n/a | **No.** The prompt says "A class with no hit needs no finding" (`tier2-review.template.js:860`), which is the P3/P4 silent drop | TRANSFER |
| E8–E10 lens → refute → report → fold | findings, then verdicts, then dispositions | one row each | **Yes:** computed joins (flow-steps :473–:476) | TRANSFER-shaped, already designed |
| E11 `test.route` → `test.attribute` | reds | one judgment each | **Yes** (:289) | already designed |
| E12 `design.inventory` → decompose | per-unit verdicts | — | **Yes** (:178) | already designed |
| E13 research or probe → asking item | candidates and picks; the probe verdict | the asker's return cites each one as adopted or rejected | **Partial.** It returns as input (`[rules]`); the fork record holds a decision but no row per candidate | TRANSFER, low |
| E14 work order → prompt writer → actor | every field | none | The executor wraps the prompt in the work order (`[cycle]` 4), so P7 does not apply here | n/a |

P29 (`DL/…-layer-roles.md [trust]` items 4, 7, 9) hands claimed facts as keyed content. It only requires a disposition when a fact proves false (repair), and returns carry provenance keys rather than dispositions. Edge rows are the missing piece: **every handed commitment gets a disposition, not only false ones.**

## 5. The shape mapping, and what in v2 is stale

### 5a. The figures, re-derived

I copied AS's instruments and ran them on the temp copy:
- `system …-1-3-cases.json …-1-5-results.json m1cA@medium d1v2@medium t1r@medium t2r@medium` printed `m1cA 15/23 · d1v2 13/23 · t1r 20/23 · t2r 20/23` and `system m1cA + t1r: 21/23`.
- On the held-out set it printed `m1c 8/12 · t1r 11/12 · system m1c + t1r: 12/12`.
- `bench.py judged … d1 d1@medium d1v2@medium d1v2@low` printed primaries 11, 7, 14 and 8 of 23.

So the owner's 94% is 33 of 35, the union of two arms, one run each with one judge per case.

**One finding the records do not state.** The same run printed `system m1cA@medium + d1v2@medium: 21/23`, identical to the system with the card. The 7 cases the card added to T1 were all cases the orientation had already covered:
- nc-medint-v1 and nc-medint-restage;
- nc-acct-plancards and nc-api-carousel;
- gov-reaped-census, gov-ruled-markerindex and gov-declared-gitcommondir.

So the card added no union recall on the tuning set. What P7 measurably did was move the orientation's advisory catch into the step that gates. That matters in gov's flow, where seams are advice until a gate reads them. But it means `AS/…-3-1` "What this decides" item 1 ("not just a union") is not what the union figure shows. The held-out set has no no-card arm, so the card was never isolated there.

**Other places where AS's records disagree with each other or with the code:**
- `AS/…-3-3 §1` row 6 ("0 of 6") sits under the heading "blind judge unless marked", but `AS/…-1-9` Confounds says it was graded by the path matcher only, with no blind judge.
- `AS/…-3-3 §4` says the orient → spec edge was measured. I found no arm in `-1-7`, `-1-10`, `-1-12` or `-3-1` that hands the card to a spec writer. The measured edge is orientation → diff check.
- AS spec TOOL-aScoutedSeam-3 rev-5 S2 says "T1 ran against empty cards, so this half is unmeasured". `-3-1`'s t1r arm measured it afterwards.

### 5b. The best-performing shape

The best measured shape is a two-stage pipeline of one role, the reuse scout:
- stage 1 is a `single` at medium;
- stage 2 runs at medium too, driven by a deterministic lister, and answers stage 1's MUSTs as rows;
- it has no skeptic, no judge and no twin in production;
- an optional T2 variant is unioned in, but it measured a tie.

How it maps onto the registry's kinds (`[design-role-shapes]`):

| Part of the measured shape | Registry kind | Where it stands |
|---|---|---|
| stage 1 | `single` | `design.seams`, already in v2 |
| stage 2 | `per-unit` (AS F1 resolved it per unit, but that was a ruling, not a measurement) | needs a new Build item before the closing review |
| the edge rows | none | needs an `upstream` declaration on the item: which item's commitments it must answer |
| T2 union | not `twin` (a twin is two runs of one shape) | no kind; leave it out |
| the method | `experiment` | registered |
| `panel` | was not measured on T1 rows | — |

**Where stage 2 could live: four mechanisms, each with its losing test.**

| Mechanism | Losing test | Result |
|---|---|---|
| **A.** A Build role item: reuse scout, `per-unit`, medium, the T1 prompt plus the lister plus wiring rows | The built item must reproduce the measured figures through gov's route | Not runnable before the build; this is the acceptance it owes. **Survives.** |
| B. A reuse lens swapped into the closing review's diff preset (`panel`) | Can the panel carry T1's row contract over a listed population? | **Loses** as the panel stands: the finding schema holds no rows (`tier2-review.template.js:561-584`), the open "return findings: []" frame (:1136-1140), a swap drops a default lens, it runs once per build (against F1's per unit), and a skeptic over T1 is unmeasured |
| C. Builder self-report rows only | — | **Loses** to the design's own rule: "a verifier stage whose role wrote the artifact it verifies is refused" (systems.md:431) |
| D. Status quo: design-time scout plus the spec audit's reuse lens | — | **Loses** on the figures: orientation alone is 23 of 35 against 33 of 35 for the system. The spec audit is also "opt-in by default" (flow-steps:203) |

### 5c. What in v2 is stale against the new results

1. **v2 `[owed]`** (v2:1578–1583) cites "13 to 16 of 24" and "one checklist scout matched a two-scout workflow". Both are true, but the best shape is now the two-stage pipeline with an edge contract.
2. **`DL/…-layer-roles.md [owner-notes]`** (:647) and `DL/…-research-role-shapes-b.md:164` read the diff-time recall falling from 7 to 4 as an effort need. `AS/…-1-10` and `-1-12` show the loss was the prompt's composition: T1 at medium scored 14 against D1 at extra's 11.
3. **"Unmerged" and "no chain build counts on it"** (layer-roles:670; v2:1475 "by blob from the unmerged commit `b0fe68f30`"; flow-steps:531) is stale: `git merge-base --is-ancestor b0fe68f30 origin/main` holds. dClosedLoop's view stopped at `b0fe68f30` (2026-10-13), so M1d, T1, the low arm, the held-out set, the system and P1–P13 are all newer than the design.
4. **The flow has no diff-time reuse check** (`[build]`; review-system :134).
5. **The `experiment` shape** (flow-steps:531–538) lacks the method of `AS/…-3-3 §5`: a held-out set frozen before tuning, one variable per arm, counting parsed replies before scoring, labels rotated per case, and reading the union.
6. **dLinkedLibrary's acceptance** (v2:1482) re-runs "the benchmark" but does not name the held-out set (`-1-13-held-out-cases.json`).
7. **The reuse scout's return** is unspecified in v2 (flow-steps:179: "seams … probe digests"). It lacks M1c's contract (`AS/…-1-13-system.py:44-48,81-84`): at most 12 seams, at most 5 MUSTs, MUST defined as a defect, census lines, an `edits` bucket and `unmet`. Today's role returns "the seam", singular (`tools/roles/agents/gov-reuse-scout.agent.md:10`), which is the P1 failure.

## 6. Ranked changes, and the measurement plan

| Rank | Change | Principles | Status |
|---|---|---|---|
| 1 | A Build diff-check item (mechanism A). Duplicate rows and bypassed MUSTs become a fix pass before the closing review. Effort medium, never low | P1–P7, P9, P11 | MEASURED (reuse); owes a reproduction |
| 2 | S-item and AC rows into the closing review's intent lens (E6) | P2, P3, P4, P7 | TRANSFER |
| 3 | Seam rows through decompose and §10 (E2, E3) | P7, P3 | TRANSFER |
| 4 | The experiment shape gains AS's §5 method | method | measured as instrument validity |
| 5 | The reuse scout's return gets the M1c contract, with caps | P6, P11 | MEASURED precision (`-1-9`: MUSTs fell from 80 to 56 at equal recall) |
| 6 | Checklist classes as rows (E7) | P3, P4; P10 is a risk | TRANSFER |
| 7 | Plan observations → decompose rows (E4) | P7 | TRANSFER |
| 8 | Needs listed from the plan record into `design.seams` | P2 in place of P8 | TRANSFER; `-1-11` calls it untested |
| 9 | The skeleton (`AS/…-3-3 §3`) as the prompt writer's frame | all | TRANSFER, with P10's caution |

**Measurement plan for rank 1.**
- **Cases:** AS's 23 tuning plus 12 held-out cases, re-run through gov's built item with seams from `design.seams`.
- **Arms:** one variable only, whether the card arrives as rows or not at all.
- **Judge:** blind, labels rotated, rubric `AS/…-1-10-judge-task.md`.
- **Bars:** T1 with the card at least 29 of 35, and the system at least 31 of 35 (the measured figures minus the stated noise of 2). Parsed replies are counted first.
- **What is new to test:** gov's card comes from a plan record, not the raw request.

**Measurement plan for rank 2.**
- **Cases:** 20–30 past gov builds where an S-item or AC went unmet past its closing review. Objective evidence is a later fix commit naming the unit, a confirmed intent finding in a later round, or a recorded ask. Ground truth is checked at the reviewed head, and the specs are taken as they were.
- **Held-out:** 10 or more cases from builds after a cut date, committed before any arm runs, and never read to change a prompt.
- **Arms:** A is today's intent lens alone. B is the same plus lister rows (S-items by regex, ACs by `extract_acceptance`) with `met | missed | not-applicable` and a no-stop line. The effort stays fixed at high, and only the intent finder runs, which isolates the variable.
- **Judge:** one blind judge per case, labels rotated. Read primary coverage first, then false "missed" rows.
- **Budget:** about 60 finder agents plus about 30 judges, at most 5 at once.

**A cheap test for rank 3:** AS's corpus already has ground-truth seams. Hand the M1c card to a spec writer as prose (today's P29 content) or as rows (one variable), and judge whether the spec binds the primary seam.

## 7. Adopt now, and what waits on measurement

**Adopt now** (measured on the reuse task itself, or pure method):
- rank 1 as a designed item, with its reproduction as its acceptance;
- rank 5;
- rank 4;
- an `upstream` row declaration on items, with the reuse edge as its first instance;
- a rule that no coverage item drops below medium without an experiment record (P9);
- correcting the seven stale lines in 5c.

**Waits on measurement:** ranks 2, 3, 6, 7, 8 and 9; a T2 second pass; per-unit versus per-build placement; any effort below medium.

**Caveat on the size of the gain:** the card's +7 is a gain in enforcement, not in discovery (5a). Rollout should therefore target edges that feed a gate.
