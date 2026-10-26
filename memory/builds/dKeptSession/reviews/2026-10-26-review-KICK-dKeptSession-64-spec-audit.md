**Serves:** spec-audit KICK-dKeptSession-64@rev-1

# Tier-2 spec audit — dKeptSession, the round-5 minors batch (KICK-dKeptSession-64), ROUND 1

*This is an adversarial pre-code pass over the unit that the round-5 spec audit promoted, dated 2026-10-26. Five lenses found the findings: coherence, grounding, reuse, blast-radius and failure-envelope. A skeptic then tried to refute each one. Only confirmed findings appear below. Each item gives its address, its consequence, the fix and a left-shift gate.*

Reviewed: memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md@49d3cb0c306de8a92d623c2a7923f8b35336341b

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker or high finding was confirmed. Ten medium items and twelve low items must be fixed in the spec before the build. That is 22 items covering 26 raw confirmed findings: 13 medium and 13 low.

## Review shape

The review ran at intensity full. It had 26 raw findings: 26 confirmed, 0 refuted, 0 unverified (0 uncertain), for a precision of 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |

Adjudicated tally: by item, 0 blocker, 0 high, 10 medium and 12 low (22 items). By raw confirmed finding, 0 blocker, 0 high, 13 medium and 13 low (26 findings).

Findings that describe one defect but carry different binding grades are kept as separate items, one per grade. This happens three times: the S10 `del` spelling (10 and 24 medium, 6 and 17 low), the AC8 cutoff key (9 medium, 5 low) and the `policy fixtures` guard list (15 medium, 12 low). Each pair should get one fix.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 25 judged sound, 1 judged UNSOUND (id 12, whose corrected fix is the one given below), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 3 RE-GRADED (ids 17, 18 and 22, each from medium to low).
- Unverified: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 63 spec documents were supplied as `specs`, as sibling context.
- Checklist: 55 items, 11 for each of the 5 lenses. By design: 1 invariant.
- Move check: no checked subject moved.

Every lens and every skeptic batch returned, so the run is complete.

## Blockers

None.

## High

None.

## Medium

### M1. S1's "already acked" skip reads a precedence-ordered state, so it misses answered-and-acked ids (ids 1, 11, 21)

- **Where:** section 2 S1 and S2, the section 4 "ack batch, in order" sketch, and the section 4/8 alternative claiming that `acked` is "the one predicate that says an ack exists".
- **What is wrong:** S1 skips an id when its `state` column reads `acked`. Unit 5 S7 gives each row one state and tests `answered` before `acked`, so an id that has both an answer and an ack reads `answered`. S1 also glosses the predicate as "a cached ack naming the id in `answers`", which is a different test.
- **Consequence:** A re-ack of an answered-and-acked id is not skipped. It reaches `check_mail_duplicate`, gets rc 1, and S2 refuses the whole batch with exit 2. That is the repeat-ack refusal this batch exists to remove, now on a narrower path. It also breaks S3's promise that an already-acked id never refuses. The `expired` and `withdrawn` parts of the original claims do not hold, and neither does the unit 42 impact. The answered-and-acked path is enough to confirm the finding.
- **Fix (skeptic judged SOUND):** Define the skip as "a cached message of kind `ack` from <slug> names the id in `answers`", read from the `read_mailbox <slug> cache` rows whatever the displayed state. Alternatively, make unit 5 S7's precedence explicit and supersede it by name. Correct the section 4 alternative. Add an AC1/AC3 case: an id that is answered and acked, re-acked alone and in a mixed batch, exits 0 and prints `mail — already acked`.
- **Left-shift gate:** Add a bug-class checklist entry: "a predicate read off a derived single-valued summary column where the question is whether a fact exists". A unit test that seeds an answered-and-acked row then holds the gate.

### M2. S10's scrub spelled as a bare `del` crashes on an unset variable, and AC10 rewards that spelling (ids 10, 24)

- **Where:** section 2 S10, section 6 AC10, and the section 7 runlog arm.
- **What is wrong:** S10 prescribes "a module-level `del os.environ[...]`" for GOV_REMOTE and GOV_DEFAULT_BRANCH. The `GIT_*` loop beside it (tools/runlog/selftest.py:355-356) is safe only because it deletes keys it has found. A bare `del` of an unset key raises KeyError, and unset is the normal case. AC10's ast check for something that "deletes" passes on the crashing form and may fail the safe `pop(k, None)` form. The section 7 arm plants only GOV_REMOTE, which is one variable and only the "set" case.
- **Consequence:** Built literally, `tools/runlog/selftest.py` dies at import on every ordinary run, and the runlog selftest leg goes red. A builder who writes the safe form may red AC10. The arm never shows GOV_DEFAULT_BRANCH scrubbed.
- **Fix (skeptic judged SOUND):** Spell S10 as `for _k in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH"): os.environ.pop(_k, None)` at module level, or as a present-keys loop. Have AC10 require a no-raise form and accept either `os.environ.pop(<name>, None)` or a `del` guarded by membership. Make the arm start one process with both variables planted and one with neither.
- **Left-shift gate:** Add a red case to the runlog arm in which the suite imports cleanly with neither variable set.

### M3. AC8's fixture recipe omits `SPEC_GUARD_LEGS_CUTOFF`, so the guards join never arms (id 9)

- **Where:** section 6 AC8, and the section 4 Evidence sentence that names `derive_legs_path` as the only thing AC8 relies on.
- **What is wrong:** AC8 says to build the fixture as the spec-tokens self-test does "its lines 203 and 317". Line 317 closes the printf of `SPEC_LEGLINE_CUTOFF`. The guards join prints a `guards` hit only when `g_armed` is true (check-spec-tokens.py:1468 and :1572-1579). That requires `SPEC_GUARD_LEGS_CUTOFF` to be set on or before the spec's date. The first fixture that sets it is test.sh:591-592.
- **Consequence:** A literal fixture prints a NEAR line ("SPEC_GUARD_LEGS_CUTOFF blank (arm off)") and no `policy fixtures <- tools/policy/...` hit. AC8 then goes red for a fixture reason. A builder who "fixes" this by reading NEAR lines grades the wrong output.
- **Fix (skeptic judged SOUND):** Point AC8 at `tools/check-spec-tokens.test.sh:591-592` (GUARD_LEGS and `SPEC_GUARD_LEGS_CUTOFF="2026-09-01"`). Require the fixture's `.memory-tree.conf` to set the key on or before 2026-10-26, and require `memory/project/spec-token-waivers.txt` to exist. Add the cutoff key to section 4's "which the probe of AC8 relies on" sentence.
- **Left-shift gate:** Add a checklist entry: "a probe recipe that cites fixture line numbers must cite the lines that arm the path under test".

### M4. The `policy fixtures` guard is understated, so this unit's own population is misjudged (id 15)

- **Where:** section 4 Evidence, section 2 S7, section 6 AC8 and section 7.
- **What is wrong:** Section 4 says origin/main's `policy fixtures` leg has the guard `{prefix}/policy/`. At origin/main it carries 65 guards, among them `{prefix}/memory-tree/gen_build_index.py`, `{prefix}/workflows/unattended-build.template.js` and `{prefix}/lib/`, all of which this unit edits. S7 still fixes the work as "the lines of units 58 to 61", which contradicts S6's derived population. Section 7 leaves `policy fixtures` off this unit's leg line. AC8's fixture declares only the directory guard.
- **Consequence:** A builder writes ledger lines for 58 to 61 only. At the reconcile, the guards join prints `policy fixtures <- tools/memory-tree/gen_build_index.py` for this spec and its siblings. AC8 never exercises a file-level guard, so the probe passes while the real join reds.
- **Fix (skeptic judged SOUND):** Correct section 4 to say the guard list holds 65 entries, including gen_build_index.py and unattended-build.template.js. Drop "units 58 to 61" from S7 in favour of S6's derived population. Name this unit as a member that owes a `NOT RUN — policy fixtures not declared` line until the reconcile. Add `{prefix}/memory-tree/gen_build_index.py` as a second guard in AC8's fixture, and plant a copy of this unit to show a file-level hit.
- **Left-shift gate:** This is class `hand-named-gate-list-green-while-the-bar-reds`. The spec-tokens guards join is the gate. Add a checklist entry: "Evidence quoting a manifest value quotes it derived, never summarised".

### M5. 63 AC14 is left unsuperseded while 64 S10 moves its subject (id 2)

- **Where:** section 2 S10 and section 6 AC17, against 63 AC14 and 63 §7's runlog arm line.
- **What is wrong:** This is class `two-guards-one-question-two-answers`. 64 S10 moves the unset out of `build_arm_env`, and AC10 requires that `build_arm_env` names neither variable. 63 AC14 still requires that "`build_arm_env` under `GOV_REMOTE=planted` returns an environment without `GOV_REMOTE`". AC17 lists 63 S14 as superseded but not AC14, and not the §7 arm line that covers it.
- **Consequence:** `build_arm_env` copies `os.environ` (selftest.py:1515-1520), so an arm that plants the variable after import reds under 64's design. 63's ledger then has no legal answer for AC14.
- **Fix (skeptic judged SOUND):** Add 63 AC14's `build_arm_env` clause and 63 §7's runlog arm line to S10 as superseded by name, and add both to AC17's list. Restate the clause as "a process started under GOV_REMOTE=planted reaches no case with GOV_REMOTE set".
- **Left-shift gate:** Add a ledger lint that flags any acceptance criterion of a superseded spec item whose subject the superseding spec changes but does not list.

### M6. AC11's floor-rise count leaves out most of 63's arm (id 3)

- **Where:** section 6 AC11 and section 2 S11.
- **What is wrong:** AC11 diffs `<parent of 63's pass>..HEAD -- unattended.test.sh` and expects the pins to rise only by "63's chain read and this unit's S1, S3 and S5". 63's arm covers AC7, AC11, AC12, AC15 and AC16 (63.md:390), which includes the chained ack pair, the repeated and empty ack lists, and the feed lines. AC11 also allows only one `FLOOR_SHARD_<k>` line.
- **Consequence:** On a correct build the stated rise does not match the diff, so AC11 reds. A build made to match AC11 undercounts, and dropped assertions go unnoticed.
- **Fix (skeptic judged SOUND):** Restate the rise as "by the counted assertions of every case the diff adds or removes (63's whole unattended.test.sh arm and this unit's S1, S3 and S5 cases)", derived from the diff. Allow more than one `FLOOR_SHARD_<k>` line.
- **Left-shift gate:** Add a checklist entry: "a pin-rise criterion states the rise as derived from its diff range, never as an enumerated subset".

### M7. AC9 reuses AC8's fixture, which has no unit 61 copy and no `tools/loop/` stub (id 4)

- **Where:** section 6 AC8 and AC9, with S6 and S7's population of 58 to 61.
- **What is wrong:** AC9 expects a `loop selftest <- tools/loop/...` hit from "unit 61's copy". AC8's fixture copies units 58, 59, 60, 62 and 63, with stubs only at the policy paths. `tools/loop` does not exist at this base.
- **Consequence:** AC9's loop half has no subject. It either reds a correct reconcile step or is read loosely, which leaves the second instance of S9's class unexercised.
- **Fix (skeptic judged SOUND):** Have AC8's fixture also copy unit 61 and this unit (whose Files touched names `tools/loop/selftest.py`), with tracked stubs under `tools/loop/`. Alternatively, give AC9 a fixture of its own that lists them.
- **Left-shift gate:** Add a checklist entry: "a criterion that reuses another's fixture names every subject its expected output needs, and the fixture holds each one".

### M8. S5 retires `--mail chain` but leaves out its production caller in loop_transition.py (id 16)

- **Where:** section 2 S5 (the Readers line), section 6 AC5 and section 4 Files touched.
- **What is wrong:** S5 retires `read_mail_chain` and `--mail chain` "wherever unit 61's or unit 63's pass left them". Unit 61 S2's `write_consumed_acks`/`derive_mail_chain` in `tools/loop/loop_transition.py` consumes "the parent's `--mail chain` rows". S5's readers, AC5's grep and Files touched all leave that file out.
- **Consequence:** In the case S5 itself hedges for, where 61's verb survived, the caller survives too. AC5 prints 0 everywhere it looks, and the next loop transition calls a verb that no longer exists, which breaks ack placement at runtime.
- **Fix (skeptic judged SOUND):** Add `tools/loop/loop_transition.py` to S5's by-name readers and to Files touched as "S5, if a `--mail chain` call survives". Add it to AC5's `grep -c -e read_mail_chain -e "--mail chain"`, which must print 0 there too.
- **Left-shift gate:** Make retirement criteria grep the tracked tree (`git grep`) for the retired names, not a hand list of files.

### M9. The batched ack never places the bounded fetch, so the skip and the duplicate check can read a stale cache (id 20)

- **Where:** section 2 S1, the section 4 "ack batch, in order" sketch, and section 5 perf/scale.
- **What is wrong:** The order goes from the addressed-to check, to `read_mailbox <slug> cache` (which runs no fetch, per 63 S11), to `check_mail_duplicate` (which "reads the cache only; its caller fetches first", per unit 22 S3). Unit 5 S5's bounded fetch and `add_feed_sightings` are never placed, and the soft/strict exit on a failed fetch is never stated for the batch.
- **Consequence:** An id acked by another session or node and not yet fetched reads as not acked, the duplicate check passes on the stale cache, and a second ack lands. If the fetch runs between the two reads, they judge different caches. A dead remote's exit code is left to the builder.
- **Fix (skeptic judged SOUND):** Add a first row to S1 and the sketch: one bounded fetch of the build's mail refs plus `add_feed_sightings`, as in unit 5 S5, before the per-id loop. State its failure exit: strict exits 2 with nothing built, soft prints the `mail — local copy` line. Say that the state read and `check_mail_duplicate` both read the cache that fetch filled. Add an AC3-style case: an id acked on a second clone's session ref and pushed is skipped by the acking clone only after the fetch.
- **Left-shift gate:** Add a checklist entry: "every cache-only reader in a write path names the fetch that precedes it and that fetch's failure exit".

### M10. The amended dPlacedRequest ask row leaves the walk's order against `add_feed_event` open (id 23)

- **Where:** section 2 S13 and S18, and section 8 F1.
- **What is wrong:** This is class `append-without-an-idempotence-key`. The row adds an `add_feed_sightings` walk to `write_gov_ref`'s success exit "after S3 sets the cache ref". It never says whether TOOL-dPlacedRequest-13 S3's `add_feed_event` stays for a create or an update, or where it sits relative to the walk.
- **Consequence:** Built in event-then-walk order, the tip is already in the feed, the walk stops at once, and commits 1..k-1 of a chained landing get no feed lines. That is the gap 63 S16 exists to close. AC13 and AC18 grep only the row's words, so this build passes them. The skeptic found that walk-then-event does not duplicate, because `add_feed_event` is keyed.
- **Fix (skeptic judged SOUND):** Have the row say that for a create or an update the walk REPLACES S3's `add_feed_event`, the walk appending the tip as its newest event, and that only a deletion keeps the single `add_feed_event`. Add to the accept clause: a three-message chained landing appends exactly three events, each key once, and `check_feed` passes. The probe for dPlacedRequest is a chained `write_gov_ref` in a scratch repo followed by `--feed check`.
- **Left-shift gate:** Make that probe the gate the ask row's accept clause carries.

## Low

### L1. The S10 `del` spelling, at its low-graded reading (ids 6, 17)

- **Where:** section 2 S10 and section 6 AC10.
- **What is wrong:** This is the same defect as M2: a bare module-level `del os.environ[...]` raises KeyError when the variable is unset, and AC10's "deletes" leaves open whether `os.environ.pop(k, None)` passes.
- **Consequence:** The import crash reds the `runlog selftest`, `pre-push run-log line` and `run-gates run-log line` legs at once, so the defect cannot ship. Id 17 was re-graded from medium to low by the skeptic for that reason. What is left is a misleading spelling.
- **Fix (skeptic judged SOUND):** As M2: an absent-tolerant unset (`os.environ.pop(<name>, None)`, or a `del` guarded by membership), with AC10 accepting either form at module level.
- **Left-shift gate:** M2's no-variables import case.

### L2. AC8 cites line 317, which writes the wrong cutoff key (id 5)

- **Where:** section 6 AC8.
- **What is wrong:** This is the same defect as M3, at low grade. Line 317 writes `SPEC_LEGLINE_CUTOFF`, but the join arms on `SPEC_GUARD_LEGS_CUTOFF` (test.sh:592). Without it, the hits land in NEAR.
- **Consequence:** A literal probe prints no `guards` hit and meets AC8's own red-when on a correct step. The liveness that S8 moves onto this probe is not shown.
- **Fix (skeptic judged SOUND):** Cite `tools/check-spec-tokens.test.sh:592` (`SPEC_GUARD_LEGS_CUTOFF="2026-09-01"`), and require the fixture's `.memory-tree.conf` to set that key on or before 2026-10-26.
- **Left-shift gate:** M3's checklist entry.

### L3. The section 4 evidence and the section 7 reconcile note understate the `policy fixtures` population (id 12)

- **Where:** section 4 Evidence ("origin/main's manifest declares `policy fixtures` with guard `{prefix}/policy/`") and the section 7 note on reconcile.
- **What is wrong:** The guard list has 65 entries. Its non-broad paths, those under `BROAD_LEG_FLOOR = 5`, include `{prefix}/workflows/unattended-build.template.js` and `{prefix}/memory-tree/gen_build_index.py`, both in this unit's Files touched. Section 7 names only `loop selftest` as a leg to add at reconcile.
- **Consequence:** S9's derived join still adds the leg, so behaviour does not change. The next reader is told that only units touching tools/policy/ owe `policy fixtures`.
- **Fix (skeptic judged the finder's fix UNSOUND, so this is the skeptic's corrected fix):** Correct the evidence: origin/main's `policy fixtures` guard has 65 entries, and its non-broad paths include `{prefix}/policy/`, `{prefix}/workflows/unattended-build.template.js` and `{prefix}/memory-tree/gen_build_index.py`, which this unit's Files touched trips. Make the section 7 note say the reconcile adds `policy fixtures` to this spec's leg line as well as `loop selftest`.
- **Left-shift gate:** M4's checklist entry.

### L4. S18 and AC18 use bare S3 and S4 for another spec's items (id 7)

- **Where:** section 2 S18 and section 6 AC18.
- **What is wrong:** This is class `two-answers-to-one-question`. "after S3 sets the cache ref", "S4's walk factored per ref" and "the walk S3 calls" mean TOOL-dPlacedRequest-13 S3 and S4. In this spec, bare S3 and S4 are its own mixed-batch and ledger-answers items.
- **Consequence:** The BACKLOG ask row can name the wrong caller of the walk, and AC18's grep has no fixed text to match.
- **Fix (skeptic judged SOUND):** Spell every outside reference in full: "TOOL-dPlacedRequest-13 S3" and "TOOL-dPlacedRequest-13 S4's walk".
- **Left-shift gate:** Add a spec-tokens check: a bare `S<n>` in a sentence that names another spec's id must carry that id's prefix.

### L5. S17's line numbers disagree with section 4 and 63 §4 (id 8)

- **Where:** section 2 S17, against section 4 Evidence and 63 section 4.
- **What is wrong:** This is class `two-answers-to-one-question`. S17 cites `:1004`, `:1135` and `:1209` in tools/runlog/extract.py, which are a call line and two glob lines. Section 4 and 63 cite the `def` lines `:991`, `:1131` and `:1204`. Both sets of numbers are accurate.
- **Consequence:** The next audit will read the mismatch as drift. Behaviour is unaffected.
- **Fix (skeptic judged SOUND):** Cite the `def` lines in S17 (`scan_preflights` :991 calling `_check_inside` at :1004, `measure_tree` :1131, `measure_ready_tree` :1204), or say that the numbers are the call and glob lines.
- **Left-shift gate:** Add a checklist entry: "a code citation is the def line unless the sentence says otherwise".

### L6. The left-shift gates sent to "a separate unit by M2" have no owning unit or row (id 13)

- **Where:** section 3 Non-goals, the left-shift gates bullet.
- **What is wrong:** This is class `orchestrator-hand-off-owed-a-disposition`. The round-4 audit's gates (the ledger lint, the spec-tokens "reads as" check and the lander reconcile step) are deferred without naming a unit or a parked row. The build's BACKLOG holds only KICK-dKeptSession-29 and its SEV row.
- **Consequence:** BUILD-METHOD requires every confirmed finding to be left-shifted. The classes behind M1, M2 and M4 can return with no gate and no record that one is owed. Only traceability is affected.
- **Fix (skeptic judged SOUND):** Add one parked row per gate to memory/builds/dKeptSession/BACKLOG.md, or name the unit id that owns it, and cite the rows in the non-goal bullet.
- **Left-shift gate:** Add a checklist entry: "a deferral names its owning unit id or BACKLOG row".

### L7. S16 hand-edits a rendered file instead of running the kit's renderer (id 14)

- **Where:** section 2 S16, with section 4 Files touched and section 10 Reuse audit.
- **What is wrong:** S16 edits `tools/workflows/unattended-build.js` and the template "to the same bytes". tools/workflows/kit.toml:62-65 declares the `.js` file as rendered from the template by `check-protocol-parity.test.sh --render`. Section 10 names no renderer seam for S16, though S12 names the adopter for the VERBS pair. The `review-protocol parity (kit vs dogfood)` leg is missing from section 7's leg line.
- **Consequence:** A one-byte slip reds the parity leg at the bar. The precedent of treating rendered pairs as two hand-edited files carries into the next amendment. The effect is contained, because the parity leg catches any drift.
- **Fix (skeptic judged SOUND):** Edit `tools/workflows/unattended-build.template.js:2078`, then regenerate with `bash tools/workflows/check-protocol-parity.test.sh --render`. Add that renderer to section 10's seams. Add an AC16 probe: `bash tools/workflows/check-protocol-parity.test.sh` exits 0 at the pass. That run is a gate, so the build must run it.
- **Left-shift gate:** The parity leg. Also add a checklist entry: "a file a kit.toml marks `role="rendered"` is never in a hand-edit instruction".

### L8. S13's Files touched leaves out the derived carriers of a new dPlacedRequest ask (id 18)

- **Where:** section 2 S13 and section 4 Files touched.
- **What is wrong:** Filing the ask mints a TOOL-dPlacedRequest id with a `SEV` row. It also moves `memory/backlog/TOOL.md` (generated) and the `ids:` and gen:build-index regions of `memory/builds/dPlacedRequest/README.md`. Files touched names only the BACKLOG file.
- **Consequence:** The M6 write set omits a file that every ask-filing build shares, and the derived views stay stale until a freshness gate reds. Id 18 was re-graded from medium to low by the skeptic: Files touched is an estimate, and the derived files can be regenerated.
- **Fix (skeptic judged SOUND):** Extend the entry to "`memory/builds/dPlacedRequest/BACKLOG.md` (the ask row and, if newly filed, its SEV disposition), `memory/backlog/TOOL.md` and `memory/builds/dPlacedRequest/README.md`, both regenerated by gen_build_index.py". Name the id allocation rule from memory/HYGIENE.md.
- **Left-shift gate:** Add a checklist entry: "Files touched lists every generated file its writes regenerate".

### L9. S9's rev bumps move the generated build README, which Files touched omits (id 19)

- **Where:** section 2 S9 and section 4 Files touched.
- **What is wrong:** S9's rev bumps change the rev column in the generated `memory/builds/dKeptSession/README.md`. Prior spec commits 80cddd199 and 9e508febc each rewrote that file. Files touched lists only `spec/` and `build/`. The skeptic found that the gen:spec-records regions would not change.
- **Consequence:** The README render stays stale until the build-index or hygiene leg reds.
- **Fix (skeptic judged SOUND):** Add "`memory/builds/dKeptSession/README.md` and the specs' `gen:spec-records` regions, regenerated by `python tools/memory-tree/gen_build_index.py` after S9's rev bumps and the new ledger records" to Files touched.
- **Left-shift gate:** L8's checklist entry.

### L10. The empty id list is spelled two ways (id 22)

- **Where:** section 2 S1 against the section 4 sketch, and section 2 S3 and section 6 AC3.
- **What is wrong:** S1 gives `--mail ack <slug> [<id> ...]`, and the sketch gives `--mail ack <slug> <id> [<id> ...]`.
- **Consequence:** Id 22 was re-graded from medium to low by the skeptic. 63 S15 and AC15 already assert that `--mail ack <slug>` exits 0, and 64 S3 keeps that case, so a criterion catches a build that follows the sketch. What is left is a wording mismatch.
- **Fix (skeptic judged SOUND):** Make the sketch's grammar `--mail ack <slug> [<id> ...]` and add a row "no ids given -> exit 0, nothing written", or rule the empty list a refusal and supersede 63 S15 by name. Add an AC3 clause: `--mail ack <slug>` with no ids exits 0 and leaves the tip unchanged.
- **Left-shift gate:** Add a checklist entry: "a verb's grammar is stated once and the sketch quotes it".

### L11. S14 never says the closing `<<<` marker takes `MARKER_LEAD` (id 25)

- **Where:** section 2 S14 and section 6 AC14.
- **What is wrong:** The `blk` extractor at tools/lib/resolve-python.test.sh:213 holds two regexes, the opener `^# >>> ` and the closer `^# <<< `. S14 treats `blk` as one site. AC14 checks only the grep lines and the `nblk` count, so it never runs `blk`.
- **Consequence:** A build that changes only the opener extracts every `// >>>` block to the end of the file, the JS parity rows report false drift, and AC14 stays green.
- **Fix (skeptic judged SOUND):** Have S14 say that `blk` reads both markers through `MARKER_LEAD`. Extend AC14's probe: `blk` over a scratch file with a `// >>> s` ... `// <<< s` block followed by trailing lines prints only the block.
- **Left-shift gate:** That `blk` probe, kept as a case in resolve-python.test.sh.

### L12. S9 handles only legs the base adds, not legs it renames or retires (id 26)

- **Where:** section 2 S9.
- **What is wrong:** S9 calls itself the class but derives only the legs the base declares and HEAD does not. The leg history since 2026-09-01 shows retired names such as "branch-reconcile skill wiring" and "template size <=48KiB".
- **Consequence:** After such a reconcile, every non-terminal spec that names a retired leg fails the spec-tokens leg, and S9 has no rule for it. The reconcile stops red, so nothing ships wrong.
- **Fix (skeptic judged SOUND):** Add the other direction of the comparison to S9: a name HEAD declares and the base does not is removed from, or renamed on, every leg line that names it, each edit a rev bump with its section 9 line. Add an AC9 clause over a reconciled manifest that renames one leg.
- **Left-shift gate:** AC9's rename clause. Also add a checklist entry: "a derived set-difference step states both directions".

review-shape kind=spec-audit round=1 intensity=full at=synth raw=26 confirmed=26 refuted=0 unverified=0 blocker=0 high=0 medium=13 low=13 agents=11 out-tokens=150387

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S1 (and section 4 Alternatives rejected, second bullet) | medium | medium | confirmed | In 5.md:81-83, S7 gives each row one state, and `answered` (an answer names the id) is checked before `acked`. A row that has both an answer and an ack therefore reads `answered`. 64.md:40-42 and its sketch at :216 take 'already acked' from the state column reading `acked`, so that row is not skipped. It goes on to check_mail_duplicate, gets rc 1, and S2 refuses the batch with exit 2. The §4 line at :253 ('the one predicate that says an ack exists') is false as written. One side claim does not hold: in 55 `withdrawn` is a message kind, not a state, and in 24 S5 `expired` only replaces `open`. The answered-and-acked path alone is enough to confirm. | sound | - |
| 2 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S10 and section 6 AC17 (versus 63 AC14) | medium | medium | confirmed | 63.md:98-102 (S14) puts the unset in `build_arm_env`, and AC14 at :326-328 observes that with '`build_arm_env` under `GOV_REMOTE=planted` returns an environment without `GOV_REMOTE`'. 64 S10 supersedes S14, and 64 AC10 requires that `build_arm_env` names neither variable. AC17 lists S14 among the superseded texts but not AC14, and not 63 §7's runlog arm line, which covers AC14 (63.md:393). In selftest.py:1515-1520, `build_arm_env` copies `os.environ`, so if the variable is planted after import, the copy carries GOV_REMOTE. 63's ledger then has a criterion that conflicts with 64's design and has no superseding answer. | sound | two-guards-one-question-two-answers |
| 3 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 6 AC11 (and section 2 S11) | medium | medium | confirmed | 63.md:390: 63's unattended.test.sh arm covers AC7, AC11, AC12, AC15 and AC16. That includes the chained ack pair and the repeated and empty ack lists, not only the S7 chain read (AC7). The floor rises 'by the arm's count'. 64 AC11 (blob lines 332-338) reads the diff from the parent of 63's pass to HEAD, which holds that whole arm, yet counts only '63's chain read and this unit's S1, S3 and S5'. The stated rise therefore does not match the diff for a correct build. AC11 also allows only one FLOOR_SHARD line. | sound | - |
| 4 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 6 AC8 and AC9 | medium | medium | confirmed | 64 AC8 (blob lines 313-318) builds the fixture from copies of units 58, 59, 60, 62 and 63, with stubs only at the policy paths. AC9 reuses AC8's base manifest and expects a `loop selftest <- tools/loop/...` hit from 'unit 61's copy', but the fixture has no unit 61 copy and no tools/loop stub. `ls tools/loop` printed 'No such file or directory', so nothing at this base supplies one. Run as written, AC9's loop half has nothing to test. | sound | - |
| 5 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 6 AC8 | low | low | confirmed | `sed -n 315,319p tools/check-spec-tokens.test.sh` shows line 317 writing `SPEC_LEGLINE_CUTOFF`. The guards join's key, `SPEC_GUARD_LEGS_CUTOFF`, is written at :592 and the later fixtures. In check-spec-tokens.py:1468, `g_armed` needs guards_cut set, and at :1576-1579 an unarmed missing leg goes to `near`, not `hits`. A fixture built only from the cited lines prints no `guards` hit. The defect sits in an acceptance-criterion recipe, so the impact is contained. | sound | - |
| 6 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S10 and section 6 AC10 | low | low | confirmed | S10 (blob lines 95-97) prescribes a module-level `del os.environ[...]`. `env -u GOV_REMOTE python -c "import os; del os.environ['GOV_REMOTE']"` printed `KeyError: 'GOV_REMOTE'`. The GIT_* loop beside it at selftest.py:355-356 deletes only keys it found. Built literally, the module crashes at import on the usual machine where the variable is unset, which the runlog selftest leg would catch at once. AC10's ast 'deletes' does not say whether `pop(k, None)` passes. The consequence is small and caught by a gate. | sound | - |
| 7 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S18 and section 6 AC18 | low | low | confirmed | Read 64.md:146-152. S18 opens with 'TOOL-dPlacedRequest-13 S4's add_feed_sightings' but then says 'after S3 sets the cache ref' and 'S4's walk factored per ref' with no prefix. AC18 (lines 365-366) says 'TOOL-dPlacedRequest-13 S4 as the walk S3 calls'. In this same spec, S3 (line 53) is the mixed-batch item and S4 (line 57) is the ledger-answers item, so the bare references can be read two ways. The surrounding context usually settles it, so the effect is cosmetic. | sound | two-answers-to-one-question |
| 8 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S17 (versus section 4 Evidence and 63 section 4) | low | low | confirmed | Ran grep -n on tools/runlog/extract.py. It printed 991:def scan_preflights, 1004 for the _check_inside call, 1131:def measure_tree and 1204:def measure_ready_tree. sed -n 1135p and 1209p each printed the root.glob("*/*.jsonl") line. So S17's :1004/:1135/:1209 are the call and glob lines. This spec's own section 4 says scan_preflights opens at :991, and 63.md:185-186 cites :1131/:1204 as the defs. Both sets of numbers are accurate but they disagree. Nothing behaves differently. | sound | two-answers-to-one-question |
| 9 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 6 AC8; section 4 Evidence (the derive_legs_path sentence) | medium | medium | confirmed | Ran sed on tools/check-spec-tokens.test.sh. Line 203 writes the '[{"name":"real leg"}]' manifest. Line 317 closes the printf of SPEC_LEGLINE_CUTOFF (316) into .memory-tree.conf. The first SPEC_GUARD_LEGS_CUTOFF is at line 592, where it sits beside GUARD_LEGS at 591. In tools/check-spec-tokens.py, line 1468 sets g_armed = bool(guards_cut) and ... and lines 1572-1579 print a 'guards' hit only if g_armed. Otherwise the missing leg goes to near with 'SPEC_GUARD_LEGS_CUTOFF blank (arm off)'. Section 4 names only derive_legs_path as the thing AC8 relies on. So a fixture built from the cited lines prints no hit, and AC8 goes red because of the fixture. | sound | - |
| 10 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S10; section 6 AC10 | medium | medium | confirmed | 64.md:95-101 specifies 'a module-level `del os.environ[...]`'. Ran sed -n 355,356p on tools/runlog/selftest.py: the GIT_* loop deletes only keys that exist (for _k in [k for k in os.environ if ...]: del os.environ[_k]). grep for GOV_REMOTE/GOV_DEFAULT_BRANCH in that file found nothing. A literal del of an unset key raises KeyError at import, which would turn the runlog selftest leg red on any machine that does not export them. AC10's wording ('deletes ... from os.environ') points the builder toward that form, or would fail a safe pop. | sound | - |
| 11 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S1 (the 'read as `acked` by unit 5 S7, a cached ack naming the id in `answers`' clause); section 8 alternatives for S1 | medium | medium | confirmed | Read 5.md:81-83 (S7). A non-reply row is 'answered' when a cached answer names its id and 'acked' when an ack does, with answered tested first, so a row has one state. 64 S1 (lines 41-43) bases the skip on the state column reading 'acked'. An id that was answered by 25's --mail answer and then acked therefore reads 'answered'. A re-ack would not be skipped and would reach check_mail_duplicate (rc 1), and S2 refuses the batch with exit 2. That breaks S3's promise that an already-acked id never refuses. The path is narrow but reachable. | sound | - |
| 12 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 4 Evidence ('origin/main's manifest declares `policy fixtures` with guard `{prefix}/policy/`'); section 7 note on reconcile | low | low | confirmed | Ran git show origin/main:tools/gate-legs.json with a Counter over every leg's guards. 'policy fixtures' has 65 guard entries, not only {prefix}/policy/. They include {prefix}/workflows/unattended-build.template.js (count 1) and {prefix}/memory-tree/gen_build_index.py (count 2), both under BROAD_LEG_FLOOR = 5 (check-spec-tokens.py:331). This unit's Files touched names both (64.md:239-240). The section 4 evidence understates the guard, and section 7 mentions only loop selftest as a leg to add at reconcile. S9's derived join would still catch it, so behaviour is unchanged. | unsound | - |
| 13 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 3 Non-goals (the left-shift gates bullet) | low | low | confirmed | The spec's non-goal (:167-169) does say the report's left-shift gates (ledger lint, spec-tokens checks, lander reconcile step) are 'a separate unit by M2' without naming any unit or row. memory/builds/dKeptSession/BACKLOG.md has 9 lines, holding only KICK-dKeptSession-29 and its SEV row. The finder's 'lines 56, 68, 80, 92' are not in BACKLOG, though. They are the 'Left-shift gate:' paragraphs of reviews/2026-10-26-review-KICK-dKeptSession-63-spec-audit.md, so the evidence was mislabelled, but the claim still holds. BUILD-METHOD.md:275-276 requires every confirmed finding to be left-shifted ('a finding fixed and not left-shifted returns'), and nothing records these gates as owed. Graded low because the effect is only on traceability of later work, not on how this unit behaves. | sound | orchestrator-hand-off-owed-a-disposition |
| 14 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S16 (with section 4 Files touched and section 10 Reuse audit) | low | low | confirmed | tools/workflows/kit.toml:62-65 declares unattended-build.js as role="rendered" from unattended-build.template.js. check-protocol-parity.test.sh:6 documents `--render` as the step that writes every rendered copy. S16 (:138-139) tells the builder to hand-edit both files 'to the same bytes', and §10 names no renderer seam for S16, while S12 does name the adopter for the VERBS pair. `git grep 'parallel group'` printed identical text at line 2078 in both files, with no placeholder on that line, so a correct hand edit keeps parity. The 'review-protocol parity (kit vs dogfood)' leg exists in tools/gate-legs.json and is missing from §7's leg line. Graded low: the result is the same bytes, and the parity leg catches any drift. | sound | - |
| 15 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 4 Evidence; section 2 S7; section 6 AC8; section 7 | medium | medium | confirmed | At origin/main (c53e4eb3), tools/gate-legs.json's 'policy fixtures' leg carries 65 guards, not just `{prefix}/policy/` as §4 Evidence (:206-207) says. Among them are `{prefix}/workflows/unattended-build.template.js`, `{prefix}/memory-tree/gen_build_index.py` and `{prefix}/lib/`, all of which this unit's Files touched names (S16, S14). So this unit is itself in the population. S7 (:83) still fixes the work as 'the lines of units 58 to 61', which contradicts S6's derived population ('never lines fixed in advance'). AC8's fixture declares only the `{prefix}/policy/` guard. A builder trusting the Evidence would misjudge the population. | sound | hand-named-gate-list-green-while-the-bar-reds |
| 16 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S5 (Readers line); section 6 AC5; section 4 Files touched | medium | medium | confirmed | In spec 61, S2 (:40-43) makes `write_consumed_acks`/`derive_mail_chain` in tools/loop/loop_transition.py consume 'the parent's `--mail chain` rows', and 61's Files touched lists loop_transition.py. 64's S5 Readers line (:68-72) names only the VERBS line, the loop-selftest AC3 case and the §5 lines. AC5 (:298-301) greps unattended.sh and the VERBS pair but not loop_transition.py, and 64's Files touched omits that file. 63 S6 does re-point `write_consumed_acks` to S11's sent rows, but S5 explicitly hedges for the case where 61's verb survived 63's pass ('wherever unit 61's or unit 63's pass left them'). In that same case the production caller can survive too, and AC5 would stay green while the caller breaks at runtime. The path is narrow, so medium. | sound | - |
| 17 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S10; section 6 AC10 | medium | low | confirmed | S10 (:95-97) spells the scrub as 'a module-level `del os.environ[...]` beside the `GIT_*` loop'. tools/runlog/selftest.py:355-356 is safe only because it iterates keys that are present. `env -u GOV_REMOTE python -c "import os; del os.environ['GOV_REMOTE']"` printed `KeyError: 'GOV_REMOTE'`, so a literal build crashes at import whenever the variable is unset. AC10's 'deletes' wording may also reject the safe `pop(k, None)` form. Graded low rather than medium: the crash reds the runlog selftest leg at once, so the defect cannot ship. What remains is a misleading spelling. | sound | - |
| 18 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S13; section 4 Files touched | medium | low | confirmed | Every ask in memory/builds/dPlacedRequest/BACKLOG.md (-22, -65, -66, -67) has a `- SEV ·` disposition row. `git grep dPlacedRequest-67 -- memory` hits memory/backlog/TOOL.md:470, whose header reads 'generated by tools/memory-tree/gen_build_index.py --write', and memory/builds/dPlacedRequest/README.md:7 and :93. Those are the `ids:` line, which gen_build_index.py:1831 derives, and the gen:build-index region. §4 Evidence says the F1 row is not filed yet, so S13's 'files it' path applies, yet Files touched (:245) names only the BACKLOG file. Graded low: Files touched is an estimate, the derived files are regenerable, and freshness gates catch staleness. The gap is in the M6 write set and in traceability. | sound | - |
| 19 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S9; section 4 Files touched | low | low | confirmed | Spec-64 §4 Files touched (blob 49d3cb0c, re-hashed) names `spec/` for S9's leg lines and `build/` for the ledger lines, and nothing else under memory/builds/dKeptSession/. Running `grep -n rev- memory/builds/dKeptSession/README.md` printed index rows with a rev column (`\| OPEN \| rev-2 \|`). `git log --stat` shows that the spec commits 80cddd199 and 9e508febc each also rewrote README.md. So S9's rev bumps move a generated file the write set leaves out, while S20 does list another generated render (symbols.json). One part of the claim does not hold: the new ledger lines go into the existing agent-ledger journal, which every spec's region already lists, so the gen:spec-records regions would not change. The effect is limited to a stale render that the build-index or hygiene leg catches. | sound | - |
| 20 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S1, section 4 'The ack batch, in order', section 5 perf/scale | medium | medium | confirmed | In spec-64, S1 and the §4 'ack batch, in order' sketch go straight from the addressed-to check to `read_mailbox <slug> cache` and then to `check_mail_duplicate`. Spec-63 S11 (:78-80) says the `cache` mode 'runs no fetch and no add_feed_sightings'. Spec-22 S3 (:44) says check_mail_duplicate 'reads the cache only; its caller fetches first'. Spec-5 S5 puts the bounded fetch and add_feed_sightings before derive_message_id. Grepping 63 and 64 for 'fetch' finds no fetch anywhere in the batch. Unit 5 S8 does call an ack 'a post', which might imply S5's fetch, but 64's explicit order (and cache mode) never places it. Its failure exit under soft or strict is also never stated for the batch. So a stale cache can let a second ack through, or the batch can end on an exit code the builder picks. | sound | - |
| 21 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S1 and S2 | medium | medium | confirmed | Spec-5 S7 (:80-83) ranks the states in order: 'answered' when an answer names the id, then 'acked' when an ack does. An id with both an answer and an ack therefore reads 'answered'. Spec-64 S1 glosses the skip predicate two ways: 'the id's state column ... read as acked' and 'a cached ack naming the id in answers'. Read the first way, a re-ack of an answered-and-acked id reaches check_mail_duplicate, gets rc 1 and is refused with exit 2 under S2. The expired part of the claim does not hold: spec-24 S5 sets expired only on rows that would otherwise be open. The unit 42 impact is also overstated, because spec-42 S3 acks only rows that read open. The manual re-ack case remains a real, contained defect. | sound | - |
| 22 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S1 vs section 4 'The ack batch, in order'; section 2 S3; section 6 AC3 | medium | low | confirmed | Spec-64 S1 spells the verb `--mail ack <slug> [<id> ...]`, while the §4 sketch spells it `--mail ack <slug> <id> [<id> ...]`. The inconsistency is real. The impact is overstated, though. Spec-63 S15 (:107) says 'An empty list exits 0', and spec-63 AC15 (:331) asserts that '`--mail ack <slug>` exits 0'. Spec-64 S3 only amends AC15's second call and its mixed batch, and keeps the empty case. So a criterion does catch a build that follows the sketch. What is left is a wording mismatch inside the sketch. | sound | - |
| 23 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S13 and S18, section 8 F1 | medium | medium | confirmed | TOOL-dPlacedRequest-13 S3 (:43-46) sets the cache ref and then calls add_feed_event. S4 (:47-50) walks only refs whose tip the feed does not hold. Spec-64 S13 and S18 say the walk runs 'after S3 sets the cache ref' but never say where it sits relative to S3's add_feed_event for a create or an update. If the walk runs after add_feed_event, the tip is already in the feed, the walk appends nothing and commits 1..k-1 get no lines. That is the gap 63 S16 closes, and 64's AC13 and AC18 only grep the row's words. The second half of the claim is false: S2 (:41) says add_feed_event appends only when no line carries the key (ref, blob, commit), so walk-then-event appends no duplicate and check_feed would not red. Only the event-then-walk order fails. | sound | append-without-an-idempotence-key |
| 24 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S10, section 6 AC10, section 7 runlog arm | medium | medium | confirmed | Spec-64 S10 specifies 'a module-level `del os.environ[...]`'. The loop it sits beside, tools/runlog/selftest.py:355-356, deletes only keys that are present. Running `env -u GOV_REMOTE python -c "import os; del os.environ['GOV_REMOTE']"` printed `KeyError: 'GOV_REMOTE'`, so a bare del crashes at import on every run where the variable is unset. AC10's ast check would pass on that code. The §7 arm plants only GOV_REMOTE. The runlog selftest leg would show the crash on its first run, so the effect is contained. | sound | - |
| 25 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S14, section 6 AC14 | low | low | confirmed | Checked against the tree and the pinned spec. tools/lib/resolve-python.test.sh:213 `blk` has two awk regexes, the opener `^# >>> ` and the closer `^# <<< `. grep finds no MARKER_LEAD in the file yet. Spec-64 S14 (lines 125-128) treats `blk` as a single site that reads the lead "natively" and never says the closing `<<<` marker takes it too. AC14 (lines 348-352) checks only the git grep -lE / grep -cE lines and the nblk count, so it never runs `blk`. A build that changes only the opener therefore passes AC14. I grade it low rather than higher because 63 S25 and S14 both say the extractor as a whole uses the lead, so the omission is a gap in wording and in the test, not a contradiction in the design. | sound | - |
| 26 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md:section 2 S9 | low | low | confirmed | S9 (spec-64 lines 89-94) only adds names: it takes the legs the reconciled base declares and HEAD did not, yet it calls itself the class. I re-ran the finder's command, `git log -p --since=2026-09-01 -- tools/gate-legs.json \| grep '^-\s*"name"'`. It printed removed leg names ("branch-reconcile skill wiring", "unattended arms-groups selftest", "template size <=48KiB" and others), so the base does retire and rename legs. check-spec-tokens.py:5 says a section 7 gate name that is not a leg is a failure, so a retired name would turn the spec-tokens leg red at reconcile, and S9 gives no rule for that. The red leg stops the reconcile, nothing ships wrong, and the effect is contained. | sound | - |
