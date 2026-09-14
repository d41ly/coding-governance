**Serves:** spec-audit TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14

# dDerivedDocket — spec audit of topic group G2, the derived backlog core, round 1

*Node `d`, 2026-09-14. A Tier-2 adversarial pass over the nine specs of topic group G2: the ask
parser and status fold (unit 6), the generated family view (7), the hygiene engine in builds mode
(8), the transition-merge audit (9), the row driver's shard-into-view refusal (10), the migration
planner (11), the relocation tools (12), the straggler hook bodies and inventory (13), and the
retired rotation-note check (14). Four primed finder lenses ran, then a skeptic stage prompted to
REFUTE each finding in five batches, then this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
and the spec brief's roster and edge tables. Sibling specs outside G2 were read wherever an edge or
an interface named them, units 33 and 34 most of all, because contradiction between specs is in
scope. Every blocker and every high below was re-checked against source at `abac6d59` before it was
written down here, and the sites read are named in each entry. H2's premise was also re-measured, in
a scratch repository and against node `d`'s live configuration.*

**Round: 1.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-6.md@3963d3cdb0182dff1b579ac689da11418c346759`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-7.md@af475d58021ad414a6bc00d58cd5fe2c32aeb1d5`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-8.md@ba84e869ef92deff5523b309aee8a3c7426ec057`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-9.md@589df56f3ab75acdd6f7b882bbbce66a733bbbfa`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-10.md@02c8043379e0cb45962bd3a747d2f0410c3cbebd`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-11.md@fcabedc7fc34e89cbc999f55a075eb903ffc7e57`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-12.md@f8850211d16b67a55e30793ee48bbf59598bdec8`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-13.md@02298b80b515252a992760be3d89c68b55a6e820`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-14.md@21e8bb60a9500012046a75bb79cdc8859cbcf975`

## Verdict: BLOCKED

Three blockers stand, carried by five confirmed findings, and all three sit at the seam where the
planner (unit 11), the relocation engine (unit 12) and the switch-over (unit 34) meet. The owner
delegated the D2 and D6 signatures "so the switch-over lands in this run", and as specified it
cannot. B1: the engine has no policy for a legacy hold that names no id, so `--write` refuses gov's
own corpus (2 and 41 are one defect). B2: nobody mints, files or substitutes the one triage ask those
holds are meant to wait on (23 and 43 are one defect). B3: the landing reconcile names no verb whose
semantics fit it, so the flip parks at its own landing (42). B1 and B2 share a root. Unit 11 §10
deferred the step-6 policy to "the M2 interface cross-read", and the cross-read never carried it into
unit 34.

Four confirmed findings are HIGH, which is three defects. Unit 9 hands off two interfaces that no
scope item carries (H1, from 1 and 48). Unit 13's layer rests on a hooksPath premise that this repo's
own wiring falsifies, re-measured here (H2). Unit 7's data-loss guard has no defined reach, and units
10 and 34 need opposite answers from it (H3).

Every blocker and high is a defect in a document this round read, so the disposition
`memory/guides/BUILD-METHOD.md` M4 prescribes is FOLD for all of them. Two folds change a ratified
design point and should be decided rather than folded silently. The first is B3, whose confirmation
rule for the tip's flips either restates or relaxes design amendment A6, the lab case e09b
protection. The second is H2, which diverges from design §18.1's measured premise. Each takes a §9
line. The folded text is unreviewed surface (`memory/gotchas/fold-text-is-unreviewed-surface.md`), so
round 2 re-reviews the fold. Unit 12's engine and classification table, unit 34's S1 and landing
reconcile, unit 11's S7 and hands-off, and unit 9's new scope items need that re-review most.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

Every counter that could make this run incomplete is zero, so the finding set is complete for what
the four lenses were primed to hunt. That is not a claim that G2 holds no other defect. It is a claim
that nothing was lost between the lenses and this page. The pipeline's duplicate count of 0 comes
from its own exact-match dedupe. On reading, six pairs of confirmed findings each describe one defect
from two lenses: 2/41, 23/43, 1/48, 12/47, 27/44 and 60/75. Each pair is folded into one entry below,
and every count on this page stays per finding id.

## Review shape

Raw 82, confirmed 47, refuted 35, unverified 0, precision 0.57. The 47 confirmed ids collapse to 41
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 5 | 3 |
| HIGH | 4 | 3 |
| MEDIUM | 31 | 28 |
| LOW | 7 | 7 |

**Severity is adjudicated here, not copied from the finders.**

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written, or it ships a layer that stays inert
  while its suite reads green, and the fold is local to one or two specs.
- MEDIUM covers three things: a contradiction between specs with a bounded consequence, a
  declaration whose absence reds a leg at the post-build bar, and a rule whose break no criterion can
  see.
- LOW is the same kinds of defect where the reachable harm is small.

Against the finders' ratings, 2, 41, 42 and 43 move from high to BLOCKER. 23 moves from medium to
BLOCKER, because it is B2 together with 43, and 48 moves from medium to HIGH, because it is H1
together with 1. No finding moved down.

Precision at 0.57 sits just above the ~0.5 floor that `AGENTS.md` section 8 sets. The dominant class
is the one G1 named, `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`: an
acceptance criterion that cannot see its own S-item break. Ids 5, 10, 15, 17 to 22, 24 to 26, 28 to 34
and 36 to 38 are that class outright, which is 22 of the 47, and ids 7 and 27 each have it as one
half. G1's report asked the remaining groups to prime their lenses with the gotcha's skip test. That
priming is how these were found, but the count also shows the class survives spec authoring (class
item 2 below). The second cluster is six findings: 57, 58, 60, 74, 75 and 76. In each, a new moving
part owes a declaration that its spec's Files touched and Gates never name. Each one reds a leg at
the one post-build bar, and no unit-pass observation runs that leg. Unit 14, retired at WONTDO,
drew no confirmed finding.

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 2 | BLOCKER | B1 | 12 | §4 The engine; §4 Classification; §3 Edges |
| 41 | BLOCKER | B1 | 12 | §4 The engine and Classification, against unit 11 S7 and unit 34 S1 |
| 23 | BLOCKER | B2 | 11 | §2 S7; §3 Edges |
| 43 | BLOCKER | B2 | 11 | §2 S7; §3 Non-goals and Edges; §4 Inventory |
| 42 | BLOCKER | B3 | 12 | §2 S1, S5, S6; §3 Edges; against unit 34 §4 |
| 1 | HIGH | H1 | 9 | §3 Edges; §2 S4 to S7 |
| 48 | HIGH | H1 | 9 | §2 S6 against §3 Edges |
| 54 | HIGH | H2 | 13 | §4 Why a library beside the hooks; §2 S1 |
| 55 | HIGH | H3 | 7 | §2 S8; §3 Edges |
| 12 | MEDIUM | M1 | 7 | §2 S7 |
| 47 | MEDIUM | M1 | 6 | §2 S11 against §4 Verdicts; §3 Edges |
| 7 | MEDIUM | M2 | 6 | §2 S11 |
| 45 | MEDIUM | M3 | 7 | §2 S8, against unit 10 §4 |
| 56 | MEDIUM | M4 | 7 | §2 S11, S12; §4 The JSON projection |
| 27 | MEDIUM | M5 | 11 | §2 S8; §8 F4 |
| 44 | MEDIUM | M5 | 11 | §4 The worksheets; §8 F4 |
| 49 | MEDIUM | M6 | 9 | §3 Edges against §4 Liveness and §8 F2 |
| 50 | MEDIUM | M7 | 12 | §2 S1 against S5; §4 Confirmation |
| 76 | MEDIUM | M8 | 9 | §4 Data model; §2 S12 |
| 72 | MEDIUM | M9 | 6 | §3 Non-goals; §8 |
| 57 | MEDIUM | M10 | 11 | §2 S11; §4 Files touched; §7 |
| 58 | MEDIUM | M11 | 8 | §4 Files touched; §7 |
| 74 | MEDIUM | M12 | 10 | §2 S6; §4 Inventory and Files touched; §7 |
| 60 | MEDIUM | M13 | 13 | §2 S7 |
| 75 | MEDIUM | M13 | 13 | §2 S7, S8; §6 AC9 |
| 5 | MEDIUM | M14 | 6 | §2 S6; §4 The fold; §8 F2 |
| 10 | MEDIUM | M15 | 7 | §2 S4; §4 The view grammar |
| 15 | MEDIUM | M16 | 9 | §2 S1 |
| 17 | MEDIUM | M17 | 9 | §2 S7; §8 F2 |
| 18 | MEDIUM | M18 | 9 | §6 AC9 against §4 Liveness |
| 21 | MEDIUM | M19 | 10 | §2 S1; §4 The refusal |
| 22 | MEDIUM | M20 | 10 | §2 S5 |
| 24 | MEDIUM | M21 | 11 | §2 S3 |
| 25 | MEDIUM | M22 | 11 | §2 S6; §8 F2, F5 |
| 26 | MEDIUM | M23 | 11 | §2 S4 |
| 28 | MEDIUM | M24 | 11 | §5; §2 S2, S3 |
| 32 | MEDIUM | M25 | 12 | §2 S1 |
| 33 | MEDIUM | M26 | 12 | §2 S5; §8 F1 |
| 34 | MEDIUM | M27 | 12 | §4 Classification, the `filed` rule |
| 36 | MEDIUM | M28 | 13 | §4 default conf source; §5 |
| 19 | LOW | L1 | 9 | §2 S4 |
| 20 | LOW | L2 | 9 | §2 S12 |
| 29 | LOW | L3 | 11 | §2 S5; §6 AC11 |
| 30 | LOW | L4 | 11 | §2 S7 |
| 31 | LOW | L5 | 11 | §6 AC10 |
| 37 | LOW | L6 | 13 | §2 S1; §8 F4 |
| 38 | LOW | L7 | 13 | §2 S7 |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number.

## Blockers

### B1 — the engine has no policy for a hold that names no id, so `--write` refuses gov's corpus (2, 41)

**Where.** Unit 12 §4 "The engine", the paragraph giving the two policy parameters. Also unit 12 §4
"Classification": the row for "a hold naming no id" and the row for a flip to BLOCKED or DEFERRED
"naming an id". Also unit 12 §3 Edges, the hands-off to unit 34. These are read against unit 11 §2
S7 and §10, and against unit 34 §2 S1.

**Defect.** Unit 12 classifies a hold naming no id as NEEDS-HUMAN. S4 then writes nothing while any
NEEDS-HUMAN entry stands. The engine exposes exactly two policies, disposition home and provenance,
"so unit 34 can drive the same engine". Unit 34 S1 is that thin driver, and it writes "the
migration's own step-6 dispositions".

Unit 11 S7 follows design §9 step 6: "a BLOCKED or DEFERRED row that names an id as a hold on that
id; otherwise a hold on ONE triage ask the migrating session files once". So unit 11 previews every
such hold as a hold on the triage ask. It also counts a hold as naming none when its target is
neither a census id nor a spec H1, such as a shorthand `-4` or a decision id.

Unit 12's "naming an id" row has no such test. It writes `- BLOCKED · <id> · on <X>` verbatim, and
unit 6 V6 reds that. Unit 11 §10 measured five of the seven legacy BLOCKED and DEFERRED rows at BASE
naming no full id. It said the policy "is a line the M2 interface cross-read must see in the
switch-over spec", and unit 34 carries no such line. `--drop` offers no way out either: under
`--write` provenance is off, so a drop writes nothing and the hold is lost.

**Impact.** Over gov's own corpus, `--write` either refuses as a whole, or the builder invents an
unreviewed third policy whose statuses the planner did not predict. Either way, unit 34's S16 and
AC3 per-id status proof cannot pass, and the switch-over the owner delegated for cannot land as
specified. A relocated straggler hold that names a decision id lands as a V6 red.

**Fix.** Add a third engine policy for a hold naming no id: NEEDS-HUMAN for the three straggler
verbs, and a hold on a supplied triage-ask id under `--write`. Adopt unit 11 S7's test in the
classification table, so that "names an id" means a census id or a spec H1 at the target tree. Name
the policy and its `--write` value in unit 12's hands-off to 34 and in unit 34 S1. Give each policy
value a selftest AC.

**Left-shift.** Add arms to `migrate_backlog.py --selftest`: a DEFERRED row naming nothing and a
BLOCKED row naming an EXMP decision id, each run under both policy values. The straggler value
expects NEEDS-HUMAN and the `--write` value expects the triage hold. Stage them RED against the
two-policy engine. L4's planner arm should read the same fixture, so the planner and the engine
cannot drift on it. The class-level gate is item 1 of "Left-shift, by class".

### B2 — nobody mints, files or substitutes the one triage ask (23, 43)

**Where.** Unit 11 §2 S7. Also unit 11 §3 Non-goals: "Minting the triage ask's id. The orchestrator
mints it at the switch-over." Also unit 11 §4 Inventory, the `TRIAGE-ASK` row: "the switch-over
substitutes the minted id". Also unit 11 §3 Edges, the hands-off to unit 34. These are read against
unit 34 §2, §4 Rollout and §6.

**Defect.** Unit 11 writes the step-6 holds on the placeholder `TRIAGE-ASK`, because a planner never
mints. It assigns the switch-over two jobs: minting the triage ask's id, and substituting that id for
the placeholder. Design §9 step 6 also has the migrating session file the ask. Unit 11's hands-off to
34 names neither job. Unit 34 has no S-item, rollout step or AC that mints, files or substitutes a
triage ask. Neither `TRIAGE-ASK` nor "triage ask" appears in it.

**Impact.** At the flip, the step-6 holds have no target. Written verbatim, a hold on `TRIAGE-ASK` is
a V6 target, neither a filed ask nor a spec H1, and it renders `UNRESOLVED`. That fails unit 34 AC1,
which requires `--check` to exit 0. Dropped instead, the legacy BLOCKED and DEFERRED statuses are
lost, and unit 34 AC3's comparison against the planner's prediction ("held on `TRIAGE-ASK`") shows
each one as a differing id. Even with B1 folded, the engine's `--write` policy needs an id that
nobody supplies.

**Fix.** Add the placeholder substitution to unit 11's hands-off to 34. Give unit 34 an S-item and
an AC covering three steps before `--write`: file the one triage ask in this build's `BACKLOG.md`
under an id the orchestrator mints, pass that id as B1's policy value, and compare the per-id report
against the status worksheet with the id substituted for `TRIAGE-ASK`. Add the step to unit 34's
Rollout between steps 3 and 4.

**Left-shift.** A unit 34 observation that `gen_build_index.py --asks <the triage id>` prints the
ask, and that no switched status is decided by a hold on `TRIAGE-ASK`. Class item 1b below is the
mechanical join: a backticked token one spec assigns to a named sibling must occur in that sibling.
It is a live hit here.

### B3 — the landing reconcile has no verb, so the flip parks at its own landing (42)

**Where.** Unit 12 §2 S1, S5 and S6. Also unit 12 §3 Non-goals, where the reconcile "is unit 34's
decision (its §8 F5), not this unit's", and unit 12 §3 Edges, the hands-off to 34. These are read
against unit 34 §4 "The landing reconcile", §8 F5 and §6 AC15.

**Defect.** Unit 34's reconcile runs the delta engine during the in-place merge of the shards-mode
remote tip into the builds-mode run branch. It writes the tip's status flips as dispositions without
confirmation and parks only text amendments. Its F5 option (b) reads "ingest what classifies
mechanically". No unit 12 verb has that shape:

- `--relocate` takes HEAD as the straggler side while MERGE_HEAD exists, and the other side as
  MERGE_HEAD. Here HEAD is the builds side and MERGE_HEAD is the shards tip, and AC9 exits 2 when the
  other side's conf is in shards mode.
- `--ingest` is specified as "delta of `<ref>` against `HEAD`, no merge made". S5 makes every
  status-changing record wait for `--confirm <id>`, and that covers every tip flip step 2 means to
  write.

Unit 12 disowns the reconcile, and its hands-off to 34 names only `--write`'s policies,
`--stragglers` and `--dry-run`. AC15's classes, "new, flipped, already present or needing a human",
have no CONFIRM class.

**Impact.** The flip cannot land as unit 34 specifies. With `--relocate` the reconcile refuses. With
`--ingest` it stops on every flip main made since the fork. F5 option (b) was chosen so the
switch-over lands in this run, and it collapses into option (a), which parks. AC15's rehearsal runs
a path the real landing cannot take, so it cannot catch this. M6 compounds it: step 4 then confirms
a transition that may not exist.

**Fix.** There are two ways to fold it.

- Give unit 12 a mode for an in-progress merge whose MERGE_HEAD is the shards side. State its
  confirmation rule, and how that rule squares with lab case e09b, and hand the mode off to 34.
- Or rewrite unit 34 §4 to run `--ingest <tip>` before the merge, with explicit `--confirm`
  handling.

Either way, add CONFIRM to AC15's classes and name the verb in AC15's command. The confirmation rule
is a design A6 point, so the spec that states it takes a §9 line. It should be decided explicitly,
not folded silently.

**Left-shift.** A unit 12 selftest arm, or a unit 34 rehearsal fixture, that stages exactly the
landing shape: a builds-mode HEAD, and a shards-mode MERGE_HEAD carrying one flip and one new row.
It runs the named verb to completion. Stage it RED by pointing it at `--relocate`. The class is item
1a below: an edge line must name the S-item that carries it, and unit 12's hands-off to 34 has none
for the reconcile.

## High

### H1 — unit 9 hands off a no-merge delta and a named-tip audit that no scope item carries (1, 48)

**Where.** Unit 9 §3 Edges (the hands-off to 12 and 13), §2 S4 to S7, and §4 "The walk" step 1.
These are read against unit 12 §3 Edges and §9, and against unit 13 §2 S4, §4 "Resolving the audit
from a hook" and §6 AC5.

**Defect.** Every form unit 9 specifies is bound to HEAD or to a merge:

- S4 defines the delta over a transition merge's parents.
- S5 accounts against HEAD's tree.
- S6 runs full mode over "the history HEAD carries", and §4's walk starts at
  `git rev-list --parents HEAD`.
- S7's liveness cross-check reads HEAD's mode through the shell engine.
- S9's staged form covers only a pending merge.

The edges still promise more. To unit 12 they promise "the delta and the accounting predicate ...
which `--stragglers` reuses". To unit 13 they promise "the full-mode audit at a named tip".

Unit 12 §9 says its `--ingest`, `--from` and `--stragglers` need the delta "callable for a
straggler-side commit with no merge". `--stragglers` also accounts at the default tip, which need not
be HEAD. Unit 13 S4 runs the audit "over the pushed sha, not HEAD". Both consumers' non-goals forbid
spelling a second transition rule.

**Impact.** Units 12 and 13 have no promised entry point to build against. Each will add its own or
re-spell the delta, which is the second rule both specs forbid, and no transition-audit arm
exercises either form. Unit 13's pre-push feature-branch block (S4, AC5) has nothing to call. S7's
two-reader liveness check has no counterpart for a named tip.

**Fix.** Add a unit 9 S-item that exports `delta(ours, theirs)` with no merge commit. Add a
named-tip full mode, for example `transition_audit.py --at <sha>`, whose history walk and accounting
read that commit and whose liveness rule does not need the shell's reader. Give each form an AC in
`transition-audit.test.sh`. If that is not done, strike the promise from the edges and give the call
explicitly to 12 and 13.

**Left-shift.** Those two ACs, each staged RED by binding the form back to HEAD. The class is item
1a below.

### H2 — unit 13's layer rests on a hooksPath premise this repo's own wiring falsifies (54)

**Where.** Unit 13 §4 "Why a library beside the hooks, and what it may read", and §2 S1 to S4. The
premise is inherited from design §18.1, "verified 2026-09-13, node d".

**Defect.** §4 says `core.hooksPath` is repo-global and absolute, so every worktree runs the primary
tree's hook files, and it places the library there on that basis. The repo's own wiring writes the
relative form. `tools/check-wiring.sh:259` sets `core.hooksPath .githooks` whenever the key is
unset, and the headers of `.githooks/pre-commit` and `.githooks/pre-push` give the same instruction.
Git resolves a relative value against the worktree that runs the hook.

Re-measured for this report with git 2.54.0.windows.1 in a scratch repo: under `.githooks`, a linked
worktree ran its own `.githooks/pre-commit`, not the primary's. On node `d` today, the shared config
at `C:/projects/coding-governance/.git/config` holds `.githooks`. Seven of the nine live linked
worktrees carry an absolute `config.worktree` override, and two carry none: `derived-harness-paths`
and `muffled-sentinel`. Those two resolve to their own `.githooks/`. The branch in
`derived-harness-paths` is the one design §9 step 1 names as a known straggler. Unit 13's §10
re-verified line citations only.

**Impact.** In a worktree that resolves the relative value, a straggler runs its own pre-flip hook
files. Those carry no library, no `pre-rebase` and no feature-push block, so S2, S3 and S4 never fire
where they are needed. S5's session step runs from that worktree's own old `tools/check-wiring.sh`,
so it is inert there too. The fixture suite (AC1 to AC5) sets hooksPath explicitly and stays green.
The unit therefore ships a layer that instructs nobody while its suite reads green. It is HIGH, not
a blocker, because unit 9's audit still binds at the bar, and S6's drift signal, run from any
post-flip tree, still lists the straggler.

**Fix.** The finder's fix was to locate the library through `git rev-parse --git-common-dir`. That
does not reach this case. The hook file that runs in such a worktree is the straggler's own, and it
predates any line that sources a library, so no change to main's hook text arrives there. The lever
is the configuration. Choose one:

- (a) `tools/check-wiring.sh` writes an absolute path into the primary tree's `.githooks/`, and
  upgrades its own relative value wherever it finds it. That changes check-wiring's
  "never clobbers a set value" rule, and the change is recorded as such.
- (b) §5 records that the layer is inert in any worktree that resolves a relative value, and leaves
  the guarantee to unit 9. That is design §18r.5's position anyway.

Either way, unit 13 takes a §9 line diverging from design §18.1. It also corrects the same premise
where it touches the files: the `.githooks/pre-push` header (lines 6-9 at BASE), which is already in
its Files touched, and the comment at `tools/check-wiring.test.sh:811`.

**Left-shift.** An arm in `straggler-guard.test.sh` that runs each hook from a linked worktree with
no `config.worktree` override, under the value check-wiring actually writes, and asserts the chosen
behaviour. The class is item 4 below.

### H3 — the data-loss guard's reach is undefined, and two siblings need opposite answers (55)

**Where.** Unit 7 §2 S8 and §4 "The data-loss guard and its message", and unit 7 §3 Edges, which has
no edge to unit 34. These are read against unit 34 §4 Rollout steps 4 to 6 and unit 10 §5 risks.

**Defect.** S8 fires on content, "before overwriting a view": a line that leads with an id after a
list marker, or a conflict marker. It never says whether a file at a view path that carries no
generator header counts as a view. At unit 34's rollout step 6, `gen_build_index.py --write` runs
under builds mode while `memory/backlog/*.md` still holds the authored shards. No step in unit 34,
and nothing in its S1, removes them first. At BASE, `memory/backlog/TOOL.md` alone carries 460 lines
of the form `- TOOL-…`, measured for this report. Unit 10 §5, meanwhile, names this guard as the
backstop for an operator who resolves a view conflict by taking theirs, which leaves a headerless
shard at the view path. Unit 7 declares no edge to unit 34, although unit 34 S3, S10, AC1 and AC3 all
run through unit 7's modes.

**Impact.** If the guard reads every file at a view path, the flip's render exits 1 and all four
views stay unwritten. If it reads only files the §4 view predicate recognises, `--write` overwrites
the take-theirs shard that unit 10 relies on it to catch. The straggler's rows are then erased
silently, which is the class the guard exists to stop.

**Fix.** Define the guard over every file at a view path, whether or not it has a header. Give the
first builds-mode render an explicit path: either unit 34 removes the shards before step 6 and says
so, or `--write` takes a named one-time flag that the guard honours. Add the edge between units 7 and
34 in both specs.

**Left-shift.** A unit 7 selftest arm with a headerless authored shard at a view path, expecting the
guard to fire. Also a unit 34 rollout observation that step 6 runs over a tree holding no authored
shard at a view path. The class is item 1c below, and unit 34's missing edge to unit 7 is a live hit.

## Medium

The first thirteen entries are contradictions between specs or with BASE, or declarations a new
moving part owes. The last fifteen are gaps in what the acceptance criteria can observe.

### M1 — a blank `ASK_CUTOFF` under builds is a verdict nothing reports (12, 47)

**Where.** Unit 6 §2 S11, §4 Verdicts and §3 Edges (the hands-off to 7). Unit 7 §2 S7 and §6 AC4.
Unit 8 §2 S6 and §8 F2.

**Defect.** Unit 6 S11 and AC11 make a blank `ASK_CUTOFF` under builds "itself a verdict", returned
by the conf reader. It is absent from the §4 table of V1 to V12, and §4 says "the view unit reports
them". Unit 7 S7 and AC4 report "every fold verdict V1 to V12 and the three guards", and unit 7 never
mentions the cutoff. Unit 8 F2 then skips every ask row on a blank cutoff, because "the parser unit
already reports" it.

**Impact.** A builds tree with a blank cutoff runs with V9, V12 and V14 disarmed and check 13's
forward check skipped, and neither `--check` nor hygiene reds. That is exactly the silent disarm S11
exists to prevent: `memory/gotchas/degradation-known-but-unreported.md`.

**Fix.** Give the conf verdict a number in unit 6 §4, or name it in the hands-off to 7. Add it to
unit 7 S7's reported set, and add an AC: a builds-mode fixture with a blank `ASK_CUTOFF` makes
`--check` exit 1 naming the key. M2's malformed-value verdict joins the same row.

**Left-shift.** Class item 5 below.

### M2 — `ASK_CUTOFF` has no refusal for a value that is not a date (7)

**Where.** Unit 6 §2 S11 and §6 AC11.

**Defect.** S11 gives `BACKLOG_MODE` a refusal for any other value, but says only that `ASK_CUTOFF`
"is a date". AC11 stages a blank cutoff and nothing else. `filed` and the cutoff compare as strings,
so an unpadded `2026-9-30` sorts after `2026-10-01`. The blank-cutoff verdict S11 returns also has
no code (M1).

**Impact.** Against such a cutoff, October asks read as filed before it, so V9, V12, V14 and check
13's forward check go quiet on exactly the asks they exist for, with no message.

**Fix.** A cutoff that does not match §4's `DATE` grammar is a refusal naming the key. Give both conf
verdicts codes, and stage `2026-9-30` and a blank value in AC11.

**Left-shift.** That AC11 extension, staged RED by comparing the raw string.

### M3 — a view-against-view conflict is refused as if a straggler caused it (45)

**Where.** Unit 7 §2 S8, against unit 10 §4 "The refusal".

**Defect.** Unit 10 §4 says a merge in which both sides are views is "an ordinary view merge that
`--write` repairs". The row driver classes only `^\s*[-*]\s` lines as rows
(`tools/memory-tree/merge-rows.py:25`, `:252`). A view's table rows are therefore STRUCTURE, merged
positionally by `git merge-file`, and "a disputed structure line is always a conflict" (rule 4,
`:67-76`). So two post-flip branches that change the same or adjacent rows of one view leave conflict
markers in it. Unit 7 S8 reads any conflict marker as authored content. `--write` leaves the view
untouched, exits 1 and prints the straggler recipe.

**Impact.** An ordinary post-flip conflict on a generated view blocks the re-render the charter
prescribes for generated indexes. It also points the lander at `--relocate`, `--repair` and
`--ingest`, none of which applies when there is no straggler.

**Fix.** In unit 7 S8, distinguish a conflict region whose two sides both parse as view rows from
authored rows. For such a region, either re-render over it, or print "take either side, then
`--write`". Alternatively, have unit 10 resolve a view-against-view merge by taking ours for
re-render. Then make unit 10 §4's sentence match whichever is chosen, and add an AC.

**Left-shift.** A `merge-rows.test.sh` replay arm that merges two re-rendered views with adjacent row
changes, then runs `gen_build_index.py --write` and asserts exit 0 and a byte-correct view. M19 is
the neighbouring half.

### M4 — `--asks --json` does not own its stdout, and "always exit 0" cannot hold (56)

**Where.** Unit 7 §2 S11 and S12, and §4 "The JSON projection".

**Defect.** `--asks` needs `collect()` for the spec index and the build statuses (S1). At BASE,
`collect()` prints `build-index: N header(s) tolerated by waiver` to stdout unconditionally
(`tools/memory-tree/gen_build_index.py:822`, its ratified F2). It also raises on stale front matter,
an out-of-enum streams or roster value, or an underivable status, and `main()` turns any of those
into exit 1. S12 promises a JSON object on stdout and "always exit 0". S11 adds a liveness line "on
every run" and names no stream.

**Impact.** `--asks --json` stdout is prose followed by JSON, so every consumer gets a decode error:
unit 34's three new drift signals, its re-pointed live-rows signal, and its AC3 comparison. The
hygiene engine's ON STDERR note (`tools/memory-tree/check-memory-hygiene.sh:187-194`) records this
exact class, measured in this repo. The tool meant to explain a refusal also exits 1 on any tree
that `collect()` refuses.

**Fix.** Under `--asks`, stdout carries only the table or the JSON, and the tolerated-header line and
the liveness line go to stderr. Either report a `collect()` problem inside the JSON, or narrow the
exit-0 promise to fold verdicts. Add an arm that runs `json.loads` over the whole of stdout.

**Left-shift.** Class item 6 below.

### M5 — the signed-record interface between planner and signer is unpinned and half-observed (27, 44)

**Where.** Unit 11 §2 S8, §4 "The worksheets" (the header-cell paragraph), §6 AC6 and §8 F4, against
unit 33 §4 Outputs.

**Defect.** Unit 11 locates the signed records' columns by the header cells `Ask`, `Verdict` and
`Field`, and refuses a record missing any of them. F4 says "the M2 interface cross-read pins `Ask`,
`Verdict` and `Field` in both specs". Unit 33 §4 Outputs names its columns in prose only: "row
number, ask id, spec path, verdict …" and "the `by`/`on`/`until` field". None of its ACs observes a
header. Separately, unit 11 AC6 applies only the signed same-id record, and only reaches
`mirror-closed`. No criterion covers applying the triage record or its `Field` cell, or any other
status class.

**Impact.** A signer built from unit 33 as written, with headers such as `ask id` or `by/on/until`,
is refused by `--plan --signed`. Unit 34 S16 compares the switched tree against the prediction under
both signed tables. A planner that ignores or refuses the triage record therefore passes unit 11,
and each unit passes on its own fixtures, so the mismatch first shows at the flip.

**Fix.** Pin the three header cells in unit 33 §4 Outputs, and add a unit 33 AC that
`migrate_backlog.py --plan --signed` accepts both records it writes. Alternatively, correct unit 11
§4 and F4 to read unit 33's spelling. Extend unit 11 AC6 with two cases: a signed triage record
closing one ask predicts CLOSED with class `triaged`, and a triage record missing `Field` is refused.

**Left-shift.** Make the signer's output fixture and the planner's `--signed` input fixture one file,
so the two specs cannot drift on it. The class is item 1 below.

### M6 — unit 9 says two things about the landing merge, and unit 34 relies on the wrong one (49)

**Where.** Unit 9 §3 Edges (the hands-off to 34), against its own §4 "Liveness, the registry, and
the remedy" and §8 F2. Unit 34 §2 S15, §3 Edges (its consumes-from 9), §4 "The landing reconcile"
step 4, and §5 risks.

**Defect.** Unit 9's edge says "the flip's own landing merge is a transition this check audits". Its
§4 says the landing merge "is a transition only when one side's lineage carries a shards-mode backlog
commit, which nothing guarantees". Unit 34 follows the edge. S15 calls the landing merge "itself a
transition", and its consumes-from calls it "its first transition". Its §5 risk line calls zero
transitions on the flip branch check 25's "designed dead-probe state". That is the A3 predicate
unit 9 F2 replaced, so that an honest flip branch never reds.

**Impact.** When main's shards have not moved since the fork, the landing merge is not a transition,
and unit 34's step 4 ("confirm the transition audit reads the merge accounted") has nothing to
confirm. A green check 25 at that point can be misread as a broken probe, and a real red can be
dismissed as expected. This compounds B3.

**Fix.** Make unit 9's hands-off to 34 conditional: the landing merge is a transition whenever main's
backlog shards moved since the fork. Align unit 34 S15, its edge and its §5 risk line with unit 9's
S7 predicate.

**Left-shift.** M17's AC, a linear-flip fixture with no transition that exits 0 printing
`examined 0`, pins the behaviour unit 34 must describe. The class is item 1 below.

### M7 — `--relocate --from` is `--ingest` without its confirmation gate (50)

**Where.** Unit 12 §2 S1 (`--from <ref>`), against §2 S5 and §4 "Confirmation, and why it binds two
verbs of three".

**Defect.** §4 exempts `--relocate` from `--confirm` because it "is run by the author on a fresh
merge". But S1 lets it run with no merge at all: the straggler side is the ref and the other side is
HEAD. Nothing refuses that on a builds-mode default checkout, and S11's restore to HEAD's version is
then a no-op. The result is `--ingest` without S5's gate.

**Impact.** Anyone can write a straggler's CLOSED over a deliberate REOPEN on the default side by
running `--relocate --from <ref>`. That reopens lab case e09b, which AC3 closes for `--repair` only.
It is the sibling-write-path hole that charter §9 names.

**Fix.** Put the `--from` form under S5's confirmation rule, or restrict `--from` to a HEAD whose
lineage is the straggler's. Add an AC that stages e09b through `--relocate --from`.

**Left-shift.** That AC. At class level, add a table to §4 listing every verb and form that reaches
the writer and which guard each one passes, with one arm per row. M26 is the same gate's third
entry path.

### M8 — check 25 depends at runtime on a kit no descriptor says it needs (76)

**Where.** Unit 9 §4 Data model ("Delta entry") and §2 S12, against `tools/memory-tree/kit.toml:7-8`.

**Defect.** Under builds, check 25 keys delta rows through the memory-recall kit's `extract.anchor_at`.
It uses the lazy import from `tools/memory-tree/merge-rows.py:184-210`, which raises when that kit is
absent and records "THERE IS NO DEGRADED MODE". The memory-tree descriptor declares `requires = []`
and a single `requires_if` edge to memory-recall, which covers only `DEAD_PATH_PIN` and
`ORPHAN_ID_PIN`. It also states that other checks stay available "to an adopter who took memory-tree
alone". S12 adds no edge, and the spec gives no behaviour for an absent kit.

**Impact.** A memory-tree-only adopter that flips to builds mode runs the permanent L1 guarantee on
an unguarded leg with an undeclared dependency, so the check either raises or runs unkeyed. govkit
never selects memory-recall for that adopter. Nothing in this build reaches such an adopter yet,
which keeps this at MEDIUM.

**Fix.** Add a `requires_if` edge keyed on builds mode to S12, using a value condition if
`when_any_key_set` cannot express it. State check 25's named refusal when the recall kit is absent,
and arm it.

**Left-shift.** Class item 3 below: a runtime import of a sibling kit's module is a declaration the
spec owes.

### M9 — the DECISIONS row the design owes for a superseded stance is in no spec (72)

**Where.** Unit 6 §3 Non-goals and §8, where no such line exists, and unit 34 §2 S10.

**Defect.** Design §4.4 says "A DECISIONS row records that supersession", and design §12 marks
minimal critique F3 as accepted against "§4.4 DECISIONS row". The stance being superseded is the
drift signal's "COUNTED, NEVER REFUSED ... a row's ask can be legitimately WIDER than the unit"
(`tools/drift-audit/drift_report.py:1591-1594`), recorded under DEPL-dGaugedVintage-13. Unit 6 owns
design §§2-4 and builds `unit` and `advances`, the model that replaces that stance. Unit 34 S10
retires the signal and its pin. Neither writes the row, and no other spec in the set carries it.

**Impact.** A ratified decision is superseded without the new id and note that the charter requires
for the append-only log. A later reader finds the signal gone with no record of why.

**Fix.** Add a unit 6 scope item that writes one `memory/DECISIONS.md` row under unit 6's id, naming
DEPL-dGaugedVintage-13 as superseded. Alternatively, assign the row to unit 34 S10, with the
reciprocal edge noted in both specs.

**Left-shift.** A documented check for the fold: every "a DECISIONS row records …" sentence in the
design maps to exactly one spec S-item, listed in the brief's roster notes.

### M10 — unit 11's held leg has no budget row (57)

**Where.** Unit 11 §2 S11, §4 Files touched and §7 Gates.

**Defect.** S11 puts `backlog migration selftest` in chunk `selftests` with subject `kit`. The
unguarded every-bar leg "every held leg is budgeted, every budget row resolves"
(`tools/run-gates/run-selftests.sh --check`, whose forward loop is at `:325-343`) fails any such leg
that has no row in `tools/run-gates/selftest-budgets.txt`. Neither Files touched nor §7 names that
file or that leg, and the spec gives the new leg no `ceiling`.

**Impact.** The unit lands a leg that reds a declarations leg on every bar. The unit's own gate list
never runs that leg, so the red first appears at the post-build bar.

**Fix.** Add `tools/run-gates/selftest-budgets.txt` to Files touched, with a budget row and its
basis. Add the budget leg to §7, and state the new leg's `ceiling` in `tools/gate-legs.json`.

**Left-shift.** Class item 3 below.

### M11 — unit 8's edits unpin two position-keyed install-prefix waivers (58)

**Where.** Unit 8 §2 S6 and S7, §4 Files touched and §7 Gates.

**Defect.** `tools/install-prefix-waivers.txt` pins `tools/memory-tree/corpus_ids.py:935` and `:939`,
the check-15 selftest's wrong-prefix fixture lines. `tools/check-install-prefix.sh` matches waivers
by exact `<path>:<line>` and declares that registry frozen. S7 makes the `present` expression at
`:372` mode-dependent, and S6 adds a pre-cutoff skip near `:393`. Both sit above line 935, and the
new selftest arms may land there too. §7 omits `install-prefix (shipped surface)`.

**Impact.** Both waivers go stale, the shifted fixture lines become unwaived hits, and the
install-prefix leg reds on the bar. The unit's own gate list never shows it. The class is
`memory/gotchas/line-keyed-registry-reds-on-a-file-that-grew.md`.

**Fix.** Name the two rows in §4. In the same commit, either convert those fixture lines to in-line
`gov:root-fixture — <reason>` markers, which is allowed because the registry only shrinks, or keep
every added line below line 939. Add the leg to §7.

**Left-shift.** Class item 3c below.

### M12 — unit 10's new leg is declared by no descriptor (74)

**Where.** Unit 10 §2 S6, §4 Inventory and Files touched, and §7 Gates.

**Defect.** The codebase-map dossier is the only thing that claims `row-driver view refusal`. It has
no `[[gate_leg]]` in `tools/memory-tree/kit.toml` and no `[[exempt_leg]]` in
`tools/govkit/registry.toml`. govkit's selfcheck fails any leg "claimed by no descriptor and carried
by no [[exempt_leg]] — a new leg must red until a declaration says whether an adopter receives it"
(`tools/govkit/govkit.py:1642-1644`). §7 omits `govkit selfcheck`.

**Impact.** govkit selfcheck, an unguarded declarations leg, reds at the post-build bar. The choice
the spec leaves open also matters to adopters. Claimed as a repo-subject kit leg, it would ship to
every memory-tree adopter an assertion that `memory/backlog/*.md` resolves `merge=rows`. That
includes adopters whose driver is inert, and adopters whose attribute emission is still the
concurrent adopter-wiring work. The sibling leg `row-keyed merge driver replay` is an `[[exempt_leg]]`
(`registry.toml:475`).

**Fix.** Decide in §4 between a claim and an `[[exempt_leg]]`, with the reason. Add that file to
Files touched, and add `govkit selfcheck` to §7.

**Left-shift.** Class item 3a below.

### M13 — unit 13's suite and leg owe two govkit declarations, and the leg departs from its siblings (60, 75)

**Where.** Unit 13 §2 S7 and S8, §4 Files touched and §6 AC9.

**Defect.** S7 declares govkit exempt rows for the library and `pre-rebase` only. Two declarations
are missing:

- `.githooks/straggler-guard.test.sh` falls inside the registry surface `.githooks/**` and needs its
  own `[[exempt]]` row, because an exemption does not cover siblings. The precedent is
  `.githooks/pre-commit.test.sh` (`tools/govkit/registry.toml:266`).
- Its new leg needs an `[[exempt_leg]]` or a claim, as `branch-guard self-test` has
  (`registry.toml:294`). The map dossier's claim is not a govkit declaration.

The sibling hook suites, `branch-guard self-test` and `pre-push self-test`, sit in chunk `selftests`,
guarded on `.githooks/` and held under the 2026-08-23 and 2026-08-27 owner rulings. S8 puts this
suite unheld in `declarations`, with no reason beyond not being held.

**Impact.** govkit selfcheck reds twice at landing, although AC9 says it passes. A hook fixture suite
also joins every bar, unlike its siblings.

**Fix.** Add both declarations to S7 and AC9. Then either move the leg to chunk `selftests`, guarded
on `.githooks/` like its siblings, in which case M10's budget-row rule applies too, or record in §8
why this suite differs.

**Left-shift.** Class item 3d below.

### M14 — three fold behaviours have no criterion: release, `UNRESOLVED`, and a cycle's true tokens (5)

**Where.** Unit 6 §2 S6, §4 "The fold" (hold targets) and §8 F2.

**Defect.** S6 says a hold releases when its target goes terminal. §4 renders `UNRESOLVED` for a
target that names nothing. F2 rules that members of a hold cycle render their true token. AC4 stages
R5 and R6 only with a live target. AC5 covers WONTDO closing specs, AC7 permutes order, and AC10
stages V6 but checks only its code.

**Impact.** A fold whose holds never release passes AC4, AC7 and AC10, and so does one that renders
a cycle as undecidable. Asks then stay BLOCKED after their blocker closes. Unit 11's prediction and
unit 34 AC3 run the same fold, so neither can tell.

**Fix.** Extend AC4 with three cases. An ask BLOCKED on a target that folds CLOSED derives OPEN. A
hold on a nonexistent target renders `UNRESOLVED` beside V6. Two asks holding each other both derive
their true token, and V6 names the cycle.

**Left-shift.** Those arms, staged RED by dropping "has a live target" from R5.

### M15 — the view grammar's summary, sort and exclusion of terminal asks have no criterion (10)

**Where.** Unit 7 §2 S4 and §4 "The view grammar".

**Defect.** S4 promises the §4 grammar, but AC1 and AC2 observe only view count, empty families,
anchoring and list markers. Several parts of the grammar have no criterion:

- the summary rules: `|` to `/`, backticks stripped, links reduced, the cut at the last space plus
  `…`, and the 300-character budget;
- the slug-then-numeric sort;
- the absence of terminal asks. AC1's empty families hold no asks, and it asserts only that each
  live ask appears once.

**Impact.** A pipe in ask text splits the table row. A renderer that lists terminal asks falsifies
the header's claim that an unlisted id is terminal. Both pass the suite. The skeptic narrowed the
finder's impact on two points. Unit 8 S7 drops `backlog/` from check 15's corpus under builds, so a
backticked path in view text is not graded. And a lexical sort is still deterministic, so it would
put `-10` before `-2` against §4, but it would not reorder rows on every merge.

**Fix.** Add an AC over a fixture ask whose text carries a pipe, a backticked path, a link and 200
characters, alongside ids `-2` and `-10` and one terminal ask. Assert the row bytes, the order, and
that the terminal ask is absent.

**Left-shift.** That arm.

### M16 — no criterion observes the pinned dereference (15)

**Where.** Unit 9 §2 S1, and §5 security.

**Defect.** S1 cites AC1 and AC6 for `--no-replace-objects` with `GIT_GRAFT_FILE=/dev/null`. AC1 is a
plain merge, and AC6 stages a broken conf reader and a shallow clone. The pin is copied from
`tools/unattended/check-pass-order.sh:40-48` rather than sourced, so that precedent's tests do not
cover this module.

**Impact.** A git call missing the pin passes every AC. §5's claim that "a replace ref or a graft
cannot substitute history" is then unverified, on a check whose job is to find rows lost in history
that an agent can write refs into.

**Fix.** Add an AC: with an unaccounted transition in the fixture, check 25 still exits 1 when the
merge is replaced by a non-merge commit through `git replace`, and again, separately, when a graft
file is present.

**Left-shift.** That AC.

### M17 — S7's boundary refusal and F2's honest-flip property have no criterion (17)

**Where.** Unit 9 §2 S7 and §8 F2.

**Defect.** AC5 asserts a non-zero count on a fixture that has a transition. AC6 stages the
disagreeing reader and a shallow clone. Nothing stages refusal 2: a builds-mode HEAD over shards
history that yields no mode boundary. Nothing stages the property F2 exists for either: a linear
flip with no transition merge yet must exit 0 with no DEAD PROBE.

**Impact.** Reverting to A3's rule, "N=0 on a builds tree is a DEAD PROBE", passes AC5 and AC6. That
rule would red the flip branch between its flip commit and its landing merge, and permanently red an
adopter that flips linearly and never merges a straggler. A broken boundary detector also goes
uncaught. Unit 34 §5 still calls that window a "designed dead-probe state" (M6), so the specs already
disagree on this behaviour and nothing pins it.

**Fix.** Add two cases to AC6. A linear-flip fixture with no transition exits 0 and prints
`examined 0`. With the boundary detector staged broken over a history holding both shards and builds
commits, the check exits 1 as a DEAD PROBE.

**Left-shift.** Those arms.

### M18 — AC9 asserts a cache field that the liveness line does not have (18)

**Where.** Unit 9 §6 AC9, against §4 "Liveness, the registry, and the remedy" and §2 S10.

**Defect.** AC9 expects the liveness line to report cache hits, and a foreign-epoch recompute to be
"reported so". §4 pins the line as
`transitions examined <N> · merges walked <M> · pinned <P> · unpinned <U>`, with no cache field, and
S10 specifies no recompute message.

**Impact.** AC9 cannot be observed from the output the spec defines. The builder either changes a
pinned line or ships a cache arm that grades nothing. This is the "command does not print that" form
of `criterion-asserts-what-its-own-command-cannot-show`.

**Fix.** Add a cache-hit field to §4's grammar, or name the `--report` line that carries it, and
specify the foreign-epoch message.

**Left-shift.** Class item 2 below.

### M19 — the refusal's "exactly one side is a view" condition is never staged against two views (21)

**Where.** Unit 10 §2 S1 and §4 "The refusal".

**Defect.** S1's pseudocode refuses on `view_a != view_b`, and §4 says two views, or two shards over a
view base, proceed unchanged. AC1, AC2 and AC6 stage only one view against one shard. Neither unit
10's suite nor unit 7's criteria merge two views through the driver.

**Impact.** A refusal keyed on "either side is a view" passes AC1 to AC9. Because amendment A2 keeps
`merge=rows` on the views, that refusal would conflict every concurrent re-render after the switch.
M3 is the neighbouring half.

**Fix.** Add an AC: a three-way merge of two rendered views takes the key path with no refusal, and a
shard-against-shard merge over a view base is not refused.

**Left-shift.** That arm.

### M20 — no criterion exercises `--check`'s builds-mode population (22)

**Where.** Unit 10 §2 S5 and §5 error states.

**Defect.** Under builds, S5 adds every tracked `builds/*/BACKLOG.md` to the governed population, and
§5 makes zero such files an announcement. AC6 runs on this repo, which stays in shards mode until
unit 34, and AC7 runs on a scratch copy of the same tree. Unit 34 AC5 reads the attribute with
`git check-attr` directly, not through `--check`.

**Impact.** A mis-rooted `BACKLOG.md` selector passes AC6, because `DECISIONS.md` and the shards keep
the count above zero. After the switch, the leg meant to bind the per-build attribute never checks
it.

**Fix.** Add an AC over a builds-mode fixture. `--check` counts each tracked `BACKLOG.md`, reds
naming one whose attribute is removed, and prints the announcement when none is tracked.

**Left-shift.** That arm. The class is `memory/gotchas/vacuous-selector-empty-population.md`,
extended here to a population that stays non-empty through its other members.

### M21 — the archived-copy rule that recovers lost flips has no criterion (24)

**Where.** Unit 11 §2 S3 and §10.

**Defect.** S3's second rule, that among archived copies a terminal one beats a non-terminal one, is
observed by nothing. AC1 stages a live copy over an archived one, AC2 stages two live copies, and AC7
covers sizes. §10 cites the 2026-08-17 reconcile's lost flips as the reason for this rule.

**Impact.** Taking the first archived copy passes AC1, and reopens exactly the flips that reconcile
lost. The skeptic added a caveat on reach. §10's 521 live plus 78 archived copies equals its 599
distinct ids, so gov holds no duplicate copies at BASE. The risk falls on the adopter trees where
`--plan` is meant to run.

**Fix.** Add to AC1: an id with two archived copies, one CLOSED and one OPEN, and no live copy, is
chosen as CLOSED under either file order.

**Left-shift.** That arm, run under both file orders.

### M22 — F2's exclusions and the hold proposal have no criterion (25)

**Where.** Unit 11 §2 S6, §8 F2 and F5, and §6 AC4.

**Defect.** AC4 stages a spec closure, a commit naming the ask, a dead pointer and a same-id spec. It
stages no negative case for F2's exclusions: the filing commit, and a commit that touched only the
memory tree. It stages no `row-names-hold` proposal and no `design-named` row.

**Impact.** Two regressions pass AC4. The first proposes each ask's filing commit, F2's rejected
option (a). Unit 33's T3 then signs CLOSED, because a resolvable commit's message names the ask, so
filing commits are signed as closures. The second never proposes a hold. Unit 33's T5 then never
fires, and asks that should become holds are signed KEEP.

**Fix.** Extend AC4 with three cases. An ask whose only naming commit is the one that filed it
proposes `none`, and so does an ask named only by a commit that touched just the memory tree. An ask
whose row names a live hold proposes that hold, with basis `row-names-hold`. The three design-named
rows are listed with basis `design-named`.

**Left-shift.** Those arms.

### M23 — one guard reads the low-overlap flag, and nothing observes it (26)

**Where.** Unit 11 §2 S4 and §4 "Evidence", against unit 33 rule U3.

**Defect.** S4 promises a `low_overlap` flag and score. AC3 asserts only the evidence class, and no
unit 11 or unit 33 criterion reads the flag.

**Impact.** A flag that is always false passes everything. Beyond the four U2 pairs, unit 33's U3 is
the only guard against signing `unit` on a specced-in-place pair that is about a different subject.
The silent error that unit 33 §4 says U3 prevents follows: an ask closed through a spec that never
answered it.

**Fix.** Add to AC3: a pair whose row shares no words with the spec's H1 and Goal is flagged, with
its score, and a matching pair is not.

**Left-shift.** That arm.

### M24 — §5 promises an empty-corpus refusal that no scope item carries (28)

**Where.** Unit 11 §5 error states, against §2 S2 and S3.

**Defect.** §5 lists "an empty corpus" among the refusals, but no S-item carries it and no AC stages
it. AC9 and AC11 both pass at zero, since AC11 compares two figures that would both be zero.

**Impact.** Suppose an adopter's deployer run of `--plan` mis-resolves `MEMORY_ROOT`. It reads zero
rows, proves conservation trivially, and files empty worksheets, all under a green exit. Unit 33's
empty-worksheet refusal catches this downstream in gov only. The class is
`memory/gotchas/fixture-passes-by-finding-nothing.md`.

**Fix.** Add the refusal to S2, with an AC: `--plan` over a fixture with no shard exits 1, naming the
empty population, and files no worksheet.

**Left-shift.** That arm.

### M25 — two of S1's three side resolutions are never staged (32)

**Where.** Unit 12 §2 S1, §6 AC1 and AC9.

**Defect.** S1 resolves the straggler side from MERGE_HEAD, else from the first parent of a merge
HEAD, else from `--from <ref>`. AC1 runs with MERGE_HEAD present, and AC9 stages only the refusal.

**Impact.** Swapped parents on a concluded merge relocate the default side's rows as if they were
the straggler's, and that passes. So does a `--from` that picks the wrong side. If S3's post-write
re-read uses the same resolved sides, a swap stays self-consistent and nothing reds: a guard that
shares a variable with what it guards.

**Fix.** Add to AC1: the same fixture with the merge already committed, and again with
`--from <ref>`, yields byte-identical records.

**Left-shift.** That arm. The byte-identical comparison across the three entry forms serves as the
independent reader.

### M26 — no criterion observes the confirmation F1 extended to `--ingest` (33)

**Where.** Unit 12 §2 S5 and §8 F1.

**Defect.** F1 chose option (c) so that `--ingest` also requires `--confirm`. AC3 stages only
`--repair`, and AC5's `--ingest` writes no status-changing record.

**Impact.** An `--ingest` that writes CLOSED over a deliberate reopen without `--confirm` passes. That
is lab case e09b, the reason F1 rejected option (a).

**Fix.** Add to AC3: `--ingest` of the same contested ref refuses, naming the id and `--confirm`.

**Left-shift.** One arm per verb and form that reaches the writer, driven from the entry-path table
M7 proposes.

### M27 — the `filed` rule feeds four verdicts and has no criterion (34)

**Where.** Unit 12 §4 "Classification", the paragraph on `filed`.

**Defect.** `filed` is the author day of the oldest lineage commit whose blob holds the id. AC1
checks the folder, the disposition sha, the path and the RELOCATED rows, but never `filed`. Unit 11
§3 leaves the date to this engine as its only miner. Unit 34 S4 derives `ASK_CUTOFF` from the dates
the writer wrote. V9, V12, V14 and check 13 all key on `filed`.

**Impact.** A date taken from the oldest lineage commit regardless of the id passes, and so does one
taken from the relocation commit. A date that is too early silently exempts a relocated ask from
every forward-only check, and unit 34 AC4 still passes over too-early dates.

**Fix.** Add to AC1: the relocated new ask's `filed` equals the author day of the fixture commit that
first added its row, not the day of the merge or relocation commit.

**Left-shift.** That arm, with the fixture's commits dated on distinct days so that a wrong source
cannot coincide with the right one.

### M28 — no criterion covers the remote-tracking conf read or the allow on an unresolvable default (36)

**Where.** Unit 13 §4 "Why a library beside the hooks" (the sentence naming the conf source), and §5
error states.

**Defect.** §4 reads the default branch's conf from the remote-tracking default first, "since that is
where the flip is observed". §5 says an unresolvable default branch or conf blob prints a named line
and allows. No AC builds a fixture whose remote-tracking default is in builds mode while the local
default is stale, and none has an unresolvable default.

**Impact.** A library that reads only the local default passes every AC. It stays dormant on any node
whose local main has not been fast-forwarded, which is common for worktree sessions. A library that
refuses, or stays silent, on an unresolved default also passes.

**Fix.** Add an AC with two cases. With origin's default in builds mode and the local default still
in shards mode, the pre-commit refusal fires. With no resolvable default, the hook allows and prints
the named line.

**Left-shift.** Those arms.

## Low

### L1 — no criterion isolates the A6 exclusion in unit 9's S4 (19)

**Where.** Unit 9 §2 S4 (design A6) and §6 AC4.

**Defect.** S4 carries two exclusions: a row must differ from EVERY merge base, and it must never have
been held by a shards-mode commit on the other side. AC4's criss-cross fixture holds a version equal
to one merge base, which either clause alone would omit, so AC4 observes neither clause on its own.
AC1 and AC3 never stage a version the default side held, such as a cherry-pick.

**Impact.** Dropping the A6 clause passes. The audit then reports rows that came across from the
default side as the straggler's own changes, and demands provenance rows for changes nobody made.
The failure is loud, not lossy.

**Fix.** Add an AC: a straggler merges a shards-mode default commit that carries a row change, then
merges into a builds-mode default, and that id is absent from the delta.

**Left-shift.** That arm.

### L2 — nothing observes commit-msg's entry in `GOV_WIRING_HOOKS` (20)

**Where.** Unit 9 §2 S12 and §6 AC10.

**Defect.** S12 adds `commit-msg` to `GOV_WIRING_HOOKS` (`tools/check-wiring.sh:209`) and cites AC10,
which runs only testsuite-counts and govkit selfcheck. The comment at
`tools/check-wiring.test.sh:816-817` says the hook arms derive from that list. The arms below it name
`pre-commit` and `pre-push` literally, and nothing asserts that every tracked hook file is on the
list.

**Impact.** Omitting the entry passes, and check H then never reports a diverged `commit-msg`, the
hook S9 depends on. This is low because check H reports only as a note.

**Fix.** Extend AC10 to assert that check-wiring's hook walk includes `commit-msg`.

**Left-shift.** Class item 3d below. L7 is the same gap in unit 13.

### L3 — AC11's triage-count equality compares one function with itself (29)

**Where.** Unit 11 §2 S5 and §6 AC11.

**Defect.** S5 computes the triage population after the migration's own dispositions. No criterion
puts an ask with a terminal legacy token on a finished build and asserts that it is absent: AC4's
asks are all OPEN, and AC5 asserts only the status worksheet. AC11's equality compares two outputs of
one population function.

**Impact.** An ask whose legacy row reads CLOSED can enter the triage worksheet, and AC11 still passes
because both counts share the defect. The class is
`memory/gotchas/second-implementation-is-not-a-second-opinion.md`.

**Fix.** Add to AC4: such an ask is absent from the triage worksheet. Re-derive AC11's count
independently, for example from the status worksheet's predicted-OPEN rows on finished builds.

**Left-shift.** That arm.

### L4 — a hold naming a shorthand or a decision id is never staged against S7 (30)

**Where.** Unit 11 §2 S7 and §6 AC5.

**Defect.** S7 counts a hold that names a shorthand such as `-4`, or an id that is neither a census id
nor a spec H1, as naming none. AC5 stages only a BLOCKED row naming a valid id and a DEFERRED row
naming nothing. §10 confirms such rows exist at BASE.

**Impact.** A hold naming a decision id previews as BLOCKED on that id and first surfaces at the
flip, as V6 or as an AC3 mismatch. This is the preview half of B1.

**Fix.** Add to AC5: a BLOCKED row naming `-4` and one naming an EXMP decision id both preview as
holds on `TRIAGE-ASK`.

**Left-shift.** That arm, sharing its fixture with B1's engine arm.

### L5 — AC10's Red-when names a break its observation cannot see (31)

**Where.** Unit 11 §6 AC10.

**Defect.** AC10 observes a PASS count at or above a floor and the leg's presence and claim. Its
Red-when, "an arm's failing case was never observed with its fix unstaged", cannot move either
observation.

**Impact.** The criterion stays green for exactly the break it names.

**Fix.** Name an observation that can see the break, as unit 12 AC10 does: each arm's RED is observed
by hand against a scratch fixture and recorded in the pass.

**Left-shift.** The documented check in class item 2 below.

### L6 — no AC stages the decision-log-rotation exclusion that F4 chose (37)

**Where.** Unit 13 §2 S1 (HAS-DELTA) and §8 F4.

**Defect.** S1 limits HAS-DELTA to the backlog shards and the family-named backlog archives, so that
a decision-log rotation prints no recipe. No AC stages a pre-flip branch whose only archive change is
a decision-log rotation. AC3's "branch with no backlog commit" does not say it carries one.

**Impact.** Widening the population to unit 9's whole archive directory passes every AC. The hooks
then print relocation instructions for a rotation that has nothing to relocate, and `pre-rebase`
refuses such a branch.

**Fix.** Add to AC2 or AC3: a pre-flip branch that rotated only `DECISIONS.md` gets no notice and
rebases.

**Left-shift.** That arm.

### L7 — nothing observes pre-rebase's entry in `GOV_WIRING_HOOKS` (38)

**Where.** Unit 13 §2 S7 and §6 AC9.

**Defect.** S7 adds `pre-rebase` to `GOV_WIRING_HOOKS` and cites AC9, which runs govkit selfcheck,
`test_codebase_map.py` and `check-install-prefix.sh`. None of those reads the list.

**Impact.** Omitting the entry passes, and check H never reports a diverged `pre-rebase`. This is low
for the same reason as L2.

**Fix.** Extend AC6 or AC9 to assert that check-wiring's hook walk includes `pre-rebase`.

**Left-shift.** Class item 3d below.

## Left-shift, by class

1. **An interface promised across specs that no scope item carries** (B1, B2, B3, H1, H3, M5, M6).
   Three mechanical joins fit `tools/check-spec-tokens.py`. Run each over this build first and print
   hits and near-misses before wiring it, per charter §7.
   - (a) Every `**hands-off**` bullet cites at least one `S<n>` of its own spec, and every
     `**consumes-from**` bullet cites an `S<n>` of the producer, each resolved against that spec's
     §2. Unit 9's hands-offs to 12 and 13, and unit 12's hands-off to 34 for the reconcile, would
     have nothing to cite.
   - (b) A backticked token that one spec assigns to a named sibling must occur in that sibling's
     text. Unit 11's `TRIAGE-ASK`, which "the switch-over substitutes", is a live hit against
     unit 34.
   - (c) A spec whose §4 or §6 invokes a command that another spec in the build lists in its Files
     touched declares consumes-from that spec. Unit 34 runs `gen_build_index.py --write`, `--check`
     and `--asks --json` with no edge to unit 7, and that is how H3's two readings met without either
     spec seeing the other.

   The documented half belongs to the M2 cross-read. Every sentence of the form "the <sibling> does
   X" is grepped in that sibling for X. A policy deferred to the cross-read, as unit 11 §10 deferred
   one, is not closed until the receiving spec carries it as an S-item.
2. **An S-item whose Observed-by criteria survive its deletion** (M14 to M28, L1 to L7, M2, and half
   of M5), per `criterion-asserts-what-its-own-command-cannot-show`. This group's lenses were primed
   with the skip test and still found 22 outright instances, so the class survives spec authoring.
   The fold should write the mutation that deletes each S-item, and the AC that reds on it, beside
   that S-item's "Observed by". The mechanical half is the one G1 proposed: a `check-spec-tokens.py`
   near-miss printer for an S-item whose cited ACs share no backticked token with it. It prints and
   never reds.
3. **A new moving part whose declarations the spec never names** (M8, M10 to M13, L2, L7). One join
   in `tools/check-spec-tokens.py` covers it, over inputs already in the tree: each spec's Files
   touched, its §7 legs, and the declaring files at BASE.
   - (a) A spec that adds a leg lists a `kit.toml` or `tools/govkit/registry.toml` in Files touched,
     and `govkit selfcheck` in §7.
   - (b) A leg in chunk `selftests` or with subject `kit` lists `tools/run-gates/selftest-budgets.txt`.
   - (c) A Files-touched path that `tools/install-prefix-waivers.txt` names owes
     `install-prefix (shipped surface)` in §7.
   - (d) A new tracked `.githooks/` path owes a govkit entry or `[[exempt]]` row. Its runtime half is
     a check-wiring arm that derives the tracked hook files and `GOV_WIRING_HOOKS` and compares them
     both ways.

   A runtime import of a sibling kit (M8) owes a `requires_if` edge, and that is a documented check,
   because an import does not show in Files touched.
4. **An environment premise measured under one configuration and stated as universal** (H2). This
   is not mechanically gateable from a spec. The documented check is that an environment claim in a
   spec names the configuration it was measured under, here whether a `config.worktree` override is
   present, and that §10 re-measures it under the configuration this repo's own wiring writes. The
   same premise is written in `.githooks/pre-push:6-9`, in `tools/check-wiring.test.sh:811` and in
   `memory/gotchas/hookspath-resolves-into-another-checkout.md`. Each was true for the absolute
   configuration it measured. That gotcha should gain this build as an anchor, and should say which
   configuration its premise holds under.
5. **A verdict with a producer and no reporter** (M1, M2). Unit 7's verdict arm should iterate the
   codes that unit 6's module exports, conf-reader verdicts included, rather than a typed "V1 to
   V12". A code with no reporting arm then reds. It is derive-over-author, and it would have caught
   M1.
6. **A print mode whose stdout carries more than its value** (M4). Every `--json` or `--print-*` mode
   in the memory-tree kit gets an arm that parses its whole stdout. The hygiene engine's ON STDERR
   note is the measured precedent in this repo.

## Outside the confirmed set

Two observations came out of re-checking the highs and were not put to a skeptic, so neither is
counted above. Both were read at `abac6d59` or measured on node `d` today.

Unit 11 also declares its new leg, `backlog migration selftest`, in no descriptor. Its Files touched
omit `tools/memory-tree/kit.toml` and `tools/govkit/registry.toml`, and its §7 omits
`govkit selfcheck`. By the rule at `tools/govkit/govkit.py:1642-1644`, the leg reds selfcheck at the
post-build bar. That makes a third live instance of M12's class, beside units 10 and 13. Unit 9 lists
both descriptor files in its Files touched, but its S12 names no leg declaration, so its fold should
say which one it writes.

The hooksPath configuration measured for H2 matters beyond unit 13. The shared config holds the
relative `.githooks` that check-wiring writes. The design's premise is true only for worktrees
carrying an absolute `config.worktree` override, whatever wrote it, and not for the repo's own
wiring. Every claim in this build that "old branches run main's hook files" inherits that
condition.

## What this round did not cover

- Units outside G2 were read only where an edge or an interface named them. Nothing here clears
  units 1 to 5 or 15 to 36, PLAY-dDerivedDocket-1 or DEPL-dDerivedDocket-1. B1, B2, B3, M5, M6 and M9
  name defects that also live in units 33 and 34, and their own group audits should pick them up.
  The fold for each blocker must land in both specs at once.
- This round raised two questions and did not answer them.
  - Does unit 9's `commit-msg` carrier fire in a relative-wired straggler worktree that is concluding
    its first merge of the flip, where the hook file arrives in that same merge? This is H2's premise
    one layer down, and it was not measured.
  - Where does `--write` take each migrated ask's `filed` date? Unit 34 S1 makes its delta "from an
    empty base", unit 12's rule reads the delta walk's commit list, and unit 11 disclaims mining the
    date. This is M27's input.
- Unit 14 is retired at WONTDO. It drew no confirmed finding, and this round did not re-derive its §4
  mapping.
- The design record's measured figures were not independently re-derived, except for the TOOL
  shard's 460 row lines and the hooksPath configuration, both measured for this report.
- The 35 refuted findings are not reproduced here. They were refuted, not lost, as the run-integrity
  counters show.
