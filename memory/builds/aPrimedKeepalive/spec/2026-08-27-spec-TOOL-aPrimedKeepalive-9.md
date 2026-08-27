# TOOL-aPrimedKeepalive-9 — the acceptance ledger evidences every criterion a fold added

**Status:** INPROGRESS · rev-1 · 2026-08-27 · node a · Tier-1 · base b4e1d5be · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-9-closing-diff.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-9-closing-diff.md) | diff-review | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 |

<!-- /gen:spec-records -->

## 1. Goal

Three review folds ADDED acceptance criteria — unit 1 AC8 and AC9, unit 2 AC9, unit 4 AC6, unit 6
AC5 — and none of them reached the acceptance ledger. Unit 7's fold-added AC6 did, which is what makes
it an omission rather than a convention. Hygiene check 23 reds the push boundary the moment those
units flip to CLOSED, so this is a landing blocker rather than a tidiness item.

## 2. Scope (IN)

- **S1** — every criterion added by a fold gets a ledger line in one of the two legal forms, in the
  journal record that already serves this build.
- **S2** — that record's `**Serves:**` line names the two PROMOTED units as well, since the ledger now
  evidences them.
- **S3** — two stale rows of the record's own Measured table are corrected: the manifest row read
  25 236 to 25 579 against a real 25 118 to 25 417, and the BUILD-METHOD row priced the render rather
  than the template.

## 3. Non-goals (OUT)

- Any change to the criteria themselves. This unit evidences what the folds wrote; it does not
  re-open them.
- A gate asserting that a fold's new criterion reaches the ledger. Check 23 already reds on it at
  CLOSED, which is where it bites, and a second check earlier would be the same question twice.

## 4. Design

PROMOTED from spec-audit round 3 under M4's NON-CONVERGENT exit, alongside `TOOL-aPrimedKeepalive-8`.

The mechanism is check 23's own: a `**Evidences:** <id>` block per unit, one line per numbered
criterion, in the OBSERVED form (a backticked token naming the command, file, flag or test that made
the observation) or the AMENDED form (naming the revision that changed the criterion). There is no
third form and no `N/A`.

**Three criteria in this build are recorded AMENDED rather than observed**, and that is the form
doing its job rather than a gap being hidden: unit 3 AC5 and unit 4 AC2 and AC5 each need a full-leg
run of about twenty-five minutes and this run spent three of them. The ledger says so per line.

## 5. Production-readiness checklist

- security · perf / scale · a11y · i18n · error states · migration — N/A, a record.
- observability — the record IS the observability; that is what check 23 grades.
- risks — writing an observed form for something not observed. The three AMENDED lines are where
  that risk was refused rather than papered over.
- testing + left-shift gates — hygiene check 23, which reds at CLOSED.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When the journal record at `memory/builds/aPrimedKeepalive/build/` is read, every
  criterion a fold added carries a line: unit 1 `AC8` and `AC9`, unit 2 `AC9`, unit 4 `AC6`, unit 6
  `AC5`.
- **AC2** — When `git show b4e1d5be:memory/guides/SESSION-KICKOFF.md | wc -c` and `wc -c` are compared
  against the record's Measured table, the manifest row names the real pair, and the BUILD-METHOD row
  names `tools/memory-tree/BUILD-METHOD.template.md` as the binding half.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at the push boundary with every
  unit CLOSED, check 23 is green over this build's ledger.

## 7. Gates

`memory tree hygiene`, and `bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-27 · PROMOTED from spec-audit round 3 by M4's NON-CONVERGENT exit, specced at its
  tier and built rather than parked.

## 10. Reuse audit

The seam is the ledger grammar itself, already in use by this build's own record and defined at
`memory/HYGIENE.md` under "Acceptance ledger": one `**Evidences:**` line per unit, one line per
criterion, two forms and no third. No mechanism is built — the record is extended in the shape its
reader already grades.

`TOOL-dUnstalledConvoy-11` and `-12` are the units that minted the grammar and the check; this unit
consumes both and adds nothing to either.

Recall terms used: `acceptance ledger evidences journal record observed amended check 23 closed
Tier-2 criterion coverage fold`.
