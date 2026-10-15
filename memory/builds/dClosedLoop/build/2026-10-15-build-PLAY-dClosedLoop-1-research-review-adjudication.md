# Research: the review system, whether the skeptic's and the synthesizer's instructions need changing

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 38's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-17-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md`.

---

# Do the skeptic and synthesizer instructions need changing? Measured over 50 Tier-2 review reports

**Answer:** yes, but the changes belong in the harness, `tools/workflows/tier2-review.js` (its code and its prompts), not in the two role files. Every measured gap comes from the harness: how it orders findings into skeptic batches, the synthesizer's "merge findings of one binding grade only" rule, and what the synthesizer is handed. The skeptic's role file already hands its cases, default and rubric to the harness. The synthesizer's role file already says "One item per defect", and the harness overrides it every time. Nothing measured traces to role text, so editing the roles would add a second copy of rules the harness already owns.

I wrote nothing in the repository and ran no gate, Workflow or review. The corpus is the 50 reports that carried the appendix when I parsed them: 1,122 findings, 13 spec-audit and 37 diff reports. A 51st report, `dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-instruction-a.md`, was written by another session at 22:40, during this run. It is excluded. Re-running `parse.py` picks it up.

Several measures rely on a proxy: two findings at the same file and line ±3, or the same section, are treated as twins. Every number that relies on it says so, and where I hand-checked it I say how.

## 1. [skeptic] The measures (all 50 reports unless stated)

- **Refutation cases.** 150 refutations across 45 reports. After the classifier, with the 34 it could not place hand-assigned:

  | case | spec | diff |
  |---|---|---|
  | by design | 11 | 31 |
  | pre-existing (diff kind's scope rule) | – | 24 |
  | false premise, or no path reaches it | 2 | 14 |
  | the cited section already says it | 7 | – |
  | no graded defect | 6 | 6 |
  | duplicate | 4 | 11 |
  | could not establish (all graded medium or low) | 4 | 7 |
  | hand-assigned | 10 | 13 |

  Reading the 11 "could not establish" rows, only 3 are the true default: aSightedSkeptic #20, aSparedSpawn #2 and aGraftedHelix-24 #16.
  - The six named cases exist only in the spec-kind prompt (`tier2-review.js:1324-1327`). The diff kind gets one untyped clause, "not reachable / not a bug / by-design / duplicate" (`:1330`), plus the scope rule (`:1090`).
  - In practice "by design" means "the spec says so". Of 42 by-design refutations, 40 cite a spec, design or owner source. Only 4 cite the BY DESIGN block, and 39 already quote a line.
- **By-design refutations beside a confirmed finding on the same defect.** 9 are verified:
  - 6 that synthesizers flagged themselves: aGraftedHelix-1 closing #8 and #24 against #14; aSightedSkeptic #10 against #5 and #21, and #7 against #11; aPairedSlots #18 against #8 and #29, and #21 against #7.
  - 3 from the comparison record's defect map: A59 against A38, B61 against B43, and B47 against A39 in the other run.
  - Every one sits in a different skeptic batch from its confirmed twin.
  - The address proxy adds 5 unverified candidates.
  - Later rounds: the proxy finds 0 cases where a later round's finding at the same address was confirmed. That 0 means the instrument cannot join defects across rounds, not that none exist.
- **Duplicates.** 15 in 13 reports (4 spec, 11 diff), and every one cites a target in its own batch.
  - Pooled precision is 0.866 as reported and would be 0.880 if duplicates counted as merged confirmations. Per report the change is +0.03 to +0.07; for example dRemeasuredRender goes from 0.85 to 0.92.
  - In 4 of the 15, the refuted duplicate carried a higher finder grade than its target's binding grade, for example dClosedLoop B38 high against B33 medium.
  - One diff-kind duplicate points at a refuted target (aWardedAudit #10 → #7). The orphan demotion is spec-only (`:1407`). The case was harmless here, since both were refuted.
- **Severity regrades.** 972 confirmed findings, all graded by a skeptic.
  - 140 were graded down, 9 up and 823 left alone, a 15.3% regrade rate.
  - The main moves are high to medium (83) and medium to low (52).
  - Of the 226 findings the finder graded high or blocker, 84 (37%) were bound below high: 42% on the spec kind, 34% on the diff kind.
  - The rate is fairly even across lenses, between 11% (correctness) and 24% (grounding). The per-lens table is in `I4-skeptic.out`.
- **Unsound fixes.** 151 of 972 (15.5%: 12.8% spec, 17.1% diff), in 42 of 50 reports.
  - Wherever RUN INTEGRITY prints the count, it matches the appendix.
  - The report body carries the skeptic's correction in all but 2 or so; "still to be designed" appears 5 times, 3 of them prose about the feature itself.
  - dClosedLoop shows 1 in run A and 3 in run B, as the record says.
- **Uncertain and unverified.** 0 of 1,122 each. The uncertain branch has never fired since it shipped on 2026-10-01.
- **Verdicts that disagree across batches.**
  - The structural cause: ids are assigned lens by lens, and batches are contiguous slices (`chunk`, `:24` and `:1284`). Two lenses finding one defect therefore almost never meet one skeptic. Only 8% of cross-lens pairs at the same address share a batch today.
  - With the proxy, 38 cross-batch pairs have opposite verdicts (duplicates excluded).
  - Of 168 cross-batch confirmed pairs the finders graded alike, the skeptics bound 31 (18%) at different grades. The same-batch figure is 0 of 5 pairs, too few to compare.
  - The raw proxy rates go the other way: 27% of same-batch pairs disagree against 13% of cross-batch pairs. Only 37 pairs are same-batch, mostly neighbouring findings from one lens, so that comparison is confounded.

## 2. [synthesis] The measures

- **Defects split across items.**
  - The rule binds completely. Over the 40 reports whose item headings map at least 90% of confirmed ids, 0 of 110 same-address pairs with different binding grades were merged, against 76% (139 of 183) of same-grade pairs.
  - In 15 reports, synthesizers wrote 29 statements naming a split themselves, for example aRoutedQuill r1:45, "the same defect ... so they appear twice", and aWindowedPass r2:141, "it cannot merge with them. I would grade all four alike".
  - From the dClosedLoop defect map: run A split 5 defects and run B split 4. The difference from the record's "three defects across seven items" is in the disagreements section below.
- **Conflict items.** None. Every printed "contradictory verdicts" counter reads 0. The four headings containing "conflict" are about content, not verdicts. Synthesizers wrote 5 notes on a refuted twin, in 3 reports.
- **Item naming.** 0 of 50 reports name items by tag. 39 use positions (H1, M3, B1), and 11 use "id N" headings or tables. Round-2 reports refer to round-1 items by round and position ("round 1's B1"), which worked in all 5.
- **Proposed gates.** 721 proposals in 48 reports:

  | the proposal names | count | share |
  |---|---|---|
  | an existing leg, or a `*.test.sh` suite the `run-selftests.sh` leg runs | 121 | 17% |
  | a bug class | 18 | 2% |
  | a generic checklist entry | 174 | 24% |
  | no home at all ("an arm", "a lint") | 407 | 56% |
  | another item ("as M2") | 1 | <1% |

  The synthesis prompt asks only for "a left-shift gate suggestion" (`:1680`) and hands over no leg manifest or class list. Yet 539 findings carry a class label in the appendix's `classes` column.
- **Re-found defects.** 5 round-2 reports carry an appendix, and 2 of them re-found something round 1's fold should have closed:
  - aRoutedQuill r2 found B1 still open, and the fold commit's "now exits 0" false. The fix had been judged sound, but it waived three named commits rather than the class.
  - aWindowedPass r2 #24 found the same class round 1 raised against spec 2, left on spec 4. Its #15 found that a fold branch the fold claimed was observed red never was.

## 3. [candidates] Each change, its losing test and the result

1. **A by-design refutation quotes the line it relies on — rejected.**
   - Losing test: an uneven by-design refutation that already quotes the line.
   - Result: lost. B61 quotes block line 1 verbatim and was still refuted, while its twin B43 in the same run was confirmed. 39 of 42 by-design refutations already quote something.
   - The disagreement is over whether the line covers the case, not whether it exists.
2. **A duplicate counts as a merged confirmation — keep, as a metric fix, not an instruction.**
   - Losing test: does it change any verdict, item or disposal?
   - Result: none in 50 reports. It corrects precision by +0.013 pooled.
   - It needs the orphan check extended to the diff kind.
3. **Batches formed by cited section** — two mechanisms, one rejected:
   - **(a) One group per section or file — rejected.** It brings 7 of 8 verified twins together. Losing test: does the largest batch grow? It does, in 41 of 50 reports: median 1.83x and up to 3.83x (dUnstuckLanding-1-2, 28 against 9).
   - **(b) Sort by address, then slice contiguously — recommended.** Batch sizes are unchanged by construction. It raises cross-lens same-address pairs sharing a skeptic from 8% to 59%, and verified twins together from 0 of 8 to 4 of 8.
   - The test (b)'s build must run: replay the verify stage on the dClosedLoop runtime findings. It loses if uneven twins (today 3) or grade splits (today 3 high defects per run) do not drop.
   - Cost: 24 `verify:ids-a-b` references in `tier2-review.test.sh` assume lens-ordered ids.
4. **The synthesizer is shown refuted findings — already half built.**
   - The appendix, with every refuted row's verdict and reason, is in its prompt (`:1820-1826`), and the 5 twin notes prove it gets used. Missing are the claims of refuted rows, the twin pairs, and any instruction to look.
   - The test its build must run: replay synthesis on runtime-a and runtime-b with refuted claims and an instruction. It loses if A59/A38 and B61/B43 go unflagged; today both reports missed them.
   - Its reach is limited: the synthesizer can only note a twin, never overturn a verdict.
5. **One item per defect, with the highest grade binding** — two mechanisms, one rejected:
   - **(a) The item's grade applies to every id in it — rejected.** It raises raw highs (dClosedLoop: +4 in run A, +6 in run B) and fires the "placed at a grade other than binding" warning (`:1907-1909`). That reverses the decided aSightedSkeptic-6 §8 F2.
   - **(b) Items carry a grade per id, and the item ranks by its highest — recommended.** The counts stay raw by binding grade, and downstream readers see only the `blockers`/`highs` integers.
   - The test its build must run: the tally arms with a mixed-grade item. It loses if any reader needs `items[].ids` to stay integers. The only ones found are the test stubs, `tier2-review.test.sh:300` and `:1673`.
6. **Items named by tags, not positions — undetermined.** No measured loss comes from positions. The gain is a join key across rounds, which nothing provides today (my later-round measure found 0).
   - Losing test: do two independent runs coin the same tags for shared defects? Their headings for one defect differ, as the record's map shows, so coined tags likely lose.
   - A derived key (address, or a `ref` carried in `priorFindings`) would not depend on wording.
7. **Each proposed gate names an existing leg or bug class — weak evidence, cheap.** Only 19% name either, and the synthesizer is not given the inputs to do better.
   - Losing test: does naming prevent re-finds? Of the 2 re-finds, aRoutedQuill's round 1 did name a leg and still recurred, because its fold fixed the instance rather than the class.
   - Ship it only together with the next, data-suggested change.
8. **The fix verdict asks whether the fix covers the class, not just the instance — data-suggested.** Evidence: aRoutedQuill #23's fix was judged sound and re-found in round 2, and aWindowedPass #24 repeated round 1's class on another spec.
   - The test its build must run: re-judge aRoutedQuill #23's fix with the class wording. It loses if the verdict stays sound.

**The three candidates you named:**
- **Leave the instructions as they are — loses** on the 0-of-110 cross-grade merges, the 29 split statements, and the 9 uneven twins all sitting across batches.
- **Change the harness prompts only — too narrow.** Changes 2, 3b and 5b are harness code, not prompt text. The surviving form is the harness's code and prompts together.
- **Change the role files and the harness together — loses.** No measured gap traces to role text, and `gov-skeptic.md:30-31` hands these rules to the harness.

## 4. [where] Where each change belongs

| change | where it lands | chain build |
|---|---|---|
| 2, duplicate as merged confirmation | harness tally (`:1443-1453`), lens yield, orphan check (`:1407`) | dCalibratedLens |
| 3b, address-ordered batches | harness (`:1175-1178`, `:1284`), test fixtures | dCalibratedLens |
| 4, refuted twins to the synthesizer | harness synthesis prompt and appendix or ledger | dCalibratedLens |
| 5b, a grade per id | harness items schema (`:1841-1849`) and prompt (`:1677-1679`, `:1807-1815`) | dCalibratedLens |
| 7, gates name a leg or class | caller's args (leg manifest, class names) and harness prompt | dCalibratedLens; dBoundRoles if its typed return gains a leg/class/new field |
| 8, class-level fix verdict | harness skeptic prompt (`:1350-1357`) | dCalibratedLens |
| 6, tags | caller's args (`context`, `priorFindings` refs) | dConvergedCharter, which already owns "positional references migrated to tags" |
| role text | one line: `gov-synthesizer.md:11-12` | dBoundRoles |

## Where the record and the code disagree

- `gov-synthesizer.md:11-12` says it is handed "the findings the skeptics confirmed". The harness also hands it every unverified finding (`:1667`) and every refuted row through the appendix (`:1822-1826`).
- `gov-synthesizer.md:20` says "One item per defect". The harness says "merge findings of one binding grade only" (`:1678`). The harness wins every time measured.
- The "six refutation cases" exist on the spec kind only, which is 13 of the 50 reports.
- `REVIEW-PROTOCOL.md:199` calls the skeptics "default-refute". The harness's default depends on the finder's grade (`:1334-1336`): refute for medium or low, uncertain for high or blocker.
- Run B's split: the record says three defects across seven items. The map gives four defects across eight items. The fourth, `fixture-2-population`, splits only through B4, which the map also places on `hidden-spawns`. Excluding it leaves three defects across six items (H3/M1, H4/M15, H5/M2).

## Instruments

Everything is in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/instr/`:
- `commands.sh`: all 62 commands I ran, verbatim and in order, including each inline instrument's full source.
- `parse.py`: the appendix parser (I1); it writes `rows.json`.
- `skeptic.py`: the skeptic measures (I4); it writes `refuted.json`.
- `I1-parse.out` through `I18-closedloop-bydesign.out`: each instrument's output.
- `nonconfirmed.txt`: the 150 refutation rows.

The 34 hand-assigned refutation cases are listed with their reasons in the I4 step of `commands.sh` and in `I4-skeptic.out`.
