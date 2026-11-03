# TOOL-dCalibratedLens-45 — a render error in the shape arm is that form's FAIL line, and a shape with no distinct second form is rendered once and said so

**Status:** OPEN · rev-1 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 14 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dCalibratedLens-45-deviation-451.md](../build/2026-11-03-build-TOOL-dCalibratedLens-45-deviation-451.md) | deviation | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 27, HIGH, of the round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`). The report merges ids 12 and 27
into its item H3; id 12 is `TOOL-dCalibratedLens-44`. Unit 31's shape arm renders each definition
twice, all placeholders filled and only those outside every group filled. Under its staged break
(S1 reverted) `render_shape_line` raises `RolesError` on `returned`'s second form, since `units` sits
only inside a group, and unit 31 never says whether that is a FAIL or an abort of the suite. And for
`SPEC` the second form is the first, because `<ids|none>` sits both inside and outside the group, so
the arm asserts one line twice and reads it as two observations. This unit fixes the arm's failure
envelope: a render error is that form's FAIL line and the arm goes on, and a shape whose two forms
coincide is rendered once and named. It repairs `TOOL-dCalibratedLens-31`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 31's text (rev-2, id 27): S2
  names this unit's envelope, and AC3's staged red lists the `returned` second form's `RolesError`
  as a FAIL line beside the guard's and the bracket assertion's refusals. Observed by AC1.
- **S2** — The render error. In unit 31's shape arm of `tools/hooks/format-guard.test.sh`, the python
  step renders each form inside its own `try`; a `RolesError` prints
  `FAIL shape <head> <form> — RolesError: <message>` in place of that form's line, counts as that
  form's failed assertion, and the step goes on to the next form. Any other exception is the step's
  own crash, printed by name, and fails the arm as a whole. Observed by AC1 and AC2.
- **S3** — The second form. The step builds the second form's dict from the placeholders outside
  every `[ · …]` group. When that dict equals the full form's, the definition is rendered once and
  the arm prints `ok   shape <head> — one form, every group placeholder also outside`; the floor
  counts it once. Observed by AC3.

## 3. Non-goals (OUT)

- The bracket assertion: `TOOL-dCalibratedLens-44`, id 12.
- A sample value per placeholder. One sample, `x`, fills every field, as unit 31 S2 states; the forms
  differ in which fields are filled, never in their values.
- The arm's home and its UTF-8 pipe: id 6 and id 14, `TOOL-dCalibratedLens-48`, landing on unit 31 S2.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-31` — the shape arm's python step and its two forms, whose failure envelope this unit states; without the arm there is no form to render

## 4. Design

### Evidence

- `tools/roles/handoff.py:708-719` at base: `render_shape_line` raises `RolesError` naming a
  placeholder its dict lacks, for every placeholder of the definition.
- `AGENTS.md:63` and `:65`: `<ids|none>` sits both outside and inside the `SPEC` group; `<units>` of
  unit 25's `returned` group sits only inside it. `AGENTS.md:57`: the `merged` group holds no
  placeholder, so both of its forms carry the group.
- The review's probe (finding id 9's row): only `returned`'s `<units>` raises under the staged break.

### The forms at base, by shape

| Shape | Group placeholders | Second form |
|---|---|---|
| `SPEC` | the ids placeholder, also outside | one form |
| `merged` | none | one form |
| `returned` (unit 25) | `units`, only inside | distinct; raises under the staged break |
| every other shape | no group | one form |

### Inventory

No identifier is minted.

### Files touched (estimate)

- `tools/hooks/format-guard.test.sh` — S2 and S3

### Alternatives rejected

- **Abort the suite on a render error.** One raising shape would hide every later shape's verdict,
  and the floor would read the shortfall as unreachable arms rather than as the failure it is.
- **Render the second form always.** Two identical assertions on one line inflate the floor with an
  observation that adds nothing.

## 5. Production-readiness checklist

- security — N/A: a test arm.
- perf / scale — at most one extra render per definition.
- error / empty / loading states — a render error is a FAIL line; an unexpected exception fails the
  arm by name; a fence with no shape is unit 31's floor's to catch.
- observability — each FAIL line names the shape, the form and the error.
- risks — a shape gaining a group whose placeholder sits only inside it: its second form becomes
  distinct and is asserted, with no edit to the arm.
- testing — AC1 to AC3 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the arm runs from the hooks kit directory with unit 31's group handling staged out
  of `render_shape_line`, it prints `FAIL shape returned` naming `RolesError` and `units` for the
  second form, and still prints a verdict for every later shape of the fence.
  Red when: the error aborts the suite, or the form passes.
  permission: the arm is unit 31's, built at order 13.
- **AC2** — When a `python -c` probe runs the step's per-form `try` over a planted definition naming
  a placeholder absent from both dicts, it prints one FAIL line per form and exits 0.
  Red when: the step exits on the first `RolesError`.
- **AC3** — When the arm runs over the live fence, it prints the `one form` line for `SPEC` and for
  `merged`, and two verdicts for `returned`.
  Red when: `SPEC` is asserted twice, or `returned`'s second form is not rendered.

## 7. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/hooks/format-guard.test.sh · covers AC1 AC3 · the shape arm's per-form envelope, staged red by `render_shape_line` with its group handling taken out, which raises on `returned`'s second form · FLOOR_ASSERTIONS counted once per distinct form

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, promoted from id 27 (HIGH, item H3, shared with id 12) of the
  round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`; unit 31 amended at the
  disposal (its rev-2).

## 10. Reuse audit

The seam extended is unit 31's shape arm and its python step, and the error class is the roles kit's
own `RolesError`. `python tools/codebase-map/reuse_lookup.py "turn a render error into a failing
assertion line and continue"` ranked `fail` (shell helpers across the kits), `render` and
`check_line` by name stem; the suite's own FAIL-line convention is the one this arm already uses, so
no seam fits beyond it.

Recall terms used: `python tools/memory-recall/query.py "how is a rendered shape line held to the
format guard regex" --terms "buildShapeRegex render_shape_line bracket group staged break format guard
arm RolesError FLOOR_ASSERTIONS"`
