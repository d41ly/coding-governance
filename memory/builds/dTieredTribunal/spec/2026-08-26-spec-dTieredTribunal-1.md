# TOOL-dTieredTribunal-1 — the harness READS the blocker count it already asks for, and instructs the verdict line

**Status:** SPECCED · rev-1 · 2026-08-26 · node a · Tier-2 · base da9e4cd2 · order 1 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` asks its synthesis agent for a `blockers` count and a `highs`
count, schemas both, and then never reads either. Make the harness read them and return them, and
instruct the synthesis agent to open its record with the literal verdict line the method already
requires. The confirmed-blocker count is the number the build method's convergence loop is bounded
by, and today a human types it into a park row by hand.

## 2. Scope (IN)

- **S1** — `blockers` and `highs` join `path` and `summary` in the synthesis schema's `required`
  array at `tools/workflows/tier2-review.js:366`.
- **S2** — the success return block at `:390` carries `blockers` and `highs`, taken from the
  synthesis result.
- **S3** — the three early return paths carry `blockers: null` and `highs: null`, never zero. They
  are the all-lenses-dead exit at `:215`, the nothing-raised exit at `:225`, and the
  everything-refuted exit at `:313`. A synthesis that never ran has no blocker count, and a zero on
  those paths is a clean bill nothing earned.
- **S4** — the synthesis prompt instructs the agent that the record's verdict line is the literal
  `## Verdict:` heading followed by one token from the closed set the build method declares. The
  prompt states the set and states that it is closed.
- **S5** — the synthesis prompt tells the agent that its `blockers` return field must be the count
  of CONFIRMED blocker-severity findings, so the returned integer and the written record agree.
- **S6** — a comment on each edit naming this unit id, matching the file's existing convention of
  citing the unit that introduced a hardening.

## 3. Non-goals (OUT)

- **Any review-KIND parameter.** No kind argument, no per-kind lens profile, no per-kind acquire
  sentence, no per-kind anchor predicate. That is the parked proposal named in this build's
  run-state file, and it needs a governance-carrier edit this build's own rules withhold.
- **Editing `memory/guides/BUILD-METHOD.md`, `memory/guides/REVIEW-PROTOCOL.md` or the governance
  template.** The verdict vocabulary is READ from the method here and not restated as a new rule.
- **Renaming the harness.** Refused three times on record, and three tracked documents name it.
- **A new gate leg.** The three existing scanners over the workflow scripts already select this
  file with no marker filter.
- **Changing the fan-out, the caps, the join, or the lens catalogue.** Follow-up: the parked fork.

## 4. Design

### Data model

The synthesis agent returns an object. Today the required set is two keys and the harness reads two
keys. After this unit the required set is four keys and the harness reads four.

| field | success path | early paths | meaning |
|---|---|---|---|
| `blockers` | integer from the synthesis | `null` | confirmed findings at blocker severity |
| `highs` | integer from the synthesis | `null` | confirmed findings at high severity |

Using `null` rather than zero is the load-bearing choice. Each early path is a degraded run, and two
of the three are degraded in the direction of reporting nothing. A zero there is indistinguishable
from a clean review, which is the false-clean class this file's own comments were written to kill.

### Migration

None is needed. Both fields are additive on the return, and no caller in the tree reads the return's
shape today. A synthesis agent that omits a now-required field fails schema validation, and the
existing synthesis-death guard already turns a null synthesis into a logged warning carrying every
confirmed finding rather than a silent loss.

### Files touched (estimate)

`tools/workflows/tier2-review.js` only.

### Alternatives rejected

- **Have the harness COUNT blocker-severity findings itself instead of asking the agent.** Rejected.
  The harness holds the confirmed set, so it could. Severity is a lens-supplied string the synthesis
  pass is allowed to correct, and two counts of one population computed at two points is this repo's
  own recurring class. The agent adjudicates severity, so the agent reports the count.
- **Default the two fields to zero everywhere for a simpler return shape.** Rejected under S3.
- **Add a `verdict` field to the return.** Rejected as scope. The record's verdict line is already
  graded by the memory-hygiene gate, and returning a second copy is a second answer to one question.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, and no new outbound request.
- perf / scale — N/A. No new agent and no change to the fan-out. Prompt growth is two sentences.
- a11y — N/A. This is a workflow script with no user interface.
- i18n — N/A. Same reason.
- error / empty / loading states — the empty state is the three early paths, and S3 is exactly that
  case. A synthesis that dies is already logged and returned by the existing guard.
- observability — this unit IS the observability change. The count the convergence loop reads stops
  being hand-typed into a park row.
- risks — one, and it is named. Making a schema property required can fail a synthesis that would
  previously have returned a partial object. The existing synthesis-death guard turns that into a
  logged warning plus the confirmed findings rather than a silent loss.
- testing + left-shift gates — the three shipped scanners over this file stay green. The acceptance
  observation is a direct read of the file rather than a new gate, because the change is a data-flow
  edit inside one file and a gate asserting that a return block names a field would be satisfiable
  by its own comment prose.
- migration / rollback — revert the single file.
- user docs — none. The harness is agent-facing and its own header comment is its documentation.

## 6. Acceptance criteria

- **AC1** — When the synthesis schema in `tools/workflows/tier2-review.js` is read, its `required`
  array names four keys, and a grep for the old two-key spelling returns no match.
- **AC2** — When the success return block is read, `blockers` and `highs` both appear in it, sourced
  from the synthesis result rather than recomputed from the confirmed set.
- **AC3** — When each of the three early return paths is read, each carries `blockers: null` and
  `highs: null`, and no early path carries a zero for either field.
- **AC4** — When the synthesis prompt is read, it contains the literal string `## Verdict:` and
  states the closed verdict set.
- **AC5** — When `node tools/workflows/check-workflow-syntax.js` runs over the tree, it exits zero.
- **AC6** — When `bash tools/workflows/check-review-join.sh` and
  `bash tools/workflows/check-verifier-fanout.sh` run, both stay green over the edited file.

## 7. Gates

The named legs this unit must keep green are `workflow script syntax`,
`review-join ban (no ref-keyed join)`, `verifier fan-out`, `agent-cap restatement` and
`review-protocol parity (kit vs dogfood)`. This unit adds no gate leg: the existing scanners select
this file already, and no new registration in the leg manifest or the kit descriptor is owed.

## 8. Open questions

none — the one fork this unit could have carried is the review-kind parameter, and that is parked at
the BUILD level in this build's run-state file rather than restated here.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, authored by the unattended run under the standing mandate.

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
