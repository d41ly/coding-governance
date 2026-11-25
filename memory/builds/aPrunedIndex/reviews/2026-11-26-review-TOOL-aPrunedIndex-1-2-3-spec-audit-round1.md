**Serves:** spec-audit TOOL-aPrunedIndex-1@rev-3 TOOL-aPrunedIndex-2@rev-3 TOOL-aPrunedIndex-3@rev-3

# aPrunedIndex — spec audit of units 1 to 3 at rev-3, round 1

*2026-11-26. A Tier-2 adversarial pass over three unit specs, before any code. Roles: finders
gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md@656bfa50e2f1fb6b6abcf562d3613456dfdfe935, memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md@5678553eaa44d5a8bd9cf5a127fb5c9912235300, memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md@6e3f2b5edfe327815096d957b127b96747d92b13

Round: 1

## Verdict: CLEAN WITH FIXES

No blocker stands. By item: 0 blocker, 1 high, 5 medium, 7 low, 13 in all. By raw confirmed finding:
0 blocker, 2 high, 5 medium, 8 low, 15 in all. The one high item needs a spec change before code. Unit 3
keeps a replaced edit's rows on a claim that they are always right, and the overlay can store wrong ones.

The review shape is intensity full, raw 15, confirmed 15, refuted 0, merged 0, unverified 0 (0 uncertain),
precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 7 | 7 | 0 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to
  unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded,
  0 duplicates.
- Fixes on confirmed findings: 10 judged sound, 3 judged unsound, 2 judged instance-only, 0 none
  proposed, 0 not judged.
- Severity: 0 ungraded by the skeptic, 2 re-graded by the skeptic (ids 4 and 10, medium to low). Every
  binding grade is kept here.
- Unverified: 0 answered uncertain, 0 with no usable verdict. Refuted findings shown: 0. Same-address
  pairs shown: 0, so no twin is flagged.
- Lens notes: none supplied, so every lens ran on the kit's generic brief. Preset: unit-spec, whose
  lenses coherence, grounding, reuse, blast-radius and failure-envelope ran.
- Intent: 2 spec documents supplied as sibling context. By design: none supplied, and a block of 0.
- Checklist: 24 items, each assigned to exactly one of 5 lenses: coherence 5, grounding 5, reuse 5,
  blast-radius 5, failure-envelope 4.
- Move check: no checked subject moved. Dispositions: unclassed refuse, 24 class slugs handed, 226 leg
  names read.

## HIGH

### H1 — a replaced edit's kept rows can be wrong, and are served again (ids 8 and 12, both HIGH)

**Specs:** TOOL-aPrunedIndex-3

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 4 What it
  leaves; section 2 S4; section 8 F1.
- **Wrong:** section 4 says a re-held pair's rows are right because they are keyed by content. The
  overlay hashes a file before `BEGIN IMMEDIATE` and reads its text after, up to 600 s later. An edit
  saved in between is stored under the earlier blob. A failed read stores `blob_parsed` and the `parsed`
  sentinel with no rows.
- **Consequence:** today the next build of an unbuilt tree clears such rows once the edit is replaced.
  Under this unit they stay until `--gc`, and the content is never parsed again. When a worktree holds
  it again, `show` and `check` serve wrong or missing rows. If a tree holds it, `--gc` does not clear
  them either. No plant step edits a file between hash and read, and F1 weighed file growth only.
- **Fix:** id 8's proposal was REJECTED and id 12's was judged SOUND. This is the skeptic's corrected
  fix for id 8, which is one of the two forms id 12 offers.
  - In `build_overlay`'s entries loop, read each changed file's bytes once. Derive the blob from those
    bytes with `git hash-object --stdin --path <path>`, filters applied. Have `read_text` decode the held
    bytes and never reopen the file.
  - A file whose bytes cannot be read gets no `blob_parsed` row and no `parsed` path row, and the overlay
    refuses or retries.
  - Text that is not UTF-8 is not such a failure: it is still recorded, as today.
  - Keep S4's statement that what the overlay deletes is unchanged, and reword its "is not edited".
  - Add a `released-rows` step that edits the file between the hash and the parse, restores the old
    content and requires the served text to be the old content. Add id 12's steps: the overlay's read
    answers None for a blob, then a foreign text. Replace the edit, build, commit the first content and
    require `read_dump` to equal `read_cold_dump`. See each red on today's overlay.
  - Id 12 also names re-hashing after the read. Do not take that form: id 8's skeptic found that it
    leaves a gap, and that writing no rows serves the file as defining nothing.
- **Left shift:** the `released-rows` steps in `tags bundle selftest`, and a checklist class,
  `content-key-from-another-read`.

## MEDIUM

### M1 — AC9 does not say whether its copy is already parsed at the unit's version (id 1, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 6 AC9.
- **Wrong:** AC9 asks for both SQL indexes and two unbuilt trees, and says nothing of `blob_parsed` rows
  at the version in use. The quoted 122 s run skipped 15,106 blobs as fresh. The unit's edit to
  `tag_index.py` makes a new version, which parses everything again.
- **Consequence:** two builders can time different workloads. A pre-parsed run certifies 420 s without
  the first landing, and an unparsed run has no measured basis for its cost.
- **Fix (sound):** state the copy's condition. Either run one command at the unit's version first, or
  time the first run at a new version. Preferably record both, say which binds to 420 s, and require the
  summary's `blobs parsed` figure in the record.
- **Left shift:** a checklist class, `measurement-workload-unstated`.

### M2 — `dead-versions` is said to cover AC8 but never reads stderr (id 2, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 4 The
  plant; section 6 AC8; section 7 New arm.
- **Wrong:** the four steps check counts, index presence and stamp only. No staged break touches S7's
  stderr line.
- **Consequence:** the plant stays green when `load_index` prints on every open or builds in silence. Unit
  2's AC7 keys its kill on that line.
- **Fix (sound):** add a step that captures stderr at first creation, at the reopen after the drop and at
  a reopen of the complete file. Require 0, 1 and 0 building lines, the one naming `path_row_version`,
  and make the exit depend on it. Add two staged breaks: printing always, and printing never.
- **Left shift:** the checklist class `rule-stated-with-no-check-that-fails`. Each criterion an arm line
  claims names the staged break that reds it.

### M3 — no criterion observes the `SELFTEST_ROWS` rows or the new label (id 3, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 2 S5; the
  same in unit 2 S3 and unit 3 S6.
- **Wrong:** the cited criteria run `gov_tag.py --fixture --plant` and never read `SELFTEST_ROWS` or a
  runner line. The label change has no observer.
- **Consequence:** with a row missing or misspelled, every criterion stays green and the plant runs in no
  leg.
- **Fix (judged INSTANCE-ONLY; the skeptic's class-level fix):** in each of units 1 to 4 add a criterion
  that reads `SELFTEST_ROWS` without running the leg. A Python probe importing `tag_bundle` prints exactly
  one row for each of the unit's plants, with exit 0 and the pinned last-line text. In unit 1 also require
  `grep -c 'bundle plant ' tools/playbook/tag_bundle.py` to print 0, and the `tag plant` label on the
  runner's ok, FAIL and summary lines. Cite it from unit 1 S5, unit 2 S3, unit 3 S6 (both plants) and unit
  4 S6 (`gc-predates`).
- **The finder's proposal, which cures the cited instance alone:** the same probe in units 1 to 3, with
  unit 4's row left unobserved.
- **Left shift:** the checklist class `rule-stated-with-no-check-that-fails`. A gate form is `tags bundle
  selftest` failing on an unregistered plant.

### M4 — the wait behind worktrees on older code is not priced (id 13, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 4 What does
  not change, last bullet; section 5 risks; section 6 AC9.
- **Wrong:** 100 of 104 worktrees carry the old sweep, which runs inside the write lock. Every check takes
  that lock at its overlay, even when clean. Only which rows old code clears is priced.
- **Consequence:** after landing a check can still wait past 420 s behind an older build, whose two sweeps
  took 537 s. The README promises the leg fits its ceiling, and AC9 measures a private copy with no other
  writer. No result is wrong.
- **Fix (sound):** name the residual in section 5: the leg fits once the node's active worktrees carry this
  code. Add a Rollout line to bring the worktrees that run bars onto it. State in AC9 that it does not
  observe lock contention from older code, and soften the headline to match.
- **Left shift:** a checklist class, `mixed-fleet-cost-unpriced`.

### M5 — a full disk during the index build has no stated behaviour (id 14, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 5 error /
  empty / loading states; section 4 Migration.
- **Wrong:** section 5 names only the lock timeout and section 4 only a kill. A `CREATE INDEX` that meets
  a full disk makes `load_index` refuse, though every row is intact.
- **Consequence:** on a nearly full node each open spends minutes building, fails with `cannot be opened`
  and is retried. Every leg that opens the index goes red there, where the same file opened before.
- **Fix (the finder's was REJECTED; the skeptic's corrected fix):** in unit 1's Rollout, and so for unit
  2's index, state the free space both `CREATE INDEX` statements need, about 1 GB of file growth plus
  sorter temp space on the 12.6 GB file, and have it checked before the open. In section 5 state that a
  full disk raises the existing `cannot be opened` refusal, with every row intact and any finished index
  kept.
  - If degrading is chosen instead, run each SQL index of `SCHEMA` as its own statement and warn on
    `SQLITE_FULL` alone, with lock and other errors still refusing.
  - Test it by removing the index, VACUUMing the fixture, and wrapping `sqlite3.connect` so that
    `load_index`'s own connection sets `PRAGMA max_page_count` to the current `page_count` before `SCHEMA`
    runs. Require the chosen behaviour and unchanged row counts.
- **Left shift:** a checklist class, `disk-full-state-unhandled`.

## LOW

### L1 — the live-index gate is stated without the owner's conditions (id 4, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 3 last
  bullet and section 7; unit 1 section 3 and Rollout; unit 2 sections 3 and 6.
- **Wrong:** the specs wait for an "owner's go" that was given on 2026-11-25 with conditions they do not
  state.
- **Consequence:** read literally, the go already stands and the live file could be opened early. Each
  section 3 separately forbids the open and the README carries the condition, so the effect is wording.
- **Fix (judged INSTANCE-ONLY; the skeptic's class-level fix):** state the conditioned answer once per spec
  in section 3: all four units built and measured on private copies, closing review clean, before the bar,
  citing 2026-11-25-prompt-TOOL-aPrunedIndex-3-revision. Make every other mention point to it: the Edges
  external bullets, unit 1's Rollout and risks, the Gates closing sentences, and unit 4's section 3 and
  gates.
- **The finder's proposal, which cures the cited instance alone:** replace only "before the owner's go" in
  the three specs with those conditions.
- **Left shift:** the checklist class `two-answers-to-one-question`.

### L2 — unit 2's gate line omits legs its siblings name (id 5, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md`, section 6 Gates
  against section 4 Files touched.
- **Wrong:** its section 3 lists four legs that open the live index and section 6 names only `tags`. The
  three others and `lexicon naming predicates` are missing.
- **Consequence:** those legs run in the closing bar either way, so nothing ships wrong.
- **Fix (sound):** add those four legs to the gate line, and widen its closing sentence to the form units
  1 and 3 use ("the four section 3 lists").
- **Left shift:** the checklist class `hand-named-gate-list-green-while-the-bar-reds`.

### L3 — AC6 reads no docstring that S7 changes (id 6, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 2 S7 against
  section 6 AC6.
- **Wrong:** S7 cites AC6 for four functions' docstrings. AC6 greps only the README, the help page and the
  lines that define or call `remove_unheld_rows`.
- **Consequence:** the docstrings of `build_index` and `remove_dead_versions` can stay false unseen.
- **Fix (the finder's was REJECTED; the skeptic's corrected fix):** extend AC6 to read docstrings with
  `ast.get_docstring` on `tag_index.py`, whitespace collapsed. `build_index`'s holds "let go of" and not
  "rows no tree or worktree holds are removed". Those of `remove_dead_holders` and `remove_released_rows`
  each hold "let go of". Those of `remove_unheld_rows` and `remove_dead_versions` each hold "old edit", and
  the latter's does not hold "as a build's sweep does".
- **Left shift:** the checklist class `criterion-asserts-what-its-own-command-cannot-show`.

### L4 — the owner's word is declared as the wrong kind of edge (id 7, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 3 Edges, last
  bullet; the same in unit 3.
- **Wrong:** units 1 and 3 spell it `hands-off external` and unit 2 `consumes-from external`. The template
  makes a precondition the second.
- **Consequence:** two declarations are backwards, on the record only.
- **Fix (sound):** spell it `consumes-from external` in units 1 and 3.
- **Left shift:** the checklist class `two-answers-to-one-question`. The sibling edges are read side by
  side.

### L5 — the leg and its runner still say they run bundle plants (ids 9 and 11, both LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 2 S5, section
  4 Files touched and Alternatives rejected; the same re-homing in unit 2 S3 and unit 3 S6.
- **Wrong:** S5 changes only the printed label. The leg's `purpose`, the exempt row's `why`, the runner's
  docstring and its summary lines still say bundle plants. No spec says the plants leave the kit's own
  selftest for a gov-only leg.
- **Consequence:** the records describe the wrong population. No verdict moves.
- **Fix (both sound, merged):** in S5 name `tag_bundle.py#run_selftest`'s docstring and its PASS and FAIL
  summary lines beside the arm label. Add `tools/gate-legs.json` (the `purpose`), `tools/govkit/registry.toml`
  (the exempt row's `purpose` and `why`) and the `memory/map/generated` files derived from them to S5 and
  Files touched, and join section 7 against their guards again. State in Alternatives rejected that the
  leg is exempt, so the plants are gov-only. Confirm with the docs, registry and map freshness legs at the
  close. Id 11's alternative is to declare the stale purpose a non-goal.
- **Left shift:** the checklist class `amendment-leaves-its-other-half-standing`.

### L6 — unit 2 owes figures to a record it does not list (id 10, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md`, section 4 Files
  touched (estimate).
- **Wrong:** AC5 and AC7 require figures in the unit's record. Units 1, 3 and 4 list an acceptance ledger
  and unit 2 lists none. Hygiene check 23 skips a Tier-1 unit.
- **Consequence:** the figures may go unrecorded or into an undeclared file. Behaviour is unchanged.
- **Fix (sound):** add
  `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-2-1-acceptance-ledger.md` to Files
  touched, or name another record there.
- **Left shift:** a checklist class, `record-owed-outside-the-write-set`.

### L7 — the growth figure is not per edit, and covers one table of three (id 15, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 4 What it
  leaves, last paragraph; section 5 perf / scale.
- **Wrong:** the mean of 28 is over a tree's 15,028 paths, not over edits. It counts `path_row` alone,
  though rows stay in all three tables, and no edit rate is given.
- **Consequence:** a reader cannot size the growth or decide when to run `--gc`.
- **Fix (sound):** label 28 as the mean over a tree's paths. Give rows in all three tables for the charter
  and a guide. Measure recorded edits per day or say the rate is unmeasured.
- **Left shift:** the checklist class `rate-quoted-without-its-denominator`.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=15 confirmed=15 refuted=0 merged=0 unverified=0 blocker=0 high=2 medium=5 low=8 agents=11 out-tokens=107291 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=2 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 6 AC9 | medium | medium | confirmed | Unit 3 AC9 requires only that both SQL indexes stand and the two trees are unbuilt. It says nothing about blob_parsed rows at the version in use. Re-read big3.err/big3.out: 'LAB rc=0 wall 122.1 cpu 41.0' and '0 blobs parsed, 0 extractor runs, 15106 skipped as fresh', the diagnosis's 122.1 row, so the quoted cost is a pre-parsed run. tag_index.py#derive_extractor_versions hashes the on-disk module bytes, and CITATIONS lives in tag_index itself. AC4's loading rule uses the worktree's own path, so the edited file gives a new version and a full re-parse unless the copy was prepared. Unit 1's Rollout and unit 2's Migration both state that re-parse. Unit 3's AC9 text settles neither workload. Consequence contained: an ambiguous acceptance measurement. The fix states the condition, the binding run and the parsed count, which removes the ambiguity. AC4 of units 1 and 3 compares like with like, so needs nothing. | sound | - | new:measurement-workload-unstated |
| 2 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 4 The plant, section 6 AC8, section 7 New arm | medium | medium | confirmed | Read unit 1 section 4 'The plant', steps 1-4: only step counts, index presence, path_row count and stamp. Step 3 reopens through load_index but captures no stderr, and nothing opens a complete file or watches first creation. AC8's red conditions (prints always, builds silently) are met by none of the four staged breaks in the section 7 New arm line, which nevertheless claims 'covers AC1 AC2 AC3 AC8'. A plant built to section 4 prints its passing last line with load_index silent or noisy. Unit 2 AC7 keys its kill on that line. The fix adds the three captures (0, 1, 0), makes the exit depend on them and adds both breaks, which covers every half of AC8. | sound | rule-stated-with-no-check-that-fails | class:rule-stated-with-no-check-that-fails |
| 3 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 2 S5 (same in unit 2 S3 and unit 3 S6) | medium | medium | confirmed | tag_bundle.py#run_selftest iterates SELFTEST_ROWS only, and a plant absent from it is not run. S5 (unit 1), S3 (unit 2) and S6 (unit 3) say their row is observed by criteria that run `gov_tag.py --fixture --plant <name>` or measure other things. None reads SELFTEST_ROWS or a runner line, and unit 1 AC5 greps only POINT_ROWS there. Unit 4 AC8 bounds the leg's wall, which a missing row only lowers. The label change has no observer; grep found 'bundle plant' at lines 387, 398, 401, 404, 406. The leg in section 7 does not fail on a missing row. The New arm lines name the row, but as a declaration, not a check of its presence. The fix cures units 1 to 3, but unit 4's S6 carries the identical pattern for its gc-predates row (observed by AC1-4 and AC7, all plant runs) and the fix leaves it standing. | instance | rule-stated-with-no-check-that-fails | class:rule-stated-with-no-check-that-fails |
| 4 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 3 last bullet and section 7 (same in unit 1 section 3 and Rollout, unit 2 sections 3 and 6) | medium | low | confirmed | Revision prompt lines 63-67 read 'Answer: Yes, once built (Recommended)', qualified 'once all four units are built and measured on private copies, when the closing review is clean and before the bar'. README Build-level rules say '(said 2026-11-25, for after the closing review)'. All three rev-3 specs (dated 2026-11-26) still say only 'before the owner's go' or 'the owner's word', with no conditions, so the go already reads as given. Contained: each section 3 separately forbids any open of the live files, the gates sections say 'owed at the close', and the README carries the condition. So the effect is wording. Fix: it replaces only the phrase 'before the owner's go'. The same unconditioned gate also stands as 'the owner's word' in the Edges bullets, 'the owner's go comes first' in unit 1's Rollout, 'the owner is asked' in unit 1's risks, and 'after the owner's go' in the gates sections. Unit 4 lines 58 and 278 carry it too. | instance | two-answers-to-one-question | class:two-answers-to-one-question |
| 5 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md:section 6 Gates against section 4 Files touched | low | low | confirmed | Unit 2 section 6 names six legs and only `tags` among those that open the live index. Its own section 3 lists four such legs, and units 1 and 3 with the same files name all four. The manifest shows those three with no guard, and tools/playbook/edge_grammar.py@809a9b70:605-606 and tools/playbook/instructions_edit.py@4d0923c2:517 reach load_index/load_view. The lexicon part is weaker: its guard {prefix}/ is carried by 13 legs, so by the template's broad-guard exclusion it is not owed, though the siblings list it. These legs run in the closing bar either way, so nothing ships wrong. Fix: adding the legs and widening the closing sentence brings unit 2 level with its siblings, and the extra lexicon leg does no harm. | sound | - | class:hand-named-gate-list-green-while-the-bar-reds |
| 6 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 2 S7 against section 6 AC6 | low | low | confirmed | S7 cites AC6 for the docstrings of S1, S2, S3 and S5. AC6's greps read remove_unheld_rows definition/call lines, README.md and help/tags.md, and no docstring. The docstrings at tools/playbook/tag_index.py@4b10fce5:771-772 ('Then rows no tree / or worktree holds are removed') and :908 ('as a build's sweep does') become false. Fix: I ran its greps. `Then rows no tree or worktree` prints 0 today because the phrase wraps, so that check can never fail. A single `let go of` hit would also leave the other functions' docstrings unobserved. | unsound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 7 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 3 Edges, last bullet (same in unit 3) | low | low | confirmed | grep of 'external' over the specs: unit 1:76 and unit 3:76 say hands-off for the owner's word before this code first opens the live index, while unit 2:59 says consumes-from for the same words. TEMPLATE-SPEC.md defines consumes-from external as the precondition the unit does not build and hands-off external as work deferred outside the build. A go is a precondition, so two declarations are backwards. Record only. Unit 4:77 defers real work and is correctly a hands-off, so the fix covers every instance. | sound | two-answers-to-one-question | class:two-answers-to-one-question |
| 8 | grounding | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 4 What it leaves ("When the pair is held again its rows are right"); also section 2 S4 and section 8 F1 | high | high | confirmed | Read tag_index.py build_overlay: hash-object runs in the entries loop, then BEGIN IMMEDIATE, then _write_parsed calls read_text, which read_bytes the working file and stores the rows under the earlier blob. A read failure gives None, and blob_parsed is still inserted with no rows. I re-ran a copy of the probe under my own scratch: 'disk EDIT1, served: [('EDIT2\n',)]', then 'after a full sweep: [('EDIT1\n',)]'. So section 4's 'When the pair is held again its rows are right' is false, and leaving replaced rows until --gc removes the sweep that heals them today. F1 and the owner's revision cover retention but not this exposure, and no non-goal withholds the fix. It needs a file edited between hash and parse plus the old content held again: a wrong result on a narrow path. The fix's root sentence is right, but its example (read, then re-hash the path, and write no rows on a mismatch) leaves the overlay recording a dirty pair with no rows. That run then serves the file as defining nothing, and it still leaves a gap between the read and the re-hash. | unsound | - | new:content-key-from-another-read |
| 9 | reuse | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 2 S5, section 4 Files touched and Alternatives rejected (the same re-homing in TOOL-aPrunedIndex-2 S3 and TOOL-aPrunedIndex-3 S6) | low | low | confirmed | gate-legs.json and registry.toml both carry purpose 'self-tests bundling a tag's node and its inbound edges', and the exempt_leg why reads 'every `bundle-*` plant'. tag_bundle.py run_selftest's docstring says 'every bundle plant', and its FAIL and PASS lines say 'bundle plant rows' and 'the bundle plants'. Unit 1 S5 changes only the printed label; no Files touched names gate-legs.json or registry.toml, and unit 4 S8 touches only the budget and evidence rows. Unit 1's rejected alternative argues leg time alone. tools/playbook/kit.toml@0699b629:214 ships `playbook render selftest`, where queued-writers sits (tools/playbook/adopt-playbook.sh@ff84b4d8:385), so the new plants do move to a gov-only leg unstated. Descriptions only; no verdict moves. The fix names every stale text I found. | sound | - | class:amendment-leaves-its-other-half-standing |
| 10 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md:section 4, Files touched (estimate) | medium | low | confirmed | Re-read unit 2: Files touched lists only tag_index.py, gov_tag.py, tag_bundle.py and the kit README. Its AC5 and AC7 both require figures in 'the unit's record', and no section names that record. Units 1, 3 and 4 each list an acceptance-ledger path. In check-memory-hygiene.sh the check 23 selection has `if (hdr !~ /Tier-2/) next`, so a Tier-1 unit gets no backstop. The list is headed an estimate and a builder may still write a record, so only documentation is at stake and behaviour is unchanged. Fix: naming the ledger path supplies the record for both criteria and follows the siblings' form. | sound | - | new:record-owed-outside-the-write-set |
| 11 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 2 S5; section 4, Files touched (estimate) | low | low | confirmed | Re-ran the grep. tools/playbook/tag_bundle.py@773a5b42:387 (docstring), 398 and 401 (arm lines), 404 and 406 (summaries) say bundle plants. registry.toml says 'every `bundle-*` plant' in why and 'self-tests bundling a tag's node and its inbound edges' in purpose, and tools/gate-legs.json@8abeccfb:4947 repeats the purpose. S5 renames only the 'printed label', and Files touched names neither registry.toml nor gate-legs.json. Units 1 to 3 add dead-versions, named-probe, released-rows and released-cost to that leg. Effect is descriptive only. Fix: it covers every carrier the grep found, or declares the stale purpose a non-goal. A grep for 'inbound edges' over memory/map and help found no other carrier. | sound | - | class:amendment-leaves-its-other-half-standing |
| 12 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 4 What it leaves (also section 2 S4) | high | high | confirmed | Read the code: build_overlay runs hash-object first and reads bytes later inside the write block, mapping OSError to None. _write_parsed inserts blob_parsed even for text None, and _write_path_rows adds the `parsed` sentinel. Spec 3 section 4 says a re-held pair's 'rows are right: they are keyed by content', and section 5 and the plants cover no unread or raced read. My own in-memory probe over the module's SCHEMA and both writers recorded B1 from a bad read, replaced the edit, then had a tree hold B1. With B1 cleared as today's sweep does, both cases gave doc#good. Unswept, a None read gave skipped x:1 and only the sentinel, and a foreign read gave skipped x:1 and doc#two. BASE has the same hole when the raced edit is re-held before an unbuilt tree is built; this unit extends it until --gc. Rows are served wrong, on a narrow path (a raced or failed read plus return to that content). F1 chooses retention but does not withhold correct keying. Fix: deriving the id from the same bytes, or re-hashing, and writing neither sentinel on failure closes both the unread and the raced forms. A non-UTF-8 text stays None on both sides (read_blobs_at also answers None), so it must still be recorded, and the fix limits itself to OSError and mismatch. The build side reads immutable objects and raises on a failed call. | sound | - | new:content-key-from-another-read |
| 13 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 4 What does not change, last bullet; section 5 risks; section 6 AC9 | medium | medium | confirmed | Re-ran the count: 100 of the 104 worktrees carry `def remove_unheld_rows(con, root`. In tag_index.py, build_index runs the sweep inside BEGIN IMMEDIATE. build_overlay takes BEGIN IMMEDIATE unconditionally, even with no changed file, and load_view calls it on every check; BUSY_TIMEOUT is 600. The diagnosis gives 537 s for the two sweeps, one per tree build. Unit 3 section 4 says older code runs the full sweep 'under the same write lock' but prices only which rows it clears. Section 5 risks and unit 1's Rollout do not mention the wait, and AC9 measures a private copy. The README still promises the leg fits its ceiling on the index as it stands. The correctness of results is unaffected, so the effect is contained. Fix: it names the residual, says what AC9 does not observe, adds the rollout step and qualifies the headline. | sound | - | new:mixed-fleet-cost-unpriced |
| 14 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 5 error / empty / loading states; section 4 Migration | medium | medium | confirmed | load_index runs executescript(SCHEMA) in the try whose handler turns sqlite3.Error into TagError 'cannot be opened'. My scratch probe capped max_page_count at the current size and created path_row_version: it raised OperationalError 'database or disk is full', with all 20000 rows intact. A grep of the specs found no free-space or disk-full text; unit 1 section 5 names only the lock timeout, and section 4 only the kill. The roughly 1 GB figure is in Migration, but with no precondition or failure behaviour. The path needs a nearly full disk (C: printed 26G free here), so it is contained. Fix: the design options cure it, but the proposed check cannot work. max_page_count is per-connection, so load_index's own connection ignores the cap. Dropping the index also leaves free pages that the rebuild reuses under the cap. Catching every failed CREATE INDEX would also swallow the 600 s lock refusal the spec keeps. Unit 2's path_row_named is built by the same executescript and has the same failure. | unsound | - | new:disk-full-state-unhandled |
| 15 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 4 What it leaves, last paragraph; section 5 perf / scale | low | low | confirmed | Unit 3 section 4 'What it leaves' says the rows 'stand in all three tables', then sizes 'one file's rows per replaced edit' with path_row alone: 15,028 paths, 426,387 rows, mean 28, 96 for AGENTS.md, 2,010 largest. That mean is over a tree's paths, not over edits. No blob_row or blob_parsed figure and no edit rate appears there or in section 5 perf. `git ls-files` printed 15743 and the '*.md' form 14995, so the denominator is indeed essentially the whole tree. The spec labels the mean as a tree mean, gives two larger points, and section 5 already says a whole-view read walks the retained rows, so only the sizing prose is affected. Fix: relabelling, three-table counts, and a rate or a stated absence of one cover the gap. | sound | rate-quoted-without-its-denominator | class:rate-quoted-without-its-denominator |
