# TOOL-cBriefedPilot-16 — the method's pointers name the new layer

**Status:** CLOSED · rev-2 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling · ratified 2026-08-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |

<!-- /gen:spec-records -->

## 1. Goal

Make `memory/guides/BUILD-METHOD.md` point at the directive layer this build installs, in four places
where it already points at something, so a run reading the method whole learns that a waived directive
is relaxed for that run. Every edit is a POINTER; not one of them states a rule the layer's carriers
own.

## 2. Scope (IN)

- **S1** — M8's landing pointer gains `when a build may land` to the list of topics it hands to
  template §1 Landing and to the unattended protocol. One phrase, no new sentence.
- **S2** — M9's `open / parked` row gains `or directive waiver` after the recorded DoD override, so
  the wrap-up derivation reads the fourth parked kind unit 3 writes.
- **S3** — M10 gains a waiver bullet: a directive recorded as waived at preflight is relaxed for that
  run only, and the vocabulary, the act, its record and its limits are the unattended protocol's.
- **S4** — M10 gains a parallelism pointer bullet, **only if unit 15 takes branch A**. It names M6 as
  the carrier and states nothing M6 states.
- **S5** — M10's index stops reading `Two deltas, and no others` and reads a count EQUAL to the number
  of bullets M10 then carries.
- **S6** — the edits land in `tools/memory-tree/BUILD-METHOD.template.md` and
  `memory/guides/BUILD-METHOD.md` is re-rendered from it, never hand-edited.

## 3. Non-goals (OUT)

- **M6's sentence.** Unit 15 owns it, and this unit is sequenced after it because they share a file.
- **Any M8 review-record edit.** The design pass deleted it: M4 already mandates the opening verdict
  line, and a second answer in M8 would be the M1 defect.
- **Restating the waiver mechanism.** The bullet names it and hands off. The eleven handles are the
  Skill's table (unit 9) and the mechanism is the protocol (unit 18).
- **A new M-section.** Four edits to three existing sections; the method's shape is unchanged.

## 4. Design

The waiver bullet points at `memory/guides/UNATTENDED-PROTOCOL.md` with **no section number**,
deviating from the design pass's `§10` spelling. §10 does not exist until unit 18, which is sequenced
after this unit, and the build README's ordering constraint is that nothing may land in a state a
later unit repairs. A document pointer never dangles, costs no line, and is M11's own style — names
here, scopes there.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` and the re-rendered `memory/guides/BUILD-METHOD.md`.

### The measured cost

Two bullets at roughly 180 characters each are +4 lines. S1 fits on M8's 39-character closing line and
S2 grows one table row, so both are +0 lines; the index word is +2 characters. Branch B drops S4 and
costs +2 lines. Against a 236-line file this is 240 or 238 lines, and 244 once unit 15's branch A
lands its own +4 — six lines under M1's 250. The design pass estimated 6 lines for this unit; the
difference is S1 and S2 fitting on lines that already exist.

**M1's 250-line budget is authorial.** Hygiene rule 6 gives `memory/guides/*.md` 750 lines and 61440 B
— the row-document cap of 250 does not apply to this file — and check 16's read path is 68989 B
against a ceiling of 86476. A reviewer counting lines is the only thing holding the budget, which is
why the spend is stated here rather than assumed to be gated.

### Alternatives rejected

Adding the waiver rule to M2, M3 and M4 beside each unconditional obligation it can relax. Rejected:
three copies of one rule is the defect M1 names, and M10 already exists as the section where an
unattended run's deltas are indexed.

## 5. Production-readiness checklist

- security · perf / scale · a11y · i18n · observability — N/A, four pointer edits in a procedure.
- error / empty / loading states — branch B is specified in S4 rather than left to the builder.
- risks — a pointer bullet growing into a restatement. `check-method-carriers.sh` catches a copied
  `## M<n>` heading and nothing catches a paraphrase; the review lens is the control.
- testing + left-shift gates — the parity leg proves the render; leg check 16 arm B (unit 12) resolves
  every cited M-section, which is what keeps S4's pointer live.
- migration / rollback — revert the template and re-render.
- user docs — the method is the doc.

## 6. Acceptance criteria

- **AC1** — The number in M10's index sentence equals the count of M10's bullets, in whichever branch
  unit 15 took.
- **AC2** — M8's landing sentence names `when a build may land` and adds no other clause.
- **AC3** — M9's `open / parked` row names the directive waiver, and the row is still one line.
- **AC4** — `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` is green, so the live copy is
  a render of the template and no placeholder survives.
- **AC5** — `wc -l memory/guides/BUILD-METHOD.md` reads at most 250 and the measured value is written
  into §9. A green rule 6 is not the observation; rule 6 admits 750 for this file.
- **AC6** — `bash tools/memory-tree/check-method-carriers.sh` is green: no carrier gained a copied
  M-section, and no new registry row is needed because the method is not a carrier of itself.

## 7. Gates

`kit/dogfood doc parity` · `method carriers (every pointer declared)` · `memory hygiene (20 checks)` ·
the full bar. No new leg.

## 8. Open questions

none — the fork below is RESOLVED (agent, 2026-08-15, delegated): option (b) — M10's index counts every bullet the section carries.

  An index exists so a reader can check it against what follows, and one that omits its own bullet
  is the same class as the driver comment saying five facts where the protocol pins seven — a defect
  unit 18 is already fixing in this build. The count is four under unit 15 branch A and three under
  branch B; AC1 is the check either way. §8 delegated this to the agent under a standing mandate.

**What does M10's index COUNT?** Options: (a) only deltas that change a rule, leaving the waiver
bullet uncounted — which gives the three the design pass and the build README both state, and makes
the index disagree with the bullets a reader can see; (b) every bullet M10 carries, which gives four
under unit 15's branch A and three under branch B. Recommendation: (b). An index exists so a reader
can check it against what follows, and an index that deliberately omits one of its own bullets is the
same class as the driver comment saying five facts where the protocol pins seven — a defect unit 18 is
already fixing in this build. Resolver: owner, or the agent under the standing mandate if the owner
does not take it. Whichever is picked, AC1 is the check.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md` §1g and §4. Two deviations from that pass
  are argued in §4 and §8: the waiver bullet cites the protocol document rather than its §10, and the
  index count is put to a resolver instead of being fixed at three.

- rev-2 · 2026-08-15 · §8 resolved under the standing mandate for `cBriefedPilot`; the pick and the reasoning are in §8. Header gains the ratified pointer.

## 10. Reuse audit

- **M10 itself** — the seam. It already exists as the index of unattended deltas with two bullets in
  the pointer style this unit copies, so the layer needs no new section anywhere in the method.
- **`tools/memory-tree/kit-dogfood-parity.test.sh`** — the render seam, used unchanged; its `PAIRS`
  already carries the method pair.
- **`memory/project/method-carriers.txt`** — read and NOT extended. The registry lists files outside
  `memory/` that point AT the method; this unit edits the method, so it adds no row. Unit 12 and unit
  18 are the ones that add carriers.

Recall terms used: build method pointer delta unattended waiver directive M10 index wrap-up parked
landing carrier restatement.
