**Serves:** spec-audit TOOL-dBoundRoles-54@rev-1 TOOL-dBoundRoles-55@rev-1 TOOL-dBoundRoles-52@rev-1 TOOL-dBoundRoles-53@rev-1 TOOL-dBoundRoles-56@rev-1 TOOL-dBoundRoles-57@rev-1 TOOL-dBoundRoles-58@rev-1

# Tier-2 spec audit — dBoundRoles, the seven promoted unit specs 52 to 58 (round 1)

Provenance: the specs the round-3 spec audit promoted, written 2026-10-26 and recorded at the spec commit b385ea78d. Finders ran as gov-spec-reviewer, skeptic batches as gov-skeptic, and this synthesis as gov-synthesizer.

Reviewed: memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md@1c547db54e565709760dca2082bf6e139ebbffe7, memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md@9dc79c1b4917aa4a24d3f012e5136ade28ef0bc7, memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-52.md@f4537fd0668817281dffbd9da7aeef97e3959f6d, memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md@ed3239fbe79a36b8bfe41a7ee56cbf209f376801, memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md@0788292cef50928e023cc3c4c3bb5623e6a8eaab, memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-57.md@58ff67b4b0b4ea3d89c1cbbd368b88eaf26728ef, memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md@3ff0e120212a65b756d2b6103dafccb90464faac

ROUND: 1

## Verdict: CLEAN WITH FIXES

No blocker survived the skeptics.
One high finding did. Spec 53 S1 parses role `reads` with a stale copy, and it must be fixed before unit 53's build pass.
The tally is 28 items over 38 confirmed findings: 0 blocker, 1 high item (1 finding), 16 medium items (24 findings), 11 low items (13 findings).
Every fix below is a spec edit. This report touches no code.

## Review shape

Intensity full, raw 39, confirmed 38, refuted 1, unverified 0 (0 uncertain), precision 0.97.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 11 | 10 | 1 | 0 | 0 | 0.91 |
| grounding | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |

The adjudicated tally by item is 0 blocker, 1 high, 16 medium and 11 low (28 items).
By raw confirmed finding it is 0 blocker, 1 high, 24 medium and 13 low (38 findings).
The one refuted finding (id 10) was a duplicate of id 15, so its defect is covered by item M8.

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 5/5 returned, 0 died.
- Verdict hygiene: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 37 judged sound, 1 judged UNSOUND (id 28, whose skeptic correction is written below), 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 8 re-graded by the skeptic (ids 1, 2, 3, 6, 8, 12, 24, 26).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 42 spec documents supplied as `specs`, as sibling context.
- Checklist: 23 items, each assigned to exactly one of 5 lenses: coherence 5, grounding 5, reuse 5, blast-radius 4, failure-envelope 4.
- By design: none supplied, with no caller byDesign and a block of 0.
- Move check: no checked subject moved.
- No lens or batch died and every demotion count is zero, so this run is complete.

## High

### H1. Spec 53 S1 re-parses role `reads` with a stale copy instead of `parse_read_key` (id 21)

- **Where:** spec 53, section 2 S1 and its Readers clause, section 4 Evidence, section 10.
- **What is wrong:** S1 reads a role's `reads` through `load_roles` and copies the base parse at handoff.py:1025 without changing it (split on commas, strip, drop a trailing `?`). Unit 14 S4 (order 1) makes `roles_lib.parse_read_key` the single read-key parser. Unit 14 S7 rewrites every gov role's `reads:` line to tag spelling (`field.input.question`).
- **Consequence:** At order 22 the copy yields `field.input.question`, so `assert_role_reads gov-orienter input:question` fails on a correct tree. S2's unmodified case goes red, and AC1 ("fails naming input:question") passes for the wrong reason. Spec 58 S2/AC2 call the same helper on every render of 47's case and inherit the failure. The read-key grammar also gains a second, out-of-date owner.
- **Fix (judged sound):** Have `assert_role_reads` read each entry through the installed kit's `roles_lib.parse_read_key` and compare the native keys it returns. Add a consumes-from edge to TOOL-dBoundRoles-14 S4/S7. Make the Readers clause and section 4 Evidence cite `parse_read_key`, not handoff.py:1025. Add a criterion: with the tag-spelled `reads:` line unit 14 leaves (`field.input.question, field.input.prompt?`), the unmodified case passes `assert_role_reads gov-orienter input:question input:prompt`. Stage the break by swapping in the raw-split copy and watching that criterion go red.
- **Left-shift gate:** Add a grep gate that refuses any new split of a `reads` value outside `parse_read_key`, in tools/ and in spec criteria. Where no gate fits, add a checklist entry for "a spec copies a parse that a lower-order unit replaces".

## Medium

### M1. Spec 58 AC18 matches its own text and can never pass (ids 1, 12, 24)

- **Where:** spec 58, section 6 AC18 and section 2 S18.
- **What is wrong:** AC18 requires `git grep 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec` to print nothing. Spec 58 sits inside that pathspec and spells the string at S18 (:116) and in AC18's own command (:346). The unescaped `.` also matches any character.
- **Consequence:** After 46 AC1, 48 AC3 and 50 AC7 are re-pointed, the two spec-58 lines remain, so AC18 stays red on a correct build. The builder must reword the spec or answer the criterion by hand, and S18 is then judged by a check nobody specified. The criterion stays visibly red rather than falsely green, which is why the skeptics graded it medium.
- **Fix (judged sound):** Exclude spec 58 and match the string literally: `git grep -nF 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec ':!memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md'`. Better, scope the probe to `tools/` plus the three specs it repairs (46, 48, 50). Reword S18 so spec 58 does not spell the retired call in a form the probe matches. Confirm the probe is red today on 46, 48 and 50 and goes green once only spec 58 remains.
- **Left-shift gate:** The spec-tokens leg refuses an "expects nothing" grep criterion whose pathspec includes the spec that carries it, unless the spec is excluded.

### M2. Spec 53 AC3's staged break goes red before reaching S3 (ids 2, 16)

- **Where:** spec 53, section 6 AC3 and the section 7 New arm, against section 2 S2 and S3.
- **What is wrong:** S2 runs the plain-words control render first and requires exit 0 before the refusal render. AC3 stages a handoff.py that raises a usage error on every render, so the control render exits 2 and the case fails at S2's check. S3's exit-2 check is never reached.
- **Consequence:** The arm reads red even if S3 is missing or wrong. It certifies that the refusal half rejects a usage error without exercising that check.
- **Fix (judged sound):** Stage a handoff.py copy that calls `ap.error` (exit 2) only when the typed value holds the refusal span (the `record:` input shown at spec 47:40) and renders normally otherwise. The control render then passes, and only S3 can turn the case red. Restate the section 7 arm's staging to match, and state in S2 whether a failed control render stops the case. The build must run that staged copy and see red only through S3.
- **Left-shift gate:** A checklist entry for class guard-above-a-fold-makes-its-fallback-dead: a staged break must not trip an earlier precondition than the check it claims to cover.

### M3. Spec 46 AC3 depends on an entry guard spec 58 adds 20 orders later (id 3)

- **Where:** spec 58, section 2 S8 and S9, ordered against TOOL-dBoundRoles-46 AC3.
- **What is wrong:** 46 AC3 (order 12) requires `tools/hooks/agent-cap.js` through `node -e`. That file ends in a bare `main()`. Spec 46 adds the TYPED_INPUTS export but no `require.main === module` guard. Requiring the file runs `main()`, which reads stdin and calls `process.exit(0)` before any print. Spec 58 adds the guard only in spawn-guard.js at order 32, and unit 25 retires agent-cap.js at order 26.
- **Consequence:** 46 AC3 cannot pass at its own pass. The ledger either records it red, and BUILD-METHOD stops after a red pass, or leaves it unobservable for 20 orders and then holds it in a file it does not name. Unit 46 ends up depending on unit 58, which is ordered after it.
- **Fix (judged sound):** Have unit 46's pass add `if (require.main === module) main()` to agent-cap.js beside the TYPED_INPUTS export. Unit 25 then carries the guard into spawn-guard.js, and 58 S8/S9 only observe that it survived. Alternatively, under 58 section 4 "How an item closes", bump spec 46 so AC3 is answered `amended rev-<n>` at a revision naming spawn-guard.js and order 32, and say so in S9.
- **Left-shift gate:** The build-order generator refuses a criterion at order N whose precondition is written only by a unit ordered after N. Where that cannot be checked mechanically, add a checklist entry.

### M4. Spec 52's Rollout falsely says unit 26 shares no file with it (ids 4, 14, 27)

- **Where:** spec 52, section 4 Rollout.
- **What is wrong:** The Rollout says "TOOL-dBoundRoles-26 holds order 22 and writes no file this unit writes". Spec 26's Files touched (:166) and its section 7 arm (:229) write `tools/roles/adopt-roles.test.sh`, the one product file 52 and 53 edit. All three hold order 22, the README marks step 22 parallel, and no edge joins 26 to 52 or 53.
- **Consequence:** `--dispatch` gets no hold between them, so three units edit the same suite (and its FLOOR_ASSERTIONS count) in parallel. The likely results are conflicting hunks or a lost case. The same-order disjointness that 51 S1 and BUILD-METHOD M6 rely on is asserted but false.
- **Fix (judged sound):** Correct the Rollout sentence. Add a consumes-from or hands-off edge between TOOL-dBoundRoles-26 and 52 and 53, or move 52 and 53 after 26, and mirror the edge in the specs' section 3 Edges. Re-run the build-order generator so step 22 is no longer marked parallel.
- **Left-shift gate:** The build-order generator refuses to mark a step parallel when two of its units' Files touched intersect and no edge joins them.

### M5. Spec 54 AC3 is already green and does not observe S3's restatement of spec 49 (ids 5, 13)

- **Where:** spec 54, section 6 AC3 (observing section 2 S3).
- **What is wrong:** AC3 requires a section 9 line in spec 49 naming TOOL-dBoundRoles-54, and 49's AC2 to name the roster. Both already hold at HEAD: spec-49:167 is the rev-2 Edges-mirror line, and AC2 at :139 already says "roster".
- **Consequence:** S3 can be skipped while 54 closes green. S3 bumps 49's S3, its section 4 "Why two checks" and its AC2 to describe the roster-side set. Without it, spec 49 keeps describing the self-compare that an earlier round's finding showed red against a correct build.
- **Fix (judged sound):** Test the new text. Require `derive_overlay_expected` (or "role slot") in 49's S3 and AC2 lines, a phrase absent at HEAD. Require a section 9 line at a revision above rev-2 that names TOOL-dBoundRoles-54 with "S3" or "AC2".
- **Left-shift gate:** A gate that runs each new spec criterion against the base tree and flags any that already passes, since a criterion must be red before its unit builds.

### M6. Spec 55 AC1's fixture does not isolate S1's empty-set refusal (ids 7, 36)

- **Where:** spec 55, section 6 AC1, section 2 S1 and the section 7 New arm.
- **What is wrong:** AC1 empties only `agents/` and leaves the ten `house/*.md` seed includes in kit.toml. Unit 54's reverse compare still goes red on those seeded overlays, because no slot owns them, so the case fails whether S1 is present or removed. The arm's claim that removing S1 "lets an empty kit pass" is false.
- **Consequence:** An assertion on pass/fail alone is red for the wrong reason in both states, so S1 is never seen doing anything. The real case for S1 is never exercised: both sides empty, which is the shape after unit 19 or under a wrong kit path.
- **Fix (judged sound):** Build the fixture with both sides empty: no `agents/*.agent.md` and no `house/*.md` include in the scratch kit.toml. Require the failure to name the kit path. Restate the arm so removing S1 turns that fixture green, and have the build stage that break and see the arm red.
- **Left-shift gate:** A checklist entry for class fixture-passes-by-finding-nothing: a staged break must name the one check whose removal flips the fixture.

### M7. Spec 58 AC30 greps the wrong file for 38 S5's refusal (ids 9, 29)

- **Where:** spec 58, section 6 AC30 (observing section 2 S30).
- **What is wrong:** AC30 expects `grep -n 'ends inside' tools/roles/roles_lib.py` to print "38 S5's refusal only". 38 S5 raises that refusal in `render_handoff`, in tools/roles/handoff.py. roles_lib.py holds only 38 S3's walker, whose wording may or may not match.
- **Consequence:** The criterion cannot pass on a correct build. Or it passes on a docstring match, or stays silent when 48's end-of-walk clause in `check_block_fences` uses other wording. Either way the retirement S30 makes goes unobserved.
- **Fix (judged sound):** Observe by behaviour. Call `roles_lib.check_block_fences` on a section whose walk ends inside a fence and is otherwise well formed, and expect no line. Render the same section through `render_handoff` and expect exactly one refusal, 38 S5's. A weaker alternative is to grep both handoff.py and roles_lib.py and expect exactly one hit, in `render_handoff`.
- **Left-shift gate:** The spec-tokens leg checks that a function a criterion places in a file is defined in that file.

### M8. Spec 58 S5 wrongly says the control render needs no card (id 15)

- **Where:** spec 58, section 2 S5, section 4 (:244) and section 6 AC5.
- **What is wrong:** S5 says gov-builder's render resolves no kickoff checker and needs no card, because the role reads no `task:` key. But gov-builder reads `card:route?`, and handoff.py:358-360 calls `resolve_card_path` for any `card:` key. With CLAUDE_CODE_SESSION_ID set, that path finds the checker from KIT_DIR.parent and runs it. AC5 checks only `task:` keys and required `brief:` keys.
- **Consequence:** The control render's outcome depends on the environment. Inside an agent session it can spawn bash with a 30 s bound and pull a real card's route into a fixture render. If a later change made `card:route` required, AC5 would stay green while the control render went red.
- **Fix (judged sound):** Restate S5: the control role's only card key, `card:route?`, is optional, and the case renders with CLAUDE_CODE_SESSION_ID unset (or with no `--card` and no checker in the fixture). Extend AC5 to require no required `card:` key and no `task:` key.
- **Left-shift gate:** The adopter self-test unsets CLAUDE_CODE_SESSION_ID for every fixture render, so session state cannot leak into a case.

### M9. Spec 58 AC5 reads raw `reads` entries, which unit 14 tag-spells, so it cannot fail (id 22)

- **Where:** spec 58, section 6 AC5 (observing S5).
- **What is wrong:** AC5 reads the control role's raw `reads` through `roles_lib.load_roles` and asserts no `task:` key and no required `brief:` key. After 14 S7 (order 1) every entry is `field.*`, so no raw entry can start with `task:` or `brief:`.
- **Consequence:** At order 32, AC5 passes even if the control role reads `field.task.title` or a required `field.brief.goal`. It adds another reader that matches raw prefixes, where 14 S4 requires `parse_read_key` alone. AC4's render still observes the behaviour, so the effect is contained.
- **Fix (judged sound):** Map each entry through `roles_lib.parse_read_key`. Assert that no native key starts with `task:` and no non-optional native key starts with `brief:`. Stage a `field.task.title` entry on a scratch copy of the control role and require AC5 to go red.
- **Left-shift gate:** The same grep gate as H1, refusing any `reads` split outside `parse_read_key`.

### M10. Spec 56 edits a kickoff-watched file without the same-commit re-stamp (id 25)

- **Where:** spec 56, section 4 Files touched, section 2 S3 and section 7.
- **What is wrong:** S3 edits skills/session-kickoff/manifest-check.sh, which memory/guides/SESSION-KICKOFF.md:6 watches. The pre-commit staged leg (C5s, manifest-check.sh:1589-1597) refuses a commit that stages a watched file unless the same commit re-stamps last-audit. The spec lists neither SESSION-KICKOFF.md nor the `kickoff-manifest ratchet` leg.
- **Consequence:** The pass commit is refused unless it writes SESSION-KICKOFF.md, which is outside its declared dispatch write set. The pass either stalls at commit or makes a write nobody recorded.
- **Fix (judged sound):** Add `memory/guides/SESSION-KICKOFF.md` (the last-audit re-stamp, bundled into the pass commit) to section 4 Files touched. Name `kickoff-manifest ratchet` on the section 7 leg line. Add one sentence to S3 telling the pass to re-check the section-B claims that manifest-check.sh feeds before it re-stamps.
- **Left-shift gate:** The spec-tokens leg cross-checks each spec's Files touched against the kickoff manifest's watch list. It requires SESSION-KICKOFF.md wherever a watched file is listed.

### M11. Spec 55 leaves units 54 and 49 describing a check unit 19 deletes (id 28)

- **Where:** spec 55, section 2 S2 (the Readers clause).
- **What is wrong:** S2 retires `derive_overlay_expected` and its compare at unit 19's pass (order 24). The Readers clause names specs 54 and 49 but gives no disposition for either. 54 AC1/AC2 and 49 S3/AC2 still describe the deleted check, with no "before unit 19" scope. The skeptic found the problem goes further. BUILD-METHOD M8 (:280-282) has the closing loop observe every `New arm:` line red, then green. The arms at 54 section 7 (:150) and 55 section 7 (:145) are staged on checks that unit 19 deletes, so they cannot be staged at close.
- **Consequence:** Any closing re-verification of those criteria and arms goes red on a correct tree, or gets answered by hand.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** In 55 S2, give each reader a disposition. Unit 19's pass bumps specs 54 and 55; 49's AC2 is covered only through 54's restatement. The bump adds "observed at its own pass, before unit 19's pass; unit 19 deletes the check" to 54 AC1/AC2 and 55 AC1. It also re-scopes the `New arm:` lines at 54 section 7 and 55 section 7 as observed at their own pass, with the ledger recording red and green, so M8's close does not try to stage an arm on a deleted check. Add specs 54 and 55 to unit 19's write set through the existing consumes-from edge.
- **Left-shift gate:** A gate that refuses a spec deleting a function while another spec's `New arm:` line stages its break on that function without a before-scope.

### M12. Spec 56's parity case is not run when only tree_lib.py changes (id 30)

- **Where:** spec 56, section 2 S5 and section 7.
- **What is wrong:** The three-reader parity case lives in tools/hooks/scratch-guard.test.sh. The `scratch-guard self-test` leg is guarded on hooks/, lib/ and skills/session-kickoff/ only. tree_lib's `parse_spec_h1` is one of the three readers, yet `check-spec-tokens.py --legs-for tools/memory-tree/tree_lib.py` does not list that leg.
- **Consequence:** A commit touching only tree_lib skips the parity case on every guarded bar run. A divergence reaches the branch green and goes red only at the GATE_FULL push. The spec never states this gap.
- **Fix (judged sound):** Widen the leg's guard in tools/gate-legs.json with `{prefix}/memory-tree/tree_lib.py`, and add gate-legs.json to Files touched. Or state in section 3 or 5 that a tree_lib-only change is caught only at the full bar, as unit 37 section 4 does. Then confirm the leg appears under `--legs-for tools/memory-tree/tree_lib.py`.
- **Left-shift gate:** The spec-tokens leg runs `--legs-for` on every reader a new case names, and refuses if the case's leg is missing for any of them.

### M13. Spec 57 pins the no-search-tool rule on the description only, not the body (id 33)

- **Where:** spec 57, section 2 S1 and section 6 AC1.
- **What is wrong:** S1's "names neither Grep nor Glob" assertion reads only the front-matter description (`desc = parts[1]`, selftest.py:1610-1618). The body line that sends the reader to the refused tool (SKILL.template.md:66, "fall back to `Grep`") is outside that span. Spec 57 cites both lines that 51 S8 rewords, but pins only one of them.
- **Consequence:** A later edit that puts `Grep` back in the body's fallback passes the kit's self-test. That sentence steers the main loop to a tool unit 10 refuses, and 57 section 5 says this property is now pinned.
- **Fix (judged sound):** Run the no-search-tool half over the whole rendered Skill text (`text`) and keep the token-presence half on `desc`. Add a second staged case to AC1 and the section 7 arm that restores "fall back to `Grep`" in the body and must go red.
- **Left-shift gate:** A checklist entry: an invariant pinned on a rendered artifact names the span it reads and covers every line the source rule rewrites.

### M14. Spec 57 AC1's import-only probe cannot be run as written (id 34)

- **Where:** spec 57, section 6 AC1.
- **What is wrong:** AC1 says it "imports the kit's self-test module as a library, runs no suite". But the `@check` decorator (selftest.py:94-103) calls each function as it is defined, so the import runs all 86 checks. The check reads the template from the module's own directory (KIT, :71) and takes no parameter, so a "scratch copy of the template" cannot reach it.
- **Consequence:** The probe is a full suite run. The red half can be staged only by copying and importing the whole kit, which runs the suite again. A builder either runs the suite or records the criterion as answered without seeing it red.
- **Fix (judged sound):** Either run the kit's suite once and read the named check's ok/FAIL line, or have S1 lift the invariant into a plain undecorated `check_description(text)`. The probe then loads that function, behind an env guard or on its own. It calls it on the rendered text and on a scratch copy with "Grep and Glob own those" restored.
- **Left-shift gate:** A checklist entry: a criterion that imports a module must account for what the import runs.

### M15. Spec 54's two compare sides use different path forms (id 35)

- **Where:** spec 54, section 2 S1 and S2.
- **What is wrong:** S1 yields descriptor-relative `house/<slot>.md`. The plan rows from `derive_seed_expected` carry home-prefixed sources: `rule_sources` returns `f"{home}/{s}"`, and tools/roles/kit.toml:6 sets `home = "roles"`. S2 filters on `house/*.md` and never says how to normalise the two forms.
- **Consequence:** A literal build matches nothing, so the seeded side is empty and S2 goes red on every slot of a correct tree. The builder then has to invent a normalisation. Some choices, such as basename or a right-anchored match, accept an overlay from the wrong place. AC2 itself spells yet another form.
- **Fix (judged sound):** State the form in S1/S2: compare `<home>/house/<slot>.md`, with home read from the roles descriptor the plan used, against each row's `src` exactly. Or strip the descriptor's `home/` from `src` before matching. Add an AC1 assertion that the seeded side is non-empty on the default target. The finding gave the prefix as `tools/roles`. The skeptic notes it is the descriptor's home (`roles`), and the fix handles that.
- **Left-shift gate:** A checklist entry: a set compare states one canonical path form for both sides and asserts each side non-empty.

### M16. New arms on floored suites leave the assertion floor unmoved (id 37)

- **Where:** spec 58, section 7 New arm lines, and the same in spec 53 section 7 and spec 52 section 7.
- **What is wrong:** Each of these New arm lines sets the template's `<floor to move, or none>` field to `none`. adopt-roles.test.sh carries FLOOR_ASSERTIONS=50 (:81). Unit 43 S27 gives spawn-guard.test.sh a floor, and 43's own arm line says that floor is raised.
- **Consequence:** The floor guards against a skipped block of arms. If the new arms are not counted, a fixture failure or early return that skips them leaves the suite green. This covers 58's eight adopter cases and four spawn-guard cases, and 53's read-check and exit-check assertions.
- **Fix (judged sound):** Have each New arm line on adopt-roles.test.sh (52, 53, 58) and spawn-guard.test.sh (58) name the move, e.g. "`FLOOR_ASSERTIONS` raised by <n>". Have the pass add the matching "+n for <case> (<unit>)" comment beside the floor.
- **Left-shift gate:** The spec-tokens leg refuses a New arm line with floor `none` when the named suite defines FLOOR_ASSERTIONS.

## Low

### L1. The section 9 halves of 52 AC3 and 58 AC6 are already green (ids 6, 19)

- **Where:** spec 52, section 6 AC3 (observing S3), and spec 58, section 6 AC6.
- **What is wrong:** 52 AC3's half "spec 47 carries a section 9 line naming TOOL-dBoundRoles-52" and 58 AC6's half "the spec's section 9 names TOOL-dBoundRoles-58" already hold, because the rev-2 hands-off folds wrote those lines. 52 AC3's test-file half (`--role gov-builder` absent) is also green today, since unit 47's case does not exist yet. That half does bite at 52's real pass, after 47 builds at order 21.
- **Consequence:** Only the grep halves check the S3 and S6 spec bumps: 47's S1/AC1/AC2 moving to gov-orienter and input:prompt, and 45's AC1. Spec 47 could keep spelling gov-builder while 52 closes green. The skeptic graded id 6 low because the test-file half still observes the change at pass time.
- **Fix (judged sound):** Require a section 9 line at a revision above rev-2 naming the restated items ("S1, AC1, AC2" for 47, "AC1" for 45) and the promoting unit. Make 52 AC3 grep spec 47's AC1 and AC2 for `gov-orienter` and `input:prompt`. Replace the test-file half with a positive grep that the case commented TOOL-dBoundRoles-47 renders `--role gov-orienter`.
- **Left-shift gate:** The same base-tree check as M5, flagging any criterion that already passes.

### L2. Spec 19 has no criterion for the deletion spec 55 assigns it (id 8)

- **Where:** spec 55, section 2 S2 against section 6 AC2.
- **What is wrong:** S2 has unit 19's pass delete the compare and `derive_overlay_expected`, and AC2's after-half is "recorded by unit 19's ledger". Spec 19's AC1-AC6 never observe the deletion, so its ledger has no row for it.
- **Consequence:** No criterion in unit 19's acceptance observes the deletion. The skeptic graded it low: 19's section 7 runs `govkit selftest`, which would go red at 19's own pass if the compare survived without its seeds.
- **Fix (judged sound):** Fold an AC into spec 19, as a hands-off edit, that runs `grep -n 'derive_overlay_expected' tools/govkit/selftest.py` and expects nothing. Or let 55 AC2 assert only the before half and name 19's new criterion as the after half.
- **Left-shift gate:** A check that every "recorded by unit N's ledger" phrase names a criterion that exists in unit N's spec.

### L3. Spec 56 S5 miscounts its fixtures' live and decoy H1s (id 11)

- **Where:** spec 56, section 2 S5 and the third bullet of section 3.
- **What is wrong:** S5 says each of the five fixtures holds one live H1 and four hold a fenced decoy. But fixture 4, an unclosed fence holding the only H1, has no live H1, and only fixtures 1, 2 and 4 carry a fenced decoy. Section 3 repeats "one live H1 each".
- **Consequence:** A builder following the count invents a fourth decoy, or asserts an admitted id on fixture 4. Section 5 (:137) shows the intent, so the effect is a misstated count.
- **Fix (judged sound):** State that four fixtures hold one live H1, fixture 4 holds none, and fixtures 1, 2 and 4 hold a fenced decoy. Apply the admit/refuse checks only where an id or decoy exists. Align section 3.
- **Left-shift gate:** A checklist entry: a fixture list's summary counts are re-derived from its enumeration.

### L4. Spec 56's risk line misnames what the kickoff size leg measures (ids 17, 31)

- **Where:** spec 56, section 5 risks (line 140), and the `kickoff engine size <=18KiB` leg in section 7.
- **What is wrong:** The line says the size leg reads manifest-check.sh's bytes. The leg (gate-legs.json:151-155) measures skills/session-kickoff/SKILL.md only. manifest-check.sh is already about 100 KB.
- **Consequence:** It points the builder at a budget the change cannot cross, and it hides the real kickoff-side effect, the watched-file re-stamp in M10.
- **Fix (judged sound):** Replace the line with the real effect. manifest-check.sh is watched by memory/guides/SESSION-KICKOFF.md, so the pass re-stamps last-audit. Drop the size-leg claim, and keep the leg in section 7 only if its guard is tripped.
- **Left-shift gate:** The spec-tokens leg checks that any file a spec says a leg reads appears in that leg's argv or guard.

### L5. Spec 56 omits the pinned close instrument from parse_spec_h1's consumers (id 18)

- **Where:** spec 56, section 2 S2 and section 4 Evidence.
- **What is wrong:** S2 lists gen_build_index.py, extract.py, deviation_join.py and routed_commits.py. It misses memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py, which calls `gbi.parse_spec_h1` at :274 over working-tree specs and at :608 over base-revision blobs. S1 changes how that function behaves while the instrument's pinned blob stays the same.
- **Consequence:** The README rule "a moved instrument blob is a stop" cannot see this change, and section 4's measurement covered HEAD specs only. Contained, because no HEAD spec id moves.
- **Fix (judged sound):** Add deviations.py (:274, :608) to S2's consumer list. State that its pin does not cover the change. State that section 4's measurement, or AC3's re-derivation over the run's base, stands as its observation.
- **Left-shift gate:** A spec's consumer inventory is produced by `git grep` over the whole repo, memory/builds/ included.

### L6. Specs 53 and 56 spell a literal `python3` where the suites resolve a launcher (id 20)

- **Where:** spec 53, section 5 perf/scale (line 113), and spec 56, section 2 S5 (line 59).
- **What is wrong:** Both tell the builder to read through `python3 -c`. Because of the MS-Store stub, adopt-roles.test.sh (:60, `$PY`) and scratch-guard.test.sh (:127, `$TESTPY`) already resolve a launcher by running each candidate.
- **Consequence:** A literal build hard-codes `python3`. On a machine with the Store stub, the new arm exits 9009 and fails because of the platform. Only wording steers the builder, so low.
- **Fix (judged sound):** Write `"$PY" -B -c` for adopt-roles.test.sh and `"$TESTPY" -c` for scratch-guard.test.sh.
- **Left-shift gate:** A grep gate refusing a bare `python3 ` call in tools/**/*.test.sh outside the resolver.

### L7. Spec 52 cites gov-orienter's base `reads` spelling as unchanged (id 23)

- **Where:** spec 52, section 4 Evidence and section 2 S1.
- **What is wrong:** S1 and section 4 cite `input:question, input:prompt?` at gov-orienter.agent.md:8 and say "no spec of this build changes its reads". 14 S7 (order 1) tag-spells that line before 52 builds at order 22.
- **Consequence:** The role choice holds, because the role reads the same keys. A builder grepping for `input:question` at order 22 finds nothing and may conclude the role changed. The text also hides the dependency on unit 14's parser.
- **Fix (judged sound):** Say that 14 S7 tag-spells the line (`field.input.question, field.input.prompt?`) without changing what the role reads. Cite `parse_read_key` as the reader that folds it back. Add a consumes-from edge to TOOL-dBoundRoles-14.
- **Left-shift gate:** The H1 checklist entry for specs that cite a `file:line` an earlier-order unit rewrites.

### L8. Spec 54 AC1 types "ten at base" against a twelve-slot roster (id 26)

- **Where:** spec 54, section 6 AC1.
- **What is wrong:** AC1 says "one house overlay path per role file, ten at base" beside `figure: DERIVED`. Unit 54 builds at order 6. By then unit 1 (order 3) has added four role files and removed two, so the roster has twelve slots.
- **Consequence:** A builder reading "ten" sees a correct build as red and may amend the criterion. The DERIVED marker governs, so the skeptic graded it low.
- **Fix (judged sound):** Drop "ten at base". Or write "one per role file under the installed kit's agents/ at observation time (twelve once unit 1 has landed, plus gov-tester where installed)".
- **Left-shift gate:** The spec-tokens leg refuses a typed count on a line marked `figure: DERIVED`.

### L9. Specs 53, 54 and 58 omit the regenerated symbols.json from their write sets (id 32)

- **Where:** spec 58, section 4 Files touched, and the same in specs 53 and 54.
- **What is wrong:** 53 adds `assert_role_reads` and 54 adds `derive_overlay_expected`. 58 adds `readTaskBlocks` and removes `resolve_subagent_dir`. None of the three lists memory/map/generated/symbols.json; of all the specs, only 42 lists it.
- **Consequence:** The always-run `codebase-map coverage + freshness` leg byte-compares symbols.json, so each pass writes a file its declared write set omits. The effect is limited to write-set bookkeeping.
- **Fix (judged sound):** Add `memory/map/generated/symbols.json` (regenerated by `python tools/codebase-map/gen_map.py --write`) to section 4 of specs 53, 54 and 58, as spec 42 does.
- **Left-shift gate:** The spec-tokens leg requires symbols.json in Files touched when a spec adds or removes a function in an indexed file.

### L10. Spec 58 AC21 exercises CR-stripping on the marker shape only (id 38)

- **Where:** spec 58, section 2 S21 and section 6 AC21.
- **What is wrong:** S21 deletes every `\r` before matching. S22 lists four graded line shapes. AC21 tests only a CR-prefixed gov:handoff marker.
- **Consequence:** A build that strips CR only on the marker branch meets AC21. A CR-split fact or heading in `input:question` then passes the authored-line check. Contained, because the spawn guard splits lines the same way.
- **Fix (judged sound):** Loop AC21 over the four shapes (`### `, FACT_RE, MARKER_RE, `Framed by:`), each preceded by `\r` in `--input question=`. Require exit 1 and a failure naming each line.
- **Left-shift gate:** A checklist entry: a rule stated over N shapes is observed on all N.

### L11. Spec 57 S3 names an observer that does not check it (id 39)

- **Where:** spec 57, section 2 S3.
- **What is wrong:** S3 says "Observed by AC1". AC1 calls the description check and never reads section 7, which is where the leg is named.
- **Consequence:** A ledger answer for S3 cites a criterion that does not check it. Behaviour is unaffected, because section 7 already names `memory-recall kit selftest`.
- **Fix (judged sound):** Mark S3 "Observed by: the spec's section 7 line (spec tokens leg)", or drop it as a scope item.
- **Left-shift gate:** A checklist entry for class observed-by-claim-no-arm-discharges.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=39 confirmed=38 refuted=1 unverified=0 blocker=0 high=1 medium=24 low=13 agents=11 out-tokens=189184

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 6 AC18 (and section 2 S18) | high | medium | confirmed | I re-ran `git grep -n 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec`. It printed spec-46:138, spec-48:176, spec-50:265, spec-58:116 (S18) and spec-58:346 (AC18's own command). AC18 requires that probe to print nothing. After 46, 48 and 50 are re-pointed, the two spec-58 lines are still there, so AC18 can never go green as written. Graded medium, not high: a criterion that is always red gets noticed at close. It does not certify anything wrongly. | sound | - |
| 2 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md:section 6 AC3 against section 2 S2, and the section 7 New arm | high | medium | confirmed | At spec-53:48-50, S2 has the case run the plain-words render first, require exit 0 and a written prompt file, and only then run the refusal render. AC3 (:132-134) stages a handoff.py that raises a usage error on every render. That copy makes the control render exit 2, so the case fails at S2's check before S3's exit-2 check is reached. AC3's 'refusal half fails naming the usage error' cannot be observed through this staging. The section 7 arm (:140) claims the usage-error render covers AC3, so S3 can be missing and the arm still goes red. | sound | - |
| 3 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 2 S8 and S9 (ordering against TOOL-dBoundRoles-46 AC3) | high | medium | confirmed | `tail -3 tools/hooks/agent-cap.js` ends in a bare `main()`, and grep finds no `module.exports` or `require.main`. Spec 46 F2 adds the TYPED_INPUTS export but no entry guard. Requiring the file runs main(), which reads stdin at :2235 and calls `process.exit(0)` when the JSON parse fails, before any `node -e` print. So 46 AC3, which names tools/hooks/agent-cap.js, cannot pass at order 12. The README build order puts 46 at step 12, 25 (which moves the file) at step 26, and 58 at step 32. Spec 58 S8/S9 (:84-88) add the guard only in spawn-guard.js at order 32. | sound | - |
| 4 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-52.md:section 4 Rollout | medium | medium | confirmed | Spec-26 Files touched (:166) lists `tools/roles/adopt-roles.test.sh (the arm of §7)`, and its section 7 arm (:229) is that same suite. Spec-52 Rollout (:100-102) says 26 'writes no file this unit writes', yet 52's only product file is that suite. README step 22 lists 26, 52 and 53 and marks the step parallel ('yes'). The Rollout claim is false and hides a write overlap. | sound | - |
| 5 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md:section 6 AC3 (observing section 2 S3) | medium | medium | confirmed | Spec-54 AC3 (:142-144) requires a section 9 line in spec 49 naming TOOL-dBoundRoles-54, and spec 49's AC2 to name the roster. Grepping spec 49, line :167 (the rev-2 section 9 line) already names TOOL-dBoundRoles-54, and AC2 at :139 already says 'roster'. AC3 is green on today's tree, so nothing observes S3's restatement of spec 49. | sound | - |
| 6 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-52.md:section 6 AC3 (observing section 2 S3) | medium | low | confirmed | `grep -n -- '--role gov-builder' tools/roles/adopt-roles.test.sh` printed nothing (exit 1). Spec-47 :161 (rev-2 section 9) already names TOOL-dBoundRoles-52. So nothing observes the spec-bump half of 52 S3: spec 47's S1 and AC1 (:38, :131) can keep spelling gov-builder. One caveat: unit 47 builds the case at order 21, before 52, so the test-file half does bite at 52's real pass time. Only the spec-text half is vacuous, which is why I graded it low. | sound | - |
| 7 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md:section 6 AC1 and the section 7 New arm | medium | medium | confirmed | `load_roles` (roles_lib.py:330-336) returns {} when agents/ is empty. tools/roles/kit.toml:35-39 still lists the ten house/*.md seed includes, and AC1's fixture empties only agents/. Spec-54 S2 (:41-44) reds any seeded overlay no slot owns. So with S1 removed, the compare still fails, naming files. The arm's claim (:145) that removing S1 'lets an empty kit pass' is false. Only the kit-path name in the failure text separates the two states, and the fixture never tests the case where both sides are empty. | sound | fixture-passes-by-finding-nothing |
| 8 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md:section 2 S2 against section 6 AC2 | medium | low | confirmed | Grepping spec 19 finds derive_overlay_expected and TOOL-dBoundRoles-55 only at :13 (records), :99 (consumes-from edge) and :265 (section 9). Its AC1-AC6 (:208-230) never observe the deletion, so 19's ledger has no row for spec-55 AC2's after half. I graded it low: the impact's 'found late at the run's bar' is overstated. Spec 19's section 7 gates (:236) include `govkit selftest`, which would red at 19's own pass if the compare survived without its seeds. | sound | - |
| 9 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 6 AC30 (observing section 2 S30) | medium | medium | confirmed | spec-58.md:374 AC30 runs `grep -n 'ends inside' tools/roles/roles_lib.py` and expects '38 S5's refusal only'. But spec-38.md:64-65 puts S5's refusal in `render_handoff` (tools/roles/handoff.py), and roles_lib.py only gets S3's walker, whose spec wording ('when the text ends inside one', :48) is a docstring at best. The refusal text 38 never fixes. `grep -n 'ends inside' tools/roles/*.py` printed nothing at base. Built as written, the grep either fails on a correct build or passes on a docstring match whether or not 48's end-of-walk clause is gone. So S30 goes unobserved. | sound | - |
| 10 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 2 S5 (and section 4 Evidence) | low | - | refuted | duplicate of id=15. Same defect: S5 at spec-58.md:75-76 and §4 at :244 say the gov-builder render resolves no kickoff checker. But gov-builder.agent.md:7 reads `card:route?`, and handoff.py:359-360 calls resolve_card_path for any `card:` key, which runs the checker when CLAUDE_CODE_SESSION_ID is set (:262-271). | sound | - |
| 11 | coherence | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md:section 2 S5 and section 3 third bullet | low | low | confirmed | spec-56.md:54-61 says 'each holding one live H1 and, in four of them, a decoy H1 inside a fence'. In its own list, fixture 4 (an unclosed fence holding 'the only H1') has no live H1. Fixture 3 (an info string holding a backtick, so not an opener) and fixture 5 (indented four spaces, so not a fence) have no fenced decoy. That leaves three decoys, in fixtures 1, 2 and 4. §3 at :69-71 repeats 'one live H1 each'. §5 at :137 ('an unclosed fence yields no H1 in all three') shows the intent, so the effect is a mis-stated count. | sound | - |
| 12 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 6 AC18 (and section 2 S18) | high | medium | confirmed | I re-ran `git grep -n 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec`. It printed spec-46:138, spec-48:176, spec-50:265, spec-58:116 and spec-58:346. Spec 58's own two lines sit inside the pathspec and survive any correct build, so AC18 ('prints nothing') can never go green. It stays visibly red rather than falsely green: the builder must reword the spec or answer it by hand, so the effect is contained. I grade it medium, not high. | sound | - |
| 13 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md:section 6 AC3 (observes section 2 S3) | medium | medium | confirmed | spec-54.md:142-143 AC3 needs a grep for 'TOOL-dBoundRoles-54' over spec 49 to print a §9 line, and 49's AC2 to name the roster. At HEAD, spec-49.md:167 is already a §9 line naming TOOL-dBoundRoles-54 (rev-2), and :139 AC2 already reads 'not tied to the roster'. So AC3 is green before unit 54 is built and cannot catch a skipped S3 rev bump. | sound | - |
| 14 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-52.md:section 4 Rollout | medium | medium | confirmed | spec-52.md:100-101 says 'TOOL-dBoundRoles-26 holds order 22 and writes no file this unit writes'. spec-26.md:166 lists `tools/roles/adopt-roles.test.sh` in Files touched, and :229 adds its new arm there. Spec 26 carries order 22, as do 52 (:106) and 53 (:101), and both of those write the same suite. Grepping spec 26 for TOOL-dBoundRoles-52/53 matched only the records table at :13, and 52's Edges name 47 and 53, not 26. So the disjointness claim is false and no edge serialises the three writers. | sound | - |
| 15 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 2 S5 and section 6 AC5 | medium | medium | confirmed | gov-builder.agent.md:7 reads `input:spec, card:route?, brief:non-goals?`. handoff.py:358-359 calls resolve_card_path for any `task:` or `card:` key. That function (:262-271) reads CLAUDE_CODE_SESSION_ID and runs the checker resolve_kickoff_checker finds. The checker is located from KIT_DIR.parent (:246), not from the fixture root, so inside a session the control render can run the real checker and pull a real card's route. That contradicts S5 (spec-58.md:75-76) and §4 (:244, which says ':340-346 resolves a kickoff checker only for a `task:` key'). AC5 (:315-316) checks only `task:` and required `brief:` keys. | sound | - |
| 16 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md:section 6 AC3 and section 7 New arm, against section 2 S2/S3 | medium | medium | confirmed | spec-53.md:48-50 S2: the case runs the plain-words render and 'requires exit 0 and a written prompt file before it runs the refusal render'. :132-134 AC3 stages a handoff.py that 'raises a usage error for every render'. Under that staging the control render exits 2 first. The refusal half's exit-2 arm (S3, :51-53) is then never reached, so the break reads red without exercising S3. The fix's trigger exists: spec-47.md:40 shows the refusal render's input carries `record:TOOL-tFix-9@...`, and the plain-words control render carries none. | sound | guard-above-a-fold-makes-its-fallback-dead |
| 17 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md:section 5 risks (and section 7's `kickoff engine size <=18KiB` leg) | low | low | confirmed | Spec 56 line 140 reads 'the kickoff engine's size leg reads `manifest-check.sh`'s bytes'. tools/gate-legs.json:151-155 gives the 'kickoff engine size <=18KiB' leg the argv `bash {prefix}/check-template-size.sh skills/session-kickoff/SKILL.md`. `wc -c` printed 102522 for manifest-check.sh and 18310 for SKILL.md. The risk line is false, and growing the awk does not touch that leg. The only effect is a misleading sentence, so low. | sound | - |
| 18 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md:section 2 S2 and section 4 Evidence (parse_spec_h1 consumers) | low | low | confirmed | `git grep -n parse_spec_h1` printed memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:274 (over working-tree specs) and :608 (over `git show {base}:{rel}`). Spec 56 S2 (lines 44-47) and §4 Evidence (line 91) list only gen_build_index.py, extract.py, deviation_join.py and routed_commits.py. The §4 Measured paragraph covers tracked specs at HEAD only. The omission is real. Its effect is contained, because no HEAD spec id moves under the new rule. | sound | - |
| 19 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-52.md:section 6 AC3 (also TOOL-dBoundRoles-58 section 6 AC6) | low | low | confirmed | Spec 47's §9 already holds 'rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-52 and -58', and spec 45's §9 rev-2 line names TOOL-dBoundRoles-58. So 52 AC3's half 'unit 47's spec carries a §9 line naming TOOL-dBoundRoles-52' and 58 AC6's half 'the spec's §9 names TOOL-dBoundRoles-58' are both green at HEAD and cannot observe the S3/S6 restatement bumps. The grep half of each criterion still observes the change, so the effect is cosmetic coverage. | sound | - |
| 20 | grounding | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md:section 5 perf / scale (also TOOL-dBoundRoles-56 section 2 S5) | low | low | confirmed | Spec 53 §5 line 113 says 'one `python3 -c` read of the roster per call'. Spec 56 S5 (line 59) puts a case in tools/hooks/scratch-guard.test.sh that reads the id 'via `python3 -c` over `tools/memory-tree`'. Both suites already resolve a launcher by running it: adopt-roles.test.sh:60 sets `PY` by running each of GOV_PYTHON/python3/python/py, and scratch-guard.test.sh:127 sets `TESTPY=$(resolve_python)`. The comment at :56 warns that the Store python3 stub answers to the name. Spelling `python3` literally invites a platform-dependent failure. It is low because only wording steers the builder. | sound | - |
| 21 | reuse | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md:section 2 S1 (and its Readers clause), section 4 Evidence, section 10 | high | high | confirmed | Spec 53 S1 (lines 41-47) reads `reads` via load_roles and 'the parse tools/roles/handoff.py:1025-1026 makes (split on commas, strip, drop a trailing ?)', which S1 'copies without changing'. handoff.py:1025 today is `{x.strip().rstrip("?") for x in keys.get("reads","").split(",")}`. load_roles (roles_lib.py:331-335) returns the raw front-matter keys and does no folding. Spec 14 S7 rewrites every gov role's `reads:` line to tag spelling (`field.input.spec`). Spec 14 S4 adds parse_read_key and moves render_handoff onto it. The generated build order puts 14 at step 1 and 53 at step 22 (README :186, :207). At order 22, S1's copy therefore yields `field.input.question`, and `assert_role_reads gov-orienter input:question` fails on a correct tree. S1 also adds a second read-key parse that is out of date. A gate-red suite would expose it at build, so it would not ship silently. It does mislead the build and lets AC1 pass for the wrong reason, which makes it high. | sound | - |
| 22 | reuse | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 6 AC5 (S5) | medium | medium | confirmed | Spec 58 AC5 (lines 315-316) reads the control role's `reads` 'through roles_lib.load_roles' and requires that it 'holds no task: key and no required brief: key'. load_roles returns the raw entries. After spec 14 S7 (order 1, before 58 at order 32), gov-builder's line `reads: input:spec, card:route?, brief:non-goals?` becomes `field.*`, so no raw entry can begin with task: or brief:. AC5 cannot go red, and its stated Red-when is not checked. AC4's render with no brief and no card still observes the behaviour, so the effect is contained. | sound | - |
| 23 | reuse | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-52.md:section 4 Evidence, section 2 S1 | low | low | confirmed | Spec 52 S1 (lines 41-42) cites the base spelling `input:question, input:prompt?` at gov-orienter.agent.md:8, and §4 (lines 80-81) says 'no spec of this build changes its reads'. `grep '^reads' gov-orienter.agent.md` printed `reads: input:question, input:prompt?` today. Spec 14 S7 (order 1) rewrites that line to tag spelling before 52 builds at order 22. What the role reads is unchanged, so the role choice holds. The cited text and the claim are stale, so the defect is cosmetic. | sound | - |
| 24 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 6 AC18 (and section 2 S18) | high | medium | confirmed | `git grep -n 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec` printed 46.md:138, 48.md:176, 50.md:265, 58.md:116 (S18) and 58.md:346 (AC18's own command). AC18 requires that command to print nothing, and spec 58 always matches itself, so a correct build can never turn it green. The failure surfaces the first time the build runs the criterion and forces a restatement. It does not certify anything falsely, so I grade it medium, not high. | sound | - |
| 25 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md:section 4 Files touched / section 2 S3 / section 7 | medium | medium | confirmed | memory/guides/SESSION-KICKOFF.md:6 has skills/session-kickoff/manifest-check.sh in its watch list. 56 S3 edits that file, and 56 section 4 Files touched lists it. .githooks/pre-commit:191-192 runs `bash "$g" --staged`. manifest-check.sh:1589-1597 has C5s fail when a watched file is staged and the staged blockstamp equals HEAD's, with the message 'bundle the re-stamp into THIS commit'. Files touched names only tree_lib.py, manifest-check.sh, scratch-guard.js and scratch-guard.test.sh. A grep of the spec dir finds SESSION-KICKOFF.md in no spec's write set. The section 7 leg line (56.md:165) leaves out `kickoff-manifest ratchet`, which gate-legs.json lists as an unguarded leg. So the pass commit is refused unless it writes a file outside its declared write set. | sound | - |
| 26 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md:section 6 AC1 | medium | low | confirmed | 54.md:3 says order 6, and AC1 (54.md:132-134) reads 'one house overlay path per role file, ten at base' next to 'figure: the set is DERIVED'. `ls tools/roles/agents` at HEAD lists 10 files. Unit 1 (order 3) S2 adds four role files and S3 removes gov-spec-reviewer and gov-diff-reviewer, so the roster at unit 54's pass has 12 slots. 'At base' is literally true of base 462d20f3, but the typed figure does not match what the pass observes. The DERIVED marker governs the criterion, which limits the harm to a misleading count. That is low. | sound | - |
| 27 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-52.md:section 4 Rollout | medium | medium | confirmed | 52.md Rollout says 'TOOL-dBoundRoles-26 holds order 22 and writes no file this unit writes'. Unit 26's status line says order 22, and its Files touched lists `tools/roles/adopt-roles.test.sh` (the arm of section 7). That is the only file 52 lists besides 47's spec, and 53 lists it too. Neither 52 nor 53 has any edge or ordering against 26, so the disjointness sentence is false. | sound | - |
| 28 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md:section 2 S2 (Readers clause) | medium | medium | confirmed | 55 S2's Readers clause names 54.md and 49.md:65, then says 'nothing else reads it', and gives no disposition for either reader. Only 55 AC2 carries a permission/before-and-after scope line, and AC3 says 'before unit 19's pass'. 54 AC1 and AC2 (54.md:130-141) carry no such scope. The finding also understates the problem. BUILD-METHOD M8:280-282 makes the closing main loop observe every `New arm:` line red-then-green. 54.md:150 has a New arm on tools/govkit/selftest.py covering AC1 and AC2, staged on the roster-side compare. 55.md:145 has a New arm covering AC1, staged on the empty-set test. Unit 19 (order 24) deletes both before the close, so those arms cannot be staged at M8. | unsound | - |
| 29 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 6 AC30 (section 2 S30) | medium | medium | confirmed | 58.md:374 AC30 greps only tools/roles/roles_lib.py and expects '38 S5's refusal only'. 38.md:64 places S5's refusal in `render_handoff`, and `grep -n 'def render_handoff' tools/roles/*.py` prints tools/roles/handoff.py:312. 38 S3 gives roles_lib's read_unfenced_lines only a `(opened at, None)` sentinel, not the refusal text. On a correct build, then, the refusal is not in the grepped file. The criterion cannot be met as worded, and a check_block_fences end-of-walk clause worded differently would pass it silently. | sound | - |
| 30 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md:section 2 S5 / section 7 | medium | medium | confirmed | gate-legs.json gives `scratch-guard self-test` the guard ['{prefix}/hooks/', '{prefix}/lib/', 'skills/session-kickoff/']. Running `python tools/check-spec-tokens.py --legs-for tools/memory-tree/tree_lib.py` lists legs through tools/memory-tree/ and tools/, but not `scratch-guard self-test`. 56 S5 puts the three-reader parity case in tools/hooks/scratch-guard.test.sh, and tree_lib.parse_spec_h1 is one of the three readers. A tree_lib-only change therefore skips the parity case on a guarded run. 56 states nowhere that this case is caught only at the full bar. | sound | - |
| 31 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md:section 5 risks | low | low | confirmed | 56.md:140 says 'the kickoff engine's size leg reads `manifest-check.sh`'s bytes'. In gate-legs.json, `kickoff engine size <=18KiB` has argv ['bash','{prefix}/check-template-size.sh','skills/session-kickoff/SKILL.md'], so it measures SKILL.md only. The risk line's premise is false, and it misses the real kickoff-side effect, the watched-file re-stamp. | sound | - |
| 32 | blast-radius | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 4 Files touched (also 53 and 54 section 4) | low | low | confirmed | symbols.json indexes functions from these files: adopt-roles.test.sh 3, govkit/selftest.py 45, handoff.py 28, roles_lib.py 23. 53 mints `assert_role_reads` (sh.function), 54 mints `derive_overlay_expected` (py.function), and 58 mints `readTaskBlocks` and folds away `resolve_subagent_dir`. None of the three lists memory/map/generated/symbols.json in Files touched. `grep -rl symbols.json` over the spec dir matches only 42.md, which lists it at line 131. The pass will write a regenerated file its declared write set omits. The effect is contained to write-set bookkeeping. | sound | - |
| 33 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-57.md:section 2 S1; section 6 AC1 | medium | medium | confirmed | Confirmed. tools/memory-recall/selftest.py:1610-1618 splits the rendered text on '---' and checks tokens only in `desc = parts[1]`, which is the front matter. `grep -nwE 'Grep\|Glob' tools/memory-recall/SKILL.template.md` printed line 15 and line 66 ('Only then fall back to `Grep` over ...'). Line 66 is body text. 57 S1 (lines 35-40) puts the no-search-tool assertion on 'the rendered description' only, so if the body's fallback went back to `Grep`, the kit's self-test would not catch it. 57 cites the 51 S8 rewording of both :15 and :66 (57.md:21), but it pins only one of them. | sound | - |
| 34 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-57.md:section 6 AC1 | medium | medium | confirmed | Confirmed. selftest.py:94-103 `check(name)` calls `fn()` inside the decorator, so every check runs when the module is defined. `grep -n '^@check' \| wc -l` printed 86, and test_skill_description_invariants is decorated (line 1597). The `__main__` guard at :3589 does not stop the decorators from running on import. So AC1's 'imports ... runs no suite' cannot hold. copy_extra at :1348-1351 copies `KIT / n` with KIT = the module's own directory (:71), and the check takes no parameter. A 'scratch copy of the template' therefore cannot reach the check unless the whole kit is copied and imported, which runs the full suite again. | sound | - |
| 35 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md:section 2 S1 and S2 | medium | medium | confirmed | Confirmed. govkit.py:322-338 `rule_sources` returns `f"{home}/{s}"`. resolve_rule_pool (:6669) returns that list for a list include, and planned_writes (:4048) stores it as `src`. tools/roles/kit.toml:6 sets `home = "roles"`, so a row's src is prefixed (roles/house/<slot>.md), while 54 S1 yields bare `house/<slot>.md`. S2 never says how the two forms are normalized before the compare, so a literal compare finds no match. Small point: the prefix is the descriptor's home ('roles'), not 'tools/roles' as the finding wrote. That does not change the defect. The fix reads home from the descriptor, so it handles this correctly. | sound | - |
| 36 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md:section 7 New arm; section 6 AC1; section 2 S1 | medium | medium | confirmed | Confirmed. 55 AC1 (lines 127-129) empties only `agents/`. tools/roles/kit.toml:35-39 still seeds ten house/*.md overlays in such a copy. 54 S2 (lines 41-44) reds 'a seeded overlay no slot owns ... naming the file', so the compare fails with S1 present or removed. 55 §7 line 145 says removing S1's length test 'lets an empty kit pass', and that is false for the case AC1 builds. The only case where S1 alone makes the difference is when both sides are empty, and neither AC1 nor the arm builds it. | sound | - |
| 37 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 7 New arm lines (also 53 §7 and 52 §7) | medium | medium | confirmed | Confirmed. `grep -n FLOOR_ASSERTIONS tools/roles/adopt-roles.test.sh` printed :81 `FLOOR_ASSERTIONS=50`, SKIP decrements at :170/:172, and the floor check at :714. The comments at :75-80 record a '+n for arm k (unit)' entry each time arms were added. TEMPLATE-SPEC.md:280 defines the last field as '<floor to move, or none>'. 52.md:154, 53.md:140 and 58.md:394-395 all end `· none`, while 43.md:524 for spawn-guard.test.sh says '`FLOOR_ASSERTIONS` raised'. spawn-guard.test.sh does not exist yet at base, since unit 43 creates it with a floor. If the new arms are not counted, the floor cannot detect that they were skipped. | sound | - |
| 38 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md:section 2 S21; section 6 AC21 | low | low | confirmed | Confirmed. 58 S21 (lines 130-132) deletes every \r from each line before matching, and S22 (lines 139-141) lists four graded shapes on every typed-value line. AC21 (lines 354-355) only exercises `\r` followed by a gov:handoff marker line. A build that strips CR only on the marker branch would still pass AC21. The effect is contained, as the finding says. | sound | - |
| 39 | failure-envelope | memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-57.md:section 2 S3 | low | low | confirmed | Confirmed. 57.md:43-44 says S3 is 'Observed by AC1'. AC1 (57.md:120-125) is a python -c call of test_skill_description_invariants and never reads §7. §7 (line 132) does name `memory-recall kit selftest`, so the link is wrong but has no effect on behaviour. | sound | observed-by-claim-no-arm-discharges |
