**Serves:** spec-audit TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13

# dDerivedDocket — spec audit of topic group G2, the derived backlog core, round 2

*Node `d`, 2026-09-14. The second Tier-2 adversarial pass over the eight live G2 specs: the ask parser
and status fold (unit 6), the generated family view (7), the hygiene engine in builds mode (8), the
transition-merge audit (9), the row driver's shard-into-view refusal (10), the migration planner
(11), the relocation tools (12), and the straggler hooks and inventory (13). Unit 14, retired at
WONTDO, was not a subject this round. The pass was aimed at the text the round-1 fold introduced,
using each spec's §9 rev-2 line as the index, and at whether each round-1 fix actually holds. Four
primed finder lenses ran, then a skeptic stage prompted to REFUTE each finding in five batches, then
this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief's roster and edge tables, and the round-1 record
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md`.
Sibling specs outside G2 were read wherever an edge or an interface named them, units 34 and 35 most
of all. No finding was adjudicated BLOCKER or HIGH. The MEDIUM findings that rest on the behaviour
of a tool were re-checked against source at `abac6d59`, and the sites read are named in each entry.
The eight blobs below are the ones the spec set holds at `18cf0c1b`, the fold commit, and were
confirmed equal before this report was written.*

**Round: 2.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-6.md@d4459559a70ddc937f10645d41092d35b8d7cd19`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-7.md@076b3b3e3673ec0d5572186a95159baa8c1f7a7d`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-8.md@d4584f92bba0232600bb17bc30bc18cb49db2c4b`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-9.md@57d90ce67c547da6fa6f723a8a50876cbb0366bf`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-10.md@f1a4e9de2ca417fe4b2aa58bad9381323fc5b759`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-11.md@274830780cf751a752201cc812abf98a7d3dc87a`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-12.md@cb4aa20f17ac3e1cb2825f0b946cedabaae047d9`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-13.md@310819fc91f7a6253f272e333290b84fad206b5d`

## Verdict: CLEAN WITH FIXES

No blocker and no high stands. Round 1's three blockers were folded, and as adjudicated here none of
the 37 confirmed findings stops the switch-over or its landing as units 11, 12 and 34 now specify
them. Every defect below that touches that path surfaces as a named refusal or a park, with one
narrow exception stated in M1. There, a hold on an ask that main files during the build window is
re-targeted at the landing without a refusal; the ask keeps its derived token until one of the two
asks closes. What stands is 26 MEDIUM findings, which are 13 distinct defects, and 11 LOW findings,
which are 9. The MEDIUM set is not cosmetic, and three groups in it matter most.

- **The landing reconcile's engine form holds as a verb, and four seams around it do not.** This was
  round-1 B3's fix. Unit 34 spells its delta with the arguments reversed (M2). Its shards-mode
  refusal is scoped to no verb (M3). Its collision rule and its CLOSED row still read the `--as`
  file after P1 moved transferred tokens to the owner's folder (M4). Its hold test counts an ask the
  same delta files as naming nothing (M1).
- **Round-1 M8's fix does not hold (M5).** The `requires_if` edge unit 9 relies on to install the
  recall kit installs nothing, because govkit reads `requires_if` only in selfcheck.
- **Round 1 named two undeclared legs outside its confirmed set, and the fold acted on neither (M7,
  M8).** That accounts for 8 of the 37 ids. Unit 9's rev-2 line answers neither question round 1
  asked of it, and unit 11's added only the budget row.

Convergence under `memory/guides/BUILD-METHOD.md` M4: the blocker count fell from 3 to 0. M4's
BLOCKED disposition does not apply, so the prescribed act is to fold these fixes and stop
spec-auditing these eight specs. Four folds need a local decision first, and each entry states it:
M4 (what a collision at the owner's folder means), M5 (restate the edge or change govkit), M6 (where
the real-tree hook-list arm lives), and M7 (whether adopters receive the transition-audit suite).
The fold's own text is unreviewed surface (`memory/gotchas/fold-text-is-unreviewed-surface.md`):
35 of this round's 37 ids sit in round-1 fold text or in the half of a fix it left standing. The
rev-3 fold meets the closing diff review, which should take the §9 rev-3 lines as its index.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

Every counter that could make this run incomplete is zero, so this run is complete. The finding set
is complete for what the four lenses were primed to hunt. That is not a claim that G2 holds no other
defect. It is a claim that nothing was lost between the lenses and this page, so a "no confirmed
finding" below means four lenses and a skeptic stage found nothing, which is evidence but not proof.

The pipeline's duplicate count of 0 comes from its own exact-match dedupe. On reading, nine groups
each describe one defect reported by two to four lenses: 2 with 28 and 44; 20 and 13; 31 with 48
and 16; 34 and 49; 5 with 23, 33 and 50; 6 with 22, 36 and 51; 8 and 27; 15 and 45; and 11 and 30.
Each group is folded into one entry below, and every count on this page stays per finding id.

## Review shape

Raw 56, confirmed 37, refuted 19, unverified 0, precision 0.66. The 37 confirmed ids collapse to 22
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 0 | 0 |
| MEDIUM | 26 | 13 |
| LOW | 11 | 9 |

**Severity is adjudicated here, not copied from the finders**, on round 1's scale.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written for a reason its fold cannot settle
  locally, or it ships a layer that stays inert while its suite reads green.
- MEDIUM covers three kinds of defect. The first is a contradiction between specs with a bounded or
  visible consequence. The second is a declaration whose absence reds a leg at the post-build bar.
  The third is a claimed mechanism that does not exist.
- LOW is a rule whose break no criterion can see, where the reachable harm is small.

Six findings move up and none moves down. Ids 13, 16, 27, 28 and 44 move from low to MEDIUM, each
because it is one defect with a medium finding: 13 with 20, 16 with 31 and 48, 27 with 8, and 28 and
44 with 2. Id 56 moves from low to MEDIUM on its own. G1 round 2 adjudicated the same class, an
unobserved kit version move, at MEDIUM as its M11. The precedent both cite, TOOL-dMuffledSentinel-3,
recorded an adopter's pull refused.

Precision rose from round 1's 0.57 to 0.66 with the same four lenses. Three observations about the
confirmed set follow.

- **Fold text dominates.** 35 of the 37 ids, and 20 of the 22 defects, sit in text a §9 rev-2 line
  names, or in the half of a round-1 fix that line left standing. The exceptions are L2 (43) and
  M13 (56). Both are rev-1 text, in units 12 and 13, that no round-1 finding named.
- **The declarations cluster more than doubled.** Round 1 found six ids in which a new moving part
  owes a declaration its spec never names. This round finds 13 ids and six defects of that kind: M7,
  M8, M9, M13, L4 and L5. Eight of the 13 are the two gaps round 1 recorded outside its confirmed
  set.
- **The criterion-gap class is smaller but present.** Round 1's dominant class,
  `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`, returns in the fold's new
  criteria as M11, L1, L3, L6, L7 and L8, and as one half of each of M1, M2, M5 and M10. Most of
  those are a fixture in which the right input and the wrong one coincide (class item 6).

## Round-1 fixes: what this round found against them

"No confirmed finding" means four lenses and a skeptic stage confirmed nothing against the fix. It
does not certify the fix.

| Round 1 | Spec | Round-2 reading | Round-2 entries |
|---|---|---|---|
| B1 | 12, 11 | partial: the third policy holds, and its names-an-id test is not unit 11's | M1 |
| B2 | 11, 34 | no confirmed finding in G2; unit 34's half is G5's | none |
| B3 | 12, 34 | the verb holds; four seams around it do not | M2, M3, M4, L1, and M1's landing half |
| H1 | 9 | both entry points hold; the tree half of each is unobserved | M11 |
| H2 | 13 | holds in substance; the carrier correction is unobserved and misstates scope | M10, L3, L4 |
| H3 | 7 | no confirmed finding | none |
| M1 | 6, 7, 8 | holds for V16; unit 8 never stages V15 | L7 |
| M2 | 6 | no confirmed finding | none |
| M3 | 7, 10 | the behaviour holds; unit 10's mutation sweep does not reach its arm | L6 |
| M4, M6, M7 | 7, 9, 12 | no confirmed finding | none |
| M5 | 11, 33 | no confirmed finding in G2 | none |
| M8 | 9 | does not hold: the edge installs nothing | M5 |
| M9 | 6, 34 | moved to unit 34, which G5 audits; not graded here | none |
| M10 | 11 | the budget row holds; the govkit declaration round 1 flagged is still missing | M8 |
| M11 | 8 | no confirmed finding; the same class recurs in unit 13 | M9 |
| M12 | 10 | no confirmed finding | none |
| M13 | 13 | the declarations hold; the leg's guard and ceiling do not | L4, L5 |
| M14 | 6 | holds for R5 only | L8 |
| M15 to M18 | 7, 9 | no confirmed finding | none |
| M19, M20 | 10 | the arms hold; unit 10's mutation sweep does not reach them | L6 |
| M21, M23, M24 | 11 | no confirmed finding | none |
| M22 | 11 | the `design-named` case has no input | M12 |
| M25 to M28 | 12, 13 | no confirmed finding | none |
| L1, L3, L5, L6 | 9, 11, 13 | no confirmed finding | none |
| L2, L7 | 9, 13 | the both-ways arm now exists, and it ships to adopters | M6 |
| L4 | 11, 12 | the shared fixture holds, and it lacks the same-delta shape | M1 |
| unit 11's undeclared leg, outside the set | 11 | not acted on | M8 |
| unit 9's undeclared leg, outside the set | 9 | not acted on | M7 |

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 2 | MEDIUM | M1 | 12 | §4 The engine, P3; §4 Classification, the two hold rows; §6 AC12 |
| 28 | MEDIUM | M1 | 12 | §4 P3 and the Classification hold row, against unit 11 §2 S7 |
| 44 | MEDIUM | M1 | 12 | §4 The engine, P3; §6 AC14 |
| 20 | MEDIUM | M2 | 12 | §2 S6, against unit 34 §4 The landing reconcile and unit 9 §2 S13 |
| 13 | MEDIUM | M2 | 12 | §2 S6; §8 F7; against unit 34 §4 The landing reconcile |
| 18 | MEDIUM | M3 | 12 | §5 error states and migration, against §2 S6, S13 and unit 34 §4 Rollout |
| 19 | MEDIUM | M4 | 12 | §4 Classification, the CLOSED row and the collision paragraph, against §4 P1 |
| 31 | MEDIUM | M5 | 9 | §4 Data model, Delta entry; §2 S12 |
| 48 | MEDIUM | M5 | 9 | §4 Data model; §2 S12, the `requires_if` clause and its `why` |
| 16 | MEDIUM | M5 | 9 | §2 S12; §6 AC10 |
| 34 | MEDIUM | M6 | 9 | §2 S12, the both-ways hook-list arm |
| 49 | MEDIUM | M6 | 9 | §2 S12; §3 Edges, hands-off to 13; §6 AC10 |
| 5 | MEDIUM | M7 | 9 | §2 S11, S12; §6 AC10 |
| 23 | MEDIUM | M7 | 9 | §2 S11, S12, against §6 AC10 |
| 33 | MEDIUM | M7 | 9 | §2 S11, S12; §4 Files touched; §6 AC10 |
| 50 | MEDIUM | M7 | 9 | §2 S11, S12; §4 Files touched; §6 AC10 |
| 6 | MEDIUM | M8 | 11 | §2 S11; §4 Files touched; §7 |
| 22 | MEDIUM | M8 | 11 | §2 S11; §4 Files touched; §7 |
| 36 | MEDIUM | M8 | 11 | §2 S11; §4 Files touched; §7 |
| 51 | MEDIUM | M8 | 11 | §2 S11; §4 Files touched; §7; §6 AC10 |
| 24 | MEDIUM | M9 | 13 | §4 The session step; §2 S2, against §7 and §6 AC9 |
| 8 | MEDIUM | M10 | 13 | §4 Why a library beside the hooks, the four-carriers paragraph |
| 27 | MEDIUM | M10 | 13 | §4 Why a library beside the hooks, the corrected carrier sentence |
| 3 | MEDIUM | M11 | 9 | §2 S13, S14; §6 AC11, AC12 |
| 7 | MEDIUM | M12 | 11 | §2 S6; §8 F5; §6 AC4 |
| 56 | MEDIUM | M13 | 13 | §4 Files touched, the version-constant clause; against unit 9 §4 and §7 |
| 12 | LOW | L1 | 12 | §4 The landing form's cutoff; §2 S9; §6 AC14 |
| 43 | LOW | L2 | 12 | §4 Straggler inventory; §2 S8 |
| 14 | LOW | L3 | 13 | §3 Edges, hands-off to 35; §2 S8; §6 AC12 |
| 15 | LOW | L4 | 13 | §2 S8; §6 AC12 |
| 45 | LOW | L4 | 13 | §2 S8 |
| 53 | LOW | L5 | 13 | §2 S8, the ceiling sentence |
| 10 | LOW | L6 | 10 | §6 AC9, against §2 S8 |
| 11 | LOW | L7 | 8 | §2 S6; §6 AC5 |
| 30 | LOW | L7 | 8 | §2 S6, against §6 AC5 |
| 17 | LOW | L8 | 6 | §2 S6; §6 AC4 |
| 26 | LOW | L9 | 7 | §3 Edges, hands-off to 11; §5; §10; against unit 11 §2 S3 |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number. Every tool line number is at `abac6d59`.

## Blockers

None. The candidates were the four seams around the landing reconcile (M1 to M4), because round 1's
B1 and B3 sat there. Each was read against unit 34 §4 and its Rollout. M2, M3 and M4 each fail as a
named exit 2, a NEEDS-HUMAN refusal, or a park at step 6. M1 fails as a NEEDS-HUMAN refusal under the
straggler set. Under the landing form it re-targets a hold without refusing, which is its one silent
outcome. That needs main to file an ask and a hold on it inside the build window, and the held ask
keeps its derived token at the landing. Each fold is local to units 12 and 34, and none leaves the
switch-over without a path to land.

## High

None. The nearest were M5, a claimed mechanism that does not exist, and M7 and M8, where AC10's
"`govkit selfcheck` passes" cannot hold as written. M5 reaches no adopter in this build, which is
why round 1 held M8 at MEDIUM. M7 and M8 are the class round 1 placed at MEDIUM as its M12 and M13,
because the fold is one declaration each.

## Medium

### M1 — P3's names-an-id test is not unit 11 S7's, so a hold on an ask the same delta files names none (2, 28, 44)

**Where.** Unit 12 §4 "The engine", P3; §4 "Classification", the "flip to BLOCKED or DEFERRED naming
an id" row and the "a hold naming no id" row; §6 AC12 and AC14. These are read against unit 11 §2 S7
and §6 AC5.

**Defect.** P3 says a hold names an id "when its target is a filed ask or a spec H1 at the target
tree, and under `--write` every census id counts as filed". It calls this "unit 11 S7's test,
adopted verbatim". Unit 11 S7's test is census id or spec H1, and its census holds every legacy id.
The `--write` carve-out is needed only because the plain rule is evaluated before the write, and §4
"Confirmation" uses "the target tree" for that pre-record state too. So outside `--write`, an ask
the same delta files is not yet filed at the target tree. "Verbatim" is true for `--write` and false
for every other form.

No criterion stages the shape. AC12's shared fixture holds a target naming nothing and a decision
id, and AC14's landing fixture holds no hold.

**Impact.** The two policy sets fail differently.

- Under the straggler set, a delta that adds ask X and ask Y BLOCKED on X classes Y NEEDS-HUMAN. Its
  only exit is `--drop`, which writes a `dropped:` provenance row and no ask row. Y is lost, and
  check 25 reads the entry accounted.
- Under the landing form, when main filed X after the fork together with a hold on it, the hold is
  rewritten to `on <triage-id>`. Y still derives BLOCKED or DEFERRED at the landing, but it then
  releases when the triage ask closes, not when X does. Unit 34's confirm rule never reads hold
  targets, and V6 cannot see it because the triage ask is filed. Unit 11's plan over the tip counts
  X as a census id and predicts the hold on X. So the planner and the engine disagree on exactly the
  kind of record unit 34's status proof compares.

**Fix.** In every form, count as filed each id the target tree files OR the plan itself writes an
ask row for. That is unit 11 S7's census semantics, and the `--write` carve-out then follows from it
rather than standing as a special case. Add to AC12's shared fixture, which unit 11 AC5 also reads, a
new ask BLOCKED on another ask new in the same delta. Expect the hold written verbatim under both
policy sets. Add the same shape to AC14's landing fixture.

**Left-shift.** The shared-fixture rule that round 1 set for B1 holds: AC12 and unit 11 AC5 read one
corpus. It would have caught this had the corpus carried the shape. The class is item 3 below: a
spec that says it adopts another's rule "verbatim" cites the producer's S-item, and the join
compares the wording.

### M2 — the landing form's delta is spelled backwards in unit 34, and its post-merge case plans nothing (20, 13)

**Where.** Unit 12 §2 S6, §8 F7(c) and §3 Edges, the hands-off to 34. Unit 34 §4 "The landing
reconcile", at line 235 of that spec. Unit 9 §2 S13 and §6 AC11.

**Defect.** Unit 9 S13 returns entries "for the side `ours` against the side `theirs`", and AC11
passes the straggler tip as `ours`. So unit 12 S6's "the delta of `<ref>` against HEAD" is
`delta(ours=<ref>, theirs=HEAD)`. Unit 34 §4 pins the landing form as taking "unit 9's no-merge
`delta(ours=HEAD, theirs=<tip>)`", which is the reverse. Unit 12's hands-off to 34 names the form
but not the order.

Separately, S6 admits the form "whether or not a merge of `<ref>` is in progress", and F7(c) says
"during or after the landing merge". Once a landing merge is concluded, HEAD contains the tip, the
merge base is the tip itself, and the delta is empty. No criterion stages a concluded merge.

**Impact.** With `ours=HEAD`, every id the switch-over turned into a view reads REMOVED, because
views anchor no id and the archives are deleted. "Removed row that was live at the merge base" is
NEEDS-HUMAN, so a reconcile built or reviewed from unit 34's sentence parks on every live ask. An
ingest run after a conflicted landing merge has been concluded plans nothing, and the tip's flips
surface only as check 25's unaccounted red.

Read at synthesis, not by a skeptic: unit 34 §4 also says of the tip that "after a clean one it is
HEAD^2". By its own step 1 a merge is clean only when the tip's shards and backlog archives did not
move, so that delta is empty and correctly so. The post-merge form is therefore either vacuous or
wrong. Unit 34's step order ingests before concluding, and check 25 reds the gap, which keeps this
MEDIUM.

**Fix.** Write S6's call as `delta(ours=<ref>, theirs=HEAD)` and name the order in the hands-off to
34. Correct unit 34 §4 in the same fold; G5 audits that spec. Strike "after" from S6 and F7, and
have the form refuse by name when HEAD already contains `<ref>`. That is one condition, and unit 34
never needs the post-merge case. If the post-merge form is kept instead, define it as
`theirs=HEAD^1` and add an AC14 case over a concluded merge.

**Left-shift.** An interface with positional parameters is cited with keyword arguments in every
consumer spec, and class item 3's join compares the bindings across specs. A form admitted in two
states gets one criterion per state.

### M3 — §5's shards-mode refusal is scoped to no verb, and its migration line contradicts S6 (18)

**Where.** Unit 12 §5, the "error / empty / loading states" and "migration" lines. These are read
against §2 S6 and S13, §5's own "security" line, §6 AC9, and unit 34 §4 Rollout steps 5 and 6.

**Defect.** §5 says the engine exits 2 "with the recipe on a shards-mode target", and that "the modes
are inert until the default branch is in builds mode". The migration line is rev-1 text. Rev-2 S6
admits the landing form ONLY while the default tip reads shards, and §5's own security line says so.
Unit 34 Rollout step 5 runs `--write`, a thin driver over this engine's migration set, while
`.memory-tree.conf` still reads shards, and step 6 applies the conf. The refusal names no verb, and
"target" is undefined. AC9 scopes it to `--relocate` and the other side's conf, while AC12 and AC13
pin no fixture mode.

**Impact.** An engine-level mode guard passes unit 12 and then refuses somewhere at the switch-over.
Read against HEAD, it refuses `--write` at step 5. Read against the other side, as AC9 uses it, it
refuses the landing form on every tip that form is admitted for. Read as the migration line, neither
runs. The finder said every reading blocks; the skeptic narrowed that, since the HEAD reading leaves
the landing form alone. It still stops `--write`. Each outcome is a named exit 2 in the unit 34 pass,
never a silent write.

**Fix.** Scope §5's refusal to the straggler set and to the other side's conf, as AC9 states. Say
that `--write` runs over a pre-flip shards tree before the conf flips, and that the landing form
requires a shards-mode default tip under a builds-mode HEAD. Rewrite the migration line to name
those two exceptions. Pin the fixture's mode in AC12 and AC13, with a shards-mode HEAD for the
migration-set run.

**Left-shift.** Class item 2 below. When a fold admits a new state, grep the spec for every sentence
that forbids that state.

### M4 — the collision rule and the CLOSED row still read the `--as` file after P1 moved transferred tokens (19)

**Where.** Unit 12 §4 "Classification", the "flip to CLOSED" row and the paragraph on one disposition
per target. These are read against §4 P1, AC13, AC14, and unit 34 §4 "The landing reconcile", its
confirmation paragraph.

**Defect.** P1 sends a transferred legacy token to the ask owner's folder under the migration set,
and AC13 and AC14 expect it there. The classification row still writes CLOSED "in the `--as` file".
The collision rule, "a planned disposition for a target the `--as` file already disposes is
NEEDS-HUMAN", checks only that file. Unit 34 reads the same rule as a collision "for its target in
its file".

**Impact.** At the switch-over, `--write` puts every step-6 status token in the owner's folder,
holds included. That covers the holds on the triage ask: unit 11 §10 measured five of the seven
legacy holds naming no full id. Suppose the tip then flips such a held id to CLOSED.

1. The landing form plans the CLOSED into the same owner file, per P1.
2. The `--as`-only collision check misses it.
3. Unit 34's confirm rule passes it, because the hold was added AT the switch-over commit, not after
   it.
4. Unit 6 V4, "two rows of one class for one target in one file", reds at step 6's `--check`.

That is a park the step-4 dry run never shows. Unit 34 AC15 flips an id with no prior disposition,
so it stays green.

**Fix.** Make the collision rule read the destination P1 assigns for the record's class and set.
Then decide, and state which. Either a collision there is NEEDS-HUMAN, which parks the landing at
step 4 rather than at step 6. Or the migration set REPLACES a disposition that the switch-over
commit itself wrote, which lets the landing complete and needs unit 34's confirm rule to name it.
Change the CLOSED row's destination to "the P1 home". Add a landing-form arm to AC14 in which the
tip flips an id that carries a step-6 hold.

**Left-shift.** Class item 2 below. P1 moved where a record lands, and the two readers keyed on where
it lands kept the old answer.

### M5 — unit 9's `requires_if` edge installs nothing, so round-1 M8's fix does not hold (31, 48, 16)

**Where.** Unit 9 §4 Data model, "Delta entry"; §2 S12, the `requires_if` clause and its `why`; §6
AC10; §3 Edges, the hands-off to `DEPL-dDerivedDocket-1`. Also the existing edge at
`tools/memory-tree/kit.toml:8`, and the backlog row TOOL-dDerivedDocket-39 that the fold filed.

**Defect.** §4 says "S12's `requires_if` edge is what installs it beside this kit". S12's `why`
says an explicit `shards` value "over-selects the kit harmlessly because govkit has no value
condition". Both assume govkit evaluates `requires_if` when it selects, orders or applies kits. It
does not. Re-checked for this report with `git grep requires_if abac6d59 -- tools/`:

- The only reader is selfcheck check 7 (`tools/govkit/govkit.py:1357-1381`). It grades that the
  named kit is a registry entry and that each condition key appears in the kit's own config key
  lists. It selects nothing.
- `derive_install_order` (`:487-509`) and `derive_unsatisfied_requires` (`:526-547`) read plain
  `requires` only, and nothing in `tools/` evaluates `when_any_key_set`.

The existing edge's own text makes the same apply-time claim ("the edge is FALSE at apply time"), and
TOOL-dDerivedDocket-39's premise is the same selection. Finding 16 is the observation half: AC10's
selfcheck grades an edge only when it is present, so deleting the edge leaves every criterion green.

**Impact.** Round-1 M8's confirmed impact is unchanged. A memory-tree-only adopter that flips to
builds mode gets no memory-recall from `govkit apply`. Its first sign is S15's refusal, which reds
its unguarded `memory hygiene` leg on every run. The hands-off to `DEPL-dDerivedDocket-1` names only
`commit-msg`, so the runbook author will read the edge as the install step. Nothing in this build
reaches such an adopter yet.

**Fix.** Choose one, and record which in §8.

- Restate the edge as a declaration that selfcheck grades, not a selector. Reword §4 and S12's `why`
  so neither claims a selection. Add to the hands-off to `DEPL-dDerivedDocket-1` that the recall kit
  is a prerequisite of the runbook's switch step. Have S15's refusal print the install remedy, and
  extend AC15 to read it. Correct TOOL-dDerivedDocket-39's premise and the `kit.toml:8` text in the
  same fold.
- Or scope a govkit change that evaluates `when_any_key_set` against the target's conf at apply
  time, with an arm. That widens this unit into a kit whose version unit 21 moves.

The first is the smaller fold, and it is true today. Under it, finding 16's proposed observation,
a govkit plan that selects memory-recall, cannot pass; this reading is the synthesis's. The
observation becomes an AC10 presence arm instead: the edge exists and names `BACKLOG_MODE`, staged
RED by deleting it.

**Left-shift.** Class item 4 below: a spec that credits a checker with an effect cites the line that
implements it.

### M6 — unit 9's both-ways hook-list arm ships to every adopter and reds there (34, 49)

**Where.** Unit 9 §2 S12, the arm in `tools/check-wiring.test.sh`; §3 Edges, the hands-off to 13;
§6 AC10. Unit 13 §3, its consumes-from 9, and §6 AC9 inherit the arm.

**Defect.** The arm compares the running tree's tracked `.githooks/` hook files with
`GOV_WIRING_HOOKS`, both ways. That test file ships to adopters.

- `tools/govkit/entries/check-wiring.kit.toml` gives it role `engine`, together with its own
  `check-wiring self-test` `[[gate_leg]]`.
- `WIRE-INTO-PROJECT.md:614` tells every project to wire it as a gate-runner leg.
- `tools/check-wiring.sh` ships verbatim too, so `GOV_WIRING_HOOKS` goes out as gov's list. After
  units 9 and 13 that list names `commit-msg` and `pre-rebase`, which both specs keep gov-only with
  `[[exempt]]` rows.

Check H already decided the adopter case the other way: "A hook this tree does not TRACK is a SKIP,
never a comparison and never a finding" (`tools/check-wiring.sh:213-215`). S12 states no skip
condition, while the existing real-tree arms at `tools/check-wiring.test.sh:621-623` and `:668-669`
skip on absence.

**Impact.** An adopter that tracks only `pre-commit` and `pre-push` fails the list-to-tracked
direction. One that tracks any hook of its own fails the reverse. In gov, the arm sits in a held kit
suite: `check-wiring self-test` is chunk `selftests`, subject `kit`. So the repo-state drift it
exists to catch is graded only on demand.

**Fix.** Keep fixture-built arms in `tools/check-wiring.test.sh`. Put the real-tree comparison in a
gov-only unheld check: an arm of the repo-subject `transition-audit.test.sh` leg, or a govkit
selfcheck arm over the `.githooks/**` surface selfcheck already classifies. If a real-tree arm must
stay in the shipped suite, assert only the tracked-to-list direction, which is the one that catches
an unlisted `.githooks/commit-msg`. Re-point unit 13's consumes-from and AC9 at the chosen home.

**Left-shift.** Class item 5 below.

### M7 — unit 9's new leg has no descriptor, no subject pin, no ceiling and no directory (5, 23, 33, 50)

**Where.** Unit 9 §2 S11 and S12; §4 Files touched; §6 AC10.

**Defect.** S12 lists "the declarations the new moving parts owe in the same commit": the
`commit-msg` `[[exempt]]` row, `GOV_WIRING_HOOKS`, the map claim, and the `requires_if` edge. For
the new `transition-audit.test.sh` leg it gives none of the following.

- A `[[gate_leg]]` in `tools/memory-tree/kit.toml`, or an `[[exempt_leg]]` in
  `tools/govkit/registry.toml`. The map dossier's claim is not a govkit declaration.
- A row in `tools/govkit/subject-pins.tsv`.
- A `ceiling` in `tools/gate-legs.json`, which unit 11 S11 and unit 13 S8 both state.
- A directory. Files touched says "`transition-audit.test.sh` (new)" with no path. Under
  `tools/memory-tree/`, the kit's `include = "**"` engine rule ships the file to every adopter,
  unless it joins the `project-owned` list that withholds the kit's other `*.test.sh` suites
  (`tools/memory-tree/kit.toml:43-44`).

Round 1's "Outside the confirmed set" asked this fold to say which declaration unit 9 writes, and the
rev-2 line does not answer. Units 10 (its F4) and 13 (its S7) each decided the same question for
their own legs.

**Impact.** `govkit selfcheck` is an unguarded declarations leg, and it reds twice at the post-build
bar:

- "claimed by no descriptor and carried by no [[exempt_leg]]" (`tools/govkit/govkit.py:1642-1644`);
- "has no row in tools/govkit/subject-pins.tsv" (`:1714-1718`, selfcheck 7h2).

So AC10's "`govkit selfcheck` passes" cannot hold as written. A leg with no ceiling also reds the
held run-gates canary (`tools/run-gates/run-gates.gov.test.sh:261`) under the landing bar's
`GATE_SELFTESTS=1`. Whether adopters receive the permanent audit's suite stays undecided.

**Fix.** In S12:

1. Name the suite's path and its payload role. If it sits in the kit directory, add it to the
   `project-owned` include list.
2. Give the leg one declaration with its reason. Use an `[[exempt_leg]]`, as its memory-tree
   siblings `memory-hygiene self-test` and `row-keyed merge driver replay` have
   (`tools/govkit/registry.toml:471`, `:475`). Or use a `[[gate_leg]]` with `subject = "repo"` if
   adopters should receive it. Say which and why in §8, as unit 10 F4 did.
3. Regenerate `subject-pins.tsv` with `python tools/govkit/govkit.py selfcheck --write`.
4. Declare the leg's `ceiling` with its basis, sized by `tools/run-gates/ceiling-margin.txt` (see L5).

Name every file this touches in Files touched, and add the undeclared leg to AC10's Red-when.

**Left-shift.** Class item 1 below.

### M8 — unit 11's new leg is declared by no descriptor and pinned by no subject row (6, 22, 36, 51)

**Where.** Unit 11 §2 S11; §4 Files touched; §7 Gates; §6 AC10.

**Defect.** S11 adds `backlog migration selftest`, chunk `selftests`, subject `kit`. It carries a
gate-legs entry, a budget row and a codebase-map dossier claim, and no govkit declaration. Every
sibling memory-tree module selftest is a subject-`kit` `[[gate_leg]]` in `tools/memory-tree/kit.toml`:
`build-index selftest`, `corpus-ids selftest`, `gotchas selftest` and `row-grammar selftest`
(`:169-192`). Files touched omits that file and `tools/govkit/subject-pins.tsv`. §7 omits
`govkit selfcheck`, and AC10 checks codebase-map coverage and `run-selftests.sh --check`, never
govkit. Round 1 recorded this gap outside its confirmed set; the M10 fold added only the budget
row.

**Impact.** At the unit's commit, `govkit selfcheck` reds twice, as in M7: unclaimed
(`tools/govkit/govkit.py:1643`) and unpinned (`:1715`). Unit passes run no gate legs, and §7 does
not name that leg, so the red first surfaces at the post-build bar.

**Fix.** Add a `[[gate_leg]]` to `tools/memory-tree/kit.toml` matching its siblings: argv
`python3 {kit}/migrate_backlog.py --selftest`, subject `kit`, its guard. Alternatively, add an
`[[exempt_leg]]` with its reason. Regenerate `tools/govkit/subject-pins.tsv`. Name both files in
Files touched, add `govkit selfcheck` to §7, and add a selfcheck clause to AC10.

**Left-shift.** Class item 1 below.

### M9 — unit 13's pre-commit edit can unpin the frozen `.githooks/pre-commit:48` waiver (24)

**Where.** Unit 13 §4 "The session step, and where it may sit in a shipped file"; §2 S2; §6 AC9.
These are read against §7's `install-prefix (shipped surface)`.

**Defect.** `tools/install-prefix-waivers.txt` holds the frozen, position-keyed row
`.githooks/pre-commit:48`, the `gate_at` dual-spelling probe. It is a live `waived` hit in
`check-install-prefix.sh --list`. S2 adds a refusal to `.githooks/pre-commit`, and nothing bounds
where it goes. The refusal naturally sits beside the branch guard at lines 18-34, above line 48. §4
gives the below-the-waived-lines rule only for `tools/check-wiring.sh`, and AC9's Red-when names
only check-wiring's lines.

**Impact.** Lines added above 48 shift the probe. The waiver goes stale and the probe becomes an
unwaived hit, so `install-prefix` reds at the post-build bar, and AC9's stated break never fires.
This is round-1 M11's class, which the fold fixed for unit 8 and for check-wiring but not here.

**Fix.** State in §4 that every new pre-commit line sits below line 48. Alternatively, convert the
`:48` waiver to an in-line `gov:root-fixture — <reason>` marker and drop the row in the same commit,
as unit 8 S14 does for its two. Extend AC9's Red-when to the pre-commit waiver.

**Left-shift.** Class item 7 below. The record is
`memory/gotchas/line-keyed-registry-reds-on-a-file-that-grew.md`.

### M10 — unit 13's four-carrier correction is unobserved, and its sentence restates the scope error (8, 27)

**Where.** Unit 13 §4 "Why a library beside the hooks, and what it may read", the paragraph naming
four carriers and the sentence it pins. Also §4 Files touched. There is no §2 item and no §6
criterion.

**Defect.** Rev-2 commits to rewriting four carriers: the `.githooks/pre-push` header, lines 6-9;
`tools/check-wiring.sh:188-190`; `tools/check-wiring.test.sh:811`; and
`memory/gotchas/hookspath-resolves-into-another-checkout.md`. That commitment lives only in §4,
Files touched and the rev-2 line. No S-item carries it and no AC observes it.

The sentence it pins opens with "`core.hooksPath` is repo-global". The same paragraph measures the
absolute value as coming from a per-worktree `config.worktree` override, on seven of nine live
worktrees. S5 speaks of the "effective" per-worktree value, and AC12's absolute case is built as
exactly such an override. The finder checked the worktree it ran in: its `core.hooksPath` comes from
worktree scope, while the shared config holds the relative `.githooks`.

**Impact.** Nothing observes whether the premise that misled design §18.1 is corrected. The
corrected text also teaches the next reader of the pre-push header, check-wiring and its test that
one shared value governs every worktree. A reader who changes the shared value will believe it
governs the seven worktrees that override it. The gotcha body is told to name each measurement's
configuration, which covers that carrier in part; the three code carriers get only the sentence.

**Fix.** Make the rewrite an S-item with an AC that greps each carrier. Expect zero hits for BASE's
"repo-global and absolute" wording and one hit for the new sentence. Reword the sentence to say that
the shared value applies unless a worktree's `config.worktree` sets its own, and that which hook
files run depends on the value in effect for that worktree: an absolute value runs the checkout it
names, the relative `.githooks` runs the worktree's own.

**Left-shift.** Round 1's class item 4, an environment premise stated as universal, applied to the
fold's own correction. A correcting sentence names the configuration it holds under, the same test
the original failed.

### M11 — unit 9's "the tip's tree, never HEAD's" has no criterion that can see it (3)

**Where.** Unit 9 §2 S13 and S14; §6 AC11 and AC12.

**Defect.** S13's `accounted(entries, tip)` and S14's `--at <sha>` both account against the named
commit's tree, "never HEAD's". AC12's Red-when names "`--at` reads HEAD's history or tree". Neither
criterion stages a tip whose tree differs from HEAD's in its RELOCATED rows.

- AC11 passes a tip that already carries the rows, and it does not fix HEAD.
- AC12's fixture is a merge unaccounted in both trees. A walk of `<sha>`'s history that accounts
  against HEAD's tree, reading `BACKLOG.md` from disk as full mode could, still exits 1 and passes.

Unit 12 AC5 and unit 13 AC5 both run with HEAD equal to the tip, so no criterion in any unit catches
the tree half.

**Impact.** An implementation that accounts against HEAD's tree passes both criteria, and its
consumers read the wrong tree. Unit 13's pre-push audits a pushed ref that need not be HEAD. Unit
12's `--stragglers` accounts at the observed `origin/HEAD`, which a session tree's HEAD is not. A
pushed tip carrying its rows is then refused, or a tip lacking them passes whenever HEAD carries
them. The bar still binds at the default branch.

**Fix.** In AC11, call `accounted(entries, tip)` with HEAD at a commit lacking the rows and `tip`
carrying them, expecting every entry accounted. Stage the reverse and expect none. Add to AC12 a
pushed sha whose tree carries the RELOCATED rows while HEAD's does not, expecting exit 0.

**Left-shift.** Class item 6 below: the right input and the wrong one must differ in the fixture.

### M12 — unit 11's `design-named` basis has no input (7)

**Where.** Unit 11 §2 S6 and S1; §8 F5; §6 AC4. These are read against unit 33 §4.

**Defect.** S6's three selection rules are a closing spec, a commit that names the ask, and a hold
the row names. None of them produces basis `design-named`, and no S-item, option or conf key gives
the planner the three ids. Design §21.5 names them as gov ids. Rev-2 AC4 nonetheless requires "the
three design-named rows" to be listed in a fixture repository, and unit 33 §4 relies on the planner
pre-filling them. S1 declares `--plan` repo-agnostic, "so an adopter's deployer build runs it
unchanged". Unit 33 justifies its own literal list only because its script "ships nowhere", and
`migrate_backlog.py` is a kit module.

**Impact.** The builder must either hard-code three gov ids into a shipped kit module, where every
adopter's run carries them, or leave AC4 unstageable.

**Fix.** Add the input to S6, for example an optional `--design-named <file>` of ids. It is absent
in an adopter's run, and names this build's record in gov's run. AC4 supplies a fixture file of
three `EXMP` ids, and a run without the file lists no `design-named` row.

**Left-shift.** Class item 3 below: a value a criterion requires comes through an S-item's input,
never from the spec's prose.

### M13 — no unit moves the check-wiring kit version (56)

**Where.** Unit 13 §4 Files touched, the clause "the check-wiring and drift-audit version constants
where `kit version markers` requires a move". Unit 9 §4 Files touched and §7 Gates.

**Defect.** `tools/check-kit-versions.sh` checks only that each constant is present and that each
marker pairs with its constant. It has no need row for `KIT_CHECK_WIRING_VERSION` at all, so the leg
never requires a move and unit 13's condition cannot fire. This build adopted a one-owner rule for
kit versions. Unit 21 moves drift-audit, govkit, lexicon and codebase-map, which covers unit 13's
drift-audit half. No spec in the build names `KIT_CHECK_WIRING_VERSION` or a `gov:kit check-wiring@`
stamp. Units 9 and 13 both change shipped check-wiring bytes: `GOV_WIRING_HOOKS` at
`tools/check-wiring.sh:209`, the session step, and new test arms. Unit 9's §7 omits
`kit version markers`.

**Impact.** The landing range ships a changed check-wiring still at `KIT_CHECK_WIRING_VERSION=1.2`.
An adopter pulling it cannot tell the vintages apart. TOOL-dMuffledSentinel-3 records that this
class got inCMS's pull refused, and a follow-up bump build cleared it.

**Fix.** State the move unconditionally. `KIT_CHECK_WIRING_VERSION` and its `gov:kit check-wiring@`
marker move once in the landing range that carries units 9 and 13. Name the unit that moves them,
under the build's one-owner rule. Add `kit version markers` to unit 9's §7.

**Left-shift.** Class item 4 below. The monotone check G1 round 2 proposed for
`tools/check-kit-versions.sh` covers this too, once the file gains a need row for check-wiring.

## Low

### L1 — the landing form's "later of the current value" is never staged, and its dry run promises no cutoff (12)

**Where.** Unit 12 §4 "The landing form's cutoff"; §2 S9; §6 AC14. These are read against unit 34
§4 "The landing reconcile" step 4 and its AC20.

**Defect.** §4 prints "the later of the current value and the first date strictly after every
`filed` date it wrote". AC14, and unit 34 AC15, stage only a new ask filed after the current cutoff.
So a form that always prints the day after its newest `filed` passes both. Separately, S9 never says
the landing form's `--dry-run` prints the cutoff line. Its rule, "exits 0 only when the plan would
write", has no criterion. Unit 34 step 4 and AC20 act on that dry run's output.

**Impact.** Main's asks filed in the build window usually predate the switch-over's cutoff. With the
missing half, step 5 lowers the cutoff, V9 and V12 fire on migrated asks, and step 6 parks the
landing. AC20 reads a line no unit 12 criterion guarantees.

**Fix.** Add an AC14 case whose HEAD cutoff is later than the new ask's `filed`, expecting the
current value printed. State in S9 that the landing form's dry run prints the cutoff line. Assert
that AC14's dry run exits non-zero while any CONFIRM or NEEDS-HUMAN entry stands.

**Left-shift.** Class item 6 below.

### L2 — `--stragglers` finds candidates with `git log --source`, which labels each commit with one ref (43)

**Where.** Unit 12 §4 "Straggler inventory"; §2 S8.

**Defect.** Candidates come from one `git log --source` walk. `--source` labels each commit with the
ONE ref that reached it first. So a ref whose backlog commits are all shared with an earlier
labelled ref shows no commit and is never a candidate. Reproduced for this report with git
2.54.0.windows.1 in a scratch repo. Refs `s1`, `s1copy` at the same tip, and `s1fork` forked from
`s1` with no backlog commit of its own gave one commit, labelled `s1` only.

**Impact.** S8's per-ref rule, "a ref is listed while its delta holds an entry", undercounts. A local
branch and its pushed `origin/` copy are listed once. A branch forked from a straggler is never
listed. Unit 13's drift-signal value and session note inherit the undercount.

**Fix.** Walk the flagged commits once, then map them to refs with `git for-each-ref --contains`.
Alternatively, define a candidate as any selected ref whose tip reaches a flagged commit. Add an
AC6 arm with two refs at one straggler tip and one fork.

**Left-shift.** A spec that rests a population on a git primitive's output names the property it
relies on, and §10 measures it, as unit 9 §4 measured its hook order.

### L3 — unit 13 promises unit 35 a topology helper that nothing defines (14)

**Where.** Unit 13 §3 Edges, the hands-off to 35; §2 S8; §6 AC12. These are read against unit 35
§2 S2.

**Defect.** The rev-2 hands-off promises "the linked-worktree topology helper
`straggler-guard.test.sh` builds for AC12", which unit 35's scratch clone reuses "so the two cannot
drift". Unit 35 S2 binds itself to it. No unit 13 S-item defines that helper as an entry point, with
a name and a sourceable file or a mode that builds the topology without running the arms. No AC
observes it, and unit 35's Files touched omits the suite.

**Impact.** A unit 13 build that meets every S-item can inline the topology in the AC12 arm. Unit 35
must then source a test suite, edit a file outside its scope, or rebuild the topology, and rebuilding
it is the drift the edge exists to prevent.

**Fix.** Add to S8 a named helper callable without running the arms: a `--topology <dir>` mode, or a
function in a sourced fixture file. Add an AC showing that AC12 and unit 35's clone both call it.

**Left-shift.** Class item 3 below. Round 1's join, "every hands-off cites an `S<n>` of its own
spec", prints this edge as a hit.

### L4 — unit 13's new leg is guarded away from `tools/check-wiring.sh`, which its arm runs (15, 45)

**Where.** Unit 13 §2 S8; §6 AC12.

**Defect.** The rev-2 guard covers `.githooks/`, `tools/memory-tree/` and `tools/lib/`. AC12's arm
runs `tools/check-wiring.sh --fix` and `--session` in the fixture and grades S5's `hooks own-tree`
note, which that file writes. That breaks §8 F6(ii)'s own rule of guarding "on the directories its
inputs live in". The other reader of S5 is `check-wiring self-test`, which is held.

**Impact.** On a scoped bar, an edit that touches only `tools/check-wiring.sh` and breaks the note
runs no leg that exercises it. `tools/memory-tree/kit.toml:147-155` records why this now matters:
since the push boundary decides whether a full bar is owed, a guard omitting a file the leg reads
costs a wrong merge verdict.

**Fix.** Add `tools/check-wiring.sh` to the leg's guard in S8.

**Left-shift.** Class item 7 below.

### L5 — unit 13's ceiling rule is the budget file's ×1.5, not the ceiling margin (53)

**Where.** Unit 13 §2 S8, the ceiling sentence.

**Defect.** S8 re-declares the leg's ceiling at "that reading times 1.5". An unheld leg's ceiling is
governed by `tools/run-gates/ceiling-margin.txt`: headroom of max(120 s, 1.0 × max) above the
evidenced maximum. The unguarded leg `leg ceilings clear their evidenced maximum`
(`derive-ceilings.py --check`) reds any ceiling short of that. The ×1.5 factor belongs to
`tools/run-gates/selftest-budgets.txt`, which budgets held suites and says it is not the hang bound.

**Impact.** 1.5R is always short of R + max(120, R). So the derive-ceilings leg reds as soon as the
reading is distilled into the evidence file. The interim 300 s also fails once the reading exceeds
150 s.

**Fix.** Size the ceiling by `ceiling-margin.txt`, at least R + max(120 s, R), with the reading
recorded through `derive-ceilings.py --write`.

**Left-shift.** Class item 7 below. A spec that restates a factor from a file that owns it is prose
beside the source that owns the number, charter §6.

### L6 — unit 10's mutation sweep stops at AC7, so the rev-2 arms need never be seen RED (10)

**Where.** Unit 10 §6 AC9, against §2 S8.

**Defect.** S8 requires replay arms for "every behaviour above ... each observed RED with its fix
unstaged. Observed by AC9". AC9 still reads "each of AC1 to AC7's fixes". That predates rev-2's
AC10, two re-rendered views and two shards over a view base, and AC11, the builds-mode `BACKLOG.md`
population.

**Impact.** A refusal keyed on "either side is a view", or a mis-rooted `BACKLOG.md` selector, can
sit behind arms that grade nothing. Those are the breaks round-1 M19 and M20 named, and charter §7
requires each new gate's failing case to be observed.

**Fix.** Extend AC9 to cover AC1 through AC11.

**Left-shift.** Class item 2 below. An enumerated range in a criterion is the phrase to grep when a
fold adds a criterion after it.

### L7 — unit 8 stages V16 and never V15 (11, 30)

**Where.** Unit 8 §2 S6; §6 AC5.

**Defect.** Rev-2 S6 skips every ask row on either unusable cutoff: V15, a blank one, or V16, one
that is not a `DATE`. It cites AC5 as the observation. AC5 stages only `2026-9-30`, the V16 case.

**Impact.** A check 13 that compares a blank cutoff as the empty string reads every ask as filed
after it. It then reds the 27 legacy foreign anchors, which is F2's rejected option (a), while AC5
stays green.

**Fix.** Add to AC5 a builds-mode fixture with `ASK_CUTOFF=""`, expecting every ask row skipped and
one line naming V15.

**Left-shift.** Class item 6 below: one arm per named member of a set.

### L8 — unit 6 stages hold release for R5 and not R6 (17)

**Where.** Unit 6 §2 S6; §6 AC4.

**Defect.** R5 and R6 both carry "has a live target". The round-1 M14 fold stages release only for a
BLOCKED row whose target folds CLOSED, and AC4's Red-when names only R5. AC4's per-rule R6 fixture
uses a live target, so a fold that drops the test from R6 still derives DEFERRED there. AC7 permutes
order and AC10 checks verdicts, and neither can see it.

**Impact.** A DEFERRED ask never releases when its `until` target closes, which is ruling D5's
release-id meaning. Unit 11's prediction and unit 34 AC3 run the same fold, so neither can tell.

**Fix.** Add to AC4 an ask whose only hold is a DEFERRED row with an `until` target that folds CLOSED,
deriving OPEN, and name R6 in the Red-when.

**Left-shift.** Class item 6 below.

### L9 — units 7 and 11 name a flip-time view measurement that no scope item performs (26)

**Where.** Unit 7 §3 Edges, the hands-off to 11; §5 perf; §10. Unit 11 §3 Edges, its consumes-from
7, and §2 S3.

**Defect.** Unit 7 hands unit 11 "the view renderer the planner measures prospective views with",
and its §10 says "the planner re-measures the view at flip time". Unit 11's consumes-from repeats
the claim. Unit 11 S3 and AC7 size only each slug's prospective `BACKLOG.md` against
`INDEX_CAP_BYTES`, which unit 6's row renderers produce. No S-item or AC in unit 11 renders or sizes
a family view.

**Impact.** Nobody carries the flip-time measurement both specs rely on, so the 2026-09-13 pinned
figure is the only one. Each edge names a consumption no scope item performs. Rev-2 edited this very
hands-off to drop `--asks --json` and left this half standing.

**Fix.** Either add view sizing to unit 11 S3 with an AC, or strike the claim from unit 7's §5, §10
and both edge lines.

**Left-shift.** Class item 3 below.

## Left-shift, by class

1. **An observation outside the confirmed set is never folded** (M7, M8: 8 ids). Round 1 wrote both
   gaps in its "Outside the confirmed set" section and named which fold should decide them. Neither
   rev-2 line answers. Two halves close this.
   - The documented check is for the synthesis. An out-of-set observation is filed where a fold
     reads it: as a row in the build's `BACKLOG.md`, or as a named item the next fold's §9 line must
     answer. It is never left only in the report's prose.
   - The mechanical half is round 1's class item 3(a), a `tools/check-spec-tokens.py` join. A spec
     that adds a leg to `tools/gate-legs.json` lists a descriptor file and
     `tools/govkit/subject-pins.tsv` in Files touched, and `govkit selfcheck` in §7. It was proposed
     and not built. Built, it prints units 9 and 11 as hits. Run it by hand over the rev-3 fold
     before committing it, and print hits and near-misses as charter §7 requires.
2. **A fold moves one rule and leaves its readers on the old premise** (M3, M4, M5, L6, and M2's
   post-merge half). This is `memory/gotchas/amendment-leaves-its-other-half-standing.md`. P1 moved
   where a transferred token lands, and the CLOSED row and the collision rule kept "the `--as`
   file". S6 admitted a shards-mode tip, and §5 kept an unscoped refusal and "inert until builds".
   AC10 and AC11 were added, and AC9 kept "AC1 to AC7". The documented check is for whoever folds:
   for each rev-3 change, grep the spec and every sibling its edges name for the phrases that read
   the changed rule, and fix or confirm each hit in the same fold. This round's phrases are
   `--as` file, `shards-mode`, `inert until` and `AC1 to AC7`.
3. **A cross-spec interface restated rather than cited** (M1, M2, M12, L3, L9). Unit 12 P3's
   "verbatim" is not verbatim. Unit 34 spells unit 9's delta with its arguments reversed. Units 7
   and 11 name a measurement nobody performs, unit 13 hands off a helper it never defines, and unit
   11 promises a basis with no input. Round 1's join 1(a), every hands-off and consumes-from citing
   an `S<n>`, catches L3 and L9. For M1 and M2 it extends: a positional interface is cited with
   keyword arguments in every consumer, and a claim of verbatim adoption cites the producer's
   S-item. `check-spec-tokens.py` can print both as near-misses when two specs bind differently.
4. **A spec credits a checker with an effect its code does not have** (M5, M13). govkit never
   evaluates `requires_if` at apply, and `tools/check-kit-versions.sh` never requires a move. Both
   claims read the checker's name or a neighbouring comment rather than its code. The records are
   `memory/gotchas/spec-names-code-its-base-lacks.md` and `memory/gotchas/armed-but-unreachable-rule.md`.
   The documented check: a spec sentence of the form "<tool> installs, selects, requires or refuses
   X" cites the `file:line` at BASE that does it. M13's half also has the mechanical answer G1 round
   2 proposed, a monotone version check, once `tools/check-kit-versions.sh` gains a need row for
   check-wiring.
5. **A real-tree assertion in a shipped suite** (M6). A suite govkit ships as `engine` runs in trees
   whose population differs, so a set-equality over gov's population reds there on arrival. The
   nearest record is `memory/gotchas/pin-copied-from-another-corpus.md`. The documented check: an
   arm that reads the running tree's own population lives in a repo-subject suite that does not
   ship, or skips on absence as `tools/check-wiring.test.sh:621-623` does.
6. **A criterion whose fixture cannot tell the right input from the wrong one** (M11, L1, L7, L8,
   and M1's fixture half). "The tip's tree, never HEAD's" is staged with HEAD at the tip. "The later
   of the current value" is staged with the current value earlier. "V15 or V16" stages V16, and "R5
   and R6" stages R5. This is `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
   in its fixture form. Round 1's M27 fix already used the cure, commits dated on distinct days, so
   the build knows it. The documented check: for every "X, never Y" or "X or Y" in an S-item, the
   fixture makes X and Y differ, with one arm per named member.
7. **A position, a guard or a ceiling the new lines must respect** (M9, L4, L5). Round 1's join 3(c)
   ties a Files-touched path to the install-prefix waiver registry and asks for the leg in §7.
   Extend it: such a path also owes a placement bound below its last waived line, which unit 13
   states for `tools/check-wiring.sh` and not for `.githooks/pre-commit`. A new leg's guard covers
   every script its arms run. A new ceiling is sized by `tools/run-gates/ceiling-margin.txt`, never
   by the budget file's multiplier. The last two are documented checks for the spec author.

## Outside the confirmed set

Nothing new is carried here. Two readings made at synthesis qualify confirmed entries, and each is
marked in its entry rather than counted: the clean-merge half of M2, and the conflict between
finding 16's proposed fix and M5. Neither was put to a skeptic.

## What this round did not cover

- **Units outside G2**, read only where an edge or an interface named them. The unit-34 halves of
  M1, M2, M3, M4 and L1, and the unit-35 half of L3, sit in specs group G5 audits. Each fold should
  land in both specs at once. Nothing here clears units 1 to 5 or 14 to 36, PLAY-dDerivedDocket-1 or
  DEPL-dDerivedDocket-1.
- **Unit 14**, retired at WONTDO and not a subject this round. The Serves line omits it for that
  reason.
- **The design record's measured figures**, which were not re-derived. The one measurement taken for
  this report is L2's `git log --source` labelling, reproduced with git 2.54.0.windows.1 in a
  scratch repo.
- **The 19 refuted findings**, which are not reproduced here. They were refuted, not lost, as the
  run-integrity counters show.
- **The rev-3 fold this report prescribes.** It will be unreviewed surface, and its review is the
  closing diff review's.
