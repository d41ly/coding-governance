---
slug: cSpliceWarden
node: c
opened: 2026-09-12
streams: tooling+playbook
roster: TOOL
ids: TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5 TOOL-cSpliceWarden-6 TOOL-cSpliceWarden-7 TOOL-cSpliceWarden-8
---

# cSpliceWarden — the archive that contradicted itself, and the rotation nobody declared

## The problem this build exists to solve
`memory/archive/TOOL.2026-08-17.md` says in its own header that it holds "Terminal rows only …
deduplicated by id". It holds 90 rows, of which 24 are terminal. Forty-nine of its ids are also live
in `memory/backlog/TOOL.md`, seven of those disagree about status, two ids appear twice, and fifteen
rows exist nowhere else — each saying OPEN about work that closed a month ago. No gate sees any of
it. The deeper cause is that this repo never declared what a rotation MEANS, so nothing could grade
the result: `memory/HYGIENE.md` said both things at once, `git mv` the whole index AND carry every
non-terminal row forward, and that pair writes every live row into a frozen file. The archive is not
an accident; it is what the documented procedure produces. The evidence is in
`build/2026-09-13-build-TOOL-cSpliceWarden-4-archive-forensics.md`.

## Expected improvements
- A backlog id has exactly one file that owns its status, so a cross-file disagreement cannot form.
- Two hygiene checks stop reporting a reassuring zero over a population they never reached.
- Rotation semantics becomes a declared per-project choice rather than a contradiction in prose, so
  the kit can ship to a repo practising the other discipline without either being wrong.
- Fifteen closed units stop reading OPEN to every session and every recall query that finds them.

## Detriments if this is not built
- The archive keeps contradicting its own header, and every later rotation inherits the pattern.
- Fifteen closed units stay open on the record, so work already done looks like work outstanding.
- Two checks stay inert while looking green, which is worse than their being absent.

## Build-level rules
- **The archive is a ratified record.** It is corrected by SUPERSESSION, never a silent rewrite: the
  note states every false claim and quotes every removed row verbatim, and the removal is the owner's
  ratified decision of 2026-09-12 rather than the run's judgment.
- **The supersession note is prose, never a row.** A dash-led line carrying an id would key as a
  backlog row under the widened check 20 — a note that becomes a row is a new defect wearing the
  repair's clothes.
- **Unit 4 lands BEFORE unit 3, and the order is not a preference.** Widening check 20 while the two
  stale duplicate rows remain takes the measured duplicate count from 3 to 5, and
  `ROW_DUPLICATE_PIN` is shrink-only AND exact-match, so the other order forces a wrong-way pin move
  and a second commit to undo it. Evacuate first and the pin never moves.
- **A re-homed row carries the body its CLOSING COMMIT wrote, not the one the archive froze.** Four
  of fifteen differ, and the archive's copy re-asserts claims the tree refutes.
- **No figure in this build's prose is authored where a command can derive it.**

## Parked decisions
- **Nothing grades the declared `ROTATION_MODE`. RESOLVED as a deliberate omission, agent-delegated,
  2026-09-12 (`TOOL-cSpliceWarden-6`).** The key is validated against its closed set and then read by
  no check, so nothing asserts that a rotated archive holds terminal rows only, nor that no id sits
  in both a shard and its archive. Those are the left-shift owed on the very finding this build
  repaired. The owner's ratified scope covered the repair, the declaration and the widening of checks
  10 and 20; a new grading check was not among the extras offered or approved, so it is filed rather
  than built unasked. Under `snapshot` the assertion must INVERT, since the overlap is legal there by
  construction, which is a second mechanism and part of why it is not a one-liner.
- **The 2026-08-17 archive PAIR still does not partition the family. RESOLVED as out of scope,
  agent-delegated, 2026-09-12 (`TOOL-cSpliceWarden-7`).** Seventeen of the twenty-four surviving rows
  are byte-identical rows of `TOOL.2026-08-17b.md`. The brief scoped the first file only, so the
  corrected header deliberately does not claim exclusivity rather than claiming something false.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-cSpliceWarden-1` | 2 | `ROTATION_MODE` declared and validated against a closed set, and one rotation semantics written into the HYGIENE pair and the charter |
| 2 | `TOOL-cSpliceWarden-2` | 2 | hygiene check 10 reaches a backlog archive — four defects, not the two filed, and the fourth only a real-tree run found |
| 3 | `TOOL-cSpliceWarden-4` | 1 | the repair: supersession note, evacuation, fifteen rows re-homed with bodies recovered from their closing commits |
| 4 | `TOOL-cSpliceWarden-3` | 2 | hygiene check 20 scans a rotated backlog shard, on the enumeration contract unit 2 specifies |
| 5 | `TOOL-cSpliceWarden-5` | 1 | two rows filing one gap consolidated, a retirement resting on a false premise superseded, and what this build leaves undone filed |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node c · opened 2026-09-12 · streams tooling+playbook
ids TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5 TOOL-cSpliceWarden-6 TOOL-cSpliceWarden-7 TOOL-cSpliceWarden-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cSpliceWarden-1 — rotation becomes a DECLARED mode, and one semantics replaces two](spec/2026-09-12-spec-TOOL-cSpliceWarden-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cSpliceWarden-2 — hygiene check 10 reaches a backlog archive, and stops reporting a reassuring zero](spec/2026-09-12-spec-TOOL-cSpliceWarden-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cSpliceWarden-4 — the archive repair: superseded, evacuated, and fifteen rows re-homed](spec/2026-09-12-spec-TOOL-cSpliceWarden-4.md) | 3 | 1 | CLOSED | rev-3 | 2026-09-13 |
| [TOOL-cSpliceWarden-3 — hygiene check 20 scans a rotated backlog shard](spec/2026-09-12-spec-TOOL-cSpliceWarden-3.md) | 4 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cSpliceWarden-5 — two rows filing one gap become one, and a false retirement is superseded](spec/2026-09-12-spec-TOOL-cSpliceWarden-5.md) | 5 | 1 | CLOSED | rev-2 | 2026-09-13 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-cSpliceWarden-1` | no |
| 2 | `TOOL-cSpliceWarden-2` | no |
| 3 | `TOOL-cSpliceWarden-4` | no |
| 4 | `TOOL-cSpliceWarden-3` | no |
| 5 | `TOOL-cSpliceWarden-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
