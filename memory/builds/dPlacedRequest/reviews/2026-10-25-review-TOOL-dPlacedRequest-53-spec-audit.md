**Serves:** spec-audit TOOL-dPlacedRequest-53@rev-1 TOOL-dPlacedRequest-54@rev-1 TOOL-dPlacedRequest-55@rev-1 TOOL-dPlacedRequest-56@rev-2

# Tier-2 spec audit — build dPlacedRequest, the round-5 promotion specs TOOL-dPlacedRequest-53 to -56, ROUND 1

*This is an adversarial pre-code pass over the four specs that the round-5 spec audit promoted, dated 2026-10-25. Five lenses found defects, and five skeptic batches tried to refute each finding. This report is synthesised only from the findings that survived. Finders were gov-spec-reviewer, skeptic batches gov-skeptic, and synthesis gov-synthesizer.*

Reviewed: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md@5ebe9d87afade758ec52098b1da5f9e2bdefe14b, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md@4cd61d943ecadf6e2f3a6cad5ba9ff25ff0eab14, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-55.md@38d1cfafda39a9a2e6d1d4ef14b4e9ee3f764223, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md@6cbbcc168a70f800d7a1a8c3c4d9ed35b8763509

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker stands. Two highs do, and each must be fixed in the spec before its unit is built.
H1: 54 pins the oracle's base to the literal `c63aabbb`, so in the build run the oracle walks this build's own spec-run landing and AC1 is red on a correct build.
H2: 56's restated per-attempt race drops the reset of the stub's handshake files, so every retry attempt runs an unplaced race.
By item, the tally is 17 items: 0 blocker, 2 high, 5 medium and 10 low.
By raw confirmed finding, it is 23: 0 blocker, 2 high, 8 medium and 13 low.
The pinned-base defect was reported by three findings at two binding grades. It sits in H1 (id 1) and M1 (ids 8, 21), which name each other, and no finding is counted twice.

## Review shape

The review ran at intensity full: raw 23, confirmed 23, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |

**Run integrity.**
- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified. 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 19 were judged sound and 4 were judged UNSOUND (ids 1, 5, 7, 14). 0 had no fix proposed, and 0 were NOT JUDGED.
- Severity on confirmed findings: 0 were UNGRADED and 3 were RE-GRADED by the skeptic (ids 3, 4, 5).
- Unverified findings: 0 were answered UNCERTAIN, and 0 had no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

Because every count above is zero where it should be, this run is complete.

- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and synthesis gov-synthesizer.
- Intent: 52 spec documents were supplied as `specs`, as sibling context.
- Checklist: 43 items, each assigned to exactly one of 5 lenses: coherence 9, grounding 9, reuse 9, blast-radius 8, failure-envelope 8.
- By design: 1 invariant came from the checklist's by-design block.
- Move check: no checked subject moved.

Every fix below was judged by a skeptic. Where a skeptic rejected the finder's fix, the skeptic's corrected fix is the one written here.

## High

### H1 — 54 pins the oracle's base to the spec run's base, `c63aabbb` (id 1)

- **Where:** `TOOL-dPlacedRequest-54` §2 S1 and S3 (:48-50), §6 AC1 (:142-144); restated into 34 AC59 and 44 AC1.
- **What is wrong:** the own-merge test is `merge-base --is-ancestor "$t" <base>`, and S3 and AC1 fix the base to `c63aabbb`, the spec run's base (RUN.md:39). The spec run closes by landing `merge: dPlacedRequest — land onto …` (the subject push-main.sh:880 writes), after `c63aabbb`. origin/main has already moved past it (60d60e694).
- **Consequence:** in the build run, before `--prepare`, fact 1 finds the spec run's landing. Its subject matches and it is not an ancestor of `c63aabbb`, so the oracle walks the spec run's commits and exits 0. AC1 expects `no prepared merge on HEAD` with exit 2, so it is red on a correct build. S2's fifth-row guard (an earlier own landing) never applies to the real tree.
- **Fix (finder's fix judged UNSOUND; skeptic's corrected fix):** make the base argument the running build run's pinned BASE (its RUN.md `base:`) in S1, S3, 34 AC59 and 44 AC1, never a literal sha. Restate AC1 to that base, with the expected refusal and the scratch copy's header derived at observation. Add no sixth fixture row: S2's fifth row (an earlier own landing under a later base, exit 2) already stages the case.
- **Gate:** a bug-class checklist entry: "a criterion that runs in a later run never pins a sha observed in this run; it reads the observing run's own base". Same defect as M1.

### H2 — 56's per-attempt race never clears the stub's handshake files (id 20)

- **Where:** `TOOL-dPlacedRequest-56` §2 S3 and S4 (:62-68), §4 "The placed race, per attempt (S3, S4)" (:155-164).
- **What is wrong:** 52 §4 (:236-239) clears `$h/once $h/held $h/release` after each attempt. 56's restated sketch drops that clear, and S3 lists only the clone, the bare remote and the stored files as fresh per attempt. `$h` is not inside the unit-19 clone, so a fresh clone does not reset it.
- **Consequence:** the 48 stub holds only when `mkdir "$h/once"` succeeds. On attempt 2 the stale `$h/once` means A never holds, and the stale `$h/held` lets the arm's wait return at once, so B runs against an A outside its window. AC3 forces that retry path by delaying B 11 s on attempt 1, so the criterion judges an unplaced race and can pass without checking anything.
- **Fix (judged sound):** in 56 §4, after "wait for A", add "clear `$h/once $h/held $h/release` (or use a fresh `$h`)", as 52 §4 has it. In S3, name `$h` among the per-attempt fresh state. Extend AC3 so attempt 2 shows `$h/held` created after attempt 2's A starts (a held-file mtime later than attempt 2's start stamp). Run a staged break that does not clear `$h` and show AC3 going red.
- **Gate:** the round-4 checklist entry "a retry loop in a test arm names every piece of state an attempt writes, and resets or recreates each before the next attempt", plus a check that a spec restating a sibling's sketch diffs against it.

## Medium

### M1 — the pinned base makes the earlier-own-landing protection inert (ids 8, 21)

Same defect as H1, reported at binding medium. I would grade it high with H1, since it is the identical consequence, but the binding grade stands.

- **Where:** `TOOL-dPlacedRequest-54` §2 S1/S3, §4 "The oracle's head" prose (:83, :89), §6 AC1.
- **What is wrong:** §4 claims the ancestor test rejects an earlier landing of this slug. With the base pinned to `c63aabbb`, the spec run's own landing is never an ancestor of the base. AC1 is green today only because the newest first-parent merge is `c63aabbb` itself (t == base).
- **Consequence:** in the build run, before `--prepare`, the oracle walks the spec run's commits, which touch no kit file, and exits 0 ("no bump"): the shape-5 failure the unit says it closes. AC1 goes red against a correct oracle. The read after `--prepare` in 34 AC59 still works.
- **Fix (judged sound):** pass the run's own base (its recorded baseline), never `c63aabbb`, in S3, AC1, 34 AC59 and 44 AC1. Rewrite AC1 to run in the building run's worktree with that base. The build runs a probe: a fixture with an own landing merge on main and a run branch cut after it, read with `c63aabbb` and with the run base, expecting exit 2 only with the run base. Id 21's sound fix also adds that case as an AC2 fixture row. H1's skeptic holds S2's fifth row already stages it, so add the row only if the fifth row does not read an own earlier landing with an older base.
- **Gate:** the H1 checklist entry.

### M2 — 54 makes the base a required argument but strands the oracle's other readers (ids 2, 9, 16)

- **Where:** `TOOL-dPlacedRequest-54` §2 S1-S3 (:35-50, :76-79), §4 Files touched (:113-118); the readers 44 AC2/AC3 (44.md:130-138), 43 AC24, 52 AC29 (from 55 S2), 55 AC1/AC2 (55.md:113-119), 56 AC6/AC10 (56.md:245-259), and 56 S10's restatements of 44 AC3 and 43 AC24.
- **What is wrong:** the oracle now starts `base=$1` and exits 2 with `version oracle: base does not resolve` when the base is missing. 54 migrates only 52's fixtures (S14, AC11-AC14, AC17), 44 AC1 and 34 AC59. The other readers run the oracle with no base, and 54 inventories none of them.
- **Consequence:** run as written, each criterion hits the base refusal before what it checks. 44 AC2 (expects `+KIT_UNATTENDED_VERSION=1.111`), 43 AC24 (exit 0) and 55 AC1 (exit 1) are red on a correct build. 55 AC2, 52 AC29 and 56 AC6 expect exit 2, so a reader checking only the status passes them on the wrong refusal. A builder may instead default the base, which weakens the own-merge test.
- **Fix (judged sound):** add to 54 §4 Files touched an inventory of every criterion that runs the oracle (`grep -n 'oracle' memory/builds/dPlacedRequest/spec/*.md`): 43 AC24, 44 AC1-AC3, 49 S3, 52 AC11-AC14, AC17 and AC29, 55 AC1/AC2, 56 AC6/AC10. Restate each to pass a named base: the fixture's base commit in a fixture, the run's base at the close. In 55 and 56, state the base argument in each oracle-running criterion. Add a criterion that reads those bullets and finds the base argument in every run.
- **Gate:** the existing class C36 retirement-inventory-misses-readers-by-value: an interface change carries a grep-derived inventory of its callers, checked by a criterion.

### M3 — 44 S1 keeps a scope with no own-merge test (id 10)

- **Where:** `TOOL-dPlacedRequest-54` §2 S1 (:40-42), §4 Files touched (:116-117); 52 S17 (52.md:116); 56 S10 (56.md:87-92).
- **What is wrong:** 52 S17 restates 44 S1, §4 and AC1 to the fact-1 derivation. 54 adds the own-merge test to 44 §4 and AC1 only, and 56 S10 restates 44 S2, §5, Evidence, Alternatives and AC3, not S1.
- **Consequence:** after 52, 54 and 56 land, 44 S1 says the oracle walks the nearest first-parent merge with no ownership test, while 44 §4 refuses foreign merges. A change working from S1 rebuilds the H2 defect of round 4.
- **Fix (judged sound):** add 44 S1 to 54's Files touched and to S1's restatement list. Add a criterion that greps 44's S1 paragraph (by the 52 S15 awk form) for `is-ancestor` and the lander's subject.
- **Gate:** the existing class amendment-leaves-its-other-half-standing: an amendment lists every section of the target that restates the amended rule, found by grep.

### M4 — 56 S22 cites a `read_claims` seam that never reads `renews` (id 14)

- **Where:** `TOOL-dPlacedRequest-56` §2 S22 (:123-124), §4 Files touched, §5 security (:214), §10 (:322-324); `tools/unattended/unattended.sh:2167-2171`; 52 S26 (52.md:149-151).
- **What is wrong:** S22 says the age walk keeps the first occurrence "as `read_claims` keeps the first occurrence of every key". At :2167-2171 that rule applies only to keys in `want` (`slug node host session keepalive status lease-utc beat-utc`), split on `": "`. `renews` and `seen-utc` are not read there. 52 S26 gives the walk its own line rule ("a line beginning `renews:`, its value trimmed"), which differs from the `": "` split.
- **Consequence:** a second hand-written reader of the same commit-body grammar stands, tied to the first by restated prose only, and the next edit to either drifts unchecked. The citation misleads. The strict reader never reads `renews`, so the two cannot disagree on a renews value today.
- **Fix (finder's fix judged UNSOUND; skeptic's corrected fix):** make the key/value split one shared awk function that both `read_claims` and the age walk call. Keep `want` and its `ok` completeness check unchanged, and give the walk its own key list (`renews`, `seen-utc`). Where an empty value after `key:` must parse, handle it inside that function for the walk's keys only. In S22, §10 and §5, state that `read_claims` does not read `renews` today. Add an AC that feeds one duplicate-key, bare-`renews:` body through the shared function and checks it against the walk's result; its red is a scratch copy whose walk keeps its own line reader.
- **Gate:** the existing class C43 two-readers-of-one-config-one-re-derived: a spec citing a seam as the rule it copies quotes the seam's key list, checked by grep.

### M5 — 34's 346-byte margin may be spent with no unit allowed to cut it (id 17)

- **Where:** `TOOL-dPlacedRequest-56` §2 S11 (:93-96), §3 "No edit to TOOL-dPlacedRequest-34" (:135), §6 AC11 (:260-263).
- **What is wrong:** 34 is 47782 bytes, 346 under its 48128 ceiling. Pending §9 lines from 49, 52 and 54 run roughly 64-170 bytes each, offset only by 54 cutting AC59 (264 bytes) to one line, saving roughly 100-150. S11 measures the margin but says nothing about an overrun, and §3 forbids editing 34.
- **Consequence:** if `wc -c` exceeds 48128, AC11 reds and no unit in the round may cut 34, so the close blocks with nothing in scope to clear it. The gated hard ceiling is 49152, so the gate itself would not fail.
- **Fix (judged sound):** have S11 say what happens on overrun: allow a size-only cut of 34 (prose tightening, nothing dropped, as 34's rev-7 did) within S11, or move the ceiling decision to a follow-up unit. Drop or qualify the §3 non-goal. Estimate the post-edit size in §4 Evidence now (47782 plus the pending lines).
- **Gate:** a bug-class checklist entry: "a criterion that measures a budget states the action on overrun, and a non-goal never forbids that action".

## Low

### L1 — 52's pass observes AC1, AC6 and AC9 before 53 repairs them (id 3)

Re-graded low by the skeptic: 52's hands-off edge already points the builder to 53.

- **Where:** `TOOL-dPlacedRequest-53` §1 Goal, §3 Edges; 52's hands-off edge (52.md:185).
- **What is wrong:** 52 is at build order 27 and 53 at 28. 52's AC1, AC6 and AC9 still read `flat … | grep -c … at least 2`, which prints at most 1. Neither 53 nor 52's edge says 52's pass defers them, though 52 S1 (52.md:55-58) shows the build states such order gaps in text.
- **Consequence:** 52 cannot be verified done at its own pass. The builder stalls, or rewrites the criteria ad hoc, colliding with 53's in-place rewrite and rev bump.
- **Fix (judged sound):** add to 53 S1 and to 52's hands-off edge one sentence: 52's pass at order 27 observes AC1, AC6 and AC9 by `grep -o … | wc -l`, or leaves them to 53's pass and the close; either way they are read at 53's pass. Add a criterion that 52's §9 or the pass record names the deferral.
- **Gate:** a bug-class checklist entry: "a unit that repairs a lower-order unit's criteria states, in both units, at which pass the repaired criteria are read".

### L2 — 53 AC1 cannot fail: it tests grep, not 52 (ids 4, 11)

Id 4 was re-graded low by the skeptic: 53 AC2 still checks the rewrite.

- **Where:** `TOOL-dPlacedRequest-53` §6 AC1 (:105-108).
- **What is wrong:** AC1 builds a scratch file with S25 in two paragraphs and checks `grep -o | wc -l` prints 2 and `grep -c` prints 1. It never reads 52, so it is green on today's unbuilt tree, and its `Red when:` ("the rewritten form still counts lines") cannot fire.
- **Consequence:** false coverage. S1 is observed only by AC2's text check, and nothing runs 52's rewritten counts over 48 and 43.
- **Fix (judged sound):** restate AC1 to run 52's rewritten AC1, AC6 and AC9 commands, extracted from 52's bullets, over the built 48 and 43, each printing at least 2. Keep the scratch two-paragraph file as the staged red: the same pipeline with `grep -c` prints 1. (Id 11's sound alternative: drop AC1.)
- **Gate:** a bug-class checklist entry: "every criterion reads the unit's own output; a criterion green on the unbuilt tree is rejected", checked by running each AC before the pass.

### L3 — 56 AC10 and AC19 count phrases that 44 F1's rejected options keep (id 5)

Re-graded low by the skeptic: the cure is rewording one fork's option text.

- **Where:** `TOOL-dPlacedRequest-56` §2 S10 and S19 (:114-116), §6 AC10 and AC19; 44 §8 F1 (44.md:151-152) and its Alternatives bullet.
- **What is wrong:** AC10 requires `merge-base (form|origin)` 0 times in flat 44 (today 7), and AC19 requires `merge-base form elsewhere` 0 times (today 1, in F1's option (a)). S19 only says F1 is "amended in place to (a')". TEMPLATE-SPEC:556 keeps a fork's options under the F-item.
- **Consequence:** built as S19 reads, AC10 and AC19 stay red on a correct build, or the builder deletes the record of rejected options.
- **Fix (finder's fix judged UNSOUND; skeptic's corrected fix):** keep AC10 and AC19 over the whole of flat 44. In 56 S19, say that 44 F1's options (a) and (b) are reworded in place to name the rejected forms without the phrases AC10 and AC19 count (for example "the origin/main tracking-ref range"). Keep them as options under F1, with the (a') resolution.
- **Gate:** a bug-class checklist entry: "a zero-count criterion over a whole spec is run against the spec's kept history (forks, Alternatives) before it is written".

### L4 — the oracle is stated twice and no criterion compares the copies (id 6)

- **Where:** `TOOL-dPlacedRequest-54` §2 S1 and S3 (:40-42, :50), §6 AC3 (:152-154); 55 S1 (55.md:36-37); 56 S6 (56.md:74).
- **What is wrong:** 54 S1, 55 S1 and 56 S6 each write into both 44 §4 and 52's §4 sketch. Every criterion runs 44's copy; none reads 52's sketch or diffs the two. 54 AC3 reads only 34 AC59, so S3's "44 AC1 names the base argument" is unobserved.
- **Consequence:** a drift between the copies lands silently, and a change reading 52's sketch (the rationale's home) meets a different contract. The close runs 44's copy, so the effect stays in spec text.
- **Fix (judged sound):** make 52's §4 sketch a pointer to 44 §4, or add one criterion per unit that extracts both blocks and diffs them after squeezing. Add to 54 AC3 a read of 44 AC1 for the base argument.
- **Gate:** the existing class C6 two-answers-to-one-question.

### L5 — 53 AC3's sweep hits 53's own prose, and 53's evidence cites moved lines of 52 (ids 7, 12, 19)

- **Where:** `TOOL-dPlacedRequest-53` §6 AC3, §1 (:24), §4 Evidence third bullet (:74-77).
- **What is wrong:** AC3's sweep prints 53.md:24, 53's own §1 prose pairing `flat … | grep -c` with "at least 2". The Evidence cites 52:287, 52:309 and 52:300; the criteria now sit at 52:291 (AC1), 52:305-306 (AC6) and 52:313 (AC9). The finder's claim that `-A1` misses a count two lines below did not reproduce.
- **Consequence:** read literally ("no hit pairs it with flat"), AC3 is red forever on its own spec. The stale cites send a re-reader to the wrong lines, and units 53-56 all edit 52, so they will move further. This repeats the moved-line-citation class 56 S17/S18 remove elsewhere.
- **Fix (id 7's finder fix judged UNSOUND; skeptic's corrected fix; ids 12 and 19 judged sound):** match the command shape, not nearby words: squeeze each `- **AC` bullet, then grep with `-E "flat [^|]*\| grep -c [^ ]+\`? (runs, it )?prints at least [2-9]"`, or exclude 53's own file from the sweep. Cite 52's criteria by label (AC1, AC6, AC9), never by line number.
- **Gate:** a bug-class checklist entry: "evidence cites a sibling spec by label, never by line number", checkable by grepping specs for `\b[0-9]{2}:[0-9]+` cites into sibling specs.

### L6 — 56's evidence misstates 47's moved lines (id 13)

- **Where:** `TOOL-dPlacedRequest-56` §4 Evidence, fourth bullet (:185).
- **What is wrong:** it says 47 holds AC1 to AC3 at :114, :118 and :121; they are at :115, :119 and :122. S1 at :34 is right.
- **Consequence:** cosmetic. S17 removes the line cites from 50 anyway.
- **Fix (judged sound):** correct the numbers, or state the drift by label only.
- **Gate:** the L5 checklist entry.

### L7 — the oracle hard-codes a second copy of the lander's merge subject (id 15)

- **Where:** `TOOL-dPlacedRequest-54` §2 S1 (:37-38), §4 "The oracle's head" (:81-82), §5 risks (:134-135); `tools/push-main.sh:880`.
- **What is wrong:** the oracle matches the literal `"merge: dPlacedRequest — land onto "*`, while the lander writes `msg="merge: $SLUG — land onto $remote/$def at ${R:0:8}"`. Nothing ties the two; §5 admits the coupling but does not guard it.
- **Consequence:** rewording :880 makes the oracle refuse every real prepared merge with exit 2, with no gate pointing at the copy. The refusal is loud.
- **Fix (judged sound):** derive the prefix from the text the lander uses, for example a `land_subject_prefix` line or function in push-main.sh that both read. Failing that, add an AC that greps tools/push-main.sh for the exact `merge: $SLUG — land onto ` form the oracle matches, red on a scratch copy whose :880 wording differs.
- **Gate:** the existing class C43 two-readers-of-one-config-one-re-derived.

### L8 — 56 AC5 needs a phrase and a path on one physical line (id 18)

- **Where:** `TOOL-dPlacedRequest-56` §6 AC5 (:242-244, the rev-2 fold), §2 S5.
- **What is wrong:** AC5 greps `in sequence` line by line, then requires `tools/unattended/unattended.test.sh` on the same line. S5's sentence does not fit one house-wrapped line, and 48's existing sequence sentence already wraps as "run in" / "sequence.".
- **Consequence:** a correctly written and wrapped 48 or 50 makes AC5 print nothing, or the builder contorts the wrap to satisfy a grep.
- **Fix (judged sound):** have AC5 read 48's and 50's Files touched section squeezed, for example `sed -n '/### Files touched/,/### Alternatives/p' <spec> | tr -s '[:space:]' ' ' | grep -o 'unattended.test.sh[^.]*in sequence'`. Or have S5 require the path, the other unit's id and "in sequence" on one bullet line, and say so.
- **Gate:** a bug-class checklist entry: "a criterion matching two terms in prose squeezes the section first; it never relies on line wrap".

### L9 — 56 S4 does not say what the health-log offset is when the log is absent (id 22)

- **Where:** `TOOL-dPlacedRequest-56` §2 S4 (:65-68), §4 sketch line "m = lines in the health log"; 36 (36.md:36-37).
- **What is wrong:** every attempt is a fresh clone, and node-lock health events go to that clone's common dir, so at hold time the log normally does not exist. The spec never says what m is then.
- **Consequence:** `m=$(wc -l < "$log")` errors on the normal path (m empty, or the arm aborts under `set -e`), or a builder reads a correct race as a failure.
- **Fix (judged sound):** state that a missing log at hold time counts as m=0, for example `m=$( [ -f "$log" ] && wc -l < "$log" || echo 0 )`. Or drop the offset and note that S3's fresh common dir makes every node-lock-broken line this attempt's own.
- **Gate:** a bug-class checklist entry: "a sketch that reads a file names its value when the file is absent".

### L10 — the own-merge test reads a `merge-base` error as "not an ancestor" (id 23)

- **Where:** `TOOL-dPlacedRequest-54` §4 "The oracle's head" (:83).
- **What is wrong:** `if [ -z "$t" ] || [ "$own" = 0 ] || git merge-base --is-ancestor "$t" "$base"; then …exit 2` treats status 128 like status 1, so an error makes the merge this build's own. This is the swallowed-delegate class 55 closes for the walk.
- **Consequence:** on a corrupt or missing object, a foreign merge with a matching subject is walked instead of refused. The path is narrow: base and t were just resolved, and the subject must match.
- **Fix (judged sound):** capture the status: `git merge-base --is-ancestor "$t" "$base"; a=$?`. Treat 0 as foreign, 1 as own, anything else as `version oracle: the ancestor test failed` with exit 2. Stage it in AC2 with a PATH-stub git whose `merge-base` exits 128, the stub shape of 55 AC2.
- **Gate:** the round-4 checklist entry "a check whose verdict is `producer | grep` checks the producer's status", widened to any delegate whose non-zero status carries two meanings.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=23 confirmed=23 refuted=0 unverified=0 blocker=0 high=2 medium=8 low=13 agents=11 out-tokens=135247

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 2 S1 and S3, section 6 AC1 | high | high | confirmed | 54.md:48-50 (S3) and :142-144 (AC1) pin the base to the literal `c63aabbb`, and RUN.md:39 shows that is the spec run's base. `git log --first-parent -3 origin/main` printed 60d60e694 (the dOrderedCharter landing onto c63aabbb) above c63aabbb4, so main has already moved past it. README:35-37 makes this a spec run that closes on the prepared merge through the lander, and 3fdeb642d is the precedent of a spec run landing as `merge: <slug> — land onto …`. The build run will fork after this build's own spec-run landing. Before --prepare, fact 1 then finds that merge. Its subject matches, and `merge-base --is-ancestor $t c63aabbb` fails, so the §4 head walks the spec run's commits and exits 0. AC1 expects `no prepared merge on HEAD` with exit 2, and a header naming c63aabbb. AC1 is therefore red on a correct build. With a stale base, the fifth-row guard in S2 also cannot apply to the real tree. | unsound | - |
| 2 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 2 S1 (the new mandatory base argument) and section 4 Files touched | medium | medium | confirmed | 54 S1 (54.md:35-39) makes the base the oracle's one argument, and a missing base exits 2 with `base does not resolve`. 54 §4 Files touched (:113-118) lists only 52 (S12, S17, §4, AC11-14, AC17, F1), 44 §4 and AC1, and 34 AC59. Several readers still run the oracle with no base. 44 AC2 and AC3 (44.md:130-138) run it on the fixture with none. So do 55 AC1 and AC2 (55.md:113-118, 'the oracle as 44 §4 states it'), and 56 AC6 and AC10 (56.md:245-259). 56 S10 also restates 44 AC3 and 43 AC24 without naming one. Run as written after 54's pass, each prints the base refusal instead of its expected line, and nothing in 54 inventories them. | sound | retirement-inventory-misses-readers-by-value |
| 3 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md:section 1 Goal / section 3 Edges (ordering against unit 52's pass) | medium | low | confirmed | README build order puts 52 at 27 and 53 at 28. 52.md AC1, AC6 and AC9 still read `flat … \| grep -c … at least 2`. My scratch probe of flat over a two-paragraph file printed `1` for grep -c, so these criteria are red at 52's own pass on a correct build. Neither 53 S1, 53's Edges nor 52's hands-off edge (52.md:185) says that 52's pass defers these three criteria to 53's pass. 52 S1 (52.md:55-58) shows the build does state such order gaps in text. The effect is contained: 52's hands-off edge naming AC1, AC6 and AC9 for 53 points the builder there. That makes this a pass-sequencing ambiguity, not a shipped wrong result. | sound | - |
| 4 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md:section 6 AC1 | medium | low | confirmed | Re-ran in my scratch dir: flat over a file with S25 in two paragraphs before `## 9.` gave `grep -o S25 \| wc -l` = 2 and `grep -c S25` = 1. That is 53 AC1's whole pass condition, and it is met today with 53 unbuilt. AC1 never reads 52, so its `Red when:` cannot fire. Consequence is limited: 53 AC2 does check that 52's AC1, AC6 and AC9 bullets use `grep -o` and carry no `grep -c`, and 52's rewritten criteria are themselves observed later. The rewrite is still checked, so AC1 is a vacuous criterion rather than an uncovered scope item. | sound | - |
| 5 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md:section 2 S10/S19 against section 6 AC10 and AC19 | medium | low | confirmed | Re-probed: flat 44 gives `grep -oE 'merge-base (form\|origin)' \| wc -l` = 7 and `grep -o 'merge-base form elsewhere' \| wc -l` = 1. The latter hit is 44.md:151-152, F1's option text '(a) … the merge-base form elsewhere; (b) the merge-base form everywhere'. 56 S19 (56.md:114-116) only says F1 is 'amended in place to (a')' with a quoted resolution, and never says the option text is reworded. S10 covers §5 risks, Evidence and the Alternatives bullet, not §8's options. Built as S19 literally reads, with TEMPLATE-SPEC:556 keeping options under the F-item, AC10 and AC19 stay red. The cure is to reword one fork's option text, so the effect is cosmetic or record wording only. | unsound | - |
| 6 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 2 S1 and S3 (with 55 S1 and 56 S6): the oracle stated in two places | low | low | confirmed | Re-read: 54.md:40-42, 55.md:36-37 and 56.md:74 each write their change into both 44 §4 and 52's §4 sketch. 54 AC1-AC4 and 55 AC1-AC2 run the oracle 'as 44 §4 states it' and never read 52's sketch. 54 AC3 (54.md:152-154) reads only 34's AC59 bullet, and no criterion reads 44 AC1 for the base argument that S3 (54.md:50) requires. So a drift between the two copies would go unobserved. The effect is limited to spec text, because the close runs 44's copy. | sound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md:section 6 AC3 and section 4 Evidence | low | low | confirmed | I re-ran the finder's sweep. It printed 52:291, 52:305, 52:313 and 53.md:24, so 53's own §1 prose is a hit. 53 §4 Evidence (53.md:74-77) cites 52:287, 52:309 and 52:300, but the criteria now sit at 291, 305-306 and 313. The '-A1 misses a count two lines below' part did not reproduce: all three of 52's real hits are caught. The self-hit and the stale cites hold. | unsound | - |
| 8 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 2 S1/S3, section 4 'The oracle's head' prose, section 6 AC1 | medium | medium | confirmed | These commands returned no output: `git log --all --grep='^merge: dPlacedRequest'` and `git rev-list --first-parent --min-parents=2 --max-count=1 HEAD`. The second printed c63aabbb, which is the base itself. So 54 AC1 is green today only because t == base. README:35-41 says the spec run defers every unit and closes through `--prepare`, and the build run builds every carried unit, 54 included. In that run the nearest first-parent merge before `--prepare` is the spec run's own landing, `merge: dPlacedRequest — land onto ...`. It passes the subject test, and `is-ancestor <t> c63aabbb` fails. The oracle therefore walks the spec run's commits, which touch no kit file, and exits 0. AC1 then goes red, and the earlier-own-landing protection is inert while the base stays pinned to c63aabbb. | sound | - |
| 9 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-55.md:section 6 AC1, AC2 (also 56 section 6 AC6, AC10) | medium | medium | confirmed | 54.md:77-79 makes the oracle read `base=$1` and exit 2 with `base does not resolve` when the base is missing. 54 S2 (54.md:46-47) migrates only 52's S14, AC11, AC13 and AC17 fixtures, and 54 Files touched for 44 (54.md:116-117) lists §4 and AC1 only. 55 AC1 and AC2 (55.md:113-119) run 'the oracle as 44 §4 states it' on 55's own fixture without naming a base. 56 AC6 and AC10 and 44 AC2 (44.md:130-134) also name none. Built as written, those criteria either exit on the base check or leave each builder to choose a base ad hoc. The 56 AC6 case is arguably covered because 52's fixtures pass their base. The 55 and 44 AC2 cases are not. | sound | a-spelling-change-strands-its-readers |
| 10 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 2 S1, section 4 Files touched | medium | medium | confirmed | 52.md:116 (S17) restates '44 S1, §4 and AC1' to the fact-1 derivation. 54 S1 (54.md:40-42) and Files touched (54.md:116-117) give 44 only §4 and AC1. 56 S10 (56.md:87-92) restates 44's S2, §5, §4 Evidence, Alternatives and AC3, but not S1. A grep for '44 S1' across the spec set finds only 52:116. 54 restates 52 S17's own text, but no unit lists 44 S1 as a file it touches. So after 52's pass, 44 S1 keeps a scope with no own-merge test, which contradicts 44 §4. | sound | amendment-leaves-its-other-half-standing |
| 11 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md:section 6 AC1 | low | low | confirmed | 53:105-108 AC1 has the probe build a scratch file with S25 in two paragraphs, then checks that `grep -o \| wc -l` prints 2 and `grep -c` prints 1. It never reads unit 52, so it passes before 52 is rewritten. Its 'Red when: the rewritten form still counts lines' cannot happen, because the scratch commands are fixed by AC1 itself. Only AC2 (53:109-111) actually observes S1. The effect is contained: one criterion adds false coverage. | sound | - |
| 12 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md:section 4 Evidence, third bullet | low | low | confirmed | 53:74-76 cites 52:287, 52:309 and 52:300. Re-running `grep -n "grep -c" ...-52.md \| grep "at least"` printed 291 and 313. `grep -n -A1 "grep -c '43 S30'"` printed 305, with 'at least 2' on 306. The line cites are stale, and AC3 does not depend on them. | sound | - |
| 13 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md:section 4 Evidence, fourth bullet | low | low | confirmed | 56:185 says 47 holds AC1 to AC3 at :114, :118 and :121. `grep -n '^- \*\*S1\*\*\\|^- \*\*AC[123]\*\*' ...-47.md` printed 34, 115, 119 and 122. S1 at :34 is right, but each AC cite is off by one. The error is cosmetic. | sound | - |
| 14 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md:section 2 S22, section 4 Files touched, section 10 | medium | medium | confirmed | At tools/unattended/unattended.sh:2167-2171, `want` is `slug node host session keepalive status lease-utc beat-utc`. The first-occurrence rule applies only to `(k in want)`, and lines are split on index($0, ": "). `grep -n 'renews\\|seen-utc'` over the file printed nothing. So 56 S22 (:123-124) and §10 (:322-324) cite a seam that never reads `renews`. Their wording 'first occurrence of every key' is wrong, and so is §5 security's 'as the strict reader reads it' (:214). 52 S26 (:149-151) gives the walk its own line rule ('a line beginning `renews:`, its value trimmed'), which differs from the ': '-split rule. That leaves a second hand-written reader of the same commit-body grammar, tied to the first by restated prose only. The stated impact overreaches: the strict reader never reads `renews`, so the two cannot disagree on a renews value today. What remains is a contained duplication, plus a citation that misleads. | unsound | two-readers-of-one-config-one-re-derived |
| 15 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 2 S1, section 4 'The oracle's head' | low | low | confirmed | The 54 §4 sketch (:81-82) hard-codes `"merge: dPlacedRequest — land onto "*`, and S1 (:37-38) names it as the `msg` that push-main.sh:880 writes. :880 reads `msg="merge: $SLUG — land onto $remote/$def at ${R:0:8}"`. Grepping tools and skills for 'land onto' found only push-main.sh:490 and :880, so no shared reader or check ties the two copies together. §5 risks (:134-135) admits the coupling but does not guard it. If the lander's wording changes, the oracle refuses loudly with exit 2, so the effect is low. | sound | two-readers-of-one-config-one-re-derived |
| 16 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 2 S1-S3, section 4 Files touched (estimate) | medium | medium | confirmed | Read 54.md:35-50 and 76-79. The oracle now begins `base=$1` and refuses with exit 2 when the base does not resolve, and S3 gives the base argument only to 44 AC1 and 34 AC59. S2 gives it to 52's fixtures. Nothing else passes it. 44.md:131-137 (AC2 expects `+KIT_UNATTENDED_VERSION=1.111`, AC3 runs 'the oracle on that fixture's main tip'), 55.md:113-118 (AC1 expects exit 1, AC2 expects 'the walk failed') and 56.md:245-259 (AC6, AC10) all run the oracle with no base. 54's Files touched (113-118) lists only 44 '§4, AC1 and its §9 line'. Run as written, these criteria hit the base refusal before they reach anything they mean to check. The refusal is exit 2, so 55 AC2 and 56 AC6 could also pass on the wrong refusal if only the exit status is read. The effect stays within criterion text, so medium. | sound | - |
| 17 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md:section 2 S11, section 3 (No edit to TOOL-dPlacedRequest-34), section 6 AC11 | medium | medium | confirmed | `wc -c` of 34 printed 47782, a 346-byte margin under the 48128 figure that 49 S13 and 52 set. The AC59 bullet measured 264 bytes. The §9 lines of 34 run 64-166 bytes (rev-8 is 166). S11 counts §9 lines still to come from 49, 52 and 54, and 52 S11 restates AC59. A one-line AC59 saves roughly 100-150 bytes, so the net growth lands close to the margin. 56.md:135 forbids any edit to 34, and S11 and AC11 (93-96, 260-263) only measure and say nothing about an overrun. If `wc -c` goes over 48128, AC11 reds and no unit in the round may cut 34. The gated hard ceiling is 49152 (template-size-limits.txt:167), so the gate itself would not fail. The cost is a blocked close, which is contained. | sound | - |
| 18 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md:section 6 AC5 (rev-2 fold) and section 2 S5 | low | low | confirmed | Read 56.md:242-244. AC5 greps `in sequence` line by line and then requires `tools/unattended/unattended.test.sh` on the same line. Neither 48's nor 50's Files touched currently names unit 50 or 48, and 48's existing sequence sentence wraps as 'run in' / 'sequence.' over two lines, so the grep cannot match it. The spec lines here have no hard width limit (56's own AC5 and Edges lines run past 150 columns), so a builder can force a match by writing the line unwrapped. That makes this brittleness rather than a failure on every correct build. It stays within the criterion text, so low. | sound | - |
| 19 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md:section 4 Evidence, third bullet | low | low | confirmed | 53.md:74-77 cites 52:287, 52:309 and 52:300. Running `sed -n` on 52 shows 287 is the §6 fixture preamble, 309 is 'and a correct tree reds.' and 300 is an AC4 line. The hits it means are now at 291 (`grep -c 'S25'`), 313 (`grep -c 48128`) and 306 ('at least 2' on the next line). These are moved line citations in evidence prose and change no behaviour. | sound | - |
| 20 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md:section 2 S3 and S4, section 4 'The placed race, per attempt (S3, S4)' | high | high | confirmed | 52.md:236-239 resets the handshake files each attempt: 'touch $h/release; wait for A (bound); clear $h/once $h/held $h/release'. 56's restated sketch (56.md:155-164) has 'touch $h/release; wait for A (bound), else kill A and wait' with no clear. 56 S3 (62-64) lists only the clone, the bare remote and the stored files as per-attempt fresh state. Neither 48 (37, 72-77) nor 52 places $h inside the unit-19 clone, so a fresh clone does not reset it. The 48 stub holds only when `mkdir "$h/once"` succeeds. On attempt 2 the stale $h/once means A never holds, and the stale $h/held makes the arm's wait return at once, so B runs against an A that is not in its window. AC3 delays B on attempt 1 to force exactly this retry path, so the criterion judges an unplaced race and can pass on a narrow path: high. | sound | fixed-sleep-does-not-place-a-signal |
| 21 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 6 AC1 and section 2 S3 (base pinned to c63aabbb) | medium | medium | confirmed | Confirmed by reading the spec and re-running the log. 54.md:142-144 runs AC1 'in this worktree before --prepare with base c63aabbb', and S3 (54.md:48-50) puts the constant c63aabbb into 34 AC59 and 44 AC1. README.md build-level rules say the spec run defers every unit and closes by carry-forward, so unit 54 is built in a later build run. `git log --first-parent --min-parents=2 -3 HEAD` printed c63aabbb4 (dOrderedCharter), then dDeclaredLoop, then dSafePassage, and origin/main holds no dPlacedRequest landing yet. Once the spec run lands, HEAD's newest first-parent merge before --prepare will be 'merge: dPlacedRequest — land onto …'. The subject test passes it, and `merge-base --is-ancestor <it> c63aabbb` fails, so the §4 head (54.md:83) treats it as its own and walks it. AC1 then goes red against a correct oracle. This also breaks the spec's own claim at 54.md:89 that the ancestor test rejects an earlier landing of the same slug, because that only holds when the base is the run's own baseline. The read after --prepare in AC59 still works, so the damage is limited to an acceptance criterion and a mis-pinned base: medium. | sound | - |
| 22 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md:section 2 S4 and section 4 sketch line 'm = lines in the health log' | low | low | confirmed | Confirmed. 56.md:65-68 (S4) records 'the health log's line count when $h/held appears', and the §4 sketch line reads 'fresh unit-19 clone and bare remote; m = lines in the health log'. S3 makes every attempt a fresh clone. 36.md:36-37 puts the node-lock health log in that clone's git common dir. Nothing in the spec writes that log before the hold, so it is normally absent at hold time, and the spec never says what m is then. The effect is contained: a builder has to handle a missing file in a fixture harness, and S3's fresh fixture already makes every line this attempt's own. Low. | sound | - |
| 23 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md:section 4 'The oracle's head', the `git merge-base --is-ancestor` branch | low | low | confirmed | Confirmed. 54.md:83 reads `if [ -z "$t" ] \|\| [ "$own" = 0 ] \|\| git merge-base --is-ancestor "$t" "$base"; then …exit 2`. Any non-zero status from merge-base, including 128 on an error, makes the condition false, so the oracle walks $t as its own and does not refuse. That is the swallowed-delegate class 55 names for the walk. The path is narrow: base was just verified by rev-parse, t was just produced by rev-list, and the merge must also carry this slug's subject. A corrupt object would most likely also fail the walk that 55 guards. Low. | sound | - |
