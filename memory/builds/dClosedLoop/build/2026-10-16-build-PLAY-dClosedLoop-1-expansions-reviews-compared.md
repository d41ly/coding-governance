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

`[folded]` will name each defect's fix, where it sits, and its class, once the forks are answered.

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
