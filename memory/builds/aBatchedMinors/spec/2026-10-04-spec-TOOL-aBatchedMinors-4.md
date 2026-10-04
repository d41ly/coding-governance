# TOOL-aBatchedMinors-4 — the method, the Skill and the verbs entry state the batched-promotion rule

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 5ba0fc4f · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aBatchedMinors-4-1-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aBatchedMinors-4-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The rule `TOOL-aBatchedMinors-2` and `-3` enforce has to be the rule the carriers teach, or an
operator reading the method folds a closing review's mediums and the driver refuses them with nobody
to explain why. This unit rewrites the closing-review disposition in every carrier that states it,
records the owner's ruling as a decision, and bumps the kits whose shipped bytes moved.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/BUILD-METHOD.template.md` M4's disposition paragraph splits by subject:
  a SPEC subject folds its mediums and lows as today; the CLOSING DIFF REVIEW promotes every confirmed
  finding — a blocker or high to a unit each, the mediums and lows batched into ONE unit naming them
  all, TWO only when they split into two disjoint write sets by M6's clauses, so both build
  concurrently; never one per minor. It names the batch unit as the one sanctioned exception to M2's
  one-mechanism rule. Rendered into `memory/guides/BUILD-METHOD.md` within its byte cap. Observed by
  AC1 and AC2.
- **S2** — `tools/unattended/SKILL.template.md`'s review-round section states the closing exit's
  counts, how they are derived — per round, `highs` and `confirmed - blockers - highs` from the
  harness return, summed over the rounds, plus the exit round's blockers — and that the batch is
  promoted by one `--rescope --act add` per unit. Rendered into `.claude/skills/unattended/SKILL.md`.
  Observed by AC3.
- **S3** — `tools/unattended/VERBS.template.md`'s `--review` entry names `--highs` and `--minors`,
  where they are required and refused, and the unit floor. Rendered into
  `memory/guides/UNATTENDED-VERBS.md`. The driver's usage header line moved to
  `TOOL-aBatchedMinors-2` at its rev-2. Observed by AC3.
- **S4** — `memory/DECISIONS.md` gains the owner's ruling, minted in this build's TOOL family,
  superseding the closing-review half of the 2026-09-14 severity ruling. The decision log is a shared
  mutable record no dispatched pass may declare, so the row lands in a records commit of its own.
  Observed by AC4.
- **S5** — Every kit whose shipped bytes moved in this build is bumped once, after the last move, in
  every carrier `govkit epoch` names. Observed by AC5.

## 3. Non-goals (OUT)

- Rewording the spec-audit rule beyond splitting the paragraph.
- The governance template: it does not state the disposition.

### Edges

- **consumes-from** `TOOL-aBatchedMinors-2` — the flags and refusals described.
- **consumes-from** `TOOL-aBatchedMinors-3` — the floor described.

## 4. Design

### Evidence

Read at base `5ba0fc4f`. The fold is stated in M4 of the build method, in the Skill's `CONVERGED` and
`NON-CONVERGENT` bullets, and in the verbs entry for `--review`; `grep -n "MEDIUM or LOW"` over the
non-build tree finds those carriers and the driver's own exit note, which `TOOL-aBatchedMinors-2`
owns. The build method measured 27422 bytes against its 30720 cap.

### Files touched (estimate)

- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/DECISIONS.md`

## 5. Production-readiness checklist

- testing — the parity legs prove each render matches its template.
- user docs — this unit is the user docs.
- risks — the method's byte cap; the edit replaces a sentence rather than adding a paragraph.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs after the
  render, it passes.
  Red when: the new paragraph pushes the method past its cap.
- **AC2** — When the `kit/dogfood doc parity` leg runs, the rendered method matches its template.
  Red when: the template is edited and the render is not.
- **AC3** — When `bash tools/unattended/adopt-unattended.sh --check` runs, the rendered Skill and
  verbs entry match their templates, and `grep -c -- "--minors"` over each is non-zero.
  Red when: a carrier still says a closing review's mediums are folded.
- **AC4** — When `grep -n "aBatchedMinors" memory/DECISIONS.md` runs, one row records the ruling and
  names the severity ruling it supersedes for the closing review.
  Red when: the ruling lives only in this build's prompt record.
- **AC5** — When `python tools/govkit/govkit.py epoch` runs at the unit's commit, it reports no
  unbumped move.
  Red when: a touched kit's version marker is left.

## 7. Gates

`build-method size` · `kit/dogfood doc parity` · `unattended skill wiring` · `method carriers (every pointer declared)` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.
- rev-2 · 2026-10-04 · S3 · S4 · building found the usage header is check 26's, so unit 2 took it,
  and `--dispatch` refuses `memory/DECISIONS.md` as a shared record, so the row rides a records commit.

## 10. Reuse audit

The carriers are the ones the rule already lives in; no new document. Their renderers are the
existing parity gates' render modes.

Recall terms used: closing review disposition promote fold severity BLOCKER HIGH MEDIUM LOW unit rescope CONVERGED
