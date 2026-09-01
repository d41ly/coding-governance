# DEPL-dGaugedVintage-13 — a backlog row that outlived its own CLOSED spec

**Status:** CLOSED · rev-2 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 9 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-13-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-13-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-dGaugedVintage-2` swept sixteen rows by hand: `DEPL-dCarriedReceipt-1..15` read SPECCED while
every one of their specs read CLOSED, and `DEPL-aFerriedDossier-1` sat OPEN six days after its own
declared closer shipped. Nothing measures that class, so the next one accumulates the same way.

## 2. Scope (IN)

- **S1** — A drift signal, `backlog_rows_outliving_closed_specs`: for every spec at a TERMINAL
  status, the backlog row bearing that id is found in its family shard and its status token read. A
  row that is not itself terminal is a finding.
- **S2** — LIVENESS. The signal reports `live` from the count it actually examined, so a probe that
  matched no spec says so rather than printing a reassuring zero.
- **S3** — A pin measured at this base, shrink-only like every other in that table.
- **S4** — Fixtures: a non-terminal row under a CLOSED spec is found; a terminal one is not; and a
  spec whose id appears in NO backlog row is not a finding, because an id can be a unit without ever
  having been an ask.

## 3. Non-goals (OUT)

- A merge-bar REFUSAL on the first non-terminal row. A row's ask can be legitimately WIDER than the
  unit that partly served it — `DEPL-dGaugedVintage-2` §8 F1 resolved exactly that — so the honest
  instrument is a counted signal against a pin, not a gate that calls every such row a defect.
- The reverse direction: a CLOSED backlog row whose spec is still open. That is a different mistake
  with a different remedy and it earns its own signal or none.
- Reconciling any row. `DEPL-dGaugedVintage-2` did that once by hand; this unit measures so the next
  one is noticed rather than swept.
- Judging whether an acceptance ledger exists. `check-memory-hygiene.sh` check 23 owns that.

## 4. Design

### Data model

A spec's own id and status come from its H1 and status header, both already parsed by
`gen_build_index.py`. A backlog row is `- <id> · <STATUS> · …` in `memory/backlog/<FAMILY>.md`, and
`<FAMILY>` is the id's own prefix — so the shard is derived from the id rather than searched for.

### Inventory

| Fact | Where | Consequence |
|---|---|---|
| `TERMINAL` is `("CLOSED", "WONTDO")` | `tools/memory-tree/gen_build_index.py:151` | one vocabulary, not a second |
| the status-token set | same file, `:150` | a backlog row and a spec share it |
| signal shape and pins | `tools/drift-audit/drift_report.py`, `drift_signals.py` | this unit adds one row to each |

### Rollout

Report-only in the sense that matters: it lands with a pin equal to what it measures at this base, so
it cannot red on arrival for debt it merely discovered. The pin then only falls.

### Alternatives rejected

A hygiene check that refuses. Rejected on the false-positive above: it would red a row whose ask is
wider than its unit, and the operator's only recourse would be to close a row that should stay open —
which is worse than the drift it was written to catch.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one pass over the tracked spec set, already walked by this signal's siblings, plus
  one read per family shard.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a spec whose id matches no backlog row is NOT a finding, and a
  corpus with no terminal spec reports `live: false` rather than a zero.
- observability — the detail names the file, the id and the row's actual token, so the finding is
  actionable without re-deriving it.
- risks — an over-eager gate. §3 and §4 both say why this is a counted signal instead.
- testing + left-shift gates — S4's three fixtures, in the drift-audit selftest.
- migration / rollback — none; a new signal row.
- user docs — none; the signal's own name and detail are the doc.

## 6. Acceptance criteria

- **AC1** — When a backlog row is non-terminal and its spec is CLOSED,
  `python tools/drift-audit/drift_report.py` counts it and its detail names the file, id and token.
- **AC2** — When the row IS terminal, `python tools/drift-audit/drift_report.py` does not
  count it.
- **AC3** — When a CLOSED spec's id appears in no backlog row at all,
  `python tools/drift-audit/drift_report.py` does not count it, because a unit id need never have
  been an ask.
- **AC4** — `python tools/drift-audit/drift_report.py` reports the signal `live` only when it
  examined at least one terminal spec, so a probe that cannot move says so.
- **AC5** — AMENDED at build time. Reverting `-2`'s sweep on a fixture was not how the RED was
  taken; the selftest's own paired arms are, and they are stronger: the SAME fixture spec with a
  non-terminal row counts 1, and with a terminal row counts 0. That is the red and the green over one
  subject. Separately and unplanned, the signal found 27 findings across TOOL, PLAY and KICK on the
  real corpus — residue `-2`'s DEPL-only sweep never touched, which is the drift this unit exists to
  make visible.
- **AC6** — `bash tools/run-gates/run-gates.sh` — the `drift-audit records` leg stays green, with
  the new pin equal to what this base measures.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `drift-audit records` and `drift-audit selftest`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft, filed by `DEPL-dGaugedVintage-2` S3 as the answer to whether
  the class it swept by hand is gateable.
- rev-2 · 2026-09-01 · BUILT and CLOSED as the drift signal
  `backlog_rows_outliving_closed_specs`, pinned at the 27 it measures. AC5 amended: the RED is the
  selftest's paired arms over one fixture spec, which is a better observation than reverting a
  sweep. Acceptance ledger at
  `build/2026-09-01-build-DEPL-dGaugedVintage-13-acceptance-ledger.md`.

## 10. Reuse audit

- The seam is the drift-signal table itself: `closed_specs_with_no_product_commit` in
  `tools/drift-audit/drift_report.py` already walks every tracked spec, reads its status header
  through `_STATUS` and its own id through `_OWN_ID`, and returns the `{signal, value, of, live,
  detail}` shape with a pin in `drift_signals.py`. This unit adds a sibling that reuses that walk's
  parsers rather than adding a second reader of a spec header.
  `python tools/codebase-map/reuse_lookup.py "join a backlog row status token to its spec status
  header"` ranked `append_backlog` and `backlog_keys` in `map_lib.py`, which write and key rows
  rather than grade them — the query asked about a join nothing performs yet.
- Recall terms used: `ratchet shrink-only count identity swap backlog row status token spec header
  terminal join stale`
