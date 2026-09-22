# DEPL-dGaugedVintage-9 — report the per-kit version delta, once the stored half stops lying

**Status:** CLOSED · rev-3 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 4 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-9-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-9-acceptance-ledger.md) | journal | — |
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

Every receipt row stores the kit version it was written at, and nothing in gov reads it back. But the
stored half is not trustworthy yet: `update` never refreshes it. Make the field true, then report the
per-kit delta an adopter actually wants before an update.

## 2. Scope (IN)

- **S1** — `_cmd_update` refreshes `row["version"]` in each of its three mutating branches, alongside
  the `sha256` and `commit` it already refreshes, resolved through the same `to_commit` those
  branches use rather than through `HEAD`.
- **S2** — A per-kit delta report: for each entry in a target's receipt, the version its rows carry,
  gov's version now, and whether they differ. Read from the stored rows.
- **S3** — The comparison is EQUALITY, not ordering, and the report says so. A row whose stored value
  is absent, `"(none declared)"` or `"(unresolvable)"` is reported in its own state, never as level.
  REVISED at build time: the equality is on the VERSION NUMBER extracted from each side, not on the
  whole source line — see §4.
- **S4** — The report is available without writing, from a verb an adopter already runs.

## 3. Non-goals (OUT)

- Reading a version out of the target's installed BYTES. That is the marker question and belongs to
  `DEPL-dGaugedVintage-5`.
- Ordering two versions. S3 makes the comparison equality-only; a parse from a source line to a
  comparable version is a follow-up that needs its own stated failure mode.
- Deciding what to DO about a delta. This unit reports; `update` owns the acting.
- Changing the receipt schema. The field exists; this unit makes it true and reads it.

## 4. Design

### Data model

`entry_version` (`tools/govkit/govkit.py:333-353`) does NOT return a version. It returns the whole
matched SOURCE LINE via `return ln.strip()` at `:352` — `KIT_CODEBASE_MAP_VERSION = "1.3"`, not
`1.3` — or one of the sentinels `"(none declared)"` (`:341`) and `"(unresolvable)"` (`:345`, `:348`,
`:353`). That is why S3 is equality-only: there is no ordering to be had from a source line.

**But the equality is on the NUMBER, and rev-2 got this wrong.** Comparing whole lines was the rev-2
design, and running the finished report against the live adopter showed why it fails:
`DEPL-dGaugedVintage-5` added a marker COMMENT to three constants, and all three immediately read
DIFFERS at an identical version. A comment edit is not a version change, and reporting it as one is
the same false-"behind" class B1 was about, one field over. The report now extracts a dotted number
from each side and compares those; when either side yields none it falls back to the whole line AND
SAYS SO, because a silent fallback makes the output claim more than it checked.

**The stored half is stale by construction today.** `_cmd_update` spans `:5169-6317` and the string
`version` does not occur anywhere inside it. Its three mutating branches refresh `row["sha256"]` and
`row["commit"]` only. Every `"version":` write is in `apply` (`:3964`, `:4032`, `:4056`, `:4093`) or
`adopt` (`:6411`, `:6418`, `:6462`, `:6571`, `:6599`), and `entry_version` is called at `:3995` and
`:6403` and nowhere else.

`memory/builds/aTetheredConvoy/reviews/2026-08-16-review-DEPL-aTetheredConvoy-1-3.md` F6 reproduced
this: bumping `KIT_CHECK_WIRING_VERSION` 1.0 to 9.9 and running `update --write` left the target's
file reading 9.9 while the receipt row still read 1.0, against the NEW commit and the NEW sha256.
Nothing in `memory/DECISIONS.md` resolves it. So a delta report over today's field would print
"behind" for exactly the population it is run against — a maintained target. S1 is therefore a
precondition of S2, not a nicety.

### Inventory

| Fact | Where | Consequence |
|---|---|---|
| `version` written by `apply` and `adopt` only | `:3964`, `:4093`, `:6462` and five more | the stored half exists |
| `_cmd_update` never touches it | `:5169-6317`, zero occurrences | the stored half goes stale on every update |
| `entry_version` returns a source line | `:352` | equality-only, no ordering |
| no reader joins stored to live | measured: no call site compares them | the delta is underivable today |

### Rollout

S1 first and alone if need be: it is a correctness fix to a field the receipt already claims, and it
is worth landing whether or not S2 follows.

### Alternatives rejected

Reporting the delta over the un-refreshed field was the rev-1 design. It is rejected: a report whose
input is stale for every maintained target is worse than no report, because it is believed.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — S1 adds one `entry_version` resolution per refreshed row; S2 is a join over rows
  already loaded.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — three distinct non-level outcomes, never collapsed into level:
  key absent (receipt predates the field), `"(none declared)"`, and `"(unresolvable)"`.
- observability — this unit IS an observability change, and S1 is what makes it honest.
- risks — a stored version is a claim about what gov shipped, not about the target's current bytes.
  The report must say which it is.
- testing + left-shift gates — the S1 arm below, staged RED first; it fails at this base today.
- migration / rollback — a receipt written before S1 carries stale versions until its next
  `update --write`. The report must not present those as authoritative; S3's absent-key state covers
  the pre-field case and §8 F3 asks how to mark the stale-but-present case.
- user docs — `WIRE-INTO-PROJECT.md` §5b gains the delta read in the pre-update sequence.

## 6. Acceptance criteria

- **AC1** — When a kit's version constant is bumped and `python tools/govkit/govkit.py update --write`
  runs over a fixture target, the receipt row's `version`, `sha256` and `commit` all move together,
  observed by re-reading `.governance/install.json`.
- **AC2** — The AC1 arm is observed RED before S1 lands: run it at this base and confirm `version`
  stays put while `sha256` and `commit` move. It fails today, which costs nothing to demonstrate.
- **AC3** — When stored and live values are equal, `python tools/govkit/govkit.py update` reports the
  entry level rather than omitting it, so a green read is distinguishable from one not examined.
- **AC4** — When a row's stored value is `"(none declared)"`, the same command reports `undeclared`
  and not `level`, observed on a fixture.
- **AC5** — When a row carries no `version` key at all, the same command reports that the receipt
  predates the field, distinctly from AC4's state.
- **AC6** — The report writes nothing: `git status --short` in the target is empty after a run.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `govkit acceptance matrix`. This unit
ADDS the AC1/AC2 arm to the govkit selftest.

## 8. Open questions

- **F1 — which verb carries the report.** RESOLVED (agent, 2026-09-01, delegated): `update`, and NOT
  behind a flag. An adopter already runs it read-only before writing, and a flag would make the
  answer to "am I behind" opt-in — which is how this repo ended up with a five-lens manual audit
  instead. `prior:` no prior ruling found.
- **F2 — whether an entry present in gov but absent from the receipt is in scope.** RESOLVED (agent,
  2026-09-01, delegated): out of scope. It is a not-adopted entry rather than a stale one, and
  `coverage_rows` at `:2051` already answers it. `prior:` no prior ruling found.
- **F3 — how a row refreshed before S1 landed is marked.** RESOLVED (agent, 2026-09-01, delegated):
  NOT marked, and the report does not pretend to. Such a row reads as whatever it stores, which may
  be stale; the next `update --write` refreshes it. Detecting the pre-S1 case needs a schema bump to
  record when the field was last written, and that is a receipt-format change this unit is not
  taking. Recorded as a known limitation in the ledger. `prior:` no prior ruling found.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit B1, H1, L1. S1 added: the unit now fixes the field
  before reading it, because `_cmd_update` never refreshes it and aTetheredConvoy F6 had already
  reproduced that. §4 corrected — `entry_version` returns a source line, not a version, so the
  comparison is equality-only and "older" left §1 and the criteria. F1's citation to
  `DEPL-dGaugedVintage-2` was dropped; that record says nothing about verb discoverability.

- rev-3 · 2026-09-01 · BUILT and CLOSED. S1 landed as `entry_version_at` plus one `_ver_at` in
  all three of `_cmd_update`'s mutating branches. §4 REVISED at build time: the comparison is on
  the extracted version NUMBER, not the whole source line — running the finished report against
  the live adopter showed three kits reading DIFFERS purely because `-5` edited a comment on their
  constant's line. F1, F2 and F3 resolved.
  Acceptance ledger at `build/2026-09-01-build-DEPL-dGaugedVintage-9-acceptance-ledger.md`.
## 10. Reuse audit

- The seam is `entry_version` at `tools/govkit/govkit.py:333-353`, already called by `apply` at
  `:3995` and `adopt` at `:6403`; S1 adds its third caller inside `_cmd_update`'s mutating branches,
  and S2 joins its result to the stored field. `coverage_rows` at `:2051` is the existing precedent
  for a read-only join over a receipt. `python tools/codebase-map/reuse_lookup.py "assert every gov
  kit version marker site against its descriptor"` ranks `read_descriptors` in the same file as the
  descriptor-aware entry point.
- Recall terms used: `govkit receipt attribution unattributed forked role landable classify_row
  gov_oid vintage update adopt evidence`
