# Research: the whole-design shape audit, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked, "Can we review the entire design's shape for any gaps that may be left?", and chose two full runs at
medium. Two independent spec audits read the design's three defining records whole. This record compares them defect by
defect, as the earlier paired rounds were compared, and sorts each defect: a fold, a fork for the owner, or refuted.

## [runs] The two runs

- **Subjects:** v2, the gap register and the memory plan at `89e44048f`, pinned by blob, with 28 design records as
  context.
- **Harness:** `tools/workflows/tier2-review.js`, a full spec audit: five `gov-spec-reviewer` lenses, five `gov-skeptic`
  batches and one `gov-synthesizer`, every role at the owner's medium. The harness's five spec lenses are fixed, so each
  carried one of the owner's shape questions as its project note: coherence carried intent, grounding product coverage,
  reuse buildability, blast-radius supersession and the adopter's journey, and failure-envelope loop completeness and
  trust.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 116 | `wf_0dd3b79b-986` | `reviews/2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-a.md` |
  | B | 117 | `wf_359adbd0-0d7` | `reviews/2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-b.md` |

- **The args:** `build_args_shape.py` wrote both. They differ only in the run label, the report path and the scratch
  path, checked before run A launched, and the runs went one after the other.
- **The admission:** agent-cap refused the first launch, since this build's README is prompt-authorized. The one-off
  admission the owner chose on 2026-10-15 was set around each launch and restored, in the working tree only. The
  session log records it.

## [method] How the runs were compared

The runtime comparison's `[method]` applies unchanged: every finding of both runs, confirmed or refuted, is placed on
the defect it names, a finding naming two defects lands on both, a run finds a defect when one of its findings on it was
confirmed, and the defect takes the highest grade any confirmed finding on it got, the skeptic's where one was given.
The tables are derived by `compare_rounds.py` from the two reports, `[map]` and the session log.

A defect goes to the owner as a fork when its fix is a choice the design does not make itself: a new mechanism, a
change of owner, or one of two routes the reviewers left open.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `owner-proof-forgeable` | the owner-only proof (a terminal, a typed trailer) is one an agent can produce | 38 | 42 | fork SA-1 |
| `step-gate-missing` | no check reds a change to an adopter-visible surface that ships no upgrade step | 26 | 1, 13, 34 | fork SA-11 |
| `rows-lack-steps` | builds that change adopter surfaces name no step, and recovery lands after them | 27 | 1, 13, 34 | fold the step clauses; the ordering is fork SA-2 |
| `gov-first-late` | steps landed before dShippedRelease never run on gov first | 33 | 2, 37 | fork SA-3 |
| `walk-failure-route` | the upgrade walk has no route for a failed or interrupted step | 43 | 48 | fold |
| `legacy-populations` | the causes, pins, orphan and work-order gates declare no legacy population | 2, 37 | 3, 20, 46 | fold |
| `journal-rename` | the Serves kind `journal` is renamed `log` with no alias, inventory or step | 29 | 4, 19, 32 | fold |
| `migration-by-hand` | [migration] says nothing is by hand, then routes decision rows by hand | 13 | 4 | fold |
| `runaway-ceiling` | the round-count bound reads a constant the chain deletes | 31 | 5 | fold |
| `orientation-card` | retiring the orientation cards strands the write gate's route check | 1, 30 | 33 | fold |
| `root-stand-ins` | `record` refuses a missing cause before any root kind exists | 3 | — | fold |
| `door-list` | the one-door rule lists five doors while the plan names more writers | 4 | 8, 51 | fold |
| `salted-undefined` | `trace.identity: salted` is selectable but undefined | 5 | 24 | fork SA-4 |
| `values-without-route` | catalogued values no clause routes: commit-msg, refuse, accept-loss and retag | 25 | 24 | fold |
| `p35-states` | P35's not-local and pruned states and the transcript pointer have no unit | 6 | 7 | fold |
| `reads-writes-sites` | the `reads` and `writes` edges are declared at two sites | 8 | — | fold |
| `p33-addresses` | P33 and the namespace registry cannot address acts, sessions, commits or landings | 9 | — | fold |
| `edge-grammar` | a section target does not fit the edge line, whose line rule is stated two ways | 42 | 11, 50 | fold |
| `p34-rationale-owned` | P34's rationale rule has no check, and `owned` names two checks | 10 | — | fold |
| `p37-legs-missing` | P37's path, temp-file and quoting rules have no leg | 11 | — | fold |
| `p37-encoding-optional` | P37's Python encoding leg lives only in an optional kit | — | 17 | fold |
| `cycle-walk` | nothing walks the owner's cycle end to end | 12 | — | fold |
| `kickoff-skill-link` | the per-machine kickoff skill link has no fate, owner or upgrade path | 15 | — | fork SA-9 |
| `help-docs` | the `help/` pages and the docs rule have no pocket, fate or owner | 16 | 15 | fork SA-5 |
| `fates-population` | convergence's exit check never derives the shipped-part population | — | 15 | fold |
| `transcript-retention` | transcript retention is one node's setting stated as a fact | 17 | 18 | fold |
| `bash-resolver-seam` | the shared bash resolver ignores the existing resolvers and `GOV_BASH` | 19 | 28 | fold |
| `trailer-readers` | one reader for `Pass:` and `Decided:` ignores the existing readers and their deliberate difference | 7, 20 | 26 | fold |
| `trace-model` | `gov trace` duplicates runlog's timeline model | 20 | — | fold |
| `retired-edited` | an edited retired file reuses the `forked` role, whose contract does not fit | 21 | — | fold |
| `finder-two-builds` | two builds each build a record finder | 22 | 25 | fork SA-6 |
| `selector-two-builds` | two builds each spec a write-set bug-class selector | 23 | — | fork SA-7 |
| `window-before-releases` | the deprecation window counts releases before any release exists | 32 | 35 | fork SA-8 |
| `lander-commits` | the lander's own commits are neither a commit site nor an exemption | 35 | — | fold |
| `codex-retrust` | Codex hook trust is lost when an update changes a hook | 39 | 44 | fold |
| `off-node-bindings` | the commit-key and cause checks read node-local bindings with no off-node rule | 40 | 45 | fork SA-10 |
| `empty-sets` | set-valued keys accept the empty set | 41 | — | fold |
| `released-steps-frozen` | a released upgrade row can be edited or removed | 44 | — | fold |
| `step-contract` | upgrade steps have no execution contract | 45 | 53 | fold |
| `emitted-ci-pins` | emitted CI carries no action-pinning or permissions rule | 47 | 52 | fold |
| `refs-owner` | the refs pocket gives four ref families one owner | 14 | 9 | fold |
| `gitdir-pockets` | the pockets table omits live git-dir pockets | 18 | — | fold |
| `deploy-toml-pocket` | `.governance/deploy.toml` renders into the charter but is not a pocket | — | 31 | fold the row; its guard is fork SA-12 |
| `region-parsers` | the region-parser population is a typed five | 24 | — | fold |
| `unattended-inventory` | the unattended kit's retirement misses its value readers | 34 | 39 | fold |
| `policy-values-owner` | the policy-values pocket names a superseded owner | 36 | — | fold |
| `act-key-session` | the act key assumes a preset harness session id | 49 | — | fold |
| `receipt-schema` | the receipt schema bump launders a corrupt receipt past S9 | 28 | — | fold |
| `supervisor-restart` | a restarted supervisor can launch a second act on the same item | — | 49 | fold |
| `answers-no-clause` | AP-4 and AP-16 have no chain clause | — | 6 | fold |
| `promotion-node-local` | the promotion gate reads node-local auto-memory with no declared runner | — | 21 | fold |
| `scoutedseam-branch` | aScoutedSeam's grader and benchmark exist only on an unmerged branch | — | 23 | fold |
| `replay-scorers` | three replay measurements bypass dFairHearing's scorer factory | — | 27 | fold |
| `ledger-driver` | the baseline ledger's driver does not name `merge-rows.py` | — | 29 | fold |
| `kind-factory-dup` | dConvergedCharter builds a record-kind factory beside dTotalRecall's registry | — | 30 | fold |
| `credential-homes` | the default credential order names no readable home on either platform | — | 43 | fold |
| `intake-ratification` | a mailbox intake can serve as the owner's ratification | — | 47 | fold |
| `code-record-bounds` | the core `code` record has no input exclusions or over-ceiling route | — | 54 | fold |
| `malformed-spans` | malformed annotation spans are undefined | — | 55 | fold |
| `declined-retirement` | a declined retirement leaves convergence unable to exit | — | 56 | fold |
| `live-questions` | dKeptSession relies on a later build for live owner questions | — | 10 | fold |
| `pass-edge-tallies` | `Pass:` has no edge type, and the hop tallies disagree | — | 12 | fold |
| `p3-ground` | P3 states that remote CI is unavailable | — | 22 | fold |
| `map-lib-window` | the `map_lib` re-export is held one release against a window of two | — | 36 | fold |
| `backfill-owner` | the plan's adopter backfill step has no owner | — | 38 | fold |
| `floor-query` | the interpreter-floor inventory searches one value | — | 41 | fold |
| `floor-hooks` | the hooks' resolver accepts an interpreter below the raised floor | 46 | — | refuted |
| `shim-removal` | removing a shim strands an adopter held behind | 48 | — | refuted |
| `intake-redaction` | intake text reaches the record unredacted | — | 14 | refuted |
| `mirror-crlf` | a CRLF checkout breaks the policy mirror's hash | — | 16 | refuted |
| `reuse-lookup-readers` | `reuse_lookup.py`'s readers are left demanding citations | — | 40 | refuted |

## [summary] The two runs side by side

```text
$ python compare_rounds.py shape-audit-a.md shape-audit-b.md shape-reviews-compared.md session-log.md wf_0dd3b79b-986 wf_359adbd0-0d7
== runs
A: raw 49, confirmed 45, refuted 4, precision 0.92, high findings 4, agents 12, out 291.7k (sum of returned lines)
B: raw 56, confirmed 53, refuted 3, precision 0.95, high findings 6, agents 12, out 318.0k (sum of returned lines)
== defects
map rows 71, confirmed defects 66, refuted-only 5
both 26, A only 18, B only 22
A alone covers 44 of 66 (67%)
B alone covers 48 of 66 (73%)
overlap (Jaccard) 0.39
Chapman estimate of the population: 80.7, so about 15 found by neither
A only: root-stand-ins, reads-writes-sites, p33-addresses, p34-rationale-owned, p37-legs-missing, cycle-walk, kickoff-skill-link, trace-model, retired-edited, selector-two-builds, lander-commits, empty-sets, released-steps-frozen, gitdir-pockets, region-parsers, policy-values-owner, act-key-session, receipt-schema
B only: values-without-route, p37-encoding-optional, fates-population, deploy-toml-pocket, supervisor-restart, answers-no-clause, promotion-node-local, scoutedseam-branch, replay-scorers, ledger-driver, kind-factory-dup, credential-homes, intake-ratification, code-record-bounds, malformed-spans, declined-retirement, live-questions, pass-edge-tallies, p3-ground, map-lib-window, backfill-owner, floor-query
== severity (a defect takes its highest confirmed grade per round)
high defects 9: owner-proof-forgeable, step-gate-missing, rows-lack-steps, walk-failure-route, journal-rename, orientation-card, off-node-bindings, receipt-schema, supervisor-restart
  owner-proof-forgeable: A 3 B 3
  step-gate-missing: A 2 B 3
  rows-lack-steps: A 2 B 3
  walk-failure-route: A 2 B 3
  journal-rename: A 3 B 2
  orientation-card: A 3 B 2
  off-node-bindings: A 2 B 3
  receipt-schema: A 3 B 0
  supervisor-restart: A 0 B 3
shared defects graded alike 18 of 26
== lenses behind the defects one round alone found
A: coherence 6, reuse 4, blast-radius 3, failure-envelope 3, grounding 2
B: reuse 6, failure-envelope 6, grounding 4, coherence 3, blast-radius 3
== refuted findings and their twins
A25 (values-without-route): confirmed twin B24
A37 (legacy-populations): confirmed twin A2, B3, B20, B46
A46 (floor-hooks): confirmed twin none
A48 (shim-removal): confirmed twin none
B14 (intake-redaction): confirmed twin none
B16 (mirror-crlf): confirmed twin none
B40 (reuse-lookup-readers): confirmed twin none
```

- **The design does not have its full shape yet.** Two runs confirmed 66 defects, nine of them high, and Chapman's
  estimate puts about fifteen more beyond both.
- **One run finds about two thirds.** Run A alone covers 44 of the 66 and run B 48, an overlap of 0.39, the lowest of
  the paired rounds so far. Each run caught one high the other missed: the receipt schema (A) and the supervisor restart
  (B).
- **Precision held at 0.92 and 0.95.** Of the seven refuted findings, two sit on a defect another finding confirmed.
- **The gaps gather in five places:**
  - supersession: the step gate, rows that ship no step, gov first, the walk's failure route, released steps, the
    step's execution contract and the window's count;
  - the trust boundaries: the owner proof, off-node bindings, mailbox ratification, credential homes, Codex re-trust
    and emitted CI;
  - retirements that strand a live reader: the orientation card, the `journal` rename, the runaway ceiling and the
    unattended inventory;
  - gates armed over today's corpus with no legacy population;
  - one behaviour claimed by two builds: the finder, the selector, the kind factory and the scorers.

## [forks] For the owner, 2026-10-19

Twelve defects need a choice the design does not make itself. A key's default and a clause stand as written until the
owner answers.

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| SA-1 | What proves an owner-only action? Today's `tty-cli` proof is a terminal and a typed trailer, both of which an agent's shell can produce. | layered: the harness refuses a guarded command's argv from an agent's shell, `tty-cli` is recorded as proving presence against a cooperative agent only, and the floor's owner-only writes carry a signature from a key that needs user presence, checked at the push and off-node; the harness refusal and the recorded limit only; `tty-cli` as it stands, the threat recorded as accepted | v2 [witnesses], `policy.proof`, and dGroundRules' and dDeclaredLoop's guards |
| SA-2 | Builds between dSafePassage and dShippedRelease change adopter surfaces before hook unwiring, retired-edit orders and stale-lock reclaim exist. What do adopters do in between? | move hook unwiring, retired-edit orders and stale-lock reclaim into dSafePassage; hold adopters at dSafePassage's release until dShippedRelease lands | the chain |
| SA-3 | Where does running each new step on gov's own tree first live? | in dSafePassage, beside the step kind, so every step from the first runs on gov first (AP-30); in dShippedRelease, which back-runs every step registered since release-0 | the chain |
| SA-4 | `trace.identity: salted` is an allowed value no record defines. Define it, or drop it? | define it: the trailer carries a keyed hash of the session id, the key kept in the node's credential store, and the commit-key leg's refusals under it; drop `salted` from the allowed values | the key's allowed values |
| SA-5 | How are the `help/` pages kept current, as the charter's [docs] rule asks? | a docs leg that reds a changed user-facing command whose page did not change, with `help/` a pocket owned by dConvergedCharter; pages rendered from a new `help` field on each unit, plus the leg; leave `help/` out of the design | the plan's [pockets], the fates and a leg |
| SA-6 | Which build owns the record finder? | dTotalRecall: `record find` reshapes `query.py` and takes over check-recall, as the fates say, and dLinkedLibrary keeps memory-recall's bench, union and why-search; dLinkedLibrary, with `record find` struck from dTotalRecall | two [chain] rows and the fates |
| SA-7 | Which build owns the write-set bug-class selector? | dFurnishedOrders renders it as the work order's field through `gotchas.py --for-paths`, and dLinkedLibrary's clause is struck; dLinkedLibrary owns it, and dFurnishedOrders reads its output | two [chain] rows |
| SA-8 | How does `install.deprecation-window` count releases before gov has release tags? | windows start at the first cut release, every earlier shim held until then; a first tag cut at dSafePassage's landing; receipt-recorded landings counted until tags exist | dSafePassage's shim clause |
| SA-9 | The per-machine `/session-kickoff` link points at gov's live checkout outside any repository. How is it governed? | node-level install surfaces declared in dSafePassage as an upgrade-step surface, the link given a fates row and checked per node by the node registry and dWellOiledMachine's preflight; the link retired for a repository-installed skill | dSafePassage, the fates and the preflight |
| SA-10 | The commit-key and cause checks read act bindings that live on one node. What do they do on another? | every act pushes a minimal binding record (act id, epoch, node, task sha) to a ref the checks read on any node; the checks read local bindings only and count the rest as not-local, never passed | dWellOiledMachine's commit-key leg and the causes check |
| SA-11 | Add a gate in dSafePassage that reds a landing which changes an adopter-visible surface with no upgrade or retired row naming it? | yes, seen red on a planted rename with no step and green on a content-only edit; no gate, each build's review checks it | dSafePassage's row |
| SA-12 | `.governance/deploy.toml` renders into the charter's level 0. Add it to dGroundRules' minimal guard? | yes; a pocket row only | dGroundRules' guard list |

The other 56 confirmed defects fold as `[map]` says, two of them partly waiting on a fork (SA-2, SA-12), each by its
report's sound or corrected fix. The fold lands once the forks are answered, and owes its closing review.

## [answers] The owner's answers, 2026-10-19

The forks went to the owner in three batches, each question with its recommendation first. The owner's words,
verbatim:

| Fork | The owner's answer |
|---|---|
| SA-1 | "Keep tty-cli as is for now, but file layered proof as a test for a layer date." |
| SA-2 | "Move them into dSafePassage (Recommended)" |
| SA-3 | "In dSafePassage (Recommended)" |
| SA-4 | "Define it (Recommended)" |
| SA-5 | "Rendered from units" |
| SA-6 | "dTotalRecall (Recommended)" |
| SA-7 | "dFurnishedOrders (Recommended)" |
| SA-8 | "First cut release (Recommended)" |
| SA-9 | first a question, quoted below; then, re-asked as retire, keep a thin entry, or a thin entry per repository: "Retire it (Recommended)" |
| SA-10 | "Push binding records (Recommended)" |
| SA-11 | "Yes, the gate (Recommended)" |
| SA-12 | "Yes, guard it (Recommended)" |

SA-9 came back first as a question:

> does session-kickoff skill still have a place in the new architecture? Previously, it was a manual kickoff step intended mostly for attended builds but in the new design this step is handled by the flow + orientation agents. Should this skill be kept?

It was answered from the records before it was re-asked. Every job the skill does already has a home: when to orient
is `kickoff.runs: no-ready-card`, the owner's OR-2 (dRankedPlan); the card is the orientation scout's, written at
session start (dFurnishedOrders); a resumed build reads its saved card (dOrderedCharter, dPlacedRequest); and the
manifest audit is the guarded instruction manifest (dOrderedCharter). The thin entry the fates record kept would
shortcut nothing the flow does not run already, and retiring it gives the per-machine link a fate.

How each answer was read:
- **SA-1:** "a layer date" is read as "a later date". `tty-cli` stays the default, and its threat is recorded as
  accepted for now in v2's `[witnesses]`. The layered proof is filed in `[planned]`, its forged-proof probes the test
  it must pass, its trigger the owner's word. v2's `[open]` keeps the reading to confirm.
- **SA-2:** the hook unwiring, the retired-edit order and the stale-lock reclaim move from dShippedRelease to
  dSafePassage, with `gap-deploy-18` and `gap-deploy-19`. Adopters are not held at a release.
- **SA-3:** dSafePassage runs every step on gov's own tree first, with `gap-deploy-20`.
- **SA-5:** the pages render from a field on each user-facing unit, named `usage`, since a unit's `help` field
  already holds its rationale, which never renders into a page. v2's `[open]` keeps the name to confirm.
- **SA-6:** `record find` reshapes `query.py` and takes `check-recall`. memory-recall keeps its why-search, and its
  bench and union become the `experiment` instance the owner's NP-22 already gave dBoundRoles.
- **SA-9:** retired by dConvergedCharter once the scout and `kickoff.runs` have landed, with a forwarding stub for
  the deprecation window.
- **The rest** read as their recommendations read in `[forks]`.

## [fold] The fold plan

| Defect | The fold | Left-shift |
|---|---|---|
| `owner-proof-forgeable` | v2's `[witnesses]` states what `tty-cli` proves and the threat the owner accepts for now, and `[planned]` files the layered proof with its forged-proof probes as its test (SA-1) | `inputs-inside-the-subjects-reach`, an instance; the probes are the planned proof's test |
| `step-gate-missing` | dSafePassage's step gate diffs the adopter-visible surface population and reds a change no step row names, seen red on three plants and green on a content-only edit (SA-11); P38 names it; `gap-deploy-25` | the step gate; `rule-stated-with-no-check-that-fails`, an instance |
| `rows-lack-steps` | dDeclaredLoop, dTotalRecall, dLinkedLibrary, dWellOiledMachine, dBoundRoles and dMindYourWords name their own steps; the hook unwiring, the retired-edit state and the stale lock move to dSafePassage with `gap-deploy-18` and `gap-deploy-19` (SA-2) | the step gate; `step-depends-on-a-later-build`, an instance |
| `gov-first-late` | dSafePassage runs every step on gov's tree in the prepared merge first, its receipt listing every step id, with `gap-deploy-20` (SA-3) | the planted step whose witness fails on gov; `step-depends-on-a-later-build`, an instance |
| `walk-failure-route` | dSafePassage's walk: a step atomic or resumable with its witness written last, the receipt advanced per completed step, a failed step stopping the walk, downs tolerating a partial up, the rollback never run on its own; two `upgrade-walk` arms | the kill-midway and exit-1 arms; `beacon-published-before-it-is-complete`, an instance |
| `legacy-populations` | the plan's `[gates]` declares each arm's legacy population, seeded by `test.seed`; dTotalRecall's causes and orphan checks, dBoundRoles' work orders, dOrderedCharter's pins and dTendedCadence's commit reading each name theirs | `predicate-designed-without-a-run-over-the-tree`, an instance |
| `journal-rename` | `journal` kept as the read-only retired alias of `log`, every reader re-pointed by value in the rename's unit, the alias an adopter step, and the plan's count re-measured at `dd1ebb01b` | `a-spelling-change-strands-its-readers`, an instance |
| `migration-by-hand` | `[migration]` opens with the one population routed by hand | `amendment-leaves-its-other-half-standing`, an instance |
| `runaway-ceiling` | dDeclaredLoop moves `RUNAWAY_CEILING` into the loop kit's definition with its readers, seen red with `unattended.sh` deleted; the catalogue row and a fates row follow | `retirement-inventory-misses-readers-by-value`, an instance |
| `orientation-card` | dWellOiledMachine retires the per-session card into the binding and re-points the write gate's reads and the card writer in the same unit; the plan's pocket and `[chain]` rows | `retirement-inventory-misses-readers-by-value`, an instance |
| `root-stand-ins` | dTotalRecall stands the README or the claim commit in as the root, and Made-by in as the owner or the lease, until dWellOiledMachine's intake and binding kinds drain them | `step-depends-on-a-later-build`, an instance |
| `door-list` | `[doors]` lists every writer once, in the registry's writer column, and the one-door check reads it, seen red on an unlisted writer and green on a lease | `two-answers-to-one-question`, an instance |
| `salted-undefined` | `salted` defined: a keyed hash of the session id in `Gov-Session`, its key a per-node salt in the credential store, the binding holding the digest, a raw id or a mismatch refused (SA-4) | `policy-value-with-no-route`, an instance |
| `values-without-route` | `commit-msg`'s hook arm (dWellOiledMachine), `refuse` and `accept-loss` (dShippedRelease), `salted` (SA-4) and `retag`'s step (dTotalRecall), each seen on a plant | `policy-value-with-no-route`, an instance |
| `p35-states` | the act record's `transcript=` pointer, and `gov trace` rows filled, `not-local` or `pruned`, each seen on a fixture event | `rule-stated-with-no-check-that-fails`, an instance |
| `reads-writes-sites` | `reads` and `writes` declared at the role definitions and the items; the registry renders its readers under render parity and names the door | `two-answers-to-one-question`, an instance |
| `p33-addresses` | P33's three address forms, the native-id classes registered with their owners, and acts and sessions read beside the per-tree index from the binding records | the edge check's one edge per address form |
| `edge-grammar` | one `**Edges:**` line per type, a target holding no space, comma or bracket, a section target written `<doc>#<seg>` | the grammar arms; `two-answers-to-one-question`, an instance |
| `p34-rationale-owned` | dOrderedCharter's practice clause gains rationale apart with render parity, `one-owner` as its own check, and `retired` over sections | `rule-stated-with-no-check-that-fails`, an instance |
| `p37-legs-missing` | dWitnessedBar's portability pack gains path, temp-file and quoting arms, each seen red | `rule-stated-with-no-check-that-fails`, an instance |
| `p37-encoding-optional` | gate-lint's Python text-IO scan and shell-hygiene mode move into the core pack, and the fates rows follow | `core-depends-on-an-optional-part`, an instance |
| `cycle-walk` | dConvergedCharter walks the cycle by key from a planted build's intake; the plan's `[gates]` and `[chain]` name it | the walk; `rule-stated-with-no-check-that-fails`, an instance |
| `kickoff-skill-link` | dConvergedCharter retires `/session-kickoff` and its link once the scout and `kickoff.runs` land, with a reader inventory, a stub and a preflight report; `gap-orient-21` and two fates rows (SA-9) | `retirement-inventory-misses-readers-by-value`, an instance |
| `help-docs` | dConvergedCharter renders `help/` from each user-facing unit's `usage` field, with render parity and a docs leg; a pocket, a fates row and `gap-found-27` (SA-5) | the docs leg; `rule-stated-with-no-check-that-fails`, an instance |
| `fates-population` | convergence's exit derives its population from `git ls-files`, red on an unlisted file; rows for `help/` and `.claude/roles.json` | the derived-population arm |
| `transcript-retention` | the pocket rows say the retention is the node's; dWellOiledMachine's fixture measures it, and preflight warns when it is shorter than `runtime.journal` | `fixture-inherits-ambient-machine-state`, an instance |
| `bash-resolver-seam` | dWitnessedBar's resolver is extracted from `profile_bar.resolve_bash` and govkit's, keeps `GOV_BASH`, accepts a candidate only once it runs, and replaces every resolver a query finds | `two-answers-to-one-question`, an instance |
| `trailer-readers` | dDeclaredLoop's one reader offers the union and the replace views, each consumer naming its own, the three readers re-pointed in one unit with a before-and-after parity run | `two-answers-to-one-question`, an instance |
| `trace-model` | `gov trace` re-points runlog's `build_run_model` to the one index, one timeline engine | `core-depends-on-an-optional-part`, an instance |
| `retired-edited` | `retired-edited` is a receipt state of its own on the existing grid cell, with its own role rows; the catalogue row moves to dSafePassage | selfcheck arm 7g covers the state |
| `finder-two-builds` | dTotalRecall owns `record find`, reshaping `query.py` and `check-recall`; memory-recall keeps its why-search; the plan's recall index and the fates rows follow (SA-6) | `two-answers-to-one-question`, an instance |
| `selector-two-builds` | dFurnishedOrders' field through `gotchas.py --for-paths`; dLinkedLibrary's clause struck (SA-7) | `two-answers-to-one-question`, an instance |
| `window-before-releases` | windows count from the first cut release, every earlier shim held, and the release-0 fixture holds an untagged history (SA-8) | the fixture case; `step-depends-on-a-later-build`, an instance |
| `lander-commits` | the lander is a commit site of its own, its commits carrying `Gov-*` trailers from its binding; `[sites]` and `[doors]` | `invariant-held-on-one-admission-path`, an instance |
| `codex-retrust` | preflight refuses a Codex launch while a wired hook's hash is untrusted, and `update` and `kits.offer` re-surface the trust | the one-byte probe; `invariant-held-on-one-admission-path`, an instance |
| `off-node-bindings` | every act's minimal binding record pushed to `refs/gov/bindings`, read by four checks on any node over a declared range, a missing one `not-local` and never passed (SA-10) | the three-node fixture; `absence-read-from-one-of-several-homes`, an instance |
| `empty-sets` | every set-valued key says whether it may be empty, and the schema refuses an empty value where it may not, seen red on seven keys, and a key with no rule | the schema arm; `vacuous-selector-empty-population`, an instance |
| `released-steps-frozen` | a step row landed on the default branch is frozen, a correction a new step and a removal a `[[retired]]` row, dWitnessedBar's append-only population holding them | `shipped-checker-edit-is-an-adopter-contract-change`, an instance |
| `step-contract` | the step kind's isolation contract, `needs-target` checked under it, and step processes a ninth spawn kind | `foreign-code-runs-on-the-ambient-credential`, an instance |
| `emitted-ci-pins` | emitted `uses:` pinned by full sha from one declaration, least-privilege permissions, and a leg red on a tag pin | `invariant-held-on-one-admission-path`, an instance |
| `refs-owner` | the refs row split by family: claims and leases dPlacedRequest, mail dKeptSession, bar-red dWitnessedBar, bindings dWellOiledMachine | `two-answers-to-one-question`, an instance |
| `gitdir-pockets` | rows for the drift history, the sidecars, `pre-push-allow` and the lookups log, and the git-dir rows joined to a listing | the listing join |
| `deploy-toml-pocket` | a pocket row for `.governance/deploy.toml`, and dGroundRules' minimal guard covers it (SA-12) | the minimal guard |
| `region-parsers` | dLinkedLibrary's population derived by query, and `gap-mem-33` names the missed two | `predicate-designed-without-a-run-over-the-tree`, an instance |
| `unattended-inventory` | dConvergedCharter's retirement inventories the kit's readers by path and by value, and the spawn-budget leg runs without the kit; dOrderedCharter's agent-instructions move does the same | `retirement-inventory-misses-readers-by-value`, an instance |
| `policy-values-owner` | the pocket's owner is dGroundRules, the presets dKeptSession's | `two-answers-to-one-question`, an instance |
| `act-key-session` | the session id preset or taken from the start event, the act `session: pending` until then, and a lost start event failing the launch | the Codex conformance row |
| `receipt-schema` | the back-fill pinned below schema 3, the receipt's readers inventoried by value, and the bump an upgrade step with a down | `retirement-inventory-misses-readers-by-value`, an instance |
| `supervisor-restart` | a restarted supervisor reconciles before its first beat, re-adopting or killing every act under its lease | the fencing fixture; `invariant-held-on-one-admission-path`, an instance |
| `answers-no-clause` | AP-4 on dTotalRecall's README schema and AP-16 in dWellOiledMachine's conformance fixture, each with a planted red | `rule-stated-with-no-check-that-fails`, an instance |
| `promotion-node-local` | the promotion arm is a node-scoped reading in Maintain, filed as an ask, never a bar or push leg | `fixture-inherits-ambient-machine-state`, an instance |
| `scoutedseam-branch` | dFairHearing takes the grader, cases, results and judge by blob from `b0fe68f30`, never waited on, and proves the factory over committed results; dLinkedLibrary's re-run needs the two adopter clones and names a missing one | `spec-names-code-its-base-lacks`, an instance |
| `replay-scorers` | dTotalRecall's, dLinkedLibrary's and dCalibratedLens' replays score through dFairHearing's factory, and a second scorer reds | the second-scorer arm |
| `ledger-driver` | the ledger merges through `merge-rows.py`, its postconditions extended and the append-collision case run | `two-answers-to-one-question`, an instance |
| `kind-factory-dup` | dTotalRecall's registry is the record-kind factory, its gate landing with it; dConvergedCharter keeps every kind on it | `two-answers-to-one-question`, an instance |
| `credential-homes` | gov reads and copies no credential file, each credential's home is named per platform, and the fixture runs against the real store on each platform | the per-platform fixture run |
| `intake-ratification` | each intake marks its origin, and only owner-origin intake ratifies; an act's intake is seen not to pass Plan's exit | `inputs-inside-the-subjects-reach`, an instance |
| `code-record-bounds` | the `code` record's exclusions, per-file cap and time ceiling, re-timed on an adopter-scale fixture; `[owed]` | the adopter-scale fixture |
| `malformed-spans` | four span arms in the annotations leg, each seen red on a planted file | the span arms |
| `declined-retirement` | a declined retirement amends its part's row through the ratification record, and the exit join reads the amended row | `owner-item-without-its-reject-outcome`, an instance |
| `live-questions` | dKeptSession's live owner questions join when dFurnishedOrders lands them | `step-depends-on-a-later-build`, an instance |
| `pass-edge-tallies` | `Pass:` declared for `serves`, and `[frame]`'s hop tally restated from `[cycle]` | `two-answers-to-one-question`, an instance |
| `p3-ground` | P3's ground restated: remote CI runs after the fact and blocks nothing | none fits; a principle's ground is re-probed at each full audit |
| `map-lib-window` | the re-export bound to `install.deprecation-window`, and the shim covering a moved module import | `amendment-leaves-its-other-half-standing`, an instance |
| `backfill-owner` | `[migration]` and `[integration]` say no step writes under the default, and dTotalRecall's retag step under `retag` | `policy-value-with-no-route`, an instance |
| `floor-query` | dSafePassage's floor reader and `gap-tool-22` name a query for every floor statement | `predicate-designed-without-a-run-over-the-tree`, an instance |

## [folded] Every defect folded, 2026-10-19

All 66 confirmed defects and the twelve answers are folded, in one commit:
- **v2:** P3, P33 and P38; the catalogue's empty-set rule over every set-valued key, and the
  `review.design.round-count`, `trace.identity`, `install.deprecation-window`, `install.retired-edits`,
  `runtime.act-auth` and `policy.proof` rows; `[witnesses]`; eighteen chain rows; `[planned]`, `[open]` and `[owed]`;
  and a revision note.
- **The memory plan:** `[frame]`, `[families]`, `[pockets]` (the refs split by owner, six rows added and two owners
  corrected), `[practice]`, `[sites]`, `[edges]`, `[doors]`, `[integration]`, `[chain]`, `[migration]`, `[gates]` and
  `[keys]`.
- **The gap register:** `gap-deploy-25`, `gap-found-27` and `gap-orient-21` added, `gap-mem-33` and `gap-tool-22`
  restated, `gap-deploy-18`, `gap-deploy-19` and `gap-deploy-20` moved to dSafePassage, and the tally re-measured.
- **The fates record:** five rows added, the kickoff, finder, write-gate, runlog and gate-lint rows amended, the
  counts re-derived from the table, `[stale]` and the limits of `[check]`.
- **Nineteen bug classes** carry the instances, and `gotchas.py --write` re-renders their index.

The reconciliation probe reddened once on the fold, with eight UNCLASSED findings: dGroundRules' empty-set clause
named seven keys later builds own, and dWellOiledMachine's credential clause named `platforms.supported`,
dShippedRelease's. Both clauses now say what they check without naming a later build's key, and the probe reads
no finding.

The floor-statement query that `gap-tool-22` and dSafePassage's floor reader name, and what it finds today:

```text
$ git grep -nE 'py ?[>≥]=? ?3\.[0-9]+|Python ?>= ?3\.[0-9]+|CPython 3\.[0-9]+\+' -- ':!memory'
tools/codebase-map/map_lib.py:17:Python >= 3.11 (tomllib).
tools/govkit/check_runbook_parity.py:34:    sys.stderr.write("runbook-parity: needs tomllib (CPython 3.11+)\n")
tools/govkit/govkit.py:108:        "govkit: this tool needs tomllib (CPython 3.11+). The descriptors are TOML and there is no\n"
tools/settings-merge.py:3:Stdlib only (json, argparse, pathlib); py>=3.10 (write_text newline=).
```

The chain, recomputed, 381 planned units in all:

```text
critical path: 206 units, dGroundRules > dSafePassage > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dSafePassage 19, dFairHearing 31, dOrderedCharter 50, dDeclaredLoop 73, dPlacedRequest 81, dKeptSession 100, dWitnessedBar 100, dBoundRoles 118, dTotalRecall 120, dRankedPlan 133, dFurnishedOrders 136, dLinkedLibrary 143, dIndexedDesign 155, dWellOiledMachine 159, dScopedBuild 170, dTendedCadence 175, dMindYourWords 176, dShippedRelease 183, dCalibratedLens 187, dConvergedCharter 206
```

The path grows by ten units: four in dSafePassage (the isolation contract, gov first, the recovery moved from
dShippedRelease, and the step gate), one in dTotalRecall (its own steps), two in dWellOiledMachine (the card's
retirement and the binding records) and three in dConvergedCharter (`help/`, the kickoff's retirement and the cycle
walk). dBoundRoles gains its steps off the path; dShippedRelease loses the moved clause, and dLinkedLibrary its
selector.
