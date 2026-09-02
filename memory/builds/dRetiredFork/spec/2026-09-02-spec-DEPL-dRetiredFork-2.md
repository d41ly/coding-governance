# DEPL-dRetiredFork-2 — `update` lands a gov source that has no receipt row

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams deployer · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`_cmd_update` builds its population once, at `rows_all = receipt.get("files", [])`
(`tools/govkit/govkit.py:5519`), and classifies with `for row in rows_all:` (`:5718`). A gov source
with no receipt row is never constructed, never classified, never counted and never printed. So the
verb built to move an adopter forward cannot land anything gov newly started shipping. Measured:
five such files on NicoCares, and `plan --coverage` reports 59 of 142 planned writes missing on
inCMS. This is `TOOL-aFlaggedScaffold-3`, whose recorded consequence was six days of a dead lexicon
CLI under a green bar.

## 2. Scope (IN)

- **S1** — A descriptor-side pass in `update` that joins the selected entries' resolved write set
  against the receipt's paths and constructs a row for each difference. `coverage_rows` at
  `tools/govkit/govkit.py:2262` and `planned_writes` at `:2139` already perform that join.
- **S2** — New rows land through `land_through_index`, which already handles a path with no prior
  index entry.
- **S3** — Only roles in `LANDABLE_ROLES` land. A `rendered` source has no landable body — its
  `kind` is not `write` — so a new rendered source is REPORTED and handed to
  `DEPL-dRetiredFork-3`, never written as an unrendered template. This is the measured trap: the
  unattended kit's new `VERBS.template.md` is `role = "rendered"` and would otherwise land raw.
- **S4** — A new row's `evidence` value. `EVIDENCE_STATES` is a closed set joined to the engine by
  its own arm, so this unit either adds a member deliberately with that arm updated, or reuses
  `vintage-match`, which is true of a file gov just wrote. The choice is a fork in §8.
- **S5** — The report distinguishes a NEW source from a stale one, because an operator reading
  "33 stale" must not silently be reading "33 stale plus 5 new".
- **S6** — Arms: a new engine source lands; a new rendered source is reported and not written; a
  withdrawn source is unaffected; a run with no new sources produces byte-identical output.

## 3. Non-goals (OUT)

- `--add-kits`. Widening a target's claimed kit set is an owner decision and a separate unit. Note
  for whoever builds it: `update` currently PRINTS that flag as the remedy at `:5870`, and
  `selftest.py:746` asserts the string, so a selftest grades a flag the parser does not have. That
  defect is real and is filed by `DEPL-dRetiredFork-7`, not fixed here.
- Running the kit's adopter. That is `DEPL-dRetiredFork-3`.

## 4. Design

### Migration

No receipt schema change. New rows are written in the same shape as existing ones, with `gov_oid`
from the source blob and `sha256`/`oid` from the landed bytes, matching the split `apply` already
uses at `:4331`.

### Alternatives rejected

Telling operators to run `apply` for new files. `apply` writes every engine destination
unconditionally at `:4307-4341`, which is why NicoCares' own `deploy.toml` forbids it there; and it
also runs the kit's `[adopt]`, which for an adopter holding a kit deliberately inert is a posture
flip. "Use apply" is how the safe verb stays unable to add.

## 5. Production-readiness checklist

- security — a new source is gov's own blob at a resolved destination; the destination resolution
  already refuses an unanswered key before writing.
- perf / scale — one additional join per selected entry, over data both verbs already compute.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a target with no missing sources must print `0 new`, not nothing.
- observability — S5. New, stale and unattributed are three counts, printed separately.
- risks — landing a file into a target that deliberately declined it. Mitigated by `[[decline]]`,
  which already grades a deliberate omission and which BOTH adopters currently use zero times; this
  unit's report should name a decline that would have suppressed a row.
- testing + left-shift gates — S6's four arms in `tools/govkit/selftest.py`.
- migration / rollback — additive; a run that lands nothing new behaves exactly as today.
- user docs — `WIRE-INTO-PROJECT.md` maintenance section, and the `update` usage block.

## 6. Acceptance criteria

- **AC1** — When gov ships a new engine source a target does not hold, `python
  tools/govkit/govkit.py update --target <fixture> --write` lands it; the pre-change run reported
  nothing at all for that file.
- **AC2** — When gov ships a new `rendered` source, the run REPORTS it and writes no bytes.
- **AC3** — When a `[[decline]]` row covers the destination, the run names the decline and lands
  nothing.
- **AC4** — When no source is new, the run's output is byte-identical to the pre-change run. Compared across `python tools/govkit/govkit.py update --target <fixture>` runs.
- **AC5** — A read-only run against `C:/projects/nicocares/main` names all five currently invisible
  additions, and against `C:/projects/incms/main` reports a count reconcilable with
  `plan --coverage`'s 59 of 142.
- **AC6** — `python tools/govkit/selftest.py` and `python tools/govkit/govkit.py selfcheck` exit `0`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join`.

## 8. Open questions

- **F1 — what `evidence` does a newly landed row carry?** `vintage-match` is literally true and adds
  no member to the closed set. A new member such as `landed-new` is more honest and costs an engine
  arm. Recommendation: `vintage-match`, because the row IS at gov's vintage the instant it lands, and
  because widening a closed set joined to the engine by its own arm is a contract change this unit
  does not need.
- **F2 — does the new-source pass respect `--kits`?** It should, but `--kits` is currently parsed and
  DISCARDED for `update` at the dispatch in `main`. Recommendation: fix the dispatch here, since a
  scoped new-source pass is the safest way to first exercise this on a real adopter.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from `TOOL-aFlaggedScaffold-3` with the line numbers re-read at
  `b0108f13`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` was run for this build and reports the
`govkit` affordance seam plus the `derive_*` family in `tools/govkit/govkit.py`. The seam is `coverage_rows` at `tools/govkit/govkit.py:2262`, which already computes exactly the
join this unit needs and is today reachable only from `plan --coverage`; `planned_writes` at `:2139`
and `land_through_index` at `:5357` are the other two existing pieces. No new function is required,
which is the argument for the unit being small: three live seams and no fourth.

Recall terms used: `govkit`, `update`, `receipt`, `coverage`, `planned_writes`, `gap`, `rendered`,
`LANDABLE_ROLES`, `decline`, `adopter`, `evidence`, `vintage-match`, `land_through_index`.
