# Acceptance ledger — the closing review's mediums and lows, batched

**Serves:** journal TOOL-aPairedSlots-15

Observed on node a on 2026-10-12. The turnstile suite's arms 32 and 44 to 48 were sliced and run three
ways: over the runner as it stood before this unit, over the changed runner with only its nesting
test narrowed to the runner's own slot paths, and, whole, over the changed runner. The slot cap was
observed by `--print-profile` over fixture tables, the call its canary checks make, on both runners.

**Evidences:** TOOL-aPairedSlots-15
- AC1 — `ts_try_reap` — with the nonce swapped as each pid was read, the changed runner left the slot
  and the docs beacon standing with the successor's nonce; the previous runner removed both.
- AC2 — `check_worktree_unheld` — a one-slot bar from the worktree holding slot 2 waited, peak 1 over
  two registrations, and its queue line read `this worktree's bar holds slot 2` with that holder's
  pid; on the previous runner it claimed slot 1 beside it, peak 2, and printed no such line.
- AC3 — `gate queue: docs-only — this worktree's bar holds` — a doc-only bar in a worktree whose slot
  was held waited, peak 1, and named the holder; a non-doc bar in a worktree with a live docs beacon
  waited, peak 1, its line naming `the docs key`. On the previous runner both ran beside the holder,
  peak 2.
- AC4 — `slots=65` — the changed runner refused the row with exit 2 naming the ceiling of 64, and with
  `GATE_TURNSTILE_SLOTS=65` printed one NOTE and kept the row's 3; the previous runner accepted 65
  both ways.
- AC5 — `sweeping the docs beacon of an unfinished holder` — a planted beacon with only a nonce, its
  directory 100 s old under a 5 s ttl, was swept by the next doc-only bar; the previous runner left
  it standing.
- AC6 — `gate queue: nested under` — arm 32's one-slot inner runner nested under the slot-2 holder on
  the changed runner and did not on the copy whose nesting reads only its own slot paths. The stalled
  docs holder arm saw `sweeping the docs beacon of a stalled holder` and the beacon gone.
- AC7 — `FLOOR_ASSERTIONS` — the turnstile suite ran whole over the changed runner in 3598 s and printed
  `PASS (144 assertions)`, its raised floor: 142 ok and 2 announced SKIPs of a slow-host control. The
  canary's floor of 339 is its old 326, section 11s's nine checks and its four new ones, counted off
  the arm; the canary runs whole at the close's bar.
- AC8 — `2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md` — its health log row names ask
  TOOL-aPairedSlots-10, the roster row for unit 7 names no health log trim, spec 7's checklist is at
  rev-4 without the health lock, and seven classes are new in `memory/gotchas/`, each gated or saying
  it has no machine gate, by `gotchas.py --check`.
