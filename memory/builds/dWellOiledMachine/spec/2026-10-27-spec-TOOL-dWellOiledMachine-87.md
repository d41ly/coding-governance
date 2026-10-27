# TOOL-dWellOiledMachine-87 — the record door's node writer admits the sessions and keepalive the `mine` row admits, prior sessions included

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 28 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-87-deviation-871.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-87-deviation-871.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 50, item H8, at HIGH. TOOL-dWellOiledMachine-63 S2 builds the node writer's `sessions` from
`absent` plus the run-state file's `session:` fact, and its Goal and S5 claim the reach of
`check_claim_writable`'s `mine` row "and no more". That row also admits, outside a take-over, a claim
under the run's keepalive whose session is any member of the run-state file's `prior-session` set,
and it requires keepalive equality, which 63 S2 drops (`tools/unattended/unattended.sh:2260-2261`).
On a resumed run whose `--resume` claim write did not land, the tick's `--beat` is refused
`cross-session`, the lease ages stale while the run is live, and another node can take it over; and
without the keepalive check a sessionless writer can act on a claim under the same session from a
different keepalive. This unit spells the node writer's admission as the `mine` row spells it, and
proves the two agree on one claim matrix.

## 2. Scope (IN)

- **S1** — The sessions. `read_node_writer` (`tools/memory-tree/gov_record.py`, 63 S2) returns
  `sessions` as `absent`, the run-state file's `session:` fact, and every member of its
  `prior-session` fact, split on single spaces, where an empty value or a missing line is the empty
  set, exactly as `check_claim_writable` reads that fact (`tools/unattended/unattended.sh:2234-2240`,
  `:2259`). Observed by AC1.
- **S2** — The keepalive. `read_node_writer` also returns the run-state file's `keepalive:` fact, and
  63 S3's rules admit a node writer's write of a record carrying a `keepalive` key only when that key
  equals it. A record carrying no `keepalive` key is judged by `fleet-tag` and `session` alone, as
  63 S3 says. Observed by AC2.
- **S3** — Never a take-over. The node writer never takes the take-over row's reading: a prior-session
  member admits a write only where the `mine` row would, outside `take-over` mode, so a sessionless
  writer cannot adopt a claim under a prior session's different keepalive. Observed by AC2.
- **S4** — The parity case. `door_fixture.py --case node-parity` runs one claim matrix (session equal,
  prior-session member, foreign session; keepalive equal and different) through
  `check_claim_writable` with mode `beat` and through the door's node writer, and requires identical
  admit and refuse on every row. Observed by AC3.
- **S5** — 63's statement corrected. Spec 63 takes a rev bump at this unit's pass: its §8 F1 reads
  "the host compare plus the run-state file's `session:`, `prior-session` and `keepalive:` facts", and
  its §9 line names this unit and finding 50. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `check_claim_writable`: the door copies its reading and the parity case pins the two.
- The host rule's second spelling in Python is finding 36, carried by the minors batch
  TOOL-dWellOiledMachine-90.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-63` — `read_node_writer`, the node writer's rules and `door_fixture.py`'s node cases, whose session set and keepalive this unit aligns with the `mine` row

## 4. Design

### Evidence

- `check_claim_writable` reads `prior-session` from the run-state file (`:2259`) and classes a claim
  `mine` when its keepalive equals the lease's and its session is the lease's, or, outside
  `take-over`, a member of `prior-session` (`tools/unattended/unattended.sh:2260-2261`); the fact's
  grammar is a space-separated set, empty or missing being the empty set (`:2234-2240`).
- 63 S2 builds `sessions` from `absent` and `session:` only (`spec-63.md:34-41`), and its Goal says
  "the reach `check_claim_writable`'s `mine` row grants the tick today, and no more"
  (`spec-63.md:23-24`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `node-beat-prior-session`, `node-foreign-keepalive`, `node-parity` | `door_fixture.py` cases | none |

### Files touched (estimate)

- `tools/memory-tree/gov_record.py`: S1 to S3
- `tools/memory-tree/door_fixture.py`: the three cases
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-63.md` (S5's rev bump)

### Alternatives rejected

- **Calling `check_claim_writable` from the door.** The door is Python and runs for every coordination
  ref, most of which are not claims; the parity case keeps one reading without a bash spawn per write.

## 5. Production-readiness checklist

- security — the keepalive check restores the bound the `mine` row has; no reach beyond it.
- perf / scale — two more facts read from the run-state file the node writer already opens.
- error / empty / loading states — a missing `prior-session` is the empty set, as in the row.
- observability — a refusal keeps 63's `cross-session` line.
- risks — the parity case is the drift guard between the two readings.
- testing — AC1 to AC4 and the arm in §7.
- migration — none.
- user docs — none beyond 63 S5's statement of the reach, which is unchanged in scope.

## 6. Acceptance criteria

Each case runs `python door_fixture.py --case <name>` with `CLAUDE_CODE_SESSION_ID` removed from the
verb's environment.

- **AC1** — When `--case node-beat-prior-session` runs `unattended.sh --beat fx` in a clone whose
  run-state file names `session: s2` and `prior-session: s1`, against a remote build lease held under
  `s1` and the run's keepalive, the beat prints `beat — fx · renewed`.
  Red when: the beat is refused `cross-session`, as 63 S2's set refuses it.
- **AC2** — When `--case node-foreign-keepalive` runs the same beat against a lease under `s1` and a
  different keepalive, the verb exits 2 printing `cross-session` and the lease is unchanged.
  Red when: a sessionless writer renews a claim under another keepalive.
- **AC3** — When `--case node-parity` runs, it prints one line per matrix row and no row where the door
  and `check_claim_writable` disagree.
  Red when: the two readings admit different rows.
- **AC4** — When `grep -c "keepalive:. facts" 2026-10-27-spec-TOOL-dWellOiledMachine-63.md` runs
  over spec 63 after this unit, it prints 1, the corrected §8 F1.
  Red when: F1 still claims the `mine` row's reach from `session:` alone, as it does at this spec's
  base, where only its §3 edge names `prior-session`.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

The unattended kit's self-test suites are waived for this build's landing (README rule 8); the door
fixture is this unit's observation.

New arm: tools/memory-tree/door_fixture.py · covers AC1 AC2 AC3 · the three cases staged against 63 S2's `sessions` of `absent` and `session:` with no keepalive check · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  50 (H8).

## 10. Reuse audit

The seam reused is `check_claim_writable`'s `mine` row and its `prior-session` grammar
(`tools/unattended/unattended.sh:2234-2261`), copied into the door's reading and pinned to it by a
parity case rather than re-derived. The probe `python tools/codebase-map/reuse_lookup.py "admit a beat
from a prior session of the run"` ranked `run`, `run_git`, `extract_run_facts` and `extract_session`;
`extract_run_facts` (`tools/unattended/lib-unattended.sh:2057`) is bash, so the Python door reads the
facts itself. The recall query below ranked TOOL-aGraftedHelix-23, the `prior-session` fact's spec,
first.

Recall terms used: `python tools/memory-recall/query.py "which sessions may renew the claim" --terms
"check_claim_writable mine row prior-session keepalive node writer door sessionless beat resume"`
