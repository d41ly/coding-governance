**Serves:** spec-audit TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1

# dDerivedDocket — spec audit of topic group G5, the switch-over with its CI, arming and docs, round 1

*Node `d`, 2026-09-14. A Tier-2 adversarial pass over the seven specs of topic group G5: remote CI
(unit 32), the delegated signing of the same-id and triage tables (33), the switch-over (34), arming
and the real-tree staged breaks (35), the memory-tree docs and agent carriers (36), the charter
template (PLAY-dDerivedDocket-1) and the adopter runbook (DEPL-dDerivedDocket-1). Four primed finder
lenses ran, then a skeptic stage prompted to REFUTE each finding in five batches, then this
synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
and the spec brief `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md`,
whose roster table maps each unit to its design sections and whose edge table lists every cross-unit
dependency. Sibling specs outside G5 were read wherever an edge or an interface named them, because
contradiction between specs is in scope. This synthesis re-read units 6, 9, 11, 12 and 15 at the
sites each entry names. The G2 round-1 report was read where it meets unit 34, because five entries
here are the other end of defects it recorded, and the G3 report where it meets unit 35. Every
blocker and every high below was re-checked against source at `abac6d59` before it was written down,
and the sites read are named in each entry. Every source cited is byte-identical between `abac6d59`
and the tree this report was written in: the only commits since BASE touch this build's own folder
and the two generated indexes, `memory/LIVE.md` and `memory/ledger/2026-09.md`.*

**Round: 1.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md@20760fcc0a8453e9a072fe5752da0ff13984ecd8`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-33.md@ddb0e9af93e8fa54fe04424730e8d682d93fca17`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md@032aff2e975cfafdcfdf9d4d7b03a03adc21a613`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-35.md@f6ac57132e47e0b9c6df874a2f2b98a7006d9e73`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-36.md@45efed28c764279fba7bcacfa8fafd0715ac0afe`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-PLAY-dDerivedDocket-1.md@6c481b864ae786ac21d8f6cf49802f5956d641ec`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-DEPL-dDerivedDocket-1.md@d1a05e11c10daed1ee6051aeb00d07bedf117bea`

## Verdict: BLOCKED

Three blockers stand, carried by six confirmed findings, and all three sit in unit 34: the
switch-over's writer and its landing reconcile. The owner delegated the two signatures "so the
switch-over lands in this run", and as specified it cannot.

- **B1** (13, 31). Five of the seven legacy BLOCKED and DEFERRED rows name no full id. Unit 11
  previews each as a hold on a triage ask that "the switch-over files". Unit 34 never mints, files or
  substitutes that ask, and the engine its `--write` drives writes nothing past a hold that names no
  id. `--write` refuses gov's corpus.
- **B2** (14, 32, 58). The reconcile's step 2 "runs the delta engine", and no verb unit 12 specifies
  has the reconcile's direction and confirmation semantics. The flip parks at its own landing.
- **B3** (34). Step 3 re-runs the signer over "the triage population recomputed at the merged tree".
  The signer's only input is a worksheet the planner builds from authored shards and backlog
  archives, which the merged tree no longer holds, and nothing writes what it would sign. V10 then
  reds the landing bar. Measured for this report: 64 ids absent from the shards, archives, build
  folders and decision log on 2026-09-06 are OPEN rows in the shards at BASE, and 61 of them are
  homed on builds with no non-terminal unit. The population step 3 serves is the routine case, not
  an edge.

B1 and B2 are G2's B1, B2 and B3 seen from the consumer side. They are not new defects, and each
folds once, in units 11, 12 and 34 together. B3 is new. One high, H1, sits in the same reconcile:
the cutoff is never re-derived, so every ask main files in the window reds V12 and V14 at the landing
bar. Three of the eleven blocker-or-high defects therefore live in the four numbered steps of unit
34's §4 "The landing reconcile". Each surfaces only at the landing, outside any unit pass and after
the closing review, where AC15's rehearsal cannot reach it: that rehearsal names no verb and writes
nothing.

Eight HIGH defects stand, carried by thirteen confirmed findings.

- **CI** (H2 to H5). The per-sha verdict D12-i12 asks for is red on every push, for two host reasons
  unit 32 never observed. The charter render bakes the node's primary-tree path (H2), and
  `actions/checkout` leaves the drift audit no `origin/HEAD` (H3). The held-suite schedule, read
  literally, grades 7 of 62 suites (H4). Unit 32's AC3 cannot pass before the flip (H5).
- **Arming** (H6). Unit 35's AC5 cannot reach the refusal it names in a single-tree scratch clone.
- **Signing** (H7, H8). Unit 33's AC3 and AC10 each red on a correct implementation.

Every blocker and high is a defect in a document this round read, so the disposition
`memory/guides/BUILD-METHOD.md` M4 prescribes is FOLD for all of them. Four folds should be decided
rather than folded silently, and each takes a §9 line.

- B2's confirmation rule for the tip's flips, which G2 already named a design A6 point (lab case
  e09b).
- B3's route: build a post-switch triage input and a writer for its dispositions, or park when the
  population is non-empty. Parking concedes the mandate's outcome on the routine case measured above.
- H1's fold moves `ASK_CUTOFF` to the landing, which widens the ungraded window unit 34's F2
  accepted from one day to the build's span.
- H2's route: a clone at the primary-tree path inside the workflow, or an answer-overridable probe in
  the renderer, which is the playbook kit's surface and another unit.

The blocker count re-arms M4's loop, so round 2 is owed. The folded text is unreviewed surface
(`memory/gotchas/fold-text-is-unreviewed-surface.md`). Round 2 should re-read unit 34's S1, AC2, §4
reconcile and AC15, unit 33's record shape, rule order and header cells, and unit 32's job
environment, matrix derivation and AC3.

Review shape: raw 75, confirmed 56, refuted 19, unverified 0, precision 0.75. Run integrity below
reads complete.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

Every counter that could make this run incomplete is zero, so the finding set is complete for what
the four lenses were primed to hunt. That is not a claim that G5 holds no other defect. It is a claim
that nothing was lost between the lenses and this page. The pipeline's duplicate count of 0 comes
from its own exact-match dedupe. On reading, ten groups of confirmed findings each describe one
defect from two or three lenses: 1/48, 2/30/53, 11/36/55, 13/31, 14/32/58, 15/37, 39/61/70, 41/64,
49/67 and 52/65. Each group is folded into one entry below, and every count on this page stays per
finding id.

## Review shape

Raw 75, confirmed 56, refuted 19, unverified 0, precision 0.75. The 56 confirmed ids collapse to 42
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 6 | 3 |
| HIGH | 13 | 8 |
| MEDIUM | 32 | 26 |
| LOW | 5 | 5 |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the G1 to G4
reports used, so the five groups' counts compare.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  layer which stays inert or broken, or which admits or refuses a state against an owner ruling,
  while its suite reads green. In each case the fold is local to one or two specs, or needs one
  decision.
- MEDIUM covers three things: a contradiction between specs with a bounded consequence, a
  declaration or edge a spec owes, and a rule whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small.

Against the finders' ratings, thirteen findings move.

- Up to BLOCKER: 13, 14, 31, 32 and 58, from high. They are G2's B1, B2 and B3 seen from unit 34,
  and G2 adjudicated those at BLOCKER. Also 34, from medium, on the measured population in B3.
- Up to HIGH: 12, from medium. AC10 cannot pass as written, the class G3's H9 and G4's H7 put at
  HIGH. Also 39 and 53, from medium, because each joins an entry whose other findings were rated
  high on the same reasoning (61 and 70, and 2 and 30).
- Down to MEDIUM: 9, a criterion gap, the class G1 to G4 put at MEDIUM. Also 55, which is G2's M5
  from the other side, and G2 put that at MEDIUM. Also 52 and 65: a declaration whose absence reds a
  leg at the post-build bar, the class G2 put at MEDIUM, with a one-line fold.

Precision at 0.75 is the highest of the five groups (G1 0.56, G2 0.57, G3 0.64, G4 0.53), and well
above the ~0.5 floor `AGENTS.md` §8 sets.

The dominant class is again `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`.
Ids 3, 4, 5, 6, 9, 15, 17, 18, 19, 21, 24, 27, 28, 56 and 59 are that class outright, which is 15 of
the 56, and ids 1, 2, 11, 16, 25, 29, 36, 37, 41, 48, 55 and 64 have it as one half. Three carry a
`Red when:` their observation cannot see: 6, 18 and 59. The outright rate, about a quarter, is lower
than the third G1, G3 and G4 measured. The class still survives spec authoring in every group.

Two clusters are new to G5.

- **The CI runner is not a node** (H2, H3, M9, M10, M11). Unit 32 chose `windows-latest` as "the
  environment every recorded green was earned in". That environment was never only the OS and the
  shell. It was also a clone at the primary-tree path, an `origin/HEAD` that `git clone` set, and a
  machine with no job limit. Each of the five entries is one of those differences.
- **An observation staged in a tree that lacks the property** (H5, H6, M4, M12). A shallow-clone
  DEAD PROBE observed before the flip that arms it. A straggler refusal staged where the branch guard
  and BASE's hooks answer first. A kit change only builds mode exercises, shipped to adopters who run
  shards. A scratch landing that meets the real pre-push hook. Each observation is right about the
  tree it assumes and wrong about the tree the spec builds.

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 13 | BLOCKER | B1 | 34 | §2 S1; §3 Edges; §6 AC2, against 11 S7 and §10, 12 §4 |
| 31 | BLOCKER | B1 | 34 | §2 S1; §6 AC2, against 11 S7, 12 S4 |
| 14 | BLOCKER | B2 | 34 | §4 The landing reconcile step 2; §6 AC15 |
| 32 | BLOCKER | B2 | 34 | §4 The landing reconcile step 2; §8 F5; §6 AC15 |
| 58 | BLOCKER | B2 | 34 | §4 The landing reconcile step 2; §6 AC15; §8 F5 |
| 34 | BLOCKER | B3 | 34 | §4 The landing reconcile step 3, against 33 §3 and 11 S2 |
| 33 | HIGH | H1 | 34 | §4 ASK_CUTOFF, against §4 The landing reconcile step 2 |
| 50 | HIGH | H2 | 32 | §4 Why one file, and why windows-latest; §2 S3 |
| 51 | HIGH | H3 | 32 | §2 S1 and S3; §4 Why one file |
| 1 | HIGH | H4 | 32 | §2 S4; §6 AC5 |
| 48 | HIGH | H4 | 32 | §2 S4; §4 The three triggers; §6 AC5 |
| 2 | HIGH | H5 | 32 | §6 AC3 |
| 30 | HIGH | H5 | 32 | §6 AC3; §4 Liveness; §5 testing |
| 53 | HIGH | H5 | 32 | §6 AC3; §4 Liveness and Why the pre-landing checks |
| 39 | HIGH | H6 | 35 | §2 S2 and S6; §6 AC5 |
| 61 | HIGH | H6 | 35 | §2 S2 and S6; §4 What "the real tree" means here |
| 70 | HIGH | H6 | 35 | §2 S2 and S6; §6 AC5 |
| 8 | HIGH | H7 | 33 | §6 AC3; §4 The same-id rules |
| 12 | HIGH | H8 | 33 | §6 AC10; §4 Data model |
| 11 | MEDIUM | M1 | 33 | §4 Data model, Outputs; §6 |
| 36 | MEDIUM | M1 | 33 | §4 Data model, Outputs |
| 55 | MEDIUM | M1 | 33 | §4 Data model, Outputs |
| 15 | MEDIUM | M2 | 34 | §2 S1; §6 |
| 37 | MEDIUM | M2 | 34 | §2 S1; §6, against 12 §4 |
| 16 | MEDIUM | M3 | 34 | §5 error states; §2 S1 |
| 60 | MEDIUM | M4 | 34 | §2 S10; §4 The three drift signals added |
| 35 | MEDIUM | M5 | 34 | §5 risks |
| 69 | MEDIUM | M6 | 34 | §2 S10; §4 Files touched |
| 52 | MEDIUM | M7 | 32 | §2 S6; §7 |
| 65 | MEDIUM | M7 | 32 | §2 S6; §7 |
| 38 | MEDIUM | M8 | 36 | §2 S7; §4 Files touched; §7 |
| 49 | MEDIUM | M9 | 32 | §4 The three triggers; §2 S4 |
| 67 | MEDIUM | M9 | 32 | §4 The three triggers; §2 S4 |
| 3 | MEDIUM | M10 | 32 | §6 AC4 |
| 4 | MEDIUM | M11 | 32 | §2 S3 and S4; §5 observability |
| 40 | MEDIUM | M12 | 35 | §2 S2 to S4; §4 Rollout |
| 42 | MEDIUM | M13 | PLAY | §2, §3 and §10, where the item is absent |
| 71 | MEDIUM | M14 | PLAY | §2 S2; §4 Proposed text; §10 |
| 29 | MEDIUM | M15 | DEPL | §2 S2; §4 step 3; §6 AC3 |
| 41 | MEDIUM | M16 | DEPL | §4 steps 1 and 4; §6 AC3 |
| 64 | MEDIUM | M16 | DEPL | §4 steps 1 and 4; §6 AC3 |
| 5 | MEDIUM | M17 | 32 | §2 S1 and S5 |
| 6 | MEDIUM | M18 | 32 | §6 AC8; §2 S7 |
| 9 | MEDIUM | M19 | 33 | §2 S2; §6 |
| 56 | MEDIUM | M20 | 33 | §6 AC8; §2 S6 |
| 17 | MEDIUM | M21 | 34 | §6 AC4 |
| 18 | MEDIUM | M22 | 34 | §6 AC14 |
| 19 | MEDIUM | M23 | 34 | §2 S10; §6 AC10 |
| 59 | MEDIUM | M24 | 34 | §6 AC9; §2 S9 |
| 24 | MEDIUM | M25 | 36 | §2 S4; §6 AC4 and AC5 |
| 25 | MEDIUM | M26 | 36 | §6 AC1 |
| 73 | LOW | L1 | 32 | §2 S7; §8 F3 |
| 21 | LOW | L2 | 34 | §6 AC12 |
| 27 | LOW | L3 | 36 | §2 S3 |
| 28 | LOW | L4 | PLAY | §2 S2 and S4 |
| 47 | LOW | L5 | DEPL | §9; §3 Edges |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number, so "unit 34" is `2026-09-14-spec-TOOL-dDerivedDocket-34.md`. "PLAY" and
"DEPL" are `2026-09-14-spec-PLAY-dDerivedDocket-1.md` and `2026-09-14-spec-DEPL-dDerivedDocket-1.md`.

## Blockers

All three are in unit 34. Two are G2's, found again from the consumer side because no fold has
landed yet; the third is new.

### B1 — the switch-over neither files the triage ask nor gives the engine a policy for a hold naming no id (13, 31)

**Where.** Unit 34 §2 S1, §3 Edges (consumes-from 11 and 12), §4 Rollout and §6 AC2. Read against
unit 11 §2 S7, §4 Inventory's `TRIAGE-ASK` row and §10 (`…-11.md:55-60`, `:181`, `:330-335`), unit 12
§2 S4 and §4 "Classification" (`…-12.md:36`, `:137`), and unit 35 §2 S9. This is the unit-34 end of
G2's B1 and B2.

**Defect.** Unit 11 S7 previews every legacy hold that names no full id as a hold on "the one triage
ask the switch-over files, written as the placeholder `TRIAGE-ASK`". A hold whose target is neither a
census id nor a spec H1, such as a shorthand `-4`, counts as naming none. Unit 11 §10 measured five
of the seven legacy BLOCKED and DEFERRED rows at BASE naming no full id. It says the policy "is a
line the M2 interface cross-read must see in the switch-over spec". Unit 34 carries no such line,
and neither `TRIAGE-ASK` nor "triage ask" appears in it. S1 makes `--write` a thin driver over unit
12's engine. That engine classifies "a hold naming no id" as NEEDS-HUMAN, and its S4 then writes
nothing while any NEEDS-HUMAN entry stands. The engine exposes two policies, disposition home and
provenance, and neither covers the case.

**Impact.** As specified, `--write` refuses gov's whole corpus on those five rows, so the switch-over
commit cannot be made. A builder who works around it has two options, and both red a criterion.

- Writing a literal `TRIAGE-ASK` makes V6 red, so AC1's `--check` fails.
- Filing a real triage ask puts the ask-row count at census plus one, so AC2 fails.

AC3's per-id comparison fails on each of the five holds either way, because the prediction names
`TRIAGE-ASK` and the switched tree names something else.

**Fix.** Fold with G2's B1 and B2, once, across units 11, 12 and 34.

- Unit 12 gains the third policy G2 prescribed: NEEDS-HUMAN for the straggler verbs, and a hold on a
  supplied triage-ask id under `--write`.
- Unit 34 gains an S-item and a rollout step before `--write`. The orchestrator mints the triage
  ask's id, the writer files it in `memory/builds/dDerivedDocket/BACKLOG.md`, and `--write` receives
  it as that policy's value.
- AC2 counts the census's distinct ids plus the filed triage ask. AC3 compares against the status
  worksheet with the minted id substituted for `TRIAGE-ASK`.
- State how the triage ask stands at this build's close. Unit 35 S9 requires every ask homed in this
  build's folder to be terminal or disposed there, while the five holds need their target live.
  Name the ask in unit 35 S9's read.

**Left-shift.** A unit 34 observation that `gen_build_index.py --asks <minted id>` prints the ask,
and that `grep -c TRIAGE-ASK memory/builds/*/BACKLOG.md` prints 0. G2's class item 1b, a backticked
token one spec assigns to a named sibling must occur in that sibling, has its second live hit here.
Class item 3 below.

### B2 — the landing reconcile names no verb whose direction and confirmation fit it (14, 32, 58)

**Where.** Unit 34 §4 "The landing reconcile" step 2, §8 F5 and §6 AC15. Read against unit 12 §2 S1,
S5 and S6, its §3 Non-goals ("The switch-over's own landing reconcile is unit 34's decision (its §8
F5), not this unit's", `…-12.md:77-78`), and its §4 "Classification" (`:141-146`, `:155`). This is
the unit-34 end of G2's B3.

**Defect.** Step 2 runs "the delta engine over the tip's shard delta from the merge-base" during the
in-place merge of the shards-mode tip into the builds-mode branch. It writes "each status flip as a
disposition carrying `by <sha>`". It names no verb, and none of unit 12's fits.

- `--relocate` takes HEAD as the straggler side while MERGE_HEAD exists. Here HEAD is the
  post-switch branch, so the delta runs the wrong way, and unit 12's AC9 exits 2 when the other
  side's conf is in shards mode, as the tip's is.
- `--ingest <ref>` has the right direction, but it is specified as "no merge made". Unit 12 S5 also
  refuses every status-changing record without `--confirm <id>`, and every flip main made during the
  build is one. Unit 34 never says whether the reconcile passes `--confirm`, or under what rule.
- `--repair` needs a committed merge sha.

A disposition planned for a target the `--as` file already disposes is NEEDS-HUMAN too. AC15 names no
verb either. Its classes are "new, flipped, already present or needing a human", with no CONFIRM
class. It asserts no classified count and seeds no text amendment.

**Impact.** The landing merge parks whenever main's shards moved since the fork. At the rate measured
for B3, 64 new OPEN ids in the seven days to BASE, a build that spans a day meets that. Parking is F5's
option (a), the outcome option (b) was chosen to avoid, and it defeats the owner's "so the switch-over
lands in this run". Over a tip whose shards did not move, AC15 passes vacuously, and its Red-when, a
text amendment classified as a flip, cannot occur.

**Fix.** Fold with G2's B3. Choose one route and write it into unit 34 §4 step 2 and into unit 12's
hands-off to 34: a unit 12 mode for an in-progress merge whose MERGE_HEAD is the shards side, or
`--ingest <tip> --as dDerivedDocket` run before the merge. State the confirmation rule for the tip's
flips, for example every entry whose change commit is on the tip's history, and how it squares with
design A6 and lab case e09b. That rule takes a §9 line. Make AC15 run exactly that verb with
`--dry-run` over a scratch tip carrying one new row, one flip and one text amendment. It asserts a
non-zero classified count, CONFIRM or its replacement on the flip, and NEEDS-HUMAN on the amendment.

**Left-shift.** The landing-shape fixture in class item 1 below, run to completion rather than only
classified.

### B3 — step 3 re-runs a signer that has no input at the merged tree and no writer (34)

**Where.** Unit 34 §4 "The landing reconcile" step 3, and §3 Edges (consumes-from 33, "the signer the
landing reconcile re-runs"). Read against unit 33 (`2026-09-14-spec-TOOL-dDerivedDocket-33.md`) §3
Non-goals and Edges and §4 "Data model" Inputs, unit 11 §2 S2, and unit 34's own S6.

**Defect.** Step 3 re-runs the signer "over the triage population recomputed at the merged tree, so
an ask the tip added on a finished build is disposed under the same rules". The signer's input is
unit 11's triage worksheet. `--plan` builds that worksheet by reading the live shards and the family
backlog archives with the legacy parser. At the merged tree the shards are generated views, whose
rows are link-wrapped table rows in unit 7's grammar, and S6 has deleted the archives. So nothing
produces the input. The signer writes "No `BACKLOG.md` row, view or disposition" by its own non-goal,
and step 3 names no writer for the dispositions it would sign. Unit 33's hands-off promises the
re-run, and neither spec says how it happens.

**Impact.** A tip-added ask that derives OPEN on a finished build gets no disposition, and V10, a gate
from the switch-over by ruling D6, reds the landing bar. Measured for this report at `abac6d59`: 64
ids that appear in none of the shards, archives, build folders or `memory/DECISIONS.md` on
2026-09-06 (at `e55f933b`) are OPEN rows in `memory/backlog/*.md` at BASE. 61 of them carry slugs whose build folder exists and is absent from
`memory/LIVE.md`, so every unit of that build is terminal. 38 of the 64 came from one build,
`aHoistedPass`, and without it the ratio is 23 of 26. Sessions file asks at their own wrap-up, as
their build closes. The population step 3 serves is therefore non-empty on the routine landing, and
the build parks there, which is the outcome the owner's delegation exists to avoid.

**Fix.** A decision between two routes, recorded in unit 34 §9.

- Build the path. Derive V10's population from `gen_build_index.py --asks --all --json` at the
  merged tree. Have unit 33's signer accept that projection as an alternative input under the same
  rules. Name the writer that appends the signed dispositions to
  `memory/builds/dDerivedDocket/BACKLOG.md`, either a `--write` reconcile mode or the engine's `--as`
  policy. Both specs change.
- Or park. State in §4 that step 3 parks when the population is non-empty, and accept that the
  switch-over then lands by an owner turn on the case measured above.

Either way, AC15's rehearsal prints the size of that population at the current tip.

**Left-shift.** The landing-shape fixture in class item 1 carries one tip-added ask homed on a
finished build, and asserts that `gen_build_index.py --check` exits 0 after the reconcile.

## High

H1 sits in the same reconcile as B2 and B3. H2 to H5 are unit 32's, H6 is unit 35's, and H7 and H8
are unit 33's. Two were weighed for BLOCKER and put here. H1's recommended fold applies unit 34's own
S4 rule and needs no new mechanism. H2's first route is a workflow step inside unit 32.

### H1 — the reconcile never moves ASK_CUTOFF, so every ask main files in the window reds the landing bar (33)

**Where.** Unit 34 §2 S4, §4 "ASK_CUTOFF — derived, not the flip date" and §4 "The landing reconcile"
steps 2 to 4. Read against unit 12 §3 (`…-12.md:79-81`) and its `filed` rule (`:141`), unit 6 §4 V9 and
V12 (`…-6.md:201`, `:204`), and unit 15 §2 S4 (V14).

**Defect.** The writer fixes `ASK_CUTOFF` at the switch-over commit as the first date after every
`filed` date it wrote. The reconcile later writes the rows main gained during the build, and unit 12
sets each new ask's `filed` to the author day of its oldest lineage commit. Unit 12 §3 says an ask
first seen on or after the cutoff "is written and listed, and the generator's own verdicts then name
what it owes", and it invents no severity, `accept` or `seen`. V9, V12 and V14 grade every ask filed
on or after the cutoff. Steps 2 to 4 add none of what they owe, and never re-derive the cutoff.

**Impact.** Every row main files on or after the switch-over date reds the landing's one bar: V12 for
no SEV row, V14 for no `accept` or `seen`, V9 for a same-id row without `unit`. Those rows also lose
check 13's pre-cutoff skip. At the rate B3 measured, a build that lands a day after its switch-over
meets this on the routine case.

**Fix.** Add a reconcile step, after step 2, that re-derives `ASK_CUTOFF` over every `filed` date
written, the ingested rows included, and commits it with the merge. That moves the forward-only
start to the landing, which is when the switch-over reaches main. It also widens the ungraded window
F2 accepted from one day to the build's span, so record that in §9. AC15's rehearsal prints the
cutoff it would write. The alternative, an exemption for reconciled rows that units 6 and 15 honour,
is a mechanism no spec carries.

**Left-shift.** The landing-shape fixture's tip-added ask carries a `filed` date after the branch's
cutoff, and the fixture asserts no V9, V12 or V14 after the reconcile.

### H2 — the render leg bakes the primary-tree path, so the bar job is red on every push (50)

**Where.** Unit 32 (`2026-09-14-spec-TOOL-dDerivedDocket-32.md`) §4 "Why one file, and why
windows-latest", and §2 S3. Read against `tools/playbook/render_playbook.py:164-178`
(`derive_primary_tree`, `derive_worktree_root`) and `:405-419`,
`tools/govkit/entries/playbook.kit.toml:130-139`, and `AGENTS.md:157`.

**Defect.** The unguarded `playbook render wiring` leg runs `adopt-playbook.sh --target . --check`,
which byte-compares `AGENTS.md`'s region with a fresh render. `PRIMARY_TREE_A` and `WORKTREE_ROOT_A`
are class `derived`, filled by `derive_primary_tree`: the parent of `--git-common-dir`. An answer in
`deploy.toml` is consulted only when the probe returns nothing (`:405-419`), so no answer can override
a path the probe does find. The region carries `C:/projects/coding-governance` at `AGENTS.md:157`,
which every node shares. `actions/checkout` clones under the runner's workspace, never at that path.
§4's case for `windows-latest` was that every recorded green was earned there, and every one of them
was also earned at that path.

**Impact.** The render differs, the leg prints DRIFT, and `GATE_FULL=1` reds on every push. The
per-sha verdict D12-i12 asks for is permanently red for a host reason, and a verdict that is always
red reads as noise. No pre-landing observation runs the bar outside a node's primary tree, so the
first live run after landing is where this first shows.

**Fix.** Choose one route.

- (a) A workflow step that clones the checkout to `C:/projects/coding-governance` and runs the bar
  there. `actions/checkout`'s `path` cannot leave the workspace, so this is a plain `git clone` step.
  It must carry H3's `origin/HEAD` fix as well.
- (b) Make the two probes answer-overridable in the renderer. That is the playbook kit's surface and
  a separate unit.

Before landing, run the unguarded legs once from a clone at a second path, and record the result in
the journal.

**Left-shift.** Class item 2 below: the documented pre-landing run of every job's command in a clone
shaped like the runner's.

### H3 — `actions/checkout` sets no `origin/HEAD`, so the drift audit returns 2 on every push (51)

**Where.** Unit 32 §2 S1 and S3; §4 "Why one file, and why windows-latest". Read against
`tools/drift-audit/drift_report.py:1858-1873` and the `drift-audit records` row of
`tools/gate-legs.json`, which is unguarded and runs `drift_report.py --check`.

**Defect.** `drift_report.py` takes its base ref from `--base-ref`, then `GOV_DEFAULT_BRANCH`, then
`git symbolic-ref refs/remotes/origin/HEAD`, and returns 2 when none resolves. The leg passes no
`--base-ref`, and `run-gates.sh` exports no `GOV_DEFAULT_BRANCH`. `git clone` sets `origin/HEAD`,
which is why every node passes. `actions/checkout` fetches by refspec and never runs `remote
set-head`. The workflow sets neither the variable nor the symref.

**Impact.** `drift-audit records` returns 2 and the bar job reds on every push, independently of H2.

**Fix.** Add `git remote set-head origin main` after every checkout, which repairs every reader of
that symref at once, or set `GOV_DEFAULT_BRANCH: main` in the workflow's env. Observe before landing:
`drift_report.py --check` in a clone after `git remote set-head origin --delete`, recorded in the
journal.

**Left-shift.** Class item 2.

### H4 — the held-run matrix grades 7 of 62 suites, and its criterion compares the derivation with itself (1, 48)

**Where.** Unit 32 §2 S4; §4 "The three triggers and what each publishes"; §6 AC5; §8 F3. Read
against `tools/run-gates/selftest-budgets.txt` (the column header, and its 62 rows) and
`tools/run-gates/run-selftests.sh:229-268`.

**Defect.** S4 derives the matrix directories "from the argv column of
`tools/run-gates/selftest-budgets.txt`". Measured at BASE, 55 of the 62 rows leave that column blank
("empty = take it from tools/gate-legs.json"), and the seven filled rows are all under
`tools/unattended/`. So the literal derivation yields one directory. Derived from the resolved argv
instead, the directories do not partition the population. `--kit` is a substring filter (`if filt
and filt not in argv`, `run-selftests.sh:266`), and 15 resolved suites have the bare dirname
`tools`, so `--kit tools` selects nearly every suite and the other matrix jobs repeat theirs. AC5
checks that the derivation "prints every directory that the argv column names and no other", which
compares the derivation with itself, so its Red-when cannot fire.

**Impact.** Read literally, the scheduled run D12-i12 asks for grades the seven unattended suites and
silently drops 55, while F3 promises "the whole population" and AC5 stays green. Read through the
resolved argv, the `tools` job runs the whole population in one job, which is the overrun §4's split
exists to avoid, and suites run twice.

**Fix.** Derive the matrix from `run-selftests.sh --list`, which prints the resolved argv. Give the
runner a selector that partitions, an exact-directory or suite-name filter; that is a kit edit and
owes its version bump. Restate AC5: the union of the matrix selections equals the full `--list`
population by row name, with no overlap. Stage one entry dropped, and observe it red.

**Left-shift.** Class item 4: a derivation over a producer's output quotes that output, measured at
BASE.

### H5 — unit 32's AC3 shallow arm cannot be observed before the flip (2, 30, 53)

**Where.** Unit 32 §6 AC3; §4 "Liveness, in each job" and "Why the pre-landing checks are staged
breaks and not a gate"; §5 testing and error-state rows. Read against unit 9 §2 S7, §4 "The walk"
step 3, and §6 AC5 and AC6 (`…-9.md:50-54`, `:129`, `:232-242`), and
`tools/memory-tree/check-memory-hygiene.sh:1745-1749`.

**Defect.** AC3 expects a `git clone --depth 1` of the branch to make the hygiene script "exit 1 as a
DEAD PROBE". Unit 32 runs at order 32 and declares no edge to unit 34, so its branch is in shards
mode. Unit 9 S7 applies the shallow DEAD PROBE only "On a HEAD the SHELL's own conf read calls builds
mode". On a shards-mode HEAD check 25 prints its dormant line, and unit 9's AC5 has it exit 0 on that
account. The only shallow handling at BASE skips the §base arm with a stderr note rather than
reddening (`check-memory-hygiene.sh:1748`). Separately, no arm feeds the liveness step an output that
lacks check 25's line. In the shallow arm the engine's own exit dominates, so AC3's second Red-when,
a grep for the word `check` alone, is never staged.

**Impact.** AC3 reds a correct implementation at the unit's pass, or is recorded as something it did
not see, so unit 32 cannot close as written. The A9 property §4 says holds "by construction" in CI
holds only after the flip. Neither the full-history requirement nor the liveness grep is observed
failing before CI's first live run.

**Fix.** Observe the shallow case on a builds-mode tree, either unit 9's fixture or a scratch clone
of the post-switch commit. State in §4 that before the flip the audit prints the dormant line on
shallow and full clones alike. Add an arm that runs the liveness step over a captured hygiene output
with check 25's line removed, observed red. The other route is a consumes-from edge to unit 34, with
unit 32 run after the switch-over.

**Left-shift.** Class item 5: an AC naming a builds-mode behaviour names the mode of the tree it runs
in.

### H6 — unit 35 stages the straggler refusal where the branch guard and BASE's hooks answer first (39, 61, 70)

**Where.** Unit 35 (`2026-09-14-spec-TOOL-dDerivedDocket-35.md`) §2 S2, S6 and S7; §4 "What 'the
real tree' means here"; §6 AC5. Read against unit 13 §4 "Why a library beside the hooks, and what it
may read", BASE's `.githooks/pre-commit:18-34`, and G2's H2.

**Defect.** S2 builds one scratch clone and points its `core.hooksPath` at "its own `.githooks`". S6
commits on a branch forked from BASE in that clone. Git resolves the hooks path against the working
tree running the hook, and the clone has one working tree. Checking the branch out therefore puts
BASE's `.githooks/` in place. BASE has no straggler guard, and its branch guard refuses any
primary-tree commit off the default branch, printing no recipe. Unit 13 §4 says the guard reaches a
pre-switch branch only because an absolute hooks path makes a LINKED worktree run the primary tree's
post-switch hooks. Unit 35 builds neither the linked worktree nor the absolute path, and AC5's
Red-when names only an unset hooks path.

**Impact.** AC5's `--relocate` line never appears. S6 records the branch guard's refusal instead, and
from a linked worktree under the relative value there is no refusal at all. The one real-content
observation of unit 13's layer cannot be made as written.

**Fix.** Reproduce the topology unit 13 relies on. Keep the scratch clone's primary tree on its
default branch. Create the pre-switch branch in a linked worktree (`git worktree add <dir> -b
<branch> abac6d59`) and commit there. Set the hooks path to the value `tools/check-wiring.sh` writes
after G2's H2 fold, not a hand-set one, so the RED proves gov's configuration rather than the
fixture's. Add to AC5's Red-when: the straggler is checked out in the primary scratch tree, so the
branch guard or BASE's hooks answer.

**Left-shift.** Class item 5. Unit 35 should build its topology with the fixture helper unit 13's
suite uses, so the two cannot drift.

### H7 — unit 33's AC3 requires U2 to decide four pairs that U1 decides first (8)

**Where.** Unit 33 §6 AC3; §4 "The same-id rules". Read against `memory/backlog/TOOL.md:47`, `:96`,
`:140` and `:201` at BASE.

**Defect.** §4 evaluates U1 to U4 "in order; the first rule a pair FAILS decides `not-unit`". AC3
requires the four design-named collisions to read `not-unit` "under rule U2". Measured for this
report, all four rows read OPEN at BASE, and none ever read SPECCED or INPROGRESS in history. None of
the commits that added them (`a55398be`, `82e6dcfb`, `a87773d9`, `5d643ca8`) added the same-id spec;
`82e6dcfb` only modified the `aSealedCaravan` spec. Their evidence class is `none`, so U1 decides
each one.

**Impact.** AC3 reds a correct implementation. On the real worksheet U2 can never be the deciding
rule, so AC3's Red-when, the U2 set arriving empty, cannot be observed either. The denial the design
names is never exercised.

**Fix.** Evaluate U2 before U1, so a design-named collision is always named U2 whatever its evidence.
That is also the conservative order, since the design's denial should dominate evidence. The other
route keeps the order and observes U2 on a synthetic worksheet row that gives one of the four ids
`specced-in-place` evidence.

**Left-shift.** Class item 4: an AC naming the deciding rule for real rows quotes those rows'
evidence, measured at BASE.

### H8 — unit 33's AC10 expects a diff the record shape makes impossible (12)

**Where.** Unit 33 §6 AC10; §4 "Data model", Outputs and header; §2 S6 and S8.

**Defect.** AC10 expects the diff after one synthetic worksheet row to be "that one added row plus
the liveness counts". The header states "each worksheet's path and git blob sha", and both differ for
a modified copy, so the header changes too. Rows lead with a row number (S6) and no row order is
specified, so a synthetic row that sorts anywhere but last renumbers every later row.

**Impact.** AC10 reds a correct implementation, or passes only for a synthetic row that sorts last,
which cannot expose the population-dependent verdict its Red-when names. S8's promise that a re-run
"changes only the rows whose evidence moved" fails on the numbering cell, and unit 34's reconcile
relies on that promise.

**Fix.** Specify the row order, for example by ask id. Replace the row number with a stable non-id
lead cell, such as the verdict or the rule id. The anchor grammar reads only an id in the first cell,
so either keeps S6's property. State that AC10's expected diff includes the header's worksheet path
and sha lines.

**Left-shift.** Class item 4: an AC stating an expected diff is checked against every field the
record derives from its inputs.

## Medium

The first sixteen entries are contradictions between specs, design holes, or declarations a spec
owes. The last ten are criterion gaps.

### M1 — the signed records' header cells are unpinned, and nothing runs `--plan --signed` over them (11, 36, 55)

**Where.** Unit 33 §4 "Data model", Outputs. Read against unit 11 §4 "The worksheets" and §8 F4, and
unit 34 §6 AC3. This is G2's M5 from the other side.

**Defect.** Unit 11 locates the signed records' columns by the exact header cells `Ask`, `Verdict`
and, on the triage record, `Field`, and refuses a record that lacks one. Its F4 says the cross-read
"pins `Ask`, `Verdict` and `Field` in both specs". Unit 33 names its columns in prose only ("ask id",
"verdict", "the `by`/`on`/`until` field"), and no AC runs the planner's `--signed` over its output.

**Impact.** A signer built from unit 33 as written can emit headers `--plan --signed` refuses. Unit
34's AC3 and rollout step 7 then have no prediction to compare with, and `--write` reads the same
records. The mismatch first shows at the flip. It is bounded, because the records re-derive by
re-running the script.

**Fix.** Pin the header row of both records in unit 33 §4, carrying `Ask`, `Verdict` and `Field`. Add
an AC: `python tools/memory-tree/migrate_backlog.py --plan --signed <both records>` exits 0 and
reports both applied. Fold once with G2's M5.

**Left-shift.** Class item 3: the signer's output fixture and the planner's `--signed` input fixture
are one file.

### M2 — the triage dispositions' home has no engine policy and no criterion (15, 37)

**Where.** Unit 34 §2 S1; §6, where no criterion places them. Read against unit 33 §2 S10 and §8 F4,
and unit 12 §4 "The engine".

**Defect.** S1 writes the migration's step-6 dispositions in the ask owner's folder, and the signed
triage dispositions in this build's `BACKLOG.md`, as unit 33's F4 decided. It says AC1 to AC3 observe
that. Unit 33 S10 defers its own observation here. None of the three sees where a triage disposition
lands. AC1 checks freshness and a count, AC2 counts ask rows, and AC3 compares derived statuses, which
are the same in any file because the closeout accepts any file. AC11 covers only
`TOOL-aWeighedCompass-3`, which T1 excludes from the triage. Unit 12's engine exposes one
disposition-home policy, "the ask owner's folder under `--write`", while S1 needs two.

**Impact.** An implementer following unit 12's interface writes the triage dispositions, about 288 by
unit 11's count at BASE, into foreign owner folders. That is the one-writer breach F4 rejected, and
every criterion stays green.

**Fix.** Make the engine's disposition-home policy per record class, as part of B1's fold to unit 12:
migration rows go to the owner's folder, and signed triage rows to this build's. Add a unit 34 AC:
every row of the signed triage record is decided by a disposition in
`memory/builds/dDerivedDocket/BACKLOG.md`, read from `--asks --all --json`, and none sits in an
owner's folder.

**Left-shift.** Class item 6: an S-item naming two destinations carries one observation per
destination.

### M3 — the writer's refusals are unstaged, and "stale" is defined by a script adopters do not have (16)

**Where.** Unit 34 §5 error states; §2 S1; §4 Rollout step 4. Read against unit 33 §4 Inventory, and
DEPL's proposed step 4.

**Defect.** §5 lists three refusals: an unsigned or stale signed record, an id with no single chosen
copy, and an unparseable row. No AC stages any of them, and AC2 catches a dropped row only through the
count. "Stale" is defined as "the signer's `--check` fails". The signer is a build-folder script that
"ships nowhere", and charter §12 bars a kit file from naming it by literal. Rollout step 4 runs that
`--check` as a separate operator step, so §5 puts the check on the wrong actor. DEPL's step 4 sends
adopters to `--write`, and they have no signer.

**Impact.** In gov, `--write` can apply a stale signed record with nothing observing it. In an
adopter's repo, staleness has no definition at all.

**Fix.** Have `--write` compare the signed records' header worksheet blob shas with the current
worksheets and refuse on a mismatch. That is kit-local and needs no signer. Add an AC that stages a
stale record, a duplicate live copy and an unparseable row, each observed to write nothing and exit
non-zero.

**Left-shift.** Class item 6: a §5 refusal list carries one staged arm per refusal.

### M4 — the drift re-point regresses every shards-mode adopter (60)

**Where.** Unit 34 §2 S10; §4 "The three drift signals added" and "Files touched". Read against
`tools/drift-audit/drift_report.py:1332-1340` (`build_live_backlog_rows`), and unit 7 S12 and §4.

**Defect.** S10 re-points the shipped `live_backlog_rows_per_shard` signal, which reads the authored
shards at BASE, at `gen_build_index.py --asks --json`. Under `shards` that command prints the mode
notice and an empty set (unit 7 S12). The three new signals assert "asks examined > 0" in every mode,
while unit 7 §4 counts zero examined as a DEAD PROBE only "while a `BACKLOG.md` is tracked". The
drift-audit kit version moves here, so adopters receive the change, and they stay in shards mode by
this unit's own non-goal.

**Impact.** Every shards-mode adopter loses the live-rows measurement it has today, and prints four
DEAD PROBE lines on every run. They are report-only, so `--check` stays green, which is how the
regression goes unnoticed.

**Fix.** Keep the shard read when the JSON `mode` field says `shards`. Make the three new signals
report not-asked under shards, or when no `BACKLOG.md` is tracked, with `gateable: False` as
`signal_closed_specs_untraceable` does. Add an arm on a shards-mode fixture.

**Left-shift.** Class item 5: a kit change the switch-over lands carries a shards-mode observation,
because shards is what every adopter runs.

### M5 — the risks row calls the zero-transition window a dead-probe state (35)

**Where.** Unit 34 §5 risks. Read against unit 9 §2 S7, §4 and §8 F2, and unit 36 §6 AC6. G2's M6
flagged the same line from unit 9's side.

**Defect.** The row says zero transitions between the switch-over and the landing merge is check 25's
"designed dead-probe state on a builds-mode tree". Unit 9's F2 removed N=0 as a DEAD PROBE for exactly
that window, because it would red an honest flip branch, and replaced it with S7's mode-boundary
predicate. Unit 36's AC6, which runs in that window, requires the hygiene script to pass.

**Impact.** The switch-over's implementer may treat a check 25 red in that window as expected, and
miss a real DEAD PROBE such as the two conf readers disagreeing.

**Fix.** Rewrite the row: in that window check 25 prints `transitions examined 0` and passes, because
the switch-over commit is a mode boundary, and any DEAD PROBE there is a real fault. Fold with G2's
M6, which also makes the landing merge's transition status conditional.

**Left-shift.** Class item 1: the landing-shape fixture pins what check 25 prints on each side of the
landing.

### M6 — nothing writes the DECISIONS row that supersedes DEPL-dGaugedVintage-13's stance (69)

**Where.** Unit 34 §2 S10; §4 "Files touched". Read against design §4.4 and
`tools/drift-audit/drift_report.py:1583-1597`. This is G2's M9 from the other side.

**Defect.** S10 retires `backlog_rows_outliving_closed_specs` and its pin. The signal's docstring
carries DEPL-dGaugedVintage-13's stance: "COUNTED, NEVER REFUSED", because "a row's ask can be
legitimately WIDER than the unit". Design §4.4 says "A DECISIONS row records that supersession", and
the design's critique table marks that fix accepted. No spec in the set writes the row or cites the
id.

**Impact.** A recorded stance is superseded without the new id and note that charter §6 requires. A
later reader finds the signal gone and its reasoning unanswered.

**Fix.** One `memory/DECISIONS.md` row naming DEPL-dGaugedVintage-13 as superseded and citing design
§4.4, keyed by whichever unit G2's M9 fold assigns: unit 6, which builds the replacing model, or unit
34, which deletes the signal. Fold once with G2's M9.

**Left-shift.** G2's documented check: every "a DECISIONS row records …" sentence in the design maps
to exactly one spec S-item.

### M7 — adding `yml::dark` to LANGS without re-stamping `ratified` reds the drift audit (52, 65)

**Where.** Unit 32 §2 S6; §6 AC6; §7 Gates. Read against `.lexicon.conf:170-190`,
`tools/drift-audit/drift_report.py:1044-1082`, and `tools/drift-audit/drift_signals.py:305`.

**Defect.** `signal_lexicon_ratified_stale` compares `ratified="2026-09-05 node a"` with the commit
date of the last `-G LANGS=` change to `.lexicon.conf`, dark declarations included, and the signal
is gateable with a pin of 0. S6 adds `yml::dark` to `LANGS` and does not re-stamp. `.lexicon.conf`
records two re-stamps made in the same commit for this reason, one of them for a dark-only `tsv`
addition, and TOOL-dUnstalledConvoy-35, which would let a dark edit pass, is still open. §7 omits
`drift-audit records`, and AC6 runs only the lexicon and govkit checks.

**Impact.** From unit 32's commit on, the unguarded `drift-audit records` leg reds on the landing bar,
and on CI's own bar job after it, while the unit's observations stay green. It is MEDIUM rather than
high because the landing bar runs the leg and the fold is one dated line.

**Fix.** Re-stamp `ratified=` in the same commit, with a dated comment saying it covers only a dark
`yml` declaration, as the TOOL-dUnstalledConvoy-26 precedent does. Add `drift-audit records` to §7,
and an AC that runs `python tools/drift-audit/drift_report.py --check` after the edit.

**Left-shift.** Class item 7: a spec whose §2 edits `LANGS=` lists the re-stamp.

### M8 — unit 36's kit version bump edits a watched file with no manifest re-stamp (38)

**Where.** Unit 36 (`2026-09-14-spec-TOOL-dDerivedDocket-36.md`) §2 S7; §4 "Files touched"; §7 Gates;
§3. Read against `tools/memory-tree/check-memory-hygiene.sh:20` and the `watch:` line of
`memory/guides/SESSION-KICKOFF.md`.

**Defect.** S7 places the memory-tree kit's one bump in this unit. `KIT_MEMORY_TREE_VERSION` lives at
`check-memory-hygiene.sh:20`, a file the kickoff manifest watches. Unit 36's Files touched lists
neither that file nor the manifest, §7 omits `kickoff-manifest ratchet`, and §3 leaves the manifest to
the switch-over. Units 34, 35 and PLAY each plan the re-stamp for their own watched edits.

**Impact.** `manifest-check.sh --staged`, wired in `.githooks/pre-commit`, refuses the unit's commit.

**Fix.** Add `check-memory-hygiene.sh` and the manifest re-stamp, with its delta line, to S7 and to
Files touched. Add `kickoff-manifest ratchet` to §7, and an AC mirroring unit 35's AC9.

**Left-shift.** Class item 7: a join refusing a spec whose Files touched or S-items name a watched
file without naming the manifest.

### M9 — the unattended suite's sweep bound exceeds the hosted job limit (49, 67)

**Where.** Unit 32 §4 "The three triggers and what each publishes", the `--sweep` and split
paragraphs; §2 S4. Read against `tools/run-gates/selftest-budgets.txt:49` and `:115`, and
`tools/run-gates/run-selftests.sh:419-490`.

**Defect.** §4 compares the 13600 s budget with the 360-minute job limit, and says a suite slower than
its hang bound "is published as killed". `--sweep` bounds each suite at its budget times
`sweep-ceiling-factor: 2`, so `unattended gate selftest` is bounded at 27200 s, and the runner exits 2
on any `SELFTEST_WALL` below the largest bound. 27200 s exceeds the 21600 s a hosted job may run. The
spec sets no `timeout-minutes` for the held jobs.

**Impact.** On a runner slower than node `a`'s recorded 9067 s, the platform cancels the
`tools/unattended` job before the sweep can name a killed suite, and the artifact is partial or
missing. S3's wall-below-timeout discipline cannot be applied to this job at all.

**Fix.** State the bound correctly and choose a route. Either give that suite a CI-declared budget or
factor whose bound sits under `timeout-minutes`, or accept a platform kill explicitly with an
`if: always()` upload. Add an AC comparing each held job's derived per-suite bound with its
`timeout-minutes`.

**Left-shift.** Class item 2.

### M10 — AC4 bounds GATE_WALL from above only (3)

**Where.** Unit 32 §6 AC4; §2 S3 and S5. Read against `tools/run-gates/gate-profiles.txt:66-73`, and
the `unattended kit gate` row of `tools/gate-legs.json` (ceiling 16040, subject `repo`).

**Defect.** AC4 checks that the wall is below the job's timeout. Nothing requires it to exceed the
largest ceiling among the legs `GATE_FULL=1` runs. `gate-profiles.txt` records that rule, "The wall
must exceed the LARGEST DECLARED CEILING", with an observed 2026-09-09 kill of a healthy bar at
10800. `unattended kit gate` is a repo-subject leg with ceiling 16040, so it runs under
`GATE_FULL=1`. AC4 stages no break, although S5 promises one per property, and its Red-when is the
criterion's own negation.

**Impact.** A wall of 3600 s under a 90-minute timeout passes AC4 and kills a healthy leg on every
push, so the per-sha verdict reds for a non-tree reason.

**Fix.** AC4 also asserts that `GATE_WALL` is at least the ceiling maximum that `run-gates.sh
--print-profile` reports (unit 27 S3), and that `timeout-minutes` is at most 360. Stage a wall below
that maximum, and one at or above the timeout, on the scratch copy, and record both reds.

**Left-shift.** Class item 2, and class item 6: a value bounded on both sides by its sources is
staged on both sides.

### M11 — the artifact uploads are never required to run after a failure (4)

**Where.** Unit 32 §2 S3 and S4; §5 observability; §6, where no criterion covers the uploads.

**Defect.** S3 uploads "the run record under the git dir", and S4 each held job's output, but the spec
never names the files. It never requires the upload step to run after a failed step either.
`actions/upload-artifact` runs under the default `success()` condition, and only warns when its path
matches nothing. AC4 and AC5 read the wall, the permissions and the directory derivation only.

**Impact.** On a red bar or a failed held suite, the only runs whose record matters, the upload is
skipped, and a wrong path publishes nothing, silently. §5's observability row claims artifacts that
may never exist.

**Fix.** Name the paths: `<git-dir>/gate-logs/`, `gate-last-failure.txt`, and the held run's captured
output. Require `if: always()` and `if-no-files-found: error` on every upload step. Add an AC checking
both on the scratch copy, with a staged break recorded in the journal.

**Left-shift.** Class item 2 and class item 6.

### M12 — the scratch landings meet the clone's pre-push hook (40)

**Where.** Unit 35 §2 S2 to S4; §4 Rollout steps 3 and 4. Read against BASE's
`.githooks/pre-push:155-160` and `:292`, and the build README's "Unit passes run no gates".

**Defect.** Rollout step 3 sets the clone's hooks path before step 4 lands the two scratch READMEs on
the scratch remote's default branch. That is a default-branch push. A raw one is refused for lack of
the `push-main-active` marker, and the refusal routes the operator to `push-main.sh`. There the
boundary forces the full bar, because the scratch git dir holds no recorded green. S4 says "no bar
runs in this unit", and the build README says unit passes run no gates. The spec names no bypass.

**Impact.** The landings S3 and S4 need are refused, or the whole bar runs in the scratch clone for
hours.

**Fix.** State in S2 that scratch landings push with `--no-verify`, or with `GOV_GATE_CMD=true`, or
land the READMEs before setting the hooks path. Record it in the ledger as a fixture-only bypass.

**Left-shift.** Class item 5.

### M13 — PLAY keeps the authorization sentence the design gave it to fix (42)

**Where.** PLAY §2, §3 and §10, none of which carries the item; §4 "Proposed text". Read against
design §19.8 (`…-design.md:1525-1527`), the design's U6 roster rows (`:55-57`), and
`coding-governance-agents.template.md:55` at BASE.

**Defect.** Design §19.8 says "U6 gains the charter sentence the contract reader found stale". The
sentence is "A committed build folder the run did not create", which is false for every prompt-mode
run: on the protocol's second anchor the run may author its own build folder. The design maps U6's
charter half to PLAY. D12-a dropped entry mode E2, not prompt mode. PLAY keeps the bullet
"(unchanged)" inside the very fence it edits, and its §9 and §10 departure lists do not record the
omission.

**Impact.** The charter keeps a false authorization sentence, and the design's scope for U6 is
narrowed silently.

**Fix.** Add a scope item rewording the sentence net-negatively inside the byte budget, for example
"a committed build folder the run did not create at the default-branch anchor". Or list the omission
in §3 or §10 with its reason. The same words sit in gov's authored Conventions bullet in `AGENTS.md`,
outside the region, and the fold should reach them too. That carrier was read for this report and was
not put to a skeptic.

**Left-shift.** Class item 4: each edit a design roster row names maps to an S-item or to a recorded
omission.

### M14 — the kickoff-manifest exception loses its only qualifier (71)

**Where.** PLAY §2 S2; §4 "Proposed text"; §10. Read against
`coding-governance-agents.template.md:63-68` at BASE, `tools/govkit/registry.toml:115-118`, and F2 of
`memory/builds/aScouredKit/reviews/2026-08-31-review-TOOL-aScouredKit-2-wave3-lens-behaviour.md`.

**Defect.** S2 deletes the italic "Two independent blocks…" paragraph, on the ground that it asks a
reader to do what the renderer now does. Its first sentence says the kickoff-manifest exception
"applies whenever the project keeps a kickoff manifest". That block has no fence, so the renderer
does nothing for it. `kickoff-manifest` is a registry entry, so an adopter's `kits` may omit it, and a
`kit:kickoff-manifest` fence is legal. The aScouredKit review's F2 prescribed both fences. PLAY builds
one of them and does not cite the finding.

**Impact.** An adopter without the kickoff-manifest kit receives "**Kickoff-manifest merge
exception.**" unconditionally, with the only qualifier deleted.

**Fix.** Wrap the exception in `<!-- kit:kickoff-manifest -->` fences. That costs about 63 template
bytes and keeps the edit net-negative against −107. Extend AC2 with a target that omits
`kickoff-manifest`, and cite the aScouredKit finding in §10.

**Left-shift.** Class item 7: a deletion justified as "the renderer does this now" names the fence
that does it.

### M15 — DEPL's step 3 names neither a command nor the signed-record format `--write` reads (29)

**Where.** DEPL §2 S2; §4 "Proposed text for §3a-asks" step 3; §6 AC3. Read against unit 11 §4, where
the header cells are, and unit 36 §2 S1.

**Defect.** S2 promises the switch as five ordered steps "by command". Step 3, sign both worksheets,
names no command and no format. It points at gov's own build folder, whose signer is a build-folder
script adopters do not have. `--write` and `--plan --signed` locate signed records by the pinned
header cells `Ask`, `Verdict` and `Field`. Unit 36's README section, to which DEPL's F5 defers the
grammar, lists no signed-record format. AC3 resolves only the flags a step names, so a step naming
none passes.

**Impact.** An adopter following the runbook cannot produce a signed record `--write` accepts. The
kit's input contract for `--write` is stated in neither adopter-facing home.

**Fix.** Step 3 names the signed-record shape (the header cells, the columns, and the worksheet path
and sha header), or points at a unit 36 README subsection that states it, which unit 36 S1 then
gains. AC3 also checks that each of the five steps names a command or that format. Fold after M1 pins
the cells.

**Left-shift.** Class item 3.

### M16 — DEPL's step 1 runs a `--plan` that writes nothing, and step 4 a `--write` with no signed input (41, 64)

**Where.** DEPL §4 "Proposed text for §3a-asks" steps 1 and 4; §6 AC3. Read against unit 11 §2 S1 and
S10 and §6 AC9, and unit 34 §2 S1.

**Defect.** Step 1 says a bare `migrate_backlog.py --plan` "files the id census, the same-id worksheet
and the triage worksheet as records of your build". Unit 11 makes a bare `--plan` write nothing unless
`--record <dir> --record-as <unit-id>` is given. Step 4 runs a bare `--write`, while unit 34 S1 makes
the two signed records its adjudication input and names no argument for them. AC3 checks only that
each named flag appears in `--help`.

**Impact.** An adopter reaches step 3 with no worksheets to sign, then runs a `--write` with no signed
input, and AC3 stays green over both. That is the stranded-at-a-command class AC3 was written for.

**Fix.** Spell step 1 as `--plan --record <build>/build --record-as <unit-id>`. Spell step 4 with the
signed-record arguments unit 34 must first pin in its S1. Extend AC3 to check each command's required
arguments against its usage line, or to run each under `--dry-run` on a fixture.

**Left-shift.** Class item 3: a runbook command is resolved by its full argument shape, not by flag
presence.

### M17 — S1's credential, autocrlf and runner properties have no criterion (5)

**Where.** Unit 32 §2 S1 and S5; §4 "Security"; §6 AC1, AC2 and AC7.

**Defect.** S1 lists `persist-credentials: false`, a `core.autocrlf false` step before each checkout,
and `windows-latest` under `shell: bash` for every job. Its observers AC1, AC2 and AC7 read only
`fetch-depth`, the action pins and the LF pin. S5's pre-landing contract lists neither the credential
property nor the autocrlf ordering.

**Impact.** §4's claim that the token "is not left in the clone's git config" rests on nothing
observed, and F1's runner decision is never checked in the file.

**Fix.** Extend AC1: the count of `persist-credentials: false` equals the count of checkout steps, an
autocrlf step precedes each checkout, and every job carries `runs-on: windows-latest` and
`shell: bash`. Stage one break per property on the scratch copy.

**Left-shift.** Class item 6: an S-item listing N properties carries N observations.

### M18 — AC8 cannot see the `ci_file` answer it names (6)

**Where.** Unit 32 §6 AC8; §2 S7. Read against `tools/playbook/render_playbook.py:404-419` and
`.governance/deploy.toml:34-36`.

**Defect.** The renderer consults an answer only when its probe returns nothing, and nothing refuses
an unused answer. With `remote-ci.yml` present, `derive_ci_file` returns its path, so
`adopt-playbook.sh --check` passes whether or not `.governance/deploy.toml` still carries `ci_file`.
AC8's observation cannot see its Red-when, "the `ci_file` answer is left in place".

**Impact.** S7's promise that a deleted workflow makes the render refuse is never observed, and a
left-over answer later revives "none yet" silently.

**Fix.** Add that `grep -c '^ci_file' .governance/deploy.toml` prints 0, and a scratch render with
`.github/workflows/` removed, observed to refuse naming `CI_FILE`.

**Left-shift.** Class item 6: a Red-when is staged, not argued.

### M19 — U3 and U4 have no criterion (9)

**Where.** Unit 33 §2 S2; §4 "The same-id rules"; §6.

**Defect.** AC3 checks the U2 set, and that `unit` rows cite U1 evidence. No AC exercises U3, a
low-overlap pair with in-place evidence signing `not-unit` (F3). None exercises U4 either, the named
spec existing at the signing tree with the ask id in its H1.

**Impact.** A low-overlap pair signed `unit`, or one naming a missing spec, passes AC1 to AC11. §4
calls that error, a wrong `unit` closing an ask nobody answered, the silent one. This is the first
criterion gap to fold, for that reason.

**Fix.** Run the signer over synthetic worksheet rows, as AC10 does for the triage. A
`specced-in-place` row with the low-overlap flag signs `not-unit` under U3. A row whose spec path is
missing, or whose H1 lacks the id, signs `not-unit` under U4.

**Left-shift.** Class item 6: a rule table with N rows carries N arms, each staged by deleting its row.

### M20 — AC8's check 13 cannot see a triage-record anchor (56)

**Where.** Unit 33 §6 AC8; §2 S6. Read against `tools/memory-tree/corpus_ids.py:622-627`,
`tools/memory-recall/extract.py:116-121`, and unit 8 S6.

**Defect.** AC8 relies on check 13, which counts an id anchored in two or more build folders and is,
in its own comment, deliberately not "defined twice". At unit 33's pass the asks are defined in `memory/backlog/*.md`,
which is not a build folder. After the switch-over, unit 8 S6 drops pre-cutoff `BACKLOG.md` ask rows
from the build-folder definitions. A triage row that leads with an ask id that has no same-id spec is
then the only build-folder claim, and check 13 says nothing.

**Impact.** AC8 passes even when the forbidden row-leads-with-id shape ships, so the anchor hazard it
names is never observed for the triage record.

**Fix.** Check the shape directly: run `extract.py`'s `anchor_at` over every line of both records and
require zero anchored ids.

**Left-shift.** Class item 6.

### M21 — AC4 has no upper bound on ASK_CUTOFF (17)

**Where.** Unit 34 §6 AC4; §2 S4.

**Defect.** S4 defines the cutoff as the FIRST date strictly after every `filed` date. AC4 accepts any
date later than every migrated `filed` date. No other spec bounds the value, and unit 35 stages no
new-ask V12 or V14 red on the real tree.

**Impact.** A writer printing a far-future cutoff passes AC4 and silently disarms V9, V12 and V14, the
forward-only verdicts of D7, D12-d and D12-g, for every new ask.

**Fix.** AC4 asserts that `ASK_CUTOFF` equals max(`filed`) plus one day, with max(`filed`) recomputed
from the written `BACKLOG.md` rows independently of the writer's printout. H1's fold changes the
formula at the reconcile, and this equality should follow it there.

**Left-shift.** Class item 6: a derived value is compared with an independent derivation, not bounded
on one side.

### M22 — AC14 cannot see a local-only walk (18)

**Where.** Unit 34 §6 AC14; §2 S14. Read against unit 12 S8.

**Defect.** AC14 observes a refs-examined count above zero. Unit 12's `--stragglers --local` narrows
to `refs/heads`, and it also prints a count above zero on any node with local branches. So the
observation cannot see its Red-when, "only local branches are walked".

**Impact.** A local-only inventory passes AC14, and a pushed straggler on another node reads as none.
Unit 12's AC6 guards the default walk on a fixture, which lowers the practical risk.

**Fix.** Compare the printed count with `git for-each-ref refs/heads refs/remotes | wc -l`, or assert
that at least one `refs/remotes/` ref appears in the examined set.

**Left-shift.** Class item 6.

### M23 — AC10 never stages a zero, and two S10 changes are unobserved (19)

**Where.** Unit 34 §2 S10; §6 AC10. Read against `tools/drift-audit/drift_report.py:1324` and
`:1332-1373`.

**Defect.** AC10 observes exit 0, the absence of the retired signal's line, and examined counts above
zero for the three new signals on the real tree. It never stages the zero case, so a signal with no
liveness assertion passes. Two other S10 changes have no observation: the live-rows signal re-pointed
at `--asks --json` with its watermark re-measured, and `_TERMINAL_STATUSES` reading the derived
output. `build_live_backlog_rows` is `gateable: False`, so if it is never re-pointed it silently
counts view rows after the switch while `--check` exits 0.

**Impact.** AC10's Red-when, a reassuring zero turned into a DEAD PROBE, is never observed. Charter §7
says a new gate is not landed until its failing case has been observed.

**Fix.** Stage each new signal over a scratch projection that lacks its field, and observe the DEAD
PROBE. Add an AC that the live-rows reading equals the live-ask count from `gen_build_index.py --asks
--json`. M4's shards-mode arm belongs beside these.

**Left-shift.** Class item 6.

### M24 — AC9's Red-when cannot happen (59)

**Where.** Unit 34 §6 AC9; §2 S9. Read against `tools/memory-recall/extract.py:129-131`, `:145-148`
and `:674`, and `.memory-tree.conf:545`.

**Defect.** AC9 assumes the durable-home pattern feeds the recall floor. `DURABLE` selects only the
`spine` set (`extract.py:674`), and the kit's own comment says "no gate and no merge-bar floor reads
this". The pinned floor grades `records` (`RECALL_FLOOR="records:fts5:r@5>=0.81"`), and
`corpus_files()` already takes every `.md` under the memory root.

**Impact.** Leaving the pattern unwidened cannot drop the floor, so AC9 cannot detect the regression
its Red-when names, and S9's durable-pattern change goes unobserved.

**Fix.** Split AC9. Grade the `records` floor before and after the switch. Observe the widening
separately, through the spine count or extract's durable-home figure rising by the migrated ids.

**Left-shift.** Class item 4: a Red-when naming a mechanism quotes the line that wires it.

### M25 — four of S4's five carriers are unobserved (24)

**Where.** Unit 36 §2 S4; §6 AC4 and AC5.

**Defect.** S4 names five carriers. AC4 greps only `tools/workflows/tier2-review.js`. AC5 runs the
parity test and two adopt `--check` commands, which compare each render with its template and pass
whether or not the template was edited. `drift-audit-state.js` has no render and no AC.

**Impact.** A pass that edits one carrier out of five passes every AC. Reviewers following the other
four keep reading a view of live asks only, and after the switch they miss every terminal ask and its
reason.

**Fix.** AC4 greps all five carriers for `--asks --json` and the mode-fallback sentence. For each BASE
phrase it finds the phrase only inside that sentence: `tier2-review.js:315`,
`drift-audit-state.js:198`, `tools/drift-audit/SKILL.template.md:109`,
`tools/workflows/REVIEW-PROTOCOL.template.md:188` and `tools/memory-recall/SKILL.template.md:91`.

**Left-shift.** Class item 6: an S-item naming N files carries a criterion reading each.

### M26 — AC1 runs modes that need arguments, and never resolves `migrate_backlog.py`'s verbs (25)

**Where.** Unit 36 §6 AC1; §4 "The README section", the print-modes and stragglers rows. Read against
unit 15 S6, S7 and AC9, unit 16's `--asks` contract, and DEPL's AC3.

**Defect.** AC1 runs each named print mode as a bare `gen_build_index.py <mode>`. But `--build`, `--at`
and `--ready` take arguments and are sub-options of `--asks`, and `--probe` refuses under the blank
`PROBE_ALLOW` unit 35 keeps. The stragglers row names `--stragglers`, `--relocate`, `--ingest`,
`--repair` and `--recipe` of `migrate_backlog.py`, and AC1 resolves none of them. Its Red-when covers
generator flags only.

**Impact.** AC1 reds a correct README or is waved through. A misspelled verb passes in the README
that DEPL sends adopters to.

**Fix.** Resolve every flag the section names against each tool's `--help`, as DEPL's AC3 does. Run
only the argument-free print modes, and state the arguments for the rest.

**Left-shift.** Class item 3.

## Low

### L1 — the unattended runner's header stays false once the schedule runs (73)

**Where.** Unit 32 §2 S7; §8 F3. Read against `tools/unattended/run-unattended-gates.sh:2` and
`:24-26`.

**Defect.** F3 puts the unattended suites on the daily schedule. S7 corrects "nothing runs these
automatically" only in `run-selftests.sh`. `run-unattended-gates.sh` says its self-tests are "run on
demand and nowhere else", and that "nothing runs the self-tests automatically". Unit 1 S8 counts this
statement's carriers as three: `kit.toml` and both runner headers.

**Impact.** A shipped kit header is false in gov from the schedule's first run.

**Fix.** Extend S7 to the unattended runner's header, with the unattended kit version bump that edit
owes, or narrow F3 to exclude the unattended suites.

**Left-shift.** Class item 7: a behaviour change names every carrier of the sentence it falsifies.

### L2 — AC12 observes one of the four manifest claims S12 updates (21)

**Where.** Unit 34 §6 AC12; §4 "What the one commit carries", the manifest row.

**Defect.** The manifest row updates four claims: the rotation-union trap at `SESSION-KICKOFF.md:200`,
the check-8 trap at `:251`, the pointer-map rows at `:114-117`, and the governing-docs line at `:67`.
AC12 greps only for the first.

**Impact.** The re-stamp can assert re-verification of three claims left stale, which is the class
AC12's own Red-when names.

**Fix.** AC12 greps `memory/guides/SESSION-KICKOFF.md` for each of the four BASE strings and expects
none.

**Left-shift.** Class item 6.

### L3 — three S3 claims in the kit README have no criterion (27)

**Where.** Unit 36 §2 S3; §6 AC3. Read against `tools/memory-tree/README.md:205` and
`memory/guides/BUILD-METHOD.md`.

**Defect.** AC3 checks the file table and the three attribute lines. Three S3 claims go unobserved:
the README's M6 clause-3 section agreeing with the BUILD-METHOD render, the upgrade note, and the
sentence on why the backlog attribute stays. No gate compares the kit README with BUILD-METHOD.

**Impact.** The kit README can disagree with BUILD-METHOD on M6 with every AC green.

**Fix.** Grep for the upgrade note and the keep-the-line sentence, and compare the README's M6
clause-3 text with the rendered clause.

**Left-shift.** Class item 6.

### L4 — PLAY's heading-note deletion and layout-line edit are unobserved (28)

**Where.** PLAY §2 S2 and S4; §4 "Byte accounting"; §6 AC1 to AC3 and AC6.

**Defect.** Without the −93 heading-note deletion the file still shrinks (+89 −186 +49 +34 = −14), so
AC1 passes. AC2 and AC3 pass too, because the note sits inside the new fence. S4 moves
`backlog/<FAMILY>.md` into `AGENTS.md`'s GENERATED list, and AC6 checks only the node-registry
paragraph.

**Impact.** A stale drop instruction survives in every kit-selecting render, and gov's layout line
can keep listing the views as authored.

**Fix.** Add that `grep -c 'kit-conditional — drop this block' coding-governance-agents.template.md`
prints 0, and a grep that the layout line lists `backlog/<FAMILY>.md` among the GENERATED members.

**Left-shift.** Class item 6.

### L5 — DEPL's §9 says no producer end is written, and hides the one that is missing (47)

**Where.** DEPL §9 rev-1; §3 Edges. Read against unit 9 §3 Edges (`…-9.md:96-104`).

**Defect.** §9 says the producer ends of its seven added edges "are not written". Units 10, 11, 12, 13,
34 and 36 and PLAY each carry a hands-off to DEPL. Only unit 9 lacks one, for the `commit-msg` edge,
and the brief requires both ends.

**Impact.** The false sentence hides the one missing end. DEPL is Tier-1, so the hygiene join does not
grade it.

**Fix.** Add hands-off DEPL-dDerivedDocket-1 to unit 9's Edges, and correct DEPL's §9 to name unit 9
as the only unreciprocated producer.

**Left-shift.** Class item 7: a reciprocity check over this build's own edge table, Tier-1 specs
included, kept as a documented check until the join grades Tier-1.

## Left-shift, by class

1. **The landing reconcile runs only at the landing** (B2, B3, H1, M5). All four live in unit 34's
   four reconcile steps, which run outside any unit pass and after the closing review. AC15 rehearses
   classification only, "writes nothing", and names no verb. The left-shift is one fixture, owned by
   unit 34 or unit 12. It holds a builds-mode HEAD and a shards-mode tip that carries three changes:
   one new ask homed on a finished build and filed after the branch's cutoff, one flip, and one text
   amendment. Run the reconcile to completion in the scratch repo, then assert four things.
   `gen_build_index.py --check` exits 0, with no V9, V10, V12 or V14. The flip is written or confirmed
   under the stated rule. The amendment parks with the recipe. Check 25 reads the merge accounted.
   Stage RED by skipping each step in turn.
2. **The CI runner is not a node** (H2, H3, M9, M10, M11). Every recorded green was earned in a clone
   at the primary-tree path, with `origin/HEAD` set by `git clone`, on a machine with no job limit.
   S5's staged breaks cover the workflow file's text, never the environment it creates. The
   documented pre-landing check has two parts. First, run every job's command in a clone shaped like
   the runner's: a `git clone` at a second path, `git remote set-head origin --delete`, and no local
   config. Second, compare each derived bound, the bar's wall and each sweep bound, against the job's
   `timeout-minutes`. H2 and H3 each show on the first part.
3. **An interface two specs share, spelled in only one** (B1, M1, M15, M16, M26). `TRIAGE-ASK`, the
   signed records' header cells, the signed-record input of `--write`, `--plan`'s record flags, and
   `migrate_backlog.py`'s verb spellings. G2 proposed the join: a backticked token one spec assigns
   to a named sibling must occur in that sibling. `TRIAGE-ASK` is its second live hit. This group
   adds one extension: a runbook or README command is resolved by its full argument shape against
   the producer's usage line, not by flag presence.
4. **A real producer's output assumed instead of run** (H4, H7, H8, M13, M24). The budget file's
   argv column, the four rows' history evidence, the record header's derived fields, the design's
   roster, and the recall floor's document set. G4's class item 2 stands: a spec relying on an output
   shape quotes that output, measured at BASE, beside the command that produced it.
5. **An observation staged in a tree that lacks the property** (H5, H6, M4, M12). The documented
   check: every AC names the mode, the worktree topology and the hooks of the tree it runs in. A unit
   ordered before 34 names no builds-mode-only verdict without a fixture, and a kit change landed by
   the switch-over carries a shards-mode observation.
6. **An S-item whose Observed-by criteria survive its deletion** (M2, M3, M10, M11, M17 to M23, M25,
   L2 to L4, and half of H4). This is the fifth group in a row where it leads. G1 to G4's proposal
   stands: beside each S-item's "Observed by", write the mutation that deletes it and the AC that
   reds on it. The G5 form: an S-item listing N properties, carriers, claims or destinations carries
   N observations. Here that is S1's four properties in unit 32, S4's five carriers in unit 36, S12's
   four claims and S1's two homes in unit 34.
7. **What an edit owes and does not carry** (M6, M7, M8, M14, L1, L5). The DECISIONS supersession
   row, the lexicon re-stamp, the manifest re-stamp, a fence for a qualifier being deleted, a second
   carrier of a falsified sentence, and a reciprocal edge. A `tools/check-spec-tokens.py` join can
   refuse a spec whose Files touched names a watched file without the manifest, or whose §2 edits
   `LANGS=` without `ratified`. Run it over this build first and print hits and near-misses before
   wiring it.

## Outside the confirmed set

One observation came out of re-checking the highs. It was not put to a skeptic, so it is not counted
above.

**Whether a `GATE_FULL=1` bar fits a hosted job at all is unmeasured.** Unit 32 §4 says a four-core
runner resolves to the `modest` row of `tools/run-gates/gate-profiles.txt`. That row declares
`wall=21600`, which equals the hosted job maximum, and `unattended kit gate` alone declares a 16040 s
ceiling. So M10's window for `GATE_WALL` is from 16040 s to just under 21600 s. No spec in the set
measures a `GATE_FULL=1` bar at width 4. If the bar cannot finish in that window on the runner,
D12-i12's per-sha verdict needs a narrower bar or a different runner, and that is an owner question
rather than a fold.

## What this round did not cover

- Units outside G5 were read only where an edge or an interface named them. Nothing here clears units
  1 to 31. B1 and M2 land in unit 12, B1 in unit 11, B3 in unit 33, M6 in unit 6 or 34, and L5 in
  unit 9. Each fold must land in both specs at once.
- Six entries overlap other groups' round-1 entries, and the group folds must agree.
  - B1 with G2's B1 and B2.
  - B2 with G2's B3.
  - M1 with G2's M5.
  - M5 with G2's M6.
  - M6 with G2's M9.
  - H6 depends on the route G2's H2 fold takes.
  G3 also recorded, outside its confirmed set, that unit 35's S4 RED passes for the wrong reason while
  G3's H1 or H2 stands. That note is unaffected by this report.
- Re-measured for this report, at `abac6d59`:
  - the budget file's argv column and the resolved directories, the substring filter, and the sweep
    factor and wall refusal (H4, M9);
  - the renderer's probe precedence and the placeholder class (H2), and the drift report's base-ref
    ladder (H3);
  - the lexicon signal, its stamp and its pin (M7), and the wall rule and the largest ceiling (M10);
  - the four U2 rows and the commits that added them (H7);
  - BASE's branch guard and pre-push marker (H6, M12), and the watched kit constant (M8);
  - unit 9's S7, AC5 and AC6, and BASE's shallow arm (H5);
  - the recall pattern and floor (M24), the drift reader and the superseded docstring (M4, M6), and
    the unattended runner's header (L1);
  - the aScouredKit finding (M14) and the producer ends of DEPL's edges (L5);
  - the new OPEN ids on main in the seven days to BASE and the status of their home builds (B2, B3,
    H1).
- Not re-derived: the GitHub platform facts that H2, H3, M9 and M11 rest on. Those are the hosted job
  limit, `actions/checkout`'s workspace path and missing `origin/HEAD`, and `upload-artifact`'s
  default step condition. They are the finders' and skeptics' statements, not measured here, because
  no workflow run can be made before landing. The first live run after landing is their first
  observation, and class item 2's pre-landing check is the substitute.
- This round raised three questions and did not answer them.
  - After B2's fold, does the reconcile run before the merge, ingesting the tip into the branch, or
    during it? The answer decides whether step 1, "take the branch's side of every conflicted view",
    survives.
  - Does a `GATE_FULL=1` bar finish inside a hosted job at width 4? See "Outside the confirmed set".
  - Which route G2's H2 fold takes decides what configuration unit 35 stages in H6.
- The 19 refuted findings are not reproduced here. They were refuted, not lost, as the run-integrity
  counters show.
