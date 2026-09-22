# TOOL-aGradedMandate-4 — `build-complete` refuses a CLOSED unit whose spec grades THIN

**Status:** CLOSED · rev-3 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md) | journal | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 |
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-prompt-TOOL-aGradedMandate-1-owner-brief.md](../prompts/2026-08-31-prompt-TOOL-aGradedMandate-1-owner-brief.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 |
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 |
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-5 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

`plan_state` already grades a spec THIN when its §2 Scope, §6 Acceptance criteria or §7 Gates is
empty or names nothing observable — the kit's own predicate for "too thin to build against". Its one
caller computes that grade and overwrites it a line later with `DONE` the moment the unit's status is
terminal. This unit makes `build-complete` read the grade before the status hides it, so a unit
cannot be CLOSED against a spec that never said what done was.

## 2. Scope (IN)

- **S1** — Add a sixth term to `dod_met`'s `build-complete` arm: for every unit id in the generated
  region whose status is `CLOSED`, run `plan_state` over that unit's spec and refuse the item when
  the grade is `THIN`.
- **S2** — Order it AFTER the five existing terms, so a structural failure still reports as a
  structural failure and this term never masks one.
- **S3** — A `DOD_OUT` message naming each thin unit. It does NOT name which of the three sections
  is empty: `plan_state`'s per-section map is built and consumed inside its own awk `END` block and
  the caller receives one bare token, and §3 forbids widening that output because the function body
  is SLICED out of the shipped bytes and graded by two harnesses, `unattended.test.sh` and the
  cross-kit `marker-contract.test.sh`. A second section-emptiness derivation beside `plan_state`
  would be a second spelling of M2's THIN rule. The grade is a single token by design.
- **S4** — Date-grandfather the term on the spec's FILENAME date against a new `.unattended.conf`
  key `SPEC_THIN_CUTOFF`, absent or blank meaning "grandfather everything", set to this build's own
  landing date. Two of 307 tracked CLOSED specs grade THIN today, both from a pre-kit July build,
  and a term that reds a landed spec no run may rewrite is unlandable.
- **S5** — At `--plan`, print the grade BESIDE `DONE` rather than in place of it, so the discard
  stops being silent for a human reader too.
- **S6** — Declare `SPEC_THIN_CUTOFF` in FOUR places, for three different reasons, and the reasons
  do not overlap. **Check 22's three-way key join** needs two of them: the kit example
  `tools/unattended/.unattended.conf.example`, and the row in the protocol's §8 declaration table —
  the check computes `documented but in no example` as a `comm` between those two populations, and a
  key in one and not the other reds `unattended kit gate`. **`set -u`** needs the third: the driver's
  conf-default init block at `unattended.sh:288-291`, because every conf key the DRIVER reads is
  defaulted there and this one is read in `dod_met`. **This project's own declaration** is the
  fourth, `.unattended.conf`, which is what actually sets the date.
  The sibling cutoffs are not carried identically and the difference is worth knowing before copying
  one: `UNITS_REGION_CUTOFF` is a driver key and is defaulted at `unattended.sh:289`, while
  `LANDED_ANCHOR_CUTOFF` is a LEG key and is defaulted at `check-unattended.sh:118`. This key is
  read by the driver, so it follows the first.

## 3. Non-goals (OUT)

- **No change to `plan_state` itself.** Its three-section predicate is M2's classification and this
  unit computes nothing new.
- **No leg-side clause.** The grade is a property of a build's own specs at close time; a leg
  sweeping every tracked spec would grade builds this item never bound, including the two July ones.
- **No Tier-1 widening.** Whether a Tier-1 spec should carry §7 at all is memory hygiene's question,
  not this kit's, and the tier-blindness proposal is backlogged rather than built here.

## 4. Design

### Data model

No new fact. One new declaration, `SPEC_THIN_CUTOFF`, in `.unattended.conf`, following the idiom
`UNITS_REGION_CUTOFF` and `LANDED_ANCHOR_CUTOFF` already establish in that file: a date, absent or
blank grandfathers everything, moving it later re-admits more.

### Inventory

| Site | Change |
|---|---|
| `unattended.sh` `dod_met` `build-complete` | the sixth term |
| `unattended.sh` `verb_plan` | the grade printed beside `DONE` |
| `.unattended.conf` | `SPEC_THIN_CUTOFF`, with its reason beside it |
| `tools/unattended/.unattended.conf.example` | the key, blank, with the grandfather semantics beside it |
| `PROTOCOL.template.md` §8 · `memory/guides/UNATTENDED-PROTOCOL.md` §8 | the declaration-table row check 22 joins the example against |
| `unattended.sh:288-291` conf-default init block | the key defaulted, or `set -u` aborts the driver |
| `PROTOCOL.template.md` §8 · `memory/guides/UNATTENDED-PROTOCOL.md` §8 | one declaration-table row |
| `unattended.test.sh` | a thin-and-CLOSED arm, a thin-but-grandfathered arm, a fat arm |

### Migration

The cutoff is the whole migration. The two July specs predate it and stay green.

### Alternatives rejected

Refusing at `--phase CLOSED`. There is no such verb — a unit's status lives in its spec header, which
the driver never writes — so the refusal has to sit where the roster is read, which is
`build-complete`.

## 5. Production-readiness checklist

- security — N/A. Reads tracked spec bytes.
- perf / scale — one `plan_state` call per CLOSED unit, at close only. `verb_plan` already makes the
  same call per unit on every invocation.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — a unit whose spec cannot be resolved is already reported by the
  existing `missing_units` term, which runs first.
- observability — the message names the unit and the empty section.
- risks — the term is inside an overridable item, so a deliberate thin unit is a recorded decision.
  A declared cutoff whose value is absent turns the term off entirely, which is announced.
  **The cutoff's VALUE is not shape-checked**, and that is deliberate rather than overlooked: neither
  sibling cutoff is either, and building the first cutoff-shape validator in this leg is a change to
  a file this unit inventories as untouched. A malformed value therefore sorts as an ordinary string
  and grandfathers unpredictably. Stated here rather than discovered, and it is the one residual this
  unit ships with.
- testing + left-shift gates — five arms (AC1, AC2, AC3, AC6, AC7), each observed RED first where a
  red is reachable; AC3's clean-roster arm is a control and is stated as one.
- migration / rollback — deleting the term, or blanking the cutoff, reverts it.
- user docs — none owed; the Skill does not enumerate `build-complete`'s terms.

## 6. Acceptance criteria

- **AC1** — When a unit is `CLOSED` and its spec's §6 Acceptance criteria section is empty,
  `--close` blocks on `build-complete` naming that unit, verified by an arm in `unattended.test.sh`.
  The message names the UNIT and not the section, for the reason S3 gives.
- **AC2** — When the same spec's filename date is before `SPEC_THIN_CUTOFF`, the item is MET and the
  grandfather is announced.
- **AC3** — When every CLOSED unit's spec grades READY under `plan_state`, the item is MET and
  nothing is printed.
- **AC4** — `bash tools/unattended/unattended.sh --plan <slug>` prints the THIN grade beside `DONE`
  for a closed thin unit rather than replacing it.
- **AC5** — `bash tools/unattended/check-unattended.sh` stays green with the new key declared in
  all three carriers, which is what check 22's three-way key join asserts.
- **AC6** — When a fixture is BOTH structurally broken and thin — a unit whose spec is missing AND a
  second unit that is `CLOSED` and thin — `--close` reports the missing-unit failure and NOT the
  THIN grade, which is what S2's ordering requirement means in behaviour.
- **AC7** — Running the driver with `SPEC_THIN_CUTOFF` unset in the conf does not abort under
  `set -u`, verified by an arm in `unattended.test.sh`.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F9 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.

- rev-2 · 2026-08-31 · round-1 fold of F7, F15 and F16: SPEC_THIN_CUTOFF gains its two missing carriers (S6), AC6 observes the term ORDERING S2 requires, AC7 the set -u default, and AC5's orphaned shape clause is dropped with the residual stated in section 5.

- rev-3 · 2026-08-31 · round-2 fold of R6, R9 and R10: S3 stops promising a section name plan_state cannot emit past its own awk END block, S6 names check 22's actual join plus the set -u default and corrects a false claim about the sibling cutoffs, and section 5's arm count follows the criteria that now exist.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is `plan_state` at `tools/unattended/unattended.sh:1589`, which already computes exactly
this grade and is already reached from `build-complete`'s own neighbourhood through `unit_ids_of` and
`missing_units`. Nothing new is derived; an existing derivation stops being discarded.

The cutoff idiom is `UNITS_REGION_CUTOFF` in `.unattended.conf`, whose header states the reason a
date is used rather than a boolean and why moving it in either direction is visible. That header is
the template for this key's, and the parallel `.memory-tree.conf` family (`SPEC10_CUTOFF`,
`SPEC_WITNESS_CUTOFF`) is the prior art for grandfathering a spec rule by FILENAME date rather than
by commit date.
