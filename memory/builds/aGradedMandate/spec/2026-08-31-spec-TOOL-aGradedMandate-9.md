# TOOL-aGradedMandate-9 — the leg's two-way Skill join extended to `DOD_NO_OVERRIDE`

**Status:** SPECCED · rev-3 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 |

<!-- /gen:spec-records -->

## 1. Goal

The Skill named one non-overridable Definition-of-Done item where the driver holds two, and nothing
noticed. The leg already joins the Skill's directive table against `DIRECTIVES_CORE` in both
directions, so the machinery for catching exactly this class exists and is pointed at one set. This
unit points it at a second, so `TOOL-aGradedMandate-8`'s correction cannot silently rot back.

## 2. Scope (IN)

- **S1** — Add a check to `tools/unattended/check-unattended.sh` joining `DOD_NO_OVERRIDE`, read
  from the driver, against the members the rendered Skill names in its non-overridable paragraph, in
  BOTH directions: a member the Skill omits and a member the Skill names that the driver does not
  hold are each a refusal.
- **S2** — Anchor the Skill side on a stable, greppable marker rather than on prose, since the
  paragraph is English and a substring search over it is the fragile half. The marker is a backticked
  item name inside the paragraph the check selects by heading.
- **S3** — Assert the selected population is NON-EMPTY, so a moved heading fails loudly instead of
  disarming the check — the vacuous-selector class the charter names.
- **S4** — The check's own header states what it does NOT check: that the paragraph's PROSE is
  correct, only that the member set matches.
- **S5** — Declare the check in whatever count or arms pin the leg carries, so adding it does not
  red an existing floor.

## 3. Non-goals (OUT)

- **No join over the full `DOD_CORE` set.** The Skill deliberately does not enumerate the core
  Definition-of-Done set, and demanding it would create a fourth copy of a set that already has
  three.
- **No re-implementation of the directive join.** The existing two-way join is the pattern; this is
  a sibling using the same shape, not a generalisation of it into one parameterised checker.
- **No adopter-facing declaration.** `DOD_NO_OVERRIDE` is kit-owned with no conf channel and stays
  that way.

## 4. Design

### Data model

No new fact. The driver side is `core_of`-style extraction of the `DOD_NO_OVERRIDE` constant, which
the leg already does for `AUTH_MODES`, `SECOND_ANCHOR_MODES`, `PARK_KINDS` and the three core sets.
The Skill side is the backticked names inside one selected paragraph.

### Inventory

| Site | Change |
|---|---|
| `check-unattended.sh` | the new check, beside the directive join |
| `check-unattended.test.sh` | a Skill-omits arm, a Skill-invents arm, a moved-heading arm |
| `tools/unattended/SKILL.template.md` | already carries both names after `TOOL-aGradedMandate-8` |

### Migration

The check is green only after `TOOL-aGradedMandate-8` lands, so the two are ordered and the ordering
is recorded in the build order rather than left to chance.

### Alternatives rejected

Rendering the set into the Skill from the driver at adopt time. Rejected: `adopt-unattended.sh`
substitutes DECLARED project values, and a kit constant rendered through the adopter would make the
Skill's bytes depend on the driver's source, which the parity legs then compare in a third direction.
A join is cheaper and states the relation instead of hiding it in a substitution.

## 5. Production-readiness checklist

- security — N/A. Reads two tracked files.
- perf / scale — N/A. Two greps on a leg that already makes many.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — S3 makes an empty selection a refusal.
- observability — the refusal names the missing or invented member and both file paths.
- risks — a prose-anchored check is brittle; S2's marker and S3's non-empty assertion are the
  mitigations, and the header states the residual.
- testing + left-shift gates — three arms, each observed RED first.
- migration / rollback — deleting the check.
- user docs — none owed; the check is a leg.

## 6. Acceptance criteria

- **AC1** — When the rendered Skill names only `authorization-reachable` in the selected paragraph,
  `bash tools/unattended/check-unattended.sh` fails naming the omitted `pieces-complete`.
- **AC2** — When the Skill names an item the driver's `DOD_NO_OVERRIDE` does not hold, the check
  fails naming that item.
- **AC3** — When the paragraph's heading is renamed so the selector matches nothing,
  `bash tools/unattended/check-unattended.sh` fails with an empty-population refusal rather than
  passing.
- **AC4** — On the tree at HEAD with `TOOL-aGradedMandate-8` landed, the check passes.
- **AC5** — `bash tools/unattended/run-unattended-gates.sh --selftests` reports the leg suite green,
  and any arms floor the suite pins is moved in the same commit with its reason.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F10 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`, its machine half.
- rev-3 · 2026-08-31 · round-2 fold of R11: this header read rev-1 over a rev-2 log, which
  `check-memory-hygiene.sh:919` cannot see because it fires only on a header AHEAD of its log.
- rev-2 · 2026-08-31 · round-1 fold of the spec audit's F19: the prose count in section 3 replaced
  with a name, since the set is eleven by the time this unit lands.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is the directive join at `tools/unattended/check-unattended.sh:1289` — it already reads a
kit constant out of the driver, already selects a table out of the rendered Skill, and already
refuses in both directions. This unit copies that shape for a second set rather than parameterising
it, because the two selectors differ (a markdown TABLE against a paragraph) and one predicate serving
two callers whose edges disagree is the failure recorded in `TOOL-dUnstalledConvoy-23`.

`core_of` is the existing driver-constant reader and is reused; its own refusal text records that it
reads a double-quoted value only, so `DOD_NO_OVERRIDE`'s declaration must stay quoted and that is
asserted rather than assumed.
