**Serves:** spec-audit TOOL-dBoundRoles-59@rev-1 TOOL-dBoundRoles-60@rev-1

# Tier-2 spec audit — dBoundRoles, the two promoted unit specs 59 and 60 (round 1)

Provenance: the specs the round-4 spec audit promoted, written 2026-10-26 and recorded at the spec commit 13ac01368. Finders ran as gov-spec-reviewer, skeptic batches as gov-skeptic, and this synthesis as gov-synthesizer.

Reviewed: memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md@64c2f4551f9e4a3683788fa66bbae05c0236d58b, memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md@0b89f29442e386f05e40f398d3fee90661b1f7bf

ROUND: 1

## Verdict: CLEAN WITH FIXES

No blocker survived the skeptics.
Two high findings did, and both must be fixed before the build pass of the unit they sit in.
The first is in spec 59: the read-check slice counts a crash as a pass (H1).
The second is in spec 60: AC15 checks a floor that one of its two suites does not have (H2).
The tally is 18 items over 21 confirmed findings: 0 blocker, 2 high items (2 findings), 9 medium items (12 findings), 7 low items (7 findings).
Every fix below is a spec edit. This report changes no code.

## Review shape

Intensity full, raw 22, confirmed 21, refuted 1, unverified 0 (0 uncertain), precision 0.95.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 8 | 7 | 1 | 0 | 0 | 0.88 |
| grounding | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |

By item, the adjudicated tally is 0 blocker, 2 high, 9 medium and 7 low (18 items).
By raw confirmed finding, it is 0 blocker, 2 high, 12 medium and 7 low (21 findings).

Run integrity:
- All 5 of 5 lenses returned and none died. All 5 of 5 skeptic batches returned and none died.
- No verdict was demoted to unverified as contradictory, none as an orphaned duplicate refutation, and no spurious verdict or duplicate was discarded.
- Fixes on confirmed findings: 20 judged sound, 1 judged UNSOUND (id 17, whose corrected fix is written below), 0 had no fix proposed, and 0 were NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED, and 3 RE-GRADED by the skeptic (ids 9, 15 and 20, each from high to medium).
- Unverified findings: 0 answered UNCERTAIN, and 0 with no usable verdict.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 49 spec documents were supplied as `specs`, as sibling context.
- Checklist: 23 items, each assigned to exactly one lens (coherence 5, grounding 5, reuse 5, blast-radius 4, failure-envelope 4).
- By design: none was supplied, with no caller byDesign and a block of 0.
- Move check: no checked subject moved.

The run is complete on every integrity count.
One finding was refuted: id 1, on repair ordering. The skeptic showed that BUILD-METHOD sanctions repairs ordered after the units they repair.

## High

### H1. Spec 59: the read-check slice counts its own crash as a pass (id 19)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-59.md`, §4 "The slice", §2 S1 and §5 error/empty states.
- **What is wrong:** the slice has one verdict: "an empty line means every key is read". The spec never says what happens when the Python slice exits non-zero. `tools/roles/adopt-roles.test.sh` runs under `set -u` only, with no `set -e`. A `$(...)` capture of a slice that crashes therefore comes back empty and the case continues.
- **Consequence:** three cases exit 1 with empty stdout: a role slot that does not exist (KeyError on `load_roles(...)[role]`), malformed front matter (`parse_front_matter` raises RolesError), and an entry `parse_read_key` refuses. In each one, `assert_role_reads` certifies a read it never checked. This is the wrong-reason pass the unit exists to remove. AC1 and AC2 cannot catch it, because neither of them makes the slice crash.
- **Fix (judged SOUND by the skeptic):** in S1 and in the slice text, require the helper to capture the slice's exit status. Any non-zero exit fails the case, naming the role and the Python error. The case passes only on exit 0 with empty output. Add a criterion row: with the case's role renamed to a slot that does not exist (e.g. `gov-orienterX`), the call fails naming the role. Add a §5 error-states line for the missing-role input and the unparseable-entry input.
- **Related:** id 9 (M2) reports the same defect at the skeptic's medium grade. It is kept separate only because grades may not be merged, and one spec edit closes both.
- **Left-shift gate:** add a bug-class checklist entry, "a check whose pass verdict is empty output must also assert exit status 0". The spec-audit failure-envelope lens should probe for it.

### H2. Spec 60: AC15 checks a floor the spawn guard's suite does not have (id 21)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §2 S24 and §6 AC15.
- **What is wrong:** S24 and AC15 check "each suite's floor" over two suites. One of them, the spawn guard's suite, has no floor: `tools/hooks/agent-cap.test.sh`, which unit 25 moves to `tools/roles/spawn-guard.test.sh`. `grep -c FLOOR_ASSERTIONS` over it prints 0. No spec creates a floor for it: spec 43 says only "raised", spec 58's spawn-guard arm line ends in "none", and spec 25 creates none.
- **Consequence:** over a suite with no `FLOOR_ASSERTIONS` line, AC15 has nothing to sum. It then either passes vacuously or errors, and the spec does not say which. Unit 58's spawn-guard arm lands with no floor while AC15 reports that suite as covered. AC15 also does not say whether "units 52, 53 and 58 each appear in a term" applies per suite or overall, and units 52 and 53 have no spawn-guard arms.
- **Fix (judged SOUND by the skeptic):** either scope a new floor in `tools/roles/spawn-guard.test.sh` (its initial value, its comment and its `n -ge` check, listed in §4 Inventory), or drop that suite from S24 and say why. Make AC15 fail when a named suite has no `FLOOR_ASSERTIONS` line. State, per suite, which units must appear in its terms.
- **Related:** ids 2 and 10 (M1) raise the same missing floor beside the base-term defect.
- **Left-shift gate:** have the selftest-budgets check, or a hygiene check, refuse a spec criterion that names a suite's `FLOOR_ASSERTIONS` when that suite carries no such line at the pinned base.

## Medium

### M1. Spec 60: AC15 sums only the `+<n>` terms and leaves out the floor comment's base term (ids 2, 10, 15, 22)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §6 AC15, §2 S24 and §4 Evidence, last bullet.
- **What is wrong:** the floor comment in `tools/roles/adopt-roles.test.sh:73` opens with a base term that carries no `+`: `# 10, then +3 for arm 7 ...`. The thirteen `+<n>` terms on lines 73-80 sum to 40, and line 81 is `FLOOR_ASSERTIONS=50`. AC15 sums only the `+<n>` terms. §4 Evidence says "the comment terms sum to 50", which is true only when the base is counted, so the spec contradicts itself. For the spawn-guard suite (ids 2 and 10), unit 43 pins any floor with no per-unit `+n` history, so the terms from unit 58 alone cannot equal it.
- **Consequence:** AC15 is red on a correct build. The builder must then either rewrite the comment convention, which no item scopes, or bend the probe until it goes green. Either way AC15 stops showing whether the arms moved the floor.
- **Fix (judged SOUND by the skeptic):** restate AC15 and S24 as: the base term (the first bare number in the floor comment) plus every `+<n>` term equals `FLOOR_ASSERTIONS`, with units 52, 53, 58 and 59 each named in a `+<n>` term. An alternative is for S24 to rewrite the base as an explicit `+10 for arms 1-6 (...)` term. Correct §4 Evidence to "the base 10 plus the `+n` terms sum to 50". Before landing, run the probe on the base file and confirm it prints 50. For the spawn-guard suite, apply H2's fix.
- **Left-shift gate:** add a selftest-budgets check that parses every suite's floor comment as base plus `+<n>` terms and requires the result to equal `FLOOR_ASSERTIONS`. That pins the grammar a spec can then cite.

### M2. Spec 59: an empty slice output is read as "every key is read", whatever the exit status (id 9)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-59.md`, §4 "The slice" and S1.
- **What is wrong:** this is the defect in H1. The success contract is an empty printed line, and the slice's exit status is never checked. A KeyError, a RolesError, an import failure or a `parse_read_key` that raises exits 1 with empty stdout. The finder's probe printed `rc=1 out=[]`.
- **Consequence:** `assert_role_reads` certifies a read it never made. The skeptic graded this medium, because in 47's case the plain-words render that follows (53 S2 requires exit 0) goes through the same load and parse and still turns the case red downstream.
- **Fix (judged SOUND by the skeptic):** have S1 and the slice text check the exit status, and fail the case on anything other than 0, naming the role and the slice's stderr. An alternative is to print an explicit OK token on success. Add an AC2 half that calls `assert_role_reads` with a role slot absent from the fixture (e.g. `gov-nosuch`), where the case must fail. One edit closes both this item and H1.
- **Left-shift gate:** the same checklist entry as H1.

### M3. Spec 60: AC4 cannot observe S7, because spec 52 already passes it (id 3)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §6 AC4, which observes §2 S7.
- **What is wrong:** spec 52's §4 Rollout (lines 102-104) already names `TOOL-dBoundRoles-26`, the suite and `--dispatch`. It also says 26 "writes no file this unit writes", and that is false: spec 26 lists `tools/roles/adopt-roles.test.sh` under Files touched. S7 exists to remove that claim. AC4 greps only for the names, never for the claim's absence.
- **Consequence:** S7 has no observation that can fail. A pass that leaves the false disjointness claim in place passes AC4, and that is exactly the defect AC4's Red-when names.
- **Fix (judged SOUND by the skeptic):** add to AC4 that `grep -n 'writes no file this unit writes'` over spec 52 prints nothing, and that 52's Rollout names `TOOL-dBoundRoles-26` as a writer of `tools/roles/adopt-roles.test.sh`.
- **Left-shift gate:** add a checklist entry, "a criterion that observes a removal must assert the removed text is absent, and must be red at base". The spec audit can check this by running each AC against the base tree.

### M4. Spec 60: AC14's grep for S34 is green at base, because spec 54 wraps the phrase across a line break (id 4)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §6 AC14, which observes §2 S34.
- **What is wrong:** AC14 checks that `grep -n 'ten at base'` over spec 54 prints nothing. In 54 AC1 (lines 134-135), the phrase is split across a line break: `ten at` / `base`. `grep -c 'ten at base'` prints 0 today, before the unit is built.
- **Consequence:** S34 has no observation that can fail. A build that leaves 54 AC1's typed count of ten in place still passes AC14.
- **Fix (judged SOUND by the skeptic):** observe the count in a way that does not depend on line breaks. For example, a python probe can extract 54's AC1 bullet, join its lines, and assert it holds no `ten at` and no numeric count. Alternatively, grep `-c 'ten at$'` alongside the joined form.
- **Left-shift gate:** the same red-at-base check as M3. Separately, a spec-lint rule that flags a grep criterion whose phrase spans a line break in its target file.

### M5. Spec 60: S19 and AC11 run a self-test suite inside a pass, which the spec's own F4 forbids (id 5)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §2 S19 and §6 AC11, against §8 F4 and §4 Alternatives rejected.
- **What is wrong:** S19 says "This pass observes both arms" of specs 54 and 55 on the archived tree. AC11 requires each arm to be staged and restored, reading red then green. Those arms are `tools/govkit/selftest.py` cases, so the observation means running the self-test suite. BUILD-METHOD M6 (lines 195-198) forbids a pass from doing that and gives the red-first observation to the main loop at M8. F4 and Alternatives rejected refuse a suite run inside a pass for 57 AC1 on exactly that ground, while AC13 and AC6 use direct probes. The spec gives two answers to one question.
- **Consequence:** built as written, the pass either breaks M6, and the role hook blocks it, or cannot observe AC11 at all.
- **Fix (judged SOUND by the skeptic):** restate AC11 in AC13's form, as a direct probe. Load `derive_overlay_expected` and its compare from the archived module through `ast` or importlib, without running the suite, and observe red and green on the staged fixture. Alternatively, give the arm observation to the main loop explicitly and drop "This pass observes both arms".
- **Left-shift gate:** a spec-lint rule flagging a criterion of a pass-run unit that stages a `New arm:` suite case or invokes a self-test suite.

### M6. Spec 60: S19 rewrites the §7 arm lines of specs 54 and 55 but leaves their §5 testing lines saying "at the close" (id 13)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §2 S19 and §6 AC11.
- **What is wrong:** S19 takes the `New arm:` prefix off the §7 arm lines of specs 54 and 55, so each arm lives only until unit 19's pass. Spec 54:126 and spec 55:123 still read `the arm of §7 at the close`. AC11 counts only lines that open with `New arm:`, so it stays green while those lines stand.
- **Consequence:** after the bump, each spec gives two answers about its arm. §5 sends the closer to stage an arm on a check that unit 19 has already deleted, which is the failure S19 exists to prevent. The harm is limited to a misleading line, because the close's tooling keys on the `New arm:` prefix.
- **Fix (judged SOUND by the skeptic):** extend S19 so the same bump rewrites 54 §5 and 55 §5. Each testing line should say the arm is observed at the unit's own pass and on the archived parent of unit 19's pass commit, not at the close. Add an AC11 half: `grep -n 'arm of §7 at the close'` over specs 54 and 55 prints nothing.
- **Left-shift gate:** add a checklist entry for the class amendment-leaves-its-other-half-standing: an amendment to a §7 arm line must also restate every §5 line that cites that arm.

### M7. Spec 60: the write set leaves out specs 45, 48 and 50, which the pass may have to bump (id 16)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §4 Files touched (estimate), with S2/S3/AC1 and S26/AC16.
- **What is wrong:** Files touched (line 247) lists the specs of units 14, 19, 46, 47, 49 and 52 to 58. §4 "How an item closes" tells the pass to do whatever a landed unit left undone. AC1 needs specs 46, 48 and 50 to stop quoting `handoff.derive_section_sha`, and all three quote it at base. AC16 needs `gov-builder` in 45's AC1 bullet, and that is absent at base. Unit 58 owns those bumps, and its own write set (spec 58:280) declares 45, 48 and 50.
- **Consequence:** if unit 58's pass left any of those specs unrestated, unit 60 writes a file outside its declared dispatch write set. `--check-commit` refuses the commit, or the close counts an undeclared write.
- **Fix (judged SOUND by the skeptic):** add 45, 48 and 50 to the "the specs of units ..." bullet in §4 Files touched. Alternatively, have S2 and S26 state that unit 58 owns those writes and unit 60 only observes them, so AC1 and AC16 read as observation.
- **Related:** id 8 (L3) is the low-graded finding on spec 45 alone. It is kept separate only because grades may not be merged.
- **Left-shift gate:** a hygiene check that every spec path a unit's §2 or §6 says the pass may bump appears in its §4 Files touched.

### M8. Spec 59: AC4 checks only one spelling of the citation S4 retires (id 17)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-59.md`, §6 AC4, against §2 S4.
- **What is wrong:** S4 retires `handoff.py:1025` as the read-key grammar's citation in spec 53. AC4 greps only for `handoff.py:1025-1026`, which spec 53 has on line 41. Spec 53 also has the bare `handoff.py:1025` in its Readers clause (line 45), and `handoff.py:1025-1028` on lines 26 and 76.
- **Consequence:** a pass that rewrites line 41 and appends `parse_read_key` to the Readers clause turns AC4 green. Line 45 would still credit handoff.py's copy with the grammar that unit 14 rewrote, which is the stale-citation class this unit exists to close.
- **Fix: the finder's proposal was REJECTED by the skeptic. The skeptic's corrected fix is the one to write:** have AC4 extract two bullets: the S1 bullet, from `**S1**` through the end of its Readers clause, and the §4 Evidence bullet that cites the read set. Each must name `parse_read_key`. The S1 bullet must hold no `handoff.py:1025` in any spelling (`handoff\.py:1025($|[^0-9])`). Line 76's citation of the `ap.error` refusal and the §1 Goal text may stay.
- **Related:** id 11 (L4) reports the same defect at low.
- **Left-shift gate:** a checklist entry, "an absence check on a retired citation must match every spelling of the citation, scoped to the section being amended".

### M9. Spec 60: the archived-tree observations run govkit's self-test module where there is no git repository (id 20)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §4 "Where each item lands at order 33", §2 S12, S19 and S23, and §6 AC6, AC11 and AC14.
- **What is wrong:** these items observe on a `git archive` extraction under %TEMP%, which has no `.git`. `tools/govkit/selftest.py` exits at import outside a repository. `derive_install_prefix()` (lines 34-47) raises SystemExit. `GOV_ROOT = next(...)` (line 70) raises StopIteration. Lines 195-196 run `run_gov_git(... 'rev-parse', 'HEAD')` at module level. The spec also never says how "unit 19's pass commit" is found when that pass spans several commits.
- **Consequence:** AC6, AC11 and AC14 cannot be observed as written. The builder has to improvise a repository or record OBSERVED by hand, so the red and green readings those items exist to pin are left unproven. The failure is loud, which keeps the effect contained.
- **Fix (judged SOUND by the skeptic):** state how the archived tree is made runnable, e.g. `git init` plus one commit inside the extraction, or a read-only `git worktree add --detach` under %TEMP% in place of `git archive`. The build runs this step, not the review. Say how unit 19's pass commit is found: the ledger's pass-commit sha. Add a step that fails the observation if the archived module does not import.
- **Left-shift gate:** a checklist entry, "an observation on an extracted tree must state the preconditions its imported modules need (a git repository, a resolved pin)".

## Low

### L1. Spec 60: S1 and S2 give two command shapes for 58 AC18's probe (id 6)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §2 S1, against S2 and §6 AC1.
- **What is wrong:** S1 gives the probe the whole spec tree with an exclusion pathspec for spec 58. S2 and AC1 scope it to `tools/` plus specs 46, 48 and 50, with no exclusion, and AC1 requires that 58 AC18 "spells that command".
- **Consequence:** a builder who follows S1 fails AC1's "spells that command". Both forms print the same lines, so the effect is cosmetic.
- **Fix (judged SOUND by the skeptic):** drop the exclusion-pathspec wording from S1, keep the literal `-F` match, and leave scoping to S2.
- **Left-shift gate:** a checklist entry for the class two-answers-to-one-question: a command a criterion requires to be spelled literally appears in one place only.

### L2. Spec 59: S4 records unit 53's AC1 and AC2 as amended, although their text does not change (id 7)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-59.md`, §2 S4.
- **What is wrong:** S4 bumps 53's S1, its Readers clause, §4 Evidence, §10 and §9, yet records 53's AC1 and AC2 as `amended rev-<n>`. Neither criterion cites handoff.py:1025, so its text is unchanged. Specs 60 §4 and 58 §4 both limit AMENDED to an item that changes another unit's criterion.
- **Consequence:** the ledger records two criteria as amended at a revision whose §9 line names only S1. Hygiene check 23 matches only the token, so the misleading record goes unchallenged.
- **Fix (judged SOUND by the skeptic):** either keep 53's AC1 and AC2 answers OBSERVED, re-observed under the folded helper, or have the bump restate AC1 and AC2 text (e.g. AC2's fixture in the tag spelling) and name them in the §9 line.
- **Left-shift gate:** extend hygiene check 23 so an `amended rev-<n>` answer requires the cited revision's §9 line to name that AC.

### L3. Spec 60: S26 has no fallback clause and no write-set entry for spec 45 (id 8)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §4 Files touched, against §2 S26 and §6 AC16.
- **What is wrong:** AC16 requires `gov-builder` inside spec 45's AC1 bullet, and "How an item closes" tells the pass to do what is missing. Spec 45 is not in Files touched. S26 also lacks the "where the pass left it unrestated, this pass makes the bump" clause that S11 carries for spec 49.
- **Consequence:** if unit 58's pass skipped that bump, unit 60 writes outside its declared set. That is the class unit 60's own title says it closes. The path is narrow.
- **Fix (judged SOUND by the skeptic):** add spec 45 to §4 Files touched, and give S26 the same "where unit 58's pass left 45 unrestated, this pass makes the bump" clause that S11 carries for 49. M7's fix covers the Files touched half.
- **Left-shift gate:** the same write-set hygiene check as M7.

### L4. Spec 59: AC4 misses the bare `handoff.py:1025` in spec 53's Readers clause (id 11)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-59.md`, §6 AC4, against S4.
- **What is wrong:** AC4's absence check matches only `handoff.py:1025-1026`. Spec 53's Readers clause (line 45) cites `tools/roles/handoff.py:1025`, "which S1 copies without changing".
- **Consequence:** a Readers clause that adds `parse_read_key` but keeps the stale copy claim passes AC4. This leaves a stale record in the spec, with no change in behaviour.
- **Fix (judged SOUND by the skeptic):** have AC4 also require that the Readers line (53 S1, the line opening `**Readers:**`) no longer names `handoff.py:1025`. Lines 26 and 76, which cite :1025-1028 for the `ap.error` refusal, legitimately stay. M8's corrected fix covers this.
- **Left-shift gate:** the same checklist entry as M8.

### L5. Spec 60: two §4 Evidence citations do not match the source (id 12)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-60.md`, §4 Evidence, bullets 1 and 4.
- **What is wrong:** bullet 1 says the `derive_section_sha` grep prints specs 46, 48, 50 and 58 "at base 462d20f3". At that base it prints nothing, because spec 46 does not exist there. Bullet 4 cites `selftest.py:1615-1618`, which covers the desc assignment and comments but not the token loop, at :1619-1620.
- **Consequence:** a builder re-running the Evidence at the stated base gets empty output and may doubt S1-S3. The range points away from the token-presence half that S21 keeps.
- **Fix (judged SOUND by the skeptic):** say the grep was read at HEAD (spec commit 13ac01368), where it prints 46:139, 48:176, 50:265, 58:117 and 58:349, plus spec 60's own lines. Cite `tools/memory-recall/selftest.py:1615` (desc) and `:1619-1620` (the token loop).
- **Left-shift gate:** a spec-lint rule that re-runs each Evidence command at its stated base and flags empty output.

### L6. Spec 59: S4's §10 clause has nothing in spec 53 §10 to replace (id 14)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-59.md`, §2 S4 and AC4.
- **What is wrong:** S4 says 53's §10 should cite `parse_read_key` "in place of `handoff.py:1025`". 53 §10 cites no `handoff.py:1025`. It names only `check_arm` and `roles_lib.load_roles` as seams. AC4 never checks §10.
- **Consequence:** the builder may skip the edit, and AC4 still passes. 53's reuse audit would then omit unit 14's `parse_read_key`, the seam its check actually reads through. The stale part is the reuse record only.
- **Fix (judged SOUND by the skeptic):** reword S4's §10 clause as an addition: 53 §10 names `roles_lib.parse_read_key` (unit 14 S4) beside `load_roles` and `check_arm` as the seam the read check folds through. Add an AC4 half requiring that `grep -n 'parse_read_key'` over spec 53 also prints a §10 line.
- **Left-shift gate:** a checklist entry, "an 'in place of X' amendment must name a section that contains X".

### L7. Spec 59: Files touched omits unit 53's ledger, which S4 writes (id 18)

- **Where:** `2026-10-26-spec-TOOL-dBoundRoles-59.md`, §4 Files touched (estimate), against §2 S4.
- **What is wrong:** S4 has the pass write unit 53's ledger answers for AC1 and AC2. Files touched names only `tools/roles/adopt-roles.test.sh` and spec 53. Specs 60 and 58 both declare this kind of write, and none of `check_commit_message`'s subtractions covers the journal record.
- **Consequence:** `--check-commit` may refuse the commit, or the close may count an undeclared write, on one bookkeeping file.
- **Fix (judged SOUND by the skeptic):** add to §4 Files touched "unit 53's acceptance ledger, the AMENDED answers of S4, named here for the dispatch write set", worded like unit 60's bullet. If L2's fix keeps the answers OBSERVED, the entry still applies to the re-observed answers.
- **Left-shift gate:** a hygiene check that a spec whose §2 writes another unit's ledger answer declares that ledger in §4 Files touched.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=22 confirmed=21 refuted=1 unverified=0 blocker=0 high=2 medium=12 low=7 agents=11 out-tokens=138486

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 4 Rollout / header order 23 (also 60 section 4 Rollout, order 33, against 58 AC18) | high | low | refuted | Refuted on premise (3). The facts the finder cites do reproduce: 53 S1 at lines 39-41 still copies the handoff.py:1025-1026 parse; 53 §7 lists `roles adopter self-test`; the orders are 52/53=22, 59=23, 58=32, 60=33; and 58 AC18 greps a path set that includes spec 58 itself. The consequence it draws does not follow. BUILD-METHOD lines 195-200 say a pass runs no merge bar, no self-test suite and no gate, and that the bar runs ONCE after the last unit is terminal. So 53's §7 gate is never run at 53's pass, and by the time it runs, 59 (order 23) has folded the helper. Unit 53's pass also does not have to break spec-before-code: BUILD-METHOD lines 55-56 say 'to diverge, change the spec first (rev bump + §9 line), then code'. That is a sanctioned in-pass path, and 59 S4 explicitly covers it ('Where unit 53's pass already folded ... records that'). For 58 AC18, the close-time check needs EVIDENCED or AMENDED. 60 lands the AMENDED revision at order 33, before the close, and that is the same pattern 60 S6 uses for 46 AC3. Repairs ordered after the units they repair are the method's design (M4 promotes, never folds), not a defect. | unsound | - |
| 2 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 6 AC15 (with section 2 S24) | medium | medium | confirmed | Reproduced. tools/roles/adopt-roles.test.sh:73 opens '# 10, then +3 for arm 7'. The '+<n>' terms on lines 73-80 are 3,3,3,4,10,1,4,2,3,1,3,2,1, which sum to 40, and line 81 is FLOOR_ASSERTIONS=50. Only the unprefixed base 10 closes the gap, so 60 AC15's 'sum of +<n> terms equals the floor' is red on a correct build. tools/roles/spawn-guard.test.sh does not exist at base. `grep -n -i floor tools/hooks/agent-cap.test.sh` printed nothing. In spec 25, 'floor' appears only on the §7 gates line, and its arm line floors the suite through a selftest-budgets row, so S24/AC15's 'each suite's FLOOR_ASSERTIONS' has nothing to read for that suite. | sound | - |
| 3 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 6 AC4 (observing section 2 S7) | medium | medium | confirmed | Reproduced. spec-52.md:102-104 reads '`TOOL-dBoundRoles-26` holds order 22 and writes no file this unit writes; `TOOL-dBoundRoles-53` shares the order ... same suite, so `--dispatch` holds it'. So 52's Rollout already names 26, the suite and --dispatch. spec-26.md:166 lists tools/roles/adopt-roles.test.sh under Files touched, so the disjointness claim is false. AC4 (spec-60.md:281-283) only greps for TOOL-dBoundRoles-26 plus the suite and --dispatch, and never checks that the false phrase is gone. A pass that edits only spec 53 passes the 52 half, so S7 has no observation that can fail. The effect is confined to spec prose. | sound | - |
| 4 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 6 AC14 (observing section 2 S34) | medium | medium | confirmed | Reproduced. `grep -c 'ten at base'` over spec-54.md printed 0 today. spec-54.md:134-135 wraps the phrase as '...one house overlay path per role file, ten at' / 'base; with a scratch kit copy...'. So AC14's S34 half (spec-60.md:314) is already green before the unit is built, and cannot fail on a build that leaves the typed count in place. | sound | - |
| 5 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 2 S19, section 6 AC11 (against section 8 F4 and section 4 Alternatives rejected) | medium | medium | confirmed | Reproduced. spec-60.md S19 says 'This pass observes both arms on the tree archived at the parent of unit 19's pass commit'. AC11 requires the archived tree's 54 and 55 arms 'staged and restored, each reads red then green'. Those arms are `New arm: tools/govkit/selftest.py` cases (spec-54.md:152, spec-55.md:147), so reading them red then green means running govkit's self-test cases. BUILD-METHOD:195-198 says a pass runs no self-test suite and that a new arm's RED-first observation is the main loop's at M8. The same spec's F4 and its Alternatives rejected refuse a suite run inside a pass for 57 AC1 on exactly that ground, while AC13 and AC6 use direct ast or function probes. The spec therefore answers the same question two ways. | sound | - |
| 6 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 2 S1 against S2 and section 6 AC1 | low | low | confirmed | Read spec-60.md:58-61 and :271-273. S1 requires `git grep -nF 'handoff.derive_section_sha'` with an exclusion pathspec for spec 58. S2 scopes the probe to tools/ and specs 46, 48 and 50. AC1's literal command has those four paths and no exclusion pathspec, and it requires that 58 AC18 'spells that command'. A builder who follows S1 adds an exclusion that AC1's literal command lacks. Since S2's scope already leaves spec 58 out, the exclusion would be redundant anyway. The two answers to one question disagree, but either form prints the same lines, so the effect is cosmetic. | sound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 2 S4 | low | low | confirmed | spec-59.md S4 (lines 49-54) bumps 53's S1, its Readers clause, §4 Evidence, §10 and §9 only, yet it has 53's ledger answer AC1 and AC2 `amended rev-<n>`. Spec 53's AC1 and AC2 (spec-53.md:126-133) cite neither handoff.py:1025 nor the parse, so the bump leaves their text as it is. Spec 60 §4 (lines 197-200) and spec 58 §4 (lines 228-233) both limit AMENDED to an item that changes another unit's criterion. check-memory-hygiene.sh:3149 classifies only by the `amended rev-[0-9]+` token, so it would accept the misleading answer. The effect is limited to the record. | sound | - |
| 8 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 4 Files touched (against section 2 S26 and section 6 AC16) | low | low | confirmed | spec-60.md:247-248 lists the specs of units 14, 19, 46, 47, 49, 52 to 58, and spec 45 is not among them. S26 (lines 126-127) and AC16 (lines 323-325) require `gov-builder` inside 45's AC1 bullet, and 'How an item closes' (lines 197-198) tells the pass to do whatever is missing. S11 (lines 81-83) carries an explicit fallback bump for spec 49, and S26 has none for 45. At HEAD, spec 45's AC1 (lines 158-163) has no `gov-builder`. Spec 58 owns that bump: its write set at :280 includes 45, and its AC6 checks it. So 60's pass writes 45 only if 58's pass skipped the bump. That is a narrow contingency, but if it happens 60 writes outside its declared set. | sound | - |
| 9 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 4 "The slice" (and S1) | high | medium | confirmed | spec-59.md:96-104 gives the slice's success contract as an empty printed line ('An empty line means every key is read') and says nothing about the exit status. The slice indexes `load_roles(...)[sys.argv[2]]` and calls parse_read_key per entry. A KeyError, a RolesError, an import failure or a raising parse_read_key makes Python exit 1 with nothing on stdout. Re-ran the finder's probe: it printed `rc=1 out=[]`. Spec 53's S1 (lines 38-43) carries no exit check for the slice either, and assert_role_reads does not yet exist in adopt-roles.test.sh. So the read check would certify a read it never made. I grade it medium, not high: in 47's case, the plain-words render that follows (53 S2 requires exit 0) goes through the same load and parse, so a missing role or a broken roles_lib still reds the case downstream. The effect is contained. | sound | - |
| 10 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 2 S24, section 6 AC15 (against section 4 Evidence, last bullet) | medium | medium | confirmed | Re-ran the finder's command: `sed -n 73,80p tools/roles/adopt-roles.test.sh \| grep -oE '\+[0-9]+' ...` printed `13 terms sum 40`, and :81 holds FLOOR_ASSERTIONS=50. Line 73 opens with the unsigned base '10, then +3'. So the §4 Evidence line at spec-60.md:223 holds only if that base counts, while AC15 (lines 320-322) sums only the `+<n>` terms. tools/roles/spawn-guard.test.sh does not exist at HEAD. Unit 43 creates it (S27 at spec-43.md:121-123) against a pinned FLOOR_ASSERTIONS with no per-unit `+n` history, so the terms from 58 alone cannot equal its floor. Built as written, AC15 stays red on a correct tree, or the builder has to bend the probe. | sound | - |
| 11 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 6 AC4 (against S4) | low | low | confirmed | I re-ran the grep over spec 53. It prints :26 and :76 (`handoff.py:1025-1028`), :41 (`handoff.py:1025-1026`) and :45, where the Readers clause reads `tools/roles/handoff.py:1025` ... `which S1 copies without changing`. Spec 59 AC4 (:160-163) checks three things: parse_read_key appears in S1's Readers clause, `handoff.py:1025-1026` is absent, and §9 has its line. A Readers clause that adds parse_read_key but keeps the bare `:1025` copy claim passes all three. The effect is a stale record in a spec, with no behaviour change. | sound | - |
| 12 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 4 Evidence, bullets 1 and 4 | low | low | confirmed | `git grep -n 'handoff.derive_section_sha' 462d20f3 -- tools memory/builds/dBoundRoles/spec` printed nothing (rc=1), and `git show 462d20f3:` on spec 46 says the file does not exist at that base. At HEAD the same grep prints 46:139, 48:176, 50:265, 58:117 and 58:349, plus spec 60's own lines. In tools/memory-recall/selftest.py, :1615 is `desc = parts[1]`, :1617-1618 are comments, and the token loop is at :1619-1620. So the cited `:1615-1618` misses the loop. Both are wrong citations, so the grade is low. | sound | - |
| 13 | reuse | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 2 S19 (and AC11) | medium | medium | confirmed | The grep shows spec 54:126 and spec 55:123 both read `testing — AC1 to AC3 by probe and grep; the arm of §7 at the close.` Spec 60 S19 (:101-106) changes only 54 AC1/AC2, 55 AC1 and the §7 arm lines. AC11 (:305-308) counts only lines that open with `New arm:`. After the bump, §5 still points the closer at an arm on a check unit 19 has deleted, and AC11 stays green. Once the `New arm:` prefix is gone, the close's tooling is unlikely to act on it, so the harm is limited to a misleading line. | sound | amendment-leaves-its-other-half-standing |
| 14 | reuse | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 2 S4 (and AC4) | low | low | confirmed | Spec 53 §10 reads: "The seams are the suite's `check_arm` (...) and the installed kit's `roles_lib.load_roles`". It names neither handoff.py:1025 nor parse_read_key, so S4's "§10 likewise ... in place of handoff.py:1025" has nothing to replace. Spec 59 AC4 (:160-163) does not check §10 at all. The stale part is the reuse record only. | sound | - |
| 15 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 6 AC15 (with section 2 S24 and section 4 Evidence) | high | medium | confirmed | tools/roles/adopt-roles.test.sh:73-81 opens the floor comment with a bare `# 10, then +3 for arm 7 ...`, and the floor is `FLOOR_ASSERTIONS=50`. The `+<n>` terms add up to 3+3+3+4+10+1+4+2+3+1+3+2+1 = 40, which reaches 50 only once the base 10 is counted. Spec 60 AC15 (:320) sums only the `+<n>` terms against the floor, so it is red on a correct tree, while §4 Evidence (:223) says the comment terms sum to 50. The spec contradicts itself. The criterion fails rather than certifying something false, and a builder will see it fail at build time, so the harm is contained: I grade it medium, not the finder's high. tools/roles/spawn-guard.test.sh does not exist in this tree, so the finder's second-suite concern cannot be checked here. Spec 59 §7 also raises this floor with a `+n` comment, so naming unit 59 in the fix is consistent. | sound | - |
| 16 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 4 Files touched (estimate), with S2/S3/AC1 and S26/AC16 | medium | medium | confirmed | Read spec 60 at blob 0b89f29. Files touched (line 247) lists 'the specs of units 14, 19, 46, 47, 49, 52, 53, 54, 55, 56, 57 and 58'; 45, 48 and 50 are missing. §4 'How an item closes' says 'the pass does what is missing or records that a landed unit already left it'. S2/AC1 require 46, 48 and 50 to stop matching, and S26/AC16 require `gov-builder` inside 45's AC1 bullet. Re-ran `git grep -n -F 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec`: it printed 46:139, 48:176, 50:265 and 58:117/349, so all three still quote it at base. Spec 58:221 gives those bumps to unit 58 ('S4 to S6 ... bump spec 45; S18 bumps 46, 48 and 50 together'). Spec 58's own Files touched (line 280) names 45, 48 and 50, so the precedent is to declare them. If unit 58's pass leaves any of these undone, unit 60 writes a file outside its declared set. unattended.sh check_commit_message refuses an open pass's commit that stages an undeclared path (a `--dispatch` widening is the way out). The effect is a refused commit or a counted undeclared write on a narrow path, so it is contained. | sound | - |
| 17 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 6 AC4 (against section 2 S4) | medium | medium | confirmed | Ran `grep -n 'handoff.py:10'` over spec 53. It printed 26 (`handoff.py:1025-1028`), 41 (`handoff.py:1025-1026` makes ...), 45 (`**Readers:** by name: tools/roles/handoff.py:1025, the render's read set, which drops the same`) and 76 (`handoff.py:1025-1028` builds the read set). Spec 59's AC4 (line 161) checks absence of only `handoff.py:1025-1026`. S4 retires `handoff.py:1025` in the Readers clause, but AC4 cannot see line 45. A pass that rewrites line 41 and appends `parse_read_key` to the Readers clause turns AC4 green while line 45 still credits handoff.py's copy with the grammar. | unsound | - |
| 18 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 4 Files touched (estimate), against section 2 S4 | low | low | confirmed | Spec 59:51-52 (S4) has the pass write unit 53's ledger answers for AC1 and AC2 as `amended rev-<n>`. Files touched (lines 123-124) names only `tools/roles/adopt-roles.test.sh` and spec 53. Both siblings declare this kind of write: spec 60:247-248 and spec 58:280 each name 'the ledgers the AMENDED answers ... write' for the dispatch write set. The ledger lives in a journal record under memory/builds/dBoundRoles/build/. check_commit_message's subtractions are the run-state file, brief rows, generated outputs and gen regions, and none of them covers that record. The consequence is a refused commit or a counted undeclared write on one bookkeeping file. | sound | - |
| 19 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md:section 4 "The slice" and section 2 S1 (also section 5 error/empty states) | high | high | confirmed | Spec 59 §4 'The slice' (lines 95-105) defines the verdict only as 'An empty line means every key is read; a printed key fails the case'. Neither S1 nor §5 mentions the slice's exit status. tools/roles/adopt-roles.test.sh runs under `set -u` only (line 51), with no `set -e`, so a `$(...)` capture of a crashing slice gives empty output and the case continues. In roles_lib.py:306-336, `parse_front_matter` raises RolesError and `load_roles` returns a dict keyed by slot, so a missing slot raises KeyError. `parse_read_key` can also refuse an entry. Each of these crashes produces exactly the empty output the spec reads as a pass. The check then certifies a read it never made, on a narrow set of inputs, and AC1/AC2 do not cover it. | sound | - |
| 20 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 4 "Where each item lands at order 33"; section 2 S12, S19, S23; section 6 AC6, AC11, AC14 | high | medium | confirmed | In tools/govkit/selftest.py, `derive_install_prefix()` (lines 34-47) raises SystemExit 'not inside a git repository' and runs at import (`PFX = ...`). Line 70 has `GOV_ROOT = next(p for p in HERE.parents if (p / ".git").exists())`, and lines 195-196 run `resolve_gov_pin`/`run_gov_git(... 'rev-parse','HEAD')` at module level. Spec 60 §4 'Where each item lands' (lines 204-207) has S12, S13, S19 and S23 observe on a `git archive` extraction under %TEMP%, which carries no .git, and it never says how that tree gets a repository. AC6, AC11 and AC14 therefore cannot be observed as written. The failure is loud, because the module dies at import, and the builder has to improvise. That makes the defect contained (medium), not a silent wrong result. Finding unit 19's pass commit is also left implicit. | sound | - |
| 21 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 2 S24; section 6 AC15 | high | high | confirmed | Re-probed. `grep -c FLOOR_ASSERTIONS tools/hooks/agent-cap.test.sh` printed 0, while format-guard.test.sh and scratch-guard.test.sh each printed 3. tools/roles/ has no spawn-guard.test.sh yet. In the spec set, only spec 43:524 mentions a floor for spawn-guard.test.sh, and it only says '`FLOOR_ASSERTIONS` raised' with no minting. Spec 58:398's spawn-guard `New arm:` line ends in 'none', and spec 25 mints no floor. Spec 60 S24 (lines 120-122) and AC15 (lines 320-322) still treat that suite as floored. That leaves AC15 vacuous or undefined for that suite, so it would report as covered a floor that does not exist. AC15 also does not say per suite which units must appear, and 52 and 53 have no spawn-guard arms. | sound | - |
| 22 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md:section 6 AC15 (and section 4 Evidence, last bullet) | medium | medium | confirmed | Re-probed. tools/roles/adopt-roles.test.sh:73 opens '# 10, then +3 for arm 7', and :81 is `FLOOR_ASSERTIONS=50`. Summing the `+<n>` tokens on lines 73-80 printed 40. Spec 60 AC15 (line 320) sums only the `+<n>` terms and requires that sum to equal the floor, and §4 Evidence (line 223) claims the terms sum to 50. So on a correct tree the probe comes out 10 short and goes red. The builder would have to reword the comment or the probe outside any stated clause. | sound | - |
