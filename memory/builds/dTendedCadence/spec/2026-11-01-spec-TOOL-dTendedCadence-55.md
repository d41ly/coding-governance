# TOOL-dTendedCadence-55 — the red leg reads each node's newest node record beside the newest period record, so a node-scoped breach the red leg holds is counted

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 9 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
HIGH, item H1. Unit 43 S4 points the red leg at `read_newest_record(root, run="period")` alone
(spec-43:39-41), and its §3 says node records "carry no `held` route (unit 16 S8)" (:49-50). Unit 16
S8 covers only its own `route = "ask"` rows: the node pass sends direct-fix survivors and every other
finding to `item.maintain.file` (spec-16 S6, :89-93), unit 8's node-scoped rows default to `file`,
and under `maintain.on-breach: red-leg` unit 15 S3 holds each of them as an `over-pin:` line in a
`<period>.<node>` record. No leg reads that record, so the bar stays green while those offenders
stand. This unit has the leg read each node's newest node record beside the newest period record.

## 2. Scope (IN)

- **S1** — The reader. `read_breach_records(root)` in `tools/drift-audit/maintenance.py` returns the
  newest committed period record and, for each node, the newest committed node record whose key's
  node segment names it, each newest by unit 15 F3's rule and read as `read_newest_record` reads one.
  The node segment is the key's text after its first dot, the `node` family's (TOOL-dTendedCadence-35
  §4). Observed by AC1.
- **S2** — The leg. `check_breach_record` (unit 15 S4) counts the distinct `over-pin:` lines across
  the records S1 returns, prints one line per offender naming the record it came from, and exits 1
  above 0. With no committed period record it prints unit 43 S4's dead-probe line and exits 1,
  whatever the node records say. Observed by AC1 and AC2.
- **S3** — The clean node record. Unit 43 S5's rule, a clean `on-finding` run still writing its record
  when the newest committed record of its own run kind carries an `over-pin:` line, reads for a node
  record the newest committed record of its own node, so a node's clean pass clears that node's lines
  and no other's. Observed by AC3.
- **S4** — The correction. Unit 43 §3's sentence on node records is read with S1: node records carry
  the red leg's holds wherever unit 15 S3 makes them. The docs line of unit 43 §5, the section "When a
  reading breaches its pin" of `help/maintain.md`, says the leg reads the period record and each
  node's newest. Observed by AC4.

## 3. Non-goals (OUT)

- Event records: id 49, TOOL-dTendedCadence-59, which extends S1's population.
- Which breaches a node pass holds: unit 15 S3 and unit 16 S6, unchanged.
- A node that stops running: its newest record stands until a clean pass of that node replaces it
  (§5 risks).

### Edges

- **consumes-from** `TOOL-dTendedCadence-43` — `check_breach_record`'s period read (S4) and the clean-record rule (S5), which this unit widens to each node's newest record
- **consumes-from** `TOOL-dTendedCadence-35` — the `node` family, whose key's node segment S1 groups the records by
- **hands-off** `TOOL-dTendedCadence-16` — the node pass's `<period>.<node>` record, whose `over-pin:` lines the leg now counts and whose clean pass clears its own node's lines
- **hands-off** `TOOL-dTendedCadence-59` — `read_breach_records`, whose population that unit extends with the event records committed after the period record (review id 49)
- **hands-off** `TOOL-dTendedCadence-74` — `read_breach_records`' node population, which the minors batch bounds to the nodes the current policy runs (review id 41)

## 4. Design

### The population

```
read_breach_records(root):
    period = newest committed record whose **Run:** is period      # unit 43 S3
    nodes  = { node segment of key : newest committed record }
             over the committed records whose **Run:** is node
    return [period] + nodes.values()        # period None -> the leg's dead probe
```

Under `every-node` the period run reads no node-scoped row (unit 16 S6), so a node record's
offenders are not a period record's; counting distinct lines makes an overlap count once in any
case. Under `lease-holder` no node pass writes a record, and the population is the period record
alone.

### Evidence

- Spec-16 S6 (:86-93) routes a node-scoped direct-fix survivor and every other finding to
  `item.maintain.file`, and writes the node pass's record under `<period>.<node>`.
- Spec-15 S3 holds a breach under `red-leg` as an `over-pin:` line, and S4 counts the lines of one
  record.
- Spec-43 S1 and S2 give each record its `**Run:**` kind, derived from the key's family.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_breach_records` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S3
- `tools/drift-audit/maintain_file.py`: S2
- `tools/drift-audit/selftest.py`: the cases of §6
- `help/maintain.md`: S4

### Alternatives rejected

- **A node-scoped breach under `red-leg` takes `file`, never the hold.** It makes `red-leg` mean "red
  for some offenders", a second meaning of one policy value, and it files asks the owner chose not to
  receive.
- **Sum the line counts of every record.** A period record superseded by a newer one would still be
  counted; newest per run and per node is the population.

## 5. Production-readiness checklist

- security — N/A — a read of committed records at `HEAD`, offline, as unit 15 S4 reads.
- perf / scale — one first-parent walk of the home, grouped by key, in place of one per kind.
- error / empty / loading states — no period record is the dead probe; no node record adds nothing.
- observability — each offender line names its record, so a node's hold is told from the period's.
- risks — a node that leaves the fleet keeps its newest record's lines red until a record of its key
  is committed clean; the owner's remedy is that clean record, which unit 43 S5 writes on the node's
  next pass.
- testing — the criteria of §6.
- migration — N/A — the home is new in this build.
- user docs — `help/maintain.md`, S4.

## 6. Acceptance criteria

The fixture is unit 43's scratch worktree with committed records and `maintain.on-breach =
"red-leg"` planted.

- **AC1** — When the worktree commits a clean period record `2026-11-01` and a node record
  `2026-11-01.node-a` carrying one `over-pin:` line, `python maintain_file.py leg` exits 1 and names
  `idle_processes_past_ceiling` from the node record.
  Red when: a node-pass hold leaves the leg green.
- **AC2** — When the worktree holds only node records, the leg prints the dead-probe line and exits
  1; when it adds a later clean node record `2026-11-02.node-a` and a clean period record, the leg
  exits 0.
  Red when: node records stand in for a missing period record, or a superseded node record is
  counted.
- **AC3** — When `on-finding` is planted and node `node-b`'s clean pass runs while `node-a`'s newest
  record carries a line, no record is written for `node-b`; when `node-a`'s clean pass runs, its
  record is written with no `over-pin:` line.
  Red when: a clean pass writes or skips by another node's record.
- **AC4** — When `grep -n "each node" maintain.md` runs in `help/`, it matches inside "When a reading
  breaches its pin".
  Red when: the page says the leg reads the period record alone.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 · committed period and node records in a scratch worktree under `red-leg`, staged against a leg reading the period record alone · none

## 8. Open questions

- **F1 — Count the node records, or keep node breaches off the hold?** Options: (a) the leg reads each
  node's newest node record; (b) a node-scoped breach under `red-leg` takes `file` or `reported`,
  stated in unit 15 S3 and unit 16 S6. Both are the report's. (b) splits `red-leg` by scope and files
  what the owner asked to see as red. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the option
  keeping one meaning per policy value. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 2 (HIGH, item H1) of the round-1 spec
  audit of units 35 to 48.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 74); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are unit 6's and unit 43's `read_newest_record`, whose newest rule S1 applies per
group, and unit 15's `check_breach_record`. `python tools/codebase-map/reuse_lookup.py "read the
newest committed record of each node and count its offenders"` ranked name stems only, `read`,
`read_text`, `counts`, `records` and `read_journal` (`tools/runlog/runlog_lib.py`), none a reader of
committed records grouped by node, so no existing seam fits beyond unit 6's reader.

Recall terms used: `python tools/memory-recall/query.py "which maintenance records does the red leg
read and which run kinds hold a breach" --terms "red leg over-pin node record period record event
record held red-leg newest committed run kind"`
