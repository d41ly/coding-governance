**Serves:** spec-audit KICK-dKeptSession-63@rev-1

# Tier-2 spec audit — dKeptSession, the round-4 minors batch (KICK-dKeptSession-63), ROUND 1

*This is an adversarial pre-code pass over the unit that the round-4 spec audit promoted, dated 2026-10-26. Five lenses found the findings: coherence, grounding, reuse, blast-radius and failure-envelope. A skeptic then tried to refute each one. Only confirmed findings appear below. Each item gives its address, its consequence, the fix and a left-shift gate.*

Reviewed: memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md@667d5701dc6941349d3de1b221eaf9cc9e56e718

ROUND 1

## Verdict: CLEAN WITH FIXES

The audit found no blocker and no high, so the verdict is CLEAN WITH FIXES.
There are 16 items: 0 blocker, 0 high, 10 medium and 6 low.
Counted by raw confirmed finding, that is 20: 0 blocker, 0 high, 13 medium and 7 low.
Every item must still be fixed in the spec before the unit is built.

## Review shape

Intensity full, raw 22, confirmed 20, refuted 2, unverified 0 (0 uncertain), precision 0.91.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 8 | 7 | 1 | 0 | 0 | 0.88 |
| failure-envelope | yes | 4 | 3 | 1 | 0 | 0 | 0.75 |

Run integrity: lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
No verdict was demoted to unverified, no spurious verdict was discarded, and there were no duplicates.
Fixes on confirmed findings: 20 judged sound, 0 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
Severity on confirmed findings: 0 ungraded, 3 re-graded by the skeptic (ids 9, 10 and 11).
No lens notes were supplied, so every lens ran on the kit's generic brief.
Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
Intent: 62 spec documents were supplied as `specs`, as sibling context.
Checklist: 57 items, each assigned to one lens (coherence 12, grounding 12, reuse 11, blast-radius 11, failure-envelope 11).
By design: 1 invariant from the checklist's by-design block.
Move check: no checked subject moved.
The run is complete: every count above that must be zero is zero.

Merges: ids 4, 15 and 19 describe one defect (the S15 skip-versus-refusal order) and form one item. Ids 2 and 20 describe one defect (the S17 ledger rule written for one leg) and form one item. Ids 7 and 17 describe one defect (the S24 carriers left out) and form one item. Id 20's second half (S13 never adds `loop selftest`) is the defect of id 14 and is answered there; id 20 is counted once, in item M4.

## Medium

### M1. S15 never says whether a repeated ack is a skip or a refusal (ids 4, 15, 19)

**Where:** section 2 S15; section 6 AC15 and AC27.

**What is wrong:** S15 runs every id's ack through `derive_message_id` and `check_mail_duplicate` before any commit, and says "One refusal refuses the batch with exit 2". It also says "An id already acked is skipped" and prints `mail — already acked <id>`. The message id takes no session and no time (KICK-dKeptSession-22 S2), so a re-ack of `<a>` derives the same id, and `check_mail_duplicate` returns rc 1 for it. By S15's own sentence, that rc 1 is a refusal. S15 gives no order between the two checks, no predicate for "already acked", and no exit status for a skip. It also never names as superseded unit 5 S5's "a duplicate post exits 1" or unit 22's retry row (`mail — duplicate <id>`, rc 1, refused). AC15 checks only the stderr line and the tip. It never asserts an exit status and has no mixed batch.

**Consequence:** Built in the written order, a repeated `--mail ack <slug> <a>` exits 2 with `mail — duplicate <id> · <ref>` and fails AC15. A batch that mixes one acked id with new ones is refused whole, so the new acks never land. Built the other way, AC15 passes but the exit status is unpinned. That status matters to unit 42 AC4, which refuses a transition as "ack not posted" when `--mail ack` exits 1. Unit 5's duplicate case and its VERBS line also go stale, and AC27 asks no answer from unit 5 or unit 22.

**Fix (judged SOUND by the skeptic):** State the order and the predicate. "Already acked" is the S7 state read for the id (a cached ack whose answers names it), checked before `derive_message_id`, and a skipped id never reaches `check_mail_duplicate`. The skipped id is named on stderr and left out of the batch. Any rc 1 from `check_mail_duplicate` on an id not read as acked, any rc 2, or a failed addressed-to check refuses the batch with exit 2. A batch in which every id is skipped exits 0 and writes nothing. Name unit 5 S5's exit-1 duplicate and unit 22's retry row as superseded for `--mail ack`, and add both to AC27. Make AC15 assert the second call's exit (0) and add a mixed batch `<a> <c>` with `<a>` already acked, which lands only `<c>`'s ack and exits 0.

**Left-shift gate:** A bug-class checklist entry: "a spec that adds a skip beside an existing refusal on the same input states which check runs first and the skip's exit status". An acceptance criterion that names an output line and not its exit status is a red case for the spec-audit lens.

### M2. AC27's population leaves out superseded sibling texts (id 1)

**Where:** section 6 AC27, against section 1 and section 2 S2, S8, S11, S12, S22, S23, S24 and S26.

**What is wrong:** Section 1 says AC27 decides that every superseded sibling text has its ledger answer. AC27 (spec lines 375-378) lists only units 53, 57, 60, 61 (S1, S2, Inventory) and 62 (S1, S15's sketch, S20, S22, S24, S26, AC20, AC25, section 4 Evidence). Section 2 supersedes more than that. Missing are unit 59's unanchored `re.search` sketch (replaced by S8 and S26). Also missing are unit 61's AC3, section 4 "its caller" (rewritten by S22), Files touched, section 5 observability and section 7 arm, all of which still name the `--mail chain` verb that S11 retires. Unit 62's S19 (S23), S31 (S24) and section 5 "seven definitions" (S2) are missing as well. AC27 also names one unit 62 text two ways: S12 calls it "section 4's ack-chain sketch", while AC27 and the Edges call it "S15's sketch".

**Consequence:** A correct build can pass AC27 and still leave unit 61's AC3 in force. That AC3 requires `bash unattended.sh --mail chain <parent>` to print four rows, and this unit forbids the verb. Units 59 and 62 likewise keep texts that contradict the code as built, and nothing in AC27 shows they were dropped. The next change that reads those specs is misled.

**Fix (judged SOUND by the skeptic):** Make AC27's list match every "superseded by name" and "reads as" clause in section 2. Add unit 59's section 4 regex sketch (S8, S26). Add unit 61's AC3, section 4 "its caller" and Files touched, section 5 observability and section 7 arm. Add unit 62's S19, S31 and section 5. Spell the unit 62 sketch one way everywhere, for example "S15 and section 4's ack-chain sketch".

**Left-shift gate:** A check in `tools/check-spec-tokens.py` that every "superseded" or "reads as" clause naming a sibling `<unit> <section>` appears in the same spec's ledger-answer criterion. Where no gate fits yet, a checklist entry.

### M3. S11 says unit 61's reader is "never minted", but unit 61 builds it first (id 12)

**Where:** section 2 S11; section 4 Files touched; section 6 AC27.

**What is wrong:** S11 says unit 61's `read_mail_chain` and `--mail chain` are "superseded by name and never minted". Unit 61 is order 27 and this unit is order 34, and section 1 says each item amends code its unit has built. So both already exist when this unit is built. AC11 requires `grep -c read_mail_chain unattended.sh` to print 0, which forces a deletion that section 2 and section 4 never state.

**Consequence:** The builder has to delete a function and a verb with no instruction to do so. The deletion breaks or stales unit 61's AC3 (`--mail chain <parent>` prints four rows), the `tools/loop/selftest.py` arm that covers it, the `--mail chain` line unit 61 adds to `tools/unattended/VERBS.template.md`, and unit 61's section 5 observability and user-docs lines. AC27 asks unit 61 to answer only S1, S2 and the Inventory, so those texts get no answer.

**Fix (judged SOUND by the skeptic):** Replace "never minted" with an explicit retirement. Remove `read_mail_chain` and the `--mail chain` dispatch row from `unattended.sh`, and the `--mail chain` line from `VERBS.template.md` and its render (see M9). Move unit 61's loop-selftest AC3 case to `--mail read <parent> --cached --sent`. Add unit 61's AC3, its section 7 arm and its section 5 user-docs line to AC27's list.

**Left-shift gate:** A checklist entry: "a spec at a later order that retires a name an earlier-order sibling mints says 'remove', lists the sibling's callers, arms and docs, and never says 'never minted'".

### M4. The ledger rule of S17 covers `loop selftest` alone, so AC9 demands lines naming a leg that does not exist (ids 2, 20)

**Where:** section 2 S9, S13 and S17; section 6 AC9 and AC17; section 7.

**What is wrong:** S17 says a refused query writes a `GAP —` line, never a leg list, and that a line names a leg only when `tools/gate-legs.json` carries it, else `NOT RUN —`. It writes that rule for `loop selftest` alone, and AC17 tests only that leg. At this base `policy fixtures` is just as absent: `grep -c '"policy fixtures"' tools/gate-legs.json` prints 0, `tools/policy/` is untracked, and `--legs-for` over the policy paths refuses with exit 2. Yet AC9 requires the ledgers of units 58, 59 and 60 to each carry a line naming `policy fixtures`, and unit 61's to name `loop selftest`.

**Consequence:** A builder who follows S17 fails AC9. To pass AC9, a builder has to write ledger lines naming legs the query never printed. That is the false-clean record S17 exists to forbid, and AC17 exists to red. Either way the acceptance does not decide the item.

**Fix (judged SOUND by the skeptic):** Rewrite S17 as the class: a line names a leg L only when `gate-legs.json` at that pass carries L, otherwise `NOT RUN — <L> not declared`, for `policy fixtures` and `loop selftest` alike. Add the `policy fixtures` case to AC17. Restate AC9 to follow S17. Each unit whose Files touched trips either guard, or whose query refuses or reads untracked paths, carries one line: the leg list, `GAP —` with the query's exit and output, or `NOT RUN —` with the reason. This unit's ledger lists the population it derived, and AC9's red case is a unit with no line. Alternatively, gate AC9 on the reconcile tip that S13 names.

**Left-shift gate:** A ledger lint that reds a ledger line naming a leg absent from the `tools/gate-legs.json` of the tree that pass ran on.

### M5. AC13 cannot fail on this unit's own tree (id 3)

**Where:** section 6 AC13, against section 2 S13 ("This unit's pass re-checks the step on its own tree"). Class C31, liveness negative from another population.

**What is wrong:** AC13 applies only when `grep -c '"policy fixtures"' tools/gate-legs.json` prints 1. On this unit's tree it prints 0, and `--legs-for` over units 58 to 60 refuses with exit 2 because the policy paths are untracked. So the re-check that S13 says this unit's pass runs is green before anything is built. Nothing in the spec requires this pass to run on a reconciled tip, and nothing says which pass owns AC13.

**Consequence:** This unit's pass certifies S13's reconcile step without exercising it. A reconcile that drops `policy fixtures` from a leg line goes unseen until some later pass, which the spec does not require to run AC13.

**Fix (judged SOUND by the skeptic):** Either drop S13's claim that this unit's pass re-checks the step, or make AC13 run against a scratch manifest that declares `policy fixtures` with a guard over `tools/policy/`, plus a scratch spec tree. Its red case is a spec missing the name, written as the probe the build runs. State that AC13 at the real reconcile is owned by the reconcile pass.

**Left-shift gate:** The existing liveness class C31 in the checklist: every conditional criterion names a tree where its condition holds and a red probe that runs there.

### M6. S13's reconcile step fixes `policy fixtures` and leaves the class open for `loop selftest` (id 14)

**Where:** section 2 S13; section 7 prose under the leg line; section 6 AC13.

**What is wrong:** S13 and AC13 cover only `policy fixtures`. `origin/main` declares `policy fixtures` and not `loop selftest`, and this branch's manifest has neither. This spec and its siblings touch `tools/loop/` (this unit's `loop_transition.py` and `loop/selftest.py`, units 61 and 53), and dDeclaredLoop will declare `loop selftest`. Section 7 names `loop selftest` only in prose and says "S13 adds the first to the line above". The spec-tokens guards join does not read that prose. No spec adds `loop selftest` to a section 7 leg line.

**Consequence:** When the branch reconciles onto a base that declares `loop selftest`, the guards join reds again for every open spec whose Files touched trips `tools/loop/`, this unit included. That is the round-4 id-18 defect, fixed for one instance and not for its class. The bar catches it at landing, so the effect is contained.

**Fix (judged SOUND by the skeptic):** State S13 as the class. At each reconcile, for every leg the reconciled base's `tools/gate-legs.json` declares and HEAD's did not, add the leg's name to the backtick leg line of every non-terminal spec whose Files touched `--legs-for` maps to it. Re-run it on `loop selftest` once dDeclaredLoop lands. Widen AC13 to iterate over the newly declared legs, not only `"policy fixtures"`.

**Left-shift gate:** A reconcile step in the lander or the reconcile pass that diffs the declared leg names between the two bases and runs the guards join over every open spec of the build.

### M7. S14's environment scrub lives in the wrong place, so in-process cases still read the ambient remote (id 5)

**Where:** section 2 S14; section 6 AC14. Class C22, fixture inherits ambient machine state.

**What is wrong:** S14 says `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` are "unset by `build_arm_env` beside the `GIT_*` scrub". The two are not in one place. The `GIT_*` scrub is a module-level `del os.environ[...]` at import (`tools/runlog/selftest.py:355-356`). `build_arm_env` (`:1515-1520`) copies `dict(os.environ)` and only shapes the environment passed to subprocess runs. The selftest also calls `rl_model.build_run_model` in-process (`:2585`), and that call reaches `resolve_remote` (`model.py:652`, via `read_refs` at `:690`), which `build_arm_env` does not cover.

**Consequence:** On a machine that exports `GOV_REMOTE` (`post-merge.sh:86` does), every in-process model case still reads that value, so the fixture behaves differently there. AC14's second clause checks only what `build_arm_env` returns, so it passes while the leak stays.

**Fix (judged SOUND by the skeptic):** Unset `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` in `os.environ` at import, next to the `GIT_*` loop at `selftest.py:355`. KICK-dKeptSession-62 S26 already says "unset at import" there. Make AC14 also run an in-process `rl_model.build_run_model` (or `resolve_remote`) under `GOV_REMOTE=planted` and show it ignores the planted value.

**Left-shift gate:** The existing C22 class in the checklist, extended: a fixture scrub criterion observes both the subprocess environment and an in-process read.

### M8. S7 claims a gate leg runs `unattended.test.sh`, and none does (id 11)

**Where:** section 2 S7; section 7, the first New arm line.

**What is wrong:** S7 says `unattended.test.sh` is a suite "which a selftest leg runs when tools/unattended/unattended.sh changes". No leg in `tools/gate-legs.json`, `run-gates.sh` or `remote-ci.yml` runs it. `tools/unattended/kit.toml:47-50` says the suite file ships and the leg does not. The suite runs only from the `unattended driver selftest shard k/8` rows of `tools/run-gates/selftest-budgets.txt:122-129`, which `run-unattended-gates.sh` picks up. The floor is also unclear: `unattended.test.sh` has two `FLOOR_ASSERTIONS` assignments, the one at `:17665` is marked SHADOWED, and the effective pin is `FLOOR_ASSERTIONS=2776` at `:17940`. "FLOOR_ASSERTIONS rises" names neither the pin nor the shard's budget row.

**Consequence:** The new arm for AC7, AC11, AC12, AC15 and AC16 runs at no merge bar. Round-4 audit id 1 (M4) was about the chain read having no arm in a leg that runs, and this fix moves the arm into a suite the bar never runs. The defect stays open while section 7 reads as covered.

**Fix (judged SOUND by the skeptic):** Rewrite S7 to say what is true: `unattended.test.sh` is a withheld suite run by `tools/unattended/run-unattended-gates.sh`, through its shard rows, and not a gate leg. Then either put the AC7/AC11/AC12/AC15/AC16 arm in a suite that a guarded leg runs, or record the gap as [gate] requires, with a VERIFYING step that runs the matching shard of `run-unattended-gates.sh`. Name the effective floor (the `:17940` pin and its mode-selected shard floor, not the shadowed `:17665` one) and the shard's `selftest-budgets.txt` row.

**Re-grade:** The finder graded this high. The skeptic graded it medium because the arm exists and runs under the owner's shard runs. What remains is a false coverage statement. The binding grade is medium.

**Left-shift gate:** A spec-tokens check that every suite a section 7 arm line names is run by a leg in `tools/gate-legs.json`, or is marked withheld with its runner named.

### M9. The VERBS template's render is missing from Files touched (id 13)

**Where:** section 4 Files touched; section 5 user docs.

**What is wrong:** The spec edits `tools/unattended/VERBS.template.md` for S11 and S15 but does not list its dogfooded render, `memory/guides/UNATTENDED-VERBS.md`. `check-unattended.sh` check 10 (`:3152-3153`, `_c10_cmp`) byte-compares the two. Unit 5 names this pair ("rendered to `memory/guides/UNATTENDED-VERBS.md`"), and units 21, 24, 25 and 27 list it as "its render".

**Consequence:** An edit to the template alone turns `unattended kit gate` red with the drift message. The render's path is also missing from the write set that dispatch draws from. The gate catches it, so the effect is contained.

**Fix (judged SOUND by the skeptic):** Add "memory/guides/UNATTENDED-VERBS.md, the render of VERBS.template.md, regenerated by `bash tools/unattended/adopt-unattended.sh`" to section 4 Files touched, next to the template, as unit 5 does.

**Left-shift gate:** A spec-tokens check that a Files touched list naming a template with a known render also names the render. The template-to-render pairs are already declared by check 10.

### M10. F1's ask leaves deletion and create undefined and does not price the change for other writers (id 21)

**Where:** section 8 F1 (resolved option (a)); section 2 S16; section 5 security and risks.

**What is wrong:** F1(a) has `write_gov_ref`'s success exit append "one line per first-parent commit between [`<tip read>` and the landed tip], oldest first, the tip last". It defines no case for the two `write_gov_ref` shapes where "between" is undefined. A deletion has an empty `<src>` (TOOL-dPlacedRequest-11 S1), and a create has an empty expected sha. TOOL-dPlacedRequest-13 S3 has a separate deletion branch at that exit, and KICK-dKeptSession-23 relies on it for the mailbox prune. Claims, leases, registers, cards and bar-red all share `write_gov_ref`, and F1 itself says (a) "covers every multi-commit governance-ref write in the one writer". Section 5's risks line speaks only of unit 5's callers.

**Consequence:** Built as `rev-list --first-parent <src> ^<expected>`, a deletion has no landed tip, so the walk prints nothing or fails. That drops the deletion event the mailbox prune needs. A `<src>` that does not descend from the expected tip (a rewritten card or bar-red ref) would put its whole unseen ancestry into the feed. Nothing prices the change for the non-mail writers. The effect stays inside the feed and its census.

**Fix (judged SOUND by the skeptic):** Have the ask spell out all three cases. A deletion keeps S3's single deletion event. A create (empty expected) appends the new chain oldest first. Otherwise reuse `add_feed_sightings`'s existing walk (TOOL-dPlacedRequest-13 S4: the unseen first-parent chain oldest first, stopping at the newest commit the feed holds for the ref or at the first non-`gov-claim` commit), not a second walk. Add a criterion that a delete through `write_gov_ref` still appends exactly one event. List the non-mail callers under section 5 risks.

**Left-shift gate:** A checklist entry: "an ask that changes a shared writer enumerates the writer's input shapes (create, update, delete) and its callers outside the asking build".

## Low

### L1. S25's single `MARKER_LEAD` spans three regex dialects (id 6)

**Where:** section 2 S25.

**What is wrong:** S25 says one `MARKER_LEAD` variable "matching `# ` or `// `" serves all three sites in `resolve-python.test.sh`. Those sites use three dialects: awk (ERE) in `blk` at `:213`, `git grep -l` (BRE by default) at `:218`, and `grep -c` (BRE) at `:224`. The spec names no spelling and no per-site flag. Probed with `M='(# |// )'` against `tools/runlog/model.py`, `grep -c` printed 0, `grep -cE` printed 1, and awk matched 1 line.

**Consequence:** Spelled as ERE, `grep -c` prints 0, `nblk` is 0, the per-copy loop never runs, and the copies are silently not compared. AC25's own red case should catch this, but the design text points the builder at the trap.

**Fix (judged SOUND by the skeptic):** Name the dialect in S25. Spell `MARKER_LEAD` as ERE and switch the population read and the count to ERE (`git grep -E`, `grep -cE`), or spell it once per dialect. Keep AC25's `nblk` red as the observed check.

**Left-shift gate:** A checklist entry: "a spec that shares one pattern across tools names its regex dialect and each site's flag".

### L2. S24 rewords the "parallel group" claim at two sites and misses its other carriers (ids 7, 17)

**Where:** section 2 S24; section 6 AC24.

**What is wrong:** S24 lists the texts that say a shared order is the parallel group as `gen_build_index.py:202-203` and `build-readme-surface.md:109`. `git grep -n -i 'parallel group'` also finds `tools/unattended/unattended.sh:13649` ("Units sharing an `order` value are the parallel group and do not block") and `:13692`, `unattended.test.sh:6398`, `tools/workflows/unattended-build.test.sh:1353`, and the prompt string at `tools/workflows/unattended-build.js:2078` and its `.template.js` twin. `unattended.sh` is already in this unit's write set. AC24's `git grep` is scoped to the two named files, so it cannot see the others.

**Consequence:** After the unit lands, the driver's comments and the shipped workflow prompt still say a shared order is one parallel group, while the build index and its dossier say "candidates". A later reader gets two answers, and the next change to the order gate may be misled. Behaviour is unaffected.

**Fix (judged SOUND by the skeptic):** Widen S24 to every carrier, either by listing them or by taking `git grep -n -i 'parallel group' -- tools memory/map` as the population, and look at `unattended.sh:13692`. Widen AC24's pathspec to match, or name each excluded hit with its reason. Leave `TEMPLATE-SPEC.md:84` and `SPEC-TEMPLATE.template.md:84` out, since unit 62 already hands those off.

**Left-shift gate:** A checklist entry: "a reword criterion derives its population from a repo-wide grep and names each exclusion, never a fixed file list".

### L3. Section 4 Evidence miscites `_check_inside` (id 8)

**Where:** section 4 Evidence.

**What is wrong:** The Evidence says "`extract.py` applies `_check_inside` (`:176`) in `scan_preflights` only". Line 176 is the definition. The function is applied at `:252`, `:258`, `:278`, `:961` and `:1004`, and only `:1004` is in `scan_preflights`.

**Consequence:** The design still holds, because `measure_tree` and `measure_ready_tree` do glob without the check (S23). The miscited line misleads a reader of the window-scan containment.

**Fix (judged SOUND by the skeptic):** Reword it as: "`_check_inside` (defined at `:176`) guards `scan_preflights` (`:1004`) among others, while `measure_tree` (`:1135`) and `measure_ready_tree` (`:1209`) glob without it."

**Left-shift gate:** A checklist entry: "an Evidence claim of 'only' or 'every' cites the grep that proves it".

### L4. F1(a) asks for a new walk where `add_feed_sightings` already exists (id 9)

**Where:** section 8 F1; section 2 S16.

**What is wrong:** F1's resolved option (a) asks `write_gov_ref` to walk the first-parent commits between the tip read and the landed tip. TOOL-dPlacedRequest-13 S4's `add_feed_sightings <cache prefix>` already appends a cached ref's unseen first-parent chain oldest first, stopping at the newest commit the feed holds. F1 weighs only options (a), (b) and (c), and Alternatives rejected says nothing about reusing S4's walk. The round-4 audit's own fix named that reuse ("or calls `add_feed_sightings` for that ref").

**Consequence:** The ask filed in dPlacedRequest's BACKLOG would put a second first-parent walk inside the one writer, beside the sightings walk and `derive_feed_events` (S5). Two appenders would then encode the chain-order rule that `check_feed` (S6) grades, and they can drift, for example on the `gov-claim`-author stop. Both walks exist only in specs so far, so the cost is a second encoding, not a wrong result.

**Fix (judged SOUND by the skeptic):** Add an option (d) to F1 and prefer it. After S3 sets the cache ref `refs/gov/remote/<tail>`, `write_gov_ref`'s success exit calls `add_feed_sightings` over that ref, or the S4 walk is factored out and called from there. The tip read is already in the feed, so the walk stops there and appends the newer commits. Mail commits are authored `gov-claim`, so the author stop does not cut the chain short. File the ask as "S3 calls S4's walk", not as a new walk. If (a) is kept, add an Alternatives-rejected line saying why `add_feed_sightings` does not fit. M10 carries the same reuse for the deletion and create cases.

**Re-grade:** The finder graded this medium. The skeptic graded it low because both walks exist only in specs and nothing wrong is built. The binding grade is low.

**Left-shift gate:** A checklist entry: "an option that a prior audit's fix named is either weighed in the spec's options or rejected by name".

### L5. AC13 rebuilds the guards join by hand from a different population (id 10)

**Where:** section 2 S13; section 6 AC13.

**What is wrong:** `tools/check-spec-tokens.py` (TOOL-aBlindedTrial-8) already runs the guards join over Files touched against section 7 (`:1543-1576`). `SPEC_GUARD_LEGS_CUTOFF` is 2026-09-22 (`.memory-tree.conf:356`), so the join is armed for these specs, and section 7 already lists the `spec tokens` gate. AC13 instead takes its population from `--legs-for`. `print_legs_for` (`:651-669`) prints broad-only matches, marked ` broad`, which the join excludes (`:1580`), and it does not apply the join's directory-token tripping.

**Consequence:** AC13 can demand a leg the merge bar does not, or count a broad-only trip as covered. The reconcile then has two predicates for one rule, and the hand-built one has no red arm. The two differ only on broad-only or directory-token paths, so AC13 is stricter or redundant, not a hole.

**Fix (judged SOUND by the skeptic):** Restate S13's re-check and AC13 as the existing join. At the reconciled tip, once `tools/gate-legs.json` declares `policy fixtures`, the `spec tokens (a spec's own names resolve)` leg prints no `guards` hit `policy fixtures <- <path>` for any spec of this build. Drop the `--legs-for` population from AC13. The build's red probe: in a scratch copy, remove `policy fixtures` from unit 58's leg line and observe the join name it. S9's ledger population can keep `--legs-for`, since it is a query and not a gate.

**Re-grade:** The finder graded this medium. The skeptic graded it low because the disagreement makes AC13 stricter or redundant, not unsafe. The binding grade is low.

**Left-shift gate:** A checklist entry: "an acceptance criterion that restates a rule a gate leg already enforces cites that leg's output instead".

### L6. `memory/map/generated/symbols.json` is missing from Files touched (id 18)

**Where:** section 4 Files touched; section 4 Inventory.

**What is wrong:** The spec adds the top-level function `derive_kit_imports` to `tools/runlog/selftest.py`. That makes the generated render `memory/map/generated/symbols.json` stale, and section 4 does not list it. The unguarded `codebase-map coverage + freshness` leg (`gate-legs.json:833`, `test_codebase_map.py:291-293`) byte-compares that file against a fresh render. The skeptic found no `read_mail_chain` in any tracked tool file, so the retirement half of the finding does not hold.

**Consequence:** The leg stays red until someone runs `gen_map.py --write`, and the write set the spec declares misses the path. The build rule allows shared renders, so nothing is refused.

**Fix (judged SOUND by the skeptic):** Add "memory/map/generated/symbols.json, regenerated by `python tools/codebase-map/gen_map.py --write`" to section 4 Files touched.

**Left-shift gate:** A spec-tokens check that a spec whose Inventory adds or removes a top-level symbol in a mapped file lists `symbols.json` in Files touched.

## Refuted

Two findings were refuted and are not items: id 16 (the dPlacedRequest README write is the shared build-index render) and id 22 (both selections read one cache snapshot). Their reasons are in the appendix.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=22 confirmed=20 refuted=2 unverified=0 blocker=0 high=0 medium=13 low=7 agents=11 out-tokens=136076

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 6 AC27 (against section 1, section 2 S2 S8 S11 S12 S22 S23 S24 S26) | medium | medium | confirmed | spec-63.md:375-378 limits AC27 to units 53, 57, 60, 61 (S1, S2, Inventory) and 62 (S1, S15's sketch, S20, S22, S24, S26, AC20, AC25, §4 Evidence). Section 2 names more texts than that. S2 says 62's §5 'seven definitions' 'read as eight', and spec-62.md:267 does say 'S22 moves seven definitions', yet 62 §5 is not in AC27. S22 says 61 §4's 'derive_mail_chain and its caller' 'reads as' both callers, and that phrase is at spec-61.md:96, yet 61 §4 is not in AC27. S11 retires `--mail chain` by name, but spec-61.md:136 AC3 still requires `bash unattended.sh --mail chain <parent>` to print four rows, and :98, :114 and the Inventory also name it. Only S1 and the Inventory are listed. S12 calls the 62 text '§4's ack-chain sketch'. spec-62.md:213 shows that sketch sits under §4 '### The ack chain', while AC27 calls it 'S15's sketch'. The unit-59 regex sketch is real (spec-59.md:72, unanchored re.search). S8 replaces it without the words 'superseded', so it is a weaker gap, but it is still a contradicted text. A build can pass AC27 and leave 61 AC3 and 62 §5 unanswered. | sound | - |
| 2 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 6 AC9 against section 2 S9 and S17 | medium | medium | confirmed | Re-probed. `grep -c '"policy fixtures"' tools/gate-legs.json` printed 0 and `grep -c 'loop selftest'` printed 0. tools/policy and tools/loop do not exist. `--legs-for tools/policy/policy.py tools/policy/check_policy.py` printed `legs-for: REFUSING — no path given is tracked at HEAD` with rc=2, and the same for tools/loop/selftest.py. origin/main declares `policy fixtures`, but S13 says the leg only appears on a reconciled base. S17 (spec-63.md:113-117) says a refusal writes `GAP —` and never a leg list, and that a line names `loop selftest` only when the manifest carries that leg. Yet AC9 (:303-306) requires lines that name `policy fixtures` and `loop selftest`. Unless the pass runs on a tree that is both reconciled and carries the loop leg, AC9 contradicts the S17 rule it says it follows. | sound | - |
| 3 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 6 AC13 against section 2 S13 ("This unit's pass re-checks the step on its own tree") | medium | medium | confirmed | S13 (spec-63.md:95-96) says 'This unit's pass re-checks the step on its own tree'. AC13 (:319-323) applies only when `grep -c '"policy fixtures"' tools/gate-legs.json` prints 1 at a reconciled tip. On this tree it printed 0, and `--legs-for` over the policy paths refused with rc=2. So on an unreconciled pass tree, AC13 is vacuously green and cannot fail, and the re-check S13 claims never runs. origin/main does carry the leg (count 1), so a reconciled pass would make AC13 live. But nothing in the spec requires this unit's pass to happen on a reconciled tip, and nothing says which pass owns AC13. | sound | liveness-negative-from-another-population |
| 4 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S15 against section 6 AC15 | medium | medium | confirmed | spec-22.md S2 says derive_message_id 'takes no session and no time'. S3 says check_mail_duplicate gives rc 1 `mail — duplicate <id> · <ref>`, and its red-case table marks an equal-fields retry 'rc 1, refused'. A re-ack of the same <a> has equal fields, so it gets rc 1. S15 (spec-63.md:102-106) runs every ack through check_mail_duplicate before any commit and says 'One refusal refuses the batch with exit 2'. It separately says an already-acked id is skipped. It never says whether rc 1 counts as a skip or a refusal. AC15 (:328-332) expects `mail — already acked <a>` but states no exit for that call, and has no mixed-batch case. The ordering ambiguity is real and changes behaviour. | sound | - |
| 5 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S14, section 6 AC14 | medium | medium | confirmed | tools/runlog/selftest.py:355-356 holds the GIT_* scrub as a module-level `del os.environ[_k]`. build_arm_env (:1515-1520) copies `dict(os.environ)` and only shapes the environment passed to subprocess calls, so it is not 'beside the GIT_* scrub'. The selftest calls rl_model.build_run_model in-process (:2585). model.py read_refs calls resolve_remote at :690, and resolve_remote reads os.environ GOV_REMOTE (:652). So an unset done in build_arm_env leaves the in-process cases exposed to an ambient GOV_REMOTE. 62 S26 (spec-62.md:128-130) itself says 'unset at import beside the GIT_* scrub', which agrees with the fix. AC14's second clause only checks what build_arm_env returns. | sound | fixture-inherits-ambient-machine-state |
| 6 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S25 | low | low | confirmed | S25 (spec line 140) names one MARKER_LEAD that matches `# ` or `// ` and gives no dialect. The three sites in resolve-python.test.sh use different regex engines: awk at :213, `git grep -l` (BRE) at :218 and `grep -c` (BRE) at :224. I re-ran the probe with M='(# \|// )' against tools/runlog/model.py. `grep -c` printed 0, `grep -cE` printed 1 and awk matched 1 line. So the ERE spelling silently zeroes nblk at the BRE sites. AC25's red would catch this, so the effect is contained to an underspecified design text. | sound | - |
| 7 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S24, section 6 AC24 | low | low | confirmed | `git grep -n "parallel group" -- ':!memory/builds'` prints tools/unattended/unattended.sh:13649, which says 'Units sharing an `order` value are the parallel group and do not block'. unattended.sh is in this unit's Files touched (S7, S11, S12, S15, S16). S24 (lines 136-139) names only gen_build_index.py:202-203 and build-readme-surface.md:109. AC24's git grep is scoped to those two files, so it cannot see this line. Unit 62 F1 hands only the two template :84 lines to the owner, not unattended.sh. Comment only, so no behaviour changes. | sound | - |
| 8 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 4 Evidence | low | low | confirmed | `grep -n _check_inside tools/runlog/extract.py` prints 176 (the def), 252, 258, 278, 961 and 1004. Only 1004 is inside scan_preflights (def at :991). So 'applies `_check_inside` (`:176`) in `scan_preflights` only' is false. The measure_tree (:1131/:1135) and measure_ready_tree (:1204/:1209) globs carry no check, as claimed, so S23's design still holds. This is a miscited Evidence line. | sound | - |
| 9 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 8 F1 (and section 2 S16) | medium | low | confirmed | dPlacedRequest-13 S4 (lines 47-50) specifies add_feed_sightings, a first-parent walk oldest first that stops at a held commit or at a non-gov-claim commit. S3 (lines 43-45) has write_gov_ref call add_feed_event once. KICK-63 F1 (lines 397-406) weighs only options (a), (b) and (c), and option (a) has the ask describe a new per-commit walk in write_gov_ref. Its Alternatives-rejected section (lines 242-250) says nothing about reusing S4's walk. The round-4 audit at review line 138 named that reuse. `git grep add_feed_sightings -- tools` finds nothing, so both walks exist only in specs, and the cost is a second encoding of the chain-order rule, not a wrong result as built. I grade it low, not medium. | sound | - |
| 10 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S13, section 6 AC13 | medium | low | confirmed | check-spec-tokens.py:1543-1576 runs the guards join over Files touched against §7. Line 1580 excludes paths whose only matches are broad. print_legs_for (:651-669) prints those broad matches, marked ' broad', and it does not apply the join's symmetric directory-token tripping. AC13 (spec lines 333-337) takes its population from `--legs-for`, while S13's text already defers to 'every sibling the guards join names'. So one rule gets two predicates. SPEC_GUARD_LEGS_CUTOFF="2026-09-22" (.memory-tree.conf:356) arms the join for these specs, and §7 lists `spec tokens`. AC13 can disagree with the bar only on a broad-only or directory-token path. That makes it stricter or redundant, not a hole, so the effect is contained. | sound | - |
| 11 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S7; section 7 first New arm line | high | medium | confirmed | Re-probed. `grep -n "run-unattended-gates\\|unattended.test" tools/gate-legs.json tools/run-gates/run-gates.sh .github/workflows/remote-ci.yml` prints nothing. The only unattended legs run lib-unattended.sh, check-unattended.sh, check-pass-order.sh and check-brief-recorded.sh. tools/unattended/kit.toml:47-50 says outright that the suite FILE ships and the LEG does not, and it names unattended.test.sh among the three. The suite runs only from selftest-budgets.txt:122-129, the `unattended driver selftest shard k/8` rows that run-unattended-gates.sh picks up. So S7's claim that 'a selftest leg runs [it] when tools/unattended/unattended.sh changes' is false, and no merge bar runs the arm for AC7/11/12/15/16. The audit's own M4 text (review :229) already noted that check-unattended.sh names no unattended.test.sh case. On the floors: :17665 is marked SHADOWED and :17940 holds `FLOOR_ASSERTIONS=2776`. The §7 arm line does say 'and its shard floor', but it names neither the effective pin nor the budget row. I grade this medium, not high: the arm exists and runs under the owner's shard runs. What remains is a false coverage statement, and the defect it was meant to close stays open. | sound | - |
| 12 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S11; section 4 Files touched; section 6 AC27 | medium | medium | confirmed | Re-read. spec-61:3 is 'order 27' and spec-63:3 is 'order 34'. Spec-63 §1 (:30-31) says each item amends code its unit has built. So unit 61's `read_mail_chain` (61:34, :86, :95) and `--mail chain` (61:38, :87) already exist when 63 is built, and 'never minted' (63:83-84) cannot be true. AC11 requires `grep -c read_mail_chain unattended.sh` to print 0, which forces a deletion that §2/§4 never state. That deletion breaks or stales several unit 61 texts: AC3 at 61:136 (`--mail chain <parent>`), the loop selftest arm covering AC3 at 61:147, the VERBS `--mail chain` line at 61:98, the observability line at 61:114 and the user-docs line at 61:119. AC27 (63:375-378) asks unit 61 to answer only S1, S2 and Inventory. The finder's line numbers are off by a few lines, but the claim holds. | sound | - |
| 13 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 4 Files touched; section 5 user docs | medium | medium | confirmed | Re-read. check-unattended.sh:3152-3153 sets VERBSHIP to VERBS.template.md and VERBDOC to memory/guides/UNATTENDED-VERBS.md, and `_c10_cmp` byte-compares each such pair, so editing only the template reds `unattended kit gate`. Spec-63 §4 (:233-234) and §5 (:264-265) name only the template. Siblings name the render: spec-5:242 has 'rendered to `memory/guides/UNATTENDED-VERBS.md`', and specs 21, 24, 25 and 27 list it as 'its render'. The gate catches the miss, so the effect is contained, but the render path is missing from the write set. | sound | - |
| 14 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S13; section 7 prose under the leg line; AC13 | medium | medium | confirmed | Re-probed. `git show origin/main:tools/gate-legs.json \| grep` finds `"policy fixtures"` at :1766 and no `"loop selftest"`. This branch's manifest has neither. S13 (63:91-96) and AC13 cover only `policy fixtures`. §7's prose (63:385-387) names `loop selftest` but says S13 adds only the first, and that prose is not a backtick leg line the join reads. Spec 63 and its siblings touch tools/loop/ (63:235, 61, 53). Audit M10 (review :246) shows the join reds a spec when a declared leg's guard is tripped and the leg is absent from the spec's leg line. So when dDeclaredLoop lands `loop selftest`, the same red returns for those specs. The fix covers one instance and leaves the class open. The bar catches it at landing, so the effect is contained. | sound | - |
| 15 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S15; section 6 AC15 and AC27 | medium | medium | confirmed | Re-read. spec-5 S8 (:86-88) defines `--mail ack` as 'a post of kind ack', and S5 (:68-69) says a duplicate post exits 1 while a refusal exits 2. spec-22:43 and :89 have `check_mail_duplicate` rc 1 refusing a retry, printed as `mail — duplicate <id>`. Spec-63 S15 (:102-107) says each ack passes `check_mail_duplicate` before any commit, that one refusal refuses the batch with exit 2, and that an already-acked id is skipped as `mail — already acked <id>`. It gives the skip no exit code and names neither unit 5's exit-1 duplicate nor unit 22's message as superseded. AC15 (:328-332) never asserts the second call's exit code. AC27 lists no unit 5 or unit 22 text. Unit 42 AC4 (42:146-147) refuses a transition when `--mail ack` exits 1, so the unstated exit code matters to a caller. | sound | - |
| 16 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 4 Files touched; section 8 F1 | medium | low | refuted | Premise false on re-probe. 5c2390bb3 did touch memory/builds/dPlacedRequest/README.md (4 +-), but the change is to the front matter's `ids:` line, and that line is a generated render. tools/memory-tree/gen_build_index.py:1822 says 'Rewrite the front matter's `ids:` line from the roster, in place', and check-memory-hygiene.sh:1147 says '`--write` rewrites `ids:` from the derived roster'. HYGIENE.md:640 calls that roster a reservation range, and ids resolve against spec H1s, never against it. The build rule at README.md:49-50 allows, outside the build folder, 'an ask row in another build's BACKLOG.md and the shared renders'. So the README write is the shared build-index render: it is neither refused nor a departure. And check 9 (build-index drift) plus `--write` keep any stale roster from surviving. | unsound | - |
| 17 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S24; AC24 | low | low | confirmed | Re-ran the grep. `git grep -n -i 'parallel group'` prints carriers that S24 (:136-139) and AC24 (:362-366) do not name: tools/unattended/unattended.sh:13649 and :13692, unattended.test.sh:6398, tools/workflows/unattended-build.test.sh:1353, and the prompt string at tools/workflows/unattended-build.js:2078 and its .template.js twin ('Units sharing an order are a parallel group and do not block each other'). unattended.sh:13692 itself states that the edge refusal can still block units at one order. So the shipped workflow prompt keeps the old claim while the index and the dossier say 'candidates', and AC24's two-file pathspec cannot see the others. The effect is limited to comments and prompt prose. | sound | - |
| 18 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 4 Files touched; section 4 Inventory | low | low | confirmed | memory/map/generated/symbols.json is generated by gen_map.py and already lists 253 symbols from tools/runlog/selftest.py and 278 from tools/unattended/unattended.sh. Adding the new top-level `derive_kit_imports` therefore makes it stale. test_codebase_map.py:291-293 lists the symbols.json tier in CONDITIONAL_TIERS for test_generated_artifacts_are_fresh, and in gate-legs.json:833 the 'codebase-map coverage + freshness' leg has no guard. §4 Files touched (:229-240) does not name symbols.json. Other builds' specs record that a new function stales symbols.json (e.g. aBlindedTrial-3:77). The read_mail_chain half does not hold: the name is in no tracked tool file, so nothing is retired. The consequence is a regen step left out of the write-set estimate. The build rule allows shared renders, so nothing is refused. | sound | - |
| 19 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S15, section 6 AC15 | medium | medium | confirmed | Spec 63 S15 (:102-107) runs every id's ack through derive_message_id and check_mail_duplicate before any commit, and says 'One refusal refuses the batch with exit 2', then 'An id already acked is skipped'. Unit 5 S5 (:66-69) derives the id from slug, item, pass, kind, subject and answers. Unit 22's table (:89-90) says an equal-field repeat gets check_mail_duplicate rc 1 and is refused, and unit 5 maps a duplicate to exit 1. So a second ack of <a> derives the same id and hits the duplicate check. The spec never says whether that rc 1 is the skip or the refusal, what decides 'already acked', or what a fully or partly skipped batch exits with. AC15 checks only the stderr line and the tip, so either build passes it. The weaker half of the impact does not hold: a collision between two genuinely different messages cannot happen, because answers is a field of the id. The ambiguity in exit status and ordering is real, and its effect is contained. | sound | - |
| 20 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S17 and S13, section 6 AC17, section 7 | medium | medium | confirmed | `grep -c '"policy fixtures"\\|"loop selftest"' tools/gate-legs.json` prints 0, so both legs are absent at this base. S17 (:115-117) applies its 'names the leg only when gate-legs.json carries it, else NOT RUN —' rule to `loop selftest` alone, and AC17 (:339-340) tests only that leg. Yet S9 and AC9 (:69-73, :304) require ledger lines for units 58, 59 and 60 naming `policy fixtures`, a leg that does not exist yet. That is a ledger line reading as clean for a leg that never ran. §7 (:385-387) has S13 add only `policy fixtures` at reconcile; no spec adds `loop selftest` to a §7 leg line (checked by grep). That half matters less, since a declared leg runs on its guard whatever the §7 line says. The asymmetry is real, and it misleads the ledger record. | sound | - |
| 21 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 8 F1 (resolved (a)), section 2 S16, section 5 security/risks | medium | medium | confirmed | I re-read spec-63 (blob 667d570 matches the pin). Section 8 F1(a), at :397-406, has write_gov_ref's success exit append 'one line per first-parent commit between them, oldest first, the tip last', and gives no deletion or create case. TOOL-dPlacedRequest-11 S1 says 'An empty <src> pushes the ref's deletion' and allows the expected sha to be empty. TOOL-dPlacedRequest-13 S3 has a separate deletion branch at that same exit ('clears it when the write was a deletion, then calls add_feed_event'), and KICK-dKeptSession-23 relies on that branch for the mailbox prune ('whose deletion branch TOOL-dPlacedRequest-13 S3 already appends'). An ask built literally as 'the commits between tip and landed tip' has no landed tip on a deletion, so it would drop that event. Section 5's risks line (:259-260) talks only about callers of unit 5's code and never prices the change to the exit that every governance-ref writer shares. F1 itself says (a) 'covers every multi-commit governance-ref write in the one writer'. The effect stays inside the feed and its census, so I grade it medium. | sound | - |
| 22 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-63.md:section 2 S11 and S6, section 4 'The two selections of the one reader' | medium | - | refuted | The premise does not hold on re-probe. In S11's table (:196-199), the dependent's `rows` (soft or strict) and the parent's `cache sent` rows come from the same cache, refs/gov/remote/mail/*. The rows addressed to the dependent are therefore always a subset of the parent's cached sent rows. If the cache is empty or was never populated, `rows` is empty too and write_consumed_acks has nothing to ack. If it is stale, both selections read the same snapshot, so derive_mail_chain cannot place a row over a chain that lacks it. The class KICK-dKeptSession-5 red-tests, a failed fetch read as an empty mailbox, lives in the soft and strict fetch, which S11 leaves unchanged. Also, S11 supersedes only 61 S1's names `read_mail_chain` and `--mail chain`, so the clause 'reads the cache the dependent's --mail read has just fetched' is not plainly gone. The fix is also unsound: a parent that never sent mail legitimately has no cached ref, and making `cache sent` exit non-zero there would refuse the valid empty case. | unsound | - |
