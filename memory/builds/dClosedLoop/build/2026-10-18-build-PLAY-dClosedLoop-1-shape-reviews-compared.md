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
