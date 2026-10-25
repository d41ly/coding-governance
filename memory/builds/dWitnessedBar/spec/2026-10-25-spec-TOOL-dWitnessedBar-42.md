# TOOL-dWitnessedBar-42 — the tail sweep keeps every tail any worktree's retained run names, and never a fresh one

**Status:** DEFERRED · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 19 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-42-deviation-421.md](../build/2026-10-25-build-TOOL-dWitnessedBar-42-deviation-421.md) | deviation | — |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 60 at HIGH**, its item **H3**, alone in that item. `TOOL-dWitnessedBar-25` writes
tails to the shared `<common-dir>/gate-tails/` so they outlive their worktree, and its S4 makes the run
sweep keep "exactly the tails some retained run record names". The sweep it extends walks only the
running worktree's `RUNROOT` (`tools/run-gates/run-gates.sh:5692-5695`). A bar finishing in worktree A
would delete tails only worktree B's retained runs name, or a tail B wrote a moment ago for a run whose
verdict is not yet written, and B's `keep_tails.py --run <id>` would find the file gone. Unattended runs
sit in parallel worktrees by design. This unit takes the report's fix. It repairs
`TOOL-dWitnessedBar-25`.

## 2. Scope (IN)

- **S1** — The retained set is every worktree's. The tail sweep reads the `tail.<n>` keys of the
  `verdict` file of every run dir under `<common-dir>/gate-run/` and under each
  `<common-dir>/worktrees/<id>/gate-run/`, the git dir of every worktree of the clone, linked ones
  included. Observed by AC1.
- **S2** — A fresh tail is never swept. A tail file whose modification time is younger than
  `TAIL_GRACE_S`, 604800 seconds (seven days), is kept whether or not a verdict names it, so a tail
  written by a bar still running in another worktree survives. Observed by AC2.
- **S3** — Tails are written atomically. The runner writes each tail to a temp path from
  `derive_temp_path` beside it and renames it into place, so no reader meets a partial file and the
  sweep never sees one. Observed by AC3.
- **S4** — Unit 25's sweep arm ages its tail. The evidence-suite case for `TOOL-dWitnessedBar-25` AC5
  sets its tail's modification time past `TAIL_GRACE_S` before the sweep, so the case still observes
  removal of an unnamed tail. Observed by AC1.

## 3. Non-goals (OUT)

- The tail itself, its cut, its hash and the keep verb: `TOOL-dWitnessedBar-25`'s. Its fence and byte
  cut are the minors batch's id 61 (`TOOL-dWitnessedBar-51`).
- Retention of the per-tree verdict files: the minors batch's id 48 (`TOOL-dWitnessedBar-51`), which
  applies the same every-worktree reading to `gate-verdict/`.
- Sweeping run dirs across worktrees: each worktree still sweeps its own `RUNROOT` only.
- A bug-class checklist entry for common-dir sweeps, the report's left-shift: no clause of this build
  names it, and AC1 is the two-worktree fixture.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-25` — the tails directory `<common-dir>/gate-tails/`, the `tail.<n>` verdict keys and the sweep this unit widens; without them there is nothing to sweep
- **hands-off** `TOOL-dWitnessedBar-51` — the every-worktree reading of S1, which the minors batch's id 48 item applies to the per-tree verdict directory
- **hands-off** `TOOL-dWitnessedBar-56` — the tail sweep and `TAIL_GRACE_S`, which the verdict-boundary minors batch extends to both temp spellings and annotates with the rejected seam (ids 23, 52)

## 4. Design

### Evidence

- The sweep: `ls -1t "$RUNROOT" | grep -v '^current$' | tail -n "+$((GATE_RUN_KEEP+1))"` removes the
  worktree's own older run dirs (`run-gates.sh:5692-5695`); `RUNROOT="$gd/gate-run"` (`:2601`).
- A linked worktree's git dir is `<common-dir>/worktrees/<id>`, the main worktree's is the common dir
  itself, which is git's own layout; the runner already resolves the common dir once
  (`RG_COMMON_RAW`, `run-gates.sh:113-117`).
- `derive_temp_path` (`run-gates.sh:782`) is the runner's existing temp-name helper.

### The sweep

```
named  = tail.<n> hashes in  <common>/gate-run/*/verdict  and  <common>/worktrees/*/gate-run/*/verdict
for each file t in <common>/gate-tails/ (no .tmp suffix):
    keep  if t in named
    keep  if now - mtime(t) < TAIL_GRACE_S
    else  remove t
```

Reading `<common>/worktrees/*/` rather than `git worktree list` costs no fork and keeps the run dirs of
a worktree whose directory was removed but not yet pruned, which errs toward keeping. A temp file older
than the grace is removed with the rest.

### Inventory

Minted: the constant `TAIL_GRACE_S`. Naming cells: asked of `python tools/lexicon/lexicon.py --suggest
TAIL_GRACE_S` at the pass.

### Migration

None: tails exist only from `TOOL-dWitnessedBar-25`'s pass, one step earlier.

### Rollout

Live at landing.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`

### Alternatives rejected

- **A reference file per tail naming its run ids.** A second record per tail, and a writer race of its
  own when two runs name one hash.
- **The oldest running bar's start as the grace.** It reads the turnstile beacons, and a docs-mode bar
  or a runner older than the beacon holds none (`run-gates.sh:1495-1517`), so the bound could be missed.

## 5. Production-readiness checklist

- security — the sweep removes only files under `<common-dir>/gate-tails/`; nothing outside it is read
  for removal.
- perf / scale — one directory listing per worktree's `gate-run/`; tails are at most 8192 bytes, so a
  week of red bars costs megabytes at most.
- error / empty / loading states — an unreadable `verdict` file names nothing and its tails fall to the
  grace; an absent `worktrees/` directory is no linked worktree.
- observability — the sweep prints the count it removed and kept.
- risks — a tail lives at least seven days after its last naming run is swept, which is the cost of
  never racing a running bar.
- testing — AC1 to AC3 by fixture; the arm of §7 at the close.
- migration — none.
- user docs — `tools/run-gates/README.md`'s tails paragraph names the grace at the pass; no page under
  `help/` covers it.

## 6. Acceptance criteria

- **AC1** — When a scratch clone with a linked worktree B holds a tail named only by B's retained run,
  aged past the grace, and worktree A completes more runs than `GATE_RUN_KEEP`, the tail survives; a tail
  aged past the grace and named by no run of either worktree is removed.
  Red when: the sweep reads only the running worktree's `RUNROOT`, so B's tail is removed.
  fixture: a scratch clone and `git worktree add` under `%TEMP%/<short-name>`; the tree holds none.
- **AC2** — When the same sweep meets a tail named by no run whose modification time is one minute old,
  the tail survives, and `grep -c 'TAIL_GRACE_S' run-gates.sh` in `tools/run-gates/` prints at least 2.
  Red when: a fresh tail of a bar still running in another worktree is removed.
- **AC3** — When the runner writes a tail, the file appears under its hash with no `.tmp` sibling
  left, and `grep -n 'gate-tails' tools/run-gates/run-gates.sh` shows the write beside a
  `derive_temp_path` call.
  Red when: the tail is written in place, so a reader can meet a partial file.

## 7. Gates

`measure-legs selftest` · `run-gates evidence` · `run-gates canary` · `memory hygiene`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 · two worktrees of a scratch clone, one tail named by the other's run and one fresh unnamed tail, staged red by restricting the sweep to `RUNROOT` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-25`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How long is a tail kept when nothing names it?** Options: (a) seven days, a fixed constant far
  past any bar's wall; (b) the runner's `WALL` times two; (c) the oldest running bar's beacon. (b) is
  zero when no wall is profiled (`run-gates.sh:1054`); (c) misses bars that hold no beacon. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the bound that needs no other reading to be true.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 60 (HIGH, item H3).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seam extended is the runner's own sweep (`tools/run-gates/run-gates.sh:5688-5696`) and its
common-dir resolution (`RG_COMMON_RAW`). `python tools/codebase-map/reuse_lookup.py "sweep a common-dir
cache across every worktree's retained runs"` ranked `run`, `resolve_kit_dir`, `kit_dir`, `run_arms`,
`run_git` and `extract_run_facts`, none a sweep; no existing seam reads every worktree's run dirs, so the
reading is added to the one sweep there is.

Recall terms used: `python tools/memory-recall/query.py "how are common-dir records swept across worktrees" --terms "gate-tails sweep GATE_RUN_KEEP common-dir worktree gate-run retained run record tail hash"`
