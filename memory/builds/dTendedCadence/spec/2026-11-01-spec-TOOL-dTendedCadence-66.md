# TOOL-dTendedCadence-66 — the record push's fixture runs with the tracked hooks installed, and a lander's marker leaves its three verdict files intact

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 22 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 37 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H2 with ids 5 (TOOL-dTendedCadence-64) and 26 (TOOL-dTendedCadence-65). Unit
49's fixture is a scratch repository with a bare remote and no `core.hooksPath` (spec-49:158-160), so
no criterion runs `.githooks/pre-push`, whose every run clears the lander's three verdict files
(`.githooks/pre-push:494`). The parity with `write_claim` the spec claims is therefore observed by
nothing. This unit builds the fixture with the tracked hooks and observes the files the hook would
clear.

## 2. Scope (IN)

- **S1** — The fixture. Unit 49's scratch repository sets `core.hooksPath` to the absolute path of this
  repository's `.githooks`, pushes one commit of `main` to its bare remote and records
  `refs/remotes/<name>/HEAD` with `git remote set-head <name> -a`, so the hook observes a default
  branch. Every push-path case of units 49, 64 and 65 runs in it. Observed by AC1.
- **S2** — The marker case. With `push-main-active` and the three files `pre-push-refusal`,
  `pre-push-bar` and `pre-push-allow` planted in the fixture's git dir, each holding one known line,
  `write_record_landing` raises, no ref reaches the bare remote, and the three files are byte-equal to
  what was planted. Observed by AC2.
- **S3** — The hook ran. Without the marker, a successful push leaves `pre-push-refusal` absent, the
  hook's own clear, which shows the hook ran on the push. Observed by AC1.

## 3. Non-goals (OUT)

- The guards themselves: TOOL-dTendedCadence-64 and -65.
- A branch bar's timing: TOOL-dTendedCadence-65 AC2, in this fixture.

### Edges

- **consumes-from** `TOOL-dTendedCadence-49` — the scratch repository and bare remote of its §6, which this unit equips with the tracked hooks
- **consumes-from** `TOOL-dTendedCadence-64` — the marker refusal and the lock, whose cases run here
- **consumes-from** `TOOL-dTendedCadence-65` — the push by name and the refusal token, whose cases run here

## 4. Design

The hook path is the repository's own `.githooks`, never a copy, so the fixture runs the hook every
push from a governed git dir runs. The fixture repository sits under `%TEMP%` with a short name, as
unit 49 §6 states. A planted `pre-push-refusal` that survives a push is the observation that the hook
did not run, which S3 turns into a red. Where the hook needs a file of the scratch tree to reach its
non-default exit (`.githooks/pre-push:1166`), the fixture copies that file and the case names it.

### Files touched (estimate)

- `tools/drift-audit/selftest.py`: S1 to S3

## 5. Acceptance criteria

- **AC1** — When `git -C <fixture> config core.hooksPath` runs in the fixture the selftest builds, it
  prints the absolute path of this repository's `.githooks`; and after a successful
  `write_record_landing`, a `pre-push-refusal` planted before the call is absent.
  Red when: the fixture carries no hook, so a push that skips it passes.
- **AC2** — When `write_record_landing` runs with `push-main-active` and the three verdict files
  planted, it raises naming the marker, `git -C <bare> for-each-ref refs/gov/` prints nothing, and
  `cmp` of each verdict file against its planted copy exits 0.
  Red when: a record push clears a landing's verdict.

## 6. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · the tracked hooks as `core.hooksPath` and a planted lander marker with three verdict files, staged against a push that tests no marker · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 37 (HIGH, item H2) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

The seam is unit 49's §6 fixture, extended with the hook path, and `.githooks/pre-push`'s own clear
of its verdict files (`:494`) as the observation. `python tools/codebase-map/reuse_lookup.py "take a
lock before pushing from a git dir"` ranked name stems only, so no existing fixture builder fits.

Recall terms used: `python tools/memory-recall/query.py "how does a push from a governed git dir avoid
clearing the lander's verdict files" --terms "claim-push lock push-main-active marker verdict files
pre-push refusal lander fixture hooksPath"`
