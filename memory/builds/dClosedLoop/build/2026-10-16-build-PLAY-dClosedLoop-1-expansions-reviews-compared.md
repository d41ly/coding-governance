# Research: the expansion round's two Tier-2 reviews, compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked for the expansion round's Tier-2 review twice: "go ahead with the Tier-2 review,
twice" (the session log's `Events`, 2026-10-16). This record compares the two runs defect by defect,
sets them beside the five core layers' rounds, and plans the fold. Two defects turn on a choice the
records leave open, so they go to the owner first, in `[forks]`.

## [runs] The two rounds

- **Subject:** the round's six commits, `ee2eee68e..f56e80fee`, read as a diff without the atlas page
  and its generator.
- **Harness:** `tools/workflows/tier2-review.js` at full intensity: five lenses (`gov-diff-reviewer`),
  five skeptic batches (`gov-skeptic`) and one synthesis (`gov-synthesizer`), every role at high, the
  closing-review roles' declared effort.
- **Runs and reports:**

  | Run | Workflow run | Dispatch | Report |
  |---|---|---|---|
  | A | `wf_644d225b-42a` | 57 | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md` |
  | B | `wf_3a59e7c4-201` | 58 | `reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-b.md` |

- **The args:** layer-expansions `[review]` holds run A's, verbatim. Run B's differ only in the run
  label and the report path. Run B started once run A returned, so no more than five agents ran at once.
- **The ledger:** the roles kit derived every agent and returned line, and the session log holds them.

## [method] How the rounds were compared

The comparison of layers 1 to 4 (`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`,
`[method]`) applies unchanged:
- every finding of both runs, confirmed or refuted, is placed on the defect it names;
- a finding that names two defects lands on both, its main defect first;
- a run finds a defect when one of its findings on it was confirmed;
- the defect takes the highest grade any confirmed finding on it got, the skeptic's where one was given.

The script is unchanged too: `[compare]` in that comparison's instruments record, byte for byte, run
over this record's one map, `[map]`. The map places all 99 findings on 49 defects.

## [summary] The two runs, beside the five core layers

| Rounds | Findings A / B | Confirmed A / B | Precision A / B | Out A / B |
|---|---|---|---|---|
| the expansion round | 45 / 54 | 37 / 46 | 0.82 / 0.85 | 244.9k / 278.9k |
| the five core layers | 285 / 266 | 249 / 232 | 0.87 / 0.87 | 1188.3k / 1193.9k |

| Rounds | Defects | Both | A only | B only | A alone covers | B alone covers | Overlap | Chapman: found by neither | High defects | High, one round only | Shared, graded alike | Refuted, with a confirmed twin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| the expansion round | 38 | 20 | 5 | 13 | 66% | 87% | 0.53 | 3 | 8 | 2 | 13 of 20 | 5 of 16 |
| the five core layers | 265 | 130 | 65 | 70 | 74% | 75% | 0.49 | 35 | 29 | 6 | 97 of 130 | 40 of 70 |

- **Out** sums each run's returned lines, the resume probe included. The reports' own counts are
  215.0k and 294.0k, over the eleven agents each names.
- The five core layers' row is the earlier comparison's `[summary]`, and every column means what it
  meant there.

## [patterns] What the comparison shows

- **Run B found a third more than run A.** Alone, B covers 87% of the 38 defects and A 66%. That is
  the widest split of any pair so far: the five core layers' rounds covered 69% to 82%. B's correctness
  lens found five of its thirteen B-only defects.
- **Both high defects that one run missed are security defects, and run B found both.**
  - `pin-closure`: the trust pin covers the workflow file, not the bar the workflow runs.
  - `offer-runs-adopter-code`: an unattended offer runs adopter-authored code on gov's ambient
    credential.
  - A's security lens raised nine findings and kept five. B's raised four and kept all four.
- **The skeptics split on three defects.** On `maintain-owns-unread`, A20 was confirmed and B30
  refuted. On `core-points-gap-rows`, A26 was refuted and B41 confirmed. Within run B, B54 was
  confirmed and B32 refuted on `naming-collisions`. The fold takes the confirmed reading, as `[method]`
  says.
- **The library round's class bit again, seven times.** `policy-value-with-no-route` was on both runs'
  checklist. Seven defects belong to it: `release-hold-unrouted`, `empty-environments-close`,
  `maintain-owns-unread`, `velocity-values-unrouted`, `distribution-values-unrouted`,
  `integrations-values-unrouted` and `verdict-remote-ci-value`. Its fix walks each preset through the
  transition table, and the settlement ran no such walk.
- **P28's direction broke behind a guard.** Four defects make the core depend on an optional part:
  `absent-clause-refuses-presets`, `lexicon-signals-core`, `grant-enforcement-owner` and the fallback
  half of `ci-red-unpublished`. Each read as degrading safely, through a guard or an Absent clause.
- **One run's claim was recorded as both runs'.** `date-claim-attribution`, `literal-list-attribution`
  and `peer-node-two-owners` each rest on a claim one research run made.

## [fold] The fold plan

Each defect takes one of the layers comparison's dispositions: amend, gap, fork or none. Five rules
bound the fold:
- **Amend in place, under a dated revision.** layer-expansions gains `[revised]`, which names each
  defect and where its fix sits. flow-steps, layer-runtime, layer-memory and v2 each gain a dated line.
- **v2 and the register move in the same pass.** The gap-ownership join and the preset check run
  again.
- **A rename sweeps every current record.** Dated records keep the old names: the research returns,
  revision notes, `[settled]` and the session log's past entries. The fold renames:
  - `release.cadence` to `kits.cadence`, so `release.*` stays integrations';
  - the key `maintain.record` to `maintain.record-when`, so the item keeps its name;
  - `maintain.detector-admission` to `maintain.reading-admission`, the design's word;
  - `integrations.secret-home` and `integrations.secret-scan` to `runtime.secret-home` and
    `runtime.secret-scan`, because the grant they enforce is Runtime's field;
  - the item `deploy.version` to `kits.version`, since the slot moves into Test.
- **A defect with no catalogue class gets one.** The new classes are filed under `memory/gotchas/` and
  claimed in the build method's dossier.
- **The fold gets its own review.** Fold text is unreviewed surface, so one light diff review runs
  over the fold's commits, as dispatch 47 did for the layers' fold.

`[folded]` names each defect's fix, where it sits, and its class.

## [forks] Asked, 2026-10-16

Each option becomes an allowed value of a new key, and the answer is its default.

**RH-1. "Under `build.closes: after-release-verifies`, what waits for the release?"** This decides
`release-hold-unrouted`. Run A's skeptic held the leases and the close, and run B's held the close
alone. The key is `build.release-hold`.
- **Only the close (Recommended).** `deploy.unlease` runs at landing, so the build's leases and mailbox
  free up and other builds can take its paths. The build stays open until a release record verifies
  its SHA, or a later SHA that contains it, and the close records the outcome.
- **The whole close.** The card, the leases and the mailbox stay held until the release verifies, and
  the supervisor renews the leases, as for a paused build. No other build can lease the build's paths
  while an approval waits.

**PIN-1. "What does the remote verdict's pin cover?"** This decides `pin-closure`. Run B found that
the workflow runs the bar from the tree it judges. The key is `verdict.remote.pin-scope`.
- **The workflow file, its guarantee stated (Recommended).** The pin covers `remote-ci.yml`. A remote
  verdict then witnesses that the landed tree's own bar passed on a clean host. That is the guarantee
  the local hook gives on the node, and it never claims the bar is independent of the pusher. A change
  to the bar is reviewed as any change is.
- **The bar's dispatch closure.** The pin covers `remote-ci.yml`, `tools/run-gates/run-gates.sh`,
  `tools/gate-legs.json` and `.githooks/gate-env.sh`. Any change to them needs the owner's re-pin
  before a remote verdict stands again, so under `ci` most kit builds wait on the owner.

## [answers] Answered, 2026-10-16

The owner took the recommended option on both forks. Verbatim:
- **RH-1:** "Only the close (Recommended)".
- **PIN-1:** "Workflow file, guarantee stated (Recommended)".

| Fork | Answer | Key | Default | Also allowed |
|---|---|---|---|---|
| RH-1 | Only the close | `build.release-hold` | `close-only` | `whole-close` |
| PIN-1 | Workflow file, guarantee stated | `verdict.remote.pin-scope` | `workflow` | `dispatch-closure` |

Their non-default preset values were assigned by analogy: `strict`, the maximum-assurance preset, selects
`whole-close` and `dispatch-closure`, and the other three presets take the defaults.

## [folded] Where every map row went, 2026-10-16

Each defect's fix sits in place, under the dated revision line of the record named. A defect's class
is a record under `memory/gotchas/`.

| Defect | Disposition | Where the fix sits | Its class |
|---|---|---|---|
| `release-hold-unrouted` | fork, amend | RH-1; flow-steps' `deploy.released` and `[transitions]`; layer-expansions' release program and `release.record`; v2's `build.release-hold` | `policy-value-with-no-route` |
| `empty-environments-close` | amend | flow-steps' `build.closes` values and Deploy's policy list; layer-expansions' integrations Absent; v2's paragraph on `strict` and `guarded` | `policy-value-with-no-route` |
| `release-pick-key` | amend | layer-expansions' release program and `release.pick`; `deploy.released` reads a SHA that contains the build's own | `two-answers-to-one-question` |
| `verify-failed-no-producer` | amend | layer-expansions: `release.route` ends in `release.record`, and the slot's exit record produces `release-verify-failed` | `route-names-an-output-its-actor-never-emits` |
| `maintain-owns-unread` | amend | layer-expansions' Maintain: the event run and the release reading under `at-landing-maintain-owns`; flow-steps' `build.closes` values | `policy-value-with-no-route` |
| `absent-clause-refuses-presets` | amend | layer-expansions' distribution Absent; v2's `policy.on-missing-expansion` row | `core-depends-on-an-optional-part` |
| `peer-node-two-owners` | amend | layer-expansions' `[core-points]`, kinds and engine kits; flow-steps' Test extension points | `one-run-claim-recorded-as-agreed` |
| `version-slot-step` | amend | flow-steps' `test.merge` and Test extension points; layer-expansions' `kits.version`; `gap-deploy-11` | `two-answers-to-one-question` |
| `cadence-host-key` | amend | layer-expansions' distribution items and keys; layer-runtime `[schedule]`; v2's `kits.host` and `kits.watch-cadence` | `route-names-an-output-its-actor-never-emits` |
| `journal-key-owner` | amend | layer-runtime `[policies]`, `[schedule]` and `[tests]`; layer-expansions' observability keys | `amendment-leaves-its-other-half-standing` |
| `velocity-values-unrouted` | amend | layer-expansions' `maintain.lease`, `maintain.read`, registration, `loop.gather` and the run record; `maintain.reading-admission` | `policy-value-with-no-route` |
| `distribution-values-unrouted` | amend | layer-expansions' `kits.cut`, `kits.currency`, `kits.fleet` and the `currency` leg; flow-steps' leg packs | `policy-value-with-no-route` |
| `integrations-values-unrouted` | amend | layer-expansions' witness-rule arms, `release.approve`, `release.promote` and the release paragraph; flow-steps' release slot | `policy-value-with-no-route` |
| `pin-closure` | fork, amend | PIN-1; layer-expansions' witness rule; `gap-test-11`; v2's `verdict.remote.pin-scope` | `inputs-inside-the-subjects-reach` |
| `workflow-pin-home` | amend | layer-expansions' pin paragraph; v2's `verdict.remote.pin`, which presets never touch | `inputs-inside-the-subjects-reach` |
| `ci-red-unpublished` | amend, gap | layer-expansions' remote verdict; flow-steps' core re-check (K1); `gap-deploy-10` | `route-names-an-output-its-actor-never-emits` |
| `bar-red-witness` | amend | layer-expansions' observability line and events: the per-SHA verdict is the witness, the ref its index | `two-answers-to-one-question` |
| `verdict-remote-ci-value` | amend | layer-expansions' remote verdict; flow-steps' Test bullets and extension points; `gap-test-02` | `policy-value-with-no-route` |
| `offer-runs-adopter-code` | amend, gap | layer-expansions' `kits.offer`; `gap-deploy-13`; v2's dShippedRelease row | `foreign-code-runs-on-the-ambient-credential` |
| `grant-enforcement-owner` | amend | layer-runtime `[extend]` and `[policies]`; layer-expansions' grants; v2's `runtime.secret-home` and `runtime.secret-scan` | `core-depends-on-an-optional-part` |
| `secret-scan-population` | amend | layer-runtime `[extend]`: the secret value scan's population | `zero-witness-over-an-unnamed-population` |
| `secret-scan-zero` | amend | layer-runtime `[extend]`: the secret value scan's witness | `zero-witness-over-an-unnamed-population` |
| `lexicon-signals-core` | amend, gap | layer-expansions' observability line and Absent; flow-steps' leg packs; `gap-maint-09`, `gap-lex-08` | `core-depends-on-an-optional-part` |
| `loop-file-key` | amend | layer-expansions' `loop.file`, and `[design]`'s idempotence rule | `append-without-an-idempotence-key` |
| `seen-row-key` | amend | layer-expansions' `maintain.file` | `append-without-an-idempotence-key` |
| `date-claim-attribution` | amend | layer-expansions' `[cross]` and `[gaps-proposed]`; `gap-test-12` | `one-run-claim-recorded-as-agreed` |
| `literal-list-attribution` | amend | layer-expansions' `[cross]` | `one-run-claim-recorded-as-agreed` |
| `extend-split` | amend | layer-runtime `[extend]` | `amendment-leaves-its-other-half-standing` |
| `record-unbound` | amend | the seven records' Serves lines, in `f1c2cb0f3` | `record-without-serves-or-with-a-round-counter` |
| `cut-decline-route` | amend | layer-expansions' `kits.cut` | `owner-item-without-its-reject-outcome` |
| `key-schema-split` | amend | layer-expansions' key tables state v2's values | `two-answers-to-one-question` |
| `journal-floor-prose` | amend | v2's pair rule in `[presets]`, and dDeclaredLoop's row | `rule-stated-with-no-check-that-fails` |
| `ex1-unchecked` | amend, gap | v2's dOrderedCharter row; `gap-found-17` | `rule-stated-with-no-check-that-fails` |
| `core-points-gap-rows` | amend | `gap-test-02`, `gap-deploy-01`, `gap-rt-15` and `gap-deploy-11` widened | `amendment-leaves-its-other-half-standing` |
| `spine-07-evidence` | amend | `gap-spine-07` reworded, in the register and `[gaps-proposed]` | `amendment-leaves-its-other-half-standing` |
| `tool-02-undercount` | amend | `gap-tool-02`: five lockstep checks, selfcheck's arm 5c among them | `amendment-leaves-its-other-half-standing` |
| `source-receipt-route` | amend | layer-expansions' `kits.currency`, `install.from` and receipt integrity | `route-names-an-output-its-actor-never-emits` |
| `naming-collisions` | amend | `kits.cadence`, `maintain.record-when` and `maintain.reading-admission`, across v2, flow-steps and layer-expansions | `two-answers-to-one-question` |
| `env-injected-reach` | none | refuted; the map's row gives the reason | — |
| `owner-answer-channel` | none | refuted; the map's row gives the reason | — |
| `fleet-field-validation` | none | refuted; the map's row gives the reason | — |
| `extend-fields-missing` | none | refuted; the map's row gives the reason | — |
| `record-home-attribution` | none | refuted; the map's row gives the reason | — |
| `tag-order` | none | refuted; the map's row gives the reason | — |
| `ex3-record-rate` | none | refuted; the map's row gives the reason | — |
| `gov-currency-arm-unexercised` | none | refuted; the map's row gives the reason | — |
| `ex3-fixtures` | none | refuted; the map's row gives the reason | — |
| `di1-planned-unit` | none | refuted; the map's row gives the reason | — |
| `tool-07-owner` | none | refuted; the map's row gives the reason | — |

- **The left-shift.** Five classes are new: `core-depends-on-an-optional-part`,
  `foreign-code-runs-on-the-ambient-credential`, `zero-witness-over-an-unnamed-population`,
  `one-run-claim-recorded-as-agreed` and `rule-stated-with-no-check-that-fails`. The build method's
  dossier claims them. `policy-value-with-no-route` and `route-names-an-output-its-actor-never-emits`
  record this round's hits. No gate fits a design record's prose, so each new class names the chain
  build that owes its gate.
- **Two gaps join the register,** `gap-deploy-13` (dShippedRelease) and `gap-lex-08`
  (dMindYourWords). Nine take added facts, and two are corrected.
- **The checks, run again on the folded records:** the preset check (153 keys, 143 presettable, 143
  preset rows, no findings), the gap-ownership join (193 keys over 15 builds, none unowned or owned
  twice), the role matrix (75 items, 0 findings) and `gotchas.py --check` (exit 0).
- **Still owed:** the fold's own closing review, dispatched as `[fold-review]` says.

## [fold-review] The fold's closing review, dispatched 2026-10-16

- **What runs.** Dispatch 59: one light Tier-2 diff review over the fold's two commits, `3fccdd78a..6e0ce0a55`, as the
  layers' fold had (dispatch 47). Three lenses, batched skeptics and one synthesis run at the
  closing-review roles' declared effort.
- **What it reads.** The two review reports ride as specs, so a lens can hold each fix against its
  finding. The diff leaves them out, with the atlas and the generated files.
- **The report:** `reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`.

Its args, verbatim:

```json
{
 "kind": "diff-review",
 "base": "3fccdd78a61099791d52794f4708767b62ae2ca2",
 "head": "6e0ce0a5541f255b4cfddc692c4ffac539a29c5e",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "intensity": "light",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "high",
  "skeptic": "high",
  "synthesis": "high"
 },
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
  "memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md",
  "memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-b.md",
  "memory/gotchas/core-depends-on-an-optional-part.md",
  "memory/gotchas/foreign-code-runs-on-the-ambient-credential.md",
  "memory/gotchas/zero-witness-over-an-unnamed-population.md",
  "memory/gotchas/one-run-claim-recorded-as-agreed.md",
  "memory/gotchas/rule-stated-with-no-check-that-fails.md"
 ],
 "context": "The diff is the fold of the expansion round's two Tier-2 reviews, in build dClosedLoop, a design-only build that re-architects gov onto one loop. This is the fold's closing review: fold text is unreviewed surface. The diff holds two commits. f1c2cb0f3 files the two review reports, compares them defect by defect in memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md ([runs], [method], [summary], [patterns], [fold], [forks], [map] and [instrument]), and adds the Serves line seven of the build's records lacked. 6e0ce0a55 folds: the owner answered the comparison's two forks, RH-1 \"Only the close (Recommended)\" and PIN-1 \"Workflow file, guarantee stated (Recommended)\", and the fold amended layer-expansions (its design and a new [revised]), flow-steps (Test's backends and version slot, Deploy's new deploy.released item, the release slot's exit record, [transitions], [expansions]), layer-runtime ([extend], [schedule], [contract], [policies], [tests]), layer-memory, layer-roles' derived matrix, v2 ([policies], [presets], [chain] and a dated revision) and the gap register (gap-deploy-13, gap-lex-08, widened and corrected rows, a re-measure block), and filed five classes under memory/gotchas/, claimed in memory/map/features/build-method.md. The comparison record's [answers] and [folded] say where each of its 49 map rows went. The two review reports, memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md, memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-b.md, are handed in as specs so a fix can be checked against its finding; they are not under review. Read the diff without them, the atlas and the generated files: git -C C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 diff 3fccdd78a61099791d52794f4708767b62ae2ca2...6e0ce0a5541f255b4cfddc692c4ffac539a29c5e -- . ':(exclude)memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md' ':(exclude)memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-b.md' ':(exclude)memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html' ':(exclude)memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py' ':(exclude)memory/map/generated' ':(exclude)memory/gotchas/INDEX.md' ':(exclude)memory/builds/dClosedLoop/README.md'. Review for five things: (1) a confirmed finding of either run that the fold left unfixed, fixed only in part, or fixed in a way its own text contradicts, against [folded]'s claim; (2) a defect the fold itself introduced: an item, route, witness, key, value or record kind with no producer, no arm or no home, a rename one current record still misses, or one fact now stated two ways; (3) a settled answer misapplied: RH-1, PIN-1, EX-1 to EX-3, DI-1 or LR-4; (4) text wrong about the tree: a seam, file, line, key, check or count that does not exist or says otherwise; (5) a new bug class that misstates where it bit or what fixes it. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds, as layer-expansions [open] says.\n- The owner's settled answers (RH-1, PIN-1, EX-1 to EX-3, DI-1, and the earlier KN-1, LB-1 to LB-4, F*, R-*, RT-* and LR-*) are decisions: a finding may show one contradicts a record or the tree, but does not re-argue the owner's choice.\n- The non-default preset values of the new keys were assigned by analogy: a finding may show one inconsistent with its preset, not that it is unasked.\n- Renames sweep current text only. Dated records keep the old names: the research returns, layer-expansions' [forks], [settled] and [review], every revision note, flow-steps' [revised] history, and the session log's past entries. [agreement]'s \"Both runs\" cells keep what the runs said.\n- A refuted finding stays refuted: the map's none rows carry the skeptic's reason.\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.",
 "checklist": "# recurring-bug-class checklist for 3fccdd78a..6e0ce0a55 (30 changed file(s))\n# 19 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 11 path · 4 directory · 4 basename; a cut tier prints one line per class\n# invariants are read at 3fccdd78a610; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] policy-value-with-no-route (path)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] core-depends-on-an-optional-part (path)\n      a core item, leg, field or preset cannot run, or cannot be enforced, without an expansion or an optional component, and the dependency hides behind the guard or Absent clause that seems to degrade it\n      memory/gotchas/core-depends-on-an-optional-part.md\n\n- [ ] foreign-code-runs-on-the-ambient-credential (path)\n      an unattended item runs code another repository authored, on the node's whole environment and ambient credential, so that repository's committers gain the node's rights\n      memory/gotchas/foreign-code-runs-on-the-ambient-credential.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] zero-witness-over-an-unnamed-population (path)\n      a scan whose zero is the witness names no population, so a skipped scan and a scan over less than the guarded boundary publishes both read as clean\n      memory/gotchas/zero-witness-over-an-unnamed-population.md\n\n- [ ] append-without-an-idempotence-key (path)\n      a command that appends to an append-only record declares no key, so a retried run writes the same row twice and a set-join witness stays green\n      memory/gotchas/append-without-an-idempotence-key.md\n\n- [ ] insert-after-a-key-that-occurs-twice (path)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] one-run-claim-recorded-as-agreed (path)\n      a comparison of two independent runs records a claim only one run made as what both found, so a single measurement carries the weight of agreement\n      memory/gotchas/one-run-claim-recorded-as-agreed.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] rule-stated-with-no-check-that-fails (path)\n      a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not\n      memory/gotchas/rule-stated-with-no-check-that-fails.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory) · memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] rate-quoted-without-its-denominator (basename) · memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename) · memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n"
}
```

## [map] Every finding, placed

Run A is `wf_644d225b-42a` and run B is `wf_3a59e7c4-201`. The ids are each report's appendix ids. A
finding that names two defects sits on both, its main defect first.

| defect | what | A | B | disposition |
|---|---|---|---|---|
| `release-hold-unrouted` | under `build.closes: after-release-verifies` no core item waits on the release, so the build closes at landing, and `release.record` routes to a `deploy.close` that has already run | 19, 11 | 19, 5, 44 | fork RH-1, amend |
| `empty-environments-close` | `strict` and `guarded` select `after-release-verifies`, while `release.environments` defaults to none and presets never set it, so no route closes the build | 31, 41 | 6, 19, 44 | amend |
| `release-pick-key` | the release program is keyed by (SHA, environment), yet `release.pick` takes the newest SHA the environment lacks, so an overtaken build's SHA never gets a record | 19 | 9, 19 | amend |
| `verify-failed-no-producer` | `release.record` runs only on a green verify, so the `release-verify-failed` event Maintain registers has no producer on the failure path | — | 7, 27 | amend |
| `maintain-owns-unread` | `build.closes: at-landing-maintain-owns` names Maintain, but no Maintain item reads the key or a closed build's release | 20 | 30 | amend |
| `absent-clause-refuses-presets` | distribution's Absent clause refuses any preset naming `release.cadence` or `deploy.currency`, which every shipped preset names, while the canonical rule refuses by value | 21 | 20, 45 | amend |
| `peer-node-two-owners` | `peer-node` is a core backend in dWitnessedBar's cell and P3, and also an integrations adapter on integrations B's claim alone | 12, 27 | 43 | amend |
| `version-slot-step` | the version slot is declared in Deploy, while the landing's prepare is Test's `test.merge`, which still mints | 30, 40 | 21 | amend |
| `cadence-host-key` | the cadence-items point requires a host key and a period, and distribution's programs name no host key, two of them no period, and the Loop Review no host key | 17, 25, 35 | 25 | amend |
| `journal-key-owner` | `runtime.journal` is claimed by observability, missing from Runtime's key table and still listed as retired; `notify.channel` is missing from Runtime's tables | 15, 32, 43 | 28, 38, 53 | amend |
| `velocity-values-unrouted` | the values `velocity` selects for `maintain.reading-tree`, `maintain.node-readings`, `maintain.detector-admission`, `observability.run-record` and `review.loop.catch-source` have no arm in the items that read them | 22 | 22, 17 | amend |
| `distribution-values-unrouted` | `currency.on-behind: red`, `install.from: any-commit`, `deploy.currency: pull-only` and `release.cadence: every-landing` have no route | 13, 23 | 23, 16 | amend |
| `integrations-values-unrouted` | `verdict.remote.trust`'s other two values have no arm in the witness rule, no environment is marked production for `owner-approves-prod`, and no item reads `deploy.runs` | 2, 24 | 24 | amend |
| `pin-closure` | the trust pin covers the workflow file, while the workflow runs the bar from the tree it judges, so the pin is not the answer to a pusher certifying itself | — | 1 | fork PIN-1, amend |
| `workflow-pin-home` | the pinned workflow blob has no home, no writer and no mismatch route | 1 | 1 | amend |
| `ci-red-unpublished` | under `GATE_POST_MERGE=ci` a remote red never reaches `refs/gov/bar-red`, and the core names no fallback with integrations absent | — | 13, 26 | amend, gap |
| `bar-red-witness` | `refs/gov/bar-red` is called a witness, against the design's own rule that refs never witness | 6 | — | amend |
| `verdict-remote-ci-value` | `verdict` still offers `remote-ci` as the binding verdict, while the design reads remote CI after the landing only | — | 12 | amend |
| `offer-runs-adopter-code` | `kits.offer` runs an adopter's update unattended on gov's node, and govkit's update executes adopter-authored code with the ambient credential | — | 2 | amend, gap |
| `grant-enforcement-owner` | the grant is a core field on every adapter row, but its enforcement and its keys live only in integrations | — | 3 | amend |
| `secret-scan-population` | the value scan leaves out pushed history and the core's refs, and names no boundary it binds at | 4 | 4 | amend |
| `secret-scan-zero` | the value scan's zero cannot tell a clean scan from a skipped one | 36, 5 | — | amend |
| `lexicon-signals-core` | the two lexicon drift signals become core legs that import the optional lexicon component | 14 | 8, 47 | amend, gap |
| `loop-file-key` | `loop.file` has no idempotence key, so an undisposed proposal is asked again every week | 37 | 37 | amend |
| `seen-row-key` | `maintain.file`'s `seen` row has no key of its own | 38 | — | amend |
| `date-claim-attribution` | `[cross]` and gap-test-12 credit integrations B's 2026-10-13 14:03 claim to both runs | 16, 44 | 29, 46 | amend |
| `literal-list-attribution` | `[cross]` credits integrations B with the literal-list finding only integrations A measured | — | 51 | amend |
| `extend-split` | the `[extend]` insertion split the selector-keys bullet from its validation clause, and the list misses four keys that take registered names | 42, 18, 28, 34 | 15, 33, 42, 52 | amend |
| `record-unbound` | the round's design record carries no Serves line, and six other records of the build carried none before it | 10 | 14 | amend |
| `cut-decline-route` | `kits.cut` under `owner-cut` routes no decline | 9 | — | amend |
| `key-schema-split` | `maintain.dead-after` and `currency.max-behind` are enumerations in v2 and counts in the design | 29 | 31 | amend |
| `journal-floor-prose` | `runtime.journal` of at least `review.loop.window-days` is prose only, so an override can break it | 33 | 36 | amend |
| `ex1-unchecked` | no check can fail on EX-1's rule that one expansion never uses a point another declares | — | 35 | amend, gap |
| `core-points-gap-rows` | two core points "join" gap rows that were never widened, and two points have no row | 26 | 41 | amend |
| `spine-07-evidence` | gap-spine-07 cites v2 rows the same commit rewrote, so its evidence no longer shows the gap | — | 18 | amend |
| `tool-02-undercount` | gap-tool-02 keeps the lockstep count that `[agree-distribution]` calls an undercount | — | 50 | amend |
| `source-receipt-route` | DI-1's settled "source, 0 behind" has no arm in `kits.currency`, and `install.from` admits no source | — | 11 | amend |
| `naming-collisions` | `release.cadence` drives distribution's `kits.cut` against the three senses of "release", and `maintain.record` is both an item and a key | — | 54, 32 | amend |
| `env-injected-reach` | an `env-injected` secret's reach | 3 | — | none: `env-injected` names how a secret is delivered, and the process-only rule bounds its reach |
| `owner-answer-channel` | an owner's answer arriving through a notification channel | 7 | — | none: an owner's answer returns only through `next`, as `[agreement]` records, and a channel message is no owner proof |
| `fleet-field-validation` | the fields `kits.fleet` reads from each adopter's receipt, unvalidated | 8 | — | none: validating each field is the reader's unit-level detail, and the receipt is schema-versioned with an integrity gate |
| `extend-fields-missing` | the new adapter fields missing from `[extend]` | 39 | — | none: the bullet under `[extend]` names every new field |
| `record-home-attribution` | `[cross]` crediting observability B with the missing record home | 45 | — | none: observability B raised the missing home on its own |
| `tag-order` | `gov/v<date>.<n>` tags misordering past nine releases a day | — | 10 | none: `<n>` is an integer, and a version sort orders it |
| `ex3-record-rate` | EX-3's "about 30 records a month" misattributed | — | 34 | none: the option names B, and B's return uses the same words |
| `gov-currency-arm-unexercised` | DI-1 leaving gov's currency probe unable to exercise its over-the-bar arm | — | 39 | none: DI-1 says gov reads "source, 0 behind", and the owner chose it knowing B's objection |
| `ex3-fixtures` | EX-3's two arms owing fixtures no record names | — | 40 | none: `[settled]` owes each arm a fixture, and planned units are owed at the re-cut |
| `di1-planned-unit` | DI-1 recorded in no chain build's planned units | — | 48 | none: the answer is recorded in `[settled]` and in the receipt kind it declares |
| `tool-07-owner` | gap-tool-07 assigned to the wrong owner | — | 49 | none: the register assigns no owner until the chain opens |

## [instrument] The run

The comparison, run from the worktree root on this record:

```bash
python compare_rounds.py memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-b.md memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md wf_644d225b-42a wf_3a59e7c4-201
```

It printed:

```text
== runs
A: raw 45, confirmed 37, refuted 8, precision 0.82, high findings 1, agents 12, out 244.9k (sum of returned lines)
B: raw 54, confirmed 46, refuted 8, precision 0.85, high findings 5, agents 12, out 278.9k (sum of returned lines)
== defects
map rows 49, confirmed defects 38, refuted-only 11
both 20, A only 5, B only 13
A alone covers 25 of 38 (66%)
B alone covers 33 of 38 (87%)
overlap (Jaccard) 0.53
Chapman estimate of the population: 41.1, so about 3 found by neither
A only: maintain-owns-unread, bar-red-witness, secret-scan-zero, seen-row-key, cut-decline-route
B only: verify-failed-no-producer, pin-closure, ci-red-unpublished, verdict-remote-ci-value, offer-runs-adopter-code, grant-enforcement-owner, literal-list-attribution, ex1-unchecked, core-points-gap-rows, spine-07-evidence, tool-02-undercount, source-receipt-route, naming-collisions
== severity (a defect takes its highest confirmed grade per round)
high defects 8: release-hold-unrouted, empty-environments-close, release-pick-key, absent-clause-refuses-presets, peer-node-two-owners, pin-closure, workflow-pin-home, offer-runs-adopter-code
  release-hold-unrouted: A 3 B 3
  empty-environments-close: A 2 B 3
  release-pick-key: A 3 B 3
  absent-clause-refuses-presets: A 2 B 3
  peer-node-two-owners: A 2 B 3
  pin-closure: A 0 B 3
  workflow-pin-home: A 2 B 3
  offer-runs-adopter-code: A 0 B 3
shared defects graded alike 13 of 20
== lenses behind the defects one round alone found
A: security 2, verification 2, seams 1
B: correctness 5, security 3, intent 3, seams 2, verification 2
== refuted findings and their twins
A3 (env-injected-reach): confirmed twin none
A5 (secret-scan-zero): confirmed twin A36
A7 (owner-answer-channel): confirmed twin none
A8 (fleet-field-validation): confirmed twin none
A26 (core-points-gap-rows): confirmed twin B41
A34 (extend-split): confirmed twin A42, A18, A28, B15, B33, B42, B52
A39 (extend-fields-missing): confirmed twin none
A45 (record-home-attribution): confirmed twin none
B10 (tag-order): confirmed twin none
B30 (maintain-owns-unread): confirmed twin A20
B32 (naming-collisions): confirmed twin B54
B34 (ex3-record-rate): confirmed twin none
B39 (gov-currency-arm-unexercised): confirmed twin none
B40 (ex3-fixtures): confirmed twin none
B48 (di1-planned-unit): confirmed twin none
B49 (tool-07-owner): confirmed twin none
```
