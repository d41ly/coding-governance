**Serves:** spec-audit TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1

# dDerivedDocket — spec audit of topic group G5, the switch-over with its CI, arming and docs, round 2

*Node `d`, 2026-09-14. The second Tier-2 adversarial pass over the seven G5 specs: remote CI (unit
32), the delegated signing (33), the switch-over and its landing reconcile (34), arming and the
real-tree staged breaks (35), the memory-tree docs and agent carriers (36), the charter template
(PLAY-dDerivedDocket-1) and the adopter runbook (DEPL-dDerivedDocket-1). The pass was aimed at the
text the round-1 fold introduced, using each spec's §9 rev-2 line as the index, and at whether each
round-1 fix actually holds. Four primed finder lenses ran, then a skeptic stage prompted to REFUTE
each finding in five batches, then this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md`
with its roster and edge tables, and the round-1 record
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round1.md`.
Sibling specs outside G5 were read wherever an edge or an interface named them: unit 2 most of all,
because the landing reconcile now names its verb, and units 9, 11, 12 and 13. The G2 round-2 record
was read where it meets unit 34. Every high below was re-checked before it was written down, against
the sibling specs it cites and, where it rests on a tool, against source at `abac6d59`. The sites
read are named in each entry. Since BASE the only files changed
outside this build's folder are `memory/LIVE.md`, `memory/ledger/2026-09.md` and
`memory/backlog/TOOL.md`, so every tool line cited is byte-identical between BASE and the tree this
report was written in. The seven blobs below are the ones the spec set holds at `18cf0c1b`, the fold
commit, and each was confirmed equal to the working file before this report was written.*

**Round: 2.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md@63f9d20f1544b131ad9fd8932790e6608afa7ff7`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-33.md@e450666f599ce4a0e024d3593341f39d0ff30e38`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md@76d3ea8e1f6744950eef4a80f09d2075573e04fe`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-35.md@169de8f5d5a5f78b701a0632165e8088daf1f7c7`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-36.md@058d238cd8b177a8dbd608f914bdd1ad727520ac`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-PLAY-dDerivedDocket-1.md@3fb27375658c792596c4a05dd2352ef3408b5f4b`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-DEPL-dDerivedDocket-1.md@21cb9927b99df3b2a39e73b96e687515e88e4b2b`

## Verdict: CLEAN WITH FIXES

No blocker stands. Round 1's three blockers were folded. The one finding a finder rated BLOCKER this
round, id 36, is adjudicated HIGH as H1 below, because the mechanism its fold needs is one a sibling
spec already carries. What stands is six HIGH defects carried by nine finding ids, 19 MEDIUM defects
carried by 24, and six LOW defects carried by six. Review shape: raw 64, confirmed 39, refuted 25,
unverified 0, precision 0.61. The run-integrity section below reads complete.

The weight sits where round 1's did, in unit 34 §4 "The landing reconcile". Round-1 B2's fix holds
as a verb, unit 12's landing form of `--ingest`, and does not hold as a procedure.

- Step 1 names `push-main.sh --prepare`. Unit 2 specifies that verb to merge the other way and to
  abort on the very conflict step 1 resolves (H1).
- The confirmation rule reads text, so this build's own ledger and rehearsal park the flips the rule
  exists to confirm (H2). It also names no command for either of its two conditions (M6).
- The delta is spelled backwards (M3). Step 3 signs from line numbers read in a tree step 1 replaced
  (M4). Step 5 writes a watched file that step 6's commit cannot carry past pre-commit without a
  re-stamp (M2).

With the rehearsal's own records (M5), those are 11 of the 39 ids. The reconcile runs outside any
unit pass and after the closing review. Its one pre-landing observation, AC15, cannot see H2 or M2
as written, because its scratch repository carries neither this build's own records nor the
manifest's staged hook.

The other four HIGH defects each stop a unit's own criterion. Unit 34's AC3 cannot print zero
differing ids (H3). Unit 35's AC8 reds on two asks the round-1 fold commit itself filed (H4). Unit
32's AC12 expects a DRIFT line that names a key (H5). Unit 35 sets its hooks path with a mode that
writes nothing (H6).

Convergence under `memory/guides/BUILD-METHOD.md` M4: the blocker count fell from 3 to 0, so
BLOCKED's disposition does not apply. The prescribed act is to fold these fixes and stop
spec-auditing these seven specs. Four folds need a local decision first, and each entry states it:
H4 (which unit writes two dispositions), M1 (the tail the flip's re-signing runs under), M10 (a
held-job route or a sweep option), and M15 (edit two authored lines or record the omission). The
fold's own text is unreviewed surface (`memory/gotchas/fold-text-is-unreviewed-surface.md`): 38 of
this round's 39 ids sit in round-1 fold text, in a record the fold commit wrote, or in the half of a
round-1 fix it left standing. The rev-3 fold meets the closing diff review. That review should take
the §9 rev-3 lines as its index and read unit 34's reconcile first. Class item 2's AC15 extension is
what lets a unit pass, rather than the landing, see the next defect there.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

Every counter that could make this run incomplete is zero, so this run is complete. The finding set
is complete for what the four lenses were primed to hunt. That is not a claim that G5 holds no other
defect. It is a claim that nothing was lost between the lenses and this page. So a "no confirmed
finding" below means four lenses and a skeptic stage found nothing, which is evidence but not proof.

The pipeline's duplicate count of 0 comes from its own exact-match dedupe. On reading, seven groups
each describe one defect reported by two or three lenses: 1 and 39; 21 with 36 and 52; 26 and 51;
8 and 30; 28 and 54; 17 and 33; and 19 and 42. Id 52 also carries the defect id 29 reports, as one
of its halves. Each group is folded into one entry below, and every count on this page stays per
finding id.

## Review shape

Raw 64, confirmed 39, refuted 25, unverified 0, precision 0.61. The 39 confirmed ids collapse to 31
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 9 | 6 |
| MEDIUM | 24 | 19 |
| LOW | 6 | 6 |

**Severity is adjudicated here, not copied from the finders**, on G5 round 1's scale, so this
group's two rounds compare.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  layer which stays inert or broken while its suite reads green. In each case the fold is local to
  one or two specs, or needs one decision.
- MEDIUM covers three kinds of defect: a contradiction between specs with a bounded consequence, a
  declaration or step an edit owes, and a rule whose break no criterion can see. A criterion whose
  wording names an output its command cannot print sits here when the property it guards stays
  observable by an obvious equivalent. Round 1 held that case at MEDIUM as its M26.
- LOW is the same kinds of defect where the reachable harm is small.

G2 round 2 used a narrower HIGH, one whose fold cannot be settled locally. Under that scale at
least H3, H5 and H6 would read MEDIUM, so the two groups' HIGH counts do not compare directly.

Six findings move.

- Down: 36, from BLOCKER to HIGH. Its fold is a rewrite of one step and one edge, over a reconcile
  that unit 2's own refusal names and unit 3 S6 already sequences. That is the reasoning round 1
  used to hold its H1 at HIGH.
- Up to HIGH: 39, from medium, because it joins 1. Also 13, from medium: the spec's own procedure
  produces AC5's failing reading, and the observation it guards is round-1 H6's subject.
- Up to MEDIUM: 51 and 33, from low, because each joins a medium finding (26 and 17). Also 11, from
  low: G1 round 2 (its M11) and G2 round 2 (its M13) adjudicated an unobserved kit version move at
  MEDIUM, citing the refused adopter pull TOOL-dMuffledSentinel-3 records.

Precision fell from round 1's 0.75 to 0.61, on four lenses again. Four observations about the
confirmed set follow.

- **Fold text dominates.** 38 of the 39 ids sit in text a §9 rev-2 line names, in a record the fold
  commit wrote, or in the half of a round-1 fix that line left standing. The one exception is M14
  (4), the workflow's triggers, which rev-1 wrote and no round-1 finding named.
- **The fold wrote records as well as text.** Commit `18cf0c1b` filed two OPEN asks under this
  build's slug in `memory/backlog/TOOL.md`, the trail protocol §11 requires for a declined
  discovery. No spec disposes them (H4). A fold's records are unreviewed surface too, and the
  gotcha names only its text.
- **The fold wrote lists and staged a prefix.** S5 in unit 32 promises one staged break per
  property and stages seven of twelve. §5 in unit 34 lists eight refusals and AC17 stages four. The
  M19 fold staged U3 and U4 and left T4 and T5. The confirmation rule has two conditions and AC15
  stages one. This is round 1's class item 6 in a new form (class item 5 below).
- **The criterion-gap class is still present.** `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  returns as H5, H6, M10 and M18. The fold's new criteria were written to observe round-1 fixes, and
  four of them name an output their command does not print.

## Round-1 fixes: what this round found against them

"No confirmed finding" means four lenses and a skeptic stage confirmed nothing against the fix. It
does not certify the fix.

| Round 1 | Spec | Round-2 reading | Round-2 entries |
|---|---|---|---|
| B1 | 34, 35 | holds: S17 mints and files the triage ask, and AC16 observes it; the status proof and the close's read do not | H3, H4, M7 |
| B2 | 34 | the verb holds; the procedure around it does not | H1, H2, M3, M6 |
| B3 | 34, 33 | the route holds; the signer reads the wrong tree, and the rehearsal leaves its records behind | M4, M5, L3 |
| H1 | 34 | the rule holds; the landing commit that writes it owes a re-stamp | M2 |
| H2 | 32 | the clone route holds; its attribution cannot be observed | H5 |
| H3 | 32 | holds; the assertion step is read by no criterion | M13 |
| H4 | 32 | no confirmed finding against the matrix; each row now runs its argv unresolved | M12 |
| H5 | 32 | no confirmed finding | none |
| H6 | 35 | does not hold as written: the named script writes no hooks path | H6 |
| H7, H8 | 33 | no confirmed finding | none |
| M1 | 33, 34 | no confirmed finding in unit 33; the writer's header-cell refusal is unstaged | M7 |
| M2 | 34 | no confirmed finding | none |
| M3 | 34 | the kit-local check holds; it refuses the flip with no re-plan step, and half its arms are unstaged | M1, M7 |
| M4 | 34 | holds under shards; the builds-mode arm with no `BACKLOG.md` is unstaged | L5 |
| M5 to M8 | 34, 32, 36 | no confirmed finding | none |
| M9 | 32 | the bound and the marking hold; the captured output is only the sweep's header | M10 |
| M10 | 32 | holds for the wall; the 360-minute cap is read and never staged | M13 |
| M11 | 32 | holds for the uploads; the copy step and the tee are read by no criterion | M11 |
| M12 | 35 | no confirmed finding | none |
| M13 | PLAY | holds for the template and `AGENTS.md:582`; two authored carriers keep the old claim | M15 |
| M14 | PLAY | the fence holds; the runbook is not told | L6 |
| M15 | DEPL | no confirmed finding | none |
| M16 | DEPL | the argument shapes hold; step 4 omits the archives, and the fold's added command cannot be resolved | M16, M18, M19 |
| M17 | 32 | read, not staged: five properties and one step have no break | M13 |
| M18 | 32 | no confirmed finding | none |
| M19 | 33 | holds for U3 and U4; T4 and T5 carry the same gap | M9 |
| M20 | 33 | no confirmed finding | none |
| M21 | 34 | holds; the `filed` values it recomputes from are unchecked | L4 |
| M22 | 34 | no confirmed finding | none |
| M23 | 34 | AC21 stages the zero; AC10's tuple clause cannot be shown | L5 |
| M24 | 34 | split as asked; the cache-version bump is visible to neither half | M8 |
| M25, M26 | 36 | no confirmed finding | none |
| L1 | 32 | half holds: line 25 is graded, line 2 is not, and neither header's new content is read | L1, L2 |
| L2 | 34 | no confirmed finding | none |
| L3, L4, L5 | 36, PLAY, DEPL | no confirmed finding | none |
| none, rev-1 text | 32 | the triggers were never read | M14 |
| none | DEPL | the runbook stops at the switch-over commit | M17 |

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 36 | HIGH | H1 | 34 | §4 The landing reconcile, step 1 and the paragraph before the steps; §3 Edges |
| 21 | HIGH | H1 | 34 | §4 The landing reconcile, the verb paragraph and step 1; §6 AC15; §3 Edges |
| 52 | HIGH | H1 | 34 | §4 The landing reconcile, the verb paragraph and step 1; §3 Edges; §6 AC15 |
| 22 | HIGH | H2 | 34 | §4 Confirmation, and A moved tip; §8 F7; §6 AC15 |
| 23 | HIGH | H3 | 34 | §6 AC3, against §2 S11, S17 and §4 Rollout steps 6 to 8 |
| 53 | HIGH | H4 | 35 | §2 S9; §4 This build's own close; §6 AC8 |
| 1 | HIGH | H5 | 32 | §6 AC12 |
| 39 | HIGH | H5 | 32 | §6 AC12 |
| 13 | HIGH | H6 | 35 | §2 S2; §4 Rollout step 3; §6 AC5 |
| 56 | MEDIUM | M1 | 34 | §5 error states; §4 Rollout step 5; §8 F11 |
| 28 | MEDIUM | M2 | 34 | §4 The landing reconcile, steps 5 and 6 |
| 54 | MEDIUM | M2 | 34 | §4 The landing reconcile, steps 5 and 6 |
| 29 | MEDIUM | M3 | 34 | §4 The landing reconcile, the delta sentence |
| 26 | MEDIUM | M4 | 33 | §2 S11; §4 T4 and T5; against 34 §4 reconcile steps 1 to 3 |
| 51 | MEDIUM | M4 | 33 | §2 S11; §4 T4 and T5 |
| 27 | MEDIUM | M5 | 34 | §6 AC20; §4 reconcile steps 2 and 3; §4 Rollout steps 11 and 12 |
| 9 | MEDIUM | M6 | 34 | §4 Confirmation; §6 AC15 |
| 8 | MEDIUM | M7 | 34 | §2 S1 and S17; §5 error states; §6 AC17 |
| 30 | MEDIUM | M7 | 34 | §2 S1; §5 error states; §7; §6 AC17 |
| 11 | MEDIUM | M8 | 34 | §2 S9; §4 What the one commit carries; §7 |
| 6 | MEDIUM | M9 | 33 | §2 S3; §6 AC4 and AC5 |
| 37 | MEDIUM | M10 | 32 | §2 S8 and S9; §5 observability |
| 2 | MEDIUM | M11 | 32 | §2 S8 and S9; §6 AC10 and AC11 |
| 38 | MEDIUM | M12 | 32 | §3 Non-goals, the runner-image sentence; §2 S4 |
| 3 | MEDIUM | M13 | 32 | §2 S5 and S1; §6 AC1, AC2 and AC4 |
| 4 | MEDIUM | M14 | 32 | §2 S2, S3 and S4; §3 Non-goals; §4 Security |
| 17 | MEDIUM | M15 | PLAY | §2 S8; §6 AC11 |
| 33 | MEDIUM | M15 | PLAY | §2 S8 and S4; §6 AC11; §3 and §10 |
| 19 | MEDIUM | M16 | DEPL | §2 S2; §4 step 4; §6 AC3 |
| 42 | MEDIUM | M16 | DEPL | §4 step 4 |
| 58 | MEDIUM | M17 | DEPL | §4 steps 4 and 5; §3 Edges; §6 AC3 |
| 18 | MEDIUM | M18 | DEPL | §4 step 4; §6 AC3 |
| 41 | MEDIUM | M19 | DEPL | §4 Proposed text; §4 Files touched; §6 |
| 5 | LOW | L1 | 32 | §2 S7; §6 AC8 |
| 32 | LOW | L2 | 32 | §2 S7; §6 AC8 |
| 7 | LOW | L3 | 33 | §2 S11; §6 AC13 |
| 10 | LOW | L4 | 34 | §2 S1; §6 AC2, AC3 and AC4 |
| 12 | LOW | L5 | 34 | §2 S10; §6 AC10 and AC21 |
| 34 | LOW | L6 | PLAY | §2 S2; §3 Edges; against DEPL §2 S4 |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number, so "unit 34" is `2026-09-14-spec-TOOL-dDerivedDocket-34.md`. "PLAY" and
"DEPL" are `2026-09-14-spec-PLAY-dDerivedDocket-1.md` and `2026-09-14-spec-DEPL-dDerivedDocket-1.md`.
Every tool line number is at `abac6d59`.

## Blockers

None. The candidate was H1, which a finder rated BLOCKER, and it was weighed against the scale's
second clause. As specified, the landing reconcile cannot run on the routine case, so the first
clause holds. The fold needs no mechanism the set lacks, though. Unit 2's `--prepare` refusal names
the manual reconcile, a plain merge of the tip on the run branch. Unit 3 S6 already sequences
"reconcile onto the run branch, then `--prepare`". The fold rewrites one step of unit 34 and adds
one edge. H2 was weighed too. It parks the routine landing, but its fold is a structural definition
built on unit 6's parser, and F7 has already recorded the decision it implements. Both can also be
caught in unit 34's own pass rather than at the landing. H1 reds AC15 as written, and H2 reds it
once the fixture carries what class item 2 asks for.

## High

### H1 — step 1 names `--prepare`, which never leaves the merge that steps 2 to 6 conclude (21, 36, 52)

**Where.** Unit 34 §4 "The landing reconcile": the verb paragraph, with its MERGE_HEAD and HEAD^2
sentence, and step 1; §3 Edges, where no edge names unit 2; §6 AC15. These are read against unit 2
§2 S1, S2 and S7, its §4 "Data model", its §4 "`--prepare --slug <slug>`" steps 4 to 6, and its §6
AC3 and AC8. Also unit 3 §2 S3 and S6, and unit 10 S2.

**Defect.** Step 1 says `push-main.sh --prepare` "merges the tip in place". It says the merge "stops
conflicted" when the tip's shards moved, and that the reconciler then takes the branch's side of
each view and archive path. Unit 2 specifies the opposite on every count, re-read for this report.

- `--prepare` checks the advertised tip R out detached and merges B onto it (unit 2 §4 step 4). T^1
  is therefore the tip and T^2 is B's old tip (the data model; AC3).
- On any conflict it runs `git merge --abort`, checks B out at its old tip and exits 1. Its refusal
  names `git merge <remote>/<def>` on B as the reconcile to do first (§4 step 6; S2; AC8).
- It refuses without `--slug`, exit 2 (S7). Step 1 passes none.

So on the routine landing no conflicted merge ever exists for steps 2 to 6 to conclude. After a clean
`--prepare`, the paragraph's "after a clean one it is HEAD^2" names B's old tip, not the tip. And
with R checked out, R's pre-switch attributes and driver run that merge. Unit 10 S2 claims the view
refusal only where the post-switch tree's attributes govern (id 52's point). Unit 34 carries no edge
to unit 2, which is how the contradiction survived the fold.

**Impact.** The row driver's view refusal makes the conflicted case certain whenever main's shards
moved since the fork. Round 1 measured that as the routine landing: 64 new OPEN ids in the seven
days to BASE (its B3). In that case `--prepare` exits 1 with B restored, and steps 2 to 6 have no
merge. AC15 stages exactly that case and asks the six steps to run to completion, so it cannot pass.
After a clean `--prepare`, an operator following the paragraph hands B's old tip to `--ingest`. The
landing form admits only the resolved default tip, so it refuses. As specified, the reconcile the
round-1 B2 fold wrote cannot run.

**Fix.**

1. Rewrite step 1 as the reconcile unit 2's refusal names: `git merge --no-ff <tip>` on the run
   branch B. HEAD is then post-switch, so unit 10's refusal governs. Take the branch's side of each
   view and backlog-archive path.
2. Run steps 2 to 6 inside that merge and conclude it. The tip is MERGE_HEAD during the merge and
   HEAD^2 of the concluded reconcile merge.
3. Only then run `push-main.sh --prepare --slug dDerivedDocket`. It merges clean, because B contains
   the tip, and it satisfies unit 3 S3's `--prepared`.

Add consumes-from `TOOL-dDerivedDocket-2` and `TOOL-dDerivedDocket-3`, with the reciprocal hands-off
in unit 2. Have AC15 stage `--prepare`'s refusal on the conflicting fixture first, then the manual
merge, then the six steps. Write the delta as M3 states in the same fold.

**Left-shift.** Class item 1. Unit 37, adopted in the fold, extends the spec-tokens leg to join
hands-off payloads. Extend the same join so that a backticked verb whose tool a sibling spec defines
requires a consumes-from edge to that sibling. It would print unit 34 to unit 2 as a hit. As a
near-miss it would also print the flag set: unit 2 spells the verb `--prepare --slug <slug>`, and
unit 34 omits `--slug`.

### H2 — the confirmation rule reads text, so this build's own records park the flips it exists to confirm (22)

**Where.** Unit 34 §4 "Confirmation, with design A6 kept rather than relaxed" and "A moved tip is
re-reconciled from step 1"; §8 F7; §6 AC15. These are read against §4 "Staged REDs" ("Each RED is
copied verbatim into the unit's acceptance ledger"), §6 AC20, unit 35 S5 to S7, and unit 11 S8.

**Defect.** The rule confirms an id only if "no line added on the branch after the switch-over
commit names it", with no limit on which files count. After the switch-over this branch adds lines
that name real ids, by design.

- The acceptance ledger copies the V1, V10 and V13 REDs verbatim, and each names an id.
- AC20's rehearsal prints each CONFIRM entry, and the ledger records what AC20 printed.
- Unit 35's ledger cites real ids in its S5 to S7 readings.
- After a push race, the re-reconcile meets the first attempt's committed step-2 status worksheet,
  which names every census id.

The rule's first condition compares the switch-over parent's legacy row with "the merge-base". After
a first reconcile merge, that base is the previous tip. So an id main flipped both before and after
that tip fails the first condition too.

**Impact.** Every id main flipped before AC20's rehearsal is CONFIRM again at the landing and is
named in the ledger, so it parks. After any race, every flip of a pre-existing id parks. That is F5's
option (a), the outcome the owner's delegation exists to avoid. AC15's scratch repository holds none
of these records, so it stays green.

**Fix.** Define "acted on" structurally. It means a record added after the switch-over, in some
`memory/builds/*/BACKLOG.md`, whose target is the id: a disposition, a REOPEN, a SEV row or an ask
row, read through unit 6's parser. It never means a grep over every added line. Pin the first
condition to the original fork point, the switch-over's merge-base with the tip it forked from,
rather than the current merge-base. Record the definition as a §9 line, since it is F7's reading of
design A6 made precise. Add two AC15 arms, and require both to confirm: one in which a ledger line
names the untouched flip's id, and one that re-reconciles after a second tip.

**Left-shift.** Class item 2. The record is `memory/gotchas/inputs-inside-the-subjects-reach.md`:
the rule's input "a line names it" is partly supplied by the build that the rule grades.

### H3 — AC3's "zero differing ids" fails on two ids the specs make differ (23)

**Where.** Unit 34 §6 AC3, against §2 S11 and S17 and §4 Rollout steps 6 to 8. Unit 33 §2 S4, its
rule T1 and its AC6. Unit 11 S8.

**Defect.** Unit 11 S8's prediction applies only the signed records' verdicts. Unit 33's T1 excludes
TOOL-aWeighedCompass-3 from the triage, and its AC6 finds it only in the exclusions list, so the
prediction reads that ask's legacy OPEN. S11 then writes a WONTDO for it at rollout step 6, before
step 8 confirms the per-id report, and AC11 requires that WONTDO. The triage ask S17 files appears in
no prediction row at all. AC3 demands zero differing ids and grants one exception, the `TRIAGE-ASK`
substitution.

**Impact.** A correct switch-over shows TOOL-aWeighedCompass-3 as a differing id. It shows
`<triage-id>` too, when the comparison iterates the JSON's ids. AC3 is the flip's status proof, at
its most consequential commit, and it cannot pass as written. The builder either waves a difference
through by hand or stops.

**Fix.** State both exceptions in AC3. TOOL-aWeighedCompass-3 compares against WONTDO decided by
S11's disposal in this build's file, and `<triage-id>` compares against KEEP. The alternative is to
give unit 11's prediction the superseded disposal as its own class.

**Left-shift.** Class item 3: a proof against a prediction lists each write the pass makes outside
the predicted set as a named exception.

### H4 — two asks the fold filed migrate into this build's file, and nothing disposes them (53)

**Where.** Unit 35 §2 S9, §4 "This build's own close", and §6 AC8. These are read against
`memory/backlog/TOOL.md:468-469` as the fold commit `18cf0c1b` wrote them, unit 34 §2 S1 and S17,
unit 33 §4's triage population, unit 11 S7, and unit 17 §4 (`asks-disposed`, T3).

**Defect.** The round-1 fold commit filed TOOL-dDerivedDocket-38 and TOOL-dDerivedDocket-39 as OPEN
rows in `memory/backlog/TOOL.md`. That is the trail protocol §11 requires for a declined discovery. Re-checked for this report, they are the
only shard rows under this build's slug. At the switch-over their slug homes both in
`memory/builds/dDerivedDocket/BACKLOG.md`, and unit 34's writer transfers them as live asks. Nothing
then disposes them.

- Unit 11 S7 turns only terminal tokens and holds into dispositions, and OPEN is neither.
- Unit 33's triage population is asks on terminal builds, and this build is not terminal when it
  signs.
- Unit 34 S17 files a KEEP only for the triage ask.
- Unit 35 S9 assumes every homed ask is already terminal or disposed, and names only `<triage-id>`.
  Its declared writes, which its AC7 checks, cannot add a disposition row.

**Impact.** AC8 reds at unit 35's pass. At `--close`, `asks-disposed` T3 is unmet, because an ask in
the build's file has no disposition row and is not terminal. Once every unit is CLOSED the build is
terminal, so V10 reds reconcile step 6 and the landing bar. Any declined discovery a later pass files
in the shards before order 34 joins them.

**Fix.** Give one spec the write. This takes a decision.

- Either unit 34's writer files a KEEP in the `--as` file for every census ask homed there that
  derives OPEN. That generalizes S17, and AC16 extends to read it.
- Or unit 35 S9 writes one KEEP per live ask in this build's `BACKLOG.md`, citing its §11 decline,
  and adds that file to its Files touched.

Either way, S9 and AC8 name TOOL-dDerivedDocket-38 and TOOL-dDerivedDocket-39 beside `<triage-id>`.

**Left-shift.** Class item 3. A documented check for every fold: any shard row it files under this
build's slug names, in the same commit, the unit that disposes it. At spec time,
`grep -n 'dDerivedDocket-[0-9]* · OPEN' memory/backlog/*.md` lists the population S9 must name.

### H5 — unit 32's AC12 expects a DRIFT line that names a key, and `--check` names none (1, 39)

**Where.** Unit 32 §6 AC12, the H2 fold. It is read against `tools/playbook/render_playbook.py:594`
and `:612-613`, and `tools/playbook/adopt-playbook.sh:59`, re-read for this report.

**Defect.** AC12 requires `adopt-playbook.sh --target . --check`, in a clone at a second path, to
print "DRIFT naming `PRIMARY_TREE_A`". The wrapper execs the renderer. Its check branch prints one
fixed sentence, `render-playbook: DRIFT — the charter region differs from a fresh render`, and
returns. The per-placeholder `derived   PRIMARY_TREE_A = …` notes print only in write mode, after
`--check` has returned. No unit in the build changes that output.

**Impact.** AC12 cannot pass as written. Its purpose also goes unobserved, which is to show that the
clone path, and no other node fact, is what drifts. A second-path clone that drifted for any other
reason prints the same line. So whether cloning to `C:/projects/coding-governance` is enough to make
the per-sha verdict green, round 1's H2, rests on reading the workflow text alone. If a second fact
also drifts on the runner, the first sign is the first live run after landing.

**Why HIGH.** Id 39 was rated medium and joins id 1. AC12 is the only pre-landing observation of
round-1 H2's fix, and it cannot pass as written, the class round 1 put at HIGH as its H8.

**Fix.** Attribute the drift in write mode. Render the second-path clone into a scratch copy with
`render_playbook.py --target <clone>`, without `--check`, and record its
`derived   PRIMARY_TREE_A = <second path>` note. Diff the region against the tracked `AGENTS.md`,
and require every differing line to carry the second path. Keep the bare `--check` DRIFT line as the
red reading, and drop "naming `PRIMARY_TREE_A`" from it.

**Left-shift.** Class item 6.

### H6 — unit 35 sets the hooks path with the script's check mode, which writes nothing (13)

**Where.** Unit 35 §2 S2, §4 Rollout step 3 and §6 AC5. These are read against
`tools/check-wiring.sh:110-116` and `:258-262`, re-read for this report, and unit 13 S5 and AC12.

**Defect.** S2 and rollout step 3 set `core.hooksPath` by "running the clone's own post-switch
`tools/check-wiring.sh`", with no mode. The bare form is `--check`. With the path unset, it prints
`UNWIRED hooks — core.hooksPath unset` and writes nothing. Only `--fix` or `--session` writes
`.githooks`. AC5's relative arm reads a `hooks own-tree` note that only `--session` prints (unit 13
S5), and AC5's only command is `git commit`. Unit 13 AC12 spells both modes.

**Impact.** Followed as written, the primary scratch tree has no hooks. S7's `commit-msg` refusal
(AC6) never fires. The relative arm's reading, a commit landing with no recipe, cannot be told apart
from an unset path, which is AC5's own first Red-when. The unit cannot pass without an unrecorded
fix-up, or without a hand-set `git config`, which the fold's settlement in §8 F5 excluded. Round-1
H6's fix does not hold as written.

**Why HIGH.** It was rated medium. The spec's own procedure produces the failing reading. The
observation it guards is the one real-content observation of unit 13's layer, round-1 H6's subject.

**Fix.** Spell `bash tools/check-wiring.sh --fix` in S2 and in rollout step 3. Add to AC5 that
`bash tools/check-wiring.sh --session`, run in the primary scratch tree after the relative arm,
prints the `note` line naming the straggler with `hooks own-tree`, and that the ledger records it.

**Left-shift.** Class item 1, since a step that runs a sibling's tool names the mode that has the
effect it relies on. Also class item 6.

## Medium

The first seven entries sit on the flip and its landing, and M1 is the likeliest of them to fire.
M8 and M9 are criterion gaps in units 34 and 33. M10 to M14 are unit 32's, and M15 to M19 are the
charter's and the runbook's.

### M1 — the flip's staleness refusal fires on the routine path, and no step re-plans (56)

**Where.** Unit 34 §5 error states (the F11 refusal), §4 Rollout step 5, and §8 F11. These are read
against unit 11 S6 and S10, and unit 33 S1, S11 and AC1.

**Defect.** F11(c) makes `--write` refuse when a tracked worksheet's data rows differ from what
`--plan` computes at the switch-over's tree. The only worksheets are the pair unit 11 files at its
own pass, and unit 33 signs that pair by default. No rollout step in unit 33 or 34 re-plans or
re-signs at order 34. Three things move the planner's output between orders 11 and 34.

- A pass files a §11 decline row. H4's two rows show the pattern.
- Any shard line shifts, because the triage `source` column is `<file>:<line>`.
- A pass commit's message names an ask, which moves unit 11 S6's `commit-names-ask` basis. Unit 30
  works on TOOL-aHoistedPass-37 and TOOL-aHoistedPass-40, both asks on a CLOSED build.

**Impact.** `--write` refuses at the flip, and no recovery is specified. The operator improvises a
re-plan and a re-sign at the most consequential commit, choosing record names and a unit id for
records of units already CLOSED. The refusal writes nothing, which keeps this MEDIUM.

**Fix.** Before rollout step 5, run
`migrate_backlog.py --plan --record memory/builds/dDerivedDocket/build --record-as TOOL-dDerivedDocket-34`
at the switch-over's parent. Run the signer over that pair through unit 33 S11's `--worksheets`,
under a tail unit 33 names; `switch` is one candidate, and naming it is the local decision. Feed
those records to `--write`. AC2 and AC3 then compare against the re-planned census and per-id report.

**Left-shift.** Class item 3.

### M2 — the landing writes a watched file, and its commit carries no re-stamp (28, 54)

**Where.** Unit 34 §4 "The landing reconcile", steps 5 and 6. These are read against
`memory/guides/SESSION-KICKOFF.md:6`, whose `watch:` line names `.memory-tree.conf`, against
`skills/session-kickoff/manifest-check.sh:408-421` (C5s), and against `.githooks/pre-commit:54`, all
re-read for this report.

**Defect.** Step 5 writes `ASK_CUTOFF` into `.memory-tree.conf`. Step 6 concludes the merge, or
commits the follow-up, and nothing re-stamps. `.githooks/pre-commit` runs the manifest check's
staged leg. Its C5s arm refuses any staged watched change whose staged `last-audit` stamp equals
HEAD's, and tells the committer to bundle the re-stamp into that commit. Every other watched edit in
this group carries its re-stamp: unit 34's own S12, unit 35 S10, unit 36 S7 and PLAY S6.

**Impact.** Whenever the ingest moves the cutoff, pre-commit refuses the landing's commit, outside
any unit pass and after the closing review. That is round-1 M8's class, brought back by the H1
fold. The refusal names its remedy, so the landing is delayed rather than lost. One finder's claim
that `--no-verify` is the only way past it is overstated. The charter's kickoff-manifest merge
exception also asks for a post-merge fresh audit when a merge brings in watch-touching commits, and
the reconcile names no such step.

**Fix.** Add a step between 5 and 6. Re-verify the §B claims that the merged conf and any
watch-touching tip commits feed. Re-stamp `last-audit` by the manifest's stamp rule and stage it into
the landing commit. Give AC15's scratch repository the manifest and the pre-commit hook, so the
refusal can be observed.

**Left-shift.** Class item 4. It extends round 1's join to files a §4 procedure writes, not only
files a Files-touched row names.

### M3 — the landing delta is spelled backwards (29)

**Where.** Unit 34 §4 "The landing reconcile", the verb paragraph. It is read against unit 9 §2 S13
and §6 AC11, and unit 12 §2 S6. G2 round 2 recorded the same defect from unit 12's side as its M2.

**Defect.** Unit 9 S13 returns entries for side `ours` against side `theirs`, and its AC11 passes the
shards-side tip as `ours`. Unit 12 S6 takes "the delta of `<ref>` against HEAD", which is
`ours=<ref>`. Unit 34 writes `delta(ours=HEAD, theirs=<tip>)`. Id 52 makes the same point.

**Impact.** Read as written, the landing plans the builds-mode branch's own side instead of the rows
main gained. There every id the switch-over turned into a view reads REMOVED. G2 round 2's M2 traced
the consequence: every live ask classes NEEDS-HUMAN, and the reconcile parks. A reviewer checking an
engine against this sentence reds a correct one.

**Fix.** Write `delta(ours=<tip>, theirs=HEAD)`, matching unit 12 S6. Fold with G2 round 2's M2 in
the same pass.

**Left-shift.** Class item 1, and G2 round 2's class item 3: a positional interface is cited with
keyword arguments in every consumer, and the join compares the bindings.

### M4 — at the landing the signer reads each row's text from a file step 1 replaced (26, 51)

**Where.** Unit 33 §2 S11, "the rules and every other property are S2 to S9's", and its §4 rules T4
and T5. These are read against unit 34 §4 reconcile steps 1 to 3, and unit 11 §4, the triage
worksheet's columns.

**Defect.** T4 reads a withdrawal in "the row's own text … cited by file and line". T5 reads a hold
target "the row's own text names". Unit 11's triage worksheet carries no row text, only `source` as
`<file>:<line>` in the tip's shards. At the landing, step 2 plans at the tip and removes that
worktree. Step 3 then signs in the run tree, where step 1 took the branch's side of every view and
archive path. So each `source` names a line of a generated view, or of an archive the switch-over
deleted. Nothing routes T4 or T5 to the worksheet's computed-at sha.

**Impact.** At the landing, most tip rows decided by T4 or T5 sign KEEP, so S8's "only rows whose
evidence moved" fails for those rules. Where the view line at that number is another ask's row, a
verdict is signed from that ask's text. The reconcile then confirms it for a tip-added id.

**Why MEDIUM.** Id 51 was rated low and joins id 26.

**Fix.** Have S11 read `source` at the landing worksheet's recorded tree sha, with
`git show <sha>:<file>`. S11's header already records that sha (see L3). The alternatives are to run
step 3 inside the tip worktree before step 2 removes it, or to have the planner's triage worksheet
carry the row text. Make AC13's added row one that T4 decides.

**Left-shift.** Class item 2.

### M5 — AC20's rehearsal writes six records and says it writes nothing (27)

**Where.** Unit 34 §6 AC20, against §4 reconcile steps 2 and 3 and §4 Rollout steps 11 and 12. Also
unit 11 S10, unit 33 S11, unit 35 AC7 and unit 3 S3.

**Defect.** AC20 prints "the size of the landing triage population steps 2 and 3 compute", so the
rehearsal runs both steps. Step 2's `--plan --record <run-tree>/memory/builds/dDerivedDocket/build`
writes a census summary and three worksheets. Step 3 writes two `-landing` records beside them.
AC20's cost line says "it writes nothing", and rollout steps 11 and 12 neither commit nor remove the
six files.

**Impact.** Left untracked, the files dirty the tree. Unit 35 AC7 reads `git status --porcelain`,
and the unattended landing path's `gates-green` refuses a non-empty porcelain with untracked files
included (unit 3 S3). Committed, they are landing records computed at a tip that will move, and they
name every census id on the branch, which feeds H2.

**Fix.** Point the rehearsal's `--record` and the signer's output at a scratch directory, or state
that rollout step 11 deletes the six files before step 12. Have the ledger record AC20's counts
rather than ids. Scope "it writes nothing" to step 4.

**Left-shift.** Class item 2.

### M6 — the confirmation rule's first condition has no command and no arm (9)

**Where.** Unit 34 §4 "Confirmation" and §6 AC15. Also unit 12 §4, which defers to unit 34 the
choice of which ids to confirm.

**Defect.** The rule has two conditions. First, the id's legacy row at the switch-over's first parent
equals its row at the merge-base, meaning the branch made no pre-switch edit. Second, no line added
after the switch-over names the id. §4 names no command that computes either one; the reconciler
"passes `--confirm` for exactly" the qualifying ids. AC15 stages only the second, through a REOPEN
after the switch-over. Unit 12 AC14 stages only an untouched flip.

**Impact.** A reconcile that checks only post-switch lines confirms a tip flip over an id whose
legacy row the branch amended before its switch-over. That writes a disposition over a
receiving-side act, lab case e09b's class, which F7 says the rule keeps out. AC15 stays green.

**Fix.** Name a command for each condition. For the first, a row compare of
`git show <fork>:<shard>` against `git show <switch>^1:<shard>`, with `<fork>` pinned as H2 pins it.
For the second, the structural test H2 defines. Add a fifth tip entry to AC15's park arm: a flip of
an id whose legacy row the branch edited before its switch-over, which must park and be named.

**Left-shift.** Class item 5.

### M7 — AC17 stages four of the writer's eight refusals (8, 30)

**Where.** Unit 34 §2 S1 ("its refusals are §5's, each observed by AC17") and S17; §5 error states;
§6 AC16 and AC17; and §7's new-arm line.

**Defect.** The fold grew §5 to eight refusals:

- a signed record whose header names a stale worksheet blob sha;
- worksheet rows that differ from what `--plan` computes now;
- a missing `Ask`, `Verdict` or `Field` header cell;
- an id with no single chosen copy;
- a row the writer cannot parse;
- `--triage-ask` missing while a hold names no id;
- a `--triage-ask` whose slug is not `--as`'s;
- a `--triage-ask` equal to a spec H1.

AC17 stages four of them: the first, the second, the fourth and the fifth. §7 promises fixtures for
every refusal, and no criterion requires them. S17's zero-holds arm, which files nothing and prints
`triage ask: 0 holds`, has no criterion either. AC16 runs only on gov's corpus, which has holds.
Unit 12's AC12 and AC13 stage none of these.

**Impact.** The three `--triage-ask` refusals are round-1 B1's guards. Consider a writer that, given
no `--triage-ask`, writes an empty `on ` target, or files the triage ask in a foreign folder, or
holds on a spec H1. It passes AC16 and AC17. The first person to meet it is an adopter following
DEPL's step 4, in its own switch-over commit.

**Fix.** List the four missing refusals and the zero-holds arm in AC17 as `--write` fixtures. Each
refusal writes nothing, leaves `git status --porcelain` unchanged, and exits non-zero naming its
cause. The zero-holds arm exits 0, files no ask, and prints `triage ask: 0 holds`.

**Left-shift.** Class item 5.

### M8 — three version moves have no criterion, and AC9 cannot see the cache bump (11)

**Where.** Unit 34 §2 S9; §4 "What the one commit carries", the recall and drift rows; §6 AC9 and
AC23; §7. These are read against `tools/memory-recall/check-recall.py`'s `build_data_dir`, near
`:154`, as the skeptic read it.

**Defect.** S9 says the `CACHE_VERSION` bump is observed by AC9 and AC23. `check-recall.py` extracts
into a throwaway directory and never reads the query cache, and AC23 runs `extract.py`, so neither
sees the bump. AC9's cost line says the bump forces a cache rebuild, which it does not for that
command. The memory-recall and drift-audit kit versions move in §4's table, and §7 omits
`kit version markers`, which units 1, 13 and 32 list for the same class.

**Impact.** A constant moved without its marker, or a version left unmoved while shipped bytes
change, first shows at the landing bar. A missing cache bump shows nowhere before a stale cache
serves anchors from files this commit deletes, which is the reason §4 itself gives for the bump.

**Why MEDIUM.** It was rated low. G1 round 2 (its M11) and G2 round 2 (its M13) adjudicated an
unobserved kit version move at MEDIUM.

**Fix.** Add `kit version markers` to §7. Add an AC that `git diff` against the parent shows
`CACHE_VERSION` and both kit constants moved, and that `bash tools/check-kit-versions.sh` passes.
Correct AC9's cost line.

**Left-shift.** Class item 4.

### M9 — T4 and T5 have no arm (6)

**Where.** Unit 33 §2 S3; §4 rules T4 and T5, and "The script never originates a hold"; §6 AC4 and
AC5.

**Defect.** S3 says CLOSED and WONTDO are signed only on evidence the script re-reads itself, and §4
says the script never originates a hold. AC4 grades CLOSED rows only. No criterion stages a proposed
WONTDO whose cited file and line records no withdrawal (T4). None stages a proposed hold whose
target the row's text does not name, or that is not live, or, for DEFERRED, whose legacy token does
not read DEFERRED (T5). AC5 names no fixture, and a row with no proposal at all satisfies it.
Round-1 M19's fold closed this gap for U3 and U4 with AC14 and left it open for T4 and T5.

**Impact.** A signer that copies the planner's WONTDO or hold through on its word signs a withdrawal
nobody wrote, or a dependency judgment the row's author never made, and every criterion stays green.
The flip then applies those dispositions exactly (unit 34 AC18).

**Fix.** Add an AC in AC14's style over synthetic triage rows. Each is expected to sign KEEP and to
name its rule.

- A proposed WONTDO citing a line that records no withdrawal.
- A proposed BLOCKED whose target the row text does not name.
- A proposed BLOCKED whose target is not live at the signing tree.
- A proposed DEFERRED whose legacy token reads OPEN.

**Left-shift.** Class item 5.

### M10 — the held job's captured output is the sweep's header, because the sweep deletes each suite's output (37)

**Where.** Unit 32 §2 S8 and S9, and §5 observability. These are read against
`tools/run-gates/run-selftests.sh:492-493`, `:571` and `:681`, re-read for this report.

**Defect.** S8 and S9 assume that `tee`ing `run-selftests.sh --sweep` captures the suite's output as
it runs. It does not. The sweep writes each suite's output to `<root>/<k>/out`, under a `mktemp -d`
root that its EXIT trap deletes. It prints only header lines until the pool drains. Then it renders
verdicts, with at most four grepped lines for a FAIL.

**Impact.** If the platform cancels a `platform-bounded` suite, the upload holds the sweep's header,
not the "what ran" S9 promises. Every held red's artifact carries at most four lines. §5's "each
suite's held output" is false, and round-1 M9's and M11's fixes do not hold for the held path.

**Fix.** A local decision between two routes.

- Have the held job run the row's argv directly under `timeout -k 5 <budget × factor>`, piped
  `2>&1 | tee` into a workspace file, keeping the plan job's bound.
- Or add a sweep option that streams or keeps per-suite output in a named directory. That is a
  run-gates surface, and it owes its version move.

Either way, observe the captured output in AC10 or AC11 under a staged cancellation.

**Left-shift.** Class item 6: an observability claim cites the line that prints the output it
claims. Also class item 7.

### M11 — AC10 reads `if: always()` on the uploads only, not on the copy step or the tee (2)

**Where.** Unit 32 §2 S8 and S9; §6 AC10 and AC11.

**Defect.** AC10 counts `if: always()` on the `actions/upload-artifact` steps. The `bar` job's copy
step, which S8 says carries `if: always()`, appears in AC10 only for naming `gate-logs`. The `held`
job's `tee` to a workspace file, which S9 says AC11 observes, is read by neither criterion: AC11
reads the bounds and `timeout-minutes`.

**Impact.** If the copy step runs under the default `success()`, a red bar skips it. The upload then
finds no files and errors under `if-no-files-found: error`, so the red run publishes nothing. That is
AC10's own Red-when, with AC10 green. A held sweep printed only to the log leaves nothing to upload
after a platform cancellation.

**Fix.** Extend AC10 so that every step writing a file an upload names carries `if: always()`,
counted against the uploads. Add a read that each held job pipes its output through `tee` to the
path its upload names, or to whatever path M10's fix chooses. Stage one break for each: the copy
step's `if: always()` deleted, and the `tee` removed.

**Left-shift.** Class item 5.

### M12 — ten held rows start with a literal `python3`, which the sweep runs unresolved (38)

**Where.** Unit 32 §3 Non-goals, the runner-image sentence, and §2 S4. These are read against
`tools/run-gates/run-selftests.sh:571` and `tools/run-gates/run-gates.sh:1369`, re-read for this
report.

**Defect.** The bar runner rewrites a leading `python` or `python3` to the resolved launcher.
`--sweep` passes each argv to `bash -c` unchanged. Re-counted for this report, ten of the 62 rows
`run-selftests.sh --list` prints begin with a literal `python3`: build-index, check-arms,
codebase-map kit, corpus-ids, gotchas, memory-recall kit, recall floor arms, row-grammar,
settings-merge and shell-hygiene. §3 asserts only that "a Python the repo's resolver can run" is on
`windows-latest`, and the resolver accepts `python` when `python3` is absent or is the Store stub.

**Impact.** The held path depends on a working literal `python3` on the runner, which the spec
never states or checks. If it fails, ten held jobs red every day for a host reason and read as tree
failures. AC5 and AC11 run `--list` only, so nothing before landing observes it.

**Fix.** State the dependency, and assert it in the held job with a `python3 -c 'import sys'` step
before the sweep. Or resolve the launcher in the held job and rewrite argv[0] as `run-gates.sh`
does. Name the dependency in §5 risks.

**Left-shift.** Class item 7.

### M13 — five contract properties are read and never staged, and the symref assertion step is read by nothing (3)

**Where.** Unit 32 §2 S1 and S5; §6 AC1, AC2 and AC4.

**Defect.** S5 promises that each contract property is observed by a staged break confirmed to fail.
AC1, AC2 and AC4 stage breaks for seven properties: `fetch-depth`, `persist-credentials`, the
autocrlf order, `runs-on`, a `set-head` step, a tag pin, and `GATE_WALL` on both sides. They stage
none for these five.

- A second `permissions` grant. AC4 reads "no other grant" with no break and no Red-when.
- `timeout-minutes` above 360.
- A job with no `shell: bash`.
- A `secrets.` reference in the bar clone URL.
- A `uses:` of a non-`actions/` action. AC2 stages only a tag pin.

S1's step asserting `git symbolic-ref refs/remotes/origin/HEAD` in every job is half of round-1 H3's
fold, and no criterion reads it.

**Impact.** The permissions grant is the unit's security bound. A "no other grant" read never seen to
fail passes a job-level `permissions: contents: write`, which overrides the workflow level, and §8 F2
leaves no gate over the file. Without the assertion step, a job that lost its `set-head` fails later,
inside a bar leg, for a host reason.

**Fix.** Stage breaks as follows. In AC4, a job-level `permissions: contents: write` and
`timeout-minutes: 361`, each with a Red-when. In AC1, a job with no `shell: bash`, a
`${{ secrets.X }}` in the clone URL, and one job's `symbolic-ref` assertion step deleted. In AC2, a
third-party action pinned by sha.

**Left-shift.** Class item 5.

### M14 — no criterion reads the workflow's `on:` block (4)

**Where.** Unit 32 §2 S2, S3 and S4; §2 S5; §3 Non-goals; §4 Security.

**Defect.** No criterion reads the triggers: `history-audit` and `bar` on a push to the default
branch, and the held jobs on `schedule` and `workflow_dispatch`. §4's claim that no job runs on an
event a fork can trigger is unchecked, and so is §3's ban on pull-request and feature-branch
triggers. S5's hand-observed contract lists none of them. §3's non-goal withholds only criteria that
depend on the live run, not a static read. This is the one entry in rev-1 text that no round-1
finding named.

**Impact.** A `branches: [master]` typo, or an event filter that never matches, passes AC1 to AC12.
D11-b's per-push audit then never runs, and the first sign is the wrap-up's missing live run, after
the landing. An added `pull_request_target` is invisible to every criterion.

**Fix.** Add the triggers to S5 with an AC. The `on:` block names `push` restricted to `main`, plus
`schedule` and `workflow_dispatch`, and no `pull_request*` event, and each job's `if:` routes it to
its own triggers. Stage breaks for `branches: [master]` and for an added `pull_request_target`.

**Left-shift.** Class item 5. A security claim in §4 names the criterion that reads it.

### M15 — two authored `AGENTS.md` lines keep the unqualified authorization claim (17, 33)

**Where.** PLAY §2 S8 and S4; §6 AC11; §3 and §10, where no omission is recorded. These are read
against `AGENTS.md:38`, `:559` and `:582` at BASE, re-read for this report. The first two sit outside
the `gov:playbook` region. Also `memory/guides/UNATTENDED-PROTOCOL.md:32`.

**Defect.** S8 qualifies the template's substitute bullet to the default-branch anchor. It repoints
the Conventions bullet at `AGENTS.md:582`, and calls the unqualified property "false for every run
the second anchor authorizes". Two more authored lines state that property: `:38`, under "What ships
here", and `:559`, under "Two protocols are BINDING". Each says the run replaces the checkpoint "with
a committed standing mandate it ASSERTS and cannot have written". AC11 greps "folder the run did not
create", which matches neither line. No spec in the build touches them.

**Impact.** After PLAY, gov's charter gives both answers. The rendered region qualifies the
property, and two authored lines say no run can have written its mandate. That is the contradiction
round-1 M13 was folded to remove, and AC11 cannot see it. M13's fix offered a rewording or a
recorded omission, and the fold made neither for these two lines.

**Why MEDIUM.** Id 33 was rated low and joins id 17.

**Fix.** A local decision. Extend S8 to `:38` and `:559`, pointing each at §1 Landing's substitute
as `:582` now is, and widen AC11's grep to "cannot have written" outside the region. The run's veto
2 kept `AGENTS.md`'s hooks-path sentence out of scope in the decision `RUN.md` parked. If it keeps
these two lines out as well, record the omission in PLAY §10 and park it in `RUN.md` instead.

**Left-shift.** Class item 4: a sentence a fold calls false is grepped by its BASE text across every
tracked carrier, not only the one the finding quoted.

### M16 — the runbook's step 4 never removes the family archives builds mode refuses (19, 42)

**Where.** DEPL §2 S2; §4 "Proposed text for §3a-asks" step 4; §6 AC3. These are read against unit 7
S10 and AC7, unit 34 §2 S1 and S6, unit 11 S2, and `tools/memory-tree/.memory-tree.conf.example`'s
`ROTATION_MODE`.

**Defect.** Step 4 removes the shards through `--write`, sets the mode, renders, and ends "Commit
when `--check` exits 0". `--write` migrates the family backlog archives' rows too (unit 34 S1), but
it removes only the shard files. Gov deletes its three archives in a separate step (unit 34 S6,
owner ruling D8). Under builds mode, unit 7 S10 makes `gen_build_index.py --check` exit 1 on any
tracked rotated archive whose stem is a declared family. The runbook never says to delete them. AC3
runs only step 1, over a scaffold fixture holding no archive, so no criterion runs step 4.

**Impact.** An adopter whose tree ever rotated a backlog shard is stranded at step 4. `--check` never
exits 0, and the runbook's only guidance is the verdict line. Adopters do rotate: the shipped conf
example declares `ROTATION_MODE="snapshot"`, and inCMS practises it.

**Fix.** Add to step 4, after `--write`'s conservation proof, the deletion of every tracked
family-stem backlog archive, and the rewording of any carrier outside the memory root that names
one, citing ruling D8. Extend AC3 with a fixture holding one rotated family archive, taken through
steps 1 to 4 as the section spells them, and expect `--check` to exit 0.

**Left-shift.** Class item 1, since a runbook procedure replays the reference repo's rollout step
for step, and its fixture runs every step, not the first. Also class item 4.

### M17 — the runbook stops at the switch-over commit and names no landing path (58)

**Where.** DEPL §4 "Proposed text for §3a-asks", steps 4 and 5; §3 Edges; §6 AC3. These are read
against unit 10 S1, unit 12 S6, S10 and AC9, and unit 34 §4 "The landing reconcile".

**Defect.** The five steps end at the switch commit. Unit 34 §4 exists for the case they skip: a
switch branch whose default branch gained shard rows meanwhile. The only recipe the row driver prints
is `--relocate` (unit 10 S1, unit 12 S10). `--relocate` exits 2 when the other side's conf is in
shards mode (unit 12 AC9), and it is, whenever an adopter merges its default branch into its switch
branch. The verb for that landing, unit 12 S6's landing form of `--ingest`, appears nowhere in the
runbook. Unit 34's hands-off to DEPL covers only `--write`'s argument shape.

**Impact.** An adopter whose default branch moves during its switch build is stranded at the
driver's refusal, holding a recipe that exits 2. That is the stranded-at-a-command class AC3 was
written to guard.

**Fix.** Add a landing step. When the default branch moved since the fork, merge it into the switch
branch and take the branch's side of the views. Run
`migrate_backlog.py --ingest <default tip> --as <your-slug> --signed <records> --triage-ask <id> --dry-run`,
confirm per id, write the `ASK_CUTOFF` it prints, and re-render. Add unit 12 S6 and unit 34's
reconcile to the Edges and to AC3's resolved commands. Fold this after unit 34's H1, H2 and M3
folds, which change the procedure the step copies.

**Left-shift.** Class item 1.

### M18 — step 4's new `merge-rows.py --check` cannot be resolved against the usage AC3 reads (18)

**Where.** DEPL §4 step 4, the orchestrator's post-fold edit, and §6 AC3. These are read against
`tools/memory-tree/merge-rows.py:1098-1104`, re-read for this report, and unit 10 S5 and S9.

**Defect.** AC3 checks each command's flags against "its tool's `--help` usage". `merge-rows.py
--help` takes the fewer-than-four-arguments branch. It prints the docstring's first two paragraphs:
the summary, and the `git config merge.rows.driver '… merge-rows.py %O %A %B %P'` line. That names
no `--check`, and it marks three paths required. Unit 10 S5 adds the mode, and S9 edits the
docstring, but neither pins a usage line naming it. DEPL cannot fix the usage itself: its F6 rules
out a kit bump, and it runs after unit 36's.

**Impact.** AC3 reds on a correct unit 10 in two ways. `--check` is not listed. And "every argument
the usage marks required for that verb appears in the step" demands three paths the step correctly
omits. The only way through is to waive AC3 for this command, which is round-1 M26's "reds or is
waved through".

**Why MEDIUM.** The property AC3 guards, that the command exists and runs, is observable by running
it.

**Fix.** Resolve step 4's command by running it: `merge-rows.py --check` on the switched tree exits 0
and prints its `merge-rows: check ·` liveness line. Alternatively, add an AC to unit 10 that the
driver's usage paragraphs name `--check`, and cite it here.

**Left-shift.** Class item 6.

### M19 — the runbook's new commands raise a pinned install-prefix count (41)

**Where.** DEPL §4 "Proposed text for §3a-asks"; §4 Files touched; §7, which lists
`install-prefix (shipped surface)`; §6. These are read against `tools/install-prefix-carried.txt:11`,
re-read for this report.

**Defect.** `WIRE-INTO-PROJECT.md` is pinned at 53 carried literals, which is its current count. The
list's header says only a person raises a row, with a reason, in the pass that needs it. The
47-to-53 raise on 2026-09-08 is the precedent. The proposed section adds eight
`tools/memory-tree/<file>` occurrences: `README.md` once, `migrate_backlog.py` five times, and
`gen_build_index.py` and `merge-rows.py` once each. Files touched lists only the runbook and the
adopter script, and no spec in the build names the list.

**Impact.** The `install-prefix (shipped surface)` leg, which DEPL's own §7 lists, reds with ROSE at
the post-build bar. No criterion runs it in the pass.

**Fix.** Add `tools/install-prefix-carried.txt` to Files touched, with the runbook's row raised by
hand and a reason: these are commands an operator types. Add a criterion that runs
`bash tools/check-install-prefix.sh`.

**Left-shift.** Class item 4: a new `tools/<kit>/` literal in a file the carried-prefix list pins
puts that list in Files touched.

## Low

### L1 — AC8 checks S7's header edits only for absence (5)

**Where.** Unit 32 §2 S7 and §6 AC8, the L1 fold.

**Defect.** AC8 checks that the old "nothing runs … automatically" phrases are gone from both runner
headers, and that `AGENTS.md` no longer calls remote CI a follow-up. S7's positive content has no
criterion. Each header should name the daily CI schedule beside unit 1 S8's compensating-check
wording. The merge-bar sentence should name the workflow, its jobs, detection after landing, and no
required check.

**Impact.** Deleting either header's whole "WHAT IS THEREFORE NOT COVERED" paragraph passes AC8. It
also removes the compensating-check sentence unit 1 S8 rewrote, which unit 1 AC7 observed only at
unit 1's commit. Deleting the `AGENTS.md` sentence passes too.

**Fix.** Add positive greps to AC8. Each header names the schedule and still carries unit 1 S8's "no
NEW FAIL" wording, and the `AGENTS.md` merge-bar section names `remote-ci.yml`.

**Left-shift.** Class item 5.

### L2 — the unattended runner's line 2 still says "nowhere else" (32)

**Where.** Unit 32 §2 S7 and §6 AC8, read against `tools/unattended/run-unattended-gates.sh:2`.

**Defect.** Line 2 says the self-tests are "run on demand and nowhere else", which round-1 L1 quoted
beside `:24-26`. AC8's grep matches only "nothing runs the self-tests automatically" and "nothing
runs these automatically".

**Impact.** L1's fix holds for line 25 and not for line 2. That header stays false from the
schedule's first run, with every criterion green.

**Fix.** Name line 2's clause in S7, and add "nowhere else" to AC8's grep.

**Left-shift.** Class item 4.

### L3 — AC13 reads no landing header, and leaves its records in the tracked folder (7)

**Where.** Unit 33 §2 S11; §6 AC13; §4 Inventory, which puts the landing records in the same folder.

**Defect.** S11 has each landing record's header name its worksheets' paths, their blob shas, and the
tree sha they were computed at. AC13 compares rows only, so the header, and the tree sha nothing else
pins, go unread. AC13 also writes two real-named `-landing` records carrying a synthetic ask row into
the tracked build folder, and nothing says they are removed.

**Impact.** At the landing, a record whose header omits or misstates the tip it was planned at cannot
be tied to that tip, and M4's fix relies on that sha. If committed with the pass, AC13's records name
a scratch worksheet path and an id nothing defines, which check 14 reds at the bar.

**Fix.** Add to AC13 a read that each landing header names the worksheet paths, the blob shas, and a
tree sha equal to the one on the worksheet's own `#` line. Run AC13 in a scratch copy of the build
folder, or have it remove its two records and show `git status --porcelain` clean.

**Left-shift.** Class item 5.

### L4 — no criterion checks the `filed` value on roughly 600 migrated asks (10)

**Where.** Unit 34 §2 S1, where `filed` is taken by unit 12's rule, and §6 AC2, AC3 and AC4.

**Defect.** AC2's normalization 2 admits the inserted field without checking its value. AC3 compares
status and hold target only. AC4 derives the cutoff from the same written `filed` values it should
be grading, which is circular. Unit 12 AC1 grades `filed` only for the relocate form, on a fixture,
and the walk over shard and archive history is unit 34's own wiring.

**Impact.** A writer that stamps every row with the flip date, or stamps archived rows with a
rotation commit's date, passes AC2 to AC4, because the cutoff follows the wrong dates. Each ask's
permanent filing date is lost at the one commit that writes it.

**Fix.** Add, to AC3 or a new AC, a per-id compare of `filed` against the oldest lineage commit
holding the id. Cover a sample that includes an archived id and a wrapped row.

**Left-shift.** Class item 5, and round 1's M21: a derived value is compared with an independent
derivation.

### L5 — AC10's tuple clause cannot be shown, and S10's no-`BACKLOG.md` arm has no fixture (12)

**Where.** Unit 34 §2 S10, and §6 AC10 and AC21, the M23 and M4 folds.

**Defect.** AC10 says its count also shows the terminal-status tuple reading the derived output. The
re-pointed signal counts the entries of `--asks --json`, which lists live asks only. The tuple's
other caller, `drift_report.py:1618`, retires. So the equality holds whatever the tuple reads. S10's
"not-asked while no `BACKLOG.md` is tracked" has no fixture, because every builds-mode fixture in
AC21 carries asks.

**Impact.** Two S10 claims the fold says are observed are not. A builds-mode tree with no
`BACKLOG.md` yet would print three DEAD PROBE lines unseen.

**Fix.** Drop the tuple clause from S10 and AC10. Or have the signal read `--asks --all --json`,
filter it with the tuple, and stage a CLOSED ask being counted live. Add to AC21 a builds-mode
fixture with no tracked `BACKLOG.md` that prints the three signals as not-asked.

**Left-shift.** Class item 5.

### L6 — the runbook is not told that deselecting `kickoff-manifest` now drops the merge exception (34)

**Where.** PLAY §2 S2, the new `kit:kickoff-manifest` fence, and §3 Edges, the hands-off to DEPL.
Read against DEPL §2 S4.

**Defect.** The fold makes the kickoff-manifest merge exception kit-conditional, and
`playbook.kit.toml` does not require that kit, so an adopter can deselect it. PLAY's hands-off to
DEPL covers only the unattended blocks, and DEPL S4 edits only that bullet. The runbook's §2 lists
the kits whose blocks the charter carries. At BASE those are codebase-map, lexicon and unattended,
and the list has no kickoff-manifest entry.

**Impact.** An adopter who deselects `kickoff-manifest` loses the merge exception from its charter
and is not told. That is the operator-not-told class DEPL AC5 grades for unattended.

**Fix.** Name the kickoff-manifest fence in PLAY's hands-off to DEPL. Give DEPL a §2 line, or extend
S4, saying that keeping the kit keeps the merge exception.

**Left-shift.** Class item 4: a new fence is a new kit-selection consequence, and the runbook's kit
list is one of its carriers.

## Left-shift, by class

1. **A procedure step runs a sibling's verb for a state that verb never leaves** (H1, H6, M3, M16,
   M17). Unit 34 step 1 and unit 2's `--prepare`. Unit 35's bare `check-wiring.sh`. Unit 34's delta
   and unit 9 S13. The runbook's step 4 against gov's rollout, and its missing landing against unit
   12's `--relocate` refusal. This is G2 round 2's class item 3, restated rather than cited, in its
   procedural form.
   - The documented check, for the spec author: a step that runs a sibling's verb cites the
     producer's §4 step for the state it leaves, meaning the exit code, the HEAD, the mode and the
     parents of any merge. The next step reads that state. A runbook's fixture runs every step, not
     only the first.
   - The mechanical half extends the hands-off payload join that unit 37, adopted in the fold, adds
     to the spec-tokens leg. A backticked verb whose tool a sibling spec defines requires a
     consumes-from edge to that sibling, and its flag set is compared with the producer's S-item.
     Run it by hand over the rev-3 fold first, printing hits and near-misses. H1 is a hit on both
     counts.
2. **A rule read in a tree that this build's own writes have already changed** (H2, M4, M5, L3).
   The confirmation rule's "a line names it" is supplied partly by this build's ledger, its
   rehearsal and a re-run's worksheets. The signer's `source` line points into a shard that step 1
   replaced with a view. The record is `memory/gotchas/inputs-inside-the-subjects-reach.md`.
   - The documented check: for each landing input, name the sha it is read at, and list which of
     this build's own writes land in that tree before the read.
   - The fixture half is AC15's scratch repository. Its branch carries this build's ledger with one
     verbatim RED naming the untouched flip's id, a committed rehearsal record, and the kickoff
     manifest with its pre-commit hook. It stages `--prepare`'s refusal before the manual merge, and
     one tip row that T4 decides. As written, AC15 can see H1 only. Extended, it sees H1, H2, M2 and
     M4 in unit 34's pass instead of at the landing.
3. **A write the build makes into the population its own plan or proof grades** (H3, H4, M1). S11
   and S17 write outside the predicted set. The fold commit filed two asks no spec disposes. Passes
   between orders 11 and 34 move the planner's input.
   - The documented checks: a proof against a prediction lists every write outside the predicted
     set as a named exception. A fold that files a shard row under this build's slug names the
     disposing unit in the same commit. The flip re-plans at the switch-over's parent and diffs
     against the signed census before `--write`.
4. **What an edit owes and does not carry** (M2, M8, M15, M16, M19, L2, L6). This is round 1's class
   item 7 again: a re-stamp, a version marker, two more carriers of a falsified sentence, an archive
   deletion, a carried-prefix row, a second line in a header, and a kit-list line. Round 1 proposed
   the joins for `tools/check-spec-tokens.py`, and none is built. This round extends them.
   - A watched file that a §4 procedure writes, not only a Files-touched row, needs the manifest
     re-stamp named in that procedure.
   - A version constant moved in §4 needs `kit version markers` in §7.
   - A new `tools/<kit>/` literal in a file that `tools/install-prefix-carried.txt` pins needs that
     list in Files touched.
   - A sentence a fold calls false is grepped by its BASE text across tracked files. Round-1 L1's fix
     missed line 2, and M13's missed `:38` and `:559`.
5. **An S-item listing N members, staged for fewer** (M6, M7, M9, M11, M13, M14, L1, L3, L4, L5).
   This is round 1's class item 6, the sixth group in a row where it leads. The fold's form is new:
   it wrote the list and then staged a prefix of it. Unit 32's S5 lists twelve properties and stages
   seven. Unit 34's §5 lists eight refusals and AC17 stages four. U3 and U4 are staged without T4 and
   T5, and one of the confirmation rule's two conditions is staged.
   - The documented check is round 1's: beside each "Observed by", write the mutation that deletes
     the member and the AC that reds on it.
   - The mechanical proposal: a join that counts the enumerated members of a §5 refusal list or an
     S-item's property list against the fixtures named in the criterion the S-item cites, and prints
     a shortfall as a near-miss.
6. **A criterion or claim quotes an output its own command cannot print** (H5, H6, M10, M18). A
   DRIFT line naming a key, from `--check`. A session note, from `git commit`. A `--check` flag, in
   `--help` usage. "Each suite's held output", from a sweep that deletes it. The record is
   `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`.
   - The documented check: every quoted output in an AC, or in §5 observability, cites the BASE
     `file:line` that prints it, in the mode the AC runs.
7. **The CI runner is not a node, again** (M12, and M10's cancellation half). Round 1's class item 2
   covered the clone path, `origin/HEAD` and the job limit. This round adds the Python launcher and
   the sweep's scratch output.
   - The pre-landing, runner-shaped run gains two readings. One held row per distinct argv[0] runs
     under `bash -c` exactly as the sweep does, with `python3` absent or shadowed by the Store stub.
     The sweep runs under a staged cancellation, and the captured file is read.

## Outside the confirmed set

One observation came out of re-checking H1. It was not put to a skeptic, so it is not counted above.

**After H1's fold, `--prepare` still merges with the tip's driver.** `--prepare` checks R out
detached and merges B onto it, so R's pre-switch `.gitattributes` and R's `merge-rows.py` run that
merge. R's driver has no view refusal. When R is the tip the reconcile merged, B contains R and the
merge is trivially clean. R can move between the reconcile and `--prepare`, though, and `--land`'s
race path re-prepares onto a newly advertised tip (unit 2 S6). Then a merge that R's driver resolves
without conflict could row-merge R's new shard rows into B's generated view. The unattended path's
`gates-green` bar and the pre-push hook would red such a view through check 9's byte-compare, so the
harm looks bounded. The fold should still say that `--prepare` runs against the tip the reconcile
merged, and that a moved tip returns to step 1 rather than being re-prepared over.

## What this round did not cover

- **Units outside G5**, read only where an edge or an interface named them. H1's fold lands in unit
  34, with a reciprocal hands-off in unit 2, which group G1 audits. M3 is G2 round 2's M2, so fold
  it once. G2 round 2's M1 (its landing half), M3, M4 and L1 also sit in unit 34's reconcile, and
  they should fold in the same pass as H1, H2 and M6 here. H4's fix lands in unit 34 or unit 35, and
  M1's needs a tail name from unit 33.
- **Unit 36**, where no finding was confirmed this round. That means four lenses and a skeptic stage
  found nothing, not that the spec is certified.
- **Re-measured for this report**, at `abac6d59` or at the fold commit where stated:
  - unit 2's `--prepare` steps and data model (H1);
  - `render_playbook.py:594` and `:612-613`, and `adopt-playbook.sh:59` (H5);
  - `check-wiring.sh:110-116` and `:258-262` (H6);
  - `run-selftests.sh:492-493`, `:571` and `:681` (M10);
  - `run-gates.sh:1369`, and the ten literal-`python3` rows among the 62 that `--list` prints (M12);
  - `merge-rows.py:1098-1104` (M18), and `install-prefix-carried.txt:11` (M19);
  - `SESSION-KICKOFF.md:6`, `manifest-check.sh:408-421` and `.githooks/pre-commit:54` (M2);
  - `AGENTS.md:38`, `:559` and `:582` (M15);
  - the two OPEN rows at `memory/backlog/TOOL.md:468-469` from `18cf0c1b`, and that no other shard
    row carries this build's slug (H4);
  - the triggers' rev-1 text in unit 32's rev-1 blob (M14).
- **Not re-derived.** The GitHub platform facts that M11, M12 and M13 rest on are the finders' and
  skeptics' statements: the job limit, the runner image's Python, and `upload-artifact`'s behaviour.
  So is M8's reading of `check-recall.py`'s cache handling. The first live run after landing is the
  first observation of the platform facts, and class item 7's pre-landing run is the substitute.
- **The 25 refuted findings**, which are not reproduced here. They were refuted, not lost, as the
  run-integrity counters show.
- **The rev-3 fold this report prescribes.** It will be unreviewed surface, and its review is the
  closing diff review's, indexed on the §9 rev-3 lines.
