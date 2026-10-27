# TOOL-dWellOiledMachine-72 — runlog verify reports a record whose journal lines retention pruned as `pruned`, never as tampering

**Status:** OPEN · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 3 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-72-deviation-721.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-72-deviation-721.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-79 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 49, item H9, at HIGH. TOOL-dWellOiledMachine-16 S5 prunes every file of `PRODUCER_FILES` to
`runtime.journal` days, 60 by default, and its §4 says no runlog reader changes; but runlog's
`verify` recomputes a committed run's journal commitment from those same files, so every run record
older than the window verifies as `mismatch — the journal changed after the render`, a false tamper
verdict. This unit teaches `verify` to recognise a journal whose head retention removed, report it as
`pruned`, and keep `mismatch` for every other difference.

## 2. Scope (IN)

- **S1** — The `pruned` state. `check_commitment` (`tools/runlog/record.py`) returns
  `("pruned", <why>)` when the recomputed commitment differs from the committed one and every producer
  file the run's commitment draws on begins with a line whose `t` is later than the run's start: the
  lines the commitment hashed sat before the file's present head, which is what
  `write_retained_lines` (16 S5) leaves. `<why>` reads `the journal's oldest line (<utc>) is newer than
  this run's start (<utc>), so retention removed the lines its commitment hashed`. Every other
  difference stays `mismatch`. Observed by AC1, AC2.
  **Readers:** by name: `tools/runlog/record.py` (`check_commitment`) and `tools/runlog/runlog.py`. by value: `tools/runlog/runlog.py`, whose `verify` prints and exits on the state.
- **S2** — The exit. `runlog verify` prints `runlog: verify <record>: pruned — <why>` and exits 0, as
  it does for `none`, since neither is a verdict on the record's integrity; `mismatch` keeps exit 1
  (`tools/runlog/runlog.py:472`). Observed by AC1.
- **S3** — The limit, stated in `check_commitment`'s docstring and in the runlog README's verify
  section: `verify` cannot tell retention from a deletion of a journal file's head; it can tell either
  from an edit, insertion or deletion among the lines that remain. Observed by AC3.
- **S4** — The record corrected. TOOL-dWellOiledMachine-16's §4 says no runlog reader changes; spec 16
  takes a rev bump at this unit's pass naming `check_commitment` and `measure_commitment` as by-value
  readers of the pruned files, its §9 line naming this unit and finding 49. Observed by AC3.

## 3. Non-goals (OUT)

- No change to the prune, its window or `PRODUCER_FILES`: 16 S5 stands.
- No retention of committed runs' lines: §8 F1 rejects it.
- No change to how a commitment is computed or rendered.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-16` — S5's `write_retained_lines` and `journal.py prune`, whose effect on a committed run this unit reads
- **hands-off** `TOOL-dWellOiledMachine-86` — S1's `pruned` predicate, which reads an empty or absent producer file as consistent with it (finding 41)
- **hands-off** `TOOL-dWellOiledMachine-88` — S1's `pruned` predicate, whose population and head that unit defines (finding 61)
- **hands-off** `TOOL-dWellOiledMachine-90` — the combined idle-and-unparseable case over S1's predicate (finding 20)
- **hands-off** `TOOL-dWellOiledMachine-94` — S3's stated limit, which the batch extends to an unparseable line read as deleted (finding 16)

## 4. Design

### Evidence

- `check_commitment` rebuilds the run model from the journal now and recomputes
  `measure_commitment(model, journal_root, count=want["lines"])`, returning `mismatch` on any
  difference (`tools/runlog/record.py:1296-1307`); `measure_commitment` skips a line number outside
  the file (`:1221-1222`) and hashes line bytes, so lines pruned away shorten the recomputed set.
- `runlog verify` exits 1 on `mismatch` and 0 otherwise (`tools/runlog/runlog.py:467-472`).
- 16 S5 applies the cutoff to each file of `PRODUCER_FILES` (`spec-16.md:63-70`).

### Files touched (estimate)

- `tools/runlog/record.py`: S1, S3
- `tools/runlog/runlog.py`: S2
- `tools/runlog/selftest.py`: the aged-record case
- `tools/runlog/README.md`: S3
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-16.md` (S4's rev bump)

### Alternatives rejected

- **Pruning only the `runtime` producer.** The other producers' files then grow without bound, which
  the retention clause 16 S5 carries exists to stop.
- **Keeping every committed run's lines through the prune.** §8 F1.

## 5. Production-readiness checklist

- security — a tamper verdict stays a tamper verdict for every edit among the remaining lines; S3
  states the one case `verify` cannot judge.
- perf / scale — one read of each producer file's first line on a differing commitment.
- error / empty / loading states — an empty producer file reads as having no head, which is
  `mismatch`, never `pruned`.
- observability — the `pruned` line names both instants.
- risks — a deleted head reads `pruned`; S3 says so.
- testing — AC1 to AC3 and the arm in §7.
- migration — none.
- user docs — the runlog README's verify section.

## 6. Acceptance criteria

- **AC1** — When `python tools/runlog/runlog.py verify <record>` runs in a scratch clone holding a
  rendered run record whose journal was then cut by `write_retained_lines` at a cutoff after the run's
  last line, it prints `pruned —` naming both instants and exits 0.
  Red when: the aged record verifies as `mismatch`.
  fixture: needs TOOL-dWellOiledMachine-16's `write_retained_lines`, unbuilt at this base.
- **AC2** — When the same clone's journal keeps every line and one byte of a hashed line is edited
  instead, `verify` prints `mismatch` and exits 1.
  Red when: an edit among the remaining lines reads `pruned`.
- **AC3** — When `grep -n "cannot tell retention" tools/runlog/record.py tools/runlog/README.md` runs,
  both name the limit, and spec 16's §9 carries the rev line naming this unit.
  Red when: either omits the limit.

## 7. Gates

`runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/runlog/selftest.py · covers AC1 AC2 · the pruned and edited cases staged against today's `check_commitment`, which reads both as `mismatch` · none

## 8. Open questions

- **F1 — How does a pruned record verify?** (a) `verify` reports `pruned` when the journal's head is
  newer than the run's start; (b) prune only the `runtime` producer; (c) the prune keeps every
  committed run's lines. (b) drops retention for every other producer, a clause of 16 S5; (c) couples
  the journal prune to runlog's records and keeps lines forever for every committed run, which is
  most of them. (a) keeps both units' clauses and leaves one stated limit. Rung 3, the most capable
  surviving option. RESOLVED (agent, 2026-10-27, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 49 (H9).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-86, TOOL-dWellOiledMachine-88, TOOL-dWellOiledMachine-90.
- rev-3 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam extended is runlog's `check_commitment` and `measure_commitment` (`tools/runlog/record.py`),
the one verifier of a commitment, given a third state beside `match` and `mismatch`. The probe
`python tools/codebase-map/reuse_lookup.py "verify a run record whose journal lines were pruned"`
ranked `run`, `records`, `read_journal` and `check_line` by name stem; `read_journal`
(`tools/runlog/runlog_lib.py`) reads the lines and none judges retention, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "what does runlog verify report when journal
lines are gone" --terms "runlog verify commitment journal prune retention mismatch runtime.journal
PRODUCER_FILES tamper"`
