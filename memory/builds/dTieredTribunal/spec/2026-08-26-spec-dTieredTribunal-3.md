# TOOL-dTieredTribunal-3 — the two drift-audit harnesses gain the trust accounting their sibling already carries

**Status:** SPECCED · rev-1 · 2026-08-26 · node a · Tier-2 · base da9e4cd2 · order 2 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Three files in `tools/workflows/` implement one review pipeline three times, and two of them are
missing every hardening the third learned from a shipped defect. `drift-audit-state.js` reports the
CONFIGURED lens set rather than the surviving one, so a dead lens is invisible to its caller; neither
sibling counts a dead lens, a dead skeptic, a spurious verdict or a contradictory one; and both
resolve a disagreeing repeat by keeping whichever verdict arrived first. The merge bar is green over
all of it. Port the accounting, so the two siblings can no longer report a clean bill for a run that
reviewed or judged nothing.

## 2. Scope (IN)

- **S1** — both siblings count dead lenses. `drift-audit-state.js:234` and
  `drift-audit-code.js:218` each do `finderResults.filter(Boolean)` and discard the drop count; each
  gains a `lensesDead` value derived as the configured count minus the surviving count.
- **S2** — both siblings count dead skeptic batches, derived the same way over their verdict batches
  at `drift-audit-state.js:306` and `drift-audit-code.js:287`.
- **S3** — `drift-audit-state.js:378` stops returning `LENSES.map((L) => L.slug)`, the CONFIGURED
  set, and returns the surviving lens slugs plus `lensesDead`. `drift-audit-code.js` returns no lens
  information at all today and gains the same pair.
- **S4** — both siblings gain the all-lenses-dead early return: when every lens failed to return, log
  that nothing was reviewed and return with the counts, rather than proceeding to synthesize a report
  over an empty finding set.
- **S5** — both siblings count a spurious verdict, an agreeing duplicate, and a contradictory repeat,
  and a contradictory repeat DEMOTES its finding to unverified rather than keeping the first
  verdict. This replaces the first-write-wins guard `if (typeof v.id === 'number' && !vmap.has(v.id))`
  that both files carry.
- **S6** — both siblings gain the synthesis-death log: when the synthesis agent returns null, log
  every confirmed and unverified finding before returning, so the findings are not lost silently.
- **S7** — both return blocks carry every counter on the success path AND on the new early path, and
  each file's `note` field distinguishes a complete run from a degraded one, in the shape
  `tools/workflows/tier2-review.js` already uses.
- **S8** — each ported guard carries a comment naming the unit that originally earned it in
  `tier2-review.js`, so the provenance travels with the code rather than being re-lost.

## 3. Non-goals (OUT)

- **Merging the three files into one engine.** That is the research record's engine-and-profile
  proposal, priced as expensive, and the runtime forecloses the obvious shape because workflow
  scripts cannot import. This unit duplicates the guards deliberately, which the governance template
  already instructs for exactly this runtime reason.
- **Any review-KIND parameter, on any of the three files.** Parked at the build level.
- **Changing either sibling's lenses, prompts, subjects, caps, or output paths.** The audits keep
  finding what they find; only the accounting around them changes.
- **Changing `tools/workflows/tier2-review.js`.** That file is the source being copied FROM, and the
  unit before this one is the only one that edits it.
- **A shared helper file.** Workflow scripts cannot import, so there is nowhere to put one.
- **Tightening the fan-out guard's marked-derivation branch.** `drift-audit-state.js:224` uses that
  branch and the research reproduced a hole in it. Fixing the hook is a separate unit and is a
  follow-up, recorded in section 8.

## 4. Design

### Inventory

The delta, derived by reading all three files at the pinned base. Every row is a guard present in
`tier2-review.js` and absent from both siblings.

| Guard | In `tier2-review.js` | In either sibling |
|---|---|---|
| dead-lens count | `:205` | absent |
| all-lenses-dead early return | `:214` | absent |
| dead-skeptic count | derived over its verdict results | absent |
| spurious-verdict count | `:277` | absent |
| duplicate-verdict count | `:280` | absent |
| contradictory repeat demotes to unverified | `:281` and `:283` | absent, first write wins |
| synthesis-death log | `:381` | absent |
| surviving lens set on the return | `:401` | `state.js` returns the configured set, `code.js` returns none |

Two guards are already present in both siblings and are NOT in scope: the orchestrator-assigned
integer join key, and the rule that a finding with no verdict is unverified rather than refuted.
Both were verified by reading the files rather than assumed.

### Data model

Each sibling's return block gains `lensesRun` as the SURVIVING count, `lensesDead`, `skepticsDead`,
`conflicts`, `duplicates`, `spurious`, and a `note` string. The existing `counts` object and
`precision` are unchanged, so no field a reader relies on today changes meaning.

The new early return carries the same fields, with the report and summary null. This is the property
the prior-art refusal insists on: every counter on every exit path, or the port is the same refusal
on a different filename.

### Migration

None. Every field is additive and no tracked caller reads either sibling's return shape. The one
behavioural change a caller can observe is the new early return, which fires only when every lens
died, which today produces a synthesized report over an empty finding set.

### Files touched (estimate)

`tools/workflows/drift-audit-state.js` and `tools/workflows/drift-audit-code.js`. No third file: the
scanners that grade these two select on markers both already carry, and neither has a kit descriptor
row of its own to update.

### Alternatives rejected

- **A rendered engine emitting all three files from one source, with a parity gate.** Rejected as a
  build in itself, and it walks into the recorded refusal on any replacement engine unless every
  counter survives on every exit path of every profile, which is what this unit does directly and
  cheaply.
- **Leaving `drift-audit-code.js` alone because it returns no lens information at all.** Rejected:
  returning nothing is not safer than returning the wrong thing, it is the same false-clean with
  fewer words.
- **Making the contradictory-repeat rule last-write-wins instead of demote-to-unverified.** Rejected.
  Two skeptics disagreeing is exactly the state where the harness does not know, and the recorded
  defect that produced the current rule in the sibling was a last-write-wins collision.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, and no new outbound request.
- perf / scale — N/A. No new agent, and the new early return strictly reduces work by skipping a
  synthesis over an empty set.
- a11y — N/A. These are workflow scripts with no user interface.
- i18n — N/A. Same reason.
- error / empty / loading states — this unit IS the empty-state work. The all-lenses-dead path and
  the dead-synthesis path are the two empty states, and neither is currently handled.
- observability — the counters ARE the observability. A caller can currently not tell a full audit
  from one where half the lenses died.
- risks — the demote-to-unverified rule can move a finding out of the confirmed set that the
  first-write-wins rule would have confirmed. That is the intended correction and it lowers reported
  precision on a degraded run, which is the honest number.
- testing + left-shift gates — the acceptance observations are direct reads of both files plus the
  three shipped scanners. A new leg asserting a return block names a field would be satisfiable by
  its own comment prose, which is the class the merge bar is full of gates against.
- migration / rollback — revert the two files.
- user docs — none. Both scripts are agent-facing and their headers are their documentation.

## 6. Acceptance criteria

- **AC1** — When `grep -nE 'lensesDead|skepticsDead|spurious|conflicts' tools/workflows/drift-audit-state.js tools/workflows/drift-audit-code.js`
  runs, it returns hits in both files, where at the pinned base it exits non-zero with no output.
- **AC2** — When `drift-audit-state.js` is read, its return no longer contains
  `lensesRun: LENSES.map((L) => L.slug)`, and the value it returns is derived from the surviving
  results.
- **AC3** — When each sibling's verdict-join loop is read, a verdict carrying an id the run never
  assigned increments a `spurious` counter, and a repeat disagreeing with the standing verdict
  removes that finding from the confirmed set rather than being discarded.
- **AC4** — When each sibling is read, an all-lenses-dead condition returns before its `agent(` call
  labelled `synth`, and that early return carries `lensesDead` and `skepticsDead` exactly as the
  success return does.
- **AC5** — When each sibling is read, a falsy `synth` is logged together with every confirmed and
  unverified finding before the function returns, matching the guard in
  `tools/workflows/tier2-review.js`.
- **AC6** — When `node tools/workflows/check-workflow-syntax.js` runs, it exits zero over both
  edited files.
- **AC7** — When `bash tools/workflows/check-review-join.sh` and
  `bash tools/workflows/check-verifier-fanout.sh` run, both stay green over both edited files.

## 7. Gates

The named legs this unit must keep green are `workflow script syntax`,
`review-join ban (no ref-keyed join)`, `verifier fan-out`, `drift-audit selftest` and
`drift-audit wiring`. This unit adds no gate leg.

## 8. Open questions

- **F1 — should the ported spurious and conflict counters also be asserted by a gate, rather than
  only read?** The research measured a candidate hook predicate for an uncounted `filter(Boolean)`
  and found it would red BOTH of these files, correctly, as live instances. Options seen: port the
  guards only and leave the predicate for a later unit; or port the guards and wire the predicate in
  the same unit, which requires observing its failing case and re-running it over the whole tree
  first. RESOLVED (agent, 2026-08-26, delegated): port the guards only. The predicate is a change to
  `tools/hooks/agent-cap.js`, which is the enforcement point the review protocol binds, and the
  research also reproduced a separate live hole in that file's marked-derivation branch. Wiring one
  predicate into a file with a known open hole, inside a unit whose subject is two other files, is
  two mechanisms in one spec. Follow-up: the hook work is its own unit and this run does not open it.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, authored by the unattended run under the standing mandate.

## 10. Reuse audit

The seam is `tools/workflows/tier2-review.js`, which already implements every guard this unit ports,
each one beside a comment naming the defect that earned it. This unit copies from that file rather
than inventing a predicate, and the copy is deliberate: the governance template instructs inlining in
this runtime because workflow scripts cannot import, so a shared helper is not available.

`tools/codebase-map/reuse_lookup.py` was run for the phrase naming a review harness that drives
lenses and skeptics over a subject. It returned `tier2-review.js`, `drift-audit-state.js` and
`drift-audit-code.js` together under the `workflow-scripts` inventory key, which is the population
this unit is about.

Recall terms used with `tools/memory-recall/query.py`: `tier2-review harness lens skeptic verdict
spec-audit diff-review blockers convergence trust counters unverified fan-out`. That query returned
the aFoldedQuarry integer-join record, the aGuardedTally dead-lens record and the aBoundedVerdict
synthesis-death record. All three describe guards this unit ports, and all three confirm the guards
were earned by observed defects rather than designed in advance.
