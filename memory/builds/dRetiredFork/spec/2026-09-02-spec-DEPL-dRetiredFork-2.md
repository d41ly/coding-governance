# DEPL-dRetiredFork-2 — `update` lands a gov source that has no receipt row

**Status:** OPEN · rev-4 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams deployer · order 6 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

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
- **S3** — Land on `UPDATE_ROLE`'s `table` disposition — **engine only** — and NOT on
  `LANDABLE_ROLES`, which rev-1 named. Measured at `b0108f13`: `LANDABLE_ROLES` is
  `tuple(k for k, v in ROLE_KINDS.items() if v == "write")` at `tools/govkit/govkit.py:1987`, and
  `ROLE_KINDS` at `:1960-1968` marks BOTH `engine` and `seed` as `"write"`, so rev-1's gate
  admitted `seed` — a role `UPDATE_ROLE["seed"] = "report-reseed"` at `:4958-4960` says this verb
  never writes.
- **S3b** — Carry the copy-once guard into the new-source write path. `_cmd_apply` has it at
  `:4332-4338` with its reason beside it — "seed: copied ONCE, then the target owns it" — and
  `land_through_index` at `:5357` writes unconditionally with no `dp.exists()` check.
  Only roles in `UPDATE_ROLE`'s `table` disposition land. A `rendered` source has no landable body — its
  `kind` is not `write` — so a new rendered source is REPORTED and handed to
  `DEPL-dRetiredFork-3`, never written as an unrendered template. This is the measured trap: the
  unattended kit's new `VERBS.template.md` is `role = "rendered"` and would otherwise land raw.
- **S4** — A new row's `evidence` value. `EVIDENCE_STATES` is a closed set joined to the engine by
  its own arm, so this unit either adds a member deliberately with that arm updated, or reuses
  `vintage-match`, which is true of a file gov just wrote. The choice is a fork in §8.
- **S5** — The report distinguishes a NEW source from a stale one, because an operator reading
  "33 stale" must not silently be reading "33 stale plus 5 new".
- **S5b** — Fix the per-verb flag dispatch so `--kits` BINDS for `update`. It is parsed and then
  discarded at `main`'s dispatch today, so a scoped run silently runs unscoped. This unit OWNS that
  fix: `DEPL-dRetiredFork-7` S5 filed it at rev-1 and the two specs disagreed, which M2 forbids;
  DEPL-7 rev-2 strikes its `--kits` clause and keeps `--add-kits`.
- **S6** — Arms: a new engine source lands; a new rendered source is reported and not written; a
  new SEED source whose destination already exists is REPORTED and not written; a withdrawn
  source is unaffected; a run with no new sources produces byte-identical output.

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
- risks — overwriting a target-owned `seed` file. This is the severe one and rev-1 missed it: the
  destination exists by declared design, gov does not own the repository, and the verb's whole
  selling point here is that it needs no operator turn. S3 and S3b are the mitigation, and S6's
  seed arm is what observes it. Secondly, landing a file into a target that deliberately declined it. Mitigated by `[[decline]]`,
  which already grades a deliberate omission and which BOTH adopters currently use zero times; this
  unit's report should name a decline that would have suppressed a row.
- testing + left-shift gates — one arm per S6 item, in `tools/govkit/selftest.py`.
- migration / rollback — additive; a run that lands nothing new behaves exactly as today.
- user docs — `WIRE-INTO-PROJECT.md` maintenance section, and the `update` usage block.

## 6. Acceptance criteria

- **AC1** — When gov ships a new engine source a target does not hold, `python
  tools/govkit/govkit.py update --target <fixture> --write` lands it; the pre-change run reported
  nothing at all for that file.
- **AC2** — When gov ships a new `rendered` source, the run REPORTS it and writes no bytes.
- **AC3** — When a `[[decline]]` row covers the destination, the run names the decline and lands
  nothing.
- **AC4** — When no source is new, the run's output differs from the pre-change run by EXACTLY
  the `0 new` line §5 requires, and by nothing else; compared across `python
  tools/govkit/govkit.py update --target <fixture>` runs. rev-1 demanded byte-identity, which
  that line makes impossible — the same pair `TOOL-dRetiredFork-3` AC5 already reconciles.
- **AC5** — A read-only run against `C:/projects/nicocares/main` names all five currently invisible
  additions, and against `C:/projects/incms/main` reports a count reconcilable with
  `plan --coverage`'s 59 of 142.
- **AC6** — When a new `seed` source's destination already exists in the target, `python
  tools/govkit/govkit.py update --target <fixture> --write` REPORTS it and the file's bytes are
  unchanged; with the guard removed the same run overwrites it.
- **AC6b** — When `--kits <one-entry>` is passed to `update`, only that entry's sources are
  classified; before the fix the same invocation classified the whole receipt.
- **AC7** — `python tools/govkit/selftest.py` and `python tools/govkit/govkit.py selfcheck` exit `0`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join`.

## 8. Open questions

- **F1 — what `evidence` does a newly landed row carry?** `vintage-match` is literally true and adds
  no member to the closed set. A new member such as `landed-new` is more honest and costs an engine
  arm. Recommendation: `vintage-match`, because the row IS at gov's vintage the instant it lands, and
  because widening a closed set joined to the engine by its own arm is a contract change this unit
  does not need.
- **F2 — does the new-source pass respect `--kits`?** RESOLVED (agent, 2026-09-02, delegated): yes,
  and this unit owns the dispatch fix, promoted to S5b with AC6b. The alternative left the defect
  filed by `DEPL-dRetiredFork-7` at order 2 and fixed here at order 6, so that build would have
  shipped a backlog row that was already false.
## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from `TOOL-aFlaggedScaffold-3` with the line numbers re-read at
  `b0108f13`.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding B2. rev-1's S3 gated landing on
  `LANDABLE_ROLES`, which admits `seed` because `ROLE_KINDS` marks it `"write"` — so a new gov seed
  source would have overwritten a file the target owns by design, through a write path carrying no
  copy-once guard. S3 now gates on `UPDATE_ROLE`'s `table` disposition, S3b carries the guard, S6
  gains the seed arm, AC6 observes it, and §5 names the risk rev-1 omitted.
- rev-3 · 2026-09-02 · folded spec-audit round 1, finding H8. `DEPL-dRetiredFork-7` S5 FILED the `--kits` dispatch defect
  while F2 here recommended FIXING it, and M2 requires a disagreement resolved in exactly one
  document before the first code pass. This unit takes it; DEPL-7 strikes its clause.
- rev-4 · 2026-09-02 · folded spec-audit round 2, findings 13, 14 and 30d. 13: §5 requires an unconditional
  `0 new` line and AC4 demanded byte-identity; both cannot hold. 14: §5 counted S6's arms and
  the count went stale the moment S6 grew — it points now. 30d: the rev-3 fold marked F2
  RESOLVED without the `ratified` pointer TEMPLATE-SPEC requires beside the mark.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` was run for this build and reports the
`govkit` affordance seam plus the `derive_*` family in `tools/govkit/govkit.py`. The seam is `coverage_rows` at `tools/govkit/govkit.py:2262`, which already computes exactly the
join this unit needs and is today reachable only from `plan --coverage`; `planned_writes` at `:2139`
and `land_through_index` at `:5357` are the other two existing pieces. No new function is required,
which is the argument for the unit being small: three live seams and no fourth.

Recall terms used: `govkit`, `update`, `receipt`, `coverage`, `planned_writes`, `gap`, `rendered`,
`LANDABLE_ROLES`, `decline`, `adopter`, `evidence`, `vintage-match`, `land_through_index`.
