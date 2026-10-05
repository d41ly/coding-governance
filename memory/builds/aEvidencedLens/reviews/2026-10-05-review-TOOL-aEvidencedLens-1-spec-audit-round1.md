**Serves:** spec-audit TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11

# aEvidencedLens — spec audit of the eleven-unit set, round 1

*Node `a`, 2026-10-05. A Tier-2 adversarial pass over the eleven specs the harness's spec stage
authored at 4d0d64688: four finder lenses, a skeptic stage prompted to refute each finding, and one
synthesis. Findings are graded by consequence under the run's severity rubric.*

**Round: 1.** Range reviewed: the eleven subjects below, each pinned at the blob it was read at, plus the tree they cite.

- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md@de140c3ea4acd5571eb7ee42f9cf4ebbb669e34c`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md@1ea5a3a513b452f2072c8ab8825d2ba371e8c87e`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md@075af74ddcb7603efee1e08d2eb2cbb5955616f9`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md@099033058fe14bfe3407d038ddd4efaf0af34895`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md@3f4fafd20ffdec3b119b9f4ab319f51e654717e0`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md@88b6a0f1477ab70a89d33b09b05cf89c824a9b66`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md@6d1c0773338495d741eccfa96cb18b2573507948`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md@7d4dce07d8899d54bfff2a1e1515aa297b090950`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md@9e4e4704eaa6dd5ea1795bcce1019ac1ea03e28a`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md@629cc42227ce6bb803160f25f74a9ce1fc3db2c4`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md@69275b8ac283e870a83a368db20a8222fa0263fc`

## Verdict: CLEAN WITH FIXES

No blocker was confirmed. Three highs were confirmed, and each one must be fixed in its spec before
that unit is built. Unit 6's AC7 compares against an unbound base that cannot pass on a correct
build. Unit 3 folds skeptic evidence through a renderer that escapes pipes. Unit 9's round scan
would red forever on an archived record. Below those sit twenty-six mediums and seventeen lows.

The dominant defect class is an acceptance gap. Twenty-four of the forty-six confirmed findings are
a §2 item that says "Observed by ACn" while ACn observes less than the item promises. The usual
forms are a grep alternation that misses the stale sentence, a single case where the item names
several, or a promised regression arm with no floor move. None of these ships a wrong result by
itself, but each lets a partial build pass its own Definition of Done.

## Review shape

- Intensity full. Raw 49, confirmed 46, refuted 3, unverified 0 (0 uncertain). Precision 0.94.
- Adjudicated tally by item: 0 BLOCKER, 3 HIGH, 11 MEDIUM, 9 LOW, which is 23 items.
- Adjudicated tally by raw confirmed finding: 0 blockers, 3 highs, 26 mediums, 17 lows, which is 46.
- Refuted and dropped: ids 15, 26 and 42. Their reasons are in the appendix.

## Run integrity

- Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 42 judged sound, 4 judged UNSOUND (ids 6, 14, 16 and 18), 0 none
  proposed, 0 NOT JUDGED. For each unsound fix, this report carries the skeptic's corrected fix only.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 8 RE-GRADED by the skeptic (ids 1, 2,
  6, 13, 16, 30, 38 and 45). The bracketed grade is binding and is the grade used below.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: NEITHER `specs` nor `context` was supplied to this run. The lenses did not read the build
  mandate or the sibling-spec list as declared inputs, so a finding that depends on the mandate's
  intent may be missing.
- Checklist: NONE swept, because no checklist was supplied. A zero count for any of this project's
  recurring bug classes is not evidence that the class is absent.

Every counter that this run must report as zero is zero, so the run is complete in the sense the
harness defines. The two declared absences above still limit what the finding set can prove.

One duplicate the run did not catch: ids 1 and 25 are the same defect in unit 6 AC7, found by two
lenses. Their binding grades differ (1 medium, 25 high), so they sit in separate items. One fix
discharges both. Under the rubric the high is the right grade, because a builder chasing the red
may revert unit 1's shape bump, which misleads the next change.

## HIGH

### H1 — unit 6 AC7 compares against an unbound base (id 25)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md`, section 6 AC7.
- Defect: AC7's fixture is `git show <base>:tools/workflows/tier2-review.js`, "at the pass's base",
  which no document defines. The unit's header pins base 028b5cac, and that base predates unit 1's
  REVIEW_SHAPE bump. The bump moves the review key and every DURABILITY line in the find: and
  verify: prompts, so AC7 is red on a correct build.
- Fix (judged sound): make the fixture the pass-start render, the `git show` of
  `tools/workflows/tier2-review.js` at HEAD before the pass's first edit, as units 1 to 4 word it.
  State that the comparison is not to BASE because unit 1 moved the key.
- Left-shift: a spec-lint rule that refuses an acceptance criterion carrying `git show <base>` or
  any unbound `<base>` placeholder. Every comparison fixture must name `BASE`, a sha, or "HEAD
  before the pass's first edit".

### H2 — unit 3 folds evidence through renderCell, which escapes pipes (id 36)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md`, section 2 S3
  and the section 4 Evidence bullet on renderCell.
- Defect: renderCell (`tools/workflows/tier2-review.template.js:1061-1063`) folds line breaks and
  also rewrites every `|` to `\|`. The skeptic is told to re-run the evidence command. A command
  such as `git ls-files | grep x` reaches it escaped, prints something else, and a true finding is
  refuted under refutation case (3). AC2's fixture has no pipe, so it cannot observe this.
- Fix (judged sound): fold evidence with a line-break-only fold, either renderCell's first replace
  factored out or a sibling one-liner. Never escape pipes in a prompt line. Add a pipe-bearing
  evidence case to AC2 asserting the `|` survives unescaped.
- Left-shift: a `tier2-review.test.sh` arm feeding a finding whose evidence contains `|` and
  asserting the verify: prompt carries it byte-for-byte.

### H3 — unit 9's round scan reds forever on a terminal record (id 37)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md`, section 2 S3.
- Defect: in check 19, the terminal walk through read_run_exclusions runs only under
  `if [ -n "$maywr" ] && [ "$maywalk" = 1 ]`, that is, only on a grant hit. S3 re-scans rounds
  "exactly when the grant scan does". With no grant hit, the round scan grades the unwalked
  base..witness superset, which holds every default-branch commit since BASE. An owner raise of
  REVIEW_ROUNDS on main, merged into the run before its witness, then fails 19 on an archived
  record on every later bar. AC3 tests the owner raise only on a live record.
- Fix (judged sound): walk when EITHER scan hits on the superset, by testing
  `[ -n "$maywr$rndwr" ]`, and re-run both scans over the walked list. Add an arm with a terminal
  record whose base..witness range contains an owner raise merged into the run branch, expecting
  no fail 19.
- Left-shift: that arm is the gate. Add also a checklist entry: a new scan sharing an existing
  scan's walk must share its walk TRIGGER, not only its walk.

## MEDIUM

### M1 — unit 6: the base binding and the all-dead exit (ids 1, 11)

- Where: `...-6.md` section 6 AC7 (id 1); section 2 S5 with section 6 AC4 and AC5 (id 11).
- Id 1 is the same defect as H1, found by a second lens at a medium binding grade. Fix (judged
  sound): bind the fixture to the pass-start sha as units 3 and 4 do, and state why BASE is
  excluded. One edit discharges both ids.
- Id 11: no criterion exercises the every-lens-dead early exit at template :821-833, so a build that
  leaves `lensYield` off that return passes, and a caller crashes on the most degraded run. Fix
  (judged sound): add an AC5 case where every lens double returns null, and assert the return
  carries `lensYield` with one row per running lens, each `returned: false` with zero counts.
- Left-shift: the H1 lint rule, plus a `tier2-review.test.sh` arm iterating every return site and
  asserting each one carries the declared return fields.

### M2 — unit 4: the spec probe's `blobs` is never observed (ids 2, 3)

- Where: `...-4.md` section 2 S4 (and section 8 F2) with section 6 AC4.
- Id 2: no criterion reads the spec-kind `resume:probe` prompt or its schema, so a build that never
  asks for `hash-object` or never admits `blobs` passes, and every subject reads unchecked forever.
  Fix (judged sound): add to AC4 that the traced `resume:probe` prompt carries `hash-object` and
  each subject path, and that the probe schema lists `blobs` among its properties and not in
  `required`.
- Id 3: no case covers a live probe returning a valid object with no `blobs` key. A natural
  `(probe.blobs || [])` reads that as zero moves, the silent zero S4 forbids. Fix (judged sound):
  add an AC4 case where the stub returns a valid object with no `blobs`, and RUN INTEGRITY names
  every subject as unchecked without saying the resume probe died.
- Left-shift: a test-harness rule that every optional field a spec's §2 makes load-bearing has an
  "absent key" arm beside its "null" arm.

### M3 — unit 1: the promised arms and floor move are unobserved (id 5)

- Where: `...-1.md` section 2 S6 with section 6 AC8.
- Defect: S6 raises FLOOR_ASSERTIONS by the arms added, "Observed by AC8", but AC8 observes only
  retired-key greps and two stub `raw` counts. A build adding no arm passes.
- Fix (judged sound): add the AC6 shape units 3 and 4 use, a named-arm grep count rising over the
  pre-pass file and FLOOR_ASSERTIONS equal to its pre-pass value plus the assertions added. Write
  both figures in the commit message.
- Left-shift: see the class gate under "Left-shift summary" below.

### M4 — unit 2: refusal arms, path folding, and a criterion unit 3 makes red (ids 7, 8, 27)

- Where: `...-2.md` section 2 S7 with AC8 (id 7); section 2 S4 with AC3 (id 8); section 6 AC1
  against unit 3 S5 and AC3 (id 27).
- Id 7: AC8 greps only `scratch` literals and checks MT_ARGS does not throw, so the refusals can
  ship with no arm and an unmoved floor. Fix (judged sound): add a criterion counting the new refusal
  arms against the pre-pass file and checking FLOOR_ASSERTIONS equals its pre-pass value plus the
  assertions added.
- Id 8: AC3 tests only exact-case POSIX pairs. A naive `startsWith(repo)` refuses the sibling
  `/tmp/rs`, and a missing case fold admits `C:/R/x` under `c:/r`. Fix (judged sound): extend AC3 so
  that `/tmp/rs` proceeds, `C:\\R\\x` beside repo `c:/r` throws, and `/tmp/r/` beside `/tmp/r`
  throws. Also assert a run handed `C:\\t\\s` carries `C:/t/s` in its PROBE POLICY line.
- Id 27: AC1 asserts no verify: prompt carries PROBE POLICY on the live render, and unit 3,
  ordered after it, puts that block into every spec-kind verify prompt. Fix (judged sound): reword
  AC1 to say no synth prompt carries the block and the verify: prompt is unit 3's, or mark the
  verify clause as observed at unit 2's pass only and superseded by TOOL-aEvidencedLens-3 S5.
- Left-shift: a build-set lint that, for each AC asserting an absence on a live file, checks no
  later-ordered sibling's §2 adds that text to that file.

### M5 — unit 3: kind scoping and the timed-out probe (ids 9, 10, 31)

- Where: `...-3.md` section 2 S6 with AC4 and AC5 (id 9); section 2 S3 with AC1 and AC2 (id 10);
  section 4 "The sentence" against section 3's retained default (id 31).
- Id 9: nothing observes that the orphaned-duplicate demotion stays off the diff kind. Fix (judged
  sound): add to AC5 a diff-kind run whose skeptic stubs refute id 2 as `duplicate of id=1` beside a
  refuted id 1, with the ledger and the return identical between `pre-u3.js` and the new render, and
  no orphan WARNING logged.
- Id 10: the rule that an unrunnable probe falls to the grade default is in no criterion's marker
  list. Fix (judged sound): add to AC1's markers `could not run inside its bound` and
  `not a refutation`.
- Id 31: the skeptic-facing sentence says an unrunnable probe is "not a refutation", while the
  retained default refutes an unestablished medium or low. Fix (judged sound): word it as "A probe
  you could not run inside its bound is a finding you cannot establish; apply the default by the
  finder's grade, and never call it evidence that does not reproduce."
- Note: the id 10 fix's marker `not a refutation` must follow the id 31 rewording. Pick the marker
  from the final sentence, for example `apply the default by the finder's grade`.
- Left-shift: an invariant-2 arm that runs every kind-scoped behaviour once on the other kind and
  asserts byte-identical verdicts and ledger.

### M6 — unit 8: the disposal prompt clauses and the promotion cascade (ids 14, 45)

- Where: `...-8.md` section 2 S1 with AC1 (id 14); section 5 perf/scale, section 3 and section 10
  (id 45).
- Id 14: AC1 checks three markers, so the closes-verb ban, the per-batch `repairs` rule, report-id
  naming and `folded` as 0 can all be dropped. The finder's fix was judged UNSOUND. Skeptic's
  corrected fix: pin exact new sentences in S1, for example "never through the `closes` verb",
  "`repairs` names the one unit every minor in the batch lands on, or `none`", "names every finding
  by report id in its §1" and "return `folded` as 0". Then have AC1 assert each of those phrases,
  each absent from the base prompt.
- Id 45: section 5 calls the promotion chain bounded and cites TOOL-aWokenSentinel-30, which is
  still OPEN and measured the cascade not converging. Unit 8 makes nearly every round promote a
  batch unit, and unit 3 confirms at any severity, which raises the precision M4's chain bound
  needs to fall. Fix (judged sound): cite TOOL-aWokenSentinel-30 as open and TOOL-dLoggedFlight-34
  with TOOL-dGatedProse-4 as the governing ruling, and state the interaction. Then either (a) close
  a spec-audit minors batch unit under M4's recorded specs-audited override rather than auditing it
  as a fresh subject, or (b) park the generation bound as a fork for the owner. In unit 3 section 5,
  add that confirming at any severity raises the precision M4's chain bound reads, and have unit 11
  S1 keep the chain sentence consistent with the chosen option.
- Decision needed: option (a) or (b) above is an owner call, because it sets how many audit
  generations a build may spend.
- Left-shift: a spec-lint that refuses a citation of an OPEN ask as the record that "measured" or
  "bounded" something, using the `gen_build_index --asks` status.

### M7 — unit 9: the default read, the terminal path, the working copy and the ruling's record (ids 17, 18, 41, 47)

- Where: `...-9.md` section 2 S1 with AC1 (id 17); section 2 S3 with AC3 (id 18); section 2 S4 and
  the section 4 Evidence bullet (id 41); section 5 user docs, with unit 11 S5 and AC5 (id 47).
- Id 17: AC1 expects `rounds=1`, which a hard-coded 1 also prints. Fix (judged sound): point DRIVER
  at a scratch driver whose `REVIEW_ROUNDS_DEFAULT=3`, and expect `rounds=3` for the blob with no
  assignment.
- Id 18: no criterion runs the round scan on a terminal record or after exclusions. The finder's
  fix was judged UNSOUND. Skeptic's corrected fix: add an AC3 case where a terminal run-state file
  whose base..witness range holds a run commit raising the bound fails check 19 naming `1 -> 2`.
  For the excluded-commit case, first amend S3 so the exclusion walk runs on a terminal record
  whenever EITHER scan has a hit, which is H3's fix. Then assert the same raise, in a commit
  read_run_exclusions removes, is not named.
- Id 41: the driver sources the working-copy conf, so a run can raise its own REVIEW_ROUNDS
  uncommitted and leave check 19 nothing to see. S4's does-NOT-check list omits this. Fix (judged
  sound): name "an uncommitted working-copy edit the driver sources for the current run" in S4's
  does-NOT-check header, or have the driver read REVIEW_ROUNDS from the conf blob at the pinned BASE
  as it does for LANDING_NODES, adding it to scope with an AC. The skeptic notes the second option
  conflicts with section 3's non-goal, so the first is the in-scope choice.
- Id 47: no decision record holds the ruling that agents never change REVIEW_ROUNDS, and unit 9's
  hand-off to unit 11 for the protocol row lands on no owner. Fix (judged sound): either widen unit
  11 so S5 records both 2026-10-05 rulings, with AC5 allowing the extra line, and add the
  `tools/unattended/PROTOCOL.template.md` REVIEW_ROUNDS row and its render to unit 11's files. Or
  drop the hand-off sentence in unit 9 section 5, and have check 19's message and header cite the
  run mandate prompt record as provenance.
- Left-shift: an AC-lint that flags an expected value equal to the current kit default with no
  override in the fixture; and a build-set check that every "is TOOL-…'s" hand-off names a file in
  that unit's declared scope.

### M8 — unit 10: arm count and the pin line (ids 20, 28)

- Where: `...-10.md` section 2 S7 with AC1 (id 20); section 2 S5 with AC6 against S1 (id 28).
- Id 20: S7 promises six arms, and AC1 is satisfied by one. Fix (judged sound): AC1 reads K is at
  least 25 (19 + 6), and the closing output names an arm for each of no-appendix, section-ref,
  window-0, kind-mismatch, subject-pins and per-lens-known.
- Id 28: S5 reads pins from "the record's opening line", which in every real record is the
  `**Serves:**` binding line, and AC6's fixture opens with pins, so S1 would not detect it as spec
  mode. Fix (judged sound): S5 reads the pins from the first line after the binding line that
  carries `<path>@<hex>` pairs, and AC6's fixture opens with `**Serves:** spec-audit` and then the
  pin line.
- Left-shift: build AC fixtures from a real record emitted by the harness (this one, for example),
  not a hand-typed opening.

### M9 — unit 11: unobserved bullets and a counts contradiction (ids 22, 23, 29)

- Where: `...-11.md` section 2 S1 with AC1 and AC2 (id 22); section 2 S3 and S4 with AC4 and AC6
  (id 23); section 2 S3's counts paragraph against unit 8 S5 and S6 (id 29).
- Id 22: the read-only probe sentence, the fold-then-STOP rewrite and M2's "a review's minors
  batch" are unobserved. Fix (judged sound): add greps to AC2 so that the method carries
  `read-only` beside `scratch` in M4, the fold-then-STOP sentence carries the "not an exit" wording,
  M2 says `a review's minors batch`, and `the closing review's minors batch` prints 0.
- Id 23: three stale carriers match neither alternation, namely the Skill's "refused on any other
  round or subject", the CONVERGING bullet, and the verbs entry's "reaches only at `CONVERGED`".
  Fix (judged sound): add `refused on any other round or subject` and `reaches only at .CONVERGED.`
  to AC4's alternation, and assert the CONVERGING bullet names the spec subject's fold.
- Id 29: the Skill tells an operator spec counts take "no summing", while unit 8 adds every
  promoted UNVERIFIED finding to `--minors`. Fix (judged sound): in the S3 counts sentence, add
  "plus every UNVERIFIED finding the disposal promoted" to the minors term.
- Left-shift: see the class gate below; and a carrier-parity check that greps every carrier of the
  disposition rule for the old phrasings the build retires.

### M10 — unit 5: inputs the callee would refuse (ids 38, 39, 40)

- Where: `...-5.md` section 2 S2 (id 38); section 2 S3 and the gotchas.py Evidence bullet (id 39);
  section 2 S4 (id 40).
- Id 38: an empty `units[].specPath`, which the harness carries for every freshly authored unit,
  enters `specs` and kills the Audit stage. Fix (judged sound): build `specs` only from units whose
  specPath is a non-empty string, filtered before the subject exclusion. Add an AC whose UNITS
  fixture carries an empty specPath and asserts it is absent from `specs` and the audit proceeds.
- Id 39: `gotchas.py --for-paths` exits 0 with no `- ` line when nothing is selected, and
  parseChecklist throws on that. Fix (judged sound): treat stdout with no line starting `- ` as
  `checklistError` ("no bug class selected"), announce it with the S8 WARNING and omit `checklist`.
  Add an AC whose audit:subjects double returns a header-only checklist.
- Id 40: the build harness validates `scratch` by shape only, so a scratch under the repo passes it
  and dies late in the callee. Fix (judged sound): apply unit 2's two extra refusals in the build
  harness's own `scratch` validation, or validate against the callee's rule before the Audit stage
  and throw `unattended-build: ...` naming the field.
- Left-shift: a contract arm that feeds every value the caller's prelude accepts through the
  callee's prelude, so a caller cannot accept what its callee refuses.

### M11 — unit 7: the new rule has no ratchet on history (id 46)

- Where: `...-7.md` section 2 S8 and section 3 "A cutoff for old rows".
- Defect: check 2 grades `fold` only on a counted row or beside a non-zero blocker count
  (`check-unattended.sh:779-780`), so a countless spec row recording fold still passes the bar
  after this build. The repo's FOLD_CUTOFF precedent says a ratchet grading history needs one cutoff
  per rule, and a cutoff grades only new rows, so the non-goal does not cover this.
- Fix (judged sound): add a kit cutoff constant beside FOLD_CUTOFF, using the same "strictly past
  the newest record any branch can still write under the old contract" idiom. Have check 2 refuse,
  on a row first-committed on or after it, a terminal spec-subject row that carries no counts or
  records `fold`. Put this in unit 9, which holds `check-unattended.sh` this order, with a
  consumes-from edge to unit 7, or make it a declared hands-off from unit 7. Replace the "no
  cutoff" non-goal with that edge.
- Left-shift: a checklist entry that a write-time refusal added to a verb owes a dated check-2
  cutoff, citing FOLD_CUTOFF.

## LOW

### L1 — unit 4: wording, a count and the moved-text read (ids 4, 44)

- Id 4 (`...-4.md` S3, S6): the `none supplied for this round-<n> review` line and the prevBlob
  count are in no criterion. Fix (judged sound): in AC3 assert the round-2 `find:` prompt carries
  `none supplied for this round-2 review`; in AC2 assert the synth RUN INTEGRITY block names `2 of 3`
  subjects carrying prevBlob, or the chosen wording.
- Id 44 (`...-4.md` S5): `git -C <repo> cat-file -p <blob> | diff -u - <path>` assumes the cwd is
  `repo` and matching line endings. Fix (judged sound): spell the read as
  `git -C <repo> diff <blob> -- <path>`.
- Left-shift: a lint that any shell recipe giving `git -C` gives every other path in the pipeline an
  anchor too.

### L2 — unit 1: AC8's regex and an uncited open ask (ids 6, 48)

- Id 6 (`...-1.md` AC8): the quoted `'prior-art'` alternative cannot see
  `scanSpawned('find:prior-art')` at `tools/workflows/tier2-review.test.sh:336`. The finder's fix
  was judged UNSOUND. Skeptic's corrected fix: add `find:prior-art` as an explicit alternative,
  `grep -c -E "underspecification|unstated-assumption|'prior-art'|find:prior-art"`.
- Id 48 (`...-1.md` section 10): the reuse audit names neither TOOL-dUnstalledConvoy-16 nor
  dTieredTribunal's parked P3. Fix (judged sound): name both, and state that this unit closes that
  instance by removing the second carrier rather than by P3's parity leg, so the ask's instance
  list can be updated at the close.
- Left-shift: run every retired-key grep in an AC over the current tree before freezing the spec,
  printing hits and near-misses.

### L3 — unit 6: README sentence, floor, count word and attribution (ids 12, 30, 35, 49)

- Id 12 (S9, AC8): "Every return carries three fields" can survive. Fix (judged sound): add
  `grep -c 'carries three fields' tools/workflows/README.md` prints 0.
- Id 30 (section 7, also units 5 and 8 section 7, and unit 1 S6): units declare floor "none" or
  "by arms" where siblings raise the same file's floor by assertions. Fix (judged sound): units 5,
  6 and 8 raise their suite's FLOOR_ASSERTIONS by the assertions their arms add; unit 1 S6 and
  section 7 say "assertions added", as units 3 and 4 do.
- Id 35 (S6): "the four counts" names six. Fix (judged sound): say "the counts known before the
  synthesis, raw to precision, with returned".
- Id 49 (section 10): the counters precedent is TOOL-aWeldedTribunal-4, not the open
  TOOL-dTieredTribunal-16. Fix (judged sound): cite TOOL-aWeldedTribunal-4 as the built precedent
  and mention TOOL-dTieredTribunal-16 only as the ask it answered.
- Left-shift: a build-set lint that every `New arm:` line in §7 naming a file that keeps
  FLOOR_ASSERTIONS declares a floor move other than "none".

### L4 — unit 7: two stale fold comments (id 13)

- Where: `...-7.md` S6 with AC7. `tools/unattended/unattended.sh:10059` and `:10185` contradict S3
  and match neither alternation.
- Fix (judged sound): add `reachable from ONE exit, CONVERGED` and `ACCEPTED there and never
  required` to AC7's alternation, or state the regex is a floor and list these two anchors.
- Left-shift: the class gate below.

### L5 — unit 8: the reconciliation comment (id 16)

- Where: `...-8.md` S8 with AC9, against `unattended-build.template.js:1268-1275`.
- The finder's fix was judged UNSOUND. Skeptic's corrected fix: add `AT LEAST the confirmed rest`
  and `folded or named standing` to AC9's alternation.
- Left-shift: the class gate below.

### L6 — unit 9: check 2's other message and comment (id 19)

- Where: `...-9.md` S5 with AC5. The `:794` message and the `:728` comment are unobserved.
- Fix (judged sound): add `grep -c 'closing-review subject(s)'` prints 0 and
  `grep -c 'build-slug subject terminal round only'` prints 0.
- Left-shift: the class gate below.

### L7 — unit 10: kind-mismatch one direction only (id 21)

- Where: `...-10.md` S4 with AC5.
- Fix (judged sound): add an AC5 case of a diff-review known record against a
  `**Serves:** spec-audit` candidate exiting 2 with kind-mismatch, and an unbound candidate scored
  by section beside a spec known record.
- Left-shift: a checklist entry that a symmetric refusal owes one case per direction.

### L8 — unit 5: warnings, header lines and wording (ids 24, 32, 33, 43)

- Id 24 (S8, S9, AC5, AC8): the one-arg-missing warning, the meta Audit detail and the
  `priorFindings` header line are unobserved. Fix (judged sound): add an AC5 case with
  `prevSubjects` given and `priorFindings` absent, logging a WARNING naming `priorFindings`. Extend
  AC8 with `grep -n priorFindings` in the header block, and check that the meta Audit detail names
  `context`, `specs`, `checklist` and `scratch`.
- Id 32 (S8 against unit 4 S3): a single missing fold input is not DEGRADED. Fix (judged sound):
  name a missing prevSubjects as "whole-file review of each subject" and a missing pair as "a
  degraded fold review", matching unit 4 S3.
- Id 33 (AC7 against S8): AC7 passes an empty priorFindings array that S8 forbids. Fix (judged
  sound): omit priorFindings from the RESULT when confirmedFindings is absent, which the WARNING
  announces, or let S8 except an empty array the caller copied back.
- Id 43 (S1): `context` re-spells `memory/builds/<slug>/prompts/`. Fix (judged sound): compose
  `context` from the harness's `briefDir` const.
- Left-shift: a lint that a spec's §2 never re-spells a path the harness already holds in a const.

### L9 — units 3 and 4: a second BASE (id 34)

- Where: the status headers of `...-3.md` and `...-4.md`, which pin 3640cf58 while the other nine
  pin 028b5cac. Neither commit is an ancestor of the other.
- Fix (judged sound): pin units 3 and 4 to base 028b5cac, and restate their section-4 Evidence line
  against it.
- Left-shift: a build-set check that every spec in one build carries the same `base` in its status
  header.

## Left-shift summary

The class behind twenty-four findings is a §2 item marked "Observed by ACn" whose ACn checks less
than the item states. A cheap gate for most of it: for every §2 item that quotes a phrase it adds or
retires, require that the named AC quotes the same phrase. A second rule covers promised arms: a
§2 item that says FLOOR_ASSERTIONS rises must name an AC with both a pre-pass count and a floor
equality. Where a phrase cannot be quoted, the item belongs on the project's recurring-bug-class
checklist as a documented spec-audit check, because this run swept no checklist.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 6 AC7 | high | medium | confirmed | Unit 6 AC7 (line 206-211) compares against 'the render at the pass's base' and uses an unbound `git show <base>:...`. 'Pass's base' is defined nowhere; the spec header says `base 028b5cac`, BUILD-METHOD uses BASE for the run's pinned sha, and the spec's own Evidence reads 'at base 028b5cac'. Unit 6 is order 5 and unit 1 (order 1, S3) moves REVIEW_SHAPE to lenses5-r2, which joins inputPrint and so the key every find DURABILITY line carries (template :784). Against 028b5cac the byte-identical and same-key claims fail on a correct build. Units 1, 3 and 4 bind to the pass-start sha explicitly for this reason. Contained, because a red on a correct build is noticed rather than shipped. | sound |
| 2 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S4 / section 6 AC4 | high | medium | confirmed | Unit 4 S4 adds the hash-object step to the spec resume probe and an optional `blobs` in its schema. AC4 injects `blobs` from a probe stub, AC6 checks only the diff-kind probe, and the S9 arms are stubs too. No criterion reads the spec `resume:probe` prompt or its schema, so a build that omits both passes AC1 to AC7 while a real probe never returns `blobs`. The effect is contained: S6 still names every subject as unchecked in RUN INTEGRITY, and S5 lenses still run hash-object themselves, so the loss is announced rather than silent. | sound |
| 3 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S4 (section 8 F2) / section 6 AC4 | medium | medium | confirmed | AC4 covers a moved `now`, an empty `now` and a null probe. A live probe object with no `blobs` key, which S4 says must read as every subject unchecked and never as none moved, is not exercised. A natural `(probe.blobs \|\| [])` reads that case as zero moves and zero unchecked, which is the silent-zero S4 forbids, and AC4 stays green. | sound |
| 4 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S3, S6 | low | low | confirmed | S3's `none supplied for this round-<n> review` line and S6's count of subjects carrying prevBlob are in no criterion. AC3 only asserts the absence of `first-round review` plus DEGRADED, and AC2 reads find/verify prompts, never the synth RUN INTEGRITY block. The effect is limited to operator-facing wording and one figure. | sound |
| 5 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:section 2 S6 / section 6 AC8 | medium | medium | confirmed | Unit 1 S6 says FLOOR_ASSERTIONS rises by the arms added, 'Observed by AC8'. AC8 only greps for retired keys and checks two MT stub `raw` counts. Neither §7 `New arm:` line nor the floor move is observed, unlike units 3 and 4 AC6/AC7. A build adding no arm passes. The effect is a missing regression arm, which is contained. | sound |
| 6 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:section 6 AC8 | medium | low | confirmed | At HEAD 8357cbe2, tools/workflows/tier2-review.test.sh:336 holds `scanSpawned('find:prior-art')`. The quoted `'prior-art'` alternative in AC8 does not match it; it matches only :334/:419/:434/:593. S6's table says `find:prior-art` becomes `reuse`, so AC8 can print 0 with :336 un-rekeyed. The suite at VERIFYING would red on that arm, so nothing ships wrong and only a cycle is lost. The fix's first option, an unquoted `prior-art`, depends on a `'prior-' + 'art'` spelling of the new refusal arm that no spec states, and it would red on the retired-key arm unit 1 §7 adds; only its second option holds. | unsound |
| 7 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 2 S7 / section 6 AC8 | medium | medium | confirmed | Unit 2 S7 promises prelude arms for each S4 refusal and its passing case, with FLOOR_ASSERTIONS raised, 'Observed by AC8'. AC8 greps only `scratch` literals in the fixtures and checks that MT_ARGS does not throw. Adding the fixture literals alone satisfies it, so the refusals can ship with no arm and an unmoved floor. The effect is missing regression coverage, which is contained. | sound |
| 8 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 2 S4 / section 6 AC3 | medium | medium | confirmed | Unit 2 §4 'The argument' specifies folding to forward slashes, lowercasing, dropping a trailing slash and 'equal to or under' repo. AC3 tests only exact-case POSIX '/tmp/r' and '/tmp/r/sub', and 'C:\\t\\s' only for proceeding, not for the folded value in the PROBE POLICY line. A naive startsWith, which refuses the sibling '/tmp/rs', and a missing case fold, which admits 'C:/R/x' under 'c:/r', both pass AC3. The effects are a loud refusal or a write-into-tree hole on Windows spelling, both contained. | sound |
| 9 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S6 / section 6 AC4, AC5 | medium | medium | confirmed | Unit 3 S6 confines the orphan scan to the spec kind. AC5 compares only diff-kind prompts, AC4 runs only the spec kind, and the §7 diff-kind arm checks only the verify prompt. A build scanning both kinds passes everything and would demote a diff-kind refutation that opens `duplicate of id=<n>` against an unconfirmed survivor, which breaks shared invariant 2. The path is narrow, because the diff skeptic's duplicate rule names no surviving id, and the outcome is a demotion to unverified, not a loss. | sound |
| 10 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S3 / section 6 AC1, AC2 | medium | medium | confirmed | Unit 3 S3's sentence, that a probe the skeptic could not run inside its bound falls to the grade default and never to a refutation by itself, is in neither AC1's marker list nor AC2. AC2 checks the re-run instruction and the absent-evidence clause only. A build dropping it passes, and a skeptic could read a timed-out probe as 'does not reproduce' and refute a high. The effect is contained to that path. | sound |
| 11 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S5 / section 6 AC4, AC5 | medium | medium | confirmed | The template at base 028b5cac has the every-lens-dead return at the `lensesDead === lensesRunning` branch (:821-833), and that exit runs before verify. S5 names it as one of 'the two exits before the verify stage'. AC5 covers only no-finding and every-refuted, and AC4 covers only a PARTIAL dead fan. So no criterion observes lensYield on the all-dead exit. The §7 'two early exits' arm is ambiguous: AC5's every-refuted case is not pre-verify. A build that leaves the field off that return passes every AC. | sound |
| 12 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S9 / section 6 AC8 | low | low | confirmed | README line 207 at base reads 'Every return carries three fields beside the counts:'. AC8's observation is `grep -n lensYield` naming defects, unique and null. Adding a lensYield line satisfies it even when that sentence survives, which is exactly AC8's own Red-when. The consequence is stale documentation only. | sound |
| 13 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:section 2 S6 / section 6 AC7 | medium | low | confirmed | Both comments exist in tools/unattended/unattended.sh. The first, '`fold` is reachable from ONE exit, CONVERGED' (:10059), sits above review_exit_note. The second, 'on a SPEC subject a disposition is ACCEPTED there and never required' (:10185), is in verb_review. Both contradict S3. AC7's alternation matches neither, so S6's rewrite of these comments goes unobserved. The defect is in comments only and has no behavioural effect, so it is graded low. | sound |
| 14 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 2 S1 / section 6 AC1 | medium | medium | confirmed | S1 says it is 'Observed by AC1'. AC1 checks only three markers and a negative, so the closes-verb ban, the per-batch `repairs` rule, the §1/§2 report-id naming and `folded` returned as 0 can all be dropped with AC1 green. The resulting agent misbehaviour is caught later by other legs, so the effect is contained. | unsound |
| 15 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 2 S3 / section 6 AC3, AC4 | medium | - | refuted | The 'promoted below confirmed' arm is implied by the other arms, so dropping it ships no silent loss. A non-empty `standing` is already refused by the existing `stood.length` arm. S2 forces `folded` to 0. `refuted` must lie in [0, unverified] (refutedOk). The sum must equal outstanding = confirmed + unverified (:1101). Together these give promoted = confirmed + (unverified - refuted), which is at least confirmed. The finder's scenario, promoted 2 with one standing over 3 confirmed, is refused by the standing arm, so nothing is accepted and nothing is dropped. | unsound |
| 16 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 2 S8 / section 6 AC9 | medium | low | confirmed | S8 names the reconciliation comment for rewrite. At unattended-build.template.js:1268-1275 that comment says every outstanding finding is 'promoted,/ folded or named standing' and '`folded` AT LEAST the confirmed rest'. AC9's case-insensitive alternation matches neither phrase, though it does catch the separate 'MEDIUM or LOW still folded' and `mustFold` lines. A stale comment survives with AC9 green. The defect is comment-only. | unsound |
| 17 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1 | medium | medium | confirmed | REVIEW_ROUNDS_DEFAULT=1 at tools/unattended/unattended.sh:384, so AC1's expected `rounds=1` for the no-assignment blob is also what a hard-coded 1 prints. S1's read from $DRIVER is therefore unobserved. AC2's 'kit-default addition is not a write' arm rests on that same fallback, so a later default change would mis-grade such commits. | sound |
| 18 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S3 / section 6 AC3 | medium | medium | confirmed | In check 19 the grant scan computes `maycs` per recorded state: from the witness for a terminal record, re-scanned after read_run_exclusions, and from HEAD or the landing commit for a live one (check-unattended.sh:2382-2424). AC3 builds only a live run-state file, and AC4 calls scan_round_writes directly. No criterion therefore observes the round scan on a terminal record or after exclusions. | unsound |
| 19 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S5 / section 6 AC5 | low | low | confirmed | Two of S5's three edits can stay stale with AC5 green. AC5 greps only the :801 phrase 'closing-review row carrying counts'. The :794 message ('closing-review subject(s)... on a row carrying highs and minors') and the :728 comment ('on the build-slug subject terminal round only') are unobserved. The consequence is operator-facing wording plus a comment, with no change to what check 2 reads. | sound |
| 20 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S7 / section 6 AC1 | medium | medium | confirmed | S7 promises one --selftest arm per behaviour S1 to S6. AC1 requires only K == ARMS_DECLARED, K above 19, and 'the new arms are named', which one added arm satisfies, and §7 declares a single New arm. AC2-AC7 observe the behaviours once inside the pass, but five of the six can land with no regression arm, so a later change can break them unseen. | sound |
| 21 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S4 / section 6 AC5 | low | low | confirmed | Unit 10 S4 refuses kind-mismatch in either direction and reads an unbound candidate in the known record's mode. AC5 observes only a spec known record against a diff-review candidate, so a one-directional build passes. The design text is right; the criterion is narrower than the behaviour it claims to observe, and the effect is contained to a mis-scored replay. | sound |
| 22 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 2 S1 / section 6 AC1, AC2 | medium | medium | confirmed | Unit 11 S1 lists the read-only probe sentence, the fold-then-STOP rewrite (template line 139, 'Fold fixes into the spec ... then STOP') and M2's 'the closing review's minors batch (M4) excepted' (template line 34). AC1 is a byte budget and AC2 greps only 'FOLDED into its spec', SPEC_LENSES and two lens names. None of the three bullets is observed, so a delete-only build passes and the method keeps text that contradicts the new promote-everything rule. | sound |
| 23 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 2 S3, S4 / section 6 AC4, AC6 | medium | medium | confirmed | At BASE the Skill template says the counts are 'REQUIRED there and refused on any other round or subject' (lines 852-853), the CONVERGING bullet scopes the fold to the closing diff review, and the verbs template line 224-226 says fold is a row 'which the driver reaches only at `CONVERGED`'. S3 and S4 require all three rewritten, but AC4's alternation matches none of them, and AC6 does not either. A stale sentence telling the operator counts are refused on a spec subject sends them into unit 7's refusal. | sound |
| 24 | underspecification | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S8, S9 / section 6 AC5, AC8 | low | low | confirmed | Unit 5 S8 announces a fold re-invoke 'without prevSubjects or priorFindings', and AC5 tests only the both-absent case. S9's meta Audit phase detail is unobserved, and AC8 greps only prevSubjects in the header block. All three are acceptance gaps. The design states the behaviour, and the effect is a missing warning or a stale doc line. | sound |
| 25 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 6 AC7 | high | high | confirmed | Unit 6 AC7's fixture is `git show <base>:tools/workflows/tier2-review.js` 'at the pass's base'. That term is defined nowhere in the method, and the unit's own header says base 028b5cac. Unit 1 S3 moves REVIEW_SHAPE, which unit 1 itself says is interpolated into every finder and skeptic DURABILITY line. Units 3 and 4 therefore compare against the pre-pass HEAD render and explicitly 'not to BASE'. Read as the header base, AC7 is red on a correct build and invites undoing unit 1's key move. | sound |
| 26 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S6/S8 against unit 3 section 2 S7 and unit 4 section 3 | medium | - | refuted | The spec brief's unit-6 section says lensYield 'applies to BOTH kinds ... it moves no prompt text a lens or skeptic reads, and invariant 2 is about lens and skeptic prompts'. Invariant 2's own proof clause names only the finder and skeptic prompts. Unit 6 S8 follows that carve-out explicitly. Unit 3 S7 and unit 4's AC are each scoped 'before and after this unit', and both units are ordered before unit 6, so neither is violated. Unit 4's dropped round>1 line would change the meaning of a diff finder prompt, which invariant 2 forbids on any reading. No sibling becomes wrong. Fix: its first option, scoping the block to the spec kind, contradicts the brief's explicit both-kinds ruling. | unsound |
| 27 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 6 AC1 against unit 3 section 2 S5 / AC3 | medium | medium | confirmed | Unit 2 AC1 evaluates the live render `tools/workflows/tier2-review.js`, not a pass-pinned one, and asserts that no `verify:` prompt carries PROBE POLICY. Unit 3 S5 and AC3, ordered after it, require every spec-kind verify prompt to carry those same bytes. After unit 3 lands, unit 2's criterion is red on a correct tree. The effect is a false red on any re-observation, which is contained. | sound |
| 28 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S5 / section 6 AC6 against section 2 S1 | medium | medium | confirmed | The harness's ordered-opening instruction (template ~1232-1248) puts the `**Serves:**` binding line FIRST, then the title, then the subject@blob line. Unit 10 S1 detects spec mode from that first line, but S5 reads the pins from 'the record's opening line', which is the binding line, so every real record prints `subjects none-stated`. AC6's fixture opens with the pins, so under S1 it would not be read as spec mode, and the criterion cannot pass as written. Scoring itself is unaffected, so the effect is contained. | sound |
| 29 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 2 S3 (counts paragraph) against unit 8 section 2 S5/S6 | medium | medium | confirmed | Unit 11 S3 says a hand-recorded spec exit's counts are `highs` and `confirmed - blockers - highs` 'with no summing'. Unit 8 S5 adds `adjudicated` to `<m>`, and unit 8 S6's DEGRADED hand-record note says to add every promoted UNVERIFIED finding to `--minors`. Unit 11 consumes from unit 8 and contradicts it. Under unit 7 S3, an operator following the Skill after a disposal that promoted only unverified findings records a zero standing count, and that refuses `promote`. | sound |
| 30 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 7 New arm lines (also unit 5 and unit 8 section 7) against units 1-4 section 7 | medium | low | confirmed | tier2-review.test.sh's FLOOR_ASSERTIONS=180 is a tight executed-count pin whose history raises it by assertions added. Units 1 to 4 raise it, but unit 6 declares 'none' for four new arms in the same file, so those arms can go unreachable with no red. unattended-build.test.sh's floor is a static count at about 10% headroom, so 'none' there is weaker but defensible. Unit 1's 'by arms' still gives a valid lower bound, only a looser one. The template permits 'none', and no shipped behaviour changes, only guard strength. | sound |
| 31 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 4 The sentence (last line) / section 2 S3 against section 3 (uncertain default) | medium | medium | confirmed | Unit 3 section 4 'The sentence' ends 'A probe you could not run inside its bound is a finding you cannot establish, not a refutation.' The default paragraph the harness keeps (tier2-review.template.js:894, 'WHEN YOU CANNOT ESTABLISH A FINDING ... medium or low ... is "refuted"') makes exactly that case a refutation at medium and low, and section 3 retains that default. So the prompt gives two conflicting instructions for medium and low findings. S3's 'never to a refutation by itself' is consistent with the default, but the sentence the skeptic actually reads is not. The effect is limited to verdicts on medium and low findings whose probes could not run. | sound |
| 32 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S8 against unit 4 section 2 S3 | low | low | confirmed | Unit 5 S8 says a fold re-invoke missing prevSubjects OR priorFindings is one 'the callee then runs as a degraded fold review'. Unit 4 S3 makes the round DEGRADED only when no subject carries prevBlob AND no priorFindings were supplied. When only one is missing, the callee draws a per-path WARNING or a 'none supplied' line, not DEGRADED. Only the WARNING wording is wrong. AC5, where both are missing, is consistent. | sound |
| 33 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 6 AC7 against section 2 S8 | low | low | confirmed | S8 says an input the harness could not produce is 'never passed as an empty value'. AC7 has the CONVERGING RESULT carry "priorFindings":[] when the callee returned no confirmedFindings. S5 and S6 accept any array, so the copied-back [] reaches the callee on the next fold re-invoke. The spec contradicts itself, but the callee treats an empty array as none, so behaviour is unaffected. | sound |
| 34 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:status header (also unit 4 status header) | low | low | confirmed | Re-probed: units 3 and 4 have status-header base 3640cf58 and the other nine have 028b5cac. `git merge-base --is-ancestor` fails in both directions. `git diff 3640cf58 028b5cac -- tools/workflows/tier2-review.template.js` shows only the version line (1.28 to 1.30). Every identifier and line the two units cite is unchanged between the bases, so the effect is a confusing second BASE rather than a wrong build. `git diff --stat 028b5cac b3950dc7 -- tools/` is empty, so re-pinning to 028b5cac also simplifies unit 3's Evidence line. | sound |
| 35 | contradiction | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S6 against section 4 Data model | low | low | confirmed | Unit 6 S6 (line 45) says 'The four counts known before the synthesis, `raw` to `precision` with `returned`'. The section-4 data model and table run raw, confirmed, refuted, uncertain, unverified, precision, which is six columns. The word is wrong, and the table governs what gets built. | sound |
| 36 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S3, section 4 Evidence (renderCell bullet) | high | high | confirmed | Read tier2-review.template.js:1061-1063. renderCell folds line breaks AND applies `.replace(/\\|/g, '\\\|')`, so every pipe becomes `\\|`. Unit 3 S3 and its data flow fold evidence through renderCell, and its Evidence bullet describes renderCell as only folding line breaks, which is false. The skeptic is told to RE-RUN the command, and refutation case (3) covers evidence that does not reproduce. A pipe-bearing command run as rendered passes a literal '\|' argument and produces different output, so a true finding can be refuted. AC2's fixture has no pipe and cannot observe this. The path is narrow (a skeptic re-running the command literally), but the consequence is a wrong verdict. | sound |
| 37 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S3 | high | high | confirmed | Read check-unattended.sh check 19. The terminal walk runs only under `if [ -n "$maywr" ] && [ "$maywalk" = 1 ]`, so it runs only on a GRANT hit over the base..witness superset. The arm's own header says that superset holds every default-branch commit landed since BASE. Unit 9 S3 re-scans rounds 'exactly when the grant scan does', so with no grant hit the round scan grades the unwalked superset. An owner commit on main that changes REVIEW_ROUNDS, merged into the run before its witness, would then fail 19 on an archived record on every bar. This is the forever-red that the header comment and unit 9's own F1 history bullet set out to avoid. AC3 tests the owner raise only on a live record. | sound |
| 38 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S2, section 4 Evidence ('units[].specPath arrives from --plan, repo-relative') | high | medium | confirmed | unattended-build.template.js:1534 states that specPath IS EMPTY for every unit the spec stage just authored. :1572 carries `u.specPath \|\| ''`, :1637 guards on `u.specPath &&`, and the resolver prompt at :782 handles only units that HAVE a spec path, so an empty specPath is reachable at the Audit stage. Unit 5 S2 adds every units[].specPath that is not a subject. An empty or undefined specPath is not a subject, so it enters `specs`. tier2-review.template.js:235-240 refuses any non-string or empty member before any lens, and the whole Audit stage dies. The failure is loud and leaves no wrong result, so it is contained: medium, not high. | sound |
| 39 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S3, section 4 Evidence (gotchas.py bullet) | medium | medium | confirmed | gotchas.py cmd_for_paths (:364-385) returns 0 after printing only the two '#' header lines when no universal class exists and no anchor hits. It also returns 0 with 'selects no file - nothing to check' when normalise_paths leaves nothing. tier2-review parseChecklist (:266-268) THROWS on a non-blank string with no line starting '- '. Unit 5 S3 lists only no path, a non-zero exit and a timeout as checklistError cases, so this output is passed through as `checklist` and the callee refuses the audit with no S8 announcement. This repo's universal classes hide the case, so it reaches only adopters, and the failure is loud. | sound |
| 40 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S4 | medium | medium | confirmed | The build harness refuses `scratch` by shape only (unattended-build.template.js:218-225). Unit 2 S4 and its 'The argument' block make the callee also refuse a control character and a value equal to or under `repo`. Unit 5 S4 passes the folded scratch straight through and adds no matching check. A scratch under the repo therefore passes the build harness, spends the spec stage and the resolver, and is refused only in the callee's prelude. Every lens is still blocked and nothing is written, so the cost is wasted work and a late, indirect refusal. | sound |
| 41 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S4, section 4 Evidence (driver sources the conf) | medium | medium | confirmed | unattended.sh sources the working-copy conf (`. "$CONF"`, :526) and reads REVIEW_ROUNDS from it at :811. Only LANDING_NODES and SPEC_AUDIT_DEFAULT are re-read from the BASE blob (:519-524). check-unattended.sh never grades a run's round count against the conf: grep finds no REVIEW_ROUNDS reader in the leg. So a run that raises the key in the working copy and reverts before committing gets more rounds, and check 19 has no commit to see. S4's does-NOT-check list names non-commit vectors such as a preflight --waive, but it omits this one. The second fix option conflicts with section 3's non-goal ('the driver's reading of it'). The omission in the header is still real. | sound |
| 42 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 4 The policy / The argument | low | - | refuted | Section 4 says the block is built 'after scratch is validated' and that PROBE_RULES sits 'beside SEVERITY_RUBRIC' (template :380). 'After' sets an order. It does not say 'immediately after', and the prelude placement is stated only for the argument validation. inputPrint at :614, which the spec also makes read PROBE_RULES, is already below :380. A builder placing the block where its constant is initialised is ordinary JS, and AC1 catches a TDZ anyway. This is a request for placement detail, not a defect in the spec. | sound |
| 43 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S1 | low | low | confirmed | unattended-build.template.js:230 has `const briefDir = a.briefDir \|\| 'memory/builds/' + slug + '/prompts'` and passes it to renderRoster at :622 and :781. Spec 5's S1 and its data-model snippet hard-code `memory/builds/<slug>/prompts/` in `context`. A caller passing another briefDir would therefore send lenses to a directory the mandate is not in. No caller passes one today (git grep), so the effect is narrow and contained. | sound |
| 44 | unstated-assumption | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S5 | low | low | confirmed | S5 spells `git -C <repo> cat-file -p <blob> \| diff -u - <path>`. Giving git -C while diff gets a bare repo-relative <path> assumes the lens's cwd is repo, an assumption the -C exists to avoid. Off-repo, diff fails. The CRLF half is real only off this repo, because here memory/**/*.md is eol=lf (.gitattributes:49). The effect is contained: the lens still reviews the whole file. I checked the proposed form: `git diff <old-blob> -- AGENTS.md` printed a working-tree diff under git's filters. | sound |
| 45 | prior-art | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 5 perf / scale (and section 3, section 10) | high | medium | confirmed | TOOL-aWokenSentinel-30 is OPEN (gen_build_index --asks). The governing bound is M4's precision rule (BUILD-METHOD.md:142, TOOL-dLoggedFlight-34, closed by TOOL-dGatedProse-4). Unit 8 makes every terminal spec round with any standing MEDIUM or LOW promote at least one batch unit, and M4 audits each one as a fresh subject. Unit 3:119 confirms 'AT ANY RUBRIC SEVERITY', which raises the precision that has to fall below the floor to end a chain. Unit 8 section 5 does say the rule 'feeds' the cascade, but it calls the chain bounded without engaging either effect. The consequence is token cost and an unclosing chain, not a wrong result, so the grade is medium rather than high. | sound |
| 46 | prior-art | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:section 2 S8, and section 3 'A cutoff for old rows' | medium | medium | confirmed | check-unattended.sh:779-780 grades `fold` only on a counted row (closefold) or beside a non-zero blocker count after FOLD_CUTOFF (foldbad). A countless spec row reading `blockers 0 · BOUNDED · disposition fold` therefore passes check 2 after this build, and so does a terminal spec row with no counts. Unit 7 enforces the new rule only in the verb (S3), and S8 and section 3 reject a cutoff. The repo's FOLD_CUTOFF comment (unattended.sh:828-836, check-unattended.sh:530-535) records the precedent that a ratchet grading history needs one cutoff per rule. The non-goal says 'old rows keep today's reading', but a cutoff would grade only NEW rows, so the non-goal does not cover this gap. | sound |
| 47 | prior-art | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 5 user docs (and unit 11 section 2 S5 / section 6 AC5) | medium | medium | confirmed | DECISIONS.md holds TOOL-aProbedUnit-9 (the one-round default) and nothing that records 'an agent never changes REVIEW_ROUNDS'. Unit 11 S5 writes one row for the promotion answer only, and AC5 demands exactly one added line. Unit 11's scope covers M4, the memory-tree README, the Skill, VERBS and DECISIONS. It never covers tools/unattended/PROTOCOL.template.md, whose REVIEW_ROUNDS row is at :468 with no owner-held clause. Unit 9 section 5's hand-off to unit 11 therefore lands on no owner. | sound |
| 48 | prior-art | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:section 10 Reuse audit | low | low | confirmed | Unit 1 section 10 cites only TOOL-dTieredTribunal-11 S2's copy direction. That spec (:183-186, :428-430) names the README/harness pair as an open instance of TOOL-dUnstalledConvoy-16, with parked P3 (dTieredTribunal README:65, run-state row) as its fix. Unit 1 names neither, so the records keep describing an instance this unit removes. The effect is on the records only, with no change in behaviour. | sound |
| 49 | prior-art | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 10 Reuse audit | low | low | confirmed | Unit 6:254 names TOOL-dTieredTribunal-16 as the record that put the run counters into the synthesis prompt. That ask is OPEN (gen_build_index --asks), and the shipped RUN INTEGRITY block is attributed to TOOL-aWeldedTribunal-4 at tier2-review.template.js:1164. The precedent is misattributed, which affects the records only. | sound |
