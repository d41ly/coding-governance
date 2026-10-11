# TOOL-aPairedSlots-5 — a worktree holds at most one slot, so every path under its git dir stays one bar's

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base b6cd02bc · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aPairedSlots-1.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md) | research | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-6 |

<!-- /gen:spec-records -->

## 1. Goal

Two bars admitted at once must never be two bars in ONE worktree, because every file a bar keeps
under its worktree's git dir assumes one writer. So the claim refuses a slot to a run whose worktree
already holds one, and the paths the shared-path audit found under the git dir stay per-bar by
construction. This unit also carries the audit itself and the check that two real bars on two
worktrees of one repository give the verdicts they give run serially, with no record lost.

## 2. Scope (IN)

- **S1 — the claim refuses a second slot to one worktree.** At `TS_SLOTS` above 1, the head of
  the queue does not claim while any live slot's `repo` file equals this run's `$ROOT`. It waits
  exactly as it waits for a full host, and its queue line names the same-worktree holder. At one
  slot the predicate is unreachable, since the head claims only an empty slot 1, so the base
  behaviour is unchanged. Observed by AC1.
- **S2 — the audit, recorded.** The predicates run over the real tree, their hits and near-misses,
  and each path's disposition are written to
  `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md`.
  It classes every path two concurrent bars on one repository both write as per-worktree (made
  per-bar by S1), common and safe as measured, or common and changed by TOOL-aPairedSlots-7 or
  TOOL-aPairedSlots-8. Observed by AC2.
- **S3 — two real bars, concurrent against serial.** An instrument under this build's `build/`
  freezes one clone of the build tip with two worktrees, runs a `GATE_FULL=1` bar in each one after
  the other and then both at once under `GATE_TURNSTILE_SLOTS=2`, and compares them. Observed by
  AC3.

## 3. Non-goals (OUT)

- Changing any common-dir writer; that is TOOL-aPairedSlots-7, and the one fixed-name leg fixture
  is TOOL-aPairedSlots-8.
- Two bars in one worktree at once. S1 forbids it rather than making every git-dir file
  multi-writer.
- A nested run, which takes no slot and writes beside its parent by design.

### Edges

- **consumes-from** `TOOL-aPairedSlots-2` — the slot paths and their `repo` files.
- **hands-off** `TOOL-aPairedSlots-7` — the common-dir writes the audit found unsafe.
- **hands-off** `TOOL-aPairedSlots-8` — the leg fixture the audit found writing a fixed name in the
  real common dir.

## 4. Design

The audit split the population in two. Everything the runner keeps under `$GD`, the WORKTREE's git
dir — the ledger, the run records and `current`, the summary and failure files, the gate logs, the
full and inherited greens and the queue status and heartbeat files — is written by one bar at a
time today because the turnstile admitted one bar. Two worktrees have two git dirs, so admitting two
bars keeps that true for them, and the only way to break it is two bars in one worktree. S1 removes
that way in the claim rather than auditing a dozen read-merge-write sites for a second writer.

What remains shared is the common dir and the host's temp root: the health log, the run log, the
drift history, the shared full green, the scratch sweep, and the leg fixtures. Those are
TOOL-aPairedSlots-7's and TOOL-aPairedSlots-8's, or recorded safe with the measurement that says so.

### Inventory

No function or variable is minted beyond a local in the claim. New record:
`2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md`, and the two-bar instrument and its
rows beside it.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `memory/builds/aPairedSlots/build/`

### Alternatives rejected

- **Making every git-dir file safe for two writers.** The ledger merge, the run-record pruning and
  `current` are read-merge-write sites; locking each is a dozen new mechanisms for a case nobody
  asked for.
- **Keying the exclusion on the git dir rather than the top level.** `$ROOT` is already in the beacon
  as `repo`, and a worktree has exactly one of each.

## 5. Production-readiness checklist

- security — N/A — a predicate over files the turnstile already writes.
- perf / scale — a same-worktree second bar waits instead of running; two worktrees still overlap.
- error / empty / loading states — a slot with no readable `repo` file does not block, since an
  older runner's beacon may lack one; that run cannot be told apart from another worktree's.
- observability — the queue line names the same-worktree holder.
- risks — head-of-line: a same-worktree head keeps other worktrees' waiters behind it until its
  sibling finishes. Stated in the README.
- testing — AC1 in the turnstile suite; AC3 on real bars.
- migration — none.
- user docs — the README's turnstile section.

## 6. Acceptance criteria

- **AC1** — When two fixture bars start in ONE worktree under `GATE_TURNSTILE_SLOTS=2`, the peak is
  1 and the second's queue line names the first; when they start in two worktrees of one fixture
  repository, the peak is 2.
  Red when: the claim ignores `repo`, and the one-worktree peak is 2.
- **AC2** — When `2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md` is read, every path the
  prompt names has a row with a disposition and the measurement or code line behind it, and every
  COLLIDES row names the unit that fixes it.
  Red when: a named path has no row.
- **AC3** — When the two-bar instrument runs, the concurrent pair and the serial pair give the same
  set of leg verdicts for each worktree, each worktree's `gate-ledger.tsv` carries a row per leg per
  bar, the common dir's `gates.log` carries four new whole lines, and all four run records carry a
  verdict file.
  Red when: a row, a line or a record is missing or torn, or a leg's verdict differs.
  cost: two full bars serial and two concurrent, about three hours, run once at VERIFYING.

## 7. Gates

`run-gates turnstile` · `memory hygiene`

New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC1 · a runner copy whose claim ignores the slot's repo file · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

The seam is TOOL-aPairedSlots-2's claim in `tools/run-gates/run-gates.sh` and the `repo` file
TOOL-aFrugalTurnstile-5 already writes into every beacon. `reuse_lookup.py` named no
per-worktree admission seam. Recall returned TOOL-aUnblockedFleet-8, two closes in one clone
contending on the turnstile, which this unit keeps serialized inside one worktree.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
