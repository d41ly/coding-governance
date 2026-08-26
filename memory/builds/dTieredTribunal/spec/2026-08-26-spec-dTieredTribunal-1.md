# TOOL-dTieredTribunal-1 — the harness READS the blocker count it already asks for, and instructs the verdict line

**Status:** SPECCED · rev-3 · 2026-08-26 · node a · Tier-2 · base da9e4cd2 · order 1 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-2 TOOL-dTieredTribunal-3 |
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-2 TOOL-dTieredTribunal-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` asks its synthesis agent for a `blockers` count and a `highs`
count, schemas both, and then never reads either. Make the harness read them and return them, and
instruct the synthesis agent where the literal `## Verdict:` heading goes relative to the binding
line the prompt already mandates as the record's first line at `tools/workflows/tier2-review.js:357`.
The confirmed-blocker count is the number the build method's convergence loop is bounded by, and
today a human types it into a park row by hand. WHICH LOOP THIS REACHES is narrower than that
sentence alone implies, and the difference is the whole reason P1 is parked. M4's convergence loop is
the SPEC AUDIT loop, and M4 forbids this harness on a spec, so while P1 stays parked the returned
integer reaches a `diff-review` round and nothing else. A spec audit keeps hand-typing its count.
That is a real narrowing of this unit's value and it is stated here rather than discovered later.

## 2. Scope (IN)

- **S1** — `blockers` and `highs` join `path` and `summary` in the synthesis schema's `required`
  array at `tools/workflows/tier2-review.js:366`.
- **S2** — the success return block at `:390` carries `blockers` and `highs`, sourced from the
  synthesis result and from nothing else.
- **S3** — the three EARLY return paths carry `blockers: null` and `highs: null`, never zero. They
  are the all-lenses-dead exit at `:215`, the nothing-raised exit at `:225`, and the
  everything-refuted exit at `:313`. A synthesis that never ran has no blocker count, and a zero on
  those paths is a clean bill nothing earned.
- **S3b** — synthesis death is a FOURTH degraded exit, and it is not an early return. `if (!synth)`
  at `:381` only logs, and execution then falls through to the success return at `:390`. So S2's
  source is spelled `blockers: synth ? synth.blockers : null`, and `highs` the same way.
  Never zero, because a fabricated zero on a dead synthesis is the false-clean class this file's
  own comments were written to kill. Never `undefined`, because `synth.blockers` throws on a null
  synthesis and `synth?.blockers` yields `undefined`, which serializes as an absent key rather than
  as a stated absence. Not `synth?.blockers || null` either: after S1 the field is required, so a
  returned `0` is a real adjudicated count and the falsy idiom would map it to `null`.
- **S4** — the synthesis prompt instructs the agent on the record's opening ORDER, not merely on the
  verdict line's existence. The prompt already mandates a first line at `:357`, so a second
  first-line instruction would be resolved by the agent rather than by this spec. The order is the
  `**Serves:**` binding line, then the record's title and provenance, then the literal
  `## Verdict:` heading carrying one token from the closed set. The prompt states the set and states
  that it is closed. A THIRD sentence claims the opening and the order must place it too:
  `tools/workflows/tier2-review.js:349` reads "Open the report with a line naming the reviewed
  range", and it sits after the title-and-provenance block and before the `## Verdict:` heading.
  Three sentences claim an opening; the order names all three or the agent resolves the leftover.
  Keeping the binding line first satisfies check 21's 12-line binding-head window
  (`BIND_HEAD_LINES = 12`, `tools/memory-tree/gen_build_index.py:382`) by construction.
- **S4b** — the set the prompt states is READ from the carrier that ENFORCES it on a `diff-review`
  record, which is hygiene check 22 in `memory/HYGIENE.md`, gated by `REVIEW_VERDICT_CUTOFF` in
  `.memory-tree.conf`. It is not restated as a new rule in this spec, and the build method is not
  the enforcing carrier for this record kind.
- **S5** — the synthesis prompt defines BOTH new integer fields, not only one. `blockers` is the
  count of CONFIRMED blocker-severity findings and `highs` the count at high severity, and in both
  cases the severity meant is the one the synthesis pass adjudicated. The returned integers and the
  written record then agree by construction. S1 makes both fields REQUIRED, so a definition for one
  and silence on the other ships a mandatory integer with no stated population.
- **S6** — a comment on each edit naming this unit id, matching the file's existing convention of
  citing the unit that introduced a hardening. The edited sites are the schema, the success return,
  the three early returns, and the two synthesis-prompt edits S4 and S5 make — seven in all. An
  earlier revision of this bullet said five and named only the code sites, which is false of this
  unit's own scope. The version line of S7 is excluded, because its inline comment is the deployer's
  own version marker and is not a place to add provenance prose.
- **S7** — `meta.version` moves from `1.2` to `1.3` at `tools/workflows/tier2-review.js:3`, and the
  same-line `gov:kit tier2-review@` marker moves with it. `tools/workflows/kit.toml:6` declares
  `version_from = { file = "tier2-review.js", pattern = "version: " }`, so that field IS the
  review-harness kit version, and this unit changes the harness's return contract. Both tokens sit
  on one line, so this is a two-token edit in a file already being edited.

## 3. Non-goals (OUT)

- **Any review-KIND parameter.** No kind argument, no per-kind lens profile, no per-kind acquire
  sentence, no per-kind anchor predicate. That is the parked proposal named in this build's
  run-state file, and it needs a governance-carrier edit this build's own rules withhold.
- **Editing `memory/guides/BUILD-METHOD.md`, `memory/guides/REVIEW-PROTOCOL.md` or the governance
  template.** The verdict vocabulary is READ from its enforcing carrier here and not restated as a
  new rule.
- **Renaming the harness.** Refused on record in the aFoldedQuarry unit spec, on the ground that
  `AGENTS.md`, `README.md` and `WIRE-INTO-PROJECT.md` all name the file and all three still do. The
  three-times count in the research record belongs to a DIFFERENT refusal, the wholesale adoption of
  an upstream engine, and an earlier revision of this bullet transposed it onto the rename.
- **A new gate leg.** Only ONE of the three shipped scanners takes this file without a marker
  filter: `tools/workflows/check-review-join.sh:43` selects every tracked `tools/**/*.js`. The other
  two select on the `export const meta =` marker — `tools/workflows/check-verifier-fanout.sh:49` and
  `tools/workflows/check-workflow-syntax.js:30`. `tier2-review.js` carries that marker on line 1 and
  must keep it, so all three grade this file today and no new registration is owed. The marker
  selection is a real seam rather than a formality, which is why the reason is stated per scanner.
- **Changing the fan-out, the caps, the join, or the lens catalogue.** Follow-up: the parked fork.

## 4. Design

### Data model

The synthesis agent returns an object. Today the required set is two keys and the harness reads two
keys. After this unit the required set is four keys and the harness reads four.

There are FOUR exit paths, not three. Three are early returns. The fourth is the success return
reached with a dead synthesis, because the guard at `:381` logs without returning.

| field | success, synthesis returned | success, synthesis DIED | the three early paths |
|---|---|---|---|
| `blockers` | the integer the synthesis adjudicated | `null` | `null` |
| `highs` | the integer the synthesis adjudicated | `null` | `null` |

Both fields mean the same thing wherever they carry an integer: the count of CONFIRMED findings at
that severity, as adjudicated by the synthesis pass.

Using `null` rather than zero is the load-bearing choice on the degraded paths. Each of them is a
run that adjudicated nothing, and two of the three are degraded in the direction of reporting
nothing. A zero there is indistinguishable from a clean review. On the success path with a live
synthesis a `0` is the opposite thing — an adjudicated count — and S3b's ternary preserves it.

### Migration

Both fields are additive on the return, and no caller in the tree reads the return's shape today.
A synthesis agent that omits a now-required field fails schema validation.

The synthesis-death guard at `:381` does NOT return, which is why S3b spells the source rather than
trusting the guard to have handled the path. That guard logs a warning naming every confirmed
finding, and execution continues into the success return one block below it.

### Files touched (estimate)

`tools/workflows/tier2-review.js` only. S7's version bump is on line 3 of that same file.

### Alternatives rejected

- **Have the harness COUNT blocker-severity findings itself instead of asking the agent.** Rejected.
  The harness holds the confirmed set, so it could. Severity is a lens-supplied string the synthesis
  pass is allowed to correct, and two counts of one population computed at two points is this repo's
  own recurring class. The agent adjudicates severity, so the agent reports the count.
- **Default the two fields to zero everywhere for a simpler return shape.** Rejected under S3 and
  S3b.
- **Add a `verdict` field to the return.** Rejected as scope. The record's verdict line is already
  graded by hygiene check 22, and returning a second copy is a second answer to one question.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, and no new outbound request.
- perf / scale — N/A. No new agent and no change to the fan-out. Prompt growth is three sentences.
- a11y — N/A. This is a workflow script with no user interface.
- i18n — N/A. Same reason.
- error / empty / loading states — the empty states are the three early paths, which S3 covers, plus
  the synthesis-death fall-through, which S3b covers. A synthesis that dies is logged by the
  existing guard and then returned by the SUCCESS block, so the fields need a value there.
- observability — this unit IS the observability change, for the review kind it can reach. A
  `diff-review` round's blocker count stops being hand-typed. A spec audit's does not, because M4
  forbids this harness on a spec and P1, which would lift that, is parked.
- risks — one, and it is named. Making a schema property required can fail a synthesis that would
  previously have returned a partial object. The existing guard turns that into a logged warning
  naming every confirmed finding, and under S3b the return then carries `null` counts rather than a
  fabricated zero.
- testing + left-shift gates — the three shipped scanners over this file stay green. The acceptance
  observation is a direct read of the file rather than a new gate, because the change is a data-flow
  edit inside one file and a gate asserting that a return block names a field would be satisfiable
  by its own comment prose.
- migration / rollback — revert the single file.
- user docs — none. The harness is agent-facing and its own header comment is its documentation.

## 6. Acceptance criteria

- **AC1** — When the synthesis schema in `tools/workflows/tier2-review.js` is read, its `required`
  array names four keys, and `grep -n "required: \['path', 'summary'\]"
  tools/workflows/tier2-review.js` returns no match. The grep is scoped to THIS FILE deliberately.
  `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js` carry the same
  two-key spelling byte for byte, at `drift-audit-code.js:353` and `drift-audit-state.js:370`, so an
  unscoped tree-wide grep could not return no match while those two files stand. `TOOL-dTieredTribunal-3`
  is silent on that spelling rather than protecting it, so the scoping is what makes this criterion
  observable, not a promise borrowed from a sibling spec.
- **AC2** — When the success return block is read — the final `return {` of the file, which this
  unit's own S6 comments will have moved off `:390` — `blockers` and `highs` both appear in it, each
  sourced from the synthesis result through a ternary on `synth` rather than recomputed
  from the confirmed set.
- **AC3** — When each of the three early return paths is read, each carries `blockers: null` and
  `highs: null`, and no early path carries a zero for either field.
- **AC4** — When the success return is read for the synthesis-death case, `blockers` and `highs`
  resolve to `null` whenever `synth` is falsy. No path in the file yields `undefined` for either
  field, and no path yields a literal `0` that a live synthesis did not adjudicate. Observation:
  `grep -n 'synth ?' tools/workflows/tier2-review.js` shows the ternary on both fields.
- **AC5** — When the synthesis prompt is read, it states the opening ORDER of the record and not
  only the presence of a verdict line: the `**Serves:**` binding line first, then the title and
  provenance, then the literal `## Verdict:` heading, and the range line `:349` between the two. The
  prompt still contains the binding-line sentence at `:357` unchanged in its first-line role.
- **AC5b** — When the synthesis prompt is read, it states the closed verdict set and states that the
  set is closed, and the tokens it lists are the same three hygiene check 22 grades in
  `tools/memory-tree/check-memory-hygiene.sh`. The rev-2 fold rewrote this criterion into an ORDER
  assertion and dropped the set observation with it, leaving S4's second sentence and all of S4b
  unobserved.
- **AC6** — When the synthesis prompt is read, it states that `blockers` is the count of CONFIRMED
  findings at blocker severity AND that `highs` is the count at high severity, and that the severity
  meant is the one the synthesis pass adjudicated. Both, because S1 makes both required.
- **AC7** — When `grep -n 'dTieredTribunal-1' tools/workflows/tier2-review.js` runs, it returns a
  hit at each of the seven sites S6 enumerates: the schema, the success return, the three early
  returns, and the two synthesis-prompt edits.
- **AC8** — When `bash tools/check-kit-versions.sh` runs, it exits zero, and
  `grep -n "tier2-review@1.3" tools/workflows/tier2-review.js` returns the single line 3 that also
  carries `version: '1.3'`.
- **AC9** — When `node tools/workflows/check-workflow-syntax.js` runs over the tree, it exits zero.
- **AC10** — When `bash tools/workflows/check-review-join.sh` and
  `bash tools/workflows/check-verifier-fanout.sh` run, both stay green over the edited file.

## 7. Gates

The named legs this unit must keep green are `workflow script syntax`,
`review-join ban (no ref-keyed join)`, `verifier fan-out`, `agent-cap restatement`,
`review-protocol parity (kit vs dogfood)`, `kit version markers`, `review-join self-test` and
`verifier fan-out self-test`.

Several of those are unguarded in `tools/gate-legs.json` and run on every bar. No count is written
here: `tools/gate-legs.json` owns it and a number typed beside a manifest is wrong on the next
commit. They are
`workflow script syntax`, `review-join ban (no ref-keyed join)`, `verifier fan-out` and
`agent-cap restatement`, joined by `kit version markers`. That last leg is named because it runs,
NOT because it grades S7: `tools/check-kit-versions.sh:24` is a bare presence check that this file
carries SOME version-shaped token, and it holds no assertion pairing `meta.version` with the
same-line `gov:kit tier2-review@` marker. So it stays green whether or not S7 lands, and AC8's grep
is the whole observation of the bump. Adding that pair assertion is a gate change rather than spec
text and is recorded in §8 as a fork.

Three are guarded on `tools/workflows/` and therefore arm for this diff:
`review-protocol parity (kit vs dogfood)`, `review-join self-test` and `verifier fan-out self-test`.
The last two carry `subject: kit`, so `tools/run-gates/run-gates.sh` HOLDS them unless
`GATE_SELFTESTS=1` is set. A guarded leg arming is not the same as a leg running, and a Definition of
Done needs the run that sets both that variable and `GATE_FULL=1`.

This unit adds no gate leg. The existing scanners select this file already, per §3, and no new
registration in the leg manifest or the kit descriptor is owed.

One gap is knowingly left OPEN rather than closed here. S4 makes the synthesis prompt a further
carrier of the closed verdict vocabulary with no parity gate joining it to hygiene check 22. That is
the class already tracked as `TOOL-dUnstalledConvoy-16`, its fix is a gate or a machine-compared
pair in `tools/check-playbook-parity.sh` rather than spec text, and folding a mechanism into a
spec-text round would smuggle it past the round meant to price it. This spec does not close it, and
any later report claiming it closed without a gate or a parity pair is itself the defect.

## 8. Open questions

This section carries ONE open fork and it is stated first. An earlier revision opened with `none` and
then listed a fork beneath it, which is the shape `memory/TEMPLATE-SPEC.md` pins as undetectable by
either reader: both grade the section as one squeezed string, so a leading `none` is not a vote and
an open item under it goes unseen.

- **F2 — should `tools/check-kit-versions.sh` gain an assertion pairing `tier2-review.js`'s
  `meta.version` with its same-line `gov:kit tier2-review@` marker?** Round 2's finding 35 established
  that no such pair assertion exists: `:24` is a bare presence check, so a bump that moves one token
  and not the other is invisible to the bar, and the same file DOES carry that exact pairing for both
  drift-audit siblings at `:180-193`. Options seen: add the assertion in this unit; add it in a
  separate gate unit; leave the asymmetry. NOT RESOLVED here and deliberately not folded — a gate is a
  mechanism, and folding one into a spec-text round smuggles it past the round meant to price it,
  which is the same disposition round 1 gave finding 45. Parked for the owner through the verb, so it
  reaches the wrap-up with the rest of the set rather than living only in this section.

The review-KIND parameter is NOT a fork of this unit. It is parked at the BUILD level, with P9, in
this build's run-state file.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, authored by the unattended run under the standing mandate.
- rev-2 · 2026-08-26 · folded spec-audit round 1
  (`memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md`),
  taking every confirmed finding whose `Where` names this spec. The synthesis-death defect (findings
  6, 14, 40, 43) became new scope item S3b, a fourth column in §4's table, and AC4: the guard at
  `:381` only logs and falls through to the success return, so the source is spelled
  `synth ? synth.blockers : null` and a genuine adjudicated `0` survives. The verdict-line collision
  (34, 44) became an ORDER rule in S4 and an order assertion in AC5, since `:357` already owns the
  first line. Finding 45's owner-slip half became S4b, citing hygiene check 22 and
  `REVIEW_VERDICT_CUTOFF` as the enforcing carrier instead of the build method; the parity half of
  45 is NOT folded and is recorded as standing in §7, because its fix is mechanism rather than spec
  text. Finding 3 gained AC6 over S5's prompt sentence and finding 12 gained AC7 over S6's
  provenance comments, both previously unobserved. Finding 15 scoped AC1 to this file and named the
  two siblings that keep the two-key spelling by design. Findings 26 and 53 rewrote the
  no-new-gate-leg bullet: `check-review-join.sh:43` is the only scanner with no marker filter, and
  the other two select on `export const meta =`. Two version-marker obligations round 1 did not
  raise were added as S7 and AC8, because `tools/workflows/kit.toml:6` derives the review-harness kit
  version from this file's `meta.version` and a return-contract change owes the bump. The stale
  companions of the folded text were DELETED rather than negated beside it: §4 Migration and §5's
  error-states and risks bullets each claimed the synthesis-death guard returns, and it does not.
  Two findings were deliberately not folded here. Finding 27 keeps `node a` in the header, which is
  true of the session that authored it; the divergence from the build folder's node `d` is explained
  in the build README rather than by falsifying the header. Finding 29's spec-1 half needed no edit:
  S3's `:215`, `:225` and `:313` were re-read at HEAD and all three reproduce, so the correction it
  asks for is spec-3's alone.

- rev-3 · 2026-08-26 · folded spec-audit round 2, the record at
  `memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md`.
  Ten edits, eight of them answering defects the rev-2 fold itself created. 11 restored what rev-2
  DELETED: rewriting AC4 into an order assertion dropped the closed-set observation, leaving S4's
  second sentence and all of S4b unobserved; AC5b is that observation, added rather than merged so
  the order assertion stays readable. 30 placed the third opening-claim sentence — `:349`, the range
  line — which rev-2's order rule settled two of three and left the agent to resolve. 13 is a
  ROUND1_MISSED and the sharpest of them: S1 makes `highs` a REQUIRED schema field and S2 returns it,
  and nothing anywhere defined it, so a mandatory integer shipped with no stated population. S5 and
  AC6 now define both. 24 corrected S6's edit-site list from five to seven — it named only the code
  sites while S4 and S5 both edit the prompt — and AC7's literal count with it. 17 dropped the `:390`
  pin rev-2 added to AC2, which this unit's own S6 comments are guaranteed to move before the
  criterion is answered. 8 deleted a derived count from §7 prose. 38 is a ROUND1_MISSED: the rename
  bullet's "refused three times" transposed the upstream-adoption refusal's count onto the rename,
  which was refused once, on the three-carrier ground. 35's TEXT arm landed — §7 no longer calls
  `kit version markers` the reason to care about S7, because `check-kit-versions.sh:24` is a bare
  presence check that cannot see the bump — and its GATE arm is recorded as F2 rather than folded.

## 10. Reuse audit

The seam is `tools/workflows/tier2-review.js` itself, which already asks for and schemas both fields
at its synthesis call. There is nothing to build and nothing to extend. The fields are requested,
described, and dropped on the floor between the schema and the return.

`tools/codebase-map/reuse_lookup.py` was run for the phrase naming a review harness that drives
lenses and skeptics over a subject. It returned `tier2-review.js` under the `workflow-scripts`
inventory key plus the `agent-cap` dossier's shared seam, and no other candidate implements a
synthesis return.

Recall terms used with `tools/memory-recall/query.py`: `tier2-review harness lens skeptic verdict
spec-audit diff-review blockers convergence trust counters unverified fan-out`. That query returned
the aFoldedQuarry integer-join record and the aBoundedVerdict synthesis-death record. Both describe
the return block this unit edits, and neither touches the two fields it adds.
