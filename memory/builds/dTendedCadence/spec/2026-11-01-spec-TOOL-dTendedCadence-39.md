# TOOL-dTendedCadence-39 — the security review's head committed: its own record key and a records-only landing intake, so the next run starts where the last one stopped

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 18 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-prompt-TOOL-dTendedCadence-35-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-35-promoted-fix-brief.md) | research | TOOL-dTendedCadence-35 TOOL-dTendedCadence-48 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 5 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H4. Unit 13 takes each run's base from "the newest COMMITTED maintenance record carrying
`security-head`" (spec-13 S3, :47-48) and writes the head through unit 6's writer (S6, :78-84), which
commits nothing (spec-6 S6, :89-91); only the Maintain walk files a landing intake (spec-1 S6), and
unit 13 files none. Every run therefore falls back to the period start, and landings between the last
review and that start are never reviewed. Both programs also key a weekly record `2026-W44`, so they
write one file. This unit gives the review its own key and lands its record the way the walk lands its
own. The filtered reader the base needs is id 28 (M15), carried by TOOL-dTendedCadence-48; this unit
reads the review's records by run kind, which TOOL-dTendedCadence-43 adds, and needs no filter.

## 2. Scope (IN)

- **S1** — The key. `RECORD_KEY_FAMILIES` (TOOL-dTendedCadence-35) gains the family `security`,
  pattern `security-[0-9a-f]{12}`, run kind `security` (TOOL-dTendedCadence-43 S1). `security_review.py`
  writes its record under `security-<head12>`, the first 12 hex of the reviewed head, never under the
  period key, so it never shares a file with Maintain's record. Observed by AC1.
- **S2** — The landing. After unit 13 S6 writes the record, `write_review_landing(repo, path, key,
  head)` in `tools/drift-audit/security_review.py` files one cadence intake, `python
  <runtime>/intake.py file --origin cadence --filer security-review`, whose stable text is §4 "The
  intake". The records-only patch build that takes it re-writes the record with `python maintenance.py
  write --key <key> --base <head>` from the text alone and lands it, as unit 1 S6 lands Maintain's. The
  review commits nothing. A refused filing prints its line and exits 1, so the lease releases as a
  hand-over and the next wake reviews the same range. Observed by AC2.
- **S3** — The base. Unit 13 S3's base is the `security-head` of `read_newest_record(root,
  run="security")` (TOOL-dTendedCadence-43 S3); with none, or one that is not an ancestor of `head`,
  the fallback is unit 13 S3's as written. Observed by AC3.

## 3. Non-goals (OUT)

- The `carrying=` filter on the reader: id 28, TOOL-dTendedCadence-48.
- The finding key of a security finding: id 53, TOOL-dTendedCadence-48.
- The patch build that lands a records-only intake: Plan's patch disposition, as for unit 1 S6.

### Edges

- **consumes-from** `TOOL-dTendedCadence-13` — `security_review.py`, its range and its head write, which this unit re-keys and lands
- **consumes-from** `TOOL-dTendedCadence-35` — `RECORD_KEY_FAMILIES`, the table the `security` family joins
- **consumes-from** `TOOL-dTendedCadence-43` — the run kind on each family and `read_newest_record`'s `run=` filter, which S3 reads the base through
- **hands-off** `TOOL-dTendedCadence-48` — `read_newest_record`, the base read with `run="security"`, to which that unit's S17 adds `carrying=` (review id 28)
- **hands-off** `TOOL-dTendedCadence-52` — `security_review.py`'s landing (S2), which that unit files through `write_record_landing` (review id 43)
- **hands-off** `TOOL-dTendedCadence-59` — the security landing's README section, the family list and the Files touched, which the minors batch repairs (review ids 5, 24, 36)

## 4. Design

### The intake

```
land maintenance-record security-<head12>
base: <head, 40 hex>
security-head: <head, 40 hex>
```

The text names one reviewed head, so its content key is that head's and a re-filed landing of one
head appends a receipt rather than a second intake. It carries no readings: the review's record holds
none, so the re-write takes stdin `{"read": [0, 0], "readings": [], "fields": {"security-head":
"<head>"}}`, the members unit 6 defaults for the rest.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `security` | `RECORD_KEY_FAMILIES` row | none |
| `write_review_landing` | function, `security_review.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `security-review` | the intake's `--filer` value, the cadence row's name | none |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1
- `tools/drift-audit/security_review.py`: S1, S2, S3
- `tools/drift-audit/selftest.py`: the cases of §6
- `help/maintain.md`: the section "The security review" states the key and the landing

### Alternatives rejected

- **Carry `security-head` in a committed home unit 13 owns.** A second home for one value the record
  kind already holds, and a second write path to land.
- **Keep the period key and merge into Maintain's record.** Two programs on two leases writing one
  file, the collision the finding names.

## 5. Production-readiness checklist

- security — the review's record goes through unit 6's write boundary and its key through the family
  table; the intake text carries two shas and no finding text.
- perf / scale — one intake per completed review, `weekly` by default.
- error / empty / loading states — a refused filing exits 1 and re-reviews the range; a run with
  nothing landed writes no head and files nothing (unit 13 S3).
- observability — the run prints `security-review — <head8> · landing filed <content key>`.
- risks — a range reviewed and filed but not yet landed is reviewed again by a run that starts before
  the patch build lands; the overlap is re-reported findings, which the filing dedupes.
- testing — the criteria of §6.
- migration — N/A — no review record exists at base.
- user docs — `help/maintain.md`.

## 6. Acceptance criteria

- **AC1** — When `python security_review.py run --dry-run` runs under `GOV_CADENCE_KEY=2026-W44` in a
  fixture whose landed tip is `H`, it prints the record key `security-<H12>`, and `derive_record_family`
  answers `security` for it and `weekly` for `2026-W44`.
  Red when: the review writes under the period key.
- **AC2** — When a completed review runs in the fixture with a recording filer, it files one intake
  with filer `security-review` whose text is §4's three lines for `H`, and `git rev-list --count HEAD`
  is unchanged by the run.
  Red when: the record's landing is not filed, or the review commits.
- **AC3** — When two runs chain in the fixture with no planted record, the first reviewing `B..H1`, and
  the fixture lands the first run's intake by running the text's re-write and committing it as the
  patch build would, the second run's range line names base `H1`.
  Red when: the second run's base is the period start.
  fixture: a scratch repository under `%TEMP%` with a stub harness return; `intake.py` is
  TOOL-dWellOiledMachine-27's, absent at `f4597719`, so the filer is a recording stub.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 · a two-run chain over a fixture with a stub harness and a recording filer, staged against a review that writes under the period key and files no landing · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 5 (HIGH, item H4) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (units 52 and 59); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are unit 13's `security_review.py`, unit 35's key table, unit 43's run kind, and the
landing shape of unit 1 S6, whose records-only intake this unit files for the review's record.
`python tools/codebase-map/reuse_lookup.py "file a records-only intake so a written record is
committed and landed"` ranked `records`, `corpus_files`, `extract_records` and `read_records`, none an
intake filer; `intake.py` is an ancestor's and absent at base, so no existing seam fits beyond unit 1
S6's call shape, reused here.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
