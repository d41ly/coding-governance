**Serves:** journal TOOL-aMendedFleet-93

# Tier-2 closing diff review — aWindowedPass, ROUND 1

*The closing review of build aWindowedPass. It covers the cumulative diff of units TOOL-aWindowedPass-1..5 landing on `main`, at the integration boundary. The report was synthesized from a workflow-orchestrated find, verify and synthesize run on 2026-10-06 and filed under aMendedFleet's build folder.*

Reviewed range: `886b089dfd9c4bf98dc2024e21d7d9607f9b5cc0...e252bafb3fe306e0118c2771ef627b865528e895`

## Verdict: BLOCKED

Two confirmed findings carry a binding grade of blocker (ids 4 and 22). Both are the same defect: the memory-tree kit's unconditional `{memory_root}/backlog` `[[generated]]` rows collide with the default and example `SHARED_RECORDS`, so an adopter's driver refuses at load. A third report of that defect (id 10) is bound at high, so the grading disagrees with itself; see B1 and H1. The tally is 22 items: 1 blocker, 3 high, 12 medium, 6 low. By raw confirmed finding it is 27: 2 blocker, 4 high, 15 medium, 6 low.

## Review shape and run integrity

- **Round:** 1. **Intensity:** full. **Raw** 29, **confirmed** 27, **refuted** 2 (both duplicates, ids 11 and 12), **unverified** 0 (0 uncertain). **Precision** 0.93.
- **Adjudicated tally.** By item it is 22: BLOCKER 1, HIGH 3, MEDIUM 12, LOW 6. By raw confirmed finding it is 27: BLOCKER 2, HIGH 4, MEDIUM 15, LOW 6.
- **Lenses:** 5/5 returned, 0 died. **Skeptic batches:** 5/5 returned, 0 died. No verdicts were demoted for contradiction, none were discarded as spurious, and no duplicates were dropped by the harness.
- **Fixes on confirmed findings:** 19 judged sound, 8 judged UNSOUND, 0 none proposed, 0 NOT JUDGED. Where a fix was judged unsound, this report gives the skeptic's corrected fix and never the rejected one.
- **Severity:** 0 confirmed findings were left ungraded by the skeptic. 6 were RE-GRADED by the skeptic (ids 1, 2, 10, 13, 14, 15).
- **Lens notes:** none supplied, so every lens ran on the kit's generic brief.
- **Intent:** neither `specs` nor `context` was supplied to the run. The lenses had only the range's commit messages to judge intent from, although several intent-lens findings cite the spec text they read in the tree.
- **Checklist:** NONE swept. The project's recurring-bug-class checklist was absent from this run, so the zero count of checklist hits is not evidence that those classes are absent.
- Every lens and skeptic batch returned, so the run is complete as a run. The finding set is complete only to the extent that five generic-brief lenses can make it.

## BLOCKER

### B1 — memory-tree's `{memory_root}/backlog` rows collide with the default and example SHARED_RECORDS (ids 4, 22)

- **Where:** `tools/memory-tree/kit.toml:424`, `tools/unattended/.unattended.conf.example:377`, and the `resolve_shared_records` default in `tools/unattended/lib-unattended.sh` (about line 508).
- **Defect:** `tools/memory-tree/kit.toml` declares two unconditional `[[generated]]` rows for `{memory_root}/backlog`. `resolve_generated_indexes` merges every tracked `tools/*/kit.toml`. The shipped example conf sets `SHARED_RECORDS="memory/DECISIONS.md memory/backlog"`, and an undeclared key defaults to `$M/DECISIONS.md $M/backlog`. `scan_shared_index_overlaps` therefore finds `memory/backlog` under both keys.
- **Impact:** for any adopter with memory-tree installed and the example or default SHARED_RECORDS, `unattended.sh` exits 2 at conf load on every verb, `--check-commit` included, and check 38 reds the bar. Gov escapes only because its own conf already dropped backlog from SHARED_RECORDS. The fixtures carry no memory-tree `kit.toml`, so no suite catches this.
- **Fix (skeptic-corrected; both finders' proposals were judged UNSOUND):**
  - Keep `memory/backlog` in SHARED_RECORDS, in both the default and the example.
  - Make both backlog rows conditional, for example with `when = ".memory-tree.conf:BACKLOG_MODE=builds"`.
  - Teach `resolve_generated_indexes` and govkit 6c to read that key from the named conf and to skip the row unless it matches.
  - Do NOT drop the rows: gov runs `BACKLOG_MODE=builds` with `GENERATED_INDEXES=""` and relies on them.
- **Left-shift gate:** add a check-unattended arm that loads every real `tools/*/kit.toml` against the example conf's SHARED_RECORDS and against the kit default, and asserts no overlap. Add a `BACKLOG_MODE=builds` control asserting that the rows do apply there.

## HIGH

### H1 — the same backlog collision, bound at high (id 10)

- **Where:** `tools/memory-tree/kit.toml:424`.
- **Defect and impact:** the same as B1. The skeptic re-graded this report from blocker to high because the driver fails closed with a message naming the remedy, and it neither ships a wrong result nor certifies an unchecked change.
- **Grade note:** the binding grades disagree. Ids 4 and 22 are blocker and id 10 is high, all for one defect. Under the rubric, I judge high to be the right grade for all three: a fail-closed refusal is not a wrong result, a security hole, data loss or a false certification. The binding grades stand as given, so the verdict stays BLOCKED.
- **Fix:** the skeptic judged the finder's fix SOUND here: drop `backlog` from the `resolve_shared_records` default and from the example's SHARED_RECORDS. **This conflicts with B1's corrected fix,** which two other skeptics reached by rejecting exactly that change. Dropping backlog from SHARED_RECORDS is wrong for an adopter whose backlog is authored, not generated (any `BACKLOG_MODE` other than builds). Take B1's conditional-row fix. The later commit `e4abc55bf` adopts that shape too.
- **Left-shift gate:** the same arm as B1.

### H2 — check 23's negative arms cannot fail since the per-run grading (ids 13, 14)

- **Where:** `tools/unattended/check-unattended.test.sh:3466`, and the `Pass:` trailer arm at `:3724`.
- **Defect:** `check 23 FAILED` is printed only for a counted overlap in a run bound to the checked-out branch. These arms dispatch one unit through plain `drow` on a record with no `run-branch`. A single-unit run is always SOLO and an unbound run prints OTHER RUN, so `miss "check 23 FAILED"` cannot fire. The affected arms are at 3466, 3602, 3633, 3672, 3714, 3774 and 3842, plus F's second miss at 3658. The arm for pass_commit's `Pass:` trailer attribution (TOOL-aWindowedPass-2, at 3724) has the same shape: remove the `[ -n "$_ptr" ]` branch and the records commit would print SOLO, never FAILED.
- **Impact:** regressions to `covers` normalisation, the supersede fold, windowing or trailer attribution would leave the suite green. Nothing that can fail covers pass_commit honouring `Pass: none`.
- **Fix (judged SOUND):**
  - Dispatch each negative arm through `odrow`, which binds the run and adds an overlapping sibling.
  - Alternatively, assert something that can still fire, such as `miss "$out" "wrote <path>"`, or for 3724 `miss "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)" "wrote notes/records.md"`.
  - Watch the trailer arm go red with the `_ptr` branch removed.
- **Left-shift gate:** a suite self-scan that reds any `miss ... check 23 FAILED` arm whose fixture neither binds the run nor dispatches a sibling. This is the vacuous-assertion class, gated rather than remembered.

### H3 — `--check-commit` lists a staged rename by its destination only (id 23)

- **Where:** `tools/unattended/unattended.sh:9742`.
- **Defect:** porcelain `git diff --cached --name-only` applies `diff.renames`, which is on by default, so it lists only a rename's destination. Check 23 at the close uses `diff-tree --name-only -r`, which does no rename detection and lists the deleted source too.
- **Impact:** a `git mv` of an undeclared file into a declared path passes the commit-time step. Check 23 then counts the source at the close, when `--dispatch` can no longer widen the declaration. The commit-time check certifies a commit that the close grader then rejects.
- **Fix (skeptic-corrected; the finder's proposal was judged UNSOUND):** use `st=$(git diff --cached --no-renames --name-only)` or `git diff-index --cached --name-only HEAD`. Keep newline separation for the existing `for p in $st` loop rather than switching to `-z`.
- **Left-shift gate:** an arm that stages a `git mv` from an undeclared path into a declared one, and expects rc 1 naming the source.

## MEDIUM

### M1 — a pass can exempt itself by editing a kit descriptor (id 1)

- **Where:** `tools/unattended/lib-unattended.sh:552`.
- **Defect:** `resolve_generated_indexes` reads `[[generated]]` rows from the working tree when the check runs. A pass whose declaration includes `tools/foo/` can add a broad row, such as `path = "tools"` with an existing generator, and its own and its siblings' writes go uncounted at commit time and at the close. govkit 6c accepts that row.
- **Grade note:** the skeptic re-graded this from high to medium. The class predates the diff, because a pass could already edit the working-tree `.unattended.conf` the same way. The diff adds a parallel route, not a new capability.
- **Fix (skeptic-corrected; the finder's proposal was judged UNSOUND):**
  - Make check 23 and `--check-commit` both resolve the kit rows from the run's recorded base (`git show <base>:<kit.toml>`), so rows added during a run never exempt that run's own writes.
  - Fall back to the conf pairs alone when the base does not resolve.
  - In govkit 6c, refuse a row whose resolved path is a bare root (`{memory_root}`, `{map_root}`, `{kit}`, a top-level directory) or that covers any `kit.toml` or generator source.
- **Left-shift gate:** an arm where a pass adds a `[[generated]]` row mid-run and writes under it, expecting the write to be counted. A govkit selftest staging a bare-root row, expecting 6c red.

### M2 — `--check-commit` reads trailer and subject differently from the close (ids 3, 25)

- **Where:** `tools/unattended/unattended.sh:9720`.
- **Defect:**
  - `sed -n 's/^Pass: *//p'` is case-sensitive. The close's `%(trailers:key=Pass)` is not.
  - Any `none` token short-circuits the check, while pass_commit attributes `TOOL-x-1 none` to TOOL-x-1.
  - The subject is taken as the first non-blank line, while `%s` joins the whole first paragraph.
- **Impact:** a `pass: TOOL-x-1` trailer, a mixed `Pass: TOOL-x-1` plus `Pass: none`, or a unit id on a wrapped subject line each passes the commit-time step without the subset test. The close then attributes the commit to the pass and counts the stray write, when it is no longer repairable.
- **Fix (judged SOUND):**
  - Derive the trailer case-insensitively, for example `git interpret-trailers --parse | sed -n 's/^[Pp][Aa][Ss][Ss]: *//p'`.
  - Return 0 only when `none` is the sole value, and grade every other id.
  - Take the subject as the joined first paragraph.
  - Better still, derive both through the tokeniser that `log_attribution_tokens` uses.
- **Left-shift gate:** a parity arm that feeds one message set (lowercase key, mixed none, wrapped subject) both to `--check-commit` and to a committed fixture graded by check 23, and asserts the two agree on attribution.

### M3 — the rename-detection divergence, bound at medium (id 5)

- **Where:** `tools/unattended/unattended.sh:9742`.
- **Defect and impact:** the same as H3, reported by the correctness lens and bound at medium because the close still catches the write.
- **Grade note:** H3 carries the same defect at high. Medium fits the rubric better here, since the effect is contained to a lost early repair.
- **Fix (judged SOUND):** `git diff --cached --no-renames --name-only`, or `git diff-index --cached --name-only HEAD`.
- **Left-shift gate:** the same arm as H3.

### M4 — `git commit --amend` of a pass commit is refused (ids 6, 26)

- **Where:** `tools/unattended/unattended.sh:9749`.
- **Defect:** during an amend, HEAD is the pass commit, so `check_pass_open` reports the row closed and the hook refuses with "has no open dispatched pass ... declare it first".
- **Impact:** an ordinary amend is blocked. Following the printed `--dispatch` remedy anchors a row at a commit the amend then orphans, and switching to `Pass: none` drops the attribution.
- **Fix (judged SOUND):** detect the amend. When HEAD's own Pass trailer names the unit and pass_commit for that row is HEAD, grade the index against `HEAD^` using that row's declaration. Alternatively, evaluate openness over `<anchor>..HEAD^`.
- **Left-shift gate:** an amend arm that commits a pass, amends it carrying the same trailer and a declared path, and expects rc 0. Add a control amend adding an undeclared path, expecting rc 1.

### M5 — check 23's ambiguity test reads the subject of a trailered commit (ids 7, 24)

- **Where:** `tools/unattended/check-unattended.sh:3770`.
- **Defect:** the guard reads `%s` and matches sibling ids against it. pass_commit now attributes a trailered commit by its trailer alone.
- **Impact:** a commit trailered `Pass: TOOL-x-3` whose subject mentions sibling TOOL-x-1 is called ambiguous and skipped, so its undeclared writes are never graded. In the other direction, a `Pass: A B` trailer is attributed to both units and is not flagged.
- **Fix (judged SOUND):** test siblings against `log_attribution_tokens -1 "$dshit"`, which gives the trailer ids when present and the subject otherwise.
- **Left-shift gate:** two arms. A trailered commit whose subject names a sibling must be graded, not called ambiguous. A `Pass: A B` commit must be flagged ambiguous.

### M6 — widening arm B never binds the run and is red (id 15)

- **Where:** `tools/unattended/check-unattended.test.sh:3611`.
- **Defect:** the arm hits the bound-run `fail 23` text, but it runs `reset_tree; drows ...; drow ARCH-tRun-9` with no `bindrun`. The checker prints OTHER RUN instead.
- **Impact:** the suite is red, and the property "a superseding row is still graded" has never been observed passing under the new grading.
- **Grade note:** the skeptic re-graded this from high to medium, because the production grading is correct.
- **Fix (judged SOUND):** add `bindrun` after `reset_tree`, confirm the arm goes green, then confirm it goes red with the supersede fold broken.
- **Left-shift gate:** the H2 self-scan, extended to `hit` arms on bound-run text.

### M7 — the truncated-subject-cache arm's staged break is a no-op (id 16)

- **Where:** `tools/unattended/check-brief-recorded.test.sh:509`.
- **Defect:** the arm seds `| tr -c` in the copied leg. That pipeline moved into `log_attribution_tokens` in lib-unattended.sh, so the sed changes nothing and rc 2 cannot occur.
- **Impact:** the arm is red, and no staged break exercises the `_SUBJ` size refusal.
- **Fix (judged SOUND):** truncate the feed instead, rewriting `done < <(log_attribution_tokens HEAD)` to append `| head -n -1`. Before asserting rc 2, assert that the sed changed the file.
- **Left-shift gate:** a shared `mutate` helper that fails the arm when its edit matched nothing, so every staged break proves it was staged.

### M8 — adopter arm 10 expects a GENERATED_INDEXES pair the example no longer ships (id 17)

- **Where:** `tools/unattended/adopt-unattended.test.sh:637`.
- **Defect:** the shipped example now sets `GENERATED_INDEXES=""`, but arm 10 still expects the stamped `{{MEMORY_TREE_DIR}}` pair. The adopter suite is red.
- **Fix (skeptic-corrected; the finder's proposal was judged UNSOUND):**
  - Assert that `GENERATED_INDEXES=""` survives the stamp unchanged.
  - Keep GENERATED_INDEXES in `STAMP_RE`.
  - Add a separate arm that stamps a conf carrying a `{{MEMORY_TREE_DIR}}` pair, and asserts it resolves to `${TR_T}${MT_KIT}/gen_build_index.py`.
- **Left-shift gate:** the separate stamp arm keeps the `STAMP_RE` path exercised whatever the example ships.

### M9 — the commit-msg hook's new block has no behavioural arm (id 18)

- **Where:** `.githooks/commit-msg:46`.
- **Defect:** the hook now calls `--check-commit` ahead of the MERGE_HEAD exit, blocks only on rc 1, and announces any other code. No test drives it. F10's fixture has no unattended kit, check-wiring uses a stub, and unattended.test.sh calls the verb directly.
- **Impact:** moving the call below the merge-only exit, mis-mapping rc, or breaking the kit probe would leave every suite green.
- **Fix (judged SOUND):** install `.githooks/commit-msg` in the fixture repo. Make a real `git commit` with a `Pass: <unit>` trailer that stages an undeclared path, and assert it is refused. Add a control with no conf, where the commit lands.
- **Left-shift gate:** that arm.

### M10 — the fail-closed overlap path has no arm (id 19)

- **Where:** `tools/unattended/check-unattended.sh:3835`.
- **Defect:** when the record's base does not resolve, every pass is counted as overlapped and `check 23 overlap unavailable` is reported. No fixture sets an unresolvable base.
- **Impact:** changing this branch to treat every pass as solo would stop grading an unplaceable record, and nothing would red.
- **Fix (judged SOUND):** bind the run, give it a single unit with a stray write, and set `base:` to a sha absent from the clone. Assert `check 23 FAILED` and the `overlap unavailable` line.
- **Left-shift gate:** that arm. The later commit `e4abc55bf` (M7 there) adds it.

### M11 — three `--check-commit` branches have no arm (id 20)

- **Where:** `tools/unattended/unattended.sh:9752`.
- **Defect:** these branches are not exercised:
  - the brief-row subtraction (`read_brief_paths` over the index);
  - the gen-region-only subtraction (`check_gen_region_only "HEAD:$p" ":$p"`), whose index-side `:$p` spelling is exercised nowhere;
  - the refusal for a trailer naming a unit with no open pass (9749).
- **Fix (judged SOUND):** extend the unattended.test.sh `--check-commit` block with:
  - a staged brief file with its `brief · item` row, expecting rc 0;
  - a README edit confined to a gen region, expecting rc 0, plus a control edit outside the region, expecting rc 1;
  - `Pass: ARCH-tRun-7` with no dispatch row, expecting rc 1 and the "no open dispatched pass" text.
- **Left-shift gate:** those arms.

### M12 — a record with no branch fact is promised a close that never comes (id 27)

- **Where:** `tools/unattended/check-unattended.sh:3899`.
- **Defect:** when a live record has neither `run-branch` nor `branch-ref`, `dsrb` is empty. No checkout can bind it, yet the OTHER RUN line says its counted writes are "graded at its own close". `memory/builds/aCollapsedScan/RUN.md` is such a record today.
- **Impact:** those counted writes are never failed anywhere, while the output claims a later grading. Before this diff, the repo-global ceiling counted them.
- **Fix (judged SOUND):** when `dsrb` is empty, print a distinct line, such as `check 23 UNBOUND <run>: <n> counted, no run branch recorded, so no close binds it`, or fail the check.
- **Left-shift gate:** an arm with an unbound live record and a counted write, asserting the UNBOUND line, or the failure if that route is chosen.

## LOW

### L1 — comments promise check 23 grades `Pass: none` commits; it does not (id 2)

- **Where:** `tools/unattended/unattended.sh:9705`, and `.githooks/commit-msg` lines 35 and 48.
- **Defect:** pass_commit attributes a `Pass: none` commit to no unit, which is the TOOL-aWindowedPass-2 design. The comments say check 23 "still grades" such commits.
- **Grade note:** the skeptic re-graded this from high to low. The behaviour matches the base; only the stated backstop is false.
- **Fix (skeptic-corrected; the finder's proposal was judged UNSOUND):** correct the verb header and the hook text to say that check 23 does not grade a `Pass: none` commit. Say that only the non-failing dodged-join line observes declared paths moving without an attributed pass commit.
- **Left-shift gate:** none fits. This is a documented check, to be added to the project's §10 checklist as "a comment naming a backstop must name the function that is the backstop".

### L2 — case-sensitive trailer key, bound at low (id 8)

- **Where:** `tools/unattended/unattended.sh:9720`.
- **Defect:** the case-sensitivity half of M2.
- **Grade note:** M2 carries the same defect at medium. The lens bound this one at low on the reading that the hook only re-asks for a trailer, but the skipped subset test makes medium the better fit.
- **Fix (judged SOUND):** `sed -n 's/^[Pp][Aa][Ss][Ss]: *//p'`, or `awk` with `tolower` on the key.
- **Left-shift gate:** the M2 parity arm.

### L3 — stale ceiling text and a misplaced build_commit header (id 9)

- **Where:** `tools/unattended/check-unattended.sh:3871` ("the ratchet below decides the verdict"), the EXCLUDED message at `:3682` ("not graded against the ceiling"), and `tools/unattended/lib-unattended.sh`, where new comment blocks were inserted between build_commit's header and `build_commit()`.
- **Fix (skeptic-corrected; the finder's proposal was judged UNSOUND):**
  - Reword the check 23 comment and the EXCLUDED message to describe per-run grading against zero.
  - In lib-unattended.sh, keep the gen-region comment, `GEN_REGION_AWK` and `check_gen_region_only` together.
  - Put the `log_attribution_tokens` comment directly above `log_attribution_tokens()`.
  - Put the whole build_commit header directly above `build_commit()`.
- **Left-shift gate:** a grep leg that reds on `ceiling` in check-unattended.sh outside the `RETIRED_CONF_KEYS` line, since the key is retired.

### L4 — govkit selfcheck 6c's other failure conditions are never staged (id 21)

- **Where:** `tools/govkit/govkit.py:1987`.
- **Defect:** the only arm stages a missing generator. A bad path token, an empty path and a missing `why` are never staged.
- **Fix (judged SOUND):** add two staged breaks to the aWP-4 AC5 block in selftest.py, a `path = "{nope}/x"` row and a row with `why` removed. Assert each reds 6c and is green once restored.
- **Left-shift gate:** those arms.

### L5 — the hook skips silently when the conf exists but the kit does not (id 28)

- **Where:** `.githooks/commit-msg:44`.
- **Defect:** spec 3 promises an announced skip. When `.unattended.conf` exists and no `unattended.sh` is found, the hook prints nothing.
- **Fix (judged SOUND):** after the probe loop, if the conf exists and no kit was found, echo a one-line notice that the unattended commit-time check was skipped.
- **Left-shift gate:** fold it into the M9 arm as a control with the conf present and the kit absent, asserting the notice.

### L6 — the effective generated set is never reported, and the README omits `[[generated]]` (id 29)

- **Where:** `tools/unattended/lib-unattended.sh:527`.
- **Defect:** spec 4 §5 promises that check 23 prints the effective set with each pair's source, and that the kit README describes the row shape. Neither was built.
- **Fix (skeptic-corrected; the finder's proposal was judged UNSOUND):**
  - Emit `report "check 23 generated outputs: $GENERATED_INDEXES"` at a point after `report()` is defined, for example at the head of check 23 beside `DS_HEAD_REF`.
  - Ideally, note for each pair whether it came from a `kit.toml` or from the conf.
  - Add a README paragraph covering the `[[generated]]` keys (`path`, `generator`) and the `{memory_root}`, `{map_root}` and `{kit}` tokens.
- **Left-shift gate:** an arm asserting that the report line appears under `GOV_UNATTENDED_REPORT=1`.

## Cross-cutting notes

- **Commit-time and close disagree.** Four items (H3, M2, M4 and L2) are one class: `--check-commit` re-derives what the close derives, by a different reader. The durable fix is one shared reader for both. Short of that, the left-shift is the M2 parity arm, generalised to staged path set, trailer, subject and openness.
- **Vacuous negative arms.** Three items (H2, M6 and M7) are the could-not-fail class that §7 names. Each passed review because nobody watched it go red. The self-scan in H2 and the `mutate` guard in M7 gate the class rather than the instances.
- **The later fix commit.** Several why-real notes cite the later commit `e4abc55bf` (closing review r1) as having addressed B1, H3, M2, M4 and M10. That commit lies outside the reviewed range, and this report does not verify it.

review-shape kind=diff-review round=1 intensity=full at=synth raw=29 confirmed=27 refuted=2 unverified=0 blocker=2 high=4 medium=15 low=6 agents=11 out-tokens=168018

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/lib-unattended.sh:552 | high | medium | confirmed | At e252baf, resolve_generated_indexes lists the tracked tools/*/kit.toml files with ls-files, then awk-reads each one from the working tree ($_rg_root/$_rg_d). Check 23 (check_generated_render) and verb_check_commit both forgive any path a resolved row covers. So a pass that may write tools/foo/kit.toml can add a broad [[generated]] row, for example path="tools" with generator set to a file the kit already ships, and its own and its siblings' writes go uncounted. govkit 6c checks only the tokens, that the generator exists and that why is non-empty, so it accepts the row. The diff did make this route reachable. The class is not new, though: at base GENERATED_INDEXES came from the working-tree .unattended.conf, which a pass could edit the same way to exempt itself. The diff adds a parallel route rather than a new capability, and it needs a deliberately broad row. Contained, so medium. | unsound | - |
| 2 | security | tools/unattended/unattended.sh:9705 | high | low | confirmed | In pass_commit, a commit with any Pass: trailer is attributed only by that trailer: case " none " does not contain the unit, so the loop continues. A Pass: none commit is therefore never a unit's pass commit, and check 23 never subset-tests it. If no commit names the pass, the dodged-join branch only printfs. So the comment at unattended.sh 9704-9705 ("`Pass: none` is taken at its word. Check 23 still grades both at the close") is false for Pass: none, and so is the commit-msg hook's line-48 fallback wording when it reaches a Pass: none commit. The behaviour itself is by design: TOOL-aWindowedPass-2 says Pass: none names no unit. It is also equivalent to the base, where a commit whose subject did not name the unit was equally ungraded. The defect is a misstated backstop in comments, with no change in behaviour. | unsound | - |
| 3 | security | tools/unattended/unattended.sh:9720 | medium | medium | confirmed | verb_check_commit builds trl with `git interpret-trailers --parse \| sed -n 's/^Pass: *//p'`, which is case-sensitive. I confirmed on git 2.54 that --parse keeps a lowercase `pass:` key as written. git log's %(trailers:key=Pass), which pass_commit and log_attribution_tokens use, matches the key case-insensitively. A message trailed `pass: TOOL-x-1` with a subject that does not name the unit therefore returns 0 from the hook, yet the close attributes it to TOOL-x-1 and grades it. Separately, `case " $trl " in *" none "*) return 0` short-circuits on any none token, while pass_commit attributes `TOOL-x-1 none` to TOOL-x-1. The commit-time step and the close disagree. The close still catches the write, as it did before this diff, but only once the declaration can no longer be widened. Contained, so medium. | sound | - |
| 4 | correctness | tools/unattended/.unattended.conf.example:377 | blocker | blocker | confirmed | At e252baf, tools/memory-tree/kit.toml declares {memory_root}/backlog as [[generated]] with no condition, in two rows. The resolver reads tools/*/kit.toml beside the unattended kit, and the comment says adopters read the same descriptors. The shipped .unattended.conf.example still sets SHARED_RECORDS="memory/DECISIONS.md memory/backlog", and the resolve_shared_records default is "$2/DECISIONS.md $2/backlog". scan_shared_index_overlaps then reports memory/backlog under both keys. unattended.sh refuses at load with exit 2 on every verb, and check 38 fails. Gov's own conf escapes only because its SHARED_RECORDS omits backlog. The repo's later fix (the closing review r1 B1 comment and test arm) states that every adopter's conf was refused at load. | unsound | - |
| 5 | correctness | tools/unattended/unattended.sh:9742 | medium | medium | confirmed | verb_check_commit collects staged paths with porcelain `git diff --cached --name-only`, which applies diff.renames (default true) and lists only the destination of a staged rename. Check 23 grades the commit with `diff-tree --no-commit-id --name-only -r`, which detects no renames and lists both the deleted source and the new path. If a pass runs `git mv` on an undeclared file into a declared directory, the hook sees only the declared destination and passes. At the close, check 23 counts the deleted source as an undeclared write, after --dispatch can no longer widen the declaration. The scenario is real but narrow, and the close still catches it, so medium. | sound | - |
| 6 | correctness | tools/unattended/unattended.sh:9749 | medium | medium | confirmed | During `git commit --amend` of a pass commit, HEAD is that pass commit when commit-msg runs. check_pass_open calls pass_commit over anchor..HEAD, which finds HEAD with the Pass: u trailer and declared writes, so it returns 1 (closed). rows then omits u, decl is empty, and verb_check_commit refuses with 'has no open dispatched pass ... declare it first'. The refusal blocks an ordinary amend. Following the printed --dispatch remedy anchors a row at a commit the amend then orphans, and switching to Pass: none drops the attribution. --no-verify is the workaround. The effect is a contained false refusal, so medium. | sound | - |
| 7 | correctness | tools/unattended/check-unattended.sh:3770 | medium | medium | confirmed | At e252baf, check 23 reads the pass commit's subject with `dshitsub=$(GIT log -1 --format=%s "$dshit")` and runs `id_in "$dshitsub" "$dssunit"` on each sibling. In the same diff, `pass_commit` was changed to attribute a commit by its `Pass:` trailer alone when one is present. Before this diff both sides read the subject, so a subject naming two siblings really was ambiguous. Now a commit with `Pass: X-3` and a subject that mentions X-2 is selected only for X-3, yet the guard still prints 'one commit names two passes' and `continue`s, so that pass's undeclared writes are never graded. The reverse case also holds. `--check-commit` accepts a multi-id trailer, and `pass_commit` would select a `Pass: A B` commit for both A and B. The guard misses it unless the subject names both, so each unit is graded against the other's writes. I grade this medium: the path is narrow, and the refusal line goes to the default channel instead of failing silently. | sound | - |
| 8 | correctness | tools/unattended/unattended.sh:9720 | low | low | confirmed | `verb_check_commit` does `git interpret-trailers --parse <msg \| sed -n 's/^Pass: *//p'`, which is case-sensitive, and `--parse` keeps the key's case as written. `pass_commit` and `log_attribution_tokens` use `%(trailers:key=Pass)`, which git matches case-insensitively. So a `pass: X` trailer is ignored by the hook but still attributes the commit at the close. The effect is limited. Either the hook asks for a trailer that is already there, and fixing the case clears it, or the staged-path check is skipped and check 23 still grades the pass at the close. | sound | - |
| 9 | correctness | tools/unattended/check-unattended.sh:3871 | low | low | confirmed | At e252baf, line 3871 still says 'the ratchet below decides the verdict', and line 3682's EXCLUDED message still says 'not graded against the ceiling'. This diff retired the ceiling (RETIRED_CONF_KEYS=UNDECLARED_WRITE_CEILING), and that is what made the text stale. In lib-unattended.sh, the `log_attribution_tokens` and `GEN_REGION_AWK` comment blocks were inserted between build_commit's '`index:generator` pairs' header and `build_commit()`. Behaviour is unaffected. | unsound | - |
| 10 | seams | tools/memory-tree/kit.toml:424 | blocker | high | confirmed | At e252baf, tools/memory-tree/kit.toml declares two `[[generated]]` rows with path `{memory_root}/backlog`. `resolve_generated_indexes` reads every tracked `kit.toml` beside the unattended kit, so this is what an adopter gets as well. Meanwhile the example conf still ships `SHARED_RECORDS="memory/DECISIONS.md memory/backlog"`, and `resolve_shared_records` still defaults to `$M/DECISIONS.md $M/backlog`. Right after both resolve, unattended.sh calls `scan_shared_index_overlaps`, prints REFUSING and does `exit 2` before any verb dispatches, `--check-commit` included. Check 38 in check-unattended.sh reports the same overlap. Before this diff the example's GENERATED_INDEXES did not name backlog, so the diff introduced the conflict. Gov's own bar stays green only because gov's .unattended.conf no longer lists backlog under SHARED_RECORDS. I grade this high, not blocker. It fails closed with a message naming the remedy, and it does not produce a wrong result or certify an unchecked change. It still blocks every verb for an adopter on the default or example value. | sound | - |
| 11 | seams | tools/unattended/check-unattended.sh:3770 | high | - | refuted | Duplicate of finding 7: the same subject-based ambiguity guard at check-unattended.sh:3770 against trailer-based `pass_commit` attribution, with the same false-ambiguity scenario and the same fix. Finding 7 also covers the multi-id trailer direction, so I have graded the defect there. | sound | - |
| 12 | seams | tools/unattended/lib-unattended.sh:786 | low | - | refuted | Duplicate of finding 9: the misplaced build_commit header and the `log_attribution_tokens` / `GEN_REGION_AWK` blocks inserted above it are the third part of finding 9, and that finding is confirmed. | sound | - |
| 13 | verification | tools/unattended/check-unattended.test.sh:3466 | blocker | high | confirmed | At e252baf the only thing that prints 'check 23 FAILED' is `fail 23` (check-unattended.sh:3897). It runs only when ds_over_n>0 and the record's run-branch/branch-ref equals DS_HEAD_REF. The PRISTINE tRun RUN.md has no run-branch or branch-ref fact; only `bindrun` adds one. With a single unit, dsposok=2, so dsov=0 and any undeclared write prints a SOLO line rather than being counted. With no base, a counted write in an unbound run prints OTHER RUN. So every cited arm (3466, 3602, 3633, 3672, 3714, 3774, 3842) that uses drow/drows with a single unit and no bindrun, followed by `miss "check 23 FAILED"`, cannot fail. F's second miss at 3658 has two units but is unbound, so it gets OTHER RUN at most. Its first miss, the ambiguity text, is still effective. At base the fixture's UNDECLARED_WRITE_CEILING was 0, so these arms could fire there. This diff made them vacuous, so it is in scope. Production code is unaffected today, but regressions to covers, the fold or the windowing would go undetected. That misleads the next change, so high. | sound | - |
| 14 | verification | tools/unattended/check-unattended.test.sh:3724 | blocker | high | confirmed | The arm (check-unattended.test.sh ~3719-3725 at e252baf) is drow ARCH-tRun-1 (single unit, unbound) followed by `miss "check 23 FAILED"`. If pass_commit's `[ -n "$_ptr" ]` branch (lib-unattended.sh:736-738) were removed, id_in would match the 'records for ARCH-tRun-1..3' subject; the spec comment itself says a range like -1..4 was taken as the pass. The records commit would then be graded and print SOLO with notes/records.md, never FAILED. The no-trailer sibling arm only hits 'ARCH-tRun-1 at', and the build_commit arm exercises log_attribution_tokens, not pass_commit. git grep finds no other test that drives pass_commit with a `Pass: none` commit. unattended.test.sh only feeds message files to --check-commit. So nothing that can fail covers the trailer attribution in pass_commit. | sound | - |
| 15 | verification | tools/unattended/check-unattended.test.sh:3611 | high | medium | confirmed | At e252baf, arm B is `reset_tree; drows ARCH-tRun-1 ...; drow ARCH-tRun-9 ...` with no bindrun. reset_tree restores PRISTINE, whose RUN.md Run facts hold only phase, witness and base. The overlap is counted (ds_over_n=1), but dsrb is empty while DS_HEAD_REF is refs/heads/unit. The checker therefore prints 'check 23 OTHER RUN ...', and the fail-23 text the arm hits ('a pass of the run this branch drives ...') is never printed, so the arm is red. The diff introduced this: it changed the hit text and added the sibling row but not bindrun. The production grading itself is correct. The effect is a red arm and an unobserved property, which is contained, so medium. | sound | - |
| 16 | verification | tools/unattended/check-brief-recorded.test.sh:509 | medium | medium | confirmed | At e252baf, check-brief-recorded.sh fills _SUBJ from `done < <(log_attribution_tokens HEAD)` (line 303) and holds no `\| tr -c`; the pipeline now lives in lib-unattended.sh's log_attribution_tokens. The arm's sed only edits the copied leg, so it is a no-op. The 'ok' fixture leg then exits normally rather than with rc 2, and `same ... "2"` reds. The existing guard checks only the commit count, not whether the edit happened. The _SUBJ size refusal is left unexercised by any staged break. | sound | - |
| 17 | verification | tools/unattended/adopt-unattended.test.sh:637 | medium | medium | confirmed | The shipped .unattended.conf.example at e252baf sets GENERATED_INDEXES="" (line 378); at base it carried the {{MEMORY_TREE_DIR}} pair. Arm 10 in adopt-unattended.test.sh still expects the stamped pair, so the stamp leaves the line empty and the `same` assertion reds. The diff made this reachable. | unsound | - |
| 18 | verification | .githooks/commit-msg:46 | medium | medium | confirmed | The diff adds an --check-commit block to .githooks/commit-msg (lines 31-51) ahead of the MERGE_HEAD exit. The only behavioural test of the hook is transition-audit.test.sh F10. F10's new_repo fixture has no unattended kit and no .unattended.conf, so the new block is skipped there. check-wiring.test.sh writes a stub hook, and unattended.test.sh calls --check-commit directly. Spec AC5 is only a grep for 'check-commit'. Moving the call below the merge-only exit, mis-mapping rc, or breaking the kit/conf probe would leave every suite green. The effect is contained: check 23 still grades at the close. So medium. | sound | - |
| 19 | verification | tools/unattended/check-unattended.sh:3835 | medium | medium | confirmed | At e252baf, check-unattended.sh sets dsposok=0 when the base does not resolve, and every pass is then counted as overlapped (dsov=1). No test file at e252baf asserts 'check 23 overlap unavailable' or 'counted as overlapped'. The base-0000 fixtures at test lines 1419 and 1792 only assert the separate BASE-resolve check. The fail-closed arm is therefore unguarded. A later commit (e4abc55bf, 'M7') adds exactly this arm, which confirms the gap was real. The effect is contained to test coverage. | sound | - |
| 20 | verification | tools/unattended/unattended.sh:9752 | medium | medium | confirmed | The --check-commit block in unattended.test.sh (lines 5742-5779 at e252baf) covers four cases: an undeclared stray path, run-state plus a conf GENERATED_INDEXES subtraction, a subject with no trailer, Pass: none, and an unbound branch. Nothing stages a brief row, which would exercise read_brief_paths with an empty commit, i.e. the index. Nothing stages a gen-region-only edit, which would exercise check_gen_region_only HEAD:$p :$p. Nothing sends a trailer naming a unit with no open dispatch row. Those three branches are reachable and untested. The effect is limited to verification. | sound | - |
| 21 | verification | tools/govkit/govkit.py:1987 | low | low | confirmed | 6c ORs together missing path, missing generator, extra tokens, missing generator file and missing why into one failure. The only selftest arm added (aWP-4 AC5) swaps the generator for a missing file. A regression in the token-set comparison or in the why test would leave selftest green. This is a test gap only, with no runtime effect. | sound | - |
| 22 | intent | tools/memory-tree/kit.toml:424 | blocker | blocker | confirmed | At e252baf, memory-tree/kit.toml declares two unconditional [[generated]] rows for {memory_root}/backlog. resolve_generated_indexes reads every tools/*/kit.toml with no condition support. resolve_shared_records defaults an undeclared key to '$M/DECISIONS.md $M/backlog', and .unattended.conf.example sets SHARED_RECORDS="memory/DECISIONS.md memory/backlog". So scan_shared_index_overlaps finds memory/backlog under both keys. unattended.sh then exits 2 at conf load for every verb, and check 38 reds. Gov escapes only because its own conf removed backlog from SHARED_RECORDS. The later fix commit e4abc55bf names this B1 and adds `when = ".memory-tree.conf:BACKLOG_MODE=builds"`. | unsound | - |
| 23 | intent | tools/unattended/unattended.sh:9742 | high | high | confirmed | verb_check_commit at e252baf reads the staged set with porcelain `git diff --cached --name-only`. diff.renames defaults to true, so a staged rename lists only its destination. Check 23 lists the commit with plumbing `git diff-tree --no-commit-id --name-only -r`, which does no rename detection and lists the deleted source too. Example: a `git mv` of an undeclared path into a declared one passes --check-commit, then is counted at close, when it can no longer be repaired. That is narrow, but it is a commit-time check certifying a commit the close grader then rejects. The later fix commit states '--check-commit lists staged paths with no rename detection'. | unsound | - |
| 24 | intent | tools/unattended/check-unattended.sh:3770 | medium | medium | confirmed | At e252baf, check 23 sets dshitsub with `git log -1 --format=%s` and runs id_in over sibling ids for every pass commit, trailered or not. Spec 2 S2 (lines 30-31) says a commit with a trailer is attributed by that trailer alone and its subject is never read. pass_commit/log_attribution_tokens already honour that, so a sibling mentioned only in a trailered commit's subject cannot be selected for that sibling. The ambiguity refusal is a false positive. It prints to stdout and `continue`s, so that pass's undeclared writes are neither counted nor reported SOLO. The later fix commit states 'Check 23's ambiguity test reads a trailered commit's trailer'. The escape is contained to one pass's grading. | sound | - |
| 25 | intent | tools/unattended/unattended.sh:9720 | medium | medium | confirmed | In unattended.sh at e252baf, verb_check_commit reads the trailer with `sed -n 's/^Pass: *//p'`, which is case-sensitive. It reads the subject with `sed -n '/[^[:space:]]/{p;q}'`, which takes the first non-blank line only. pass_commit (lib-unattended.sh:778) and the attribution log (lib:830, check-unattended:3807) use `%s` and `%(trailers:key=Pass)`; git matches that trailer key case-insensitively, and `%s` joins the whole first paragraph. Take a commit trailered `pass: X`, or one with the unit id on a wrapped subject line and no trailer. --check-commit sees no trailer and no unit in the subject, so it exits 0, while the close attributes the commit to the pass and counts the stray write. The later fix commit on HEAD ("READ AS THE CLOSE READS THEM (closing review r1, M2/L2)") confirms the defect existed in this range. The impact is contained: check 23 still grades the commit, only the early repair is lost. | sound | - |
| 26 | intent | tools/unattended/unattended.sh:9749 | medium | medium | confirmed | `git commit --amend` runs commit-msg and keeps the `Pass: <unit>` trailer. During the amend HEAD is the pass commit, so pass_commit returns it, and check_pass_open sees it writing inside the declared set and returns 1 (closed). The rows list then has no entry for the unit, decl is empty, and the verb fails 49 with 'has no open dispatched pass ... declare it first: --dispatch'. An ordinary amend is therefore refused unless --no-verify is used. HEAD later added exactly the proposed 'O' row arm (closing review r1, M4), which confirms the defect was in this range. | sound | - |
| 27 | intent | tools/unattended/check-unattended.sh:3899 | medium | medium | confirmed | At e252baf, check 23 sets dsrb from the run-branch fact, falling back to branch-ref. A live record can carry neither: run-branch is not written on a detached preflight, branch-ref is written only on the second anchor, and older records predate fact 13. Such a record is reachable in this tree: memory/builds/aCollapsedScan/RUN.md is in phase LANDING with no branch fact. For it, `[ "$dsrb" = "$DS_HEAD_REF" ]` can never hold on any checkout, so the record always prints 'OTHER RUN ... graded at its own close', and that close never happens. This diff introduced the problem: before it, the repo-global ceiling counted these writes. The header comment admits that an undriven run is not failed, but the printed line still claims a later grading that never comes. | sound | - |
| 28 | intent | .githooks/commit-msg:44 | low | low | confirmed | In the commit-msg hook, the unattended probe loop runs the kit only when both unattended.sh and .unattended.conf are found, and otherwise falls through silently. It prints only when the kit ran and exited with something other than 0 or 1. Spec 3 S4 and §5 promise that an absent kit is an announced skip. When the conf is present and the kit is missing, nothing is printed. Check 23 still grades at the close, so the effect is contained. | sound | - |
| 29 | intent | tools/unattended/lib-unattended.sh:527 | low | low | confirmed | Spec 4 §5 promises that check 23 prints the effective set it read, with each pair's source, and that the kit README describes the declaration. At e252baf, check-unattended.sh calls resolve_generated_indexes at line 303 and never reports the result. It only reports individual exclusions at about line 3812, which partly covers observability. The README diff adds only the hook paragraph, with no `[[generated]]` description; the PROTOCOL key row and the conf example do describe it. This is observability and docs only. | unsound | - |
