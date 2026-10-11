**Serves:** diff-review TOOL-dHomedResolver-1 TOOL-dHomedResolver-2 TOOL-dHomedResolver-3

# dHomedResolver — Tier-2 closing diff review, round 1

*Node `d`, 2026-10-09. This is an adversarial pass over the whole diff of the three-unit build. A
primed fan of five finder lenses ran first, then a skeptic stage prompted to REFUTE each finding,
then one synthesis. The skeptics reproduced the load-bearing claims by mutation in a scratchpad copy
of the kit. The synthesis re-read the cited lines at HEAD `04b0b2395` before writing them down here.*

**Range reviewed: `b39dff78aae970c8428289aa781cf21f79c6fbff...04b0b2395dd1cc3cc70554fca2acb9046a75505c`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No blocker and no high. The two units' shipped behaviour is correct at HEAD: check 10 and check 24
resolve one declared home, and the archive guard runs first in both `cmd_check` and `cmd_write`. Seven
confirmed findings merge into four items, two medium and two low. Both mediums are real and contained.
The first is that `--new-build` writes and stages two files before the new refusal fires, and then
says nothing was written. The second is that the self-test arm certifying "nothing was written" cannot
fail. Both should be fixed before landing, because the second is the guard's only ordering witness and
the first is the path where that ordering is actually wrong.

## Review shape

Intensity full. Raw 8, confirmed 7, refuted 1, unverified 0 (0 uncertain), precision 0.88.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| seams | yes | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 blocker, 0 high, 2 medium, 2 low. By raw confirmed finding: 0 blocker,
0 high, 5 medium, 2 low. The difference comes from duplicates. Three lenses independently reached the
vacuous arm (ids 1, 4 and 5), and two reached the `--new-build` ordering (ids 3 and 7).

**Run integrity.** All 5 of 5 lenses returned and none died. All 4 of 4 skeptic batches returned and
none died. No contradictory verdict was demoted to unverified, no spurious verdict was discarded, and
no duplicate was dropped at the verdict stage. Of the fixes on confirmed findings, 7 were judged sound,
0 unsound, 0 had none proposed and 0 were not judged. On severity, 0 confirmed findings went ungraded
by the skeptic and 1 was re-graded (id 1, high to medium). No unverified finding was answered
UNCERTAIN, and none lacked a usable verdict. No lens notes were supplied, so every lens ran on the
kit's generic brief. Intent was read from 4 spec documents beside the range's commit messages. The
checklist held 22 items, each assigned to exactly one lens: security 5, correctness 5, seams 4,
verification 4, intent 4. By-design items came from the caller's list. Since no lens or batch died,
the seams lens's zero is a returned zero and not a gap from a dead agent. It is still only one lens's
search, not proof that no seam defect exists.

## Findings

### M1 — `--new-build` writes and stages before the refusal, which then says "Nothing was written" (ids 3, 7) — MEDIUM

- **Where:** `tools/memory-tree/gen_build_index.py:2497` (the guard's only write-path call site, at the
  top of `cmd_write`), reached from `cmd_new_build` at `:3478-3481`; the refusal text is at `:2306-2316`.
- **What:** `cmd_new_build` calls `write_text` on the new README, runs `add_contract_row`, and runs
  `git add` on both. Only then does it `return cmd_write(root, conf)`, whose first line is
  `check_archives_tracked`. Take a tree with an untracked file under `<MEMORY_ROOT>/archive/` and run
  `--new-build <slug>`. The command leaves a staged README with unrendered regions and a staged BOUND
  row, then raises a Problem ending "Nothing was written." The message says to stage the archive and
  re-run. A re-run of `--new-build` is then refused by `check_slug_claimed`, because its `git grep`
  finds the slug in the staged README, so the stated remedy is a dead end. This breaks spec 2's S2
  promise that a refused write writes nothing, and it breaks `cmd_new_build`'s own docstring ordering.
  A secondary gap is that `collect()` and the readiness grading have already run over the half-staged
  corpus by that point.
- **Impact:** contained to one operator command. Recovery is manual: stage the archive and run
  `--write`, or unstage and delete the two files. The diff introduced both the guard and its
  "Nothing was written" text, so the diff made this path reachable.
- **Fix (judged SOUND by the skeptic):** call `check_archives_tracked(root, conf)` at the top of
  `cmd_new_build`, before `check_slug_claimed` and before any `write_text`, `add_contract_row` or
  `git add`.
- **Left-shift gate:** a self-test arm that runs `cmd_new_build` over a fixture with an untracked
  archive and asserts two things. It must refuse with the remedy text, and afterwards no README exists
  at the slug's path and the contract registry holds no row for it. Confirm the arm reds against HEAD
  as it stands before the fix lands. For the class, consider a structural arm asserting that every
  verb that can reach a `write_text` calls the guard before its first write.

### M2 — the arm "a refused --write wrote nothing" cannot fail (ids 1, 4, 5) — MEDIUM

- **Where:** `tools/memory-tree/gen_build_index.py:3808`, with the half-staged fixture at `:3790-3808`.
- **What:** the fixture renders the tree, commits it, and then only ADDS an untracked archive. Every
  artifact derives from `git ls-files`, so an unguarded render over that state is byte-identical, and
  `read_text(readme_h) == before_h` is True whether or not the guard ran first. Three skeptics each
  reproduced this independently in the scratchpad. In the first, the guard was moved below the
  `write_text` loop in `cmd_write`: all five TOOL-dHomedResolver-2 arms printed `arm ok`, this one
  included. In the second, the guard was a no-op: `cmd_write` returned rc 0, made 4 `write_text` calls,
  and the README still compared equal. The third was a mutation on a `git archive` copy of
  `04b0b2395`, with the same result. The fixture also never reproduces the incident it cites, where a
  moved row vanishes from a tracked live document. Its id `ARCH-tOne-1` lives in a spec H1, not in a
  DECISIONS row.
- **Impact:** the guard's ordering property, which is that nothing is written before the refusal, has
  no witness that can go red. A later refactor that moves the guard below `plan()` or the write loop
  would land green and bring back the seventeen-README rewrite this unit closes. The shipped placement
  is correct today, so the reach is a future regression. That is why the skeptic re-graded id 1 from
  high to medium and the other two were graded medium. This synthesis agrees with the binding grade:
  under the rubric, "a check that certifies what it does not check" would be a blocker if the
  certified property were false on a reachable path, and at HEAD it is true.
- **Fix (judged SOUND by the skeptic, all three):** make the fixture a real half-staged move. Delete a
  row whose id a build README cites from its tracked live document and stage that deletion before
  writing the untracked archive, so that an unguarded render WOULD change the README ids or `LIVE.md`.
  Then assert that both are unchanged after the refused `--write`. Alternatively, wrap the writer and
  assert zero `write_text` calls during the refused `cmd_write`. Either way, observe the arm RED with
  the guard moved below the write loop, then restore the guard. §7 requires this before the arm counts
  as landed.
- **Left-shift gate:** this is the `fixture-passes-by-finding-nothing` class. Pair every "nothing
  changed" arm with a staged mutant that would change something, and record the RED observation beside
  the arm. A cheap generic form is a write-counting shim, which the M1 arm can share.

### L1 — the refusal's `git add` remedy pastes raw, unquoted filenames (id 2) — LOW

- **Where:** `tools/memory-tree/gen_build_index.py:2315` (listing at `:2307-2308`).
- **What:** the guard runs `git ls-files --others` without `-z`, splits on newlines, and space-joins
  the result into `git add ...`. A path containing a space splits into two arguments. Under
  `core.quotePath`, a non-ASCII or control-character name is C-quoted, so the remedy names a path that
  does not exist. Shell metacharacters are printed verbatim inside a command a reader is invited to
  paste. Nothing executes them, and the input is the operator's own working-tree filenames. Rotation
  names its archives `<stem>.<date>.md`, so the path is narrow.
- **Impact:** wrong remedy text only. The refusal and its exit code are still correct.
- **Fix (judged SOUND by the skeptic):** list with `git ls-files -z --others --exclude-standard`, split
  on NUL, and build the remedy with `' '.join(shlex.quote(p) for p in untracked)`. Alternatively,
  print the remedy as `git add -- <MEMORY_ROOT>/archive/`, which needs no per-file quoting at all.
- **Left-shift gate:** a self-test arm with an untracked archive named with a space, asserting that
  the printed remedy holds the quoted path as one argument.

### L2 — S items claim "Observed by" an AC that does not read them (id 8) — LOW

- **Where:** `memory/builds/dHomedResolver/spec/2026-10-09-spec-TOOL-dHomedResolver-2.md:36`, and the
  same pattern in spec 1.
- **What:** spec 2's S4, the guard header's "what it does NOT check" paragraph, cites AC5. AC5 only
  greps for `check_archives_tracked` and its call sites, and for "untracked" in `HYGIENE.md`. Spec 1's
  S2 ("the header says so") cites AC3, which is a fixture-output arm. Spec 1's S6 lists the
  memory-tree README upgrade note but cites AC7, whose grep covers `HYGIENE.md`, the template and the
  dossier and not the README. The properties do exist in the tree. The docstring carries
  "WHAT THIS DOES NOT CHECK", check 10's header states that a declared home is one path, and the README
  carries the "Upgrading past 2.137" note. Only the traceability claim is wrong.
- **Impact:** no effect on behaviour. Deleting any of those three prose items would leave every arm
  green while the ledgers still record them as observed. This is the
  `observed-by-claim-no-arm-discharges` class.
- **Fix (judged SOUND by the skeptic):** point each S item at an AC that actually reads it. For
  example, extend AC5 to grep the docstring for `WHAT THIS DOES NOT CHECK`, and extend AC7 to assert
  that `tools/memory-tree/README.md` carries "declared home". Otherwise, mark the items as unobserved
  prose claims instead of "Observed by".
- **Left-shift gate:** a spec-lint leg that, for each `Observed by ACn` claim, checks that the S item's
  named file path or quoted literal appears in ACn's text. That is structural only, and its header
  should say so.

## Refuted

- **id 6** (verification, `tools/memory-tree/row_grammar.py:896`, finder graded low): it claimed check
  24's missing-home branch has no dedicated row-grammar arm. Refuted as PRE-EXISTING. At the base, the
  equivalent branch (`row_grammar.py:875`) had no arm either, and the only hygiene-suite assertion
  (`test.sh:2118`) was check 10's text, as `test.sh:2120` is now. The diff rewrote the predicate and the
  message but removed no coverage. The finder also conceded that deleting the branch would crash on
  `idx[0]` rather than skip silently. It is not counted here. The gap is real but older than this
  build, so it belongs in a straggler ask and not in this verdict.

review-shape kind=diff-review round=1 intensity=full at=synth raw=8 confirmed=7 refuted=1 unverified=0 blocker=0 high=0 medium=5 low=2 agents=10 out-tokens=99085

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/memory-tree/gen_build_index.py:3808 | high | medium | confirmed | Reproduced. In a scratchpad copy of tools/memory-tree/ I moved check_archives_tracked in cmd_write (gen_build_index.py:2497) to after the write_text loop and ran --selftest. All five TOOL-dHomedResolver-2 arms printed 'arm ok', including 'a refused --write wrote nothing' (line 3808). The fixture renders and commits the tree first. Its only change is an untracked archive, and git ls-files never sees that file, so an unguarded render produces byte-identical README text and the comparison cannot fail. The arm's own comment says the tree is committed first 'so the only thing the arms below can be reacting to is the untracked archive'. That is exactly why the arm is vacuous. The shipped code is correct today, because the guard runs first in both verbs. The defect is limited to a future reorder that would land green with no warning, so I graded it medium rather than high. | sound | fixture-passes-by-finding-nothing |
| 2 | security | tools/memory-tree/gen_build_index.py:2315 | low | low | confirmed | gen_build_index.py:2309-2316 lists the files with `git ls-files --others` (no -z), splits on newlines and space-joins them into `git add ...`. git does not quote a path containing a space, so the printed remedy splits it into two arguments. Under core.quotePath a non-ASCII or control-character name is C-quoted, so the remedy names a path that does not exist. Shell metacharacters are printed verbatim, but nothing executes them. The input is the user's own working-tree filenames, and rotation names its archives <stem>.<date>.md, so the path is narrow. The effect is wrong remedy text only: the refusal and its exit code are still correct. | sound | - |
| 3 | correctness | tools/memory-tree/gen_build_index.py:2497 | medium | medium | confirmed | Read gen_build_index.py:3429-3481. cmd_new_build writes the README (write_text), adds the BOUND row (add_contract_row), runs git add on both, and only then returns cmd_write(root, conf), whose first line (2497) is the new check_archives_tracked. With an untracked file under memory/archive/, the Problem raised says 'Nothing was written' while two files are written and staged. A re-run hits check_slug_claimed first, whose `git grep -I -l --fixed-strings` searches index-tracked files, so the staged README names the slug and the re-run is refused. The guard is new in this diff, so the diff made this path reachable. The effect is contained to one operator command with a manual recovery, so medium. | sound | - |
| 4 | correctness | tools/memory-tree/gen_build_index.py:3808 | medium | medium | confirmed | Reproduced in scratch. Built the same fixture (_fixture, cmd_write, git add -A, commit), added the untracked archive, replaced check_archives_tracked with a no-op and wrapped write_text. cmd_write returned rc 0, made 4 write_text calls, and the README compared equal to before_h. So the arm at 3808 'a refused --write wrote nothing' passes whether or not the write precedes the refusal. The guard moved below the write loop would keep all three --write arms green. The refusal itself is still covered by the two text arms, and the current code checks before it writes, so the gap only reaches a future regression. That makes it medium. | sound | - |
| 5 | verification | tools/memory-tree/gen_build_index.py:3808 | medium | medium | confirmed | Reproduced. The halfstaged fixture (gen_build_index.py:3790-3808) renders and commits the tree, then only ADDS an untracked archive. Nothing is deleted from a tracked document, and the fixture's id ARCH-tOne-1 lives in a spec H1, not in a DECISIONS row. Since every artifact derives from git ls-files, an unguarded render is byte-identical, so the before/after compare is True either way. Mutation run in the scratchpad on a git-archive copy of 04b0b2395: I removed check_archives_tracked from the top of cmd_write and re-inserted it after the write loop. All five TOOL-dHomedResolver-2 arms still printed 'arm ok', including 'a refused --write wrote nothing'. The refusal-text arms pass because the guard still raises after the writes. The arm therefore cannot detect the ordering regression it exists for. Graded medium, not higher, because the shipped guard is correctly placed today; the defect is a regression arm that cannot fail. | sound | - |
| 6 | verification | tools/memory-tree/row_grammar.py:896 | low | - | refuted | The gap is PRE-EXISTING. At base b39dff78a, check 24's equivalent branch (row_grammar.py:875, 'resolves to N live index(es)') had no dedicated row-grammar arm either. The only hygiene-suite assertion at base (test.sh:2118, 'resolves to 0 live index(es)') was check 10's text, just as the head's test.sh:2120 is now. The diff rewrote the predicate and message, but it removed no coverage. The missing arm for check 24's missing-home branch is the same gap as before. The remaining effect is an unasserted message string, which is cosmetic. The finder also concedes that deleting the branch would crash on idx[0], so a silent skip is not the only failure mode. | sound | - |
| 7 | intent | tools/memory-tree/gen_build_index.py:2306 | medium | medium | confirmed | Read gen_build_index.py: cmd_new_build (3429-3481) runs write_text on the README, add_contract_row, and `git add` on both, then returns cmd_write(root, conf). check_archives_tracked is called only at the top of cmd_check (2320) and cmd_write (2497), so on --new-build it raises after the files are written and staged. Its message still says 'Nothing was written' and 're-run'. A re-run of --new-build then hits check_slug_claimed's git grep probe, because the staged README is tracked and names the slug. The diff introduced both the refusal and its 'Nothing was written' text, and spec 2 S2 promises that a refused write writes nothing. The effect is contained: the owner can stage the archive and run --write to fill the regions. But the stated remedy fails, and the half-made build is not mentioned. There is a second gap: at the guard's current position, collect() and the readiness grading already ran over the half-staged corpus. | sound | - |
| 8 | intent | memory/builds/dHomedResolver/spec/2026-10-09-spec-TOOL-dHomedResolver-2.md:36 | low | low | confirmed | The claims check out against the specs. Spec 2 S4 (the guard's NOT-checked header) cites AC5, and AC5 only greps for check_archives_tracked and for 'untracked' in HYGIENE.md. Spec 1 S2's 'the header says so' cites AC3, a fixture-output arm. Spec 1 S6 lists the memory-tree README upgrade note but cites AC7, whose grep covers HYGIENE.md, the template and the dossier, and not the README. The properties do exist in the tree: the docstring has 'WHAT THIS DOES NOT CHECK', check 10's header states 'a declared home is one path', and the README has the 'Upgrading past 2.137' note. So the only defect is the traceability claim in the new spec records, which has no effect on behaviour. Low. | sound | observed-by-claim-no-arm-discharges |
