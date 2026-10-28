**Serves:** spec-audit TOOL-dWellOiledMachine-100@rev-1 TOOL-dWellOiledMachine-101@rev-1 TOOL-dWellOiledMachine-98@rev-1 TOOL-dWellOiledMachine-99@rev-1 TOOL-dWellOiledMachine-102@rev-1 TOOL-dWellOiledMachine-103@rev-1 TOOL-dWellOiledMachine-104@rev-1 TOOL-dWellOiledMachine-105@rev-1 TOOL-dWellOiledMachine-106@rev-1 TOOL-dWellOiledMachine-107@rev-1 TOOL-dWellOiledMachine-108@rev-1

# Tier-2 review: Build dWellOiledMachine, spec audit of the eleven round-5 promotion specs (units 98-108)

Provenance: this is round 1 of a Tier-2 spec audit of the specs that the round-5 spec audit promoted (spec commit 05ab0d1f8). Five finder lenses ran as gov-spec-reviewer and five skeptic batches as gov-skeptic. gov-synthesizer wrote this synthesis.

Reviewed: memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-100.md@43f14f9425d2ad714da3912a9b4dea38a0a28912, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-101.md@9725bbaf51a3cb441087e6679f961cef19a13bf3, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-98.md@aaa23e425164efcd4ecb5762816ebf22290f1d27, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-99.md@deb3c149b2596d3072ac975c5b61099a38c61592, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-102.md@88bd61252c829fb81dd3d61218ef2e2047623f9c, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-103.md@e9eea889ecaca037f85b2cef0fb94e6c78055a90, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-104.md@923c9597291eb3c52963eeba1d95cabb32ce91e5, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-105.md@a5deb1baa5531e0fc03a2be92de33316350167bc, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-106.md@399456c38609f8795e4024d4780cceb77cebb884, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-107.md@51f7afccc79b435a11dd8f6cf86221ba5dee87a0, memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md@852d5db45ceaefe97789363f5e7eef66f3d13f19

ROUND: 1

## Verdict: BLOCKED

One blocker is confirmed. Spec 108 AC12 is already green at base, so it certifies a rewrite of 90 AC20 that it never checks (item B1). The blocker must be fixed before unit 108 builds.

By item, the tally is 20 items: 1 blocker, 4 high, 7 medium and 8 low. By raw confirmed finding, it is 30 findings: 1 blocker, 5 high, 14 medium and 10 low. The two tallies differ because findings that describe one defect are merged into one item. Findings are merged only when they share a binding grade.

Every binding grade is kept as given. The skeptics re-graded 7 findings: ids 8, 9, 10, 23 and 26 from high to medium, and ids 13 and 32 from medium to low. Those grades bind.

Three defects were each reported under more than one binding grade, so each one appears in more than one item:
- The AC12 defect in spec 108 binds at blocker (id 27), at high (id 4, which adds the unobserved S12/S13 edits) and at medium (id 10). In this synthesis's judgement the defect is one blocker.
- The duplicate loader count in 103 AC1 binds at high (id 20) and at medium (ids 1, 8, 26).
- The duplicate loader count in 106 AC1 binds at high (id 21) and at medium (ids 2, 9, 26).

For the loader-count defects, this synthesis judges medium right: the effect is a false red that surfaces as a deviation and lets nothing wrong pass. The high grades bind regardless.

## Review shape

Intensity full, raw 32, confirmed 30, refuted 2, unverified 0 (0 uncertain), precision 0.94.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| failure-envelope | yes | 7 | 6 | 1 | 0 | 0 | 0.86 |

The two refuted findings, ids 22 and 28, were refuted as duplicates of ids 27 and 23. Their defects are covered by items B1 and M3.

## Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdict handling: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 29 judged sound, 1 judged UNSOUND (id 30), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by a skeptic, 7 re-graded by a skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 97 spec documents were supplied as `specs`, as sibling context.
- Checklist: 18 items, each assigned to exactly one of the 5 lenses (coherence 4, grounding 4, reuse 4, blast-radius 3, failure-envelope 3).
- By design: none was supplied (no caller byDesign, and a block of 0).
- Move check: no checked subject moved.

Every integrity count is zero, so the run is complete.

## Blocker

### B1. Spec 108 AC12 is green at base and certifies a rewrite it never checks (id 27)

- **Where:** `2026-10-27-spec-TOOL-dWellOiledMachine-108.md`, section 6 AC12, checked against section 2 S12/S13.
- **What is wrong:** S12 requires the AC20 slice of spec 90 to spell the full paths `tools/runtime/supervise.py` and `tools/memory-tree/door_fixture.py`. AC12 greps only the bare names `supervise.py` and `door_fixture.py`. At HEAD the slice already holds each bare name once, holds `tools/**` zero times, and holds each full path zero times.
- **Consequence:** AC12 passes before the unit is built. It accepts the exact red case it names: "the rewrite was skipped and the bare name still satisfies the clause". A build that skips 97 S1's rewrite of 90 AC20 is certified as done.
- **Fix (judged sound by the skeptic):** Grep the full paths over the flattened slice: `grep -c 'tools/runtime/supervise.py'` and `grep -c 'tools/memory-tree/door_fixture.py'`, each printing 1. Keep the `tools/\*\*` clause at 0. Confirm that both counts print 0 on today's spec 90.
- **Left-shift gate:** a spec-lint leg that runs every grep-count criterion against the base tree, and fails any criterion whose red case is already green there.

## High

### H1. AC12 also leaves the S12 and S13 edits to spec 97 unobserved (id 4)

- **Where:** `...-108.md`, section 6 AC12, checked against section 2 S12 and S13.
- **What is wrong:** AC12 has the bare-name defect of B1, and it also reads only spec 90. S12 and S13 rewrite 97 AC1, and S13 adds a line to 97 section 4. No criterion reads either edit.
- **Consequence:** S12's and S13's edits to spec 97 could be skipped, and AC12 would still certify them.
- **Fix (judged sound by the skeptic):**
  - Grep the full paths, each printing 1, and keep `tools/\*\*` at 0, as in B1.
  - Also pipe `<AC1 of spec 97>` to `grep -c "AC20"` (or to the awk slice text), printing 1.
  - Grep 97 section 4 for the recorded base-0 count.
- **Left-shift gate:** an "Observed by" parity check. Each S-bullet's named criterion must read every file that the bullet edits.

### H2. AC21 checks spec 97's amendment only against unit 94, not the earliest unit it corrects (ids 5, 29)

- **Where:** `...-108.md`, section 6 AC21, checked against section 2 S9, S10, S21, S22 and S23.
- **What is wrong:** AC21 runs only `check_amended_before_built 97 108 94` for spec 97, and unit 94 is order 67. The batch's spec-97 amendment corrects text that earlier units consume:
  - S21 corrects 97 S20, which rev-bumps spec 92 (order 31).
  - S9/S10 correct 97 S1's rewrite of 90 AC20 (order 65).
  - S22 corrects 97 S15, which bumps spec 93 (order 66).
- **Consequence:** Suppose M2's cross-read is skipped and the batch lands after unit 92 builds but before unit 94 builds. Unit 92 then builds without the S21 guard, which can file a second disposition row, and AC21 still exits 0. Its stated red case ("lands after the build commit of a unit whose spec it corrects") is not what it checks. The path is narrow, because S23 routes every bump to M2 first.
- **Fix (judged sound by the skeptic):** Use `check_amended_before_built 97 108 92`, and keep `95 108 90` and `96 108 93`. Better, loop over every unit that spec 97 amends (90 91 92 93 94), as 106's AC15 loop does, so the failing unit is named.
- **Left-shift gate:** derive the unit list of every ordering criterion from the amended spec's S-bullets, not from hand-typed text.

### H3. 103 AC1 counts the predicate loader once, but a correct build leaves two copies in spec 96 (id 20)

- **Where:** `...-103.md`, section 6 AC1, last clause, read with `...-104.md` section 2 S1.
- **What is wrong:** AC1 requires `grep -c "sed -n '/^check_amended_before_built() {/,/^}/p'" <spec 96>` to print 1. 103 S2 puts that loader in 96's section 6 preamble. 104 S1 puts its fixture into 96 section 4 verbatim, and the fixture's first line holds the same string. Both land at the same M2 cross-read (order 68), so a correct build counts 2. Spec 103 names 104 only as "the staged red case" and has no edge on the shared string.
- **Consequence:** AC1 is red at unit 103's pass on a correct build. The run stalls, records a false deviation, or "fixes" the spec by deleting correct text.
- **Fix (judged sound by the skeptic):**
  - Count the loader in the preamble alone: `awk '/^## 6\./{p=1;next} /^- \*\*AC1\*\*/{p=0} p' <spec 96> | grep -c "sed -n '/^check_amended_before_built() {/,/^}/p'"` prints 1. Requiring "1 or more" also works.
  - Name TOOL-dWellOiledMachine-104 in 103's Edges.
  - Run AC1 once over a scratch spec 96 that has both amendments applied.
- **Grade note:** this synthesis judges this medium, for the reason given under the verdict. The high grade binds.
- **Left-shift gate:** before a batch is promoted, apply every same-pass amendment to a scratch copy of the target spec, then run each sibling's criteria over it.

### H4. 106 AC1 counts the predicate loader once, but a correct build leaves two copies in spec 97 (id 21)

- **Where:** `...-106.md`, section 6 AC1, last clause, read with `...-107.md` section 2 S1.
- **What is wrong:** This is H3's defect in spec 97. 106 S2 puts the loader in 97's section 6 preamble. 107 S1 puts its fixture, whose first line is the same `eval "$(sed -n ...)"`, into 97 section 4. Both land at M2 (order 69), so the count is 2 where AC1 requires 1.
- **Consequence:** Unit 106's pass is falsely blocked, or a deviation is recorded. The criterion cannot tell whether the preamble load landed.
- **Fix (judged sound by the skeptic):**
  - Scope the grep to 97's section 6 preamble, from `## 6.` (line 236) to the AC1 bullet (line 243), or accept "1 or more".
  - Add an edge to TOOL-dWellOiledMachine-107.
  - Run AC1 over a scratch spec 97 that has both 106 S2 and 107 S1 applied.
- **Grade note:** this synthesis judges this medium. The high grade binds.
- **Left-shift gate:** the same as H3.

## Medium

### M1. 103 AC1's loader count goes red on a correct build (ids 1, 8, 26)

- **Where:** `...-103.md`, section 6 AC1, read with S2 and with `...-104.md` section 4 The fixture.
- **What is wrong:** This is the defect in H3, as reported at medium. Id 26 also names the same clause in 106 AC1, which is covered in M2.
- **Consequence:** The criterion is falsely red at unit 103's pass. A builder may be pushed to strip the fixture's loader line to make the count 1.
- **Fix (judged sound by the skeptic):** Count the loader only inside the section 6 preamble (the awk slice in H3), printing 1. Alternatively, state the whole-file count as 2 and name the fixture line as the second copy.
- **Left-shift gate:** the same as H3.

### M2. 106 AC1's loader count goes red on a correct build (ids 2, 9)

- **Where:** `...-106.md`, section 6 AC1, read with S2 and with `...-107.md` section 4 The fixture.
- **What is wrong:** This is the defect in H4, as reported at medium. Spec 97 holds 0 copies of the loader at base and holds 2 after both amendments, while AC1 requires 1.
- **Consequence:** The criterion is falsely red at unit 106's pass.
- **Fix (judged sound by the skeptic):** Scope the count to spec 97's section 6 preamble, printing 1. Alternatively, require 2 and name the fixture line.
- **Left-shift gate:** the same as H3.

### M3. 108 AC8 uses bare-name pathspecs that can never match (ids 3, 11, 23)

- **Where:** `...-108.md`, section 6 AC8, checked against section 2 S8.
- **What is wrong:** AC8 runs `git ls-files --error-unmatch supervise.py door_fixture.py` from the repository root. A bare pathspec matches only a root-level file, so the command exits 1 even after both files are tracked under `tools/runtime/` and `tools/memory-tree/`. S8 spells the full paths.
- **Consequence:** AC8 is falsely red at unit 108's pass. It also repeats the bare-name class that finding 7 and S12 exist to remove.
- **Fix (judged sound by the skeptic):** `git ls-files --error-unmatch tools/runtime/supervise.py tools/memory-tree/door_fixture.py` exits 0.
- **Left-shift gate:** a spec-lint leg that flags any git pathspec in a criterion that has no `/` and names no root-level tracked file.

### M4. 108 AC12 can never tell whether the AC20 rewrite was made (id 10)

- **Where:** `...-108.md`, section 6 AC12, checked against section 2 S12.
- **What is wrong:** This is the defect in B1, as reported at medium. Each full path contains its bare name, so AC12 stays green both before and after the rewrite.
- **Grade note:** the skeptic graded this medium because AC10 still catches a wholly skipped AC20 rewrite. This synthesis judges the defect a blocker, as in B1. The medium grade binds for id 10.
- **Fix (judged sound by the skeptic):** Grep the full paths, each printing 1. The build must first confirm that both print 0 on today's spec 90.
- **Left-shift gate:** the same as B1.

### M5. S10's AST walk is narrower than the regex it replaces, and it flags the resolver idiom (ids 12, 16, 30)

- **Where:** `...-108.md`, section 2 S10, section 4 Evidence (the walk) and section 6 AC10.
- **What is wrong:** S10 defines the class as "any spawn whose argv's first element is the literal `bash`". Its walk flags only a Call whose first positional argument is a List or Tuple literal that opens with `'bash'`. Run over scratch files, the walk shows three problems:
  - It misses a variable-held argv (`cmd = ["bash", s]; subprocess.run(cmd)`), a walrus form, a keyword argv (`args=["bash", ...]`) and the concatenated shape `["bash", ...] + rest`. The concatenated shape is used in the tree at tools/run-gates/held_halves.py:129. 90 AC20's current regex catches the variable and walrus forms.
  - It flags the correct resolver form, `resolve_shell_argv(["bash", ...])`, as used at tools/govkit/matrix.py:911. All 4 of its hits on the real tree are such non-spawn calls.
  - It re-implements an existing check: `test_no_bare_bash_argv` at tools/run-gates/measure_legs.py:2685 already limits the match to `subprocess.<attr>` calls, unwraps `ast.BinOp`, and keeps a liveness count.
- **Consequence:** 90 AC20, 94 AC8 and 97 AC1 would pass a supervise.py that ships a bare-bash spawn in any of the missed shapes, and go red on one that uses the resolver correctly. Section 4 Evidence records neither gap.
- **Fix:** the fixes for ids 12 and 16 were judged sound. The fix for id 30 was judged UNSOUND, and the skeptic's corrected fix is the one given here.
  - Base 90 AC20's walk on measure_legs' `test_no_bare_bash_argv`: match `subprocess.*` calls only, unwrap `ast.BinOp` to its left operand, and keep its liveness count (`calls >= N`). Cite measure_legs.py:2685 in S10 and in section 10.
  - Also flag any `ast.List` or `ast.Tuple` node in the two files whose first element is the constant `'bash'`, so that variable-held, walrus and `args=` keyword argvs are caught.
  - Add staged cases to 94 AC8's red arm and to AC10: a variable-held argv (`cmd=['bash','x']; subprocess.run(cmd)`), an `args=['bash','x']` keyword, and `subprocess.run(["bash", "x"] + y)`.
  - Expect zero hits over a file that calls `resolve_shell_argv(["bash", ...])`.
  - Change AC10's single-spelling grep to a distinctive substring of the new walk: it counts 1 over spec 90, 0 over spec 94 and 0 over 97 AC1. The current `isinstance(n.args[0],(ast.List,ast.Tuple))` spelling no longer survives.
  - Record in section 4 what the walk does not check.
- **Left-shift gate:** a reuse-audit check. A spec that writes a new AST or regex guard must cite the existing guard of the same class, or state that none exists.

### M6. Spec 98's predicate walks build_commit uncached over a growing window, and section 5 gives no timing (id 14)

- **Where:** `...-98.md`, section 5 perf / scale, and the predicate's `build_commit` call in section 4.
- **What is wrong:** The predicate calls `build_commit` over `$floor..HEAD` with no `_SUBJ` cache and no cap. Uncached, that costs a `read_attribution_tokens` call plus a `git show` per commit, about 0.2 s per commit as measured. The window includes main's landings. AC3's `999` case walks the whole window.
- **Consequence:** About 25 predicate calls across units 98 to 108, plus the fixtures, could each take minutes. One call can exceed a bounded criterion run, and that red would come from the timeout, not from the order.
- **Fix (judged sound by the skeptic):** Time one `check_amended_before_built 90 95 999` on a realistic window and state the figure in section 5. Better, declare `_SUBJ` in the predicate (one `read_attribution_tokens` pass over `$floor..HEAD`, as check-pass-order.sh does).
- **Left-shift gate:** require a measured figure in any section 5 perf line that prices a history walk.

### M7. The three history fixtures share one fixed scratch path per spec (id 31)

- **Where:** `...-101.md` section 4 The fixture, and the same in specs 104 and 107. Also section 5 risks.
- **What is wrong:** Each fixture builds its repository at `$(cygpath -u "$TEMP")/abb95`, `abb96` or `abb97`, and runs `rm -rf` on it at both start and end. Section 5 prices only the cygpath dependency and says nothing about concurrent runs.
- **Consequence:** Two overlapping runs, from two worktrees or parallel skeptics, would delete and re-init each other's repository. The printed before/after/unbuilt lines could then be falsely red or falsely green.
- **Fix (judged sound by the skeptic):** Use `fx=$(mktemp -d "$(cygpath -u "$TEMP")/abb95.XXXXXX")` with `trap 'cd /; rm -rf "$fx"' EXIT` in all three fixtures, and say in section 5 that runs are isolated. Run two copies concurrently once to confirm they no longer collide.
- **Left-shift gate:** a spec-lint leg that flags a fixed `$TEMP/<name>` path in any fixture script.

## Low

### L1. Line citations of specs 95-97 predate the folds in 05ab0d1f8 (ids 6, 15, 24)

- **Where:** section 4 Evidence of `...-98.md`, `-99`, `-100`, `-102`, `-103`, `-105` and `-106`. Also 108 section 4 Evidence, which cites "96's lines 20 and 124".
- **What is wrong:** The cites were measured at 0d8692025. The hands-off folds in the same commit moved those lines by 1 to 6. Some examples:

  | Target | Cited at | At HEAD |
  |---|---|---|
  | 95 AC2 | 136-140 | 142 |
  | 96 AC5 | 179 | 184 |
  | 97 AC15 | 295 | 300 |
  | 96 `<BASE>` | 150/179 | 155/184 |
  | 97 `<BASE>` | 234/295 | 239/300 |
  | 96 "274" | 20/124 | 21/129 |

- **Consequence:** The effect is cosmetic: a reader lands a few lines off. It is the same class that 108 S19 repairs.
- **Fix (judged sound by the skeptic):** Cite by bullet label (95 AC2, 96 AC5 and its section 6 preamble, 97 AC15 and its preamble), as 108 S19 does, or re-measure every cite at the landing HEAD.
- **Left-shift gate:** a lint that rejects `spec-NN.md:<line>` cites of a spec that is still open, and requires a bullet label instead.

### L2. S21 adds a second exactly-1 count of the row that 97 AC14 already counts (id 7)

- **Where:** `...-108.md`, section 2 S21, checked against TOOL-dWellOiledMachine-97 AC14.
- **What is wrong:** 97 AC14 already greps the `SEV · TOOL-dPlacedRequest-<id> ·` disposition row and expects 1. S21 adds the same count to 97 AC12.
- **Consequence:** The two copies can drift apart. There is no effect on behaviour.
- **Fix (judged sound by the skeptic):** Point S21 at 97 AC14, strengthened to "exactly 1", instead of adding a count to AC12.
- **Left-shift gate:** a lint that flags one grep pattern asserted by two criteria of one spec.

### L3. The first clause of 108 AC15 is green at base and cannot observe S17 (id 13)

- **Where:** `...-108.md`, section 6 AC15, first clause, checked against section 2 S17.
- **What is wrong:** `<S1 of spec 90>` piped to `grep -c "re-render"` already prints 1 today, so the clause cannot observe S17's pointer to TOOL-dWellOiledMachine-93's tree-wide re-render.
- **Consequence:** A skipped cross-reference rewording reads as done.
- **Fix (judged sound by the skeptic):** Grep a token that only the amendment adds, such as `TOOL-dWellOiledMachine-93` together with "tree-wide", within the S1 bullet. Confirm that it prints 0 at base.
- **Left-shift gate:** the same as B1.

### L4. Spec 98's predicate attributes A by subject only and P by trailer or subject (id 17)

- **Where:** `...-98.md`, section 4 The predicate: the `a=$(git log --reverse --format='%H %s' ... | grep -E ...)` line and the bullet **A**.
- **What is wrong:** A is found by a subject-only grep. P comes from `build_commit`, which uses `read_attribution_tokens` (lib-unattended.sh:1149) and honours `Pass:` trailers. The id regex is a hand copy of `id_rows`/`id_in`.
- **Consequence:** A commit attributed by a `Pass:` trailer is mis-attributed, against the library's "attributed one way everywhere" rule. The effect is contained, because S3's route names the unit in the subject.
- **Fix (judged sound by the skeptic):** Find A with `read_attribution_tokens --reverse "$floor..HEAD" -- "$d/spec/*-TOOL-dWellOiledMachine-$1.md"` and keep the first line whose tokens contain ` TOOL-dWellOiledMachine-$2 `. Alternatively, state the gap under "What it does not check" and require S3's commit to carry no `Pass:` trailer.
- **Left-shift gate:** a lint that flags `git log --format=... %s | grep` attribution in a script that sources lib-unattended.sh.

### L5. The reuse audits in specs 101, 104 and 107 miss routed_commits.py's build_fixture (id 18)

- **Where:** section 10 Reuse audit of `...-101.md`, and the same sentence in 104 and 107.
- **What is wrong:** All three say that no existing seam builds a git-history fixture. `build_fixture` at tools/memory-tree/routed_commits.py:387 builds a scratch repository from an ordered commit list in one `git fast-import`.
- **Consequence:** Each fixture hand-rolls `git init`/`git commit`, and the reuse record misleads the next author.
- **Fix (judged sound by the skeptic):** Name `build_fixture` in each section 10. Either use it, or say why not: it is Python inside a kit self-test, and the predicate is bash.
- **Left-shift gate:** an entry in the project's bug-class checklist: reuse audits grep for `fast-import` and `build_fixture` before claiming that no seam exists.

### L6. Spec 107's fixture re-spells AC15's loop instead of running it (id 19)

- **Where:** `...-107.md`, section 4 The fixture (the `loop()` line), checked against section 10.
- **What is wrong:** Section 10 says the predicate runs "inside AC15's own loop". The fixture defines its own `loop()`, and AC15's text is never loaded or run.
- **Consequence:** A wrong unit list or argument order in 97 AC15 would not turn AC16 red. This is contained, because 106 AC1 separately greps AC15.
- **Fix (judged sound by the skeptic):** Extract and run AC15's loop from spec 97 inside the fixture, the way the predicate is loaded with `sed`, and wrap its output in the bracket form. Alternatively, reword section 10 to say the fixture re-spells the loop, and add an AC1 clause that greps both 97 AC16's fixture and 97 AC15 for `check_amended_before_built $n 97 $n`.
- **Left-shift gate:** the fixture loads every criterion text it claims to test from the spec, never a re-typed copy.

### L7. Spec 108's Files touched omits RUN.md, which F1's park entry writes (id 25)

- **Where:** `...-108.md`, section 4 Files touched, checked against section 8 F1.
- **What is wrong:** F1 resolves (a) as a park entry in the run-state file at the M2 cross-read that lands S11, but Files touched lists only specs 95-97 and the README.
- **Consequence:** The write-set renders under-state the route. The effect is cosmetic, because the list is labelled an estimate.
- **Fix (judged sound by the skeptic):** Add `memory/builds/dWellOiledMachine/RUN.md` to section 4 Files touched, and name the park entry in S11 or S23.
- **Left-shift gate:** a lint that cross-checks every path named in sections 2 and 8 against section 4 Files touched.

### L8. Spec 108's "Observed by" claims for S11 and S13 have no reading criterion (id 32)

- **Where:** `...-108.md`, section 2 S11 and S13, which are claimed to be observed by AC11 and AC12.
- **What is wrong:** S11 adds `tools/memory-tree/README.md` to spec 93's Files touched and `kit/dogfood doc parity` to its section 7 leg line. AC11 reads only the kit README and the docstring. S13's line in 97 section 4 is claimed by AC12, which reads only spec 90.
- **Consequence:** A skipped edit goes unflagged, and unit 93's pass runs without the doc-parity leg. The merge bar still runs its legs.
- **Fix (judged sound by the skeptic):**
  - Add to AC11: `awk '/^## 7\./{p=1;next} /^## 8\./{p=0} p' <spec 93> | grep -c "kit/dogfood doc parity"` prints 1.
  - Add to AC11: `awk '/^### Files touched/{p=1;next} /^#/{p=0} p' <spec 93> | grep -c "tools/memory-tree/README.md"` prints 1.
  - Add to AC12 a grep over spec 97's section 4 for the recorded base count.
- **Left-shift gate:** the "Observed by" parity check in H1.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=32 confirmed=30 refuted=2 unverified=0 blocker=1 high=5 medium=14 low=10 agents=11 out-tokens=231790

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-103.md:section 6 AC1 (against TOOL-dWellOiledMachine-104 section 4 The fixture) | medium | medium | confirmed | Spec 103 S2 (line 36) puts the one-line eval loader into 96's section 6 preamble. Spec 104 S1 puts its fixture into 96 section 4 verbatim, and the fixture's first line (104:62) is the same eval line. Both specs are order 68 and both amend 96 in the M2 spec pass. Piping those two lines into the grep pattern from 103 AC1 printed 2, but AC1 (103:100-101) requires 1, so AC1 goes red on a correct build. At HEAD spec 96 holds 0 copies of the loader, so the count is not 1 today either. | sound | - |
| 2 | coherence | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-106.md:section 6 AC1 (against TOOL-dWellOiledMachine-107 section 4 The fixture) | medium | medium | confirmed | Spec 106 S2 (line 36) writes the eval loader into 97's preamble. Spec 107 S1 places its fixture in 97 section 4 verbatim, and the fixture opens with the same eval line (107:62 region). Both units are order 69. A grep over specs 106 and 107 together finds the pattern at 106:36 and at the fixture line, so after both amendments spec 97 counts 2. 106 AC1 (line 103) requires 1, so it is red on a correct build. | sound | - |
| 3 | coherence | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC8 (against section 2 S8) | medium | medium | confirmed | 108 AC8 (line 254) runs `git ls-files --error-unmatch supervise.py door_fixture.py`. I ran it from the repository root: it printed "pathspec 'supervise.py' did not match" and exited 1. Bare pathspecs match only root-level files, so this cannot pass once the files exist under tools/runtime and tools/memory-tree. S8 (108:70-72) spells the full paths. Neither file exists yet even under its full path, but the bare-name form can never pass. | sound | - |
| 4 | coherence | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC12 (against section 2 S12, S13) | high | high | confirmed | I re-ran 108 AC12's slice over spec 90 at HEAD. It reads "git grep -nE ... -- supervise.py door_fixture.py". The counts were supervise.py=1, door_fixture.py=1 and tools/\*\*=0, so AC12 is already green at base. The full paths tools/runtime/supervise.py and tools/memory-tree/door_fixture.py each count 0. AC12 reads only spec 90, while S12 and S13 (108:89-96) rewrite 97 AC1 and 97 section 4. Nothing observes those edits, so S12 and S13 could be skipped and AC12 would still certify them. | sound | fixture-passes-by-finding-nothing |
| 5 | coherence | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC21 (against section 2 S9, S10, S21, S23) | high | high | confirmed | 108 AC21 (lines 302-303) checks spec 97's amendment only against unit 94 (`97 108 94`). The status headers give these orders: 92=31, 91=56, 90=65, 93=66, 94=67. 108 S21 (line 120) corrects 97 S20, and 97 S20 (97:120) governs how unit 92's pass files the ask row, so it must land before unit 92 builds at order 31. If 108 lands after unit 92 has built but before unit 94, AC21 still passes. Its red case says "a unit whose spec it corrects", which is not what it checks. Unit 92 is the earliest of 90 to 94, so `97 108 92`, or a loop over all of them, covers every case. | sound | - |
| 6 | coherence | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-98.md:section 4 Evidence (and 99, 100, 102, 103, 105, 106 section 4 Evidence) | low | low | confirmed | At HEAD, 95 AC2 is at line 142, but 98:116 and 100:58 cite spec-95.md:136-140. `grep -n '<BASE>'` prints 155 and 184 for spec 96, but 103:62 records 150 and 179. For spec 97 it prints 239 and 300, but 106:61 records 234 and 295. Commit 05ab0d1f8 edited specs 95, 96 and 97 (+10, +9, +9), which explains the offset. The effect is limited to citations. | sound | - |
| 7 | coherence | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 2 S21 (against TOOL-dWellOiledMachine-97 AC14) | low | low | confirmed | 97 AC14 (lines 297-298) already greps "SEV · TOOL-dPlacedRequest-<id> · HIGH · a second write_node_lock" and expects it to print 1. 108 S21 (lines 120-122) adds a second exactly-1 count of the same row to 97 AC12, and 108 AC19 counts the same row again. The duplication has no effect on behaviour, but the two copies can drift apart. | sound | two-answers-to-one-question |
| 8 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-103.md:section 6 AC1 (with section 2 S2; interacts with TOOL-dWellOiledMachine-104 section 4 The fixture) | high | medium | confirmed | I checked this by grep. In spec 103 the eval/sed load appears on line 36 (the S2 preamble text) and on line 101 (AC1, which says 'prints 1'). Spec 104 line 62 is the first line of its fenced fixture, and spec 104's S1 puts that fixture verbatim into spec 96 §4. Both status lines read order 68, and both S3/S4 route the rev bumps to the same M2 cross-read, before unit 103's pass. Spec 96 has the line 0 times today. On a correct build it will have it twice (preamble plus fixture), so AC1 goes red. The result is a false stop or deviation, not a wrong result, so I grade it medium. | sound | - |
| 9 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-106.md:section 6 AC1 (with section 2 S2; interacts with TOOL-dWellOiledMachine-107 section 4 The fixture) | high | medium | confirmed | Same pattern as id 8. Spec 106 S2 (line 36) adds the eval/sed load to spec 97's §6 preamble, and AC1 (line 103) requires the count to print 1. Spec 107 line 62 is the first line of its fixture, and spec 107's S1 places that fixture verbatim in spec 97 §4. Both specs are order 69 and both land at the M2 cross-read. Spec 97 has the line 0 times at base and will have it twice after both bumps, so AC1 is red on a correct build. I grade it medium. | sound | - |
| 10 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC12 (against section 2 S12) | high | medium | confirmed | I re-ran the probe at HEAD. The flattened AC20 slice of spec 90 reads '-- supervise.py door_fixture.py'. grep -c printed supervise.py 1, door_fixture.py 1, 'tools/\*\*' 0, and 0 for each full path. So spec 108's AC12 (lines 269-272) is already green at base. Because each full path contains its bare name, AC12 also stays green after the rewrite, so it can never tell whether the rewrite was made, which its own 'Red when' claims to catch. AC10 still catches a wholly skipped AC20 rewrite, which contains the damage, so I grade it medium. The fix greps the full paths, which print 0 today, so the check can now fail. | sound | - |
| 11 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC8 (against section 2 S8) | medium | medium | confirmed | Spec 108's AC8 (line 254) spells `git ls-files --error-unmatch supervise.py door_fixture.py`, while S8 (line 71) spells the full tools/ paths. I re-probed from the repo root: `git ls-files --error-unmatch lib-unattended.sh` returned rc=1, and the same command with tools/unattended/lib-unattended.sh returned rc=0. So bare names match only files at the root, and AC8 is red on a correct build. | sound | - |
| 12 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 2 S10 and section 4 Evidence (the walk), section 6 AC10 | medium | medium | confirmed | I ran S10's exact walk over a scratch file. It printed only the direct `subprocess.run(["bash","x"])` call (line 2). It printed nothing for `cmd = ["bash","y"]; subprocess.run(cmd)`, for `args=["bash","x"]` or for the walrus form. 90 AC20's current regex `\[\"bash\"\|\['bash'` matched all four lines. So the walk is narrower than the regex it replaces and narrower than S10's stated class ('any spawn whose argv's first element is the literal bash'), and §4 Evidence does not record that gap. | sound | - |
| 13 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC15, first clause (against section 2 S17) | medium | low | confirmed | At HEAD, spec 90's S1 bullet ends 'the README's build-order region is re-rendered', and the flattened bullet piped to grep -c re-render printed 1. So the first clause of spec 108's AC15 is already green at base and cannot observe S17's pointer to TOOL-dWellOiledMachine-93. Today the S1 bullet has TOOL-dWellOiledMachine-93 0 times, so the proposed token can fail. Only the wording of a spec cross-reference goes unobserved, so I grade it low. | sound | - |
| 14 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-98.md:section 5 perf / scale, and section 4 (the predicate's build_commit call) | medium | medium | confirmed | I read spec 98's predicate (lines 75-84). It runs build_commit over "$floor..HEAD" in a subshell, declares no _SUBJ and passes no cap, and §5 (line 150) gives no figure. lib-unattended.sh line 1226 checks for _SUBJ; without it, each commit costs a read_attribution_tokens call plus a git show. I timed build_commit over HEAD~20..HEAD (53 commits): real 0m11.5s, about 0.2 s per commit. Past landing merges in this repo (67a943daa, d2e071573) pull 26-28 main commits into the run branch, so the window grows with main's landings as well as the run's own commits. A full walk over a few hundred commits (AC3's 999 case, or late-built units) runs from one to several minutes, so a timeout is a real risk. I could not time the build-time window itself, because it does not exist yet. I grade it medium. | sound | - |
| 15 | grounding | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-98.md:section 4 Evidence in specs 98, 99, 100, 102, 103, 105 and 106 (line citations of specs 95, 96, 97); also 108 section 4 Evidence '96's lines 20 and 124' | low | low | confirmed | Spec 98 at line 116 cites `spec-95.md:136-140`, `spec-96.md:179-181` and `spec-97.md:295-297`. At HEAD, grep puts 95 AC2 at line 142, 96 AC5 at 184 and 97 AC15 at 300. `git show 0d8692025:` of spec 95 puts AC2 at 136. In spec 96, `<BASE>` is now at lines 155 and 184 and '274' at lines 21 and 129. So the cites were measured before the folds in 05ab0d1f8 and are off by a few lines. The only effect is on navigation. | sound | - |
| 16 | reuse | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 2 S10 (and AC10) | medium | medium | confirmed | 108 S10 (lines 75-82) spells the walk as any ast.Call whose args[0] is a List or Tuple opening with 'bash'. I ran that exact walk over a scratch file. It flagged `subprocess.run(g.resolve_shell_argv(["bash","y"]))`, which is the resolved form, and printed nothing for `subprocess.run(["bash","x.sh"]+extra)`. measure_legs.py:2680-2700 `test_no_bare_bash_argv` limits the match to `subprocess.<attr>` calls, unwraps BinOp and keeps `calls >= 3`. tools/run-gates/held_halves.py:129 uses the `["bash", ...] + list(...)` shape, and tools/govkit/matrix.py:911 uses the resolver form. So the check misses a real bare-bash shape and goes red on correct code. | sound | - |
| 17 | reuse | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-98.md:section 4 The predicate, line `a=$(git log --reverse --format='%H %s' ... \| grep -E ...)` and the bullet **A** | low | low | confirmed | Spec 98 at line 79 finds A with `git log --reverse --format='%H %s' ... \| grep -E`, which reads the subject only. At line 96, P comes from `build_commit`, which attributes by `Pass:` trailer or subject. lib-unattended.sh:1144-1155 `read_attribution_tokens` says a commit with a `Pass:` trailer is attributed by that trailer and not its subject, and that `Pass: none` names no unit. So A and P use two different attribution rules. Spec 98 has no Pass-trailer caveat; grep for `Pass:` hits only the build_commit description. The effect is contained, because S3's route puts the unit in the subject. | sound | - |
| 18 | reuse | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-101.md:section 10 Reuse audit (the same sentence in -104 §10 and -107 §10) | low | low | confirmed | §10 of 101 (lines 158-159), 104 (line 150) and 107 (lines 150-151) all say that no existing seam fits a history fixture. tools/memory-tree/routed_commits.py:385-415 `build_fixture` builds a scratch repository from an ordered commit list in one `git fast-import`, with messages, file edits and parents. That is a git-history fixture builder. The §10 text describes a selftest-tree builder (lib-selftest.sh), so the reuse record misses this seam. The fixtures hand-roll `git init` and `git commit` (101 lines 66-69). The effect is limited to scaffolding and a misleading record. | sound | - |
| 19 | reuse | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-107.md:section 4 The fixture (`loop()` line) vs section 10 | low | low | confirmed | 107 §10 says the predicate is loaded 'inside AC15's own loop'. But 107 §4's fixture defines its own `loop() { r=""; for n in 91 92 93 94; do check_amended_before_built $n 97 $n \|\| r="$r $n"; done; echo "[${r# }]"; }`. That is a re-spelling of the loop 106 S1 writes into 97 AC15 (`... \|\| echo $n; done`). AC15's text is never loaded or run, so a wrong unit list or argument order in AC15 would not turn AC16 red. The §10 claim is inaccurate. The effect is contained, because 106 AC1 separately greps AC15 for `check_amended_before_built $n 97 $n` and `91 92 93 94`. | sound | - |
| 20 | blast-radius | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-103.md:section 6 AC1, last clause (with TOOL-dWellOiledMachine-104 section 2 S1) | high | high | confirmed | 103 AC1 (lines 99-101) requires `grep -c "sed -n '/^check_amended_before_built() {/,/^}/p'" <spec 96>` to print 1. 103 S2 puts that string into 96's §6 preamble. 104 S1 (lines 29-30) puts 104 §4's fixture into spec 96 verbatim, and that fixture holds the same string: `grep -c` of it over spec 104 prints 1, and over spec 96 at HEAD it prints 0. Both edits land at the M2 cross-read, before 103's pass. So on a correct build the count is 2, AC1 reads red, and the run may 'fix' it by deleting correct text. 103 names 104 only as 'the staged red case' (line 48) and has no edge on the shared string. | sound | criterion-asserts-what-its-own-command-cannot-show |
| 21 | blast-radius | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-106.md:section 6 AC1, last clause (with TOOL-dWellOiledMachine-107 section 2 S1) | high | high | confirmed | 106 AC1 (lines 100-103) requires `grep -c "sed -n '/^check_amended_before_built() {/,/^}/p'" <spec 97>` to print 1. 106 S2 adds that span to 97's §6 preamble. 107 S1 (lines 29-30) adds 107 §4's fixture to spec 97 verbatim, and its first line is `eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' ...)"`. `grep -c` over spec 107 prints 1, and over spec 97 at HEAD it prints 0. On a correct build of both units the count is 2, so AC1 reads red. In spec 97, `## 6.` is at line 236 and AC1 at line 243, so the proposed preamble slice is well defined. | sound | criterion-asserts-what-its-own-command-cannot-show |
| 22 | blast-radius | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC12 (vs section 2 S12, S13 and §4 Evidence) | high | - | refuted | duplicate of id=27. Same defect: AC12 greps the bare names where S12 names the full paths. I re-ran the AC20 slice greps at HEAD and got supervise.py 1, door_fixture.py 1, tools/** 0, and 0 for each of the two full paths. | sound | criterion-asserts-what-its-own-command-cannot-show |
| 23 | blast-radius | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC8 (vs section 2 S8) | high | medium | confirmed | 108 S8 (lines 70-72) gives the full paths, but AC8 (line 254) runs `git ls-files --error-unmatch supervise.py door_fixture.py`. From the repo root that printed 'pathspec 'supervise.py' did not match' and the same for door_fixture.py, then exit 1. A bare pathspec at the root matches only a root-level file, so AC8 is red even after the files under tools/ are tracked. The full-path form also exits 1 at base, because 108 §4 says neither file is tracked yet. That is the intended red-before-build. The effect is contained: a falsely red criterion surfaces as a deviation and passes nothing wrong. | sound | criterion-asserts-what-its-own-command-cannot-show |
| 24 | blast-radius | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-100.md:section 4 Evidence (also 98 §4 Evidence, 103 §4 Evidence, 106 §4 Evidence) | low | low | confirmed | At HEAD, 95 AC2 is at line 142 and its <BASE> lines are 135/142/144. Spec 96's <BASE> lines are 155/184 and spec 97's are 239/300. The new specs still cite the old lines: 100:58 cites `spec-95.md:136-140`, 98:116 cites 136-140, 179-181 and 295-297, 103:62 cites 'lines 150 and 179', and 106:61 cites 'lines 234 and 295'. The effect is cosmetic: the citations point at the wrong lines. | sound | fold-text-is-unreviewed-surface |
| 25 | blast-radius | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 4 Files touched (vs section 8 F1) | low | low | confirmed | 108 §8 F1 (lines 321-324) resolves (a) 'as a surfaced park entry in the run-state file' at the M2 cross-read that lands S11. Files touched (lines 188-194) lists only specs 95, 96 and 97 and the README, so RUN.md is missing. The list is labelled an estimate, so the gap is cosmetic. | sound | - |
| 26 | failure-envelope | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-103.md:section 6 AC1 (and the same clause in spec 106 section 6 AC1) | high | medium | confirmed | 103:101 has AC1 require a whole-file `grep -c "sed -n '/^check_amended_before_built() {/,/^}/p'" <spec 96>` to print 1. 103 S2 (line 36) puts that loader into 96's §6 preamble. 104:62 is the first line of the fixture script, which 104 states 'S1 places in spec 96's §4', and it carries the same loader. On a built set the count is 2. 107:62 against 106:36 and 106:103 is the same case for spec 97. Both criteria are red on a correct build, and a builder could be pushed to drop the fixture's loader to make the count 1. | sound | - |
| 27 | failure-envelope | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC12 (against S12/S13) | blocker | blocker | confirmed | 108 S12 and S13 (lines 89-96) require the full paths and claim that AC12 tells a skipped rewrite from a made one. AC12 (lines 269-272) greps only the bare names. I re-ran the AC20 slice of spec 90 at HEAD: supervise.py 1, door_fixture.py 1, tools/** 0, and 0 for both full paths. So AC12 is green before the unit is built and accepts the exact red case it names. This is a check that certifies what it does not check. | sound | - |
| 28 | failure-envelope | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC8 (against S8) | high | - | refuted | duplicate of id=23. Same AC8 bare-pathspec defect. I re-ran it: exit 1 with 'pathspec did not match' for both names. | sound | - |
| 29 | failure-envelope | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 6 AC21 (against S10, S21, S22 and S23) | high | high | confirmed | Confirmed. 108 AC21 runs `check_amended_before_built 97 108 94` and nothing else for spec 97. Spec 97's amendments correct text that earlier units consume. 97 S20 and S21 rev-bump spec 92, whose status header reads order 31. 108 S10 rewrites 90 AC20 (spec 90 is order 65), and 97 S15 bumps spec 93 (order 66). Spec 98:75-82 shows the predicate takes any built unit as $3, so the check is bounded by unit 94 alone. A spec-97 bump that lands after unit 92's build commit but before unit 94's still exits 0, which breaks AC21's own 'Red when'. The path is narrow, because S23 routes every bump to M2 before the first code pass. Skipping M2 is the failure the criterion exists to catch, so on that path it certifies what it does not check. | sound | - |
| 30 | failure-envelope | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 2 S10 (and AC10) | medium | medium | confirmed | Confirmed. I wrote a scratch sup.py under scratchpad/verify-b with a variable-held argv, an `args=` keyword argv and a literal-list argv, then ran S10's exact walk over it. It printed only the literal-list line (line 4 of my file). The walk tests `n.args[0]` alone, so a Name argument and a keyword argv both escape it, and AC10's three staged cases are all literal positional lists or tuples. The two files are not written yet, so either shape would ship past 90 AC20 and 94 AC8. The fix is unsound as written. Its first option replaces the walk's `isinstance(n.args[0],(ast.List,ast.Tuple))` text, but 108 AC10 requires exactly that substring to count 1 over spec 90, so AC10 would go red. The fix does not adjust that grep. | unsound | - |
| 31 | failure-envelope | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-101.md:section 4 The fixture (same in spec 104 section 4 and spec 107 section 4); section 5 risks | medium | medium | confirmed | Confirmed. 101:66, 104:64 and 107:64 each build the fixture at a fixed path, `$(cygpath -u "$TEMP")/abb95` (abb96 and abb97 in the other two), with `rm -rf "$fx"` before `git init`, and 101:80 removes it at the end. Two overlapping runs on one machine share that repository. Parallel skeptics, like this fan-out, or two worktrees would delete and re-init it mid-run, so commits interleave and the before/after/unbuilt lines can come out falsely red or falsely green. Section 5 risks (101:116, 104:109, 107:112) name only cygpath, and nothing in the specs addresses concurrency. The effect is contained to a criterion's fixture output. | sound | - |
| 32 | failure-envelope | memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md:section 2 S11 and S13 (Observed by AC11 / AC12) | medium | low | confirmed | Confirmed. S11 (108:83-88) puts two edits in spec 93: `tools/memory-tree/README.md` in Files touched, and `kit/dogfood doc parity` on the section 7 leg line. It says 'Observed by AC11', but AC11 (108:265-268) greps only the kit README and the `__doc__`. On re-probe both of the fix's awk counts print 0 over spec 93 today, so the edits are not made yet and nothing observes them. S13's spec 97 section 4 Evidence line is likewise claimed by AC12, which reads only spec 90's AC20 slice. The consequence is a skipped spec-text edit that goes unflagged, plus a missing guard leg at unit 93's pass. The merge bar still runs its legs, so this is graded low. | sound | observed-by-claim-no-arm-discharges |
