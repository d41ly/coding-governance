---
slug: aBlindedTrial
node: a
opened: 2026-09-20
streams: tooling+playbook
roster: TOOL
ids: TOOL-aBlindedTrial-1 TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 TOOL-aBlindedTrial-5 TOOL-aBlindedTrial-6 TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8
authorized-by: prompt
---

# aBlindedTrial — does speccing and auditing before code buy code quality, measured on a blinded trial

## The problem this build exists to solve
Every Tier-2 unit in this repo pays for a spec, an adversarial spec audit and a fold before its
first line of code, and adopters inherit the same rule through the template's §1. Nobody has
measured what that ceremony buys. The owner's standing impression is that sessions often spec after
building, that specs are abstract, and that nothing checks whether code follows them. Two of those
three are answerable from the tree; the third needs a controlled comparison, which has never been
run. Part two, after the trial: the audit measured no quality at 12× the cost, so it becomes opt-in —
owed only when a build README declares `spec-audit: <date>` — in the driver, the harness, the hook
and the method text.

## Expected improvements
- A measured answer to "spec-first or build-first", per token spent, on tasks shaped like this
  repo's own work.
- The retrospective figures — how often the order is honoured, how often the audit precedes code,
  how concrete a spec is — derived by command, not recalled.
- Evidence on which to keep, narrow or drop the §1 design-pass rule in the template.

## Detriments if this is not built
- The most expensive step of every Tier-2 unit keeps running on faith.
- If it buys nothing, adopters keep paying for it; if it buys a lot, the sessions that skip it keep
  shipping worse code and nobody can say so with a number.

## Build-level rules
- **This unit reports; it does not fix.** A template or method change is a follow-up unit with its
  own spec, never a rider on an evaluation.
- **Every arm works in a scratch cell under the sanctioned temp root, never in this tree.** A cell is
  its own git repository holding the brief and the fixtures; an arm may read nothing outside its
  cell.
- **The acceptance suite is hidden, written from the brief alone, and FROZEN by hash before any arm
  runs.** Its author never sees an implementation; its verifier re-tags any test that asserts more
  than the brief pins.
- **Judges are blind.** Reviewers see a script under a code name and the brief, never the cell, the
  spec or the plan.
- **Every number in the record names the command or file that derives it.** A figure with no
  derivation is not written.
- **Concurrency stays inside the review protocol's bound.** One task's arms run at a time, spec-first
  replicates sequentially, and the audit is the shipped `tier2-review.js` harness.
- **Units 2–5 take no spec audit.** The owner ruled in this session (2026-09-20) that the audit is
  opt-in; this build is the first not to declare it. The M8 closing diff review runs.
- **The core sets do not move.** Removing a member trips every adopter's floor pins; the opt-in is a
  term zero on the grader, the shape the driver already has.

## Parked decisions
- **A fourth task with a deliberately vague brief.** Every brief here pins exit codes, tokens and
  formats, so the case where a spec has the most room to help — a three-sentence owner brief — is
  untested. Options: run the same three arms on one vague brief (≈60 agents), or accept the present
  verdict as bounded to explicit briefs. Not the run's to decide: it is the trial's scope, ratified
  at three tasks on 2026-09-20.
- **A project-wide "audits owed by default" declaration.** The per-build `spec-audit:` key is the
  owner's instrument; an adopter wanting today's rule on every build has no one-line way to say so.
  Options: a conf key that pins the fact for every build, or nothing. Backlog `TOOL-aBlindedTrial-7`.
- **A spec's §7 leg line versus the legs its files trip.** Round 1's F7: unit 4 omitted a leg whose
  guard its own edit tripped. Both inputs are machine-readable. Backlog `TOOL-aBlindedTrial-8`.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBlindedTrial-1` | 1 | a retrospective over every spec in the tree (order, audit-before-code, concreteness, adherence) plus a prospective blinded trial: three tasks × three arms × three replicates, graded by a frozen hidden suite, blind adversarial review, adherence judges and per-arm token cost |
| 2 | `TOOL-aBlindedTrial-2` | 2 | the driver reads `spec-audit:` from the build README at BASE, pins it, and its `specs-audited` grader reports not-owed when absent |
| 3 | `TOOL-aBlindedTrial-3` | 2 | the build harness runs its AUDIT stage only when `specAudit` is declared, and says NOT-OWED otherwise |
| 4 | `TOOL-aBlindedTrial-4` | 2 | the fan-out hook denies a direct spec-audit Workflow call the build README did not declare |
| 5 | `TOOL-aBlindedTrial-5` | 2 | M4 becomes the procedure for a declared audit; the tier rule and one decision row follow |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node a · opened 2026-09-20 · streams tooling+playbook
ids TOOL-aBlindedTrial-1 TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 TOOL-aBlindedTrial-5 TOOL-aBlindedTrial-6 TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBlindedTrial-1 — spec-first versus build-first, measured on a blinded trial](spec/2026-09-20-spec-TOOL-aBlindedTrial-1.md) | 1 | 1 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aBlindedTrial-2 — the driver reads `spec-audit:` from the build README and owes the audit only when it is declared](spec/2026-09-20-spec-TOOL-aBlindedTrial-2.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-20 |
| [TOOL-aBlindedTrial-3 — the build harness runs its AUDIT stage only when `specAudit` is declared](spec/2026-09-20-spec-TOOL-aBlindedTrial-3.md) | 2 | 2 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aBlindedTrial-4 — the fan-out hook denies a direct spec-audit call the build README did not declare](spec/2026-09-20-spec-TOOL-aBlindedTrial-4.md) | 2 | 2 | CLOSED | rev-5 | 2026-09-20 |
| [TOOL-aBlindedTrial-5 — M4 becomes the procedure for a declared audit, and the ruling is recorded](spec/2026-09-20-spec-TOOL-aBlindedTrial-5.md) | 2 | 2 | CLOSED | rev-3 | 2026-09-20 |
<!-- /gen:build-units -->

Records: 5 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aBlindedTrial-1 TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 TOOL-aBlindedTrial-5.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBlindedTrial-1`, `TOOL-aBlindedTrial-2` | yes |
| 2 | `TOOL-aBlindedTrial-3`, `TOOL-aBlindedTrial-4`, `TOOL-aBlindedTrial-5` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
