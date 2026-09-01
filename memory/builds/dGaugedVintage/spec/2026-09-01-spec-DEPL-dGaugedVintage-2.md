# DEPL-dGaugedVintage-2 — fifteen rows that outlived their specs

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-1 · base d65da7ab · streams deployer · order 7

*Tier-1 light profile per `memory/TEMPLATE-SPEC.md`: the status header binds, the ten-section canon
does not. The sections below are the ones that carry decisions.*

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-dCarriedReceipt-1` through `-15` read SPECCED in the backlog while their specs read CLOSED and
their code is in the tree. One consequence is live: `DEPL-aFerriedDossier-1` is still OPEN asking for
a hand-fork update path whose declared closer, `DEPL-dCarriedReceipt-13`, shipped on 2026-08-26.

## 2. Scope (IN)

- **S1** — Reconcile each of the sixteen rows against its spec's status header, one at a time, and
  update the row in place. A row whose spec is CLOSED and whose acceptance criteria are evidenced
  becomes CLOSED; anything else keeps its status and gains a note saying why.
- **S2** — Close `DEPL-aFerriedDossier-1` by citation to `DEPL-dCarriedReceipt-13`, or record why it
  survives its declared closer.
- **S3** — Ask whether this class is gateable: a backlog row whose id matches a CLOSED spec and which
  is not itself terminal. If it is cheap, say so and file it; if it is not, say why.

## 3. Non-goals (OUT)

- Any change to the specs themselves. Their status headers are the source of truth here and this
  unit reads them.
- Rows outside `DEPL-dCarriedReceipt-*` and `DEPL-aFerriedDossier-1`. A wider sweep is a different
  unit with a different cost.
- Building the gate S3 scopes. S3 produces a decision and, if warranted, a row.

## 6. Acceptance criteria

- **AC1** — When the sweep is done, `grep -c 'SPECCED' memory/backlog/DEPL.md` returns a count whose
  every remaining member is a row whose spec is genuinely not CLOSED, checked one by one.
- **AC2** — When `DEPL-aFerriedDossier-1` is resolved, its row cites the id that closed it or states
  what remains, observed in `memory/backlog/DEPL.md`.
- **AC3** — S3's answer is recorded under `memory/builds/dGaugedVintage/build/` whether it is yes
  or no, so a decision not to gate is distinguishable from never having asked.
- **AC4** — `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 after the sweep, with the
  status-vocabulary check green over every edited row.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the records chunk, `memory hygiene` in particular.

## 8. Open questions

- **F1 — whether a CLOSED spec is sufficient evidence to close its backlog row.** A spec closes when
  its unit is built; a backlog row is an ASK, and an ask can outlive the unit that partly served it.
  Recommendation: require the spec CLOSED and its acceptance ledger present, and where the row's ask
  is wider than the unit, keep it open with a note. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
