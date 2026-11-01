# Brief — dFoldedAudit: a spec audit folds local fixes, promotes only new mechanisms, and its chain stops itself

**Serves:** research TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8

## The prompt

> Changes are required to the current Gov - build method's M4 'spec audit' clause specifically and its enforcement machinery. If necessary, the same changes should be applied to the design of the architecture redesign (dClosedLoop chain of builds).
>
> * Build method's M4 currently binds spec audits to PROMOTE all their findings to new units (never fold into existing specs) - this has proven to be problematic in certain instances. Adjustments need to be made to the spec review principles (this only applies to the spec reviews, closing reviews reviews remain as they are).
> * A declared review chain STOPS when no blockers are found (currently BLOCKER and HIGH) and all the specs fully reviewed. If no blockers were found but new units were promoted by the audit (new mechanisms), those specs still need to be reviewed before the chain stops.
> * Fold local fixes in place: a wording or citation, a missing witness, an edge mirror, a criterion’s reach, small fixes, etc.. get folded into their specs, revisions bumped.
> * In spec reviews, **promote only findings that need new mechanisms**.
> * Let a repair unit edit its sibling’s spec with a rev bump, rather than patching it from outside. That removes the H1/H7 class.
> * Stop the chain at the first round whose highs all sit in the previous round’s own promotions. That is the signal you’ve stopped auditing the design.
> * Review dClosedLoop's design and chain of specs for spec audit principles, and introduce those changes only if applicable.

## The brief

### Goal
A spec audit folds a local fix into its spec with a rev bump, promotes only a finding that needs a new mechanism, and ends its chain on a derived verdict with a ceiling that holds for the owner, in the method, the driver, the harness and dClosedLoop's unbuilt specs. Closing diff reviews do not change.

### Items
1. M4's text and its carriers state the spec-audit disposal and the chain stop, the precision bound retired. [planned TOOL-dFoldedAudit-1]
2. `--review` and check 2 record and grade a spec exit that folds, rows counting folded and promoted, behind a dated cutoff so in-flight runs finish under the old rule. [planned TOOL-dFoldedAudit-2]
3. The DISPOSAL stage disposes by nature, each fold naming its spec and rev, and its reconciliation refuses a HIGH vanishing into prose. [planned TOOL-dFoldedAudit-3]
4. A repair unit edits its unbuilt sibling's spec with a rev bump; a built spec stays frozen. [planned TOOL-dFoldedAudit-4]
5. Each HIGH records the specs it would change, and a verb derives the R1 and R5 stops and the ceiling hold from those records. [planned TOOL-dFoldedAudit-5]
6. An audit's own fold owes no hand `spec-revised` deviation record. [planned TOOL-dFoldedAudit-6]
7. Policy keys carry the new rules as defaults and the old rule as an allowed value. [planned TOOL-dFoldedAudit-7]
8. dClosedLoop's unbuilt specs DL-32, DL-20 and FH-17 are revised and its frozen design takes a deviation record for `cl-0117`; PLAY-dClosedLoop-1 needs nothing. [planned TOOL-dFoldedAudit-8]

### Acceptance
1. M4 states the new disposal, the two stops and the ceiling; the method fits its 30720-byte ceiling; DIFF wording is unchanged; the review-protocol parity leg is green.
2. A staged `--review` spec exit with `--disposition fold` records and grades green past the cutoff, and the same row dated before it reds; a counted fold on a diff subject still reds.
3. An `unattended-build.test.sh` arm shows a local HIGH folded with its spec and rev, and a fold return naming no spec refused.
4. A disposal fixture shows the repair unit's sibling edit, a rev bump and §9 line, admitted on an unbuilt sibling and refused on a built one.
5. A selftest arm derives STOP on a round whose HIGHs all name prior promotions, CONTINUE on one HIGH naming an older spec, and HOLD at the ceiling; an empty HIGH population does not read as R5.
6. `deviation_join` admits an audit-fold rev move with no record and still reports a non-fold rev move.
7. `policy.py get` reports each key's default and the old value restores today's refusal in a fixture.
8. Each revised spec carries its rev bump and §9 line, the deviation record cites the prompt, and `dSafePassage` shows no diff.

### Gates
unattended kit gate · unattended-build self-test · tier2-review self-test · workflow script syntax · harness arms (fail branches armed or pinned) · review-protocol parity (kit vs dogfood) · kit/dogfood doc parity · kit version markers · template size <=48KiB · policy check · policy fixtures · memory hygiene · build README slot contract · spec tokens (a spec's own names resolve) · the plain bar, `bash tools/run-gates/run-gates.sh`, once at the close.

### Non-goals
Closing diff reviews and their disposal; `closing-review-recorded`; retiring or refolding units already promoted; retroactive edits to landed specs; a built sibling's spec; a spec audit of this build's own specs, which the owner did not ask for; `tools/loop/`, which dDeclaredLoop builds.

### Limitations
Never write a governance carrier beyond M4's stated change; M1's byte ceiling stands. No write to dSafePassage or to any build with a live run claim, checked at the pass that writes it. dClosedLoop's v2 changes only by a deviation record quoting the owner. Kit self-tests stay held per the standing owner instruction. Every new id is `TOOL-dFoldedAudit-<n>`.

### Reuse
`verb_review` in `tools/unattended/unattended.sh` and its `subj = slug` split; the DISPOSAL stage and `DISPOSAL_SCHEMA` in `tools/workflows/unattended-build.template.js`; check 2's awk in `tools/unattended/check-unattended.sh` with a third cutoff beside `FOLD_CUTOFF` and `SPEC_COUNTS_CUTOFF`; `deviation_join.scan` and `derive_past_pin_ids`; `SPEC-TEMPLATE`'s rev-bump shape. Decision rows TOOL-aProbedUnit-9, TOOL-aBatchedMinors-5 and TOOL-aEvidencedLens-17, the last superseded for spec audits. Both scout returns are recorded under `build/`.

## Drawn from the session

> R5 stops the chain while HIGHs still stand. What happens to those HIGHs? Fold, or build unaudited (Recommended)
— owner, 2026-11-01 step 2

> A round confirms HIGHs, folds them all and promotes nothing. R1 says stop only when no blockers are found. Does another round run? Re-audit folded specs only (Recommended)
— owner, 2026-11-01 step 2

> Precision never ended a chain in practice, so M4's bound was never reached. What is the chain's backstop now? Retire it, ceiling then hold (Recommended)
— owner, 2026-11-01 step 2

> Class: a one-line correction to spec A becomes a whole unit B that overrides A's text from outside
— agent, the reuse scout's return, recorded under `build/`

## Owner confirmation

Asked: Do you accept this brief? It sets the build's scope, and the run proceeds from it with no further owner turn.
Answer: Accept the brief (Recommended)
