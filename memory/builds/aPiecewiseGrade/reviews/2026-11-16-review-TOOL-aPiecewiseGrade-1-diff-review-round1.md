**Serves:** diff-review TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4

# Tier-2 diff review: Build aPiecewiseGrade (TOOL-aPiecewiseGrade-1..4), round 1

Provenance: an attended Tier-2 review. Finders were gov-diff-reviewer, skeptic batches were gov-skeptic, and synthesis was gov-synthesizer. Intent came from 4 spec documents supplied as `specs`, read beside the range's commit messages.

Range: 388216ff878e0f57a17682a6dd5dce8034ecd27b...4cdddad5cdcb2173f62c2d598bdbbca51378b12c (local main with aLightenedLoop merged, to HEAD). ROUND 1.

## Verdict: CLEAN WITH FIXES

No blocker and no high was confirmed. Two medium items remain open, and both need a fix before the build's next pass. By item: 2 items, both medium. One holds a single finding; the other merges three findings. By raw confirmed finding: 0 blocker, 0 high, 2 medium (ids 1 and 5), 2 low (ids 2 and 3).

Review shape: intensity full, raw 6, confirmed 4, refuted 0, merged 2, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 0 | 0 | 1 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 0 | 0 | 1 | 0 | 0 | 1.00 |

Run integrity: no lens and no skeptic batch died, and this run is complete.
- Lenses: 5 of 5 returned, 0 died. Skeptic batches: 3 of 3 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Merges: 2 duplicate refutations counted as merged confirmations (id 4 into id 3, id 6 into id 5).
- Fixes on confirmed findings: 2 judged sound (ids 3, 5), 0 judged unsound, 2 judged INSTANCE-ONLY (ids 1, 2), 0 none proposed, 0 not judged.
- Severity: 0 ungraded by the skeptic, 0 re-graded by the skeptic.
- Unverified: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Checklist: 56 items acquired from --for-diff 388216ff878e0f57a17682a6dd5dce8034ecd27b..HEAD, split as security 12, correctness 11, seams 11, verification 11, intent 11.
- By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twin flags.
- Dispositions: unclassed is refuse; 56 class slugs and 175 leg names (from tools/gate-legs.json) were handed.

## Items

### 1. MEDIUM: the start half's generation sweep deletes another in-flight run's next generation (id 1)

- **Where:** tools/unattended/unattended.sh@e57e48e3:14617 (init_spec_token_check, lines 14613-14621; read half at 14686-14687; called at 14986 and 15078; claim check at 15107-15113).
- **What is wrong:** The start half of run_spec_token_check runs rm -rf on every `spec-tokens.<slug>.specs.*` generation except the one `spec-tokens.<slug>.live` names. A fresh generation is only named in `.live` at the read half, so another in-flight `--dispatch`'s SPEC_TOKENS_CACHE_NEXT is not protected. The sweep also runs before the claim check. No verb lock serialises two `--dispatch` calls in one worktree; the only lock is claim-push.lock (line 2618).
- **Consequence:** Two same-slug `--dispatch` calls in one worktree can overlap. Examples are sibling passes fired in parallel, or a second session whose claim check 108 refuses only after the sweep has run. The second start then deletes the first checker's next generation while it is being written. The first run's cache writes fail silently and its promotion is skipped. The second run's read half can also delete the live generation the first checker is reading. Findings stay correct, because the checker swallows OSError on its cache paths (check-spec-tokens.py 2041-2093) and every miss re-grades. The cost is contained to lost cache work and repeated full re-grades of about 43 s each (PINNED 65111499e, TOOL-aPiecewiseGrade-3). It is still a deletion triggered by a caller that may hold no claim.
- **Grade:** medium (binding, kept).
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** Take one per-slug lock in the sidecar: `mkdir spec-tokens.<slug>.lock`, holding the owner's pid and a deadline so a killed run's lock can be broken. Hold it from the start half to the end of the read half. Put every piece of per-slug state under it: the `rm -f` of the `.inputs` record, the key write, the `.live` write, the sweep and the old-generation `rm -rf`. A run that cannot take the lock runs with the cache off (SPEC_TOKENS_INPUTS, SPEC_TOKENS_CACHE and SPEC_TOKENS_CACHE_NEXT all empty) and records no key. Probe: start two same-slug start halves in parallel; assert that the second removes neither the first run's NEXT nor its `.inputs`.
- **Finder's proposal (cures the cited instance alone):** Move the sweep and the mktemp after a same-slug serialisation point, or sweep only generations older than the name file's mtime or not held by a live lock.
- **Left-shift gate:** An arm in the unattended-build self-test that starts two same-slug `--dispatch` start halves in parallel, stops the first after its next generation exists, and asserts that the directory survives the second start. A second arm covers the refusal branch (lock not taken, cache off), so the harness-arms leg sees it armed.

### 2. MEDIUM: scan_live_spec's 24 counter names are spelled twice, and a mismatch silently reads 0 (ids 2, 3, 5)

- **Where:** tools/check-spec-tokens.py@93a5d813:2452 (main's read-back at 2452-2459, from `totals = collections.Counter()` at 2437 and `totals.update(got[2])` at 2450-2451; scan_live_spec's return dict at 2286-2294).
- **What is wrong:** The diff moved the per-spec loop into scan_live_spec, which returns its 24 counters as a literal dict. main sums them into a collections.Counter and reads them back by names typed a second time. A Counter returns 0 for a key it does not hold. A name misspelled on either side, or a counter added to one side only, therefore reads 0 and raises nothing. Cached entries are not checked either: read_spec_cache keeps any `counts` key as `{str(k): int(v)}`. At base 388216ff8 these were locals used directly in the summary print, with no second spelling. This is the concern the builder flagged, and it is confirmed. Today both sides hold the same 24 names (symmetric difference empty), so no output is wrong at this sha.
- **Consequence:** A later one-sided edit would print a zero in the checker's summary with no error and no red, in the plain and cached runs alike. Affected lines include "citation(s) skipped", "by bare name", "ac-order join · 0 of N" and "0 out of order". A zeroed liveness count reads as an empty population, which the [gate] rule forbids. No arm could catch it: the suite asserts only 0 for skipped, so_bare, ao_graded and ao_bad (tools/check-spec-tokens.test.sh lines 564, 1067, 1070). The PG1 differential arm cannot catch it either, because both runs go through the same dict and read-back. The totals feed only print lines and gate no exit status.
- **Grades:** id 2 low, id 3 low, id 5 medium (all binding, kept). The item is medium, from id 5. id 5 grades higher because it adds the verification gap: for four counters, no arm can detect the mismatch. Ids 2 and 3 grade the latent trap alone.
- **Fix (ids 3 and 5 judged SOUND by the skeptic; id 2 judged INSTANCE-ONLY, and its skeptic's class-level fix is folded in):** Spell the names once, as a module tuple such as SPEC_COUNTERS. Build scan_live_spec's return dict from it. Replace the Counter with a plain dict seeded from SPEC_COUNTERS, so that a misspelled name in main's read-back raises KeyError. In main, check that every `got[2]`, fresh or cached, has exactly the SPEC_COUNTERS key set, and fail loudly on a mismatch. In read_spec_cache, treat any other counts key set as a miss, so the entry re-grades instead of adding 0. Add one arm with a nonzero expected value for each of skipped, so_bare, ao_graded and ao_bad. An example is an out-of-order spec dated at the cutoff that expects `ac-order join · 1 of 1 live spec(s) · ... · 1 out of order`. Probe: in a scratch copy, misspell one name on each side in turn, watch an arm go red, then restore it and watch it go green.
- **Finder's proposal on id 2 (cures the cited instance alone):** a single COUNTER_NAMES tuple iterated by both sides, or a `set(got[2]) == set(COUNTER_NAMES)` check in main.
- **Left-shift gate:** The nonzero arms above, in the spec-tokens self-test leg. Also a checklist entry under two-answers-to-one-question: "a dict returned by one function and read back by typed names elsewhere is single-sourced, and is not read through a defaulting container."

review-shape kind=diff-review round=1 intensity=full at=synth raw=6 confirmed=4 refuted=0 merged=2 unverified=0 blocker=0 high=0 medium=2 low=2 agents=9 out-tokens=68099
review-round round=1 limit=- prior=- count=0 state=CONVERGED
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/unattended.sh@e57e48e3:14617 | medium | medium | confirmed | I read tools/unattended/unattended.sh@e57e48e3:14613-14621. init_spec_token_check runs rm -rf on every spec-tokens.<slug>.specs.* directory except the one the .live file names, and a fresh generation is only named in .live at the read half (14686-14687). So another in-flight run's SPEC_TOKENS_CACHE_NEXT is not protected. The start half is called at 14986 and read at 15078. The claim check comes after that, at 15107-15113. A grep for locks found only claim-push.lock (line 2618), so nothing serialises two same-slug --dispatch calls in one worktree. All of this is new in this diff. If the sweep deletes a run's NEXT, that run's [ -d "$_stnext" ] test fails and it skips promotion. The checker's cache read and write paths (check-spec-tokens.py 2041-2093) swallow OSError, so any failure becomes a miss and a re-grade. Findings therefore stay correct: the cost is lost cache work and repeated full re-grades, reached only on a narrow concurrent path. That is a contained effect, so medium. | instance | - | class:destructive-step-before-its-precondition |
| 2 | security | tools/check-spec-tokens.py@93a5d813:2452 | low | low | confirmed | I read tools/check-spec-tokens.py@93a5d813:2286-2294, where scan_live_spec returns a dict of 24 names, and 2452-2459, where main types the same names again against a collections.Counter, which returns 0 for a missing key. Both are new in this diff. The two key sets match today. I traced every use after the unpack: the totals only feed print lines (the summary f-strings) and gate no exit status, so a mismatch would print a wrong zero and nothing else. Today there is no behavioural effect; it is a latent trap for a later edit, so low. | instance | two-answers-to-one-question | class:two-answers-to-one-question |
| 3 | correctness | tools/check-spec-tokens.py@93a5d813:2452 | low | low | confirmed | I confirmed this at HEAD. scan_live_spec returns its 24 counters as a literal dict (tools/check-spec-tokens.py@93a5d813:2286-2294). main adds them into a collections.Counter (:2437, :2451) and reads them back by names typed a second time (:2452-2459). A Counter returns 0 for a key it does not hold, so a name that differs between the two sides would read 0 and raise nothing. The two sets agree today, so the output is correct now. The diff introduced this: the base has no scan_live_spec and no Counter unpack. It is graded low because it changes no behaviour today; it is a trap for a future edit. | sound | - | class:two-answers-to-one-question |
| 4 | seams | tools/check-spec-tokens.py@93a5d813:2452 | low | - | refuted | duplicate of id=3. It names the same two spellings at the same lines (:2287 and :2452-2459), the same Counter returns-0 mechanism, the same unchecked cached counts, and the same fix. | sound | - | - |
| 5 | verification | tools/check-spec-tokens.py@93a5d813:2452 | medium | medium | confirmed | Observed at tools/check-spec-tokens.py: totals = collections.Counter() (2437), totals.update(got[2]) (2450), and read-back by literal names at 2452-2459, while scan_live_spec's return dict spells the same 24 names again at 2286-2294. A Counter answers 0 for a missing key, so a mismatch is silent. This was introduced by the diff: at base 388216ff8 the counters were locals (ao_graded, ao_bad = 0, 0 at 2079) used directly in the summary print, with no second spelling. The names agree today, so no output is wrong yet. The defect is latent, and only a future one-sided edit would trigger it, which is why I grade it medium. The plain and incremental runs go through the same read-back, so a differential arm cannot catch a mismatch. | sound | - | class:two-answers-to-one-question |
| 6 | intent | tools/check-spec-tokens.py@93a5d813:2449 | medium | - | refuted | duplicate of id=5. It covers the same defect: the 24 counter names are spelled twice, at the return dict (2286-2294) and at main's Counter read-back (2452-2459), and a missing key silently reads 0. I confirmed this under id=5 against the code and the base, where the counters were locals. | sound | - | - |
