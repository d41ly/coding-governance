**Serves:** spec-audit TOOL-dSafePassage-52@rev-1 TOOL-dSafePassage-51@rev-1

# Tier-2 spec audit: dSafePassage, units TOOL-dSafePassage-51 and -52, ROUND 1

*This is an adversarial review, done before any code, of the two specs the round-6 audit promoted, 2026-10-23.
Five finder lenses (coherence, grounding, reuse, blast-radius, failure-envelope) read the pair. A skeptic then
tried to refute each finding. This report carries only what the skeptics confirmed, at the grade the skeptic
bound. It adds no finding and drops none.*

Reviewed: memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md@d7fb9b3005bc144588bd768a77edc6de4a549914, memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md@e6bc10a61a6b79ba4c423e9092704a771b05d4e2

ROUND: 1

## Verdict: BLOCKED

There is one blocker item, which covers two raw findings. TOOL-dSafePassage-51's walk refuses any directory
that does not exist. Built as written, it refuses every ordinary submodule and every target with no `.git/modules/`.
The tally is 20 items: 1 blocker, 3 high, 7 medium and 9 low. By raw confirmed finding it is 27: 2 blocker,
3 high, 10 medium and 12 low.

The run completed. All five lenses returned and none died, so a zero count here is evidence of absence within the five lenses' scope.

## Review shape

Intensity full, raw 29, confirmed 27, refuted 2, unverified 0 (0 uncertain), precision 0.93.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| grounding | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 8 | 7 | 1 | 0 | 0 | 0.88 |

Adjudicated tally: 20 items (blocker 1, high 3, medium 7, low 9), covering 27 raw confirmed findings
(blocker 2, high 3, medium 10, low 12).

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified. 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 24 judged sound and 3 judged UNSOUND (ids 9, 12 and 27). None lacked a proposal and none went unjudged.
- Severity on confirmed findings: 0 UNGRADED by the skeptic and 8 RE-GRADED (ids 10, 13, 14, 16, 17, 19, 23 and 26).
- Unverified findings: 0 answered UNCERTAIN, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 50 spec documents were supplied as `specs`, as sibling context.
- Checklist: 39 items, each assigned to one lens: coherence 8, grounding 8, reuse 8, blast-radius 8, failure-envelope 7.
- By design: none supplied. There was no caller byDesign, and its block held 0 entries.
- Move check: no checked subject moved.

Where two findings describe one defect at different binding grades, the protocol keeps them in separate items, one
per grade. Each such item names its partner. The pairs are: id 8 (HIGH) with id 23 (MEDIUM), and id 3 (HIGH) with
ids 9, 14 and 27 (MEDIUM).

## Blockers

### B1. The walk refuses a missing directory, so every ordinary target is refused (ids 7, 22)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md`, §2 S6 and §4 "The walk, in sequence" (`try: entries = subdirectories of d` / `except OSError: refuse d`, and the `walk(c/modules)` recursion).
- **What is wrong:** S6 turns any OSError raised while listing a directory into a refusal. FileNotFoundError is an OSError. The walk lists directories git normally never creates:
  - `<git_dir>/modules/` does not exist in a repository with no submodules.
  - `<c>/modules` does not exist in a submodule git dir with no nested submodules.

  A scratch `git submodule add` produced `.git/modules/sub` with no `modules`, and `os.scandir` on it raised FileNotFoundError.
- **Consequence:** The step kind gets refused on the common path:
  - Gov's own tree has no `.git/modules`, so every gov-first walk (TOOL-8) is refused.
  - Every superproject whose submodules have no nested submodules is refused.

  This contradicts TOOL-47 §5, TOOL-36 §5 and TOOL-47 AC1, which say no `modules/` yields no candidate and exit 0. `tools/govkit/upgrade_steps.py` does not exist yet, so this pseudocode is the design.
- **Fix (both findings' fixes judged SOUND):** Write the missing-directory class into S6 and into the §4 pseudocode. Two forms work:
  - `if not lexists(d): return`.
  - `except FileNotFoundError: return`, placed before `except OSError: refuse d`.

  Only an existing directory that cannot be listed is a refusal. Add a `submodule-sound-no-nested` case whose expected outcome is listed, not refused. Add a criterion that runs the `isolation` fixture over two trees and expects exit 0 with no refusal: a superproject with one sound, non-nested submodule, and gov's own tree.
- **Left-shift gate:** Add a bug-class checklist entry, "an error handler that refuses on OSError must first carve out the absent-path class the sibling specs call empty". Also make the step-kind fixture's sound baseline a gate: a tree with no `.git/modules/` and a tree with one plain submodule must both exit 0.

## High

### H1. S1's hand-out refusal does not check that TOOL-18 and TOOL-19 sit above TOOL-4 (id 1)

- **Where:** TOOL-dSafePassage-51 §2 S1 (the hand-out refusal), against §6 AC1. TOOL-dSafePassage-49 §3's hands-off bullet to this unit (TOOL-49.md:232) has the same narrow wording.
- **What is wrong:** S1 holds the roster back only while TOOL-4's order is not greater than both TOOL-43's and TOOL-7's. AC1 and TOOL-49 AC2 also require TOOL-18 and TOOL-19 to come after TOOL-4, and moving them is a separate header edit. Within one order, the driver breaks ties by string id (`unattended-build.js:608-613`), and `TOOL-dSafePassage-18` sorts before `TOOL-dSafePassage-4`.
- **Consequence:** Suppose a half-done sweep moves TOOL-4 to order 3 but leaves 18 and 19 at order 3. S1's refusal passes, and both consumers build before the unit they consume from. AC1 sees this only at order 14, when nothing can be undone.
- **Fix (judged SOUND):** Widen S1's refusal to TOOL-49 AC2's whole predicate. No roster goes out unless all of these hold:
  - order(43) > order(3)
  - order(4) > max(order(43), order(7))
  - order(18) > order(4) and order(19) > order(4)

  Update TOOL-49 §3's hands-off bullet to this unit to say the same.
- **Left-shift gate:** Add a checklist entry: "a guard that stands in for a criterion tests the criterion's whole predicate, never a subset". Where possible, have the hand-out step run AC2's header probe itself, so the predicate has one source.

### H2. TOOL-52 AC1 cannot fail: it reads neither the arm nor the suite (id 3)

- **Where:** `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md`, §6 AC1, which observes §2 S1. AC2's first half has the same flaw.
- **What is wrong:** Both halves of AC1 pass on today's tree, before TOOL-50 or this unit is built:
  - The first half re-runs the existing scan line and tests that `tools/memory-tree/check-arms.py`, which already exists, exists.
  - The second half tests bash's own `set -u` behaviour.

  AC2's first half (`grep -c '^_mt_rc='`) already prints 1.
- **Consequence:** AC1 certifies S1 without reading the arm: the claim that the arm's guard takes its ok branch in gov's tree and that a misplaced arm aborts. It stays green in three cases:
  - The arm is missing.
  - The arm is misplaced.
  - The arm is guarded by `${_mt_rc:-}`, the form §4 rejects.

  A criterion that certifies what it does not check will mislead the next change.
- **Fix (judged SOUND):** Make AC1 read the arm itself:
  - Extract the arm's guard line from `tools/push-main.test.sh` by content.
  - Assert that it reads `$_mt_rc` bare, with no `:-` default.
  - Eval it after the scan and confirm it takes the ok branch.
  - For the abort half, eval the arm's guard line alone under `set -u`, with no scan before it, and require exit 127.
  - As the build's red probe, stage a suite copy with the arm moved above line 873 and see the suite abort.
- **Related:** Ids 9, 14 and 27 (item M2) describe the same defect at MEDIUM.
- **Left-shift gate:** Checklist class `fixture-passes-by-finding-nothing`. Every new criterion carries a "red at the base" line, and the build run executes each criterion at the base and must see it red before the build.

### H3. A link at `<candidate>/modules` or at the root `modules/` is followed (id 8)

- **Where:** TOOL-dSafePassage-51 §2 S6 and §4 "The walk, in sequence".
- **What is wrong:** S6 says the walk never follows a symlink or a junction, but the `islink(c) or isjunction(c)` test runs only on the children of a listed directory. Two kinds of path are listed without any link test:
  - the root `<git_dir>/modules/`
  - each path passed to `walk(c/modules)`

  A scratch junction `m\a\modules -> m` listed `['a']` silently and without end.
- **Consequence:** Two failure modes follow:
  - A junction `.git/modules/a/modules -> .git/modules` recurses until it hits a path-length OSError, which becomes a refusal naming the wrong path, or a RecursionError.
  - A `c/modules` junction to a directory outside `.git/modules` is walked, and its configs are read and listed. That falsifies §5's claim that S6 stops the walk leaving `.git/modules/`.

  The `submodule-modules-link-loop` plant tests only the child position, so AC4 stays green.
- **Fix (judged SOUND):** Test `islink(d) or isjunction(d)` at the top of `walk(d)`, before listing, so the root and every `c/modules` get the same test as a child. Add a plant `submodule-modules-link-nested`, where a candidate's `modules` is a junction back to `.git/modules`, and have AC4 cover it.
- **Related:** Id 23 (item M6) describes the same defect at MEDIUM.
- **Left-shift gate:** Add a checklist entry: "a no-link-followed rule is tested on every path the walk enters, including the root and every recursion argument, not just on listed children". The step fixture should plant a link at each position the walk enters.

## Medium

### M1. TOOL-51 AC1 and AC2 grade the sweep, and S1's refusal is never seen to refuse (id 2)

- **Where:** TOOL-dSafePassage-51 §6 AC1 and AC2, and §7 "New arm" / "What the check does not cover".
- **What is wrong:** AC1 and AC2 grade work done outside this unit's write set: the commit order and the sweep's Rollout edits. Both are settled before this order-14 pass starts. The only real guard is S1's hand-out refusal, which §7 calls the only one. No criterion covers that refusal, and no staged case ever sees it refuse.
- **Consequence:** In this pass's acceptance ledger, AC1 and AC2 read green while observing nothing the unit built. If the hand-out check were miswired, it would go unnoticed until AC1 read the history afterwards.
- **Fix (judged SOUND):** Add a criterion the build run must observe before hand-out:
  - Over a scratch copy of the spec directory whose TOOL-4 header still reads `order 2`, the hand-out step refuses and names the inversion.
  - Over the swept tree, the same step proceeds.

  Record AC1 and AC2 as checks of the sweep, attributed to the build run, not to this unit's pass.
- **Left-shift gate:** Add a checklist entry: "a criterion attributes itself to the actor whose write it grades". Any guard §7 names as "the only" guard gets a staged red case.

### M2. TOOL-52 AC1 types its own guard and passes at the base (ids 9, 14, 27)

- **Where:** TOOL-dSafePassage-52 §6 AC1, and §2 S1's "Observed by AC1".
- **What is wrong:** AC1 evaluates a guard it typed itself (`[ -f "$HERE/$_mt_rc/check-arms.py" ]`) after evaluating the existing scan line. Its abort half is a synthetic two-line `set -u` script, not the suite. `grep -n check-arms.py tools/push-main.test.sh` prints nothing at the base, yet AC1 prints `ok-branch` and the `unbound variable`/127 pair.
- **Consequence:** AC1's "Red when" can never fire from this unit's build. It stays green in four cases:
  - The real arm tests the wrong file.
  - The real arm skips in gov's tree.
  - The real arm sits above the scan.
  - `_mt_rc` reaches the suite from the environment.

  The effect is contained, because S1 routes the ok line to TOOL-50's New arm and AC2 reads the arm's place.
- **Fix:** Id 14's fix was judged SOUND. Ids 9 and 27 had their finders' fixes REJECTED, and the skeptics' corrected fixes are folded in here:
  - Replace AC1's first half with a run of the built suite in gov's own tree. Assert that TOOL-50's derived-count arm prints its `ok` line and that no `skip —` line appears for that arm.
  - Alternatively, for an eval form, take the suite's own `if` line that spells `check-arms.py`. Strip its leading `if ` and its trailing `; then`, and eval that condition after the eval'd scan line, followed by `&& echo ok-branch` (id 9's correction).
  - State that AC1 is red at the base, where no such line exists.
  - Keep the staged break as the second half: a scratch copy of the suite with the arm block moved above the `^_mt_rc=` line, run under `env -u _mt_rc`. It must print `unbound variable`, exit non-zero, and print no `push-main.test: all cases ok`. The build runs this staged break, not the review.
  - If none of this can be observed, mark S1 NOT OBSERVED and cite TOOL-50's New arm line.
- **Related:** Id 3 (item H2) describes the same defect at HIGH. H2's and M2's fixes are compatible, and applying both closes the class.
- **Left-shift gate:** Same class as H2 (`rule-stated-with-no-check-that-fails`). A criterion that names an arm must read that arm's text or run the suite that holds it.

### M3. S6 and S15 build a second link and file-type test, and §10 says no seam exists (id 12)

- **Where:** TOOL-dSafePassage-51 §2 S6 and S15, §4 "The walk, in sequence", and §10.
- **What is wrong:** `read_plain_stat(root, parts, want)` in `tools/run-gates/measure_legs.py:1373` is already a link-and-type seam. It lstats each component, refuses any `st_reparse_tag`, and requires S_ISDIR or S_ISREG, plus `nlink == 1` for a file. §10 concludes "no existing seam fits", because its grep looked only for `islink`/`isjunction`. S15 takes `os.lstat` and then `os.stat`, which follows links, so a symlinked or junctioned `.gitmodules` passes and is read. The spec never says whether that is intended.
- **Consequence:** The spec carries an inaccurate reuse conclusion and an unstated policy on linked `.gitmodules`. The effect is contained.
- **Fix (finder's fix REJECTED; the skeptic's corrected fix):** Keep TOOL-51's own test, and do four things:
  - In §4 "Alternatives rejected", name `read_plain_stat` in `tools/run-gates/measure_legs.py`. Give the reasons it is not reused: it is a run-gates kit primitive across the copy-install boundary, and its `nlink == 1` rule fits scratch files, not a worktree file.
  - Make S15's type test refuse a link by `os.lstat` before the `os.stat`/S_ISREG test. S_ISLNK or a nonzero `st_reparse_tag` is a refusal that names the path.
  - Or, instead of refusing, state outright that a linked `.gitmodules` is admitted.
  - Correct §10's conclusion to name the seam.
- **Left-shift gate:** Add a checklist entry: "a reuse census greps by behaviour (`st_reparse_tag`, `S_ISREG`, `lstat`) as well as by function name".

### M4. TOOL-52 AC2's anchor stops one line short of the `fi` it claims to bound (ids 15, 28)

- **Where:** TOOL-dSafePassage-52 §6 AC2, §2 S2, and §4 "The arm's place, by content".
- **What is wrong:** AC2 anchors on the literal `skip — 28-32`, which resolves to line 1046, the else-branch echo. The block's closing `fi` is at line 1047, and S2 and §4 name that `fi` as the bound.
- **Consequence:** An arm inserted between 1046 and 1047, inside the else-branch, passes AC2. That contradicts AC2's "Red when … inside the 28-32 block". Such an arm never runs in gov's tree. If the skip message were edited, AC2 would have no line to compare against and would turn vacuous. The effect is contained, because TOOL-50's New arm would see its ok line missing.
- **Fix (both findings' fixes judged SOUND):** Anchor on the target itself. Require the first `check-arms.py` line to be greater than the first `^fi$` after the `skip — 28-32` line, for example with `awk '/skip — 28-32/{s=1} s&&/^fi$/{print NR; exit}'`. Alternatively, require that no line between the skip line and that `fi` spells `check-arms.py`. Make the probe fail loudly when it finds no skip line or no `fi`. The build's staged break inserts the arm between 1046 and 1047 and must see AC2 red.
- **Left-shift gate:** Checklist class `anchor-literal-resolves-above-its-target`. A placement probe anchors on the structural line it names, and fails loudly when the anchor is absent.

### M5. `os.path.isjunction` needs Python 3.12, but govkit's floor is 3.11 (id 18)

- **Where:** TOOL-dSafePassage-51 §2 S6 and §4 "The walk, in sequence".
- **What is wrong:** The walk calls `os.path.isjunction` unconditionally, and that function was added in Python 3.12. govkit's floor is CPython 3.11 (`tools/govkit/govkit.py:104-112`), and the spec states no floor and does no feature detection.
- **Consequence:** On 3.11, the walk raises AttributeError at the first entry under `.git/modules/`. That is a Traceback on every submodule-bearing target, which AC4 forbids. The node-d probe ran on 3.14.5 and cannot show it.
- **Fix (judged SOUND):** Feature-detect, as `tools/memory-recall/selftest.py:347-349` does: `isj = getattr(os.path, 'isjunction', None)`. Fall back on Windows to `os.lstat(c).st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT`, and on POSIX to `islink` alone. State the floor in §5. The build's probe runs the walk under a stubbed `os.path` that lacks `isjunction`.
- **Left-shift gate:** Add a checklist entry, "a stdlib call newer than the kit's stated python floor is feature-detected". Where feasible, add a gate that greps copy-installed kit code for `isjunction` without `getattr`.

### M6. The walk's link rule is written for children only (id 23)

- **Where:** TOOL-dSafePassage-51 §2 S6 and §4 "The walk, in sequence".
- **What is wrong:** The link test runs on the entries listed inside `d`, never on the directory the walk descends into. A link at `<candidate>/modules`, or at `<git_dir>/modules` itself, is followed. Inside such a junction, no entry reads as a link: a scratch path `m/a/loop/a` read islink False and isjunction False. The rule covers one instance, a link at a name segment (the `modules/a/loop` plant), when the class is "no link followed under `modules/`".
- **Consequence:** §5's claim that S6 stops the walk leaving `.git/modules/` through a link is false on this path, and AC4's plant cannot show it. The grade is MEDIUM: the walk spawns only a read-only `config --list`, and a loop most likely ends in an OSError that becomes a refusal.
- **Fix (judged SOUND):** State the rule over every path the walk enters:
  - Test `islink(d) or isjunction(d)` at the top of `walk(d)`, as well as on each entry.
  - Add a plant `submodule-nested-modules-link`, where `.git/modules/a` is a sound repository and `.git/modules/a/modules` links back to `.git/modules`. Expect a refusal naming `.git/modules/a/modules`, no `Traceback`, and exit 1 within 60 seconds.
  - State whether `a` in `submodule-modules-link-loop` is a name segment. If `a` is a repository, `loop` is never listed.
- **Related:** Id 8 (item H3) describes the same defect at HIGH. One fix closes both.
- **Left-shift gate:** Same as H3.

### M7. The walk's listing step can drop a link before the link test sees it (id 24)

- **Where:** TOOL-dSafePassage-51 §4 "The walk, in sequence" (`entries = subdirectories of d  # never following a link`), against S6.
- **What is wrong:** The population is defined as "subdirectories of d", and only those entries reach the link test. A builder might list with `DirEntry.is_dir(follow_symlinks=False)` or `os.path.isdir`. Under either, a POSIX directory symlink, a dangling link, or a file link is filtered out before the test and skipped silently. S6 says any link under `modules/` is refused.
- **Consequence:** Whether a link is refused or skipped depends on how the builder lists entries. Git follows a symlinked `.git/modules/<name>`, so a skipped one leaves a submodule config ungraded while the step passes.
- **Fix (judged SOUND):** Define the population as every directory entry of `d` (`os.scandir(d)`, no type filter). Run the link/junction test first and refuse on a hit. Only then filter to real directories with `is_dir(follow_symlinks=False)`. Add a POSIX-or-Windows plant with a dangling symlink under `modules/`, which must be refused by name.
- **Left-shift gate:** Add a checklist entry: "a refusal rule's population is defined before any filter that could drop the refused class".

## Low

### L1. S9's Readers census for `UNLISTED_EXECUTOR_KEYS` was taken at the base and misses readers (ids 4, 17)

- **Where:** TOOL-dSafePassage-51 §2 S9 Readers line, and §4 Inventory.
- **What is wrong:** S9 retires TOOL-49's `UNLISTED_EXECUTOR_KEYS` and says "READER NOT IN TREE … no tracked file spells it at the base". That census has two gaps:
  - It misses TOOL-29 §3's hands-off bullet to TOOL-49 (TOOL-29.md:73), which still says to keep the constant.
  - It is taken at the base, not at the HEAD after TOOL-49's order-13 pass. TOOL-49's S8 and Inventory mint the constant in `tools/govkit/upgrade_steps.py`, and the selftest reads it.

  The Inventory lists no retirement. AC6 greps only `upgrade_steps.py`. `memory/TEMPLATE-SPEC.md:444` reserves READER NOT IN TREE for a name that lives outside this tree.
- **Consequence:** TOOL-49's pass reads two conflicting bullets and may mint the constant, which this unit must then remove. A stale reference in a help page or in prose would go unlisted. The effect is contained, because AC6 catches the name in the module, TOOL-49's bullet to TOOL-51 already says to drop it, and a stale selftest reference fails loudly.
- **Fix (both findings' fixes judged SOUND):**
  - Add TOOL-29 §3's hands-off bullet to S9's list of texts read as naming the selftest literal, and to the Readers line.
  - Take the Readers census at the tree this pass builds on, for example with `git grep -n UNLISTED_EXECUTOR_KEYS -- tools help` at the post-TOOL-49 HEAD.
  - List the retirement in §4 Inventory.
  - Widen AC6's grep to `-- tools help` so that it prints nothing.
- **Left-shift gate:** Checklist class `retirement-inventory-misses-readers-by-value`. A retirement census runs at the unit's build HEAD, over specs, code and help.

### L2. S12 says the section probe skips fenced blocks, but it only knows backtick fences (id 5)

- **Where:** TOOL-dSafePassage-51 §4 "The section probe", and §2 S12.
- **What is wrong:** The awk line toggles only on lines that start with three backticks. A `~~~` fence that holds a `# ` line ends the section early, as a scratch probe confirmed.
- **Consequence:** If the help page ever uses a tilde fence, TOOL-49 AC12, TOOL-47 AC4 and TOOL-48 AC3 go red on a correct page, or skip lines silently. No help page uses `~~~` today.
- **Fix (judged SOUND):** Toggle on `/^(```|~~~)/`. Alternatively, state in S12 that only backtick fences are recognised, and add a §7 "does not cover" line for tilde fences.
- **Left-shift gate:** Add a checklist entry: "a markdown probe that claims to skip fences names the fence forms it recognises".

### L3. S1 gives the misplaced-arm abort exit 127, but the suite exits 1 (id 10)

- **Where:** TOOL-dSafePassage-52 §2 S1, and §7 (the staged failing case).
- **What is wrong:** Exit 127 is what `bash -c` returns on an unbound read. `tools/gate-legs.json:664` runs the suite as a script file, and there the same abort prints `<file>: line N: _mt_rc: unbound variable` and exits 1. That is the same code as `push-main.test: FAILURES`.
- **Consequence:** A builder who asserts 127 on the staged break gets a wrong expectation. The only signal that separates the abort from FAILURES is the `unbound variable` text, which the spec never names. No criterion asserts 127 on the suite, so built behaviour is unaffected.
- **Fix (judged SOUND):** Restate S1. Under `bash <file>`, the abort prints `<file>: line N: _mt_rc: unbound variable`, exits 1, and prints no `push-main.test:` final line. The staged break's red is the missing final line plus the `unbound variable` text, not an exit code. Label AC1's 127 as a property of `bash -c` only.
- **Left-shift gate:** Add a checklist entry: "an exit code quoted for a failure mode is measured in the invocation form the bar uses".

### L4. TOOL-52's `--render` route writes four live copies, not one (ids 11, 20, 26)

- **Where:** TOOL-dSafePassage-52 §2 S4, §4 Rollout and Files touched, the order-13 M6 disjointness claim, and §6 AC3.
- **What is wrong:** `tools/memory-tree/kit-dogfood-parity.test.sh --render` runs `render "$ship" > "$live"` for all four PAIRS (line 61): `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` and `memory/guides/ANNOTATION-STYLE.md`. The spec names only `memory/TEMPLATE-SPEC.md` as an output. A render that dies mid-stream truncates its live copy, and §5 does not name that case.
- **Consequence:** The stated write set and the M6 disjointness claim are incomplete. While the `kit/dogfood doc parity` bar leg holds, the other three come out byte-identical (render_doc strips CR), so normally nothing extra changes. Only a tree that has already drifted would fold unrelated rewrites, possibly of BUILD-METHOD.md, into this commit. A failed render is loud.
- **Fix (all three findings' fixes judged SOUND):**
  - In S4, Files touched and the Rollout, name all four `--render` outputs.
  - Require that `git diff --name-only` after the render lists only `memory/TEMPLATE-SPEC.md` among them, or that `git diff --quiet` holds on the other three. Otherwise stop, or restore them before commit.
  - Add to §5: a non-zero `--render` exit is a stop, and the live copy is restored from HEAD, never committed.
- **Left-shift gate:** Add a checklist entry: "a write set routed through a tool lists every output the tool writes, read from the tool's own pair list".

### L5. §7 says only S1 guards the commit order, but the dispatch edge refusal already does (id 13)

- **Where:** TOOL-dSafePassage-51 §2 S1, §5 risks, and §7 "What the check does not cover".
- **What is wrong:** The driver already has a refusal for this case. `tools/unattended/unattended.sh:13691-13761`, TOOL-dTrueNorth-16 S2's `--dispatch` edge refusal, stops with fail 49 while a same-build producer is neither CLOSED nor WONTDO. TOOL-4 declares `consumes-from` on TOOL-7 and TOOL-43. S1 does not cite that refusal, and §7 says the commit order is the thing "which only S1's hand-out step guards".
- **Consequence:** The inaccurate claim could lead the next change to weaken the dispatch refusal. S1 still adds something: it stops the run before any pass starts. Nothing behaves wrongly.
- **Fix (judged SOUND):** In S1 and §7, cite the TOOL-dTrueNorth-16 S2 edge refusal (fail 49) in `tools/unattended/unattended.sh` as the existing guard of AC1's commit order. Keep S1's sweep step only for what that refusal does not see: the header order the driver sorts by. Otherwise drop the new refusal and let AC1 rest on the dispatch refusal. Rewrite §7's "which only S1's hand-out step guards" to match.
- **Left-shift gate:** Add a checklist entry: "a 'does not cover' or 'only guard' claim is checked against the driver's existing refusals".

### L6. TOOL-51 AC1's "first line reading `TOOL-dSafePassage-4`" invites a prefix match (id 16)

- **Where:** TOOL-dSafePassage-51 §6 AC1.
- **What is wrong:** AC1 spells no match command. `TOOL-dSafePassage-4` is a prefix of `TOOL-dSafePassage-43`, which commits first, and of -44 to -49.
- **Consequence:** An unanchored grep resolves to TOOL-43's commit and goes red on a correct history. This can cause a false red only, never a false pass.
- **Fix (judged SOUND):** Spell the probe with whole-line matching, for example `git log --reverse --format='%(trailers:key=Pass,valueonly)' <BASE>..HEAD | grep -n -x -m1 'TOOL-dSafePassage-4'`. Use the same `-x` for -43, -7, -18 and -19. Add a red case in which only TOOL-43's commits exist.
- **Left-shift gate:** Add a checklist entry: "an id-matching probe is spelled whole-line (`-x`) wherever one id is a prefix of another".

### L7. S12 calls the section probe "the one probe", but seven sibling criteria grep the whole page (id 19)

- **Where:** TOOL-dSafePassage-51 §2 S12.
- **What is wrong:** S12 reads only TOOL-47 AC4, TOOL-48 AC3 and TOOL-49 as citing the probe. Seven other criteria grep the whole of `help/upgrade-steps.md` and then assert what "the section" names: TOOL-7 AC8, TOOL-24 AC5, TOOL-29 AC5, TOOL-36 AC3, TOOL-37 AC4, TOOL-38 AC4 and TOOL-42 AC12.
- **Consequence:** Those criteria stay green when a required term sits on the right page but outside the section. The rule is applied to three instances, not to the class.
- **Fix (judged SOUND):** Name each of those seven criteria as read with §4's probe piped into the grep. Or narrow S12's claim to the three it lists.
- **Left-shift gate:** Add a checklist entry: "a rule declared 'the one probe for X' lists every criterion asserting X, found by grep".

### L8. §7 says the unit moves no arm, yet it touches push-main.test.sh and may repair the arm (id 21)

- **Where:** TOOL-dSafePassage-52 §7 ("This unit adds no arm and moves none"), against §4 Files touched and the Rollout write set.
- **What is wrong:** `tools/push-main.test.sh` is in Files touched, and AC2 goes red on a misplaced arm, so a repair would move the arm. §7 still carries no `New arm:` line, although `memory/TEMPLATE-SPEC.md:550` requires one per arm a unit "adds or moves". The leg line also omits the unguarded `harness arms (fail branches armed or pinned)` leg.
- **Consequence:** The spec is inconsistent with itself. Coverage is not lost, because the arms leg runs on every change.
- **Fix (judged SOUND):** Choose one:
  - Drop `push-main.test.sh` from Files touched, and state that a misplacement found by AC2 goes back to TOOL-50.
  - Add a conditional `New arm: tools/push-main.test.sh · covers AC2 · ...` line, and name `harness arms (fail branches armed or pinned)` on the leg line.
- **Left-shift gate:** Add a checklist entry: "a suite file in Files touched implies either a `New arm:` line or an explicit hand-back".

### L9. S3 drops S2's "on one line" rule, but AC2's grep needs it (id 29)

- **Where:** TOOL-dSafePassage-51 §2 S3 (against S2), and §6 AC2.
- **What is wrong:** S2 requires `TOOL-dSafePassage-4 builds at order 3` "in these words and on one line". S3, the TOOL-43 Rollout amendment, does not. AC2's `git grep -c` over all three specs is line-local, and TOOL-43's Rollout already wraps its sentence today.
- **Consequence:** A correct but wrapped amendment makes AC2 print 0 for that file. This false red is loud and is caught before merge.
- **Fix (judged SOUND):** Add "in these words and on one line" to S3. Or state once, in AC2's preamble, that the phrase is held on one line in each of the three Rollouts.
- **Left-shift gate:** Checklist class `ledger-token-wrapped-across-a-line-joins-nothing`. Every rollout phrase a line-local grep counts carries the one-line constraint at each site.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=29 confirmed=27 refuted=2 unverified=0 blocker=2 high=3 medium=10 low=12 agents=11 out-tokens=168835

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S1 (the hand-out refusal) against section 6 AC1 | high | high | confirmed | I re-read TOOL-51.md:64-66. The refusal holds the roster only "while TOOL-dSafePassage-4's order is not greater than both TOOL-dSafePassage-43's and TOOL-dSafePassage-7's", and TOOL-49.md:232's hands-off bullet says the same. Neither mentions 18 or 19. TOOL-49 AC2 (:351-356) and TOOL-51 AC1 (:296-297) both require 18 and 19 to come after 4. TOOL-49's order-move table (:256-261) shows moving 18 and 19 from order 3 to 4 is a separate header edit. I read unattended-build.js:608-613: within one order the tie-break is `String(x.id) < String(y.id)`, and 'TOOL-dSafePassage-18' sorts before 'TOOL-dSafePassage-4' because '1' < '4'. Headers today read 4=order 2 and 18=19=order 3. So a sweep that moves only TOOL-4 passes S1's refusal and builds both consumers before the unit they consume from. AC1 would only see that at order 14. S1 does say the sweep runs AC2's header probe, but the refusal condition it actually states is the narrow one. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 6 AC1, AC2 and section 7 New arm / What the check does not cover | medium | medium | confirmed | I re-ran AC2's git grep. It prints TOOL-2.md:222, TOOL-43.md:118 and TOOL-7.md:208, so it is red today. But S2, S3 and §4 Rollout (:251-253) put those edits in the sweep before hand-out, and AC1's commit order is fixed before order 14. Nothing this unit's pass writes can move either criterion. S1's refusal is the guard §7 (:351-352) names as the only one before this pass. No §6 criterion and no case in the New arm line (:349) stages that refusal or sees it refuse, so a miswired hand-out check would go unnoticed until AC1 reads the history afterwards. The effect is contained because AC1 still catches the inversion, though too late to prevent it. | sound | - |
| 3 | coherence | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 6 AC1 (observing section 2 S1) | high | high | confirmed | I ran both AC1 commands on today's tree. The first printed `ok-branch` with rc=0. The second printed `bash: line 1: _mt_rc: unbound variable` with rc=127. tools/memory-tree/check-arms.py already exists, and `grep -c '^_mt_rc=' tools/push-main.test.sh` printed 1. Neither command reads the arm, and the suite has no check-arms.py line yet, so AC1 is green before TOOL-50 or this unit is built. It stays green whether the arm is missing, misplaced, or guarded with `${_mt_rc:-}`, the form §4 rejects. Yet S1 says AC1 observes that the arm's guard takes its ok branch. AC2's second half does read the arm's place (it is red today), so only AC1, plus AC2's first half, is vacuous. A criterion that certifies S1 without reading it will mislead the next change. | sound | fixture-passes-by-finding-nothing |
| 4 | coherence | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S9 Readers line | low | low | confirmed | `git grep -n UNLISTED_EXECUTOR_KEYS` prints TOOL-29.md:73, a hands-off bullet to TOOL-49 that says "... and keeping `UNLISTED_EXECUTOR_KEYS`, finding 27 ...". S9 (TOOL-51.md:119-129) lists only TOOL-49's own sections as read with the selftest literal. Its Readers line even says "no tracked file spells it at the base". It does not name TOOL-29's bullet, which still tells TOOL-49's order-13 pass to keep the constant, while TOOL-49.md:232 says to drop it. AC6 catches the name in the module, so the effect is contained. | sound | retirement-inventory-misses-readers-by-value |
| 5 | coherence | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 4 "The section probe" / section 2 S12 | low | low | confirmed | I wrote page2.md under my scratch directory (verify-b1) with the lines '## What a step can reach', 'a', '~~~', '# x', '~~~', 'b', '## End' and ran §4's awk line over it. It printed only `a` and `~~~`, so the section ended at `# x` inside the tilde fence. S12 says the probe "skips fenced blocks" without limiting that to backtick fences. `grep -rn '^~~~' help` printed nothing, so no help page uses a tilde fence today and the effect is contained. The fix's second option, stating backtick-only and adding a §7 line, cures it cleanly. | sound | - |
| 6 | coherence | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 6 AC1 | low | - | refuted | Case (2): the cited section already says it. AC1 (TOOL-51.md:293-297) asks for the first line *reading* `TOOL-dSafePassage-4`, meaning a line whose content is that value. A line holding `TOOL-dSafePassage-43` reads `TOOL-dSafePassage-43`. The spec set uses a different verb for containment: TOOL-52 AC2 says the line *spelling* `check-arms.py`. `%(trailers:key=Pass,valueonly)` prints each Pass value on its own line, so a commit with several values needs no extra split step. The ambiguity the finding assumes is not in the text. | sound | - |
| 7 | grounding | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S6, section 4 "The walk, in sequence" | blocker | blocker | confirmed | TOOL-51 §4 lines 198-208 (blob e6bc10a6 verified) read `try: entries = subdirectories of d / except OSError: refuse d` (S6), and they call `walk(c/modules)` for every listed candidate with no existence test first. I re-ran the probe in scratch (verify-b2): `git submodule add ../sub sub` and then `ls .git/modules/sub` printed HEAD config description hooks index info logs objects packed-refs refs, with no `modules`. `os.scandir('.git/modules/sub/modules')` raised `FileNotFoundError: [WinError 3]`. So every sound submodule gets the S6 refusal. TOOL-47 §5 (line 150) and TOOL-36 §5 do say a target with no root `modules/` yields no candidate. S6's blanket OSError rule contradicts that for the root, and no sibling covers a candidate's missing `c/modules`. Upgrade_steps.py is absent at the base, so the pseudocode is the design. The step is falsely refused for any target that has submodules, which is the common path. | sound | - |
| 8 | grounding | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S6, section 4 "The walk, in sequence" | high | high | confirmed | In TOOL-51 §4 lines 199-210 the link test is `if islink(c) or isjunction(c)` on children only. Neither the root `d` nor the path passed to `walk(c/modules)` is tested before it is listed. S6's prose says the walk tests before it descends, but the amended `walk(d)` puts the test on children alone. I probed in scratch with `mklink /J m\a\modules m`: islink/isjunction/isdir printed `False True True`, `os.scandir('m/a/modules')` listed `['a']`, and `m/a/modules/a/modules/a/modules` also listed `['a']`. So listing through the junction is silent and recursive. In practice the loop more likely ends at a path-length OSError than at a RecursionError, and that OSError becomes an S6 refusal naming the wrong path. Even so, a `c/modules` junction to a directory outside `.git/modules` is walked, and its configs are read and listed. That falsifies §5's claim that S6 stops the walk leaving `.git/modules/`. The `submodule-modules-link-loop` plant only exercises the child position, so AC4 stays green while that position goes unchecked. | sound | - |
| 9 | grounding | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 6 AC1 | medium | medium | confirmed | I ran TOOL-52 AC1's first command at the base from the repo root. It printed `rc=[memory-tree]` then `ok-branch`, exit 0. The second command printed `bash: line 1: _mt_rc: unbound variable`, exit 127. `grep -n 'check-arms.py' tools/push-main.test.sh` printed nothing (grep exit 1), so TOOL-50's arm is absent and AC1 is already green. AC1 evaluates a guard it typed itself, not the arm's code, yet S1 cites it as observing that the arm's guard takes its ok branch. The effect is contained: AC2 does locate the arm by `check-arms.py`, and the suite run prints the arm's own ok line. | unsound | rule-stated-with-no-check-that-fails |
| 10 | grounding | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 2 S1 and section 7 (staged failing case) | medium | low | confirmed | I probed in scratch. A file holding `set -u` / `if [ -n "$_mt_rc" ] && true; then ...` / `echo after`, run as `bash arm.sh`, printed `arm.sh: line 2: _mt_rc: unbound variable` and exited 1. The same text under `bash -c` exited 127, single-line or multi-line, on bash 5.3.9. tools/gate-legs.json:664 runs the suite as the file `{prefix}/push-main.test.sh`, and push-main.test.sh:1049 exits 1 on FAILURES. So S1's 127 holds only for the `-c` form, and the real abort shares exit 1 with FAILURES. S1 reports 127 as a property of its own reproduction, and no criterion asserts 127 on the suite (AC1 uses `-c`, where it is true). So the spec built as written changes no behaviour; the misstatement can only mislead a reader. | sound | - |
| 11 | grounding | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 2 S4, section 4 Rollout and Files touched, section 6 AC3 | low | low | confirmed | tools/memory-tree/kit-dogfood-parity.test.sh:61 sets PAIRS to four live copies: HYGIENE.md, TEMPLATE-SPEC.md, guides/BUILD-METHOD.md and guides/ANNOTATION-STYLE.md. The `--render` arm (:367-377) runs `render "$ship" > "$live"` for every pair. So S4's route writes three files that TOOL-52's Files touched and its M6 disjointness claim leave out. render_doc strips CR (`out=${out//$'\r'/}`) and prints with printf, so while the parity leg holds the three come out byte-identical. The consequence is therefore an incomplete write-set statement, not a content change. | sound | - |
| 12 | reuse | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S6 and S15; section 4 "The walk, in sequence"; section 10 | medium | medium | confirmed | tools/run-gates/measure_legs.py:1373 at the base defines `read_plain_stat(root, parts, want)`. It lstats each component, refuses any `st_reparse_tag` and requires S_ISDIR or S_ISREG, plus nlink==1 for a file, and it is used at :1433, :1450, :1543 and :1572. It is a link-and-type seam that TOOL-51 §10 never names, even though §10 concludes 'no existing seam fits'. §10's literal grep report is accurate: islink appears only in check_app_alias's docstrings at :892 and :2254. The conclusion missed the seam because the seam spells st_reparse_tag. S15 as written takes `os.stat` after `os.lstat`, so a `.gitmodules` that is a symlink or junction to a regular file passes and is read, and the spec never says whether that is intended. The effect is contained. | unsound | - |
| 13 | reuse | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S1; section 5 risks; section 7 "What the check does not cover" | medium | low | confirmed | The claim holds. tools/unattended/unattended.sh:13691-13761 (also present at base 3708a705, line 13691) is the TOOL-dTrueNorth-16 S2 edge refusal. It reads the dispatched spec's own consumes-from edges with read_consumes_from and stops with fail 49 while a same-build producer is neither CLOSED nor WONTDO. Its comment names the same-order blind spot. TOOL-4's spec has column-0 consumes-from bullets on TOOL-7 (:115) and TOOL-43 (:122), so a TOOL-4 pass ahead of them is already refused at dispatch. TOOL-51's §7 (pinned blob, lines 351-352) still says the commit order is the thing 'which only S1's hand-out step guards', and S1, §3 and §5 never cite the dispatch refusal. Graded low, not medium. S1's step still adds something: it stops the run before any pass starts, where the edge refusal only stops it mid-run at TOOL-4's dispatch. So nothing behaves wrongly. The defect is an inaccurate 'does not cover' statement. | sound | - |
| 14 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 6 AC1 (and section 2 S1's 'Observed by AC1') | high | medium | confirmed | Re-ran both halves of AC1 at HEAD, which is base state. The eval probe printed `ok-branch` with rc=0. The set -u probe printed `bash: line 1: _mt_rc: unbound variable` with rc=127. `grep -n check-arms.py tools/push-main.test.sh` printed nothing (rc=1), so the arm does not exist yet. AC1 is green before anything is built. AC1 also types its own guard (`[ -f "$HERE/$_mt_rc/check-arms.py" ]`) and never reads TOOL-50's arm, so a real arm that tests the wrong file or skips would leave it green. Its second half only tests how bash behaves. S1 still claims 'the arm's guard takes its ok branch, which AC1 observes'. Graded medium, not high. S1 itself sends the printed ok line to TOOL-50's New arm (it must print ok and no skip in gov's tree), and AC2 reads the arm's place. So the real arm's behaviour is checked elsewhere and the effect is contained. | sound | - |
| 15 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 6 AC2 / section 2 S2 / section 4 'The arm's place, by content' | medium | medium | confirmed | Re-ran the AC2 grep. It printed 873 (`_mt_rc=` scan), 1046 (the `echo "  skip — 28-32 ..."` line) and 1049 (the final `[ "$fail" = 0 ]` line). `sed -n 1015,1049p` shows `else` at 1045, the echo at 1046 and `fi` at 1047. AC2 only requires the check-arms.py line to be above 1046 and below 1049. An arm inserted between the echo and the `fi`, inside the else-branch, therefore passes. AC2's 'Red when ... inside the 28-32 block' does not catch that case, even though S2 and §4 name the `fi` as the bound. The effect is contained: in gov's tree that else-branch never runs, so TOOL-50's New arm would see its ok line missing. | sound | anchor-literal-resolves-above-its-target |
| 16 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 6 AC1 | medium | low | confirmed | TOOL-51 AC1 (pinned blob, lines 293-297) says 'the first line reading `TOOL-dSafePassage-4`' and spells no match command. `TOOL-dSafePassage-4` is a string prefix of `TOOL-dSafePassage-43` (order 2, which S1 requires to commit first) and of -44 to -49. So the natural unanchored or prefix grep resolves to TOOL-43's commit and goes red on a correct history. Read plainly, 'reading' suggests a whole-line match, and the finding's point about the S1 hand-out is shaky because that probe reads header orders, not trailers. The risk is a false red only, never a false pass, so graded low. | sound | - |
| 17 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S9 Readers / section 4 Inventory | medium | low | confirmed | `git grep -n UNLISTED_EXECUTOR_KEYS` shows TOOL-49's spec minting the constant in upgrade_steps.py (S8 :163, §4 :269, Inventory :290, Alternatives :323, §7 :417). TOOL-49 is at order 13 and TOOL-51 at order 14. TOOL-51 S9's Readers line uses READER NOT IN TREE 'at the base'. memory/TEMPLATE-SPEC.md:444 reserves that escape for 'a name that lives outside this tree', and this name lives in this tree's specs and, if TOOL-49 builds as written, in its code. TOOL-51's Inventory lists no retirement, and AC6 greps only tools/govkit/upgrade_steps.py. This is mitigated: TOOL-49's hands-off bullet to TOOL-51 already says 'no UNLISTED_EXECUTOR_KEYS in the module', and a stale reference left in selftest.py would fail loudly. What remains is mainly the census record and a possible stale help or prose mention. | sound | - |
| 18 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S6 / section 4 'The walk, in sequence' | medium | medium | confirmed | TOOL-51 S6 and the §4 walk call `os.path.isjunction` unconditionally. That function was added in Python 3.12, and the spec states no floor and no feature detection. govkit's own floor is CPython 3.11: tools/govkit/govkit.py:104-112 gates on tomllib '3.11+', and upgrade_steps.py imports from govkit.py. On 3.11 the walk raises AttributeError at the first entry under .git/modules/. That is a Traceback on every target with submodules, which AC4 forbids. The repo feature-detects in the same situation: tools/memory-recall/selftest.py:347-349 ('this kit ships to adopters whose python this repo does not pick') and tools/memory-tree/deviation_join.py:1264. The effect is a loud crash on older interpreters, with no wrong result, so graded medium. | sound | - |
| 19 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S12 | medium | low | confirmed | Re-ran `git grep -n "What a step can reach"` over the spec directory. These criteria each run a whole-page `git grep ... -- help/upgrade-steps.md` and then assert what "the section" names: TOOL-7 AC8 (:294-295), TOOL-24 AC5 (:157-158), TOOL-29 AC5 (:191-192), TOOL-36 AC3 (:139-140), TOOL-37 AC4 (:172-173), TOOL-38 AC4 (:168-169) and TOOL-42 AC12 (:347-348). Spec-51 S12 (:144-149) calls §4's awk line "the one probe for the section". It reads only TOOL-47 AC4, TOOL-48 AC3 and TOOL-49 §4/S17/AC12 as citing it, so a required term placed elsewhere on the page keeps those criteria green. No non-goal withholds this, and S12 does not already say it. The page and its module are unbuilt (help/ holds only README.md, measure-legs.md and roles.md), so these criteria have not run yet. Graded low: each is a docs-placement check, and a miss means a term sits on the right page but in the wrong section. | sound | - |
| 20 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 2 S4 / section 4 Rollout and Files touched | low | low | confirmed | Read tools/memory-tree/kit-dogfood-parity.test.sh. Line 61 sets PAIRS to four live:template pairs (HYGIENE.md, TEMPLATE-SPEC.md, guides/BUILD-METHOD.md, guides/ANNOTATION-STYLE.md). The loop at :356-379 runs `render "$ship" > "$live"` for every pair under --render. Spec-52 S4 routes the repair through that render, but §4 Rollout (:129-134) and Files touched (:136-141) name only memory/TEMPLATE-SPEC.md as its output. So the stated write set understates what the command writes. Graded low: the unguarded-by-path `kit/dogfood doc parity` leg keeps the other three in parity on main, so normally the render rewrites them byte-identical and no extra file changes. Only drift present when the pass runs would fold extra rewrites into the commit. | sound | - |
| 21 | blast-radius | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 7 ('This unit adds no arm and moves none') vs section 4 Files touched | low | low | confirmed | Spec-52 lists `tools/push-main.test.sh` in Files touched (:138) and in the Rollout write set (:130). S3 and AC2 make a misplaced arm or a second scan line red, so a repair would move or edit the arm. Yet §7 (:193) says "This unit adds no arm and moves none" and carries no `New arm:` line. memory/TEMPLATE-SPEC.md:550 requires a `New arm:` line "per arm this unit adds or moves". gate-legs.json shows `harness arms (fail branches armed or pinned)` (argv check-arms.py --check) with no guard, and it is absent from the leg line. It runs on every change anyway, so leaving it off loses no coverage. The finding is true but limited to the spec's own consistency. | sound | - |
| 22 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 4 "The walk, in sequence" (S6 lines `try: entries = subdirectories of d` / `except OSError: refuse d`) | blocker | blocker | confirmed | Spec-51 §4 (:198-200) lists d inside `try ... except OSError: refuse d`, and :208 recurses `walk(c/modules)` for every sound candidate. I re-probed with `python -c`: `issubclass(FileNotFoundError, OSError)` printed True, and os.scandir on a missing directory raised FileNotFoundError. A submodule's git directory holds `modules/` only when it has nested submodules, and the target's own `<git_dir>/modules/` is absent when it has no submodules. tools/govkit/upgrade_steps.py does not exist yet, so the walk will be built from this pseudo-code. Built as written, it refuses almost every target and every superproject with ordinary submodules. That contradicts TOOL-47 §5 (:150) and TOOL-36 §5 (:117-118), both of which say no `modules/` yields no candidate, and TOOL-47 AC1, which expects exit 0. The common-case result would be wrong, so this is a blocker. | sound | - |
| 23 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S6 and section 4 "The walk, in sequence" | high | medium | confirmed | In spec-51 §4, the link test (:202) runs only on the entries listed inside d, and :208 calls `walk(c/modules)` with no test on c/modules itself. The root `<git_dir>/modules` is never tested either. My scratch probe made a junction m/a/loop -> m. A path through it, `m/a/loop/a`, read islink False, isjunction False and isdir True. So once the walk enters a junction at `<candidate>/modules`, no entry below it reads as a link and the walk follows it. That makes §5's claim (:277) that S6 stops the walk leaving `.git/modules/` through a link false on this path, and AC4's name-segment plant cannot show it. Graded medium, not high. The walk only spawns read-only `config --list`, and a loop most likely ends in an OSError from path length or reparse limits, which the spec turns into a refusal. The effect is extra reads or an odd refusal, not a pass that skips grading or a hole. | sound | - |
| 24 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 4 "The walk, in sequence" (`entries = subdirectories of d  # never following a link`) vs S6 | medium | medium | confirmed | Spec-51 :199 defines the population as `subdirectories of d  # never following a link`, and only those entries reach the link test at :202. S6's prose (:104) says any link under `modules/` is refused. My scratch probe on Windows found a junction lists as `is_dir(follow_symlinks=False)` True, so the junction plant is caught. But by the documented os semantics, a POSIX directory symlink reads False under `is_dir(follow_symlinks=False)`, and a dangling link fails every isdir filter. A builder who filters that way skips such a link silently instead of refusing it. Git follows a symlinked `.git/modules/<name>`, so that submodule config would go ungraded. That is a real but narrow, builder-dependent gap, so medium. | sound | - |
| 25 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S15 | low | low | refuted | (3) The premise is false when re-probed. The first half is true: in a scratch repo I made `.gitmodules` a native symlink to `../target.gm`. `os.lstat` showed S_ISLNK True, `os.stat` showed S_ISREG True, and `git config -f .gitmodules -z --get-regexp '^submodule\..*\.path$'` read the target with rc=0. So S15's test (spec-51:165-168) does accept the link. The claimed consequence does not reproduce. Git does refuse to put such a link in the index (`git add .gitmodules` gave `error: invalid path '.gitmodules'`, rc=128, git 2.54.0.windows.1). But when git reads the worktree's submodule config, it follows the link: after I staged a gitlink at `outside`, `git submodule init` printed `Submodule 'x' (...) registered for path 'outside'` from the target's contents. So the `config -f` read grades the same file git acts on. It is not some file git would ignore. S6's refusal of links is a different rule, aimed at walk loops under `.git/modules`, and its existence does not make this a defect. | unsound | - |
| 26 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 2 S4 and section 4 "Files touched" / "Rollout" | medium | low | confirmed | The text claim is true. tools/memory-tree/kit-dogfood-parity.test.sh:61 lists four PAIRS (HYGIENE, TEMPLATE-SPEC, guides/BUILD-METHOD, guides/ANNOTATION-STYLE), and its `--render` loop writes every pair with `render "$ship" > "$live"`. spec-52 S4 (:69-72), Files touched (:136-141) and the order-13 M6 write set (:129-134) name only `memory/TEMPLATE-SPEC.md` as a render output. The consequence is narrower than claimed, though. `kit/dogfood doc parity` is a bar leg (tools/gate-legs.json:437-440), so at a green base the other three live copies already equal their render, and re-rendering them writes the same bytes with no diff. A failed render is loud: the script prints `kit-parity: FAILED to write`, sets st=1, and the parity leg would then go red on the truncated copy. What remains is an incomplete write-set and Files-touched statement, which affects behaviour only on a tree that has already drifted. | sound | - |
| 27 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 6 AC1 | medium | medium | confirmed | I re-ran both halves of AC1 at HEAD, before any build. The first printed `rc=[memory-tree]` then `ok-branch`, rc=0. The second printed `bash: line 1: _mt_rc: unbound variable`, rc=127. `grep -n check-arms.py tools/push-main.test.sh` matches nothing, because the arm does not exist yet. AC1 evaluates the scan line and a guard it types itself, plus a synthetic two-line script. It never reads TOOL-50's arm or the suite. So it is green before the unit is built and cannot fail, even though its 'Red when: the arm's guard would take its skip branch' claims to observe the arm. The damage is limited because the arm's own `New arm:` ok line is observed elsewhere (S1, spec-52:50-52). | unsound | - |
| 28 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md:section 6 AC2 and section 4 "The arm's place, by content" | medium | medium | confirmed | I re-ran the grep. It printed 873 `_mt_rc=...`, 1046 `  echo "  skip — 28-32 ..."` and 1049 `[ "$fail" = 0 ] ...`. `sed -n 1040,1052p` shows `else` at 1045, the echo at 1046 and `fi` at 1047. AC2 (spec-52:174-177) only requires the arm's first `check-arms.py` line to be greater than the skip-echo line and the scan, and less than the final line. An arm placed at line 1047, after the echo and before the `fi`, is inside the else-branch and still passes. That contradicts the 'Red when: ... inside the 28-32 block' clause. An edit to the skip message would leave the probe with no line to compare against. On that narrow path the arm never runs in gov's tree and AC2 certifies the placement anyway. The arm's missing ok line elsewhere would expose it, so the effect is contained. | sound | - |
| 29 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md:section 2 S3 (vs S2) and section 6 AC2 | low | low | confirmed | S2 (spec-51:71-72) requires the phrase 'in these words and on one line'. S3 (:76) asks only that the amended TOOL-43 Rollout 'says `TOOL-dSafePassage-4 builds at order 3`' and gives no line constraint. AC2 (:300-303) uses a line-local `git grep -c 'TOOL-dSafePassage-4 builds at order 3'` over all three specs. The TOOL-43 Rollout today wraps its sentence (`git grep` shows spec-43:118 'TOOL-dSafePassage-4, also at order 2, writes its moves through this rule, so M6 clause 2', continued on the next lines). So a wrapped amendment that is otherwise correct would print 0 for that file, a false red. That red is loud and caught before merge, so this is wording only. | sound | ledger-token-wrapped-across-a-line-joins-nothing |
