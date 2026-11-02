# TOOL-dTendedCadence-51 — the landing round trip as a drift-audit arm: walk, intake and landing on another clone under another home, the landed record byte-equal

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 21 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-51-deviation-511.md](../build/2026-11-01-build-TOOL-dTendedCadence-51-deviation-511.md) | deviation | — |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 42 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
BLOCKER (the skeptic re-graded it from HIGH), which shares item B1 with id 1 (TOOL-dTendedCadence-49)
and id 28 (TOOL-dTendedCadence-50). Unit 48 S24's re-derivation reads the landing node's
`AUTO_MEMORY_DIR` (`drift_signals.py:476`, expanded per user and per checkout by `resolve_auto_memory_dir`, `drift_report.py:944-953`),
its idle processes and the online remote-CI streak, so no landing on another node or day reproduces
the walk, and unit 48 AC20's fixture inherits the builder's own auto-memory. This unit is the arm that
proves the carried landing is free of all of it: one end-to-end case through the real walk seam and
the real landing verb, on a second clone under another home and auto-memory directory.

## 2. Scope (IN)

- **S1** — The round trip, one case in `tools/drift-audit/selftest.py`. A walk clone writes a record
  from a stdin of at least 70 KiB holding readings routed `red-leg` (TOOL-dTendedCadence-56) with
  their keys, and files its landing through `write_record_landing` (TOOL-dTendedCadence-49) into a
  recording intake stub. A second clone of the same bare remote then runs `maintenance.py land`
  (TOOL-dTendedCadence-50) with the recorded text's four values. Observed by AC1.
- **S2** — The separation. The landing runs with `HOME` and `USERPROFILE` pointed at an empty
  scratch directory, so the auto-memory path `resolve_auto_memory_dir` expands names another
  directory, and in another clone, so its primary checkout differs too; a landing that read the host
  would differ. That the landing reads no clock is TOOL-dTendedCadence-50 AC4's source probe, so a
  landing on a later day is covered without a test clock. Observed by AC1.
- **S3** — The planted mismatch: the same landing with one hex digit of `sha256:` changed is refused
  and writes nothing. Observed by AC2.

## 3. Non-goals (OUT)

- The seam and the verb themselves: TOOL-dTendedCadence-49 and -50.
- The security family's landing: TOOL-dTendedCadence-52.

### Edges

- **consumes-from** `TOOL-dTendedCadence-48` — S24 and AC20, whose round trip this arm observes in place of the re-derivation
- **consumes-from** `TOOL-dTendedCadence-49` — `write_record_landing`, the walk half the arm drives
- **consumes-from** `TOOL-dTendedCadence-50` — `maintenance.py land`, the landing half the arm drives
- **consumes-from** `TOOL-dTendedCadence-56` — the record route `red-leg`, whose readings' keys are the `over-pin:` lines the arm compares

## 4. Design

The case builds its repositories under `%TEMP%` with short names, as unit 1's walk fixture does: a
bare remote, the walk clone and the landing clone. It compares two byte strings, the walk's written
file and the landing clone's file at the same path, and the two sets of `over-pin:` lines, both read
with unit 6's `read_newest_record` after the landing clone commits the path.

### Files touched (estimate)

- `tools/drift-audit/selftest.py`: S1, S2, S3

## 5. Acceptance criteria

- **AC1** — When the case runs, the landing clone's `land` exits 0, the file at the record's path is
  byte-equal to the walk clone's, and the `over-pin:` lines `read_newest_record` returns in the
  landing clone equal, in order and count, the keys of the stdin's `red-leg` readings, and that count
  is at least 1.
  Red when: the landing re-derives a reading or reads the host, so the bytes differ, or the landed
  record carries fewer `over-pin:` lines than the walk wrote.
- **AC2** — When the case lands with a `sha256:` value changed in one hex digit, `land` exits 2 and
  `git status --porcelain` in the landing clone prints nothing.
  Red when: a payload whose digest differs is written.

## 6. Gates

`drift-audit selftest` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · a 70 KiB stdin with `red-leg` routes, a second clone, a scratch auto-memory directory and a changed digest, staged against a landing that runs `drift_report.py --readings` · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 42 (BLOCKER, item B1) of the round-1
  spec audit of units 35 to 48.

## 9. Reuse audit

The seam is the drift-audit selftest arm that unit 6's §7 declares, and its scratch-repository
fixtures; the case calls units 49 and 50 by name and adds no helper. `python
tools/codebase-map/reuse_lookup.py "carry a written record to another node under a git ref and land
it"` named no round-trip fixture, so no existing seam fits beyond that arm.

Recall terms used: `python tools/memory-recall/query.py "how does a records-only patch build land a
maintenance record the walk wrote" --terms "records-only patch intake landing maintenance record refs
gov ref parentless commit digest re-derive"`
