# TOOL-aEvidencedLens-8 — the build harness promotes spec-audit minors, batched, and records the counts

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 7 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-8-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-8-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md) | diff-review | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-16 TOOL-aEvidencedLens-17 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20 |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

The owner answered on 2026-10-05 that a spec audit's MEDIUM and LOW findings are promoted, batched
into one unit or two, exactly as the closing diff review's are since `TOOL-aBatchedMinors-5`. The
only automated caller of the spec audit, the DISPOSAL stage of
`tools/workflows/unattended-build.template.js`, still tells its agent to FOLD every MEDIUM and LOW
and refuses a disposal that folds too few. This unit makes that stage promote them, batched, and
makes the round record carry the `--highs` and `--minors` counts `TOOL-aEvidencedLens-7` requires at
a spec subject's terminal exit, so the driver accepts the harness's record and check 2 owes the units.

## 2. Scope (IN)

- **S1** — The DISPOSAL prompt says PROMOTE where it said FOLD for every confirmed MEDIUM and LOW.
  All of them go into ONE batched unit whose spec names every finding by report id in its §1 and
  gives each its own §2 item. TWO units are used only when the minors split into two disjoint write
  sets by BUILD-METHOD M6's clauses, so the halves build concurrently. Never one unit per minor. Each
  batch unit is added by the same `--rescope --act add` a promoted blocker takes, or by a README
  roster row in attended mode, its reason naming every report id it closes. The
  prompt says a finding is not an ask, so it is named in scope and never through the `closes` verb,
  which joins a spec to a `BACKLOG.md` ask. The batch's placement `repairs` names the one unit every
  minor in it lands on, or `none` when they land on several. The prompt says `folded` is returned
  as 0. The prompt carries these four sentences verbatim, so a criterion can read each:
  "never through the `closes` verb"; "`repairs` names the one unit every minor in the batch lands
  on, or `none`"; "names every finding by report id in its §1"; and "return `folded` as 0".
  Observed by AC1.
- **S2** — The disposal guard refuses a non-zero `folded`, by name: a spec audit's MEDIUM and LOW
  are promoted, never folded, owner 2026-10-05. `folded` stays in `DISPOSAL_SCHEMA`, so the
  reconciliation `promoted + folded + refuted + standing === outstanding` keeps its shape. Observed
  by AC2.
- **S3** — The severity-split guard is rebuilt on the promotion rule. Every confirmed finding is
  promoted, so `promoted` is at least `confirmed`. The unit floor is
  `promotedIds.length >= blockers + highs + (minors > 0 ? 1 : 0)`, and the unit ceiling is
  `promotedIds.length <= blockers + highs + adjudicated + (confirmedMinors > 0 ? 2 : 0)`. Here
  `confirmedMinors` is `confirmed - blockers - highs`, `adjudicated` is `promoted - confirmed` (the
  UNVERIFIED findings the stage promoted), and `minors` is their sum. A breach of either bound
  refuses with its own reason and an empty roster, in the existing refusal shape. Observed by AC3
  and AC4.
  **Readers:** by name: `tools/workflows/unattended-build.template.js` and
  `tools/workflows/unattended-build.js` spell `mustFold` in the guard and its comment;
  `tools/workflows/unattended-build.test.sh` spells it in the MT arms' comment. by value: the
  refusal reason string in `tools/workflows/unattended-build.template.js` prints it, and nothing
  outside this file reads the integer.
- **S4** — `writeRound` records the counts at a TERMINAL exit, in two cases. At zero blockers the
  harness knows the exit is `CONVERGED`, so the record command carries `--highs <h> --minors <m>`
  from the start. At a positive count only the driver knows whether the loop ended, so the first
  command carries no counts and no disposition, which a `CONVERGING` round accepts. The retry
  instruction then reads: when the command refuses naming `--disposition`, `--highs` or `--minors`,
  the round is a terminal exit, so run the same command once more with
  `--highs <h> --minors <m> --disposition promote` appended, the integers spelled in. Observed by AC5
  and AC6.
- **S5** — The counts. `<h>` is the review's own `highs`. `<m>` is the review's
  `confirmed - blockers - highs`, plus `adjudicated` on the zero-blocker record that follows a
  disposal. A record written before the disposal, at a positive blocker count, cannot know
  `adjudicated` and omits it. That understates check 2's floor and never overstates it. `promote`
  rides the record exactly when `promotedIds` is non-empty, as today, and S3's floor makes that the
  case exactly when `<h>` or `<m>` or the blocker count is above zero. Observed by AC5 and AC6.
- **S6** — The DEGRADED note on the record-after-disposal path, which hands the operator a
  `--review` command to run by hand, names `--highs` and `--minors` with the review's integers and
  says to add every promoted UNVERIFIED finding to `--minors`. Observed by AC7.
- **S7** — The `CONVERGING` return's `nextAction` states the boundary. Under `REVIEW_ROUNDS` above 1
  a `CONVERGING` round still folds the findings the round confirmed and re-invokes, as today. That
  in-loop fold is the review loop's own fix step and not a disposition. Only the terminal exit
  disposes, and it promotes whatever stands. Observed by AC8.
- **S8** — Every comment in the template that states the fold disposition of a spec audit is
  rewritten to the promotion rule: the stage header near the DISPOSAL phase, the reconciliation
  comment, and the `mustFold` comment. Observed by AC9.
- **S9** — The template and its render land in one commit, rendered by
  `bash tools/workflows/check-protocol-parity.test.sh --render` and never hand-edited (shared
  invariant 1). Observed by AC10.
- **S10** — `tools/workflows/unattended-build.test.sh` is edited where it pins the fold. The 21
  dispose doubles carrying `"folded"` above 0 are rewritten to promote. The default `returns()`
  double emits one `promotedIds` entry per promoted blocker, so the floor holds. The C arms pin the
  new record commands. New arms cover S2, the floor, the ceiling, the zero-blocker counts and the
  retry text. The suite runs once at `VERIFYING`, never inside the pass. NOT OBSERVED inside the
  pass, because shared invariant 9 keeps suites out of passes; the `New arm:` lines in §7 declare it.

## 3. Non-goals (OUT)

- The driver's refusals at a spec subject's exit. Those are `TOOL-aEvidencedLens-7`'s.
- The review harness `tools/workflows/tier2-review.template.js`. Its `highs` and `confirmed` returns
  already give both counts, as `TOOL-aBatchedMinors-1` measured when it retired a `minors` key.
- Splitting `promoted` by severity in `DISPOSAL_SCHEMA`. S5's floor-safe count makes it
  unnecessary; see §8 F2.
- The in-loop fold of a `CONVERGING` round. It is unchanged; see §8 F1.
- The carriers that teach the rule. `TOOL-aEvidencedLens-11` owns them.
- A kit version bump. The main loop bumps once at the close (shared invariant 7).
- The audit stage's inputs (`context`, `specs`, `checklist`, `scratch`, `prevBlob`). Those are
  `TOOL-aEvidencedLens-5`'s, in the same file, landed before this unit by order.
- A bound on how many audit generations a chain of promotions may spend. It sets the owner's audit
  cost and is parked for the owner (§8 F3); this unit neither adds one nor moves M4's precision rule.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-7` — the `--highs` and `--minors` flags on a spec subject's
  terminal exit, and the refusals that make the S4 retry fire. Without them the driver refuses the
  counts on a spec subject, and every record S4 writes at zero blockers is refused.
- **hands-off** `TOOL-aEvidencedLens-11` — the method's M4, the Skill and the verbs entry state that
  the harness promotes spec-audit minors batched and records `--highs` and `--minors` itself.
- **hands-off** `TOOL-aEvidencedLens-21` — the closing diff review's batched minors, which amend what this unit built.

## 4. Design

### Evidence

Read at base `028b5cac`, which is `origin/main` at preflight. The run branch's later commits touch
only `memory/builds/aEvidencedLens/`.

- The DISPOSAL prompt says `'FOLD every MEDIUM and every ' + 'LOW into the spec it belongs to'` at
  `tools/workflows/unattended-build.template.js:1233`.
- The guard computes `mustPromote = au.blockers + au.highs` and `mustFold = au.confirmed -
  mustPromote` at `:1345` and refuses `d.folded < mustFold` at `:1350`.
- `writeRound` builds `--review <slug> --subject <s> --verdict <v> --blockers <n>` plus a
  disposition at `:1034`. It never passes `--highs` or `--minors`. Its retry fires only on a refusal
  "naming --disposition" at `:1040`.
- The driver refuses either count on a spec subject today, at `tools/unattended/unattended.sh:10109`.
  So the harness passing them before `TOOL-aEvidencedLens-7` lands would be refused; this is the
  edge in §3.
- On the closing subject the driver requires both counts at `CONVERGED`, `NON-CONVERGENT` and
  `CEILING` and refuses them on a non-terminal round, at `:10215` to `:10241`. The state gate that
  refuses a missing disposition at a terminal exit runs first, at `:10187`. Unit 7 extends the
  counts block to spec subjects, so after it a terminal spec exit with no flags is refused by the
  state gate or the counts block, whichever unit 7 orders first. S4's retry names all three flags
  so it fires on either.
- The CONVERGING `nextAction` says `'FOLD the confirmed findings in ' + lastReport` at `:1151`.
- `grep -cE '"folded":[1-9]' tools/workflows/unattended-build.test.sh` printed 21. PINNED, measured
  2026-10-05.

### The disposal guard after this unit

```js
const confirmedMinors = au.confirmed - au.blockers - au.highs
const adjudicated = counted ? d.promoted - au.confirmed : 0      // UNVERIFIED findings promoted
const minors = confirmedMinors + Math.max(adjudicated, 0)
const unitFloor = au.blockers + au.highs + (minors > 0 ? 1 : 0)
const unitCeiling = au.blockers + au.highs + Math.max(adjudicated, 0) + (confirmedMinors > 0 ? 2 : 0)
// refusal order, after the existing standing, counted, disposed and refuted arms and the sum:
//   d.folded !== 0                       -> 'folded N — a spec audit's MEDIUM and LOW are PROMOTED, batched, never folded (owner, 2026-10-05)'
//   d.promoted < au.confirmed            -> 'promoted P is below the C confirmed — every confirmed finding is promoted'
//   promotedIds.length < unitFloor       -> 'K unit(s) for B blocker(s), H high(s) and M minor(s) — one unit per blocker and high, plus one for the minors'
//   promotedIds.length > unitCeiling     -> 'K unit(s) where at most CEIL fit — the minors are batched into one unit or two, never one per minor'
```

The existing arms stay where they are: `(d.promoted > 0) !== (promotedIds.length > 0)`, the edge pairs,
the placements. The ceiling is generous on purpose. `adjudicated` findings are of unknown severity,
so each may be a blocker owing its own unit, and the ceiling grants each one. The ceiling still
refuses the measured shape it exists for: five confirmed minors promoted into five units.

### The record command after this unit

```text
zero blockers:     --review <slug> --subject <s> --verdict "CLEAN" --blockers 0 --highs <h> --minors <m>[ --disposition promote]
positive blockers: --review <slug> --subject <s> --verdict "BLOCKED" --blockers <b>
  retry on a refusal naming --disposition, --highs or --minors:
                   ... --blockers <b> --highs <h> --minors <m> --disposition promote
```

At a positive blocker count every terminal exit stands on at least one blocker, so `promote` is
always the right retry. Zero blockers is `CONVERGED` unconditionally in the driver's `review_state`,
so the zero-blocker command is the terminal one and needs no retry.

Attended mode records nothing with the driver, as today. S1 to S3 still bind it.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`

### Alternatives rejected

- Predicting terminality from `round` and a passed `REVIEW_ROUNDS`. The harness does not receive the
  bound, and the driver's sequence verdict is the authority; adding an arg to mirror the conf is a
  second source of one value.
- A schema `maximum: 0` on `folded`. A schema failure reaches the script as a null return, which the
  guard reports as "returned nothing at all". The named refusal says what was wrong.

## 5. Production-readiness checklist

- security — N/A: no new write path. The stage already runs `--rescope` and writes specs; it now
  writes one or two batch specs where it wrote rev bumps.
- perf / scale — The batch caps new units at two for the minors per round. The governing bound on a
  chain of promotions is BUILD-METHOD M4's precision rule, `TOOL-dLoggedFlight-34`, closed by
  `TOOL-dGatedProse-4`: a promoting round whose precision falls below the review protocol's floor
  ends the chain. `TOOL-aWokenSentinel-30` is an OPEN ask that measured the cascade NOT converging.
  This unit makes nearly every terminal spec round with a standing MEDIUM or LOW promote a batch
  unit, and M4 audits each as a fresh subject; `TOOL-aEvidencedLens-3` confirms at any rubric
  severity, which RAISES the precision that must fall for the chain to end. Both effects lengthen a
  chain, so this unit does not call the chain bounded. Whether a minors batch closes under M4's
  recorded override instead of a fresh audit, or a generation cap applies, is parked for the owner
  (§8 F3).
- error / empty / loading states — Zero findings keeps the skip path. Zero confirmed with promoted
  UNVERIFIED findings records `--minors` above zero, so `promote` is never paired with zero standing.
- observability — The `disposal: done` log line keeps `folded`, which now always reads 0.
- risks — The driver and the harness must agree on the retry trigger. S4 names all three flags, so
  either refusal order fires it. A refusal for any other reason still returns stderr.
- testing — AC1 to AC10 are stub runs of the render. The suite edits in S10 run once at `VERIFYING`.
- migration — N/A: rows written before this unit carry no counts and keep their reading (unit 7).
- user docs — `TOOL-aEvidencedLens-11` owns the carriers.

## 6. Acceptance criteria

Every criterion below is a stub run of the RENDER `tools/workflows/unattended-build.js` with
recording `agent()` globals. It uses the `run_wf` AsyncFunction shape of
`tools/workflows/unattended-build.test.sh`, copied into a scratch script under the run's scratch
directory and run there, never by running the suite. Inputs use that file's `UNITS` args and its
`review_out <blockers> <confirmed> <highs> <unverified>` and `rec <token>` doubles.

- **AC1** — When the stub runs with `review_out 0 3 1` and `rec CONVERGED`, the traced
  `prompt:dispose:` line contains `PROMOTE every MEDIUM and every LOW`, `never one unit per minor`,
  `disjoint write sets`, and each of S1's four verbatim sentences, read by the markers
  ``never through the `closes` verb``, `names the one unit every minor in the batch lands on`,
  `names every finding by report id in its §1` and ``return `folded` as 0``; the same run over the
  base render's prompt contains none of those four; and it does not contain `FOLD every MEDIUM`.
  Red when: the prompt still tells the stage to fold a MEDIUM or LOW, or drops a clause S1 names.
- **AC2** — When the dispose double returns `"promoted":2,"folded":1` with two `promotedIds` over
  `review_out 0 3 1`, the trace logs `disposal: NOT done` with `never folded` and the RESULT carries
  `"roster":[]`.
  Red when: the fold is accepted and the roster is handed out.
- **AC3** — When the dispose double returns `"promoted":3,"folded":0` with ONE `promotedIds` entry
  over `review_out 0 3 1`, the trace logs `disposal: NOT done` naming the floor. When it returns two
  entries, it logs `disposal: done` and the RESULT's `roster` is non-empty.
  Red when: one unit for one high and two minors is accepted.
- **AC4** — When the dispose double returns five `promotedIds` for `"promoted":5` over
  `review_out 0 5 0`, the trace logs `disposal: NOT done` with `never one per minor`. With two
  entries it logs `disposal: done`.
  Red when: one unit per minor is accepted.
- **AC5** — When the stub runs with `review_out 0 3 1` and an accepting two-unit disposal, the
  `prompt:audit:record` line contains `--blockers 0 --highs 1 --minors 2 --disposition promote`.
  When it runs with `review_out 0 0 0 0`, it contains `--blockers 0 --highs 0 --minors 0` and no
  `--disposition`. When it runs with `review_out 0 0 0 2` and a disposal promoting both UNVERIFIED
  findings into one unit, it contains `--highs 0 --minors 2 --disposition promote`.
  Red when: a zero-blocker record omits a count, or pairs `promote` with zero standing.
- **AC6** — When the stub runs with `review_out 2 5 1` and `rec BOUNDED`, the `prompt:audit:record`
  line's first command ends `--blockers 2` with no `--highs`. The same prompt carries the retry
  `--highs 1 --minors 2 --disposition promote` and names `--disposition`, `--highs` and `--minors`
  as its trigger.
  Red when: the first command carries counts a `CONVERGING` round would refuse, or the retry omits one.
- **AC7** — When the stub runs with `review_out 0 3 1` and a dispose double returning `standing`
  non-empty, the RESULT's `note` names `--highs 1 --minors 2` and says to add promoted UNVERIFIED
  findings to `--minors`.
  Red when: the hand-recording command would be refused by the driver at a spec subject's exit.
- **AC8** — When the stub runs with `review_out 2 2 0` and `rec CONVERGING`, the RESULT's
  `nextAction` still says `FOLD the confirmed findings` and also says the in-loop fold is not the
  exit's disposition.
  Red when: the boundary sentence is missing, or the in-loop fold instruction was removed.
- **AC9** — When `grep -niE 'MEDIUM or LOW (is|still) fold|FOLD every MEDIUM|mustFold|AT LEAST the confirmed rest|folded or named standing'`
  runs over `tools/workflows/unattended-build.template.js`, it prints nothing.
  Red when: a comment or prompt still states the fold disposition.
- **AC10** — When `node tools/workflows/check-workflow-syntax.js` runs after the render, it exits 0.
  When `grep -c 'unitCeiling' tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js`
  runs, both counts are equal and non-zero.
  Red when: the render was not regenerated, or the template does not parse in the workflow runtime.
- **AC11** — When the main loop's second spec audit of this build records a terminal round through
  the real driver, the row carries `highs` and `minors` and is accepted.
  Red when: the driver refuses the harness's record at a spec subject's exit.
  permission: observed by the main loop after `TOOL-aEvidencedLens-7` and this unit both land, never
  inside this unit's pass.
  fixture: needs a run-state file, which only this build's own run holds.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `review-join self-test` · `verifier fan-out self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · a dispose double with `folded` 1 · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · one unit for one high and two minors · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · five units for five minors · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · the zero-blocker record command without counts · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · a retry text omitting `--highs` · `FLOOR_ASSERTIONS` raised by the assertions added

## 8. Open questions

- **F1 — Does a `CONVERGING` spec round fold everything it confirmed, or its blockers only, as the
  closing diff review's does?** Blockers only would carry highs and minors to the exit, where they
  are summed over rounds. That needs the harness to carry running counts between invocations. It also
  double-counts: a spec round re-audits the whole subject, so the next round re-confirms what stood
  unfixed. Folding everything confirmed is today's behaviour, and the brief says it stays.
  Recommendation: keep today's in-loop fold and state the boundary (S7).
  RESOLVED (agent, 2026-10-05, delegated): today's in-loop fold stays; only the terminal exit
  promotes, and its counts are the exit round's own.
- **F2 — What counts does the zero-blocker record carry when the disposal promoted UNVERIFIED
  findings?** Unit 7 refuses `promote` beside zero standing, and the review's own counts are 0 when
  only unverified findings stood. Options: (a) add `adjudicated` to `--minors`, which keeps check 2's
  floor at or below the units promoted; (b) drop the disposition when the review's counts are 0,
  which hides the promoted unit from check 2, the defect cluster B of `aProbedUnit`'s closing review
  fixed; (c) split `promoted` by severity in `DISPOSAL_SCHEMA`, which widens the schema for no
  stronger check. Recommendation: (a).
  RESOLVED (agent, 2026-10-05, delegated): (a), S5.
- **F3 — Does this unit bound how many audit generations a chain of promotions may spend?** The
  round-1 spec audit's finding 45 named two options: (a) close a spec-audit minors batch unit under
  M4's recorded `specs-audited` override rather than auditing it as a fresh subject; (b) park the
  generation bound for the owner. Option (a) rewrites M4, a governance carrier, and sets how much
  audit the owner pays per build, so M3's veto 2 removes it and no delegated resolver remains.
  RESOLVED (agent, 2026-10-05, delegated): neither is built here. This unit's scope stops at
  promoting the minors and recording the counts; the generation bound is parked for the owner in
  the run-state file as a `decision` row naming both options and the veto, and §5 states the
  interaction meanwhile.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft.
- rev-2 · 2026-10-05 · §3 §5 §7 §8 S1 AC1 AC9 · round-1 spec audit fold. Id 14 (MEDIUM): S1 pins
  four verbatim sentences and AC1 reads each, absent from the base prompt. Id 45 (MEDIUM): §5 cites
  `TOOL-aWokenSentinel-30` as open and `TOOL-dLoggedFlight-34` with `TOOL-dGatedProse-4` as the
  governing ruling, states the interaction with `TOOL-aEvidencedLens-3`, and no longer calls the
  chain bounded; the generation bound is §8 F3, parked for the owner as option (b). Id 16 (LOW):
  AC9's alternation adds the reconciliation comment's two phrases. Id 30 (LOW, its unit-8 half):
  §7's arms raise `FLOOR_ASSERTIONS` by the assertions added.
- rev-3 · 2026-10-05 · §3 · the mirror of `TOOL-aEvidencedLens-21`'s consumes-from edge, written by
  the main loop when the closing review's minors were promoted.

## 10. Reuse audit

The seam is the existing DISPOSAL stage and `writeRound` in
`tools/workflows/unattended-build.template.js`, extended in place. No new stage, schema field or
function. The batch rule, the refusal shape and the counts are the ones `TOOL-aBatchedMinors-2` built
for the closing review, applied to the spec subject. The placement rule is `TOOL-cMendedVintage-19`'s,
reused with `repairs: none` for a batch spanning several units. The minors count is
`confirmed - blockers - highs`, which `TOOL-aBatchedMinors-1` showed the review harness already
returns.
`python tools/codebase-map/reuse_lookup.py "dispose spec audit findings by severity and promote batched minors"`
returned no JavaScript seam: the lookup scans Python and says `unscanned layers: .sh`, so the seam was
found by grep over `tools/workflows/` and `tools/unattended/unattended.sh`. The recall query's top
hits were `TOOL-aProbedUnit-9`, `TOOL-aBatchedMinors-5`, `TOOL-aWokenSentinel-30` and
`TOOL-cMendedVintage-19`, each cited above.

Recall terms used: `python tools/memory-recall/query.py "should spec audit mediums and lows be promoted to a batched unit instead of folded into the spec" --terms "spec-audit disposal promote fold MEDIUM LOW batched minors unattended-build harness severity REVIEW_ROUNDS BOUNDED"`
