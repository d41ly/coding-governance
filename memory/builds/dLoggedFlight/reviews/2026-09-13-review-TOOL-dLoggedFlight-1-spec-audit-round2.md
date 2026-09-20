**Serves:** spec-audit TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13

# dLoggedFlight — spec audit of the thirteen-unit set, round 2

*Node `d`, 2026-09-13, on `branch/unattended-build-transparency-ea83a5` at HEAD `f698f6e6`, which is the
rev-2 fold of the round-1 audit, against the specs' stated base `9fac2b53`. No file under `tools/` or
`.githooks/` differs between those two commits, so every line a spec cites at base holds at HEAD. This is
ROUND 2 of the spec audit. It is a Tier-2 adversarial pass: four primed finder lenses, a skeptic stage of
five batches prompted to REFUTE each finding, and one synthesis, which is this record. Round 1 is
[the round-1 record](2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md). Every claim this record
states in its own voice was re-derived against the tree, and the list is under "What this synthesis
re-derived". A figure that came from verification and was not re-derived here says so where it appears.*

**Reviewed subjects, each pinned at the blob it was read at — ROUND 2:** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md@d8253e74a1a7c3b6380f057677f96efed0456c20`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md@d2ef4ab4a573df0e7b81510cfd4aac83ee733430`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md@8e68cff52f776d4bf734fc02b40465ed3385006c`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md@b71f21348eace8a949f15b0241a59757227c0bf4`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-5.md@714125052a0fc2aaaa783952402f8f81c02d4071`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md@8972da1c0ad0babc5337b4c5373f23148b1f5efc`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-7.md@4710b424f8e2d73dac7ad9ff3892139b09d4e21e`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md@7328a88fe2269cbabf35ea7e73a46ab24e8e7738`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md@5705672e1f153ef766c0ffd534eddc2c5313d631`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md@bcf8a4486c7d55e4bde869a29c2c18cf655d88c0`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md@e1f77db400794d640fe00baa7c2081b0bd7bb530`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-12.md@cc46d43c2707c683f8aa3f046b84c78731a9776a`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md@27b0eebb7c50eef3ff41976a060f4439f6fe416f`.

## Verdict: BLOCKED

One blocker stands, and it is the fold of a round-1 blocker. Round 1's B2 found that the record's key had
no input for a run that predates the writers. The fold keyed each run on the commit that created its
run-state file, and unit 9 S1 asserts that commit is "distinct for every preflight, including a rotated
record's". On this tree it is distinct for no rotated record. All six rotated builds resolve their archived
record and their live record to one commit, because rotation modifies RUN.md rather than adding it (B1).
Unit 8 uses the same derivation to start the window of every run that predates the writers, so each
rotated build's live run swallows the run it replaced. The derivation the fold implemented is the one
round 1's own fix text proposed, and round 1 never ran it over the six records.

Five highs sit beside it. Two of them fail on this build's own run. The window of a run with no terminal
END ends at "the last line or commit naming its slug", which already runs three days past aLeakedHandle's
landing and leaves AC7 one commit from red (H1). The fold that moved this build's landing onto the lander
left standing the render placement written for the old route, so the Skill step this build writes cannot
satisfy its own landing criterion (H2). The other three are pre-push refusals that now write an END with
no START (H3), a merged test that counts a run which never moved its witness (H4), and a Skill mechanism
justified, for the second round running, by a precedent that does not exist (H5).

The fold dominates the finding set. Of the 36 confirmed findings, 15 sit in text the fold wrote and 9 in
text where the fold answered a round-1 finding only in part. 11 sit in rev-1 text that round 1 did not
flag, and 1 straddles. That is the shape `memory/gotchas/fold-text-is-unreviewed-surface.md` records for
two earlier builds. The confirmed-blocker count fell from 4 to 1. That is strictly smaller, so under
`memory/guides/BUILD-METHOD.md` M4 the loop re-arms: fold this round, and round 3 measures that fold.

Review shape, stated in full below: raw 65, confirmed 36, refuted 29, unverified 0, precision 0.55.
Adjudicated here as 1 BLOCKER, 5 HIGH, 14 MEDIUM and 5 LOW, over 25 items.

Most of the fold held. Round 1's B1, the journal epoch and `partial`, drew no confirmed finding against
its mechanism. Neither did B3, the closed schema; L5 touches one of B3's vocabularies only because that
vocabulary copies a rev-1 list. The wall-clock floors are now counts, and the location contract has its
linked-worktree arms. That is a statement about what four lenses found, not a certificate.

## Run integrity

- lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.

Every counter is zero, so the run is complete in the only sense the orchestration can certify: every lens
reported and every finding reached a skeptic. A complete run is still not a clean bill. The 36 confirmed
findings are a lower bound on the defects in this set, not a census of them. Units 5, 7 and 12 drew no
confirmed finding, which means none was found there, not that they are sound.

## Review shape

- raw 65, confirmed 36, refuted 29, unverified 0, precision 0.55.
- Adjudicated in this report: **1 BLOCKER, 5 HIGH, 14 MEDIUM, 5 LOW**, over 25 items. Counted by raw
  finding instead of by item, the same split is 5, 8, 18 and 5.
- Seven folds take 18 raw findings into 7 items: B1 (25, 28, 42, 43, 54), H1 (2, 50), H2 (26, 56), H5
  (51, 55), M1 (10, 11, 59), M2 (15, 35) and M10 (12, 60). The other 18 are one item each. The pipeline's
  duplicate count is zero because it discarded nothing as a duplicate. These folds are this synthesis
  grouping distinct findings that describe one defect, and every raw id stays in the header of the item
  that absorbed it.
- A fold takes the highest filed severity among its members, as in round 1. That raised raw 28 from medium
  and raw 25, 43 and 54 from high to BLOCKER. It raised raw 50 from medium, and raw 51 from low, to HIGH.
  No finding was lowered, and no item sits above its highest filed member. B1 and H5 state their own
  grounds as well.
- Five survivors were narrowed by their skeptics, and each item carries the narrowed claim: raw 7 (M9),
  raw 15 (M2), raw 26 (H2), raw 27 (H3) and raw 46 (M12).
- Precision 0.55 clears the ~0.5 threshold in `AGENTS.md` §8, down from round 1's 0.58. This synthesis
  received the survivors only, so it does not characterize the refuted 29.
- Confirmed blockers by round: 4, then 1.

## Findings

Unit N below is `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-N.md`. The Origin
column is this synthesis's reading of the rev-1 blobs at `1dd6f3da` against rev-2 at `f698f6e6`. `fold`
means the defective text was written by the fold. `in part` means the fold answered a round-1 finding and
left part of it standing. `missed` means the text is rev-1 and round 1 did not flag it.

| # | Sev | Unit | Address | Origin | One line |
|---|---|---|---|---|---|
| B1 | BLOCKER | 9, 8 | 9 §2 S1, AC1; 8 §2 S1, AC1, AC9 | fold | one creating commit answers for both records of every rotated build |
| H1 | HIGH | 8 | §2 S1 window end; AC7 | fold | "the last commit naming its slug" runs past the landing and reds AC7 |
| H2 | HIGH | 11, 8 | 11 §2 S2 against S5, S6, AC5; 8 §4 | fold | the placement written for the old landing route survived the route change |
| H3 | HIGH | 4 | §2 S1 and S4; §4 exit list; AC1 | fold | the pre-loop refusals write an END with no START |
| H4 | HIGH | 8, 13 | 8 §2 S5; 13 §2 S1, AC3 | fold; missed | a witness still equal to its base reads as merged |
| H5 | HIGH | 11 | §2 S1; §4 ¶2; §9; §10 | in part | an agent-read conf key justified by a precedent that does not exist |
| M1 | MEDIUM | 1, 2, 3 | 1 §2 S1, S6, AC1; 2 S10, AC9; 3 S6, AC6 | in part; missed | new self-tests ship to adopters, or their withholding goes unobserved |
| M2 | MEDIUM | 9 | §2 S6 against S3; AC6 | in part | Units, Decisions and the JSON twin have no bound under the 24 KB cap |
| M3 | MEDIUM | 2 | §4 Placement, the END unit field | missed | END reads `RS_ITEM`, which does not exist |
| M4 | MEDIUM | 8 | §2 S3 decision-log bullet; AC11 | in part | the owner spellings miss `(owner)`, half the parenthesised rows |
| M5 | MEDIUM | 8 | §2 S1 segmentation; AC1 | missed | which run a journal line belongs to is unobserved |
| M6 | MEDIUM | 13, 8 | 13 §2 S3, AC3; 8 §2 S5 | missed | the four sub-classes have no mapping from a parked row |
| M7 | MEDIUM | 8 | §2 S7; AC13 | fold | four owner-position classes, three stated boundaries |
| M8 | MEDIUM | 8 | §2 S6, the share clause | missed | the unit-and-phase share has no rule and no criterion |
| M9 | MEDIUM | 8 | AC5, AC6, AC12 against S5, S6 | in part | `COVERAGE_STATES`, two of its states and `refused-landing` are unstaged |
| M10 | MEDIUM | 6 | §2 S5 and S8; AC5, AC6, AC8 | in part | the self-test writes into the operator's real state store |
| M11 | MEDIUM | 11 | AC6 | fold | `git log` cannot show which tool pushed |
| M12 | MEDIUM | 2, 4 | 2 AC3; 4 AC3 | fold | a fixed one-second TERM races the gate child |
| M13 | MEDIUM | 2, 11 | 2 §2 S11, AC10; 11 §2 S4, AC4 | missed | byte identity passes when the protocol paragraph is absent from both copies |
| M14 | MEDIUM | 1 | §2 S5; AC5, AC7 | missed | `journal`'s success output has no criterion |
| L1 | LOW | 9 | §2 S5; AC5 | fold | `commitment=none`, and `verify` on it, are unobserved |
| L2 | LOW | 10 | §2 S1; AC1, AC2 | missed | no fixture separates the index from the working tree |
| L3 | LOW | 6 | §2 S3 keepalive join; AC3 | missed | a prefix matcher passes the keepalive fixture |
| L4 | LOW | 2 | §2 S2; §4 Placement; AC2 | fold | the exit enumeration cannot see a verb body |
| L5 | LOW | 8, 9 | 8 §2 S3; 9 §2 S4 | missed | the ledger's owed kinds restate the driver's, minus two |

---

### B1 — BLOCKER — unit 9 §2 S1 and §6 AC1; unit 8 §2 S1, §6 AC1 and AC9 — raw 25, 28, 42, 43, 54

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** Unit 9 S1 keys each record on "the commit that CREATED the run's run-state file, found
with `git log --diff-filter=A --follow`", and asserts that commit is "distinct for every preflight,
including a rotated record's". Unit 8 S1 uses the same derivation as the window start of any run with no
preflight START, which is every run before the writers. On this tree the derivation returns one commit for
both records of every rotated build. Re-derived here over all six:

| build | archive and live RUN.md both resolve to | the rotation commit, where the successor started |
|---|---|---|
| aBoundedVerdict | `e8be30e9` | `9ea808cf` |
| aDeclaredBound | `5ffeab51` | `a9fd55d2` |
| aGradedDialect | `1e656286` | `67964f14` |
| aPacedTurnstile | `86e56f5e` | `2d03cb5a` |
| dTieredTribunal | `bb41f748` | `136cdb70` |
| dUnstalledConvoy | `eed45133` | `02f8495e` |

The mechanism is the driver's rotation. `verb_preflight` runs `git mv -f` on the finished record
(`tools/unattended/unattended.sh:2658`) and re-scaffolds RUN.md (`:2686`), and the preflight's records
commit carries both changes. So `9ea808cf` shows `A RUN.ABORTED.fc79c21d.md` beside `M RUN.md`. The live
file is never added again, and `--follow` walks the archive back to the original creation.
TOOL-dClosedLexicon-11 already records this: a finished run is retired by rotation inside the next
`--preflight`, "no verb here commits", and that is why the archive's name derives from the record's bytes
rather than from a commit.

**Impact.** The key stops identifying a run. An aborted run renders at `--abort` and its successor at its
own end, and on three of the six builds the first preflight and the rotation fell on one date. Two
records of one build rendered on one date with the same lowest served id get one filename, and the second
write replaces the first committed record. In unit 8 the live run's window starts at the previous run's
preflight and contains the whole aborted run. S2's own-commit filter keys on unit ids, which both runs of
one build share, so each run's commits, rows and owner turns enter the other's timeline, conformance and
anomalies. Unit 8 AC1's red condition, "the rotated record merges into the live run", is what happens on
real data. The criteria still pass on hand-built fixtures: unit 8 AC9 holds a single run, and both AC1
pairs can be built as two files that were each added, which is not what the driver produces.

**Why blocker.** The claim S1 makes about the population it names is false for every member of that
population on this tree. The identifier becomes a committed filename that the build index then cites, and
it anchors the segmentation of every run from before the writers. It is also the fold of a round-1
blocker, adopting round 1's own proposed fix, "a rotation is a `git mv` that `--follow` reaches", which
nobody ran.

**Fix.** Key a run on the commit that STARTED it, derived from the build's run-state history rather than
from one path's creation. List, oldest first, the commit that first added `RUN.md`, then every commit that
added a `RUN.<phase>.<8hex>.md` sibling, found with `git log --diff-filter=A` on that glob and without
`--follow`; each such commit is also the successor's preflight. Run k takes
entry k. An archive's key is the entry immediately before the commit that added it, and the live RUN.md
takes the last entry. Over the six builds above this gives the two distinct columns of the table. A build
that never rotated keeps its creating commit, so this run's key stays `2f11f32d` and unit 11 S5 needs no
change. Make this one function in unit 8's model, and have unit 9's `derive_runkey` read the model's value
rather than re-derive it, so the filename and the window cannot disagree. Cite TOOL-dClosedLexicon-11 in
both units. Build the rotated fixture of unit 9 AC1 and of unit 8 AC1 and AC9 the way the driver rotates,
`git mv -f` plus a fresh RUN.md in one commit, and assert distinct keys and disjoint windows. Raw 54
proposes keying on the `keepalive:` id instead; it differs in the two pairs this synthesis spot-checked,
but it needs a content search that the rotation order does not.

**Left-shift.** A real-population arm: unit 10's repo-subject leg, which already reads tracked files in a
constant number of git calls, also derives the key of every tracked `RUN*.md` and asserts the keys are
pairwise distinct. On this tree it would red on six pairs today, which is charter §7's "run a
candidate gate predicate over the real tree before wiring it". The class of the hand-built pair is
`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`: the fixture proves the derivation for two
files that were each added, which is not the shape the driver produces. The synthesis rule: *a fix a
review proposes that names a derivation is run over the population it claims before the review is
recorded.*

---

### H1 — HIGH — unit 8 §2 S1, the window end, and §6 AC7 — raw 2, 50

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** For a run with no terminal END, which is every run before the writers, S1 ends the window
"at the last line or commit naming its slug". It never says what naming is, and no criterion observes the
end rule; AC9 covers only the start. Commits keep naming a slug after its run ends. aLeakedHandle went
LANDED at `7d9e2d47` on 2026-09-10. `9fac2b53`, on 2026-09-13 and this build's own base, names it in its
subject, touches `memory/builds/aLeakedHandle/README.md`, and records four owner-ruled follow-ups. Read by
content, the window already reaches this build's own commits: `1dd6f3da`, `b21c5dd3` and `f698f6e6` all
carry the slug, because AC7 and the round-1 review of it name it. The "or commit" half is the fold's;
rev-1 said only "the last line naming its slug", which gave a journal-less run no end at all.

**Impact.** AC7 expects aLeakedHandle's journal sources to read `absent` because its window predates each
journal's epoch. The epoch of `driver.log` on this node is the first line it ever receives, which this
run's first verb after unit 2 lands will write. Under a content reading, the build's own later records of
AC7, its acceptance-ledger line among them, name the slug. The window then contains the epoch, the
sources read `partial`, and AC7 reds on a correct model. Under a subject or path reading, AC7 holds only
until the next commit that names aLeakedHandle in its subject, and `9fac2b53` shows those keep coming
after a landing. The same overshoot pulls unrelated work into the S7 owner positions and the S8 usage of
every landed run from before the journals.

**Fix.** End a terminal run's window at the commit that first wrote its terminal `phase:` into its
run-state file, which is `7d9e2d47` for aLeakedHandle. End an archived run's window no later than the
rotation commit that archived it (B1). End a non-terminal run's window at the later of its last journal
line and the last commit that touched its run-state file. If a slug-naming fallback survives anywhere,
define naming as subject, path or content, and bound it by the run's own events. Add an AC arm in which a
later records commit naming the slug leaves the window end where it was.

**Left-shift.** The arm above. The spec-audit rule: *a window bound phrased as "the last X naming Y" is a
join over future history; bound it by an event of the run itself.* Round 1's B1 rule applies again, and
here it reaches the unit's own records: *an acceptance criterion observed "on this tree" is evaluated
against the tree as it will stand after every earlier-ordered unit has landed.*

---

### H2 — HIGH — unit 11 §2 S2 against S5, S6 and §6 AC5; §1; §4 ¶1; unit 8 §4 ¶1 — raw 26, 56

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** The fold of round 1's M20 moved this build's landing (S6) from the owner-allowed worktree
push to the protocol's own route: merge in the primary tree, `tools/push-main.sh`, then `--landed`. The run
mandate says the worktree route ends the record "at `LANDING`"
(`memory/builds/dLoggedFlight/prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-0-run-mandate.md:41-42`), and
S2's third placement, "where the run's record stays at LANDING, after `--close` and before the merge", was
written for that route. On the new route this run reaches LANDED, and S2 places a LANDED run's render
"after `--landed`, in the LANDED record commit", which follows the push. The Skill forbids any commit
between the push and `--landed` (`tools/unattended/SKILL.template.md:781`). S5 and AC5 require this run's
record on the merged tree and graded before the push, and AC5 reds when "the run reaches its landing with
no record". Followed literally, the Skill step this unit writes makes AC5's red condition true.

A second contradiction rides with it. Unit 4 §5 says `pushes.log` lines appear only once the primary tree
carries the hook change, so this node's first push line is this build's landing push. A render before that
push reads `pushes` as `absent`, while unit 8 §4 says this run's "journals read `partial`". (A skeptic
narrowed one horn: a close-time render can ride the close's existing records commit, so §4's "no path
gains a commit" need not break. The contradiction with S2 stands.)

**Impact.** The build's only end-to-end criterion has no placement that satisfies both S2 and S5, and the
builder resolves it by departing from the Skill text the same unit ships.

**Fix.** Say in S5 that this run renders at S2's third placement, after `--close` and before the merge,
riding the close's records commit, even though it goes on to LANDED. Or widen S2 so that any run whose
landing criterion grades its own record renders before the merge. State whether the LANDED commit
re-renders. If it does, the re-render must keep the first render's filename, since the name carries the
render date. Correct unit 8 §4: at a pre-push render, `driver` and `gates` read `partial` and `pushes`
reads `absent`.

**Left-shift.** The class is `memory/gotchas/amendment-leaves-its-other-half-standing.md`: the route
changed, and the placement written for the old route stayed. `gotchas.py --for-diff b21c5dd3..f698f6e6`
selects that record for this fold. The spec-audit rule: *a criterion observed at the end of the build
names the Skill or protocol step that produces its input, and that step is walked on the route S6
selects.*

---

### H3 — HIGH — unit 4 §2 S1 and S4 against §4's exit list and §6 AC1 — raw 27

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md`.

**The defect.** S1 writes START "after the stdin loop", which is `.githooks/pre-push:115-117`. The fold of
round 1's M13 made the three default-branch refusals at `:95`, `:102` and `:108` write an END with
`decision=refuse-default-branch`, and AC1 requires one at `:95`. Re-read here, all three run before the
stdin loop. S4 sets the clean-exit marker on "every exit after `:49`", so the EXIT trap is live there, and
each such refusal writes an END whose nonce has no START. Unit 1 pairs `start` and `end` on `n` and
reserves `once` for an unpaired act, so this output breaks the grammar by design. The END also carries no
`wt`, and unit 8 joins push lines by worktree, so the refusal can never be attributed to a run. If the
trap is installed after the loop instead, AC1's `:95` arm cannot pass. No criterion checks that a push's
START and END pair. (Narrowed by its skeptic: `orphan-end` is a reader state in unit 1, not one of unit
8's anomaly kinds, so the refusal surfaces only as an `orphan-end` invocation that no consumer reads.)

**Fix.** Two routes. The smaller: the three pre-loop refusals each write an `ev=once` line carrying
`decision`, the remote fields, `lander` and `wt`, and the EXIT trap is installed with START after the
loop. That uses the grammar's own unpaired event and moves nothing else. The other: install the trap and
write START right after the directory resolution at `:49-52`, carrying the fields known before stdin, and
move `ref.<i>` and `ref_more` to END. That changes unit 1's golden push line and unit 8's ref reader. On
either route, AC1 asserts that every END in `pushes.log` has a START with its nonce.

**Left-shift.** Each producer suite asserts, over the whole journal it produced, that every `ev=end`
nonce has an `ev=start` in the same file. That is one `awk` line per suite. State it once in unit 1's
grammar as a producer duty, and unit 4's own arm would have caught this.

---

### H4 — HIGH — unit 8 §2 S5, the `nonterminal-merged` kind; unit 13 §2 S1 and §6 AC3 — raw 57

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md`.

**The defect.** Both units call a non-terminal run merged when its witness is an ancestor of the default
branch. At preflight the driver writes `witness:` equal to `base:`, re-derived here in the creating commits
of dLoggedFlight, aClosedDocket, aUnblockedFleet and dRatifiedSeam. The base is on the default branch by
construction, so a run that never moved its witness reads as merged. TOOL-cFinalBerth-2 already decided
this ambiguity: the merge-base "cannot tell a run that BUILT NOTHING from one FULLY LANDED", and the
recorded base can. Measured here at HEAD, the six non-terminal records whose witness is an ancestor of
`origin/main` are aClosedDocket, aCollapsedScan, aUnblockedFleet, dRatifiedSeam, dRetiredFork and
dSealedTally. dRatifiedSeam is at LANDING with its witness equal to its base, `a69e57d7`. So one of unit
13's measured six is vacuous. The unit 8 half is the fold's, from round 1's M6; the unit 13 half is rev-1.

**Impact.** A run that died before its first `--phase` is reported as work on the default branch by the
drift signal, and as an anomaly in its own public record. Neither spec cites the decision that settled it.

**Fix.** Count a run as merged only when its witness is an ancestor of the default branch AND is neither
equal to nor an ancestor of its recorded base. Report a witness at or behind its base as its own
sub-class, or as unjudgeable, in both units. Add a witness-equals-base fixture to unit 13 AC3 and unit 8
AC5, and cite TOOL-cFinalBerth-2 in both.

**Left-shift.** Unit 13's detail row prints the witness-to-base relation for every counted record, so a
vacuous case is visible on every run rather than folded into the count. The recurring class is round 1's
"recorded decisions not consulted"; see "Classes across the set".

---

### H5 — HIGH — unit 11 §2 S1, §4 ¶2, §9 rev-2 line and §10 — raw 51, 55

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md`.

**The defect.** The fold of round 1's M19 made `RUNLOG_CLI` "a declared value the agent reads at run
time" that "follows the `RECALL_CLI` and `MAP_CLI` precedent exactly", and §4 calls this what "the Skill
already does for the recall and map CLIs". That precedent does not exist. Re-checked here: neither
`tools/unattended/SKILL.template.md` nor `.claude/skills/unattended/SKILL.md` names `RECALL_CLI`, `MAP_CLI`
or `.unattended.conf`. Both keys are read by the driver alone, in its `reuse-probed` Definition-of-Done
item (`tools/unattended/unattended.sh:3644-3699`), with defaults at `:291`. Every declared value the Skill
uses reaches it through `render()`. Round 1's M19 said this precedent was not one and named `AUTH_PARAM`
as the real rendered-key precedent. The fold kept the false precedent and gave it a new form.

**Impact.** The Skill gains its first agent-side read of a sourced-shell conf, with no recorded decision,
no specified read and no check. S2's `<RUNLOG_CLI> record <slug> --write` leaves the agent to turn a key's
name into a command by a lookup the Skill never describes. TOOL-aUnmannedHelm-7 recorded that failure for
a rendered key, and this reaches it by another route.

**Why HIGH.** Raw 55 was filed high and raw 51 low, and the fold takes the highest. The adjudication
agrees on its own ground. This is the second round in which this seam's justification is a precedent that
is not one. A precedent claim is what tells the next reader not to look, and the mechanism ships to every
adopter's Skill with nothing checking it.

**Fix.** Choose one route and record it. The first route records the agent-read key as a named third
exception beside `ANCHOR_SCOPE` (TOOL-aPromptedMandate-5) and `AUTH_PARAM` (TOOL-aNamedGesture-1). It
needs a DECISIONS row, a Skill instruction naming the exact read, such as
`bash -c '. ./.unattended.conf; printf %s "${RUNLOG_CLI:-}"'` with empty output meaning skip, and a render
arm asserting that instruction is present. The second route renders `RUNLOG_CLI` defaulted to its own
token, so an undeclared value reds per TOOL-aWrittenMethod-1, and states the adopter migration. Either
way, strike the `RECALL_CLI` and `MAP_CLI` claim from S1, §4, §9 and §10.

**Left-shift.** Round 1's M19 left-shift, which the fold did not take, widened to cover this: the
adopter's `--check`, which the `unattended skill wiring` leg runs, refuses a Skill that names a conf key
`render()` does not substitute, unless that key is on a named-exception list carrying its decision id.
The fold-record practice applies too: *re-derive every citation the fold writes.* One grep of the Skill
would have refuted this one.

---

### M1 — MEDIUM — unit 1 §2 S1 and S6, §6 AC1; unit 2 §2 S10, §6 AC9; unit 3 §2 S6, §6 AC6 — raw 10, 11, 59

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md`,
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md`.

**The defect.** TOOL-aQuenchedHarness-3, CLOSED, is that a self-test never reaches an adopter, as a leg or
as a file. Each kit carries it as a `project-owned` rule under its `include = "**"` engine rule, with an
`[[exempt_leg]]` row in `tools/govkit/registry.toml` for each withheld leg. Re-read here: the engine rule
is `tools/run-gates/kit.toml:17-19` and `tools/unattended/kit.toml:9-11`, and the explicit project-owned
lists are at `:39-41` and `:31-33` respectively. The set honours the rule unevenly:

- Unit 1 creates `tools/runlog/kit.toml`, `selftest.py` and the `runlog selftest` leg, and units 5, 6, 8
  and 9 add `fixtures/`. None is claimed project-owned, and AC1's "claiming every file under the kit" is
  met by the engine rule.
- Unit 3 creates `tools/run-gates/run-gates.runlog.test.sh` and does not add it to that kit's explicit
  `project-owned` list. Listing `kit.toml` under Files touched is not an instruction.
- Unit 2 S10 states the withholding, which is the fold of round 1's B4. AC9 checks the floor, the PASS
  line, the budget and the manifest, and never `tools/unattended/kit.toml`.

**Impact.** The runlog self-test with its fixtures and leg, and the new run-gates suite, ship to every
adopter as engine files, reversing a closed decision without saying so. The `**` rule claims every file,
so govkit stays green. Verification reports that the only gate arms for the rule cover agent-cap; that was
not re-derived here.

**Fix.** In unit 1, add a `project-owned` rule for `selftest.py` and `fixtures/**` to
`tools/runlog/kit.toml` and an `[[exempt_leg]]` row for `runlog selftest`, and make AC1 assert that
govkit resolves both as withheld. In unit 3, add the suite to `tools/run-gates/kit.toml`'s project-owned
list with its exempt_leg row, observed in AC6. In unit 2, make AC9 also assert that the suite is in the
`project-owned` include of `tools/unattended/kit.toml`. Cite TOOL-aQuenchedHarness-3 in all three.

**Left-shift.** Gate the class rather than the instance: a govkit selfcheck arm that reds when a kit
file matching `*.test.sh`, `selftest.py` or `fixtures/**` resolves to a landable role, unless the kit
declares it shippable by name. Stage it RED with `tools/runlog/selftest.py`. Round 1's B4 left-shift was a
budgets-checker refusal for one kit's legs, which is the instance.

---

### M2 — MEDIUM — unit 9 §2 S6 against S3; §6 AC6 — raw 15, 35

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md`.

**The defect.** S6 promises the 24 KB cap is "kept reachable for every input" and bounds three sections:
the timeline at its first and last 60 rows, and anomalies and conformance at 40 rows each. S3 renders
`## Decisions` as counts "with shas and repo-relative record paths", and unit 8 S3 has each ledger entry
point at its source, so that section grows with the entries. `## Units` has one row per unit. Neither has
a bound. S3 does not say whether the `## Data` twin carries the elided rows or all of
them. Verification estimates a twin mirroring a 500-row timeline at about 30 KB of JSON on its own; that
was not re-derived here. AC6 stages 500 timeline rows, 30 units and 200 anomalies, and no decisions. (A
skeptic corrected raw 15, which said AC6 stages no units.)

**Impact.** A long run with many parked rows, review rounds and trailers renders past 24 KB, unit 10 S2
refuses it, and that run can never commit a passing record. Unit 11 AC5 requires this run's own record to
pass. The fold of round 1's M16 added the universal claim and bounded the two sections M16 named.

**Fix.** Give Units and Decisions an aggregation rule past a stated row count. State that the twin is
elided by the same rules and carries the same counts. Add a fixture with a few hundred ledger entries to
AC6.

**Left-shift.** Round 1's M16 left-shift, which the fold did not take: the renderer derives the
worst-case size of each section from the model's bounded enumerations, and an arm renders that declared
worst case under the cap. A section with no bound then has no worst case to declare, and reds.

---

### M3 — MEDIUM — unit 2 §4 Placement, the END unit field — raw 45

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md`.

**The defect.** END takes its unit "from whichever of `BR_UNIT`, the dispatch pass, `RS_ITEM` or
`RV_SUBJECT` the verb set". Re-read here, no `RS_ITEM` exists: the driver initialises only `RS_ACT` and
`RS_SUCC` (`tools/unattended/unattended.sh:4913`). `--pass` and `--item` both land in `PK_ITEM` (`:4938`,
`:4942`), and `verb_rescope` and `verb_dispatch` both take `$PK_ITEM` (`:5056-5057`). `PK_ITEM` is also the
free-text item of `--park`, `--propose` and `--attest` (`:5049-5053`), which §3 bans from a line. `PH_SLUG`
is assigned only inside the `--phase` arm (`:5016`), and the driver runs under `set -u` (`:41`).

**Impact.** The spec cannot be followed as written. Read literally, the trap references an unbound name,
and verification measured that this aborts the rest of an EXIT trap, so the END line is silently lost; that
was not re-derived here. Read as `PK_ITEM` without a switch on the verb, the line carries the `--item`
text §3 bans, unvalidated on a refused call.

**Fix.** Name `PK_ITEM` as the source and read it only when `VERB` is `--dispatch` or `--rescope`, and
read `PH_SLUG` only for `--phase`. Write `unit` only when the value matches the unit-id shape, and set
`unit_bad=1` otherwise. Add an arm per unit-bearing verb, and a `--park --item` arm asserting the item
text is absent from the line.

**Left-shift.** The class is `memory/gotchas/spec-names-code-its-base-lacks.md`. A report-only extension
of the spec-tokens leg: an upper-case shell identifier backticked in a live spec's §4, beside a cited
driver line, must exist in that file at the spec's base. `RS_ITEM` is the case it would have caught.

---

### M4 — MEDIUM — unit 8 §2 S3, the decision-log bullet; §6 AC11 — raw 58

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** The fold of round 1's M9 classifies a decision-log row as the owner's when it carries "an
`OWNER RULING` prefix, `(owner, <date>)`, `(owner:` or 'owner call'". Counted here in
`memory/DECISIONS.md`: 16 rows carry `(owner`. Of those, 7 read `(owner, ` and 1 reads `(owner:`, and the
other 8 read bare `(owner)`, at lines 22, 23, 28, 29, 30, 74, 75 and 84. Two more rows read `Owner ruling`,
at lines 109 and 141. The adopted list therefore matches 8 of the 16 `(owner` rows that §4's own
rejection line counts, and S3's "any observed owner spelling" is false. AC11 exercises only
`(owner, 2026-09-01)`.

**Impact.** Half the parenthesised owner rulings read as decisions the run took, which is AC3's and
AC11's own red condition, and AC11 passes anyway.

**Fix.** Match `(owner` followed by `)`, `,` or `:`, plus a case-insensitive "owner ruling" and "owner
call". Add a bare `(owner)` row and an `Owner ruling` row to AC11's fixture.

**Left-shift.** Round 1's M9 left-shift, which the fold did not take: a report-only arm runs the
classifier over the tracked `memory/DECISIONS.md` and prints its hits per spelling AND its near-misses,
meaning rows that mention the owner and were not classified. That is charter §7's rule for a predicate
over a real population, and its near-misses would have included all eight bare `(owner)` rows and both
`Owner ruling` rows.

---

### M5 — MEDIUM — unit 8 §2 S1, the segmentation of journal lines; §6 AC1 — raw 3

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** S1 separates a slug's runs by "the driver's successful record-creating `--preflight`
calls". AC1 stages a rotated run-state FILE and checks that "facts come from their own files". No
criterion stages journal lines from two successful preflights and one refused preflight and asserts which
run each line belongs to, so the qualifier "successful record-creating" is never exercised.

**Impact.** A model that gives the live run every journal line of the slug passes AC1 and AC9. That
segmentation feeds the timeline, `phases-walked`, `killed-verb`, `refusal-loop`, and unit 9 S5's integrity
commitment, which is computed over "the journal lines attributed to this run".

**Fix.** Add an AC over a fixture `driver.log` holding a successful preflight, verbs, a refused
preflight, a second successful preflight and more verbs. It yields two runs whose timelines hold exactly
their own lines, and the refused preflight starts no run.

**Left-shift.** The spec-audit rule: *a qualifier in a scope item is observed by a fixture that stages
its negation.* "Successful" and "record-creating" each name a case the fixture must contain.

---

### M6 — MEDIUM — unit 13 §2 S3 and §6 AC3; unit 8 §2 S5 — raw 6

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** S3 derives `surfaced-park`, `retired-unit`, `no-rows` and `other` "from the record's own
last parked row" and gives no mapping. No parked kind carries those names: `PARK_KINDS` is `decision
abort override waiver proposal rescope dispatch review brief` (`tools/unattended/unattended.sh:355`).
`PARK_KINDS_OWED` together with `PARK_ACTS_OWED="retire supersede"` (`:369`, `:382`) makes a `rescope`
retire row owed. So one row is both a surfaced park and a retired unit, with no stated precedence, and
`supersede` has no place.

**Impact.** AC3's "names each with its sub-class" has no defined expected value, so any mapping passes.
Unit 8 S5 imports the same sub-classes for `nonterminal-merged`, in a different kit and built earlier, so
two independent inventions of one unstated rule can diverge with no gate noticing.

**Fix.** Put a table in unit 13 S3 that maps the last parked row to each sub-class, naming the kind and
the field or token that decides it, with a precedence for a retire row and a place for `supersede`. AC3
stages one row per mapping, plus one of a kind that must fall to `other`. Unit 8 S5 cites the table
rather than restating it.

**Left-shift.** The class is `memory/gotchas/two-answers-to-one-question.md`. Carry the same staged rows,
with the same expected sub-class, in both kits' fixtures, and add a PAIRS row to the existing parity leg
comparing the two copies, so both implementations are graded on one set of answers.

---

### M7 — MEDIUM — unit 8 §2 S7; §6 AC13 — raw 5

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** The fold of round 1's M14 added S7, which classes each owner turn as `launch`, `pre-run`,
`in-window` or `post-close` "against the window and the `--close` END". Those two reference points
separate three regions, not four, so the `launch` and `pre-run` boundary cannot be derived, and the build
defines neither term. No rule covers a run with no `--close`, such as an aborted one. AC13's "one before
the preflight, one at launch" puts both turns before the preflight START without saying which is which.
AC13's red settles one edge only: a turn after the close is not in-window.

**Impact.** Two correct readings give different per-position counts, and unit 9 S4 publishes those
counts, so the disagreement never reds.

**Fix.** Define each class by its boundary events. For example, `launch` is the session's first owner
turn when it precedes the preflight START, and `pre-run` is any other turn before it. `in-window` runs from
the preflight START to the `--close` END. `post-close` is after the `--close` END, or after the terminal
END when there is no close. For a run with no START, B1's start commit stands in. AC13 stages a turn on
each side of each boundary, plus one run with no close.

**Left-shift.** The spec-audit rule: *a classification into N classes names its boundaries, and its
criterion stages a case on each side of each.*

---

### M8 — MEDIUM — unit 8 §2 S6, the share attributed to a unit and a phase — raw 4

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** S6 reports "the share of calls and of wall time attributed to a unit and a phase", and
the build states no attribution rule. §4 rejects the extractor's sticky last-verb rule "alone" and names
nothing in its place. A grep of the build folder here finds no rule in the design research record either.
S6 names AC6 and AC7 as its observers, and neither touches the share.

**Impact.** The builder invents the rule without review, and the figure is published in the record's
Coverage section with nothing able to red.

**Fix.** State the rule. For example, an event is attributed to the unit and phase of the most recent
driver START at or before it in the same session, and is otherwise unattributed. Add an AC over a fixture
with known splits, including an event before any verb that must read unattributed.

**Left-shift.** A sibling of round 1's H6 rule: *a figure the public record publishes names its rule and
a fixture with a known value.* Unit 9 AC4 renders one value per class; extend it so that each model
figure reaching Coverage comes from a fixture with a stated expected value.

---

### M9 — MEDIUM — unit 8 §6 AC5, AC6 and AC12, against §2 S5 and S6 — raw 7

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** §5 promises that "the closed kind, item and state lists each drive their fixtures in
both directions". AC5 does that for `ANOMALY_KINDS` and AC12 for `CONFORMANCE_ITEMS`, and nothing does it
for `COVERAGE_STATES`. AC6 stages `absent`, `dead` and `partial`, and never `present` or `not-local`.
`not-local` is the transcripts' state for the 30 of 50 runs made on other nodes, per unit 9 §1. The
`refused-landing` sub-class the fold added to S5 has no criterion, because AC5 stages kinds, not
sub-classes. None of
`COVERAGE_STATES`, `present`, `not-local` or `refused-landing` appears anywhere in §6, checked here. (Its
skeptic judged the raw finding's main claim weak, namely that the constants are not pinned to S4's and
S5's literal lists, and it is not carried here.)

**Impact.** A state or sub-class the implementation drops disappears from every model and every record,
and no arm reds. That is the failure the rev-2 closed lists were folded in to prevent.

**Fix.** Pin `COVERAGE_STATES` in both directions against AC6's fixtures, as AC5 does for kinds, and
stage `present` and `not-local`. Add a `refused-landing` fixture, and pin the sub-class list the same way.

**Left-shift.** Charter §7's declared-population rule applied to the Inventory: an arm enumerates every
closed constant the model declares and requires each to have a both-ways arm, so the next constant
without one reds.

---

### M10 — MEDIUM — unit 6 §2 S5 and S8; §6 AC5, AC6 and AC8 — raw 12, 60

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md`.

**The defect.** The fold of round 1's H10 isolated the self-test's READS: S8 points `CLAUDE_CONFIG_DIR`
and `--transcripts` at scratch. Nothing isolates its WRITES. S5 sends extracts to
`%LOCALAPPDATA%\runlog\<repo-key>`, or the macOS or XDG equivalent, unless `RUNLOG_STATE_DIR` is set, and
no clause tells the self-test to set it. AC5 runs `extract` from two worktrees of a scratch clone, and the
key hashes that clone's fresh absolute common dir. AC6's "the store directory is unchanged" then observes
the real per-user store. AC8's red, "an arm reads the real store", is observed only by checking that a
variable is set.

**Impact.** Every self-test run leaves a new `<repo-key>` directory in the operator's profile, outside
TEMP, and nothing prunes them. AC6 can pass or fail on what another local session writes at the same
moment.

**Fix.** S8 sets `RUNLOG_STATE_DIR`, together with `HOME`, `USERPROFILE`, `LOCALAPPDATA` and
`XDG_STATE_HOME`, to scratch before any arm runs. Add an arm that plants a sentinel in a decoy real root
and reds if any arm touches it.

**Left-shift.** The class is `memory/gotchas/fixture-inherits-ambient-machine-state.md`. The spec-audit
rule: *a self-test's isolation clause enumerates every root the kit resolves, for reading and for
writing.* The fold answered the half its finding named.

---

### M11 — MEDIUM — unit 11 §6 AC6 — raw 9

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md`.

**The defect.** AC6 observes that "`git log` on `main` shows a `--no-ff` merge of the run branch pushed by
`tools/push-main.sh`". Git log records commits, never the tool that pushed them, and neither red condition
leaves a trace there. A `--no-verify` push and a hand-made marker produce the same history, and a
hand-made marker also satisfies `--landed`'s marker check.

**Impact.** The criterion cannot fail on the bypasses it names, so the landing route S6 exists to enforce
is asserted, never observed.

**Fix.** Observe the push through unit 4's `pushes.log`. The primary tree's hook writes it once this
build is merged there, and `core.hooksPath` routes every push through that hook. Look for a START with
`lander=1` and an END with `decision=full` or `decision=scoped` for the merge commit's sha. No line for
that sha is the `--no-verify` signature. Either state that a hand-made marker cannot be told apart there,
or drop that clause from the red.

**Left-shift.** The class is `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`. The
spec-audit rule: *each Red-when names evidence the criterion's own command can print.*

---

### M12 — MEDIUM — unit 2 §6 AC3; unit 4 §6 AC3 — raw 46

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md`.

**The defect.** Unit 2 AC3, rewritten by the fold of round 1's M18, sends TERM "after one second" of
`--close` with `GATE_CMD` set to a 20 s sleep, and grades that the driver exits promptly with
`exit=unclean`. A fixed second is not synchronised with the gate child. `--close` runs `observe_anchor`
(`tools/unattended/unattended.sh:2943`) and the Definition-of-Done loop (`:2982`) before
`run_bounded $GATE_CMD` (`:3085`). A TERM that lands during those short git children ends the driver
promptly whether or not a TERM trap exists, so the stated red case, "a TERM trap is added", is not
reliably observable. Verification measured about 0.12 s to the parse loop and about 0.72 s for an
equivalent anchor sequence against a local bare origin, which puts the gate child's start near the
one-second mark. Those figures were not re-derived here. (The raw finding's 1.16 s launch figure was
stale, and the race stands without it.) Unit 4 AC3 has the same fixed-second shape, against a hook that
does work before the bar.

**Impact.** The arm races on node speed. It can red for a timing reason, or pass against the exact
regression it exists to catch.

**Fix.** The `GATE_CMD` stub, and unit 4's `GOV_GATE_CMD` stub, write a ready file as their first act.
TERM is sent only after that file appears, with a bounded poll, and the arm asserts the child was
running when the signal arrived.

**Left-shift.** A gotcha record anchored on both suites: *a fixed sleep before a signal does not place
the signal inside the child it means to interrupt.* It sits beside the deferral record unit 2 S12 already
adds.

---

### M13 — MEDIUM — unit 2 §2 S11 and §6 AC10; unit 11 §2 S4 and §6 AC4 — raw 16

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md`.

**The defect.** Unit 2 S11 adds a run-log paragraph to protocol section 2 and one sentence to the verbs
preamble, and names AC10 as their observer. AC10 checks the adopter `--check`, `check-kit-versions.sh`,
byte identity of the copies at 1.20 and check 22, and reds only on the section 8 row or the example line.
Byte identity holds when neither copy has the paragraph. Unit 11 S4 and AC4 leave the sentence they add to
that paragraph unobserved in the same way.

**Impact.** The protocol text that tells an agent the run log exists, which unit 11 then extends, can be
missing while every gate is green.

**Fix.** Add to unit 2 AC10 an anchored grep for the section 2 paragraph in
`memory/guides/UNATTENDED-PROTOCOL.md` and for the preamble sentence in
`memory/guides/UNATTENDED-VERBS.md`. Add the same for unit 11's sentence in its AC4. The set already greps
rendered prose elsewhere, in unit 11 AC2.

**Left-shift.** The spec-audit rule: *byte identity between a template and its copy is parity, not
presence; a carrier a spec adds gets an anchored presence check.*

---

### M14 — MEDIUM — unit 1 §2 S5; §6 AC5 and AC7 — raw 14

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md`.

**The defect.** S5's main behaviour has no criterion: printing a producer file's parsed lines as JSON on
stdout, with the bad-line count and the resolved path on stderr. AC5 covers only the absent file, and AC7
checks only that `journal` names the resolved path. §5 calls the bad-line count "always printed".

**Impact.** A `journal` that prints nothing, or drops the bad-line count, passes every AC. It is the one
CLI a person uses to see what a producer wrote.

**Fix.** Add an AC over a fixture holding two good lines and one torn line: `journal --producer driver`
prints two JSON objects whose keys match the lines, and stderr carries a bad-line count of 1 and the path.

**Left-shift.** Round 1's S-to-AC token check would not catch this, because S5 and AC5 share `journal`.
The rule that does: *every CLI subcommand has a criterion over its success output, not only its absent
case.*

---

### L1 — LOW — unit 9 §2 S5; §6 AC5 — raw 22

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md`.

The fold added "A run with no journal lines records `commitment=none`", and no criterion observes it.
`verify` has no stated result on such a record. AC5 stages an edited journal and an untouched one, and
AC1 renders a journal-less run but asserts only its file name. Every run from before the journals renders
on this path, so a `verify` that exits 1 on it, or a renderer that hashes nothing, goes unobserved.
**Fix.** An arm in which AC1's journal-less fixture carries `commitment=none` and `verify` on it exits 0
with a named line.
**Left-shift.** `commitment=none` appears nowhere in §6, checked here. See "Classes across the set" for a
literal-presence check that flags it, and for why that check is a reviewer's aid rather than a gate.

### L2 — LOW — unit 10 §2 S1; §6 AC1 and AC2 — raw 23

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md`.

S1 reads records "from the index, not the working tree", and every AC runs over a fixture whose index and
working tree agree. AC4 counts git calls, which `ls-files` followed by `open()` also satisfies. A leg
reading the working tree passes, and then grades unstaged bytes at pre-commit. The fold of round 1's M12
added exactly this arm to unit 13 AC1 and not here.
**Fix.** Add an arm where the staged record violates S2 while the working copy is clean, which must red,
and the reverse, which must stay green.
**Left-shift.** The fold record's fourth practice: *when a finding's class has several carriers, edit
all of them or record the refusal.* "Reads the index, not the working tree" has two carriers in this set.

### L3 — LOW — unit 6 §2 S3, the keepalive join; §6 AC3 — raw 24

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md`.

S3 finds keepalive fires by joining them to a same-session `CronCreate` prompt "rather than matched by
wording", and §4 justifies that with 86 of 86 fires found against 73 of 86. AC3's fixture holds one
keepalive fire and does not require its wording to miss every known prefix. A prefix matcher passes, and
the 13 fires that wording misses would count as owner turns.
**Fix.** AC3's keepalive fire carries prompt wording that matches no known prefix, so only the join can
find it.
**Left-shift.** The class is `memory/gotchas/armed-but-unreachable-rule.md`: *a Red-when that names a
rejected alternative needs a fixture that alternative fails on.*

### L4 — LOW — unit 2 §2 S2, §4 Placement and §6 AC2 — raw 53

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md`.

The fold's exit enumeration reads `exit` lines "after the install line", near `:4925`. Every verb
function is defined above that line and runs after the install: `verb_phase` at `:2194`, `verb_landed` at
`:2264`, `verb_abort` at `:2482`, `verb_preflight` at `:2553` and `verb_close` at `:2914`. The property
holds today, re-checked here. Every `exit` between `fail()` at `:331` and `:4925` is awk program text or a
comment, and `tools/unattended/lib-unattended.sh` has none outside comments. But the likeliest future exit
site is inside a verb body, so §4's "a future exit site cannot slip past" is false. Such an exit would
record `exit=unclean` for an exit the driver chose, which unit 8 reads as `killed-verb`.
**Fix.** Enumerate `exit` across all of `unattended.sh` and `lib-unattended.sh`, excluding awk text and
comments, and exempt only the named pre-install lines, which are `:74`, `:275`, `:276`, `:279` and `:310`.
**Left-shift.** Charter §7: *gate the CLASS, not the instance.*

### L5 — LOW — unit 8 §2 S3, the first ledger bullet; unit 9 §2 S4, the ledger-source vocabulary — raw 62

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md`.

Unit 8 types the ledger's run-state sources as "parked decisions, rescope acts and overrides", and unit 9
types the vocabulary as `parked`, `rescope` and `override`. The driver owns this taxonomy, from
TOOL-aBoundedVerdict-5: `PARK_KINDS_OWED="decision abort override waiver"` and
`PARK_ACTS_OWED="retire supersede"` (`tools/unattended/unattended.sh:369`, `:382`). Its comment warns that
a reader taking a partial set gets the double count `history_exclude_re` exists to prevent. `abort` and
`waiver` appear in neither spec's list. Read narrowly, a preflight waiver (TOOL-cBriefedPilot-3) and an
abort's reason drop out of the ledger and the record's Decisions counts. Read broadly, overrides and
rescope acts count twice.
**Fix.** Enumerate the four owed kinds and the owed rescope acts in unit 8 S3, each with a ledger-source
token in `RECORD_SCHEMA`.
**Left-shift.** The class is `memory/gotchas/two-answers-to-one-question.md`. Where the unattended kit is
present, a self-test arm parses both constants from the driver and compares them with the ledger's list;
where it is absent, the arm announces its skip.

---

## Classes across the set

**The fold is the dominant source, and the blocker came from round 1's own fix.** By the Origin column,
15 raw findings sit in text the fold wrote and 9 in text where it answered a round-1 finding only in
part. That is 24 of 36, against 11 in rev-1 text that round 1 did not flag and one that straddles. The
record `memory/gotchas/fold-text-is-unreviewed-surface.md` measured the same majority on two earlier
builds. The fold shapes it names recur here. H5 is a fold writing a citation it did not re-derive. M2,
M4 and M10 are a fold answering one half of a finding. L2 is a fold widening one carrier while its
sibling keeps the old shape. H2 is the amendment that leaves its other half standing, which has a record
of its own. The blocker adds a shape the record does not yet name: the fold implemented a fix the REVIEW
proposed, and the review had stated that fix in its own voice without running it. A review's recommended
fix is unreviewed surface too. The synthesis rule under B1 is the left-shift, and the gotcha record could
carry it as a sixth shape.

**The catalogue reached this round.** Unlike round 1, `python tools/memory-tree/gotchas.py --for-diff
b21c5dd3..f698f6e6` selects 2 anchored classes and 5 universal ones. Four of the seven name shapes
confirmed here: `amendment-leaves-its-other-half-standing` (H2), `fold-text-is-unreviewed-surface` (the
split above), `staged-break-substitutes-a-synthetic-value` (B1's hand-built pair) and
`two-answers-to-one-question` (M6 and L5, and the two derivations B1 unifies). Whether the lenses were
primed with that checklist is not visible to this synthesis.

**Rules stated over populations the tree already holds, graded on fixtures the author built.** B1's rule
fails on 6 of 6 rotated pairs. H4's counts 1 of 6 records vacuously. M4's leaves 8 of 16 `(owner` rows
unclassified. H1's window for aLeakedHandle is already three days long. Each rule was written about a
population this tree holds, each criterion stages a hand-built fixture, and each defect shows the first
time the rule is run over the real population. Charter §7 already says to run a candidate predicate over
the real tree before wiring it and print hits and near-misses. The spec-audit rule: *a rule a spec states
over a population this tree already holds carries in §4 its output over that population, as a count and
its near-misses, measured when the spec is written.*

**"Observed by ACn" where ACn observes something else, still.** M5, M8, M9, M13, M14 and L1 are that
shape, and M1 carries it for unit 2. Round 1 proposed a check that each S item share a backticked token
with each AC it names, and it was not built. This synthesis measured the obvious stronger variant instead:
a throwaway script requiring every backticked literal in a spec's §2 to appear somewhere in its §6. It
flags 245 of the set's 340 such literals, because criteria usually observe an enumeration as "each member
of X" rather than by name, so it cannot gate. Its hits do include the unobserved tokens of at least eight
items here, among them `commitment=none` (L1), `refused-landing` and `not-local` (M9), `RUNLOG_STATE_DIR`
(M10), `CronCreate` (L3) and `project-owned` (M1). It is worth running as a printed reviewer's aid that
grades nothing.

**Recorded decisions not consulted, again.** TOOL-dClosedLexicon-11 records the rotation mechanics B1
depends on. TOOL-cFinalBerth-2 settled H4's ambiguity. TOOL-aQuenchedHarness-3 governs M1, and the fold
cited it for unit 2 alone, which is this class at the scale of a single citation. TOOL-aBoundedVerdict-5
owns L5's taxonomy, and TOOL-aWrittenMethod-1 with its two named exceptions governs H5. Round 1 named this
class; five of this round's 25 items repeat it.

**This run as its own test subject, again.** H1 and H2 fail on the run building the logger, as round 1's
B1, B2, B3, M5 and M20 did. The fold addressed those five, and two of its answers fail on this run again.
H1 reaches AC7 by a different path than round 1's B1 did, and H2 is the placement half of M20's answer.

## What this synthesis re-derived

- The thirteen blob shas at HEAD `f698f6e6`, and that no file under `tools/` or `.githooks/` differs from
  base `9fac2b53`.
- `git log --diff-filter=A --follow` over all twelve records of the six rotated builds, the dates of the
  first preflights and rotations, the rotation commit `9ea808cf`'s name-status, and the `keepalive:` facts
  of two rotated pairs.
- The `witness:` and `base:` facts in the creating commits of four run-state files, and the phase, witness
  ancestry and witness-to-base relation of all seven non-terminal records at HEAD.
- aLeakedHandle's landing commit `7d9e2d47`, and every later commit on this branch naming it in subject,
  path or content.
- The pre-push refusals at `:95`, `:102` and `:108` against the stdin loop at `:115-117`.
- In `tools/unattended/unattended.sh`: `set -u`, the absence of `RS_ITEM`, the `PK_ITEM` and `PH_SLUG`
  assignments, the verb dispatch lines, `PARK_KINDS`, `PARK_KINDS_OWED`, `PARK_ACTS_OWED`, the rotation
  lines, the `--close` sequence, the verb function definitions, and every `exit` before the install point.
- The absence of `RECALL_CLI`, `MAP_CLI` and `.unattended.conf` from both copies of the Skill, and the
  driver's reads of both keys.
- The `project-owned` rules in `tools/run-gates/kit.toml` and `tools/unattended/kit.toml`.
- The owner-spelling counts in `memory/DECISIONS.md` and their line numbers.
- The run mandate's landing clause and the Skill's no-commit-between-push-and-landed rule.
- The rev-1 text of every clause the Origin column classifies, read at `1dd6f3da`.
- The `gotchas.py --for-diff` selection for the fold, and the literal-presence measurement above.

## What this pass did not cover

- The design research record and the two prompts were not pinned subjects. The run mandate was read only
  at the landing clause H2 cites. The build brief prompt is untracked in this worktree and was not read.
- The 29 refuted findings are not reproduced or characterized here.
- Units 5, 7 and 12 drew no confirmed finding. Round 1's findings in those units were folded, and this
  synthesis did not re-verify each of those folds individually.
- Four figures come from verification and were not re-derived: M12's timings, M3's unbound-name trap
  behaviour, M2's twin-size estimate, and M1's statement that the rule's only gate arms cover agent-cap.
- No code exists yet. The specs were audited against a tree whose tool and hook files are byte-identical
  to base `9fac2b53`.
- No finding reopens the owner's 2026-09-13 rulings in the README. H2 concerns the fold's move from the
  worktree landing, which the mandate allowed and did not require, to the protocol's own route. S6 records
  that move and gives its reason.
- This record is not yet bound into the build index. The specs' records regions and the README's records
  line need re-rendering in the commit that lands it, as round 1's commit did.
