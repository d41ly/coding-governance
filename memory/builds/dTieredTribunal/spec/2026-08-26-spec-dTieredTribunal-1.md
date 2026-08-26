# TOOL-dTieredTribunal-1 — the harness READS the blocker count it already asks for, and instructs the verdict line

**Status:** SPECCED · rev-2 · 2026-08-26 · node a · Tier-2 · base da9e4cd2 · order 1 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-2 TOOL-dTieredTribunal-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` asks its synthesis agent for a `blockers` count and a `highs`
count, schemas both, and then never reads either. Make the harness read them and return them, and
instruct the synthesis agent where the literal `## Verdict:` heading goes relative to the binding
line the prompt already mandates as the record's first line at `tools/workflows/tier2-review.js:357`.
The confirmed-blocker count is the number the build method's convergence loop is bounded by, and
today a human types it into a park row by hand.

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
  that it is closed. Keeping the binding line first satisfies check 21's 12-line binding-head window
  (`BIND_HEAD_LINES = 12`, `tools/memory-tree/gen_build_index.py:382`) by construction.
- **S4b** — the set the prompt states is READ from the carrier that ENFORCES it on a `diff-review`
  record, which is hygiene check 22 in `memory/HYGIENE.md`, gated by `REVIEW_VERDICT_CUTOFF` in
  `.memory-tree.conf`. It is not restated as a new rule in this spec, and the build method is not
  the enforcing carrier for this record kind.
- **S5** — the synthesis prompt tells the agent that its `blockers` return field must be the count
  of CONFIRMED blocker-severity findings, and that the severity in question is the one the synthesis
  pass adjudicated. The returned integer and the written record then agree by construction.
- **S6** — a comment on each edit naming this unit id, matching the file's existing convention of
  citing the unit that introduced a hardening. The edited sites are the schema, the success return,
  and the three early returns. The version line of S7 is excluded, because its inline comment is the
  deployer's own version marker and is not a place to add provenance prose.
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
- **Renaming the harness.** Refused three times on record, and three tracked documents name it.
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
- observability — this unit IS the observability change. The count the convergence loop reads stops
  being hand-typed into a park row.
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
- **AC2** — When the success return block at `:390` is read, `blockers` and `highs` both appear in
  it, each sourced from the synthesis result through a ternary on `synth` rather than recomputed
  from the confirmed set.
- **AC3** — When each of the three early return paths is read, each carries `blockers: null` and
  `highs: null`, and no early path carries a zero for either field.
- **AC4** — When the success return is read for the synthesis-death case, `blockers` and `highs`
  resolve to `null` whenever `synth` is falsy. No path in the file yields `undefined` for either
  field, and no path yields a literal `0` that a live synthesis did not adjudicate. Observation:
  `grep -n 'synth ?' tools/workflows/tier2-review.js` shows the ternary on both fields.
- **AC5** — When the synthesis prompt is read, it states the opening ORDER of the record and not
  only the presence of a verdict line: the `**Serves:**` binding line first, then the title and
  provenance, then the literal `## Verdict:` heading. The prompt still contains the binding-line
  sentence at `:357` unchanged in its first-line role.
- **AC6** — When the synthesis prompt is read, it states that the `blockers` return field is the
  count of CONFIRMED findings at blocker severity, and that the severity meant is the one the
  synthesis pass adjudicated.
- **AC7** — When `grep -n 'dTieredTribunal-1' tools/workflows/tier2-review.js` runs, it returns a
  hit at each of the five edited code sites: the schema, the success return, and the three early
  returns.
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

Four of those are unguarded in `tools/gate-legs.json` and run on every bar. They are
`workflow script syntax`, `review-join ban (no ref-keyed join)`, `verifier fan-out` and
`agent-cap restatement`, joined by `kit version markers`, which S7 is the reason to care about.

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

none — the one fork this unit could have carried is the review-kind parameter, and that is parked at
the BUILD level in this build's run-state file rather than restated here.

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
