**Serves:** spec-audit TOOL-aPrunedIndex-1@rev-1 TOOL-aPrunedIndex-2@rev-1 TOOL-aPrunedIndex-3@rev-1 TOOL-aPrunedIndex-4@rev-1

# aPrunedIndex — spec audit of units 1 to 4, round 1

*2026-11-25. A Tier-2 adversarial pass over the four unit specs, before any code. Roles: finders
gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md@07d3d557eab31ffb92bdf52e589d0ee8ac8ab465, memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md@3723eb6b45fe48adc4e42428551ba0b2b0abd780, memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md@1f48e39c4ec811568d0288cf2ff989f19e7e90f9, memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md@78fa0d58732c749e91c09413d7b7f6cda1615ea1

Round: 1

## Verdict: CLEAN WITH FIXES

No blocker stands. By item: 0 blocker, 3 high, 6 medium, 7 low, 16 in all. By raw confirmed finding:
0 blocker, 3 high, 7 medium, 8 low, 18 in all. No finding contests the two SQL indexes, the gc skip or
which rows the sweep releases. Two highs are plant proofs that cannot fail. The third is a read window
that the overlay release opens for a running check. All three need a spec change before code.

The review shape is intensity full, raw 18, confirmed 18, refuted 0, merged 0, unverified 0
(0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 8 | 8 | 0 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to
  unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded,
  0 duplicates.
- Fixes on confirmed findings: 16 judged sound, 0 unsound, 2 instance-only, 0 none proposed, 0 not judged.
- Severity: 0 ungraded by the skeptic, 5 re-graded by the skeptic. Every binding grade is kept here.
- Unverified: 0 answered uncertain, 0 with no usable verdict. Refuted findings shown: 0. Same-address
  pairs shown: 0, so no twin is flagged.
- Lens notes: none supplied, so every lens ran on the kit's generic brief. Preset: unit-spec, whose
  lenses coherence, grounding, reuse, blast-radius and failure-envelope ran.
- Intent: 1 spec document supplied as sibling context. By design: none supplied.
- Checklist: none swept, as it is absent. A zero count is not evidence that the project's recurring bug
  classes are absent.
- Move check: no checked subject moved. Dispositions: unclassed refuse, 0 class slugs handed, 226 leg
  names read.

## HIGH

### H1 — the dead pad's proof is met by the plant's own rows (id 1, HIGH)

**Specs:** TOOL-aPrunedIndex-1

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 4 The
  plant, step 4; section 6 AC3.
- **Wrong:** step 3 adds 500 rows of the reading version and nothing removes them. Step 4 drops the SQL (PINNED, 2026-11-25)
  index and asks only for more than twice the first count. With no dead row at all the counts were 319
  first and 19498 after the drop.
- **Consequence:** AC3's stated red cannot occur. A dead pad that reaches no read keeps AC1 and AC3 green.
- **Fix (sound):** remove the 500 own rows before step 4, or run step 4 before step 3. Compare the
  index-dropped count with the index-present count on the same rows, and with a no-pad, index-dropped
  count. Stage a dead pad that reaches no read and see it red.
- **Left shift:** a checklist class, `proof-met-by-another-cause`. For each positive control, run it with
  its cause removed and require red.

### H2 — the pads' proof is met by the index drop alone (id 2, HIGH)

**Specs:** TOOL-aPrunedIndex-2

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md`, section 4 The
  plant, step 2; section 6 AC2.
- **Wrong:** dropping `path_row_named` raises the count from 886 to 8946 with no pad. Step 2 requires only
  a rise.
- **Consequence:** pads that touch no probed path leave AC1 and AC2 green, so the plant certifies nothing
  about dead versions.
- **Fix (sound):** after the drop, compare each padded count with an unpadded count that also lacks
  `path_row_named`, per pad. Drop `path_row_version` as well for the dead pad, which is invisible while
  that index stands. Each padded count must exceed the unpadded one. Stage a pad on an unprobed path and
  see it red.
- **Left shift:** the same class as H1, `proof-met-by-another-cause`.

### H3 — the overlay release empties a running check's reads (id 16, HIGH)

**Specs:** TOOL-aPrunedIndex-3

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 2 S4;
  section 4 What it cannot see, second bullet.
- **Wrong:** a check reads in many autocommit queries over a fixed view. Another leg of the same worktree
  that meets an edit releases the earlier blob's rows at once. The running check then reads nothing for
  that path. At BASE those rows stay until some build. The spec names the window and neither handles,
  detects nor tests it.
- **Consequence:** a false green where the edited file held the bad citation, or a false "resolves to
  nothing" where it held the definition. This contradicts "No row any worktree is served changes". The
  spec's comparison with a commit does not cover an edit, which is more frequent.
- **Fix (the skeptic's class-level fix):** after its last served read, the reading command checks that every (path, blob) of the view it loaded
  is still held by a tree or dirty row, or that its tree and dirty rows are unchanged since `load_view`.
  Otherwise it refuses with "the view moved, re-run". This covers an edit, a commit and a removed
  worktree. Add plants for an edit and for a commit between `load_view` and the read.
- **The finder's proposal, which cures the cited instance alone:** defer the release by a generation, or have the reader
  refuse when its `dirty_path` changes, with one `released-rows` step for an edit.
- **Left shift:** a checklist class, `release-under-a-live-reader`, plus the two plants above.

## MEDIUM

### M1 — no criterion observes the build's headline result (id 3, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/README.md`, Expected improvements item 2, against section 6 of
  units 1 to 4 (unit 1 AC4, unit 3 AC4).
- **Wrong:** the README promises that the leg fits its 420 s ceiling on the index as it stands. Unit 1 AC4 (PINNED, 2026-11-25)
  reds on output bytes only, and the other timings bound one sweep and one probe pass.
- **Consequence:** every criterion can be green while `check` still exceeds 420 s. (PINNED, 2026-11-25)
- **Caveat:** the sub-claim that reads may not get faster is overstated, as the step counts and the
  EXPLAIN bound them.
- **Fix (sound):** at unit 3 or 4, require that `check` on a private copy of the 12.6 GB index, with an
  unbuilt HEAD and base, finishes below 420 s once both SQL indexes exist. Make unit 1 AC4 red when the (PINNED, 2026-11-25)
  unit's CPU seconds are not below BASE's.
- **Left shift:** a checklist class, `goal-without-criterion`.

### M2 — named-probe demands equal counts that correct code does not give (id 9, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md`, section 4 The
  plant, item 1; section 5 AC1.
- **Wrong:** SQLite 3.53.4 fires the progress handler during a compile, so the first call counts it. On
  one connection the counts were 886, 839, 840. A warm-up call still leaves a one-step difference.
- **Consequence:** the plant exits 1 on the finished unit, so AC1 and the new arm cannot go green.
- **Fix (sound):** run the probe once uncounted, or count each case on its own fresh connection. Replace
  equality with a bound, such as each later count at most 1.1 times the first. The dropped-index count
  should exceed twice it. Run the finished plant green, then red with `path_row_named` removed and the
  version index present.
- **Left shift:** a checklist class, `count-includes-setup-cost`, shared with M3.

### M3 — dead-versions demands equal counts across a compile (id 10, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 4 The
  plant, item 3; section 6 AC2.
- **Wrong:** the first tag read's count includes its compile and the second's does not. In the spec's order
  the prototype printed 837 and 820. The pinned 820, 820 came from a statement already run once.
- **Consequence:** `dead-versions` exits 1 on correct code and AC2 cannot pass.
- **Fix (sound):** state that `read_step_count` runs the read once uncounted, or counts on a prepared
  statement, and that the handler also fires during compile. Alternatively bound step 3, with the second
  count at most twice the first. Re-pin the table from the plant's own sequence. Run the finished plant
  green with no tag read ahead of step 3.
- **Left shift:** `count-includes-setup-cost`. M2 is separate because it is another plant, and its
  one-step drift survives a warm-up.

### M4 — five plants go into a leg with no measured room (id 12, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md`, section 7 New arm
  line and section 6 AC1 cost, and the New arm lines of units 1, 2 and 3.
- **Wrong:** `playbook render selftest` has a 300 s ceiling and a 60 s selftest budget, and no spec names (PINNED, 2026-11-25)
  either. Nine plants timed at a mean of about 4.5 s put its 95 rows at about 430 s. (PINNED, 2026-11-25)
- **Consequence:** a leg killed at its ceiling reports no arm, and a standalone run breaches its budget.
- **Caveat:** the 430 s is an extrapolation and the overrun predates this build. A killed leg reds rather (PINNED, 2026-11-25)
  than passing, and the criteria run the plants directly.
- **Fix (sound):** before code, time `bash tools/playbook/adopt-playbook.sh --selftest` alone at BASE.
  Record it against the 300 s ceiling and the 60 s row of `tools/run-gates/selftest-budgets.txt`. State the (PINNED, 2026-11-25)
  added seconds per plant in each spec. If it does not fit, home the five plants in a leg with room, with
  its budget and ceiling-evidence rows, or collapse the runs that `run_plant_rows` repeats per row. Add a
  criterion that the leg finishes under its ceiling.
- **Left shift:** the leg `leg ceilings clear their evidenced maximum`, whose evidence row for this leg is
  1.5 s. That row needs a fresh reading.

### M5 — the SQL index build is priced for a waiter and for one node only (ids 13 and 17, both MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 4 Migration
  and section 5 risks and error states; unit 2, section 4 Migration.
- **Wrong:** the first opener builds both indexes, about 205 s, under whatever ceiling it has. The specs (PINNED, 2026-11-25)
  do not cover a killed build, name no build step free of a ceiling, and treat this node's file alone. The
  openers include legs with ceilings of 120 s and 180 s, where the risk line names only 180 and 420. (PINNED, 2026-11-25)
- **Consequence:** on any node with a large index a killed CREATE INDEX rolls back and the next opener
  starts it again. Other openers wait on the lock and can hit their own ceilings.
- **Caveat:** each CREATE INDEX commits alone, so progress is lost per index and not per pair. No row or
  verdict is wrong, and a 420 s leg can complete the build. (PINNED, 2026-11-25)
- **Fix (sound, both):** add a rollout step to section 4. One named command outside any leg, such as
  `gov_tag.py where <tag>`, opens the index once per node before that node's first bar. Say that a killed
  first open rolls back and is restarted. Put it in `help/tags.md` beside S6's sentence. Give `load_index`
  one stderr line when it starts building a missing index. State how the building worktree avoids opening
  the live file before the owner's word. Probe by killing an opener mid-build on a private copy, then
  reopening and observing both indexes present and the rows unchanged.
- **Left shift:** a checklist class, `migration-under-a-leg-ceiling`.

### M6 — section 7 lists legs that open the live index section 3 forbids (id 14, MEDIUM)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 3 against
  section 7; the same in units 2, 3 and 4 for the legs each lists.
- **Wrong:** three listed legs open the live index from the worktree under build. A fourth opener,
  `instruction units selftest`, is in no section 7, and it reaches the index through `load_resolver()`.
- **Consequence:** running a listed leg after the first edit of `tag_index.py` adds the SQL indexes to the
  live file without the owner's word. Each further edit then writes another full set of rows.
- **Fix (sound):** in section 3 of every unit list `tags (the resolver's checks)`, `instruction edits
  (manifest checks)`, `edges (every declared edge parses, is registered and resolves)`, `instruction units
  selftest` and any hand-run `gov_tag.py` verb. State that none runs from this worktree before the owner's
  go, and that per-unit verification uses `--fixture` plants and private copies only. Say the section 7
  leg line is owed at the close after the go. Add `instruction units selftest` to unit 1's section 7.
- **Left shift:** a checklist class, `listed-leg-breaks-a-non-goal`.

## LOW

### L1 — unit 2 repeats unit 1's help sentence (id 4, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md`, section 2 S4 and
  section 6 AC6.
- **Wrong and consequence:** unit 1 S6 adds the sentence first, so unit 2's grep is green before it is
  built and its `help/tags.md` entry is never edited.
- **Fix (sound):** drop the sentence from unit 2's S4, AC6 and files touched.
- **Left shift:** a checklist class, `criterion-green-before-unit`.

### L2 — unit 3 declares no edge to units 1 and 2 (id 5, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md`, section 3 Edges,
  against section 6 AC5 and section 4 The plans.
- **Wrong and consequence:** AC5's fixture and the plans need the SQL indexes of both units, so the edge
  join cannot see a change there that breaks AC5.
- **Fix (sound):** add consumes-from `TOOL-aPrunedIndex-1` and `TOOL-aPrunedIndex-2`, with the reciprocal
  hands-off in unit 1. Unit 2 is Tier-1, so its side is optional.
- **Left shift:** a checklist class, `undeclared-spec-edge`.

### L3 — unit 4 names a caller unit 3 moves (id 6, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md`, section 4 Evidence.
- **Wrong and consequence:** `read_worktree_trees` is said to serve `remove_unheld_rows`, which is false
  after unit 3. The return-shape constraint still holds.
- **Fix (sound):** name `remove_dead_holders` as the caller after unit 3.
- **Left shift:** a checklist class, `stale-caller-after-sibling-unit`.

### L4 — AC1's break figure is another case's (id 7, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 6 AC1 Red
  when.
- **Wrong and consequence:** 378 and about 11,500 include DISTINCT, while the staged break reverts only
  the join. The red still fires and the pinned figure cannot be reproduced.
- **Fix (sound):** re-measure the break as staged (old `VIEW_JOIN`, no DISTINCT, index present) and pin it.
- **Left shift:** a checklist class, `pinned-figure-from-another-case`.

### L5 — named-probe does not name the shared step counter (ids 8 and 11, both LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md`, section 4 The plant,
  Inventory and Reuse.
- **Wrong and consequence:** unit 1 adds `read_step_count` to the same file and unit 2 never names it, so
  a second copy of the counter can land and the two can drift.
- **Fix (sound, both):** count with `read_step_count(con, lambda: ti._write_path_rows(con, pairs, versions,
  conf))`. Add it to the Reuse seams and to the consumes-from edge. Read the "no pad" count on a second
  call. The one-step drift that remains is M2's.
- **Left shift:** a checklist class, `helper-not-named-by-sibling`.

### L6 — the generated symbol map is missing from files touched (id 15, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md`, section 4 Files
  touched; units 3 and 4, the same.
- **Wrong and consequence:** these units add functions that `memory/map/generated/symbols.json` lists, so a
  unit committed without regenerating it reds an unguarded leg.
- **Fix (sound):** add the regenerated file to Files touched of units 1, 3 and 4, and name the freshness
  leg in their section 7. Unit 2 adds no function.
- **Left shift:** the existing leg `codebase-map coverage + freshness`.

### L7 — gc's refusal leaves the conf file out (id 18, LOW)

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md`, section 2 S2;
  section 4 Mechanism 2.
- **Wrong:** S2 promises every unreadable worktree refuses, and `.memory-tree.conf` is read outside the try.
  A missing or non-file conf yields the default key. An unreadable one escapes as a traceback that names
  no worktree.
- **Consequence:** a re-parse or an untidy refusal. Rows collected are ones the worktree does not then
  read, and a non-default conf that no other worktree derives is needed.
- **Fix (the skeptic's class-level fix):** in `read_live_versions`, inside the try, refuse naming the
  worktree when the conf is not a regular file and either something stands at its path (`os.path.lexists`)
  or the HEAD tree holds `.memory-tree.conf` (`ls-tree`). Move `load_conf` inside the try and convert
  OSError and UnicodeDecodeError to the same refusal. Add a `gc-predates` step for a conf committed with a
  non-default CHARTER and deleted from disk, which refuses naming the worktree with the rows unmoved.
- **The finder's proposal, which cures the cited instance alone:** the same without the non-file case, so
  a directory at the conf path still passes.
- **Left shift:** a checklist class, `partial-refusal-of-unreadable-input`.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=18 confirmed=18 refuted=0 merged=0 unverified=0 blocker=0 high=3 medium=7 low=8 agents=11 out-tokens=108725 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=3 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 4 The plant step 4; section 6 AC3 | high | high | confirmed | Read unit 1 section 4: step 3 writes 500 rows of the reading version at a view path and nothing rolls them back; step 4 then drops the index and asks only for more than twice the count from step 1. Re-ran coherence/p.py: with 0 dead versions it printed first (319,10), after own pad with index present (10804,510), index dropped (19498,510). It then raised on its own savepoint bookkeeping (the DROP INDEX executescript), which affects only the later iterations, not this line. So the 2x condition holds with no dead row and AC3's stated red for the pad cannot occur. The pad as designed copies the fixture's own rows, so it does reach the read today; the proof of that is what is void, which makes it the narrow case. Fix: the spec's table shows the unpadded index-dropped count (467) is under twice 308 while the padded one is 8868, so reordering or removing the own rows plus the same-rows and no-pad comparisons restores the proof. | sound | - | new:proof-met-by-another-cause (PINNED, 2026-11-25) |
| 2 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md:section 4 The plant step 2; section 6 AC2 | high | high | confirmed | Re-ran coherence/q.py: 886 with both indexes, 8946 after dropping path_row_named, with no pad at all. Unit 2's step 2 and AC2 require only that the count rises, so their stated red ('the pads touch no probed path, so the count stays') is unreachable; the spec's table agrees (887 against 50164 unpadded). My own per-pad probe with path_row_named dropped: dead pad 8944 to 8920 (invisible while the version index stands), own pad 8944 to 168920, dead pad with path_row_version also dropped 1174 to 15159. So the proposed per-pad comparison, dropping the version index for the dead pad, separates both pads, and load_index rebuilds both indexes. The pads are by construction copies of the probed rows (dead) so the failure needs the pad to break: narrow path. | sound | - | new:proof-met-by-another-cause |
| 3 | coherence | memory/builds/aPrunedIndex/README.md:Expected improvements item 2, against section 6 of units 1 to 4 (unit 1 AC4, unit 3 AC4) | medium | medium | confirmed | grep for 420 and ceiling over the four specs printed unit 1 lines 100, 192, 263 and unit 3 line 126, none in a criterion. README promises 'The leg fits its ceiling on the index as it stands' and the brief's Goal says it reliably fits 420 s. Unit 1 AC4 reds on output bytes only and uses built trees; unit 3 AC4 bounds only sweep seconds, unit 2 AC5 only the probe pass. So no criterion observes the end-to-end wall on the 12.6 GB file. The sub-claim that reads may not get faster is overstated, since the step-count AC1 and the EXPLAIN in AC5 bound the reads, but the headline gap stands. The proposed measurement is feasible on a private copy: the diagnosis did it at 122.1 s wall on an unbuilt tree, and 117.0 to 28.5 CPU s on a built 12-dead-version copy, so both criteria discriminate. Contained: the prototype measured the outcome already. | sound | - | new:goal-without-criterion (PINNED, 2026-11-25) |
| 4 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md:section 2 S4 and section 6 AC6, help/tags.md half | low | low | confirmed | Read unit 1 S6 and AC6 and unit 2 S4 and AC6: same sentence, same `grep -n "SQL index" help/tags.md`. The grep prints nothing today, and unit 1 (order 1) adds the sentence, so unit 2's half is green before unit 2 is built; S4 itself says 'Where unit 1 already wrote that sentence, this unit adds none'. Files touched still lists help/tags.md for unit 2. Consequence is redundant text only. Dropping it from unit 2 removes every duplicate instance, and unit 2 consumes unit 1, so the sentence is always present. | sound | - | new:criterion-green-before-unit |
| 5 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 3 Edges, against section 6 AC5 and section 4 The plans | low | low | confirmed | Read unit 3: its Edges section holds one bullet, 'hands-off external'. Yet AC5's fixture is 'opened through this code so units 1 and 2 are on it', and The plans were read 'with the SQL indexes of units 1 and 2 added'. Unit 1's Edges names unit 2 and external only, and unit 2's names unit 1 and external only. TEMPLATE-SPEC says order is not an edge and edges cover a criterion resting on something the unit does not build. No behaviour changes, so low. The fix cures it: the edge is declared, the Tier-2 reciprocal is added, and the Tier-1 side is outside the join. | sound | - | new:undeclared-spec-edge |
| 6 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md:section 4 Evidence | low | low | confirmed | Unit 4 section 4 says 'read_worktree_trees also serves remove_unheld_rows and read_index_rows'. That holds at BASE: grep shows calls at tools/playbook/tag_index.py@4b10fce5:829, 890 and 1501. Unit 3 (order 3) makes it remove_unheld_rows(con) running only the three sweep statements, and moves the worktree read to remove_dead_holders. So the caller list is stale when unit 4 (order 4) is built. The return-shape conclusion still holds, so low. Naming remove_dead_holders cures the only stale sentence; unit 4's non-goal on remove_unheld_rows remains true. | sound | - | new:stale-caller-after-sibling-unit |
| 7 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 6 AC1 Red when | low | low | confirmed | Unit 1's plant table gives 'today' as 378, 11538, which is the code with DISTINCT, and this unit as 308, 309. AC1's break reverts only VIEW_JOIN while S4 has dropped DISTINCT. I ran an in-memory probe of the old join with path_row_version present, 15 rows and 40 dead versions on SQLite 3.53.4. With DISTINCT it took 514 then 10704 steps (SCAN p USING INDEX path_row_tag). Without it, 421 then 9412 (SCAN p). So DISTINCT changes both the baseline and the plan, and the pinned pair is not the staged break's. The red still fires and the plant derives its own counts, so only a pinned figure is wrong. Re-measuring the break as staged cures it. The other break figures match their own rows (no index 8868; one join 146 to 3646). | sound | - | new:pinned-figure-from-another-case (PINNED, 2026-11-25) |
| 8 | coherence | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md:section 4 The plant | low | low | confirmed | Unit 1 S5 adds read_step_count(con, read) to gov_tag.py, counting through set_progress_handler at one instruction. Unit 2's plant describes the same count of one _write_path_rows call over the same API in the same file, and neither its plant, Inventory nor Reuse names the helper. Unit 2 is order 2, so the helper exists by then. The call fits read_step_count's shape as a lambda. Unit 3 section 10 explains its own non-reuse. The effect is a possible duplicate counter in a plant, with no change in behaviour. The fix covers the only unexplained instance. | sound | - | new:helper-not-named-by-sibling |
| 9 | grounding | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md:section 4 The plant, item 1; section 5 AC1 | medium | medium | confirmed | I re-ran it in memory on SQLite 3.53.4, with BASE SCHEMA, both new indexes and the repository's own _write_path_rows. Counts on one connection for (no pad, dead pad, both pads, index dropped): 5 pairs [151,104,105,2766], 6 pairs [172,125,126,3944], 40 pairs [886,839,840,168946]. With an uncounted warm-up call, 40 pairs still gave [839,839,840]. Section 4 item 1 and AC1 require the three counts to be equal, so the plant exits 1 on correct code. It fails loudly and is contained to the plant. The fix cures both effects: the warm-up removes the compile cost and the bound absorbs the one-step drift. The dropped-index count is over 20 times higher, so 'exceed twice' stays discriminating. | sound | - | new:count-includes-setup-cost |
| 10 | grounding | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 4 The plant, item 3; section 6 AC2 | medium | medium | confirmed | I ran scratch spec1_plant.py in mode new as it stands: 'new point 77 820 820'. With only its earlier p0=steps(P) call removed, which is the order the spec gives, it printed 'new point 0 837 820'. The pinned 820/820 comes from a pre-warmed statement. The LIKE read printed 324 then 301, and the population read 282 then 176, so first counts include compile steps. Section 4 step 3 and AC2 demand equal counts and nothing warms the statement, so the plant reds on correct code. An uncounted first run inside read_step_count cures it, because the later executions of that statement are equal. | sound | - | new:count-includes-setup-cost |
| 11 | reuse | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md:section 4 The plant, Inventory and Reuse | medium | low | confirmed | I read unit 2 whole. It says the plant counts steps 'with set_progress_handler at one instruction', states 'No function is added', and its Reuse names SCHEMA, _write_parsed and the runner. It never names read_step_count, although unit 1 (order 1, declared consumes-from) adds that helper to the same gov_tag.py with a signature that wraps a _write_path_rows call. Unit 3 explains why it does not use the helper; unit 2 does not. The consequence is duplicated test code with no effect on behaviour. The fix uses the helper and names the seam and the edge. The warm second call fits; the remaining one-step drift is id 9's matter. | sound | - | new:helper-not-named-by-sibling |
| 12 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md:section 7 New arm line and section 6 AC1 cost (also the New arm lines of units 1, 2 and 3) | high | medium | confirmed | The ceiling of `playbook render selftest` in tools/gate-legs.json is 300, its selftest-budgets.txt row is 60 ('worst of 8 readings 10s'), and the ceiling-evidence row is 1.5 s. The only retained log is dated Sep 9 with 8 arms. The tags plant table has 95 rows, run one after another by run_plant_rows. I timed nine plants: none 6.4, rebuild 3.8, retired-old 5.4, bad-ns 5.1, owned 4.6, scope 6.8, bare 3.9, slice 2.1, dirty 2.5 s. The mean is about 4.5 s, so the 95 rows take about 430 s, past both figures, before the edge and load-set rows. I did not run the leg itself, so the total is an extrapolation. A grep of the specs finds neither the ceiling nor the budget for this leg. Each spec homes its new arm there. The overrun predates the build, a killed leg reds rather than passing, and the acceptance criteria run the plants directly, so the effect is contained: medium. Measuring the leg, stating the added cost, and rehoming or collapsing with a criterion that the leg finishes under its ceiling covers all four units. | sound | - | gate:leg ceilings clear their evidenced maximum (PINNED, 2026-11-25) |
| 13 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 4 Migration and section 5 risks (and unit 2 section 4 Migration) | high | medium | confirmed | Re-read: load_index runs con.executescript(SCHEMA) at every open, and edge_grammar.read_tag_rows calls it under the `edges` leg, ceiling 180 in gate-legs.json. Spec 1 Migration and Unit 2 Migration give 205 s; section 5 itself says a 180 s leg would time out, with only 'the owner is asked before it runs'. A grep of the build's records found 'once per node' in the dinosis only and no pre-build step or other-node rollout. The effect is contained: it needs a large file on another node, and a 420 s leg can finish the build or each CREATE INDEX commits alone, so it self-heals. Hence medium. The proposed rollout step works: `gov_tag.py where` runs load_index outside any leg. | sound | - | new:migration-under-a-leg-ceiling (PINNED, 2026-11-25) |
| 14 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 3 (no live index open; 'a tree holding this unit alone opens no shared index') against section 7 | medium | medium | confirmed | My probe replaced tag_index.load_index with a raiser and called load_resolver(): it reached the live worktree root. arm_statements calls load_resolver() first, and the selftest-budgets row records a lock on the shared index. gov_tag.run_kit_verb, instructions_edit's check and edge_grammar.read_tag_rows also open the repository's index. Units 1 to 4 list such legs in section 7 while section 3 (or the edge) forbids the open before the owner's word, and nothing says which legs open it; `instruction units selftest` is in no section 7. The owner's go is stated as a precondition, but the hazard of running a listed leg is not. I checked whether other legs open it: run_grammar returned 0 without reaching load_index, and no overlay `floor=` row exists, so the finding's list holds today. | sound | - | new:listed-leg-breaks-a-non-goal |
| 15 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 4 Files touched (also units 3 and 4) | low | low | confirmed | git grep shows symbols.json lines 3881, 23226, 25071 and 29501 list build_overlay, read_defined, read_live_versions and remove_unheld_rows from tag_index.py. test_codebase_map.py CONDITIONAL_TIERS compares symbols.json, and that leg has no guard. Units 1, 3 and 4 add functions per their inventories and their Files touched omit the file, as does their section 7 the leg. Unit 2 adds no function, and the entries hold id, kind and file with no line number, so excluding it is right. | sound | - | gate:codebase-map coverage + freshness |
| 16 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md:section 2 S4; section 4 What it cannot see, second bullet | high | high | confirmed | I re-ran it on the module's own SCHEMA and read_rows with two connections: connection A read ('bad.cite','p',3,'span'); connection B ran the spec's release statements for (p,b1) after dirty_path moved to (p,b2), and A's next read returned []. run_check makes many autocommit reads with no transaction, and edges and other legs call load_view on the same worktree. At BASE build_overlay sweeps nothing, so the row stays until some build. The spec's 'What it cannot see' discloses the window but leaves it unhandled and untested, and it contradicts 'No row any worktree is served changes'; its commit comparison does not cover edits. A false green on a narrow race is high. The fix covers the edit case. It leaves the same window the spec names for a commit's build sweep, its defer option needs stored pairs that section 3 rules out, and its detection watches dirty_path alone. | instance | - | new:release-under-a-live-reader |
| 17 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md:section 4 Migration; section 5 risks and error states (same in unit 2 section 4 Migration) | high | medium | confirmed | Observed: load_index runs executescript(SCHEMA) at every open and prints nothing about it. Both Migration sections price only a waiting opener. I re-ran a killed-opener probe in scratch: the child was killed at 25% of full time during the first CREATE INDEX, and after reopening no index was present, so the work is discarded. One nuance: the two CREATE statements autocommit separately, so a kill in the second keeps the first; progress is lost per index, not per pair. Ceilings in gate-legs.json: instruction units and instruction grammar 120 (instruction_units.load_resolver opens the live index), edges 180, writing practice 180, tags 420. Unit 1's risk line names only 180/420. It does say a leg meeting the build would time out and that the owner is asked first, and the owner's word is an edge. It names no ceiling-free build step and no killed-mid-build case, and covers no other node or adopter. The effect is timeouts or wasted work with no wrong rows or verdicts, and the owner-ordered open or the 420 s leg can complete the build, so it is contained. Fix: a ceiling-free first open through load_index, named in help and rollout with a stderr line, plus the stated kill case, cures the class the claim names. | sound | - | new:migration-under-a-leg-ceiling (PINNED, 2026-11-25) |
| 18 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md:section 2 S2; section 4 Mechanism 2 | medium | low | confirmed | Observed: in read_live_versions, load_conf runs after the try/except TagError. load_conf returns {} when the path is not a file; I ran it on a missing path and on a directory and got {} {}. Its read_text is unguarded, so a decode or OS error escapes untyped. remove_dead_versions then deletes path_row for confs outside `keys` and tree_built for digests outside the set. Unit 4 S2 says every worktree that cannot be read refuses, naming it, and lists only registry, module and HEAD; Mechanism 2 leaves the conf read outside the try. Consequence is smaller than claimed: a worktree whose conf is absent itself derives the default key when it reads or builds, so the collected rows are ones it does not currently read, and restoring the conf re-parses. It also needs a non-default MEMORY_ROOT/CHARTER that no other worktree derives; this repo's conf is the default. The traceback happens before any deletion. Only a re-parse or an untidy refusal results. The proposed fix tests 'working tree lacks' and raised errors, but a directory at the conf path neither is lacking nor raises (load_conf returned {}), so the claim's non-file instance stands. | instance | - | new:partial-refusal-of-unreadable-input |
