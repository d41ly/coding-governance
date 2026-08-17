# TOOL-cBriefedPilot-2 — the directive registry, eleven pointers and not one restated rule

**Status:** CLOSED · rev-1 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

Declare the eleven default directives an unattended build runs under, as a kit-owned constant of
`handle:M<n>` pointer pairs that the gate leg's existing parser can read. The registry names rules;
it never states them.

## 2. Scope (IN)

- **S1** — `DIRECTIVES_CORE` in `tools/unattended/unattended.sh`, one `KEY="…"` line in the shape
  `core_of()` already parses, holding eleven space-separated `handle:M<n>` pairs.
- **S2** — a `directives()` accessor composing core plus `DIRECTIVES_EXTRA`, matching the existing
  `phases()` and `dod()` shape, for the membership test unit 3 needs.
- **S3** — `DIRECTIVES_EXTRA=""` declared in `.unattended.conf` and added to the driver's own
  default-init line, so a conf that omits it does not abort under `set -u`.
- **S4** — `DIRECTIVES_FLOOR="11"` in `.unattended.conf`, a separate additive key. `CORE_FLOOR` keeps
  its two-field shape.
- **S5** — one line in `verb_resume` pointing a compacted agent at the Skill's table and at its own
  parked waivers.
- **S6** — a source-level arm asserting that every conf key the driver READS appears in its own
  default-init line, observed RED with the new key removed.

## 3. Non-goals (OUT)

- **Printing the directive list from the driver.** An early design had a `print_directives()`; it was
  cut. At preflight the agent has just read the Skill's table, and at `--resume` a compacted agent
  cannot decode `sub-specced:M2` any better than it could decode nothing. M7's read list is
  explicitly closed.
- **Any gloss, condition or procedure text in the registry.** The value is a handle and a pointer.
  Prose belongs in the Skill's table (unit 9), where a human reads it.
- **The join that proves the pointers resolve.** That is leg check 16, unit 12.
- **Extending `CORE_FLOOR` to a triple.** Rejected on the leg's own recorded failure mode — a single
  malformed value already disarms both shrink-only pins while the conf still looks configured, and a
  third field would make one typo disarm three. It would also require re-cutting the one branch whose
  job is refusing malformed shapes.

## 4. Design

### Data model

`DIRECTIVES_CORE="minimal-prose:M10 sub-specced:M2 forks-resolved:M3 specs-reviewed:M4 reuse-first:M5
parallel-when-disjoint:M6 passes-committed:M6 diff-reviewed:M8 land-once-done:M8
conflicts-reconciled:M8 wrap-up-derived:M9"`

Two handles may point at one section — `parallel-when-disjoint` and `passes-committed` both cite M6 —
because the section is the carrier, not the rule. Three cite M8 for the same reason.

### Why a kit constant and not a conf key

The owner's requirement is MUST-by-default. A conf declaration lets a project declare zero
directives, which is a global waiver carrying no name, no reason and no record — the argument the kit
already wrote for `CORE_FLOOR`. Core is kit-owned and shrink-only; `DIRECTIVES_EXTRA` is where a
project adds.

A registry document was the third option and loses to both: it is a spelling nothing parses, and its
absence reads as silence rather than as a refusal.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the constant, `directives()`, the default-init line, one
`verb_resume` echo) · `.unattended.conf` (two keys) · `tools/unattended/unattended.test.sh` (one arm).

### Alternatives rejected

A four-key conf split naming the carrier and its anchors was proposed and loses: `verb_resume`
already derives the build-method path from `MEMORY_ROOT` with no declaration, so the carrier needs no
key.

## 5. Production-readiness checklist

- security — N/A, a constant and a membership test.
- perf / scale — N/A.
- a11y · i18n — N/A, no user surface.
- error / empty / loading states — an undeclared `DIRECTIVES_EXTRA` must not abort the driver; S3 and
  S6 are that control.
- observability — one `verb_resume` line; nothing else prints.
- risks — the two init lists in the driver and the leg already disagree today and nothing pairs them.
  S6's arm catches the CLASS rather than this instance.
- testing + left-shift gates — the arm in S6; the pointer join is unit 12.
- migration / rollback — additive. No verb reads the registry until unit 3 lands.
- user docs — the Skill's table, unit 9.

## 6. Acceptance criteria

- **AC1** — When `.unattended.conf` omits `DIRECTIVES_EXTRA`, `--status` runs with no unbound-variable
  error.
- **AC2** — When `--resume` runs on a live fixture, it prints the one-line pointer at the Skill's
  table and the parked waivers.
- **AC3** — When the new key is removed from the driver's default-init line, the S6 arm is observed
  RED; with it present, green.
- **AC4** — `core_of()` in the leg returns eleven pairs from the new constant without modification to
  the parser.

## 7. Gates

`unattended driver selftest` · `unattended kit gate` · `harness arms`.

## 8. Open questions

none — the forks this unit could have carried were taken in the design pass. FORK A resolved to a kit
constant, FORK E to a separate `DIRECTIVES_FLOOR`, and both are recorded in the build README with the
evidence.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds C14, D8 and D13 from that pass.

## 10. Reuse audit

- **`core_of()` in `tools/unattended/check-unattended.sh`** — the parser. It reads a `KEY="…"` line
  out of the driver rather than sourcing it, because sourcing a script whose tail runs a verb would
  run the verb. The registry adopts that exact shape so the parser needs no change, which is the
  seam this unit wires through.
- **`phases()` and `dod()` in the driver** — the core-plus-extra composition. `directives()` is the
  third instance of a shape that already has two.
- **`CORE_FLOOR`'s shrink-only pin** — the precedent for `DIRECTIVES_FLOOR`, copied in behaviour and
  deliberately not in spelling.

Recall terms used: unattended directive registry core floor shrink-only phases dod conf declaration
extension point kit-owned parser membership.

No existing seam holds a directive vocabulary; the three above are the machinery it is built from.
