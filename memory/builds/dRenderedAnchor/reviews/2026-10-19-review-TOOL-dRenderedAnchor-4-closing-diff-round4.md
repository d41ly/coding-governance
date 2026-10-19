**Serves:** diff-review TOOL-dRenderedAnchor-3 TOOL-dRenderedAnchor-4

# Closing diff review, round 4: dRenderedAnchor unit 4, the round-3 fix batch

2026-10-19 · Tier-2 · on `branch/frosty-feistel-42acd4` · adversarial fan through `tier2-review.js`: 5 finder lenses, then 4 skeptic batches, then this synthesis. This round reads the fix for the 3 round-3 items (record `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-3-closing-diff-round3.md`). M4 promoted them into the batch unit TOOL-dRenderedAnchor-4, built at 6d560aed2. No running code changed in this range.

**Reviewed range:** `66ccdb26de56187068205b5c7a02a35eca610b66...f626f6e4712db576d3da210ed39e02c5664fb33a`. **ROUND 4.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker, a high or a medium. No confirmed finding says a round-3 item is still open.

Round 3's M1 is closed. Arm 17 builds a layout whose answer depends on the branch at `roles_lib.py:626`. Its preconditions sit inside the assertion. The main loop observed it RED with that line staged as `here = kit` (FAIL 1 of 62, arm 17 alone) and GREEN on the shipped line (PASS 62).

L1 and L2 are closed in substance.

Two low items remain, both in text this fold wrote. The arm 17 comment overstates which layouts tell the branch apart. The new gotcha entry overstates how the L2 phrase was reflowed.

## Review shape

Intensity **full** · raw **7** · confirmed **5** · refuted **2** · unverified **0** (0 uncertain) · precision **0.71**.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |

Adjudicated tally by item: **2 items**, 0 blocker, 0 high, 0 medium, 2 low. By raw confirmed finding: 0 blocker, 0 high, 0 medium, 5 low (ids 2, 3, 4, 5, 6).

Refuted: ids 1 and 7. Both describe a receipt row that can place a non-harness citation at the repository root, against docs that say a root file is never named at a prefixed install. The skeptics reproduced the behaviour. They refuted both findings as pre-existing: the unconditional claim already stood at base 66ccdb26, and this fold only added the round-3 L1 scope "at a prefixed install". The skeptic on id 7 notes it as a docs-only follow-up outside this range.

Run integrity:
- Lenses 5/5 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 4 judged sound, 1 judged UNSOUND (id 6, whose corrected fix is written below), 0 with none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED and 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

The run is complete.

Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent: 3 spec documents were supplied as `specs`, beside the range's commit messages. Checklist: 10 items, each assigned to exactly one of 5 lenses (security 2, correctness 2, seams 2, verification 2, intent 2). By design: the caller's byDesign.

## Items

### L1 [LOW]: arm 17's comment says the two values of `here` part on one layout only, but they part on two (ids 2, 4, 5, 6)

**Where:** `tools/roles/adopt-roles.test.sh:674-676`, the arm 17 comment: "the two values of `here` part on one layout only: a harness held only in the directory above the tool root, with no receipt row". The comment copies spec TOOL-dRenderedAnchor-4 §4 (lines 80-81), which copies the round-3 record's "only one case".

**What is wrong:** `resolve_kit_dir` probes `here/<home>` first and then `here.parent/<home>` (`roles_lib.py:127`).
- With `here = kit.parent` (the tool root), the probes are `<tool root>/<home>` and the directory above the tool root.
- With `here = kit`, the probes are `<kit>/<home>` and `<tool root>/<home>`.

The receipt branch does not depend on `here`, because the `.git` walk reaches the same root from either value. So the two values part on a second layout as well: a harness held at `<kit>/<home>/<file>`, which only `here = kit` reaches. That probe comes first, so it also wins when `<tool root>/<home>` holds the same file.

Two finders reproduced this in scratch repos. With `.git` plus a single file at `tools/roles/workflows/<harness>.js`, the tool-root call raised LookupError. The kit-directory call returned `.../tools/roles/workflows`.

**Consequence:** None in behaviour. Arm 17 is sound: its own layout is one of the two that part the branch, and it goes red on the `here = kit` break. The comment records the coverage argument, though, and it presents arm 17's layout as the only one that tells the branch apart. The next change to the probe order or to line 626 would read that as proof the guard is exhaustive. The reach is small, because no real install puts a home directory such as `workflows/` under `tools/roles/`.

**Fix:** Reword lines 674-676 along these lines: "with no receipt row, the two values of `here` part where a harness is held at `<kit>/<home>/` (only the kit directory reaches it, and it is probed first) or only in the directory above the tool root (only the tool root reaches it). This arm builds the second, the layout on which the C2 break moves a template harness."

Skeptics judged the fixes from ids 2, 4 and 5 sound; they say the same thing. The skeptic rejected id 6's own proposal ("part wherever a harness sits outside `<tool root>/<home>/`"), and the wording above is that skeptic's correction. Adding the kit-directory layout to the arm's WHAT THIS DOES NOT CHECK block is an acceptable alternative.

Spec TOOL-dRenderedAnchor-4 §4 is closed, so leave it unchanged. This record holds the correction.

**Left-shift gate:** add a checklist entry: "a comment or spec line that states which layouts a resolver call reaches is derived from the probe tuple, with each probe's reach listed for every value of `here`, never copied from a prior record". The read-only probe from id 5 belongs beside that entry:

```
python -I -c "import pathlib;k=pathlib.PurePosixPath('/fx/tools/roles');[print(h,[str(h/'workflows'),str(h.parent/'workflows')]) for h in (k.parent,k)]"
```

### L2 [LOW]: the gotcha entry says the full L2 phrase sits on one line in every carrier, but it still wraps after the article in three (id 3)

**Where:** `memory/gotchas/two-answers-to-one-question.md:65-67`, a new entry. It says the fix wrote "a `workflow`-driver harness of the workflow table" into every carrier "each on one line". Spec TOOL-dRenderedAnchor-4 S5 (line 41) says the same.

**What is wrong:** The phrase, article included, still breaks after the article in three places:
- `help/roles.md:130-131` ("Only a" / "`workflow`-driver harness of the workflow table ...")
- `tools/roles/adopt-roles.sh:33-34` ("Only a" / "# `workflow`-driver ...")
- arm 15's comment at `tools/roles/adopt-roles.test.sh:591-592` ("a citation that is" / "no `workflow`-driver ...")

Only `tools/roles/README.md:316` and `tools/roles/roles_lib.py:611` hold the whole phrase on one line. At base 66ccdb26 the break fell inside "harness of the / workflow table". The fold moved it to just before the article, so a grep without the article now finds every carrier. AC6 passes only because its grep drops the article.

**Consequence:** None in behaviour. The practical goal was met. The record meant to warn about wrapped phrases still states a wrap claim that is false for the phrase as quoted.

**Fix (skeptic judged SOUND):** Choose one:
- Reflow `help/roles.md:130-131` and `tools/roles/adopt-roles.sh:33-34` so that "a `workflow`-driver harness of the workflow table" sits whole on one line.
- Reword the gotcha entry (and S5, if it is still open) to say that "`workflow`-driver harness of the workflow table" sits on one line, without the article.

**Left-shift gate:** add a checklist probe that greps the carriers for the exact phrase the record quotes, article included, and compares the hit count with the carrier count. A record that says "each on one line" is then checked against the literal it states, not against a shortened grep.

review-shape kind=diff-review round=4 intensity=full at=synth raw=7 confirmed=5 refuted=2 unverified=0 blocker=0 high=0 medium=0 low=5 agents=10 out-tokens=80115

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/roles/adopt-roles.sh:38 | low | - | refuted | Pre-existing, so out of scope for this fold. The claim itself holds: in roles_lib.py:117-126, resolve_kit_dir reads a receipt row from the .git root before it probes, so a row can place a non-harness citation at the repository root. However, the adopt-roles.sh header at the base already stated the absolute with no receipt clause. `git show 66ccdb26:tools/roles/adopt-roles.sh` lines 41-42 read 'so its probes stop at `<tool root>/<home>/` and an adopter's file at the repository root is never named'. The fold only added the 'at a prefixed install' scope that the round-3 L1 item asked for. That item (round-3 record, lines 57-70) concerned the root install only, not the receipt. The receipt clause was missing at the base and is still missing at the tip: the diff left that defect as it was and made nothing newly reachable. The help page and README already carried 'a receipt row can place it' at the base. | sound | fold-text-is-unreviewed-surface |
| 2 | correctness | tools/roles/adopt-roles.test.sh:674 | low | low | confirmed | I checked the code. resolve_kit_dir probes `here/home` and then `here.parent/home` (roles_lib.py:127). From here=kit (tools/roles) the probes are tools/roles/<home> and tools/<home>. From here=kit.parent they are tools/<home> and <repo>/<home>. A harness held only at <kit>/<home>/ (tools/roles/workflows/x.js), with no receipt row, is reached only by here=kit. The shipped branch (roles_lib.py:626) therefore leaves the citation plain, and the `here = kit` collapse names it inside the kit, so the two values of `here` part on two layouts, not one. This diff introduced the wrong sentence: the arm 17 comment is new in adopt-roles.test.sh, and so is spec TOOL-dRenderedAnchor-4 §S1 line 80-81, 'part on one layout only'. The round-3 record made the same overstatement ('only one case'), and the fold copied it. Arm 17 still goes red on the `here = kit` break, because its own layout is one of the parting layouts. Only the explanation is wrong, and it could make the next editor think the arm covers every parting layout. Comment only, no behaviour effect: low. | sound | - |
| 3 | correctness | memory/gotchas/two-answers-to-one-question.md:65 | low | low | confirmed | The diff added the gotcha entry at memory/gotchas/two-answers-to-one-question.md:65-67. It says the fix wrote "a `workflow`-driver harness of the workflow table" into every carrier "each on one line", and spec S5 (spec-4 :41) says the same. In the tree the full phrase, article included, still breaks after the article in three places: help/roles.md:130-131 ('Only a' / '`workflow`-driver harness of the workflow table ...'), tools/roles/adopt-roles.sh:33-34 ('Only a' / '# `workflow`-driver ...') and adopt-roles.test.sh:591-592 ('a citation that is' / 'no `workflow`-driver ...'). Only README.md:316 and roles_lib.py:611 hold the whole phrase on one line. At the base 66ccdb26 the line break fell inside 'harness of the / workflow table'. The fold moved it to just before the article, so the review's article-less grep now finds every carrier. That means the practical goal was met and only the record's wording is wrong. It is a record and spec claim with no effect on behaviour, so it is low. | sound | - |
| 4 | seams | tools/roles/adopt-roles.test.sh:674 | low | low | confirmed | Arm 17's comment is new in this diff (adopt-roles.test.sh:674-675), and it says the two values of `here` 'part on one layout only'. resolve_kit_dir (roles_lib.py:127) probes `here/home` and then `here.parent/home`. With here=kit the probes are <kit>/<home> and <tool root>/<home>. With here=kit.parent they are <tool root>/<home> and <above>/<home>. The two choices therefore also give different answers for a harness held only at <kit>/<home> (kit finds it, kit.parent raises LookupError), and for one held at both <kit>/<home> and <tool root>/<home> (each returns a different directory). Spec §4 :78 even lists the `<tool root>/roles/<home>` probe and still concludes 'one layout only'. The arm's fixture and assertion are unaffected, so the defect is in the comment only. No real install puts a home dir such as workflows/ under tools/roles/ (ls shows none), so the misleading reach is small: low. | sound | - |
| 5 | verification | tools/roles/adopt-roles.test.sh:674 | low | low | confirmed | Arm 17 and its comment are new in this diff: the base 66ccdb26 has no 'arm 17' in adopt-roles.test.sh, and line 674 now reads 'the two values of `here` part on one layout only'. The resolver at roles_lib.py:127 is `probes = (here / home, here.parent / home)`. With here=kit.parent that gives <tool root>/<home> and <repo-ish parent>/<home>. With here=kit it gives <kit>/<home> and <tool root>/<home>. The receipt branch does not depend on `here`, because root is found by walking up to .git and is the same for both. So the two values also part when a harness sits at <kit>/<home>/<file>: only `here = kit` reaches that, and it is probed first, so it also wins when <tool root>/<home> holds the file too. The 'one layout only' claim is false. Arm 17 itself is unaffected: its layout does part the two values. This is a comment that misstates coverage and changes no behaviour, so the grade is low. | sound | two-answers-to-one-question |
| 6 | intent | tools/roles/adopt-roles.test.sh:674 | low | low | confirmed | This is the same defect as id 5, found through the intent lens. The comment at adopt-roles.test.sh:674 is new in this diff and says the two values of `here` part on one layout only. roles_lib.py:127 probes `here/home` first, so `here = kit` also reaches <kit>/<home>/<file>, which the tool-root call never probes. The finder's scratch probe agrees with the code: kit/workflows resolves with here=kit and raises LookupError with here=tools. The comment is false and states coverage wrongly. It has no behavioural effect. | unsound | - |
| 7 | intent | help/roles.md:134 | low | - | refuted | The behaviour the finder describes is real, but the defect is older than this diff, so it is out of scope. I reproduced the probe in a scratch tree with `.git`, `tools/roles/`, `run-gates/run-gates.sh` at the root, and `.governance/install.json` holding the row source=path=`run-gates/run-gates.sh`. `resolve_cited_paths` returned `[('{{TOOL_ROOT}}run-gates/run-gates.sh', 'run-gates/run-gates.sh')]`. With the receipt removed it returned `[]`. The reason is in `resolve_kit_dir` (roles_lib.py:112-125): it reads the receipt from the `.git` root before any probe, so a receipt row can name a file at the repository root. The wrong half of the claim, though, is unchanged from the base. `git show 66ccdb26:help/roles.md` line 134 already reads 'a receipt row can place it, and a file at the repository root never answers it'. Base tools/roles/README.md:320-321 and adopt-roles.sh:36-38 already say 'an adopter's file at the repository root is never named'. Both make the same unconditional claim, and the same receipt row falsifies them at the base. This fold only added the qualifier 'at a prefixed install', which was round 3's L1 cure for the root-install counterexample. That edit neither created the false-under-receipt reading nor made it reachable. Round 3 reviewed the range that introduced these sentences and raised only the root-install case. This receipt counterexample is a separate, pre-existing gap in that text, not a defect in this fold's fix. By the SCOPE rule it is refuted as pre-existing. It is still worth noting as a docs-only follow-up. | sound | - |
