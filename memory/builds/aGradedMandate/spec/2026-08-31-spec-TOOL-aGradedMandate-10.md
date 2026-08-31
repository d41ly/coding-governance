# TOOL-aGradedMandate-10 — the history side of the parked split subtracts acts too

**Status:** CLOSED · rev-3 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md) | journal | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-11 |
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-11 |
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-11 TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-5 |
| [2026-08-31-review-TOOL-aGradedMandate-10-promotion-audit.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-10-promotion-audit.md) | spec-audit | TOOL-aGradedMandate-11 |

<!-- /gen:spec-records -->

## 1. Goal

PROMOTED, not authored: round 2 of this build's spec audit exited `NON-CONVERGENT`, and its blocker
R1 became this unit rather than a fold. `TOOL-aGradedMandate-5` makes the OWED side of the parked
split act-aware; `park_kinds_unowed` still subtracts at KIND granularity, so a
`rescope · item retire …` row matches BOTH alternations and `--status` reports one retirement as an
unanswered decision AND as a note. This unit makes the history side subtract the owed ACTS too, and
adds the partition invariant that gates the class rather than the instance.

## 2. Scope (IN)

- **S1** — `park_kinds_unowed` at `unattended.sh:3352` stops being a pure kind-difference. A
  `rescope` row is HISTORY only when the first token of its item field is outside `PARK_ACTS_OWED`;
  every other kind keeps the existing kind-granular complement.
- **S2** — `verb_status`'s history count at `:2628` reads that predicate, so the printed
  `· parked N · noted M` is a PARTITION of the parked rows rather than two overlapping counts.
- **S3** — The PARTITION INVARIANT becomes an arm: over a fixture record holding one row of every
  member of `PARK_KINDS`, `parked + noted` equals the row count. That arm gates the CLASS — any
  future kind or act landing in both alternations or in neither — where an arm about `retire`
  specifically would gate this instance only.
- **S4** — The complement rule is restated in `park_kinds_unowed`'s own header on BOTH axes, since
  the one-axis sentence is what produced this defect and the function is where a later reader looks.

## 3. Non-goals (OUT)

- **No change to `PARK_KINDS_OWED` or `PARK_ACTS_OWED`.** Both are `TOOL-aGradedMandate-5`'s and this
  unit consumes them.
- **No change to the leg.** `check-unattended.sh:366-371` and `:1943-1951` read
  `PARK_KINDS_OWED`, which still holds bare kinds; nothing there sees this edit.
- **No new act vocabulary.** `verb_rescope`'s act case at `unattended.sh:3882` stays the writer's
  closed set.

## 4. Design

### Data model

No new fact and no new declaration. One predicate changes from a set difference over kinds to a
difference over kinds PLUS a positional test on the `rescope` kind's first item token.

### Inventory

| Site | Change |
|---|---|
| `unattended.sh:3352` `park_kinds_unowed` | act-aware history side, and its header on both axes |
| `unattended.sh:2628` `verb_status` history count | reads the new predicate |
| `unattended.test.sh` | the retire-not-noted arm and the partition arm |

`park_kinds_unowed` currently returns a WORD LIST that `kinds_re` turns into an alternation, and a
positional act test does not fit a word list. The shape is therefore a predicate the counter applies
per row rather than a widened alternation, and `kinds_re` is left alone — it is `verb_status`'s owed
site and `TOOL-aGradedMandate-5` already took it.

### Migration

None. The only behaviour that changes is a count printed by `--status`, and no record stores it.

### Alternatives rejected

Excluding `rescope · item (retire|supersede) ` positionally in the NOTES alternation and leaving
`park_kinds_unowed` alone. Rejected: the function is the declared home of the history class and a
second exclusion beside it is a second answer to one question — the defect
`TOOL-aGradedMandate-5`'s own §10 was folded for.

## 5. Production-readiness checklist

- security — N/A. A count printed by a status verb.
- perf / scale — N/A. One predicate per parked row on a file already read whole.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — a record with no parked rows prints NEITHER field. `verb_status`
  omits `parked` at zero (`unattended.sh:2618-2619`) and `noted` at zero (`:2629`), by the design its
  own comment at `:2615` states, and `unattended.test.sh:2840` already pins that. The partition arm
  must therefore read an ABSENT field as zero rather than expect a printed `0`, which is stated here
  because assuming the printed form is how this arm would pass against nothing.
- observability — `--status` is the observability, and this unit is the reason its two numbers add
  up.
- risks — the ONLY consumer of `park_kinds_unowed` is `verb_status`, verified by grep, so the blast
  radius is one line of output. If a later reader adds a second consumer expecting a word list, the
  header S4 rewrites is what tells them.
- testing + left-shift gates — two arms, both observed RED against the pre-change predicate first.
- migration / rollback — reverting the predicate restores the overlap.
- user docs — none owed; `--status`'s output shape is not documented in the Skill.

## 6. Acceptance criteria

- **AC1** — Over a fixture record holding exactly one `rescope · item retire TOOL-x-1 · reason …`
  row, `bash tools/unattended/unattended.sh --status <slug>` prints `parked 1` and does NOT print a
  non-zero `noted`, verified by an arm in `unattended.test.sh`.
- **AC2** — Over a fixture record holding one row of every member of `PARK_KINDS`, **whose
  `rescope` row's act is `retire`**, the printed `parked` and `noted` counts SUM to the number of
  parked rows. The act is PINNED because with `add` the arm is green before the fix — an `add` row is
  owed by neither alternation, so the counts already partition — and a class arm that passes against
  the defect is the shape this build has now produced three times.
- **AC3** — Both arms are observed RED against the predicate as `TOOL-aGradedMandate-5` leaves it,
  and that observation is recorded in this build's journal record before the fix lands.
- **AC4** — `grep -c 'park_kinds_unowed' tools/unattended/unattended.sh` returns exactly **2**
  after this unit lands — one definition and one consumer — and **it returns 2 today**, measured
  before the edit. The criterion is therefore a NO-CHANGE assertion and says so: it fails if this unit
  adds a second consumer, which is the risk §5 names. A grep-shaped criterion carries its measured
  pre-edit value or it is an assertion about nothing.
- **AC5** — AMENDED at rev-3. `bash tools/unattended/check-unattended.sh` is GREEN, observed. The
  second half named `bash tools/unattended/run-unattended-gates.sh --selftests`, which the owner
  instructed this run to skip mid-build; the driver suite that actually exercises this unit's code
  is green, and the wrapper's other suites are unrun.

## 7. Gates

`unattended kit gate` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · PROMOTED from round 2 of the spec audit, blocker R1, per the build method's
  M4 exit rule: the loop went 2 blockers then 2 blockers, did not shrink, and stopped
  `NON-CONVERGENT`, so every blocker still standing becomes a unit rather than a fold.

- rev-2 · 2026-08-31 · promotion-audit fold of H2, H3, M1 and M2. AC2's partition fixture PINS the rescope act to retire, because with add the arm is green before the fix; AC4 carries its measured pre-edit value of 2 and declares itself a no-change assertion; section 10 stops claiming a one-row-per-kind fixture the suite does not have; and section 5 stops claiming verb_status prints a zero it in fact omits.

- rev-3 · 2026-08-31 · the acceptance criterion naming `run-unattended-gates.sh --selftests` is AMENDED: the owner instructed this run to skip that suite mid-build, and the criterion now names what WAS observed instead. The acceptance ledger's AMENDED form exists for exactly this case, so the divergence is visible rather than written untruly.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is `park_kinds_unowed` itself at `tools/unattended/unattended.sh:3352`, which is already the
declared home of the history class and already computes it by difference. This unit changes that
computation rather than adding a second exclusion somewhere else, which is what keeps one question
with one answer.

The partition arm has no seam and NEITHER DOES ITS FIXTURE. No arm in `unattended.test.sh` builds a
record holding one row per kind: the nearest build one `decision` plus two `proposal` rows, and the
file carries exactly one raw parked-row append at `:3771`. The verb route cannot produce the set
either — `--abort` terminates the record and an `override` row is written only by `--close` — so the
one-row-per-kind fixture is NEW CONSTRUCTION by direct append, priced here rather than assumed as
reuse.

A STALE hit is recorded rather than trusted: `TOOL-aGradedMandate-5`'s rev-1 §10 named `:3348` and
`:3340` for this function and `kinds_re`; both had drifted to `:3352` and `:3344` and were verified
against source before this spec was written.
