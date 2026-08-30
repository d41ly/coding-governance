# TOOL-aGradedMandate-6 — check 24's RETIRE arm keys its baseline to the run's pinned BASE

**Status:** SPECCED · rev-2 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

Check 24 asks whether the scope moved with nothing on the record saying so, and takes its baseline
from the first commit whose run-state file carries a live phase — `BUILDING`, `RUNNING`,
`VERIFYING`, `LANDING` or `LANDED`. `SPECCING`, `REVIEWING`, `FOLDING`, `RESEARCHING` and `TESTING`
are all before that line, so a unit authored `WONTDO` while speccing is already retired at the
baseline and owes no row. This unit keys the RETIRE arm to the run's pinned BASE, where the owner's
authorization actually sits, and leaves the ADD arm exactly as it is.

## 2. Scope (IN)

- **S1** — Add `pinned_units` beside `baseline_units` in `tools/unattended/lib-unattended.sh`: the
  build README's units region as it stood at a NAMED commit, with the same cutoff handling and the
  same refusal shapes.
- **S1a** — `pinned_units` VALIDATES its commit before the blob read: a value shorter than 7 hex, or
  one failing `GIT cat-file -e "<c>^{commit}"`, is its own named refusal. This is not inherited from
  the sibling and is the one shape `same refusal shapes` naturally omits, because the sibling CHOOSES
  its commit and this one is GIVEN one. An empty value does not fail the read — `GIT show ":<path>"`
  is INDEX syntax and succeeds, verified live on this tree — so an absent or truncated `base:` would
  silently grade the working index instead of the pinned BASE, and S3's skip would never fire because
  the read returned plausible bytes. That is the same degeneration the driver's own
  `closing-review-recorded` header records from `check_authorization`.
- **S2** — Point check 24's RETIRE loop at `pinned_units "$rb" …` while the ADD loop and the
  supersession-successor loop keep `baseline_units`.
- **S3** — Report the two baselines separately when either is unreadable, so a skip names which
  question could not be asked rather than skipping the whole check. THREE distinguishable skips: the
  ADD baseline unreadable, the RETIRE baseline unreadable, and the RETIRE commit refused by S1a's
  validation. Today a `baseline_units` failure skips all three loops at once, including the
  supersession-successor loop, and removing that whole-check skip is what S3 is for.
- **S4** — State in the arm's header why the two arms take different baselines: M2 MANDATES
  authoring an absent spec, so an addition is expected between BASE and BUILDING and a retirement is
  not.
- **S5** — Refuse a retirement that is WONTDO at the pinned BASE only when it is ALSO absent from
  the rescope rows, unchanged — the arm's exemption logic is correct and only its baseline moves.

## 3. Non-goals (OUT)

- **No change to the ADD arm.** Its BUILDING baseline is load-bearing and its own header states why;
  moving it would red a run for obeying the method.
- **No change to `verb_rescope`.** The driver's own membership question is about the CURRENT region
  and is a different question with a different answer, which is exactly the pair that was
  unsatisfiable together before `TOOL-dUnstalledConvoy-33`.
- **No retroactive red.** No live instance of the SPECCING drop exists in this corpus, which the
  review's skeptics confirmed by re-reading `aBoundedCeiling`; this closes a shape.

## 4. Design

### Data model

No new fact. `pinned_units` reads the same generated region from a blob at a named commit, which
`baseline_units` already does once it has chosen its commit.

### Inventory

| Site | Change |
|---|---|
| `lib-unattended.sh` | `pinned_units`, sharing the blob read with `baseline_units` |
| `check-unattended.sh` check 24 | the RETIRE loop's baseline and the two-way skip report |
| `check-unattended.test.sh` | a SPECCING-drop arm, a legitimate-retirement arm, an unreadable-BASE arm |

Two predicates rather than one parameterised predicate. That is the round-4 conclusion recorded in
`TOOL-dUnstalledConvoy-23` — one predicate serving callers whose edges disagree is what failed four
adversarial rounds — so the shared part is the blob read and the two questions stay two functions.

### Migration

None. Every tracked run-state file is re-graded on the next bar; the arm reds nothing in the current
corpus, which is verified by running the candidate predicate over the real tree before it is wired,
printing hits AND near-misses.

### Alternatives rejected

Widening the live-phase list in `baseline_units` to include `SPECCING`. Rejected: it would move the
ADD arm's baseline too, and an addition before `BUILDING` is the case that arm exists to permit.

## 5. Production-readiness checklist

- security — N/A. Reads tracked blobs through the leg's pinned `GIT()` wrapper.
- perf / scale — one extra `git show` per run-state file, on a leg that already makes several.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — S3: an unreadable baseline is a named skip naming WHICH baseline,
  never a silent pass over both arms.
- observability — the refusal names the unit and says the drop happened before `BUILDING`.
- risks — a leg-side refusal over records no verb can rewrite is the unlandable shape this build
  refuses elsewhere; here it is safe because the predicate reds nothing in the corpus, and that is
  MEASURED before wiring rather than argued.
- testing + left-shift gates — three arms, each observed RED first.
- migration / rollback — reverting the one call site restores the old baseline.
- user docs — none owed; check 24 is a leg, not an agent-facing surface.

## 6. Acceptance criteria

- **AC1** — When a fixture's build README carries a unit that is non-`WONTDO` at the run's pinned
  `base:` and `WONTDO` at HEAD, with no `retire` or `supersede` rescope row, and every phase commit
  is `SPECCING`, `bash tools/unattended/check-unattended.sh` fails check 24 naming that unit.
- **AC2** — When the same fixture carries the `retire` row, the check passes.
- **AC3** — When the pinned BASE does not resolve, `bash tools/unattended/check-unattended.sh`
  reports a skip naming the RETIRE baseline specifically and still evaluates the ADD arm.
- **AC3b** — When `baseline_units` fails and the pinned BASE resolves, the check reports a skip
  naming the ADD baseline specifically and STILL evaluates the RETIRE arm, which is the direction
  that inherits today's whole-check skip.
- **AC3c** — When a fixture run-state file carries a blank `base:`, check 24 reports S1a's named
  refusal rather than a verdict. An empty base RESOLVES, to the git index, so AC3's
  `does not resolve` fixture cannot reach this.
- **AC4** — Running `pinned_units` over every tracked `RUN.md` before the arm is wired prints zero
  hits and its near-misses, recorded in this build's journal record.
- **AC5** — `bash tools/unattended/check-unattended.sh` is green on the tree at HEAD after the
  change.

## 7. Gates

`unattended kit gate` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F4 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`, the leg half.

- rev-2 · 2026-08-31 · round-1 fold of F5 and F14: pinned_units validates its commit before the blob read (S1a), since an empty base resolves to the git INDEX rather than failing; and AC3b covers the mirror direction S3 promises.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is `baseline_units` at `tools/unattended/lib-unattended.sh:150` — it already reads the
units region out of a blob at a chosen commit, already handles `UNITS_REGION_CUTOFF`, and already
returns its refusals as prose on stdout with a non-zero status. `pinned_units` shares that blob read
and differs only in how the commit is chosen.

`rb` is already read in check 24's own neighbourhood and already handed to `baseline_units` as the
fallback commit, so the value this unit needs is in scope at the call site with no new derivation.
`id_in` and `id_rows` in the same library are reused for the membership and status tests.
