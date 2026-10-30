# DEPL-dShippedRelease-70 — a second node reads a landed SHA by containment, and an unlanded SHA by its own class

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 7 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 76 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H14, which stands beside ids 15 and 81. Unit 12 S8 reads "the SHA on the tip reads
landed-ungated ... neither present reads nothing-pushed". A take-over needs a stale lease, 24 hours
by default, by which time a landed SHA is routinely buried, so the killed-supervisor case S8 exists
for reads `nothing-pushed`, a landed class in unit 1 S5, and unit 1 records that nothing was pushed.

## 2. Scope (IN)

- **S1** — The test. The no-record branch of `read_landing_outcome` fetches the advertised default
  branch and runs `git merge-base --is-ancestor <sha> <tip>`. A contained SHA reads
  `landed-ungated`. Observed by AC1.
- **S2** — A SHA not contained reads `unlanded`, an eighth class that is no landing:
  `read_landing_outcome` prints it and exits 1, and unit 1 writes no record for it (§8 F1). A failed
  fetch is a dead probe, exit 2, and never a class. Observed by AC2, AC3.
- **S3** — The fixture rule. Every read of a landed SHA also runs with one later landing on top.
  Observed by AC1.

## 3. Non-goals (OUT)

- The prior tip this branch prints: DEPL-dShippedRelease-52.
- Unit 1's allow-list: review ids 15 and 81, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-12` — `read_landing_outcome`, its no-record branch and the class table
- **hands-off** `DEPL-dShippedRelease-52` — the no-record branch, in which that unit derives `landing_prior_tip`
- **hands-off** `DEPL-dShippedRelease-78` — `unlanded`, the class that unit's allow-list reads for review ids 15, 35 and 81

## 4. Design

### Evidence

- Unit 12 §4 records `leases.expiry-hours` defaulting to 24, and report id 76 read consecutive landings on the first-parent line, so a landed SHA is routinely behind the tip.
- Unit 1 S5 uses "contain" for the same fact and names `nothing-pushed` among the landed classes.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `help/loop.md`: the eighth class

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — one bounded fetch on a node that holds no record, the take-over path alone.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/loop.md` names `unlanded`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant outcome-buried` deletes the record of a
  landed SHA with one later landing on top, `outcome <sha>` prints `landed-ungated`.
  Red when: a buried landing reads as nothing pushed, the take-over case.
- **AC2** — When `--plant outcome-unlanded` asks for a SHA the default branch does not contain,
  `outcome <sha>` prints `unlanded` and exits 1.
  Red when: a SHA that never landed reads a landed class.
- **AC3** — When `--plant outcome-dead-remote` runs, `outcome <sha>` exits 2 and prints no class.
  Red when: a network fault reads as a class a reader acts on.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 · the three plants, their failing case the tip compare · none

## 8. Open questions

- **F1 — What does a SHA absent from the default branch read?** Options: (a) a distinct class
  `unlanded`; (b) `nothing-pushed`, as the report's H14 says. M9 of the same report asks a distinct
  class. (b) reads a landed class in unit 1 S5, so a record would be written for a landing that
  never happened. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, one answer for both items.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 76 (HIGH, item H14) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-12's outcome and queue code.
`python tools/codebase-map/reuse_lookup.py "append an entry to a ref chain and skip or tombstone an entry"`
ranked name-stem helpers (`skip`, `build_self_chain`, `resolve_entry`, `read_chain_clauses`) and no
ref-held queue, since unit 12's is specced and unbuilt, so no existing seam fits outside it. The
recall probe surfaced scout B's queue row and report item H15, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what is the tip before a landing when the close commits records on the prepared merge" --terms "landing_prior_tip first parent prepared merge close commit in-place records stacked range lander"`
