# TOOL-dWellOiledMachine-80 — a supervisor start claim left incomplete by a dead tick is judged by its age, so it never blocks every later start

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 30 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-80-deviation-801.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-80-deviation-801.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 1, item H1, at HIGH. TOOL-dWellOiledMachine-78 S3 makes the start claim
`<git-common-dir>/gov/supervisors/<slug>.starting` with one `mkdir` and only then writes the tick's pid
and UTC stamp inside it, and 78 S4 reaps a claim only when that pid reads `no` and that stamp is older
than two beats. A tick that dies between the two steps leaves a claim carrying neither, which neither
test can judge, so every later tick prints `starting elsewhere` and the build has no supervisor until
someone intervenes. This unit gives the claim's stale test an arm for an incomplete claim, judged by
the directory's own age, so a torn claim is reaped once it is older than two beats.

## 2. Scope (IN)

- **S1** — The incomplete-claim arm. 78 S4's stale test, the shell function
  `check_supervisor_claim_stale <claim dir>` in the tick (a builder finding 78's test inline names it
  so), reads the claim stale when its recorded pid or its stamp is missing, empty or unparseable and
  the claim directory's modification time is older than `2 * SUPERVISOR_BEAT_SECONDS`, measured by
  `find <dir> -maxdepth 0 -mmin +<minutes>` as `check_claim_push_lock_stale`
  (`tools/unattended/unattended.sh:2325-2330`) measures its no-deadline arm. A complete claim keeps
  78 S4's reading unchanged. Observed by AC1, AC2.
- **S2** — The young incomplete claim is kept. An incomplete claim younger than two beats is not
  stale: the tick prints `supervisor — <slug> · starting elsewhere` and starts nothing, since its
  writer may still be between its `mkdir` and its writes. Observed by AC3.
- **S3** — The reap prints its cause. Reaping an incomplete claim prints
  `supervisor — <slug> · claim reaped · incomplete, <age>s old`, so the torn write is visible in the
  tick's output. Observed by AC1.

## 3. Non-goals (OUT)

- No change to how a stale claim is removed: the break procedure is TOOL-dWellOiledMachine-83's.
- No change to how the claim is created or its parent made: TOOL-dWellOiledMachine-89's.
- No change to the complete-claim arm (a dead tick's pid and an old stamp): 78 S4 stands.
- Which pid the claim records under MSYS is finding 23 and 64's, carried by the minors batch
  TOOL-dWellOiledMachine-90.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-78` — the start claim of S3 and the stale test of S4, whose incomplete-claim case this unit decides
- **hands-off** `TOOL-dWellOiledMachine-90` — `check_supervisor_claim_stale`, whose `unknown` reading the batch adds (finding 64)
- **hands-off** `TOOL-dWellOiledMachine-94` — S1's and AC2's claim layout, S3's reap line, §4's citations and the symbol render (findings 4, 21, 29, 30)

## 4. Design

### Evidence

- 78 S3 creates the claim, then writes the pid and stamp into it (`spec-78.md:34-40`); 78 S4's stale
  test needs both (`spec-78.md:42-45`); AC4 plants only a complete dead claim (`spec-78.md:112-114`).
- The tree's other `mkdir` lock already judges a lock with no deadline by its directory age:
  `check_claim_push_lock_stale` reads `until` and, with none, `find "$1" -maxdepth 0 -mmin +2`
  (`tools/unattended/unattended.sh:2325-2330`).
- `SUPERVISOR_BEAT_SECONDS` is PINNED at 60 (`spec-6.md:198`), so two beats is two minutes.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_supervisor_claim_stale` | shell function, the tick | `check`, OK |
| `empty-claim`, `torn-claim`, `young-empty-claim` | `supervise.py --fixture` plants | none |

### Files touched (estimate)

- `tools/unattended/resume-tick.sh` (or `tools/runtime/resume-tick.sh` once TOOL-dWellOiledMachine-28
  moves it): S1 to S3
- `tools/runtime/supervise.py`: the three plants

### Alternatives rejected

- **Publishing the claim complete by renaming a filled temporary directory into place.** A `rename`
  onto an existing empty directory replaces it on POSIX, so a stray empty claim would be overwritten
  rather than refused; the age arm needs no new create path.

## 5. Production-readiness checklist

- security — none beyond exactly one act session per item, which the claim protects.
- perf / scale — one `find` on an incomplete claim, none on a complete one.
- error / empty / loading states — an incomplete claim is the empty state, and S1 and S2 decide it.
- observability — S3's reap line names the age.
- risks — a tick stalled for two beats between its `mkdir` and its writes loses its claim; the
  supervisor it then starts is guarded by the pid file re-read 78 S3 makes under the claim.
- testing — AC1 to AC3 and the arm in §7.
- migration — none.
- user docs — none: no verb, key or message a user types changes.

## 6. Acceptance criteria

- **AC1** — When `python supervise.py --fixture --plant empty-claim` leaves an empty `.starting`
  directory whose modification time is three minutes old, the next tick prints `claim reaped ·
  incomplete` and starts exactly one supervisor.
  Red when: the empty claim blocks the start and the tick prints `starting elsewhere`.
- **AC2** — When `--plant torn-claim` leaves a claim whose pid file is present and whose stamp file
  reads `garbage`, three minutes old, the next tick reaps it and starts one supervisor.
  Red when: an unparseable stamp is read as a live claim.
- **AC3** — When `--plant young-empty-claim` leaves an empty `.starting` directory ten seconds old,
  the tick prints `starting elsewhere` and starts nothing.
  Red when: a claim younger than two beats is reaped.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/supervise.py · covers AC1 AC2 AC3 · the three plants staged against 78 S4's test with no incomplete-claim arm · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding 1
  (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam reused is the age arm of the tree's other `mkdir` lock, `check_claim_push_lock_stale`
(`tools/unattended/unattended.sh:2325-2330`), whose `find -maxdepth 0 -mmin` reading this arm takes.
The probe `python tools/codebase-map/reuse_lookup.py "reap a lock directory left incomplete by a dead
writer"` ranked `write`, `write_text`, `write_record` and `writeSidecarLine` by name stem, none a lock
reaper; the recall query below ranked TOOL-dWellOiledMachine-78 first and TOOL-aGraftedHelix-37's
claim-push lock beside it, the one age-judged lock in the tree.

Recall terms used: `python tools/memory-recall/query.py "what happens to a claim directory left empty
by a dead tick" --terms "supervisor claim starting directory dead tick incomplete pid stamp mtime age
reap"`
