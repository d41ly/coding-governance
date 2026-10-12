**Serves:** diff-review TOOL-cListedCensus-1

# Implementation diff review, round 1: cListedCensus unit 1, ps-hygiene grades the tracked .ps1 files instead of walking the disk

Node `c` · 2026-10-13 · Tier-2 · on `branch/unruffled-roentgen-9f0c5c` · run through `tools/workflows/tier2-review.js` at intensity light (3 finder lenses, then 4 skeptic batches, then this synthesis). The range is two commits. `3428b802a` opens the build with its spec and brief. `65418bcc3` replaces `scan()`'s `rglob('*.ps1')` walk and its `SKIP_DIRS` prune with `git ls-files -z -- '*.ps1'`, adds an exit-2 refusal for a dead listing and another for an empty one, adds four scratch-repo selftest arms, and syncs the kit README, the root README kit line, the gate-lint dossier, a new class record and the generated indexes.

**Reviewed range:** `6e8f8b1da4dc036b7fce23555b78fb4b5db0e60c...65418bcc33652ce8401f0af1cfc28eb3c9780036`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker. The HIGH item is the failure this gate exists to prevent. The new pathspec `*.ps1` is case-sensitive on Windows even under `core.ignorecase=true`. A tracked `Deploy.PS1` that BASE's walk graded is therefore dropped, and the scanner prints `OK` over the wrong population (ids 1 and 6). I reproduced it. Fix it before this unit lands, with a selftest arm that reds on the current pathspec. The MEDIUM item is the adopter wiring runbook: it still promises a clean report for a repo with no `.ps1`, and that repo now refuses with exit 2 (id 12). Id 8 is the same sentence at its binding LOW grade. The other LOW items are a header exit-code line, a class record that names an unrun selftest as its gate, duplicate listing during a conflicted merge, an uncaught decode error, two missing selftest assertions, and spec "Observed by" claims that no AC discharges. This was a light review. The security and intent lenses did not run, so this verdict covers what three lenses and the checklist could see, and it is not a full review.

## Review shape

Intensity **light** · raw **16** · confirmed **13** · refuted **3** · unverified **0** (0 uncertain) · precision **0.81**.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 5 | 3 | 2 | 0 | 0 | 0.60 |
| seams | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| verification | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

Precision is above the 0.5 floor. I merged the 13 confirmed findings into **10 items** while writing, and each merge joins findings of one binding grade only:

- Ids 1 and 6 are one case-sensitivity defect, seen by correctness and by seams.
- Ids 9 and 16 are the same header line.
- Ids 7 and 13 are the same `## Gated by` section.

Ids 8 and 12 flag the same runbook sentence but carry different binding grades (LOW and MEDIUM), so they stay separate items. One edit closes both.

Adjudicated, by item: **0 BLOCKER · 1 HIGH · 1 MEDIUM · 8 LOW** (10 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 2 HIGH · 1 MEDIUM · 10 LOW** (13 findings).

Every id keeps its binding grade, and I re-grade none. Two skeptics graded the same runbook sentence differently, MEDIUM for id 12 and LOW for id 8. Either grade is defensible: the sentence's advice to drop the kit still holds, and the failure it now mis-states is a loud refusal.

The three refuted findings (ids 2, 5 and 11) are listed with their reasons in the appendix and are not re-adjudicated here.

## Run integrity

- Lenses **3/3** returned, **0 DIED**.
- Skeptic batches **4/4** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates.
- Fixes on confirmed findings: **11** judged sound, **2** judged UNSOUND (ids 13 and 14), **0** none proposed, **0** NOT JUDGED.
- Severity on confirmed findings: **0** ungraded by the skeptic, **4** re-graded by the skeptic (ids 7, 8, 13 and 14, each from medium to low).
- Unverified findings: **0** answered UNCERTAIN by a skeptic, **0** with no usable verdict.
- Intensity **light**: the security and intent lenses were NOT run. Their classes were swept only through the checklist shares, so this run is not a full review.
- Lens notes supplied for: correctness, seams, verification.
- Intent: 2 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 18 items, each assigned to exactly one of 3 lenses (correctness 6, seams 6, verification 6).
- By design: the caller's byDesign list.

Every scheduled stage returned, and every counter that could mark a hole is zero. A zero in this report is evidence of absence only for the three lenses that ran. It says nothing about the security or intent classes beyond their checklist shares.

What this synthesis checked itself, at the worktree HEAD `65418bcc3` (git 2.55.0.windows.1):

- **Ids 1 and 6.** I built a scratch repository with `core.ignorecase=true`, a clean `a.ps1`, and a BOM-less em dash in `Tools/B.PS1`, and tracked both. `git ls-files -z -- '*.ps1'` lists only `a.ps1`. `:(glob,icase)**/*.ps1` lists both. `ps-hygiene.py .` prints `OK — 1 tracked .ps1 file(s) clean` and exits 0.
- **Lines read in `tools/gate-lint/ps-hygiene.py`.** `:140-141` is a strict `encoding="utf-8"` listing. `:147` iterates with no dedup. `:149` is the skip. `:216-221` checks main's exit code alone. `:5` is the exit-code line.
- **Other files read.** `WIRE-INTO-PROJECT.md:136-138`, the class record's `:30-46`, and spec lines `:22-45` and `:66-69`. Each matches its finding's premise.
- **Siblings outside this range.** These bear only on H1's left-shift and are not findings of this review. `tools/gate-lint/sh_hygiene.py:342` lists with `["git", "ls-files", "-z", "*.sh"]`, which is the same case-sensitive shape. `encoding_posture.py:144` filters with a case-sensitive `.endswith(".py")`. The new class record (`:32-34`) cites both files as the model to copy.

The remaining findings rest on the finders' and skeptics' verification and were not re-executed here.

## HIGH

### H1. The `*.ps1` pathspec is case-sensitive under `core.ignorecase`, so a tracked `.PS1` drops out and the scanner certifies `OK` over the wrong population (ids 1, 6)

- **Where:** `tools/gate-lint/ps-hygiene.py:140`. The class record `memory/gotchas/a-gate-that-walks-the-repo-root-reads-other-worktrees.md:32-34` recommends the same pathspec as the fix for the whole class.
- **Defect:** a git pathspec glob matches case-sensitively even when `core.ignorecase=true`. BASE's `root.rglob("*.ps1")` matched case-insensitively on Windows, so on the Windows nodes where gov and nc run it graded a tracked `Deploy.PS1`. The new listing does not grade it. Separately, an inherited `GIT_GLOB_PATHSPECS=1` stops `*` at `/`, which leaves only top-level files in the population. That sub-claim reproduces (3632 drops to 5 on `*.md`), but nobody realistically exports the variable.
- **Impact:** this is a false green that BASE did not have. If any lowercase `.ps1` is also tracked, main prints `OK — N tracked .ps1 file(s) clean` and exits 0, while PowerShell 5.1, the host the BOM class targets, still runs the `.PS1`. The kit README, the dossier and the class record all say "every tracked .ps1". The path is narrow: it needs an upper- or mixed-case extension on a Windows host. That narrowness is why the grade is HIGH and not BLOCKER.
- **Fix** (both finders' fixes judged SOUND by the skeptics):
  - Id 1's fix lists with `["git", "ls-files", "-z", "--", ":(glob,icase)**/*.ps1"]`. It was verified to return the full nested, case-insensitive set with and without `GIT_GLOB_PATHSPECS=1`. Under `GIT_LITERAL_PATHSPECS` it still produces the exit-2 refusal rather than a pass.
  - Id 6's fix uses `:(icase)*.ps1`. Its alternative runs `git ls-files -z` with no pathspec and keeps the entries where `rel.lower().endswith(".ps1")`.
  - I prefer the no-pathspec listing with the suffix filter. It is the shape `encoding_posture.py` already uses, and no `GIT_*_PATHSPECS` variable can narrow it. A bare `:(icase)*.ps1` still narrows under `GIT_GLOB_PATHSPECS=1`.
  - Whichever form you take, add a selftest arm that tracks a BOM-less `sub/B.PS1` and requires exit 1, and observe it red against the current pathspec first.
  - Change the class record's "The fix" paragraph so it names a case-insensitive listing, not `git ls-files -z -- '<glob>'`.
- **Left-shift:** the new arm is the instance's check. No leg runs `--selftest` (see L2), so it guards only when someone runs it by hand, until a ps-hygiene leg is wired. The class is a population query narrower than the walk it replaced. Candidate predicate: an `ls-files` argv under `tools/` whose pathspec is a bare `*.<ext>` glob with no `icase` magic. Run it over the real tree first. It would also hit `sh_hygiene.py:342`, and that hit decides whether `.sh` shares the consequence. If no gate fits, add a bug-class checklist entry: "converting a walk to a listing owes a parity check of the two populations on a case-insensitive host".

## MEDIUM

### M1. The wiring runbook still promises a clean report for a repo with no `.ps1`, and that repo now refuses with exit 2 (id 12)

- **Where:** `WIRE-INTO-PROJECT.md:136-138`.
- **Defect:** the bullet says a repo with no `.ps1` "gets a clean report that proves nothing". That was true at BASE, which printed `OK — 0` and exited 0. After this diff, main exits 2 with the `graded NOTHING` refusal. The runbook names the kit as `gate-lint/` and never says `ps-hygiene`, which is why the update missed it when it changed every place that names the scanner.
- **Impact:** an adopter gets two answers. The kit README and the dossier say exit-2 refusal, and the runbook that agents follow when wiring a target says clean report. An agent that keeps the kit and wires `ps-hygiene.py . || exit 1` gets a red the runbook said would not happen. The effect is contained: the advice to drop the kit when there is no `.ps1` still holds, and the red is loud, not a false green.
- **Fix** (judged SOUND): rewrite lines 136-138 to say that a repo with no tracked `.ps1` gets a refusal (exit 2, `graded NOTHING`), not a clean report, and that this is why the kit is adopted only where the language exists. Add the file to spec S4's doc list and to its Readers inventory. The same edit closes L3.
- **Left-shift:** add a bug-class checklist entry: "a changed exit code or verdict owes a grep of every doc that names the kit, by its directory (`gate-lint/`) as well as by the tool's name". The miss happened because the grep was done by the tool's name only.

## LOW

### L1. The header's exit-code line leaves out the empty-population refusal (ids 9, 16)

- **Where:** `tools/gate-lint/ps-hygiene.py:5`.
- **Defect:** the line names exit 2 for "usage error or a population that could not be derived". The code uses that phrase only for the git failure. Main (`:260-263`) also exits 2 when `scanned == 0`, which is a population that was derived and is empty. The kit README treats that as a separate cause.
- **Impact:** a reader of the header alone would expect a repo that tracks no `.ps1` to exit 0. The same docstring at `:34-35` and the runtime stderr line both state the refusal, so nobody is actually misdirected. This is a comment-level defect.
- **Fix** (both judged SOUND): change the line to "Exit 0 clean, 1 on findings, 2 on a refusal: usage error, a failed `git ls-files`, or no tracked .ps1 at all." Id 9's wording is equivalent.
- **Left-shift:** add a checklist entry: "a header's exit-code line enumerates every exit-2 cause main has".

### L2. The class record names `ps-hygiene.py --selftest` as the gate and never says that no leg runs it (ids 7, 13)

- **Where:** `memory/gotchas/a-gate-that-walks-the-repo-root-reads-other-worktrees.md:43-46`.
- **Defect:** `## Gated by` names the selftest as the instance's gate. Every other selftest the gotcha records name is a declared `[[gate_leg]]`. `tools/gate-lint/kit.toml` declares only the three sh_hygiene legs, so no leg runs this selftest, held or otherwise, and `GATE_SELFTESTS=1` does not reach it. Spec §7 and the dossier both say so. Sibling records state an unwired guard outright.
- **Impact:** `gotchas.py --for-paths tools/gate-lint/ps-hygiene.py` hands this record to the next editor of the scanner. That editor can assume the bar catches a revert to a walk, and it does not. The effect stays in documentation: the sentence is accurate about what the selftest does, and the dossier that claims the record states the gap.
- **Fix:** id 7's fix was judged SOUND. Id 13's finder fix was REJECTED, and the skeptic's corrected fix supersedes both. Replace the instance sentence with: "The instance has a check and no gate: `ps-hygiene.py --selftest` stages a BOM-less copy untracked under a nested worktree path and asserts it is not graded, with the same bytes staged as the red control. No leg runs it, held or otherwise, because the kit declares no ps-hygiene leg and wiring one is a later unit. Run it by hand after editing the scanner."
- **Left-shift:** a candidate memory-hygiene predicate. When a record's `## Gated by` names a `--selftest`, either some `kit.toml` leg command must invoke that selftest or the section must say no leg runs it. Run it over `memory/gotchas/` first.

### L3. The runbook's stale sentence, flagged a second time at its binding LOW (id 8)

- **Where:** `WIRE-INTO-PROJECT.md:137`.
- **Defect and impact:** the same as M1. The skeptic graded this flag LOW, because only the bullet's stated rationale is stale and its advice still holds.
- **Fix** (judged SOUND): edit the bullet to say that a repo with no tracked `.ps1` gets the scanner's refusal (exit 2), not a clean report, which is why the PowerShell line is dropped there. List `WIRE-INTO-PROJECT.md` in S4's docs. M1's edit discharges this item.
- **Left-shift:** M1's checklist entry.

### L4. An unmerged `.ps1` is listed once per stage, so a conflicted merge grades and counts it 2-3 times (id 3)

- **Where:** `tools/gate-lint/ps-hygiene.py:147`.
- **Defect:** without `--deduplicate`, `git ls-files` lists an unmerged path once per stage, and `scan()` iterates the listing with no dedup. BASE's walk could not produce duplicates.
- **Impact:** the verdict does not change, because the same file gets the same grade each time. The report line overstates the tracked count and repeats each finding of the conflicted file.
- **Fix** (judged SOUND): iterate `sorted(set(p for p in listing.stdout.split("\0") if p))`, or pass `--deduplicate` (needs git >= 2.31).
- **Left-shift:** a selftest arm that leaves the scratch repo with a conflicted `a.ps1` and asserts `scan(tree)[1] == 1`.

### L5. A non-UTF-8 listing raises `UnicodeDecodeError`, which main's `except OSError` misses (id 4)

- **Where:** `tools/gate-lint/ps-hygiene.py:141`, caught at `:257`.
- **Defect:** the listing decodes with strict `encoding="utf-8"`. Two inputs break it: on POSIX, a tracked `.ps1` whose name is not UTF-8, and a git stderr localized in a non-UTF-8 locale. Either raises `UnicodeDecodeError`, which is a `ValueError`, not an `OSError`.
- **Impact:** the run dies with a traceback and exit 1, the code the contract reserves for findings, instead of the exit-2 refusal. The other files go ungraded. It is never a false green.
- **Fix** (judged SOUND): catch `ValueError` beside `OSError` in main and return 2. That branch is sound on its own. Alternatively pass `errors="surrogateescape"`. That alone cures the listing crash, but a finding in such a file would then crash at print time, which still exits 1.
- **Left-shift:** a checklist entry: "a scanner that gains a subprocess call routes that call's decode failures to the refusal exit".

### L6. No selftest arm reaches the missing-on-disk skip, and the spec gives the wrong reason for it (id 14)

- **Where:** `tools/gate-lint/ps-hygiene.py:149`, and spec §4 at `memory/builds/cListedCensus/spec/2026-10-12-spec-TOOL-cListedCensus-1.md:68-69`.
- **Defect:** every fixture path the index lists is on disk. Two breaks pass all four arms:
  - Counting before the skip, or `scanned = len(paths)`.
  - Dropping `-z` and splitting on newlines, which quotes a non-ASCII name so it fails `is_file`. Every fixture name is ASCII, so the arms never see the quoting.
  
  The spec says the skip drops "a deletion staged in the index". A staged deletion is never listed. What the skip actually drops is unstaged deletions and skip-worktree entries.
- **Impact:** the shipped code is correct and mirrors `sh_hygiene.scan_tree`. The cost is a missing red arm for a future regression, and a wrong rationale in a build record.
- **Fix:** the finder's fix was REJECTED, and this is the skeptic's corrected fix.
  - **Missing-on-disk arm:** put it in the empty-repo stage, right after `git init` and before `a.ps1` is staged. Write a clean `b.ps1`, `git add` it, then delete it from disk. Assert `scan(tree)[1] == 0`, and that main exits 2 with `graded NOTHING` in its output. Afterwards run `git rm --cached b.ps1` or leave the entry; either way arm 3's count of 1 still holds.
  - **Non-ASCII-name arm:** put it after the control arm. Write BOM-less non-ASCII bytes to a file with a non-ASCII character in its name (for example `ü.ps1`), `git add -f` it, and assert main exits 1 and the output names that file. A name with only spaces will not do, because git does not quote spaces.
  - **Spec §4:** change the sentence to say the skip drops tracked paths that are absent from disk (unstaged deletions and skip-worktree entries), not staged deletions.
- **Left-shift:** the two corrected arms are the gate. Observe each red under its break before calling it one.

### L7. The not-a-repo arm checks main's exit code and never its reason (id 15)

- **Where:** `tools/gate-lint/ps-hygiene.py:219-221`. The comment at `:215` promises that each refusal is asserted by its reason.
- **Defect:** suppose main's `except OSError` branch became `findings, scanned = [], 0`. Main would still exit 2 through the empty-population refusal, so the arm stays green. A dead probe would then be reported in the empty tree's wording.
- **Impact:** the mutated run still refuses, so this is not a false green. Only the misreported reason goes unnoticed.
- **Fix** (judged SOUND): `code, said = run_quiet(); if code != 2 or 'git ls-files failed' not in said or 'graded NOTHING' in said: FAIL`.
- **Left-shift:** the strengthened assertion is the gate. Observe it red under the mutation above.

### L8. The spec's "Observed by" lines cite an AC that does not read the stated surface (id 10)

- **Where:** `memory/builds/cListedCensus/spec/2026-10-12-spec-TOOL-cListedCensus-1.md:25` (S1), `:31-32` (S2) and `:43` (S4).
- **Defect:**
  - S1 and S4 cite AC4. AC4 runs only `gotchas.py --for-paths` and the codebase-map and memory-hygiene format legs. Those read neither `scan()`'s listing nor what the docs say.
  - S2's "clean and finding lines count tracked files" cites AC1 and AC3. AC1 compares `scan(tree)[1]` and the exit code, and AC3 covers only the `NOTHING` line. Neither reads the count in the clean or finding line.
- **Impact:** the spec records S4's doc sync as observed, but nothing checked it, and M1's runbook miss shows the gap. If someone re-adds the recount that BASE's main had, no arm notices. No behaviour changes.
- **Fix** (judged SOUND):
  - Drop AC4 from S1's observers.
  - Mark S4 as observed by a named grep over the docs that state the scanner's empty-population verdict, with `WIRE-INTO-PROJECT.md` among them.
  - Either assert the `tracked .ps1 file(s)` count in the untracked arm, or drop S2's count sentence from its "Observed by" claim.
- **Left-shift:** this is the known class `observed-by-claim-no-arm-discharges` (`tier2-review.test.sh:1170`, TOOL-aSightedSkeptic-10). Add a spec-audit checklist entry: "each Observed by ACn names an AC whose command reads the surface the requirement states".

review-shape kind=diff-review round=1 intensity=light at=synth raw=16 confirmed=13 refuted=3 unverified=0 blocker=0 high=2 medium=1 low=10 agents=8 out-tokens=162517

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/gate-lint/ps-hygiene.py:140 | high | high | confirmed | I reproduced this on this machine (git 2.55.0.windows.1, core.ignorecase=true, Python 3.14.6). `git ls-files -- '*.MD'` lists 0 files and `'*.md'` lists 3632. `pathlib.Path('tools').rglob('*.PY')` and `rglob('*.py')` both return 79, so BASE's walk matched case-insensitively on Windows and the new git pathspec does not. A tracked `Deploy.PS1` was graded by BASE and is now silently left out, while the OK line still certifies 'N tracked .ps1 file(s) clean'. That is a false green introduced by this diff. Item 7 of the by-design list does not cover it, because the population is exactly what changed. It is graded high rather than blocker because it needs an upper-case extension and a Windows host. The GIT_GLOB_PATHSPECS=1 sub-claim also reproduces (3632 drops to 5), but nobody realistically exports that variable. | sound | - |
| 2 | correctness | tools/gate-lint/ps-hygiene.py:149 | medium | - | refuted | Skipping a listed path that is missing on disk is the spec's explicit design (section 4: 'A listed path that is not a file on disk is skipped and not counted'). The sibling sh_hygiene.py scan_tree (line 355) and encoding_posture.py (line 146) do the same, and the effect matches BASE: a walk never read a file that was absent from disk either, whether from an unstaged deletion or a skip-worktree entry. Grading worktree bytes rather than index bytes also predates this diff. The half-staged-move scenario, where BASE goes red and the new scanner goes green, comes from the intended exclusion of untracked files, not from this skip, and it needs a deliberately inconsistent worktree. A CI checkout of the commit would still go red on the bad b.ps1. The docstring's 'the question is about the commit' explains why the population is tracked files; it does not claim the bytes come from the index. One part of the finding is true: the spec's rationale is wrong, because a staged deletion is never listed. That is wording in a record with no effect on behaviour, not the medium-grade defect claimed. The fix is unsound. Grading the index blob only for missing paths mixes two byte sources, worktree for present files and index for absent ones. Refusing with 2 would turn a routine unstaged deletion into a refusal and break parity with the siblings. | unsound | index-derivation-reads-a-half-staged-move-as-a-deletion |
| 3 | correctness | tools/gate-lint/ps-hygiene.py:147 | low | low | confirmed | git's own documentation of `ls-files --deduplicate` says that without it, an unmerged path is listed once per stage. scan() iterates `sorted(p for p in listing.stdout.split('\0') if p)` with no dedup, so during a conflicted merge a .ps1 is graded, counted and reported 2-3 times. BASE's walk could not produce duplicates, so this diff introduced the behaviour. The verdict (exit 0/1/2) is unaffected, because the same file gets the same grade each time. Only the count and the repeated finding lines are wrong. | sound | - |
| 4 | correctness | tools/gate-lint/ps-hygiene.py:141 | low | low | confirmed | The new `subprocess.run(..., text=True, encoding='utf-8')` decodes both stdout and stderr with strict errors. On POSIX, a tracked .ps1 with a non-UTF-8 name (raw bytes under -z), or a git error message localized in a non-UTF-8 locale, raises UnicodeDecodeError. That is a ValueError, not an OSError, so main's `except OSError` misses it and the run dies with a traceback and exit 1. BASE made no git call, so the diff introduced this. It is never a false green, because a traceback is a red, which keeps it low. On the fix: the catch-ValueError-in-main branch is sound on its own and returns the exit-2 refusal. The surrogateescape branch alone cures the listing crash, but a finding in such a file would then crash at print time under a strict UTF-8 stdout. That still exits 1, which is the correct verdict class. | sound | - |
| 5 | correctness | tools/gate-lint/ps-hygiene.py:194 | low | - | refuted | The hold set at ps-hygiene.py:194-195 is exactly what spec S3 asks for (GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE, plus the pinned ceiling). The sibling sh_hygiene.py selftest (lines 801-802) holds the same three names. GIT_OBJECT_DIRECTORY and GIT_ALTERNATE_OBJECT_DIRECTORIES are exported only by receive-pack into server-side pre-receive/update hooks. Nothing runs `ps-hygiene.py --selftest` there: by-design item 1 and spec section 7 put the selftest on no leg, and AC1 runs it by hand. Pre-commit and pre-push hooks do not export those variables. Even on that hypothetical path the selftest's verdict is unaffected, because ls-files reads the scratch index and the scratch work tree. The only side effect would be a few unreferenced loose blobs, which gc prunes and which a rejected quarantine discards. The finder itself calls the effect harmless. No reachable path has an impact. | sound | - |
| 6 | seams | tools/gate-lint/ps-hygiene.py:140 | high | high | confirmed | Verified read-only on this node (git 2.55.0.windows.1, core.ignorecase=true, Python 3.14.6). `git ls-files -z -- '*.MD'` lists 0 files, against 3632 for '*.md'. `:(icase)*.MD` lists 3632. `Path('tools/gate-lint').rglob('*.MD')` matches README.md. So BASE's `root.rglob("*.ps1")` graded a tracked `X.PS1` on the Windows nodes where gov and nc run, and the new `["git","ls-files","-z","--","*.ps1"]` at ps-hygiene.py:140 silently drops it. The diff introduced this regression. If any lowercase .ps1 is also tracked, main prints `OK — N tracked .ps1 file(s) clean` and exits 0 over the wrong population: the false green this tool's own security model ranks as the severe failure. None of the nine by-design items covers it; item 7 is about the predicates, not the population. The path is narrow: nc tracks only scripts/new-stream.ps1 (checked with `:(icase)`), and the failure needs an upper- or mixed-case extension. Per the rubric, that is high, not blocker. | sound | - |
| 7 | seams | memory/gotchas/a-gate-that-walks-the-repo-root-reads-other-worktrees.md:45 | medium | low | confirmed | The record's '## Gated by' section (lines 43-46) names `ps-hygiene.py --selftest` as the instance's gate. It never says that no leg runs that selftest, yet spec section 7 says the arms 'run on no leg' and that 'the bar's green therefore does not observe this unit'. The brief says the same ('which no leg runs'), as does the dossier ('Neither is on the bar'). Sibling records state an unwired guard outright ('No bar leg runs that suite', 'Nothing runs it today'). AC4 surfaces this record to the next change to ps-hygiene.py, so the omission can suggest the bar catches a revert to a walk. The finder overstates the effect: the record makes no false claim about legs, and the dossier that claims the record says plainly that the scanner is on no leg. The defect is a doc omission with no effect on behaviour, so low. | sound | - |
| 8 | seams | WIRE-INTO-PROJECT.md:137 | medium | low | confirmed | WIRE-INTO-PROJECT.md:137 says 'A repo with none gets a clean report that proves nothing, which is honest'. The sentence is unchanged from BASE, where it was accurate: BASE main printed `OK — 0 .ps1 file(s) clean` and exited 0. This diff changed main to exit 2 with 'graded NOTHING — that is a refusal and not a pass'. So the diff made the adopter runbook false and contradicted the kit README it updated ('A repo with no tracked .ps1 files gets the refusal and exit 2, not a green line'). A grep shows this is the only live copy of the sentence; the other hits are archived templates. Severity is low, not medium: the bullet's actual advice, 'drop it if the project has no .ps1 files', is unchanged and still correct. An adopter who ignores that advice gets a loud, self-explaining refusal (the lesser false-red failure), not a silent wrong result. Only the stated rationale is stale. | sound | - |
| 9 | seams | tools/gate-lint/ps-hygiene.py:5 | low | low | confirmed | This diff introduced line 5 of tools/gate-lint/ps-hygiene.py. The base line was 'Exit 0 clean, 1 on findings, 2 on usage error.' Line 5 now names exit 2 for usage error and for a population that could not be derived. main (lines 260-263) also exits 2 when `scanned == 0`, which is a population that was derived and is empty. The kit README treats this as a separate cause: 'A failed listing and a root that tracks no .ps1 each refuse with exit 2 ... only one of them means there is nothing to grade.' So the header's exit-code summary is incomplete. The impact is small: the same docstring says at lines 34-35 that 'No tracked .ps1 at all is a refusal', and runtime behaviour is unaffected. This is a comment-level defect. | sound | - |
| 10 | seams | memory/builds/cListedCensus/spec/2026-10-12-spec-TOOL-cListedCensus-1.md:43 | low | low | confirmed | Spec line 25 says S1 (the `scan()` listing) is observed by AC4. AC4 (lines 127-130) runs only gotchas.py --for-paths and the codebase-map and memory-hygiene format legs, so it reads nothing about the listing. Line 43 says S4 (what the kit docs say about population and exit codes) is observed by AC4. AC4's legs grade the docs' format, not their content, and the missed WIRE-INTO-PROJECT.md line shows nothing checked the content. S2's 'clean and finding lines count tracked files' cites AC1 and AC3. The AC1 arms compare `scan(tree)[1]` and the exit code; the control asserts the finding text, not the count. AC3 covers only the NOTHING line. So no cited AC reads the count in the clean or finding line. The repo treats unread 'Observed by' claims as a real class (tier2-review.test.sh:1170, TOOL-aSightedSkeptic-10). The spec is new in this diff. The defect sits only in a build record and changes no behaviour, so it is low. | sound | observed-by-claim-no-arm-discharges |
| 11 | seams | memory/gotchas/a-gate-that-walks-the-repo-root-reads-other-worktrees.md:32 | low | - | refuted | This is not a defect. Lines 32-33 wrap the code span `git ls-files -z -- '<glob>'` across a line break, and a CommonMark code span may contain a line ending, which renders as a space. The span renders correctly. ANCHOR_RE in tools/memory-tree/gotchas.py:65 runs findall over the whole body (line 281), not line by line, and excludes whitespace, so the finder's own check holds: anchor harvesting is unaffected. No per-line backtick pairer exists among the gates. Wrapped code spans are also an existing convention: 13 other records in memory/gotchas/ each have lines with an odd backtick count, and no gate reds on them. The claimed impact is hypothetical and the finder graded it low, so it is refuted. | sound | ledger-token-wrapped-across-a-line-joins-nothing |
| 12 | verification | WIRE-INTO-PROJECT.md:137 | medium | medium | confirmed | WIRE-INTO-PROJECT.md:136-138 is unchanged from base and still says that, under the gate-lint kit, a repo with no .ps1 'gets a clean report that proves nothing'. Before this diff that was true: BASE printed 'OK — 0' and exited 0. After this diff, main exits 2 with the 'graded NOTHING' refusal. The diff's behaviour change made the line false, so the finding is in scope. BY DESIGN item 2 covers the green-to-red verdict and says it is documented in the kit README. It does not cover the agent wiring runbook, which still contradicts the kit README and the dossier. The finder overstates one point: the brief's Limitations line asks for 'the README' to say so, and the kit README does. Even so, the runbook is a separate adopter-facing statement that is now wrong. The effect is contained: the runbook's instruction to drop the kit when there is no .ps1 still holds, and an agent that keeps it gets a loud exit-2 red, not a false green. | sound | - |
| 13 | verification | memory/gotchas/a-gate-that-walks-the-repo-root-reads-other-worktrees.md:45 | medium | low | confirmed | The record is new in this diff. Its '## Gated by' section names `ps-hygiene.py --selftest` as the instance's gate and never says that nothing runs it. That matters here more than in other records. Every other selftest the gotcha records name is a declared `[[gate_leg]]` (subject=kit, held until GATE_SELFTESTS=1 or owed by guard). tools/gate-lint/kit.toml declares only the three sh_hygiene legs, so no leg, held or otherwise, names ps-hygiene.py, and GATE_SELFTESTS=1 does not run it either. Spec section 7 says so ('The bar's green therefore does not observe this unit'), and so does the dossier ('Neither is on the bar'). By-design item 1 covers the missing leg, not the record's wording. Two things hold the grade at low. First, the sentence is accurate about what the selftest does. Second, the effect is limited to documentation: `gotchas.py --for-paths` prints only the record's name and description, and the dossier that claims the record states the gap. DECLARES_RE is satisfied either way, by the heading and by 'no machine gate'. | unsound | - |
| 14 | verification | tools/gate-lint/ps-hygiene.py:149 | medium | low | confirmed | No arm reaches the skip at ps-hygiene.py:149. Arm 1 raises before the loop, arm 2 lists nothing, and arms 3 and 4 list a.ps1 and .claude/worktrees/x/a.ps1, which are both on disk. Both proposed breaks survive all four arms. Break (a), `scanned = len(paths)` or the increment moved above the skip, still gives 0, then 1, then findings. Break (b), dropping -z and splitting on newlines, still works because every fixture name is ASCII, so git does not quote it. The spec sentence in section 4 is also wrong. A deletion staged with `git rm` leaves the index, so `git ls-files` never lists it. The skip actually drops unstaged deletions and skip-worktree entries, which the index, and so the commit, still holds. The code as shipped is correct and mirrors sh_hygiene.scan_tree. The cost is a missing red arm for a future regression plus a wrong rationale in a build record, so the effect is contained and graded low. | unsound | - |
| 15 | verification | tools/gate-lint/ps-hygiene.py:220 | low | low | confirmed | In the not-a-repo arm (ps-hygiene.py:219-221), main is checked only for exit 2. The OSError reason is asserted on the direct `scan(tree)` call, but main's handling of it is not. Take a mutation of main's `except OSError` branch to `findings, scanned = [], 0`. scan still raises, main falls through to the zero-population refusal and exits 2, and the arm stays green. The comment at line 215 promises each refusal is asserted by its reason, and that is not fully true for main. The mutated run would still exit 2 rather than pass, so this is not a false green. The only cost is a dead probe being reported with the empty-tree message, so low. | sound | - |
| 16 | verification | tools/gate-lint/ps-hygiene.py:5 | low | low | confirmed | Line 5 lists exit 2 as 'usage error or a population that could not be derived'. The code uses that phrase only for the git failure: the OSError reads 'the population could not be derived at all'. Spec section 4 says the same, separating 'the probe died' from 'the probe answered and nothing is graded'. So the empty-population refusal this diff added is missing from the exit-code line. The impact is cosmetic. The same docstring (lines 34-35) says 'No tracked .ps1 at all is a refusal', and the runtime stderr line says exactly why the run refused, so an adopter is not actually misdirected. | sound | two-answers-to-one-question |
