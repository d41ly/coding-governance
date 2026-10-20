# Research: the bug-class lookup, measured on gov's history

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 135's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-16-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

**Bug-class lookup research (point 6): does it serve the right class at the right moment?**

**Short answer: no.** The selector gets the moment wrong (only about 18% of the time does the file being edited pick the right class) and is mostly noise (6% precision on code reviews). The work it does is on the review side. My pick is to stop using it while code is being written, keep classes for review and gates, and serve classes at writing time only through a scout that selects by intent, and only if that scout wins a replay test. The four parts follow.

## 1. How it selects today

**Anchors.** A class's anchors are not declared. They are taken from its body: every backticked token that contains a `/` or ends in a known source extension (`tools/memory-tree/gotchas.py:16-20`, pattern at `:65`, harvested at `:281`).
- The match rule is in `selectable`. It matches by substring in both directions, or by equal basename, and the catalogue never matches itself (`gotchas.py:340-355`).
- A path that normalises to the repository root is refused (`:631-636`).

**Specificity tiers.** These only order the list; they never decide what is in it (`gotchas.py:358-372`):
- `path`: the anchor is the file, or a trailing suffix of it.
- `directory`: the anchor is a leading directory of the path.
- `basename`: everything else `selectable` admits.

The checklist sorts by tier, then by how many paths the class reaches, then by name. Whole tiers print in full while they fit inside `CHECKLIST_FULL_BUDGET = 12`; from the first tier that does not fit, each class prints as one line. No class is ever dropped (`:80-81`, `:681-691`, `:714-718`).

**Universal set.** A record marked `universal: true` (`:257`) is printed on every checklist, outside the budget (`:664-666`, `:712-713`). The cap is 6, set by `UNIVERSAL_BUDGET` (`.memory-tree.conf:536`). The six today are:
- `fixture-passes-by-finding-nothing`
- `guard-above-a-fold-makes-its-fallback-dead`
- `heredoc-escape-reaches-the-regex`
- `inline-fence-swallows-the-rest-of-the-file`
- `staged-break-substitutes-a-synthetic-value`
- `two-answers-to-one-question`

**Verbs.** `--for-diff` gets the paths from `git diff --no-renames --name-only` and hands them to `--for-paths` (`:776-802`, `:643-725`). Invariants print afterwards as a separate "by design" block.

**Callers:**
- The charter line "run it before any review" (`coding-governance-agents.template.md:118`, `AGENTS.md:121`).
- The unattended Skill's per-pass step (`.claude/skills/unattended/SKILL.md:121`).
- The build driver's post-commit `CHECKLIST` (`--for-diff HEAD~1..HEAD`), the spec audit's `--for-paths`, and the spec commit's checklist (`tools/workflows/unattended-build.template.js:561`, `:584`, `:601-603`).
- The unit prompt's post-commit step (`tools/workflows/unattended-unit.js:322`).
- The opt-in, default-off `prebuild` (`unattended-unit.js:43-51`, `:275-281`).
- The review harness: it splits the items across lenses and labels findings by `C<n>` (`tools/workflows/tier2-review.js:450-454`, `:846-866`, `:1501-1514`, `:1532`).
- The build method (`tools/memory-tree/BUILD-METHOD.template.md:168`, `:190`).
- In v2, the work order's bug-class field, "selected by `gotchas.py --for-paths`, the one selector" (architecture-v2 [SA-7]; dFurnishedOrders roster row).

**Catalogue today** (`gotchas.py --report`): 148 records, of which 145 are classes and 3 are invariants. 6 are universal and none is unanchored.

**A limit on what the records can show.** A finding's `classes` cell can only name a class that was on the checklist handed to that review (`tier2-review.js:1501-1513`). So from the records, recall is 100% by construction, and misses are invisible. I measured misses separately, by a hand sample (end of section 2).

## 2. Measured on gov's history

**Commands.** All were run in a `git clone --no-checkout` copy of this worktree under the session temp root, now deleted:
- For each review: `git checkout -q --detach -f <head>`, then `python tools/memory-tree/gotchas.py --for-diff <base>...<head>`, using each head's own tool and catalogue.
- Items were parsed with `^- \[ \] (\S+) \((universal|path|directory|basename)\)`.
- Ranges and ledgers came from the 66 review appendices that have a `classes` column. 47 of them carry a 40-hex range; 19 dClosedLoop design reviews carry none and are excluded.

How to read the table:
- **sel**: classes selected (universal + anchor).
- **rec**: the checklist size the review record states.
- **conf / cls**: confirmed findings, and how many of those carry a class.
- **hit**: distinct selected classes found on a confirmed finding.
- **noise**: selected classes that never matched a confirmed finding.
- **miss**: a labelled class not in the re-run.

| review | files | sel (u+a) | rec | conf | cls | hit | miss | noise |
|---|---|---|---|---|---|---|---|---|
| aBenchedProbe-1 | 21 | 33 (6+27) | 20 | 8 | 3 | 3 | 0 | 30 |
| aBriskPreflight | 66 | 50 | 50 | 10 | 3 | 3 | 0 | 47 |
| aFrugalTurnstile | 85 | 62 | none handed | 17 | 0 | 0 | – | 62 |
| aHeardState | 35 | 44 | 44 | 23 | 8 | 8 | 0 | 36 |
| aHomedAnchor | 24 | 56 | 15 | 30 | 11 | 6 | 0 | 50 |
| aLevelledCopy | 29 | 38 | 37 | 15 | 2 | 1 (+1 bare C<n>) | 0 | 37 |
| aMendedFleet | 369 | 89 | 89 | 17 | 5 | 1 (+4 C<n>) | 0 | 88 |
| aOrientedCast-1 | 162 | 84 | 84 | 13 | 7 | 6 | 0 | 78 |
| aOrientedCast-16 | 139 | 76 | 36 | 14 | 5 | 5 | 0 | 71 |
| aPairedSlots | 47 | 49 | 50 | 30 | 8 | 7 | 0 | 42 |
| aPrimedIndex | 35 | 33 | 33 | 20 | 7 | 7 | 0 | 26 |
| aQuotedBrief-1 r2 | 8 | 40 | 4 | 1 | 1 | 1 | 0 | 39 |
| aQuotedBrief-3 | 24 | 46 | 30 | 18 | 3 | 3 | 0 | 43 |
| aRoutedQuill-1 | 92 | 75 | 38 | 27 | 14 | 7 | 0 | 68 |
| aRoutedQuill-3 r2 | 101 | 80 | none | 3 | 0 | 0 | – | 80 |
| aSparedSpawn | 180 | 98 | 75 | 21 | 8 | 8 | 0 | 90 |
| aSweptBar | 68 | 78 | none | 11 | 0 | 0 | – | 78 |
| aTrimmedHook | 33 | 36 | 15 | 16 | 5 | 4 | 0 | 32 |
| cListedCensus | 15 | 18 | 18 | 13 | 2 | 2 | 0 | 16 |
| dHomedResolver | 29 | 34 | 22 | 7 | 2 | 2 | 0 | 32 |
| dRemeasuredRender | 90 | 91 | 42 | 11 | 5 | 4 | 0 | 87 |
| dSweptBranches 1-5 r1 | 40 | 38 | 17 | 28 | 3 | 0 (+3 C<n>) | 0 | 38 |
| dSweptBranches 1-5 r2 | 13 | 29 | 4 | 4 | 3 | 0 (+2 C<n>) | 0 | 29 |
| dSweptBranches 19-21 | 34 | 40 | 15 | 10 | 4 | 4 | 0 | 36 |
| 23 dClosedLoop design reviews with ranges (expansions a/b, fold ×5, library ×3, runtime-fold ×2, debt-folds, answers ×2, audit-fold, away-pass, night-pass, folds-closing ×2) | 11–39 each | 11–34 each | ≈ same | 522 | 160 | 99 total | 7 | 399 total |

**Totals:**
- **Code reviews (24):** 1,317 classes selected, 82 hits, **precision 6.2%**.
- **Design reviews (23):** 498 selected, 99 hits, 19.9%. This figure is inflated by self-anchoring. The classes this build filed anchor on this build's own records. For example, `route-names-an-output-its-actor-never-emits` and `policy-value-with-no-route` cite `memory/builds/dClosedLoop/...` files, so later rounds hit them at `path` tier. An anchor records where a class bit, not what triggers it.

**Where the hits come from, by tier:** path 102, basename 27, directory 25, universal 27. The six universals were selected 282 times and hit 27 times.

**The selector degenerates on large diffs.** On diffs of 85 files or more it selects 60–95% of the catalogue (aSparedSpawn 93%, aMendedFleet 95%, dRemeasuredRender 84%). Twelve classes are selected on every one of the 24 code reviews.

**Census:**
- 145 classes.
- Across all 66 appendices, 61 distinct named classes ever appear on a confirmed finding.
- 79 of the 137 classes ever selected in the 47 ranged reviews never hit.
- 400 of 1,771 confirmed findings carry a class (22.6%).
  - This is consistent with gap-register [gap-review-10], which records 724 of 907 unclassed over 36 appendices.
  - Today's count is 1,371 of 1,771 unclassed.

**Gate status** (each class record as it stands today):
- 50 classes are fully gated, 14 partly gated, and 84 ungated or documented-check only.
- Fully gated classes take 533 of the 1,815 selected items (29%) but carry only 20 of 389 labels (5%).
- Ungated classes carry 281 of 389 labels (72%).

**How often sessions run the lookup.** I scanned 4,736 transcript files: 76 main sessions plus their subagents, on this machine only, from 2026-08-04 to 2026-10-19.
- `--for-diff`: 871 calls (252 main, 619 subagent), in 47 sessions.
- `--for-paths`: 256 calls (101 main, 155 subagent), in 44 sessions.
- Workflow calls with gotchas.py in their arguments: 199.
- Read or Grep of any class record: **45**, in 7 sessions.

So about 1,127 checklist runs led to 45 opens of a class body. The subagent-to-session grouping is approximate.

**Misses, judged by hand.** I sampled 12 confirmed findings that carry no class:
- **Catalogue misses (5): the class did not exist at the head.**
  - aHeardState #2 → `held-suite-guard-misses-a-sibling-kit`, filed 2026-10-13 in `f1d88c60d`.
  - aFrugalTurnstile #1 and aSparedSpawn #1 → `a-runner-knob-owes-a-push-class`, filed 2026-10-11 in `32ec91177`, which is not in the aSparedSpawn head's tree.
  - aPrimedIndex #11 → `parser-drops-rows-it-cannot-place`.
  - dRemeasuredRender #1 → `verdict-printed-before-the-step-that-reverts-it`, filed the same day in `b41d79bc6`.
- **Labelling misses (2): the class was selected but the finding was not labelled.**
  - dRemeasuredRender #6 → `observed-by-claim-no-arm-discharges`.
  - aSparedSpawn #15 → `vacuous-selector-empty-population`.
- **Serving miss (1): no checklist was handed.** aFrugalTurnstile #9 fits `decision-re-derived-by-a-second-process`, and the re-run selects it.
- **No class fits (6):** aSweptBar #1, #3, #6 and #9, aPrimedIndex #5, and the other aBenchedProbe staged-break finding (#8).
- **Selector misses (the class existed and fit, but was not selected): 0.**

Conclusion: the selector's failure is noise, not recall.

**Where a record and the code disagree:**
1. Fifteen review records state a smaller checklist than `--for-diff` re-selects over the recorded range: 12 code reviews (for example aHomedAnchor 15 vs 56, dRemeasuredRender 42 vs 91) and 3 design reviews. The four design reviews that state a larger one (fold 6 vs 11, fold-round3 22 vs 16, runtime-fold 19 vs 13) are those whose labelled classes include ones the re-run does not select, which is where the 7 design misses come from. The ambiguity: callers evidently passed a different range or tool version than the recorded one. So the noise figures above describe the recorded range, not exactly what each review was handed.
2. `unattended-unit.js:47` says prebuild "stays off until a build has measured whether it cuts checklist-fix commits". I found no record of that measurement; only the spec and ledger of TOOL-aMendedFleet-74 mention it. The earlier source report found the pre-build list is 76–94% of the post-commit list, and counted 9 checklist-fix commits, 7 of them from one build (aMendedFleet source report [B#6]).

## 3. Where a gotcha bites (the moment of the mistake)

**Measured over every labelled code finding.** I ran the selector on just the file the finding cites, at the reviewed head, to see if that one path would have picked the class:
- Of 98 resolvable labels: path 10, directory 1, basename 7, universal 12, **none 68**.
- The 11 remaining labels were bare `C<n>` or a renamed class.

So the file being edited selects the right class about 18% of the time, outside the universals.

**Hand sample:**

| finding | moment of the mistake | input available then that could select it |
|---|---|---|
| aSparedSpawn #7, `text-mode-read-eats-a-bare-cr` | Writing new file `tools/run-gates/held_halves.py` (`06d38291c`); `open(..., encoding="utf-8", errors="replace")` at :150 | Path: none. Content: an `open(` in text mode. But a naive trigger matches 144 lines in 53 of 111 `.py` files today. |
| aSparedSpawn #16, `fixed-sleep-does-not-place-a-signal` | Editing a fixture in `run-gates.test.sh:3072` (`sleep 12`) | Content `sleep N` matches 163 lines in 14 test files. |
| aPrimedIndex #8, `subprocess-resolves-a-different-shell` | Editing `regen.py:217`, `shutil.which(run[0])`. The adjacent comment already describes the WSL hazard. | None needed: the author knew the class and still chose an insufficient fix. A sibling `resolve_bash` existed. This is a reuse or gate problem, not a serving problem. |
| aRoutedQuill #16, `two-guards-one-question-two-answers` | Writing a second reader of the conf (`check-wiring.sh:1455`, `${MEMORY_ROOT:-memory}`) that answers what `scratch-guard.js` answers | Only the intent ("grade it by the rules the gate grades it by") and a reuse probe. No path does. |
| aHomedAnchor #17, `amendment-leaves-its-other-half-standing` | Editing `.unattended.conf` and `adopt-unattended.sh`. The cited file, `SKILL.md`, was never touched. | A map from render source to rendered copy. The review says the bar's skill-wiring gate already reds it (record claim, not verified). |
| aBenchedProbe #2, `hand-named-gate-list-green-while-the-bar-reds` | Writing the spec's non-goal ("no selftest fixtures") and verifying against named legs | The spec and the verify step. No file edit is involved. |
| dRemeasuredRender #3, `line-claim-matched-over-the-whole-output` | Writing a two-substring assertion in `govkit/selftest.py` | Path tier `path` (one of the 10). The pattern is also syntactic, so Semgrep could catch it. |
| aTrimmedHook #11, labelled `hookspath-resolves-into-another-checkout` | `os.path.relpath` across drives in `gen_build_index.py:877` | No class fits. The label was stretched onto whatever item was on the list, so measured hits are, if anything, inflated. |

**Pattern.** The classes that carry the hits are shaped by an *act*, not by a path:
- amending a rule: 20 hits
- answering one question twice: 18
- routing an output: 11
- an "Observed by" claim no arm discharges: 8
- a policy value with no route: 8
- an owner decision whose "no" has no route: 7

Those acts are visible in a spec or intent, not in a file path. The classes that are syntactic are a minority (roughly 35 of 148 by my reading of the descriptions; approximate). For those, a trigger precise enough to stay quiet is a lint rule.

## 4. Candidates

Existing seams I checked first:
- the repository's own path-scoped rule (`.claude/rules/product.md`, `paths:` frontmatter)
- the PreToolUse Edit/Write hook (`scratch-guard.js`, wired in `.claude/settings.json`)
- the harness's `checklist` argument
- `review.left-shift`
- the dFurnishedOrders work order

`recall-opened.js` is only an observer and is not a seam for this.

Each candidate below carries the test that would make it lose, written before it was run, and that test's result.

**A. Status quo: anchor selection for authoring and review, plus SA-7 `--for-paths` in the work order.**
- *Loses if:* code-review precision is under 10%, or large diffs select at least 80% of the catalogue.
- *Result: loses.* Precision is 6.2%; large diffs select 84–95%; 1,127 runs led to 45 reads of a class body. SA-7 inherits the same numbers, because the pre-build list is 76–94% of the post-commit one [B#6].

**B. Path-scoped just-in-time serving.** This means either a PreToolUse hook returning `additionalContext`, or class anchors rendered into Claude Code `paths:` rules, Cursor `globs`, or Copilot `applyTo`.
- *Loses if:* the cited file selects the confirmed class in under 50% of labelled findings.
- *Result: loses.* 18 of 98; 68 select nothing.
- Timing makes it worse. PreToolUse `additionalContext` is "added to Claude's context alongside the tool result", so for an allowed Edit it arrives after the write. Path-scoped rules load earlier, when Read, Write or Edit touches a matching file, but they use the same selector. Per-edit load on code files would average 3.0 classes, with 0 of 395 code files firing nothing.

**C. Content- or command-triggered just-in-time serving.** Each class carries a regex or Semgrep-style trigger, matched against Edit `new_string` or a Bash `command`.
- *Loses if:* the classes carrying the hit mass have no syntactic trigger, or naive triggers fire on a large share of edits.
- *Result: loses.* None of the top six hit classes is syntactic. The naive triggers fire on 53 of 111 Python files (text-mode `open`) and 14 of 68 test suites (`sleep`). The regen.py case shows that serving the class does not help when the author already knew it. A precise trigger is a gate, so this collapses into D.

**D. Turn classes into gates and retire the lookup.**
- *Loses if:* most labels fall on classes no machine gate can express.
- *Result: loses as a full replacement* (72% of labels are on ungated, judgment-shaped classes). *It wins for the syntactic subset*, under the charter's [class] rule, through `review.left-shift`.
- Dropping fully gated classes from any checklist removes 29% of the items for 5% of the labels.

**E. Runtime injects classes per act** (v2's runtime layer).
- *Loses if:* it uses the B or C selector.
- *Result: loses* (it inherits the 18% and the noise). With E2's selector it is E2 run per act, which costs more and has no evidence that it does better.

**E2. The orientation scout selects classes by intent.** It reads the unit's spec or brief against the catalogue's one-line descriptions (the INDEX) and returns at most k classes, each with a reason, in the work order. This is the "Apply Intelligently (description)" mode of Cursor rules, and the embedded, active delivery Weber and Aha argue for.
- *Loses if (not run here; the build must run it):* replayed over the 21 closed code reviews that had a checklist, with the scout given each unit's spec at its pre-build commit and the INDEX as of that commit, and never the review, it scores no better than the top k of the anchor ranking at the same k against the confirmed labels plus hand-judged unlabelled findings, or its precision is under 20%.
- *Result: not run.* The only evidence for it is that the hit classes are act-shaped and named in specs.

**F. Retire outright: no checklist for authoring or review; the catalogue stays as library entries and gates.**
- *Loses if:* reviews with a checklist yield more confirmed findings than reviews without.
- *Result: inconclusive.* The three code reviews that had no checklist yielded 0.12 confirmed findings per changed file, against 0.23 for the 21 that had one. That is confounded: a round-2 review and record-heavy ranges, with n=3. Labels cannot exist without the checklist, so the records cannot settle it.
- *The test still owed:* an A/B with the checklist on and off, using `tools/workflows/review_replay.py` over the known-defect corpus that dFairHearing already plans. The authoring-time half can retire now on the numbers above.

## Pick

1. **Retire the anchor selector as the thing that serves classes while code is being written.** That means:
   - the post-commit per-pass checklist (`unattended-build.template.js:561`, `unattended-unit.js:322`, `SKILL.md:121`)
   - the default-off `prebuild`
   - SA-7's `--for-paths` field in the work order

   It loses its own losing test: 6.2% precision, 18% recall at the moment of the edit, 45 body reads in 1,127 runs.
2. **Keep classes on the review**, where they are the only source of labels and left-shift dispositions. Drop fully gated classes from the list (−29% items, −5% labels), and keep the anchors only to order the list. Whether review also stops selecting by anchors and gets every ungated class goes to the owner, decided by F's replay A/B.
3. **Turn the syntactic classes into gates** through `review.left-shift`, at their second occurrence, and take each gated class off the checklist.
4. **Answering the owner's question:** serving at writing time moves to the orientation scout (E2) only if it wins its replay test. Runtime per-act injection (B, C, E) is rejected on measured evidence. If E2 loses its test, writing-time serving retires outright.

## Sources (all read 2026-10-19)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks): PreToolUse `additionalContext` is "added to Claude's context alongside the tool result"; Edit and Write `tool_input` fields.
- [Claude Code memory, path-specific rules](https://code.claude.com/docs/en/memory): a rule "loads when Claude uses the Read, Write, or Edit tool on a matching file".
- [Cursor rules](https://cursor.com/docs/context/rules): glob rules are "auto-attached when a matching file is in context"; "Apply Intelligently" goes by description.
- [GitHub Copilot path-specific instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions): `applyTo` globs.
- [Semgrep rule syntax](https://docs.semgrep.dev/writing-rules/rule-syntax): `id`, `message`, `severity`, `languages`, `pattern`, and `paths` include and exclude.
- [Weber, Aha, Muñoz-Ávila, Breslow, "Active Delivery for Lessons Learned Systems", 2003](https://researchdiscovery.drexel.edu/esploro/outputs/bookChapter/Active-Delivery-for-Lessons-Learned-Systems/991019238533004721): lessons systems "should be embedded into the processes that they are meant to improve". A commentary's figure that 70% of lessons-learned systems fail ([IGI Global](https://www.igi-global.com/chapter/top-lessons-lessons-learned-systems/52208)) is secondary, and I did not verify it.
- [Sadowski et al., "Lessons from Building Static Analysis Tools at Google", CACM 2018](https://research.google/pubs/lessons-from-building-static-analysis-tools-at-google/): only the abstract was readable (fixes happen "before the problematic code is checked into the codebase"). The full text returned 403.

I wrote nothing in the repository, and my scratch clone and probe files are deleted. The two untracked research files in `git status` belong to other agents. Files I relied on:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\gotchas.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\tier2-review.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\unattended-unit.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\unattended-build.template.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\aMendedFleet\prompts\2026-10-04-prompt-TOOL-aMendedFleet-1-1-source-report.md`
