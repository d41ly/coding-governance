# TOOL-dWellOiledMachine-89 — the supervisor start claim made on a fresh node, and only a claim that exists read as a rival

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 30 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-89-deviation-891.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-89-deviation-891.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 63, item H9, at HIGH. TOOL-dWellOiledMachine-78 S3 claims
`<git-common-dir>/gov/supervisors/<slug>.starting` with one `mkdir` and reads any failure as
`starting elsewhere`. Nothing creates `gov/supervisors/`, which only the supervisor itself writes
(TOOL-dWellOiledMachine-6 S1, its `.pid`), so on a fresh node every tick's `mkdir` fails with "no such
file or directory", prints `starting elsewhere`, and no supervisor ever starts; a permission error is
misread as a live rival the same way. This unit makes the parent before the claim and reads a failed
claim as a rival only when the claim is actually there.

## 2. Scope (IN)

- **S1** — The parent made first. Before it takes the claim, the tick runs
  `mkdir -p <git-common-dir>/gov/supervisors`. A failure prints
  `supervisor — <slug> · not started · cannot make <dir>: <mkdir's stderr>` and starts nothing.
  Observed by AC1, AC3.
- **S2** — A lost claim is one that exists. When the claim's take fails, whatever takes it (78 S3's
  `mkdir`, or TOOL-dWellOiledMachine-83's `write_node_lock`), the tick tests `[ -d <claim> ]`: present
  prints `supervisor — <slug> · starting elsewhere`, as today; absent prints
  `supervisor — <slug> · not started · claim <claim> not created` and starts nothing, so a failure that
  is not a rival is never reported as one. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- No change to how the claim is taken or broken: 78 S3 and TOOL-dWellOiledMachine-83.
- No change to which claims are stale: 78 S4 and TOOL-dWellOiledMachine-80.
- No retry within a tick: the next tick tries again, as for every other refusal of the start.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-78` — the start claim of S3, whose parent this unit makes and whose failure this unit classifies
- **hands-off** `TOOL-dWellOiledMachine-94` — S2's absent-claim branch, its plant and §4's citation (findings 5, 21, 37)

## 4. Design

### Evidence

- 78 S3 claims with "one `mkdir`" and reads a lost `mkdir` as "starting elsewhere"
  (`spec-78.md:34-37`).
- 6 S1 has the supervisor write `<git-common-dir>/gov/supervisors/<slug>.pid` (`spec-6.md:36-38`),
  the only writer under that directory, so the directory exists only after a first supervisor ran.
- `grep -n "gov/supervisors" tools/unattended/resume-tick.sh` prints nothing at this base: nothing
  there makes the directory.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `fresh-node`, `claim-unwritable` | `supervise.py --fixture` plants | none |

### Files touched (estimate)

- `tools/unattended/resume-tick.sh` (or `tools/runtime/resume-tick.sh` once TOOL-dWellOiledMachine-28
  moves it): S1, S2
- `tools/runtime/supervise.py`: the two plants

### Alternatives rejected

- **`mkdir -p` the claim itself.** `mkdir -p` succeeds on an existing directory, so the claim would
  stop being exclusive.
- **Parsing `mkdir`'s message for "File exists".** The message is locale- and platform-dependent;
  the presence test asks the file system the question directly.

## 5. Production-readiness checklist

- security — none beyond exactly one act session per item.
- perf / scale — one `mkdir -p` per tick that may start a supervisor, a no-op once the directory
  exists.
- error / empty / loading states — the fresh node is the empty state, and S1 handles it; S2 names a
  failure that is not a rival.
- observability — each refusal prints its cause on the tick's output.
- risks — none beyond the next tick retrying a start S2 refused.
- testing — AC1 to AC3 and the arm in §7.
- migration — none.
- user docs — none: no verb, key or message a user types changes.

## 6. Acceptance criteria

- **AC1** — When `python supervise.py --fixture --plant fresh-node` runs a tick in a scratch clone
  whose git common dir holds no `gov/` directory, the tick creates `gov/supervisors/` and starts
  exactly one supervisor.
  Red when: the tick prints `starting elsewhere` and starts nothing.
- **AC2** — When `--plant claim-unwritable` replaces `gov/supervisors/` with a regular file of that
  name, the tick prints `not started` naming the path and never `starting elsewhere`.
  Red when: a failure with no claim present is reported as a rival.
- **AC3** — When `--plant double-tick` runs twenty times over a fresh node, every run ends with
  exactly one supervisor, and the losing tick prints `starting elsewhere`.
  Red when: making the parent lets both ticks start.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/supervise.py · covers AC1 AC2 AC3 · the plants staged against 78 S3's bare `mkdir` with no parent made and every failure read as a rival · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  63 (H9).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

No existing seam fits beyond the claim itself: the probe `python tools/codebase-map/reuse_lookup.py
"create the parent directory before an atomic claim"` ranked `before`, `claims`, `write_claim` and
`check_claim_push_lock_stale` by name stem, and the last two are the claim writer and lock this
build's other units reuse, neither of which makes a parent. The fix is two shell tests in the tick.
The plants use a file in place of a directory, the write-failure plant that fails on Windows.

Recall terms used: `python tools/memory-recall/query.py "what happens to a claim directory left empty
by a dead tick" --terms "supervisor claim starting directory dead tick incomplete pid stamp mtime age
reap"`
